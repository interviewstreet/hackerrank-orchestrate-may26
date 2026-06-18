"""Load local Markdown support articles into structured corpus documents."""

from __future__ import annotations

from pathlib import Path

from support_agent.config import normalize_company
from support_agent.models import CorpusDocument


def infer_company_from_path(path: Path, corpus_root: Path) -> str:
    """Infer the corpus owner from the first path segment under the corpus root."""
    try:
        relative = path.relative_to(corpus_root)
    except ValueError as exc:
        raise ValueError(f"{path} is not inside corpus root {corpus_root}") from exc

    if not relative.parts:
        return "none"
    return normalize_company(relative.parts[0])


def extract_title(markdown_text: str, fallback: str) -> str:
    """Return the first Markdown heading, or a fallback title if none exists."""
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or fallback
    return fallback


def load_corpus_documents(corpus_root: Path) -> list[CorpusDocument]:
    """Discover every Markdown file under the corpus root and package it for retrieval."""
    documents: list[CorpusDocument] = []
    for path in sorted(corpus_root.rglob("*.md")):
        content = path.read_text(encoding="utf-8")
        documents.append(
            CorpusDocument(
                source_path=path,
                company=infer_company_from_path(path, corpus_root),
                title=extract_title(content, fallback=path.stem),
                content=content,
            )
        )
    return documents
