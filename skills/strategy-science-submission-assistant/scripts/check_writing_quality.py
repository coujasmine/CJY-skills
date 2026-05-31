#!/usr/bin/env python3
"""Aggregate Strategy Science writing-quality checks.

This controller combines AI-style marker scanning, punctuation pattern checks,
throat-clearing openers, structural warnings, and sentence-length variation.
It locates risks; it does not rewrite manuscript text.

Usage:
  python scripts/check_writing_quality.py manuscript.txt
  cat manuscript.txt | python scripts/check_writing_quality.py
  python scripts/check_writing_quality.py --json manuscript.txt
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

try:
    from scan_ai_style_markers import scan_lines
    from check_sentence_burstiness import stats_for_text
except ImportError:  # pragma: no cover - fallback for unusual execution paths
    sys.path.append(str(Path(__file__).resolve().parent))
    from scan_ai_style_markers import scan_lines
    from check_sentence_burstiness import stats_for_text


WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?")

THROAT_CLEARING_PATTERNS: list[tuple[str, str]] = [
    (r"\bIt\s+is\s+important\s+to\s+note\s+that\b", "It is important to note that"),
    (r"\bIt\s+is\s+worth\s+noting\s+that\b", "It is worth noting that"),
    (r"\bIt\s+should\s+be\s+noted\s+that\b", "It should be noted that"),
    (r"\bIn\s+recent\s+years,\s+there\s+has\s+been\s+growing\s+interest\s+in\b", "In recent years...growing interest"),
    (r"\bThere\s+has\s+been\s+growing\s+interest\s+in\b", "There has been growing interest"),
    (r"\bIn\s+today'?s\s+rapidly\s+changing\s+business\s+environment\b", "today's rapidly changing business environment"),
    (r"\bIn\s+an\s+era\s+(where|when|of)\b", "In an era where/when/of"),
    (r"\bAs\s+(organizations|firms|companies)\s+increasingly\b", "As firms increasingly"),
    (r"^\s*(Furthermore|Moreover|Additionally),\s", "transition opener"),
    (r"^\s*(Notably|Importantly|Crucially|Together),\s", "adverb opener"),
]

STRUCTURAL_PATTERNS: list[tuple[str, str, str]] = [
    (
        r"\b(we\s+make|this\s+study\s+makes|our\s+study\s+makes)\s+(three|several)\s+(main\s+)?contributions\b",
        "three-contribution structure",
        "HIGH",
    ),
    (
        r"\b(first|firstly),\s+we\s+contribute\s+to\b.*?\b(second|secondly),\s+we\s+contribute\s+to\b.*?\b(third|thirdly),\s+we\s+contribute\s+to\b",
        "serial contribute-to template",
        "HIGH",
    ),
    (
        r"\bnot\s+only\b[^.]{0,200}?\bbut\s+also\b",
        "not-only-but-also reflex",
        "MEDIUM",
    ),
    (
        r"\bconsistent\s+with\s+(the|our)\s+[^.]{1,80}?\s+logic\b",
        "repeated interaction-logic formula",
        "MEDIUM",
    ),
    (
        r"\b(Notably|Importantly|Crucially|Together),\s[^.]{0,200}\.\s+(Notably|Importantly|Crucially|Together),\s",
        "serial adverb-openers",
        "MEDIUM",
    ),
    (
        r"\b(however|yet|nevertheless),\s+this\s+(finding|result|study)\s+(has|offers)\s+(important|significant)\s+implications\b",
        "generic implication closer",
        "MEDIUM",
    ),
]


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def risk_from_count(count: int, medium: int, high: int) -> str:
    if count >= high:
        return "HIGH"
    if count >= medium:
        return "MEDIUM"
    return "LOW"


def line_excerpt(text: str, line_no: int) -> str:
    lines = text.splitlines()
    if 1 <= line_no <= len(lines):
        excerpt = lines[line_no - 1].strip()
        return excerpt[:180] + ("..." if len(excerpt) > 180 else "")
    return ""


def scan_throat_clearers(text: str) -> list[dict[str, str | int]]:
    findings: list[dict[str, str | int]] = []
    for idx, line in enumerate(text.splitlines(), start=1):
        for pattern, label in THROAT_CLEARING_PATTERNS:
            if re.search(pattern, line, flags=re.IGNORECASE):
                findings.append(
                    {
                        "line": idx,
                        "rule": "throat-clearing opener",
                        "match": label,
                        "severity": "MEDIUM",
                        "action": "Replace the opener with the concrete phenomenon or claim.",
                        "excerpt": line.strip()[:180],
                    }
                )
    return findings


def scan_structures(text: str) -> list[dict[str, str | int]]:
    findings: list[dict[str, str | int]] = []
    for pattern, label, severity in STRUCTURAL_PATTERNS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE | re.DOTALL):
            line_no = text[: match.start()].count("\n") + 1
            if label == "repeated interaction-logic formula":
                action = "Vary interaction interpretations: direction, boundary, alternative mechanism, or limitation."
            elif label == "serial adverb-openers":
                action = "Replace most adverb openers with subject-led sentences or concrete transitions."
            elif label == "not-only-but-also reflex":
                action = "Break the parallel unless it marks a real theoretical contrast."
            elif label == "generic implication closer":
                action = "Replace the generic implication with the specific mechanism or delete."
            else:
                action = "Recast as one or two precise theoretical movements."
            findings.append(
                {
                    "line": line_no,
                    "rule": label,
                    "match": re.sub(r"\s+", " ", match.group(0))[:80],
                    "severity": severity,
                    "action": action,
                    "excerpt": line_excerpt(text, line_no),
                }
            )
    return findings


def punctuation_summary(text: str) -> dict[str, int | str]:
    word_count = len(WORD_RE.findall(text))
    em_dash_count = text.count("\u2014")
    semicolon_count = text.count(";")
    parenthetical_count = text.count("(")
    em_dash_per_1000 = (em_dash_count / word_count * 1000) if word_count else 0
    if em_dash_count > 3 or em_dash_per_1000 > 1:
        em_dash_risk = "HIGH"
    elif em_dash_count > 0:
        em_dash_risk = "LOW"
    else:
        em_dash_risk = "LOW"
    return {
        "word_count": word_count,
        "em_dash_count": em_dash_count,
        "em_dash_per_1000_words": round(em_dash_per_1000, 2),
        "em_dash_risk": em_dash_risk,
        "semicolon_count": semicolon_count,
        "parenthetical_count": parenthetical_count,
    }


def build_report(text: str) -> dict[str, object]:
    ai_findings_raw = scan_lines(text)
    ai_findings = [
        {
            "line": line_no,
            "rule": label,
            "match": matched,
            "severity": "HIGH" if label.startswith("SS-D5") or "anthropomorphizing" in label else "MEDIUM",
            "action": hint,
            "excerpt": excerpt,
        }
        for line_no, label, matched, hint, excerpt in ai_findings_raw
    ]
    throat_findings = scan_throat_clearers(text)
    structure_findings = scan_structures(text)
    punctuation = punctuation_summary(text)
    burstiness = stats_for_text(text)

    ai_rule_counts = Counter(str(f["rule"]) for f in ai_findings)
    ai_risk = risk_from_count(len(ai_findings), medium=3, high=12)
    if any(str(f["severity"]) == "HIGH" for f in ai_findings + structure_findings):
        ai_risk = "HIGH"
    structural_rule_counts = Counter(str(f["rule"]) for f in structure_findings)
    if (
        structural_rule_counts.get("repeated interaction-logic formula", 0) >= 2
        or structural_rule_counts.get("serial adverb-openers", 0) >= 2
        or (
            structural_rule_counts.get("serial adverb-openers", 0) >= 1
            and structural_rule_counts.get("not-only-but-also reflex", 0) >= 1
        )
    ):
        ai_risk = "HIGH"
    readability_risk = "MEDIUM" if burstiness.get("burstiness") == "LOW" else "LOW"
    if punctuation["em_dash_risk"] == "HIGH":
        readability_risk = "HIGH"
    ss_positioning_risk = "HIGH" if any(f["rule"] == "three-contribution structure" for f in structure_findings) else "LOW"

    line_flags = ai_findings + throat_findings + structure_findings
    line_flags.sort(key=lambda f: (int(f["line"]), str(f["rule"])))

    return {
        "overall": {
            "ai_style_risk": ai_risk,
            "readability_risk": readability_risk,
            "ss_positioning_risk_from_prose": ss_positioning_risk,
        },
        "summary": {
            "ai_marker_count": len(ai_findings),
            "ai_marker_rules": dict(ai_rule_counts),
            "throat_clearing_count": len(throat_findings),
            "structural_warning_count": len(structure_findings),
            "punctuation": punctuation,
            "sentence_length_variation": burstiness,
        },
        "line_flags": line_flags,
    }


def print_report(report: dict[str, object]) -> None:
    overall = report["overall"]  # type: ignore[index]
    summary = report["summary"]  # type: ignore[index]
    punctuation = summary["punctuation"]  # type: ignore[index]
    burstiness = summary["sentence_length_variation"]  # type: ignore[index]

    print("Writing Quality Check - Strategy Science")
    print()
    print("Overall risk")
    print(f"- AI-style risk: {overall['ai_style_risk']}")
    print(f"- Readability risk: {overall['readability_risk']}")
    print(f"- SS positioning risk from prose alone: {overall['ss_positioning_risk_from_prose']}")
    print()
    print("Mechanical summary")
    print(f"- AI high-frequency / style markers: {summary['ai_marker_count']}")
    print(f"- Throat-clearing openers: {summary['throat_clearing_count']}")
    print(f"- Structural warnings: {summary['structural_warning_count']}")
    print(
        "- Em dashes: "
        f"{punctuation['em_dash_count']} "
        f"({punctuation['em_dash_per_1000_words']} per 1,000 words; risk {punctuation['em_dash_risk']})"
    )
    print(
        "- Sentence variation: "
        f"mean {burstiness['mean_words']} words, std dev {burstiness['std_dev']}, "
        f"burstiness {burstiness['burstiness']}"
    )
    print()

    flags: list[dict[str, object]] = report["line_flags"]  # type: ignore[assignment]
    if not flags:
        print("Line-level flags: PASS")
        print("Do-not-rewrite notice: diagnostic report only; no text rewritten.")
        return

    print("Line-level flags")
    for finding in flags:
        print(
            f"- Line {finding['line']}: \"{finding['match']}\" - {finding['rule']} - "
            f"{finding['severity']} - {finding['action']}"
        )
    print()
    print("Do-not-rewrite notice: diagnostic report only; no text rewritten.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run aggregate SS writing-quality checks.")
    parser.add_argument("path", nargs="?", help="Text file to inspect; stdin if omitted.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    report = build_report(read_text(args.path))
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print_report(report)
    overall = report["overall"]  # type: ignore[index]
    return 1 if "HIGH" in overall.values() else 0


if __name__ == "__main__":
    raise SystemExit(main())
