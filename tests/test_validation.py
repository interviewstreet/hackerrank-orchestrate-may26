from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import _path
from support_agent.models import TicketPrediction
from support_agent.validation import read_predictions, validate_predictions


class ValidationTests(unittest.TestCase):
    def test_validate_predictions_reports_bad_enums_and_missing_fields(self) -> None:
        issues = validate_predictions(
            [
                TicketPrediction(
                    issue="Issue",
                    subject="Subject",
                    company="Visa",
                    response="",
                    product_area="",
                    status="bad",
                    request_type="wrong",
                    justification="",
                )
            ],
            expected_count=1,
        )

        messages = {issue.message for issue in issues}
        self.assertIn("Invalid status: bad", messages)
        self.assertIn("Invalid request_type: wrong", messages)
        self.assertIn("Missing generated field: response", messages)
        self.assertIn("Missing generated field: product_area", messages)
        self.assertIn("Missing generated field: justification", messages)

    def test_read_predictions_rejects_unexpected_headers(self) -> None:
        csv_text = "Issue,Subject,Company\nfoo,bar,baz\n"
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "output.csv"
            path.write_text(csv_text, encoding="utf-8")

            with self.assertRaises(ValueError):
                read_predictions(path)
