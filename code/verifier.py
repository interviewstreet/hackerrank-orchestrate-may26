"""Post-hoc grounding verifier.

Extracts the high-risk fabrication targets — phone numbers, URLs, and
dollar amounts — from the reasoner's response, and checks each one
appears in the union of retrieved corpus chunks. Generic numerics
(years, dates, small running-text counts) are intentionally NOT checked
because the reasoner often paraphrases them.

A fabrication of any of the three target classes returns ``False``.
That escalation signal feeds T-1 in the escalation policy (R-1 mitigation).

PRD references: FR-030, R-1, AC-4.
Architecture references: section 3.8.
"""

from __future__ import annotations

import re

from schemas import RetrievedDoc

_PHONE_RE = re.compile(
    r"(?:\+?\d{1,3}[-.\s]+)?\(?\d{3}\)?[-.\s]+\d{3}[-.\s]+\d{4}"
)
_URL_RE = re.compile(r"https?://[^\s)\]<>,;]+", re.IGNORECASE)
_DOLLAR_RE = re.compile(r"\$\d+(?:,\d{3})*(?:\.\d{1,2})?")


def _normalize_phone(raw: str) -> str:
    return re.sub(r"\D", "", raw)


def _normalize_url(raw: str) -> str:
    return raw.rstrip(".,;)").lower()


def _extract_phones(text: str) -> set[str]:
    return {_normalize_phone(m.group(0)) for m in _PHONE_RE.finditer(text)}


def _extract_urls(text: str) -> set[str]:
    return {_normalize_url(m.group(0)) for m in _URL_RE.finditer(text)}


def _extract_dollars(text: str) -> set[str]:
    return {m.group(0) for m in _DOLLAR_RE.finditer(text)}


def verify_grounding(response: str, retrieved: list[RetrievedDoc]) -> bool:
    """Return ``True`` iff every checkable token in ``response`` is present
    in the union of retrieved chunk text.

    Checkable tokens are phone numbers (NANP-style 3-3-4 digits, optionally
    international-prefixed), HTTP/HTTPS URLs, and dollar amounts. Dates,
    years, and bare integers in running text are ignored.
    """
    if not response:
        return True

    chunk_text_union = "\n".join(d.text for d in retrieved)

    response_phones = _extract_phones(response)
    response_urls = _extract_urls(response)
    response_dollars = _extract_dollars(response)

    if not (response_phones or response_urls or response_dollars):
        return True

    chunk_phones = _extract_phones(chunk_text_union)
    chunk_urls = _extract_urls(chunk_text_union)
    chunk_dollars = _extract_dollars(chunk_text_union)

    if not response_phones <= chunk_phones:
        return False
    if not response_urls <= chunk_urls:
        return False
    if not response_dollars <= chunk_dollars:
        return False
    return True
