import re


ESCALATION_PATTERNS = [
    (r'\b(my\s+)?identity\s+(has\s+been\s+)?stolen\b', 'Contains identity theft - high security risk'),
    (r'\bsecurity\s+vulnerability\b', 'Contains security vulnerability report'),
    (r'\b(delete|give\s+me)\s+.*(all\s+)?files?\s+from\s+(the\s+)?system', 'Request to delete system files - dangerous'),
    (r'\b(stolen|lost)\s+(card|identity)\b', 'Stolen/lost card with sensitive data'),
]

SUSPICIOUS_PATTERNS = [
    (r'\b(delete\s+all\s+files)\b', 'Suspicious file deletion request'),
]


def should_escalate(issue: str, subject: str) -> tuple:
    text = (issue + " " + (subject or "")).lower()
    text = re.sub(r'\s+', ' ', text).strip()
    
    for pattern, reason in ESCALATION_PATTERNS:
        if re.search(pattern, issue, re.IGNORECASE):
            return True, reason
    
    for pattern, reason in SUSPICIOUS_PATTERNS:
        if re.search(pattern, issue, re.IGNORECASE):
            return True, reason
    
    return False, "Standard processing"