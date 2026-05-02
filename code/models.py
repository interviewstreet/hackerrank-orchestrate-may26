"""
models.py — Pydantic v2 schemas for input, output, and retrieved docs.

WHY PYDANTIC:
  LLM or template output must match the output.csv schema exactly.
  Pydantic catches wrong enum values, empty strings, and missing fields
  before they ever reach the CSV.
"""

from typing import Literal
from pydantic import BaseModel, Field, model_validator


# ── Input ─────────────────────────────────────────────────────────────────────

class TicketInput(BaseModel):
    """One row from support_tickets.csv."""
    issue:   str = Field(default="")
    subject: str = Field(default="")
    company: str = Field(default="None")

    @model_validator(mode="after")
    def clean(self) -> "TicketInput":
        self.issue   = (self.issue   or "").strip()
        self.subject = (self.subject or "").strip()
        self.company = (self.company or "None").strip()
        return self

    @property
    def query(self) -> str:
        """Combined text used for BM25 retrieval."""
        parts = [self.issue]
        if self.subject:
            parts.append(self.subject)
        return " ".join(parts)


# ── Retrieved doc chunk ───────────────────────────────────────────────────────

class DocChunk(BaseModel):
    """One BM25-retrieved chunk from the corpus."""
    text:    str
    source:  str
    company: str
    score:   float


# ── Output ────────────────────────────────────────────────────────────────────

class TicketOutput(BaseModel):
    """
    One row written to output.csv.
    All five fields required by problem_statement.md.
    """
    status:        Literal["replied", "escalated"]
    product_area:  str = Field(min_length=1)
    response:      str = Field(min_length=1)
    justification: str = Field(min_length=1)
    request_type:  Literal["product_issue", "feature_request", "bug", "invalid"]


# ── Factories (pre-built deterministic outputs) ───────────────────────────────
# WHY: Escalation and invalid outputs should NEVER touch any retrieval or LLM.
# They are always the same — fast, deterministic, zero risk.

ESCALATION_RESPONSE = (
    "This issue has been escalated to a human support agent who will be in touch shortly. "
    "Please do not share sensitive information such as card numbers, passwords, or "
    "personal identification in follow-up messages."
)

INVALID_RESPONSE = (
    "I'm sorry, this request is outside the scope of what I can help with. "
    "I handle support for HackerRank, Claude, and Visa. If your question relates "
    "to one of these products, please describe your issue and I'll do my best to assist."
)


def make_escalation(
    reason: str,
    product_area: str = "general_support",
    request_type: Literal["product_issue", "feature_request", "bug", "invalid"] = "product_issue",
) -> TicketOutput:
    return TicketOutput(**{
        "status": "escalated",
        "product_area": product_area,
        "response": ESCALATION_RESPONSE,
        "justification": reason,
        "request_type": request_type,
    })


def make_invalid(product_area: str = "general_support") -> TicketOutput:
    return TicketOutput(**{
        "status": "replied",
        "product_area": product_area,
        "response": INVALID_RESPONSE,
        "justification": "Ticket is out of scope or contains no actionable support request.",
        "request_type": "invalid",
    })
