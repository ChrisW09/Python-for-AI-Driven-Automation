# Module 4 — Web Scraping

> 🧭  [◀ Real-world I/O](../03_real_world_io/)  ·  [🏠 Course home](../README.md)  ·  [Machine Learning ▶](../05_machine_learning/)

**Goal:** Get data *off the web* responsibly — parse HTML yourself when the page is simple, reach for a managed API when pages fight back, and always prefer a clean open API when one exists. By the end you can pick the right tool for any "I need data from that website" problem and use it politely.

**Estimated time:** ~4 hours (three lessons of ~60–70 min each, plus exercises).
**Prerequisites:** Module 3 — NB 12 (HTTP & APIs, JSON) is essential; NB 13 (SQL) is helpful. NB 7 (pandas) throughout. NB 31 (document processing / structured extraction) helps with the Firecrawl lesson.

```
                    "I need data from that website."
                                 │
                 ┌───────────────┴───────────────────┐
                 ▼                                    ▼
      Is there an open API?  ── yes ─▶  Use it.  (NB 16 — OpenAlex)
                 │                       cleanest, most stable, most polite
                 no
                 ▼
      Is the page static HTML?  ── yes ─▶  Parse it yourself.
                 │                          (NB 14 — requests + BeautifulSoup)
                 no  (JavaScript-rendered / anti-bot / messy)
                 ▼
      Use a managed scraper.  ──────────▶  (NB 15 — Firecrawl → markdown / typed JSON)
```

Everything in this module runs **100% offline**: NB 14 parses an inline mock website, NB 15 uses a built-in `MockFirecrawl`, and NB 16 ships a canned OpenAlex snapshot that automatically upgrades to the live API when a network is present. No API key is ever required.

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll build |
|---|---|---|---|---|
| 47 | `14_web_scraping_fundamentals.ipynb` | ~70 min | Intermediate | A polite, paginated scraper — BeautifulSoup, CSS selectors, tables → pandas, `robots.txt`, throttling & caching |
| 48 | `15_scraping_with_firecrawl.ipynb` | ~60 min | Intermediate | Managed scraping with Firecrawl — scrape/crawl/map/search, schema-driven **typed JSON** extraction |
| 49 | `16_openalex_scholarly_data.ipynb` | ~65 min | Intermediate | A scholarly-data pipeline on the **OpenAlex** open API — filtering, cursor pagination, a citations mini-analysis |

## Notebook guides

### 47 · Web Scraping Fundamentals — `14_web_scraping_fundamentals.ipynb`

The foundation: how to pull structured data out of raw HTML with `requests` + **BeautifulSoup**, and how to do it without getting yourself (or your IP) blocked. The running example is a tiny inline mock bookshop — a paginated catalogue, detail pages, a bestsellers table, and its own `robots.txt` — so every technique is runnable with no network. The mental model: **a web page is a tree (the DOM); scraping is fetch-the-tree, then navigate to the nodes you want — and be a polite guest while you do it.**

**Learning objectives:**
- Decide *whether* to scrape at all — and read `robots.txt`, Terms of Service, and rate limits before you do.
- Navigate the DOM with BeautifulSoup (`find` / `find_all`) and **CSS selectors** (`.select()`).
- Pull a table into a pandas DataFrame and follow **pagination** across pages.
- Scrape **politely**: a `User-Agent`, a throttle, a cache, and a `robots.txt` check with `urllib.robotparser`.
- Recognise where DIY scraping breaks (JavaScript-rendered pages, anti-bot) and what to reach for next.

**Sections:** 1 When to scrape & the rules you don't break · 2 HTTP recap for scrapers · 3 The HTML/DOM tree · 4 BeautifulSoup basics · 5 CSS selectors · 6 A table → pandas · 7 Following pagination · 8 Polite scraping (throttle + cache + robots) · 9 Where DIY breaks

**Practice:** 4 ✋ checkpoints · 5 🧪 practice exercises (incl. a 🐞 debug-me) · 3 🧠 stretch exercises · 🎁 bonus mini-project: a polite paginated scraper returning a clean DataFrame · ✅ self-assessment.

**Offline:** parses an inline mock website (Python strings); `requests` is shown for reference but never called.

### 48 · Scraping with Firecrawl — `15_scraping_with_firecrawl.ipynb`

When DIY scraping hits JavaScript rendering, anti-bot walls, or just messy markup, a **managed scraping API** that returns clean **markdown or typed JSON** earns its keep. This lesson is the fuller, dedicated treatment of **Firecrawl** (the Module 3 appendix [`../03_real_world_io/A1_web_scraping_firecrawl.ipynb`](../03_real_world_io/A1_web_scraping_firecrawl.ipynb) is the quick intro). Mental model: **give Firecrawl a URL, get back LLM-ready content** — scrape one page, crawl a whole site, map its URLs, or search-and-scrape.

