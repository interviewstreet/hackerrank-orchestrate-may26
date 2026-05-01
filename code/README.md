# Support Triage Agent

A production-grade multi-domain support triage agent built with the [Parlant SDK](https://parlant.io) and ChromaDB RAG. It processes support tickets for HackerRank, Claude, and Visa, producing a structured 5-field CSV output grounded in the provided support corpus.

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- An [OpenRouter](https://openrouter.ai) API key (used to route to Claude models)

## Setup

**1. Install dependencies**

```bash
uv sync
```

This creates a `.venv` and installs all pinned dependencies from `pyproject.toml`.

**2. Configure environment**

```bash
cp .env.example .env
# Edit .env and set OPENROUTER_API_KEY
```

**3. Run**

```bash
uv run python code/main.py
```

Output is written to `support_tickets/output.csv`.

> **First run:** ChromaDB will index all 774 support corpus files (~2 minutes). Subsequent runs skip this step automatically.

## Architecture

```
main.py
  ├── build_index()          retriever.py   → ChromaDB (code/chroma_db/)
  ├── start_server()         agent.py       → Parlant server (background thread)
  │     └── configure_agent()
  │           ├── _add_glossary()
  │           ├── create_triage_journey()   → rag_lookup tool (retriever.py)
  │           └── add_guidelines()
  └── process_ticket() loop
        ├── ParlantClient.sessions.create()
        ├── sessions.create_event()        → sends ticket as customer message
        ├── sessions.list_events()         → long-polls for agent response
        └── parse_agent_output()           classifier.py → TriageResult
```

### Module responsibilities

| File | Role |
|---|---|
| `retriever.py` | Builds and queries ChromaDB. Exposes `@p.tool rag_lookup`. |
| `agent.py` | Defines the Parlant journey (state machine), guidelines, and glossary. |
| `classifier.py` | Regex parser that extracts the 5 structured fields from the agent's response. |
| `main.py` | Entry point: starts the Parlant server in a background thread, iterates the CSV, writes output. |

## Design Decisions

**Why Parlant?** Parlant's journey + guideline model provides explicit, inspectable behavioral contracts rather than a single monolithic prompt. Each escalation rule is a named guideline that can be audited, adjusted, and explained independently.

**Why ChromaDB + sentence-transformers?** Local embeddings (`all-MiniLM-L6-v2`) require no extra API key, run offline, and are fast enough for 774 documents. The persistent collection means index build cost is paid once.

**Why one session per ticket?** Each support ticket is a self-contained interaction. Fresh sessions prevent context bleed between tickets and keep the agent's reasoning grounded on exactly the retrieved chunks for that ticket.

**Escalation logic:** Only systemic, platform-wide outages and confirmed account security breaches are escalated. Individual user issues (stolen card, locked account, billing) are answered from the corpus — this matches the sample data pattern.

## Output Format

Each row in `output.csv` contains:

| Column | Values |
|---|---|
| `status` | `replied` or `escalated` |
| `product_area` | Lowercase category derived from corpus path (e.g. `screen`, `privacy`, `travel_support`) |
| `response` | User-facing answer grounded in the support corpus |
| `justification` | One-sentence explanation of the triage decision |
| `request_type` | `product_issue`, `feature_request`, `bug`, or `invalid` |

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `OPENROUTER_API_KEY` | Yes | OpenRouter API key |
| `OPENROUTER_MODEL` | No | Model name (default: `anthropic/claude-3.5-sonnet`) |
| `PARLANT_SERVER_URL` | No | Parlant server URL (default: `http://localhost:8800`) |
| `PARLANT_HOME` | No | Directory for Parlant session state (default: `./parlant_data`) |
