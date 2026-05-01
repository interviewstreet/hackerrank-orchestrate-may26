"""
main.py — Entry point for the HackerRank Support Triage Agent.

Run:
    python main.py

Reads:  support_tickets/support_tickets.csv
Writes: output.csv
"""

import sys
import time

from agent import SupportTriageAgent
from config import INPUT_CSV, OUTPUT_CSV
from utils import load_tickets, log, set_seeds, write_output


def main() -> None:
    start_time = time.perf_counter()

    log.section("HackerRank Support Triage Agent — HackerRank Orchestrate May 2026")

    # ── 0. Determinism ────────────────────────────────────────────────────
    set_seeds()

    # ── 1. Load input tickets ─────────────────────────────────────────────
    log.info(f"Loading tickets from: {INPUT_CSV}")
    try:
        tickets = load_tickets(INPUT_CSV)
    except FileNotFoundError:
        log.error(f"Input file not found: {INPUT_CSV}")
        sys.exit(1)

    if not tickets:
        log.warn("No tickets found in CSV. Exiting.")
        sys.exit(0)

    log.success(f"Loaded {len(tickets)} ticket(s).")

    # ── 2. Initialise agent (builds RAG index) ────────────────────────────
    agent = SupportTriageAgent()

    # ── 3. Process all tickets ────────────────────────────────────────────
    results = agent.process_batch(tickets)

    # ── 4. Write output ───────────────────────────────────────────────────
    log.section("Writing Output")
    write_output(OUTPUT_CSV, results)
    log.success(f"Output written to: {OUTPUT_CSV}")

    # ── 5. Summary ────────────────────────────────────────────────────────
    elapsed = time.perf_counter() - start_time
    replied   = sum(1 for r in results if r["status"] == "replied")
    escalated = sum(1 for r in results if r["status"] == "escalated")

    log.section("Run Summary")
    print(f"  Total tickets : {len(results)}")
    print(f"  Replied       : {replied}")
    print(f"  Escalated     : {escalated}")
    print(f"  Elapsed time  : {elapsed:.2f}s")
    print()
    log.success("Done.")


if __name__ == "__main__":
    main()
