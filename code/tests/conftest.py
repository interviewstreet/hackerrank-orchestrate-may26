"""Pytest configuration: put code/ on sys.path so tests can ``import loader``.

Also pins PYTHONHASHSEED=0 for determinism (NFR-001, AC-12).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("PYTHONHASHSEED", "0")

CODE_DIR = Path(__file__).resolve().parent.parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))
