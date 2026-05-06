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
            "title": post.metadata.get("title", Path(filename).stem),
            "body": post.content,
            "id": filename
            }

# walk over all the data folders - recursively to find the .md files
def walk_data_files(folder_name: str) -> list[Data]:
    path = Path(folder_name)
    if not path.exists():
        raise FileNotFoundError(f"data folder does not exist {folder_name}")
    data_files = list(path.rglob("*.md"))      
    data = []
    for df in data_files:
        d = open_data_file(str(df))
        data.append(d)
    return data

# open ticket files (.csv)
def open_ticket_file(filename: str) -> list[Query]:
    if not Path(filename).exists():
        raise FileNotFoundError(f"file does not exist {filename}")
    
    queries = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            company = row.get("comapny", "none").lower()
            if company not in ("hackerrank", "claude", "visa", "none"):
                raise ValueError(f"Unknown company: {row.get('company', 'none')}")

            query = {
                    "issue": row.get("issue", "none"),
                    "company": company,
                    "subject": row.get("subject", "")
                    }
            queries.append(query)
    return queries
