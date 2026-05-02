"""
logger.py — AGENTS.md §5 compliant structured log writer.
"""

import sys
from datetime import datetime
from pathlib import Path

from loguru import logger as _loguru_logger

from config import LOG_FILE, LOG_DIR

def setup_logging(log_level: str = "INFO") -> None:
    _loguru_logger.remove()
    _loguru_logger.add(sys.stderr, level=log_level, format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | {message}")

class AgentLogger:
    def __init__(self) -> None:
        LOG_DIR.mkdir(parents=True, exist_ok=True)

    def _now(self) -> str:
        return datetime.now().astimezone().isoformat(timespec="seconds")

    def _append(self, text: str) -> None:
        with open(LOG_FILE, "a", encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")

    def session_start(self) -> None:
        self._append(f"\n## {self._now()} SESSION START\n\nAgent: Antigravity\nRepo Root: {Path.cwd().resolve()}\nLanguage: py\n")

    def ticket_turn(self, row_num: int, company: str, status: str, request_type: str, product_area: str, safety_triggered: bool, safety_reason: str, top_retrieval_score: float, num_chunks: int) -> None:
        safety_info = f"Safety gate triggered: {safety_reason}" if safety_triggered else "Safety gate: passed"
        entry = f"""
## {self._now()} Ticket #{row_num} | {company.title()} | {status.upper()} | {request_type}

User Prompt (verbatim, secrets redacted):
[Ticket #{row_num} — company={company}, content redacted]

Agent Response Summary:
Processed ticket #{row_num}. Decision: status={status}, request_type={request_type}, product_area={product_area}. {safety_info}. Retrieval: top_score={top_retrieval_score:.3f}.

Actions:
* classifier.detect_company → {company}
* safety.check → escalate={safety_triggered}
* retriever.retrieve → {num_chunks} chunks
* agent.generate_response → {status}

Context:
tool=Antigravity
repo_root={Path.cwd().resolve()}
"""
        self._append(entry)

    def session_end(self, total: int, replied: int, escalated: int, elapsed: float) -> None:
        self._append(f"\n## {self._now()} Batch Complete\n\nProcessed {total} tickets in {elapsed:.1f}s. Replied: {replied}, Escalated: {escalated}.\n")

    def log_error(self, row_num: int, error: str) -> None:
        self._append(f"\n## {self._now()} ERROR on Ticket #{row_num}\n\nFailed. Error: {str(error)}.\n")
