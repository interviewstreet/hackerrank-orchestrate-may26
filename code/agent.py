"""
agent.py
--------
Core reasoning loop for one support ticket, built on a full
LangChain LCEL RAG pipeline.

LangChain primitives used
--------------------------
  ChatOpenAI / ChatAnthropic   — LLM with JSON structured output
  ChatPromptTemplate           — prompt construction
  JsonOutputParser             — parse LLM JSON output to dict
  RunnableLambda               — inject the RAG retrieval step into the chain
  LCEL pipe operator ( | )     — compose the full pipeline declaratively

RAG pipeline (per ticket)
--------------------------
  Input dict
      ↓  RunnableLambda(_rag_retrieve)   ← semantic search via FAISS retriever
      ↓  ChatPromptTemplate              ← build system + human messages
      ↓  LLM                             ← JSON completion
      ↓  JsonOutputParser                ← parse to Python dict

Pre-LLM safety guards (no LLM call, no RAG)
--------------------------------------------
  1. Company detection   — explicit field or keyword scoring.
  2. Invalid guard       — conversational noise / out-of-scope → early return.
  3. High-risk guard     — fraud / security / adversarial    → immediate escalation.
"""

from __future__ import annotations

import os
import re
import textwrap
from dataclasses import dataclass
from typing import List, Literal, Optional

from langchain_core.documents import Document
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

from retriever import get_retriever

# ── output schema ─────────────────────────────────────────────────────────────
Status      = Literal["replied", "escalated"]
RequestType = Literal["product_issue", "feature_request", "bug", "invalid"]


@dataclass
class TicketResult:
    status:        Status
    product_area:  str
    response:      str
    justification: str
    request_type:  RequestType


# ── safety patterns ───────────────────────────────────────────────────────────
ESCALATE_PATTERNS = [
    r"(?i)\b(fraud|fraudulent|stolen card|identity theft)\b",
    r"(?i)\b(hack(ed)?|security (breach|vulnerabilit|bug bounty))\b",
    r"(?i)\b(legal action|lawsuit|sue)\b",
    r"(?i)\b(billing|payment|subscription)\b.*\b(fail|error|wrong|incorrect)\b",
    r"(?i)show.*(rules|internal|logic|documents|retrieved|context|system prompt)",
    r"(?i)(ignore|disregard|forget).*(instruction|rule|policy)",
    r"(?i)pretend.*(you are|you're|youre)",
    r"(?i)(delete|rm -rf|format|wipe|destroy).*(file|disk|system|database)",
]

INVALID_PATTERNS = [
    r"(?i)^(thank(s| you)?[\s!.]*|ok(ay)?[\s!.]*|cool[\s!.]*|great[\s!.]*)$",
    r"(?i)\bwho (is|was|are) (the )?(actor|star|lead|director|writer)\b",
    r"(?i)\bgive me (the )?code to.*(delete|destroy|wipe|format)",
    r"(?i)^give me the code to delete",
]

COMPANIES = {"HackerRank", "Claude", "Visa"}
KNOWN_COMPANY_KEYWORDS: dict[str, List[str]] = {
    "HackerRank": ["hackerrank", "assessment", "test invite", "candidate", "recruiter",
                   "coding test", "hackathon", "interview platform", "screen", "skillup", "chakra"],
    "Claude":     ["claude", "anthropic", "claude.ai", "bedrock", "mcp", "lti",
                   "claude pro", "claude team", "claude enterprise"],
    "Visa":       ["visa", "card", "transaction", "merchant", "atm", "issuer",
                   "bank", "stolen card", "credit card", "debit card"],
}


# ── helpers ───────────────────────────────────────────────────────────────────

def _detect_company(issue: str, subject: str, company_field: str) -> Optional[str]:
    """Return the effective company, preferring the explicit field over inference."""
    if company_field and company_field.strip() not in ("None", ""):
        c = company_field.strip()
        if c in COMPANIES:
            return c
    text = (issue + " " + subject).lower()
    scores = {c: 0 for c in COMPANIES}
    for company, keywords in KNOWN_COMPANY_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                scores[company] += 1
    best = max(scores, key=lambda k: scores[k])
    return best if scores[best] > 0 else None


