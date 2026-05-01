"""Ticket sanitization and prompt-injection neutralization.

PRD references: FR-035, T-6, NFR-008.
Architecture references: section 3.4.
"""

from __future__ import annotations

from schemas import CleanedTicket, Ticket


def clean(ticket: Ticket) -> CleanedTicket:
    """Sanitize the ticket body and detect prompt-injection signatures.

    Iter 3 implementation: control-char strip, whitespace collapse,
    body cap at 8000 chars, injection regex set, delimiter-wrapping.
    """
    raise NotImplementedError("Iter 3: preprocessor")
