"""Eval against sample_support_tickets.csv (10 gold rows)."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from dotenv import load_dotenv

import config
from agent import SupportAgent
from corpus import build_company_product_areas, load_corpus
from io_csv import read_sample_gold
from retriever import make_retriever
from schemas import TicketInput


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    p = argparse.ArgumentParser()
    p.add_argument("--sample", type=Path, default=config.SAMPLE_CSV)
    p.add_argument("--data-dir", type=Path, default=config.DATA_DIR)
    p.add_argument("--no-embeddings", action="store_true")
    p.add_argument("--model", default=config.ANTHROPIC_MODEL)
    args = p.parse_args(argv)

    chunks = load_corpus(args.data_dir, config.CHUNK_SIZE_TOKENS,
                         config.CHUNK_OVERLAP_CHARS)
    retriever = make_retriever(chunks, cache_dir=config.CACHE_DIR,
                               use_embeddings=not args.no_embeddings,
                               model_name=config.EMBED_MODEL_NAME)
    agent = SupportAgent(retriever, build_company_product_areas(chunks),
                         model=args.model)

    gold = read_sample_gold(args.sample)
    print(f"[eval] {len(gold)} gold rows")

    status_hits = req_hits = area_hits = 0
    confusion_status: Counter[tuple[str, str]] = Counter()
    confusion_req: Counter[tuple[str, str]] = Counter()

    for g in gold:
        t = TicketInput(issue=g["issue"], subject=g["subject"],
                        company=g["company"])
        pred = agent.resolve(t)
        s_hit = pred.status == g["status"]
        r_hit = pred.request_type == g["request_type"]
        a_hit = pred.product_area.lower() == (g["product_area"] or "").lower()
        status_hits += s_hit
        req_hits += r_hit
        area_hits += a_hit
        confusion_status[(g["status"], pred.status)] += 1
        confusion_req[(g["request_type"], pred.request_type)] += 1
        mark = "✓" if (s_hit and r_hit) else "✗"
        print(f"{mark} company={g['company']:10s} "
              f"status:{g['status']}->{pred.status} "
              f"req:{g['request_type']}->{pred.request_type} "
              f"area:{g['product_area']}->{pred.product_area}")

    n = len(gold) or 1
    print()
    print(f"status accuracy:        {status_hits}/{n} = {status_hits/n:.2f}")
    print(f"request_type accuracy:  {req_hits}/{n} = {req_hits/n:.2f}")
    print(f"product_area accuracy:  {area_hits}/{n} = {area_hits/n:.2f}")
    print(f"status confusion:       {dict(confusion_status)}")
    print(f"request_type confusion: {dict(confusion_req)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
