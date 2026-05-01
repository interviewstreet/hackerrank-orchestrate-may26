"""
Run once:  python -m utils.loader
Reads all .md files under data/, chunks, embeds, and upserts into local embeddings store.
Safe to re-run (upsert is idempotent).
"""

import os
import glob
import frontmatter
from tqdm import tqdm

from config import DATA_DIR, LOCAL_STORE_DIR, CHUNK_SIZE, CHUNK_OVERLAP
from utils.chunker import chunk_text
from utils.embeddings import embed_batch
from utils.local_store import LocalStore


DOMAIN_MAP = {
    "claude":      "claude",
    "hackerrank":  "hackerrank",
    "visa":        "visa",
}


def get_client():
    """Get or create local embeddings store."""
    return LocalStore(LOCAL_STORE_DIR)


def ingest():
    client = get_client()

    for domain_dir, domain in DOMAIN_MAP.items():
        pattern = os.path.join(DATA_DIR, domain_dir, "**", "*.md")
        files   = glob.glob(pattern, recursive=True)

        if not files:
            print(f"[loader] WARNING: no files found for domain '{domain}' at {pattern}")
            continue

        collection = client.get_or_create_collection(name=domain)

        print(f"[loader] Ingesting {len(files)} files → collection '{domain}'")

        for filepath in tqdm(files, desc=domain):
            try:
                post = frontmatter.load(filepath)
            except Exception as e:
                print(f"[loader] SKIP {filepath}: {e}")
                continue

            meta         = post.metadata
            body         = post.content
            parts        = filepath.replace("\\", "/").split("/")

            # parts: [..., "data", "claude", "claude-code", "article.md"]
            data_idx     = next((i for i, p in enumerate(parts) if p == "data"), None)
            product_area = parts[data_idx + 2] if data_idx and len(parts) > data_idx + 2 else "general"
            article_id   = str(meta.get("article_id", os.path.splitext(os.path.basename(filepath))[0]))
            source_url   = meta.get("source_url", "")
            title        = meta.get("title", "")

            chunks = chunk_text(body, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)
            if not chunks:
                continue

            texts     = [c["text"] for c in chunks]
            headings  = [c["heading"] for c in chunks]
            embeddings = embed_batch(texts)

            ids       = [f"{article_id}__{i}" for i in range(len(chunks))]
            metadatas = [
                {
                    "domain":       domain,
                    "product_area": product_area,
                    "source_url":   source_url,
                    "title":        title,
                    "article_id":   article_id,
                    "heading":      headings[i],
                }
                for i in range(len(chunks))
            ]

            collection.upsert(ids=ids, documents=texts, embeddings=embeddings, metadatas=metadatas)

    print("[loader] Ingestion complete.")


if __name__ == "__main__":
    ingest()