"""
Safety Pass 1 — Pre-retrieval
Catches: prompt injection, gibberish, zero-content tickets.
Runs FIRST — before any compute is spent on retrieval.
"""

import re
import math
from collections import Counter
from config import INJECTION_PATTERNS, ESCALATION_RESPONSE


def _entropy(text: str) -> float:
    """Shannon entropy of character distribution — low = repetitive/gibberish."""
    if not text:
        return 0.0
    counts = Counter(text)
    total  = len(text)
    return -sum((c / total) * math.log2(c / total) for c in counts.values())


def run(query: str) -> dict | None:
    """
    Returns an escalation dict if the ticket should be rejected immediately.
    Returns None if the ticket passes and should continue through the pipeline.
    """
    cleaned = query.strip().lower()

    # R1 — prompt injection
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, cleaned, re.IGNORECASE):
            return _escalate(
                rule="R1-injection",
                reason=f"Prompt injection pattern detected: '{pattern}'",
            )

    # R2 — too short to be meaningful
    if len(cleaned.replace(" ", "")) < 10:
        return _escalate(
            rule="R2-too-short",
            reason="Ticket content is too short or empty to process.",
        )

    # R3 — gibberish: very low entropy OR all-caps random chars
    if _entropy(cleaned) < 1.5:
        return _escalate(
            rule="R3-gibberish",
            reason="Ticket appears to be gibberish (low character entropy).",
        )

    # R4 — no real words (sequence of random chars)
    word_count = len([w for w in cleaned.split() if len(w) > 1 and w.isalpha()])
    if word_count < 2:
        return _escalate(
            rule="R4-no-words",
            reason="Ticket contains no recognisable words.",
        )

    return None  # passed


def _escalate(rule: str, reason: str) -> dict:
    return {
        "status":           "escalated",
        "request_type":     "invalid",
        "product_area":     "unknown",
        "response":         ESCALATION_RESPONSE,
        "justification":    f"[{rule}] {reason}",
        "rule_triggered":   rule,
    }