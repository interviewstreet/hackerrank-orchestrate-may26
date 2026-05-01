#!/usr/bin/env python3
"""Runner for the modular SupportTicketAgent in `code/agent.py`."""

import sys
from pathlib import Path

# Ensure `code/` is on sys.path so local modules import reliably when running
CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from agent import SupportTicketAgent


def main():
    agent = SupportTicketAgent(corpus_path="../data")
    repo_root = CODE_DIR.parent
    input_file = str(repo_root / "support_tickets" / "support_tickets.csv")
    output_file = str(repo_root / "support_tickets" / "output.csv")

    print("Starting ticket triage...")
    agent.process_csv(input_file, output_file)
    print("✓ Triage complete")


if __name__ == "__main__":
    main()
