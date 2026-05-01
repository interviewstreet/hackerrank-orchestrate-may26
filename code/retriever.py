"""
Builds a FAISS vector store from the support corpus using HuggingFace
sentence-transformers embeddings (all-MiniLM-L6-v2, free, runs locally).

Provides a retriever that can filter by domain for targeted search.
"""

from typing import List, Optional

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from corpus_loader import load_corpus, REPO_ROOT

INDEX_DIR = REPO_ROOT / "data" / "index"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def get_embeddings() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True, "batch_size": 64},
    )


def build_vector_store(force_rebuild: bool = False) -> FAISS:
    """Build or load the FAISS vector store."""
    embeddings = get_embeddings()

    if INDEX_DIR.exists() and not force_rebuild:
        try:
            return FAISS.load_local(
                str(INDEX_DIR), embeddings, allow_dangerous_deserialization=True
            )
        except Exception:
            pass

    print("Building vector store from corpus...")
    documents = load_corpus()
    print(f"Loaded {len(documents)} raw documents")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n## ", "\n### ", "\n#### ", "\n\n", "\n", ". ", " "],
    )
    chunks = splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")

    store = FAISS.from_documents(chunks, embeddings)

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    store.save_local(str(INDEX_DIR))
    print(f"Vector store saved to {INDEX_DIR}")

    return store


def get_retriever(
    store: FAISS,
    domain: Optional[str] = None,
    k: int = 8,
):
    """Return a retriever, optionally filtered to a specific domain."""
    search_kwargs = {"k": k}
    if domain and domain != "None":
        search_kwargs["filter"] = {"domain": domain}
    return store.as_retriever(search_kwargs=search_kwargs)


def retrieve_relevant_docs(
    store: FAISS,
    query: str,
    domain: Optional[str] = None,
    k: int = 8,
) -> List[Document]:
    """Retrieve the most relevant documents for a query."""
    retriever = get_retriever(store, domain=domain, k=k)
    return retriever.invoke(query)


if __name__ == "__main__":
    store = build_vector_store()
    docs = retrieve_relevant_docs(store, "How do I reset my password?", domain="HackerRank")
    print(f"\nRetrieved {len(docs)} docs:")
    for d in docs:
        print(f"  [{d.metadata['domain']}] {d.metadata['source'][:60]}: {d.page_content[:100]}...")
