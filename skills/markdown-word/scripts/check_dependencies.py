#!/usr/bin/env python3
"""Verify the skill's runtime dependencies are present.

Exits 0 if all deps are available, 1 otherwise — printing install commands.
"""
import shutil
import subprocess
import sys


def main() -> int:
    failures = []
    notes = []

    pandoc = shutil.which("pandoc")
    if not pandoc:
        failures.append(
            "pandoc:\n"
            "    macOS:   brew install pandoc\n"
            "    Linux:   sudo apt install pandoc   # or your distro's package manager\n"
            "    Windows: choco install pandoc"
        )
    else:
        try:
            ver = subprocess.check_output(
                [pandoc, "--version"], text=True
            ).splitlines()[0]
            notes.append(f"pandoc: {ver}")
        except Exception:
            notes.append(f"pandoc: found at {pandoc}")

    try:
        import docx  # noqa: F401
        notes.append("python-docx: available")
    except ImportError:
        failures.append("python-docx:\n    pip install python-docx")

    try:
        import yaml  # noqa: F401
        notes.append("PyYAML: available")
    except ImportError:
        failures.append("PyYAML:\n    pip install PyYAML")

    if failures:
        print("Missing dependencies:\n", file=sys.stderr)
        for f in failures:
            print(f"  - {f}\n", file=sys.stderr)
        return 1

    for n in notes:
        print(f"  {n}")
    print("All dependencies present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
