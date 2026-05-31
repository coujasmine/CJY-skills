#!/usr/bin/env python3
"""Scan a manuscript for strong causal verbs that may overshoot the design.

Locates candidates; does not decide. The reference file
utd24_methods_identification.md (Dim 5.1 table) decides whether each instance
is overclaim or correctly licensed by identification.

Usage:
    python3 scan_causal_overclaim.py <file>
    cat draft.txt | python3 scan_causal_overclaim.py -
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CAUSAL_VERBS = [
    r"\bcause(?:s|d)?\b",
    r"\blead(?:s|ing)? to\b",
    r"\bproduce(?:s|d)?\b",
    r"\bdrive(?:s|n)?\b",
    r"\bdetermine(?:s|d)?\b",
    r"\bresult(?:s|ed)? in\b",
    r"\bgenerate(?:s|d)?\b",
    r"\binduce(?:s|d)?\b",
    r"\btrigger(?:s|ed)?\b",
    r"\bbring(?:s)? about\b",
    r"\bgive(?:s)? rise to\b",
    r"\bmake(?:s)? .* (?:more|less)\b",
    r"\bforce(?:s|d)?\b",
    r"\bcompel(?:s|led)?\b",
]

PATTERN = re.compile("|".join(CAUSAL_VERBS), re.IGNORECASE)


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8", errors="replace")


def scan(text: str) -> list[tuple[int, int, str, str]]:
    """Return (line_no, char_offset, matched_phrase, sentence_context)."""
    hits: list[tuple[int, int, str, str]] = []
    lines = text.splitlines()
    for line_no, line in enumerate(lines, start=1):
        for match in PATTERN.finditer(line):
            sentence = extract_sentence(line, match.start())
            hits.append((line_no, match.start(), match.group(0), sentence))
    return hits


def extract_sentence(line: str, offset: int) -> str:
    """Return the sentence around the match offset."""
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


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: scan_causal_overclaim.py <file|->", file=sys.stderr)
        return 2
    text = read_text(argv[1])
    hits = scan(text)
    if not hits:
        print("[OK] No causal-verb candidates found. Verify identification still matches if causal claims are implicit.")
        return 0
    print(f"[FLAG] {len(hits)} causal-verb candidate(s) found. Calibrate each against utd24_methods_identification.md Dim 5.1 table.")
    print()
    for line_no, offset, phrase, sentence in hits:
        print(f"  L{line_no}:{offset}  \"{phrase}\"  ->  {sentence}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
