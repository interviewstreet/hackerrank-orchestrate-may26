"""
main.py — Fast, lean orchestrator using BM25 and Rules.
"""

import argparse
import sys
import time
from pathlib import Path

import pandas as pd
from loguru import logger
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

sys.path.insert(0, str(Path(__file__).parent))

from config import INPUT_CSV, OUTPUT_CSV, SAMPLE_CSV, DEFAULT_PRODUCT_AREA
from models import TicketInput, make_escalation
from classifier import detect_company, classify_request_type, infer_product_area
from safety import check as safety_check
from retriever import get_retriever
from agent import generate_response
from logger import AgentLogger, setup_logging

console = Console()
OUTPUT_COLUMNS = ["status", "product_area", "response", "justification", "request_type"]


def process_ticket(ticket: TicketInput, retriever, row_num: int, agent_logger: AgentLogger):
    try:
        # 1. Classify
        company = detect_company(ticket.issue, ticket.subject, ticket.company)
        request_type = classify_request_type(ticket.issue, ticket.subject)
        product_area = infer_product_area(ticket.issue, company)

        # 2. Safety Gate
        safety_result = safety_check(ticket.issue, ticket.subject, request_type, product_area)
        if safety_result.escalate or (safety_result.output and safety_result.output.status == "replied"):
            agent_logger.ticket_turn(
                row_num, company, safety_result.output.status, request_type, product_area,
                True, safety_result.reason, 0.0, 0
            )
            return safety_result.output

        # 3. Retrieve
        search_company = company if company != "unknown" else None
        chunks = retriever.retrieve(ticket.query, company=search_company)

        # 4. Confidence check
        if retriever.is_low_confidence(chunks):
            reason = f"No relevant docs found (score: {retriever.top_score(chunks):.2f})."
            output = make_escalation(reason, product_area, request_type)
            agent_logger.ticket_turn(row_num, company, output.status, output.request_type, output.product_area, True, reason, retriever.top_score(chunks), len(chunks))
            return output

        # 5. Generate Response (LLM Synthesizer)
        output = generate_response(ticket, chunks, product_area, request_type)
        agent_logger.ticket_turn(row_num, company, output.status, output.request_type, output.product_area, False, "", retriever.top_score(chunks), len(chunks))
        return output

    except Exception as e:
        logger.error(f"[#{row_num}] Error: {e}")
        agent_logger.log_error(row_num, str(e))
        return make_escalation(f"Error processing: {e}", DEFAULT_PRODUCT_AREA.get(ticket.company, "general_support"), "product_issue")


def run_batch(input_path: Path, output_path: Path, agent_logger: AgentLogger):
    df = pd.read_csv(input_path, keep_default_na=False)
    df.columns = [c.strip().lower() for c in df.columns]
    if "subject" not in df.columns: df["subject"] = ""

    total = len(df)
    console.print(f"\n[cyan]Processing {total} tickets (Fast BM25 Mode)[/cyan]\n")

    retriever = get_retriever()
    retriever.build()

    results = []
    replied = escalated = 0
    t0 = time.time()

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), TaskProgressColumn(), console=console) as progress:
        task = progress.add_task("Processing…", total=total)
        for i, row in enumerate(df.itertuples(index=False), 1):
            ticket = TicketInput(issue=str(getattr(row, "issue", "")), subject=str(getattr(row, "subject", "")), company=str(getattr(row, "company", "None")))
            progress.update(task, description=f"#{i}/{total} [{ticket.company}]", advance=1)
            
            output = process_ticket(ticket, retriever, i, agent_logger)
            results.append({
                "status": output.status, "product_area": output.product_area,
                "response": output.response, "justification": output.justification,
                "request_type": output.request_type
            })
            if output.status == "replied": replied += 1
            else: escalated += 1
            
            # Respect Gemini Free Tier limits (15 RPM = 1 request every 4 seconds)
            if i < total:
                time.sleep(4)

    pd.DataFrame(results, columns=OUTPUT_COLUMNS).to_csv(output_path, index=False)
    elapsed = time.time() - t0
    agent_logger.session_end(total, replied, escalated, elapsed)
    console.print(f"\n[green]✓ Done in {elapsed:.1f}s[/green] | Replied: {replied} | Escalated: {escalated}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=INPUT_CSV)
    parser.add_argument("--output", type=Path, default=OUTPUT_CSV)
    parser.add_argument("--sample", action="store_true")
    args = parser.parse_args()

    setup_logging("WARNING")
    logger = AgentLogger()
    logger.session_start()
    run_batch(SAMPLE_CSV if args.sample else args.input, args.output, logger)
