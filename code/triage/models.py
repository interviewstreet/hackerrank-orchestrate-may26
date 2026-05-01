from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class CorpusDoc:
    doc_id: str
    company: str
    product_area: str
    title: str
    source_url: str
    path: str
    content: str
    tokens: List[str] = field(default_factory=list)
    token_freq: Dict[str, int] = field(default_factory=dict)


@dataclass(frozen=True)
class RetrievalHit:
    doc: CorpusDoc
    score: float


@dataclass(frozen=True)
class TicketInput:
    issue: str
    subject: str
    company: str


@dataclass(frozen=True)
class TriageDecision:
    status: str
    product_area: str
    response: str
    justification: str
    request_type: str