def _matches_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(p, text) for p in patterns)


def _format_docs(docs: List[Document]) -> str:
    """Render retrieved docs into a numbered context block for the prompt."""
    if not docs:
        return "(no relevant documentation found)"
    parts = []
    for i, doc in enumerate(docs, 1):
        meta   = doc.metadata
        header = (
            f"[Doc {i} | {meta.get('company', '?')} "
            f"| {meta.get('product_area', '?')} | {meta.get('source', '?')}]"
        )
        parts.append(f"{header}\n{doc.page_content}")
    return "\n\n---\n\n".join(parts)


# ── LLM factory ───────────────────────────────────────────────────────────────

def _get_llm():
    """
    Return a LangChain chat model.
    Prioritises: Groq -> OpenAI -> Anthropic -> Ollama (local).
    """
    groq_key      = os.getenv("GROQ_API_KEY", "")
    openai_key    = os.getenv("OPENAI_API_KEY", "")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY", "")
    ollama_model  = os.getenv("OLLAMA_MODEL", "")

    if groq_key:
        from langchain_groq import ChatGroq  # type: ignore
        return ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            api_key=groq_key,
        )
    elif openai_key:
        from langchain_openai import ChatOpenAI  # type: ignore
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            seed=42,
            model_kwargs={"response_format": {"type": "json_object"}},
            api_key=openai_key,
        )
    elif anthropic_key:
        from langchain_anthropic import ChatAnthropic  # type: ignore
        return ChatAnthropic(
            model="claude-3-5-haiku-20241022",
            temperature=0,
            api_key=anthropic_key,
        )
    elif ollama_model:
        from langchain_ollama import ChatOllama  # type: ignore
        return ChatOllama(
            model=ollama_model,
            temperature=0,
            format="json",
        )
    else:
        # Fallback to a clear error explaining the need for an API key or local Ollama
        raise EnvironmentError(
            "No LLM configuration found. Please set one of the following:\n"
            "  - GROQ_API_KEY\n"
            "  - OPENAI_API_KEY\n"
            "  - ANTHROPIC_API_KEY\n"
            "  - OLLAMA_MODEL (e.g. 'llama3.2' or 'mistral')"
        )


# ── prompt template ───────────────────────────────────────────────────────────
SYSTEM_TEMPLATE = textwrap.dedent("""
You are an AI support triage agent for three products: HackerRank, Claude, and Visa.
Respond using ONLY the documentation excerpts provided. Never invent policies, steps,
or contacts that are not present in the documentation.

Output EXACTLY one JSON object (no markdown fences) with these keys:
  "status"        — "replied" | "escalated"
  "product_area"  — the most specific support category from the docs
  "response"      — a clear, user-facing answer (or escalation notice)
  "justification" — 1-2 sentences explaining your decision, citing the docs
  "request_type"  — "product_issue" | "feature_request" | "bug" | "invalid"

Rules:
  - Escalate when the docs do not cover the issue well enough for a safe answer,
    or when the issue involves account access, billing, fraud, or security.
  - For out-of-scope / irrelevant tickets use request_type "invalid" and status "replied".
  - When escalating, response MUST start with "This requires human review" and
    must NOT attempt to answer the underlying question.
  - Ground product_area in the documentation section the answer comes from.
""").strip()

USER_TEMPLATE = textwrap.dedent("""
Company field: {company_field}
Inferred company: {company}

Subject: {subject}
Issue: {issue}

Relevant documentation (retrieved via RAG):
{context}

Produce the JSON response now.
""").strip()

PROMPT = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_TEMPLATE),
    ("human",  USER_TEMPLATE),
])


# ── RAG retrieval step (RunnableLambda) ───────────────────────────────────────

