"""CLI entry point for the HackerRank Orchestrate triage agent.

Per AGENTS.md section 6.1 the evaluator invokes ``python code/main.py``
and the agent reads ``support_tickets/support_tickets.csv``, processes
each ticket end-to-end, and writes ``support_tickets/output.csv``.

PRD references: FR-001, FR-006, FR-060..FR-064, AC-1, AC-2.
Architecture references: section 3.1, section 6.
"""

from __future__ import annotations

import argparse
import os
import random
import sys
import time
import traceback
from pathlib import Path
from typing import Any

import numpy as np
import yaml

# Ensure code/ is on sys.path when invoked as ``python code/main.py``.
_CODE_DIR = Path(__file__).resolve().parent
if str(_CODE_DIR) not in sys.path:
    sys.path.insert(0, str(_CODE_DIR))


def _seed_determinism() -> None:
    random.seed(0)
    np.random.seed(0)
    os.environ.setdefault("PYTHONHASHSEED", "0")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")


def build_parser() -> argparse.ArgumentParser:
    repo_root = _CODE_DIR.parent
    parser = argparse.ArgumentParser(
        prog="python code/main.py",
        description="HackerRank Orchestrate support triage agent.",
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=repo_root / "support_tickets" / "support_tickets.csv",
        help="Path to input CSV (default: support_tickets/support_tickets.csv).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo_root / "support_tickets" / "output.csv",
        help="Path to output CSV (default: support_tickets/output.csv).",
    )
    parser.add_argument("--limit", type=int, default=None, help="Process only N rows.")
    parser.add_argument("--start", type=int, default=0, help="Skip the first N rows.")
    parser.add_argument(
        "--rebuild-index",
        action="store_true",
        help="Force corpus reindex before running.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=_CODE_DIR / "config.yaml",
        help="Path to config.yaml.",
    )
    parser.add_argument(
        "--corpus-root",
        type=Path,
        default=repo_root / "data",
        help="Root directory of the corpus (default: <repo>/data).",
    )
    parser.add_argument(
        "--index-dir",
        type=Path,
        default=_CODE_DIR / "index",
        help="Directory containing chunks.parquet, faiss.index, bm25.pkl.",
    )
    return parser


def _load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _ensure_env() -> None:
    try:
        from dotenv import load_dotenv  # python-dotenv
    except ImportError:
        return
    repo_env = _CODE_DIR.parent / ".env"
    if repo_env.exists():
        load_dotenv(repo_env)


def _ensure_index(corpus_root: Path, index_dir: Path, force: bool) -> None:
    from indexer import build_index

    if force or not (index_dir / "manifest.json").exists():
        print(f"[main] building index at {index_dir} (force={force}) ...", flush=True)
        build_index(corpus_root, index_dir, force=force)
        print("[main] index ready.", flush=True)


def _domain_for_retrieval(classification, domain_min_confidence: float):
    """Architecture §3.6: scope retrieval to inferred domain only when confident."""
    domain = classification.domain
    if domain in {"hackerrank", "claude", "visa"} and classification.domain_confidence >= domain_min_confidence:
        return domain
    return None


def _build_query(cleaned) -> str:
    subj = cleaned.sanitized_subject or ""
    body = cleaned.sanitized_body or ""
    return f"{subj}\n{body}".strip() or subj or body


def _error_row(ticket, exc: BaseException, *, exc_kind: str = "pipeline error"):
    """Build an Escalated/invalid row when a per-ticket exception escapes."""
    from schemas import OutputRow

    return OutputRow(
        issue=ticket.issue,
        subject=ticket.subject,
        company=ticket.company if ticket.company != "None" else "None",
        status="Escalated",
        product_area="uncategorized",
        response="",
        justification=f"trigger T-1: {exc_kind} ({type(exc).__name__}: {str(exc)[:200]}).",
        request_type="invalid",
    )


