#!/usr/bin/env python3
"""
Main entry point for Ticket Triage Agent.

Processes support tickets and generates responses using the agent.
"""

import csv
from pathlib import Path
from agent import TicketTriageAgent

# Configuration
DATA_DIR = Path(__file__).parent.parent / "data"
SUPPORT_TICKETS_DIR = Path(__file__).parent.parent / "support_tickets"
INPUT_CSV = SUPPORT_TICKETS_DIR / "support_tickets.csv"
OUTPUT_CSV = SUPPORT_TICKETS_DIR / "output.csv"




def process_tickets(agent: TicketTriageAgent):
    """Process support tickets using agent and write output."""
    rows = []
    
    try:
        with open(INPUT_CSV, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                issue = row.get("Issue", "").strip()
                subject = row.get("Subject", "").strip()
                company = row.get("Company", "").strip()
                
                # Process ticket with agent
                result = agent.process_ticket(issue, subject, company)
                rows.append(result)
    
    except Exception as e:
        print(f"Error processing tickets: {e}")
        raise
    
    # Write output
    try:
        with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ["Status", "Product_Area", "Response", "Justification", "Request_Type"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"✓ Processed {len(rows)} tickets. Output written to {OUTPUT_CSV}")
    except Exception as e:
        print(f"Error writing output: {e}")
        raise


def main():
    """Main entry point."""
    print("Initializing Ticket Triage Agent...")
    agent = TicketTriageAgent(DATA_DIR)
    stats = agent.get_corpus_stats()
    print(f"✓ Loaded {stats['total_chunks']} corpus chunks")
    print(f"  - HackerRank: {stats['hackerrank_chunks']}")
    print(f"  - Claude: {stats['claude_chunks']}")
    print(f"  - Visa: {stats['visa_chunks']}")
    
    print("\nProcessing support tickets...")
    process_tickets(agent)
    print("✓ Done!")


if __name__ == "__main__":
    main()
