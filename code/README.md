# Support Triage Agent

A terminal-based AI agent that resolves support tickets across three ecosystems — **HackerRank**, **Claude**, and **Visa** — using only the provided local support corpus (no live web calls).

---

## Architecture

```
code/
├── main.py           # Entry point — reads CSV, calls agent, writes output.csv
├── agent.py          # Core reasoning: safety checks, retrieval, LLM call, output
├── retriever.py      # FAISS vector index over the corpus chunks
├── corpus_loader.py  # Markdown loader + chunker for data/ directory
├── requirements.txt
└── README.md
```

### Design decisions

| Concern | Approach |
|---|---|
| Retrieval | `sentence-transformers/all-MiniLM-L6-v2` embeddings → FAISS `IndexFlatL2` (converted to 0-1 Cosine similarity scale) |
| Decision Engine | **Retrieval-driven**: Escalate/Auto-reply decisions are mathematically determined *before* the LLM call using strict priority: `Score → Context Quality → Rules → Fallback`. |
| Grounding | High-confidence chunks are injected into LLM context; parametric knowledge is strictly forbidden. |
| Fault Tolerance | If the LLM throws an API error (e.g., Groq `429`), the system seamlessly falls back to answering with raw context chunks rather than artificially escalating. |
| Safety & Rules | High-confidence matches (>0.75) bypass keyword rules. Medium-confidence matches undergo rule-based filters (e.g., adversarial prompts → immediate escalation). |
| Metrics | Auto-Reply Rate, Escalation Rate, and Total Processed counts are automatically calculated at the end of every run. |
| Index cache | Saved to `code/.cache/` — delete to force rebuild |

---

## Setup

### 1. Prerequisites

- Python ≥ 3.10
- An API key for **Groq** (`GROQ_API_KEY`), **OpenAI** (`OPENAI_API_KEY`), **Anthropic** (`ANTHROPIC_API_KEY`), or a local **Ollama** model (`OLLAMA_MODEL`).

### 2. Install dependencies

```bash
cd code/
pip install -r requirements.txt
```

### 3. Set environment variables

Copy the example `.env`:

```bash
# from repo root
cp .env.example .env
```

Edit `.env` and fill in your preferred key (the system cascades through them automatically):

```
GROQ_API_KEY=gsk-...
# or
OPENAI_API_KEY=sk-...
# or
ANTHROPIC_API_KEY=sk-ant-...
# or
OLLAMA_MODEL=llama3
```

---

## Running

From the **repo root** (recommended):

```bash
python code/main.py
```

Or from inside `code/`:

```bash
cd code
python main.py
```

### Options

| Flag | Default | Description |
|---|---|---|
| `--input PATH` | `support_tickets/support_tickets.csv` | Input ticket CSV |
| `--output PATH` | `support_tickets/output.csv` | Output predictions CSV |
| `--rebuild-index` | off | Force rebuild the FAISS index |

### Example (test against sample tickets)

```bash
python code/main.py \
  --input  support_tickets/sample_support_tickets.csv \
  --output support_tickets/sample_output.csv
```

---

## Output schema

The agent appends these columns to each input row:

| Column | Allowed values |
|---|---|
| `status` | `replied`, `escalated` |
| `product_area` | free text — most relevant support category |
| `response` | user-facing answer grounded in the corpus |
| `justification` | 1-2 sentences explaining the routing decision |
| `request_type` | `product_issue`, `feature_request`, `bug`, `invalid` |

---

## Notes

- The FAISS index is cached in `code/.cache/` after the first run (typically 30–60 s to build). Subsequent runs load from cache in seconds.
- The LLM logic seamlessly cascades in priority: Groq > OpenAI > Anthropic > Ollama depending on which environment variable is set.
