"""NB18 fraud: add PR-curve (vs prevalence baseline) and static queue-economics curve."""
import json
PATH="05_industry_applications/18_fraud_anomaly_detection.ipynb"
nb=json.load(open(PATH)); cells=nb["cells"]
def md(t,k): return {"cell_type":"markdown","id":f"impr-md-{k}","metadata":{},"source":t.splitlines(keepends=True)}
def code(s,k): return {"cell_type":"code","id":f"impr-cd-{k}","metadata":{},"execution_count":None,"outputs":[],"source":s.splitlines(keepends=True)}
def iid(cid):
    for i,c in enumerate(cells):
        if c.get("id")==cid: return i
    raise SystemExit("missing "+cid)

pr_md=md("""### The precision–recall curve — the right picture for rare events

At 0.5% prevalence the ROC-AUC looked flattering; the **PR curve** is the honest view because it ignores the huge, easy true-negative mass and focuses on the positives. The dashed line is what *random* guessing scores (a flat line at the prevalence rate) — any useful detector must sit well above it.
""","pr1")
pr_cd=code('''from sklearn.metrics import precision_recall_curve

prevalence = test["fraud"].mean()
fig, ax = plt.subplots(figsize=(8, 5))
for name, sc, color in [("Supervised GBM", score_sup, "#4C72B0"),
                        ("Isolation Forest", score_iso, "#DD8452")]:
    p, r, _ = precision_recall_curve(test["fraud"], sc)
    ap = average_precision_score(test["fraud"], sc)
    ax.plot(r, p, lw=2.5, color=color, label=f"{name}  (PR-AUC = {ap:.3f})")
ax.axhline(prevalence, ls="--", color="grey", lw=1.5,
           label=f"random guessing = prevalence ({prevalence:.2%})")
ax.set(xlabel="recall (share of all fraud caught)",
       ylabel="precision (share of alerts that are real fraud)",
       title="Precision–Recall curve — supervised vs unsupervised", ylim=(0, 1.02))
ax.legend(loc="upper right"); sns.despine(); plt.tight_layout(); plt.show()
''',"pr2")

q_md=md("""### The staffing trade-off as a curve (no widget needed)

The slider above is fun live, but the decision is clearer as a static chart: sweep the **daily alert budget** and plot precision@k, recall@k, and the **EUR prevented** it implies. The review team picks a column on this chart — the point where catching one more fraud stops being worth the review cost.
""","q1")
q_cd=code('''daily = np.arange(10, 301, 10)
total = int(test["fraud"].sum())
precs, recs, prevented = [], [], []
for d in daily:
    k = d * 30
    idx = np.argsort(-score_sup)[:k]
    caught = int(test["fraud"].iloc[idx].sum())
    precs.append(caught / k)
    recs.append(caught / total)
    prevented.append(caught * AVG_FRAUD_LOSS - k * REVIEW_COST)

best = int(np.argmax(prevented))
fig, ax1 = plt.subplots(figsize=(9, 5))
ax1.plot(daily, precs, color="#4C72B0", lw=2.5, label="precision@k")
ax1.plot(daily, recs,  color="#C44E52", lw=2.5, label="recall@k")
ax1.set(xlabel="alert budget (reviews per day)", ylabel="precision / recall", ylim=(0, 1.02))
ax2 = ax1.twinx()
ax2.plot(daily, prevented, color="#55A868", lw=2.5, ls="--", label="EUR prevented (30d)")
ax2.axvline(daily[best], color="#55A868", lw=1, alpha=0.5)
ax2.set_ylabel("EUR prevented over 30 days")
ax1.legend(loc="center left"); ax2.legend(loc="lower right")
ax1.set_title(f"Where metrics meet staffing — net value peaks near {daily[best]} alerts/day "
              f"(€{prevented[best]:,.0f})")
sns.despine(right=False); plt.tight_layout(); plt.show()
''',"q2")

ins=sorted([
    (iid("cell-011")+1,[pr_md,pr_cd]),     # after Isolation Forest (both scores exist)
    (iid("0b8f6eb9")+1,[q_md,q_cd]),       # after the interactive widget
],key=lambda t:t[0],reverse=True)
for at,new in ins: cells[at:at]=new
nb["cells"]=cells
json.dump(nb,open(PATH,"w"),indent=1,ensure_ascii=False)
print(f"NB18 done — {len(cells)} cells")
