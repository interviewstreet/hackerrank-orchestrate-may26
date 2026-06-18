from __future__ import annotations

import unittest

import _path
from support_agent.config import normalize_company, normalize_header


class ConfigTests(unittest.TestCase):
    def test_normalize_header_handles_spaces_and_case(self) -> None:
        self.assertEqual(normalize_header("Product Area"), "product_area")
        self.assertEqual(normalize_header(" Request Type "), "request_type")

    def test_normalize_company_defaults_to_none(self) -> None:
        self.assertEqual(normalize_company(" HackerRank "), "hackerrank")
        self.assertEqual(normalize_company(""), "none")
        self.assertEqual(normalize_company(None), "none")
