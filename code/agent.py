"""
Orchestrator — CLI entry point and pipeline coordinator.
No LLM calls. Drives Gatekeeper → Scout → Sentinel → Anchor → Verifier.

Usage:
    python agent.py                              (from inside code/)
    python code/agent.py                         (from repo root)
    python code/agent.py path/to/tickets.csv     (explicit tickets file)

    # One-shot query
    python agent.py --query "I can't log in to my account" [--company HackerRank] [--subject "Login issue"]

    # Interactive REPL
    python agent.py --interactive

Reads:  tickets CSV (arg or default: <code_dir>/support_tickets/support_tickets.csv)
Writes: <repo_root>/support_tickets/output.csv  if that dir exists,
        otherwise ./out/output.csv
"""

import argparse
import csv
import os
import sys
import textwrap
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

# Allow running as `python code/agent.py` from repo root
sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv

load_dotenv()

import anchor
import gatekeeper
import scout
import sentinel
import verifier
from model_client import ModelClient, ModelClientError
from retriever import index_exists_for_all_companies, retrieve

_CODE_DIR = Path(__file__).parent

ESCALATION_RESPONSE = "Escalate to a human"
OUTPUT_COLUMNS = ["status", "product_area", "response", "justification", "request_type"]
TOP_K = int(os.environ.get("RETRIEVAL_TOP_K", "5"))
BULK_CONCURRENCY = int(os.environ.get("BULK_CONCURRENCY", "10"))


def _resolve_paths(tickets_arg: str | None) -> tuple[Path, Path]:
    if tickets_arg:
        tickets_path = Path(tickets_arg).resolve()
    else:
        # Check repo root's support_tickets/ first, then code/support_tickets/
        candidates = [
            _CODE_DIR.parent / "support_tickets" / "support_tickets.csv",
            _CODE_DIR / "support_tickets" / "support_tickets.csv",
        ]
        tickets_path = next((p for p in candidates if p.exists()), None)
        if tickets_path is None:
            checked = "\n  ".join(str(p) for p in candidates)
            print(
                f"ERROR: support_tickets.csv not found. Checked:\n  {checked}\n"
                "Please provide the path explicitly:\n"
                "  python code/agent.py path/to/support_tickets.csv",
                file=sys.stderr,
            )
            sys.exit(1)

    sibling_support = _CODE_DIR.parent / "support_tickets"
    if sibling_support.is_dir():
        output_path = sibling_support / "output.csv"
    else:
        output_path = Path.cwd() / "out" / "output.csv"

    return tickets_path, output_path


def _check_env() -> None:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key and os.environ.get("MODEL_BACKEND", "openrouter") == "openrouter":
        print(
            "ERROR: OPENROUTER_API_KEY environment variable not set.\n"
            "Set it in .env and re-run: cp .env.example .env && nano .env",
            file=sys.stderr,
        )
        sys.exit(1)


def _check_index() -> bool:
    """Return True if the Qdrant index is ready; False with a warning printed otherwise."""
    ok, msg = index_exists_for_all_companies()
    if not ok:
        print(
            f"WARNING: {msg}\n"
            "Build the index first: python code/build_index.py\n"
            "Running without corpus — all tickets will be escalated to a human.",
            file=sys.stderr,
        )
    return ok


def _check_output_writable(output_path: Path) -> None:
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", newline="", encoding="utf-8") as _:
            pass
    except OSError as exc:
        print(f"ERROR: Cannot write to {output_path}: {exc}", file=sys.stderr)
        sys.exit(1)


