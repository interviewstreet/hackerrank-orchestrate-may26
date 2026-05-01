"""End-to-end triage: retrieval + optional safety overrides + LLM structured output."""

from __future__ import annotations

import os
import re
from typing import Any

from corpus import Chunk, load_chunks
from llm_client import triage
from retrieve import CorpusIndex, build_company_indexes
from safety import SafetyDecision, assess_risk, trivial_invalid_greeting


def _normalize_company(raw: str | float | None) -> str | None:
    if raw is None or (isinstance(raw, float) and str(raw) == "nan"):
        return None
    s = str(raw).strip()
    if not s or s.lower() == "none":
        return None
    lower = s.lower()
    if lower == "hackerrank":
        return "hackerrank"
    if lower == "claude":
        return "claude"
    if lower == "visa":
        return "visa"
    return None


def _format_excerpt(rank: int, chunk: Chunk, score: float) -> str:
    head = f"[{rank}] company={chunk.company} path={chunk.path} title={chunk.title}"
    if chunk.breadcrumbs:
        head += f" breadcrumbs={chunk.breadcrumbs}"
    head += f" score={score:.3f}"
    return f"{head}\n---\n{chunk.text.strip()}\n"


def _validate(pred: dict[str, Any]) -> dict[str, Any]:
    status = str(pred.get("status", "")).strip().lower()
    if status not in ("replied", "escalated"):
        status = "escalated"
    rt = str(pred.get("request_type", "")).strip().lower()
    if rt not in ("product_issue", "feature_request", "bug", "invalid"):
        rt = "product_issue"
    pa = str(pred.get("product_area", "")).strip().lower()
    pa = re.sub(r"[^a-z0-9_]+", "_", pa).strip("_") or "general_support"
    resp = str(pred.get("response", "")).strip()
    jus = str(pred.get("justification", "")).strip()
    return {
        "status": status,
        "product_area": pa,
        "response": resp,
        "justification": jus,
        "request_type": rt,
    }


class SupportAgent:
    def __init__(self, top_k: int | None = None) -> None:
        self.top_k = int(top_k or os.getenv("RETRIEVAL_TOP_K", "8"))
        chunks = load_chunks()
        self.indexes = build_company_indexes(chunks)

    def build_query(self, issue: str, subject: str, company: str | None) -> str:
        parts = [issue.strip(), subject.strip()]
        if company:
            parts.append(company)
        return "\n".join(p for p in parts if p)

    def retrieve(self, query: str, company: str | None) -> list[tuple[Chunk, float]]:
        key = company if company in self.indexes else None
        idx: CorpusIndex = self.indexes[key]  # type: ignore[index]
        return idx.query(query, self.top_k)

    def triage_row(
        self,
        issue: str,
        subject: str,
        company_raw: str | float | None,
        *,
        force_escalate: SafetyDecision | None = None,
    ) -> dict[str, Any]:
        company = _normalize_company(company_raw)

        if trivial_invalid_greeting(issue, subject):
            return {
                "status": "replied",
                "product_area": "general_support",
                "response": "Happy to help — let us know if you need anything else.",
                "justification": "Short acknowledgment with no actionable support request.",
                "request_type": "invalid",
            }

        risk = assess_risk(issue, subject, company)
        eff = force_escalate or risk

        query = self.build_query(issue, subject, company)
        hits = self.retrieve(query, company)
        excerpts = "\n".join(_format_excerpt(i + 1, ch, sc) for i, (ch, sc) in enumerate(hits))

        raw = triage(issue, subject, company, excerpts)
        out = _validate(raw)

        if eff is not None:
            out["status"] = "escalated"
            prev = out["justification"]
            out["justification"] = f"{eff.reason} | {prev}".strip(" |")

        if out["status"] == "escalated" and not out["response"]:
            out["response"] = (
                "Thanks for reaching out. This needs a closer look from our team, "
                "so we've routed your case to a human specialist."
            )

        return out
