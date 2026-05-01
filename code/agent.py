"""
agent.py — Support Triage Agent orchestration layer.

This is the main brain: it coordinates retrieval, classification, escalation
logic, and LLM calls to produce the final output row for each support ticket.

Architecture:
  Ticket → [Domain Detection] → [Corpus Retrieval] → [Risk Assessment]
         → [Escalation Decision] → [Response Generation] → Output
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent))

from retriever import get_index, format_context, CorpusIndex
from classifier import (
    detect_domain,
    classify_request_type,
    classify_product_area,
    detect_escalation_signals,
    is_invalid_ticket,
)
from escalation import decide_escalation
from llm import (
    classify_ticket as llm_classify,
    generate_response,
    generate_escalation_response,
    generate_justification,
)

# ─── Output schema ────────────────────────────────────────────────────────────

OUTPUT_COLUMNS = ["status", "product_area", "response", "justification", "request_type"]


# ─── Agent ────────────────────────────────────────────────────────────────────

class TriageAgent:
    """
    Multi-domain support triage agent.

    Processing pipeline for each ticket:
    1. Sanitize & validate input
    2. Detect domain (rule-based, fallback to LLM)
    3. Retrieve top-k relevant corpus chunks
    4. Rule-based risk + escalation check
    5. LLM classification refinement (if API available)
    6. Generate grounded response or escalation message
    7. Build output row
    """

    def __init__(self, data_dir: Optional[Path] = None, verbose: bool = False):
        self.verbose = verbose
        print("[Agent] Loading corpus index...", end=" ", flush=True)
        self.index: CorpusIndex = get_index(data_dir) if data_dir else get_index()
        chunk_count = len(self.index.chunks)
        print(f"done ({chunk_count} chunks loaded).")
        if chunk_count == 0:
            print("[Agent] WARNING: No corpus chunks loaded. Check your data/ directory.")

    def _log(self, msg: str):
        if self.verbose:
            print(f"  [Agent] {msg}")

    def process_ticket(self, issue: str, subject: str, company: str) -> Dict[str, str]:
        """
        Process a single support ticket and return an output dict.
        """
        # ── Step 1: Sanitize ──────────────────────────────────────────────────
        issue = (issue or "").strip()
        subject = (subject or "").strip()
        company = (company or "").strip()

        self._log(f"Processing: {issue[:80]!r}")

        # ── Step 2: Validity check ────────────────────────────────────────────
        invalid = is_invalid_ticket(issue, subject)
        if invalid:
            return self._build_invalid_output(issue, subject)

        # ── Step 3: Domain detection ──────────────────────────────────────────
        domain = detect_domain(issue, subject, company)
        self._log(f"Domain: {domain}")

        # ── Step 4: Corpus retrieval ──────────────────────────────────────────
        # Build query from issue + subject + domain hints
        search_query = f"{subject} {issue}".strip()
        domain_filter = domain if domain != "unknown" else None

        # Multi-query retrieval: full query + key phrases
        key_phrases = self._extract_key_phrases(issue, domain)
        results = self.index.search_multi(
            queries=[search_query] + key_phrases,
            top_k=6,
            domain_filter=domain_filter,
        )

        top_score = results[0][1] if results else 0.0
        context = format_context(results, max_chars=3500)
        self._log(f"Retrieved {len(results)} chunks, top_score={top_score:.3f}")

        # ── Step 5: Rule-based classification ────────────────────────────────
        request_type = classify_request_type(issue, subject)
        product_area = classify_product_area(issue, subject, domain)
        escalation_signals = detect_escalation_signals(issue, subject)

        self._log(f"Request type: {request_type}, Product area: {product_area}")
        self._log(f"Escalation signals: {escalation_signals}")

        # ── Step 6: Rule-based escalation decision ────────────────────────────
        escalation = decide_escalation(
            issue=issue,
            subject=subject,
            domain=domain,
            product_area=product_area,
            retrieval_top_score=top_score,
            is_invalid=invalid,
            corpus_chunks_found=len(results),
        )

        self._log(f"Escalation: {escalation.status} | Risk: {escalation.risk_level}")

        # ── Step 7: LLM refinement (if API available) ─────────────────────────
        llm_result = None
        if not escalation.should_escalate or escalation.risk_level in ("low", "medium"):
            # Only call LLM for non-critical cases (to save API calls for high-risk)
            llm_result = llm_classify(issue, subject, company, context)
            if llm_result:
                self._log(f"LLM classification: {llm_result}")
                # Trust LLM for product_area and request_type refinement
                if llm_result.get("product_area"):
                    product_area = llm_result["product_area"]
                if llm_result.get("request_type") in ("product_issue", "feature_request", "bug", "invalid"):
                    request_type = llm_result["request_type"]
                # LLM can upgrade escalation but NOT downgrade hard-escalate decisions
                if llm_result.get("should_escalate") and not escalation.should_escalate:
                    escalation.should_escalate = True
                    escalation.reasons.append(llm_result.get("escalation_reason", "LLM flagged for escalation."))
                    escalation.risk_level = "high"

        # ── Step 8: Generate response ─────────────────────────────────────────
        if escalation.should_escalate:
            escalation_reason = escalation.summary()
            response = generate_escalation_response(issue, subject, escalation_reason)
            justification = self._build_justification(
                issue, "escalated", escalation_reason, domain, product_area
            )
        else:
            response = generate_response(issue, subject, company, context)
            justification = self._build_justification(
                issue, "replied", f"Corpus coverage score={top_score:.2f}", domain, product_area
            )

        # ── Step 9: Build output ──────────────────────────────────────────────
        return {
            "status": escalation.status,
            "product_area": product_area,
            "response": response,
            "justification": justification,
            "request_type": request_type,
        }

    def _extract_key_phrases(self, issue: str, domain: str) -> list[str]:
        """Extract focused sub-queries from the ticket text."""
        import re
        # Extract noun phrases and technical terms (simple heuristic)
        phrases = []
        # Sentences as sub-queries
        sentences = re.split(r"[.!?]\s+", issue)
        for s in sentences[:3]:
            s = s.strip()
            if len(s.split()) >= 3:
                phrases.append(s)
        return phrases[:3]

    def _build_justification(
        self,
        issue: str,
        status: str,
        reason: str,
        domain: str,
        product_area: str,
    ) -> str:
        """Generate justification via LLM or fallback to template."""
        llm_just = generate_justification(issue, status, reason, domain, product_area)
        if llm_just:
            return llm_just
        # Fallback template
        if status == "escalated":
            return f"Escalated to human agent: {reason}"
        return f"Replied using {domain} support corpus (area: {product_area})."

    def _build_invalid_output(self, issue: str, subject: str) -> Dict[str, str]:
        """Output for invalid / injection tickets."""
        return {
            "status": "replied",
            "product_area": "unknown/invalid",
            "response": (
                "We were unable to process this request as it appears to be invalid, "
                "incomplete, or outside the scope of our support system. "
                "Please submit a valid support ticket describing your issue."
            ),
            "justification": "Ticket classified as invalid: too short, nonsensical, or contains injection attempt.",
            "request_type": "invalid",
        }
