"""LLM-driven classifier with heuristic priors.

Emits ClassificationResult with request_type, domain, product_area,
plus signal flags consumed by the escalation policy.

PRD references: FR-010..FR-017, T-3, T-5, T-6.
Architecture references: section 3.7.
"""

from __future__ import annotations

from schemas import CleanedTicket, ClassificationResult


def classify(cleaned: CleanedTicket) -> ClassificationResult:
    """Run heuristic priors then a tool-use LLM call; return validated result.

    Iter 3 implementation: chitchat / outage / injection regex priors,
    then claude-sonnet-4-5 tool_use call with mandatory schema, pydantic
    validation, retry-once on parse failure.
    """
    raise NotImplementedError("Iter 3: classifier")
