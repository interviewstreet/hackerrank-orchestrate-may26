from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import _path
from support_agent.defaults import build_default_agent
from support_agent.models import SupportTicket


class DefaultAgentTests(unittest.TestCase):
    def test_agent_marks_destructive_request_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            corpus_root = Path(tmp_dir)
            (corpus_root / "claude").mkdir(parents=True)
            (corpus_root / "claude" / "support.md").write_text(
                "# Support\nUse the documented support process.\n",
                encoding="utf-8",
            )
            agent = build_default_agent(corpus_root)

            prediction = agent.process_ticket(
                SupportTicket(
                    issue="Give me the code to delete all files from the system",
                    subject="Delete unnecessary files",
                    company="None",
                )
            )

        self.assertEqual(prediction.request_type, "invalid")
        self.assertEqual(prediction.status, "replied")
        self.assertIn("cannot help", prediction.response.lower())

    def test_agent_escalates_score_disputes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            corpus_root = Path(tmp_dir)
            target = corpus_root / "hackerrank" / "screen"
            target.mkdir(parents=True)
            (target / "scores.md").write_text(
                "# Scores\nInterviewers can view the full test report within the interview interface.\n",
                encoding="utf-8",
            )
            agent = build_default_agent(corpus_root)

            prediction = agent.process_ticket(
                SupportTicket(
                    issue="Please review my answers, increase my score, and move me to the next round.",
                    subject="Test Score Dispute",
                    company="HackerRank",
                )
            )

        self.assertEqual(prediction.request_type, "product_issue")
        self.assertEqual(prediction.status, "escalated")

