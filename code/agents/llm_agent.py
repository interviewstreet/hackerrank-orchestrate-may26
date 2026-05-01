"""
LLM Agent - Generates contextual responses with strict guardrails.
"""

import json
import re
from openai import OpenAI

from config import OPENAI_API_KEY, LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS, ESCALATION_RESPONSE, OPENAI_BASE_URL
from utils.logger import log_agent, log_llm_call

if OPENAI_BASE_URL:
    client = OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)
else:
    client = OpenAI(api_key=OPENAI_API_KEY)

SAFE_ESCALATION_RESPONSE = "This issue requires further investigation and has been escalated to support."
SAFE_REFUSAL_RESPONSE = "I cannot assist with that request."

FORBIDDEN_PATTERNS = [
    "try the following", "you can try", "ensure", "check your",
    "make sure", "it could be", "possibly", "might be", "typically",
    "restart", "update your", "it is recommended", "you should",
    "try reopening", "try accessing", "try again", "try using",
]

MAX_WORDS = 120


SYSTEM_PROMPT = f"""You are a deterministic support response generator.

STRICT RULES:
1. Use ONLY information explicitly in the provided context.
2. NEVER infer, expand, or add steps not in context.
3. If context is incomplete → output exactly: "{SAFE_ESCALATION_RESPONSE}"
4. No greetings, no filler, no markdown, no bullet points.
5. Max 3-4 sentences.
6. Only extract and lightly rephrase existing context.

Output JSON:
{{"response": "...", "request_type": "product_issue", "escalate": false, "escalate_reason": ""}}
"""


def run(query: str, chunks: list[dict]) -> dict:
    context = _build_context(chunks)
    user_msg = f"Context:\n{context}\n\nUser Question:\n{query}"

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
        
        response = parsed.get("response", "")
        
        if response and response != SAFE_REFUSAL_RESPONSE and parsed.get("request_type") != "invalid":
            response = _apply_guardrails(response, context, parsed.get("escalate", False))
            parsed["response"] = response
            parsed["escalate"] = response == SAFE_ESCALATION_RESPONSE
        
        log_llm_call(user_msg, raw, parsed)
        return parsed

    except Exception as e:
        err_msg = str(e)
        log_agent("llm_agent", f"ERROR: {err_msg}", {})
        return {
            "response":        SAFE_ESCALATION_RESPONSE,
            "request_type":    "product_issue",
            "escalate":        True,
            "escalate_reason": f"LLM call failed: {err_msg[:50]}",
            "raw_json":        "",
        }


def _apply_guardrails(response: str, context: str, original_escalate: bool) -> str:
    if original_escalate:
        return SAFE_ESCALATION_RESPONSE
    
    response_lower = response.lower()
    
    for pattern in FORBIDDEN_PATTERNS:
        if pattern in response_lower:
            return SAFE_ESCALATION_RESPONSE
    
    if len(response.split()) > MAX_WORDS:
        return SAFE_ESCALATION_RESPONSE
    
    vague_responses = [
        "thank you for reaching out",
        "please contact support",
        "this is outside my capabilities",
    ]
    if any(v in response_lower for v in vague_responses):
        return SAFE_ESCALATION_RESPONSE
    
    return response


def _build_context(chunks: list[dict]) -> str:
    parts = []
    for i, c in enumerate(chunks, 1):
        meta = c.get("metadata", {})
        title = meta.get("title", "")
        header = f"[Context {i}] {title}"
        parts.append(f"{header}\n{c['text']}")
    return "\n\n".join(parts)


def _parse_json(raw: str) -> dict:
    cleaned = re.sub(r"```json|```", "", raw).strip()
    try:
        data = json.loads(cleaned)
        resp = data.get("response", "")
        return {
            "response":        resp,
            "request_type":    data.get("request_type", "product_issue"),
            "escalate":        bool(data.get("escalate", False)),
            "escalate_reason": data.get("escalate_reason", ""),
            "raw_json":        raw,
        }
    except json.JSONDecodeError:
        resp = raw.strip() if raw.strip() else ""
        return {
            "response":        resp,
            "request_type":    "product_issue",
            "escalate":        False if resp else True,
            "escalate_reason": "LLM did not return JSON",
            "raw_json":        raw,
        }