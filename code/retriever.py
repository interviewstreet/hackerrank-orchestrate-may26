"""Single dense index over corpus with metadata filter. TF-IDF fallback."""
from __future__ import annotations

import hashlib
import os
import pickle
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from schemas import ChunkDoc


@dataclass
class RetrievalResult:
    chunks: list[ChunkDoc]
    scores: list[float]

    @property
    def max_score(self) -> float:
        return max(self.scores) if self.scores else 0.0

    @property
    def mean_top3(self) -> float:
        if not self.scores:
            return 0.0
        top = sorted(self.scores, reverse=True)[:3]
        return float(sum(top) / len(top))


class DenseRetriever:
    def __init__(self, chunks: list[ChunkDoc], cache_dir: Path,
                 model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
                 use_embeddings: bool = True) -> None:
        self.chunks = chunks
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.use_embeddings = use_embeddings
        self.model_name = model_name
        self._embeddings: np.ndarray | None = None
        self._tfidf = None
        self._tfidf_matrix = None
        self._build()

    def _corpus_signature(self) -> str:
        h = hashlib.sha256()
        h.update(self.model_name.encode())
        for c in self.chunks:
            h.update(c.chunk_id.encode())
            h.update(str(len(c.text)).encode())
        return h.hexdigest()[:16]

    def _build(self) -> None:
        if self.use_embeddings:
            self._build_embeddings()
        else:
            self._build_tfidf()

    def _build_embeddings(self) -> None:
        sig = self._corpus_signature()
        cache_file = self.cache_dir / f"embeds_{sig}.npy"
        if cache_file.exists():
            self._embeddings = np.load(cache_file)
            return
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(self.model_name)
        texts = [c.text for c in self.chunks]
        embs = model.encode(
            texts, batch_size=64, show_progress_bar=True,
            convert_to_numpy=True, normalize_embeddings=True,
        )
        self._embeddings = embs.astype(np.float32)
        np.save(cache_file, self._embeddings)

    def _build_tfidf(self) -> None:
        from sklearn.feature_extraction.text import TfidfVectorizer
        self._tfidf = TfidfVectorizer(
            ngram_range=(1, 2), max_features=50000, lowercase=True,
        )
        self._tfidf_matrix = self._tfidf.fit_transform(c.text for c in self.chunks)

    def _embed_query(self, query: str) -> np.ndarray:
        from sentence_transformers import SentenceTransformer
        if not hasattr(self, "_qmodel"):
            self._qmodel = SentenceTransformer(self.model_name)
        v = self._qmodel.encode(
            [query], convert_to_numpy=True, normalize_embeddings=True,
        )
        return v[0].astype(np.float32)

    def retrieve(self, query: str, company: str | None = None,
                 top_k: int = 8) -> RetrievalResult:
        if self.use_embeddings:
            qv = self._embed_query(query)
            scores = self._embeddings @ qv
        else:
            qm = self._tfidf.transform([query])
            scores = (self._tfidf_matrix @ qm.T).toarray().ravel()

        idx = np.arange(len(self.chunks))
        if company and company != "None":
            mask = np.array([c.company == company for c in self.chunks])
            if mask.any():
                idx = idx[mask]
                scores = scores[mask]

        order = np.argsort(-scores, kind="stable")[:top_k]
        return RetrievalResult(
            chunks=[self.chunks[idx[i]] for i in order],
            scores=[float(scores[i]) for i in order],
        )


def make_retriever(chunks: list[ChunkDoc], cache_dir: Path,
                   use_embeddings: bool = True,
                   model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
                   ) -> DenseRetriever:
    if use_embeddings and os.environ.get("HRK_NO_EMBEDDINGS") == "1":
        use_embeddings = False
    return DenseRetriever(chunks, cache_dir,
                          model_name=model_name,
                          use_embeddings=use_embeddings)
