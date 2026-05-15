import os
import glob
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.chunks = []
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None
        self._load_data()

    def _load_data(self):
        # Recursively find all .txt and .md files
        file_paths = glob.glob(os.path.join(self.data_dir, "**", "*.md"), recursive=True) + \
                     glob.glob(os.path.join(self.data_dir, "**", "*.txt"), recursive=True)

        for file_path in file_paths:
            # Infer company from path
            company = "general"
            path_lower = file_path.lower()
            if "hackerrank" in path_lower:
                company = "hackerrank"
            elif "claude" in path_lower:
                company = "claude"
            elif "visa" in path_lower:
                company = "visa"

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self._chunk_content(content, file_path, company)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

        if self.chunks:
            texts = [c['text'] for c in self.chunks]
            self.tfidf_matrix = self.vectorizer.fit_transform(texts)
            print(f"Total chunks indexed: {len(self.chunks)}")
        else:
            print("No data found to index.")

    def _chunk_content(self, content, file_path, company, chunk_size=300, overlap=50):
        words = content.split()
        if not words:
            return

        for i in range(0, len(words), chunk_size - overlap):
            chunk_words = words[i:i + chunk_size]
            chunk_text = " ".join(chunk_words)
            self.chunks.append({
                "text": chunk_text,
                "source_file": file_path,
                "company": company,
                "chunk_index": len(self.chunks)
            })
            if i + chunk_size >= len(words):
                break

    def retrieve(self, query: str, company: str = None, top_k: int = 5) -> list[dict]:
        if not self.chunks or self.tfidf_matrix is None:
            return []

        # Filter chunks by company if provided
        filtered_indices = []
        if company and company.lower() != "none":
            target_company = company.lower()
            filtered_indices = [i for i, c in enumerate(self.chunks) if c['company'] == target_company]
            
            # If no chunks for specific company, fall back to all or general
            if not filtered_indices:
                filtered_indices = range(len(self.chunks))
        else:
            filtered_indices = range(len(self.chunks))

        filtered_indices = list(filtered_indices)
        if not filtered_indices:
            return []

        # Transform query
        query_vec = self.vectorizer.transform([query])
        
        # Calculate similarities for filtered subset
        subset_matrix = self.tfidf_matrix[filtered_indices]
        similarities = cosine_similarity(query_vec, subset_matrix).flatten()
        
        # Get top K
        top_indices = similarities.argsort()[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            orig_idx = filtered_indices[idx]
            results.append({
                "text": self.chunks[orig_idx]["text"],
                "source_file": self.chunks[orig_idx]["source_file"],
                "company": self.chunks[orig_idx]["company"],
                "score": float(similarities[idx])
            })
            
        return results

# Singleton instance for startup efficiency
_retriever = None

def get_retriever():
    global _retriever
    if _retriever is None:
        _retriever = Retriever()
    return _retriever

def retrieve(query: str, company: str = None, top_k: int = 5) -> list[dict]:
    return get_retriever().retrieve(query, company, top_k)
