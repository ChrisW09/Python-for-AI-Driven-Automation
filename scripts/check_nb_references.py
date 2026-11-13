#!/usr/bin/env python3
"""Verify that references in markdown / notebooks / LaTeX resolve to real files.

Catches drift between documentation and the actual repository layout. Three checks:

1. NB-number references — "NB 7" / "NB7" / "NB 24–28" / "NB 29-31", "Notebook 7" /
   "Notebooks 24–28", LaTeX forms like "NB~43", "NB 17--19" — must name a notebook
   number that exists (*.md, notebook markdown cells, slides/*.tex).
2. Literal notebook filenames — "01_python_basics.ipynb" — must exist somewhere in
   the live tree (*.md, notebook markdown cells).
3. Relative links and images — "[text](../data/README.md)", "![fig](images/x.png)",
   <a href="…">, <img src="…"> — must point at an existing file or folder, resolved
   from the referencing file's own directory (*.md, notebook markdown cells). URLs,
   in-page #anchors, and anything inside `inline code` or fenced code blocks are
   ignored. In docs_site/, "_static/…" resolves to docs_site/assets/ (Sphinx merges
   that folder into _static/ at build time).

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
from urllib.parse import unquote


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
    ".pytest_cache",
    ".venv",
    "node_modules",
    ".git",
}
# Individual files that intentionally describe old states of the course.
EXCLUDED_FILE_NAMES = {"10_course_review_2026.md"}  # historical record; uses pre-renumber NB numbers
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
        # non-breaking space "NB~43" and en/em dashes "NB 17--19".
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


# NB-number references like "NB 12", "NB12", "Notebook 12", "Notebooks 24–28",
# "NB 29-31". The trailing (?!\.\d) keeps version-like strings ("NB 4.0") from
# matching; integers only, same semantics as before.
NB_REF_RE = re.compile(
    r"\b(?:NB|Notebooks?)\s*(\d{1,2})(?!\.\d)(?:\s*[–—-]\s*(\d{1,2})(?!\.\d))?\b"
)

# Surrounding text that signals the missing NB is explicitly documented as such
RESERVED_MARKERS = ("reserved", "folded", "originally planned", "absent", "intentional")

# --- checks 2 & 3: literal notebook filenames and relative links ---------------
# Code is not prose: a filename or link inside `inline code` or a fenced block is
# an example, not a reference, so both are blanked out before matching.
CODE_RE = re.compile(r"^(```|~~~).*?^\1|`[^`\n]*`", re.MULTILINE | re.DOTALL)
NB_FILENAME_RE = re.compile(r"(?<![\w/.-])([\w-]+\.ipynb)\b")
# [text](target), ![alt](target), [text](<target>), [text](target "title")
MD_LINK_RE = re.compile(r"!?\[[^\]\n]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HTML_LINK_RE = re.compile(r"""\b(?:href|src)\s*=\s*["']([^"']+)["']""")
URL_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")  # http:, mailto:, attachment:, …
DOCS_SITE = ROOT / "docs_site"
# Build output of docs_site/generate.py + Sphinx (git-ignored copies with rewritten
# links); checking them would make the result depend on whether docs were built.
DOCS_SITE_GENERATED = tuple(DOCS_SITE / d for d in ("modules", "extras", "_static", "_build"))


def iter_link_files():
    """Yield every live markdown file and notebook whose links should resolve.

    Unlike :func:`iter_text_files`, fast-track notebooks are included: their
    prose links are live, only their NB *numbering* is separate.

    Yields
    ------
    pathlib.Path
        A ``.md`` or ``.ipynb`` file outside the excluded archive folders and
        the docs site's generated build tree.
    """
    for pat in ("**/*.md", "**/*.ipynb"):
        for p in sorted(ROOT.glob(pat)):
            if not is_excluded(p) and not any(p.is_relative_to(g) for g in DOCS_SITE_GENERATED):
                yield p


def markdown_prose(path: Path) -> str:
    """Return a file's markdown with fenced blocks and inline code removed.

    Parameters
    ----------
    path : pathlib.Path
        A ``.md`` file or a notebook (only its markdown cells are used).

    Returns
    -------
    str
        The prose, ready for link / filename matching.
    """
    if path.suffix == ".ipynb":
        try:
            nb = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return ""
        text = "\n".join("".join(c.get("source", [])) for c in nb.get("cells", [])
                         if c.get("cell_type") == "markdown")
    else:
        text = path.read_text(encoding="utf-8", errors="ignore")
    return CODE_RE.sub("", text)


def link_target_exists(source: Path, target: str) -> bool:
    """Decide whether a relative link written in ``source`` resolves.

    Parameters
    ----------
    source : pathlib.Path
        The file containing the link; relative targets resolve from its folder.
    target : str
        The raw link target, possibly with ``#fragment`` or ``?query``.

    Returns
    -------
    bool
        True if the target is external (has a URL scheme), a pure in-page
        anchor, or an existing file / folder.
    """
    if URL_SCHEME_RE.match(target) or target.startswith(("#", "//")):
        return True
    path = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not path:
        return True
    if (source.parent / path).exists():
        return True
    # docs_site/: Sphinx merges docs_site/assets/ into _static/ at build time.
    if source.parent == DOCS_SITE and path.startswith("_static/"):
        return (DOCS_SITE / "assets" / path.removeprefix("_static/")).exists()
    return False


def find_broken_links() -> tuple[list[tuple[Path, str]], list[tuple[Path, str]]]:
    """Run checks 2 and 3 over the live tree.

    Returns
    -------
    missing_files : list of (pathlib.Path, str)
        Literal ``*.ipynb`` names that match no live notebook.
    broken_links : list of (pathlib.Path, str)
        Relative link / image targets that do not exist.
    """
    live_notebooks = {p.name for p in ROOT.glob("**/*.ipynb") if not is_excluded(p)}
    missing_files, broken_links = [], []
    for path in iter_link_files():
        prose = markdown_prose(path)
        for m in NB_FILENAME_RE.finditer(prose):
            if m.group(1) not in live_notebooks:
                missing_files.append((path, m.group(1)))
        for m in (*MD_LINK_RE.finditer(prose), *HTML_LINK_RE.finditer(prose)):
            if not link_target_exists(path, m.group(1)):
                broken_links.append((path, m.group(1)))
    return missing_files, broken_links


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

    missing_files, broken_links = find_broken_links()
    status = 0

    if failures:
        print(f"❌ {len(failures)} NB-number reference(s) point to missing notebooks:\n")
        for path, ref, num in failures:
            rel = path.relative_to(ROOT)
            print(f"  {rel}: '{ref}' → NB {num:02d} not on disk")
        print("\nFix the docs to match the filesystem, add the missing notebook, ")
        print("or mark the surrounding context as 'reserved'.\n")
        status = 1
    else:
        print(f"✅ All NB-number references resolve. Discovered notebooks: {sorted(existing)}")

    if missing_files:
        print(f"❌ {len(missing_files)} notebook filename(s) match no notebook in the tree:")
        for path, name in missing_files:
            print(f"  {path.relative_to(ROOT)}: '{name}'")
        status = 1
    if broken_links:
        print(f"❌ {len(broken_links)} relative link(s) / image(s) point to a missing path:")
        for path, target in broken_links:
            print(f"  {path.relative_to(ROOT)}: ({target})")
        status = 1
    if not (missing_files or broken_links):
        print("✅ All notebook filenames and relative links resolve.")
    return status


if __name__ == "__main__":
    sys.exit(main())