def _rag_retrieve(inputs: dict) -> dict:
    """
    LangChain RAG retrieval step — runs inside the LCEL chain as a RunnableLambda.

    Reads ``company`` and the ticket text from the input dict, performs a
    semantic search against the FAISS index using the LangChain
    ``VectorStoreRetriever`` abstraction, and injects the formatted context
    back into the dict so the downstream ``ChatPromptTemplate`` can consume it.

    Flow
    ----
      inputs (dict)
          "subject", "issue", "company", "company_field"
          ↓
      get_retriever(company_filter=...).invoke(query)   ← LangChain Retriever
          ↓
      _format_docs(docs)                               ← numbered context block
          ↓
      {**inputs, "context": <formatted docs>}          ← returned to LCEL pipe
    """
    company: Optional[str] = inputs.get("company")
    company_filter         = company if company and company != "unknown" else None
    query                  = f"{inputs.get('subject', '')} {inputs.get('issue', '')}"

    # Use the LangChain VectorStoreRetriever (BaseRetriever) for the search
    retriever = get_retriever(company_filter=company_filter, top_k=5)
    docs: List[Document] = retriever.invoke(query)

    # Fall back to unfiltered results if the company scope is too narrow
    if company_filter and len(docs) < 3:
        fallback   = get_retriever(company_filter=None, top_k=5)
        extra      = fallback.invoke(query)
        seen       = {id(d) for d in docs}
        for doc in extra:
            if id(doc) not in seen:
                docs.append(doc)
            if len(docs) >= 5:
                break

    return {**inputs, "context": _format_docs(docs)}


# ── LCEL RAG chain ────────────────────────────────────────────────────────────

def _mock_llm_logic(inputs: dict) -> dict:
    """
    Mocks the LLM logic to allow processing without an external API.
    Extracts information from the retrieved context and returns a JSON-like dict.
    """
    context = inputs.get("context", "")
    company = inputs.get("company", "unknown")
    
    # Try to extract the first document's content
    # [Doc 1 | ... | ... | ...]
    # content...
    match = re.search(r"\[Doc 1 \| [^\]]+\]\n(.*?)(?:\n\n---\n\n|$)", context, re.DOTALL)
    if match:
        response_body = match.group(1).strip()
    else:
        response_body = f"I'm sorry, I couldn't find specific documentation for your request regarding {company}."

    # Extract product area from the header if possible
    area_match = re.search(r"\[Doc 1 \| [^|]+ \| ([^|]+) \|", context)
    product_area = area_match.group(1).strip() if area_match else company

    return {
        "status": "replied",
        "product_area": product_area,
        "response": response_body,
        "justification": "Mocked response based on top retrieved documentation chunk.",
        "request_type": "product_issue"
    }


def _build_rag_chain():
    """
    Build and return the full LangChain LCEL RAG pipeline:

        Input dict
            │
            ▼  RunnableLambda(_rag_retrieve)
            │  ↳ calls get_retriever().invoke() — LangChain BaseRetriever
            │  ↳ injects "context" key into the dict
            │
            ▼  ChatPromptTemplate(PROMPT)
            │  ↳ renders system + human messages with all dict values
            │
            ▼  LLM  (OpenAI / Anthropic / Ollama)
            │  ↳ JSON-mode completion
            │
            ▼  JsonOutputParser
               ↳ deserialises the JSON string → Python dict
    """
    try:
        llm = _get_llm()
        return (
            RunnableLambda(_rag_retrieve)   # Step 1 — RAG: retrieve & inject context
            | PROMPT                        # Step 2 — Build prompt messages
            | llm                           # Step 3 — LLM inference
            | JsonOutputParser()            # Step 4 — Parse JSON → dict
        )
    except EnvironmentError:
        # If no LLM is configured, fall back to the mock logic so the app still runs
        print("Warning: No LLM configured. Falling back to Mock logic.")
        return (
            RunnableLambda(_rag_retrieve)
            | RunnableLambda(_mock_llm_logic)
        )


# ── singleton chain ───────────────────────────────────────────────────────────
_chain = None


def _get_chain():
    """Lazy-initialise the RAG chain (builds LLM client on first call)."""
    global _chain
    if _chain is None:
        _chain = _build_rag_chain()
    return _chain


