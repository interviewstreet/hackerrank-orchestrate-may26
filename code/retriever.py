from typing import List, Dict, Optional
from pathlib import Path

from corpus_index import CorpusIndex


class Retriever:
    """Wrapper around CorpusIndex to provide a simple retrieve API."""

    def __init__(self, corpus_path: str = "../data"):
        self.corpus_path = Path(corpus_path)
        self.index = CorpusIndex(str(self.corpus_path))

    @property
    def document_count(self) -> int:
        return len(self.index.documents)

    def retrieve(self, query: str, company: Optional[str] = None, limit: int = 5) -> List[Dict]:
        return self.index.retrieve(query, company=company, limit=limit)
