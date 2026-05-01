import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional


REQUIRED_COLUMNS = ["status", "product_area", "response", "justification", "request_type"]
ALLOWED_STATUS = {"replied", "escalated"}
ALLOWED_REQUEST_TYPES = {"product_issue", "feature_request", "bug", "invalid"}


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def read_header(path: Path) -> List[str]:
    with path.open("r", newline="", encoding="utf-8-sig") as file:
        return next(csv.reader(file), [])


def validate(input_path: Path, output_path: Path, log_path: Optional[Path]) -> Dict[str, object]:
    input_rows = read_csv(input_path)
    output_rows = read_csv(output_path)
    issues = []
    if read_header(output_path) != REQUIRED_COLUMNS:
        issues.append("Output header does not match required columns exactly.")
    if len(input_rows) != len(output_rows):
        issues.append(f"Row count mismatch: input={len(input_rows)} output={len(output_rows)}")

    empty_values = []
    bad_status = []
    bad_request_type = []
    for index, row in enumerate(output_rows, start=1):
        for column in REQUIRED_COLUMNS:
            if not str(row.get(column, "")).strip():
                empty_values.append({"row": index, "column": column})
        if row.get("status") not in ALLOWED_STATUS:
            bad_status.append({"row": index, "value": row.get("status")})
        if row.get("request_type") not in ALLOWED_REQUEST_TYPES:
            bad_request_type.append({"row": index, "value": row.get("request_type")})

    if empty_values:
        issues.append(f"Empty required values: {empty_values}")
    if bad_status:
        issues.append(f"Invalid status labels: {bad_status}")
    if bad_request_type:
        issues.append(f"Invalid request_type labels: {bad_request_type}")

    log_tickets = None
    if log_path:
        if not log_path.exists():
            issues.append(f"Log file does not exist: {log_path}")
        else:
            text = log_path.read_text(encoding="utf-8", errors="ignore")
            log_tickets = text.count("\nTicket ") + (1 if text.startswith("Ticket ") else 0)
            if log_tickets != len(output_rows):
                issues.append(f"Log ticket count mismatch: log={log_tickets} output={len(output_rows)}")

    return {
        "passed": not issues,
        "issues": issues,
        "input_rows": len(input_rows),
        "output_rows": len(output_rows),
        "log_tickets": log_tickets,
        "status_distribution": Counter(row["status"] for row in output_rows),
        "request_type_distribution": Counter(row["request_type"] for row in output_rows),
        "product_area_distribution": Counter(row["product_area"] for row in output_rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate triage output and logs")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--log")
    args = parser.parse_args()
    report = validate(Path(args.input), Path(args.output), Path(args.log) if args.log else None)
    print(json.dumps(report, indent=2, default=dict))
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