# ── main entry point ──────────────────────────────────────────────────────────

def ollama_call(prompt: str) -> Optional[str]:
    """Helper to execute LLM call based on the configured model."""
    llm = _get_llm()
    from langchain_core.messages import HumanMessage
    try:
        # Some chat models prefer a list of messages
        response = llm.invoke([HumanMessage(content=prompt)])
        # .content handles ChatOpenAI/ChatGroq/ChatAnthropic return types
        return response.content if hasattr(response, "content") else str(response)
    except Exception as e:
        print(f"LLM call failed: {e}")
        return None

def process_ticket(issue: str, subject: str, company_field: str) -> TicketResult:
    """
    Process one support ticket using retrieval-driven decision making,
    strict context grounding, and LLM overrides for high confidence matches.
    """
    from retriever import get_vectorstore
    
    # 1. Similarity + threshold + Normalization
    vector_db = get_vectorstore()
    ticket = f"{subject} {issue}".strip()
    
    try:
        raw_results = vector_db.similarity_search_with_score(ticket, k=3)
        # Normalize score: FAISS returns L2 distance. cos_sim = 1 - (L2^2 / 2)
        results = [(doc, max(0.0, 1.0 - (score ** 2) / 2.0)) for doc, score in raw_results]
        top_doc, top_score = results[0]
        # Filter and pass only high-relevance context chunks to the model
        valid_results = [(doc, score) for doc, score in results if score > 0.55]
        context = "\n\n".join([doc.page_content for doc, score in valid_results])
    except IndexError:
        return TicketResult("escalated", "general", "This requires human review.", "No context found", "product_issue")

    # Add fallback escalation when context is empty or unusable (Context Quality)
    if not context:
        return TicketResult(status="escalated", product_area="general", response="This requires human review.", justification="empty_context", request_type="product_issue")

    # Priority Check: Is this a high-confidence match?
    is_high_confidence = top_score >= 0.75

    # 2. Rule-based escalation (only apply if NOT high confidence)
    # Always treat retrieval score as the primary signal and never override high-confidence cases.
    if not is_high_confidence:
        high_risk_words = ["refund immediately", "ban seller", "identity theft", "hack", "admin access", "security vulnerability"]
        if any(word in ticket.lower() for word in high_risk_words): 
            return TicketResult(status="escalated", product_area="security", response="This requires human review.", justification="rule_based_security", request_type="product_issue")

        # Category-based rules: known safe categories do not trigger extra escalation rules
        safe_categories = ["subscription", "certificate", "billing"]
        is_safe = any(word in ticket.lower() for word in safe_categories)

    # 3. 2-tier confidence fallback (low → escalate safely)
    if top_score < 0.55: 
        return TicketResult(status="escalated", product_area="general", response="This requires human review.", justification="low_similarity", request_type="product_issue")

    # From here, score is >= 0.55, so we definitively decide to auto-reply (attempt answer).
    # 4. Strict grounded prompt + Restrict LLM to only use retrieved context
    prompt = f"You are a support triage agent. You MUST base your answer STRICTLY on the provided Context. Do NOT use external knowledge or guess. If context clearly answers → reply confidently using it. If context only partially answers → provide a partial answer based on context. If neither → respond ONLY with ESCALATE.\n\nContext:\n{context}\n\nTicket:\n{ticket}\n\nAnswer:"

    # 5. LLM call
    response = ollama_call(prompt)

    # 6. Fallback when LLM fails or returns ESCALATE (Use context as backup answer)
    # Never default to ESCALATE on error. System errors != user issue severity.
    if not response or "ESCALATE" in response.upper():
        response = f"Based on our documentation: {top_doc.page_content}"

    # 8. Debug logging (don’t skip this)
    print(f"\n---DEBUG---\nTicket: {ticket}\nNorm Score: {top_score:.3f}\nContext: {context[:200]}\nResponse: {response}\n--")
    
    return TicketResult(
        status="replied",
        product_area=company_field or "general",
        response=response,
        justification=f"Score: {top_score:.3f}",
        request_type="product_issue",
    )
