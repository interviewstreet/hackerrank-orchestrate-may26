"""Provider-agnostic LLM client. Anthropic primary, OpenAI fallback.

Structured output via tool/function calling on both sides — same JSON schema,
same parsed Pydantic LLMOutput.
"""
from __future__ import annotations

import json
import os
import sys

from schemas import LLMOutput

TOOL_NAME = "emit_triage"
TOOL_DESCRIPTION = "Emit the triage decision for the support ticket."
TOOL_INPUT_SCHEMA: dict = {
    "type": "object",
    "required": ["status", "product_area", "response", "justification",
                 "request_type", "citations", "confidence"],
    "properties": {
        "status": {"type": "string", "enum": ["replied", "escalated"]},
        "product_area": {"type": "string"},
        "response": {"type": "string"},
        "justification": {"type": "string"},
        "request_type": {
            "type": "string",
            "enum": ["product_issue", "feature_request", "bug", "invalid"],
        },
        "citations": {"type": "array", "items": {"type": "string"}},
        "confidence": {"type": "number", "minimum": 0.0, "maximum": 1.0},
    },
}


class LLMError(Exception):
    """Raised when an LLM provider call fails or returns unparseable output."""


# ---------- Anthropic ----------

def _call_anthropic(system: str, user: str, model: str,
                    max_tokens: int, max_retries: int) -> LLMOutput:
    try:
        from anthropic import Anthropic
    except ImportError as e:
        raise LLMError(f"anthropic package not installed: {e}") from e

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise LLMError("ANTHROPIC_API_KEY not set")

    client = Anthropic(api_key=api_key)
    tool = {
        "name": TOOL_NAME,
        "description": TOOL_DESCRIPTION,
        "input_schema": TOOL_INPUT_SCHEMA,
    }

    last_err: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            resp = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=0,
                system=system,
                tools=[tool],
                tool_choice={"type": "tool", "name": TOOL_NAME},
                messages=[{"role": "user", "content": user}],
            )
            for block in resp.content:
                if getattr(block, "type", None) == "tool_use":
                    payload = block.input
                    if isinstance(payload, str):
                        payload = json.loads(payload)
                    return LLMOutput(**payload)
            raise LLMError("anthropic: no tool_use block")
        except Exception as e:  # noqa: BLE001
            last_err = e
            if attempt >= max_retries:
                break
    raise LLMError(f"anthropic call failed: {last_err}")


# ---------- OpenAI ----------

def _call_openai(system: str, user: str, model: str,
                 max_tokens: int, max_retries: int) -> LLMOutput:
    try:
        from openai import OpenAI
    except ImportError as e:
        raise LLMError(f"openai package not installed: {e}") from e

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise LLMError("OPENAI_API_KEY not set")

    client = OpenAI(api_key=api_key)
    tool = {
        "type": "function",
        "function": {
            "name": TOOL_NAME,
            "description": TOOL_DESCRIPTION,
            "parameters": TOOL_INPUT_SCHEMA,
        },
    }

    last_err: Exception | None = None
    for attempt in range(max_retries + 1):
        try:
            resp = client.chat.completions.create(
                model=model,
                temperature=0,
                seed=42,
                max_tokens=max_tokens,
                tools=[tool],
                tool_choice={"type": "function",
                             "function": {"name": TOOL_NAME}},
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
            choice = resp.choices[0]
            calls = choice.message.tool_calls or []
            if not calls:
                raise LLMError("openai: no tool_calls in response")
            args = calls[0].function.arguments
            payload = json.loads(args) if isinstance(args, str) else args
            return LLMOutput(**payload)
        except Exception as e:  # noqa: BLE001
            last_err = e
            if attempt >= max_retries:
                break
    raise LLMError(f"openai call failed: {last_err}")


# ---------- Public API ----------

def call_llm(system: str, user: str,
             provider: str = "auto",
             model: str | None = None,
             openai_model: str | None = None,
             max_tokens: int = 1024,
             max_retries: int = 1) -> LLMOutput:
    """Call the configured LLM provider with auto-fallback.

    provider:
      - "anthropic": Anthropic only.
      - "openai":    OpenAI only.
      - "auto":      Try Anthropic; on failure or missing key, fall back to OpenAI.
    """
    provider = (provider or "auto").lower()
    anth_model = model or os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
    oai_model = openai_model or os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    if provider == "anthropic":
        return _call_anthropic(system, user, anth_model, max_tokens, max_retries)
    if provider == "openai":
        return _call_openai(system, user, oai_model, max_tokens, max_retries)

    # auto
    try:
        return _call_anthropic(system, user, anth_model, max_tokens, max_retries)
    except LLMError as e:
        if not os.environ.get("OPENAI_API_KEY"):
            raise e
        print(f"[llm] anthropic unavailable ({e}); falling back to openai",
              file=sys.stderr)
        return _call_openai(system, user, oai_model, max_tokens, max_retries)
