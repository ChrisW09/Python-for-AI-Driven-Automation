#!/usr/bin/env python3
"""Execute every .ipynb under a root and exit non-zero if any errors.

Usage:
    python scripts/run_all_notebooks.py refined_course
    python scripts/run_all_notebooks.py . --exclude refined_course

Designed for CI. Each notebook runs end-to-end with a fresh kernel and a
per-cell timeout. The notebook's own folder is used as the working directory.
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


DEFAULT_EXCLUDES = ["previous_versions", ".ipynb_checkpoints", "__pycache__"]


def iter_notebooks(root: Path, exclude: list[str]) -> list[Path]:
    excludes = set(exclude) | set(DEFAULT_EXCLUDES)
    out: list[Path] = []
    for p in sorted(root.rglob("*.ipynb")):
        if any(part in excludes for part in p.parts):
            continue
        out.append(p)
    return out


def run_one(nb_path: Path, timeout: int) -> tuple[bool, str]:
    start = time.time()
    try:
        nb = nbformat.read(str(nb_path), as_version=4)
    except Exception as e:
        return False, f"load error: {e}"
    client = NotebookClient(
        nb, timeout=timeout, kernel_name="python3",
        resources={"metadata": {"path": str(nb_path.parent)}},
        allow_errors=False,
    )
    try:
        client.execute()
        dt = time.time() - start
        return True, f"{dt:.1f}s"
    except CellExecutionError as e:
        # Pull the first error from the executed notebook
        for i, c in enumerate(nb.cells):
            if c.cell_type != "code":
                continue
            for o in c.get("outputs", []):
                if o.get("output_type") == "error":
                    return False, f"cell {i} {o.get('ename')}: {o.get('evalue', '')[:160]}"
        return False, f"CellExecutionError: {str(e)[:160]}"
    except Exception as e:
        return False, f"kernel error: {type(e).__name__}: {str(e)[:160]}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", help="folder to walk for notebooks")
    ap.add_argument("--exclude", action="append", default=[],
                    help="sub-folder (relative to root) to skip; can repeat")
    ap.add_argument("--timeout", type=int, default=120, help="per-cell timeout in seconds")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    nbs = iter_notebooks(root, args.exclude)
    if not nbs:
        print(f"No notebooks found under {root}", file=sys.stderr)
        return 1

    failures = 0
    for nb in nbs:
        rel = nb.relative_to(root)
        ok, note = run_one(nb, args.timeout)
        status = "✅" if ok else "❌"
        print(f"  {status} {rel}  {note}", flush=True)
        if not ok:
            failures += 1
    print()
    if failures:
        print(f"❌ {failures} / {len(nbs)} notebooks failed")
        return 1
    print(f"✅ All {len(nbs)} notebooks executed cleanly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
