#!/usr/bin/env python3
"""Terminal entry point: triage CSV tickets using local corpus + LLM."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

from agent import SupportAgent


def _default_paths() -> tuple[Path, Path]:
    root = Path(__file__).resolve().parent.parent
    return (
        root / "support_tickets" / "support_tickets.csv",
        root / "support_tickets" / "output.csv",
    )


def main(argv: list[str] | None = None) -> int:
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")

    default_in, default_out = _default_paths()
    p = argparse.ArgumentParser(description="Support triage agent (corpus-grounded).")
    p.add_argument("--input", type=Path, default=default_in)
    p.add_argument("--output", type=Path, default=default_out)
    p.add_argument("--limit", type=int, default=0, help="Process only first N rows (0=all).")
    p.add_argument("--top-k", type=int, default=int(os.getenv("RETRIEVAL_TOP_K", "8")))
    args = p.parse_args(argv)

    df = pd.read_csv(args.input, dtype=str).fillna("")
    if args.limit > 0:
        df = df.head(args.limit)

    agent = SupportAgent(top_k=args.top_k)

    rows: list[dict[str, str]] = []
    total = len(df)
    for i, rec in enumerate(df.itertuples(index=False), start=1):
        issue = str(getattr(rec, "Issue", "") or "")
        subject = str(getattr(rec, "Subject", "") or "")
        company = str(getattr(rec, "Company", "") or "")
        pred = agent.triage_row(issue, subject, company)
        rows.append(
            {
                "Issue": issue,
                "Subject": subject,
                "Company": company,
                "status": pred["status"],
                "product_area": pred["product_area"],
                "response": pred["response"],
                "justification": pred["justification"],
                "request_type": pred["request_type"],
            }
        )
        print(f"[{i}/{total}] status={pred['status']} area={pred['product_area']}", file=sys.stderr)

    out = pd.DataFrame(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)
    print(f"Wrote {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
