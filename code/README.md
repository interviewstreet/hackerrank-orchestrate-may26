# HackerRank Orchestrate — Support Triage Agent

A multi-domain support triage agent that processes customer support tickets for HackerRank, Claude, and Visa. Answers are grounded exclusively in the provided corpus (`data/`). Zero hallucination by design.

## Directory Layout

```
repo-root/
├── data/               ← corpus (visa/, hackerrank/, claude/)  [auto-detected]
├── qdrant_db/          ← created automatically by build_index.py
├── support_tickets/    ← output.csv written here (if this directory exists)
│   └── support_tickets.csv
└── code/
    ├── agent.py
    ├── build_index.py
    ├── requirements.txt
    └── .env.example
```

> You must cd into the `code/` directory before running the agent.

## Quick Start

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
```

Keep the venv active for all subsequent steps. To deactivate later: `deactivate`.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

```bash
cp .env.example .env
# Edit .env and set OPENROUTER_API_KEY
```

### 4. Add the corpus and tickets

Place the `data/` directory (with `visa/`, `hackerrank/`, `claude/` sub-folders) at the **repo root** (sibling of `code/`). The agent auto-detects it there. If you need a custom location, set `DATA_PATH=/path/to/data` in `.env`.

The tickets CSV can live anywhere — pass it as a CLI argument, or place it at `support_tickets/support_tickets.csv` inside the repo root for the default path to resolve automatically.

### 5. Build the vector index

Run once before the first processing run. Safe to re-run on corpus changes.

```bash
python build_index.py
```

This chunks all documents under `data/`, generates embeddings with `all-MiniLM-L6-v2`, and stores them in Qdrant (local file-based, no server required).

### 6. Run the agent

The agent supports three modes: **bulk CSV**, **one-shot query**, and **interactive REPL**.

#### Bulk CSV mode (default)

Reads every ticket from a CSV file and writes `output.csv`.

```bash
# Default — tickets from support_tickets/support_tickets.csv (repo root)
python agent.py

# Explicit tickets file
python agent.py path/to/support_tickets.csv
```

**Output path resolution:**

1. If `support_tickets/` exists at the repo root → writes `support_tickets/output.csv` there.
2. Otherwise → creates `out/` in the current working directory and writes `out/output.csv`.

#### One-shot query mode

Pass a single query on the command line and get a formatted response immediately. No CSV needed.

```bash
python agent.py --query "I can't log in to my HackerRank account"

# With optional context flags
python agent.py \
  --query   "Why was my card charged twice?" \
  --company  Visa \
  --subject  "Duplicate charge on statement"
```

| Flag             | Short | Description                                                                 |
| ---------------- | ----- | --------------------------------------------------------------------------- |
| `--query TEXT`   | `-q`  | The support question or issue description                                   |
| `--subject TEXT` | `-s`  | Optional subject line (improves classification)                             |
| `--company NAME` | `-c`  | `HackerRank` / `Claude` / `Visa` / `None` (default: `None` — auto-detected) |

#### Interactive REPL mode

Start a prompt loop to ask multiple questions without restarting the process.

```bash
python agent.py --interactive
# short alias:
python agent.py -i
```

At each prompt enter your issue text; the agent then asks for an optional subject and company, runs the full pipeline, and prints a formatted result. Type `quit` or `exit` (or press Ctrl-C) to stop.

Exit code `0` on success; non-zero on configuration or I/O error.

---

## Architecture

```
support_tickets.csv
        │
        ▼
  [Gatekeeper]  ← deterministic validation, truncation, schema check
        │
        ▼
  [Scout]       ← google/gemini-2.5-flash-lite
                   classify request_type + product_area
                   extract sub-requests
                   infer company when None
        │
        ▼ (per sub-request)
  [Sentinel]    ← anthropic/claude-haiku-4-5
                   apply escalation rules
                   produce status + justification
        │
        ├── escalated ──────────────────────────────► "Escalate to a human"
        │
        │ replied
        ▼
  [Anchor]      ← google/gemini-2.5-flash
                   retrieve top-k corpus chunks (Qdrant, company pre-filter)
                   generate grounded response
                   grounded=false if top similarity < 0.65 → escalate
        │
        │ grounded=true
        ▼
  [Verifier]    ← google/gemini-2.5-flash-lite
                   does the response actually solve the issue?
                   confidence < 0.60 → escalate
        │
        │ verified=true
        ▼
  [Orchestrator] → output.csv
```

All LLM agents run through **OpenRouter** using a single API key. One billing balance, one SDK.

---

## Environment Variables

| Variable             | Required                     | Default                     | Description                                              |
| -------------------- | ---------------------------- | --------------------------- | -------------------------------------------------------- |
| `OPENROUTER_API_KEY` | Yes (for openrouter backend) | —                           | OpenRouter API key                                       |
| `MODEL_BACKEND`      | No                           | `openrouter`                | `openrouter` / `local_ollama` / `local_vllm`             |
| `OLLAMA_BASE_URL`    | No                           | `http://localhost:11434/v1` | Ollama endpoint                                          |
| `VLLM_BASE_URL`      | No                           | `http://localhost:8000/v1`  | vLLM endpoint                                            |
| `QDRANT_PATH`        | No                           | `<repo_root>/qdrant_db`     | Qdrant storage path; auto-placed beside `data/` if unset |
| `RETRIEVAL_TOP_K`    | No                           | `5`                         | Number of corpus chunks retrieved per query              |

---

## Output Format

`support_tickets/output.csv` (or `out/output.csv`) — columns in order:

| Column          | Values                                                  | Description                                     |
| --------------- | ------------------------------------------------------- | ----------------------------------------------- |
| `status`        | `replied` / `escalated`                                 | Triage decision                                 |
| `product_area`  | corpus section name                                     | Most specific support category                  |
| `response`      | text / `"Escalate to a human"`                          | User-facing reply                               |
| `justification` | text                                                    | Routing decision rationale with source citation |
| `request_type`  | `product_issue` / `feature_request` / `bug` / `invalid` | Ticket classification                           |

Multi-request tickets produce one row per sub-request (consecutive rows, input order preserved).

---

## Models Used

| Agent    | Model                          | Role                          |
| -------- | ------------------------------ | ----------------------------- |
| Scout    | `google/gemini-2.5-flash-lite` | Classification                |
| Sentinel | `anthropic/claude-haiku-4-5`   | Escalation judgment           |
| Anchor   | `google/gemini-2.5-flash`      | RAG + response generation     |
| Verifier | `google/gemini-2.5-flash-lite` | Post-generation quality check |

---

## Design Decisions

- **RAG over fine-tuning**: grounding is observable and auditable; corpus changes don't require retraining.
- **Qdrant over Chroma**: company pre-filter runs before similarity computation, preventing cross-domain contamination.
- **No agent framework**: four stages in a fixed sequence — no coordination problem. Plain Python gives full control over model selection and cost.
- **Sequential pipeline**: Sentinel needs Scout's `request_type` to apply escalation rules correctly.
- **Hardcoded escalation string**: `"Escalate to a human"` is never generated by an LLM — prevents manipulation via ticket content.
