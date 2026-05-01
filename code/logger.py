def log_entry(f, ticket, product, req, score, decision):
    f.write(f"Ticket: {ticket}\n")
    f.write(f"Product: {product}\n")
    f.write(f"Type: {req}\n")
    f.write(f"Score: {score:.3f}\n")
    f.write(f"Decision: {decision}\n")
    f.write("-" * 40 + "\n")
