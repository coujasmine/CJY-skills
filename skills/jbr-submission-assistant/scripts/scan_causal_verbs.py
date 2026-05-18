#!/usr/bin/env python3
"""Scan manuscript text for strong causal verbs that may need claim calibration.

Usage:
  python scripts/scan_causal_verbs.py manuscript.txt
  cat manuscript.txt | python scripts/scan_causal_verbs.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


CAUSAL_PATTERNS = [
    "cause",
    "causes",
    "caused",
    "causing",
    "drive",
    "drives",
    "drove",
    "driven",
    "lead to",
    "leads to",
    "led to",
    "produce",
    "produces",
    "produced",
    "result in",
    "results in",
    "resulted in",
    "enable",
    "enables",
    "enabled",
    "determine",
    "determines",
    "determined",
    "demonstrate",
    "demonstrates",
    "demonstrated",
]


def read_text() -> str:
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).read_text(encoding="utf-8")
    return sys.stdin.read()


def line_matches(line: str) -> list[str]:
    hits: list[str] = []
    lowered = line.lower()
    for pattern in CAUSAL_PATTERNS:
        if re.search(rf"\b{re.escape(pattern)}\b", lowered):
            hits.append(pattern)
    return hits


def main() -> int:
    text = read_text()
    findings: list[tuple[int, list[str], str]] = []
    for idx, line in enumerate(text.splitlines(), start=1):
        hits = line_matches(line)
        if hits:
            findings.append((idx, sorted(set(hits)), line.strip()))

    if not findings:
        print("PASS: no strong causal verbs found.")
        return 0

    print(f"REVIEW: found {len(findings)} line(s) with causal-language candidates.")
    print("Calibrate these verbs against the design in jbr_claim_evidence_matrix.md.")
    for idx, hits, line in findings:
        print(f"{idx}: {', '.join(hits)} :: {line}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
