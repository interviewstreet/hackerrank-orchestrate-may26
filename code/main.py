"""
Main entry point for the Multi-Domain Support Triage Agent.

Usage:
    python main.py                          # Process support_tickets.csv -> output.csv
    python main.py --sample                 # Process sample_support_tickets.csv (for dev/testing)
    python main.py --rebuild-index          # Force rebuild the vector index
    python main.py --single "your issue"    # Triage a single issue interactively
"""

import argparse
import csv
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

# Load .env from repo root
REPO_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(REPO_ROOT / ".env")

from retriever import build_vector_store  # noqa: E402
from agent import triage_ticket  # noqa: E402


TICKETS_DIR = REPO_ROOT / "support_tickets"
INPUT_FILE = TICKETS_DIR / "support_tickets.csv"
SAMPLE_FILE = TICKETS_DIR / "sample_support_tickets.csv"
OUTPUT_FILE = TICKETS_DIR / "output.csv"

OUTPUT_COLUMNS = ["Issue", "Subject", "Company", "Response", "Product Area", "Status", "Request Type"]


def process_tickets(input_path: Path, output_path: Path, store, verbose: bool = True):
    """Process all tickets from input CSV and write results to output CSV."""
    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    total = len(rows)
    results = []

    if verbose:
        print(f"\nProcessing {total} tickets from {input_path.name}...")
        print("=" * 60)

    for i, row in enumerate(rows, 1):
        issue = row.get("Issue", "").strip()
        subject = row.get("Subject", "").strip()
        company = row.get("Company", "").strip()

        if verbose:
            print(f"\n[{i}/{total}] Company: {company or 'None'} | Subject: {subject[:50] or '(empty)'}...")

        try:
            result = triage_ticket(store, issue, subject, company)
        except Exception as e:
            print(f"  ERROR: {e}")
            result = {
                "status": "escalated",
                "product_area": "unknown",
                "response": "Unable to process this ticket automatically. Escalating to human support.",
                "justification": f"Agent error: {str(e)[:200]}",
                "request_type": "product_issue",
            }

        output_row = {
            "Issue": issue,
            "Subject": subject,
            "Company": company,
            "Response": result["response"],
            "Product Area": result["product_area"],
            "Status": result["status"].capitalize(),
            "Request Type": result["request_type"],
        }
        results.append(output_row)

        if verbose:
            print(f"  Status: {result['status']} | Type: {result['request_type']} | Area: {result['product_area']}")

        # Small delay to respect rate limits
        if i < total:
            time.sleep(0.5)

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(results)

    if verbose:
        print(f"\n{'=' * 60}")
        print(f"Done! Results written to {output_path}")
        replied = sum(1 for r in results if r["Status"].lower() == "replied")
        escalated = sum(1 for r in results if r["Status"].lower() == "escalated")
        print(f"  Replied: {replied} | Escalated: {escalated}")


def interactive_mode(store, issue: str, company: str = "None"):
    """Triage a single issue interactively."""
    print(f"\nTriaging issue: {issue[:100]}...")
    result = triage_ticket(store, issue, "", company)
    print(f"\nStatus: {result['status']}")
    print(f"Request Type: {result['request_type']}")
    print(f"Product Area: {result['product_area']}")
    print(f"Response: {result['response']}")
    print(f"Justification: {result['justification']}")


def main():
    parser = argparse.ArgumentParser(description="Multi-Domain Support Triage Agent")
    parser.add_argument("--sample", action="store_true", help="Process sample tickets instead")
    parser.add_argument("--rebuild-index", action="store_true", help="Force rebuild vector index")
    parser.add_argument("--single", type=str, help="Triage a single issue")
    parser.add_argument("--company", type=str, default="None", help="Company for --single mode")
    parser.add_argument("--quiet", action="store_true", help="Suppress verbose output")
    args = parser.parse_args()

    # Validate GROQ_API_KEY
    if not os.environ.get("GROQ_API_KEY"):
        print("ERROR: GROQ_API_KEY environment variable is not set.")
        print("Set it in your .env file or export it: export GROQ_API_KEY=your_key")
        sys.exit(1)

    print("Initializing vector store...")
    store = build_vector_store(force_rebuild=args.rebuild_index)
    print("Vector store ready.")

    if args.single:
        interactive_mode(store, args.single, args.company)
    else:
        input_path = SAMPLE_FILE if args.sample else INPUT_FILE
        process_tickets(input_path, OUTPUT_FILE, store, verbose=not args.quiet)


if __name__ == "__main__":
    main()
