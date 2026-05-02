"""
logger.py — Structured file logger and terminal progress printer.

Responsible for:
  - Writing a timestamped append-only session log to log.txt
  - Formatting one structured block per processed ticket
  - Printing colour-coded per-ticket progress to the terminal
  - Gracefully degrading to plain text when colorama is unavailable
"""

import sys
import threading
from datetime import datetime

from agent.classifier import Classification
from agent.responder import AgentResponse
from agent.safety import SafetyDecision
from corpus.loader import Document

# ---------------------------------------------------------------------------
# Colorama — optional; falls back to plain text if not installed
# ---------------------------------------------------------------------------

try:
    from colorama import Fore, Style, init as _colorama_init
    _colorama_init(autoreset=True)
    _HAS_COLOR = True
except ImportError:
    _HAS_COLOR = False

# Colour mapping for each action type
_ACTION_COLORS: dict[str, str] = {
    "reply":    "\033[92m",   # bright green
    "escalate": "\033[93m",   # bright yellow
}
_RESET = "\033[0m"
_BOLD  = "\033[1m"
_DIM   = "\033[2m"

# Domain badge colours (used if colorama IS available)
_DOMAIN_COLORS: dict[str, str] = {
    "hackerrank": Fore.CYAN    if _HAS_COLOR else "",
    "claude":     Fore.MAGENTA if _HAS_COLOR else "",
    "visa":       Fore.BLUE    if _HAS_COLOR else "",
    "unknown":    Fore.WHITE   if _HAS_COLOR else "",
}


# ---------------------------------------------------------------------------
# TriageLogger — file-based structured logger
# ---------------------------------------------------------------------------


class TriageLogger:
    """Append-only structured logger for the triage agent session.

    Opens log_path in append mode and writes a session header on init.
    Each call to log_ticket() appends one formatted block.
    Call close() at the end of the run to write the session footer.

    Example:
        >>> logger = TriageLogger("log.txt")
        >>> logger.log_ticket("T001", ticket_text, clf, sd, docs, resp)
        >>> logger.close()
    """

    _SEPARATOR = "-" * 60

    def __init__(self, log_path: str = "log.txt") -> None:
        """Open the log file and write the session header."""
        self._path = log_path
        self._lock = threading.Lock()
        self._file = open(log_path, "a", encoding="utf-8")
        
        with self._lock:
            self._write(
                f"\n{'=' * 60}\n"
                f"=== TRIAGE SESSION {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n"
                f"{'=' * 60}\n"
            )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _write(self, text: str) -> None:
        """Write text to the log file and flush immediately.

        Args:
            text: The string to append to the log file.
        """
        self._file.write(text)
        self._file.flush()

    @staticmethod
    def _truncate(text: str, limit: int, suffix: str = "...") -> str:
        """Return text truncated to limit characters with suffix if cut.

        Args:
            text:   Input string.
            limit:  Maximum character count before truncation.
            suffix: String appended when truncation occurs.

        Returns:
            Original text if shorter than limit, else truncated + suffix.
        """
        text = text.replace("\n", " ").replace("\r", "")
        if len(text) <= limit:
            return text
        return text[:limit] + suffix

    @staticmethod
    def _doc_titles(docs: list[Document]) -> str:
        """Return a comma-separated string of document titles.

        Args:
            docs: List of Document objects.

        Returns:
            Comma-separated titles, or "(none)" if list is empty.
        """
        if not docs:
            return "(none)"
        return ", ".join(d.title for d in docs)

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def log_ticket(
        self,
        ticket_id: str,
        ticket_text: str,
        classification: Classification,
        safety_decision: SafetyDecision,
        retrieved_docs: list[Document],
        agent_response: AgentResponse,
    ) -> None:
        """Append a structured log block for one processed ticket.

        Format:
            --- TICKET {ticket_id} ---
            TEXT: {ticket_text[:200]}...
            CLASSIFICATION: domain=... request_type=... product_area=... confidence=...
            RETRIEVED DOCS: N docs | titles: title1, title2
            SAFETY: escalate=... reason=...
            ACTION: reply | escalate
            RESPONSE: {response[:300]}...
            SOURCES: [url1, url2]
            --------------...

        Args:
            ticket_id:      Identifier string for the ticket (e.g. "T001").
            ticket_text:    Raw input text of the ticket.
            classification: Classifier output.
            safety_decision: Safety check output.
            retrieved_docs: BM25 corpus retrieval results.
            agent_response: Final response generated by the responder.
        """
        reason = safety_decision.reason if safety_decision.reason else "(none)"
        sources = agent_response.sources if agent_response.sources else ["(none)"]

        block = (
            f"\n--- TICKET {ticket_id} ---\n"
            f"TEXT: {self._truncate(ticket_text, 200)}\n"
            f"CLASSIFICATION: "
            f"domain={classification.domain} "
            f"request_type={classification.request_type} "
            f"product_area={classification.product_area} "
            f"confidence={classification.confidence:.2f}\n"
            f"RETRIEVED DOCS: {len(retrieved_docs)} docs | "
            f"titles: {self._doc_titles(retrieved_docs)}\n"
            f"SAFETY: escalate={safety_decision.should_escalate} "
            f"reason={reason}\n"
            f"ACTION: {agent_response.action}\n"
            f"RESPONSE: {self._truncate(agent_response.response, 300)}\n"
            f"SOURCES: {sources}\n"
            f"{self._SEPARATOR}\n"
        )
        with self._lock:
            self._write(block)

    def close(self) -> None:
        """Write the session footer and close the log file."""
        with self._lock:
            self._write(
                f"{'=' * 60}\n"
                f"=== SESSION END {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n"
                f"{'=' * 60}\n"
            )
            self._file.close()


# ---------------------------------------------------------------------------
# Terminal progress printer
# ---------------------------------------------------------------------------


def print_progress(ticket_id: str, action: str, domain: str) -> None:
    """Print a one-line colour-coded progress update for each ticket.

    Uses ANSI escape codes directly when colorama is unavailable so that
    terminals that support ANSI still get colour. Falls back to plain text
    if stdout is not a TTY (e.g. redirected to a file).

    Output format:
        [T001] hackerrank | reply
        [T002] visa       | escalate

    Args:
        ticket_id: Identifier string (e.g. "T001").
        action:    "reply" or "escalate".
        domain:    Classified domain ("hackerrank" | "claude" | "visa" | "unknown").
    """
    use_color = sys.stdout.isatty()

    if use_color:
        if _HAS_COLOR:
            domain_color = _DOMAIN_COLORS.get(domain, Fore.WHITE)
            action_color = (
                Fore.GREEN if action == "reply" else Fore.YELLOW
            )
            reset = Style.RESET_ALL
            line = (
                f"{_BOLD}[{ticket_id}]{_RESET} "
                f"{domain_color}{domain:<12}{reset} | "
                f"{action_color}{action}{reset}"
            )
        else:
            # Plain ANSI fallback
            action_code = _ACTION_COLORS.get(action, "")
            line = (
                f"{_BOLD}[{ticket_id}]{_RESET} "
                f"{domain:<12} | "
                f"{action_code}{action}{_RESET}"
            )
    else:
        line = f"[{ticket_id}] {domain:<12} | {action}"

    print(line)
