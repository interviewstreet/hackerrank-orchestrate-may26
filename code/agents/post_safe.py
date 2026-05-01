"""
Safety Pass 2 — Post-retrieval
Catches: fraud, legal threats, account access, financial disputes.
Runs AFTER retrieval so domain is confirmed.
"""

from config import SENSITIVE_KEYWORDS, ESCALATION_RESPONSE
from utils.logger import log_agent


def run(query: str, domain: str) -> dict | None:
    """
    Returns escalation dict if a sensitive keyword is found, else None.
    """
    q_lower  = query.lower()
    keywords = SENSITIVE_KEYWORDS.get(domain, [])

    for kw in keywords:
        if kw in q_lower:
            log_agent("safety_post", f"ESCALATE — keyword='{kw}' domain={domain}", {})
            return _escalate(
                rule=f"S2-{domain}-sensitive",
                reason=f"Sensitive topic detected ('{kw}'). Requires human specialist.",
                keyword=kw,
            )

    # Cross-domain safety: Visa card data in any ticket
    if any(t in q_lower for t in ["cvv", "card number", " pan ", "stolen card"]):
        log_agent("safety_post", "ESCALATE — card PII detected", {})
        return _escalate(
            rule="S2-card-pii",
            reason="Card/payment PII detected. Do not process — escalate immediately.",
            keyword="card-pii",
        )

    log_agent("safety_post", "PASS — no sensitive keywords", {"domain": domain})
    return None


def _escalate(rule: str, reason: str, keyword: str = "") -> dict:
    return {
        "status":         "escalated",
        "request_type":   "product_issue",
        "product_area":   "unknown",
        "response":       ESCALATION_RESPONSE,
        "justification":  f"[{rule}] {reason}",
        "rule_triggered": rule,
        "keyword":        keyword,
    }