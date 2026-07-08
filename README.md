# The Chronicles, Distantly Read

A computational ("distant") reading of the **Crusader Kings III developer diaries**
and the **community reply threads** they drew on the Paradox Interactive forums —
built for Week 4 of the NEH *Humanities in the Age of AI* workshop.

**Live site:** http://www.kirklundblade.com/ck3-distant-reading/

## What this is

Between October 2019 and May 2026, Paradox Interactive published 245 developer
diaries chronicling the design of Crusader Kings III, and the community answered
with roughly 48,900 forum replies totaling 3.2 million words. This project treats
that exchange as a corpus: it extracts both sides into provenance-tagged Markdown,
runs them through a distant-reading pipeline (word frequencies, TF-IDF, concept
networks, frequent-phrase mining), and publishes three interpretive reports:

1. **[The Dev Diaries](http://www.kirklundblade.com/ck3-distant-reading/ck3_distant_reading/CK3_distant_reading_report.html)** — what Paradox talks about when it talks about medieval rule
2. **[The Community Responds](http://www.kirklundblade.com/ck3-distant-reading/ck3_distant_reading/CK3_community_responses_report.html)** — themes, concerns, and enthusiasms of the player base
3. **[The Reply Corpus](http://www.kirklundblade.com/ck3-distant-reading/ck3_distant_reading/CK3_Reply_Corpus_Distant_Reading.html)** — a full distant reading of the forum replies

## Methodology

The analysis follows **Anastasia Salter's eight-step distant-reading method**
(preprocess → bag of words → iterated stopwords → word cloud → themes → concept
network → frequent phrases → verification), hardened with **Ted Underwood's
ground-truthing discipline**: every frequency-derived claim is verified against
actual passages before it survives into a report. See
[salter_best_practices.md](salter_best_practices.md) for the full set of
practices and a candid self-assessment against them.

Extraction is "flag but do not alter": source text is preserved verbatim, with
forum infrastructure (quotes, signatures, page chrome) recorded in YAML
front-matter and inline `<!-- artifact:* -->` comments rather than silently
removed. This keeps the corpus citable and the cleaning decisions auditable.

## Repository layout

| Path | Contents |
|------|----------|
| `index.html` | Landing page for the live site (CK3 parchment theme) |
| `ck3_distant_reading/` | The three HTML reports plus their data (word clouds, concept networks, TF-IDF tables, ranked bags of words as JSON/PNG/SVG) |
| `ck3_dev_diaries/` | **Corpus, OP side** — 245 dev diaries as `dd_*.md` (~625k words, 2019–2026), with `MANIFEST.md` and the capture scripts that built it |
| `ck3_dev_diary_replies/` | **Corpus, reply side** — 245 reply threads as `rt_*.md` (~48.9k replies, ~3.2M words), with `MANIFEST.md` |
| `ck3_reply_scraper/` | Pipeline that captured the reply threads: Claude-in-Chrome live capture, extraction, manifest building, corpus comparison |
| `distant-reader/` | The reusable **distant-reader skill** (v0.3.0) — corpus building and analysis scripts, report template, methodology references |
| `ck3-style-guide/` | CK3 visual theme (colors, typography, components) used by the landing page |
| `salter_best_practices.md` | Nine methodological practices distilled from Salter's course, with self-assessment |

## Corpus at a glance

- **Dev diaries:** 245 files, ~624,700 words, 3,445 preserved image references, spanning the base game and 17 expansions/updates (Royal Court and All Under Heaven are the largest at ~92k and ~82k words)
- **Replies:** 245 threads, 48,866 replies, ~3,241,000 words
- Both manifests (`ck3_dev_diaries/MANIFEST.md`, `ck3_dev_diary_replies/MANIFEST.md`) list every file with date, author, expansion, and word count

## Reproducing or extending the analysis

The corpus was captured live from the Paradox forums (June 2026) using the
scripts in `ck3_dev_diaries/` and `ck3_reply_scraper/`, then analyzed with the
tooling in `distant-reader/scripts/`. To extend the analysis — new diaries, new
visualizations, different stopword sets — regenerate through those scripts
rather than hand-editing the reports; the reports are build artifacts.

## Publishing

The repository root **is** the live site: GitHub Pages serves the `main` branch
directly (a `.nojekyll` file keeps Pages from running the corpus through
Jekyll, which chokes on CK3 game syntax). Any push to `main` redeploys in about
a minute.

## Acknowledgments

- Methodology: [Anastasia Salter, *Humanities in the Age of AI*](https://anastasiasalter.net/HumanitiesAI/), Week 4
- Theoretical grounding: [Ted Underwood, "A Genealogy of Distant Reading" (DHQ 11.2)](https://digitalhumanities.org/dhq/vol/11/2/000317/000317.html)
- Source texts © Paradox Interactive and their forum authors; extracted for scholarly analysis under fair use. The visual theme is an unofficial homage to the game's UI.
