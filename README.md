# HackerRank Orchestrate Support Agent

AI-powered support agent that automatically resolves real customer tickets for **HackerRank**, **Claude**, and **Visa** using semantic search over a local knowledge base.

Built for the HackerRank Orchestrate 24-hour hackathon (May 2026).

---

## What it does

Given a CSV of support tickets (`support_tickets.csv`), the agent:

1. **Escalates** high-risk or out-of-scope requests (identity theft, security issues, policy violations)
2. **Classifies** each ticket by product area and request type
3. **Retrieves** relevant documentation from a local corpus using **semantic vector search** (sentence-transformers + FAISS)
4. **Generates** accurate, helpful responses grounded solely in the retrieved context — no hallucinations

Outputs a complete `support_tickets/output.csv` with responses for all tickets.

---

## Quickstart

```bash
# Clone & setup
git clone <repo-url>
cd hackerrank-orchestrate-may26
python3 -m venv venv
source venv/bin/activate

# Install dependencies
cd code
pip install -r requirements.txt

# Configure Groq API key
cp .env.example .env
# Edit .env: GROQ_API_KEY=your_key_here

# Run
python main.py
```

First run builds a **FAISS vector index** from the `../data/` corpus (~1,085 markdown files → 1,512 overlapping chunks). Subsequent runs load the cached index instantly.

---

## Key features

| Feature | Implementation |
|---|---|
| **Semantic search** | `all-MiniLM-L6-v2` embeddings + FAISS cosine similarity |
| **Context preservation** | 500-word overlapping chunks (50-word overlap) |
| **Large context window** | Top-5 chunks × 2,000 chars each (~10K total) |
| **Deterministic output** | Temperature = 0.1 (Llama 3.1 8B via Groq) |
| **Safety-first** | Pre-defined escalation patterns; no guessing on sensitive issues |
| **Persistent index** | FAISS index saved to `code/vector_db/` (~20 MB) |

---

## Project structure

```
.
├── code/
│   ├── main.py           # Entry point
│   ├── config.py         # Settings & paths
│   ├── corpus.py         # Load, chunk, and build FAISS index
│   ├── retriever.py      # Semantic search over vector DB
│   ├── classifier.py     # Ticket categorization
│   ├── escalator.py      # Risk & scope detection
│   ├── generator.py      # LLM response generation
│   ├── pipeline.py       # Orchestration logic
│   ├── vector_db/        # Persisted FAISS index (built on first run)
│   │   ├── faiss.index
│   │   └── documents.json
│   ├── requirements.txt  # Dependencies
│   └── README.md         # This folder's README
├── data/                 # Support corpus (HackerRank, Claude, Visa)
├── support_tickets/
│   ├── support_tickets.csv   # Input tickets
│   └── output.csv            # Agent predictions (generated)
└── README.md            # You are here
```

---

## How it works

```
Ticket (Issue + Subject + Company)
         ↓
   [Escalation check] → sensitive/high-risk? → ESCALATE
         ↓
   [Classifier] → product_area + request_type
         ↓
   [Retriever] → embed query → FAISS similarity search → top-5 chunks
         ↓
   [Generator] → prompt with context → Llama 3.1 8B → response
         ↓
   Written to output.csv
```

**RAG details:**

- Documents split into 500-word chunks with 50-word overlap
- Each chunk embedded to 384-D vector using `all-MiniLM-L6-v2`
- FAISS `IndexFlatIP` stores all vectors (cosine similarity on normalized embeddings)
- Domain filtering applied: results restricted to matching company (`hackerrank` / `claude` / `visa`)
- Retrieved chunks truncated to 2,000 chars each, sent to LLM with strict grounding instruction

---

## Evaluation

The agent is evaluated on:

- **Accuracy** — responses correctly address the ticket using only provided corpus
- **Appropriateness** — escalation decisions handle sensitive cases correctly
- **Architecture** — code quality, design patterns, and engineering rigor
- **AI fluency** — effective use of AI tools (logged in `log.txt`)

See `problem_statement.md` and `evaluation_criteria.md` for full details.

---

## Notes

- Terminal-based only — runs as a Python script, no web/GUI
- Uses only local `data/` corpus — no live web searches
- Responses limited to 2–3 sentences; escalates when context is insufficient
- All API keys read from environment variables (`.env`);
never committed