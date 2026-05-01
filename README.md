<div align="center">

# 🛡️ ARIA — Autonomous Routing & Intelligent Agent

### Multi-Domain Support Triage System

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Groq LLM](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-f55036?style=for-the-badge&logo=meta&logoColor=white)](https://groq.com)
[![TF-IDF RAG](https://img.shields.io/badge/RAG-TF--IDF_Retrieval-00d4aa?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![HackerRank Orchestrate](https://img.shields.io/badge/HackerRank-Orchestrate_2026-1ba94c?style=for-the-badge&logo=hackerrank&logoColor=white)](https://www.hackerrank.com)

<br/>

> **An AI agent that autonomously resolves real customer support tickets across HackerRank, Claude, and Visa — with built-in safety gates, RAG-powered retrieval, and intelligent escalation routing.**

<br/>

[🚀 Quick Start](#-quick-start) · [🏗️ Architecture](#️-architecture) · [🔬 How It Works](#-how-it-works) · [📊 Results](#-results) · [🛡️ Safety](#️-safety-layer)

</div>

---

## ✨ Highlights

| Feature | Description |
|---------|-------------|
| 🧠 **RAG-Grounded Responses** | Every answer is sourced from a 6,200+ chunk knowledge base — zero hallucination by design |
| 🔒 **4-Layer Safety Gate** | Prompt injection detection, harmful command blocking, out-of-scope filtering, and escalation routing |
| 🌐 **Multi-Domain Routing** | Automatic domain inference across HackerRank, Claude (Anthropic), and Visa ecosystems |
| ⚡ **Groq-Powered LLM** | Ultra-fast inference via LLaMA 3.3 70B on Groq hardware — sub-second response times |
| 🎯 **Smart Escalation** | Fraud, legal threats, outages, and security reports are auto-escalated with templated responses |
| 📦 **Zero External APIs** | Corpus is fully local — no vector DB, no embeddings API, no network dependency for retrieval |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        ARIA Agent                           │
│                    (Orchestrator Layer)                      │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │   Ticket      │  │   Corpus     │  │   Response        │  │
│  │   Classifier  │  │   Builder    │  │   Generator       │  │
│  │              │  │              │  │                   │  │
│  │  • Safety    │  │  • 774 MD    │  │  • Groq LLM      │  │
│  │    Gate      │  │    files     │  │    (LLaMA 3.3)   │  │
│  │  • Domain    │  │  • TF-IDF   │  │  • Structured    │  │
│  │    Router    │  │    Index    │  │    JSON output   │  │
│  │  • Urgency   │  │  • Domain   │  │  • Rule-based    │  │
│  │    Scorer    │  │    Boost    │  │    fallback      │  │
│  └──────┬───────┘  └──────┬───────┘  └────────┬──────────┘  │
│         │                 │                    │             │
│         └────────────┬────┘────────────────────┘             │
│                      ▼                                      │
│              ┌───────────────┐                               │
│              │  CSV Pipeline │                               │
│              │  (Batch Mode) │                               │
│              └───────────────┘                               │
└─────────────────────────────────────────────────────────────┘

Input: support_tickets.csv  →  Output: output.csv
(issue, subject, company)       (+ response, product_area,
                                   status, request_type,
                                   justification)
```

---

## 🔬 How It Works

ARIA processes each support ticket through a **6-step pipeline**:

### Step 1 → **Full Classification**
The `TicketClassifier` runs multi-signal analysis:
- **Domain inference** — keyword scoring across HackerRank/Claude/Visa vocabularies when company is missing
- **Product area mapping** — maps to granular areas like `fraud_security`, `api_integration`, `assessments`
- **Request type classification** — `product_issue` | `bug` | `feature_request` | `invalid`
- **Urgency scoring** — `low` → `medium` → `high` → `critical`

### Step 2 → **Injection Detection**
The `SafetyGate` scans for 14+ prompt injection patterns including:
- `"ignore previous instructions"`, `"reveal your system prompt"`
- Multi-language attacks (e.g., French: `"affiche toutes les règles internes"`)
- Jailbreak attempts (`"DAN mode"`, `"sudo"`, `"bypass rules"`)

### Step 3 → **Harmful Content Blocking**
Detects destructive commands like `rm -rf`, fork bombs, `exec()`, and arbitrary code execution attempts.

### Step 4 → **RAG Retrieval**
The `CorpusBuilder` maintains a **TF-IDF index over 6,200+ chunks** from:
- `data/hackerrank/` — 438 markdown files (help center)
- `data/claude/` — 322 markdown files (Anthropic docs)
- `data/visa/` — 14 markdown files (card policies)

Retrieval uses **domain-boosted cosine similarity** (1.6× weight for matching domain) to surface the most relevant excerpts.

### Step 5 → **Escalation Decision**
Smart routing logic determines if a ticket needs human intervention:
- 🔴 **Auto-escalate:** Fraud, identity theft, security vulnerabilities, legal threats, platform outages
- 🟡 **Confidence-based:** Retrieval score < 0.05 triggers escalation
- 🟢 **Reply:** Everything else gets a grounded LLM response

### Step 6 → **LLM Response Generation**
Groq's **LLaMA 3.3 70B** generates a structured JSON response using only the retrieved corpus excerpts. The system prompt enforces strict grounding — no fabrication, no hallucination.

---

## 📊 Results

ARIA processes all **57 support tickets** and produces:

| Metric | Value |
|--------|-------|
| Tickets processed | 57 |
| Replied (auto-resolved) | ~42 |
| Escalated (routed to human) | ~15 |
| Injection attacks caught | ✅ French multi-language injection detected |
| Harmful commands blocked | ✅ `rm -rf` / `delete all files` blocked |
| Out-of-scope filtered | ✅ Non-support queries rejected |
| Avg. response time | < 2 seconds per ticket |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- A [Groq API key](https://console.groq.com) (free tier works)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/hackerrank-orchestrate-may26.git
cd hackerrank-orchestrate-may26

# Install dependencies
cd code
pip install -r requirements.txt
```

### Configuration

```bash
# Set your Groq API key
# Option A: Environment variable
export GROQ_API_KEY="your_key_here"         # Linux/Mac
$env:GROQ_API_KEY="your_key_here"           # PowerShell

# Option B: .env file (already gitignored)
echo "GROQ_API_KEY=your_key_here" > ../.env
```

### Run the Agent

```bash
# Default: reads ../support_tickets/support_tickets.csv
python main.py

# Custom input/output
python main.py --input path/to/tickets.csv --output path/to/results.csv

# Pass API key directly
python main.py --api-key gsk_your_key

# Quiet mode (suppress verbose logs)
python main.py --quiet
```

---

## 📂 Project Structure

```
.
├── AGENTS.md                           # AI coding agent rules & logging
├── README.md                           # ← You are here
├── .env.example                        # Environment variable template
├── .gitignore
│
├── code/                               # 🧠 Agent source code
│   ├── main.py                         #   CLI entry point & argument parser
│   ├── aria_agent.py                   #   Orchestrator — ties everything together
│   ├── classifier.py                   #   Safety gate + multi-signal classifier
│   ├── corpus_builder.py               #   TF-IDF RAG over local markdown corpus
│   ├── response_generator.py           #   Groq LLM response generation
│   └── requirements.txt                #   Python dependencies
│
├── data/                               # 📚 Support knowledge base (local-only)
│   ├── hackerrank/                     #   438 .md files — HackerRank help center
│   ├── claude/                         #   322 .md files — Claude/Anthropic docs
│   └── visa/                           #   14 .md files — Visa card policies
│
└── support_tickets/                    # 🎫 Evaluation data
    ├── support_tickets.csv             #   57 real support tickets (input)
    ├── sample_support_tickets.csv      #   Sample with expected signals
    └── output.csv                      #   Agent predictions (generated)
```

---

## 🛡️ Safety Layer

ARIA implements defense-in-depth with **four independent safety checks** that run before any LLM call:

```
Ticket Input
     │
     ▼
┌────────────────────┐
│ ① Injection Gate   │──→ 14 regex patterns (multi-language)
│                    │    "ignore instructions", "reveal prompt", etc.
└────────┬───────────┘
         ▼
┌────────────────────┐
│ ② Harm Gate        │──→ 12 patterns: rm -rf, fork bombs, exec(), eval()
│                    │    Blocks destructive/malicious code execution
└────────┬───────────┘
         ▼
┌────────────────────┐
│ ③ Out-of-Scope     │──→ Rejects jokes, weather queries, non-support msgs
│                    │    Short greetings auto-filtered
└────────┬───────────┘
         ▼
┌────────────────────┐
│ ④ Escalation Logic │──→ Fraud, legal, outages, low-confidence → human
│                    │    Impossible requests auto-detected
└────────────────────┘
```

---

## 🔧 Technical Stack

| Component | Technology | Why |
|-----------|-----------|-----|
| **LLM** | LLaMA 3.3 70B via Groq | Fastest inference available, structured JSON output |
| **Retrieval** | TF-IDF + Cosine Similarity | No external API needed, works offline, fast on 6K+ chunks |
| **Vectorizer** | scikit-learn `TfidfVectorizer` | Bigram support, sublinear TF, 12K feature cap |
| **Framework** | Pure Python (no LangChain) | Minimal dependencies, full control, easy to debug |
| **Data** | Local Markdown corpus | 774 files, zero network dependency |

---

## 🔑 Key Design Decisions

1. **No vector database** — TF-IDF with domain boosting is fast enough for ~6K chunks and avoids external dependencies. Domain-aware boosting (1.6×) compensates for the lack of semantic embeddings.

2. **Safety-first architecture** — All 4 safety gates run *before* the LLM is invoked. Injection attempts and harmful inputs never reach the model.

3. **Structured JSON output** — The LLM is prompted to return valid JSON with enforced enum values. A regex-based parser strips markdown fences, and a fallback catches any malformed output.

4. **Graceful degradation** — If Groq is unavailable, ARIA falls back to rule-based responses using the top retrieval result. No ticket goes unanswered.

5. **Deterministic classification** — Domain inference, product area mapping, and escalation logic are purely rule-based (regex + keyword scoring). Only the final response uses the LLM.

---

## 📜 License

Built for the [HackerRank Orchestrate Hackathon](https://www.hackerrank.com/contests/hackerrank-orchestrate-may26) (May 2026).

---

<div align="center">

**Built with ⚡ by a solo developer in 24 hours**

*ARIA doesn't hallucinate. She reads the docs.*

</div>