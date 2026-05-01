"""Post-hoc grounding verifier.

Checks every numeric claim, URL, phone number, and dollar amount in the
generated response against the union of retrieved chunk text.

PRD references: FR-030, R-1.
Architecture references: section 3.8 (grounding contract).
"""

from __future__ import annotations

from schemas import RetrievedDoc


def verify_grounding(response: str, retrieved: list[RetrievedDoc]) -> bool:
    """Return True iff every checkable token in response appears in retrieved.

    Iter 4 implementation: regex-extract phones, URLs, dollar amounts and
    explicit numerics from response, substring-check union of chunk text.
    """
    raise NotImplementedError("Iter 4: verifier")
