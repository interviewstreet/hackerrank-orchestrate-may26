"""
ModelClient — thin abstraction over OpenRouter (default) or local backends.
All LLM pipeline calls flow through this module.
"""

import json
import os
import re
import time

from openai import OpenAI


class ModelClientError(Exception):
    pass


class ModelClient:
    def __init__(self):
        backend = os.environ.get("MODEL_BACKEND", "openrouter")
        if backend == "openrouter":
            api_key = os.environ.get("OPENROUTER_API_KEY")
            if not api_key:
                raise ModelClientError(
                    "OPENROUTER_API_KEY environment variable not set.\n"
                    "Set it in .env and re-run: cp .env.example .env && nano .env"
                )
            base_url = "https://openrouter.ai/api/v1"
        elif backend == "local_ollama":
            api_key = "ollama"
            base_url = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434/v1")
        elif backend == "local_vllm":
            api_key = "vllm"
            base_url = os.environ.get("VLLM_BASE_URL", "http://localhost:8000/v1")
        else:
            raise ModelClientError(f"Unknown MODEL_BACKEND: {backend}")

        self._client = OpenAI(api_key=api_key, base_url=base_url)
        self.backend = backend

    def complete(
        self,
        model: str,
        messages: list[dict],
        temperature: float = 0.0,
        response_format: dict | None = None,
        extra_body: dict | None = None,
    ) -> dict:
        """
        Call the LLM once. Returns parsed JSON dict.
        Raises ModelClientError on API failure (caller owns retry logic).
        """
        kwargs: dict = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }
        if response_format is not None:
            kwargs["response_format"] = response_format
        if extra_body is not None:
            kwargs["extra_body"] = extra_body

        try:
            response = self._client.chat.completions.create(**kwargs)
        except Exception as exc:
            raise ModelClientError(str(exc)) from exc

        content = response.choices[0].message.content or ""
        return _parse_json(content)

    def complete_with_retry(
        self,
        model: str,
        messages: list[dict],
        temperature: float = 0.0,
        response_format: dict | None = None,
        extra_body: dict | None = None,
    ) -> dict:
        """
        Attempt the call; on failure wait 2 s and retry once.
        Raises ModelClientError if both attempts fail.
        """
        last_exc: Exception | None = None
        for attempt in range(2):
            try:
                return self.complete(model, messages, temperature, response_format, extra_body)
            except ModelClientError as exc:
                last_exc = exc
                if attempt == 0:
                    msg = str(exc).lower()
                    if "429" in msg or "rate limit" in msg:
                        wait = _parse_retry_after(str(exc))
                        time.sleep(wait)
                    else:
                        time.sleep(2)
        raise ModelClientError(f"Both attempts failed: {last_exc}") from last_exc


def _parse_retry_after(error_text: str) -> float:
    match = re.search(r"retry.after[:\s]+(\d+)", error_text, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return 60.0


def _parse_json(content: str) -> dict:
    content = content.strip()
    # Strip markdown fences
    if content.startswith("```"):
        lines = content.splitlines()
        inner = []
        inside = False
        for line in lines:
            if line.startswith("```") and not inside:
                inside = True
                continue
            if line.startswith("```") and inside:
                break
            if inside:
                inner.append(line)
        content = "\n".join(inner).strip()
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        pass
    # Best-effort: extract first {...} block
    match = re.search(r"\{.*\}", content, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return {}
