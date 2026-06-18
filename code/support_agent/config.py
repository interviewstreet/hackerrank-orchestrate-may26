from __future__ import annotations

import re

INPUT_COLUMNS = ("issue", "subject", "company")
GENERATED_COLUMNS = (
    "response",
    "product_area",
    "status",
    "request_type",
    "justification",
)
OUTPUT_COLUMNS = INPUT_COLUMNS + GENERATED_COLUMNS

ALLOWED_STATUSES = frozenset({"replied", "escalated"})
ALLOWED_REQUEST_TYPES = frozenset({"product_issue", "feature_request", "bug", "invalid"})
SUPPORTED_COMPANIES = frozenset({"hackerrank", "claude", "visa", "none"})


def normalize_header(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower())
    return normalized.strip("_")


def normalize_company(value: str | None) -> str:
    if value is None:
        return "none"
    cleaned = value.strip().lower()
    return cleaned if cleaned else "none"
