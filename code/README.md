# Support Agent

This directory contains a deterministic Python support triage agent for the HackerRank Orchestrate challenge.

## Design goals

- Preserve the required terminal entry point at `code/main.py`.
- Use only the local Markdown corpus under `data/`.
- Keep routing deterministic and explainable.
- Write only the five required output columns:
  `status,product_area,response,justification,request_type`.

## Project layout

- `main.py`: required terminal entry point.
- `support_agent/cli.py`: command-line interface.
- `support_agent/agent.py`: orchestration layer for ticket processing.
- `support_agent/corpus.py`: local Markdown corpus discovery and loading.
- `support_agent/defaults.py`: deterministic retrieval, routing, product-area inference, and response generation.
- `support_agent/io.py`: CSV input/output helpers.
- `support_agent/validation.py`: schema and output validation.

## Run

From the repo root:

```bash
uv run python code/main.py --help
```

Validate an existing output file:

```bash
uv run python code/main.py --validate-output \
  --input support_tickets/support_tickets.csv \
  --output support_tickets/output.csv
```

Run the unit tests:

```bash
uv run python -m unittest discover -s tests -v
```

## Assumptions

- Final output should follow the five generated columns from `problem_statement.md`.
- Input headers may arrive in mixed case and with spaces; the loader normalizes them.
- Only local files under `data/` are considered corpus sources.

## Limitations

- Retrieval is lexical and deterministic; it will miss some paraphrases.
- Response generation uses extracted corpus sentences and conservative escalation templates instead of an LLM.
