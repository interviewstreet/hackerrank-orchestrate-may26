from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from support_agent.config import (
    ALLOWED_REQUEST_TYPES,
    ALLOWED_STATUSES,
    GENERATED_COLUMNS,
    OUTPUT_COLUMNS,
    normalize_header,
)
from support_agent.io import read_tickets
from support_agent.models import TicketPrediction


@dataclass(frozen=True)
class ValidationIssue:
    message: str
    row_index: int | None = None
    column: str | None = None


def validate_predictions(predictions: list[TicketPrediction], expected_count: int) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if len(predictions) != expected_count:
        issues.append(
            ValidationIssue(
                message=f"Expected {expected_count} predictions but found {len(predictions)}"
            )
        )

    for index, prediction in enumerate(predictions, start=1):
        if prediction.status not in ALLOWED_STATUSES:
            issues.append(
                ValidationIssue(
                    message=f"Invalid status: {prediction.status}",
                    row_index=index,
                    column="status",
                )
            )
        if prediction.request_type not in ALLOWED_REQUEST_TYPES:
            issues.append(
                ValidationIssue(
                    message=f"Invalid request_type: {prediction.request_type}",
                    row_index=index,
                    column="request_type",
                )
            )
        for column in GENERATED_COLUMNS:
            value = getattr(prediction, column)
            if column == "product_area" and prediction.request_type == "invalid":
                continue
            if not value.strip():
                issues.append(
                    ValidationIssue(
                        message=f"Missing generated field: {column}",
                        row_index=index,
                        column=column,
                    )
                )
    return issues


def read_predictions(path: Path) -> list[TicketPrediction]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV file {path} is missing a header row")

        normalized_headers = [normalize_header(name) for name in reader.fieldnames]
        if tuple(normalized_headers) != OUTPUT_COLUMNS:
            raise ValueError(
                f"CSV file {path} has headers {normalized_headers}, expected {list(OUTPUT_COLUMNS)}"
            )

        predictions: list[TicketPrediction] = []
        for row in reader:
            normalized_row = {normalize_header(key): (value or "") for key, value in row.items()}
            predictions.append(TicketPrediction(**normalized_row))
    return predictions


def validate_output_file(input_path: Path, output_path: Path) -> list[ValidationIssue]:
    tickets = read_tickets(input_path)
    predictions = read_predictions(output_path)
    return validate_predictions(predictions, expected_count=len(tickets))
