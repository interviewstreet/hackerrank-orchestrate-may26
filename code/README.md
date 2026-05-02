# Support Triage Agent — HackerRank Orchestrate (May 2026)

Terminal-based RAG agent that triages support tickets across HackerRank, Claude, and Visa using only the local corpus in `../data/`.

## Architecture

```
ticket ──► pre-rules (regex)           ──► early return (escalate / out-of-scope)
       ──► company inference (None→best by retrieval)
       ──► language gate (non-English → escalate for None/Visa)
       ──► dense retrieval (MiniLM, single index, metadata filter)
       ──► coverage-floor check         ──► early escalate
       ──► LLM (Sonnet 4.6, tool-forced JSON)
       ──► verifier (sentence-level n-gram grounding)
       ──► post-rules (confidence/citation/area allow-list)
       ──► RowOutput
```

## Setup

```bash
cd code/
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # set ANTHROPIC_API_KEY
```

## Run

```bash
# Full pipeline against the real tickets:
python main.py

# Eval against the 10-row gold sample:
python eval.py

# Resume after partial run:
python main.py --resume

# No embeddings (TF-IDF fallback, fully offline):
python main.py --no-embeddings

# Dry run (skip LLM, only pre-rule decisions):
python main.py --dry-run --limit 5
```

Reads input from `../support_tickets/support_tickets.csv` and writes to
`../support_tickets/output.csv` with the exact 8-column header
`issue,subject,company,response,product_area,status,request_type,justification`.

## Design decisions

- **Single dense index, not BM25 + RRF.** Corpus is small (~3k chunks); MiniLM cosine is enough and avoids index-mismatch bugs under time pressure.
- **Rules before LLM, rules after LLM.** Pre-rules catch sensitive cases (fraud, legal, refund demands, score appeals, prompt injection, outage). Post-rules enforce confidence floor, mandatory citations, and product_area allow-list. The LLM is only trusted on grounded support questions.
- **Coverage floor check.** If retrieval similarity is below threshold we escalate before calling the LLM — this is the main hallucination defense.
- **Sentence-level verifier.** Every response sentence must share a 5-gram with a cited chunk; otherwise it's stripped or the row is escalated.
- **Determinism.** `temperature=0`, fixed `seed=42`, sorted tie-breaks, stable cosine sort, deterministic chunking.
- **Secrets.** Read only from env (`ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`).

## Files

| File | Purpose |
|---|---|
| `main.py` | CLI entry point |
| `agent.py` | Orchestrator |
| `retriever.py` | Dense retriever + TF-IDF fallback |
| `corpus.py` | Markdown loader + chunker |
| `escalation.py` | Pre/post rule tables |
| `verifier.py` | Citation grounding check |
| `prompts.py` | System prompt + few-shots |
| `llm_client.py` | Anthropic tool-call wrapper |
| `schemas.py` | Pydantic models |
| `io_csv.py` | CSV reader/writer with strict header |
| `eval.py` | Accuracy harness vs. gold sample |
| `config.py` | Constants |

## Known limits

- Gold sample is only 10 rows — accuracy numbers are noisy.
- Visa corpus is 14 docs; Visa tickets escalate often by design.
- We do not split multi-intent tickets; the LLM handles them in a single call.
