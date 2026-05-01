# HackerRank Orchestrate - Support Ticket Triage Agent

A deterministic, strictly grounded RAG-based support ticket triage system with zero hallucination.

## Quick Start

```bash
cd code
source venv/bin/activate
python main.py
```

## Output

Results are written to `../support_tickets/output.csv`

## Architecture

- `pipeline.py` - Decision engine with strict grounding enforcement
- `agents/` - Pre-safety, post-safety, grounding, LLM agent, product area, justification
- `utils/` - Loader, retriever, logger
- `config.py` - Configuration and constants

## Strict Evaluation Compliance

1. **Hard Grounding** - If retrieval_score < threshold, escalate
2. **Forbidden Patterns** - Blocks responses with "try", "ensure", etc.
3. **Context-Only Generation** - LLM must use only retrieved context
4. **Post-Generation Guardrails** - Grounding, length, forbidden patterns, vague response checks
5. **Response Templates** - Exact strings for escalation/refusal
6. **Status Alignment** - If response is escalation message, status must be "escalated"

## Run Options

```bash
# Run on support_tickets.csv
python main.py

# Run on sample
python main.py --sample

# Run custom file
python main.py --file path/to/tickets.csv
```

## Requirements

- Python 3.10+
- OpenAI API key (set in `.env`)
- Dependencies in `requirements.txt`