import os
import glob
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import numpy as np
import json


# Load embedding model globally (lazy load on first use)
_embedding_model = None

def get_embedding_model():
    """Lazy-load the sentence transformer model."""
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    return _embedding_model


def load_corpus(data_dir: str) -> List[Dict]:
    documents = []
    md_pattern = os.path.join(data_dir, "**/*.md")
    
    for filepath in glob.glob(md_pattern, recursive=True):
        if filepath.endswith("index.md"):
            continue
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                content = strip_frontmatter(content)
                content = content.strip()
                if not content or len(content) < 50:
                    continue
                chunks = chunk_text(content, filepath)
                documents.extend(chunks)
        except Exception as e:
            print(f"Warning: Could not load {filepath}: {e}")
    
    return documents


def strip_frontmatter(content: str) -> str:
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return content


def chunk_text(text: str, filepath: str, max_words: int = 500, overlap: int = 50) -> List[Dict]:
    """Split text into overlapping chunks to preserve context boundaries."""
    words = text.split()
    chunks = []
    
    if len(words) <= max_words:
        # Single chunk for short texts
        chunk = {
            "text": text,
            "source": filepath,
            "metadata": {}
        }
        chunks.append(chunk)
    else:
        # Overlapping chunks with stride
        stride = max_words - overlap
        for i in range(0, len(words), stride):
            chunk_words = words[i:i + max_words]
            chunk_text_out = " ".join(chunk_words)
            chunk = {
                "text": chunk_text_out,
                "source": filepath,
                "metadata": {}
            }
            chunks.append(chunk)
    
    return chunks


def build_index(documents: List[Dict], persist_dir: str):
    """Generate embeddings for documents and build a FAISS index."""
    os.makedirs(persist_dir, exist_ok=True)
    
    model = get_embedding_model()
    texts = [doc["text"] for doc in documents]
    
    print(f"Generating embeddings for {len(texts)} chunks...")
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    
    # Normalize embeddings for cosine similarity
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    
    # Build FAISS index
    import faiss
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # Inner product for normalized vectors = cosine
    index.add(embeddings.astype('float32'))
    
    # Save index and documents
    faiss.write_index(index, os.path.join(persist_dir, "faiss.index"))
    
    # Save documents with embeddings for persistence
    index_data = []
    for i, doc in enumerate(documents):
        domain = "hackerrank" if "/hackerrank/" in doc["source"] else \
                 ("claude" if "/claude/" in doc["source"] else "visa")
        index_data.append({
            "text": doc["text"],
            "source": doc["source"],
            "domain": domain,
            "embedding": embeddings[i].tolist()
        })
    
    with open(os.path.join(persist_dir, "documents.json"), 'w') as f:
        json.dump({"documents": index_data}, f)
    
    print(f"Index built with {len(documents)} documents. Saved to {persist_dir}")


def load_index(persist_dir: str):
    """Load FAISS index and document metadata from disk."""
    import faiss
    
    index_path = os.path.join(persist_dir, "faiss.index")
    docs_path = os.path.join(persist_dir, "documents.json")
    
    if not os.path.exists(index_path) or not os.path.exists(docs_path):
        return None, None
    
    index = faiss.read_index(index_path)
    with open(docs_path, 'r') as f:
        data = json.load(f)
    
    documents = data["documents"]
    return index, documents
