"""
LLM Agent
Single call: generates response + classifies request_type.
Strict RAG — only uses provided context chunks.
Returns structured JSON.
"""

import json
import re
from openai import OpenAI

from config import OPENAI_API_KEY, LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS, ESCALATION_RESPONSE
from utils.logger import log_agent, log_llm_call

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """You are a strict support assistant. Your ONLY job is to answer support tickets using the provided context passages.

RULES (non-negotiable):
1. Answer ONLY from the context below. Do not use any outside knowledge.
2. If the context does not contain enough information to answer, set escalate=true.
3. Never guess, infer, or extrapolate beyond what the context explicitly states.
4. Be concise and helpful. Write the response as if speaking directly to the user.
5. Classify request_type honestly based on what the user is asking.

OUTPUT: You must return ONLY valid JSON in this exact schema, no other text:
{
  "response": "your user-facing answer here",
  "request_type": "product_issue | feature_request | bug | invalid",
  "escalate": false,
  "escalate_reason": ""
}

request_type definitions:
- product_issue: user cannot do something, needs help with a feature
- feature_request: user wants something that doesn't exist yet
- bug: user reports something is broken / not working as expected
- invalid: ticket is spam, irrelevant, or not a real support request
"""


def run(query: str, chunks: list[dict]) -> dict:
    """
    Returns:
    {
      response, request_type, escalate (bool), escalate_reason,
      raw_json (str)
    }
    """
    context = _build_context(chunks)
    user_msg = f"Context passages:\n{context}\n\nUser ticket:\n{query}"

    try:
        resp = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=LLM_MAX_TOKENS,
            temperature=LLM_TEMPERATURE,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg}
            ],
        )
        raw = resp.choices[0].message.content.strip()
        parsed = _parse_json(raw)
        log_llm_call(user_msg, raw, parsed)
        return parsed

    except Exception as e:
        log_agent("llm_agent", f"ERROR: {e}", {})
        return {
            "response":        ESCALATION_RESPONSE,
            "request_type":    "product_issue",
            "escalate":        True,
            "escalate_reason": f"LLM call failed: {e}",
            "raw_json":        "",
        }


def _build_context(chunks: list[dict]) -> str:
    parts = []
    for i, c in enumerate(chunks, 1):
        meta  = c.get("metadata", {})
        title = meta.get("title", "")
        url   = meta.get("source_url", "")
        score = c.get("score", 0)
        header = f"[Passage {i}] {title} (score={score:.3f}, source={url})"
        parts.append(f"{header}\n{c['text']}")
    return "\n\n---\n\n".join(parts)


def _parse_json(raw: str) -> dict:
    # Strip markdown fences if present
    cleaned = re.sub(r"```json|```", "", raw).strip()
    try:
        data = json.loads(cleaned)
        return {
            "response":        data.get("response", ESCALATION_RESPONSE),
            "request_type":    data.get("request_type", "product_issue"),
            "escalate":        bool(data.get("escalate", False)),
            "escalate_reason": data.get("escalate_reason", ""),
            "raw_json":        raw,
        }
    except json.JSONDecodeError:
        return {
            "response":        ESCALATION_RESPONSE,
            "request_type":    "product_issue",
            "escalate":        True,
            "escalate_reason": f"LLM returned non-JSON output: {raw[:100]}",
            "raw_json":        raw,
        }