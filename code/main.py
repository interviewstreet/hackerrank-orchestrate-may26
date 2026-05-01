#!/usr/bin/env python3
"""
ARIA - Autonomous Routing & Intelligent Agent
Multi-Domain Support Triage CLI

Usage:
  python main.py                            # Default: reads ../support_tickets/support_tickets.csv
  python main.py --input <path>             # Custom input CSV
  python main.py --output <path>            # Custom output CSV
  python main.py --api-key <GROQ_KEY>       # Pass Groq API key directly
  python main.py --quiet                    # Suppress verbose output

Environment variables:
  GROQ_API_KEY    — Groq API key for LLM responses
"""

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aria_agent import ARIAAgent


def resolve_default_path(filename: str) -> str:
    """Find support_tickets/ folder relative to code/ or repo root."""
    script_dir = Path(__file__).parent.resolve()
    candidates = [
        script_dir.parent / "support_tickets" / filename,  # from code/ → ../support_tickets/
        script_dir / "support_tickets" / filename,          # from repo root
        Path("support_tickets") / filename,                 # relative CWD
        Path(filename),                                    # fallback: same dir
    ]
    for c in candidates:
        if c.exists():
            return str(c)
    # Return best guess even if not found yet (output file won't exist yet)
    return str(candidates[0])


def main():
    parser = argparse.ArgumentParser(
        description="ARIA — Multi-Domain Support Triage Agent",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--input",   default=None, help="Input CSV path")
    parser.add_argument("--output",  default=None, help="Output CSV path")
    parser.add_argument("--api-key", default=None, help="Groq API key")
    parser.add_argument("--quiet",   action="store_true", help="Suppress verbose output")
    args = parser.parse_args()

    input_path  = args.input  or resolve_default_path("support_tickets.csv")
    output_path = args.output or resolve_default_path("output.csv")

    api_key = args.api_key or os.environ.get("GROQ_API_KEY", "")

    agent = ARIAAgent(
        groq_api_key=api_key,
        verbose=not args.quiet,
    )

    agent.process_csv(input_path=input_path, output_path=output_path)


if __name__ == "__main__":
    main()
