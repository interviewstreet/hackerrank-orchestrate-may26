"""Ticket sanitization and prompt-injection neutralization.

Two passes per ticket per Architecture section 3.4:
  1. Sanitize: strip control chars, collapse whitespace runs in headers
     (preserve newlines in body), cap body at 8 000 chars.
  2. Detect prompt-injection signatures in subject + body via regex; set
     ``injection_detected`` for downstream consumers (T-6).

PRD references: FR-035, T-6, NFR-008.
Architecture references: section 3.4.
"""

from __future__ import annotations

import re

from schemas import CleanedTicket, Ticket

MAX_BODY_CHARS = 8000

_CONTROL_CHARS_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
_HSPACE_RUN_RE = re.compile(r"[ \t ]+")
_ANY_WHITESPACE_RE = re.compile(r"\s+")

_INJECTION_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"ignore (the )?(previous|prior|above)\s+(instructions|rules|prompt)", re.IGNORECASE),
    re.compile(r"disregard\s+(your\s+|all\s+|the\s+)?(previous|prior|above|internal)?\s*(instructions|rules|prompt)", re.IGNORECASE),
    re.compile(r"(show|print|reveal|share|expose|leak)\s+(me\s+)?(your|the)?\s*(internal|system|hidden)?\s*(prompt|rules|tools|instructions|guidelines)", re.IGNORECASE),
    re.compile(r"(show|share|reveal)\s+(me\s+)?(your|the)?\s*(retrieved|internal|system)\s+(documents|content|context)", re.IGNORECASE),
    re.compile(r"affiche.*?(r[èe]gles|documents|logique|prompt|instructions)", re.IGNORECASE),
    re.compile(r"\bdelete\s+all\s+files\b", re.IGNORECASE),
    re.compile(r"\brm\s+-rf\b", re.IGNORECASE),
    re.compile(r"system prompt", re.IGNORECASE),
)


def _sanitize_body(text: str) -> str:
    text = text.replace("\r", "")
    text = _CONTROL_CHARS_RE.sub("", text)
    lines = text.split("\n")
    lines = [_HSPACE_RUN_RE.sub(" ", line).strip(" \t") for line in lines]
    text = "\n".join(lines).strip()
    if len(text) > MAX_BODY_CHARS:
        text = text[:MAX_BODY_CHARS]
    return text


def _sanitize_header(text: str) -> str:
    text = text.replace("\r", "")
    text = _CONTROL_CHARS_RE.sub("", text)
    text = _ANY_WHITESPACE_RE.sub(" ", text).strip()
    return text


def _detect_injection(text: str) -> bool:
    if not text:
        return False
    for pattern in _INJECTION_PATTERNS:
        if pattern.search(text):
            return True
    return False


def clean(ticket: Ticket) -> CleanedTicket:
    """Sanitize the ticket and flag prompt-injection signatures.

    The original strings are kept on ``ticket``; sanitized variants and
    the injection flag are added to the returned :class:`CleanedTicket`.
    """
    sanitized_body = _sanitize_body(ticket.issue)
    sanitized_subject = _sanitize_header(ticket.subject)
    injection_detected = (
        _detect_injection(ticket.issue)
        or _detect_injection(ticket.subject)
        or _detect_injection(sanitized_body)
        or _detect_injection(sanitized_subject)
    )
    return CleanedTicket(
        ticket=ticket,
        sanitized_body=sanitized_body,
        sanitized_subject=sanitized_subject,
        injection_detected=injection_detected,
    )
