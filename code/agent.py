"""
agent.py — Template-based response generation (No LLM).

WHAT THIS MODULE DOES:
  Instead of calling an LLM, it takes the top retrieved chunks and
  formats a safe, grounded response directly from the corpus text.

WHY:
  - 100% deterministic
  - Zero hallucination risk
  - Instant generation (no API latency, no rate limits)
  - Meets the requirement: "use only the provided support corpus"
"""

from typing import Literal
from models import TicketInput, TicketOutput, DocChunk  # type: ignore


def generate_response(
    ticket: TicketInput,
    chunks: list[DocChunk],
    product_area: str,
    request_type: Literal["product_issue", "feature_request", "bug", "invalid"],
) -> TicketOutput:
    """
    Generate a deterministic response directly from the top chunk.
    """
    if not chunks:
        # Fallback if somehow called with no chunks
        return TicketOutput(
            status="escalated",
            product_area=product_area,
            response="I am escalating this ticket because I could not find relevant documentation.",
            justification="No relevant chunks found in the corpus.",
            request_type=request_type,
        )

    # Use the best matching chunk
    top_chunk = chunks[0]
    
    # Format a direct, grounded response
    response_text = (
        f"Based on the {top_chunk.company.title()} support documentation:\n\n"
        f"{top_chunk.text.strip()}\n\n"
        f"(Source: {top_chunk.source})"
    )

    justification = f"Found a highly relevant match in {top_chunk.source} (Score: {top_chunk.score:.2f})."

    return TicketOutput(
        status="replied",
        product_area=product_area,
        response=response_text,
        justification=justification,
        request_type=request_type,
    )
