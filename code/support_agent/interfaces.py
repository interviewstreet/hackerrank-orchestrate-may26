from __future__ import annotations

from typing import Protocol, Sequence

from support_agent.models import RetrievedPassage, SupportTicket


class Retriever(Protocol):
    def retrieve(self, ticket: SupportTicket) -> Sequence[RetrievedPassage]:
        """Return relevant evidence for a ticket."""


class RequestTypeClassifier(Protocol):
    def classify(self, ticket: SupportTicket, passages: Sequence[RetrievedPassage]) -> str:
        """Return one of the allowed request_type values."""


class StatusRouter(Protocol):
    def route(
        self,
        ticket: SupportTicket,
        request_type: str,
        passages: Sequence[RetrievedPassage],
    ) -> str:
        """Return one of the allowed status values."""


class ProductAreaResolver(Protocol):
    def resolve(self, ticket: SupportTicket, passages: Sequence[RetrievedPassage]) -> str:
        """Return the product area string for the prediction."""


class ResponseComposer(Protocol):
    def compose(
        self,
        ticket: SupportTicket,
        request_type: str,
        status: str,
        product_area: str,
        passages: Sequence[RetrievedPassage],
    ) -> tuple[str, str]:
        """Return response and justification."""
