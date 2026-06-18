"""Typed records used by the support triage agent."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from support_agent.config import normalize_company


@dataclass(frozen=True)
class SupportTicket:
    """Raw input ticket fields read from `support_tickets.csv`."""

    issue: str
    subject: str
    company: str

    @property
    def normalized_company(self) -> str:
        """Return the canonical lowercase company label for routing."""
        return normalize_company(self.company)


@dataclass(frozen=True)
class TicketPrediction:
    """Final per-ticket prediction written to the output CSV."""

    issue: str
    subject: str
    company: str
    response: str
    product_area: str
    status: str
    request_type: str
    justification: str


@dataclass(frozen=True)
class RetrievedPassage:
    """A scored support passage returned by the corpus retriever."""

    source_path: Path
    company: str
    title: str
    content: str
    score: float = 0.0
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class CorpusDocument:
    """A loaded Markdown support document ready for indexing."""

    source_path: Path
    company: str
    title: str
    content: str
