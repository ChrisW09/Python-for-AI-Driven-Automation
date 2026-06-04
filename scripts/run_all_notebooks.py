#!/usr/bin/env python3
"""Execute every .ipynb under a root and exit non-zero on any unexpected error.

Usage:
    python scripts/run_all_notebooks.py .
    python scripts/run_all_notebooks.py . --json docs/notebook_execution_results.json

Designed for CI. Each notebook runs end-to-end with a fresh kernel and a
per-cell timeout. The notebook's own folder is used as the working directory.
Intentional 🐞 Debug-me cells (marked "INTENTIONALLY ERRORS") are reported with
status "xfail" and do NOT fail the run — only genuine regressions exit non-zero.
With --json, also writes a snapshot (one entry per notebook) in the schema
{notebook, status, cells_executed, duration_s, error}. Notebooks are executed
in memory and are never modified on disk.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError


DEFAULT_EXCLUDES = ["previous_versions", ".ipynb_checkpoints", "__pycache__", ".venv"]


def iter_notebooks(root: Path, exclude: list[str]) -> list[Path]:
    excludes = set(exclude) | set(DEFAULT_EXCLUDES)
    out: list[Path] = []
    for p in sorted(root.rglob("*.ipynb")):
        if any(part in excludes for part in p.parts):
            continue
        out.append(p)
    return out


def _first_error(nb) -> dict | None:
    for i, c in enumerate(nb.cells):
        if c.cell_type != "code":
            continue
        for o in c.get("outputs", []):
            if o.get("output_type") == "error":
                return {"cell_index": i, "ename": o.get("ename"),
                        "evalue": (o.get("evalue") or "")[:200]}
    return None


def _cells_executed(nb) -> int:
    return sum(1 for c in nb.cells
               if c.cell_type == "code" and c.get("execution_count") is not None)


def run_one(nb_path: Path, root: Path, timeout: int) -> dict:
    """Execute one notebook in memory; return a snapshot-schema result dict."""
    rel = nb_path.relative_to(root).as_posix()
    start = time.time()
    try:
        nb = nbformat.read(str(nb_path), as_version=4)
    except Exception as e:
        return {"notebook": rel, "status": "fail", "cells_executed": 0,
                "duration_s": round(time.time() - start, 2),
                "error": {"cell_index": None, "ename": "LoadError", "evalue": str(e)[:200]}}
    client = NotebookClient(
        nb, timeout=timeout, kernel_name="python3",
        resources={"metadata": {"path": str(nb_path.parent)}},
        allow_errors=False,
    )
    try:
        client.execute()
        return {"notebook": rel, "status": "pass", "cells_executed": _cells_executed(nb),
                "duration_s": round(time.time() - start, 2), "error": None}
    except CellExecutionError as e:
        err = _first_error(nb) or {"cell_index": None, "ename": "CellExecutionError",
                                   "evalue": str(e)[:200]}
        # An intentional 🐞 Debug-me cell is an *expected* failure, not a regression.
        ci = err.get("cell_index")
        intentional = (ci is not None
                       and "INTENTIONALLY ERRORS" in "".join(nb.cells[ci].source).upper())
        return {"notebook": rel, "status": "xfail" if intentional else "fail",
                "cells_executed": _cells_executed(nb),
                "duration_s": round(time.time() - start, 2), "error": err}
    except Exception as e:
        return {"notebook": rel, "status": "fail", "cells_executed": _cells_executed(nb),
                "duration_s": round(time.time() - start, 2),
                "error": {"cell_index": None, "ename": type(e).__name__, "evalue": str(e)[:200]}}


def _note(res: dict) -> str:
    if res["status"] == "pass":
        return f"{res['duration_s']}s"
    e = res.get("error") or {}
    loc = f"cell {e['cell_index']} " if e.get("cell_index") is not None else ""
    prefix = "(expected) " if res["status"] == "xfail" else ""
    return f"{prefix}{loc}{e.get('ename')}: {(e.get('evalue') or '')[:160]}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", help="folder to walk for notebooks")
    ap.add_argument("--exclude", action="append", default=[],
                    help="sub-folder (relative to root) to skip; can repeat")
    ap.add_argument("--timeout", type=int, default=120, help="per-cell timeout in seconds")
    ap.add_argument("--json", dest="json_path", default=None,
                    help="also write a JSON snapshot of the results to this path")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    nbs = iter_notebooks(root, args.exclude)
    if not nbs:
        print(f"No notebooks found under {root}", file=sys.stderr)
        return 1

    MARK = {"pass": "✅", "xfail": "🐞", "fail": "❌"}
    results: list[dict] = []
    failures = 0
    xfails = 0
    for nb in nbs:
        res = run_one(nb, root, args.timeout)
        results.append(res)
        print(f"  {MARK.get(res['status'], '❌')} {res['notebook']}  {_note(res)}", flush=True)
        if res["status"] == "fail":
            failures += 1
        elif res["status"] == "xfail":
            xfails += 1

    if args.json_path:
        Path(args.json_path).write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
        print(f"\nWrote snapshot: {args.json_path}")

    npass = len(nbs) - failures - xfails
    print()
    xnote = f" ({xfails} intentional 🐞 Debug-me xfail{'s' if xfails != 1 else ''})" if xfails else ""
    if failures:
        print(f"❌ {failures} / {len(nbs)} notebooks failed unexpectedly{xnote}")
        return 1
    print(f"✅ {npass} / {len(nbs)} notebooks executed cleanly{xnote}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
