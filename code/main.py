import pandas as pd
import os

# 1. Paths set karein
TICKETS_PATH = '../support_tickets/support_tickets.csv'
OUTPUT_PATH = '../support_tickets/output.csv'
DATA_DIR = '../data/'

def process_tickets():
    # CSV load karein
    if not os.path.exists(TICKETS_PATH):
        print("Error: support_tickets.csv nahi mili!")
        return

    df = pd.read_csv(TICKETS_PATH)
    
    results = []

    for index, row in df.iterrows():
        ticket_id = row['ticket_id']
        customer_query = row['customer_query']
        
        print(f"Processing ticket {ticket_id}...")

        # --- AI LOGIC YAHAN AAYEGI ---
        # Aapko yahan RAG (Retrieval-Augmented Generation) use karna hoga
        # jo data/ folder se sahi file uthaye.
        
        status = "replied" # ya "escalated"
        product_area = "General" 
        response = "Ye aapka dummy response hai. AI integration baaki hai."
        justification = "Query was simple and found in docs."
        request_type = "product_issue" # product_issue, bug, etc.
        # -----------------------------

        results.append({
            "ticket_id": ticket_id,
            "status": status,
            "product_area": product_area,
            "response": response,
            "justification": justification,
            "request_type": request_type
        })

    # Results ko output.csv mein save karein
    output_df = pd.DataFrame(results)
    output_df.to_csv(OUTPUT_PATH, index=False)
    print(f"Kaam ho gaya! Output save ho gaya hai: {OUTPUT_PATH}")

if __name__ == "__main__":
    process_tickets()
