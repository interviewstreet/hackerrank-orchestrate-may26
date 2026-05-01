"""CSV ticket loader.

Reads ``support_tickets/support_tickets.csv`` into ``Ticket`` DTOs.

PRD references: FR-001..FR-006, AC-2.
Architecture references: section 3.3.
"""

from __future__ import annotations

import csv
from pathlib import Path

from schemas import Ticket

# Closed enum of accepted company values per Ticket schema. Anything else
# (including blank or unknown) is coerced to "None" with requires_inference=True.
_KNOWN_COMPANIES: frozenset[str] = frozenset(
    {"HackerRank", "Claude", "Visa", "None"}
)


def load_tickets(path: Path) -> list[Ticket]:
    """Read the input CSV and return a list of ``Ticket`` DTOs in row order.

    Behavior (per Architecture 3.3):
      - ``utf-8-sig`` strips a leading UTF-8 BOM if present.
      - Header keys (e.g. ``Issue``, ``Subject``, ``Company``) are lowercased.
      - All field values are stripped of surrounding whitespace
        (so ``"None "`` becomes ``"None"``).
      - Unknown ``company`` values are coerced to ``"None"`` and the row is
        flagged ``requires_inference=True``.
      - Extra columns in the input (e.g. ``Response`` in
        ``sample_support_tickets.csv``) are silently ignored.
      - Row order is preserved; ``Ticket.index`` is the 0-based row index.
    """
    path = Path(path)
    tickets: list[Ticket] = []

    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            return tickets

        # Build a {lowercase_key: original_key} mapping so we can look up
        # values regardless of the input header casing.
        key_map = {name.strip().lower(): name for name in reader.fieldnames}

        issue_key = key_map.get("issue")
        subject_key = key_map.get("subject")
        company_key = key_map.get("company")

        if issue_key is None or subject_key is None or company_key is None:
            raise ValueError(
                "CSV header must contain Issue, Subject, Company columns; "
                f"found: {reader.fieldnames!r}"
            )

        for index, row in enumerate(reader):
            issue = (row.get(issue_key) or "").strip()
            subject = (row.get(subject_key) or "").strip()
            raw_company = (row.get(company_key) or "").strip()

            if raw_company in _KNOWN_COMPANIES:
                company = raw_company
                requires_inference = False
            else:
                company = "None"
                requires_inference = True

            tickets.append(
                Ticket(
                    index=index,
                    issue=issue,
                    subject=subject,
                    company=company,  # type: ignore[arg-type]
                    requires_inference=requires_inference,
                )
            )

    return tickets
