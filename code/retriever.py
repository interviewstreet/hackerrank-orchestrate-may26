"""
Retriever — Qdrant-backed corpus retrieval with company pre-filter.

build_index() walks data/ and indexes all .md files.
retrieve() returns ranked chunks scoped to a single company corpus.
"""

import os
import re
import sys
import threading
from pathlib import Path
from typing import NamedTuple

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchValue,
    PointStruct,
    VectorParams,
)
from sentence_transformers import SentenceTransformer

COLLECTION = "corpus"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
VECTOR_DIM = 384
CHUNK_SIZE = 800    # chars per chunk
CHUNK_OVERLAP = 100 # chars of overlap between chunks
VALID_COMPANIES = {"HackerRank", "Claude", "Visa"}

# Local-file Qdrant only allows one client per storage path. The bulk runner
# uses a thread pool, so we share a single QdrantClient + embedder across
# threads instead of constructing them per-call.
_CLIENT_LOCK = threading.Lock()
_CLIENT: QdrantClient | None = None
_CLIENT_PATH: str | None = None
_MODEL: SentenceTransformer | None = None


class RetrievedChunk(NamedTuple):
    text: str
    source_doc: str
    company: str
    score: float


def _get_qdrant_path() -> str:
    # Explicit override wins.
    if "QDRANT_PATH" in os.environ:
        return os.environ["QDRANT_PATH"]
    # Co-locate with data: sibling of DATA_PATH if set, otherwise sibling of repo-root data/.
    data_path = os.environ.get("DATA_PATH", "").strip()
    if data_path:
        return str(Path(data_path).parent / "qdrant_db")
    return str(Path(__file__).parent.parent / "qdrant_db")


def _get_model() -> SentenceTransformer:
    global _MODEL
    with _CLIENT_LOCK:
        if _MODEL is None:
            _MODEL = SentenceTransformer(EMBEDDING_MODEL)
        return _MODEL


def _get_client(qdrant_path: str) -> QdrantClient:
    global _CLIENT, _CLIENT_PATH
    with _CLIENT_LOCK:
        if _CLIENT is None or _CLIENT_PATH != qdrant_path:
            _CLIENT = QdrantClient(path=qdrant_path)
            _CLIENT_PATH = qdrant_path
        return _CLIENT


def _company_from_path(path: Path, data_root: Path) -> str | None:
    rel = path.relative_to(data_root)
    top = rel.parts[0].lower()
    if top == "hackerrank":
        return "HackerRank"
    if top == "claude":
        return "Claude"
    if top == "visa":
        return "Visa"
    return None


def _chunk_text(text: str, source_doc: str) -> list[str]:
    """
    Split on H2/H3 headings first; fall back to fixed-size sliding window.
    """
    sections = re.split(r"\n(?=#{1,3} )", text)
    chunks: list[str] = []
    for section in sections:
        section = section.strip()
        if not section:
            continue
        if len(section) <= CHUNK_SIZE:
            chunks.append(section)
        else:
            # Sliding window on long sections
            start = 0
            while start < len(section):
                end = min(start + CHUNK_SIZE, len(section))
                chunks.append(section[start:end])
                start += CHUNK_SIZE - CHUNK_OVERLAP
    return [c for c in chunks if len(c.strip()) >= 50]


def build_index(data_root: str | Path, qdrant_path: str | None = None) -> int:
    """
    Index all markdown files under data_root into Qdrant.
    Returns the number of points indexed.
    """
    data_root = Path(data_root)
    qdrant_path = qdrant_path or _get_qdrant_path()

    client = _get_client(qdrant_path)
    model = _get_model()

    # Recreate collection
    client.recreate_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=VECTOR_DIM, distance=Distance.COSINE),
    )

    points: list[PointStruct] = []
    point_id = 0

    for md_file in sorted(data_root.rglob("*.md")):
        company = _company_from_path(md_file, data_root)
        if company is None:
            continue
        text = md_file.read_text(encoding="utf-8", errors="replace")
        rel_path = str(md_file.relative_to(data_root.parent))
        for chunk in _chunk_text(text, rel_path):
            points.append(
                PointStruct(
                    id=point_id,
                    vector=model.encode(chunk).tolist(),
                    payload={
                        "company": company,
                        "source_doc": rel_path,
                        "text": chunk,
                    },
                )
            )
            point_id += 1

        if len(points) >= 500:
            client.upsert(collection_name=COLLECTION, points=points)
            points = []
            print(f"  Indexed {point_id} chunks so far...", file=sys.stderr)

    if points:
        client.upsert(collection_name=COLLECTION, points=points)

    return point_id


def retrieve(
    query: str,
    company: str,
    top_k: int | None = None,
    similarity_threshold: float = 0.0,
) -> list[RetrievedChunk]:
    """
    Retrieve top_k corpus chunks for query, pre-filtered by company.
    Only returns chunks with score >= similarity_threshold.
    """
    top_k = top_k or int(os.environ.get("RETRIEVAL_TOP_K", "5"))
    qdrant_path = _get_qdrant_path()

    client = _get_client(qdrant_path)
    model = _get_model()

    if company not in VALID_COMPANIES:
        # Search all companies when company is unknown
        filter_condition = None
    else:
        filter_condition = Filter(
            must=[FieldCondition(key="company", match=MatchValue(value=company))]
        )

    vector = model.encode(query).tolist()
    results = client.search(
        collection_name=COLLECTION,
        query_vector=vector,
        query_filter=filter_condition,
        limit=top_k,
        with_payload=True,
    )

    chunks: list[RetrievedChunk] = []
    for hit in results:
        if hit.score >= similarity_threshold:
            chunks.append(
                RetrievedChunk(
                    text=hit.payload["text"],
                    source_doc=hit.payload["source_doc"],
                    company=hit.payload["company"],
                    score=hit.score,
                )
            )
    return chunks


def index_exists_for_all_companies(qdrant_path: str | None = None) -> tuple[bool, str]:
    """
    Returns (True, "") if the index is populated for all three companies,
    or (False, error_message) otherwise.
    """
    qdrant_path = qdrant_path or _get_qdrant_path()
    try:
        client = _get_client(qdrant_path)
        client.get_collection(COLLECTION)
    except Exception:
        return False, f"Qdrant index not found at {qdrant_path!r}."

    for company in VALID_COMPANIES:
        count_result = client.count(
            collection_name=COLLECTION,
            count_filter=Filter(
                must=[FieldCondition(key="company", match=MatchValue(value=company))]
            ),
        )
        if count_result.count == 0:
            return False, f"Qdrant index not found or empty for company={company}."
    return True, ""
