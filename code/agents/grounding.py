"""
Grounding validator.
Ensures the retrieved chunks are relevant enough to justify calling the LLM.
"""

from config import RETRIEVAL_THRESHOLD
from utils.logger import log_agent


def run(chunks: list[dict], query: str) -> dict | None:
    if not chunks:
        log_agent("grounding", "ESCALATE — no retrieved chunks", {})
        return _escalate("low", "No retrieval context available.")

    top_score = float(chunks[0].get("score", 0))
    if top_score < RETRIEVAL_THRESHOLD:
        log_agent("grounding", "ESCALATE — low confidence retrieval", {"top_score": top_score})
        return _escalate(
            "low",
            f"Insufficient grounding (score={top_score:.3f} < threshold={RETRIEVAL_THRESHOLD:.3f}).",
        )

    log_agent("grounding", "PASS — grounded context", {"top_score": top_score})

    return None


def _escalate(rule: str, reason: str) -> dict:
    return {
        "status": "escalated",
        "request_type": "product_issue",
        "product_area": "unknown",
        "response": "This issue requires further investigation and has been escalated to support.",
        "justification": f"[{rule}] {reason}",
        "rule_triggered": rule,
    }