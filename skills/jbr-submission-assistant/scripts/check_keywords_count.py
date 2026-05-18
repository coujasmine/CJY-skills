#!/usr/bin/env python3
"""Check whether a JBR keyword list contains 4 to 6 keywords.

Usage:
  python scripts/check_keywords_count.py "AI capability; managerial myopia; TMT attention; JBR"
  cat keywords.txt | python scripts/check_keywords_count.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


MIN_KEYWORDS = 4
MAX_KEYWORDS = 6


def read_text() -> str:
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        return Path(sys.argv[1]).read_text(encoding="utf-8")
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    return sys.stdin.read()


def split_keywords(text: str) -> list[str]:
    pieces = re.split(r";|,|\n|\uFF1B|\uFF0C", text)
    return [piece.strip() for piece in pieces if piece.strip()]


def main() -> int:
    keywords = split_keywords(read_text())
    count = len(keywords)
    status = "PASS" if MIN_KEYWORDS <= count <= MAX_KEYWORDS else "FAIL"
    print(f"{status}: keyword count = {count}; JBR expects {MIN_KEYWORDS}-{MAX_KEYWORDS}.")
    if keywords:
        print("Keywords:")
        for keyword in keywords:
            print(f"- {keyword}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
