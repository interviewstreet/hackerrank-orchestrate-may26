"""Tests for code/reasoner.py — Iter 4 (grounded response generator).

Uses a fake Anthropic client (injected via the ``client`` parameter) so no
network is required.

PRD references: FR-030..FR-035, R-1.
Architecture references: section 3.8.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import pytest

from preprocessor import clean
from reasoner import reason
from schemas import ReasoningResult, RetrievedDoc, Ticket


# ---------- fake Anthropic client (mirrors test_classifier_schema) ----------


@dataclass
class _FakeContentBlock:
    type: str
    name: str = ""
    input: dict = field(default_factory=dict)


@dataclass
class _FakeResponse:
    content: list[_FakeContentBlock]
    stop_reason: str = "tool_use"


class FakeAnthropicClient:
    def __init__(self, queue: list) -> None:
        self.queue = list(queue)
        self.calls: list[dict[str, Any]] = []
        self.messages = self

    def create(self, **kwargs: Any) -> _FakeResponse:
        self.calls.append(kwargs)
        if not self.queue:
            raise RuntimeError("FakeAnthropicClient: queue exhausted")
        item = self.queue.pop(0)
        if isinstance(item, Exception):
            raise item
        if isinstance(item, dict):
            return _FakeResponse(
                content=[_FakeContentBlock(type="tool_use", name="emit_response", input=item)]
            )
        return _FakeResponse(
            content=[_FakeContentBlock(type="text", input={"text": str(item)})],
            stop_reason="end_turn",
        )


def _doc(text: str, *, file_path: str = "data/visa/sample.md", domain: str = "visa") -> RetrievedDoc:
    return RetrievedDoc(
        chunk_id=file_path + "#0",
        file_path=file_path,
        domain=domain,  # type: ignore[arg-type]
        breadcrumbs=["root"],
        title="sample",
        text=text,
        cosine_score=0.85,
        bm25_score=1.0,
        rrf_score=0.4,
    )


def _cleaned(issue: str = "How do I cancel a test invite for a candidate?", subject: str = "Cancel invite"):
    return clean(Ticket(index=0, issue=issue, subject=subject, company="HackerRank"))


def _valid_reasoning_payload(**overrides: Any) -> dict[str, Any]:
    base = {
        "can_answer_from_corpus": True,
        "response": "Open the test settings, find the candidate, and cancel the invite.",
        "citations": ["data/hackerrank/screen/test-cancel.md"],
        "justification": "Answer drawn from HackerRank Screen test-settings article.",
    }
    base.update(overrides)
    return base


# ---------- happy path ------------------------------------------------------


def test_reason_returns_validated_reasoning_result() -> None:
    fake = FakeAnthropicClient([_valid_reasoning_payload()])
    chunks = [_doc("Open test settings to cancel an invite.", file_path="data/hackerrank/screen/test-cancel.md", domain="hackerrank")]
    result = reason(_cleaned(), chunks, client=fake)
    assert isinstance(result, ReasoningResult)
    assert result.can_answer_from_corpus is True
    assert result.response
    assert result.citations


def test_reason_calls_llm_with_temperature_zero_and_pinned_model() -> None:
    fake = FakeAnthropicClient([_valid_reasoning_payload()])
    chunks = [_doc("Cancel invite via test settings.", file_path="data/hackerrank/screen/test-cancel.md", domain="hackerrank")]
    reason(_cleaned(), chunks, client=fake)
    assert len(fake.calls) == 1
    call = fake.calls[0]
    assert call["temperature"] == 0.0
    assert "claude-sonnet-4-5" in call["model"]


def test_reason_passes_mandatory_tool_choice() -> None:
    fake = FakeAnthropicClient([_valid_reasoning_payload()])
    chunks = [_doc("Cancel invite via test settings.", file_path="data/hackerrank/screen/test-cancel.md", domain="hackerrank")]
    reason(_cleaned(), chunks, client=fake)
    call = fake.calls[0]
    assert call.get("tools")
    tool_choice = call.get("tool_choice", {})
    assert tool_choice.get("type") in {"tool", "any"}


def test_reason_emits_citations_subset_of_retrieved_paths() -> None:
    """When the LLM cites paths, only paths from the retrieved set survive."""
    fake = FakeAnthropicClient([
        _valid_reasoning_payload(citations=[
            "data/hackerrank/screen/test-cancel.md",     # in retrieved
            "data/visa/fraud-handbook.md",               # NOT retrieved
        ])
    ])
    chunks = [_doc("Cancel invite from settings.", file_path="data/hackerrank/screen/test-cancel.md", domain="hackerrank")]
    result = reason(_cleaned(), chunks, client=fake)
    assert "data/hackerrank/screen/test-cancel.md" in result.citations
    assert "data/visa/fraud-handbook.md" not in result.citations


# ---------- can_answer_from_corpus=False ------------------------------------


def test_reason_can_answer_false_with_unrelated_chunks() -> None:
    fake = FakeAnthropicClient([
        _valid_reasoning_payload(
            can_answer_from_corpus=False,
            response="I do not have enough information from the support corpus to answer this.",
            citations=[],
            justification="Retrieved chunks are not relevant to the request.",
        )
    ])
    chunks = [_doc("Visa fraud reporting line is 1-800-847-2911.", file_path="data/visa/fraud.md", domain="visa")]
    result = reason(_cleaned(issue="How do I cancel a test invite?"), chunks, client=fake)
    assert result.can_answer_from_corpus is False


def test_reason_skips_llm_when_no_chunks_retrieved() -> None:
    """No retrieved chunks → return can_answer_from_corpus=False without an LLM call."""
    fake = FakeAnthropicClient([])
    result = reason(_cleaned(), [], client=fake)
    assert result.can_answer_from_corpus is False
    assert result.citations == []
    assert len(fake.calls) == 0


# ---------- retry behavior --------------------------------------------------


def test_reason_retries_once_on_pydantic_failure_then_succeeds() -> None:
    fake = FakeAnthropicClient([
        "garbage non tool_use response",
        _valid_reasoning_payload(),
    ])
    chunks = [_doc("Cancel via settings.", file_path="data/hackerrank/screen/test-cancel.md", domain="hackerrank")]
    result = reason(_cleaned(), chunks, client=fake)
    assert isinstance(result, ReasoningResult)
    assert len(fake.calls) == 2


def test_reason_two_failures_returns_can_answer_false() -> None:
    fake = FakeAnthropicClient(["fail one", "fail two"])
    chunks = [_doc("Cancel via settings.", file_path="data/hackerrank/screen/test-cancel.md", domain="hackerrank")]
    result = reason(_cleaned(), chunks, client=fake)
    assert result.can_answer_from_corpus is False
    assert len(fake.calls) == 2


# ---------- prompt safety ----------------------------------------------------


def test_reason_user_message_does_not_echo_system_prompt() -> None:
    """The user message we send to the LLM must contain the ticket but
    must NOT contain our system instructions verbatim — otherwise we
    risk leaking them via the response."""
    fake = FakeAnthropicClient([_valid_reasoning_payload()])
    chunks = [_doc("Cancel via settings.", file_path="data/hackerrank/screen/test-cancel.md", domain="hackerrank")]
    reason(_cleaned(), chunks, client=fake)
    call = fake.calls[0]
    user_msgs = call.get("messages", [])
    assert user_msgs, "Expected a user message"
    user_text = user_msgs[0]["content"]
    system_text = call.get("system", "")
    # system prompt should not be embedded in the user-role content
    assert system_text not in user_text or system_text == ""


def test_reason_passes_chunks_with_file_paths_in_user_message() -> None:
    """Each retrieved chunk's file_path should be visible to the LLM so it
    can cite correctly."""
    fake = FakeAnthropicClient([_valid_reasoning_payload()])
    chunks = [
        _doc("Cancel invite via settings.", file_path="data/hackerrank/screen/test-cancel.md", domain="hackerrank"),
        _doc("Reset password from profile.", file_path="data/hackerrank/settings/reset.md", domain="hackerrank"),
    ]
    reason(_cleaned(), chunks, client=fake)
    user_text = fake.calls[0]["messages"][0]["content"]
    assert "data/hackerrank/screen/test-cancel.md" in user_text
    assert "data/hackerrank/settings/reset.md" in user_text