def process_ticket(
    row: dict,
    row_index: int,
    total_rows: int,
    client: ModelClient,
    epoch_ms: int,
) -> list[dict]:
    """
    Run the full pipeline for one CSV row.
    Returns a list of output dicts (one per sub-request).
    """
    # Stage 1: Gatekeeper
    gate = gatekeeper.validate(row, row_index, epoch_ms)
    if not gate.ok:
        print(f"[{gate.request_id}] Gatekeeper: schema_violation → escalated", file=sys.stderr)
        return [gatekeeper.make_error_row(gate.request_id, gate.error)]

    # Stage 2: Scout
    scout_out = scout.classify(
        gate.issue,
        gate.subject,
        gate.company,
        client,
        request_id=gate.request_id,
    )

    resolved_company = scout_out["inferred_company"]
    if resolved_company == "None" or resolved_company not in {"HackerRank", "Claude", "Visa"}:
        resolved_company = "None"

    sub_requests = scout_out["sub_requests"]
    output_rows: list[dict] = []

    total_sub = len(sub_requests)
    for sub_idx, sub_req in enumerate(sub_requests, start=1):
        subreq_epoch_ms = int(time.time() * 1000)
        request_id = f"req_{row_index:03d}_{sub_idx}_{subreq_epoch_ms}"

        issue_excerpt = sub_req["issue_excerpt"]
        request_type = sub_req["request_type"]
        product_area = sub_req["product_area"]

        print(
            f"[{request_id}] Processing ticket {row_index}/{total_rows} "
            f"(sub-request {sub_idx}/{total_sub}) — company={resolved_company}"
        )

        # Stage 3: Sentinel
        sentinel_out = sentinel.judge(
            issue_excerpt=issue_excerpt,
            subject=gate.subject,
            company=resolved_company,
            request_type=request_type,
            product_area=product_area,
            client=client,
            request_id=request_id,
        )

        status = sentinel_out["status"]
        justification = sentinel_out["justification"]

        if status == "escalated":
            output_rows.append({
                "status": "escalated",
                "product_area": product_area,
                "response": ESCALATION_RESPONSE,
                "justification": justification,
                "request_type": request_type,
            })
            continue

        # Stage 4: Anchor (only when Sentinel says replied)
        query = f"{issue_excerpt} {product_area}"
        chunks = retrieve(
            query=query,
            company=resolved_company,
            top_k=TOP_K,
            similarity_threshold=0.0,
        )

        # No corpus hits at all (and not an invalid/redirection case) → escalate.
        # Soft-grounding (low score) is delegated to Anchor, which inspects the
        # actual chunk text and self-assesses with grounded=false when needed.
        if not chunks and request_type != "invalid":
            print(
                f"[{request_id}] Orchestrator: no corpus hits → escalated",
                file=sys.stderr,
            )
            output_rows.append({
                "status": "escalated",
                "product_area": product_area,
                "response": ESCALATION_RESPONSE,
                "justification": (
                    justification + " "
                    f"[{request_id}] Corpus has no matching documents for this sub-request."
                ).strip(),
                "request_type": request_type,
            })
            continue

        anchor_out = anchor.generate(
            issue_excerpt=issue_excerpt,
            subject=gate.subject,
            resolved_company=resolved_company,
            product_area=product_area,
            corpus_chunks=chunks,
            request_type=request_type,
            client=client,
            request_id=request_id,
        )

        if not anchor_out["grounded"]:
            output_rows.append({
                "status": "escalated",
                "product_area": product_area,
                "response": ESCALATION_RESPONSE,
                "justification": (
                    justification + " "
                    f"[{request_id}] Corpus does not contain sufficient grounding for this sub-request."
                ).strip(),
                "request_type": request_type,
            })
            continue

        response_text = anchor_out["response"]
        source_doc = anchor_out["source_doc"]
        full_justification = f"{justification} Source: {source_doc}".strip()

        # Stage 5: Verifier (only when grounded=true).
        # For invalid request_type the response is a deliberate polite-redirection
        # that intentionally does NOT answer the user's literal question, so the
        # Verifier (which scores "does this address the request") would always
        # reject it. Skip verification in that case — Anchor's R1 redirection is
        # the contract.
        if request_type == "invalid":
            verifier_out = {"verified": True, "verification_confidence": 1.0, "verification_reason": "redirection"}
        else:
            verifier_out = verifier.verify(
                request_id=request_id,
                issue_excerpt=issue_excerpt,
                response=response_text,
                source_doc=source_doc,
                client=client,
            )

        if not verifier_out["verified"]:
            output_rows.append({
                "status": "escalated",
                "product_area": product_area,
                "response": ESCALATION_RESPONSE,
                "justification": (
                    full_justification + " "
                    f"Verifier rejected response (confidence={verifier_out['verification_confidence']:.2f})."
                ).strip(),
                "request_type": request_type,
            })
            continue

        # All gates passed — emit replied row
        output_rows.append({
            "status": "replied",
            "product_area": product_area,
            "response": response_text,
            "justification": full_justification,
            "request_type": request_type,
        })

    return output_rows


def _print_result(result: dict, idx: int = 1) -> None:
    """Pretty-print a single pipeline result to stdout."""
    status = result["status"].upper()
    bar = "=" * 60
    print(f"\n{bar}")
    print(f"  Result #{idx}  [{status}]")
    print(bar)
    print(f"  Product area : {result['product_area']}")
    print(f"  Request type : {result['request_type']}")
    print(f"  Status       : {result['status']}")
    print()
    response_lines = textwrap.wrap(result["response"], width=70)
    print("  Response:")
    for line in response_lines:
        print(f"    {line}")
    print()
    justification_lines = textwrap.wrap(result["justification"], width=70)
    print("  Justification:")
    for line in justification_lines:
        print(f"    {line}")
    print(bar)


def run_query(
    issue: str,
    subject: str,
    company: str,
    client: ModelClient,
) -> list[dict]:
    """Run the full pipeline for a single free-text query. Returns output rows."""
    row = {"issue": issue, "subject": subject, "company": company}
    epoch_ms = int(time.time() * 1000)
    return process_ticket(row, 1, 1, client, epoch_ms)


