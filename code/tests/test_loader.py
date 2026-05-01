"""Tests for code/loader.py — Iter 1 RED phase.

PRD references: FR-001..FR-006, AC-2.
Architecture references: section 3.3.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

from loader import load_tickets

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).resolve().parent / "fixtures"
SAMPLE_CSV = REPO_ROOT / "support_tickets" / "sample_support_tickets.csv"
PRODUCTION_CSV = REPO_ROOT / "support_tickets" / "support_tickets.csv"
LOADER_QUIRKS = FIXTURES / "loader_quirks.csv"


def _write_csv(path: Path, header: list[str], rows: list[list[str]],
               encoding: str = "utf-8") -> None:
    with open(path, "w", encoding=encoding, newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        for row in rows:
            w.writerow(row)


def test_load_tickets_normalizes_titlecase_headers(tmp_path: Path) -> None:
    """Input header `Issue,Subject,Company` -> Tickets with lowercase attrs."""
    p = tmp_path / "titlecase.csv"
    _write_csv(
        p,
        ["Issue", "Subject", "Company"],
        [["my issue body", "my subject", "HackerRank"]],
    )

    tickets = load_tickets(p)

    assert len(tickets) == 1
    t = tickets[0]
    assert t.issue == "my issue body"
    assert t.subject == "my subject"
    assert t.company == "HackerRank"


def test_load_tickets_strips_company_trailing_whitespace(tmp_path: Path) -> None:
    """`"None "` -> `"None"`."""
    p = tmp_path / "trailing.csv"
    _write_csv(
        p,
        ["Issue", "Subject", "Company"],
        [["body", "subj", "None "]],
    )

    tickets = load_tickets(p)

    assert tickets[0].company == "None"


def test_load_tickets_blank_subject_ok(tmp_path: Path) -> None:
    """Empty subject string preserved as ``""`` without exception."""
    p = tmp_path / "blank_subject.csv"
    _write_csv(
        p,
        ["Issue", "Subject", "Company"],
        [["body", "", "HackerRank"]],
    )

    tickets = load_tickets(p)

    assert tickets[0].subject == ""


def test_load_tickets_preserves_row_order(tmp_path: Path) -> None:
    """Ticket.index matches enumerated row order."""
    p = tmp_path / "order.csv"
    _write_csv(
        p,
        ["Issue", "Subject", "Company"],
        [
            ["body0", "s0", "HackerRank"],
            ["body1", "s1", "Claude"],
            ["body2", "s2", "Visa"],
            ["body3", "s3", "None"],
        ],
    )

    tickets = load_tickets(p)

    assert [t.index for t in tickets] == [0, 1, 2, 3]
    assert [t.issue for t in tickets] == ["body0", "body1", "body2", "body3"]


def test_load_tickets_unknown_company_marks_inference(tmp_path: Path) -> None:
    """Unknown company -> coerced to "None" with requires_inference=True."""
    p = tmp_path / "unknown_company.csv"
    _write_csv(
        p,
        ["Issue", "Subject", "Company"],
        [["body", "subj", "OtherCorp"]],
    )

    tickets = load_tickets(p)

    assert tickets[0].company == "None"
    assert tickets[0].requires_inference is True


def test_load_tickets_utf8_with_bom() -> None:
    """File with UTF-8 BOM is parsed; BOM does not corrupt the header."""
    # Sanity: confirm the fixture begins with the BOM.
    assert LOADER_QUIRKS.read_bytes()[:3] == b"\xef\xbb\xbf"

    tickets = load_tickets(LOADER_QUIRKS)

    # Header columns lowercase + parseable means BOM was stripped.
    assert len(tickets) == 3
    assert tickets[0].issue == "Trailing whitespace ticket"
    assert tickets[0].company == "None"  # trailing space stripped
    assert tickets[1].subject == ""
    assert tickets[2].company == "None"  # unknown -> coerced
    assert tickets[2].requires_inference is True


def test_load_tickets_returns_29_rows_on_production() -> None:
    """Production support_tickets.csv currently has 29 data rows.

    NOTE: Iter dispatch said 57; on disk today it is 29. Test asserts
    the truth on disk. If a future commit grows the file to 57, update
    this test.
    """
    tickets = load_tickets(PRODUCTION_CSV)
    assert len(tickets) == 29


def test_load_tickets_returns_10_rows_on_sample() -> None:
    """sample_support_tickets.csv has 10 data rows under TitleCase headers.

    Sample CSV also has extra ground-truth columns (Response, Product Area,
    Status, Request Type) which the loader silently ignores — only the
    three input columns map to Ticket fields.
    """
    tickets = load_tickets(SAMPLE_CSV)
    assert len(tickets) == 10
