import os
import json
from datetime import datetime
from pathlib import Path

# ✅ REQUIRED LOCATION
LOG_FILE = str(Path.home() / "hackerrank_orchestrate" / "log.txt")

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)


# ---------- INTERNAL WRITE ----------
def _write(entry: dict):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ---------- 1. RUNTIME LOGS (YOUR CURRENT SYSTEM) ----------

def log_ticket_start(ticket_id, ticket: dict):
    _write({
        "type": "runtime",
        "event": "ticket_start",
        "ticket_id": ticket_id,
        "ts": datetime.utcnow().isoformat(),
        "input": ticket,
    })


def log_agent(ticket_id, agent: str, decision: str, detail: dict = None):
    _write({
        "type": "runtime",
        "event": "agent",
        "ticket_id": ticket_id,
        "agent": agent,
        "decision": decision,
        "detail": detail or {},
        "ts": datetime.utcnow().isoformat(),
    })


def log_llm_call(ticket_id, prompt: str, raw_response: str, parsed: dict):
    _write({
        "type": "runtime",
        "event": "llm_call",
        "ticket_id": ticket_id,
        "prompt_snippet": prompt[:300],
        "raw_response": raw_response[:300],
        "parsed": parsed,
        "ts": datetime.utcnow().isoformat(),
    })


def log_ticket_end(ticket_id, output: dict):
    _write({
        "type": "runtime",
        "event": "ticket_end",
        "ticket_id": ticket_id,
        "output": output,
        "ts": datetime.utcnow().isoformat(),
    })


# ---------- 2. DECISION LOGS (REQUIRED FOR SCORING) ----------

def log_decision(title: str, user_prompt: str, summary: str, actions: str = ""):
    entry = {
        "type": "decision",
        "ts": datetime.utcnow().isoformat(),
        "title": title,
        "user_prompt": user_prompt,
        "summary": summary,
        "actions": actions
    }
    _write(entry)