import json, os, ast, sys

base = "05_industry_applications"

def md(cid, text):
    lines = text.split("\n")
    src = [l + "\n" for l in lines[:-1]] + [lines[-1]]
    if text.endswith("\n"):
        src = [l + "\n" for l in lines if l != ""] if False else src
    return {"cell_type": "markdown", "id": cid, "metadata": {}, "source": src}

def code(cid, text):
    ast.parse(text)  # validate
    lines = text.split("\n")
    src = [l + "\n" for l in lines[:-1]] + [lines[-1]]
    return {"cell_type": "code", "id": cid, "metadata": {}, "execution_count": None, "outputs": [], "source": src}

def find_after(cells, predicate):
    for i, c in enumerate(cells):
        if predicate("".join(c["source"]), c):
            return i
    raise SystemExit("anchor not found")

def insert(cells, idx, new_cells):
    return cells[:idx] + new_cells + cells[idx:]

# ----------------------------------------------------------------------------
# NB 17 — churn: rank by EV, not by churn probability
# ----------------------------------------------------------------------------
def nb17(nb):
    cells = nb["cells"]
    # Misconception right after the EV-rule heading cell (## 4 ...)
    misc = md("churn35-misc-001",
        '> 🚫 **Misconception — "Rank customers by churn probability and target from the top down."**\n'
        '> Churn probability is only *half* the equation. The expected value of a save is '
        '`p × save_rate × CLV − cost`, so a low-risk Enterprise account can be worth far more than a '
        'near-certain Basic churner. Rank by **expected value**, not by `p` — the order can flip completely.')
    i_head = find_after(cells, lambda s, c: c["cell_type"] == "markdown" and s.startswith("## 4. From probability to decision"))
    cells = insert(cells, i_head + 1, [misc])

    # Prediction after the "Reading the sweep" cell
    pred_md = md("churn35-pred-001",
        '### 🔮 Predict the output\n\n'
        'Two customers, same retention offer (save rate `s = 0.30`, cost `€60`). We rank them two ways: '
        'by raw **churn probability**, and by **expected value** `p × s × CLV − 60`. Does the priority order stay the same?\n\n'
        '```python\n'
        'cust = [\n'
        '    {"name": "Basic-Bob",  "p": 0.80, "clv":   400},   # very likely to churn, low value\n'
        '    {"name": "Ent-Eve",    "p": 0.20, "clv": 5000},   # unlikely to churn, high value\n'
        ']\n'
        's, cost = 0.30, 60\n'
        'by_p  = sorted(cust, key=lambda c: -c["p"])\n'
        'by_ev = sorted(cust, key=lambda c: -(c["p"]*s*c["clv"] - cost))\n'
        'print("by prob:", [c["name"] for c in by_p])\n'
        'print("by EV:  ", [c["name"] for c in by_ev])\n'
        '```\n\n'
        'Do the two lists print in the **same** order, or does the EV ranking put a *different* customer first?')
    pred_code = code("churn35-pred-002",
        '# Predict first, then run.\n'
        'cust = [\n'
        '    {"name": "Basic-Bob",  "p": 0.80, "clv":   400},   # very likely to churn, low value\n'
        '    {"name": "Ent-Eve",    "p": 0.20, "clv": 5000},   # unlikely to churn, high value\n'
        ']\n'
        's, cost = 0.30, 60\n'
        'by_p  = sorted(cust, key=lambda c: -c["p"])\n'
        'by_ev = sorted(cust, key=lambda c: -(c["p"]*s*c["clv"] - cost))\n'
        'for c in cust:\n'
        '    print(f\'{c["name"]:11s}  p={c["p"]:.2f}  CLV={c["clv"]:>5}  EV={c["p"]*s*c["clv"]-cost:+.0f}\')\n'
        'print("by prob:", [c["name"] for c in by_p])\n'
        'print("by EV:  ", [c["name"] for c in by_ev])')
    pred_ans = md("churn35-pred-003",
        '<details>\n<summary>💡 <b>Answer</b></summary>\n\n'
        '**The order flips.** By probability, Basic-Bob (p=0.80) ranks first. But his EV is '
        '`0.80 × 0.30 × 400 − 60 = +€36`, while Ent-Eve\'s is `0.20 × 0.30 × 5000 − 60 = +€240` — '
        'nearly 7× more. With a limited budget you call **Ent-Eve first**. Ranking by raw churn '
        'probability quietly optimizes the wrong objective; ranking by expected value targets the money.\n'
        '</details>')
    i_read = find_after(cells, lambda s, c: c["cell_type"] == "markdown" and s.startswith("### Reading the sweep"))
    cells = insert(cells, i_read + 1, [pred_md, pred_code, pred_ans])
    nb["cells"] = cells

