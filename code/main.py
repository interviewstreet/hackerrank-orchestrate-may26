"""CLI entry point — runs the agent over support_tickets.csv → output.csv."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv
from tqdm import tqdm

import config
from agent import SupportAgent
from corpus import build_company_product_areas, load_corpus
from io_csv import open_output_writer, read_input_tickets
from retriever import make_retriever


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="python main.py",
                                description="HackerRank Orchestrate triage agent")
    p.add_argument("--input", type=Path, default=config.INPUT_CSV)
    p.add_argument("--output", type=Path, default=config.OUTPUT_CSV)
    p.add_argument("--data-dir", type=Path, default=config.DATA_DIR)
    p.add_argument("--limit", type=int, default=0,
                   help="Process only first N tickets (0 = all)")
    p.add_argument("--resume", action="store_true",
                   help="Skip rows whose 'issue' is already in --output")
    p.add_argument("--no-embeddings", action="store_true",
                   help="Use TF-IDF instead of sentence-transformers")
    p.add_argument("--model", default=config.ANTHROPIC_MODEL)
    p.add_argument("--dry-run", action="store_true",
                   help="Skip LLM calls; emit pre-rule outcomes only")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = parse_args(argv)

    print(f"[setup] loading corpus from {args.data_dir}", file=sys.stderr)
    chunks = load_corpus(args.data_dir,
                         chunk_size_tokens=config.CHUNK_SIZE_TOKENS,
                         overlap_chars=config.CHUNK_OVERLAP_CHARS)
    print(f"[setup] {len(chunks)} chunks", file=sys.stderr)
    if not chunks:
        print("[error] no corpus chunks loaded", file=sys.stderr)
        return 2

    use_emb = not args.no_embeddings
    retriever = make_retriever(chunks, cache_dir=config.CACHE_DIR,
                               use_embeddings=use_emb,
                               model_name=config.EMBED_MODEL_NAME)
    company_areas = build_company_product_areas(chunks)
    agent = SupportAgent(retriever, company_areas, model=args.model)

    tickets = read_input_tickets(args.input)
    if args.limit:
        tickets = tickets[: args.limit]
    print(f"[setup] {len(tickets)} input tickets", file=sys.stderr)

    f, writer, existing = open_output_writer(args.output, config.OUTPUT_HEADER,
                                             resume=args.resume)
    try:
        for t in tqdm(tickets, desc="triage", unit="ticket"):
            if args.resume and t.issue in existing:
                continue
            if args.dry_run:
                from agent import _normalize_company  # type: ignore
                from escalation import pre_check
                t.company = _normalize_company(t.company)
                pre = pre_check(t)
                row = agent._row(
                    t,
                    status="escalated" if pre.decision == "escalated" else "replied",
                    response=pre.message or "(dry-run pass)",
                    product_area=agent._default_area(t.company),
                    request_type=("invalid" if pre.decision == "invalid_reply"
                                  else agent._guess_request_type(t)),
                    justification=f"dry-run pre-rule:{pre.rule or 'pass'}",
                )
            else:
                row = agent.resolve(t)
            writer.writerow(row.to_csv_row())
            f.flush()
    finally:
        f.close()

    print(f"[done] wrote {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
