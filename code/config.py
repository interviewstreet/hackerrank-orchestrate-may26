"""Configuration and secrets loading.

Loading order (Architecture section 3.2):
  1. code/config.yaml (committed defaults)
  2. environment variables (override; from .env via python-dotenv)
  3. CLI flags (final override; applied in main.py)

Secrets are read only from environment variables (NFR-004, AC-11).

PRD references: NFR-003, NFR-004, FR-041, AC-11.
Architecture references: section 3.2.
"""

from __future__ import annotations

from pathlib import Path


class Config:
    """Holds merged configuration values. Iter 1+ implements loading."""

    def __init__(self, values: dict | None = None) -> None:
        raise NotImplementedError("Iter 1: Config.__init__")


def load_config(path: Path | None = None) -> dict:
    """Load YAML defaults, overlay env vars, return a plain dict.

    Iter 1 implementation: yaml.safe_load + python-dotenv + env-var overlay.
    """
    raise NotImplementedError("Iter 1: load_config")
