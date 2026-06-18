from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import _path
from support_agent.corpus import extract_title, infer_company_from_path, load_corpus_documents


class CorpusTests(unittest.TestCase):
    def test_extract_title_prefers_markdown_heading(self) -> None:
        title = extract_title("# Hello World\n\nBody", fallback="fallback")
        self.assertEqual(title, "Hello World")

    def test_infer_company_from_path_uses_first_directory(self) -> None:
        corpus_root = Path("/tmp/corpus")
        path = corpus_root / "claude" / "support" / "article.md"
        self.assertEqual(infer_company_from_path(path, corpus_root), "claude")

    def test_load_corpus_documents_reads_markdown_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            corpus_root = Path(tmp_dir)
            doc_path = corpus_root / "visa" / "support" / "consumer.md"
            doc_path.parent.mkdir(parents=True, exist_ok=True)
            doc_path.write_text("# Lost card\n\nCall support.", encoding="utf-8")

            documents = load_corpus_documents(corpus_root)

        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0].company, "visa")
        self.assertEqual(documents[0].title, "Lost card")
        self.assertIn("Call support.", documents[0].content)
