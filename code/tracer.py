"""Per-run JSONL tracer.

Writes one JSON line per ticket to ``code/runs/<ISO-timestamp>/trace.jsonl``.
Distinct from the AGENTS.md log (the latter is human-conversation; this
is run-of-agent telemetry).

PRD references: NFR-005.
Architecture references: section 3.11.
"""

from __future__ import annotations

from pathlib import Path


class Tracer:
    """Append-only JSONL writer for per-ticket pipeline traces."""

    def __init__(self, out_dir: Path) -> None:
        """Open trace.jsonl under out_dir. Iter 6 implementation."""
        raise NotImplementedError("Iter 6: Tracer.__init__")

    def record(self, ticket_index: int, **kwargs) -> None:
        """Write one JSON line for the given ticket. Iter 6."""
        raise NotImplementedError("Iter 6: Tracer.record")

    def close(self) -> None:
        """Flush and close the trace file. Iter 6."""
        raise NotImplementedError("Iter 6: Tracer.close")
