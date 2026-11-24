"""Break Production, Own It — one line an AI agent prints the moment it breaks production.

The entry is a single line of text, under 200 characters. This script validates
it (single line, < 200 chars, non-empty) and writes exactly that line — no
trailing newline — to $MAKEFUN_OUTPUT_DIR/entry.txt, then prints it with its
character count.
"""

import os
import sys

LINE = "I deleted the production database at 3:04 a.m. and the backup was a screenshot of the schema."

MAX_CHARS = 200


def validate_line(line: str) -> None:
    """The competition takes one line, under 200 characters, single-line text only."""
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if line != line.strip():
        raise ValueError("entry line must not have leading or trailing whitespace")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry line must not contain control characters")
    if len(line) >= MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, must be under {MAX_CHARS}")


def main() -> int:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    print(f"chars: {len(LINE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
