"""CSV IO with strict header contract."""
from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Iterable

from schemas import RowOutput, TicketInput

INPUT_HEADER_MAP = {
    "Issue": "issue", "Subject": "subject", "Company": "company",
}


def ticket_key(issue: str, subject: str = "", company: str = "") -> str:
    return "\x1f".join((
        (issue or "").strip(),
        (subject or "").strip(),
        (company or "").strip(),
    ))


def _norm_cell(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def read_input_tickets(path: Path) -> list[TicketInput]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        out: list[TicketInput] = []
        for row in reader:
            issue = _norm_cell(row.get("Issue") or row.get("issue"))
            subject = _norm_cell(row.get("Subject") or row.get("subject"))
            company = _norm_cell(row.get("Company") or row.get("company") or "None")
            out.append(TicketInput(issue=issue, subject=subject, company=company))
        return out


def read_sample_gold(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [{
            "issue": _norm_cell(r.get("Issue")),
            "subject": _norm_cell(r.get("Subject")),
            "company": _norm_cell(r.get("Company") or "None"),
            "response": r.get("Response") or "",
            "product_area": _norm_cell(r.get("Product Area")),
            "status": _norm_cell(r.get("Status")).lower(),
            "request_type": _norm_cell(r.get("Request Type")),
        } for r in reader]


def open_output_writer(path: Path, header: list[str], resume: bool = False):
    existing_keys: set[str] = set()
    write_header = True
    mode = "w"
    if resume and path.exists() and path.stat().st_size > 0:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                issue = r.get("issue") or r.get("Issue") or ""
                subject = r.get("subject") or r.get("Subject") or ""
                company = r.get("company") or r.get("Company") or ""
                existing_keys.add(ticket_key(issue, subject, company))
        mode = "a"
        write_header = False
    f = path.open(mode, newline="", encoding="utf-8")
    writer = csv.DictWriter(f, fieldnames=header, extrasaction="ignore",
                            quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    if write_header:
        writer.writeheader()
        f.flush()
    return f, writer, existing_keys


def write_rows(writer, file_obj, rows: Iterable[RowOutput]) -> None:
    for r in rows:
        writer.writerow(r.to_csv_row())
        file_obj.flush()
