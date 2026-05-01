"""
Safety Pass 2 — Post-retrieval
Catches: fraud, legal threats, account access, financial disputes, enterprise/sales.
Runs AFTER retrieval so domain is confirmed.
"""

from config import SENSITIVE_KEYWORDS, ESCALATION_RESPONSE
from utils.logger import log_agent


HIGH_RISK_KEYWORDS = [
    "identity theft", "stolen card", "lost card", "fraud", "fraudulent",
    "unauthorized transaction", "hacked", "data breach",
    "chargeback", "dispute transaction", "scam", "phishing",
    "identity stolen", "identity has been stolen", "my identity was stolen",
    "id theft", "someone stole my identity", "account taken over",
]

ENTERPRISE_KEYWORDS = [
    "infosec", "security questionnaire", "security form",
    "vendor assessment", "compliance form", "soc 2", "iso 27001",
    "enterprise procurement", "vendor form",
]


def run(query: str, domain: str) -> dict | None:
    q_lower = query.lower()
    keywords = SENSITIVE_KEYWORDS.get(domain, {})

    high_risk_list = keywords.get("high_risk", [])
    for kw in high_risk_list:
        if kw in q_lower:
            log_agent("safety_post", f"ESCALATE HIGH RISK — keyword='{kw}' domain={domain}", {})
            return _escalate(
                rule="high",
                reason=f"High-risk topic detected ('{kw}'). Requires human specialist.",
                keyword=kw,
            )

    medium_risk_list = keywords.get("medium_risk", [])
    for kw in medium_risk_list:
        if kw in q_lower:
            log_agent("safety_post", f"ESCALATE — keyword='{kw}' domain={domain}", {})
            return _escalate(
                rule="medium",
                reason=f"Sensitive topic detected ('{kw}').",
                keyword=kw,
            )

    for kw in HIGH_RISK_KEYWORDS:
        if kw in q_lower:
            log_agent("safety_post", f"ESCALATE HIGH RISK — cross-domain keyword='{kw}'", {})
            return _escalate(
                rule="high",
                reason=f"High-risk topic detected ('{kw}').",
                keyword=kw,
            )

    for kw in ENTERPRISE_KEYWORDS:
        if kw in q_lower:
            log_agent("safety_post", f"ESCALATE ENTERPRISE — keyword='{kw}' domain={domain}", {})
            return _escalate(
                rule="enterprise",
                reason=f"Enterprise/sales topic detected ('{kw}').",
                keyword=kw,
                custom_response=f"This request requires our enterprise team. Please contact sales@hackerrank.com or your account manager for security documentation and compliance forms.",
            )

    if any(t in q_lower for t in ["cvv", "card number", "pan", "stolen card"]):
        log_agent("safety_post", "ESCALATE — card PII detected", {})
        return _escalate(
            rule="high",
            reason="Card/payment PII detected. Do not process.",
            keyword="card-pii",
        )

    log_agent("safety_post", "PASS — no sensitive keywords", {"domain": domain})
    return None


def _escalate(rule: str, reason: str, keyword: str = "", custom_response: str = None) -> dict:
    response = custom_response or "This issue requires further investigation and has been escalated to support."
    return {
        "status": "escalated",
        "request_type": "product_issue",
        "product_area": "unknown",
        "response": response,
        "justification": f"[{rule}] {reason}",
        "rule_triggered": rule,
        "keyword": keyword,
        "custom_response": custom_response,
    }