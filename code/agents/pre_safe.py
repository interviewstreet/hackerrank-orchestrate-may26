"""
Safety Pass 1 — Pre-retrieval
Catches: prompt injection, gibberish, zero-content tickets, high-risk keywords.
Runs FIRST — before any compute is spent on retrieval.
"""

import re
import math
from collections import Counter
from config import INJECTION_PATTERNS, ESCALATION_RESPONSE

ENTROPY_THRESHOLD = 1.5

HIGH_RISK_KEYWORDS = [
    "identity theft", "id theft", "identity stolen", "identity has been stolen",
    "my identity was stolen", "someone stole my identity",
    "stolen card", "hacked", "fraud", "unauthorized transaction",
    "data breach", "chargeback", "legal action", "lawsuit", "court",
]

MALICIOUS_INTENT_KEYWORDS = [
    "delete all", "remove all", "wipe all", "erase all",
    "destroy all", "remove everything", "clear all data",
    "cancel all", "terminate all", "drop all",
]


def _entropy(text: str) -> float:
    """Shannon entropy of character distribution — low = repetitive/gibberish."""
    if not text:
        return 0.0
    counts = Counter(text)
    total = len(text)
    return -sum((c / total) * math.log2(c / total) for c in counts.values())


def run(query: str) -> dict | None:
    cleaned = query.strip().lower()

    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, cleaned, re.IGNORECASE):
            return _escalate(
                rule="high",
                reason=f"Prompt injection pattern detected: '{pattern}'",
            )

    for kw in HIGH_RISK_KEYWORDS:
        if kw in cleaned:
            return _escalate(
                rule="high",
                reason=f"High-risk keyword detected: '{kw}'",
            )

    for kw in MALICIOUS_INTENT_KEYWORDS:
        if kw in cleaned:
            return _escalate(
                rule="high",
                reason=f"Potentially malicious intent detected: '{kw}'",
            )

    if len(cleaned.replace(" ", "")) < 10:
        return _escalate(
            rule="R2-too-short",
            reason="Ticket content is too short or empty to process.",
        )

    if _entropy(cleaned) < ENTROPY_THRESHOLD:
        return _escalate(
            rule="R3-gibberish",
            reason="Ticket appears to be gibberish (low character entropy).",
        )

    word_count = len([w for w in cleaned.split() if len(w) > 1 and w.isalpha()])
    if word_count < 2:
        return _escalate(
            rule="R4-no-words",
            reason="Ticket contains no recognisable words.",
        )

    return None


def _escalate(rule: str, reason: str) -> dict:
    return {
        "status": "escalated",
        "request_type": "invalid",
        "product_area": "unknown",
        "response": "This issue requires further investigation and has been escalated to support.",
        "justification": f"[{rule}] {reason}",
        "rule_triggered": rule,
    }