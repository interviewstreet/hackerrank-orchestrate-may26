"""
retriever.py
------------
Builds a LangChain FAISS vector store from the corpus documents and
exposes retrieval utilities backed by LangChain abstractions.

LangChain primitives used:
  - HuggingFaceEmbeddings (sentence-transformers) → dense embeddings
  - FAISS                                         → vector store + ANN search
  - VectorStoreRetriever (via .as_retriever())    → LangChain BaseRetriever
  - Document                                      → unified chunk type

The FAISS index is cached to disk so repeated runs skip rebuilding.

Public API
----------
  get_vectorstore(force_rebuild)     → raw FAISS VectorStore
  get_retriever(company_filter, top_k) → LangChain VectorStoreRetriever
  retrieve(query, top_k, company_filter) → List[Document]  (convenience)
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import List, Optional

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever

from corpus_loader import load_corpus

# ── constants ─────────────────────────────────────────────────────────────────
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K           = 5
INDEX_DIR       = Path(__file__).parent / ".cache" / "faiss_store"
# ─────────────────────────────────────────────────────────────────────────────


def _get_embeddings() -> HuggingFaceEmbeddings:
    """Initialise the HuggingFace sentence-transformer embedding model."""
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        encode_kwargs={"normalize_embeddings": True},
    )


def _build_vectorstore(docs: List[Document]) -> FAISS:
    """Embed all documents and build a FAISS index from scratch."""
    from tqdm import tqdm
    print(f"[Retriever] Building FAISS index from {len(docs)} chunks …", flush=True)
    embeddings = _get_embeddings()
    
    # Building in batches with progress bar
    batch_size = 100
    texts = [d.page_content for d in docs]
    metadatas = [d.metadata for d in docs]
    
    vs = None
    for i in tqdm(range(0, len(texts), batch_size), desc="Indexing chunks"):
        batch_texts = texts[i : i + batch_size]
        batch_metas = metadatas[i : i + batch_size]
        if vs is None:
            vs = FAISS.from_texts(batch_texts, embeddings, metadatas=batch_metas)
        else:
            vs.add_texts(batch_texts, metadatas=batch_metas)
            
    print("[Retriever] Index built.")
    return vs


def _save_vectorstore(vs: FAISS) -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    vs.save_local(str(INDEX_DIR))
    print(f"[Retriever] Index saved to {INDEX_DIR}")


def _load_vectorstore() -> FAISS:
    embeddings = _get_embeddings()
    vs = FAISS.load_local(
        str(INDEX_DIR),
        embeddings,
        allow_dangerous_deserialization=True,
    )
    print(f"[Retriever] Loaded cached index from {INDEX_DIR}")
    return vs


# ── singleton ─────────────────────────────────────────────────────────────────
_vectorstore: Optional[FAISS] = None


def get_vectorstore(force_rebuild: bool = False) -> FAISS:
    """
    Return (or build) the singleton FAISS vector store.

    On first call the index is built from the corpus and saved to disk.
    Subsequent calls load the cached index unless force_rebuild=True.
    """
    global _vectorstore
    if _vectorstore is not None and not force_rebuild:
        return _vectorstore

    if INDEX_DIR.exists() and not force_rebuild:
        _vectorstore = _load_vectorstore()
    else:
        docs = load_corpus()
        _vectorstore = _build_vectorstore(docs)
        _save_vectorstore(_vectorstore)

    return _vectorstore


# ── LangChain Retriever factory ───────────────────────────────────────────────

def get_retriever(
    company_filter: Optional[str] = None,
    top_k: int = TOP_K,
) -> VectorStoreRetriever:
    """
    Return a LangChain ``VectorStoreRetriever`` backed by the FAISS index.

    This is the proper LangChain RAG abstraction — it implements
    ``BaseRetriever`` and is composable inside LCEL chains via the pipe
    operator (``|``).

    Parameters
    ----------
    company_filter:
        If provided (e.g. "HackerRank"), only chunks whose
        ``metadata["company"]`` matches are considered.  Falls back to
        unfiltered search when no matches are found.
    top_k:
        Number of documents to retrieve.

    Returns
    -------
    VectorStoreRetriever
        A LangChain retriever that wraps the FAISS similarity search.

    Example
    -------
    >>> retriever = get_retriever(company_filter="Visa", top_k=5)
    >>> docs = retriever.invoke("how do I dispute a transaction?")
    """
    vs = get_vectorstore()
    search_kwargs: dict = {"k": top_k}
    if company_filter:
        search_kwargs["filter"] = {"company": company_filter}

    return vs.as_retriever(
        search_type="similarity",
        search_kwargs=search_kwargs,
    )


# ── convenience wrapper ───────────────────────────────────────────────────────

def retrieve(
    query: str,
    top_k: int = TOP_K,
    company_filter: Optional[str] = None,
) -> List[Document]:
    """
    Return the top_k most semantically relevant Documents for ``query``.

    Uses ``get_retriever()`` internally so the retrieval path is always
    backed by the same LangChain abstraction.

    Falls back to unfiltered results when the company filter is too
    strict and returns fewer than ``top_k`` docs.
    """
    retriever = get_retriever(company_filter=company_filter, top_k=top_k)
    results: List[Document] = retriever.invoke(query)

    # fall back to unfiltered if the company-scoped filter was too strict
    if company_filter and len(results) < top_k:
        fallback_retriever = get_retriever(company_filter=None, top_k=top_k)
        unfiltered = fallback_retriever.invoke(query)
        seen = {id(d) for d in results}
        for doc in unfiltered:
            if id(doc) not in seen:
                results.append(doc)
            if len(results) >= top_k:
                break

    return results[:top_k]
