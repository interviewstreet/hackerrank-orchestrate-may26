"""
Main Orchestrator — HackerRank Orchestrate Support Triage Agent

Clean, single-mode pipeline using Hybrid RAG (FAISS + BM25 + RRF).

Pipeline:
  1. Safety Gate    → Regex-based pre-LLM escalation (4 layers)
  2. Classification → Rule-based company, product area, request type
  3. Retrieval      → Hybrid FAISS+BM25 Ensemble with domain filtering
  4. LLM Response   → OpenRouter (gpt-oss-120b:free) with extractive fallback
  5. Auditor        → Optional second-pass LLM validation (--audit flag)
"""

import argparse
import csv
import json
import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Fix for OMP: Error #15 (Multiple OpenMP runtimes on Windows)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Suppress TF noise
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import warnings
warnings.filterwarnings("ignore")

load_dotenv()

# Force UTF-8 on Windows to avoid charmap errors
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# ---------------------------------------------------------------------------
# Module imports
# ---------------------------------------------------------------------------
from triage import detect_company, classify_product_area, classify_request_type
from gate import check_escalation_signals
from brain import generate_grounded_response, generate_escalation_response
from output import write_output_csv

# Rich UI (optional but makes the terminal output professional)
from rich.console import Console
from rich.rule import Rule
from halo import Halo

