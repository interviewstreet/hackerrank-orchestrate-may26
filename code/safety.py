"""
safety.py — Rule-based safety and escalation gate.

WHAT THIS MODULE DOES:
  Decides if a ticket MUST be escalated (or marked invalid/replied)
  BEFORE we even try to generate a response.

WHY:
  Escalating sensitive tickets (fraud, deletion, overrides) is a core
  requirement. Rule-based checks are 100% reliable and fast.
"""

import re
import unicodedata

from config import ESCALATION_KEYWORDS, INJECTION_PATTERNS, MALICIOUS_PATTERNS
from models import TicketOutput, make_escalation, make_invalid


# ── Compiled Regexes ──────────────────────────────────────────────────────────

_INJECTION_REGEXES = [re.compile(p, re.IGNORECASE) for p in INJECTION_PATTERNS]
_MALICIOUS_REGEXES = [re.compile(p, re.IGNORECASE) for p in MALICIOUS_PATTERNS]


class SafetyResult:
    def __init__(self, escalate: bool, reason: str, output: TicketOutput | None = None):
        self.escalate = escalate
        self.reason = reason
        self.output = output


def check(issue: str, subject: str, request_type: str, product_area: str) -> SafetyResult:
    """
    Run all safety rules. Returns a SafetyResult.
    """
    combined_text = f"{subject} {issue}".strip()
    combined_lower = combined_text.lower()

    # 1. Invalid request_type (from classifier)
    if request_type == "invalid":
        reason = "Ticket classified as invalid/out-of-scope."
        return SafetyResult(True, reason, make_invalid(product_area))

    # 2. Prompt Injection
    for pattern in _INJECTION_REGEXES:
        if pattern.search(combined_text):
            reason = f"Prompt injection attempt detected: {pattern.pattern}"
            return SafetyResult(True, reason, make_escalation(reason, "security", "invalid"))

    # 3. Malicious Commands
    for pattern in _MALICIOUS_REGEXES:
        if pattern.search(combined_text):
            reason = f"Malicious command detected: {pattern.pattern}"
            return SafetyResult(True, reason, make_invalid("security"))

    # 4. Escalation Keywords (Exact substring match for speed/accuracy)
    for keyword in ESCALATION_KEYWORDS:
        if keyword in combined_lower:
            reason = f"High-risk keyword detected: '{keyword}'"
            return SafetyResult(True, reason, make_escalation(reason, product_area, request_type))

    # 5. Non-English detection
    if _is_non_english(combined_text):
        reason = "Ticket appears to be non-English."
        return SafetyResult(True, reason, make_escalation(reason, product_area, request_type))

    return SafetyResult(False, "", None)


def _is_non_english(text: str) -> bool:
    """
    Simple heuristic non-English detection (no external libs).
    Checks for non-Latin scripts and common French/Spanish triggers.
    """
    if len(text.strip()) < 20:
        return False

    # Check for non-Latin scripts
    non_latin_count: int = 0
    for ch in text:
        name = unicodedata.name(ch, "")
        if any(script in name for script in ["CYRILLIC", "ARABIC", "CJK", "DEVANAGARI", "HEBREW", "THAI"]):
            non_latin_count += 1
            if non_latin_count > 3:
                return True

    # Common French/Spanish triggers
    triggers = [
        r"\bbonjour\b", r"\bmerci\b", r"\bs'il vous pla[iî]t\b",
        r"\bhola\b", r"\bgracias\b", r"\btarjeta\b", r"\bbloqueada\b"
    ]
    text_lower = text.lower()
    for trigger in triggers:
        if re.search(trigger, text_lower):
            return True

    return False
