"""Tests for classifier heuristic priors — Iter 3.

Covers chitchat / trivia / outage detection that runs BEFORE the LLM call.
Injection detection lives in preprocessor (test_preprocessor.py).

PRD references: FR-010..FR-017, T-3, T-5.
Architecture references: section 3.7.
"""

from __future__ import annotations

import pytest

from classifier import compute_heuristic_priors
from preprocessor import clean
from schemas import Ticket


def _cleaned(issue: str = "Body", subject: str = "Subj", company: str = "HackerRank"):
    return clean(Ticket(index=0, issue=issue, subject=subject, company=company))


# ---------- outage detection -------------------------------------------------


@pytest.mark.parametrize(
    "body",
    [
        "The site is down right now",
        "the resume builder is down for everyone",
        "claude has stopped working since this morning",
        "le site n'est pas accessible",
        "none of the pages load",
        "your service is broken",
        "the app is unavailable",
        "server is inaccessible from our network",
    ],
)
def test_outage_regex_hits(body: str) -> None:
    priors = compute_heuristic_priors(_cleaned(issue=body))
    assert priors["is_outage_report"] is True, f"expected is_outage_report for: {body!r}"


@pytest.mark.parametrize(
    "body",
    [
        "I cannot log in to my account",
        "How do I reset my password?",
        "My test results are not showing the right score",
    ],
)
def test_outage_regex_misses_non_outage(body: str) -> None:
    priors = compute_heuristic_priors(_cleaned(issue=body))
    assert priors["is_outage_report"] is False, f"unexpected is_outage_report for: {body!r}"


# ---------- chitchat / trivia detection -------------------------------------


@pytest.mark.parametrize(
    "body",
    [
        "Thank you so much",
        "thanks a lot",
        "Happy to help next time",
        "Cheers!",
        "ok thanks",
    ],
)
def test_chitchat_pleasantries(body: str) -> None:
    priors = compute_heuristic_priors(_cleaned(issue=body))
    assert priors["is_chitchat_or_trivia"] is True, f"expected chitchat for: {body!r}"


def test_chitchat_short_body_no_question_word() -> None:
    priors = compute_heuristic_priors(_cleaned(issue="ok"))
    assert priors["is_chitchat_or_trivia"] is True


@pytest.mark.parametrize(
    "body",
    [
        "Who won the FIFA World Cup in 2022?",
        "What is the capital of France?",
        "tell me a movie trivia question",
    ],
)
def test_chitchat_trivia_keywords(body: str) -> None:
    priors = compute_heuristic_priors(_cleaned(issue=body))
    assert priors["is_chitchat_or_trivia"] is True, f"expected trivia for: {body!r}"


@pytest.mark.parametrize(
    "body",
    [
        "How do I cancel a test invite for a candidate?",
        "I can't log in to my HackerRank account, please advise",
        "My Visa card was charged twice last month, requesting a refund",
    ],
)
def test_chitchat_misses_real_support_questions(body: str) -> None:
    priors = compute_heuristic_priors(_cleaned(issue=body))
    assert priors["is_chitchat_or_trivia"] is False, f"unexpected chitchat for: {body!r}"


def test_priors_dict_keys_complete() -> None:
    priors = compute_heuristic_priors(_cleaned(issue="hello world"))
    assert set(priors.keys()) >= {
        "is_outage_report",
        "is_chitchat_or_trivia",
        "is_authorization_violation",
        "is_sensitive",
    }
