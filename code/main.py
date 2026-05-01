import os
import argparse
import pandas as pd
from retriever import retrieve
from agent import process_ticket
from classifier import pre_classify

def main():
    parser = argparse.ArgumentParser(description="Support Ticket Triage Agent")
    parser.add_argument("--dry-run", action="store_true", help="Process only the first 3 rows")
    parser.add_argument("--ticket", type=int, help="Process a single ticket index")
    args = parser.parse_args()

    input_path = "support_tickets/support_tickets.csv"
    output_path = "support_tickets/output.csv"

    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    df = pd.read_csv(input_path)
    
    if args.dry_run:
        df = df.head(3)
    elif args.ticket is not None:
        if 0 <= args.ticket < len(df):
            df = df.iloc[[args.ticket]]
        else:
            print(f"Error: Ticket index {args.ticket} out of range.")
            return

    results = []
    total = len(df)

    for i, row in df.iterrows():
        ticket = {
            "issue": row.get('Issue', row.get('issue', '')),
            "subject": row.get('Subject', row.get('subject', '')),
            "company": str(row.get('Company', row.get('company', 'None')))
        }

        print(f"Ticket {i+1}/{total} -> ", end="", flush=True)

        # 1. Pre-classify
        output = pre_classify(ticket)
        
        if output:
            print("escalated (safety)")
        else:
            # 2. Retrieve context
            try:
                query = f"{ticket['subject']} {ticket['issue']}"
                context = retrieve(query, company=ticket['company'])
                
                # 3. Process with LLM
                output = process_ticket(ticket, context)
                print(output.get('status', 'unknown'))
            except Exception as e:
                print(f"error: {e}")
                output = {
                    "status": "escalated",
                    "product_area": "System Error",
                    "response": "I encountered an error while processing this request. Escalating to a human.",
                    "justification": f"Exception: {str(e)}",
                    "request_type": "product_issue"
                }

        # Merge output into result row
        result_row = row.to_dict()
        result_row.update(output)
        results.append(result_row)

    # Save to output.csv
    out_df = pd.DataFrame(results)
    out_df.to_csv(output_path, index=False)
    print(f"\nProcessing complete. Results saved to {output_path}")

if __name__ == "__main__":
    main()
