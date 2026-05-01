"""Heuristic risk signals — conservative escalation when patterns clearly exceed self‑service docs."""

from __future__ import annotations

import re
from dataclasses import dataclass

from corpus import _tokenize


@dataclass(frozen=True)
class SafetyDecision:
    force_escalate: bool
    reason: str


_OUTAGE_PATTERNS = [
    re.compile(r"\bsite\b.*\bdown\b", re.I),
    re.compile(r"\bnone\b.*\bsubmissions\b.*\bworking\b", re.I),
    re.compile(r"\ball\b.*\bpages\b.*\binaccessible\b", re.I),
    re.compile(r"\bwide(spread)?\b.*\boutage\b", re.I),
]

_HR_SCORE_DISPUTE = re.compile(
    r"(unfair|wrongful).*(score|grade|grading)|"
    r"(increase|raise|change).*(score|grade)|"
    r"reject(ed)?\s+me.*(score|test)|"
    r"review\s+my\s+answers",
    re.I | re.S,
)

_HR_BILLING_FORCE = re.compile(
    r"order\s+id:\s*cs_|stripe.*charge|chargeback|dispute\s+payment", re.I
)

_VISA_MERCHANT_FORCE = re.compile(
    r"\b(ban|blacklist)\b.*\b(seller|merchant)\b|" r"force\b.*\brefund\b|refund\s+me\s+today",
    re.I | re.S,
)

_ACCESS_OVERRIDE = re.compile(
    r"restore\s+my\s+access(\s+immediately)?|" r"not\s+the\s+(owner|admin)|without\s+admin",
    re.I,
)

_PROMPT_INJECTION = re.compile(
    r"ignore\s+(all\s+)?(previous|prior)\s+instructions|" r"system\s*:\s*you\s+are\s+now|" r"jailbreak",
    re.I,
)


def assess_risk(issue: str, subject: str, company: str | None) -> SafetyDecision | None:
    blob = f"{issue}\n{subject}"
    if _PROMPT_INJECTION.search(blob):
        return SafetyDecision(True, "Possible prompt injection — escalate for human review.")

    for pat in _OUTAGE_PATTERNS:
        if pat.search(blob):
            return SafetyDecision(True, "Broad outage or platform-wide failure signal — escalate.")

    c = (company or "").strip().lower()
    if c in ("hackerrank", "none", ""):
        if _HR_SCORE_DISPUTE.search(blob):
            return SafetyDecision(
                True,
                "Score dispute or grading override request — not safely handled from docs alone.",
            )
        if _HR_BILLING_FORCE.search(blob):
            return SafetyDecision(True, "Specific billing/payment dispute identifiers — escalate.")

    if c in ("visa", "none", ""):
        if _VISA_MERCHANT_FORCE.search(blob):
            return SafetyDecision(
                True,
                "Merchant dispute or forced remediation — requires issuer/human handling.",
            )

    if c in ("claude", "none", ""):
        if _ACCESS_OVERRIDE.search(blob) and (
            "seat" in blob.lower() or "workspace" in blob.lower() or "admin" in blob.lower()
        ):
            return SafetyDecision(
                True,
                "Workspace access restoration without admin authority — escalate.",
            )

    return None


_THANKS_ONLY = re.compile(
    r"^(thank\s+you(\s+for\s+(helping\s+me|your\s+help))?|thanks(\s+again)?|thx)\s*[!.]*\s*$",
    re.I,
)


def trivial_invalid_greeting(issue: str, subject: str) -> bool:
    t = f"{issue} {subject}".strip()
    if _THANKS_ONLY.match(t.strip()):
        return True
    tl = t.lower()
    toks = set(_tokenize(t))
    if len(toks) <= 4 and re.match(
        r"^(thank(s|\s+you)|hi|hello|ok|okay|great)[!.?\s]*$", tl.strip(), re.I
    ):
        return True
    return False
