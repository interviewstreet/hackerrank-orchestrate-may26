"""
Local Embeddings Store
Simple JSON-based storage for embeddings + BM25 for retrieval.
No external dependencies like ChromaDB.
"""

import os
import json
import pickle
from pathlib import Path
from typing import Optional
import numpy as np


class LocalStore:
    """
    Stores embeddings locally in JSON format.
    Each domain has its own collection file.
    """
    
    def __init__(self, store_dir: str):
        self.store_dir = store_dir
        os.makedirs(store_dir, exist_ok=True)
    
    def _collection_path(self, collection_name: str) -> str:
        return os.path.join(self.store_dir, f"{collection_name}.json")
    
    def get_or_create_collection(self, name: str) -> "Collection":
        """Get or create a collection (domain)."""
        return Collection(self.store_dir, name)
    
    def delete_collection(self, name: str):
        """Delete a collection."""
        path = self._collection_path(name)
        if os.path.exists(path):
            os.remove(path)


class Collection:
    """Represents a single collection (domain) with embeddings."""
    
    def __init__(self, store_dir: str, name: str):
        self.store_dir = store_dir
        self.name = name
        self.path = os.path.join(store_dir, f"{name}.json")
        self._load()
    
    def _load(self):
        """Load collection from disk."""
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.data = data
            except Exception as e:
                print(f"[local_store] Error loading {self.path}: {e}")
                self.data = {"ids": [], "documents": [], "embeddings": [], "metadatas": []}
        else:
            self.data = {"ids": [], "documents": [], "embeddings": [], "metadatas": []}
    
    def _save(self):
        """Save collection to disk."""
        os.makedirs(self.store_dir, exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    def count(self) -> int:
        """Return number of chunks in collection."""
        return len(self.data.get("ids", []))
    
    def upsert(self, ids: list[str], documents: list[str], embeddings: list[list[float]], 
               metadatas: list[dict]):
        """
        Insert or update chunks.
        - ids: unique identifiers
        - documents: text chunks
        - embeddings: embedding vectors
        - metadatas: metadata dicts
        """
        # Build ID→index map for existing data
        existing_ids = {id_: i for i, id_ in enumerate(self.data.get("ids", []))}
        
        for id_, doc, emb, meta in zip(ids, documents, embeddings, metadatas):
            if id_ in existing_ids:
                # Update existing
                idx = existing_ids[id_]
                self.data["documents"][idx] = doc
                self.data["embeddings"][idx] = emb
                self.data["metadatas"][idx] = meta
            else:
                # Insert new
                self.data["ids"].append(id_)
                self.data["documents"].append(doc)
                self.data["embeddings"].append(emb)
                self.data["metadatas"].append(meta)
        
        self._save()
    
    def query(self, query_embeddings: list[list[float]], n_results: int, 
              include: list[str] = None) -> dict:
        """
        Query by embedding similarity.
        Returns top-n results with cosine distance.
        """
        if include is None:
            include = ["documents", "metadatas", "distances"]
        
        if self.count() == 0:
            return {
                "documents": [[]],
                "metadatas": [[]],
                "distances": [[]],
                "ids": [[]],
            }
        
        query_embedding = np.array(query_embeddings[0])  # Single query
        stored_embeddings = np.array(self.data["embeddings"])
        
        # Cosine similarity: 1 - cosine_distance
        # Distance = 1 - (A·B / |A||B|)
        norms = np.linalg.norm(stored_embeddings, axis=1)
        query_norm = np.linalg.norm(query_embedding)
        
        # Avoid division by zero
        safe_norms = np.where(norms > 0, norms, 1)
        normalized = stored_embeddings / safe_norms[:, np.newaxis]
        query_normalized = query_embedding / (query_norm if query_norm > 0 else 1)
        
        # Cosine similarity
        similarities = np.dot(normalized, query_normalized)
        # Convert to distance (0 to 2, where 0 = identical)
        distances = 1 - similarities
        
        # Get top-n
        top_indices = np.argsort(distances)[:n_results].tolist()
        
        result = {
            "ids": [[self.data["ids"][i] for i in top_indices]] if "ids" in include else [[]],
            "documents": [[self.data["documents"][i] for i in top_indices]] if "documents" in include else [[]],
            "metadatas": [[self.data["metadatas"][i] for i in top_indices]] if "metadatas" in include else [[]],
            "distances": [[float(distances[i]) for i in top_indices]] if "distances" in include else [[]],
        }
        
        return result
    
    def get(self, include: list[str] = None) -> dict:
        """Get all documents in collection."""
        if include is None:
            include = ["documents", "metadatas"]
        
        return {
            "ids": self.data.get("ids", []) if "ids" in include else [],
            "documents": self.data.get("documents", []) if "documents" in include else [],
            "metadatas": self.data.get("metadatas", []) if "metadatas" in include else [],
        }
