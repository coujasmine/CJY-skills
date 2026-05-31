#!/usr/bin/env python3
"""Measure sentence-length variation in manuscript prose.

Usage:
  python scripts/check_sentence_burstiness.py manuscript.txt
  cat manuscript.txt | python scripts/check_sentence_burstiness.py

The script is diagnostic only. Low variation can signal over-smoothed AI prose,
but technical method paragraphs may naturally have low variation.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from pathlib import Path


SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])")
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?")


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def sentence_lengths(text: str) -> list[int]:
    cleaned = re.sub(r"\s+", " ", text.strip())
    if not cleaned:
        return []
    sentences = [s.strip() for s in SENTENCE_RE.split(cleaned) if s.strip()]
    lengths = [len(WORD_RE.findall(s)) for s in sentences]
    return [length for length in lengths if length > 0]


def stats_for_text(text: str) -> dict[str, float | int | str]:
    lengths = sentence_lengths(text)
    if not lengths:
        return {
            "sentence_count": 0,
            "mean_words": 0.0,
            "std_dev": 0.0,
            "coefficient_of_variation": 0.0,
            "burstiness": "UNKNOWN",
        }

    mean = statistics.mean(lengths)
    std_dev = statistics.pstdev(lengths) if len(lengths) > 1 else 0.0
    cv = std_dev / mean if mean else 0.0
    if cv < 0.28 and len(lengths) >= 6:
        burstiness = "LOW"
    elif cv < 0.45:
        burstiness = "MODERATE"
    else:
        burstiness = "HIGH"
    return {
        "sentence_count": len(lengths),
        "mean_words": round(mean, 2),
        "std_dev": round(std_dev, 2),
        "coefficient_of_variation": round(cv, 3),
        "burstiness": burstiness,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Measure sentence-length variation.")
    parser.add_argument("path", nargs="?", help="Text file to inspect; stdin if omitted.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    result = stats_for_text(read_text(args.path))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0

    print("Sentence-Length Variation")
    print(f"Sentences: {result['sentence_count']}")
    print(f"Mean words: {result['mean_words']}")
    print(f"Std dev: {result['std_dev']}")
    print(f"Coefficient of variation: {result['coefficient_of_variation']}")
    print(f"Burstiness: {result['burstiness']}")
    if result["burstiness"] == "LOW":
        print("Risk: MEDIUM - inspect for over-smoothed AI-polished prose.")
        return 1
    print("Risk: LOW")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

