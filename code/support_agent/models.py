from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from support_agent.config import normalize_company


@dataclass(frozen=True)
class SupportTicket:
    issue: str
    subject: str
    company: str

    @property
    def normalized_company(self) -> str:
        return normalize_company(self.company)


@dataclass(frozen=True)
class TicketPrediction:
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
    source_path: Path
    company: str
    title: str
    content: str
    score: float = 0.0
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class CorpusDocument:
    source_path: Path
    company: str
    title: str
    content: str
