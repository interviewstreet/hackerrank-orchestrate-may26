"""Anthropic client with tool-forced JSON structured output."""
from __future__ import annotations

import json
import os

from schemas import LLMOutput

TOOL_SCHEMA = {
    "name": "emit_triage",
    "description": "Emit the triage decision for the support ticket.",
    "input_schema": {
        "type": "object",
        "required": ["status", "product_area", "response", "justification",
                     "request_type", "citations", "confidence"],
        "properties": {
            "status": {"type": "string", "enum": ["replied", "escalated"]},
            "product_area": {"type": "string"},
            "response": {"type": "string"},
            "justification": {"type": "string"},
            "request_type": {"type": "string",
                             "enum": ["product_issue", "feature_request",
                                      "bug", "invalid"]},
            "citations": {"type": "array", "items": {"type": "string"}},
            "confidence": {"type": "number", "minimum": 0.0, "maximum": 1.0},
        },
    },
}


class LLMError(Exception):
    pass


def call_llm(system: str, user: str, model: str,
             max_tokens: int = 1024, max_retries: int = 1) -> LLMOutput:
    try:
        from anthropic import Anthropic
    except ImportError as e:  # pragma: no cover
        raise LLMError("anthropic package not installed") from e

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise LLMError("ANTHROPIC_API_KEY not set")

    client = Anthropic(api_key=api_key)

    last_err: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            resp = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=0,
                system=system,
                tools=[TOOL_SCHEMA],
                tool_choice={"type": "tool", "name": "emit_triage"},
                messages=[{"role": "user", "content": user}],
            )
            for block in resp.content:
                if getattr(block, "type", None) == "tool_use":
                    payload = block.input
                    if isinstance(payload, str):
                        payload = json.loads(payload)
                    return LLMOutput(**payload)
            raise LLMError("no tool_use block in response")
        except Exception as e:  # noqa: BLE001
            last_err = e
            if attempt >= max_retries:
                break
    raise LLMError(f"LLM call failed: {last_err}")
