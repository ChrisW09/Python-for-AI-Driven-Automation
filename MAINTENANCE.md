# 🔧 Maintenance guide

Almost all of this course is deliberately **stable**: data is generated inline, the heavy vendors are mocked, and everything runs offline — those notebooks don't rot. What drifts is the small set of surfaces that describe the *outside world*: model names, prices, library versions, and regulation dates. This file is the quarterly checklist for exactly those surfaces, plus the verification gates that any edit must pass.

## Quarterly currency pass (~1–2 h)

Work through the table; most quarters most rows need nothing.

| Surface | What to check | Where |
|---|---|---|
| **LLM provider shim** | Default model IDs still current & cheapest-sensible per provider (OpenAI / Anthropic / Google / Ollama); docstring examples match | [`llm_providers.py`](./llm_providers.py) |
| **Provider guide** | Model tables, prices, context windows, free-tier claims | [`08_ai_engineering/A1_llm_providers_guide.ipynb`](./08_ai_engineering/A1_llm_providers_guide.ipynb) |
| **Vector-store survey** | Product landscape claims (hosted tiers, licenses) | [`08_ai_engineering/A2_vector_stores_survey.ipynb`](./08_ai_engineering/A2_vector_stores_survey.ipynb) |
| **RAG/agent framework survey** | Framework API idioms still current (LangChain/LlamaIndex move fast) | [`08_ai_engineering/A3_rag_and_agent_frameworks.ipynb`](./08_ai_engineering/A3_rag_and_agent_frameworks.ipynb) |
| **DeepTab** | Version claim (v2 split-config API) matches the released package | [`12_deeptab/`](./12_deeptab/) |
| **CAFE** | Package API + [cafe-ai.de](https://cafe-ai.de) links | [`18_compound_ai_evaluation/`](./18_compound_ai_evaluation/) |
| **EU AI Act section** | Obligation dates phrased as future become past as they arrive (next milestone: Annex I embedded high-risk, Aug 2027) | [`16_business_ai/52_bpm_governance_poc_mvp.ipynb`](./16_business_ai/52_bpm_governance_poc_mvp.ipynb) §5 |
| **Colab claims** | "Colab ships PyTorch preinstalled" and friends still true | root `README.md`, Module 6 |
| **Optional requirements** | Commented pins in `requirements.txt` still install cleanly on a fresh venv (spot-check the ones you touch) | [`requirements.txt`](./requirements.txt) |
| **Tools named in honest sections** | Module 7's appendices name the tools real teams reach for (Robyn / PyMC-Marketing in A9, OR-Tools in A11, `lifelines` in A5, off-policy evaluation libraries in A14). No code depends on them, but the claim "this is what the industry uses" ages | [`07_industry_applications/`](./07_industry_applications/) |
| **External links** | `make -C docs_site linkcheck` output is empty (exclusions live in `conf.py`) | `docs_site/` |

Anything *not* on this list — synthetic-data lessons, statistics, sklearn/pandas idioms — only needs attention when a library's own API deprecates something (CI's execution sweep will surface that).

## Verification gates (run after ANY notebook edit)

1. **Re-execute edited notebooks in place** — outputs are committed deliberately:
   `jupyter nbconvert --to notebook --execute --inplace <nb>`
   (exception: NB 24 hangs under `--inplace`; use `--output tmp` and move back).
2. **Checkpoints:** `python3 scripts/test_checkpoints.py` — must end "All checkpoints OK" (add `--exec` for the full kernel gate on the notebooks you touched).
3. **Solution fences:** every ```` ```python ```` fence inside a `<details>` block is *never* executed by nbconvert — extract them into a throwaway copy and run them against the notebook's final state (the `run_solutions` pattern) before trusting them.
4. **Cross-references:** `python3 scripts/check_nb_references.py`.
5. **Counts:** `python3 scripts/check_course_counts.py` — notebook/checkpoint/appendix totals in the README, docs index and 00b must match the tree (CI enforces this too).
6. **Docs:** `make -C docs_site html` builds with `-W`; `make -C docs_site linkcheck` output should be empty.

## Adding a notebook or a module

Most of the gates above are self-explanatory once they fail. Three are not, because they enforce
conventions encoded in file *names* and in the docs sidebar:

- **Appendix filenames** must be `A<n>_<slug>.ipynb` in a module directory. `check_course_counts.py`
  globs `A[0-9]*_*.ipynb`, so two-digit appendices (`A10_…`) count correctly — it globbed `A[0-9]_*`
  until Module 7 grew past nine appendices, which silently under-counted rather than failing.
- **A new module directory** must be added by hand to a `{toctree}` group in `docs_site/index.md`;
  the sidebar is grouped by theme rather than globbed, so `generate.py` refuses to build if the two
  disagree and names the module it could not place.
- **Every notebook needs a Colab row** in the root README's index — `check_course_counts.py` compares
  the number of unique Colab links against the tree and fails if one is missing.

When a module gains notebooks, the counts in the root README (badge, headline, "across the course",
appendix totals, Colab footnote), `docs_site/index.md`, and `00b_course_overview.ipynb` all move
together. Run gate 5 rather than trying to remember the list; it names each stale location.

## Editing rules that keep the course honest

- **Prose numbers must match printed output.** If a cell prints `+1.8 pp`, the paragraph below it says +1.8, not +1.9. After re-execution, re-read the surrounding prose.
- **Intentional bugs are content.** 🐞 Debug-me cells and anything marked "Buggy on purpose" / "💥" *should* error in committed output — don't "fix" them.
- **Audit the sibling.** Most lessons have a fast-track mirror; a defect found in one almost always lives in the other.
- **Never tune a decision threshold on the test set** — the course's most recurrent historical defect. Thresholds come from train/validation or from the economics (`D/V`, `PD* = m/(m+LGD)`), never from the eval argmax.
