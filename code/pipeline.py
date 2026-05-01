"""
Pipeline
Orchestrates all agents in the correct order for one ticket row.
Returns a complete output dict ready for CSV writing.
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from agents import safety_pre, router, retriever, grounding, safety_post, llm_agent, product_area, justification
from utils.logger import log_ticket_start, log_ticket_end, log_agent


def run(ticket: dict, ticket_id: int | str = "?") -> dict:
    log_ticket_start(ticket_id, ticket)

    issue   = str(ticket.get("issue", "")).strip()
    subject = str(ticket.get("subject", "")).strip()
    company = str(ticket.get("company", "")).strip() if ticket.get("company") else None
    if company and company.lower() in ("none", "nan", ""):
        company = None

    # Merged query: subject + issue
    query = f"{subject} {issue}".strip() if subject else issue

    # ── Stage 1: Safety Pass 1 ─────────────────────────────────────────────
    s1 = safety_pre.run(query)
    if s1:
        result = _finalize(s1, ticket_id)
        return result

    # ── Stage 2: Router ────────────────────────────────────────────────────
    route  = router.run(query, company)
    domain = route["domain"]

    if domain == "unknown":
        result = _finalize({
            "status":        "escalated",
            "request_type":  "product_issue",
            "product_area":  "unknown",
            "response":      "We could not determine the relevant support domain for your query. "
                             "A human agent will assist you.",
            "justification": "[R-unknown-domain] Could not route ticket to any known domain.",
        }, ticket_id)
        return result

    # ── Stage 3: Retriever ─────────────────────────────────────────────────
    chunks = retriever.run(query, domain)

    # ── Stage 4: Grounding Validator ───────────────────────────────────────
    gv = grounding.run(chunks, query)
    if gv:
        gv["product_area"] = product_area.run(chunks, domain)
        gv["justification"] = justification.run(domain, route, chunks, gv.get("rule_triggered"), None, "escalated")
        result = _finalize(gv, ticket_id)
        return result

    # ── Stage 5: Safety Pass 2 ─────────────────────────────────────────────
    s2 = safety_post.run(query, domain)
    if s2:
        s2["product_area"] = product_area.run(chunks, domain)
        s2["justification"] = justification.run(domain, route, chunks, s2.get("rule_triggered"), None, "escalated")
        result = _finalize(s2, ticket_id)
        return result

    # ── Stage 6: LLM Agent ─────────────────────────────────────────────────
    llm_result = llm_agent.run(query, chunks)

    # ── Stage 7: Product Area ──────────────────────────────────────────────
    pa = product_area.run(chunks, domain)

    # ── Stage 8: Determine final status ───────────────────────────────────
    if llm_result["escalate"]:
        status = "escalated"
        response = llm_result["response"]
    else:
        status = "replied"
        response = llm_result["response"]

    # ── Stage 9: Justification ─────────────────────────────────────────────
    just = justification.run(domain, route, chunks, None, llm_result, status)

    output = {
        "status":        status,
        "product_area":  pa,
        "response":      response,
        "justification": just,
        "request_type":  llm_result["request_type"],
    }

    result = _finalize(output, ticket_id)
    return result


def _finalize(output: dict, ticket_id) -> dict:
    # Ensure all required fields exist
    final = {
        "status":        output.get("status", "escalated"),
        "product_area":  output.get("product_area", "unknown"),
        "response":      output.get("response", ""),
        "justification": output.get("justification", ""),
        "request_type":  output.get("request_type", "product_issue"),
    }
    log_ticket_end(ticket_id, final)
    return final