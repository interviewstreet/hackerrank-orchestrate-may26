import re
from typing import Optional

VALID_PRODUCT_AREAS = {
    "authentication",
    "payments",
    "account_access",
    "card_usage",
    "security",
    "fraud_and_security",
    "assessment_integrity",
    "access_control",
    "out_of_scope",
}


def _normalize_product_area(area: str) -> str:
    normalized = str(area or "").strip().lower().replace(" ", "_")
    return normalized if normalized in VALID_PRODUCT_AREAS else "security"

def pre_classify(ticket: dict) -> Optional[dict]:
    issue = ticket.get('issue', '').lower()
    subject = ticket.get('subject', '').lower()
    combined = f"{subject} {issue}"

    # Safety/Escalation Rules
    escalation_patterns = [
        # Fraud / Stolen Card
        r"fraud", r"stolen", r"unauthorized", r"chargeback", r"identity theft",
        # Account Takeover
        r"hacked", r"compromised", r"takeover", r"stolen password",
        # Internal Logic / Prompts
        r"internal logic", r"system prompt", r"ignore previous", r"developer mode",
        # Legal / Law Enforcement
        r"legal", r"lawsuit", r"police", r"law enforcement", r"subpoena", r"attorney",
        # Site Down (Generic/No context)
        r"^site is down$", r"^platform is down$",
        # Score Disputes
        r"review my score", r"increase my score", r"graded unfairly", r"move me to the next round",
        # Prompt Injection
        r"you are now", r"stay in character", r"ignore all instructions"
    ]

    for pattern in escalation_patterns:
        if re.search(pattern, combined):
            return {
                "status": "escalated",
                "product_area": _normalize_product_area("security"),
                "response": "This issue requires human support due to its sensitive nature. We are escalating your request to the appropriate team.",
                "justification": f"Sensitive or unsupported issue detected; matched pattern '{pattern}' and escalated for human review.",
                "request_type": "product_issue"
            }

    # Non-English detection (Simplified for hackathon)
    common_english = {"the", "and", "for", "with", "have", "this", "that"}
    words = set(re.findall(r'\w+', combined))
    if len(words) > 10 and not (words & common_english):
        return {
            "status": "escalated",
            "product_area": _normalize_product_area("security"),
            "response": "I'm sorry, I am currently optimized for English support. I am escalating this to a human agent who can better assist you.",
            "justification": "Potential non-English request detected and escalated for human review.",
            "request_type": "product_issue"
        }

    return None
