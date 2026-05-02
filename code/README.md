# Support Triage Agent — Code README

**Multi-Domain Support Triage Agent for HackerRank Orchestrate Hackathon**

## Fast BM25 + Rule-Based Pipeline

This implementation uses a minimal, powerful, zero-dependency stack built for speed and reliability. **No LLMs, no APIs, no vector databases.**

### Why This Stack Wins
- **BM25 Retrieval**: World-class text search algorithm (powers Lucene/ElasticSearch). Zero model download. Matches exact vocabulary.
- **Rules Engine**: Fast regex/keyword classification. 100% deterministic. Zero hallucination risk on high-risk topics.
- **Template Generation**: Answers are pulled directly from the corpus. Guarantees adherence to the "use only provided documentation" rule.
- **Speed**: Ingests 700+ docs, chunks them, and processes 57 tickets in **< 3 seconds**.

## Quick Start

```bash
# 1. Install lean dependencies
pip install pandas pydantic rank-bm25 loguru rich

# 2. Run on all tickets
python code/main.py

# Output saved to: support_tickets/output.csv
```

## Architecture

```
CSV Input
    ↓
classifier.detect_company()      → Keyword based inference
    ↓
safety.check()                   → Fast regex for fraud, injection, bypass
    ↓
BM25Retriever.retrieve()         → Token overlap search (Rank-BM25)
    ↓
agent.generate_response()        → Safely templates the best corpus chunk
    ↓
output.csv + AGENTS.md Logs
```
