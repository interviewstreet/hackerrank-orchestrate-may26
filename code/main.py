#!/usr/bin/env python3
"""
main.py - Terminal-based Support Triage Agent entry point.

Usage:
    python main.py                          # Process support_tickets/support_tickets.csv
    python main.py --input path/to/in.csv  # Custom input CSV
    python main.py --output path/to/out.csv # Custom output CSV
    python main.py --sample                 # Run on sample_support_tickets.csv
    python main.py --verbose               # Show per-ticket debug info
    python main.py --ticket "My issue..."  # Process a single ticket interactively

Environment variables:
    ANTHROPIC_API_KEY   — Required for LLM-powered responses (recommended)
    DATA_DIR            — Override path to corpus directory

Output: support_tickets/output.csv
"""

from __future__ import annotations

import os
import sys
import csv
import time
import argparse
import traceback
from pathlib import Path
from typing import Optional
from env_utils import load_env_file

# ─── Path setup ───────────────────────────────────────────────────────────────

ROOT = Path(__file__).parent.parent
DATA_DIR = Path(os.environ.get("DATA_DIR", str(ROOT / "data")))
TICKETS_DIR = ROOT / "support_tickets"
INPUT_CSV = TICKETS_DIR / "support_tickets.csv"
SAMPLE_CSV = TICKETS_DIR / "sample_support_tickets.csv"
OUTPUT_CSV = TICKETS_DIR / "output.csv"

sys.path.insert(0, str(Path(__file__).parent))

# ─── Banner ───────────────────────────────────────────────────────────────────

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║       Multi-Domain Support Triage Agent  v1.0               ║
║       HackerRank Orchestrate · May 2026                      ║
╚══════════════════════════════════════════════════════════════╝
Domains: HackerRank | Claude | Visa
"""


# ─── CSV helpers ──────────────────────────────────────────────────────────────

def load_tickets(path: Path) -> list[dict]:
    """Load tickets from CSV; normalize column names."""
    if not path.exists():
        print(f"[ERROR] Input CSV not found: {path}")
        sys.exit(1)
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # normalize keys to lowercase
            norm = {k.strip().lower(): (v or "").strip() for k, v in row.items()}
            rows.append(norm)
    return rows


def write_output(rows: list[dict], path: Path):
    """Write output CSV with required columns."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["status", "product_area", "response", "justification", "request_type"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})
    print(f"\n✅ Output written to: {path}")


# ─── Progress display ─────────────────────────────────────────────────────────

def print_progress(i: int, total: int, status: str, product_area: str):
    bar_len = 30
    filled = int(bar_len * i / max(total, 1))
    bar = "█" * filled + "░" * (bar_len - filled)
    icon = "🔺" if status == "escalated" else "✅"
    print(f"\r[{bar}] {i}/{total} {icon} {product_area[:30]:<30}", end="", flush=True)


def print_ticket_summary(i: int, row: dict, result: dict, elapsed: float):
    """Print a clean summary line for each processed ticket."""
    status_icon = "🔺 ESCALATED" if result["status"] == "escalated" else "✅ REPLIED  "
    print(
        f"  [{i:>3}] {status_icon} | {result['product_area']:<30} | "
        f"{result['request_type']:<15} | {elapsed:.1f}s"
    )


# ─── Single ticket mode ───────────────────────────────────────────────────────

def run_single_ticket(agent, issue: str, subject: str = "", company: str = ""):
    """Interactive single-ticket mode."""
    print(f"\n🎫 Processing ticket...")
    print(f"   Issue: {issue[:100]}")
    start = time.time()
    result = agent.process_ticket(issue=issue, subject=subject, company=company)
    elapsed = time.time() - start

    print("\n" + "─" * 60)
    print(f"  Status       : {result['status'].upper()}")
    print(f"  Product Area : {result['product_area']}")
    print(f"  Request Type : {result['request_type']}")
    print(f"  Response     :\n    {result['response']}")
    print(f"  Justification: {result['justification']}")
    print(f"  Time         : {elapsed:.2f}s")
    print("─" * 60)
    return result


