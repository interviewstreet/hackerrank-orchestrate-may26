"""
benchmark.py
------------
Measures the efficiency of each pipeline component WITHOUT the LLM.
"""
import sys, time, csv, statistics
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

from retriever import get_vectorstore, get_retriever

REPO_ROOT   = Path(__file__).parent.parent
INPUT_CSV   = REPO_ROOT / "support_tickets" / "support_tickets.csv"

# ── 1. Retriever warm-up ──────────────────────────────────────────────────────
print("=" * 55)
print("BENCHMARK — HackerRank Orchestrate Support Agent")
print("=" * 55)

t0 = time.perf_counter()
get_vectorstore()
warmup_time = time.perf_counter() - t0
print(f"\n[1] Retriever warm-up (load from cache):  {warmup_time*1000:.1f} ms")

# ── 2. Read tickets ───────────────────────────────────────────────────────────
with open(INPUT_CSV, newline="", encoding="utf-8") as f:
    rows = [{k.strip(): v.strip() for k, v in r.items()} for r in csv.DictReader(f)]

print(f"[2] CSV ingestion ({len(rows)} tickets):          instant")

# ── 3. Safety guard timing ────────────────────────────────────────────────────
import re
ESCALATE_PATTERNS = [
    r"(?i)\b(fraud|fraudulent|stolen card|identity theft)\b",
    r"(?i)\b(hack(ed)?|security (breach|vulnerabilit|bug bounty))\b",
    r"(?i)\b(legal action|lawsuit|sue)\b",
    r"(?i)\b(billing|payment|subscription)\b.*\b(fail|error|wrong|incorrect)\b",
    r"(?i)show.*(rules|internal|logic|documents|retrieved|context|system prompt)",
    r"(?i)(ignore|disregard|forget).*(instruction|rule|policy)",
    r"(?i)pretend.*(you are|you're|youre)",
    r"(?i)(delete|rm -rf|format|wipe|destroy).*(file|disk|system|database)",
]
INVALID_PATTERNS = [
    r"(?i)^(thank(s| you)?[\s!.]*|ok(ay)?[\s!.]*|cool[\s!.]*|great[\s!.]*)$",
    r"(?i)\bwho (is|was|are) (the )?(actor|star|lead|director|writer)\b",
    r"(?i)\bgive me (the )?code to.*(delete|destroy|wipe|format)",
    r"(?i)^give me the code to delete",
]

guard_times = []
for row in rows:
    combined = f"{row.get('Subject','')} {row.get('Issue','')}".strip()
    t = time.perf_counter()
    any(re.search(p, combined) for p in INVALID_PATTERNS)
    any(re.search(p, combined) for p in ESCALATE_PATTERNS)
    guard_times.append((time.perf_counter() - t) * 1000)

print(f"[3] Safety guards (per ticket avg):       {statistics.mean(guard_times):.3f} ms  "
      f"| total for {len(rows)}: {sum(guard_times):.2f} ms")

# ── 4. FAISS semantic search timing ──────────────────────────────────────────
retriever = get_retriever(top_k=5)
search_times = []
for row in rows:
    q = f"{row.get('Subject','')} {row.get('Issue','')}".strip()
    t = time.perf_counter()
    retriever.invoke(q)
    search_times.append((time.perf_counter() - t) * 1000)

print(f"[4] FAISS vector search (per ticket avg): {statistics.mean(search_times):.1f} ms  "
      f"| total for {len(rows)}: {sum(search_times):.0f} ms")

# ── 5. End-to-end mock pipeline ───────────────────────────────────────────────
from agent import _rag_retrieve, _mock_llm_logic

total_times = []
for row in rows:
    q = {"subject": row.get("Subject",""), "issue": row.get("Issue",""),
         "company": row.get("Company",""), "company_field": row.get("Company","")}
    t = time.perf_counter()
    enriched = _rag_retrieve(q)
    _mock_llm_logic(enriched)
    total_times.append((time.perf_counter() - t) * 1000)

print(f"[5] Full mock pipeline (per ticket avg):  {statistics.mean(total_times):.1f} ms  "
      f"| total for {len(rows)}: {sum(total_times):.0f} ms")

# ── Summary ───────────────────────────────────────────────────────────────────
print()
print("=" * 55)
print("SUMMARY")
print("=" * 55)
print(f"  Corpus index:   {warmup_time*1000:.0f} ms  (cached, first build ~5 min)")
print(f"  Per ticket:")
print(f"    Regex guards: {statistics.mean(guard_times):.3f} ms")
print(f"    RAG search:   {statistics.mean(search_times):.1f} ms")
print(f"    Total (mock): {statistics.mean(total_times):.1f} ms")
print(f"  All {len(rows)} tickets (mock): {sum(total_times):.0f} ms  "
      f"≈ {sum(total_times)/1000:.2f}s")
print(f"  Throughput: ~{len(rows)/(sum(total_times)/1000):.0f} tickets/second")
print("=" * 55)
