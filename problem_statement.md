# Multi-Domain Support Triage Challenge

Build a terminal-based support triage agent that can handle support tickets across three ecosystems:

- HackerRank Support: [https://support.hackerrank.com/](https://support.hackerrank.com/)
- Claude Help Center: [https://support.claude.com/en/](https://support.claude.com/en/)
- Visa Support: [https://www.visa.co.in/support.html](https://www.visa.co.in/support.html)

Your agent must use only the provided support corpus to understand the issue, decide whether it can be answered safely, and determine when it should be escalated to a human.

## What the agent should do

For each issue, the agent should:

- identify the request type
- classify the issue into a product area
- assess urgency and risk
- decide whether to reply or escalate
- retrieve the most relevant support documentation
- generate a safe, grounded response

Some cases will be simple FAQs. Others may involve billing, bugs, fraud, permissions, account access, assessments, or other sensitive situations that require careful routing.

## Files provided

You will receive two CSV files:

1. `sample_support_tickets.csv`  
   Contains example cases with both inputs and expected outputs. Use this to understand the format and expected behavior.

2. `support_tickets.csv`  
   Contains only the inputs. You must run your agent on this file and produce the required outputs.

## Input schema

Each row represents one support case.

Input fields:

- `issue`: the main ticket body or question
- `subject`: may be blank, partial, noisy, or irrelevant
- `company`: `HackerRank`, `Claude`, `Visa`, or `None`

Notes:

- A row may contain multiple requests
- A row may contain irrelevant, misleading, or malicious text
- If `company` is `None`, the issue may be generic or cross-domain, and your agent should infer the best handling from the content
- The agent must rely only on the provided support corpus, not outside knowledge

## Required output

For each row, generate:

- `status`
- `product_area`
- `response`
- `justification`
- `request_type`

Allowed values:

- `status`: `replied`, `escalated`
- `request_type`: `product_issue`, `feature_request`, `bug`, `invalid`

In case the issue is not relevant or outside the scope of the agent, it should be able decide whether it should escalate or reply with a response saying it is out of scope. The agent should be smart to understand on when to escalate and when to reply in these scenarios.

## Output meaning

- `status`: whether the agent should answer directly or escalate
- `product_area`: the most relevant support category or domain area
- `response`: a user-facing answer grounded in the support corpus
- `justification`: a concise explanation of the decision & response
- `request_type`: the best-fit request classification

## Requirements

Your solution must:

- be terminal-based
- use only the provided support corpus
- avoid unsupported claims or hallucinated policies
- escalate high-risk, sensitive, or unsupported cases when appropriate

These are the must-haves. Beyond that, participants are encouraged to add improvements or features of their own, such as better retrieval, stronger safety checks, clearer reasoning etc.
