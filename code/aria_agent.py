"""
ARIA - Main Agent Orchestrator
Ties together corpus, classifier, and response generator into a full pipeline.
"""

import pandas as pd
import os
import sys
import time
from typing import Dict, Optional

from corpus_builder import CorpusBuilder
from classifier import TicketClassifier
from response_generator import ResponseGenerator


class ARIAAgent:
    """
    ARIA: Autonomous Routing & Intelligent Agent
    Multi-domain support triage for HackerRank, Claude, and Visa.
    """

    def __init__(self, groq_api_key: Optional[str] = None, verbose: bool = True):
        self.verbose = verbose
        self.corpus = CorpusBuilder()
        self.classifier = TicketClassifier()
        self.generator = ResponseGenerator(api_key=groq_api_key)

        if verbose:
            print("\n" + "═" * 60)
            print("  ARIA — Autonomous Routing & Intelligent Agent")
            print("  Multi-Domain Support Triage System v1.0")
            print("═" * 60)
            print("\n[INIT] Building support corpus...")

        self.corpus.build_corpus(verbose=verbose)

        if verbose:
            llm_status = "Groq LLM (llama-3.3-70b)" if self.generator.llm_available else "Rule-based fallback"
            print(f"[INIT] Response engine: {llm_status}")
            print("[INIT] ARIA is ready.\n")

    def process_ticket(self, issue: str, subject: str, company: str, ticket_num: int = 0) -> Dict:
        """Process a single support ticket through the full ARIA pipeline."""

        if self.verbose:
            print(f"[TICKET #{ticket_num}] Processing...")
            print(f"  Subject: {subject or '(none)'}")
            print(f"  Company: {company}")

        # ── Step 1: Full Classification ─────────────────────────────────────
        classification = self.classifier.full_classify(issue, subject, company)
        domain = classification["domain"]
        product_area = classification["product_area"]
        request_type = classification["request_type"]
        escalation_signals = classification["escalation_signals"]

        if self.verbose:
            print(f"  → Domain: {domain} | Area: {product_area} | Type: {request_type} | Urgency: {classification['urgency']}")
            if escalation_signals:
                print(f"  → Escalation signals: {list(escalation_signals.keys())}")

        # ── Step 2: Injection / Harmful Check ───────────────────────────────
        if classification["is_injected"]:
            if self.verbose:
                print(f"  ⚠ INJECTION DETECTED: {classification['inject_reason']}")
            result = self.generator.generate_escalation(
                issue, domain, product_area, "invalid",
                classification["inject_reason"], {"injection": True}
            )
            result["status"] = "escalated"
            return result

        if classification["is_harmful"]:
            if self.verbose:
                print(f"  ⚠ HARMFUL REQUEST DETECTED")
            result = self.generator.generate_escalation(
                issue, domain, product_area, "invalid",
                classification["harm_reason"], {"harmful": True}
            )
            result["status"] = "escalated"
            return result

        # ── Step 3: Out-of-Scope Check ───────────────────────────────────────
        if classification["is_oos"]:
            if self.verbose:
                print(f"  → Out of scope: {classification['oos_reason']}")
            return self.generator.generate_oos_response(
                issue, product_area, classification["oos_reason"]
            )

        # ── Step 4: Corpus Retrieval ─────────────────────────────────────────
        query = f"{issue} {subject or ''} {domain}"
        retrieved = self.corpus.retrieve(query, domain=domain, top_k=5)
        confidence = self.corpus.get_confidence(retrieved)

        if self.verbose:
            print(f"  → Retrieval confidence: {confidence:.3f} | Top chunks: {len(retrieved)}")

        # ── Step 5: Escalation Decision ──────────────────────────────────────
        should_escalate, escalation_reason = self.classifier.should_escalate(
            issue, escalation_signals,
            classification["is_injected"],
            classification["is_harmful"],
            confidence,
            domain
        )

        if should_escalate:
            if self.verbose:
                print(f"  → ESCALATING: {escalation_reason}")
            return self.generator.generate_escalation(
                issue, domain, product_area, request_type,
                escalation_reason, escalation_signals
            )

        # ── Step 6: Generate LLM Response ────────────────────────────────────
        if self.verbose:
            print(f"  → Generating response (LLM: {self.generator.llm_available})...")

        result = self.generator.generate(
            issue, subject, domain, product_area, request_type, retrieved
        )

        if self.verbose:
            print(f"  ✓ Status: {result.get('status')} | Area: {result.get('product_area')}")

        return result

    def process_csv(self, input_path: str, output_path: str):
        """Process all tickets from a CSV file and write results."""
        df = pd.read_csv(input_path)

        # Normalize column names
        df.columns = [c.strip().lower() for c in df.columns]

        # Ensure required columns exist
        for col in ["issue", "subject", "company"]:
            if col not in df.columns:
                df[col] = ""

        df = df.fillna("")

        results = []
        total = len(df)

        if self.verbose:
            print(f"\n[PROCESSING] {total} tickets from '{input_path}'\n")
            print("─" * 60)

        for i, row in df.iterrows():
            ticket_num = i + 1
            result = self.process_ticket(
                issue=str(row.get("issue", "")),
                subject=str(row.get("subject", "")),
                company=str(row.get("company", "")),
                ticket_num=ticket_num
            )
            results.append({
                "issue": row.get("issue", ""),
                "subject": row.get("subject", ""),
                "company": row.get("company", ""),
                "response": result.get("response", ""),
                "product_area": result.get("product_area", ""),
                "status": result.get("status", ""),
                "request_type": result.get("request_type", ""),
                "justification": result.get("justification", ""),
            })

            if self.verbose:
                print("─" * 60)

            # Small delay to respect rate limits
            if self.generator.llm_available:
                time.sleep(0.3)

        out_df = pd.DataFrame(results)
        out_df.to_csv(output_path, index=False)

        if self.verbose:
            print(f"\n[DONE] Results saved to '{output_path}'")
            replied = sum(1 for r in results if r["status"] == "replied")
            escalated = sum(1 for r in results if r["status"] == "escalated")
            print(f"  Replied: {replied} | Escalated: {escalated} | Total: {total}")

        return results
