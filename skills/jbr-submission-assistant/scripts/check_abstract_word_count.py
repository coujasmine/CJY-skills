#!/usr/bin/env python3
"""Check whether a JBR abstract is within the 150-word limit.

Usage:
  python scripts/check_abstract_word_count.py abstract.txt
  cat abstract.txt | python scripts/check_abstract_word_count.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


LIMIT = 150


def read_text() -> str:
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        return Path(sys.argv[1]).read_text(encoding="utf-8")
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    return sys.stdin.read()


def count_words(text: str) -> int:
    # Counts English-like words and hyphenated compounds as one token.
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def main() -> int:
    text = read_text().strip()
    words = count_words(text)
    status = "PASS" if words <= LIMIT else "FAIL"
    delta = words - LIMIT
    print(f"{status}: abstract word count = {words}; JBR limit = {LIMIT}.")
    if delta > 0:
        print(f"Reduce by at least {delta} words.")
    return 0 if words <= LIMIT else 1


if __name__ == "__main__":
    raise SystemExit(main())
