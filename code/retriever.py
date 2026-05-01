"""
retriever.py — BM25-based corpus retrieval. No embeddings. No models. No API.

WHY BM25 INSTEAD OF FAISS:
  - BM25 is a proven IR algorithm (powers Elasticsearch, Lucene)
  - Zero setup time — no model download, no GPU, no API key
  - Works on word overlap — perfect for support docs where exact terminology matters
  - "reset password" → finds "how to reset your password" → correct match
  - Deterministic: same query = same result always
  - rank-bm25 is ~5KB, installs in seconds

HOW BM25 WORKS (simple explanation):
  BM25 scores each document based on:
  1. How often the query words appear in the document (term frequency)
  2. How rare those words are across all documents (inverse document frequency)
  3. Document length normalization (prevents long docs from always winning)
  Result: documents most relevant to the query get the highest score.

CHUNKING STRATEGY:
  Each corpus file is split into ~250-word chunks.
  Overlap of 30 words prevents answers from being cut mid-sentence.
  Each chunk keeps its company tag so we can filter by domain.

INDEXING:
  On first run → scan all .md/.txt files → tokenize → build BM25 index
  Cached in memory for the batch run (no file cache needed — fast enough)
"""

import re
import time
from pathlib import Path

from rank_bm25 import BM25Okapi  # type: ignore
from rich.console import Console  # type: ignore

from config import (  # type: ignore
    CHUNK_OVERLAP_WORDS,
    CHUNK_SIZE_WORDS,
    COMPANIES,
    DATA_DIR,
    MIN_BM25_SCORE,
    TOP_K_DOCS,
)
from models import DocChunk  # type: ignore

console = Console()


# ── Text cleaning ─────────────────────────────────────────────────────────────

def _clean(text: str) -> str:
    """Strip markdown noise that adds no retrieval signal."""
    # Remove YAML frontmatter
    text = re.sub(r"^---\n.*?\n---\n?", "", text, flags=re.DOTALL)
    # Remove markdown links → keep link text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    # Remove markdown headers markers (keep text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    # Collapse whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def _tokenize(text: str) -> list[str]:
    """
    Tokenize text for BM25 indexing.

    WHY LOWERCASE + SPLIT ON NON-ALPHA:
      BM25 is case-sensitive by default. Lowercasing ensures "Password"
      matches "password". Splitting on non-alpha handles hyphenated terms.
    """
    text = text.lower()
    tokens = re.findall(r"[a-z0-9]+", text)
    return tokens


# ── Chunker ───────────────────────────────────────────────────────────────────

def _chunk(text: str, size: int = CHUNK_SIZE_WORDS, overlap: int = CHUNK_OVERLAP_WORDS) -> list[str]:
    """
    Split text into overlapping word windows.
    Returns a list of chunk strings.
    """
    # Split on paragraph breaks first for natural boundaries
    paragraphs = [p.strip() for p in re.split(r"\n\n+", text) if p.strip()]

    chunks: list[str] = []
    current: list[str] = []

    for para in paragraphs:
        words = para.split()
        if current and len(current) + len(words) > size:
            chunks.append(" ".join(current))
            current = current[-overlap:] if overlap else []  # type: ignore
        current.extend(words)

    if current:
        chunks.append(" ".join(current))

    # Handle paragraphs that are individually too large
    final: list[str] = []
    for chunk in chunks:
        words = chunk.split()
        if len(words) <= size * 2:
            final.append(chunk)
        else:
            for i in range(0, len(words), size - overlap):
                piece = " ".join(words[i: i + size])  # type: ignore
                if piece.strip():
                    final.append(piece)

    return [c for c in final if len(c.split()) >= 10]


# ── Corpus scanner ────────────────────────────────────────────────────────────

def _scan_corpus(data_dir: Path = DATA_DIR) -> list[dict]:
    """
    Walk data/ and return all readable files with metadata.
    Returns list of { company, source, text }
    """
    docs = []
    for company in COMPANIES:
        company_dir = data_dir / company
        if not company_dir.exists():
            console.print(f"[yellow]Warning: corpus dir not found: {company_dir}[/yellow]")
            continue
        count = 0
        for fp in company_dir.rglob("*"):
            if fp.suffix.lower() not in {".md", ".txt"} or not fp.is_file():
                continue
            try:
                raw = fp.read_text(encoding="utf-8", errors="ignore")
                text = _clean(raw)
                if len(text.strip()) < 30:
                    continue
                docs.append({
                    "company": company,
                    "source":  str(fp.relative_to(data_dir)),
                    "text":    text,
                })
                count += 1  # type: ignore
            except Exception:
                pass
        console.print(f"  [dim]Loaded {count} files for '{company}'[/dim]")
    console.print(f"  [dim]Total documents: {len(docs)}[/dim]")
    return docs


