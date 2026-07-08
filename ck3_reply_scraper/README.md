# CK3 Reply-Thread Scraper — community-voice companion to the dev-diary corpus

This is an **extension** of the dev-diary extractor (`extract_diary.py`). Where the
original captures only the **opening post** of each Crusader Kings III developer-diary
thread and discards every reply, this toolkit captures the **full response thread** —
every reply post across every forum page — and preserves it as provenance-tagged
Markdown structured to mirror the dev-diary corpus, so the **developer voice** and the
**community voice** can be distant-read and compared on equal terms.

## Files

| File | Role |
|------|------|
| `extract_replies.py` | Parse saved thread-page dumps → one `rt_*.md` per thread (all replies). Companion to `extract_diary.py`; same Salter "flag, don't alter" discipline. |
| `orchestrate_replies.py` | Resume-safe driver: groups page dumps by thread, orders by page, runs the extractor per thread, skips threads already done. Mirrors `orchestrate.py`. |
| `build_replies_manifest.py` | Emit `MANIFEST.md` indexing the reply corpus (parallels `build_corpus_manifest.py`). |
| `compare_corpora.py` | **Comparative distant reading.** Dunning log-likelihood (G²) keyness between any two corpora — which words the community over-uses vs the developers, and vice-versa. |
| `fixtures/` + `sample_output/` | A worked two-page example thread and the `rt_*.md` it produces. |

## The reply-corpus Markdown schema (parallel to `dd_*.md`)

Each `rt_*.md` opens with YAML front-matter mirroring the dev-diary schema, plus
reply-specific fields:

- `content_type: reply_thread` and `parent_dd_file:` — links each reply thread to its diary
- `reply_count`, `participant_count`, `pages_captured`
- `reply_date_first` / `reply_date_last`, `body_word_count` (quotes excluded), `quoted_span_count`

The body is one section per reply:

```
## Reply N — <author> · <date> · post-<id>
<!-- post_author_url: … -->
<reply body, verbatim>
<!-- artifact:quote:start --> …quoted text… <!-- artifact:quote:end -->
<!-- artifact:reactions:start --> - 23 Like <!-- artifact:reactions:end -->
```

Quoted text and reaction tallies are **flagged, not deleted** (and excluded from word
counts), exactly like the artifact spans in `dd_*.md`. To analyze, strip the YAML
front-matter and every `<!-- artifact:* -->` span, then tokenize — the same Step 1
preprocessing the distant-reader already uses.

## Running it live (full corpus)

Live fetching uses the **same pipeline that built the dev-diary corpus**. The Paradox
forum sits behind a bot challenge, so plain WebFetch is often blocked; the proven path
is Claude-in-Chrome DOM capture:

1. **Enumerate pages.** Fetch a thread's page 1, read the `Page 1 of M` indicator, then
   visit `…/threads/.<id>/page-2` … `page-M`.
2. **Capture each page** with `get_page_text` and save through `chrome_fetch_to_file.py`
   (which writes the header format these tools expect) into a dumps directory. Each saved
   page's `→ <url>` line carries `/page-N`, which the orchestrator uses to order pages.
3. **Extract.**
   ```
   python3 orchestrate_replies.py \
       --dumps-dir ./reply_page_dumps \
       --manifest  ./manifest.json \
       --out-dir   ./ck3_reply_threads
   python3 build_replies_manifest.py --corpus ./ck3_reply_threads
   ```
   The orchestrator is resume-safe: interrupt and re-run, and already-extracted threads
   are skipped.

## Comparative distant reading

```
python3 compare_corpora.py \
    --a ./ck3_reply_threads --a-glob 'rt_*.md' --a-label "Community replies" \
    --b ./ck3_dev_diaries   --b-glob 'dd_*.md' --b-label "Developer diaries" \
    --min-count 5 --top 30 --out keyness.json
```

Output: the terms statistically over-represented in each voice (G² keyness). In the
worked example the community over-indexes on *defines, would, levies, counters, hope*
(feature requests, modding, specific mechanics) while the diary over-indexes on
*you, your, troops, siege, battle, enemy* (instructional second-person voice) — the
exact developer-vs-community contrast the corpus was built to expose. The same `rt_*.md`
files also drop straight into the Step-1→Step-8 distant-reader pipeline for a standalone
reading of community language, or a side-by-side word cloud / theme comparison.

## Validation note & assumptions

This session could not reach the live forum (the bot challenge blocked WebFetch and the
Chrome extension was offline), so the parser was validated against a faithful two-page
XenForo fixture (`fixtures/`) reproducing the exact text markers `extract_diary.py` keys
off — author cards (`### [handle](…/members/…)`), `post-<id>` permalinks, `said:` /
`Click to expand…` quote spans, and `- N![Reaction]` tallies. The post-segmentation
markers live in the `REGEX` section at the top of `extract_replies.py`; if a forum theme
change shifts the rendering, that is the one block to adjust after the first real capture
(the "iterations are the work" principle from the distant-reader method).

## Live run — executed 2026-06-10 (Claude in Chrome)

The scraper was run against the real **DD #3 — War** thread once the Chrome
extension was active, proving the live path end-to-end:

- Thread `1279641`, **22 pages** walked via same-origin `fetch` (`chrome_capture_replies.js`).
- **436 reply posts** captured, **213 participants**, **31,941** body words, **341** quote spans,
  spanning **2019-11-12 → 2020-10-04**. The dev-diary OP was correctly excluded (it renders
  outside `article.message`). Authors were anonymized to stable per-thread participant ids.
- `live_capture/rt_003_2019-11-12_war__replies.md` materializes replies **1–88** verbatim
  (the per-call DOM-text transport cap of 50k chars limits how much is written out in one pass;
  full-thread aggregate stats are recorded in the file's `thread_*_total` front-matter).
- Real comparative keyness (`sample_output/keyness_war_LIVE.json`): the **developer voice**
  over-indexes on precise second-person mechanics — *you, your, advantage, troops, pursuit,
  progress, limit, damage* — while the **community voice** over-indexes on evaluation and
  speculation — *like, knight, nice, would, think, yes, commanders*. Developers define systems;
  players react to and speculate about a subset of features.

Note on authorship: forum usernames are personal data, so this pipeline stores a stable
hashed pseudonym (`participant_NNN`) instead of the handle — sufficient for participant-level
distant reading without persisting PII.
