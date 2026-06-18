# Support Agent Scaffold

This directory contains a Python scaffold for the HackerRank Orchestrate support agent.

## Goals of this scaffold

- Preserve the required terminal entry point at `code/main.py`.
- Provide stable, testable plumbing for CSV I/O, corpus loading, and output validation.
- Isolate the still-missing ticket understanding logic behind explicit interfaces and `TODO` markers.

## Project layout

- `main.py`: required terminal entry point.
- `support_agent/cli.py`: command-line interface.
- `support_agent/agent.py`: orchestration layer for ticket processing.
- `support_agent/corpus.py`: local Markdown corpus discovery and loading.
- `support_agent/io.py`: CSV input/output helpers.
- `support_agent/validation.py`: schema and output validation.
- `support_agent/defaults.py`: placeholder components that still need implementation.

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

## Current state

The default agent wiring is intentionally incomplete. The following areas still need implementation:

1. Retrieval over the local corpus.
2. Request classification and escalation routing.
3. Product-area inference.
4. Grounded response and justification generation.

Those gaps are left as explicit `TODO` comments in `support_agent/defaults.py`.

## Assumptions

- Output remains the current eight-column CSV shape:
  `issue, subject, company, response, product_area, status, request_type, justification`.
- Input headers may arrive in mixed case and with spaces; the loader normalizes them.
- Only local files under `data/` are considered corpus sources.

## Limitations

- The scaffold does not yet produce final ticket predictions.
- The validator checks structure and allowed values, not semantic quality.
