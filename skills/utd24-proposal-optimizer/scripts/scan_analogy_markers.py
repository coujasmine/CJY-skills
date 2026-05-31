#!/usr/bin/env python3
"""Scan a manuscript for analogy markers that may substitute for mechanism.

Locates candidates; does not decide. The reference file
utd24_mechanism_audit.md (Dim 3.4) decides whether each hit is illustration
(fine) or substitute (DESK-REJECT-LEVEL).

Usage:
    python3 scan_analogy_markers.py <file>
    cat draft.txt | python3 scan_analogy_markers.py -
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ANALOGY_MARKERS = [
    r"\bsimilar to\b",
    r"\bsimilarly\b",
    r"\bakin to\b",
    r"\bas in\b",
    r"\bparallel(?:s|ing)?\b",
    r"\bmirror(?:s|ing)?\b",
    r"\banalogous to\b",
    r"\banalogy\b",
    r"\bby extension from\b",
    r"\bin the same vein\b",
    r"\bin the spirit of\b",
    r"\bechoes?\b",
    r"\bresembl(?:es|ing)\b",
    r"\bjust as\b",
    r"\blike\s+(?:in\b|the\b|those\b)",
]

PATTERN = re.compile("|".join(ANALOGY_MARKERS), re.IGNORECASE)


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8", errors="replace")


def extract_sentence(line: str, offset: int) -> str:
    start = max(line.rfind(".", 0, offset), line.rfind("?", 0, offset), line.rfind("!", 0, offset))
    start = start + 1 if start != -1 else 0
    end_candidates = [
        line.find(".", offset),
        line.find("?", offset),
        line.find("!", offset),
    ]
    end_candidates = [e for e in end_candidates if e != -1]
    end = min(end_candidates) + 1 if end_candidates else len(line)
    return line[start:end].strip()


def scan(text: str) -> list[tuple[int, int, str, str]]:
    hits: list[tuple[int, int, str, str]] = []
    lines = text.splitlines()
    for line_no, line in enumerate(lines, start=1):
        for match in PATTERN.finditer(line):
            sentence = extract_sentence(line, match.start())
            hits.append((line_no, match.start(), match.group(0), sentence))
    return hits


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: scan_analogy_markers.py <file|->", file=sys.stderr)
        return 2
    text = read_text(argv[1])
    hits = scan(text)
    if not hits:
        print("[OK] No analogy markers found.")
        return 0
    print(f"[FLAG] {len(hits)} analogy marker(s) found. For each, ask: would the mechanism survive if the analogy were removed? See utd24_mechanism_audit.md Dim 3.4.")
    print()
    for line_no, offset, phrase, sentence in hits:
        print(f"  L{line_no}:{offset}  \"{phrase}\"  ->  {sentence}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
