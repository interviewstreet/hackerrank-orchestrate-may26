"""
retriever.py — Local RAG (Retrieval-Augmented Generation) engine.

Design decisions:
  • Loads every .txt and .md file from data/ recursively at startup.
  • Splits documents into overlapping chunks for context preservation.
  • PRIMARY backend  : sentence-transformers (all-MiniLM-L6-v2).
  • FALLBACK backend : scikit-learn TF-IDF + cosine similarity.
  • Returns top-K chunks with confidence scores for the decision engine.
"""

from __future__ import annotations

import os
import textwrap
from pathlib import Path
from typing import NamedTuple

import numpy as np

from config import DATA_DIR, EMBEDDING_MODEL, TOP_K_DOCS, RANDOM_SEED
from utils import log


# ─────────────────────────────────────────────────────────────────────────────
# Data structures
# ─────────────────────────────────────────────────────────────────────────────

class Chunk(NamedTuple):
    text:     str    # the actual passage
    source:   str    # filename it came from
    chunk_id: int    # sequential index within the corpus


class RetrievedDoc(NamedTuple):
    chunk:      Chunk
    score:      float    # cosine similarity ∈ [−1, 1]
    is_confident: bool   # score ≥ CONFIDENCE_THRESHOLD


# ─────────────────────────────────────────────────────────────────────────────
# Encoder backends
# ─────────────────────────────────────────────────────────────────────────────

class _SentenceTransformerBackend:
    def __init__(self, model_name: str, seed: int) -> None:
        try:
            import torch
            torch.manual_seed(seed)
        except ImportError:
            pass
        from sentence_transformers import SentenceTransformer
        self._model = SentenceTransformer(model_name)

    def encode_batch(self, texts: list[str]) -> np.ndarray:
        embs = self._model.encode(
            texts,
            batch_size=32,
            show_progress_bar=False,
            normalize_embeddings=True,
        )
        return np.array(embs, dtype=np.float32)

    def encode_one(self, text: str) -> np.ndarray:
        emb = self._model.encode(text, normalize_embeddings=True, show_progress_bar=False)
        return np.array(emb, dtype=np.float32)

    @property
    def name(self) -> str:
        return "sentence-transformers"


class _TFIDFBackend:
    def __init__(self) -> None:
        from sklearn.feature_extraction.text import TfidfVectorizer
        self._vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            max_features=8000,
            sublinear_tf=True,
            stop_words="english",
        )
        self._fitted = False

    def fit(self, texts: list[str]) -> None:
        self._vectorizer.fit(texts)
        self._fitted = True

    def encode_batch(self, texts: list[str]) -> np.ndarray:
        from sklearn.preprocessing import normalize
        matrix = self._vectorizer.transform(texts).toarray().astype(np.float32)
        return normalize(matrix, norm="l2")

    def encode_one(self, text: str) -> np.ndarray:
        from sklearn.preprocessing import normalize
        vec = self._vectorizer.transform([text]).toarray().astype(np.float32)
        return normalize(vec, norm="l2")[0]

    @property
    def name(self) -> str:
        return "TF-IDF (fallback)"


# ─────────────────────────────────────────────────────────────────────────────
# Retriever
# ─────────────────────────────────────────────────────────────────────────────

