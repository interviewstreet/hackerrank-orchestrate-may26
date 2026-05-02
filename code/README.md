# HackerRank Orchestrate Triage Agent

Terminal-based, corpus-grounded support triage agent. Reads
`support_tickets/support_tickets.csv`, classifies each ticket, retrieves
relevant snippets from `data/{hackerrank,claude,visa}/`, generates a
grounded response (or escalates), and writes `support_tickets/output.csv`.

## Install

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r code/requirements.txt
cp .env.example .env
# Edit .env: set ANTHROPIC_API_KEY=sk-ant-...
```

## Build the corpus index (one-time, ~5 min)

```bash
python code/indexer.py --rebuild
```

Index artifacts land under `code/index/` and are gitignored.

## Run the agent

```bash
python code/main.py --input support_tickets/support_tickets.csv \
                    --output support_tickets/output.csv
```

Optional flags:

- `--limit 5`         process the first 5 rows only (dev iteration)
- `--rebuild-index`   force corpus reindex
- `--trace-dir DIR`   per-run JSONL trace location (default `code/runs/`)
- `--config PATH`     alternate config.yaml path

## Run tests

```bash
pytest code/tests/
```

## Environment variables

See `.env.example`. `ANTHROPIC_API_KEY` is required; everything else has
defaults in `code/config.yaml`.