# ----------------------------------------------------------------------------
# NB 18 — fraud: precision@k vs recall@k as the queue grows
# ----------------------------------------------------------------------------
def nb18(nb):
    cells = nb["cells"]
    misc = md("fraud36-misc-001",
        '> 🚫 **Misconception — "Just make the alert queue bigger to catch more fraud."**\n'
        '> A larger queue (bigger *k*) does raise **recall@k** — but each extra alert is more likely a false '
        'alarm, so **precision@k** falls and analyst review cost climbs. The two metrics move in *opposite* '
        'directions as *k* grows; the right queue size is set by the cost of a review vs the value of a catch, '
        'not by "more is better".')
    i_head = find_after(cells, lambda s, c: c["cell_type"] == "markdown" and s.startswith("## 5. The alert queue"))
    cells = insert(cells, i_head + 1, [misc])

    pred_md = md("fraud36-pred-001",
        '### 🔮 Predict the output\n\n'
        'A tiny scored day: 10 transactions, exactly **2 are fraud**, sorted by descending risk score. '
        'The flags below mark fraud (`1`) in score order — the top 2 are caught, then a gap, then the last fraud.\n\n'
        '```python\n'
        '# rows sorted high->low risk; 1 = fraud. Two frauds total.\n'
        'flags = [1, 1, 0, 0, 0, 0, 0, 0, 0, 1]\n'
        'total_fraud = sum(flags)\n'
        'def at_k(k):\n'
        '    caught = sum(flags[:k])\n'
        '    return caught / k, caught / total_fraud   # precision@k, recall@k\n'
        'for k in (2, 5):\n'
        '    p, r = at_k(k)\n'
        '    print(f"k={k}: precision={p:.2f}  recall={r:.2f}")\n'
        '```\n\n'
        'Going from k=2 to k=5, which way does **precision@k** move, and which way does **recall@k** move?')
    pred_code = code("fraud36-pred-002",
        '# Predict first, then run.\n'
        'flags = [1, 1, 0, 0, 0, 0, 0, 0, 0, 1]   # sorted high->low risk; 1 = fraud\n'
        'total_fraud = sum(flags)\n'
        'def at_k(k):\n'
        '    caught = sum(flags[:k])\n'
        '    return caught / k, caught / total_fraud\n'
        'for k in (2, 5):\n'
        '    p, r = at_k(k)\n'
        '    print(f"k={k}: precision={p:.2f}  recall={r:.2f}")')
    pred_ans = md("fraud36-pred-003",
        '<details>\n<summary>💡 <b>Answer</b></summary>\n\n'
        '**They move in opposite directions.** At k=2 both frauds you can cheaply reach are the top 2: '
        '`precision=1.00, recall=0.50`. Stretching to k=5 adds three legit transactions and no new fraud — '
        '`precision` drops to `0.40` while `recall` stays `0.50`. Growing the queue trades precision for '
        'recall; you only gain recall once a deeper fraud finally enters the window. There is no free lunch — '
        'pick *k* from the cost of a review vs the value of a catch.\n'
        '</details>')
    i_curve = find_after(cells, lambda s, c: c["cell_type"] == "markdown" and s.startswith("### The staffing trade-off as a curve"))
    cells = insert(cells, i_curve, [pred_md, pred_code, pred_ans])
    nb["cells"] = cells

# ----------------------------------------------------------------------------
# NB 19 — segmentation: inertia always drops as k grows (more clusters != better)
# ----------------------------------------------------------------------------
def nb19(nb):
    cells = nb["cells"]
    misc = md("seg37-misc-001",
        '> 🚫 **Misconception — "More clusters are always better — higher k fits the data more tightly."**\n'
        '> Inertia (within-cluster distance) *always* drops as you add clusters — at k = n every point is its '
        'own cluster with inertia 0. A lower inertia number is **not** a better segmentation; it just means '
        'finer slicing. Choose k by the **elbow** (where extra clusters stop paying off) plus whether each '
        'segment is *actionable*, not by minimizing inertia.')
    i_head = find_after(cells, lambda s, c: c["cell_type"] == "markdown" and "## 3. K-means" in s)
    cells = insert(cells, i_head + 1, [misc])

    pred_md = md("seg37-pred-001",
        '### 🔮 Predict the output\n\n'
        'Four points on a line. We run k-means for k = 1, 2, 3, 4 and print the **inertia** '
        '(sum of squared distances to each point\'s own centroid).\n\n'
        '```python\n'
        'import numpy as np\n'
        'from sklearn.cluster import KMeans\n'
        'X = np.array([[0.], [1.], [10.], [11.]])   # two tight pairs, far apart\n'
        'for k in (1, 2, 3, 4):\n'
        '    inertia = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X).inertia_\n'
        '    print(f"k={k}: inertia={inertia:.1f}")\n'
        '```\n\n'
        'As k goes 1→4, does inertia ever go **up**? And does the big drop tell you the "true" number of clusters here?')
    pred_code = code("seg37-pred-002",
        '# Predict first, then run.\n'
        'import numpy as np\n'
        'from sklearn.cluster import KMeans\n'
        'X = np.array([[0.], [1.], [10.], [11.]])   # two tight pairs, far apart\n'
        'for k in (1, 2, 3, 4):\n'
        '    inertia = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X).inertia_\n'
        '    print(f"k={k}: inertia={inertia:.1f}")')
    pred_ans = md("seg37-pred-003",
        '<details>\n<summary>💡 <b>Answer</b></summary>\n\n'
        '**Inertia only ever falls (or ties) — never rises.** It goes `k=1: 121.0 → k=2: 1.0 → '
        'k=3: 0.5 → k=4: 0.0`. The collapse from k=1 to k=2 is the **elbow**: that\'s where the two real '
        'groups get separated. After that, extra clusters just split tight pairs for a tiny gain. At k=4 '
        'inertia is 0 — a "perfect" fit that segments nothing. Lower inertia is not a better segmentation; '
        'the elbow (here k=2) is.\n'
        '</details>')
    i_loop = find_after(cells, lambda s, c: c["cell_type"] == "markdown" and s.startswith("### 🔬 What actually happens inside k-means"))
    cells = insert(cells, i_loop, [pred_md, pred_code, pred_ans])
    nb["cells"] = cells

