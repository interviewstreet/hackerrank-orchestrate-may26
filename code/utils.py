"""
utils.py — Shared utility helpers.

Keeps every other module lean: text cleaning, CSV I/O, and a tiny
colour-aware logger that works without external dependencies.
"""

import csv
import os
import re
import random
import numpy as np
from datetime import datetime
from config import OUTPUT_FIELDS, RANDOM_SEED


# ── Determinism ────────────────────────────────────────────────────────────

def set_seeds() -> None:
    """Pin all known random seeds for reproducible runs."""
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    # torch seed set lazily in retriever to avoid import overhead here
    os.environ["PYTHONHASHSEED"] = str(RANDOM_SEED)


# ── Text cleaning ──────────────────────────────────────────────────────────

def clean_text(text: str) -> str:
    """
    Normalise free-form ticket text:
    • lower-case
    • collapse whitespace / newlines
    • strip leading/trailing space
    """
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r"\s+", " ", text)       # collapse whitespace
    text = text.strip()
    return text


def combine_fields(issue: str, subject: str) -> str:
    """Return a single string the pipeline can work with."""
    parts = []
    if subject:
        parts.append(subject.strip())
    if issue:
        parts.append(issue.strip())
    return " | ".join(parts)


# ── CSV helpers ────────────────────────────────────────────────────────────

def load_tickets(path: str) -> list[dict]:
    """
    Load support_tickets.csv into a list of dicts.
    Tolerates extra columns and missing optional ones.
    """
    tickets = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            tickets.append({
                "issue":   row.get("issue", "").strip(),
                "subject": row.get("subject", "").strip(),
                "company": row.get("company", "").strip(),
            })
    return tickets


def write_output(path: str, results: list[dict]) -> None:
    """
    Write the triage results to output.csv.
    Preserves input columns (issue, subject, company) alongside output fields.
    """
    if not results:
        print("[WARN] No results to write.")
        return

    all_keys = list(results[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=all_keys)
        writer.writeheader()
        writer.writerows(results)


# ── Logger ─────────────────────────────────────────────────────────────────

class Logger:
    """
    Minimal structured logger that prints timestamped, colour-coded lines.
    No external dependencies — uses ANSI escape codes.
    """
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    RED    = "\033[91m"
    YELLOW = "\033[93m"
    GREEN  = "\033[92m"
    CYAN   = "\033[96m"
    GREY   = "\033[90m"

    def _ts(self) -> str:
        return datetime.now().strftime("%H:%M:%S")

    def info(self, msg: str) -> None:
        print(f"{self.GREY}[{self._ts()}]{self.RESET} {self.CYAN}INFO{self.RESET}  {msg}")

    def success(self, msg: str) -> None:
        print(f"{self.GREY}[{self._ts()}]{self.RESET} {self.GREEN}OK{self.RESET}    {msg}")

    def warn(self, msg: str) -> None:
        print(f"{self.GREY}[{self._ts()}]{self.RESET} {self.YELLOW}WARN{self.RESET}  {msg}")

    def error(self, msg: str) -> None:
        print(f"{self.GREY}[{self._ts()}]{self.RESET} {self.RED}ERROR{self.RESET} {msg}")

    def section(self, title: str) -> None:
        bar = "─" * 60
        print(f"\n{self.BOLD}{self.CYAN}{bar}\n  {title}\n{bar}{self.RESET}")


log = Logger()
