import json
import os
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from corpus import load_index


_embedding_model = None

def get_embedding_model():
    """Lazy-load the sentence transformer model."""
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    return _embedding_model


class Retriever:
    def __init__(self, persist_dir: str, top_k: int = 5):
        self.top_k = top_k
        self.persist_dir = persist_dir
        self.index = None
        self.documents = []
        self.model = get_embedding_model()
        self._load_or_create_index()
    
    def _load_or_create_index(self):
        """Load FAISS index and documents from disk, or initialize empty."""
        os.makedirs(self.persist_dir, exist_ok=True)
        self.index, self.documents = load_index(self.persist_dir)
        
        if self.index is None or self.documents is None:
            print(f"No existing index found in {self.persist_dir}. "
                  "Please run build_index() first.")
            self.index = None
            self.documents = []
    
    def build_index(self, documents: List[Dict]):
        """Build and save a new FAISS index from documents."""
        from corpus import build_index
        build_index(documents, self.persist_dir)
        self.index, self.documents = load_index(self.persist_dir)
    
    def query(self, text: str, company: str = None) -> List[Dict]:
        """Retrieve top-k most similar documents using vector similarity."""
        if self.index is None or not self.documents:
            return []
        
        # Encode query
        query_embedding = self.model.encode([text], convert_to_numpy=True)
        query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)
        query_embedding = query_embedding.astype('float32')
        
        # Search FAISS index
        scores, indices = self.index.search(query_embedding, self.top_k * 2)  # Fetch extra for filtering
        
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx >= len(self.documents):
                continue
            
            doc = self.documents[idx]
            domain = doc.get("domain", "")
            
            # Apply domain filter if company specified
            if company and company != "None":
                if domain != company.lower():
                    continue
            
            results.append({
                "text": doc["text"],
                "source": doc["source"],
                "distance": 1 - float(score)  # Convert cosine similarity to distance-like metric
            })
            
            if len(results) >= self.top_k:
                break
        
        return results
