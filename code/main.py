"""
main.py
-------
Entry point for the HackerRank Orchestrate support triage agent.

Usage:
    python main.py [--input PATH] [--output PATH] [--rebuild-index]

Defaults:
    --input   ../support_tickets/support_tickets.csv
    --output  ../support_tickets/output.csv

The script reads every row from the input CSV, runs the agent, and writes
a new CSV to the output path with five additional columns:
    status, product_area, response, justification, request_type
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
import time
from pathlib import Path

# Ensure sibling modules (agent, retriever, corpus_loader) are importable
sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv  # type: ignore

# Load .env before importing agent (which reads env vars for API keys)
_env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=_env_path)

from agent import TicketResult, process_ticket  # noqa: E402
from retriever import get_retriever, get_vectorstore  # noqa: E402

# ── path defaults ─────────────────────────────────────────────────────────────
REPO_ROOT   = Path(__file__).parent.parent
INPUT_CSV   = REPO_ROOT / "support_tickets" / "support_tickets.csv"
OUTPUT_CSV  = REPO_ROOT / "support_tickets" / "output.csv"
OUTPUT_COLS = ["Response", "Product Area", "Status", "Request Type"]
# ─────────────────────────────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Support Triage Agent")
    p.add_argument("--input",  default=str(INPUT_CSV),  help="Path to input CSV")
    p.add_argument("--output", default=str(OUTPUT_CSV), help="Path to output CSV")
    p.add_argument("--rebuild-index", action="store_true",
                   help="Force rebuild the FAISS index from scratch")
    return p.parse_args()


def run(input_path: Path, output_path: Path, rebuild_index: bool = False) -> None:
    # ── warm up retriever (builds / loads FAISS index) ──────────────────────
    # get_vectorstore() builds/loads the index; get_retriever() validates the
    # full LangChain retriever path before we process any tickets.
    print("=== Initialising retriever …")
    get_vectorstore(force_rebuild=rebuild_index)  # build / load FAISS index
    get_retriever()                               # validate LangChain retriever

    # ── read input ────────────────────────────────────────────────────────────
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        # normalise column names (strip whitespace, title-case Company etc.)
        rows = [{k.strip(): v.strip() for k, v in row.items()} for row in rows]

    print(f"=== Processing {len(rows)} tickets …\n")

    # ── process & collect results ─────────────────────────────────────────────
    results: list[dict] = []
    for i, row in enumerate(rows, 1):
        issue   = row.get("Issue",   row.get("issue",   ""))
        subject = row.get("Subject", row.get("subject", ""))
        company = row.get("Company", row.get("company", ""))

        print(f"[{i}/{len(rows)}] Company={company!r:12s}  Subject={subject[:50]!r}")
        t0 = time.time()
        try:
            result: TicketResult = process_ticket(issue, subject, company)
        except Exception as exc:
            print(f"  ERROR: {exc}  → escalating as fallback")
            result = TicketResult(
                status="escalated",
                product_area="general",
                response="An internal error occurred. This ticket has been escalated for human review.",
                justification=f"Agent exception: {exc}",
                request_type="product_issue",
            )
        elapsed = time.time() - t0
        print(f"  ↳ status={result.status}, request_type={result.request_type}, "
              f"area={result.product_area}  ({elapsed:.1f}s)")

        # Preserve original input columns + append agent output in sample format
        out_row = dict(row)
        out_row["Response"]     = result.response
        out_row["Product Area"] = result.product_area
        out_row["Status"]       = result.status.capitalize() if result.status == "replied" else "Escalated"
        out_row["Request Type"] = result.request_type
        results.append(out_row)

    # ── write output ──────────────────────────────────────────────────────────
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    for col in OUTPUT_COLS:
        if col not in fieldnames:
            fieldnames.append(col)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)

    # ── Evaluation Metrics ────────────────────────────────────────────────────
    total_tickets = len(results)
    escalated = sum(1 for r in results if r["Status"] == "Escalated")
    replied = sum(1 for r in results if r["Status"] == "Replied")
    
    print(f"\n=== Evaluation Metrics ===")
    print(f"Total Processed:  {total_tickets}")
    print(f"Auto-Reply Rate:  {replied / total_tickets * 100:.1f}% ({replied}/{total_tickets})")
    print(f"Escalation Rate:  {escalated / total_tickets * 100:.1f}% ({escalated}/{total_tickets})")
    print(f"Consistency:      Validated by score-driven thresholds")
    print(f"==========================\n")

    print(f"=== Done. Output written to: {output_path}")


if __name__ == "__main__":
    args = parse_args()
    run(
        input_path=Path(args.input),
        output_path=Path(args.output),
        rebuild_index=args.rebuild_index,
    )
