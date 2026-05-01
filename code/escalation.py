"""
escalation.py — Escalation decision engine.

Determines whether a ticket should be replied to or escalated to a human agent,
based on risk signals, corpus coverage, and domain-specific rules.

Design philosophy:
- When in doubt, escalate. A false positive (unnecessary escalation) is far
  safer than a false negative (giving wrong advice on a sensitive issue).
- Escalation decisions are traceable: always return a reason.
"""

from __future__ import annotations

from typing import List, Tuple

from classifier import detect_escalation_signals


# ─── Escalation rules ─────────────────────────────────────────────────────────

# These signal categories ALWAYS trigger escalation regardless of corpus coverage
HARD_ESCALATE_SIGNALS = {
    "fraud",
    "harm_threat",
    "legal_compliance",
    "account_security",  # account lockouts need identity verification
}

# These trigger escalation unless corpus has high-confidence answer
SOFT_ESCALATE_SIGNALS = {
    "billing_dispute",
    "assessment_integrity",
    "data_loss",
}

# Minimum retrieval score to consider corpus "covers" the question
CORPUS_COVERAGE_THRESHOLD = 0.15

# Domain-specific escalation rules (beyond signal matching)
DOMAIN_ESCALATION_RULES = {
    "visa": {
        # Any card-blocking, fraud, or financial transaction issues escalate
        "always_escalate_areas": ["fraud_disputes", "card_services"],
        "reason": "Financial and card-related issues require human verification for security.",
    },
    "hackerrank": {
        "always_escalate_areas": ["billing"],
        "reason": "Billing and subscription changes require human account review.",
    },
    "claude": {
        "always_escalate_areas": ["billing_plans", "privacy_data"],
        "reason": "Billing and data privacy requests require human review per policy.",
    },
}


# ─── Decision logic ───────────────────────────────────────────────────────────

class EscalationDecision:
    __slots__ = ("should_escalate", "reasons", "risk_level")

    def __init__(self, should_escalate: bool, reasons: List[str], risk_level: str):
        self.should_escalate = should_escalate
        self.reasons = reasons
        self.risk_level = risk_level  # low | medium | high | critical

    @property
    def status(self) -> str:
        return "escalated" if self.should_escalate else "replied"

    def summary(self) -> str:
        return "; ".join(self.reasons) if self.reasons else "Handled by agent."


def decide_escalation(
    issue: str,
    subject: str,
    domain: str,
    product_area: str,
    retrieval_top_score: float,
    is_invalid: bool,
    corpus_chunks_found: int,
) -> EscalationDecision:
    """
    Main escalation decision function.

    Returns an EscalationDecision with status, reasons, and risk level.
    """
    reasons: List[str] = []
    risk_level = "low"

    # ── 1. Invalid / injection tickets ──
    if is_invalid:
        return EscalationDecision(
            should_escalate=False,
            reasons=["Ticket is invalid, off-topic, or contains injection attempt."],
            risk_level="low",
        )

    # ── 2. Unknown domain with no corpus coverage ──
    if domain == "unknown" and corpus_chunks_found == 0:
        return EscalationDecision(
            should_escalate=True,
            reasons=["Domain could not be identified and no relevant documentation found."],
            risk_level="medium",
        )

    # ── 3. Hard-escalate signals ──
    signals = detect_escalation_signals(issue, subject)
    hard_hits = [s for s in signals if s in HARD_ESCALATE_SIGNALS]
    if hard_hits:
        reasons.append(f"High-risk signals detected: {', '.join(hard_hits)}.")
        risk_level = "critical" if "fraud" in hard_hits or "harm_threat" in hard_hits else "high"
        return EscalationDecision(
            should_escalate=True,
            reasons=reasons,
            risk_level=risk_level,
        )

    # ── 4. Soft-escalate signals with low corpus coverage ──
    soft_hits = [s for s in signals if s in SOFT_ESCALATE_SIGNALS]
    if soft_hits and retrieval_top_score < CORPUS_COVERAGE_THRESHOLD:
        reasons.append(
            f"Sensitive signals ({', '.join(soft_hits)}) with insufficient corpus coverage "
            f"(top score={retrieval_top_score:.3f})."
        )
        risk_level = "high"
        return EscalationDecision(
            should_escalate=True,
            reasons=reasons,
            risk_level=risk_level,
        )

    # ── 5. Domain-specific area rules ──
    area_suffix = product_area.split("/")[-1] if "/" in product_area else product_area
    domain_rules = DOMAIN_ESCALATION_RULES.get(domain, {})
    always_escalate = domain_rules.get("always_escalate_areas", [])
    if area_suffix in always_escalate:
        reasons.append(domain_rules.get("reason", "Domain policy requires escalation."))
        risk_level = "high"
        return EscalationDecision(
            should_escalate=True,
            reasons=reasons,
            risk_level=risk_level,
        )

    # ── 6. No corpus coverage at all ──
    if corpus_chunks_found == 0 or retrieval_top_score < 0.05:
        reasons.append(
            "No relevant documentation found in the support corpus. "
            "Cannot provide a grounded answer."
        )
        risk_level = "medium"
        return EscalationDecision(
            should_escalate=True,
            reasons=reasons,
            risk_level=risk_level,
        )

    # ── 7. Safe to reply ──
    return EscalationDecision(
        should_escalate=False,
        reasons=[],
        risk_level="low",
    )
