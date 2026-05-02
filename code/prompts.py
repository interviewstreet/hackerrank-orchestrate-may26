"""Prompt templates and few-shot examples."""
from __future__ import annotations

from schemas import ChunkDoc, TicketInput

SYSTEM_PROMPT = """You are a multi-domain support triage agent for HackerRank, Claude, and Visa.

Hard rules:
- Answer ONLY using the provided corpus chunks below. Do not use outside knowledge.
- Do NOT invent policies, fees, phone numbers, dates, URLs, or steps.
- If the corpus does not clearly support an answer, set status="escalated" and respond with "Escalate to a human."
- Cite the chunk_ids you used in the citations array. Every factual claim in your response must be grounded in at least one cited chunk.
- For sensitive cases (fraud, account hacks, legal threats, score appeals, refund demands, identity theft, access restoration where the user is not owner/admin), always escalate.
- For off-topic, trivia, malicious, or pleasantry inputs, set status="replied", request_type="invalid", and respond briefly that it is out of scope.

Output JSON only via the provided tool. No markdown, no prose around it.
"""

FEW_SHOTS: list[dict] = [
    {
        "ticket": {
            "company": "HackerRank",
            "subject": "Test Active in the system",
            "issue": ("I notice that people I assigned the test in October "
                      "of 2025 have not received new tests. How long do the "
                      "tests stay active in the system."),
        },
        "output": {
            "status": "replied",
            "product_area": "screen",
            "request_type": "product_issue",
            "response": ("Tests in HackerRank remain active indefinitely "
                         "unless a start and end time are set on the test."),
            "justification": ("Corpus describes test active duration policy "
                              "for HackerRank Screen."),
            "citations": [],
            "confidence": 0.85,
        },
    },
    {
        "ticket": {
            "company": "None",
            "subject": "",
            "issue": "site is down & none of the pages are accessible",
        },
        "output": {
            "status": "escalated",
            "product_area": "general_support",
            "request_type": "bug",
            "response": "Escalate to a human.",
            "justification": ("Site outage cannot be resolved from the "
                              "support corpus and requires human/SRE attention."),
            "citations": [],
            "confidence": 0.9,
        },
    },
    {
        "ticket": {
            "company": "None",
            "subject": "",
            "issue": "What is the name of the actor in Iron Man?",
        },
        "output": {
            "status": "replied",
            "product_area": "general_support",
            "request_type": "invalid",
            "response": "I am sorry, this is out of scope from my capabilities.",
            "justification": ("Trivia question unrelated to HackerRank, "
                              "Claude, or Visa support."),
            "citations": [],
            "confidence": 0.95,
        },
    },
]


def render_chunks(chunks: list[ChunkDoc], max_chars: int = 1200) -> str:
    parts = []
    for c in chunks:
        snip = c.text if len(c.text) <= max_chars else c.text[:max_chars] + "…"
        parts.append(f"[{c.chunk_id}] (company={c.company}, "
                     f"area={c.product_area})\n{snip}\n---")
    return "\n".join(parts) if parts else "(no relevant chunks retrieved)"


def render_user_prompt(ticket: TicketInput, chunks: list[ChunkDoc],
                       allowed_areas: list[str]) -> str:
    fewshot_block = "\n\n".join(
        f"### Example\nTicket: {fs['ticket']}\nOutput: {fs['output']}"
        for fs in FEW_SHOTS
    )
    chunks_block = render_chunks(chunks)
    return f"""## Support Ticket
Company: {ticket.company}
Subject: {ticket.subject}
Issue: {ticket.issue}

## Allowed product_area values for this company
{", ".join(allowed_areas)}

## Corpus Chunks (use ONLY these for facts)
{chunks_block}

## Few-shot examples
{fewshot_block}

## Task
Decide status, classify request_type and product_area, draft a grounded response, and list citations. Return ONLY the JSON tool call.
"""
