# Multi-Domain Support Triage Agent

A terminal-based AI agent that triages support tickets across HackerRank, Claude, and Visa ecosystems using RAG (Retrieval-Augmented Generation).

## Architecture

```
corpus_loader.py   - Loads all .md files from data/ into LangChain Documents
retriever.py       - Builds FAISS vector store with HuggingFace embeddings
agent.py           - Triage logic: retrieval -> classification -> response generation
main.py            - CLI entry point, CSV processing
```

### Design Decisions

- **LLM**: Groq (llama-3.3-70b-versatile) — fast inference, free tier available
- **Embeddings**: HuggingFace `sentence-transformers/all-MiniLM-L6-v2` — runs locally, no API key needed, good quality for semantic search
- **Vector Store**: FAISS — lightweight, no external service needed, persists to disk
- **Framework**: LangChain — clean abstractions for RAG pipeline

### How It Works

1. **Corpus Ingestion**: All 774 markdown files from `data/` are loaded, chunked (1000 chars, 200 overlap), and embedded into a FAISS vector store.
2. **Retrieval**: For each ticket, the agent retrieves the top 6-8 most relevant corpus chunks, filtered by domain when company is known.
3. **Triage**: The LLM analyzes the ticket against retrieved corpus documents and produces:
   - `status`: reply directly or escalate to human
   - `product_area`: relevant support category
   - `response`: grounded answer from corpus
   - `justification`: reasoning for the decision
   - `request_type`: classification (product_issue, feature_request, bug, invalid)
4. **Safety**: High-risk scenarios (billing, fraud, account security, legal) are always escalated. Out-of-scope issues get an `invalid` classification.

## Setup

### Prerequisites

- Python 3.10+
- Groq API key (free at https://console.groq.com)

### Installation

```bash
cd code/
pip install -r requirements.txt
```

### Environment Variables

Copy the example and add your key:

```bash
cp ../.env.example ../.env
# Edit .env and set GROQ_API_KEY=your_key_here
```

Or export directly:

```bash
export GROQ_API_KEY=your_key_here
```

## Usage

### Process all support tickets (generates output.csv)

```bash
cd code/
python main.py
```

### Process sample tickets (for development/testing)

```bash
python main.py --sample
```

### Triage a single issue interactively

```bash
python main.py --single "I can't log into my HackerRank account" --company HackerRank
```

### Force rebuild the vector index

```bash
python main.py --rebuild-index
```

### Quiet mode (minimal output)

```bash
python main.py --quiet
```

## Output

Results are written to `support_tickets/output.csv` with columns:
- `Issue`, `Subject`, `Company` (from input)
- `Response`, `Product Area`, `Status`, `Request Type` (generated)

## Determinism

- LLM temperature is set to 0.0 with seed=42
- Embeddings are deterministic (same model, same input = same vectors)
- Document loading order is sorted for consistency
