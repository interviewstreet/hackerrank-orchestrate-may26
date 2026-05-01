"""Alias module for the AGENTS.md section 6.1 entry-point contract.

Some evaluator scripts look for ``code/agent.py``; others look for
``code/main.py``. Architecture section 5 specifies that ``agent.py``
re-exports ``main.run`` so either name resolves to the same pipeline.
"""

from __future__ import annotations

from main import run  # noqa: F401  re-export for entry-point compatibility


def process_ticket(*args, **kwargs):
    """Per-ticket orchestrator stub. Iter 6 implements the pipeline chain."""
    raise NotImplementedError("Iter 6: process_ticket orchestrator")
