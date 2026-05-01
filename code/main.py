import csv
from classifier import classify
from retriever import Retriever
from decision import should_escalate
from generator import generate_response
from logger import log_entry

# Load docs (replace with actual corpus loading)
docs = open("data/docs.txt").read().split("\n\n")

retriever = Retriever(docs)

with open("support_issues.csv") as f:
    reader = csv.DictReader(f)
    tickets = list(reader)

output = []
log_file = open("log.txt", "w")

for t in tickets:
    text = t["ticket"]

    product, req = classify(text)

    results = retriever.search(text)
    doc, score = results[0]

    if should_escalate(req, score):
        decision = "escalate"
        response = "This issue requires human support."
    else:
        decision = "respond"
        response = generate_response(doc)

    log_entry(log_file, text, product, req, score, decision)

    output.append({
        "ticket": text,
        "product": product,
        "type": req,
        "decision": decision,
        "response": response
    })

# write CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=output[0].keys())
    writer.writeheader()
    writer.writerows(output)

log_file.close()