# ─── Batch processing ─────────────────────────────────────────────────────────

def run_batch(
    agent,
    input_path: Path,
    output_path: Path,
    verbose: bool = False,
):
    """Process all tickets from input CSV and write to output CSV."""
    tickets = load_tickets(input_path)
    total = len(tickets)
    print(f"\n📂 Input  : {input_path}")
    print(f"📝 Output : {output_path}")
    print(f"🎫 Tickets: {total}")
    print()

    results = []
    stats = {"replied": 0, "escalated": 0, "errors": 0}
    total_time = 0.0

    for i, ticket in enumerate(tickets, 1):
        issue = ticket.get("issue", "")
        subject = ticket.get("subject", "")
        company = ticket.get("company", "")

        start = time.time()
        try:
            result = agent.process_ticket(
                issue=issue,
                subject=subject,
                company=company,
            )
        except Exception as e:
            print(f"\n[ERROR] Ticket {i}: {e}")
            if verbose:
                traceback.print_exc()
            result = {
                "status": "escalated",
                "product_area": "unknown/error",
                "response": "An internal error occurred while processing this ticket. Please contact support.",
                "justification": f"Processing error: {str(e)[:100]}",
                "request_type": "product_issue",
            }
            stats["errors"] += 1

        elapsed = time.time() - start
        total_time += elapsed
        stats[result["status"]] = stats.get(result["status"], 0) + 1

        if verbose:
            print_ticket_summary(i, ticket, result, elapsed)
        else:
            print_progress(i, total, result["status"], result["product_area"])

        results.append(result)

    print()  # newline after progress bar
    write_output(results, output_path)

    # Summary
    avg_time = total_time / max(total, 1)
    print(f"\n📊 Summary:")
    print(f"   Total    : {total}")
    print(f"   Replied  : {stats['replied']}")
    print(f"   Escalated: {stats['escalated']}")
    print(f"   Errors   : {stats['errors']}")
    print(f"   Avg time : {avg_time:.2f}s/ticket")
    print(f"   Total    : {total_time:.1f}s")


# ─── Main ─────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(
        description="Multi-Domain Support Triage Agent",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--input", type=Path, default=None, help="Path to input CSV")
    p.add_argument("--output", type=Path, default=OUTPUT_CSV, help="Path to output CSV")
    p.add_argument("--sample", action="store_true", help="Run on sample_support_tickets.csv")
    p.add_argument("--verbose", "-v", action="store_true", help="Show per-ticket details")
    p.add_argument("--ticket", type=str, default=None, help="Process a single ticket text")
    p.add_argument("--subject", type=str, default="", help="Subject for --ticket mode")
    p.add_argument("--company", type=str, default="", help="Company for --ticket mode")
    p.add_argument("--data-dir", type=Path, default=DATA_DIR, help="Path to corpus data directory")
    return p.parse_args()


def main():
    print(BANNER)
    args = parse_args()

    # Check API key
    load_env_file()
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("⚠️  WARNING: ANTHROPIC_API_KEY not set. LLM responses will be fallback-only.")
        print("   Set it with: export ANTHROPIC_API_KEY=your_key_here\n")
    else:
        print(f"✅ ANTHROPIC_API_KEY detected (***{api_key[-4:]})\n")

    # Load agent
    from agent import TriageAgent
    agent = TriageAgent(data_dir=args.data_dir, verbose=args.verbose)

    # Single ticket mode
    if args.ticket:
        run_single_ticket(
            agent,
            issue=args.ticket,
            subject=args.subject,
            company=args.company,
        )
        return

    # Batch mode
    if args.sample:
        input_path = SAMPLE_CSV
        output_path = args.output.parent / "sample_output.csv"
    elif args.input:
        input_path = args.input
        output_path = args.output
    else:
        input_path = INPUT_CSV
        output_path = args.output

    run_batch(
        agent=agent,
        input_path=input_path,
        output_path=output_path,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    main()
