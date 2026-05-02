"""
Anchor — RAG response generation using Gemini 2.5 Flash.
Only called when Sentinel returns status=replied.
Never fabricates; signals grounded=false when corpus evidence is insufficient.
"""

import sys

from model_client import ModelClient, ModelClientError
from retriever import RetrievedChunk

MODEL = "google/gemini-2.5-flash"
# Cosine similarity floor for all-MiniLM-L6-v2. Empirically, paraphrased but
# topically-relevant chunks score 0.30–0.55 with this embedder; tightly-matching
# chunks score 0.55+. We keep the bar low and let Anchor's own grounded=false
# self-assessment catch chunks that look related but don't actually answer.
GROUNDING_THRESHOLD = 0.35

_COMPANY_PERSONA = {
    "HackerRank": (
        "You are a friendly HackerRank support specialist. "
        "You help developers, recruiters, and hiring teams with technical assessments, "
        "coding challenges, interviews, and the HackerRank hiring platform."
    ),
    "Claude": (
        "You are a friendly Anthropic support specialist. "
        "You help users with Claude AI products — including Claude.ai, billing, account management, "
        "the Claude API, Claude Code, and enterprise plans."
    ),
    "Visa": (
        "You are a friendly Visa support specialist. "
        "You help cardholders, small business owners, and travelers with Visa payment products, "
        "card benefits, and financial services."
    ),
    "None": (
        "You are a friendly support specialist for HackerRank, Claude (Anthropic), and Visa products."
    ),
}

_SYSTEM_PROMPT_TEMPLATE = """{persona}

You receive a customer support sub-request and retrieved corpus chunks from the official support documentation.

## Your job

Write a warm, clear, human-sounding reply using ONLY the provided corpus chunks.

## Tone and style rules

- Sound like a real, empathetic support agent — not a robot or a policy document.
- Open by briefly acknowledging the customer's issue before jumping to the solution.
- Use plain, everyday language. Avoid jargon, acronyms, and corporate-speak.
- Keep the reply concise: 2–4 short paragraphs. Use bullet points only when listing 3+ steps.
- Never start with "Certainly!", "Of course!", "Great question!", or similar hollow openers.
- End with a short offer to help further if needed (one sentence is enough).

## Hard rules

1. Use ONLY information from the provided corpus chunks. Never use your general knowledge.
2. If the corpus chunks do not contain sufficient information to answer the sub-request, set grounded=false.
3. Do NOT include document headings, file paths, section numbers, or corpus structure markers in the response body.
4. Do NOT make routing or escalation decisions — that is not your role.
5. For invalid/out-of-scope requests, write a polite redirection message explaining that this channel
   handles HackerRank, Claude, and Visa product support only.

## Output schema (JSON only, no other text)

{{
  "response": "<user-facing reply — warm, corpus-grounded prose>",
  "source_doc": "<primary source document path, e.g. data/hackerrank/screen/...md>",
  "grounded": true
}}

If the corpus has no relevant content, return:
{{
  "response": "",
  "source_doc": "",
  "grounded": false
}}"""


def _build_system_prompt(company: str) -> str:
    persona = _COMPANY_PERSONA.get(company, _COMPANY_PERSONA["None"])
    return _SYSTEM_PROMPT_TEMPLATE.format(persona=persona)

_OUT_OF_SCOPE_RESPONSE = (
    "This support channel handles questions about HackerRank, Claude (Anthropic), and Visa products. "
    "We're unable to assist with this request. If you have a product-related question, "
    "please submit a new ticket describing your issue."
)


def generate(
    issue_excerpt: str,
    subject: str,
    resolved_company: str,
    product_area: str,
    corpus_chunks: list[RetrievedChunk],
    request_type: str,
    client: ModelClient,
    request_id: str = "",
) -> dict:
    """
    Returns {"response": str, "source_doc": str, "grounded": bool}.
    Falls back to grounded=false (→ escalation) on API failure.
    """
    # Handle invalid request_type directly — no retrieval needed
    if request_type == "invalid":
        best_source = corpus_chunks[0].source_doc if corpus_chunks else ""
        return {
            "response": _OUT_OF_SCOPE_RESPONSE,
            "source_doc": best_source,
            "grounded": True,
        }

    # Check if any chunk meets the grounding threshold
    top_score = corpus_chunks[0].score if corpus_chunks else 0.0
    if top_score < GROUNDING_THRESHOLD:
        print(
            f"[{request_id}] Anchor: grounded=false (top_score={top_score:.3f} < {GROUNDING_THRESHOLD})",
            file=sys.stderr,
        )
        return {"response": "", "source_doc": "", "grounded": False}

    # Build corpus context for the prompt
    chunks_text = "\n\n---\n\n".join(
        f"Source: {c.source_doc}\n{c.text}" for c in corpus_chunks
    )

    user_content = (
        f"Company: {resolved_company}\n"
        f"Product area: {product_area}\n"
        f"Customer issue: {issue_excerpt}\n\n"
        f"Corpus chunks:\n{chunks_text}"
    )

    messages = [
        {"role": "system", "content": _build_system_prompt(resolved_company)},
        {"role": "user", "content": user_content},
    ]

    # Disable Gemini extended thinking to control costs (OpenRouter syntax).
    extra_body = {"reasoning": {"enabled": False}}

    try:
        result = client.complete_with_retry(
            model=MODEL,
            messages=messages,
            temperature=0.0,
            extra_body=extra_body,
        )
    except ModelClientError as exc:
        print(f"[{request_id}] Anchor: api_error → grounded=false → escalated", file=sys.stderr)
        return {"response": "", "source_doc": "", "grounded": False}

    if not isinstance(result, dict):
        print(f"[{request_id}] Anchor: json_parse_error → grounded=false → escalated", file=sys.stderr)
        return {"response": "", "source_doc": "", "grounded": False}

    grounded = result.get("grounded", False)
    response = str(result.get("response") or "").strip()
    source_doc = str(result.get("source_doc") or (corpus_chunks[0].source_doc if corpus_chunks else ""))

    if not grounded or not response:
        print(f"[{request_id}] Anchor: grounded=false in output → escalated", file=sys.stderr)
        return {"response": "", "source_doc": source_doc, "grounded": False}

    return {"response": response, "source_doc": source_doc, "grounded": True}
