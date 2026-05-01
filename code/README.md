# Support Triage Agent

**HackerRank Orchestrate 2026** — A production-grade, multi-domain AI support triage agent.

Classifies, retrieves, safety-gates, and responds to support tickets across HackerRank, Claude AI, and Visa — grounded entirely in the 770-document local corpus. Powered by **Google Gemini 2.5 Flash**.

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Pipeline Flow](#pipeline-flow)
3. [Module Breakdown](#module-breakdown)
4. [High-Availability: API Key Rotation](#high-availability-api-key-rotation)
5. [Security Design](#security-design)
6. [Setup and Installation](#setup-and-installation)
7. [Running the Agent](#running-the-agent)
8. [Output Schema](#output-schema)
9. [Design Decisions and Trade-offs](#design-decisions-and-trade-offs)
10. [Failure Modes and Mitigations](#failure-modes-and-mitigations)

---

## Results and Performance

The agent achieved the following metrics on the full evaluation set (29 tickets) using the Gemini 2.5 Flash parallel pipeline.

| Metric | Achievement |
|:--- |:--- |
| **Total Tickets** | 29 |
| **Automation Rate** | 79.3% (Replied) |
| **Escalation Rate** | 20.7% (Safe Escalation) |
| **Throughput** | ~14.5 tickets/minute |
| **Success Rate** | 100% (Zero unhandled exceptions) |

<p align="center">
  <img src="results/status_distribution.png" width="400" />
  <img src="results/domain_breakdown.png" width="400" />
</p>
<p align="center">
  <img src="results/request_type_breakdown.png" width="400" />
  <img src="results/escalation_by_domain.png" width="400" />
</p>

---

## Architecture Overview

```
+------------------------------------------------------------------+
|                    SUPPORT TRIAGE AGENT v1.0                     |
|              Google Gemini 2.5 Flash (Parallel)                  |
+------------------------------------------------------------------+

Corpus: 770 scraped support articles (HackerRank, Claude AI, Visa)
        Indexed in RAM via BM25. No external lookups at inference time.

                    support_tickets.csv
                           |
                           v
               +-----------+-----------+
               |   1. PARALLEL EXECUTOR|   < ThreadPoolExecutor (max_workers=7)
               |   Concurrent tickets  |     Scales throughput by 2.5x
               |   (7 rotating keys)   |     Thread-safe workload distribution
               +-----------+-----------+
                           |
                    ticket_batch
                           |
                           v
               +-----------+-----------+
               |   2. CLASSIFIER       |   < Google Gemini 2.5 Flash
               |   JSON-mode output    |     Guaranteed machine-parseable JSON
               |   domain / type /     |     Returns:
               |   product_area /      |       domain, request_type,
               |   confidence          |       product_area, confidence
               +-----------+-----------+
                           |
                  Classification dataclass
                           |
                           v
               +-----------+-----------+
               |   3. DIR-ROUTED RAG   |   < Local RAM, sub-5ms per query
               |   Targeted BM25 Search|     Isolates product directories first
               |   Offline, no cost    |     Global fallback if targeted search < 10.0
               +-----------+-----------+
                           |
                    List[Document] (top-7)
                           |
                           v
               +-----------+-----------+
               |   4. SAFETY GATE      |   < Deterministic rules, zero LLM cost
               |   7 escalation rules  |     Evaluated in strict priority order:
               |   Rule engine         |
               |                       |   RULE 1: Visa fraud     -> escalate
               |                       |   RULE 2: Billing dispute -> escalate
               |                       |   RULE 3: Hacked account  -> escalate
               |                       |   RULE 4: Legal language  -> escalate
               |                       |   RULE 5: Confidence<0.4  -> escalate
               |                       |   RULE 6: No docs found   -> escalate
               |                       |   RULE 7: Injection detection -> escalate
               +-----------+-----------+
                           |
               SafetyDecision(should_escalate, reason)
                           |
               +-----------+-----------+
               |         BRANCH        |
               +-----+-------------+--+
                     |             |
                   REPLY        ESCALATE
                     |             |
                     v             v
           +----------+    +------------------+
           | 5a.      |    | 5b. ESCALATION   |   Zero API calls
           | RESPONDER|    | NOTICE BUILDER   |   Template message
           | Gemini LLM|    |                  |   Embeds exact rule
           | Grounded |    |                  |   reason for audit
           | in corpus|    +------------------+
           +----------+
                |
      Post-generation PII/Hallucination check
      (lexical overlap >= 3 words with corpus)
                |
                v
               +-----------+-----------+
               |   6. CSV WRITER       |   Enforces output schema:
               |   output.csv          |   ticket_id, status,
               |                       |   product_area, response,
               |                       |   justification, request_type
               +-----------+-----------+
                           |
                    support_tickets/output.csv
```

---

## High-Availability: API Key Rotation

To bypass the free-tier rate limits (RPM/TPD) of the Gemini API, the system implements a **Thread-Safe Round-Robin Rotator**.

### Implementation Details:
*   **Rotator Singleton**: The `GeminiRotator` class manages a cycle of 7 different API keys.
*   **Atomic Access**: Uses a `threading.Lock` to ensure that even during parallel execution, keys are handed out in a strict sequence without race conditions.
*   **Automatic Retries**: Integrated with `tenacity`, the system automatically rotates to the *next* key in the sequence if it encounters a `429 RESOURCE_EXHAUSTED` or `503 SERVICE_UNAVAILABLE` error.

---

## Security Design

### 1. No Secrets in Code
All credentials are read exclusively from environment variables. The `.env` file is git-ignored, and a template is provided in `.env.example`.

### 2. Hallucination and PII Guard
The system performs a regex-based post-generation scan for PII (emails, phone numbers) and a lexical overlap check to ensure grounding. If a leak or hallucination is detected, the response is blocked and the ticket is safely escalated.

### 3. Deterministic Safety Gate
High-risk scenarios (Fraud, Legal, Account Compromise) are handled by pure Python rules rather than an LLM. This ensures 100% reliability and zero probabilistic variance for sensitive cases.

---

## Setup and Installation

### Prerequisites
- Python 3.10+
- Multiple Gemini API keys (recommended for parallel performance)

### Step 1 — Setup Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r code/requirements.txt
```

### Step 2 — Configuration
```bash
cp .env.example .env
# Open .env and add your Gemini API keys
```

---

## Running the Agent

### Parallel Triage Pipeline
To process the input tickets with 7 parallel workers:
```bash
python code/main.py --input support_tickets/support_tickets.csv --output support_tickets/output.csv
```

### Generate Performance Analytics
To generate the distribution charts and statistics:
```bash
python code/utils/analyze_results.py --input support_tickets/output.csv --charts-dir code/results/
```

---

## Design Decisions and Trade-offs

### Gemini 2.5 Flash over Llama-3 (Groq)
While Llama-3 is fast, the Groq free tier Tokens Per Day (TPD) limit was too restrictive for a 29-ticket RAG pipeline. **Gemini 2.5 Flash** provides superior reasoning, more stable JSON-mode output, and a more generous rate-limit profile when combined with our rotation logic.

### BM25 over Vector DB
For the 770-document corpus, BM25 provides **sub-5ms latency** with zero infrastructure overhead. Vector databases (Pinecone/Weaviate) would introduce unnecessary network latency and embedding costs without a measurable gain in retrieval quality at this scale.

---

## Failure Modes and Mitigations

| Failure Scenario | Mitigation Strategy |
|:--- |:--- |
| **API Rate Limit (429)** | Round-robin rotation to the next key + Exponential backoff |
| **Malformed Input CSV** | Graceful per-ticket exception handling; pipeline continues |
| **Prompt Injection** | Deterministic Safety Rule 0 (Blocking injections) |
| **PII Leak Detected** | Automatic blocking of reply; fallback to safe escalation |