**Learning objectives:**
- Explain when a managed scraper beats DIY — and when it's overkill for a static page.
- `scrape` a URL into markdown + metadata, and `crawl` / `map` / `search` a site.
- Get **typed JSON** back with a schema (a Pydantic model, dataclass fallback) — the real power for LLM pipelines.
- Batch many URLs into a DataFrame and reason about cost / rate limits.
- Choose deliberately between Firecrawl and the `requests`+BeautifulSoup approach of NB 14.

**Sections:** 1 Why managed scraping · 2 Setup (real SDK guarded → mock fallback) · 3 `scrape` → markdown · 4 Structured extraction with a schema → typed JSON · 5 `crawl` / `map` / `search` · 6 Batching into a DataFrame · 7 Cost, rate limits & when *not* to use it

**Practice:** 4 ✋ checkpoints · 4 🧪 practice exercises (incl. a 🐞 debug-me) · 3 🧠 stretch exercises · 🎁 bonus mini-project: a schema-driven extractor turning mock product pages into a typed DataFrame · ✅ self-assessment.

**Offline:** a built-in `MockFirecrawl` (no API key, no network); the real `firecrawl` SDK + `FIRECRAWL_API_KEY` are used automatically if present.

### 49 · OpenAlex: The Open Scholarly Graph — `16_openalex_scholarly_data.ipynb`

The most important scraping lesson is often *don't scrape at all* — check for an open API first. **OpenAlex** indexes ~250M scholarly works (papers, authors, institutions, sources, topics) for free, no key required. This lesson treats it as the model "web data via a clean API" case: the scholarly graph, filtering and search, cursor pagination, and a small citations analysis. Mental model: **works ↔ authors ↔ institutions ↔ sources ↔ topics — you query one entity and filter or expand along the edges.**

**Learning objectives:**
- Explain why an open API beats scraping a publisher's site, and describe the OpenAlex entity graph.
- Make requests, read a Work's JSON shape, and join the **polite pool** (`mailto=`) — API etiquette, the robots.txt of APIs.
- **Filter** (`filter=`) and **search** (`search=`) to build a targeted query.
- Page through a full result set with a **cursor** (`cursor=*` → `meta.next_cursor`).
- Flatten nested JSON into pandas (null-safe) and run a small citations/venue analysis.

**Sections:** 1 Don't scrape what you can query · 2 Your first request · 3 The polite pool (`mailto=`) · 4 Filtering & search · 5 Pagination with a cursor · 6 Into pandas (null-safe flattening) · 7 A mini-analysis (citations by year + top venues) · 8 Limits & good citizenship

**Practice:** 4 ✋ checkpoints · 4 🧪 practice exercises (incl. a 🐞 debug-me on the nullable `primary_location.source`) · 2 🧠 stretch exercises · 🎁 bonus mini-project: profile a research topic · ✅ self-assessment.

**Offline:** a canned OpenAlex snapshot with a `try/except` live fetch — bakes deterministically offline, upgrades to the live keyless API automatically when networked. (OpenAlex is rolling out free API keys and phasing out the email polite pool; the notebook flags this.)

## The discipline this module trains

1. **Check for an API before you scrape.** A clean, documented endpoint beats a brittle HTML parser every time (NB 16).
2. **Be a polite guest.** Read `robots.txt`, set a `User-Agent`, throttle, cache, and use the polite pool — whether you're scraping HTML or hitting an API.
3. **Parse defensively.** Real pages have missing fields and null values; `.find(...)` returns `None`. Every 🐞 debug-me in this module is a version of that bug.
4. **Escalate only when you must.** Static page → BeautifulSoup; JavaScript/anti-bot → a managed scraper; never reach for the heavy tool when three lines of `requests` would do.

## How these notebooks work

Each lesson follows the course rhythm: short teaching sections punctuated by **✋ Quick exercise (~2 min)** checkpoints with collapsible solutions (executed in a fresh kernel), then a graded block — 🧪 practice exercises (⭐-rated, each with a 🐞 debug-me), 🧠 stretch exercises, and a 🎁 bonus mini-project — closing with a ✅ self-assessment. Everything is **100% offline** by default (mock website, `MockFirecrawl`, canned OpenAlex snapshot); installing the real `firecrawl` SDK or running with a network simply upgrades the same code to live data.

## Where next

→ **Module 5 — Machine Learning** (`../05_machine_learning/`) — the spine continues. What you collect here feeds **Module 8 — AI Engineering** (`../08_ai_engineering/`) for RAG and document processing, and the **Module 15 capstones** (`../15_capstones/`) turn it into end-to-end projects.

---

📝 **Finished this module?** Test yourself with the [Module 4 quiz](../quizzes/quiz_04_webscraping.ipynb) — five questions, ~10 minutes.
