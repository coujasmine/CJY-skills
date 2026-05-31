#!/usr/bin/env python3
"""Check whether a Strategy Science abstract meets official limits.

Official Strategy Science submission guidance distinguishes two limits:
- Manuscript abstract: no more than 200 words.
- ScholarOne metadata abstract field: no more than 250 words.

Usage:
  python scripts/check_abstract_word_count.py abstract.txt
  cat abstract.txt | python scripts/check_abstract_word_count.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


QUALITY_FLOOR = 100
MANUSCRIPT_CEILING = 200
PORTAL_CEILING = 250


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


def count_words(text: str) -> int:
    # Counts English-like words and hyphenated compounds as one token.
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def main() -> int:
    text = read_text().strip()
    words = count_words(text)

    if words == 0:
        status = "FAIL"
        message = "No abstract text detected."
        rc = 1
    elif words > PORTAL_CEILING:
        status = "FAIL"
        delta = words - PORTAL_CEILING
        message = (
            f"Abstract is too long ({words} words). It exceeds the ScholarOne "
            f"metadata limit of {PORTAL_CEILING} words by {delta} words and also "
            f"exceeds the manuscript limit of {MANUSCRIPT_CEILING} words."
        )
        rc = 1
    elif words > MANUSCRIPT_CEILING:
        status = "WARN"
        delta = words - MANUSCRIPT_CEILING
        message = (
            f"Abstract is {words} words. This fits the ScholarOne metadata field "
            f"(<= {PORTAL_CEILING}) but exceeds the manuscript abstract limit "
            f"(<= {MANUSCRIPT_CEILING}) by {delta} words."
        )
        rc = 1
    elif words < QUALITY_FLOOR:
        status = "WARN"
        message = (
            f"Abstract is short ({words} words). SS has no official minimum, "
            f"but under {QUALITY_FLOOR} words often leaves too little room for "
            "the research question, design, findings, and contribution."
        )
        rc = 1
    else:
        status = "PASS"
        message = (
            f"Abstract is within official SS manuscript limit ({words} words; "
            f"manuscript <= {MANUSCRIPT_CEILING}, ScholarOne <= {PORTAL_CEILING})."
        )
        rc = 0

    print(f"{status}: {message}")
    print()
    print(
        f"  Quality floor:      {QUALITY_FLOOR} words "
        f"({'OK' if words >= QUALITY_FLOOR else 'BELOW'})"
    )
    print(
        f"  Manuscript ceiling: {MANUSCRIPT_CEILING} words "
        f"({'OK' if words <= MANUSCRIPT_CEILING else 'ABOVE'})"
    )
    print(
        f"  ScholarOne ceiling: {PORTAL_CEILING} words "
        f"({'OK' if words <= PORTAL_CEILING else 'ABOVE'})"
    )
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
