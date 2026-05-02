"""LLM-driven classifier with heuristic priors.

Pipeline:
  1. Compute hard heuristic priors (chitchat / outage / trivia / pleasantry).
  2. If the preprocessor already flagged prompt injection, short-circuit to
     ``request_type=invalid`` (T-6) without spending an LLM call.
  3. Otherwise: single Anthropic ``tool_use`` call to claude-sonnet-4-5
     with ``temperature=0`` and a mandatory tool whose schema mirrors
     :class:`ClassificationResult`. Pydantic validates the input dict.
  4. On parse / validation failure: retry once. After two failures, return
     a fallback ``request_type=invalid`` payload — the escalation table will
     fire T-1 / T-5 on it downstream.
  5. Reconcile heuristic priors with the LLM payload (more conservative
     wins — heuristic ``True`` overrides LLM ``False`` for outage and
     chitchat flags).

PRD references: FR-010..FR-017, T-3, T-5, T-6, NFR-001.
Architecture references: section 3.7.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from schemas import CleanedTicket, ClassificationResult

# Pinned per Architecture section 8 / config.yaml.
_ANTHROPIC_MODEL = "claude-sonnet-4-5"
_MAX_TOKENS_CLASSIFIER = 400

_PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"

# ---------- heuristic priors ------------------------------------------------

_OUTAGE_PATTERN = re.compile(
    r"(?ix)"
    r"("
    r"  (site|service|server|page|app|website|portal|builder|platform)"
    r"  \s+ (is\s+)? (down|broken|unavailable|inaccessible)"
    r"| none\s+of\s+the\s+pages"
    r"| pas\s+accessible"
    r"| (has\s+)?stopped\s+working"
    r"| resume\s+builder\s+is\s+down"
    r")"
)

_CHITCHAT_PLEASANTRY = re.compile(
    r"(?i)^\s*(thank(s| you)|happy to help|cheers|ok thanks|appreciated|thx)\b"
)

_TRIVIA_PATTERNS = (
    re.compile(r"(?i)\b(world cup|capital of|movie trivia|sports trivia|fifa|olympics)\b"),
    re.compile(r"(?i)^\s*(who|what|when|where)\s+(won|invented|discovered|wrote|composed)\b"),
)

_QUESTION_WORDS = re.compile(
    r"(?i)\b(how|what|why|when|where|which|who|can|could|should|would|may|will|do|does|did|is|are|was|were)\b"
    r"|\?"
)


def compute_heuristic_priors(cleaned: CleanedTicket) -> dict[str, bool]:
    """Cheap regex priors that run before the LLM call.

    Architecture says these "ride alongside" the LLM result; the merge
    rule (more-conservative-wins) is applied in :func:`classify`.
    """
    body = cleaned.sanitized_body
    subject = cleaned.sanitized_subject
    combined = f"{subject}\n{body}".strip()

    is_outage = bool(_OUTAGE_PATTERN.search(combined))

    is_chitchat = False
    if _CHITCHAT_PLEASANTRY.search(combined):
        is_chitchat = True
    elif any(p.search(combined) for p in _TRIVIA_PATTERNS):
        is_chitchat = True
    elif len(body.strip()) < 30 and not _QUESTION_WORDS.search(combined):
        is_chitchat = True

    return {
        "is_outage_report": is_outage,
        "is_chitchat_or_trivia": is_chitchat,
        "is_authorization_violation": False,  # Delegated to LLM in v1.
        "is_sensitive": False,                # Delegated to LLM in v1.
    }


# ---------- LLM tool schema -------------------------------------------------

_CLASSIFICATION_TOOL: dict[str, Any] = {
    "name": "classify_ticket",
    "description": (
        "Emit the structured classification of the support ticket. "
        "All fields are mandatory; do not return any other text."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "request_type": {
                "type": "string",
                "enum": ["product_issue", "feature_request", "bug", "invalid"],
            },
            "domain": {
                "type": "string",
                "enum": ["hackerrank", "claude", "visa", "none"],
            },
            "domain_confidence": {"type": "number", "minimum": 0, "maximum": 1},
            "product_area": {"type": "string"},
            "product_area_confidence": {"type": "number", "minimum": 0, "maximum": 1},
            "is_sensitive": {"type": "boolean"},
            "is_outage_report": {"type": "boolean"},
            "is_multi_request": {"type": "boolean"},
            "is_authorization_violation": {"type": "boolean"},
            "is_chitchat_or_trivia": {"type": "boolean"},
            "reasoning": {"type": "string"},
        },
        "required": [
            "request_type",
            "domain",
            "domain_confidence",
            "product_area",
            "product_area_confidence",
            "is_sensitive",
            "is_outage_report",
            "is_multi_request",
            "is_authorization_violation",
            "is_chitchat_or_trivia",
        ],
    },
}


def _system_prompt() -> str:
    path = _PROMPTS_DIR / "classifier.system.md"
    return path.read_text(encoding="utf-8")


def _user_message(cleaned: CleanedTicket) -> list[dict[str, Any]]:
    body = (
        f"Company hint (raw, may be 'None'): {cleaned.ticket.company}\n"
        f"Subject (delimited): <<<USER_SUBJECT_BEGIN>>>{cleaned.sanitized_subject}<<<USER_SUBJECT_END>>>\n"
        f"Body (delimited): <<<USER_TICKET_BEGIN>>>{cleaned.sanitized_body}<<<USER_TICKET_END>>>"
    )
    return [{"role": "user", "content": body}]


def _extract_tool_payload(response: Any) -> dict[str, Any] | None:
    for block in getattr(response, "content", []) or []:
        if getattr(block, "type", None) == "tool_use" and getattr(block, "name", "") == "classify_ticket":
            payload = getattr(block, "input", None)
            if isinstance(payload, dict):
                return payload
    return None


def _fallback_invalid_payload() -> dict[str, Any]:
    return {
        "request_type": "invalid",
        "domain": "none",
        "domain_confidence": 0.0,
        "product_area": "uncategorized",
        "product_area_confidence": 0.0,
        "is_sensitive": False,
        "is_outage_report": False,
        "is_multi_request": False,
        "is_authorization_violation": False,
        "is_chitchat_or_trivia": False,
    }


def _validated_kwargs(payload: dict[str, Any]) -> dict[str, Any]:
    """Drop unknown keys (e.g. ``reasoning``) before constructing the model."""
    fields = set(ClassificationResult.model_fields.keys())
    return {k: v for k, v in payload.items() if k in fields}


def _merge_with_priors(
    payload: dict[str, Any], priors: dict[str, bool]
) -> ClassificationResult:
    merged = dict(payload)
    for key in ("is_outage_report", "is_chitchat_or_trivia"):
        if priors.get(key):
            merged[key] = True
    return ClassificationResult(**_validated_kwargs(merged))


def _default_client() -> Any:
    import anthropic  # local import so tests without the SDK still pass.

    return anthropic.Anthropic()


def classify(cleaned: CleanedTicket, *, client: Any | None = None) -> ClassificationResult:
    """Classify a cleaned ticket.

    Parameters
    ----------
    cleaned: ``CleanedTicket`` from :func:`preprocessor.clean`.
    client:  Optional Anthropic client (or test double). When ``None`` a
             real ``anthropic.Anthropic()`` is constructed lazily, which
             requires ``ANTHROPIC_API_KEY`` in the environment.
    """
    priors = compute_heuristic_priors(cleaned)

    # T-6 short-circuit: prompt injection detected → invalid, skip LLM.
    if cleaned.injection_detected:
        return _merge_with_priors(_fallback_invalid_payload(), priors)

    if client is None:
        client = _default_client()

    payload: dict[str, Any] | None = None
    last_error: Exception | None = None
    for _attempt in range(2):
        try:
            response = client.messages.create(
                model=_ANTHROPIC_MODEL,
                max_tokens=_MAX_TOKENS_CLASSIFIER,
                temperature=0.0,
                system=_system_prompt(),
                tools=[_CLASSIFICATION_TOOL],
                tool_choice={"type": "tool", "name": "classify_ticket"},
                messages=_user_message(cleaned),
            )
        except Exception as exc:  # network / SDK surface — retry once.
            last_error = exc
            payload = None
            continue

        candidate = _extract_tool_payload(response)
        if candidate is None:
            payload = None
            continue

        try:
            ClassificationResult(**_validated_kwargs(candidate))
        except ValidationError as exc:
            last_error = exc
            payload = None
            continue

        payload = candidate
        break

    if payload is None:
        payload = _fallback_invalid_payload()

    return _merge_with_priors(payload, priors)
