"""CSV input/output helpers for support ticket predictions."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from support_agent.config import GENERATED_COLUMNS, INPUT_COLUMNS, OUTPUT_COLUMNS, normalize_header
from support_agent.models import SupportTicket, TicketPrediction


def read_tickets(path: Path) -> list[SupportTicket]:
    """Read input tickets from CSV and normalize the required fields."""
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError(f"CSV file {path} is missing a header row")

        field_map = {normalize_header(name): name for name in reader.fieldnames}
        missing = [column for column in INPUT_COLUMNS if column not in field_map]
        if missing:
            raise ValueError(f"CSV file {path} is missing required columns: {missing}")

        tickets: list[SupportTicket] = []
        for row in reader:
            tickets.append(
                SupportTicket(
                    issue=(row.get(field_map["issue"], "") or "").strip(),
                    subject=(row.get(field_map["subject"], "") or "").strip(),
                    company=(row.get(field_map["company"], "") or "").strip(),
                )
            )
    return tickets


def write_predictions(path: Path, predictions: Iterable[TicketPrediction]) -> None:
    """Write predictions to CSV using the repository's output column order."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        for prediction in predictions:
            writer.writerow(generated_fields(prediction))


def generated_fields(prediction: TicketPrediction) -> dict[str, str]:
    """Extract only the generated output fields from a prediction record."""
    return {field: getattr(prediction, field) for field in GENERATED_COLUMNS}
