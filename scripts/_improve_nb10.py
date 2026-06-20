"""NB10 statistics: add canonical visuals — mean/median skew, CLT, p-value tail, sample-size curve."""
import json
PATH="02_data_science/10_statistics_basics.ipynb"
nb=json.load(open(PATH)); cells=nb["cells"]
def md(t,k): return {"cell_type":"markdown","id":f"impr-md-{k}","metadata":{},"source":t.splitlines(keepends=True)}
def code(s,k): return {"cell_type":"code","id":f"impr-cd-{k}","metadata":{},"execution_count":None,"outputs":[],"source":s.splitlines(keepends=True)}
def iid(cid):
    for i,c in enumerate(cells):
        if c.get("id")==cid: return i
    raise SystemExit("missing "+cid)

# 1) mean vs median (after the print cell 914d9dfd)
mm_md=md("""**See why the mean lies here.** The numbers above say Model B's mean and median differ; this is *why*. The 10% slow spikes form a long right tail that drags the **mean** away from the bulk of users, while the **median** stays put. For latency you almost always want the median (or p99), not the mean.
""","mm1")
mm_cd=code('''m, md_ = float(np.mean(latency_b)), float(np.median(latency_b))
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.hist(latency_b, bins=40, color="#4C72B0", alpha=0.75)
ax.axvline(md_, color="#55A868", lw=2.5, label=f"median = {md_:.0f} ms  (robust)")
ax.axvline(m,   color="#C44E52", lw=2.5, label=f"mean = {m:.0f} ms  (pulled by the tail)")
ax.set(title="Model B latency — the spikes drag the mean right of the median",
       xlabel="latency (ms)", ylabel="number of calls")
ax.legend(); sns.despine(); plt.tight_layout(); plt.show()
print(f"The slow tail lifts the mean {m - md_:.0f} ms above the median — a 'typical' user is nowhere near the mean.")
''',"mm2")

# 2) CLT (after the Monte-Carlo proof cell st10-dd-003)
clt_md=md("""**The same proof, as a picture.** The table showed the standard error shrinking like σ/√n. Here are the *full sampling distributions*: draw thousands of samples at each `n`, histogram their means, and watch the curve grow taller and narrower as `n` rises — the Central Limit Theorem in one chart. This is *why* a bigger sample gives a more trustworthy mean.
""","clt1")
clt_cd=code('''clt_rng = np.random.default_rng(0)
fig, ax = plt.subplots(figsize=(9, 4.5))
for n, color in [(10, "#DD8452"), (30, "#4C72B0"), (100, "#55A868"), (300, "#C44E52")]:
    means = clt_rng.normal(MU, SIGMA, size=(4000, n)).mean(axis=1)
    ax.hist(means, bins=60, density=True, histtype="step", lw=2.2, color=color,
            label=f"n = {n:>3}   (SE ≈ {SIGMA/np.sqrt(n):.0f})")
ax.axvline(MU, color="black", ls=":", lw=1.5, label=f"true mean μ = {MU:.0f}")
ax.set(title="Central Limit Theorem — the sampling distribution of the mean narrows as n grows",
       xlabel="sample mean (ms)", ylabel="density")
ax.legend(title="sample size"); sns.despine(); plt.tight_layout(); plt.show()
''',"clt2")

# 3) p-value tail (after the permutation proof cell st10-dd-006)
pv_md=md("""**What a p-value *is*, drawn.** The cell above shuffled the pooled data thousands of times to build the world where H₀ is true. Plot that null distribution and the picture becomes obvious: the **p-value is just the shaded tail** — the fraction of null shuffles that landed at least as far out as what we actually observed.
""","pv1")
pv_cd=code('''fig, ax = plt.subplots(figsize=(9, 4.5))
ax.hist(null_diffs, bins=50, color="#4C72B0", alpha=0.7, label="|difference| under H₀ (shuffled)")
ax.axvspan(observed_diff, null_diffs.max(), color="#C44E52", alpha=0.18,
           label=f"tail ≥ observed  →  p = {p_simulated:.3f}")
ax.axvline(observed_diff, color="#C44E52", lw=2.5, label=f"observed = {observed_diff:.2f}")
ax.set(title="A p-value is a tail area: how often pure chance beats what we saw",
       xlabel="|difference of means| in a null (no-effect) world", ylabel="number of simulations")
ax.legend(); sns.despine(); plt.tight_layout(); plt.show()
''',"pv2")

# 4) sample-size curve (after cell ee1b2a6d)
ss_md=md("""**The table as a curve — and why small effects are so expensive.** Required sample size scales like 1/d², so halving the effect you want to detect *quadruples* the data you need. On a log axis the cliff is unmistakable.
""","ss1")
ss_cd=code('''ds = np.linspace(0.1, 1.2, 45)
ns = [sample_size_for_d(d) for d in ds]
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(ds, ns, lw=2.5, color="#C44E52")
for d in [0.2, 0.5, 0.8]:
    nd = sample_size_for_d(d)
    ax.plot(d, nd, "o", color="#4C72B0")
    ax.annotate(f"d={d} → n={nd:,}/group", (d, nd), textcoords="offset points",
                xytext=(10, 4), fontsize=9)
ax.set_yscale("log")
ax.set(title="Cost of detecting an effect (80% power, α = 0.05)",
       xlabel="effect size (Cohen's d)", ylabel="per-group sample size (log scale)")
sns.despine(); plt.tight_layout(); plt.show()
''',"ss2")

ins=sorted([
    (iid("914d9dfd")+1,[mm_md,mm_cd]),
    (iid("st10-dd-003")+1,[clt_md,clt_cd]),
    (iid("st10-dd-006")+1,[pv_md,pv_cd]),
    (iid("ee1b2a6d")+1,[ss_md,ss_cd]),
],key=lambda t:t[0],reverse=True)
for at,new in ins: cells[at:at]=new
nb["cells"]=cells
json.dump(nb,open(PATH,"w"),indent=1,ensure_ascii=False)
print(f"NB10 done — {len(cells)} cells")
