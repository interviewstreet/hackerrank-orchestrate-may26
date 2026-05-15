# Support Ticket Triage Agent

## Overview
Support Ticket Triage Agent is a terminal-based RAG workflow for the HackerRank Orchestrate hackathon. It reads support tickets from CSV, retrieves relevant context from local documentation, applies safety rules, and generates structured responses with Gemini.

The system supports three ticket domains: HackerRank, Claude, and Visa.

## Architecture
1. **Input**: Reads tickets from `support_tickets/support_tickets.csv`.
2. **Pre-classification**: Applies rule-based safety filters for fraud, prompt injection, account compromise, legal escalation, and similar sensitive cases.
3. **Retrieval**: Uses a TF-IDF retriever over the local `data/` corpus to gather relevant context.
4. **LLM generation**: Calls the Gemini API (`google-generativeai`) to produce grounded, structured responses.
5. **Output**: Writes results to `support_tickets/output.csv`.
6. **Logging**: Appends session activity to `$HOME/hackerrank_orchestrate/log.txt`.

## Setup
1. Install Python 3.9+.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the repository root and add your Gemini API key:

```bash
GEMINI_API_KEY=your_key_here
```

## Usage
Run the agent from the repository root:

```bash
python3 code/main.py
```

Useful flags:

- `--dry-run` processes only the first 3 tickets.
- `--ticket N` processes only ticket index `N`.

## Output Format
The agent generates `support_tickets/output.csv` with one row per ticket. The main output columns are:

- `issue`
- `subject`
- `company`
- `response`
- `product_area`
- `status`
- `request_type`
- `justification`

If a row fails during processing, the pipeline handles the error per ticket and continues with the remaining rows.

## Security
The classifier is designed to escalate sensitive or unsafe requests automatically, including:

- Prompt injection attempts
- Data exfiltration requests
- Fraud and account compromise cases
- Legal or law-enforcement related issues
- Score disputes and similar high-risk cases

Sensitive inputs are handled conservatively so the agent can defer to human support when needed.

## Notes
- This project is CLI-based and has no external UI.
- Responses are intended to be strictly grounded in retrieved context.
- JSON parsing is kept strict so the CSV output remains valid for evaluation.
- The retrieval layer is lightweight and does not require an external vector database.
