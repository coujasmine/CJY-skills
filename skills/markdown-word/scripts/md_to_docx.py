#!/usr/bin/env python3
"""End-to-end orchestrator: Markdown → Word with journal-specific formatting.

Usage:
    python3 md_to_docx.py <input.md> <journal-key> [-o output.docx]
                          [--bibliography refs.bib] [--csl style.csl]
                          [--skip-validate]

Steps:
    1. Verify pandoc / python-docx / PyYAML are installed.
    2. Build (or rebuild if stale) templates/<journal>-reference.docx from YAML.
    3. Run pandoc with --reference-doc to produce a raw docx.
    4. Run postprocess_docx.py (fonts, heading numbering, line/page numbers).
    5. Run format_apa_tables.py (three-line tables, captions, page-break behavior).
    6. Run validate_format.py (compliance report).
"""
import argparse
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))
from _lib import load_journal_config, reference_docx_path, CONFIG_DIR


def run(cmd, *, check=True, label=None):
    if label:
        print(f"\n--- {label} ---")
    print("$ " + " ".join(str(c) for c in cmd))
    result = subprocess.run(cmd, text=True)
    if check and result.returncode != 0:
        print(f"[failed] exit {result.returncode}: {' '.join(str(c) for c in cmd)}",
              file=sys.stderr)
        raise SystemExit(result.returncode)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Convert Markdown to a journal-formatted Word document.",
    )
    parser.add_argument("input_md", type=Path, help="Source Markdown file")
    parser.add_argument("journal", help="Journal key (jbr, strategy-science, generic, ...)")
    parser.add_argument("-o", "--output", type=Path, default=None,
                        help="Output .docx (default: <input stem>-<journal>.docx next to input)")
    parser.add_argument("--bibliography", type=Path, default=None,
                        help="Optional .bib file (enables Pandoc citeproc)")
    parser.add_argument("--csl", type=Path, default=None,
                        help="Optional .csl style for citeproc")
    parser.add_argument("--skip-validate", action="store_true",
                        help="Skip the final validation step")
    parser.add_argument("--no-table-format", action="store_true",
                        help="Skip APA table formatting (e.g., for already-styled tables)")
    parser.add_argument("--no-heading-numbering", action="store_true",
                        help="Skip auto-numbering of headings (use when MD has manual numbers)")
    args = parser.parse_args()

    if not args.input_md.exists():
        print(f"Input not found: {args.input_md}", file=sys.stderr)
        return 1

    # Step 1: deps
    rc = run([sys.executable, str(SCRIPTS_DIR / "check_dependencies.py")],
             check=False, label="1. Check dependencies")
    if rc != 0:
        return rc

    # Validate journal key
    config = load_journal_config(args.journal)

    # Step 2: reference docx (build if missing or YAML is newer)
    ref = reference_docx_path(args.journal)
    yaml_path = CONFIG_DIR / f"{args.journal}.yaml"
    rebuild = (not ref.exists()) or (
        yaml_path.stat().st_mtime > ref.stat().st_mtime
    )
    if rebuild:
        run([sys.executable, str(SCRIPTS_DIR / "build_reference_docx.py"),
             args.journal], label="2. Build reference.docx from YAML")
    else:
        print(f"\n--- 2. Reference docx up to date: {ref} ---")

    # Step 3: pandoc
    output = args.output or args.input_md.with_name(
        f"{args.input_md.stem}-{args.journal}.docx"
    )
    pandoc_cmd = [
        "pandoc",
        str(args.input_md),
        f"--reference-doc={ref}",
        "-o", str(output),
        "--standalone",
    ]
    if args.bibliography:
        pandoc_cmd += ["--citeproc", f"--bibliography={args.bibliography}"]
        if args.csl:
            pandoc_cmd += [f"--csl={args.csl}"]
    run(pandoc_cmd, label="3. Pandoc convert")

    # Step 4: post-process
    post_cmd = [sys.executable, str(SCRIPTS_DIR / "postprocess_docx.py"),
                str(output), args.journal]
    if args.no_heading_numbering:
        post_cmd.append("--no-heading-numbering")
    run(post_cmd, label="4. Post-process (fonts, headings, line/page numbers)")

    # Step 5: tables
    if not args.no_table_format:
        run([sys.executable, str(SCRIPTS_DIR / "format_apa_tables.py"),
             str(output), args.journal], label="5. APA tables")

    # Step 6: validate
    if not args.skip_validate:
        rc = run([sys.executable, str(SCRIPTS_DIR / "validate_format.py"),
                  str(output), args.journal], check=False, label="6. Validate")
        if rc != 0:
            print(f"\n[!] Validation found {rc} issue(s). See report next to the output docx.")

    print(f"\n[OK] {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
