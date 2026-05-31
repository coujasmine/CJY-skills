"""Shared helpers for markdown-word skill scripts."""
from pathlib import Path

import yaml

SKILL_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = SKILL_ROOT / "journal_configs"
TEMPLATE_DIR = SKILL_ROOT / "templates"


def load_journal_config(journal_key: str) -> dict:
    """Load and return the YAML config for a journal key.

    Raises FileNotFoundError with a helpful message if the key is unknown.
    """
    path = CONFIG_DIR / f"{journal_key}.yaml"
    if not path.exists():
        available = list_journals()
        raise FileNotFoundError(
            f"No journal config: {path}\n"
            f"Available journals: {', '.join(available) if available else '(none)'}\n"
            f"To add a new journal, see references/adding-new-journal.md"
        )
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def list_journals() -> list:
    """Return sorted list of journal keys (filenames in journal_configs/, excluding _schema)."""
    if not CONFIG_DIR.exists():
        return []
    return sorted(
        p.stem for p in CONFIG_DIR.glob("*.yaml") if not p.stem.startswith("_")
    )


def reference_docx_path(journal_key: str) -> Path:
    """Path where the generated reference docx for `journal_key` lives."""
    return TEMPLATE_DIR / f"{journal_key}-reference.docx"
