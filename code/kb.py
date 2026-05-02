# import os
# import re

# def load_docs(data_path="data"):
#     docs = []
#     for company in ["claude", "visa", "hackerrank"]:
#         folder = os.path.join(data_path, company)
#         for file in os.listdir(folder):
#             if file.endswith(".md") and "index" not in file.lower():
#                 with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
#                     docs.append({
#                         "text": clean_text(f.read()),
#                         "company": company
#                     })
#     return docs


# def clean_text(text):
#     import re

#     # remove markdown links but KEEP text
#     text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)

#     # remove URLs
#     text = re.sub(r'http\S+', '', text)

#     # remove excessive symbols but keep words
#     text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

#     # normalize spaces
#     text = re.sub(r'\s+', ' ', text)

#     return text.lower()

# def chunk_text(text, size=150):
#     words = text.split()
#     return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]


# def build_chunks(docs):
#     chunks = []
#     for doc in docs:
#         parts = chunk_text(doc["text"])
#         for p in parts:
#             chunks.append({
#                 "text": p,
#                 "company": doc["company"]
#             })
#     return chunks
# +++++++++++++++++++++++++++++++++++++++++++++

import os
import re


# 🔹 Clean text (balanced, not destructive)
def clean_text(text):
    # keep text inside markdown links
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)

    # remove urls
    text = re.sub(r'http\S+', '', text)

    # keep words + numbers
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # normalize spaces
    text = re.sub(r'\s+', ' ', text)

    return text.lower()


# 🔹 Load all docs (DON'T over-filter)
def load_docs(data_path="data"):
    docs = []

    for company in ["claude", "visa", "hackerrank"]:
        folder = os.path.join(data_path, company)

        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith(".md"):
                    path = os.path.join(root, file)

                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            raw = f.read()

                            # ❗ skip extremely small useless files
                            if len(raw) < 200:
                                continue

                            cleaned = clean_text(raw)

                            docs.append({
                                "text": cleaned,
                                "company": company.lower(),
                                "source": path
                            })

                    except Exception as e:
                        print(f"Error reading {path}: {e}")

    return docs


# 🔹 Smart chunking (important)
def chunk_text(text, size=120, overlap=30):
    words = text.split()

    chunks = []
    for i in range(0, len(words), size - overlap):
        chunk = words[i:i + size]
        if len(chunk) > 40:  # avoid tiny chunks
            chunks.append(" ".join(chunk))

    return chunks


# 🔹 Build chunks with metadata
def build_chunks(docs):
    chunks = []

    for doc in docs:
        parts = chunk_text(doc["text"])

        for p in parts:
            chunks.append({
                "text": p,
                "company": doc["company"],
                "source": doc["source"]
            })

    return chunks