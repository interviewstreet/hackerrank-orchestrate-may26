"""LLM-driven response generator with corpus grounding.

PRD references: FR-030..FR-035, R-1.
Architecture references: section 3.8.
"""

from __future__ import annotations

from schemas import CleanedTicket, ReasoningResult, RetrievedDoc


def reason(
    cleaned: CleanedTicket,
    retrieved: list[RetrievedDoc],
) -> ReasoningResult:
    """Generate a grounded response with citations.

    Iter 4 implementation: assemble system + user prompt with delimited
    ticket and chunks, claude-sonnet-4-5 tool_use, pydantic validation,
    retry-once on parse failure.
    """
    raise NotImplementedError("Iter 4: reasoner")
