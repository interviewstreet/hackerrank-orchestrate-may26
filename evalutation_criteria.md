# Evaluation Criteria

Your submission for **HackerRank Orchestrate** is evaluated across these dimensions. Each dimension is scored independently and then combined into your final score. Results will be announced on May 15, 2026.

---

## 1. Agent Design

We read the contents of your `code/` directory to assess **how** you built the agent.

We look for:

- **Architecture & approach** — clear separation of concerns (retrieval, reasoning, routing, output), and a justified choice of technique (RAG, tool use, structured output, agent framework, classical ML, etc.).
- **Use of the provided corpus** — grounded answers from `data/` rather than the model's parametric knowledge.
- **Escalation logic** — explicit handling of high-risk, sensitive, or out-of-scope tickets.
- **Determinism & reproducibility** — seeded sampling, pinned dependencies, and a runnable `code/README.md`.
- **Engineering hygiene** — readable code, sensible modules, secrets read from env vars, no hardcoded keys.

---

## 2. AI Judge Interview

A 30-minute interview with the AI Judge after submission (camera on, mandatory).

We look for:

- **Depth of understanding** — can you explain why you made each design decision?
- **Trade-off awareness** — what alternatives did you consider and why did you reject them?
- **Failure-mode reasoning** — where does your agent break, and how would you fix it?
- **Honesty about AI assistance** — clearly distinguish what you designed from what an AI tool generated for you.

---

## 3. Output CSV

Your agent's predictions in `support_issues/output.csv`, produced by running against `support_issues/support_issues.csv`.

We score per row across all five output columns:

| Column          | What we check                                                                 |
| --------------- | ----------------------------------------------------------------------------- |
| `status`        | Correct `replied` vs `escalated` decision                                     |
| `product_area`  | Correct support category / domain area                                        |
| `response`      | Faithful to the corpus, helpful, non-hallucinated                             |
| `justification` | Concise, accurate, traceable to the corpus                                    |
| `request_type`  | Correct `product_issue` / `feature_request` / `bug` / `invalid` classification |

No hallucinated policies, fabricated steps, or guessing instead of escalating on high-risk tickets.

---

## 4. AI Fluency (Chat Transcript)

We read your `log.txt` chat transcript (see README → *Chat transcript logging*) to assess how effectively you collaborated with AI tools while building.

We look for clear, scoped prompts and evidence that you critiqued, verified, and drove the AI rather than blindly accepting its output.
You — not the AI — should be visibly steering the architectural decisions.

---
