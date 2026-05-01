# HackerRank Support Triage Agent
### HackerRank Orchestrate — May 2026 Hackathon

A **production-grade, terminal-based AI support triage agent** that reads support tickets from a CSV, processes each ticket through a modular RAG-powered pipeline, and outputs structured triage results — all using only a **local support corpus** with **zero external API calls**.

---

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the agent
python main.py
```

Output is written to `output.csv`.

---

## Project Structure

```
code/
├── main.py           # Entry point — orchestrates the full run
├── agent.py          # SupportTriageAgent — pipeline orchestrator
├── classifier.py     # Request-type & product-area classifiers + risk detection
├── retriever.py      # RAG engine (sentence-transformers + cosine search)
├── decision.py       # Rule-based decision engine (reply vs escalate)
├── generator.py      # Response generator (corpus-grounded, no hallucination)
├── utils.py          # Text cleaning, CSV I/O, structured logger
├── config.py         # All constants, thresholds, and keyword maps
├── requirements.txt  # Python dependencies
├── README.md         # This file
│
├── data/             # Local support corpus (RAG source)
│   ├── account_management.txt
│   ├── assessments.txt
│   ├── billing.txt
│   ├── security_privacy.txt
│   ├── technical_issues.txt
│   └── general_faq.txt
│
└── support_tickets/
    └── support_tickets.csv   # Input tickets
```

---

## Architecture

```
Ticket (issue + subject + company)
        │
        ▼
┌─────────────────────────────┐
│   Preprocessing (utils.py)  │  clean, combine, normalise
└────────────┬────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│   Risk Detector  (classifier.py)          │  keyword scan for
│   ─────────────────────────────────────  │  fraud / security /
│   fraud_security │ payment_dispute       │  manipulation etc.
│   score_manipulation │ data_privacy …    │
└────────────┬─────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│   Request-Type Classifier (classifier.py) │  keyword voting
│   bug │ feature_request │ invalid │       │  (deterministic)
│   product_issue                           │
└────────────┬─────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│   Product-Area Classifier (classifier.py) │  keyword voting
│   assessments │ account_management │      │  + semantic tie-break
│   billing │ privacy │ security │          │  (sentence-transformers)
│   technical_issues │ general              │
└────────────┬─────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│   Multi-Intent Detection (classifier.py) │  flags tickets that
│                                          │  span multiple areas
└────────────┬─────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│   RAG Retriever  (retriever.py)          │  all-MiniLM-L6-v2
│   ─────────────────────────────────────  │  cosine similarity
│   load corpus → chunk → encode → search  │  top-3 chunks
└────────────┬─────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│   Decision Engine (decision.py)          │  priority-ordered rules
│   ─────────────────────────────────────  │  1. high-risk → escalate
│   replied | escalated                    │  2. invalid   → escalate
│                                          │  3. low score → escalate
│                                          │  4. multi-intent → escalate
│                                          │  5. else      → reply
└────────────┬─────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│   Response Generator (generator.py)      │  corpus-grounded reply
│   ─────────────────────────────────────  │  OR safe escalation
│   No hallucination — only corpus text    │  template
└────────────┬─────────────────────────────┘
             │
             ▼
     output.csv  (status, product_area, response, justification, request_type)
```

---

## Input Format

`support_tickets/support_tickets.csv` — three columns:

| Column  | Description                    |
|---------|-------------------------------|
| issue   | Free-form ticket description  |
| subject | Ticket subject line           |
| company | Customer company name         |

---

## Output Format

`output.csv` — original columns plus:

| Column        | Values / Description                                          |
|---------------|--------------------------------------------------------------|
| status        | `replied` or `escalated`                                    |
| product_area  | `assessments`, `account_management`, `billing`, `privacy`, `security`, `technical_issues`, `general` |
| response      | Customer-facing response text                                |
| justification | Internal explanation of the triage decision                  |
| request_type  | `bug`, `feature_request`, `invalid`, `product_issue`         |

---

## Design Decisions

### 1. RAG with Local Corpus
All answers are grounded exclusively in the `data/` folder. No external APIs or LLMs are called during triage. This ensures:
- **No hallucination** — responses can only contain what the corpus says.
- **Offline operation** — works without internet access.
- **Auditability** — every response cites its source document.

### 2. Sentence-Transformers (all-MiniLM-L6-v2)
Chosen for:
- Small footprint (~80 MB), runs on CPU.
- Strong semantic similarity for English support text.
- Produces L2-normalised embeddings so cosine similarity = dot product (fast).

### 3. Hybrid Classification (Keyword + Semantic)
- **Keyword voting** is fast and fully explainable.
- **Semantic fallback** handles edge cases where no keyword fires or there's a tie.
- Both stages are deterministic (seeds fixed).

### 4. Escalation-First Policy
The decision engine follows the principle: *"when in doubt, escalate."*
Concretely:
- Any risk keyword match → immediate escalation, skipping retrieval.
- Any retrieval score below the threshold (`0.30`) → escalation.
- Three or more distinct product areas detected → escalation (complexity).

### 5. Overlapping Chunk Retrieval
Documents are split into 300-word chunks with a 50-word overlap. This prevents useful context from being cut mid-sentence at chunk boundaries.

### 6. Confidence Threshold
Set to `0.30` cosine similarity. Below this, retrieved documents are not sufficiently related to justify a response. This is conservative by design — false escalations are cheaper than incorrect answers.

### 7. Determinism
`PYTHONHASHSEED`, `numpy`, `random`, and `torch` seeds are all pinned to `42` at startup, ensuring identical outputs across runs for the same input.

---

## Escalation Categories

| Risk Category      | Escalated To                     |
|--------------------|----------------------------------|
| fraud_security     | Security and Trust team          |
| payment_dispute    | Finance and Billing team         |
| score_manipulation | Policy and Compliance team       |
| account_permission | Account Management team          |
| vulnerability      | Security Engineering team        |
| data_privacy       | Privacy and Compliance team      |

---

## Extending the Corpus

Add new `.txt` files to the `data/` folder — they are automatically picked up on the next run. No code changes required. The retriever re-indexes on every startup.

---

## Requirements

- Python 3.10+
- `sentence-transformers==3.0.1`
- `numpy>=1.24.0`

---

## Hackathon — HackerRank Orchestrate May 2026

Built for the **Orchestrate May 2026** hackathon. The agent demonstrates:
- Modular, production-grade Python architecture.
- Local RAG without any external API dependency.
- Explainable, rule-based decisions with semantic augmentation.
- Zero hallucination by design.
