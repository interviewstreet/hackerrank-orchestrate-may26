"""Tests for code/output_writer.py — Iter 1 RED phase.

PRD references: FR-050..FR-055, AC-1..AC-3, AC-12.
Architecture references: section 3.10.
"""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path

import pytest

from output_writer import write_output
from schemas import OutputRow


HEADER_LINE = (
    "issue,subject,company,status,product_area,response,justification,request_type"
)


def _row(**overrides) -> OutputRow:
    """Build a default-valid OutputRow with optional overrides."""
    base = dict(
        issue="my issue",
        subject="my subj",
        company="HackerRank",
        status="Replied",
        product_area="screen",
        response="here is your answer",
        justification="grounded in data/hackerrank/screen/",
        request_type="product_issue",
    )
    base.update(overrides)
    return OutputRow(**base)


def _read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").split("\n")


def _read_rows(path: Path) -> list[dict[str, str]]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def test_write_output_header_lowercase_8_columns(tmp_path: Path) -> None:
    """First line == lowercase 8-column header, no trailing comma, \\n line ending."""
    p = tmp_path / "out.csv"
    write_output([_row()], p)

    raw = p.read_bytes()
    # First line ends in \n, not \r\n.
    first_newline = raw.index(b"\n")
    first_line = raw[:first_newline].decode("utf-8")
    assert first_line == HEADER_LINE


def test_write_output_status_titlecase_replied(tmp_path: Path) -> None:
    """status='Replied' is written verbatim in TitleCase."""
    p = tmp_path / "out.csv"
    write_output([_row(status="Replied")], p)

    rows = _read_rows(p)
    assert rows[0]["status"] == "Replied"


def test_write_output_status_titlecase_escalated(tmp_path: Path) -> None:
    """status='Escalated' is written verbatim in TitleCase."""
    p = tmp_path / "out.csv"
    write_output([_row(status="Escalated", response="Escalate to a human")], p)

    rows = _read_rows(p)
    assert rows[0]["status"] == "Escalated"


def test_write_output_request_type_lowercase_snakecase(tmp_path: Path) -> None:
    """All four request_type enum values written as lowercase snake_case."""
    p = tmp_path / "out.csv"
    write_output(
        [
            _row(request_type="product_issue"),
            _row(request_type="feature_request"),
            _row(request_type="bug"),
            _row(request_type="invalid"),
        ],
        p,
    )

    rows = _read_rows(p)
    assert [r["request_type"] for r in rows] == [
        "product_issue",
        "feature_request",
        "bug",
        "invalid",
    ]


def test_write_output_product_area_lowercase_snakecase(tmp_path: Path) -> None:
    """product_area written verbatim in lowercase snake_case for representative values."""
    p = tmp_path / "out.csv"
    write_output(
        [
            _row(product_area="screen"),
            _row(product_area="claude_api_and_console"),
            _row(product_area="travel_support"),
        ],
        p,
    )

    rows = _read_rows(p)
    assert [r["product_area"] for r in rows] == [
        "screen",
        "claude_api_and_console",
        "travel_support",
    ]


def test_write_output_rfc4180_quoting_for_embedded_quotes(tmp_path: Path) -> None:
    """A response containing a literal " round-trips correctly via csv module."""
    p = tmp_path / "out.csv"
    payload = 'He said "yes"'
    write_output([_row(response=payload)], p)

    rows = _read_rows(p)
    assert rows[0]["response"] == payload


def test_write_output_lf_lineendings_on_windows(tmp_path: Path) -> None:
    """No \\r byte present anywhere in the output file."""
    p = tmp_path / "out.csv"
    write_output(
        [
            _row(issue="row0"),
            _row(issue="row1"),
            _row(issue="row2"),
        ],
        p,
    )

    raw = p.read_bytes()
    assert b"\r" not in raw


def test_write_output_round_trip_byte_identical(tmp_path: Path) -> None:
    """Same input written to two paths -> identical SHA-256. NFR-001 spot test."""
    rows = [_row(issue=f"row{i}") for i in range(5)]
    p1 = tmp_path / "out1.csv"
    p2 = tmp_path / "out2.csv"

    write_output(rows, p1)
    write_output(rows, p2)

    h1 = hashlib.sha256(p1.read_bytes()).hexdigest()
    h2 = hashlib.sha256(p2.read_bytes()).hexdigest()
    assert h1 == h2


def test_write_output_invalid_enum_falls_back_to_escalated_invalid(
    tmp_path: Path,
) -> None:
    """Out-of-enum status/request_type coerced; justification flagged."""
    p = tmp_path / "out.csv"
    write_output(
        [
            _row(
                status="bogus",
                request_type="frob",
                justification="orig reason",
            ),
        ],
        p,
    )

    rows = _read_rows(p)
    assert rows[0]["status"] == "Escalated"
    assert rows[0]["request_type"] == "invalid"
    assert "(writer:invalid_value)" in rows[0]["justification"]
    # Original justification text is preserved (not erased).
    assert "orig reason" in rows[0]["justification"]


def test_write_output_preserves_row_count(tmp_path: Path) -> None:
    """7 rows in -> 7 data rows out (plus header = 8 lines, plus trailing newline)."""
    p = tmp_path / "out.csv"
    rows = [_row(issue=f"row{i}") for i in range(7)]
    write_output(rows, p)

    out_rows = _read_rows(p)
    assert len(out_rows) == 7

    # And exactly 1 header line + 7 data lines = 8 \n-terminated lines
    raw = p.read_bytes().decode("utf-8")
    # split on \n; trailing \n produces an empty tail element.
    parts = raw.split("\n")
    # parts: [header, row0..row6, ""] = 9 elements (last empty)
    assert len(parts) == 9
    assert parts[-1] == ""
