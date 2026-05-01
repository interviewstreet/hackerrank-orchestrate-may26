# Support Triage Agent

## Overview
This is a terminal-based support triage agent designed for the HackerRank Orchestrate hackathon. It handles support tickets across three domains: HackerRank, Claude, and Visa, using a grounded RAG (Retrieval-Augmented Generation) approach.

## Architecture
1. **Classifier**: A rule-based pre-filter that catches high-risk or sensitive keywords (fraud, legal, prompt injection) and forces escalation.
2. **Retriever**: A TF-IDF based search engine that indexes local support documentation (.md and .txt) from the `data/` directory.
3. Agent: An LLM-powered processor (using Gemini 1.5 Flash) that generates grounded responses based strictly on retrieved context.
4. Output: Structured JSON containing status, product area, response, justification, and request type.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the root directory:
   ```bash
   GEMINI_API_KEY=your_api_key_here
   ```

## Run
To process all tickets in `support_tickets/support_tickets.csv`:
```bash
python code/main.py
```

## Flags
- `--dry-run`: Processes only the first 3 rows for quick testing.
- `--ticket N`: Processes only the ticket at index N.

## Design Decisions
- **TF-IDF**: Chosen for its speed and lack of requirement for heavy external vector databases or GPUs.
- **Rule-based Escalation**: Ensures safety-critical issues (like fraud or score disputes) are handled by humans immediately.
- **Strict Grounding**: The system prompt forces the model to rely only on provided chunks.
