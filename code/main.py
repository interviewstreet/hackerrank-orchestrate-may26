import os
import csv
from pathlib import Path
from config import (
    GROQ_API_KEY, VECTOR_DB_DIR, TOP_K_RESULTS,
    DATA_DIR, SUPPORT_TICKETS_DIR
)
from corpus import load_corpus
from retriever import Retriever
from pipeline import process_ticket


def main():
    if not GROQ_API_KEY:
        print("Error: GROQ_API_KEY not set in environment")
        return
    
    retriever = Retriever(persist_dir=VECTOR_DB_DIR, top_k=TOP_K_RESULTS)
    
    if retriever.index is None or len(retriever.documents) == 0:
        print("Loading and indexing corpus...")
        documents = load_corpus(DATA_DIR)
        print(f"Loaded {len(documents)} document chunks")
        retriever.build_index(documents)
        print("Indexing complete")
    else:
        print(f"Using existing index with {len(retriever.documents)} documents")
    
    input_file = Path(SUPPORT_TICKETS_DIR) / "support_tickets.csv"
    output_file = Path(SUPPORT_TICKETS_DIR) / "output.csv"
    
    rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, quotechar='"', delimiter=',')
        header = next(reader)
        for row in reader:
            if len(row) >= 3:
                rows.append({
                    "Issue": row[0].replace('\n', ' ').strip(),
                    "Subject": row[1].strip(),
                    "Company": row[2].strip()
                })
    
    print(f"Parsed {len(rows)} tickets")
    
    results = []
    print(f"Processing {len(rows)} tickets...")
    
    for i, row in enumerate(rows):
        result = process_ticket(row, retriever)
        results.append({
            "Issue": row.get("Issue", ""),
            "Subject": row.get("Subject", ""),
            "Company": row.get("Company", ""),
            "Response": result["response"],
            "Product Area": result["product_area"],
            "Status": result["status"],
            "Request Type": result["request_type"]
        })
        print(f"Processed ticket {i+1}/{len(rows)}")
    
    fieldnames = ["Issue", "Subject", "Company", "Response", "Product Area", "Status", "Request Type"]
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    print(f"Results written to {output_file}")


if __name__ == "__main__":
    main()