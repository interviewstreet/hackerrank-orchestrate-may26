"""
corpus_loader.py
----------------
Loads every Markdown file from data/ into LangChain Documents,
splits them into chunks, and attaches company / product_area metadata.

LangChain primitives used:
  - TextLoader / DirectoryLoader  → raw document ingestion
  - RecursiveCharacterTextSplitter → chunking
  - Document                       → uniform document representation
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# ── constants ─────────────────────────────────────────────────────────────────
DATA_DIR     = Path(__file__).parent.parent / "data"
CHUNK_SIZE   = 800
CHUNK_OVERLAP = 100

COMPANY_MAP: dict[str, str] = {
    "hackerrank": "HackerRank",
    "claude":     "Claude",
    "visa":       "Visa",
}
# ─────────────────────────────────────────────────────────────────────────────


def _strip_frontmatter(text: str) -> str:
    """Remove YAML front-matter if present."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].lstrip()
    return text


def _derive_product_area(rel_path: str) -> str:
    """
    Turn a relative file path into a human-readable product_area tag.
    e.g. "screen/managing-tests/xxx.md" → "screen/managing-tests"
    """
    parts = Path(rel_path).parts
    if len(parts) > 2:
        return "/".join(parts[1:-1])
    if len(parts) == 2:
        return parts[0]
    return "general"


def load_corpus(data_dir: Path = DATA_DIR) -> List[Document]:
    """
    Walk data_dir, load every *.md file, split into chunks, and return
    a list of LangChain Documents with metadata:
      - company      : "HackerRank" | "Claude" | "Visa"
      - product_area : sub-directory path (e.g. "screen/managing-tests")
      - source       : relative file path for attribution
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""],
    )

    all_docs: List[Document] = []

    for company_dir in sorted(data_dir.iterdir()):
        if not company_dir.is_dir():
            continue
        company = COMPANY_MAP.get(company_dir.name.lower(), company_dir.name)

        for md_file in sorted(company_dir.rglob("*.md")):
            try:
                raw = md_file.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue

            raw = _strip_frontmatter(raw)
            rel_path = md_file.relative_to(company_dir).as_posix()
            product_area = _derive_product_area(rel_path)
            source = f"data/{company_dir.name}/{rel_path}"

            # Create a parent doc so the splitter can carry metadata forward
            parent_doc = Document(
                page_content=raw,
                metadata={
                    "company":      company,
                    "product_area": product_area,
                    "source":       source,
                },
            )
            chunks = splitter.split_documents([parent_doc])
            all_docs.extend(chunks)

    return all_docs


if __name__ == "__main__":
    docs = load_corpus()
    print(f"Loaded {len(docs)} chunks from corpus.")
    for company in ("HackerRank", "Claude", "Visa"):
        n = sum(1 for d in docs if d.metadata.get("company") == company)
        print(f"  {company}: {n} chunks")
