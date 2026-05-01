"""
Corpus Index: Load, parse, and retrieve documents from support documentation.

Uses keyword search (BM25-like) for efficient retrieval.
Semantic search via embeddings available if optional dependencies installed.
"""

import os
import re
import json
import logging
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from collections import defaultdict

try:
    # Optional embeddings support
    import numpy as np
    from sentence_transformers import SentenceTransformer
    import faiss
    HAS_EMBEDDINGS = True
except (ImportError, ValueError) as e:
    # Valley on dependency conflicts (e.g., TensorFlow version issues)
    HAS_EMBEDDINGS = False

logger = logging.getLogger(__name__)


class CorpusIndex:
    """Index and retrieve documents from the support corpus."""

    def __init__(self, corpus_path: str):
        """Initialize corpus index from directory structure.
        
        Args:
            corpus_path: Path to data directory with claude/, hackerrank/, visa/ subdirs
        """
        self.corpus_path = Path(corpus_path)
        self.documents = []  # List of {id, content, source, product, category}
        self.embeddings = None
        self.index = None
        self.embedding_model = None
        
        # Category mappings for each product
        self.category_keywords = {
            "Claude": {
                "API": ["api", "endpoint", "authentication", "request"],
                "Models": ["model", "claude", "version", "capability"],
                "Billing": ["price", "cost", "billing", "token", "quota"],
                "Account": ["account", "login", "signup", "password"],
                "Desktop": ["desktop", "app", "installation"],
                "Extensions": ["extension", "integrate", "plugin"]
            },
            "HackerRank": {
                "Assessments": ["test", "assessment", "question", "score"],
                "Hiring": ["recruiter", "hire", "interview", "candidate"],
                "Coding": ["code", "challenge", "solution", "language"],
                "Settings": ["settings", "configure", "profile"]
            },
            "Visa": {
                "Payment": ["payment", "transaction", "card"],
                "Merchant": ["merchant", "settlement", "processor"],
                "Dispute": ["dispute", "chargeback", "fraud"]
            }
        }
        
        # Load corpus
        self._load_corpus()
        
        # Build index
        if HAS_EMBEDDINGS:
            self._build_embedding_index()
        else:
            logger.warning("Embeddings not available, using keyword search only")

    def _load_corpus(self):
        """Load all markdown files from corpus directory."""
        logger.info(f"Loading corpus from {self.corpus_path}")
        
        for product_dir in ["claude", "hackerrank", "visa"]:
            product_path = self.corpus_path / product_dir
            if not product_path.exists():
                logger.warning(f"Product directory not found: {product_path}")
                continue
            
            # Infer product name
            product_name = {
                "claude": "Claude",
                "hackerrank": "HackerRank",
                "visa": "Visa"
            }.get(product_dir, product_dir)
            
            # Load all markdown files recursively
            for md_file in product_path.rglob("*.md"):
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Extract relative path for category
                    rel_path = md_file.relative_to(product_path)
                    category = str(rel_path.parent).replace("/", " > ")
                    
                    # Clean up content
                    content = self._clean_content(content)
                    if len(content) < 10:
                        continue
                    
                    doc_id = len(self.documents)
                    self.documents.append({
                        "id": doc_id,
                        "content": content,
                        "source": str(rel_path),
                        "file_path": str(md_file),
                        "product": product_name,
                        "category": category
                    })
                except Exception as e:
                    logger.warning(f"Failed to load {md_file}: {e}")
        
        logger.info(f"Loaded {len(self.documents)} documents")

    def _clean_content(self, content: str) -> str:
        """Clean markdown content."""
        # Remove frontmatter
        content = re.sub(r'^---.*?---\n', '', content, flags=re.DOTALL)
        # Remove HTML tags
        content = re.sub(r'<[^>]+>', '', content)
        # Remove extra whitespace
        content = re.sub(r'\s+', ' ', content).strip()
        return content

    def _build_embedding_index(self):
        """Build FAISS index for semantic search (optional)."""
        if not HAS_EMBEDDINGS:
            logger.info("Embeddings disabled (optional dependencies not available)")
            return
            
        try:
            logger.info("Loading embedding model...")
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
            
            # Chunk content for better embeddings
            chunks = []
            chunk_to_doc = []
            
            for doc in self.documents:
                # Split into 500-char chunks with overlap
                content = doc["content"]
                for i in range(0, len(content), 400):
                    chunk = content[i:i+500]
                    if len(chunk) > 50:
                        chunks.append(chunk)
                        chunk_to_doc.append(doc["id"])
            
            logger.info(f"Embedding {len(chunks)} chunks...")
            embeddings = self.embedding_model.encode(chunks, show_progress_bar=False)
            embeddings = np.array(embeddings).astype('float32')
            
            # Build FAISS index
            faiss.normalize_L2(embeddings)
            self.index = faiss.IndexFlatIP(embeddings.shape[1])
            self.index.add(embeddings)
            
            self.embeddings = embeddings
            self.chunk_to_doc = chunk_to_doc
            
            logger.info(f"Built FAISS index with {len(chunks)} chunks")
        except Exception as e:
            logger.warning(f"Failed to build embedding index: {e}. Using keyword search.")
            self.embedding_model = None

    def retrieve(self, query: str, company: Optional[str] = None, limit: int = 5) -> List[Dict]:
        """Retrieve relevant documents for a query.
        
        Args:
            query: Search query
            company: Optional company filter (Claude, HackerRank, Visa)
            limit: Maximum number of results
            
        Returns:
            List of documents with scores
        """
        results = []
        
        # Try semantic search first
        if self.embedding_model and self.index:
            results = self._semantic_search(query, company, limit)
        
        # Fall back to keyword search if no results
        if not results:
            results = self._keyword_search(query, company, limit)
        
        return results

    def _semantic_search(self, query: str, company: Optional[str], limit: int) -> List[Dict]:
        """Semantic search using embeddings."""
        try:
            # Embed query
            query_embedding = self.embedding_model.encode([query], show_progress_bar=False)[0]
            query_embedding = np.array([query_embedding]).astype('float32')
            faiss.normalize_L2(query_embedding)
            
            # Search
            distances, indices = self.index.search(query_embedding, min(limit * 2, len(self.embeddings)))
            
            seen_docs = set()
            for dist, idx in zip(distances[0], indices[0]):
                if idx < 0 or idx >= len(self.chunk_to_doc):
                    continue
                
                doc_id = self.chunk_to_doc[idx]
                if doc_id in seen_docs:
                    continue
                seen_docs.add(doc_id)
                
                doc = self.documents[doc_id]
                
                # Filter by company if specified
                if company and doc["product"] != company:
                    continue
                
                results.append({
                    "id": doc_id,
                    "content": doc["content"][:500],
                    "source": doc["source"],
                    "product": doc["product"],
                    "category": doc["category"],
                    "score": float(dist)  # IP distance = similarity
                })
                
                if len(results) >= limit:
                    break
            
            return results
        except Exception as e:
            logger.warning(f"Semantic search failed: {e}")
            return []

    def _keyword_search(self, query: str, company: Optional[str], limit: int) -> List[Dict]:
        """Fallback keyword search."""
        query_lower = query.lower()
        query_terms = set(query_lower.split())
        
        scored = []
        for doc in self.documents:
            # Filter by company if specified
            if company and doc["product"] != company:
                continue
            
            content_lower = doc["content"].lower()
            
            # Score based on term overlap
            matches = sum(1 for term in query_terms if term in content_lower)
            if matches > 0:
                score = matches / len(query_terms)
                scored.append((score, doc))
        
        # Sort by score descending and return top limit
        scored.sort(key=lambda x: x[0], reverse=True)
        
        return [
            {
                "id": doc["id"],
                "content": doc["content"][:500],
                "source": doc["source"],
                "product": doc["product"],
                "category": doc["category"],
                "score": score
            }
            for score, doc in scored[:limit]
        ]
