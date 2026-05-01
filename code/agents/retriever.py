"""
Retriever Agent
Primary:  sentence-transformers cosine similarity via local embeddings store
Fallback: BM25 (rank_bm25) if local store returns low-confidence results
"""

from rank_bm25 import BM25Okapi

from config import LOCAL_STORE_DIR, TOP_K
from utils.embeddings import embed
from utils.loader import get_client
from utils.logger import log_agent


def run(query: str, domain: str) -> list[dict]:
    """
    Returns top-k chunks as list of:
    { text, score, metadata: {domain, product_area, source_url, title, heading} }
    """
    if domain == "unknown":
        log_agent("retriever", "domain=unknown, skipping retrieval", {})
        return []

    client     = get_client()
    collection = client.get_or_create_collection(name=domain)

    count = collection.count()
    if count == 0:
        log_agent("retriever", f"collection '{domain}' is empty", {})
        return []

    query_embedding = embed(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(TOP_K, count),
        include=["documents", "metadatas", "distances"],
    )

    docs      = results["documents"][0]
    metas     = results["metadatas"][0]
    distances = results["distances"][0]

    # Local store cosine distance → similarity: score = 1 - distance
    chunks = []
    for doc, meta, dist in zip(docs, metas, distances):
        chunks.append({
            "text":     doc,
            "score":    round(1 - dist, 4),
            "metadata": meta,
        })

    # Sort descending by score
    chunks.sort(key=lambda x: x["score"], reverse=True)

    log_agent("retriever", f"embedding → {len(chunks)} chunks", {
        "top_score": chunks[0]["score"] if chunks else 0,
        "domain": domain,
    })

    # BM25 fallback: if top score is very low, try keyword retrieval too
    if chunks and chunks[0]["score"] < 0.25:
        bm25_chunks = _bm25_fallback(query, domain, client)
        if bm25_chunks:
            # merge: take best from each, deduplicate by text
            seen  = {c["text"] for c in chunks}
            for c in bm25_chunks:
                if c["text"] not in seen:
                    chunks.append(c)
                    seen.add(c["text"])
            chunks.sort(key=lambda x: x["score"], reverse=True)
            chunks = chunks[:TOP_K]
            log_agent("retriever", "bm25 fallback merged", {"total": len(chunks)})

    return chunks


def _bm25_fallback(query: str, domain: str, client) -> list[dict]:
    """Pull all docs from collection and rank with BM25."""
    try:
        collection = client.get_or_create_collection(name=domain)
        all_results = collection.get(include=["documents", "metadatas"])
        docs  = all_results["documents"]
        metas = all_results["metadatas"]

        if not docs:
            return []

        tokenised = [d.lower().split() for d in docs]
        bm25      = BM25Okapi(tokenised)
        scores    = bm25.get_scores(query.lower().split())

        ranked = sorted(
            zip(docs, metas, scores),
            key=lambda x: x[2],
            reverse=True,
        )[:TOP_K]

        return [
            {"text": d, "score": round(float(s), 4), "metadata": m}
            for d, m, s in ranked
            if s > 0
        ]
    except Exception:
        return []