console = Console()
VALID_DOMAINS = {"hackerrank", "claude", "visa"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def row_value(row: Dict[str, str], *names: str) -> str:
    """Read a CSV value case-insensitively and tolerate spaces/underscores."""
    normalized = {
        (key or "").strip().lower().replace(" ", "_"): value
        for key, value in row.items()
    }
    for name in names:
        key = name.strip().lower().replace(" ", "_")
        value = normalized.get(key)
        if value is not None:
            return str(value)
    return ""


def typewriter_effect(text: str, speed: float = 0.005) -> None:
    """Print text with typewriter effect for professional terminal output."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\n")


# ---------------------------------------------------------------------------
# Main Agent
# ---------------------------------------------------------------------------

class SupportTriageAgent:
    """
    Production-grade Support Triage Agent.
    
    Uses Hybrid RAG (FAISS + BM25 + RRF) for retrieval and OpenRouter for
    grounded LLM response generation. Safety gates run before retrieval.
    """

    def __init__(self, data_dir: Optional[str] = None, verbose: bool = True, fast_mode: bool = False):
        self.verbose = verbose
        self.fast_mode = fast_mode
        self.hybrid_engine = None
        self.auditor = None  # Backward compatibility if needed

        if self.verbose and not getattr(self, 'fast_mode', False):
            self._show_splash()

        console.print("[bold blue][Agent][/bold blue] Initializing Support Triage Agent...")

        # Resolve data directory
        resolved_data_dir = data_dir or str(Path(__file__).parent.parent / "data")

        # Initialize Hybrid RAG Engine (FAISS + BM25)
        try:
            from engine import HybridEngine
            self.hybrid_engine = HybridEngine(data_dir=resolved_data_dir, verbose=True)
            console.print("[bold green]✓[/bold green] Hybrid RAG Engine [dim](FAISS+BM25)[/dim] active")
        except Exception as e:
            console.print(f"[bold red]✗[/bold red] Hybrid Engine failed: {e}")
            console.print("[bold yellow][Agent][/bold yellow] Agent will use safety-gate-only mode (escalate all).")

        console.print("[bold blue][Agent][/bold blue] Ready.\n")

    def _show_splash(self):
        """Display a professional splash screen."""
        console.print("\n" * 2)
        console.print(r"""[bold green]
  _   _            _             ____              _    
 | | | | __ _  ___| | _____ _ __|  _ \ __ _ _ __ | | __ 
 | |_| |/ _` |/ __| |/ / / _ \ '__| |_) / _` | '_ \| |/ / 
 |  _  | (_| | (__|   <  __/ |  |  _ < (_| | | | |   <  
 |_| |_|\__,_|\___|_|\_\___|_|  |_| \_\__,_|_| |_|_|\_\ 
                                                          
  _____     _                        ____                            _   
 |_   _| __(_) __ _  __ _  ___      / ___| _   _ _ __  _ __   ___  _ __| |_ 
   | || '__| |/ _` |/ _` |/ _ \ ____\___ \| | | | '_ \| '_ \ / _ \| '__| __|
   | || |  | | (_| | (_| |  __/|_____|__) | |_| | |_) | |_) | (_) | |  | |_ 
   |_||_|  |_|\__,_|\__, |\___|     |____/ \__,_| .__/| .__/ \___/|_|   \__|
                    |___/                       |_|   |_|                   
[/bold green]""", justify="center")
        console.print("[bold white]>> HackerRank Orchestrate Triage Agent <<[/bold white]", justify="center")
        console.print("[bold dim]v2.5 · Hybrid RAG · Zero-Cost Scaling[/bold dim]", justify="center")
        console.print("\n" + "━" * console.width, style="bold blue")
        
        # Simple, clean startup delay for "premium" feel
        with console.status("[bold cyan]Spinning up Orchestrator engines...[/bold cyan]"):
            time.sleep(1.2)

    # -----------------------------------------------------------------------
    # Core Pipeline
    # -----------------------------------------------------------------------

    def process_ticket(
        self,
        issue: str,
        subject: str = "",
        company_hint: Optional[str] = None,
    ) -> Dict:
        """Process a single support ticket through the full pipeline."""
        # === Step 1: Safety Gate ===
        should_escalate, escalation_reason = check_escalation_signals(issue, subject)
        if should_escalate:
            company = detect_company(issue, subject, company_hint)
            request_type = classify_request_type(issue, subject)
            product_area = classify_product_area(issue, subject, company)
            res = generate_escalation_response(escalation_reason)
            return {
                "status": "escalated",
                "product_area": product_area,
                "response": res["response"],
                "justification": res["justification"],
                "request_type": request_type
            }

        # === Step 2: Classification ===
        company = detect_company(issue, subject, company_hint)
        request_type = classify_request_type(issue, subject)
        retrieval_domain = company if company in VALID_DOMAINS else None

        # === Step 3: Hybrid Retrieval ===
        if self.hybrid_engine:
            context_str = self.hybrid_engine.get_context_string(f"{issue} {subject}", retrieval_domain)
            raw_docs = self.hybrid_engine.retrieve(f"{issue} {subject}", retrieval_domain)
        else:
            context_str = "No relevant documentation found."
            raw_docs = []

        # Refine product area with retrieved docs
        product_area = classify_product_area(issue, subject, company, raw_docs)

        # Handle empty retrieval
        if context_str == "No relevant documentation found." or not raw_docs:
            res = generate_escalation_response("No matching support documentation found in corpus.")
            return {
                "status": "escalated",
                "product_area": product_area,
                "response": res["response"],
                "justification": res["justification"],
                "request_type": request_type
            }

        # === Step 4: LLM Response Generation ===
        res = generate_grounded_response(
            issue=issue,
            subject=subject,
            company=company,
            product_area=product_area,
            request_type=request_type,
            context_str=context_str,
            openrouter_key=os.environ.get('OPENROUTER_API_KEY'),
            anthropic_key=os.environ.get('ANTHROPIC_API_KEY'),
        )

        # Return only the requested fields
        return {
            "status": res["status"],
            "product_area": product_area,
            "response": res["response"],
            "justification": res["justification"],
            "request_type": request_type
        }

    # -----------------------------------------------------------------------
    # CSV Batch Processing
    # -----------------------------------------------------------------------

    def process_csv(self, input_path: str, output_path: str) -> List[Dict]:
        """Process all tickets from a CSV file and write results."""
        console.print(f"\n[bold magenta][CSV][/bold magenta] Reading from [u]{input_path}[/u]")

        tickets = []
        try:
            with open(input_path, "r", encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f)
                tickets = list(reader)
            console.print(f"[bold magenta][CSV][/bold magenta] Loaded [bold green]{len(tickets)}[/bold green] tickets")
        except Exception as exc:
            console.print(f"[bold red][CSV] Error reading CSV:[/bold red] {exc}")
            return []

        results = []
        total = len(tickets)

        for i, ticket in enumerate(tickets):
            issue = row_value(ticket, "issue").strip()
            subject = row_value(ticket, "subject").strip()
            company = row_value(ticket, "company").strip() or None

            console.print(Rule(f"Ticket {i+1}/{total}", style="blue"))

            try:
                with console.status("[bold cyan]Analyzing and retrieving documentation...[/bold cyan]"):
                    res = self.process_ticket(issue, subject, company)
                    # Small delay for visual clarity in verbose mode
                    if not getattr(self, 'fast_mode', False):
                        time.sleep(0.3)
            except Exception as exc:
                console.print(f"[bold red]Error processing ticket {i+1}:[/bold red] {exc}")
                res = {
                    "status": "escalated",
                    "product_area": "unknown",
                    "response": "Internal processing error. Please contact support.",
                    "justification": f"Exception: {str(exc)}",
                    "request_type": "product_issue"
                }

            # Map back for CSV consistency if needed
            res['issue'] = issue
            res['subject'] = subject
            res['company'] = company or "?"

            # Display result
            console.print(f"[bold cyan]Issue:[/bold cyan] {issue[:120]}...")
            status_color = "green" if res.get('status') == 'replied' else "red"
            console.print(
                f"[bold]Company:[/bold] [yellow]{res.get('company')}[/yellow] | "
                f"[bold]Area:[/bold] [magenta]{res.get('product_area')}[/magenta] | "
                f"[bold]Type:[/bold] [blue]{res.get('request_type')}[/blue] | "
                f"[bold]Status:[/bold] [{status_color}]{res.get('status', '').upper()}[/]"
            )
            
            console.print(f"\n[bold green]Response:[/bold green]")
            if not getattr(self, 'fast_mode', False):
                typewriter_effect(res.get('response', ''), speed=0.002)
            else:
                console.print(res.get('response', ''))
            
            console.print(f"[dim yellow]Justification:[/dim yellow] [italic dim]{res.get('justification')}[/italic dim]\n")

            results.append(res)

        console.print(f"\n[bold magenta][CSV][/bold magenta] Writing results to [u]{output_path}[/u]")
        write_output_csv(results, output_path)

        # Final Summary Table
        replied = sum(1 for r in results if r.get('status') == 'replied')
        escalated = sum(1 for r in results if r.get('status') == 'escalated')
        
        from rich.table import Table
        summary_table = Table(title="Execution Summary", box=None)
        summary_table.add_column("Metric", style="cyan")
        summary_table.add_column("Value", style="bold")
        summary_table.add_row("Total Tickets", str(total))
        summary_table.add_row("Successfully Replied", f"[green]{replied}[/green]")
        summary_table.add_row("Safely Escalated", f"[red]{escalated}[/red]")
        summary_table.add_row("Automation Rate", f"{ (replied/total)*100:.1f}%")
        
        console.print(Rule(style="blue"))
        console.print(summary_table)
        console.print(Rule(style="blue"))

        return results


# ---------------------------------------------------------------------------
# CLI Entry Point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Support Triage Agent — Hybrid RAG Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python main.py --file ../support_tickets/support_tickets.csv --output ../support_tickets/output.csv
  python main.py --ticket "How do I create a test?" --company HackerRank
  python main.py  (interactive mode)
"""
    )
    parser.add_argument("--file", "--files", type=str, help="Input CSV file path")
    parser.add_argument("--output", type=str, help="Output CSV file path")
    parser.add_argument("--ticket", type=str, help="Process a single ticket")
    parser.add_argument("--company", type=str, help="Company hint for single ticket")
    parser.add_argument("--data-dir", type=str, help="Path to data/ directory")
    parser.add_argument("--fast", action="store_true", help="Skip splash screen and animations")
    parser.add_argument("--quiet", action="store_true", help="Suppress verbose output")

    args = parser.parse_args()
    agent = SupportTriageAgent(
        data_dir=args.data_dir,
        verbose=not args.quiet,
        fast_mode=args.fast,
    )

    if args.file:
        agent.process_csv(args.file, args.output or "output.csv")
    elif args.ticket:
        result = agent.process_ticket(args.ticket, company_hint=args.company)
        console.print(json.dumps(result, indent=2))
    else:
        # Interactive mode
        console.print("\n[bold underline]Interactive Agent Session[/bold underline]")
        console.print("[dim]Type 'quit' to exit.[/dim]\n")
        while True:
            console.print(Rule(style="cyan"))
            issue = console.input("[bold yellow]Ticket Issue:[/bold yellow] ").strip()
            if issue.lower() in {"quit", "exit", "q"}:
                break
            
            with console.status("[bold cyan]Agent is thinking and retrieving documentation...[/bold cyan]"):
                res = agent.process_ticket(issue)
                time.sleep(0.5)

            console.print(f"\n[bold green]Response:[/bold green]")
            from rich.panel import Panel
            typewriter_effect(res.get('response', ''))
            
            console.print(Panel(
                f"[bold cyan]Justification:[/bold cyan]\n[italic]{res.get('justification', '')}[/italic]\n\n"
                f"[dim]Status: [bold]{res.get('status').upper()}[/bold] | "
                f"Area: {res.get('product_area')} | "
                f"Type: {res.get('request_type')}[/dim]",
                title="[bold blue]Support Agent Decision[/bold blue]",
                border_style="blue"
            ))
            console.print("\n")


if __name__ == "__main__":
    main()
