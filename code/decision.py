"""
decision.py — Decision Engine.

Determines whether a ticket should be:
  • replied   — high-confidence retrieval, no risk flags, supported request.
  • escalated — any of: high-risk content, unsupported action, low retrieval
                confidence, multi-intent complexity, or insufficient info.

All decisions are deterministic and explainable — every path produces
a justification string suitable for the output CSV.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from config import CONFIDENCE_THRESHOLD
from retriever import RetrievedDoc
from utils import log


# ─────────────────────────────────────────────────────────────────────────────
# Input / Output structures
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class TicketContext:
    """All pre-computed metadata about a single ticket."""
    raw_text:       str
    clean_text:     str
    request_type:   str
    product_area:   str
    is_high_risk:   bool
    risk_category:  Optional[str]
    intents:        list[str]          # detected product areas (multi-intent)
    retrieved_docs: list[RetrievedDoc]


@dataclass
class Decision:
    """Output of the decision engine for one ticket."""
    status:        str    # "replied" | "escalated"
    justification: str
    best_doc:      Optional[RetrievedDoc]    # None if escalated before retrieval


# ─────────────────────────────────────────────────────────────────────────────
# Decision Engine
# ─────────────────────────────────────────────────────────────────────────────

class DecisionEngine:
    """
    Rule-based decision engine with a clear priority order.

    Priority (highest → lowest):
      1. High-risk content        → always escalate
      2. Invalid request type     → always escalate
      3. Score / result manipulation → always escalate
      4. Low retrieval confidence → escalate
      5. No supporting docs       → escalate
      6. All checks pass          → reply
    """

    # Request types that we can attempt to reply to
    REPLIABLE_TYPES = {"product_issue", "bug", "feature_request"}

    # Escalation team mappings by risk category
    ESCALATION_TEAMS: dict[str, str] = {
        "fraud_security":   "the Security and Trust team",
        "payment_dispute":  "the Finance and Billing team",
        "score_manipulation": "the Policy and Compliance team",
        "account_permission": "the Account Management team",
        "vulnerability":    "the Security Engineering team",
        "data_privacy":     "the Privacy and Compliance team",
    }

    def evaluate(self, ctx: TicketContext) -> Decision:
        """
        Run the ticket through all decision rules in priority order.
        Returns the first matching Decision.
        """

        # ── Rule 1: High-risk content ──────────────────────────────────────
        if ctx.is_high_risk:
            team = self.ESCALATION_TEAMS.get(ctx.risk_category or "", "the specialist team")
            justification = (
                f"Ticket flagged as HIGH-RISK (category: {ctx.risk_category}). "
                f"Such requests involve sensitive matters (security, fraud, policy violations, "
                f"or data privacy) that exceed the scope of standard support. "
                f"Escalating to {team} for proper handling."
            )
            log.warn(f"ESCALATE — high-risk ({ctx.risk_category})")
            return Decision(
                status="escalated",
                justification=justification,
                best_doc=None,
            )

        # ── Rule 2: Invalid request type ──────────────────────────────────
        if ctx.request_type == "invalid":
            justification = (
                "Ticket classified as INVALID: the request violates platform policies "
                "(e.g., requesting score manipulation, unauthorised changes, or fraudulent actions). "
                "This cannot be fulfilled per HackerRank's Terms of Service. Escalating to "
                "the Policy and Compliance team."
            )
            log.warn("ESCALATE — invalid request type")
            return Decision(
                status="escalated",
                justification=justification,
                best_doc=None,
            )

        # ── Rule 3: No retrieved docs ─────────────────────────────────────
        if not ctx.retrieved_docs:
            justification = (
                "No relevant documentation was found in the local support corpus for this query. "
                "Responding without a grounded source would risk hallucination. "
                "Escalating to a human agent for accurate assistance."
            )
            log.warn("ESCALATE — no retrieved documents")
            return Decision(
                status="escalated",
                justification=justification,
                best_doc=None,
            )

        best_doc = ctx.retrieved_docs[0]

        # ── Rule 4: Low retrieval confidence ──────────────────────────────
        if not best_doc.is_confident:
            justification = (
                f"Retrieval confidence is too low (best score: {best_doc.score:.3f}, "
                f"threshold: {CONFIDENCE_THRESHOLD}). "
                f"The closest document found ({best_doc.chunk.source!r}) is not sufficiently "
                f"relevant to provide a reliable answer. Escalating to avoid misinformation."
            )
            log.warn(f"ESCALATE — low confidence ({best_doc.score:.3f} < {CONFIDENCE_THRESHOLD})")
            return Decision(
                status="escalated",
                justification=justification,
                best_doc=best_doc,
            )

        # ── Rule 5: Multi-intent with low cross-area confidence ───────────
        if len(ctx.intents) >= 3:
            # Three or more distinct product areas detected — likely complex
            justification = (
                f"Multi-intent ticket detected spanning {len(ctx.intents)} product areas "
                f"({', '.join(ctx.intents)}). Complex multi-topic tickets are better handled "
                f"by a specialised agent who can address all concerns accurately."
            )
            log.warn(f"ESCALATE — multi-intent ({ctx.intents})")
            return Decision(
                status="escalated",
                justification=justification,
                best_doc=best_doc,
            )

        # ── Rule 6: Feature request — acknowledge and log ─────────────────
        if ctx.request_type == "feature_request":
            justification = (
                f"Ticket classified as a FEATURE REQUEST. "
                f"Feature requests are directed to the product feedback portal for review. "
                f"Response grounded in document: {best_doc.chunk.source!r} "
                f"(relevance score: {best_doc.score:.3f})."
            )
            log.success(f"REPLY — feature request, doc={best_doc.chunk.source!r}")
            return Decision(
                status="replied",
                justification=justification,
                best_doc=best_doc,
            )

        # ── Rule 7: All checks passed — reply ─────────────────────────────
        justification = (
            f"Ticket classified as {ctx.request_type.upper()} in product area "
            f"{ctx.product_area.upper()}. "
            f"High-confidence answer grounded in {best_doc.chunk.source!r} "
            f"(relevance score: {best_doc.score:.3f}). "
            f"No risk flags detected. Responding with corpus-grounded information."
        )
        log.success(f"REPLY — {ctx.request_type}, doc={best_doc.chunk.source!r} ({best_doc.score:.3f})")
        return Decision(
            status="replied",
            justification=justification,
            best_doc=best_doc,
        )
