# HackerRank Orchestrate Support Ticket Triage Agent

A terminal-based agent that classifies and routes support tickets across three product ecosystems (HackerRank, Claude, Visa) using a local corpus of support documentation.

## Overview

This agent automatically triages incoming support tickets by:
1. **Inferring product domain** (HackerRank / Claude / Visa)
2. **Classifying request type** (product_issue / feature_request / bug / invalid)
3. **Retrieving relevant documentation** via semantic search
4. **Deciding response vs. escalation** based on escalation rules
5. **Generating grounded responses** directly from the corpus

### Output Schema

For each ticket, the agent produces:
| Column | Values | Description |
|--------|--------|-------------|
| `status` | `replied`, `escalated` | Whether response was provided or escalated |
| `product_area` | domain/category | e.g., `Claude/API`, `HackerRank/Assessments`, `Visa/Payment` |
| `response` | text | User-facing answer or empty if escalated |
| `justification` | text | Explanation of decision with corpus references |
| `request_type` | `product_issue`, `feature_request`, `bug`, `invalid` | Classification of request |

## Installation

### Requirements
- Python 3.9+

### Setup

```bash
# Navigate to code directory
cd code/

# Run setup script
python setup.py

# Or manually install
pip install -r requirements.txt
```

## Usage

### Quick Start

```bash
# Run agent
python main.py
```

### Testing with Sample Data

```bash
# The agent will process support_tickets.csv and write to output.csv
# To test first, copy sample file:
cp ../support_tickets/sample_support_tickets.csv test_tickets.csv
python -c "
from main import SupportTicketAgent
agent = SupportTicketAgent()
agent.process_csv('test_tickets.csv', 'test_output.csv')
"
```

## Architecture

### Components

1. **CorpusIndex** (`corpus_index.py`)
   - Loads 774+ markdown files from claude/, hackerrank/, visa/ directories
   - Uses optional embeddings if available
   - Falls back to keyword search if embeddings unavailable
   - Filters results by product domain

2. **SupportTicketAgent** (`main.py`)
   - Infers product from ticket content using keyword matching
   - Classifies request type using pattern matching
   - Retrieves top-5 relevant documentation chunks
   - Applies escalation rules for sensitive/out-of-scope cases
   - Generates deterministic extractive responses from retrieved context

### Escalation Rules

Tickets are escalated (not replied) when:
- **Content violation**: Hateful, racist, explicit, or invalid requests
- **Sensitive/Permissions**: Account access, billing, fraud, passwords, PII
- **Not found**: No relevant documentation in corpus
- **Multi-topic**: Multiple unrelated questions
- **Unresolvable**: Feature request or bug without documented workaround

### Retrieval Strategy

**Hybrid approach:**
1. **Semantic search** (optional) - Embeds corpus using `all-MiniLM-L6-v2`, searches via FAISS
2. **Keyword search** (fallback) - Term overlap matching if embeddings unavailable
3. **Product filtering** - Constrains results to inferred product domain when possible

Chunks are 500 characters with 100-char overlap for better context coverage.

## Environment Variables

```bash
ANTHROPIC_API_KEY     # Required. Anthropic API key for Claude model access
```

## Logging

All AI tool interactions are logged to:
```
$HOME/hackerrank_orchestrate/log.txt
```

Log includes:
- Corpus loading status
- API calls and responses
- Retrieved documents
- Classification decisions
- Escalation reasons

## Input Format

**support_tickets.csv** columns:
- `Issue` (string) - Main question/problem description
- `Subject` (string, optional) - Brief ticket subject line
- `Company` (string, optional) - One of "HackerRank", "Claude", "Visa", or blank

## Output Format

**output.csv** columns:
- `Status` - `replied` or `escalated`
- `Product Area` - Inferred domain and category
- `Response` - Answer text (empty if escalated)
- `Justification` - Decision explanation
- `Request Type` - Classification: `product_issue`, `feature_request`, `bug`, or `invalid`

## Performance Notes

- First run builds and caches FAISS index (~30 seconds for 774 documents)
- Each ticket requires 1 API call to Claude (generates response) or 0 calls (escalated)
- Keyword search fallback available if sentence-transformers fails to load
- All corpus data is local; no network calls except to Anthropic API

## Troubleshooting

### Import errors after `pip install`?
```bash
# Reinstall sentence-transformers (common issue)
pip install --force-reinstall sentence-transformers
```

### Slow first run?
```bash
# FAISS index building takes time. Subsequent runs use cached index.
# To rebuild: rm embeddings/ (if persisted)
```

### Escalating too many tickets?
```bash
# Adjust escalation thresholds in SupportTicketAgent.should_escalate()
# Lower the score threshold for "high relevance" (currently 0.6)
```

### API errors?
The agent is fully offline and does not require an API key.

## Development

### File Structure
```
code/
  main.py              # Main agent logic
  corpus_index.py      # Corpus loading and retrieval
  requirements.txt     # Python dependencies
  setup.py             # Setup script
  README.md            # This file
```

### Testing

```bash
# Run on sample data first
python -c "
from main import SupportTicketAgent
agent = SupportTicketAgent('../data')
pred = agent.process_ticket('I lost access to my account', company='Claude')
print(pred)
"
```

### Extending

To add new product domains:
1. Add markdown files to `data/{product_name}/`
2. Update `SupportTicketAgent.infer_company()` keywords
3. Update corpus_index category_keywords mapping
4. Rerun to rebuild index

## Notes

- Agent prioritizes **accuracy over coverage** — escalates when uncertain
- All responses are **grounded in corpus** — no hallucinations or external knowledge
- Supports **deterministic behavior** via seed-fixed keyword matching
- Designed for **24-hour implementation** with pragmatic trade-offs

## License

HackerRank Orchestrate Challenge 2026
