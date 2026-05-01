"""
agent.py — Support Triage Agent (Orchestration Layer).

Wires together every module into a single end-to-end pipeline:

  Ticket
    │
    ▼
  Preprocess (clean + combine text)
    │
    ▼
  Risk Detection ──► [high-risk] ──────────────────────────────────────┐
    │                                                                   │
    ▼                                                                   │
  Request-Type Classification                                          │
    │                                                                   │
    ▼                                                                   │
  Product-Area Classification (keyword + semantic)                     │
    │                                                                   │
    ▼                                                                   │
  Multi-Intent Detection                                               │
    │                                                                   │
    ▼                                                                   │
  Retriever (RAG, top-3 chunks)                                        │
    │                                                                   │
    ▼                                                                   │
  Decision Engine ◄──────────────────────────────────────────────────┘
    │
    ▼
  Response Generator
    │
    ▼
  Output row: {status, product_area, response, justification, request_type}
"""

from __future__ import annotations

from typing import Optional

from classifier import (
    ProductAreaClassifier,
    RequestTypeClassifier,
    RiskDetector,
    detect_multi_intent,
)
from config import TOP_K_DOCS
from decision import DecisionEngine, TicketContext
from generator import ResponseGenerator
from retriever import Retriever
from utils import clean_text, combine_fields, log


class SupportTriageAgent:
    """
    Stateful agent — build once, process many tickets.

    The retrieval index is built during __init__; subsequent calls to
    process_ticket() reuse the index for efficiency.
    """

    def __init__(self) -> None:
        log.section("Initialising Support Triage Agent")

        # Build retriever (loads corpus + encodes chunks)
        self.retriever = Retriever()
        self.retriever.build_index()

        # Classifiers
        self.risk_detector     = RiskDetector()
        self.req_type_clf      = RequestTypeClassifier()
        self.product_area_clf  = ProductAreaClassifier()

        # Decision + generation
        self.decision_engine   = DecisionEngine()
        self.generator         = ResponseGenerator()

        log.success("Agent ready.\n")

    # ── Public API ─────────────────────────────────────────────────────────

    def process_ticket(self, issue: str, subject: str, company: str = "") -> dict:
        """
        Run a single ticket through the full pipeline.

        Parameters
        ----------
        issue   : free-form description from the customer.
        subject : ticket subject line.
        company : customer's company name (used for context / logging only).

        Returns
        -------
        Dict with keys: status, product_area, response, justification, request_type
        (plus the original input fields preserved for the output CSV).
        """
        log.info(f"Processing ticket — company={company!r}, subject={subject!r}")

        # ── Step 1: Preprocess ─────────────────────────────────────────────
        combined_raw   = combine_fields(issue, subject)
        combined_clean = clean_text(combined_raw)

        # ── Step 2: Risk Detection ─────────────────────────────────────────
        is_high_risk, risk_category = self.risk_detector.detect(combined_raw)

        # ── Step 3: Request-Type Classification ───────────────────────────
        request_type = self.req_type_clf.classify(combined_clean)

        # ── Step 4: Product-Area Classification ───────────────────────────
        product_area = self.product_area_clf.classify(
            combined_clean, retriever=self.retriever
        )

        # ── Step 5: Multi-Intent Detection ────────────────────────────────
        intents = detect_multi_intent(combined_clean)

        # ── Step 6: Retrieval (RAG) ────────────────────────────────────────
        # Even for high-risk tickets we retrieve — the decision engine may
        # still use the best doc for the justification.
        retrieved_docs = self.retriever.retrieve(combined_clean, top_k=TOP_K_DOCS)
        log.info("Retrieved docs:\n" + self.retriever.pretty_results(retrieved_docs))

        # ── Step 7: Build TicketContext ────────────────────────────────────
        ctx = TicketContext(
            raw_text=combined_raw,
            clean_text=combined_clean,
            request_type=request_type,
            product_area=product_area,
            is_high_risk=is_high_risk,
            risk_category=risk_category,
            intents=intents,
            retrieved_docs=retrieved_docs,
        )

        # ── Step 8: Decision Engine ────────────────────────────────────────
        decision = self.decision_engine.evaluate(ctx)

        # ── Step 9: Response Generation ───────────────────────────────────
        response = self.generator.generate(ctx, decision)

        # ── Step 10: Assemble output row ──────────────────────────────────
        return {
            # Original input fields (for traceability in output CSV)
            "issue":        issue,
            "subject":      subject,
            "company":      company,
            # Required output fields
            "status":       decision.status,
            "product_area": product_area,
            "response":     response,
            "justification": decision.justification,
            "request_type": request_type,
        }

    def process_batch(self, tickets: list[dict]) -> list[dict]:
        """
        Process a list of ticket dicts (each with 'issue', 'subject', 'company').
        Returns a parallel list of result dicts.
        """
        results = []
        total = len(tickets)

        for i, ticket in enumerate(tickets, 1):
            log.section(f"Ticket {i}/{total}")
            result = self.process_ticket(
                issue=ticket.get("issue", ""),
                subject=ticket.get("subject", ""),
                company=ticket.get("company", ""),
            )
            results.append(result)

        return results
