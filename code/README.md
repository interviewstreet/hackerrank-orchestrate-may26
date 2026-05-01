# Support triage agent

Terminal workflow:

1. Index all markdown under `../data/{hackerrank,claude,visa}` into BM25-retrievable chunks (YAML frontmatter titles + breadcrumbs included in the lexical field).
2. For each ticket row, retrieve top‑K excerpts scoped by `Company` when set (otherwise search all corpora).
3. Call **OpenAI** (`OPENAI_API_KEY`) or **Anthropic** (`ANTHROPIC_API_KEY`) with temperature `0` and JSON output, instructing the model to ground answers only in those excerpts and to escalate when excerpts are insufficient or risk is high.
4. Apply conservative regex overrides for prompt injection, broad outages, score disputes, billing identifiers, merchant‑dispute demands, and non‑admin workspace access restoration — forcing `escalated` with an appended justification reason.

## Setup

```bash
cd code
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
Create `../.env` or export API keys in your shell.
```

Set one of:

- `OPENAI_API_KEY` (optional `OPENAI_MODEL`, default `gpt-4o-mini`)
- `ANTHROPIC_API_KEY` (optional `ANTHROPIC_MODEL`, default `claude-3-5-haiku-latest`)

Optional: `RETRIEVAL_TOP_K` (default `8`).

## Run

From repo root (paths default to `support_tickets/support_tickets.csv` → `support_tickets/output.csv`):

```bash
cd code
source .venv/bin/activate
python main.py
```

Flags:

```bash
python main.py --input ../support_tickets/support_tickets.csv --output ../support_tickets/output.csv --limit 5
```

No live HTTP calls are made for answers; only local files under `data/` feed retrieval.
