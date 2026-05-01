# Support Ticket Triage Agent — HackerRank Orchestrate

A production-grade support ticket triage system that intelligently routes and responds to support requests across three major product ecosystems: **HackerRank**, **Claude**, and **Visa**. Built with safety, transparency, and accuracy as core principles.

**Challenge:** [HackerRank Orchestrate Hackathon (May 1–2, 2026)](https://www.hackerrank.com/contests/hackerrank-orchestrate-may26/)

---

## Table of Contents

1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Technical Architecture](#technical-architecture)
4. [Quick Start](#quick-start)
5. [Installation & Setup](#installation--setup)
6. [Usage](#usage)
7. [Design & Evaluation Alignment](#design--evaluation-alignment)
8. [Project Structure](#project-structure)
9. [Detailed Implementation](#detailed-implementation)
10. [Links & Resources](#links--resources)

---

## Overview

This support triage agent processes customer support tickets and makes intelligent routing decisions based on a grounded, local-only corpus of support documentation. For each ticket, the agent:

1. **Classifies** the request type (product issue, bug, feature request, or invalid)
2. **Retrieves** the most relevant support documentation from the corpus
3. **Evaluates risk** and escalation signals (permissions, security, confidence thresholds)
4. **Routes** the ticket (reply with grounded information or escalate to human support)
5. **Generates** user-facing responses with full justification and traceability

### Core Principles

- **Corpus-grounded:** All responses are extracted from the provided support corpus; no hallucinations or external API calls
- **Safety-first:** High-risk, sensitive, and low-confidence requests are escalated to human specialists
- **Deterministic:** No randomness; identical inputs always produce identical outputs
- **Transparent:** Every decision includes a justification explaining why the ticket was routed as it was
- **Simple & maintainable:** Clean code with clear separation of concerns; production-ready

---

## Key Features

### 1. Multi-Product Support Coverage
- **HackerRank:** Assessments, interviews, hiring platform
- **Claude:** AI assistant, API, account management
- **Visa:** Fraud protection, disputes, account services

### 2. Intelligent Retrieval Engine
- **TF-IDF ranking:** Fast, semantic-aware document retrieval without heavyweight models
- **Company filtering:** Routes to the correct product knowledge base
- **Confidence scoring:** Automatically escalates low-confidence matches

### 3. Smart Escalation Logic
- Detects high-risk patterns: permission requests, security vulnerabilities, account access issues
- Low-confidence escalation: when retrieval confidence falls below threshold
- Invalid/out-of-scope handling: graceful rejection of unsupported queries

### 4. Dual Interface
- **Terminal/CLI:** Batch processing for automated ticket triage
- **Web UI (Streamlit):** Interactive single-ticket triage and batch CSV upload/download

### 5. Production Output
- CSV format with all required fields: `issue`, `subject`, `company`, `response`, `product_area`, `status`, `request_type`, `justification`
- Ready for immediate evaluation and human review

---

## Technical Architecture

### Data Flow

```
Input (CSV) → Parse Ticket → Retrieve Docs → Classify → Evaluate Risk → Route Decision → Generate Response → Output (CSV)
```

### Module Breakdown

| Module | Responsibility |
|--------|---|
| `main.py` | CLI entry point; orchestrates batch processing |
| `triage_agent.py` | Backward-compatible wrapper |
| `web_app.py` | Streamlit UI for single and batch triage |
| `triage/models.py` | Typed data classes (CorpusDoc, TicketInput, TriageDecision) |
| `triage/corpus.py` | Corpus loader, TF-IDF indexer, retrieval logic |
| `triage/engine.py` | Ticket classification, escalation rules, response generation |

### Technology Stack

- **Language:** Python 3.13+
- **Core Dependencies:** Standard library only (no external ML/vector DB dependencies)
- **Optional UI:** Streamlit (for browser interface)
- **No external APIs:** All processing is local; no network calls for retrieval or inference

---

## Quick Start

### 1. Install Dependencies

```bash
# Terminal mode only (no UI)
# No additional dependencies needed; Python 3.8+ is sufficient

# With Streamlit UI (optional)
pip install -r code/requirements.txt
```

### 2. Run Terminal Agent (Batch Processing)

From repository root:

```bash
python code/main.py \
  --input support_tickets/support_tickets.csv \
  --output support_tickets/output.csv \
  --data-dir data
```

Expected output:
```
Processed tickets and wrote predictions to: support_tickets/output.csv
```

### 3. Run Web UI (Interactive)

```bash
streamlit run code/web_app.py
```

Then open your browser to `http://localhost:8501` and choose:
- **Single Ticket Tab:** Manually triage one ticket with instant feedback
- **Batch CSV Tab:** Upload CSV, process multiple tickets, download results
- **About Tab:** Documentation and corpus information

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip or equivalent package manager

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd Hackerrank-Triage-Agent
```

### Step 2: Verify Project Structure

Ensure these files exist:
- `code/main.py` (entry point)
- `code/triage/` (package with corpus, engine, models)
- `support_tickets/support_tickets.csv` (input)
- `data/` (corpus directory with HackerRank, Claude, Visa docs)

### Step 3: (Optional) Set Up Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Streamlit (Optional, for Web UI)

```bash
pip install -r code/requirements.txt
# or
pip install streamlit
```

### Step 5: Run Agent

Choose one of the following based on your needs.

---

## Usage

### Mode 1: Terminal/Batch Processing (Recommended for Evaluation)

Process all tickets in `support_tickets/support_tickets.csv` and write results to `output.csv`:

```bash
python code/main.py \
  --input support_tickets/support_tickets.csv \
  --output support_tickets/output.csv \
  --data-dir data
```

**Output File Structure:**
```csv
issue,subject,company,response,product_area,status,request_type,justification
"I lost access to my team workspace...","Access lost","claude","I cannot safely complete...","team-and-enterprise-plans","escalated","product_issue","Escalated due to high_risk_or_permission_sensitive..."
```

### Mode 2: Web UI (Interactive)

Start the Streamlit application:

```bash
streamlit run code/web_app.py
```

**Features:**
1. **Configuration:** Choose data directory from dropdown
2. **Single Ticket Tab:**
   - Select Company, enter Subject and Issue
   - View instant triage decision with status, request type, product area
   - See detailed response and justification
3. **Batch CSV Tab:**
   - Upload CSV with columns: `Issue`, `Subject`, `Company`
   - Processing progress bar
   - Download output.csv with all fields included
4. **About Tab:**
   - Application documentation
   - Corpus path reference

### Mode 3: Programmatic Usage

```python
import sys
sys.path.insert(0, 'code')

from triage import load_corpus, CorpusIndex
from triage.engine import triage_ticket
from triage.models import TicketInput

# Load corpus
docs = load_corpus('data')
index = CorpusIndex(docs)

# Triage a ticket
ticket = TicketInput(
    issue="My account is locked",
    subject="Account access",
    company="hackerrank"
)
decision = triage_ticket(ticket, index)

# Output
print(f"Status: {decision.status}")
print(f"Response: {decision.response}")
print(f"Justification: {decision.justification}")
```

---

## Design & Evaluation Alignment

This implementation directly addresses the HackerRank Orchestrate evaluation rubric:

### 1. Agent Design (Architecture & Approach)

**✓ Clear Separation of Concerns:**
- Corpus loading isolated in `corpus.py` with TF-IDF indexing
- Ticket classification and escalation in `engine.py`
- Data models in `models.py` with type hints
- Entry points (`main.py`, `web_app.py`) orchestrate the pipeline

**✓ Justified Technical Choices:**
- **TF-IDF over embeddings:** Fast, deterministic, requires no ML models
- **Rule-based classification:** Explicit patterns for bug/feature/invalid detection
- **Confidence-based escalation:** Low retrieval confidence triggers human review
- **No external APIs:** Pure local processing ensures reproducibility

### 2. Corpus Grounding

**✓ All Responses Grounded in Provided Data:**
- Responses extracted from top-ranked corpus documents
- Source URLs included when available
- Low-confidence matches escalated rather than hallucinated
- Zero external API calls for retrieval or answer generation

### 3. Escalation Logic

**✓ Comprehensive Escalation Coverage:**

| Trigger | Response |
|---------|----------|
| Permission-sensitive requests | Escalate for human verification |
| Security vulnerabilities | Escalate to security team |
| Low retrieval confidence | Escalate when score < 0.27 |
| Bug reports (low confidence) | Escalate when confidence < 0.33 |
| Invalid/out-of-scope requests | Reply with out-of-scope guidance |

### 4. Determinism & Reproducibility

**✓ Fully Deterministic:**
- No randomness in retrieval or scoring
- TF-IDF is deterministic
- Classification uses regex patterns (no ML randomness)
- Same inputs always produce same outputs
- No dependency on system time, RNG, or async operations

### 5. Engineering Hygiene

**✓ Production-Ready Code:**
- Type hints throughout (`triage/models.py`)
- Clear module structure and imports
- No hardcoded secrets or API keys
- Secrets read from environment variables (if needed)
- Standard library dependencies only (no bloat)
- Readable, maintainable code with comments
- No unused imports or dead code

---

## Project Structure

```
code/
├── main.py                    # CLI entry point for batch processing
├── triage_agent.py            # Backward-compatible wrapper
├── web_app.py                 # Streamlit interactive UI
├── requirements.txt           # Python dependencies (Streamlit only)
├── triage/
│   ├── __init__.py           # Package exports
│   ├── models.py             # Data classes: CorpusDoc, TicketInput, TriageDecision
│   ├── corpus.py             # Corpus loading & TF-IDF retrieval engine
│   └── engine.py             # Ticket triage engine & escalation logic
└── README.md                  # This file
```

---

## Detailed Implementation

### 1. Corpus Loading (`triage/corpus.py`)

```python
def load_corpus(data_dir: str) -> List[CorpusDoc]:
    """Load all .md files from data_dir and parse as support documents."""
```

- Recursively loads all Markdown files from `data/`
- Extracts frontmatter (title, source_url, breadcrumbs)
- Normalizes company from folder structure (hackerrank/claude/visa)
- Computes product area based on folder hierarchy
- Tokenizes and indexes for TF-IDF retrieval

### 2. Retrieval Engine (`triage/corpus.py` - `CorpusIndex` class)

```python
def search(query: str, company: str, top_k: int = 3) -> List[RetrievalHit]:
    """Retrieve top-k most relevant support documents."""
```

- TF-IDF scoring with document/query frequency weighting
- Company filtering (ensures HackerRank questions hit HackerRank docs, etc.)
- Penalizes index pages and release notes
- Title/path token boosting for direct matches
- Returns ranked hits with confidence scores

### 3. Ticket Classification (`triage/engine.py`)

```python
def classify_request_type(issue: str, subject: str) -> str:
    """Classify request as: product_issue, feature_request, bug, or invalid."""
```

- **Invalid:** Detects malicious/off-topic queries (hack, delete, malware)
- **Feature request:** Matches "would like to add", "can you add", etc.
- **Bug:** Matches "error", "failed", "not working", "down"
- **Product issue:** Default fallback

### 4. Escalation Logic (`triage/engine.py`)

```python
def _should_escalate(ticket, request_type, conf, hits) -> (bool, str):
    """Determine if ticket should be escalated or replied to."""
```

**Escalation triggers:**
- Permission-sensitive: "restore my access", "increase my score", "ban the seller"
- Security: "security vulnerability", "bug bounty"
- Low confidence: < 0.27 threshold
- Bug (low confidence): bug request with confidence < 0.33

### 5. Response Generation (`triage/engine.py`)

```python
def _build_reply_response(ticket, hits) -> str:
    """Generate user-facing response from top-ranked document."""
```

- Extracts 4 most supportive lines from top-ranked doc
- Includes source URL when available
- Truncates long responses (max 550 chars)
- Graceful fallback if no lines found

---

## Evaluation Criteria Checklist

- [x] **Architecture:** Clear modules, justified design choices
- [x] **Corpus grounding:** No external APIs; all responses from `data/`
- [x] **Escalation:** Comprehensive rules for high-risk/unsupported tickets
- [x] **Determinism:** Fully reproducible; no randomness
- [x] **Engineering:** Type hints, readable code, no hardcoded secrets
- [x] **Output format:** CSV with all 8 required columns
- [x] **Documentation:** Comprehensive README with usage examples
- [x] **Runnable:** Terminal and UI modes work out-of-the-box

---

## Links & Resources

### Project Links
- **Repository:** [HackerRank Orchestrate on GitHub](https://github.com/mahammadaftab/Hackerrank-Triage-Agent.git)
- **Challenge:** [HackerRank Orchestrate Hackathon](https://www.hackerrank.com/contests/hackerrank-orchestrate-may26/)

### Developer Profile
- **GitHub:** [github.com/yourusername](https://github.com/mahammadaftab)
- **LinkedIn:** [linkedin.com/in/yourprofile](https://www.linkedin.com/in/mahammad-aftab)

### Related Documentation
- [problem_statement.md](../problem_statement.md) — Full task specification
- [AGENTS.md](../AGENTS.md) — AI tool integration guidelines

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'triage'`

**Solution:** Run from repository root, not from `code/` directory:
```bash
cd /path/to/hackerrank-orchestrate-may26
python code/main.py --input support_tickets/support_tickets.csv --output support_tickets/output.csv --data-dir data
```

### Issue: `FileNotFoundError: data/` directory not found

**Solution:** Ensure the `data/` corpus directory exists in the repository root with subdirectories: `data/hackerrank/`, `data/claude/`, `data/visa/`

### Issue: Streamlit won't start

**Solution:** Install Streamlit first:
```bash
pip install streamlit
```

### Issue: Output CSV has wrong columns

**Solution:** Verify you're running the latest version of the code. Output should have 8 columns:
```
issue,subject,company,response,product_area,status,request_type,justification
```

---

## Support

For questions or issues, please open an issue on GitHub or contact the development team via the links above.

---

**Built with ❤️ for HackerRank Orchestrate 2026**
