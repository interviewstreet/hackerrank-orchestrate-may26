from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from support_agent.agent import SupportTicketAgent
from support_agent.corpus import load_corpus_documents
from support_agent.models import RetrievedPassage, SupportTicket


class TodoRetriever:
    def __init__(self, corpus_root: Path) -> None:
        self._documents = load_corpus_documents(corpus_root)

    def retrieve(self, ticket: SupportTicket) -> Sequence[RetrievedPassage]:
        # TODO: Implement deterministic retrieval over self._documents.
        # Suggested approach:
        # 1. Normalize ticket text from subject + issue.
        # 2. Filter by ticket.normalized_company when high-confidence.
        # 3. Score passages from the local Markdown corpus.
        raise NotImplementedError("TODO: implement corpus retrieval")


class TodoRequestTypeClassifier:
    def classify(self, ticket: SupportTicket, passages: Sequence[RetrievedPassage]) -> str:
        # TODO: Classify into product_issue, feature_request, bug, or invalid.
        # Keep this deterministic and grounded in ticket text and retrieved evidence.
        raise NotImplementedError("TODO: implement request type classification")


class TodoStatusRouter:
    def route(
        self,
        ticket: SupportTicket,
        request_type: str,
        passages: Sequence[RetrievedPassage],
    ) -> str:
        # TODO: Decide between replied and escalated.
        # Sensitive account actions, refunds, access restoration, and unsupported
        # admin actions should generally escalate unless the corpus documents a safe path.
        raise NotImplementedError("TODO: implement status routing")


class TodoProductAreaResolver:
    def resolve(self, ticket: SupportTicket, passages: Sequence[RetrievedPassage]) -> str:
        # TODO: Derive a stable product_area label from evidence and ticket context.
        raise NotImplementedError("TODO: implement product area resolution")


class TodoResponseComposer:
    def compose(
        self,
        ticket: SupportTicket,
        request_type: str,
        status: str,
        product_area: str,
        passages: Sequence[RetrievedPassage],
    ) -> tuple[str, str]:
        # TODO: Generate a concise user-facing response and justification.
        # Reply only with support facts grounded in retrieved passages.
        raise NotImplementedError("TODO: implement response composition")


def build_default_agent(corpus_root: Path) -> SupportTicketAgent:
    return SupportTicketAgent(
        retriever=TodoRetriever(corpus_root),
        classifier=TodoRequestTypeClassifier(),
        router=TodoStatusRouter(),
        product_area_resolver=TodoProductAreaResolver(),
        response_composer=TodoResponseComposer(),
    )
