from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import _path
from support_agent.io import read_tickets, write_predictions
from support_agent.models import TicketPrediction


class IoTests(unittest.TestCase):
    def test_read_tickets_normalizes_sample_headers(self) -> None:
        csv_text = (
            "Issue,Subject,Company,Response,Product Area,Status,Request Type\n"
            "\"Need help\",Billing,HackerRank,ignored,screen,Replied,product_issue\n"
        )
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "sample.csv"
            path.write_text(csv_text, encoding="utf-8")

            tickets = read_tickets(path)

        self.assertEqual(len(tickets), 1)
        self.assertEqual(tickets[0].issue, "Need help")
        self.assertEqual(tickets[0].subject, "Billing")
        self.assertEqual(tickets[0].company, "HackerRank")

    def test_write_predictions_uses_lowercase_output_schema(self) -> None:
        prediction = TicketPrediction(
            issue="Issue",
            subject="Subject",
            company="Claude",
            response="Response",
            product_area="privacy",
            status="replied",
            request_type="product_issue",
            justification="Grounded in local docs.",
        )
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "output.csv"
            write_predictions(path, [prediction])
            written = path.read_text(encoding="utf-8").splitlines()

        self.assertEqual(
            written[0],
            "issue,subject,company,response,product_area,status,request_type,justification",
        )
        self.assertEqual(len(written), 2)
