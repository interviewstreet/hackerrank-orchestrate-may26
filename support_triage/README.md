# Support Triage Agent

Terminal-based support triage agent for the HackerRank, Claude, and Visa challenge.

## What it does

- Reads support tickets from a CSV.
- Uses `sample_support_tickets.csv` as the local support corpus.
- Retrieves the most relevant corpus examples with a small TF-IDF scorer.
- Classifies each ticket into `request_type`, `product_area`, and `status`.
- Replies only when a close corpus-grounded answer is available.
- Escalates sensitive, high-risk, ambiguous, or unsupported cases.

The implementation is deterministic and uses only Python's standard library.

## Run

From the repo root:

```powershell
python support_triage\triage_agent.py
```

This uses the default paths:

- Sample corpus: `support_triage\data_raw\support_tickets\sample_support_tickets.csv`
- Input tickets: `support_triage\data_raw\support_tickets\support_tickets.csv`
- Output: `support_triage\output.csv`

You can also pass explicit paths:

```powershell
python support_triage\triage_agent.py --input path\to\support_tickets.csv --sample path\to\sample_support_tickets.csv --output path\to\output.csv
```

## Routing approach

The agent first normalizes the ticket and infers the company if needed. It then:

1. Retrieves the closest support examples from the sample corpus.
2. Detects invalid or out-of-scope requests.
3. Applies conservative safety rules for billing, refunds, account access, security, fraud, disputes, outages, and unsupported administrative actions.
4. Generates a response from retrieved corpus text when safe.
5. Escalates when the answer would require human verification or unsupported policy.

The `justification` column records the decision reason and the top retrieved support example.
