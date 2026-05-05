import frontmatter
import csv
from pathlib import Path

from embeddings.embeddings import Data, Query

# open data files (.md)
# return it's content in the correct format
def open_data_file(filename: str) -> Data:
    if not Path(filename).exists():
        raise FileNotFoundError(f"file does not exist {filename}")

    post = frontmatter.load(filename)
    return {
            "title": post.metadata["title"],
            "body": post.content,
            "id": filename
            }

# open ticket files (.csv)
def open_ticket_file(filename: str) -> list[Query]:
    if not Path(filename).exists():
        raise FileNotFoundError(f"file does not exist {filename}")
    
    queries = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            company = row["company"].lower()
            if company not in ("hackerrank", "claude", "visa", "none"):
                raise ValueError(f"Unknown company: {row['company']}")

            query = {
                    "issue": row["issue"],
                    "company": company,
                    "subject": row["subject"]
                    }
            queries.append(query)
    return queries
