## I have to write all my code here only inside the code folder 
## i dont have to use any external "knowledge source" , i shud just use the data folder
## only touching data folder and support ticket folder for reading writing 
"""
main.py — Terminal entrypoint
Usage:
  python main.py                        # runs on support_tickets.csv
  python main.py --sample               # runs on sample_support_tickets.csv
  python main.py --file path/to/csv     # custom input file
  python main.py --ingest               # re-run corpus ingestion
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import argparse
import pandas as pd
from tqdm import tqdm

from config import INPUT_CSV, SAMPLE_CSV, OUTPUT_CSV
from pipeline import run as run_pipeline


def parse_args():
    parser = argparse.ArgumentParser(description="Multi-domain support triage agent")
    parser.add_argument("--sample", action="store_true",  help="Run on sample CSV")
    parser.add_argument("--ingest", action="store_true",  help="Re-ingest corpus into local embeddings store")
    parser.add_argument("--file",   type=str, default=None, help="Custom input CSV path")
    parser.add_argument("--trial", action="store_true",  help="Run on trial_*.csv with trial_*.csv output")
    return parser.parse_args()


def main():
    args = parse_args()

    if args.ingest:
        print("[main] Running corpus ingestion...")
        from utils.loader import ingest
        ingest()
        print("[main] Ingestion done. Re-run without --ingest to process tickets.")
        return

    input_path = args.file or (SAMPLE_CSV if args.sample else INPUT_CSV)

    if not os.path.exists(input_path):
        print(f"[main] ERROR: input file not found: {input_path}")
        sys.exit(1)

    df = pd.read_csv(input_path, dtype=str).fillna("")
    print(f"[main] Loaded {len(df)} tickets from {input_path}")

    # Support both lowercase and capitalized CSV headers.
    col_map = {str(col).strip().lower(): col for col in df.columns}
    issue_col = col_map.get("issue", "issue")
    subject_col = col_map.get("subject", "subject")
    company_col = col_map.get("company", "company")

    results = []
    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Processing tickets"):
        ticket = {
            "issue":   row.get(issue_col, ""),
            "subject": row.get(subject_col, ""),
            "company": row.get(company_col, None),
        }
        output = run_pipeline(ticket, ticket_id=idx)
        results.append(output)

    rows = []
    for r in results:
        rows.append({
            "status": str(r.get("status", "escalated")).lower(),
            "product_area": str(r.get("product_area", "unknown") or "unknown"),
            "response": str(r.get("response", "") or ""),
            "justification": str(r.get("justification", "") or ""),
            "request_type": str(r.get("request_type", "product_issue") or "product_issue"),
        })

    out_df = pd.DataFrame(rows, columns=[
        "status",
        "product_area",
        "response",
        "justification",
        "request_type",
    ])

    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    out_df.to_csv(OUTPUT_CSV, index=False)
    print(f"\n[main] Output written to {OUTPUT_CSV}")
    print(f"[main] Log written to logs/log.txt")


if __name__ == "__main__":
    main()