#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys

from triage import CorpusIndex, load_corpus, run_batch


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Terminal-based support triage agent using only local support corpus."
    )
    parser.add_argument(
        "--input",
        default="support_tickets/support_tickets.csv",
        help="Input ticket CSV path.",
    )
    parser.add_argument(
        "--output",
        default="support_tickets/output.csv",
        help="Output CSV path for predictions.",
    )
    parser.add_argument(
        "--data-dir",
        default="data",
        help="Path to local support corpus root directory.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    docs = load_corpus(args.data_dir)
    if not docs:
        print(f"No corpus documents found in: {args.data_dir}")
        return 2

    index = CorpusIndex(docs)
    run_batch(args.input, args.output, index)
    print(f"Processed tickets and wrote predictions to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
