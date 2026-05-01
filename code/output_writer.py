"""Output CSV writer with casing normalization and enum guards.

PRD references: FR-050..FR-055, AC-1..AC-3.
Architecture references: section 3.10.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

from schemas import OutputRow

# FR-050: lowercase, 8-column header in this exact order. Note that
# ``request_type`` is the LAST column (output schema differs from intuition).
_HEADER: list[str] = [
    "issue",
    "subject",
    "company",
    "status",
    "product_area",
    "response",
    "justification",
    "request_type",
]

# Closed enums per Architecture 3.10.
_VALID_STATUS: frozenset[str] = frozenset({"Replied", "Escalated"})
_VALID_REQUEST_TYPE: frozenset[str] = frozenset(
    {"product_issue", "feature_request", "bug", "invalid"}
)
# product_area is a closed enum in Architecture 3.7 but we accept any
# lowercase-snake-case token defensively.
_PRODUCT_AREA_RE = re.compile(r"^[a-z0-9_]+$")

_INVALID_VALUE_FLAG = " (writer:invalid_value)"


def _coerce_status(raw: str) -> tuple[str, bool]:
    """Return ``(status, dirty)``. Invalid -> ``"Escalated"`` and ``dirty=True``."""
    if raw in _VALID_STATUS:
        return raw, False
    return "Escalated", True


def _coerce_request_type(raw: str) -> tuple[str, bool]:
    """Return ``(request_type, dirty)``. Invalid -> ``"invalid"`` and ``dirty=True``."""
    if raw in _VALID_REQUEST_TYPE:
        return raw, False
    return "invalid", True


def _coerce_product_area(raw: str) -> tuple[str, bool]:
    """Return ``(product_area, dirty)``.

    Empty string is allowed (sample CSV has empty product_area on some rows
    so we mirror that ground truth). Otherwise must match
    ``^[a-z0-9_]+$``; non-matching coerces to ``"general_support"``.
    """
    if raw == "" or _PRODUCT_AREA_RE.match(raw):
        return raw, False
    return "general_support", True


def _strip_cr(s: str) -> str:
    """Strip carriage returns to keep \\n-only line endings."""
    return s.replace("\r", "")


def write_output(rows: list[OutputRow], path: Path) -> None:
    """Write ``OutputRow`` DTOs as CSV with the FR-050 8-column header.

    - UTF-8, ``\\n`` line endings (RFC 4180 with ``QUOTE_MINIMAL``).
    - Out-of-enum values are coerced to ``Escalated`` / ``invalid`` /
      ``general_support`` and the per-row ``justification`` gets
      ``(writer:invalid_value)`` appended (defense in depth, Architecture 3.10).
    - Row order matches input order.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(_HEADER)

        for row in rows:
            status, status_dirty = _coerce_status(row.status)
            request_type, rt_dirty = _coerce_request_type(row.request_type)
            product_area, pa_dirty = _coerce_product_area(row.product_area)
            dirty = status_dirty or rt_dirty or pa_dirty

            justification = row.justification
            if dirty:
                justification = justification + _INVALID_VALUE_FLAG

            writer.writerow(
                [
                    _strip_cr(row.issue),
                    _strip_cr(row.subject),
                    _strip_cr(row.company),
                    _strip_cr(status),
                    _strip_cr(product_area),
                    _strip_cr(row.response),
                    _strip_cr(justification),
                    _strip_cr(request_type),
                ]
            )
