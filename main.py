#!/usr/bin/env python3
"""Worst Superpower entry.

Writes exactly one line to entry.txt: a single invented superpower so
useless that naming it is the whole joke. Deterministic, stdlib only,
no network.
"""

import hashlib
import os
from pathlib import Path

LINE = "I can read minds \u2014 but only the minds of pigeons, and only when they're thinking about breadcrumbs."

MAX_CHARS = 140


def validate(line: str) -> None:
    """Enforce: non-empty, exactly one line, at most 140 characters."""
    if not line:
        raise ValueError("line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, over the {MAX_CHARS} limit")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    out_path = Path(out_dir) / "entry.txt"
    data = (LINE + "\n").encode("utf-8")
    out_path.write_bytes(data)
    print(f"bytes written: {len(data)}")
    print(f"line: {LINE}")
    print(f"characters: {len(LINE)}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
