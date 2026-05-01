"""
Justification Builder
Assembles a human-readable, traceable justification for every decision.
Includes: routing reason, retrieval evidence, safety rule (if triggered).
"""


def run(
    domain:       str,
    router_meta:  dict,
    chunks:       list[dict],
    safety_rule:  str | None,
    llm_result:   dict | None,
    status:       str,
) -> str:
    parts = []

    # 1. Routing
    method = router_meta.get("method", "unknown")
    conf   = router_meta.get("confidence", "")
    parts.append(f"Domain routed to '{domain}' via {method} (confidence={conf}).")

    # 2. Retrieval evidence
    if chunks:
        top  = chunks[0]
        meta = top.get("metadata", {})
        parts.append(
            f"Top retrieved article: '{meta.get('title', 'N/A')}' "
            f"(score={top.get('score', 0):.3f}, source={meta.get('source_url', 'N/A')})."
        )
    else:
        parts.append("No relevant corpus documents retrieved.")

    # 3. Safety / escalation reason
    if safety_rule:
        parts.append(f"Escalated by rule [{safety_rule}].")
    elif llm_result and llm_result.get("escalate"):
        reason = llm_result.get("escalate_reason", "LLM flagged as unresolvable.")
        parts.append(f"LLM escalation: {reason}")

    # 4. Final status
    parts.append(f"Final status: {status}.")

    return " ".join(parts)