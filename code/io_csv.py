"""CSV IO with strict header contract."""
from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from schemas import RowOutput, TicketInput

INPUT_HEADER_MAP = {
    "Issue": "issue", "Subject": "subject", "Company": "company",
}


def read_input_tickets(path: Path) -> list[TicketInput]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        out: list[TicketInput] = []
        for row in reader:
            issue = (row.get("Issue") or row.get("issue") or "").strip()
            subject = (row.get("Subject") or row.get("subject") or "").strip()
            company = (row.get("Company") or row.get("company") or "None").strip()
            out.append(TicketInput(issue=issue, subject=subject, company=company))
        return out


def read_sample_gold(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [{
            "issue": (r.get("Issue") or "").strip(),
            "subject": (r.get("Subject") or "").strip(),
            "company": (r.get("Company") or "None").strip(),
            "response": r.get("Response") or "",
            "product_area": (r.get("Product Area") or "").strip(),
            "status": (r.get("Status") or "").strip().lower(),
            "request_type": (r.get("Request Type") or "").strip(),
        } for r in reader]


def open_output_writer(path: Path, header: list[str], resume: bool = False):
    existing_keys: set[str] = set()
    write_header = True
    mode = "w"
    if resume and path.exists() and path.stat().st_size > 0:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                existing_keys.add(r.get("issue", ""))
        mode = "a"
        write_header = False
    f = path.open(mode, newline="", encoding="utf-8")
    writer = csv.DictWriter(f, fieldnames=header, extrasaction="ignore",
                            quoting=csv.QUOTE_MINIMAL)
    if write_header:
        writer.writeheader()
        f.flush()
    return f, writer, existing_keys


def write_rows(writer, file_obj, rows: Iterable[RowOutput]) -> None:
    for r in rows:
        writer.writerow(r.to_csv_row())
        file_obj.flush()
