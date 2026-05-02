# Support Agent Implementation

## Installation

```bash
pip install -r requirements.txt
```

**Dependencies:** `groq`, `sentence-transformers`, `faiss-cpu`

## Environment Setup

Create a `.env` file in the `code/` directory (copied from `.env.example`):

```bash
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

```bash
python main.py
```

**First run:** Loads all markdown docs from `../data/`, splits into overlapping chunks (500 words, 50-word overlap), generates embeddings using `all-MiniLM-L6-v2`, builds a FAISS vector index saved to `vector_db/`, then processes all tickets.

**Subsequent runs:** Loads the pre-built FAISS index and processes tickets immediately.

Output is written to `../support_tickets/output.csv`.

## Architecture

- `main.py` — Entry point; loads/builds vector index, runs pipeline
- `config.py` — Configuration (paths, model names, top-k)
- `corpus.py` — Document loading, chunking, FAISS index builder
- `retriever.py` — Semantic search with FAISS (cosine similarity on sentence-transformers embeddings)
- `classifier.py` — Ticket categorization by product area & request type
- `escalator.py` — High-risk/out-of-scope detection
- `generator.py` — LLM response generation via Groq (Llama 3.1 8B)
- `pipeline.py` — Orchestration: escalation → classification → retrieval → generation

**RAG strategy:** Overlapping chunks (500 words, 50 overlap) → sentence-transformers embeddings → FAISS cosine search → top-5 chunks × 2000 chars → Groq LLM.