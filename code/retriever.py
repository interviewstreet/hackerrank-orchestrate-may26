import hashlib
import re
from pathlib import Path

import chromadb
import parlant.sdk as p
from chromadb.utils import embedding_functions

DATA_DIR = Path(__file__).parent.parent / "data"
CHROMA_PATH = Path(__file__).parent / "chroma_db"
COLLECTION_NAME = "support_corpus"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
MAX_WORDS_PER_CHUNK = 800

_collection: chromadb.Collection | None = None


def get_company_from_path(path: Path) -> str:
    parts = path.parts
    for i, part in enumerate(parts):
        if part == "data" and i + 1 < len(parts):
            return parts[i + 1].lower()
    return "unknown"


def get_product_area_from_path(path: Path) -> str:
    parts = path.parts
    try:
        data_idx = list(parts).index("data")
        # third segment after data/ is the product area (e.g. data/hackerrank/screen/...)
        if data_idx + 2 < len(parts):
            return parts[data_idx + 2].lower().replace("-", "_")
        elif data_idx + 1 < len(parts):
            return parts[data_idx + 1].lower().replace("-", "_")
    except ValueError:
        pass
    return "general"


def extract_title(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def chunk_document(text: str) -> list[str]:
    words = text.split()
    if len(words) <= MAX_WORDS_PER_CHUNK:
        return [text]

    # Split at ## headings
    sections = re.split(r"\n(?=##\s)", text)
    chunks = []
    current = ""
    for section in sections:
        if len((current + "\n" + section).split()) <= MAX_WORDS_PER_CHUNK:
            current = (current + "\n" + section).strip()
        else:
            if current:
                chunks.append(current)
            current = section.strip()
    if current:
        chunks.append(current)
    return chunks or [text]


def build_index() -> None:
    if CHROMA_PATH.exists() and any(CHROMA_PATH.iterdir()):
        print(f"[retriever] ChromaDB index already exists at {CHROMA_PATH}, skipping build.")
        return

    print("[retriever] Building ChromaDB index from support corpus...")
    CHROMA_PATH.mkdir(parents=True, exist_ok=True)

    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=ef,
        metadata={"hnsw:space": "cosine"},
    )

    md_files = list(DATA_DIR.rglob("*.md"))
    print(f"[retriever] Found {len(md_files)} markdown files.")

    ids, docs, metas = [], [], []
    for filepath in md_files:
        try:
            text = filepath.read_text(encoding="utf-8", errors="replace").strip()
        except Exception as e:
            print(f"[retriever] Skipping {filepath}: {e}")
            continue

        if not text:
            continue

        company = get_company_from_path(filepath)
        product_area = get_product_area_from_path(filepath)
        title = extract_title(text, fallback=filepath.stem)
        chunks = chunk_document(text)

        for i, chunk in enumerate(chunks):
            chunk_id = hashlib.md5(f"{filepath}:{i}".encode()).hexdigest()
            ids.append(chunk_id)
            docs.append(chunk)
            metas.append(
                {
                    "company": company,
                    "product_area": product_area,
                    "title": title,
                    "source_path": str(filepath),
                }
            )

    # Upsert in batches to avoid memory spikes
    batch_size = 100
    for start in range(0, len(ids), batch_size):
        collection.upsert(
            ids=ids[start : start + batch_size],
            documents=docs[start : start + batch_size],
            metadatas=metas[start : start + batch_size],
        )

    print(f"[retriever] Indexed {len(ids)} chunks into ChromaDB.")


def get_collection() -> chromadb.Collection:
    global _collection
    if _collection is not None:
        return _collection

    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )
    client = chromadb.PersistentClient(path=str(CHROMA_PATH))
    _collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=ef,
        metadata={"hnsw:space": "cosine"},
    )
    return _collection


@p.tool
async def rag_lookup(
    context: p.ToolContext,
    query: str,
    company: str,
    top_k: int = 4,
) -> p.ToolResult:
    """Retrieve top_k support corpus chunks relevant to the query.

    Args:
        query: Semantic search query derived from the ticket's core issue.
        company: One of 'hackerrank', 'claude', 'visa', or 'unknown'.
        top_k: Number of results to return.
    """
    try:
        collection = get_collection()
        where_filter = (
            {"company": company.lower()} if company.lower() != "unknown" else None
        )

        results = collection.query(
            query_texts=[query],
            n_results=top_k,
            where=where_filter,
            include=["documents", "metadatas", "distances"],
        )

        chunks = []
        for i in range(len(results["documents"][0])):
            chunks.append(
                {
                    "title": results["metadatas"][0][i].get("title", ""),
                    "text": results["documents"][0][i],
                    "product_area": results["metadatas"][0][i].get("product_area", ""),
                    "company": results["metadatas"][0][i].get("company", ""),
                    "relevance_score": round(
                        1 - results["distances"][0][i], 4
                    ),
                }
            )

        return p.ToolResult(data=chunks)

    except Exception as e:
        print(f"[retriever] rag_lookup error: {e}")
        return p.ToolResult(data=[])
