Multi-Domain Support Triage Agent

This project implements a deterministic support triage agent for the HackerRank Orchestrate challenge. It processes support tickets across three domains:

- Claude (Anthropic)
- HackerRank
- Visa

The system classifies tickets, retrieves relevant documentation, decides whether to reply or escalate, and generates grounded responses.

--------------------------------------------------

System Overview

The agent follows a Retrieval-Augmented Decision Pipeline:

Input Ticket → Classification → Retrieval (TF-IDF) → Decision Engine → Response / Escalation

--------------------------------------------------

Architecture

1. Knowledge Base (kb.py)
- Loads Markdown files from the data/ directory
- Splits documents into fixed-size chunks
- Tags each chunk with its domain (claude / hackerrank / visa)

2. Retriever (retriever.py)
- Uses TF-IDF vectorization with cosine similarity
- Filters by company before scoring
- Returns top relevant chunks

3. Classifier (classifier.py)
Rule-based classification into:
- product_issue
- bug
- feature_request
- invalid

Designed to remain deterministic and avoid overfitting.

4. Decision Engine (decision.py)
Determines:
- status (replied / escalated)
- justification

Uses strict rules for:
- Financial and billing issues
- Security and fraud cases
- Vulnerabilities
- Admin actions (remove user, reschedule, etc.)
- Subscription control (pause/cancel)
- Compliance requests
- Low-confidence retrieval

5. Response Generation (main.py)
- Uses retrieved context only
- No hallucinated content
- If confidence is low → escalates instead of replying

--------------------------------------------------

Key Design Decisions

- Deterministic system  
  Same input always produces the same output.

- No external APIs  
  Fully offline; uses only the provided corpus.

- Rule-based escalation  
  Ensures safe handling of high-risk queries.

- Corpus grounding  
  All responses are derived from retrieved documentation only.

--------------------------------------------------

Escalation Policy

The system escalates in the following cases:

- Visa financial issues (billing, fraud, urgent money requests)
- Security issues (unauthorized access, stolen card, vulnerabilities)
- Admin actions (remove employee/user, account modifications)
- Subscription control (pause, cancel, stop)
- Compliance / infosec-related queries
- Low retrieval confidence
- Unsupported or unsafe queries

--------------------------------------------------

Project Structure

code/
  main.py          # Entry point (runs full pipeline)
  kb.py            # Loads and chunks support documents
  retriever.py     # TF-IDF retrieval with cosine similarity
  classifier.py    # Rule-based request classification
  decision.py      # Escalation and decision logic

data/              # Support knowledge base (Markdown files)

support_tickets/
  support_tickets.csv   # Input tickets
  output.csv            # Generated output

requirements.txt        # Python dependencies
README.txt              # Project documentation
log.txt                 # Development log

--------------------------------------------------

How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the pipeline:
python code/main.py

3. Output file will be generated at:
support_tickets/output.csv

--------------------------------------------------

Output Format

issue,subject,company,response,product_area,status,request_type,justification

--------------------------------------------------

Output Guarantees

- No hallucinated responses
- Deterministic behavior
- Strict escalation for sensitive cases
- Fully grounded in provided documentation

--------------------------------------------------

Limitations

- Keyword-based rules may miss rare paraphrases
- TF-IDF retrieval may return less optimal results for ambiguous queries

--------------------------------------------------

Future Improvements

- Semantic retrieval using embeddings
- Hybrid ranking (BM25 + vector search)
- Improved intent classification
- Smarter document chunking

--------------------------------------------------

Summary

This system prioritizes:
- Safety over automation
- Determinism over complexity
- Grounded responses over generative output

It is designed to be robust, explainable, and evaluation-ready.