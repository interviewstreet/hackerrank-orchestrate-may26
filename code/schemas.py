"""Pydantic v2 DTOs shared across pipeline modules.

These are concrete (not stubs) per Architecture section 4: they are data
classes, and the rest of the pipeline depends on their shape.

All models are frozen so equality and hashing are stable for tests.

PRD references: FR-001..FR-055.
Architecture references: section 4.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Ticket(BaseModel):
    """A single input row from support_tickets.csv."""

    model_config = ConfigDict(frozen=True)

    index: int
    issue: str
    subject: str
    company: Literal["HackerRank", "Claude", "Visa", "None"]
    requires_inference: bool = False


class CleanedTicket(BaseModel):
    """A Ticket after preprocessor sanitization and injection detection."""

    model_config = ConfigDict(frozen=True)

    ticket: Ticket
    sanitized_body: str
    sanitized_subject: str
    injection_detected: bool


class RetrievedDoc(BaseModel):
    """A single retrieved corpus chunk with its scores."""

    model_config = ConfigDict(frozen=True)

    chunk_id: str
    file_path: str
    domain: Literal["hackerrank", "claude", "visa"]
    breadcrumbs: list[str]
    title: str
    text: str
    cosine_score: float
    bm25_score: float
    rrf_score: float


class ClassificationResult(BaseModel):
    """Output of the classifier LLM call (validated against tool schema)."""

    model_config = ConfigDict(frozen=True)

    request_type: Literal["product_issue", "feature_request", "bug", "invalid"]
    domain: Literal["hackerrank", "claude", "visa", "none"]
    domain_confidence: float = Field(ge=0.0, le=1.0)
    product_area: str
    product_area_confidence: float = Field(ge=0.0, le=1.0)
    is_sensitive: bool
    is_outage_report: bool
    is_multi_request: bool
    is_authorization_violation: bool
    is_chitchat_or_trivia: bool


class ReasoningResult(BaseModel):
    """Output of the reasoner LLM call (validated against tool schema)."""

    model_config = ConfigDict(frozen=True)

    can_answer_from_corpus: bool
    response: str
    citations: list[str]
    justification: str
    grounding_failed: bool = False


class EscalationDecision(BaseModel):
    """Output of the deterministic escalation policy decision table."""

    model_config = ConfigDict(frozen=True)

    status: Literal["Replied", "Escalated"]
    triggers_fired: list[str]
    final_request_type: Literal[
        "product_issue", "feature_request", "bug", "invalid"
    ]
    final_response: str
    final_justification: str
    final_product_area: str


class OutputRow(BaseModel):
    """One row of output.csv. Casing enforced by the output writer."""

    model_config = ConfigDict(frozen=True)

    issue: str
    subject: str
    company: str
    status: str
    product_area: str
    response: str
    justification: str
    request_type: str
