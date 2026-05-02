"""Pydantic models for ticket I/O and LLM structured output."""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

Status = Literal["replied", "escalated"]
RequestType = Literal["product_issue", "feature_request", "bug", "invalid"]


class TicketInput(BaseModel):
    issue: str
    subject: str = ""
    company: str = "None"


class ChunkDoc(BaseModel):
    chunk_id: str
    company: str
    product_area: str
    text: str
    source_path: str


class LLMOutput(BaseModel):
    model_config = ConfigDict(extra="ignore")

    status: Status
    product_area: str = Field(min_length=1, max_length=80)
    response: str = Field(min_length=1, max_length=2000)
    justification: str = Field(min_length=1, max_length=500)
    request_type: RequestType
    citations: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)


class RowOutput(BaseModel):
    issue: str
    subject: str
    company: str
    response: str
    product_area: str
    status: str
    request_type: str
    justification: str

    def to_csv_row(self) -> dict[str, str]:
        return self.model_dump()
