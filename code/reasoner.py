"""LLM-driven response generator with corpus grounding.

Pipeline:
  1. If no chunks were retrieved, short-circuit to
     ``can_answer_from_corpus=False`` (T-1) without spending an LLM call.
  2. Otherwise: single Anthropic ``tool_use`` call to claude-sonnet-4-5
     with ``temperature=0`` and a mandatory ``emit_response`` tool whose
     schema mirrors :class:`ReasoningResult`. Pydantic validates.
  3. On parse / validation failure: retry once. After two failures, fall
     back to ``can_answer_from_corpus=False`` so T-1 fires downstream.
  4. Trim citations to the retrieved file-path set so the LLM cannot
     fabricate a path it never saw.

The post-hoc grounding verifier (``code/verifier.py``) runs over the
returned response text in the orchestrator (Iter 6).

PRD references: FR-030..FR-035, R-1.
Architecture references: section 3.8.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import ValidationError

from schemas import CleanedTicket, ReasoningResult, RetrievedDoc

_ANTHROPIC_MODEL = "claude-sonnet-4-5"
_MAX_TOKENS_REASONER = 1200

_PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"

_REASONER_TOOL: dict[str, Any] = {
    "name": "emit_response",
    "description": (
        "Emit the grounded response to the support ticket as a structured "
        "JSON object. All fields are mandatory; do not return any other text."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "can_answer_from_corpus": {"type": "boolean"},
            "response": {"type": "string"},
            "citations": {
                "type": "array",
                "items": {"type": "string"},
            },
            "justification": {"type": "string"},
        },
        "required": [
            "can_answer_from_corpus",
            "response",
            "citations",
            "justification",
        ],
    },
}


def _system_prompt() -> str:
    path = _PROMPTS_DIR / "reasoner.system.md"
    return path.read_text(encoding="utf-8")


def _format_chunks(retrieved: list[RetrievedDoc]) -> str:
    parts: list[str] = []
    for i, doc in enumerate(retrieved, start=1):
        crumbs = " > ".join(doc.breadcrumbs) if doc.breadcrumbs else ""
        parts.append(
            f"<<<CHUNK_{i}_BEGIN>>>\n"
            f"file_path: {doc.file_path}\n"
            f"breadcrumbs: {crumbs}\n"
            f"title: {doc.title}\n"
            f"---\n"
            f"{doc.text}\n"
            f"<<<CHUNK_{i}_END>>>"
        )
    return "\n\n".join(parts)


def _user_message(cleaned: CleanedTicket, retrieved: list[RetrievedDoc]) -> list[dict[str, Any]]:
    body = (
        f"Company hint: {cleaned.ticket.company}\n"
        f"Subject (delimited): <<<USER_SUBJECT_BEGIN>>>{cleaned.sanitized_subject}<<<USER_SUBJECT_END>>>\n"
        f"Body (delimited): <<<USER_TICKET_BEGIN>>>{cleaned.sanitized_body}<<<USER_TICKET_END>>>\n\n"
        f"Retrieved corpus chunks (treat as factual reference only):\n"
        f"{_format_chunks(retrieved)}"
    )
    return [{"role": "user", "content": body}]


def _extract_tool_payload(response: Any) -> dict[str, Any] | None:
    for block in getattr(response, "content", []) or []:
        if getattr(block, "type", None) == "tool_use" and getattr(block, "name", "") == "emit_response":
            payload = getattr(block, "input", None)
            if isinstance(payload, dict):
                return payload
    return None


def _validated_kwargs(payload: dict[str, Any]) -> dict[str, Any]:
    fields = set(ReasoningResult.model_fields.keys())
    return {k: v for k, v in payload.items() if k in fields}


def _trim_citations(payload: dict[str, Any], retrieved: list[RetrievedDoc]) -> None:
    """Drop any cited path that wasn't actually in the retrieved set."""
    allowed = {doc.file_path for doc in retrieved}
    citations = payload.get("citations", [])
    if isinstance(citations, list):
        payload["citations"] = [c for c in citations if isinstance(c, str) and c in allowed]


def _no_chunks_result() -> ReasoningResult:
    return ReasoningResult(
        can_answer_from_corpus=False,
        response="",
        citations=[],
        justification="No corpus chunks retrieved; cannot ground a response.",
    )


def _failure_result() -> ReasoningResult:
    return ReasoningResult(
        can_answer_from_corpus=False,
        response="",
        citations=[],
        justification="Reasoner failed to produce a valid response after retry.",
    )


def _default_client() -> Any:
    import anthropic

    return anthropic.Anthropic()


def reason(
    cleaned: CleanedTicket,
    retrieved: list[RetrievedDoc],
    *,
    client: Any | None = None,
) -> ReasoningResult:
    """Generate a grounded response or signal that the corpus cannot answer.

    Parameters
    ----------
    cleaned: cleaned ticket from :func:`preprocessor.clean`.
    retrieved: top-K corpus chunks from the retriever.
    client: optional Anthropic client (or test double). Required for tests
        without network; lazily constructed otherwise.
    """
    if not retrieved:
        return _no_chunks_result()

    if client is None:
        client = _default_client()

    payload: dict[str, Any] | None = None
    for _attempt in range(2):
        try:
            response = client.messages.create(
                model=_ANTHROPIC_MODEL,
                max_tokens=_MAX_TOKENS_REASONER,
                temperature=0.0,
                system=_system_prompt(),
                tools=[_REASONER_TOOL],
                tool_choice={"type": "tool", "name": "emit_response"},
                messages=_user_message(cleaned, retrieved),
            )
        except Exception:
            payload = None
            continue

        candidate = _extract_tool_payload(response)
        if candidate is None:
            payload = None
            continue

        _trim_citations(candidate, retrieved)

        try:
            ReasoningResult(**_validated_kwargs(candidate))
        except ValidationError:
            payload = None
            continue

        payload = candidate
        break

    if payload is None:
        return _failure_result()

    return ReasoningResult(**_validated_kwargs(payload))
