"""
Justification builder with standard structure.
"""

import re
from config import OPENAI_API_KEY, LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS, RETRIEVAL_THRESHOLD


def _deterministic_base(
    domain: str,
    router_meta: dict | None,
    retrieval_score: float | None,
    retrieval_threshold: float,
    safety_trigger: str | None,
    escalated: bool,
    escalation_reason: str | None,
    request_type: str = "product_issue",
    product_area: str = "unknown",
    chunks_exist: bool = True,
) -> str:
    parts = []

    if request_type == "invalid":
        parts.append("Request classified as invalid.")
        parts.append("Query outside supported domains.")

    if router_meta:
        method = str(router_meta.get("method", "unknown")).lower()
        if method == "company_field":
            parts.append(f"Routed to {domain} via company field.")
        elif method == "keyword":
            parts.append(f"Routed to {domain} via keyword match.")
        elif method == "llm_fallback":
            parts.append(f"Routed to {domain} via LLM fallback.")
        elif method == "injection_detect":
            parts.append("Routed to unknown due to injection detection.")
        elif method == "no_match":
            parts.append("Routed to unknown via no_match.")
        else:
            parts.append(f"Routed to {domain} via {method}.")
    else:
        parts.append("Routed to unknown.")

    if retrieval_score is None:
        parts.append("Top retrieval score: none.")
    else:
        parts.append(f"Top retrieval score={retrieval_score:.3f}.")

    grounded = retrieval_score is not None and retrieval_score >= retrieval_threshold
    parts.append("Grounding: PASS." if grounded else "Grounding: FAIL.")

    safety = "PASS" if not safety_trigger or safety_trigger == "low" else "FLAG"
    parts.append(f"Safety: {safety}.")

    final_status = "escalated" if escalated and request_type != "invalid" else "replied"
    parts.append(f"Final decision: {final_status}.")

    if escalation_reason:
        parts.append(f"Reason: {escalation_reason}.")

    return " ".join(parts)


def refine_justification_with_llm(base_justification: str) -> str:
    return base_justification


def build_justification(
    domain: str,
    router_meta: dict | None,
    retrieval_score: float | None,
    retrieval_threshold: float,
    safety_trigger: str | None,
    escalated: bool,
    escalation_reason: str | None,
    request_type: str = "product_issue",
    product_area: str = "unknown",
    chunks_exist: bool = True,
) -> str:
    base = _deterministic_base(
        domain,
        router_meta,
        retrieval_score,
        retrieval_threshold,
        safety_trigger,
        escalated,
        escalation_reason,
        request_type,
        product_area,
        chunks_exist,
    )
    return base