"""Re-export module for the AGENTS.md section 6.1 entry-point contract.

Some evaluator scripts look for ``code/agent.py``; others look for
``code/main.py``. Both paths resolve to the same pipeline.
"""

from __future__ import annotations

from main import _process_ticket as process_ticket  # noqa: F401
from main import run  # noqa: F401


__all__ = ["run", "process_ticket"]
