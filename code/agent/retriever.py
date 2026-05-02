"""
retriever.py — Knowledge base retrieval engine.

Responsible for:
  - Loading the pre-built BM25 index over the corpus
  - Querying the index with ticket text to fetch top-k relevant chunks
  - Scoping retrieval by domain (hackerrank / claude / visa)
"""
