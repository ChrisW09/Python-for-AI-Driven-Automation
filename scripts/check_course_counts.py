#!/usr/bin/env python
"""Keep the course's headline numbers honest.

The notebook count, checkpoint count and appendix count each appear in several
prose locations (README badge/headline, docs_site index, the 00b overview).
Whenever a notebook is added or a checkpoint lands, every one of those spots
has to move in lockstep — history shows they drift. This script derives the
real numbers from the tree and fails if any prose location disagrees, or if a
checked phrase has been reworded away (which would silently disable its check).

    python scripts/check_course_counts.py

Needs only nbformat (same as test_checkpoints.py). Exits non-zero on any drift.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import test_checkpoints as tc  # noqa: E402  (reuse FOLDERS + checkpoint parser)

EXCLUDE = ("previous_versions" + os.sep, ".ipynb_checkpoints")


def derive_notebook_count():
    nbs = [
        p for p in glob.glob(os.path.join(ROOT, "**", "*.ipynb"), recursive=True)
        if not any(x in p for x in EXCLUDE)
    ]
    return len(nbs)


def derive_checkpoint_count():
    import nbformat
    total = 0
    for path in tc.discover():
        nb = nbformat.read(path, as_version=4)
        total += sum(1 for _ in tc.find_checkpoints(nb.cells))
    return total


def derive_appendix_count():
    apps = [
        p for p in glob.glob(os.path.join(ROOT, "*", "A[0-9]_*.ipynb"))
        if not any(x in p for x in EXCLUDE)
    ]
    return len(apps)


def derive_colab_count(readme_text):
    """Unique notebook paths linked to Colab in the README (the 3 quick-start
    badges duplicate table rows, so uniqueness matters)."""
    links = re.findall(
        r"colab\.research\.google\.com/github/[^/]+/[^/]+/blob/main/([^)\s]+\.ipynb)",
        readme_text,
    )
    return len(set(links))


# (file, human label, regex with ONE capture group, which derived count, expected #matches)
CHECKS = [
    ("README.md", "badge", r"badge/(\d+)%20checkpoints", "checkpoints", 1),
    ("README.md", "headline notebooks", r"(\d+) runnable notebooks", "notebooks", 1),
    ("README.md", "headline checkpoints", r"(\d+) in-lesson checkpoints", "checkpoints", 1),
    ("README.md", "'across the course'", r"\*\*(\d+) across the course\*\*", "checkpoints", 2),
    ("README.md", "path-table appendices", r"\+ (\d+) optional appendices", "appendices", 1),
    ("README.md", "path-table appendix row", r"\(\+ (\d+) appendices\)", "appendices", 1),
    ("README.md", "repo-layout appendices", r"lessons 1–53 \+ (\d+) appendices", "appendices", 1),
    ("README.md", "Colab footnote", r"The \*\*(\d+) notebooks\*\*", "notebooks", 1),
    ("docs_site/index.md", "stats notebooks", r"<b>(\d+)</b> runnable notebooks", "notebooks", 1),
    ("docs_site/index.md", "stats checkpoints", r"<b>(\d+)</b> in-lesson checkpoints", "checkpoints", 1),
    ("00_onboarding/00b_course_overview.ipynb", "appendix note", r"\((\d+) advanced notebooks", "appendices", 1),
    ("00_onboarding/00b_course_overview.ipynb", "appendix tip", r"The (\d+) A-\* appendices", "appendices", 1),
]


def main():
    derived = {
        "notebooks": derive_notebook_count(),
        "checkpoints": derive_checkpoint_count(),
        "appendices": derive_appendix_count(),
    }
    print("derived from tree:", ", ".join(f"{k}={v}" for k, v in derived.items()))

    failures = []
    for relpath, label, pattern, key, expected_n in CHECKS:
        with open(os.path.join(ROOT, relpath), encoding="utf-8") as fh:
            text = fh.read()
        matches = re.findall(pattern, text)
        where = f"{relpath} [{label}]"
        if len(matches) != expected_n:
            failures.append(
                f"{where}: expected {expected_n} occurrence(s) of /{pattern}/, "
                f"found {len(matches)} — reworded? update CHECKS"
            )
            continue
        for m in matches:
            if int(m) != derived[key]:
                failures.append(f"{where}: says {m}, tree has {derived[key]} {key}")

    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
        readme = fh.read()
    colab = derive_colab_count(readme)
    if colab != derived["notebooks"]:
        failures.append(
            f"README.md [Colab index]: links {colab} unique notebooks, "
            f"tree has {derived['notebooks']} — a notebook is missing its Colab row"
        )

    if failures:
        print(f"\nFAILED — {len(failures)} stale count(s):")
        for f in failures:
            print("  " + f)
        sys.exit(1)
    print(f"All {len(CHECKS) + 1} count locations agree with the tree.")


if __name__ == "__main__":
    main()
