"""Orchestration layer that turns one ticket into one prediction."""

from __future__ import annotations

from collections.abc import Sequence

from support_agent.interfaces import (
    ProductAreaResolver,
    RequestTypeClassifier,
    ResponseComposer,
    Retriever,
    StatusRouter,
)
from support_agent.models import SupportTicket, TicketPrediction


class SupportTicketAgent:
    """Coordinate retrieval, routing, product-area resolution, and response writing."""

    def __init__(
        self,
        retriever: Retriever,
        classifier: RequestTypeClassifier,
        router: StatusRouter,
        product_area_resolver: ProductAreaResolver,
        response_composer: ResponseComposer,
    ) -> None:
        self._retriever = retriever
        self._classifier = classifier
        self._router = router
        self._product_area_resolver = product_area_resolver
        self._response_composer = response_composer

    def process_ticket(self, ticket: SupportTicket) -> TicketPrediction:
        """Run the full pipeline for a single ticket and return a prediction."""
        passages = self._retriever.retrieve(ticket)
        request_type = self._classifier.classify(ticket, passages)
        status = self._router.route(ticket, request_type, passages)
        product_area = self._product_area_resolver.resolve(ticket, passages)
        response, justification = self._response_composer.compose(
            ticket=ticket,
            request_type=request_type,
            status=status,
            product_area=product_area,
            passages=passages,
        )
        return TicketPrediction(
            issue=ticket.issue,
            subject=ticket.subject,
            company=ticket.company,
            response=response,
            product_area=product_area,
            status=status,
            request_type=request_type,
            justification=justification,
        )

    def process_tickets(self, tickets: Sequence[SupportTicket]) -> list[TicketPrediction]:
        """Process tickets in input order and return one prediction per row."""
        return [self.process_ticket(ticket) for ticket in tickets]