class Retriever:
    CHUNK_SIZE    = 300
    CHUNK_OVERLAP = 50
    TFIDF_THRESHOLD_MULTIPLIER = 0.6

    def __init__(self, confidence_threshold: float = 0.30) -> None:
        self.confidence_threshold = confidence_threshold
        self._chunks:     list[Chunk]        = []
        self._embeddings: np.ndarray | None  = None
        self._backend:    _SentenceTransformerBackend | _TFIDFBackend | None = None
        self._using_tfidf = False

        self._init_backend()

    def _init_backend(self) -> None:
        log.info(f"Attempting to load embedding model: {EMBEDDING_MODEL}")
        try:
            self._backend = _SentenceTransformerBackend(EMBEDDING_MODEL, RANDOM_SEED)
            log.success(f"Embedding backend: sentence-transformers ({EMBEDDING_MODEL})")
        except Exception as e:
            log.warn(f"Could not load sentence-transformers model ({e.__class__.__name__}). Activating TF-IDF fallback.")
            self._backend = _TFIDFBackend()
            self._using_tfidf = True
            self.confidence_threshold *= self.TFIDF_THRESHOLD_MULTIPLIER
            log.info(f"TF-IDF confidence threshold set to {self.confidence_threshold:.2f}")

    def build_index(self, data_dir: str = DATA_DIR) -> None:
        log.section("Building Retrieval Index")
        raw_docs = self._load_corpus(data_dir)
        if not raw_docs:
            raise FileNotFoundError(f"No valid support files (.txt or .md) found in {data_dir!r}")

        log.info(f"Loaded {len(raw_docs)} files from across all subdirectories.")

        self._chunks = []
        for filename, text in raw_docs.items():
            chunks = self._chunk_text(text, filename)
            self._chunks.extend(chunks)

        log.info(f"Created {len(self._chunks)} total chunks.")

        texts = [c.text for c in self._chunks]
        if self._using_tfidf:
            self._backend.fit(texts)

        self._embeddings = self._backend.encode_batch(texts)
        log.success(f"Index built ({self._backend.name}): {self._embeddings.shape[0]} chunks.")

    def retrieve(self, query: str, top_k: int = TOP_K_DOCS) -> list[RetrievedDoc]:
        if self._embeddings is None or len(self._chunks) == 0:
            raise RuntimeError("Call build_index() before retrieve().")

        query_vec = self._backend.encode_one(query)
        scores = self._embeddings @ query_vec
        top_indices = np.argsort(scores)[::-1][:top_k]

        results: list[RetrievedDoc] = []
        for idx in top_indices:
            score = float(scores[idx])
            chunk = self._chunks[int(idx)]
            results.append(RetrievedDoc(
                chunk=chunk,
                score=score,
                is_confident=(score >= self.confidence_threshold),
            ))
        return results

    @staticmethod
    def _load_corpus(data_dir: str) -> dict[str, str]:
        """UPDATED: Recursively finds all .txt and .md files in the corpus."""
        corpus: dict[str, str] = {}
        data_path = Path(data_dir)
        
        # Search for both markdown and text files in all subfolders
        patterns = ["**/*.txt", "**/*.md"]
        
        for pattern in patterns:
            for filepath in sorted(data_path.glob(pattern)):
                try:
                    content = filepath.read_text(encoding="utf-8", errors="replace").strip()
                    if content:
                        # Store as 'folder/filename' to avoid collisions
                        key = str(filepath.relative_to(data_path))
                        corpus[key] = content
                except Exception as e:
                    log.warn(f"Error reading {filepath}: {e}")
                    
        return corpus

    def _chunk_text(self, text: str, source: str) -> list[Chunk]:
        words = text.split()
        chunks: list[Chunk] = []
        start = 0

        while start < len(words):
            end        = min(start + self.CHUNK_SIZE, len(words))
            chunk_text = " ".join(words[start:end])
            chunk_text = " ".join(chunk_text.split())

            chunks.append(Chunk(
                text=chunk_text,
                source=source,
                chunk_id=len(self._chunks) + len(chunks),
            ))

            if end >= len(words):
                break
            start += self.CHUNK_SIZE - self.CHUNK_OVERLAP

        return chunks

    def encode(self, text: str) -> np.ndarray:
        return self._backend.encode_one(text)

    @staticmethod
    def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
        return float(np.dot(a, b))

    def pretty_results(self, docs: list[RetrievedDoc]) -> str:
        lines = []
        for i, doc in enumerate(docs, 1):
            preview = textwrap.shorten(doc.chunk.text, width=80, placeholder="…")
            lines.append(f"  [{i}] score={doc.score:.3f} ({'✓' if doc.is_confident else '✗'}) source={doc.chunk.source!r}\n      {preview}")
        return "\n".join(lines)