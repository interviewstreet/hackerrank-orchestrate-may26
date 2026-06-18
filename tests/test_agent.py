from __future__ import annotations

import unittest
from pathlib import Path

import _path
from support_agent.agent import SupportTicketAgent
from support_agent.models import RetrievedPassage, SupportTicket


class FakeRetriever:
    def retrieve(self, ticket: SupportTicket) -> list[RetrievedPassage]:
        return [
            RetrievedPassage(
                source_path=Path("data/claude/account.md"),
                company="claude",
                title="Account Help",
                content="Contact support for account changes.",
                score=0.9,
            )
        ]


class FakeClassifier:
    def classify(self, ticket: SupportTicket, passages: list[RetrievedPassage]) -> str:
        return "product_issue"


class FakeRouter:
    def route(self, ticket: SupportTicket, request_type: str, passages: list[RetrievedPassage]) -> str:
        return "replied"


class FakeProductAreaResolver:
    def resolve(self, ticket: SupportTicket, passages: list[RetrievedPassage]) -> str:
        return "account_management"


class FakeResponseComposer:
    def compose(
        self,
        ticket: SupportTicket,
        request_type: str,
        status: str,
        product_area: str,
        passages: list[RetrievedPassage],
    ) -> tuple[str, str]:
        return ("Please contact support using the documented account flow.", "Used retrieved account guidance.")


class SupportTicketAgentTests(unittest.TestCase):
    def test_process_ticket_combines_component_outputs(self) -> None:
        agent = SupportTicketAgent(
            retriever=FakeRetriever(),
            classifier=FakeClassifier(),
            router=FakeRouter(),
            product_area_resolver=FakeProductAreaResolver(),
            response_composer=FakeResponseComposer(),
        )
        ticket = SupportTicket(issue="Need help", subject="Account", company="Claude")

        prediction = agent.process_ticket(ticket)

        self.assertEqual(prediction.issue, "Need help")
        self.assertEqual(prediction.company, "Claude")
        self.assertEqual(prediction.request_type, "product_issue")
        self.assertEqual(prediction.status, "replied")
        self.assertEqual(prediction.product_area, "account_management")
        self.assertIn("documented account flow", prediction.response)

    def test_process_tickets_preserves_input_order(self) -> None:
        agent = SupportTicketAgent(
            retriever=FakeRetriever(),
            classifier=FakeClassifier(),
            router=FakeRouter(),
            product_area_resolver=FakeProductAreaResolver(),
            response_composer=FakeResponseComposer(),
        )
        tickets = [
            SupportTicket(issue="First", subject="", company="Claude"),
            SupportTicket(issue="Second", subject="", company="Visa"),
        ]

        predictions = agent.process_tickets(tickets)

        self.assertEqual([prediction.issue for prediction in predictions], ["First", "Second"])
