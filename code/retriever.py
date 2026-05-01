"""
retriever.py — Corpus ingestion and RAG retrieval engine.
"""
from __future__ import annotations
import os, re
from pathlib import Path
from typing import List, Tuple, Dict, Optional

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity as _cosine_similarity
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False
    TfidfVectorizer = None
    _cosine_similarity = None

DATA_DIR = Path(__file__).parent.parent / "data"
CHUNK_SIZE = 400
CHUNK_OVERLAP = 80
MAX_RESULTS = 6
MIN_SCORE = 0.05


class Chunk:
    __slots__ = ("source", "domain", "filename", "text", "index")
    def __init__(self, source, domain, filename, text, index):
        self.source = source
        self.domain = domain
        self.filename = filename
        self.text = text
        self.index = index
    def __repr__(self):
        return f"<Chunk domain={self.domain} src={self.source!r} len={len(self.text)}>"


def _read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def _chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> List[str]:
    words = text.split()
    chunks, start = [], 0
    while start < len(words):
        end = min(start + size, len(words))
        chunk = " ".join(words[start:end])
        if chunk.strip():
            chunks.append(chunk)
        if end == len(words):
            break
        start += size - overlap
    return chunks


def _infer_domain(path: Path) -> str:
    parts = {p.lower() for p in path.parts}
    if "hackerrank" in parts: return "hackerrank"
    if "claude" in parts: return "claude"
    if "visa" in parts: return "visa"
    return "unknown"


def load_corpus(data_dir: Path = DATA_DIR) -> List[Chunk]:
    chunks: List[Chunk] = []
    extensions = {".txt", ".md", ".html", ".json", ".csv"}
    for root, dirs, files in os.walk(data_dir):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fname in sorted(files):
            path = Path(root) / fname
            if path.suffix.lower() not in extensions:
                continue
            raw = _read_file(path)
            if not raw.strip():
                continue
            clean = re.sub(r"<[^>]+>", " ", raw)
            clean = re.sub(r"\s+", " ", clean).strip()
            domain = _infer_domain(path)
            source_label = str(path.relative_to(data_dir))
            for i, chunk in enumerate(_chunk_text(clean)):
                chunks.append(Chunk(source_label, domain, fname, chunk, i))
    return chunks


class CorpusIndex:
    """TF-IDF vector index with keyword fallback."""

    def __init__(self, chunks: List[Chunk]):
        self.chunks = chunks
        self._vectorizer = None
        self._matrix = None
        self._tf_dicts: List[Dict[str, float]] = []
        self._build_index()

    def _build_index(self):
        texts = [c.text for c in self.chunks]
        if not texts:
            return
        if HAS_SKLEARN:
            # Avoid sklearn ValueError on tiny corpora where max_df can prune all terms.
            max_df = 1.0 if len(texts) < 3 else 0.95
            self._vectorizer = TfidfVectorizer(
                ngram_range=(1, 2), min_df=1, max_df=max_df,
                sublinear_tf=True, strip_accents="unicode", analyzer="word",
            )
            self._matrix = self._vectorizer.fit_transform(texts)
        else:
            self._tf_dicts = [self._term_freq(t) for t in texts]

    @staticmethod
    def _term_freq(text: str) -> Dict[str, float]:
        words = re.findall(r"\w+", text.lower())
        tf: Dict[str, float] = {}
        for w in words:
            tf[w] = tf.get(w, 0) + 1
        total = max(len(words), 1)
        return {k: v / total for k, v in tf.items()}

    def _keyword_score(self, query_words: List[str], tf: Dict[str, float]) -> float:
        return sum(tf.get(w, 0.0) for w in query_words)

    def search(
        self,
        query: str,
        top_k: int = MAX_RESULTS,
        domain_filter: Optional[str] = None,
    ) -> List[Tuple[Chunk, float]]:
        if not self.chunks:
            return []
        if HAS_SKLEARN and self._vectorizer is not None and self._matrix is not None:
            return self._sklearn_search(query, top_k, domain_filter)
        return self._keyword_search(query, top_k, domain_filter)

    def _sklearn_search(self, query, top_k, domain_filter):
        q_vec = self._vectorizer.transform([query])
        if domain_filter:
            idx_map = [i for i, c in enumerate(self.chunks) if c.domain == domain_filter]
            if not idx_map:
                idx_map = list(range(len(self.chunks)))
            sub_matrix = self._matrix[idx_map]
            scores_arr = _cosine_similarity(q_vec, sub_matrix).flatten().tolist()
            ranked = sorted(zip(idx_map, scores_arr), key=lambda x: -x[1])
            return [(self.chunks[i], float(s)) for i, s in ranked if s >= MIN_SCORE][:top_k]
        else:
            scores_arr = _cosine_similarity(q_vec, self._matrix).flatten().tolist()
            ranked = sorted(enumerate(scores_arr), key=lambda x: -x[1])
            return [(self.chunks[i], float(s)) for i, s in ranked if s >= MIN_SCORE][:top_k]

    def _keyword_search(self, query, top_k, domain_filter):
        q_words = re.findall(r"\w+", query.lower())
        scored = []
        for i, chunk in enumerate(self.chunks):
            if domain_filter and chunk.domain != domain_filter:
                continue
            tf = self._tf_dicts[i] if self._tf_dicts else self._term_freq(chunk.text)
            s = self._keyword_score(q_words, tf)
            if s >= MIN_SCORE:
                scored.append((chunk, s))
        return sorted(scored, key=lambda x: -x[1])[:top_k]

    def search_multi(
        self,
        queries: List[str],
        top_k: int = MAX_RESULTS,
        domain_filter: Optional[str] = None,
    ) -> List[Tuple[Chunk, float]]:
        seen: Dict[int, float] = {}
        chunk_map: Dict[int, Chunk] = {}
        for q in queries:
            if not q.strip():
                continue
            for chunk, score in self.search(q, top_k=top_k, domain_filter=domain_filter):
                cid = id(chunk)
                if cid not in seen or seen[cid] < score:
                    seen[cid] = score
                    chunk_map[cid] = chunk
        ranked = sorted(seen.items(), key=lambda x: -x[1])
        return [(chunk_map[cid], score) for cid, score in ranked[:top_k]]


_INDEX: Optional[CorpusIndex] = None


def get_index(data_dir: Path = DATA_DIR) -> CorpusIndex:
    global _INDEX
    if _INDEX is None:
        chunks = load_corpus(data_dir)
        _INDEX = CorpusIndex(chunks)
    return _INDEX


def format_context(results: List[Tuple[Chunk, float]], max_chars: int = 3500) -> str:
    parts, total = [], 0
    for chunk, score in results:
        header = f"[Source: {chunk.source} | Domain: {chunk.domain} | Score: {score:.3f}]"
        block = f"{header}\n{chunk.text}\n"
        if total + len(block) > max_chars:
            break
        parts.append(block)
        total += len(block)
    return "\n---\n".join(parts) if parts else "No relevant documentation found."