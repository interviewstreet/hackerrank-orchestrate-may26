"""Smoke test: import every module in code/ and instantiate a Ticket.

Catches SyntaxError, missing module, broken import, broken pydantic schema.
This test is intentionally green from Iter 0 onward.
"""

from __future__ import annotations


def test_imports_every_module() -> None:
    """Every module in code/ must import without raising."""
    import agent  # noqa: F401
    import classifier  # noqa: F401
    import config  # noqa: F401
    import escalation  # noqa: F401
    import indexer  # noqa: F401
    import loader  # noqa: F401
    import main  # noqa: F401
    import output_writer  # noqa: F401
    import preprocessor  # noqa: F401
    import reasoner  # noqa: F401
    import retriever  # noqa: F401
    import schemas  # noqa: F401
    import tracer  # noqa: F401
    import verifier  # noqa: F401


def test_ticket_instantiates_with_valid_fields() -> None:
    """The Ticket DTO is concrete in Iter 0 and must accept valid input."""
    from schemas import Ticket

    ticket = Ticket(
        index=0,
        issue="site is down",
        subject="",
        company="None",
    )
    assert ticket.index == 0
    assert ticket.issue == "site is down"
    assert ticket.subject == ""
    assert ticket.company == "None"
    assert ticket.requires_inference is False


def test_canned_responses_are_non_empty_strings() -> None:
    """Sanity-check the placeholder strings used by Iter 5 escalation."""
    from prompts.canned_responses import CHITCHAT_REPLY, OUT_OF_SCOPE_REPLY

    assert isinstance(CHITCHAT_REPLY, str) and CHITCHAT_REPLY
    assert isinstance(OUT_OF_SCOPE_REPLY, str) and OUT_OF_SCOPE_REPLY
