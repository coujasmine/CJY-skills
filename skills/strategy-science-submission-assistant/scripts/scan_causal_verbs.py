#!/usr/bin/env python3
"""Scan manuscript text for strong causal verbs that may need claim calibration.

For Strategy Science, causal verbs are appropriate ONLY when the design supports
them (experiment, RCT, IV, DiD, RDD). Cross-sectional and panel-FE designs require
softer language. Pure-theory papers should not use empirical causal verbs at all.

Usage:
  python scripts/scan_causal_verbs.py manuscript.txt
  cat manuscript.txt | python scripts/scan_causal_verbs.py

See references/ss_claim_evidence_matrix.md for calibration rules.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


CAUSAL_PATTERNS = [
    # Strong causal verbs (always check design)
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
    # Empirical verbs that are inappropriate in pure-theory papers
    "we find",
    "we found",
    "our results show",
    "our findings show",
    "the results indicate",
    "the data show",
    "empirically demonstrate",
    "empirically show",
    # Anthropomorphizing LLM/ML
    "the llm understands",
    "the llm understood",
    "the model knows",
    "the model knew",
    "the algorithm decides",
    "the algorithm decided",
    "the ai understands",
    "the ai understood",
]


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


def line_matches(line: str) -> list[str]:
    hits: list[str] = []
    lowered = line.lower()
    for pattern in CAUSAL_PATTERNS:
        # Use word-boundary search; for multi-word patterns, just check substring
        if " " in pattern:
            if pattern in lowered:
                hits.append(pattern)
        else:
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
        print("PASS: no strong causal or anthropomorphizing verbs found.")
        return 0

    print(f"REVIEW: found {len(findings)} line(s) with causal-language candidates.")
    print("Calibrate against the design using references/ss_claim_evidence_matrix.md.")
    print()
    print("Reminders:")
    print("  - Cross-sectional / panel-FE designs: use 'is associated with' / 'predicts'")
    print("  - DiD / IV / RDD / RCT: causal verbs OK when identification is defended")
    print("  - Pure-theory papers: avoid 'we find' / 'our results show'; use 'we propose' / 'the framework predicts'")
    print("  - LLM/ML: avoid anthropomorphizing ('the LLM understood'); use 'the LLM produced' / 'the model predicted'")
    print()
    for idx, hits, line in findings:
        excerpt = line if len(line) <= 200 else line[:200] + "…"
        print(f"  Line {idx}: [{', '.join(hits)}] :: {excerpt}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
