#!/usr/bin/env python3
"""Scan manuscript text for AI-generated style markers (lexical + structural).

Usage:
  python scripts/scan_ai_style_markers.py manuscript.txt
  cat manuscript.txt | python scripts/scan_ai_style_markers.py

Reports flagged lines with the rule that triggered. Does not modify the text.
Pair with references/ai_style_markers.md for the full catalog and decontamination
guidance. For a context-aware rewrite, invoke the jbr-ai-decontaminator subagent.

Exit code 0 if no markers found, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


# Lexical markers: word/phrase patterns that are common AI tells in academic prose.
# Each entry is (regex_pattern, rule_label, replacement_hint).
LEXICAL_PATTERNS: list[tuple[str, str, str]] = [
    (r"\bleverage(s|d|ing)?\b", "L1.1 leverage", "use / draw on / apply (unless financial-leverage context)"),
    (r"\bdelve(s|d)?\s+into\b", "L1.1 delve into", "examine / investigate / study"),
    (r"\bdive(s|d)?\s+deep(\s+into)?\b", "L1.1 dive deep", "analyze in detail"),
    (r"\bdeep\s+dive\b", "L1.1 deep dive", "detailed analysis"),
    (r"\btapestr(y|ies)\b", "L1.1 tapestry", "combination / mix / set"),
    (r"\bpivotal\b", "L1.1 pivotal", "important / central / key (unless governance-theory term)"),
    (r"\bunderscore(s|d)?\b", "L1.1 underscore", "emphasize / highlight / show"),
    (r"\bunveil(s|ed|ing)?\b", "L1.1 unveil", "present / introduce / document"),
    (r"\belucidate(s|d)?\b", "L1.1 elucidate", "explain / clarify"),
    (r"\bintricate\b", "L1.1 intricate", "complex"),
    (r"\bmyriad\b", "L1.1 myriad", "many / several"),
    (r"\bnavigate(s|d|ing)?\b", "L1.1 navigate", "address / manage / handle (unless spatial)"),
    (r"\btestament\s+to\b", "L1.1 testament to", "evidence of"),
    (r"\bembark(s|ed|ing)?\s+(on|upon)\b", "L1.1 embark on", "begin / undertake"),
    (r"\bshed(s)?\s+light\s+on\b", "L1.1 shed light on", "clarify / explain"),
    (r"\bin\s+the\s+realm\s+of\b", "L1.1 in the realm of", "in / within"),
    (r"\bin\s+the\s+landscape\s+of\b", "L1.1 in the landscape of", "in / across"),
    (r"\bever[- ]evolving\b", "L1.1 ever-evolving", "evolving / changing"),
    (r"\bever[- ]changing\b", "L1.1 ever-changing", "evolving / changing"),
    (r"\bparadigm\s+shift\b", "L1.1 paradigm shift", "change / shift (unless one is documented)"),
    (r"\bholistic\b", "L1.1 holistic", "integrated / comprehensive — or delete"),
    (r"\bnuanced\b", "L1.1 nuanced", "qualified / conditional — or specify the nuance"),
    (r"\bseamless(ly)?\b", "L1.1 seamlessly", "smoothly — or delete"),
    (r"\bcompelling\b", "L1.1 compelling", "strong / convincing — or delete"),
    (r"\bIt\s+is\s+important\s+to\s+note\s+that\b", "L1.2 filler-opener", "delete and state the point directly"),
    (r"\bIt\s+is\s+worth\s+noting\s+that\b", "L1.2 filler-opener", "delete and state the point directly"),
    (r"\bIt\s+should\s+be\s+noted\s+that\b", "L1.2 filler-opener", "delete and state the point directly"),
    (r"\bIt\s+is\s+crucial\s+to\s+recognize\s+that\b", "L1.2 filler-opener", "delete and state the point directly"),
    (r"\bIn\s+recent\s+years,\s+there\s+has\s+been\s+growing\s+interest\s+in\b", "L1.2 filler-opener", "replace with the concrete phenomenon"),
    (r"\bIn\s+today'?s\s+rapidly\s+changing\s+business\s+environment\b", "L1.2 filler-opener", "delete entirely"),
    (r"^\s*(Furthermore|Moreover|Additionally),\s", "L1.2 transition-opener", "usually deletable; let the logic carry"),
    (r"\bvarious\s+studies\s+have\s+shown\b", "L1.4 vague-attribution", "cite specific studies or delete the framing"),
    (r"\bit\s+is\s+widely\s+accepted\s+that\b", "L1.4 vague-attribution", "cite or rephrase"),
    (r"\bsome\s+scholars\s+argue\b", "L1.4 vague-attribution", "name the scholars or delete"),
    (r"\bmay\s+potentially\s+(possibly\s+)?suggest", "L1.3 hedge-stack", "reduce to one hedge: 'suggests' or 'may suggest'"),
    (r"\bappears\s+to\s+seemingly\b", "L1.3 hedge-stack", "use 'appears to' or 'seemingly,' not both"),
]


# Structural markers: regex over a longer span (e.g., paragraph or two consecutive sentences).
STRUCTURAL_PATTERNS: list[tuple[str, str, str]] = [
    (r"\bnot\s+only\b[^.]{0,200}?\bbut\s+also\b", "S2.3 balanced-sentence", "break the parallel unless contrast is theoretically meaningful"),
    (r"\bon\s+the\s+one\s+hand\b[^.]{0,200}?\bon\s+the\s+other\s+hand\b", "S2.3 balanced-sentence", "use only for genuine contrast"),
    (r"\bHaving\s+established\b[^.]{0,150}?,\s*we\s+now\s+turn\s+to\b", "S2.4 echo-transition", "delete; the heading signals the turn"),
    (r"\bBuilding\s+on\s+the\s+above\s+discussion,\s+we\b", "S2.4 echo-transition", "delete"),
    (r"\bAs\s+discussed\s+earlier,\b", "S2.4 echo-transition", "usually deletable"),
]


CAUSAL_OVERCLAIM_PATTERNS: list[tuple[str, str, str]] = [
    (r"\bcause(s|d)?\b", "3.2 causal-overclaim", "soften to 'is associated with' / 'predicts' if design is observational"),
    (r"\bdrive(s|n)?\b", "3.2 causal-overclaim", "soften if design is observational"),
    (r"\bleads?\s+to\b", "3.2 causal-overclaim", "soften if design is observational"),
    (r"\bproduce(s|d)?\b", "3.2 causal-overclaim", "soften if design is observational"),
]


def read_text() -> str:
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        return Path(sys.argv[1]).read_text(encoding="utf-8")
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    return sys.stdin.read()


def scan_lines(text: str) -> list[tuple[int, str, str, str, str]]:
    """Return a list of (line_number, rule_label, matched_text, hint, line_excerpt)."""
    findings: list[tuple[int, str, str, str, str]] = []
    for idx, line in enumerate(text.splitlines(), start=1):
        for pattern, label, hint in LEXICAL_PATTERNS + CAUSAL_OVERCLAIM_PATTERNS:
            for m in re.finditer(pattern, line, flags=re.IGNORECASE):
                excerpt = line.strip()
                if len(excerpt) > 160:
                    excerpt = excerpt[:160] + "…"
                findings.append((idx, label, m.group(0), hint, excerpt))
    # Structural patterns are scanned across the whole text by paragraph.
    paragraphs = re.split(r"\n\s*\n", text)
    char_offset = 0
    for paragraph in paragraphs:
        for pattern, label, hint in STRUCTURAL_PATTERNS:
            for m in re.finditer(pattern, paragraph, flags=re.IGNORECASE | re.DOTALL):
                line_no = text[: char_offset + m.start()].count("\n") + 1
                excerpt = m.group(0).replace("\n", " ").strip()
                if len(excerpt) > 160:
                    excerpt = excerpt[:160] + "…"
                findings.append((line_no, label, m.group(0)[:80], hint, excerpt))
        char_offset += len(paragraph) + 2
    findings.sort(key=lambda x: (x[0], x[1]))
    return findings


def main() -> int:
    text = read_text()
    findings = scan_lines(text)

    if not findings:
        print("PASS: no detectable AI-style markers found.")
        return 0

    print(f"REVIEW: found {len(findings)} candidate AI-style marker(s).")
    print("Calibrate against references/ai_style_markers.md before rewriting.")
    print("For a context-aware rewrite, invoke the jbr-ai-decontaminator subagent.\n")
    print(f"{'Line':>4}  {'Rule':<28}  {'Match':<32}  Hint")
    print("-" * 110)
    for line_no, label, matched, hint, _excerpt in findings:
        match_display = matched if len(matched) <= 30 else matched[:30] + "…"
        print(f"{line_no:>4}  {label:<28}  {match_display:<32}  {hint}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