def _process_ticket(
    ticket,
    *,
    classifier_client,
    reasoner_client,
    retriever,
    config: dict,
):
    """Run one ticket through preprocess -> classify -> retrieve -> reason -> verify -> decide."""
    from classifier import classify
    from escalation import decide
    from preprocessor import clean
    from reasoner import reason
    from schemas import OutputRow
    from verifier import verify_grounding

    retrieval_top_k = int(config.get("retrieval", {}).get("top_k", 6))
    retrieval_min_score = float(config.get("retrieval", {}).get("min_score", 0.32))
    domain_min_confidence = float(
        config.get("classification", {}).get("min_confidence", 0.6)
    )

    cleaned = clean(ticket)
    classification = classify(cleaned, client=classifier_client)

    # Skip retrieval + reasoning for chitchat / injection — they short-circuit
    # in escalation.decide() and don't need corpus chunks.
    skip_retrieval = (
        cleaned.injection_detected
        or classification.is_chitchat_or_trivia
        or classification.is_outage_report
        or classification.is_sensitive
        or classification.is_authorization_violation
    )

    if skip_retrieval:
        retrieved: list = []
        reasoning = None
        grounding_failed = False
    else:
        domain = _domain_for_retrieval(classification, domain_min_confidence)
        retrieved = retriever.search(_build_query(cleaned), domain=domain, k=retrieval_top_k)
        if retrieved and retrieved[0].cosine_score >= retrieval_min_score:
            reasoning = reason(cleaned, retrieved, client=reasoner_client)
            if reasoning.can_answer_from_corpus and reasoning.response:
                grounding_failed = not verify_grounding(reasoning.response, retrieved)
            else:
                grounding_failed = False
        else:
            reasoning = None
            grounding_failed = False

    decision = decide(
        cleaned=cleaned,
        classification=classification,
        retrieval=retrieved,
        reasoning=reasoning,
        grounding_failed=grounding_failed,
        retrieval_min_score=retrieval_min_score,
        domain_min_confidence=domain_min_confidence,
    )

    return OutputRow(
        issue=ticket.issue,
        subject=ticket.subject,
        company=ticket.company,
        status=decision.status,
        product_area=decision.final_product_area,
        response=decision.final_response,
        justification=decision.final_justification,
        request_type=decision.final_request_type,
    )


def run(argv: list[str] | None = None) -> int:
    _seed_determinism()
    parser = build_parser()
    args = parser.parse_args(argv)

    _ensure_env()
    if not os.getenv("ANTHROPIC_API_KEY"):
        print(
            "ERROR: ANTHROPIC_API_KEY is not set. Copy .env.example to .env and "
            "fill in your key, or export ANTHROPIC_API_KEY in your shell.",
            file=sys.stderr,
        )
        return 2

    config = _load_config(args.config)

    _ensure_index(args.corpus_root, args.index_dir, force=args.rebuild_index)

    # Construct one shared Anthropic client; reuse across all tickets.
    import anthropic

    client = anthropic.Anthropic()

    from loader import load_tickets
    from output_writer import write_output
    from retriever import Retriever

    print(f"[main] loading retriever from {args.index_dir} ...", flush=True)
    retriever = Retriever(args.index_dir)

    print(f"[main] loading tickets from {args.input} ...", flush=True)
    tickets = load_tickets(args.input)
    if args.start:
        tickets = tickets[args.start :]
    if args.limit is not None:
        tickets = tickets[: args.limit]
    print(f"[main] processing {len(tickets)} ticket(s) ...", flush=True)

    rows = []
    n_replied = 0
    n_escalated = 0
    n_errors = 0
    started = time.time()

    for i, ticket in enumerate(tickets, start=1):
        t0 = time.time()
        try:
            row = _process_ticket(
                ticket,
                classifier_client=client,
                reasoner_client=client,
                retriever=retriever,
                config=config,
            )
        except Exception as exc:  # per-ticket exception isolation (FR-061)
            traceback.print_exc(file=sys.stderr)
            row = _error_row(ticket, exc)
            n_errors += 1

        rows.append(row)
        if row.status == "Replied":
            n_replied += 1
        else:
            n_escalated += 1
        dt = time.time() - t0
        print(
            f"[main] {i:>3}/{len(tickets)} {row.status:>9} "
            f"req={row.request_type:<15} pa={row.product_area:<25} ({dt:.1f}s)",
            flush=True,
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    write_output(rows, args.output)
    elapsed = time.time() - started
    print(
        f"[main] done in {elapsed:.1f}s -> {args.output} "
        f"(replied={n_replied}, escalated={n_escalated}, errors={n_errors})",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
