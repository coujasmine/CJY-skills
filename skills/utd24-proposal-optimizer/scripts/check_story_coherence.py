#!/usr/bin/env python3
"""Locate textual signals relevant to the UTD24 Story Coherence Gate.

This is a candidate locator, not a quality judge. It checks plain-text or
Markdown input for four signal families: gap-only framing, knot/tension,
resolution/mechanism, and before-after contribution. The agent must interpret
hits using references/utd24_storytelling_architecture.md.

Usage:
    python3 check_story_coherence.py <file>
    cat draft.txt | python3 check_story_coherence.py -
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


SIGNALS: dict[str, list[str]] = {
    "gap_only": [
        r"\bfew studies\b",
        r"\blittle is known\b",
        r"\bno (?:prior )?(?:research|study|studies)\b",
        r"\bhas not been (?:examined|studied|tested|explored)\b",
        r"\bcall(?:s|ed)? for (?:more|future) research\b",
        r"\bfill(?:s|ing)? (?:a|the) gap\b",
        r"鲜有研究",
        r"较少研究",
        r"尚未研究",
        r"缺乏研究",
        r"填补.{0,8}空白",
        r"回应.{0,8}研究呼吁",
    ],
    "knot_tension": [
        r"\bparadox(?:ical)?\b",
        r"\bcontradict(?:s|ion|ory)?\b",
        r"\bcompeting (?:logic|logics|prediction|predictions)\b",
        r"\btheoretical tension\b",
        r"\banomal(?:y|ies|ous)\b",
        r"\bunexpected(?:ly)?\b",
        r"\bcannot explain\b",
        r"\bfails? to explain\b",
        r"\bimplicit assumption\b",
        r"悖论",
        r"矛盾",
        r"理论张力",
        r"竞争(?:性)?(?:逻辑|预测|解释)",
        r"异常现象",
        r"无法解释",
        r"解释失效",
        r"隐含假设",
    ],
    "resolution_mechanism": [
        r"\bmechanism\b",
        r"\bcausal pathway\b",
        r"\bwe (?:propose|theorize|argue|show|find|demonstrate)\b",
        r"\bour (?:results|findings|evidence)\b",
        r"\balternative explanation\b",
        r"\bmediating (?:process|mechanism)\b",
        r"机制",
        r"因果路径",
        r"作用路径",
        r"核心发现",
        r"研究结果表明",
        r"替代解释",
        r"中介过程",
    ],
    "before_after": [
        r"\bbefore\b.{0,80}\bafter\b",
        r"\bpreviously (?:assumed|believed|understood)\b",
        r"\bwe now (?:know|understand|show)\b",
        r"\brethink\b",
        r"\brevise (?:our|the) understanding\b",
        r"\bchanges how we understand\b",
        r"过去.{0,80}现在",
        r"此前.{0,80}如今",
        r"原先.{0,80}现在",
        r"重新理解",
        r"改变.{0,16}理解",
        r"修正.{0,16}认识",
    ],
}

COMPILED = {
    family: re.compile("|".join(patterns), re.IGNORECASE)
    for family, patterns in SIGNALS.items()
}


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8", errors="replace")


def compact(line: str, limit: int = 220) -> str:
    text = " ".join(line.split())
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def scan(text: str) -> dict[str, list[tuple[int, str, str]]]:
    hits: dict[str, list[tuple[int, str, str]]] = {
        family: [] for family in SIGNALS
    }
    for line_no, line in enumerate(text.splitlines(), start=1):
        for family, pattern in COMPILED.items():
            for match in pattern.finditer(line):
                hits[family].append((line_no, match.group(0), compact(line)))
    return hits


def print_family(name: str, hits: list[tuple[int, str, str]]) -> None:
    print(f"\n## {name} ({len(hits)} hit(s))")
    if not hits:
        print("- none located")
        return
    for line_no, phrase, context in hits[:20]:
        print(f"- line {line_no}: [{phrase}] {context}")
    if len(hits) > 20:
        print(f"- … {len(hits) - 20} additional hit(s) omitted")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: check_story_coherence.py <file|->", file=sys.stderr)
        return 2

    hits = scan(read_text(argv[1]))
    counts = {family: len(items) for family, items in hits.items()}

    print("Story-coherence signal scan (candidate locator; not a quality score)")
    print(
        "Summary: "
        + ", ".join(f"{family}={count}" for family, count in counts.items())
    )

    for family in ("gap_only", "knot_tension", "resolution_mechanism", "before_after"):
        print_family(family, hits[family])

    print("\n## Interpretation prompts")
    if counts["gap_only"] and not counts["knot_tension"]:
        print("- [FLAG] Gap-only markers appear without located knot/tension signals. Test whether importance survives after removing the gap claim.")
    elif counts["knot_tension"]:
        print("- [CHECK] Knot/tension candidates located. Verify they name a real theoretical contradiction rather than rhetorical drama.")
    else:
        print("- [CHECK] No knot/tension signal located. The knot may be implicit, absent, or expressed with different wording.")

    if not counts["resolution_mechanism"]:
        print("- [CHECK] No resolution/mechanism signal located. Verify that the paper supplies an explanatory answer supported by the design.")
    if not counts["before_after"]:
        print("- [CHECK] No before-after signal located. Verify that Discussion states a specific change in theoretical understanding.")

    print("- Always run the qualitative Story Coherence Gate in references/utd24_storytelling_architecture.md; marker counts do not determine PASS/PARTIAL/FAIL.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
