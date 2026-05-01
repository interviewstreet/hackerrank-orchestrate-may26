"""CLI entry point for the HackerRank Orchestrate triage agent.

This module is the canonical entry point per AGENTS.md section 6.1
("Project Contract: Evaluable Submission"). The evaluator invokes
``python code/main.py`` to drive the full pipeline end-to-end.

Iter 0 (this file): argparse scaffolding only. No business logic.
Iter 6 wires the pipeline (loader -> preprocessor -> classifier ->
retriever -> reasoner -> escalation -> output_writer).

PRD references: FR-001, FR-006, FR-060..FR-064, AC-1, AC-2.
Architecture references: section 3.1, section 6.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    """Construct the CLI argument parser.

    Flags mirror Architecture section 3.1.
    """
    parser = argparse.ArgumentParser(
        prog="python code/main.py",
        description="HackerRank Orchestrate support triage agent.",
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("support_tickets/support_tickets.csv"),
        help="Path to input CSV (default: support_tickets/support_tickets.csv).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("support_tickets/output.csv"),
        help="Path to output CSV (default: support_tickets/output.csv).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Process only the first N rows (development flag).",
    )
    parser.add_argument(
        "--rebuild-index",
        action="store_true",
        help="Force corpus reindex before running.",
    )
    parser.add_argument(
        "--trace-dir",
        type=Path,
        default=Path("code/runs"),
        help="Directory for per-run trace JSONL output.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("code/config.yaml"),
        help="Path to config.yaml (default: code/config.yaml).",
    )
    return parser


def run(argv: list[str] | None = None) -> int:
    """Entry point. Returns process exit code.

    Iter 6 implementation: load config, build/load index, iterate tickets,
    write output, print summary. For Iter 0 this is a stub that parses args
    and returns 0.
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    raise NotImplementedError(
        "Iter 6: main.run() will be wired in the integration iteration. "
        f"Parsed args: input={args.input}, output={args.output}."
    )


if __name__ == "__main__":
    raise SystemExit(run())
