#!/usr/bin/env python3
"""Extract citation-bearing sentence contexts from manuscript prose.

The output helps prepare a claim-citation alignment audit. It does not judge
whether a citation supports a claim.

Usage:
  python scripts/extract_citation_contexts.py manuscript.txt
  python scripts/extract_citation_contexts.py --json manuscript.txt
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])")
PAREN_CITATION_RE = re.compile(
    r"\((?:[^()]*?\b(?:19|20)\d{2}[a-z]?(?:\s*;\s*)?)+[^()]*?\)"
)
NARRATIVE_CITATION_RE = re.compile(
    r"\b[A-Z][A-Za-z'`-]+(?:\s+et\s+al\.)?\s+\((?:19|20)\d{2}[a-z]?\)"
)
PANDOC_CITATION_RE = re.compile(r"\[@[A-Za-z0-9_:\-]+(?:[;,]\s*@[A-Za-z0-9_:\-]+)*\]")


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def split_sentences(text: str) -> list[tuple[int, str]]:
    results: list[tuple[int, str]] = []
    char_pos = 0
    for paragraph in re.split(r"\n\s*\n", text):
        for sentence in SENTENCE_RE.split(paragraph.strip()):
            sentence = sentence.strip()
            if not sentence:
                continue
            found_at = text.find(sentence, char_pos)
            if found_at == -1:
                found_at = char_pos
            line_no = text[:found_at].count("\n") + 1
            results.append((line_no, sentence))
            char_pos = found_at + len(sentence)
    return results


def citations_in_sentence(sentence: str) -> list[str]:
    citations: list[str] = []
    for pattern in (PAREN_CITATION_RE, NARRATIVE_CITATION_RE, PANDOC_CITATION_RE):
        citations.extend(match.group(0) for match in pattern.finditer(sentence))
    return citations


def extract_contexts(text: str) -> list[dict[str, object]]:
    contexts: list[dict[str, object]] = []
    for line_no, sentence in split_sentences(text):
        citations = citations_in_sentence(sentence)
        if citations:
            contexts.append(
                {
                    "line": line_no,
                    "claim_context": sentence,
                    "citations": citations,
                    "locator_status": "UNKNOWN",
                    "alignment_status": "NOT_AUDITED",
                }
            )
    return contexts


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract citation-bearing contexts.")
    parser.add_argument("path", nargs="?", help="Manuscript file; stdin if omitted.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    contexts = extract_contexts(read_text(args.path))
    if args.json:
        print(json.dumps(contexts, indent=2, ensure_ascii=False))
        return 0

    print(f"Extracted {len(contexts)} citation context(s).")
    for item in contexts:
        print(f"- Line {item['line']}: {', '.join(item['citations'])}")
        print(f"  Claim context: {item['claim_context']}")
        print("  Locator: [LOCATOR NEEDED]")
    return 0 if contexts else 1


if __name__ == "__main__":
    raise SystemExit(main())

