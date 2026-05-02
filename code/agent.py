"""Orchestrator: ticket in → RowOutput out."""
from __future__ import annotations

import re

import config
from escalation import (
    coverage_floor as _coverage_floor,
    post_check,
    pre_check,
)
from llm_client import LLMError, call_llm
from prompts import SYSTEM_PROMPT, render_user_prompt
from retriever import DenseRetriever
from schemas import LLMOutput, RowOutput, TicketInput
from verifier import verify

ASCII_RATIO_FLOOR = 0.85


def _normalize_company(c: str) -> str:
    c = (c or "").strip()
    if c in config.COMPANIES:
        return c
    return "None"


def _is_mostly_non_english(text: str) -> bool:
    if not text:
        return False
    letters = [ch for ch in text if ch.isalpha()]
    if len(letters) < 20:
        return False
    ascii_letters = sum(1 for ch in letters if ord(ch) < 128)
    return ascii_letters / len(letters) < ASCII_RATIO_FLOOR


def _infer_company(ticket: TicketInput, retriever: DenseRetriever) -> str:
    text = f"{ticket.subject}\n{ticket.issue}"
    res = retriever.retrieve(text, company=None, top_k=5)
    if not res.chunks:
        return "None"
    counts: dict[str, float] = {}
    for c, s in zip(res.chunks, res.scores):
        counts[c.company] = counts.get(c.company, 0.0) + max(s, 0.0)
    best = max(counts.items(), key=lambda kv: (kv[1], kv[0]))
    if best[1] < 0.5:
        return "None"
    return best[0]


def _short(s: str, n: int = 240) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


class SupportAgent:
    def __init__(self, retriever: DenseRetriever,
                 company_areas: dict[str, set[str]],
                 model: str | None = None) -> None:
        self.retriever = retriever
        self.company_areas = company_areas
        self.model = model or config.ANTHROPIC_MODEL

    def _allowed_areas(self, company: str) -> list[str]:
        seed = set(config.PRODUCT_AREA_SEED.get(company, []))
        seen = self.company_areas.get(company, set())
        return sorted(seed | seen)

    def resolve(self, ticket: TicketInput) -> RowOutput:
        ticket.company = _normalize_company(ticket.company)
        ticket.subject = (ticket.subject or "").strip()
        ticket.issue = (ticket.issue or "").strip()

        pre = pre_check(ticket)
        if pre.decision == "escalated":
            return self._row(ticket, status="escalated",
                             response="Escalate to a human.",
                             product_area=self._default_area(ticket.company),
                             request_type=self._guess_request_type(ticket),
                             justification=f"Pre-rule:{pre.rule}")
        if pre.decision == "invalid_reply":
            return self._row(ticket, status="replied",
                             response=pre.message,
                             product_area=self._default_area(ticket.company),
                             request_type="invalid",
                             justification=f"Pre-rule:{pre.rule}")

        if ticket.company == "None":
            inferred = _infer_company(ticket, self.retriever)
            company_for_search: str | None = inferred if inferred != "None" else None
        else:
            company_for_search = ticket.company

        if _is_mostly_non_english(ticket.issue) and ticket.company in {"None", "Visa"}:
            return self._row(ticket, status="escalated",
                             response="Escalate to a human.",
                             product_area=self._default_area(ticket.company),
                             request_type=self._guess_request_type(ticket),
                             justification="Non-English content; routing to human.")

        query = f"{ticket.subject}\n{ticket.issue}"
        res = self.retriever.retrieve(query, company=company_for_search,
                                      top_k=config.RETRIEVE_TOP_K)

        if _coverage_floor(res.max_score, res.mean_top3,
                           config.COVERAGE_MAX_FLOOR,
                           config.COVERAGE_MEAN3_FLOOR):
            return self._row(ticket, status="escalated",
                             response="Escalate to a human.",
                             product_area=self._default_area(ticket.company),
                             request_type=self._guess_request_type(ticket),
                             justification=(f"Insufficient corpus coverage "
                                            f"(max={res.max_score:.2f}, "
                                            f"mean3={res.mean_top3:.2f})."))

        allowed = self._allowed_areas(ticket.company if ticket.company != "None"
                                      else (company_for_search or "None"))
        user_prompt = render_user_prompt(ticket, res.chunks, allowed)
        try:
            llm_out = call_llm(SYSTEM_PROMPT, user_prompt, model=self.model)
        except LLMError as e:
            return self._row(ticket, status="escalated",
                             response="Escalate to a human.",
                             product_area=self._default_area(ticket.company),
                             request_type=self._guess_request_type(ticket),
                             justification=f"LLM failure: {e}")

        llm_out = verify(llm_out, res.chunks)

        post = post_check(llm_out, set(allowed),
                          res.max_score, res.mean_top3,
                          config.LLM_CONFIDENCE_FLOOR)
        if post.should_escalate:
            llm_out.status = "escalated"
            llm_out.response = "Escalate to a human."
            llm_out.justification = (f"{llm_out.justification} | "
                                     f"post:{post.reason}").strip()

        if llm_out.product_area not in allowed:
            llm_out.product_area = self._snap_area(llm_out.product_area, allowed)

        return RowOutput(
            issue=ticket.issue,
            subject=ticket.subject,
            company=ticket.company,
            response=llm_out.response,
            product_area=llm_out.product_area,
            status=llm_out.status,
            request_type=llm_out.request_type,
            justification=_short(llm_out.justification, 480),
        )

    @staticmethod
    def _default_area(company: str) -> str:
        return (config.PRODUCT_AREA_SEED.get(company, ["general_support"]) or
                ["general_support"])[0]

    @staticmethod
    def _guess_request_type(ticket: TicketInput) -> str:
        t = f"{ticket.subject} {ticket.issue}".lower()
        if any(w in t for w in ("not working", "broken", "error", "fails", "down",
                                 "doesn't work", "stopped")):
            return "bug"
        if "feature" in t and "request" in t:
            return "feature_request"
        return "product_issue"

    @staticmethod
    def _snap_area(value: str, allowed: list[str]) -> str:
        if not allowed:
            return value or "general_support"
        v = value.lower().replace(" ", "_")
        for a in allowed:
            if a.lower() == v:
                return a
        for a in allowed:
            if v in a.lower() or a.lower() in v:
                return a
        return allowed[0]

    def _row(self, ticket: TicketInput, *, status: str, response: str,
             product_area: str, request_type: str,
             justification: str) -> RowOutput:
        return RowOutput(
            issue=ticket.issue,
            subject=ticket.subject,
            company=ticket.company,
            response=response,
            product_area=product_area,
            status=status,
            request_type=request_type,
            justification=_short(justification, 480),
        )
