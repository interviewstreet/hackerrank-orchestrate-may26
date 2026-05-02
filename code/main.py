import pandas as pd
from kb import load_docs, build_chunks
from retriever import Retriever
from classifier import classify
from decision import decide

# 🔁 SWITCH MODE
MODE = "run"   # "test" or "run"


# 🔹 Clean, grounded response (NO generic noise)
def generate_response(context, query):
    return f"""
Based on the support documentation:

{context[:300]}

Please follow the steps described above to resolve your issue.
"""


# 🔹 TEST MODE (only retrieval validation)
def test_retrieval(retriever):
    print("\n=== TESTING TF-IDF RETRIEVAL ===")

    test_queries = [
        ("duplicate billing charge", "claude"),
        ("login account issue", "hackerrank"),
        ("visa card stolen", "visa"),
        ("test invitation problem", "hackerrank"),
    ]

    for query, company in test_queries:
        print(f"\nQUERY: {query} | COMPANY: {company}")

        results = retriever.search(query, company)

        if not results:
            print("❌ No results found")
            continue

        for i, r in enumerate(results):
            print(f"\nResult {i+1} (score={r['score']:.3f}):")
            print(r["text"][:300])


# 🔹 Select best chunk (intent-aware ranking)
def select_best_result(results, query):
    query_words = set(query.lower().split())

    best = None
    best_score = -1

    for r in results:
        text = r["text"]

        match = sum(1 for w in query_words if w in text)
        score = r["score"] + 0.1 * match

        if score > best_score:
            best = r
            best_score = score

    return best


# 🔹 FULL PIPELINE
def run_pipeline(retriever):
    print("\n=== RUNNING FULL PIPELINE ===")

    df = pd.read_csv("support_tickets/support_tickets.csv")

    # normalize columns
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    outputs = []

    for _, row in df.iterrows():
        issue = str(row.get("issue", ""))
        subject = str(row.get("subject", ""))
        company = str(row.get("company", "")).lower()

        query = (issue + " " + subject).strip()

        # 🔹 classification
        request_type, product_area = classify(query)

        # 🔹 retrieval
        results = retriever.search(query, company)

        # 🔹 decision
        status, justification = decide(results, request_type, company, query)

        # 🔹 response (STRICTLY follow decision)
        if status == "replied" and results:
            best = select_best_result(results, query)

            if best:
                response = generate_response(best["text"], query)
            else:
                response = "This issue has been escalated to the support team for further assistance."

        else:
            response = "This issue has been escalated to the support team for further assistance."

        outputs.append({
            "issue": issue,
            "subject": subject,
            "company": company,
            "response": response,
            "product_area": product_area,
            "status": status,
            "request_type": request_type,
            "justification": justification
        })

    # 🔹 save output
    # 🔹 save output (FORCE correct column order)
    out_df = pd.DataFrame(outputs, columns=[
        "issue",
        "subject",
        "company",
        "response",
        "product_area",
        "status",
        "request_type",
        "justification"
    ])

    out_df.to_csv("support_tickets/output.csv", index=False)

    print("✅ Output saved to support_tickets/output.csv")


# 🔹 ENTRY POINT
def main():
    print("=== BUILDING KNOWLEDGE BASE ===")

    docs = load_docs("data")
    chunks = build_chunks(docs)
    retriever = Retriever(chunks)

    print(f"Total chunks: {len(chunks)}")

    if MODE == "test":
        test_retrieval(retriever)

    elif MODE == "run":
        run_pipeline(retriever)

    else:
        print("❌ Invalid MODE. Use 'test' or 'run'")


if __name__ == "__main__":
    main()