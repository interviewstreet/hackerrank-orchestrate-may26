# Support Triage Agent — Code README

A terminal-based, multi-domain support triage agent for HackerRank Orchestrate (May 2026).

---

## Architecture Overview

```
                   Ticket Input
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│                   main.py                       │
│         CLI entry point & batch runner          │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│                   agent.py                      │
│              Orchestration layer                │
│                                                 │
│  ┌──────────┐  ┌────────────┐  ┌─────────────┐  │
│  │classifier│  │ escalation │  │    llm.py   │  │
│  │   .py    │  │    .py     │  │  (Claude AI)│  │
│  └──────────┘  └────────────┘  └─────────────┘  │
│                                                 │
│  ┌──────────────────────────────────────────┐   │
│  │              retriever.py                │   │
│  │   TF-IDF corpus index (data/ directory)  │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
                       │
                       ▼
              output.csv (5 columns)
```

### Module responsibilities

| Module | Role |
|---|---|
| `main.py` | CLI, argument parsing, CSV I/O, progress display |
| `agent.py` | Pipeline orchestration: retrieval → classify → escalate → respond |
| `retriever.py` | TF-IDF corpus index, multi-query retrieval, context formatting |
| `classifier.py` | Rule-based domain/request-type/product-area/escalation signal detection |
| `escalation.py` | Escalation decision engine (rule-based, risk-level scoring) |
| `llm.py` | Anthropic Claude API wrapper (classify + generate + justify) |
| `scraper.py` | Corpus health checks and optional enrichment utility |

### Processing pipeline (per ticket)

1. **Sanitize** — normalize whitespace, check for injection attempts
2. **Domain detection** — rule-based pattern matching on issue text + company field
3. **Corpus retrieval** — multi-query TF-IDF search over the `data/` corpus
4. **Rule-based classification** — request type, product area, escalation signals
5. **Escalation decision** — hard rules (fraud, account security) + corpus coverage check
6. **LLM refinement** — Claude API for classification refinement and response generation
7. **Output** — structured dict → CSV row

---

## Setup

### 1. Prerequisites

- Python 3.10+
- An Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com))
- The repo cloned with `data/` populated (hackerrank, claude, visa corpus)

### 2. Install dependencies

```bash
cd code/
pip install -r requirements.txt
```

### 3. Set your API key

```bash
cp ../.env.example ../.env
# Edit .env and set ANTHROPIC_API_KEY=sk-ant-...
```

Or export directly:

```bash
export ANTHROPIC_API_KEY=sk-ant-your_key_here
```

### 4. Verify corpus

```bash
python scraper.py --verify
python scraper.py --stats
```

Expected output:
```
✅ hackerrank: 45 files, ~2.1MB
✅ claude: 38 files, ~1.8MB
✅ visa: 22 files, ~0.9MB
```

If corpus is missing/sparse, optionally enrich:

```bash
python scraper.py --enrich  # fetches from official support URLs only
```

---

## Running the Agent

### Process all support tickets (main task)

```bash
cd code/
python main.py
```

Reads from `../support_tickets/support_tickets.csv`  
Writes to `../support_tickets/output.csv`

### Run on sample tickets (for validation)

```bash
python main.py --sample
```

Reads from `../support_tickets/sample_support_tickets.csv`  
Writes to `../support_tickets/sample_output.csv`

### Verbose mode (show per-ticket details)

```bash
python main.py --verbose
```

### Process a single ticket interactively

```bash
python main.py --ticket "I can't log in to my HackerRank account. I reset my password but it's still not working."
```

With optional subject and company:

```bash
python main.py \
  --ticket "My Visa card was charged twice for the same transaction" \
  --subject "Duplicate charge" \
  --company "Visa"
```

### Custom input/output paths

```bash
python main.py --input /path/to/tickets.csv --output /path/to/results.csv
```

---

## Design decisions & trade-offs

### Why TF-IDF instead of embedding-based RAG?

- **No external vector DB needed** — works offline with the local corpus
- **Deterministic** — same query always returns same results
- **Fast** — index builds in seconds, queries in milliseconds
- **Interpretable** — scores are human-readable

Trade-off: TF-IDF is weaker at semantic similarity. Mitigated by:
- Multi-query retrieval (full query + extracted sub-phrases)
- Bi-gram support (`ngram_range=(1, 2)`)

To upgrade to embeddings: swap `retriever.py` for a ChromaDB/FAISS-based index using `sentence-transformers`. The interface is identical.

### Why separate rule-based + LLM classification?

- **Determinism**: Rule-based runs first and makes hard escalation decisions (fraud, injection) that are not LLM-delegated.
- **Robustness**: If the API is down, the agent still works (degrades gracefully).
- **Cost**: Fewer LLM calls by pre-filtering with rules.

### Why escalate aggressively?

The problem statement explicitly says: *"escalate high-risk, sensitive, or unsupported cases."* A false negative (answering a sensitive billing/fraud issue incorrectly) is far worse than a false positive (escalating something the agent could have handled).

Hard escalation triggers:
- Fraud signals
- Account security (locked out, hacked)
- Legal/compliance
- Harm threats
- Domain-specific billing/card areas (Visa, Claude billing, HackerRank billing)

### Corpus grounding

The agent is instructed (via system prompt) to NEVER use parametric knowledge for policies or procedures. All responses cite only information present in the retrieved chunks.

---

## Output schema

| Column | Values |
|---|---|
| `status` | `replied` or `escalated` |
| `product_area` | e.g., `claude/billing_plans`, `hackerrank/assessment`, `visa/fraud_disputes` |
| `response` | User-facing text grounded in corpus |
| `justification` | One-sentence explanation of the routing decision |
| `request_type` | `product_issue`, `feature_request`, `bug`, or `invalid` |

---

## Environment variables

| Variable | Required | Description |
|---|---|---|
| `ANTHROPIC_API_KEY` | Recommended | Enables LLM-powered responses and classification |
| `DATA_DIR` | Optional | Override path to corpus data directory |

---

## Determinism

- LLM calls use `temperature=0`
- TF-IDF vectorizer is seeded via consistent vocabulary ordering
- CSV rows are processed in order with no parallelism

---

## Extending the agent

- **Swap retriever**: Replace TF-IDF with ChromaDB + sentence-transformers for better semantic search
- **Add domains**: Add patterns to `classifier.py` and corpus files to `data/new_domain/`
- **Tune escalation**: Adjust `CORPUS_COVERAGE_THRESHOLD` in `escalation.py`
- **Add tools**: Use Claude's tool-use API for structured multi-step classification