# ── BM25 Index ────────────────────────────────────────────────────────────────

class BM25Retriever:
    """
    In-memory BM25 index over the support corpus.

    Build once at startup → reuse for all tickets in the batch.
    Build time: ~3–5 seconds for 774 files. No caching needed.
    """

    def __init__(self) -> None:
        self._chunks: list[dict] = []          # { text, source, company }
        self._tokenized: list[list[str]] = []  # tokenized versions
        self._index: BM25Okapi | None = None
        self._built = False

    def build(self, data_dir: Path = DATA_DIR) -> None:
        """
        Scan corpus → chunk documents → tokenize → build BM25 index.
        """
        if self._built:
            return

        console.print("\n[cyan]Building BM25 index…[/cyan]")
        t0 = time.time()

        docs = _scan_corpus(data_dir)
        if not docs:
            raise RuntimeError("No corpus files found in data/ directory.")

        # Chunk all documents
        for doc in docs:
            for chunk_text in _chunk(doc["text"]):
                self._chunks.append({
                    "text":    chunk_text,
                    "source":  doc["source"],
                    "company": doc["company"],
                })

        # Tokenize
        self._tokenized = [_tokenize(c["text"]) for c in self._chunks]

        # Build BM25
        self._index = BM25Okapi(self._tokenized)

        elapsed = time.time() - t0
        console.print(
            f"[green]✓ BM25 index ready[/green] — "
            f"{len(self._chunks)} chunks from {len(docs)} files in {elapsed:.1f}s\n"
        )
        self._built = True

    def retrieve(
        self,
        query: str,
        company: str | None = None,
        top_k: int = TOP_K_DOCS,
    ) -> list[DocChunk]:
        """
        Retrieve top-K most relevant chunks for a query.

        HOW:
          1. Tokenize the query the same way as the corpus
          2. Run BM25 scoring over all chunks
          3. Filter by company (if known)
          4. Return top-K sorted by score

        WHY FILTER AFTER SCORING (not before):
          BM25Okapi scores against the full index. We filter by company
          after scoring because rebuilding the index per company would
          be slow and wasteful. Filtering results is O(N) and instant.

        Args:
            query:   Combined issue + subject text
            company: 'hackerrank' | 'claude' | 'visa' | None (search all)
            top_k:   Number of chunks to return
        """
        if not self._built:
            raise RuntimeError("Call build() before retrieve().")

        tokens = _tokenize(query)
        if not tokens:
            return []

        assert self._index is not None
        scores = self._index.get_scores(tokens)

        # Pair scores with chunk metadata and optionally filter by company
        scored = []
        for i, score in enumerate(scores):
            chunk = self._chunks[i]
            if company and chunk["company"] != company:
                continue
            scored.append((score, i))

        # Sort descending by score
        scored.sort(key=lambda x: x[0], reverse=True)

        results: list[DocChunk] = []
        for score, idx in scored[:top_k]:  # type: ignore
            chunk = self._chunks[idx]
            results.append(DocChunk(
                text=chunk["text"],
                source=chunk["source"],
                company=chunk["company"],
                score=float(score),
            ))

        return results

    def top_score(self, chunks: list[DocChunk]) -> float:
        return chunks[0].score if chunks else 0.0

    def is_low_confidence(self, chunks: list[DocChunk]) -> bool:
        """
        True if retrieval didn't find any good matches.
        WHY: Low score = corpus doesn't contain relevant info.
             Better to escalate than generate an unsupported answer.
        """
        return self.top_score(chunks) < MIN_BM25_SCORE


# ── Singleton ─────────────────────────────────────────────────────────────────
_retriever: BM25Retriever | None = None


def get_retriever() -> BM25Retriever:
    """Get or create the singleton BM25Retriever."""
    global _retriever
    if _retriever is None:
        _retriever = BM25Retriever()
    return _retriever
