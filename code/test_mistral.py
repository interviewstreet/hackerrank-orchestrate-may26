"""
test_mistral.py  — quick smoke test for Ollama Mistral integration
Run from repo root:  .\\venv\\Scripts\\python.exe code\\test_mistral.py
"""
import os
import sys
import time

# ── setup path ────────────────────────────────────────────────────────────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

print("=" * 60)
print("OLLAMA_MODEL =", os.getenv("OLLAMA_MODEL"))
print("=" * 60)

# ── 1. Direct Mistral ping ────────────────────────────────────────────────────
from langchain_ollama import ChatOllama

llm = ChatOllama(model="mistral", temperature=0, format="json")
print("\n[1] Sending direct ping to Mistral (JSON mode)...")
t0 = time.time()
resp = llm.invoke('Reply with valid JSON containing key "ok" set to true.')
elapsed = time.time() - t0
print(f"    [OK] Response in {elapsed:.1f}s")
print(f"    Content: {resp.content[:200]}")

# -- 2. Full RAG pipeline with a sample ticket ---------------------------------
print("\n[2] Running full RAG pipeline with a sample ticket...")
from agent import process_ticket

t1 = time.time()
result = process_ticket(
    issue="I cannot log into my HackerRank account. The password reset email never arrives.",
    subject="Login issue - password reset not working",
    company_field="HackerRank",
)
elapsed2 = time.time() - t1

print(f"    [OK] Ticket processed in {elapsed2:.1f}s")
print(f"    status       : {result.status}")
print(f"    product_area : {result.product_area}")
print(f"    request_type : {result.request_type}")
print(f"    response     : {result.response[:150]}")
print(f"    justification: {result.justification[:150]}")
print("\n[PASS] Mistral integration is working correctly.")
