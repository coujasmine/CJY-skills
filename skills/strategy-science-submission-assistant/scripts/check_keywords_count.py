#!/usr/bin/env python3
"""Check whether a Strategy Science keyword list meets official limits.

Official Strategy Science submission guidance requests 3-10 keywords.

Usage:
  python scripts/check_keywords_count.py "artificial intelligence; large language models; mental representations"
  cat keywords.txt | python scripts/check_keywords_count.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


MIN_KEYWORDS = 3
MAX_KEYWORDS = 10


def read_text() -> str:
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        try:
            if len(arg) < 1000 and Path(arg).exists():
                return Path(arg).read_text(encoding="utf-8")
        except (OSError, ValueError):
            pass
        return " ".join(sys.argv[1:])
    return sys.stdin.read()


def split_keywords(text: str) -> list[str]:
    # Common separators: semicolon, comma, newline, full-width semicolon/comma, bullets.
    pieces = re.split(r";|,|\n|；|，|•|·", text)
    return [piece.strip() for piece in pieces if piece.strip()]


def main() -> int:
    keywords = split_keywords(read_text())
    count = len(keywords)

    if count < MIN_KEYWORDS:
        status = "FAIL"
        message = (
            f"Keyword count is {count}; official SS range is "
            f"{MIN_KEYWORDS}-{MAX_KEYWORDS}. Add at least {MIN_KEYWORDS - count} keyword(s)."
        )
        rc = 1
    elif count <= MAX_KEYWORDS:
        status = "PASS"
        message = f"Keyword count is {count}; official SS range is {MIN_KEYWORDS}-{MAX_KEYWORDS}."
        rc = 0
    else:
        status = "FAIL"
        message = (
            f"Keyword count is {count}; official SS range is "
            f"{MIN_KEYWORDS}-{MAX_KEYWORDS}. Trim by at least {count - MAX_KEYWORDS} keyword(s)."
        )
        rc = 1

    print(f"{status}: {message}")
    if keywords:
        print()
        print("Keywords detected:")
        for i, keyword in enumerate(keywords, start=1):
            print(f"  {i}. {keyword}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
