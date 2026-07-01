#!/usr/bin/env python3
"""Verify NB-number references in markdown / notebooks / LaTeX resolve to a real file.

Catches drift between documentation and the actual notebook layout. Looks for
patterns like:
  - "NB 7"  /  "NB7"  /  "NB 18–22"  /  "NB 23-25"
  - "Notebook 7"  /  "Notebooks 18–22"  /  LaTeX forms like "NB~43", "NB 14--16"
  - "01_python_basics.ipynb" (literal filename references)
…and asserts that every NB number / filename can be found somewhere in the repo.

Scans the live course tree: *.md, *.ipynb (markdown cells) and slides/*.tex.
Historical / archival content (previous_versions/, docs/, COURSE_REVIEW_REPORT.md)
intentionally describes old states and is skipped.

Run from the repo root:
    python scripts/check_nb_references.py

Exits non-zero if any reference fails to resolve.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

# Where to look for cross-references (LaTeX is limited to the lecture decks;
# other .tex under course_intro_presentation/ & local_presentations/ is legacy)
TEXT_GLOBS = ["**/*.md", "**/*.ipynb", "slides/*.tex"]
# Where to find notebook files (skip the legacy archive)
NB_GLOBS = ["**/*.ipynb"]
# Folders ignored entirely (both for text scanning and notebook discovery):
# historical/archival trees plus tooling junk.
EXCLUDED_DIR_NAMES = {
    "previous_versions",
    "docs",
    ".ipynb_checkpoints",
    "__pycache__",
    ".venv",
    "node_modules",
    ".git",
}
# Individual files that intentionally describe old states of the course.
EXCLUDED_FILE_NAMES = {"COURSE_REVIEW_REPORT.md"}
# fast_track/ uses its own re-numbering (0-14) that diverges from the canonical
# course; cross-references in any file should resolve against the canonical
# numbering, so we don't let fast_track filenames satisfy "NB N" references and
# we don't scan its notebooks' prose. Its markdown (README) is live and scanned.
FAST_TRACK_DIR = "fast_track"


def is_excluded(path: Path) -> bool:
    return (
        any(part in EXCLUDED_DIR_NAMES for part in path.parts)
        or path.name in EXCLUDED_FILE_NAMES
    )


def discover_nb_numbers() -> set[int]:
    """Return the set of notebook *numbers* that exist on disk (e.g. {0, 1, 2, ..., 27})."""
    nums = set()
    for pat in NB_GLOBS:
        for p in ROOT.glob(pat):
            if is_excluded(p) or FAST_TRACK_DIR in p.parts:
                continue
            m = re.match(r"(\d{1,2})_", p.name)
            if m:
                nums.add(int(m.group(1)))
    return nums


def iter_text_files():
    seen = set()
    for pat in TEXT_GLOBS:
        for p in ROOT.glob(pat):
            if is_excluded(p) or p in seen:
                continue
            if FAST_TRACK_DIR in p.parts and p.suffix != ".md":
                continue
            seen.add(p)
            yield p


# Fenced code blocks in markdown may contain literal "NB n"-looking examples;
# drop them before matching.
MD_FENCE_RE = re.compile(r"^(```|~~~).*?^\1", re.MULTILINE | re.DOTALL)


def extract_text(path: Path) -> str:
    if path.suffix == ".md":
        return MD_FENCE_RE.sub("", path.read_text(encoding="utf-8", errors="ignore"))
    if path.suffix == ".tex":
        text = path.read_text(encoding="utf-8", errors="ignore")
        # Normalise LaTeX typography so the same reference regex applies:
        # non-breaking space "NB~43" and en/em dashes "NB 14--16".
        text = text.replace("~", " ")
        return re.sub(r"-{2,3}", "–", text)
    if path.suffix == ".ipynb":
        try:
            nb = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return ""
        chunks = []
        for c in nb.get("cells", []):
            if c.get("cell_type") == "markdown":
                chunks.append("".join(c.get("source", [])))
        return "\n".join(chunks)
    return ""


# NB-number references like "NB 12", "NB12", "Notebook 12", "Notebooks 18–22",
# "NB 23-25". The trailing (?!\.\d) keeps version-like strings ("NB 4.0") from
# matching; integers only, same semantics as before.
NB_REF_RE = re.compile(
    r"\b(?:NB|Notebooks?)\s*(\d{1,2})(?!\.\d)(?:\s*[–—-]\s*(\d{1,2})(?!\.\d))?\b"
)

# Surrounding text that signals the missing NB is explicitly documented as such
RESERVED_MARKERS = ("reserved", "folded", "originally planned", "absent", "intentional")


def main() -> int:
    existing = discover_nb_numbers()
    if not existing:
        print("ERROR: no notebooks discovered under repo root.", file=sys.stderr)
        return 2

    failures: list[tuple[Path, str, int]] = []
    for tf in iter_text_files():
        text = extract_text(tf)
        for m in NB_REF_RE.finditer(text):
            lo = int(m.group(1))
            hi = int(m.group(2) or lo)
            if lo > hi:
                lo, hi = hi, lo
            # Allow ranges that include known gaps if the surrounding text marks them reserved
            context = text[max(0, m.start() - 80) : m.end() + 80].lower()
            is_reserved = any(k in context for k in RESERVED_MARKERS)
            for n in range(lo, hi + 1):
                if n not in existing and not is_reserved:
                    failures.append((tf, m.group(0), n))

    if failures:
        print(f"❌ {len(failures)} NB-number reference(s) point to missing notebooks:\n")
        for path, ref, num in failures:
            rel = path.relative_to(ROOT)
            print(f"  {rel}: '{ref}' → NB {num:02d} not on disk")
        print("\nFix the docs to match the filesystem, add the missing notebook, ")
        print("or mark the surrounding context as 'reserved'.")
        return 1

    print(f"✅ All NB-number references resolve. Discovered notebooks: {sorted(existing)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
