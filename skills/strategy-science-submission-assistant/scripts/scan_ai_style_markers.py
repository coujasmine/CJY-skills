#!/usr/bin/env python3
"""Scan manuscript text for AI-generated style markers (lexical + structural + causal).

Calibrated for Strategy Science prose norms. Reports flagged lines with the rule
that triggered. Does not modify the text.

Usage:
  python scripts/scan_ai_style_markers.py manuscript.txt
  cat manuscript.txt | python scripts/scan_ai_style_markers.py

Pair with references/ai_style_markers.md for the full catalog and decontamination
guidance. For a context-aware rewrite, invoke the ss-ai-decontaminator subagent.

Exit code 0 if no markers found, 1 otherwise.

Note: The scanner does NOT know context. "Leverage" in a capital-structure
discussion is correct. "Myriad" in conflict-management literature is technical.
"Navigate" in option-value strategy is technical. Always cross-check hits
against references/ai_style_markers.md §1.5 (SS-protected vocabulary) before
rewriting.
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
    (r"\bmyriad\b", "L1.1 myriad", "many / several (unless conflict-management term)"),
    (r"\bnavigate(s|d|ing)?\b", "L1.1 navigate", "address / manage / handle (unless option-value or spatial)"),
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
    (r"\bharness(es|ed|ing)?\b", "L1.1 harness", "use / employ"),
    (r"\bushered\s+in\b", "L1.1 ushered in", "began / started"),
    (r"\bat\s+the\s+forefront\s+of\b", "L1.1 at the forefront of", "leading in"),
    (r"\bgame[- ]changer\b", "L1.1 game-changer", "important / transformative"),
    (r"\bgame[- ]changing\b", "L1.1 game-changing", "important"),
    (r"\btransformative\b", "L1.1 transformative", "significant change — or delete"),
    (r"\bcutting[- ]edge\b", "L1.1 cutting-edge", "new / recent"),
    (r"\bstate[- ]of[- ]the[- ]art\b", "L1.1 state-of-the-art", "current / leading"),
    (r"\bbreakthroughs?\b", "L1.1 breakthroughs", "advances"),
    (r"\bmultifaceted\b", "L1.1 multifaceted", "specify the dimensions or delete"),
    (r"\b(rich|valuable)\s+insights?\b", "L1.1 generic-insights", "name the finding or delete"),
    (r"\bcomplex\s+interplay\b", "L1.1 complex-interplay", "specify the relationship"),
    (r"\b(crucial|critical)\s+role\b", "L1.1 critical-role", "name the role/effect/mechanism or delete"),
    (r"\bincreasingly\s+important\b", "L1.1 increasingly-important", "specify what changed or delete"),
    (r"\bfertile\s+ground\b", "L1.1 fertile-ground", "use empirical context / setting"),
    (r"\bfill(s|ed|ing)?\s+(an?\s+)?gap\b", "L1.1 fill-gap", "answer a question / test a mechanism / extend a lineage"),
    (r"\bcontribute(s|d|ing)?\s+to\s+our\s+understanding\b", "L1.1 contribute-understanding", "specify the theoretical movement"),
    # Filler openers
    (r"\bIt\s+is\s+important\s+to\s+note\s+that\b", "L1.2 filler-opener", "delete and state the point directly"),
    (r"\bIt\s+is\s+worth\s+noting\s+that\b", "L1.2 filler-opener", "delete and state the point directly"),
    (r"\bIt\s+should\s+be\s+noted\s+that\b", "L1.2 filler-opener", "delete and state the point directly"),
    (r"\bIt\s+is\s+crucial\s+to\s+recognize\s+that\b", "L1.2 filler-opener", "delete and state the point directly"),
    (r"\bIt\s+is\s+interesting\s+to\s+note\s+that\b", "L1.2 filler-opener", "delete and state the point directly"),
    (r"\bIn\s+recent\s+years,\s+there\s+has\s+been\s+growing\s+interest\s+in\b", "L1.2 filler-opener", "replace with the concrete phenomenon"),
    (r"\bIn\s+today'?s\s+rapidly\s+changing\s+business\s+environment\b", "L1.2 filler-opener", "delete entirely"),
    (r"\bIn\s+an\s+era\s+(where|when|of)\b", "L1.2 filler-opener", "replace with the concrete change or setting"),
    (r"\bAs\s+(organizations|firms|companies)\s+increasingly\b", "L1.2 filler-opener", "keep only if the trend is evidenced and necessary"),
    (r"\bAs\s+mentioned\s+earlier,\b", "L1.2 filler-opener", "delete; trust the reader"),
    (r"\bBuilding\s+on\s+the\s+above,\b", "L1.2 filler-opener", "delete; trust the structure"),
    (r"\bTo\s+put\s+it\s+simply,\b", "L1.2 filler-opener", "delete or rephrase"),
    (r"\bSimply\s+put,\b", "L1.2 filler-opener", "delete"),
    (r"^\s*(Furthermore|Moreover|Additionally),\s", "L1.2 transition-opener", "usually deletable; let the logic carry"),
    (r"^\s*(Notably|Importantly|Crucially|Together),\s", "L1.2 adverb-opener", "vary repeated openers; use a subject-led sentence or delete"),
    # Vague attribution
    (r"\bvarious\s+studies\s+have\s+shown\b", "L1.4 vague-attribution", "cite specific studies or delete the framing"),
    (r"\bit\s+is\s+widely\s+accepted\s+that\b", "L1.4 vague-attribution", "cite or rephrase"),
    (r"\bsome\s+scholars\s+argue\b", "L1.4 vague-attribution", "name the scholars or delete"),
    (r"\bresearch\s+has\s+shown\b", "L1.4 vague-attribution", "cite specific research"),
    (r"\bstudies\s+suggest\b", "L1.4 vague-attribution", "cite specific studies"),
    (r"\bmany\s+researchers\s+have\s+noted\b", "L1.4 vague-attribution", "cite specific researchers"),
    # Hedge stacks
    (r"\bmay\s+potentially\s+(possibly\s+)?suggest", "L1.3 hedge-stack", "reduce to one hedge"),
    (r"\bappears\s+to\s+seemingly\b", "L1.3 hedge-stack", "use 'appears to' or 'seemingly,' not both"),
    (r"\bcould\s+potentially\s+be\s+considered\b", "L1.3 hedge-stack", "use 'may be'"),
    (r"\btends\s+to\s+typically\b", "L1.3 hedge-stack", "use 'typically'"),
    (r"\bconsistent\s+with\s+(the|our)\s+[^.]{1,80}?\s+logic\b", "L1.3 repeated-logic-formula", "do not repeat for every interaction; vary the evidentiary move"),
    # LLM anthropomorphizing (SS-specific concern)
    (r"\bthe\s+(llm|ai|model|algorithm)\s+(understands|understood|knows|knew|decides|decided|believes|believed|thinks|thought)\b", "L3.4 anthropomorphizing", "rewrite to 'produced output that...' or 'classified as...'"),
]


# Structural markers: regex over a longer span.
STRUCTURAL_PATTERNS: list[tuple[str, str, str]] = [
    (r"\bnot\s+only\b[^.]{0,200}?\bbut\s+also\b", "S2.3 balanced-sentence", "break the parallel unless contrast is theoretically meaningful"),
    (r"\bon\s+the\s+one\s+hand\b[^.]{0,400}?\bon\s+the\s+other\s+hand\b", "S2.3 balanced-sentence", "use only for genuine theoretical contrast"),
    (r"\b(NOTABLY|Notably|notably),\s[^.]{0,200}\.\s+(IMPORTANTLY|Importantly|importantly),\s[^.]{0,200}\.", "S2.3 serial-adverb-openers", "avoid paired adverb openers across adjacent sentences"),
    (r"\b(CRUCIALLY|Crucially|crucially),\s[^.]{0,200}\.\s+(TOGETHER|Together|together),\s[^.]{0,200}\.", "S2.3 serial-adverb-openers", "avoid paired adverb openers across adjacent sentences"),
    (r"\bHaving\s+established\b[^.]{0,150}?,\s*we\s+now\s+turn\s+to\b", "S2.4 echo-transition", "delete; the heading signals the turn"),
    (r"\bBuilding\s+on\s+the\s+above\s+discussion,\s+we\b", "S2.4 echo-transition", "delete"),
    (r"\bAs\s+discussed\s+earlier,\b", "S2.4 echo-transition", "usually deletable"),
    (r"\bFollowing\s+our\s+previous\s+discussion,\b", "S2.4 echo-transition", "usually deletable"),
    # SS-specific: three-vague-contribution detection
    (r"\b(we\s+make|this\s+study\s+makes|our\s+study\s+makes)\s+(three|several)\s+(main\s+)?contributions\b", "SS-D5 three-contribution", "HIGH SS desk-reject risk: rewrite as one or two SPECIFIC theoretical movements"),
    (r"\b(first|firstly),\s+we\s+contribute\s+to[^.]{0,80}\.[^.]{0,200}?(second|secondly),\s+we\s+contribute\s+to[^.]{0,80}\.[^.]{0,200}?(third|thirdly),\s+we\s+contribute\s+to\b", "SS-D5 three-contribution", "HIGH SS desk-reject risk: collapse into 1-2 specific theoretical movements"),
]


CAUSAL_OVERCLAIM_PATTERNS: list[tuple[str, str, str]] = [
    (r"\bcause(s|d)?\b", "3.2 causal-overclaim", "soften to 'is associated with' / 'predicts' if design is observational"),
    (r"\bdrive(s|n)?\b", "3.2 causal-overclaim", "soften if design is observational"),
    (r"\bleads?\s+to\b", "3.2 causal-overclaim", "soften if design is observational"),
    (r"\bproduce(s|d)?\b", "3.2 causal-overclaim", "soften if design is observational"),
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
    print("For a context-aware rewrite, invoke the ss-ai-decontaminator subagent.")
    print()
    print("SS-specific reminders:")
    print("  - 'Leverage' in capital-structure context is correct, preserve.")
    print("  - 'Navigate' in option-value or spatial context is correct, preserve.")
    print("  - 'Myriad' in conflict-management literature is technical, preserve.")
    print("  - SS theoretical vocabulary (mental representations, governance, ecosystem, etc.) is ALWAYS preserved.")
    print("  - LLM anthropomorphizing is a HIGH concern for SS reviewers — fix every instance.")
    print("  - Three-vague-contribution patterns trigger HIGH desk-reject (SS-D5).")
    print("  - Repeated 'Notably/Importantly/Crucially/Together' openers and repeated")
    print("    'consistent with the X logic' interaction glosses are model-trace risks.")
    print()
    print(f"{'Line':>4}  {'Rule':<28}  {'Match':<32}  Hint")
    print("-" * 110)
    for line_no, label, matched, hint, _excerpt in findings:
        match_display = matched if len(matched) <= 30 else matched[:30] + "…"
        print(f"{line_no:>4}  {label:<28}  {match_display:<32}  {hint}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
