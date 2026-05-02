"""
Verifier — post-generation quality gate using Gemini Flash Lite.
Only called when Anchor returns grounded=true.
Checks whether the response actually addresses what the customer asked.
"""

import sys

from model_client import ModelClient, ModelClientError

MODEL = "google/gemini-2.5-flash-lite"
# Sentinel + Anchor's grounding self-check already filter heavily upstream, so
# Verifier's role is to reject responses that are clearly off-topic, not to
# re-litigate borderline-helpful answers. 0.50 keeps clear failures escalated
# while letting "probably helpful" responses through.
CONFIDENCE_THRESHOLD = 0.50

_SYSTEM_PROMPT = """You are Verifier, a quality-assurance judge for support ticket responses.

You receive a customer's sub-request and a proposed response. Your job is to answer:
"Does this response actually address what the customer asked?"

## What to check

1. Issue coverage: Does the response address all parts of the sub-request?
2. Actionability: Does the response give the customer something they can actually do?
3. Accuracy fit: Does the response make sense in context of the specific issue, not just the topic?

## What NOT to do

- Do not re-classify the ticket.
- Do not make escalation decisions.
- Do not retrieve additional corpus content.
- Do not rewrite or improve the response — only approve or reject it.

## Output schema (JSON only, no other text)

{
  "verified": true | false,
  "verification_confidence": <float between 0.0 and 1.0>,
  "verification_reason": "<one sentence explaining your decision>"
}

Be conservative on responses that are flatly wrong or off-topic, but allow responses
that are clearly relevant and on-topic even if not exhaustive. The threshold for
approval is confidence >= 0.50."""


def verify(
    request_id: str,
    issue_excerpt: str,
    response: str,
    source_doc: str,
    client: ModelClient,
) -> dict:
    """
    Returns {"verified": bool, "verification_confidence": float, "verification_reason": str}.
    Defaults to verified=false on failure (safe direction = escalate).
    """
    user_content = (
        f"Customer sub-request: {issue_excerpt}\n\n"
        f"Proposed response (source: {source_doc}):\n{response}"
    )
    messages = [
        {"role": "system", "content": _SYSTEM_PROMPT},
        {"role": "user", "content": user_content},
    ]

    try:
        result = client.complete_with_retry(
            model=MODEL,
            messages=messages,
            temperature=0.0,
        )
    except ModelClientError:
        print(f"[{request_id}] Verifier: api_error → verified=false → escalated", file=sys.stderr)
        return _unverified(request_id)

    if not isinstance(result, dict):
        print(f"[{request_id}] Verifier: json_parse_error → verified=false → escalated", file=sys.stderr)
        return _unverified(request_id)

    confidence = result.get("verification_confidence")
    if confidence is None:
        print(f"[{request_id}] Verifier: missing confidence → verified=false → escalated", file=sys.stderr)
        return _unverified(request_id)

    try:
        confidence = float(confidence)
    except (TypeError, ValueError):
        confidence = 0.0

    verified = bool(result.get("verified", False)) and confidence >= CONFIDENCE_THRESHOLD
    reason = str(result.get("verification_reason") or "")

    if not verified:
        print(
            f"[{request_id}] Verifier: verified=false (confidence={confidence:.2f}) → escalated",
            file=sys.stderr,
        )

    return {
        "verified": verified,
        "verification_confidence": confidence,
        "verification_reason": reason,
    }


def _unverified(request_id: str) -> dict:
    return {
        "verified": False,
        "verification_confidence": 0.0,
        "verification_reason": f"Verifier could not assess response [{request_id}].",
    }
