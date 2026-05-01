"""
Loads the support corpus from data/ directory into LangChain Documents.
Each markdown file becomes a Document with metadata about its source domain
and category path.
"""

from pathlib import Path
from typing import List

from langchain_core.documents import Document


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"

DOMAIN_MAP = {
    "hackerrank": "HackerRank",
    "claude": "Claude",
    "visa": "Visa",
}


def load_corpus() -> List[Document]:
    """Walk every .md file under data/ and return a list of Documents."""
    documents: List[Document] = []

    for domain_dir in sorted(DATA_DIR.iterdir()):
        if not domain_dir.is_dir():
            continue

        domain_key = domain_dir.name
        domain_label = DOMAIN_MAP.get(domain_key, domain_key)

        for md_path in sorted(domain_dir.rglob("*.md")):
            try:
                text = md_path.read_text(encoding="utf-8", errors="replace").strip()
            except (FileNotFoundError, OSError) as exc:
                print(f"Warning: skipping unreadable corpus file {md_path}: {exc}")
                continue

            if not text:
                continue

            rel_path = md_path.relative_to(DATA_DIR)
            category = "/".join(rel_path.parts[1:-1]) or "general"

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": str(rel_path),
                        "domain": domain_label,
                        "category": category,
                        "filename": md_path.stem,
                    },
                )
            )

    return documents


if __name__ == "__main__":
    docs = load_corpus()
    print(f"Loaded {len(docs)} documents")
    for d in docs[:3]:
        print(f"  [{d.metadata['domain']}] {d.metadata['source']}: {len(d.page_content)} chars")
