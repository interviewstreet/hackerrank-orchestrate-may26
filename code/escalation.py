"""Pure-Python escalation policy decision table.

Evaluates triggers T-1..T-6 in order; first match wins.

PRD references: FR-040..FR-042, T-1..T-6, AC-5..AC-8.
Architecture references: section 3.9, section 9.
"""

from __future__ import annotations

from schemas import (
    ClassificationResult,
    EscalationDecision,
    ReasoningResult,
    RetrievedDoc,
)


def decide(
    classification: ClassificationResult,
    retrieval: list[RetrievedDoc],
    reasoning: ReasoningResult | None,
) -> EscalationDecision:
    """Return an EscalationDecision based on the trigger decision table.

    Iter 5 implementation: ordered trigger evaluation per Architecture
    section 3.9 (T-6, T-3, T-2 sensitive, T-2 authorization, T-4, T-5,
    T-1, chitchat allowance, happy path).
    """
    raise NotImplementedError("Iter 5: escalation")
