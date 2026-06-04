#!/usr/bin/env python3
"""One-off: regenerate docs/notebook_execution_results.json with current paths.

Executes every course notebook end-to-end in-memory (notebooks are NOT modified
on disk) with the notebook's own folder as cwd, and records one entry per
notebook in the same schema the snapshot already uses:
    {notebook, status, cells_executed, duration_s, error}
Intentional Debug-me cells surface as status="fail" (raw execution truth), as
in the previous snapshot.
"""
from __future__ import annotations
import json, time, sys
from pathlib import Path
import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

ROOT = Path(__file__).resolve().parent.parent
ROOTS = ["00_onboarding", "01_foundations", "02_data_science", "03_real_world_io",
         "04_machine_learning", "05_ai_engineering", "06_production", "07_capstones",
         "08_business_ai", "09_building_ai_pocs", "fast_track", "quizzes"]
TIMEOUT = 300

def cells_executed(nb) -> int:
    return sum(1 for c in nb.cells
               if c.cell_type == "code" and c.get("execution_count") is not None)

def first_error(nb):
    for i, c in enumerate(nb.cells):
        if c.cell_type != "code":
            continue
        for o in c.get("outputs", []):
            if o.get("output_type") == "error":
                return {"cell_index": i, "ename": o.get("ename"),
                        "evalue": (o.get("evalue") or "")[:200]}
    return None

def run_one(p: Path) -> dict:
    rel = p.relative_to(ROOT).as_posix()
    start = time.time()
    nb = nbformat.read(str(p), as_version=4)
    client = NotebookClient(nb, timeout=TIMEOUT, kernel_name="python3",
                            resources={"metadata": {"path": str(p.parent)}},
                            allow_errors=False)
    try:
        client.execute()
        return {"notebook": rel, "status": "pass", "cells_executed": cells_executed(nb),
                "duration_s": round(time.time() - start, 2), "error": None}
    except CellExecutionError:
        return {"notebook": rel, "status": "fail", "cells_executed": cells_executed(nb),
                "duration_s": round(time.time() - start, 2), "error": first_error(nb)}
    except Exception as e:
        return {"notebook": rel, "status": "fail", "cells_executed": cells_executed(nb),
                "duration_s": round(time.time() - start, 2),
                "error": {"cell_index": None, "ename": type(e).__name__, "evalue": str(e)[:200]}}

def main() -> int:
    nbs = []
    for r in ROOTS:
        nbs += sorted((ROOT / r).glob("*.ipynb"))
    results = []
    for p in nbs:
        res = run_one(p)
        results.append(res)
        mark = "OK " if res["status"] == "pass" else "FAIL"
        print(f"  {mark} {res['notebook']}  {res['duration_s']}s"
              + (f"  [{res['error']['ename']}]" if res["error"] else ""), flush=True)
    out = ROOT / "docs" / "notebook_execution_results.json"
    out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    npass = sum(r["status"] == "pass" for r in results)
    print(f"\nWROTE {out.relative_to(ROOT)} — {npass}/{len(results)} pass")
    return 0

if __name__ == "__main__":
    sys.exit(main())
