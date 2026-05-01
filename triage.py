import pandas as pd
import os

class SupportAgent:
    def __init__(self):
        # Define high-risk triggers for escalation logic
        self.escalation_keywords = [
            'bug', 'down', 'error', 'fraud', 'stolen', 
            'hacked', 'billing', 'unauthorized', 'login'
        ]

    def classify_domain(self, text, company):
        """Infers company domain if missing."""
        if pd.notna(company) and company != "None":
            return company
        
        text = text.lower()
        if any(k in text for k in ['test', 'hackerrank', 'assessment']): return "HackerRank"
        if any(k in text for k in ['claude', 'anthropic', 'artifact']): return "Claude"
        if any(k in text for k in ['visa', 'card', 'transaction']): return "Visa"
        return "Unknown"

    def get_grounded_response(self, domain, text):
        """Knowledge Base: Only uses provided support corpus logic."""
        text = text.lower()
        
        if domain == "HackerRank":
            if "active" in text or "expire" in text:
                return ("Tests remain active indefinitely unless start/end times are set in Settings > General.", 
                        "Assessment Management")
            if "invite" in text:
                return ("Click 'Invite' on the test dashboard. Ensure the test is active.", 
                        "Candidate Experience")
        
        if domain == "Claude" and "artifact" in text:
            return ("Artifacts allow side-by-side viewing/editing of code and docs.", 
                    "UI Features")
            
        if domain == "Visa" and "benefit" in text:
            return ("Benefits are managed by your issuer; contact your bank for details.", 
                    "Card Services")
            
        return (None, None)

    def process_ticket(self, row):
        issue = str(row.get('Issue', '')).lower()
        subject = str(row.get('Subject', '')).lower()
        full_text = f"{issue} {subject}"
        domain = self.classify_domain(full_text, row.get('Company'))

        # 1. Determine Request Type
        req_type = "bug" if "bug" in full_text else "product_issue"
        
        # 2. Routing Logic (Escalation vs Reply)
        grounded_text, area = self.get_grounded_response(domain, full_text)
        
        should_escalate = (
            any(k in full_text for k in self.escalation_keywords) or 
            domain == "Unknown" or 
            grounded_text is None
        )

        if should_escalate:
            return {
                "status": "escalated",
                "product_area": area if area else f"{domain} Support",
                "response": "Escalated to a human.",
                "justification": "Sensitive issue or complex query outside automated FAQ scope.",
                "request_type": req_type
            }

        return {
            "status": "replied",
            "product_area": area,
            "response": grounded_text,
            "justification": f"Grounded response provided based on {domain} support documentation.",
            "request_type": req_type
        }

def main():
    agent = SupportAgent()
    input_file = 'support_tickets.csv'
    output_file = 'output.csv'
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    df = pd.read_csv(input_file)
    results = df.apply(agent.process_ticket, axis=1)
    pd.DataFrame(list(results)).to_csv(output_file, index=False)
    print(f"Triage complete. Results saved to {output_file}")

if __name__ == "__main__":
    main()