def _interactive_loop(client: ModelClient) -> None:
    """Simple REPL: read a query, run the pipeline, print result."""
    print("Interactive support query mode. Type 'quit' or 'exit' to stop.\n")
    idx = 0
    while True:
        try:
            issue = input("Your query: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if issue.lower() in {"quit", "exit", "q"}:
            print("Goodbye.")
            break
        if not issue:
            continue

        subject = input("Subject (optional, press Enter to skip): ").strip()
        company = input("Company [HackerRank / Claude / Visa / None]: ").strip()
        if company not in {"HackerRank", "Claude", "Visa"}:
            company = "None"

        results = run_query(issue, subject, company, client)
        for r in results:
            idx += 1
            _print_result(r, idx)
        print()


def _process_row_safe(
    row: dict,
    i: int,
    total: int,
    client: ModelClient,
    corpus_ready: bool,
) -> list[dict]:
    """Run the full pipeline for one CSV row; never raises — always returns a list."""
    epoch_ms = int(time.time() * 1000)
    if not corpus_ready:
        return [{
            "status": "escalated",
            "product_area": row.get("product_area", ""),
            "response": ESCALATION_RESPONSE,
            "justification": "No corpus index available. Build the index with: python code/build_index.py",
            "request_type": row.get("request_type", ""),
        }]
    try:
        return process_ticket(row, i, total, client, epoch_ms)
    except Exception as exc:
        request_id = f"req_{i:03d}_1_{epoch_ms}"
        print(f"[{request_id}] Orchestrator: unhandled exception: {exc}", file=sys.stderr)
        return [gatekeeper.make_error_row(request_id, str(exc))]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Support ticket resolution pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Modes:\n"
            "  Bulk (default): read TICKETS_CSV and write output.csv\n"
            "  One-shot query: --query TEXT [--subject TEXT] [--company NAME]\n"
            "  Interactive:    --interactive\n\n"
            "Bulk output is written to <repo_root>/support_tickets/output.csv when\n"
            "that directory exists, otherwise to ./out/output.csv."
        ),
    )
    parser.add_argument(
        "tickets",
        nargs="?",
        metavar="TICKETS_CSV",
        help="path to support_tickets.csv (bulk mode, default: support_tickets/support_tickets.csv)",
    )
    parser.add_argument(
        "--query", "-q",
        metavar="TEXT",
        help="run the pipeline for a single query and print the result",
    )
    parser.add_argument(
        "--subject", "-s",
        metavar="TEXT",
        default="",
        help="subject line for --query (optional)",
    )
    parser.add_argument(
        "--company", "-c",
        metavar="NAME",
        default="None",
        choices=["HackerRank", "Claude", "Visa", "None"],
        help="company context for --query (default: None — auto-detected)",
    )
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="start an interactive query REPL",
    )
    args = parser.parse_args()

    _check_env()

    # ── Interactive mode ─────────────────────────────────────────────────────
    if args.interactive:
        _check_index()
        client = ModelClient()
        _interactive_loop(client)
        return

    # ── One-shot query mode ──────────────────────────────────────────────────
    if args.query:
        _check_index()
        client = ModelClient()
        results = run_query(args.query, args.subject, args.company, client)
        for i, r in enumerate(results, start=1):
            _print_result(r, i)
        return

    # ── Bulk CSV mode ────────────────────────────────────────────────────────
    tickets_path, output_path = _resolve_paths(args.tickets)
    corpus_ready = _check_index()
    _check_output_writable(output_path)

    client = ModelClient()

    try:
        with tickets_path.open(encoding="utf-8", errors="replace", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except OSError as exc:
        print(
            f"ERROR: Cannot read {tickets_path}: {exc}\n"
            "Provide the path explicitly: python code/agent.py path/to/support_tickets.csv",
            file=sys.stderr,
        )
        sys.exit(1)

    total = len(rows)
    all_output: list[dict] = []
    pipeline_failures = 0

    print(f"Processing {total} ticket(s) with concurrency={BULK_CONCURRENCY} …")

    with ThreadPoolExecutor(max_workers=BULK_CONCURRENCY) as executor:
        futures = [
            executor.submit(_process_row_safe, row, i, total, client, corpus_ready)
            for i, row in enumerate(rows, start=1)
        ]
        for future in futures:  # iterate in submission order → preserves row ordering
            results = future.result()
            all_output.extend(results)
            for r in results:
                if r["status"] == "escalated" and "pipeline" in r.get("justification", "").lower():
                    pipeline_failures += 1

    try:
        with output_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=OUTPUT_COLUMNS)
            writer.writeheader()
            writer.writerows(all_output)
    except OSError as exc:
        print(f"ERROR: Cannot write to {output_path}: {exc}", file=sys.stderr)
        sys.exit(1)

    if pipeline_failures > total // 2:
        print(
            f"WARNING: {pipeline_failures} of {total} tickets were escalated due to pipeline failures. "
            "Check API status.",
            file=sys.stderr,
        )

    print(f"Done. Wrote {len(all_output)} row(s) to {output_path}")


if __name__ == "__main__":
    main()
