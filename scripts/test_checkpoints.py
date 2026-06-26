#!/usr/bin/env python
"""Validate — and optionally execute — the inline "✋ Quick exercise" checkpoints.

Every lesson embeds short checkpoints as a three-cell block:
    1. a markdown prompt containing "Quick exercise (~2 min)"
    2. a "# ✍️ Your turn" starter cell (code) or a markdown reflection cell
    3. a collapsible markdown "✅ Solution"

Fast mode (default) — needs only `nbformat`; this is what CI runs:
    * every checkpoint has the 3-cell structure,
    * every "Your turn" code cell and every Python solution parses (no syntax errors).

    python scripts/test_checkpoints.py                 # all course notebooks
    python scripts/test_checkpoints.py path/to/nb.ipynb # specific notebooks

Exec mode — also injects each checkpoint's solution as a real cell and runs the
whole notebook in a kernel (needs the course deps + ipykernel):

    python scripts/test_checkpoints.py --exec [--timeout 300]

Exits non-zero if any check fails.
"""
import argparse
import ast
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPT_MARK = "Quick exercise (~2 min)"
SCAFFOLD_MARK = "✍️ Your turn"  # ✍️ Your turn
PY_FENCE = re.compile(r"```python\s*\n(.*?)```", re.DOTALL)

FOLDERS = [
    "00_onboarding", "01_foundations", "02_data_science", "03_real_world_io",
    "04_machine_learning", "05_industry_applications", "06_ai_engineering",
    "07_building_ai_pocs", "08_agents_tools_mcp", "09_nlp", "10_deeptab",
    "11_production", "13_capstones", "14_business_ai", "fast_track",
]


def discover():
    nbs = []
    for fo in FOLDERS:
        nbs.extend(sorted(glob.glob(os.path.join(ROOT, fo, "*.ipynb"))))
    return nbs


def src(cell):
    s = cell.get("source", "")
    return s if isinstance(s, str) else "".join(s)


def extract_solution_code(md_source):
    m = PY_FENCE.search(md_source)
    return m.group(1).rstrip() if m else None


def is_file_content(code):
    """Solution that is *file content* (an __init__.py / pytest test / TOML) meant
    to live in a file, not run as a notebook cell. Never injected/executed."""
    return bool(
        re.search(r"(?m)^\s*from \.", code)
        or "@pytest" in code
        or re.search(r"(?m)^\s*def test_", code)
        or re.search(r"(?m)^\s*\[tool\.", code)
    )


def find_checkpoints(cells):
    """Yield (prompt_idx, prompt_cell, mid_cell_or_None, sol_cell_or_None)."""
    for i, c in enumerate(cells):
        if c.get("cell_type") == "markdown" and PROMPT_MARK in src(c):
            mid = cells[i + 1] if i + 1 < len(cells) else None
            sol = cells[i + 2] if i + 2 < len(cells) else None
            yield i, c, mid, sol


def check_structure_and_syntax(path):
    import nbformat
    problems = []
    try:
        nb = nbformat.read(path, as_version=4)
    except Exception as e:  # noqa: BLE001
        return [f"unreadable: {type(e).__name__}: {e}"], 0
    cells = nb.cells
    n = 0
    for i, _prompt, mid, sol in find_checkpoints(cells):
        n += 1
        tag = f"cp@{i}"
        if mid is None or sol is None:
            problems.append(f"{tag}: incomplete 3-cell block")
            continue
        sol_src = src(sol)
        if "<details>" not in sol_src or "Solution" not in sol_src:
            problems.append(f"{tag}: solution cell missing collapsible <details>/Solution")
        # syntax-check the 'Your turn' starter if it is code
        if mid.get("cell_type") == "code":
            try:
                ast.parse(src(mid))
            except SyntaxError as e:
                problems.append(f"{tag}: scaffold syntax error: {e}")
        # syntax-check the python solution (file-content solutions are valid too)
        code = extract_solution_code(sol_src)
        if code:
            try:
                ast.parse(code)
            except SyntaxError as e:
                problems.append(f"{tag}: solution syntax error: {e}")
    return problems, n


def run_kernel(path, timeout):
    """Inject each (non-file-content) solution as a real cell and execute the
    notebook; report errors in injected solution or scaffold cells."""
    import copy
    import nbformat
    from nbclient import NotebookClient

    nb = nbformat.read(path, as_version=4)
    cells = nb.cells
    out, n_inj = [], 0
    i = 0
    while i < len(cells):
        c = cells[i]
        out.append(c)
        if c.cell_type == "markdown" and PROMPT_MARK in src(c) and i + 2 < len(cells):
            out.append(cells[i + 1])
            sol = cells[i + 2]
            out.append(sol)
            code = extract_solution_code(src(sol)) if sol.cell_type == "markdown" else None
            if code and not is_file_content(code):
                inj = nbformat.v4.new_code_cell(source=code)
                inj.metadata["ckpt_injected"] = True
                out.append(inj)
                n_inj += 1
            i += 3
            continue
        i += 1
    run_nb = copy.deepcopy(nb)
    run_nb.cells = out
    client = NotebookClient(
        run_nb, timeout=timeout, allow_errors=True, kernel_name="python3",
        resources={"metadata": {"path": os.path.dirname(os.path.abspath(path))}},
    )
    problems = []
    try:
        client.execute()
    except Exception as e:  # noqa: BLE001
        return [f"kernel crashed: {type(e).__name__}: {str(e)[:160]}"], n_inj
    for cell in run_nb.cells:
        if cell.cell_type != "code":
            continue
        injected = cell.metadata.get("ckpt_injected")
        scaffold = SCAFFOLD_MARK in src(cell)
        if not (injected or scaffold):
            continue  # ignore errors in original cells (e.g. intentional debug-me)
        for o in cell.get("outputs", []):
            if o.get("output_type") == "error":
                kind = "solution" if injected else "scaffold"
                problems.append(f"{kind} error: {o.get('ename')}: {(o.get('evalue') or '')[:90]}")
                break
    return problems, n_inj


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("notebooks", nargs="*", help="specific notebooks (default: all course notebooks)")
    ap.add_argument("--exec", dest="do_exec", action="store_true", help="also run each notebook in a kernel")
    ap.add_argument("--timeout", type=int, default=300, help="per-cell kernel timeout (exec mode)")
    args = ap.parse_args()

    nbs = [os.path.abspath(p) for p in args.notebooks] or discover()
    total_cp, total_fail = 0, 0
    failed = []
    for path in nbs:
        rel = os.path.relpath(path, ROOT)
        problems, n = check_structure_and_syntax(path)
        total_cp += n
        if args.do_exec and not problems:
            kp, _ = run_kernel(path, args.timeout)
            problems += kp
        mark = "ok  " if not problems else "FAIL"
        suffix = "" if not problems else "  <-- " + "; ".join(problems[:4])
        print(f"{mark} {rel:58} checkpoints={n}{suffix}")
        if problems:
            total_fail += 1
            failed.append(rel)

    mode = "structure+syntax+exec" if args.do_exec else "structure+syntax"
    print(f"\n{len(nbs)} notebooks · {total_cp} checkpoints · mode={mode}")
    if total_fail:
        print(f"FAILED: {total_fail} notebook(s): {', '.join(failed)}")
        sys.exit(1)
    print("All checkpoints OK.")


if __name__ == "__main__":
    main()