# ----------------------------------------------------------------------------
# NB 20 — demand: safety stock grows super-linearly with service level
# ----------------------------------------------------------------------------
def nb20(nb):
    cells = nb["cells"]
    misc = md("dm38-misc-001",
        '> 🚫 **Misconception — "A 99% service level is the safe default — just set it high."**\n'
        '> Safety stock is `z × σ`, and the normal quantile `z` blows up near the tail: z(90%)=1.28, '
        'z(95%)=1.64, z(99%)=2.33, z(99.9%)=3.09. The last few points of service level cost '
        '**super-linearly** more capital. "Safe" is not free — the right service level comes from the '
        'shortage-vs-holding cost trade-off, not from rounding up to 99%.')
    i_head = find_after(cells, lambda s, c: c["cell_type"] == "markdown" and "### 3. From forecast error to safety stock" in s)
    cells = insert(cells, i_head + 1, [misc])

    pred_md = md("dm38-pred-001",
        '### 🔮 Predict the output\n\n'
        'Safety stock is `z(service_level) × σ`. With the *same* demand variability (`σ = 50` units), '
        'we step the service level up in **equal 4-point jumps** and print the extra units each jump buys.\n\n'
        '```python\n'
        'from scipy import stats\n'
        'sigma = 50\n'
        'levels = [0.90, 0.95, 0.99]\n'
        'ss = [stats.norm.ppf(p) * sigma for p in levels]\n'
        'print("90%->95%: +%.0f units" % (ss[1] - ss[0]))\n'
        'print("95%->99%: +%.0f units" % (ss[2] - ss[1]))\n'
        '```\n\n'
        'Both steps are +4 service points. Does the second jump (95→99) cost about the **same** extra units as the first (90→95), or noticeably **more**?')
    pred_code = code("dm38-pred-002",
        '# Predict first, then run.\n'
        'from scipy import stats\n'
        'sigma = 50\n'
        'for p in (0.90, 0.95, 0.99, 0.999):\n'
        '    print(f"service {p:>6.1%}  ->  z={stats.norm.ppf(p):.2f}  ->  safety stock {stats.norm.ppf(p)*sigma:5.0f} units")\n'
        'ss = [stats.norm.ppf(p) * sigma for p in (0.90, 0.95, 0.99)]\n'
        'print(f"90%->95% costs +{ss[1]-ss[0]:.0f} units;  95%->99% costs +{ss[2]-ss[1]:.0f} units")')
    pred_ans = md("dm38-pred-003",
        '<details>\n<summary>💡 <b>Answer</b></summary>\n\n'
        '**The second jump costs much more, even though both add 4 service points.** '
        '90→95% adds about `+18` units (z 1.28→1.64), but 95→99% adds about `+34` units (z 1.64→2.33) — '
        'nearly double, for the *same* 4-point gain. And 99→99.9% adds another `+38`. The quantile `z` curves '
        'up steeply in the tail, so chasing the last sliver of service level ties up disproportionately more '
        'capital. That curvature is exactly why "set it to 99% to be safe" is an expensive default.\n'
        '</details>')
    i_after_table = find_after(cells, lambda s, c: c["cell_type"] == "markdown" and s.startswith("### See the backtest"))
    cells = insert(cells, i_after_table, [pred_md, pred_code, pred_ans])
    nb["cells"] = cells

specs = {
    "17_churn_clv_retention": nb17,
    "18_fraud_anomaly_detection": nb18,
    "19_segmentation_recommenders": nb19,
    "20_demand_maintenance": nb20,
}

for name, fn in specs.items():
    path = os.path.join(base, name + ".ipynb")
    nb = json.load(open(path))
    before = len(nb["cells"])
    fn(nb)
    # validate all code cells parse
    for c in nb["cells"]:
        if c["cell_type"] == "code":
            ast.parse("".join(c["source"]))
    # unique ids
    ids = [c.get("id") for c in nb["cells"] if c.get("id")]
    assert len(ids) == len(set(ids)), f"dup id in {name}: {[x for x in ids if ids.count(x)>1]}"
    json.dump(nb, open(path, "w"), indent=1, ensure_ascii=False)
    print(f"{name}: {before} -> {len(nb['cells'])} cells, ids unique OK")

print("done")
