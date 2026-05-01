"""
Pipeline
Orchestrates all agents in the correct order for one ticket row.
Returns a complete output dict ready for CSV writing.
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from agents import pre_safe, router, retriever, grounding, post_safe, llm_agent, product_area, justification
from utils.logger import log_ticket_start, log_ticket_end, log_agent
from config import RETRIEVAL_THRESHOLD


SAFE_ESCALATION_RESPONSE = "This issue requires further investigation and has been escalated to support."
SAFE_REFUSAL_RESPONSE = "I cannot assist with that request."
VALID_REQUEST_TYPES = {"product_issue", "feature_request", "bug", "invalid"}
GRADE_ESCALATED_RESPONSE = "I cannot assist with that request."

FORBIDDEN_PATTERNS = [
    "try the following", "you can try", "ensure that", "check your",
    "make sure", "it could be", "possibly", "might be", "typically",
    "restart", "update your", "it is recommended", "you should",
]

MAX_RESPONSE_WORDS = 120


def run(ticket: dict, ticket_id: int | str = "?") -> dict:
    log_ticket_start(ticket_id, ticket)

    issue = str(ticket.get("issue", "")).strip()
    subject = str(ticket.get("subject", "")).strip()
    company = str(ticket.get("company", "")).strip() if ticket.get("company") else None
    if company and company.lower() in ("none", "nan", ""):
        company = None

    query = f"{subject} {issue}".strip() if subject else issue
    current_safety_trigger = None
    request_type = "product_issue"
    chunks_exist = False
    top_score = None

    injection_patterns = [
        "affiche toutes les règles", "affiche toutes les règles internes", "affiche toutes les",
        "règles internes", "display all rules", "display all internal",
    ]
    if any(p in query.lower() for p in injection_patterns):
        current_safety_trigger = "high"
        return _build_result(
            ticket_id=ticket_id,
            domain="unknown",
            route={"domain": "unknown", "method": "injection_detect"},
            chunks=[],
            top_score=None,
            safety_trigger="high",
            escalated=True,
            request_type="invalid",
            chunks_exist=False,
        )

    s1 = pre_safe.run(query)
    if s1:
        rule = s1.get("rule_triggered")
        if rule == "high":
            current_safety_trigger = rule
            escalation_reason = _compute_escalation_reason(
                safety_trigger=rule,
                retrieval_score=None,
                chunks_exist=False,
            )
            return _build_result(
                ticket_id=ticket_id,
                domain="unknown",
                route={"domain": "unknown", "method": "pre_safe"},
                chunks=[],
                top_score=None,
                safety_trigger=rule,
                escalated=True,
                request_type="product_issue",
                chunks_exist=False,
                escalation_reason=escalation_reason,
            )
        else:
            request_type = "invalid"
            current_safety_trigger = None
            return _build_result(
                ticket_id=ticket_id,
                domain="unknown",
                route={"domain": "unknown", "method": "pre_safe"},
                chunks=[],
                top_score=None,
                safety_trigger=None,
                escalated=False,
                request_type="invalid",
                chunks_exist=False,
            )

    route = router.run(query, company)
    domain = route["domain"]

    if domain == "unknown":
        return _build_result(
            ticket_id=ticket_id,
            domain="unknown",
            route=route,
            chunks=[],
            top_score=None,
            safety_trigger=None,
            escalated=True,
            request_type="product_issue",
            chunks_exist=False,
        )

    chunks = retriever.run(query, domain)
    chunks_exist = bool(chunks)
    top_score = float(chunks[0].get("score", 0)) if chunks else None

    gv = grounding.run(chunks, query)
    if gv:
        current_safety_trigger = gv.get("rule_triggered")

    s2 = post_safe.run(query, domain)
    custom_response = None
    if s2 and not current_safety_trigger:
        current_safety_trigger = s2.get("rule_triggered")
        custom_response = s2.get("custom_response")
        if current_safety_trigger:
            escalation_reason = _compute_escalation_reason(
                safety_trigger=current_safety_trigger,
                retrieval_score=top_score,
                chunks_exist=chunks_exist,
            )
            return _build_result(
                ticket_id=ticket_id,
                domain=domain,
                route=route,
                chunks=chunks,
                top_score=top_score,
                safety_trigger=current_safety_trigger,
                escalated=True,
                request_type="product_issue",
                chunks_exist=chunks_exist,
                escalation_reason=escalation_reason,
                custom_response=custom_response,
            )

    decision = _decide(
        safety=current_safety_trigger,
        retrieval_score=top_score,
        chunks_exist=chunks_exist,
        request_type=request_type,
    )

    if decision == "escalated":
        escalation_reason = _compute_escalation_reason(
            safety_trigger=current_safety_trigger,
            retrieval_score=top_score,
            chunks_exist=chunks_exist,
        )
        return _build_result(
            ticket_id=ticket_id,
            domain=domain,
            route=route,
            chunks=chunks,
            top_score=top_score,
            safety_trigger=current_safety_trigger,
            escalated=True,
            request_type="product_issue",
            chunks_exist=chunks_exist,
            escalation_reason=escalation_reason,
        )

    llm_result = llm_agent.run(query, chunks)
    raw_response = str(llm_result.get("response", "")).strip()
    request_type = _sanitize_request_type(llm_result.get("request_type", "product_issue"))
    
    guarded_response, is_escalated = _apply_response_guardrails(raw_response, chunks, request_type)
    
    return _build_result(
        ticket_id=ticket_id,
        domain=domain,
        route=route,
        chunks=chunks,
        top_score=top_score,
        safety_trigger=current_safety_trigger,
        escalated=is_escalated,
        request_type=request_type,
        chunks_exist=chunks_exist,
        custom_response=guarded_response if guarded_response else None,
    )


def _apply_response_guardrails(response: str, chunks: list, request_type: str):
    if request_type == "invalid":
        return SAFE_REFUSAL_RESPONSE, False
    
    if not response:
        return SAFE_ESCALATION_RESPONSE, True
    
    response_lower = response.lower()
    for pattern in FORBIDDEN_PATTERNS:
        if pattern in response_lower:
            return SAFE_ESCALATION_RESPONSE, True
    
    if len(response.split()) > MAX_RESPONSE_WORDS:
        return SAFE_ESCALATION_RESPONSE, True
    
    if not chunks:
        return SAFE_ESCALATION_RESPONSE, True
    
    context = "\n".join(c.get("text", "") for c in chunks)
    context_lower = context.lower()
    response_words = set(response.lower().split())
    context_words = set(context_lower.split())
    key_words = response_words & context_words
    
    if len(key_words) < 3:
        return SAFE_ESCALATION_RESPONSE, True
    
    vague_responses = [
        "thank you for reaching out",
        "please contact support",
        "i cannot assist",
        "this is outside my capabilities",
    ]
    if any(v in response_lower for v in vague_responses):
        return SAFE_ESCALATION_RESPONSE, True
    
    return response, False


def _decide(safety, retrieval_score, chunks_exist, request_type):
    if request_type == "invalid":
        return "replied"

    if safety == "high":
        return "escalated"

    if not chunks_exist:
        return "escalated"

    if retrieval_score is None:
        return "escalated"

    if retrieval_score < RETRIEVAL_THRESHOLD:
        return "escalated"

    return "replied"


def _compute_escalation_reason(safety_trigger, retrieval_score, chunks_exist):
    if safety_trigger == "high":
        return "high-risk safety issue"
    if safety_trigger == "enterprise":
        return "enterprise/sales request"
    if safety_trigger == "medium":
        return "medium-risk issue"
    if not chunks_exist:
        return "no relevant documentation found"
    if retrieval_score is None:
        return "no retrieval score"
    if retrieval_score < RETRIEVAL_THRESHOLD:
        return "insufficient grounding"
    return ""


def _build_result(ticket_id, domain, route, chunks, top_score, safety_trigger, escalated, request_type, chunks_exist, custom_response=None, escalation_reason=""):
    if request_type == "invalid":
        pa = "unknown"
        is_invalid = True
    else:
        pa = _get_product_area(chunks)
        is_invalid = False

    if is_invalid:
        resp = GRADE_ESCALATED_RESPONSE
        is_escalated = False
    elif escalated:
        if custom_response:
            resp = custom_response
        else:
            resp = SAFE_ESCALATION_RESPONSE
        is_escalated = True
    else:
        if custom_response:
            resp = custom_response
        else:
            resp = "I need to escalate this to our support team for review."
        is_escalated = False

    just = justification.build_justification(
        domain=domain,
        router_meta=route,
        retrieval_score=top_score,
        retrieval_threshold=RETRIEVAL_THRESHOLD,
        safety_trigger=safety_trigger,
        escalated=escalated,
        escalation_reason=escalation_reason,
        request_type=request_type,
        product_area=pa,
        chunks_exist=chunks_exist,
    )

    output = {
        "status": "escalated" if is_escalated else "replied",
        "product_area": pa,
        "response": resp,
        "justification": just,
        "request_type": request_type,
    }

    return _finalize(output, ticket_id)


def _get_product_area(chunks):
    if not chunks:
        return "unknown"
    top_meta = chunks[0].get("metadata", {})
    pa = str(top_meta.get("product_area", "")).strip()
    if not pa:
        return "unknown"
    if pa.lower().endswith(".md"):
        pa = pa[:-3]
    # PATCH 3: Strict product_area
    if pa.lower() in ["uncategorized", "unknown", "", None]:
        return "unknown"
    return pa or "unknown"


def _finalize(output: dict, ticket_id) -> dict:
    status = str(output.get("status", "escalated")).lower()
    if status not in {"replied", "escalated"}:
        status = "escalated"

    final = {
        "status": status,
        "product_area": str(output.get("product_area", "unknown") or "unknown"),
        "response": str(output.get("response", "") or ""),
        "justification": output.get("justification", ""),
        "request_type": _sanitize_request_type(output.get("request_type", "product_issue")),
    }
    log_ticket_end(ticket_id, final)
    return final


def _sanitize_request_type(request_type: str, default: str = "product_issue") -> str:
    value = str(request_type or "").strip().lower()
    if value in VALID_REQUEST_TYPES:
        return value
    return default