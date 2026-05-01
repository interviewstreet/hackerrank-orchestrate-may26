"""
Support triage agent using LangChain + Groq.

For each ticket it:
1. Retrieves relevant support corpus documents
2. Classifies the request type, product area, urgency, and risk
3. Decides whether to reply or escalate
4. Generates a grounded response (or escalation justification)
"""

import os
import json
import re

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS

from retriever import retrieve_relevant_docs


GROQ_MODEL = "llama-3.3-70b-versatile"

TRIAGE_SYSTEM_PROMPT = """\
You are a support triage agent for three ecosystems: HackerRank, Claude (by Anthropic), and Visa.

Your job is to analyze a support ticket and produce a structured triage decision.

RULES:
1. You MUST ground your response ONLY in the provided support corpus documents. Do NOT hallucinate policies, steps, or information not present in the corpus.
2. If the corpus does not contain enough information to safely answer, you MUST escalate.
3. High-risk scenarios that MUST be escalated: billing disputes, fraud, account security breaches, legal threats, data deletion requests, requests to change test scores or hiring decisions, requests requiring admin/backend access you cannot provide, abusive or threatening language.
4. If the company is "None" and the issue is vague or cross-domain, try to infer the best domain from the issue content. If you cannot, escalate.
5. If the issue is irrelevant to all three domains (HackerRank, Claude, Visa), reply with a polite out-of-scope message and set request_type to "invalid".
6. For feature requests, acknowledge them and set request_type to "feature_request".
7. For bugs, acknowledge, provide any relevant troubleshooting from corpus, and set request_type to "bug".
8. Be concise, professional, and helpful in your response.

CORPUS DOCUMENTS (retrieved for this ticket):
{context}

TICKET:
- Issue: {issue}
- Subject: {subject}
- Company: {company}

Respond with ONLY a valid JSON object (no markdown, no code fences) with these exact keys:
{{
  "status": "replied" or "escalated",
  "product_area": "<most relevant support category/domain area>",
  "response": "<user-facing answer grounded in the corpus, or escalation message>",
  "justification": "<concise explanation of your decision, referencing corpus docs>",
  "request_type": "product_issue" or "feature_request" or "bug" or "invalid"
}}
"""


def get_llm() -> ChatGroq:
    api_key = os.environ.get("GROQ_API_KEY", "").strip()
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set")
    return ChatGroq(
        model=GROQ_MODEL,
        api_key=api_key,
        temperature=0.0,
        max_tokens=2048,
    )


def format_context(docs) -> str:
    parts = []
    for i, doc in enumerate(docs, 1):
        meta = doc.metadata
        parts.append(
            f"[Doc {i}] Domain: {meta.get('domain', 'Unknown')} | "
            f"Category: {meta.get('category', 'Unknown')} | "
            f"Source: {meta.get('source', 'Unknown')}\n"
            f"{doc.page_content}"
        )
    return "\n\n---\n\n".join(parts)


def parse_agent_output(raw: str) -> dict:
    """Parse the JSON output from the LLM, handling common formatting issues."""
    raw = raw.strip()

    # Remove markdown code fences if present
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*\n?", "", raw)
        raw = re.sub(r"\n?```\s*$", "", raw)
        raw = raw.strip()

    # Try to find JSON object
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if match:
        raw = match.group(0)

    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        result = {
            "status": "escalated",
            "product_area": "unknown",
            "response": "Unable to process this ticket. Escalating to human support.",
            "justification": "Agent output parsing failed; escalating for safety.",
            "request_type": "product_issue",
        }

    # Normalize values
    result["status"] = result.get("status", "escalated").lower().strip()
    if result["status"] not in ("replied", "escalated"):
        result["status"] = "escalated"

    result["request_type"] = result.get("request_type", "product_issue").lower().strip()
    if result["request_type"] not in ("product_issue", "feature_request", "bug", "invalid"):
        result["request_type"] = "product_issue"

    for key in ("product_area", "response", "justification"):
        result[key] = result.get(key, "").strip()

    return result


def triage_ticket(
    store: FAISS,
    issue: str,
    subject: str,
    company: str,
) -> dict:
    """Process a single support ticket through the triage agent."""
    llm = get_llm()

    # Build retrieval query from issue + subject
    query = f"{subject} {issue}".strip() if subject else issue

    # Retrieve relevant docs, trying domain-filtered first
    domain = company if company and company != "None" else None
    docs = retrieve_relevant_docs(store, query, domain=domain, k=6)

    # If domain-filtered retrieval returns few results, also search globally
    if len(docs) < 3 and domain:
        global_docs = retrieve_relevant_docs(store, query, domain=None, k=6)
        seen_sources = {d.metadata.get("source") for d in docs}
        for d in global_docs:
            if d.metadata.get("source") not in seen_sources:
                docs.append(d)
                if len(docs) >= 8:
                    break

    context = format_context(docs)

    prompt = ChatPromptTemplate.from_messages([
        ("system", TRIAGE_SYSTEM_PROMPT),
    ])

    chain = prompt | llm | StrOutputParser()

    raw_output = chain.invoke({
        "context": context,
        "issue": issue,
        "subject": subject or "(no subject)",
        "company": company or "None",
    })

    return parse_agent_output(raw_output)
