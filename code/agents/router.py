"""
Router Agent
Step 1: keyword scoring (no LLM)
Step 2: confidence check
Step 3: LLM fallback ONLY if confidence < threshold
"""

from openai import OpenAI
from config import (
    DOMAIN_KEYWORDS, ROUTER_CONFIDENCE_THRESHOLD,
    OPENAI_API_KEY, LLM_MODEL, LLM_TEMPERATURE,
)
from utils.logger import log_agent, log_llm_call

VALID_COMPANIES = {"claude", "hackerrank", "visa"}

client = OpenAI(api_key=OPENAI_API_KEY)


def run(query: str, company: str | None) -> dict:
    """
    Returns:
      { domain: str, method: str, confidence: int | str }
    domain ∈ { claude, hackerrank, visa, unknown }
    """

    # Fast path: company field is reliable
    if company and company.lower() in VALID_COMPANIES:
        domain = company.lower()
        log_agent("router", f"rule-company-field → {domain}", {"company": company})
        return {"domain": domain, "method": "company_field", "confidence": "high"}

    # Step 1 — keyword scoring
    scores = {d: 0 for d in DOMAIN_KEYWORDS}
    q_lower = query.lower()
    for domain, keywords in DOMAIN_KEYWORDS.items():
        for kw in keywords:
            if kw in q_lower:
                scores[domain] += 1

    best_domain = max(scores, key=scores.get)
    best_score  = scores[best_domain]

    if best_score >= ROUTER_CONFIDENCE_THRESHOLD:
        log_agent("router", f"rule-keyword → {best_domain}", {"scores": scores})
        return {"domain": best_domain, "method": "keyword", "confidence": best_score}

    # Step 2 — LLM fallback
    domain = _llm_classify(query)
    return {"domain": domain, "method": "llm_fallback", "confidence": "llm"}


def _llm_classify(query: str) -> str:
    prompt = (
        "You are a support ticket router. "
        "Classify the following ticket into exactly one of: visa, hackerrank, claude\n"
        "Return ONLY the single label, nothing else.\n\n"
        f"Ticket:\n{query}"
    )
    try:
        resp = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=10,
            temperature=LLM_TEMPERATURE,
            messages=[{"role": "user", "content": prompt}],
        )
        label = resp.choices[0].message.content.strip().lower()
        log_llm_call(prompt, label, {"domain": label})
        if label in VALID_COMPANIES:
            return label
    except Exception as e:
        log_agent("router", f"llm_fallback_error: {e}", {})

    return "unknown"