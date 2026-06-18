"""Command-line interface for generating or validating ticket predictions."""

from __future__ import annotations

import argparse
from pathlib import Path

from support_agent.defaults import build_default_agent
from support_agent.io import read_tickets, write_predictions
from support_agent.validation import validate_output_file


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser for generation and validation modes."""
    parser = argparse.ArgumentParser(description="HackerRank Orchestrate support agent scaffold")
    parser.add_argument("--input", type=Path, default=Path("support_tickets/support_tickets.csv"))
    parser.add_argument("--output", type=Path, default=Path("support_tickets/output.csv"))
    parser.add_argument("--corpus-root", type=Path, default=Path("data"))
    parser.add_argument(
        "--validate-output",
        action="store_true",
        help="Validate an existing output CSV instead of generating predictions.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the agent or validate an existing output file from the command line."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.validate_output:
        issues = validate_output_file(args.input, args.output)
        if not issues:
            print("Validation passed")
            return 0

        for issue in issues:
            location = []
            if issue.row_index is not None:
                location.append(f"row={issue.row_index}")
            if issue.column is not None:
                location.append(f"column={issue.column}")
            prefix = f"[{', '.join(location)}] " if location else ""
            print(f"{prefix}{issue.message}")
        return 1

    tickets = read_tickets(args.input)
    agent = build_default_agent(args.corpus_root)
    try:
        predictions = agent.process_tickets(tickets)
    except NotImplementedError as exc:
        print(str(exc))
        return 1

    write_predictions(args.output, predictions)
    print(f"Wrote {len(predictions)} predictions to {args.output}")
    return 0
