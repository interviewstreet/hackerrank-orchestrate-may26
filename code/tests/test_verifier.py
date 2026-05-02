"""Tests for code/verifier.py — Iter 4 (post-hoc grounding verifier).

PRD references: FR-030, R-1.
Architecture references: section 3.8.
"""

from __future__ import annotations

import pytest

from schemas import RetrievedDoc
from verifier import verify_grounding


def _doc(text: str, *, chunk_id: str = "c1", domain: str = "visa") -> RetrievedDoc:
    return RetrievedDoc(
        chunk_id=chunk_id,
        file_path=f"data/{domain}/fake.md",
        domain=domain,  # type: ignore[arg-type]
        breadcrumbs=["root"],
        title="t",
        text=text,
        cosine_score=0.9,
        bm25_score=1.0,
        rrf_score=0.5,
    )


# ---------- phone numbers ----------------------------------------------------


def test_verifier_passes_when_phone_in_corpus() -> None:
    chunks = [_doc("For lost cards call +1-800-VISA-911 or 1-800-847-2911 anytime.")]
    response = "Please call 1-800-847-2911 to report a lost Visa card."
    assert verify_grounding(response, chunks) is True


def test_verifier_fails_when_response_invents_phone() -> None:
    chunks = [_doc("For lost cards call 1-800-847-2911 anytime.")]
    response = "Please call 1-555-123-4567 to report a lost Visa card."
    assert verify_grounding(response, chunks) is False


def test_verifier_passes_when_phone_format_normalizes() -> None:
    """Different separators in response vs corpus should still match."""
    chunks = [_doc("Reach the help line at +1 800 847 2911.")]
    response = "Reach the help line at 1-800-847-2911."
    assert verify_grounding(response, chunks) is True


# ---------- URLs -------------------------------------------------------------


def test_verifier_passes_when_url_in_corpus() -> None:
    chunks = [_doc("Visit https://www.visa.com/support for more details.")]
    response = "Visit https://www.visa.com/support for more details."
    assert verify_grounding(response, chunks) is True


def test_verifier_fails_when_response_invents_url() -> None:
    chunks = [_doc("Visit https://www.visa.com/support for more details.")]
    response = "Visit https://fake-visa-helpline.example.com for fast support."
    assert verify_grounding(response, chunks) is False


# ---------- dollar amounts ---------------------------------------------------


def test_verifier_passes_when_dollar_amount_in_corpus() -> None:
    chunks = [_doc("The annual fee is $99 and waived for the first year.")]
    response = "The annual fee is $99."
    assert verify_grounding(response, chunks) is True


def test_verifier_fails_when_response_invents_dollar_amount() -> None:
    chunks = [_doc("The annual fee is $99 and waived for the first year.")]
    response = "The annual fee is $250."
    assert verify_grounding(response, chunks) is False


def test_verifier_passes_when_dollar_amount_with_commas() -> None:
    chunks = [_doc("Daily ATM withdrawal limit is $1,000 for cardholders.")]
    response = "Daily ATM withdrawal limit is $1,000."
    assert verify_grounding(response, chunks) is True


# ---------- generic numerics that should be IGNORED -------------------------


def test_verifier_ignores_dates_iso_format() -> None:
    chunks = [_doc("Effective for transactions after the policy update.")]
    response = "This applies to all transactions after 2024-01-15."
    assert verify_grounding(response, chunks) is True


def test_verifier_ignores_year_only() -> None:
    chunks = [_doc("Updated annually based on rate-card review.")]
    response = "The fee schedule was last updated in 2024."
    assert verify_grounding(response, chunks) is True


def test_verifier_ignores_small_counts_in_running_text() -> None:
    """Bare integers like '3 business days' aren't grounding-critical."""
    chunks = [_doc("Disputes are resolved promptly through our standard process.")]
    response = "Disputes are typically resolved in 3 business days."
    assert verify_grounding(response, chunks) is True


# ---------- mix --------------------------------------------------------------


def test_verifier_fails_when_one_of_many_facts_unverifiable() -> None:
    chunks = [
        _doc("Lost cards: call 1-800-847-2911."),
        _doc("Visit https://www.visa.com/support for more help."),
    ]
    # Phone is grounded; URL is invented.
    response = "Call 1-800-847-2911 or visit https://fake.example.com."
    assert verify_grounding(response, chunks) is False


def test_verifier_passes_with_no_extractable_tokens() -> None:
    chunks = [_doc("Please contact our consumer support team for assistance.")]
    response = "Please reach out to consumer support for help."
    assert verify_grounding(response, chunks) is True


def test_verifier_handles_empty_response() -> None:
    chunks = [_doc("any chunk text")]
    assert verify_grounding("", chunks) is True


def test_verifier_handles_empty_chunks_with_facts_in_response() -> None:
    """No chunks but response claims a phone number -> can't verify -> fail."""
    assert verify_grounding("Call 1-800-847-2911 for help.", []) is False
