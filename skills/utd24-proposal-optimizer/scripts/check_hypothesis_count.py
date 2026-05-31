#!/usr/bin/env python3
"""Count explicit hypothesis labels (H1, H2, H1a, H2b, etc.) and flag scope creep.

UTD24 norm: 3-5 hypotheses (4 modal). 6-7 = scope creep visible. 8+ = usually
two papers stitched into one. <3 = usually under-developed.

The script counts unique hypothesis labels found at sentence starts or as bold/
italic markup. It does not decide whether each is independently motivated —
the reference file utd24_hypothesis_architecture.md (Dim 4.2) does.

Usage:
    python3 check_hypothesis_count.py <file>
    cat draft.txt | python3 check_hypothesis_count.py -
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Match H1, H1a, H1.1, Hypothesis 1, Hypothesis 1a, etc.
LABEL_PATTERNS = [
    r"\bH(\d+[a-z]?(?:\.\d+)?)\b",
    r"\bHypothesis\s+(\d+[a-z]?(?:\.\d+)?)\b",
]
PATTERN = re.compile("|".join(LABEL_PATTERNS), re.IGNORECASE)


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8", errors="replace")


def find_labels(text: str) -> set[str]:
    labels: set[str] = set()
    for match in PATTERN.finditer(text):
        for group in match.groups():
            if group:
                labels.add(group.lower())
                break
    return labels


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: check_hypothesis_count.py <file|->", file=sys.stderr)
        return 2
    text = read_text(argv[1])
    labels = find_labels(text)
    count = len(labels)

    print(f"Detected hypothesis labels: {count}")
    if labels:
        print(f"  Labels: {sorted(labels)}")
    print()

    if count == 0:
        print("[WARN] No explicit hypothesis labels found. Either: (a) the paper is not testing hypotheses (qual / theory paper — verify Dim 4 is applicable), or (b) hypotheses are buried in prose. Per UTD24 norm, hypotheses should be explicitly numbered.")
    elif count < 3:
        print(f"[FLAG] {count} hypothesis label(s). UTD24 norm is 3-5. <3 typically indicates under-development. Consider whether the theory generates more commitments.")
    elif count <= 5:
        print(f"[OK] {count} hypothesis label(s). Within UTD24 norm (3-5).")
    elif count <= 7:
        print(f"[FLAG] {count} hypothesis label(s). Scope creep visible. Check whether redundant operationalizations of the same mechanism can be consolidated. See utd24_hypothesis_architecture.md Dim 4.2.")
    else:
        print(f"[FLAG-HIGH] {count} hypothesis label(s). 8+ hypotheses usually indicate two papers stitched into one, or kitchen-sink exploration disguised as theory testing. Recommend major restructuring.")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
