"""
Index builder — chunks all corpus docs and stores embeddings in Qdrant.

Usage:
    python build_index.py    (from inside code/)
    python code/build_index.py  (from repo root)

Must be run once before agent.py. Safe to re-run (recreates the collection).

Data root resolution order:
  1. <repo_root>/data/  (parent of the code/ directory)
  2. DATA_PATH environment variable
"""

import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv
load_dotenv()

from retriever import build_index

_CODE_DIR = Path(__file__).parent


def _resolve_data_root() -> Path | None:
    # 1. Check the parent directory of code/ (repo root's data/)
    candidate = _CODE_DIR.parent / "data"
    if candidate.exists() and any(candidate.rglob("*.md")):
        return candidate

    if candidate.exists():
        print(
            f"WARNING: data directory found at {candidate} but contains no .md files.",
            file=sys.stderr,
        )

    # 2. Fall back to DATA_PATH env var
    env_path = os.environ.get("DATA_PATH", "").strip()
    if env_path:
        p = Path(env_path)
        if not p.exists():
            print(
                f"ERROR: DATA_PATH={env_path!r} does not exist.\n"
                "Please update DATA_PATH in your .env file and re-run.",
                file=sys.stderr,
            )
            return None
        if not any(p.rglob("*.md")):
            print(
                f"ERROR: DATA_PATH={env_path!r} contains no .md files.\n"
                "Please point DATA_PATH to a directory with markdown corpus files and re-run.",
                file=sys.stderr,
            )
            return None
        return p

    # 3. Neither location has data
    print(
        f"ERROR: No corpus data found.\n"
        f"  Checked:  {candidate}\n"
        f"  Fix:      Set DATA_PATH=/path/to/your/data in .env and re-run.",
        file=sys.stderr,
    )
    return None


def main() -> None:
    data_root = _resolve_data_root()
    if data_root is None:
        sys.exit(1)

    print(f"Building Qdrant index from {data_root} ...")
    t0 = time.time()
    count = build_index(data_root=data_root)
    elapsed = time.time() - t0
    print(f"Indexed {count} chunks in {elapsed:.1f}s.")
    print("Index ready. You can now run: python agent.py")


if __name__ == "__main__":
    main()
