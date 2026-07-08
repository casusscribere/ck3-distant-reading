# Build log: `distant-reader` skill v0.3.0

*Constructed June 9, 2026 in one session, following the plan in `distant_reader_skill_plan.md`. This document records what was built at each stage, what design decisions were made, and how each component maps back to the Week 3 and CK3 prototype work that motivated it.*

## Stage 1 — Folder scaffold and SKILL.md

Created the kebab-case folder `distant-reader/` per Anthropic's skill-naming rules, with the four standard subdirectories (`scripts/`, `references/`, `assets/`, plus the entry-point `SKILL.md` at the top). The folder name avoids the reserved prefixes "claude" and "anthropic" per the Anthropic guide.

**SKILL.md.** The entry point carries:
- The v0.3.0 YAML frontmatter from the plan §3, sitting at ~1015 characters (under the 1024-character ceiling). The description names all input types (PDFs, Gutenberg .txt, .epub, .html, URLs) and explicitly mentions the Chrome MCP fallback so the skill loads on any of: a PDF folder, a URL list, a single forum thread, or a pure analysis request against an existing corpus. The `validated-against` metadata field points at the CK3 corpus (245 web sources) as a regression-test fixture.
- The instructions body covers the eight Salter steps, mode selection, critical reminders ("never silently strip artifacts", "stance is not endorsement", "curation determines findings", "the iterations are the work"), and pointers into the references/ folder for the deep material.
- The "Use Case A" framing from the plan — that any request for distant reading or scholarly analysis fires the skill, with B/C/D as internal dispatches based on corpus shape — is reflected in the "When to invoke" and "Mode selection" sections.

**Files created in this stage:** 1.

## Stage 2 — Step 0 extraction scripts (12 scripts)

The heart of the new design. Each script is small (~30–120 lines), single-purpose, and runs as a subprocess invocation from the orchestrator. None depend on external libraries beyond Python's standard library plus the system binaries declared in `compatibility:`.

**The orchestrator: `00_extract_corpus.py`.** Inventories inputs (a folder of files, a URL list, or a single source), classifies each by extension or URL pattern, dispatches to the appropriate extractor, then runs `00f_annotate_artifacts.py` and `00g_validate_markdown.py` on the resulting `.md` files. Emits a `MANIFEST.md` summarizing what got processed and what succeeded.

**The PDF route: `00a_probe_pdf.py`, `00b_extract_pdftotext.py`, `00c_extract_ocr.py`.** The probe runs `pdftotext` on the first two pages, checks word count, Latin-character ratio, and single-character-line clustering, and returns one of `text-layer-extraction`, `ocr-required`, or `mixed`. The text-layer extractor is a clean port of the Week 3 preprocessing logic (`pdftotext -layout`, ligature normalization, de-hyphenation) wrapped with provenance front-matter. The OCR extractor renders pages via `pdftoppm` at 300 DPI and runs Tesseract with `--oem 1 --psm 1`; degrades to a stub `.md` with `extraction_method: unrecoverable_no_ocr` when Tesseract isn't installed, so the corpus still has a placeholder rather than a missing entry.

**The plaintext route: `00d_extract_plaintext.py`.** Direct passthrough for `.txt` and `.md`. Detects Project Gutenberg markers (`*** START OF THE PROJECT GUTENBERG`) and flags the header/footer as `gutenberg_header` / `gutenberg_footer` artifacts without removing them — Salter's "flag but don't alter" principle.

**The HTML/epub route: `00e_extract_html_epub.py`.** Strips HTML tags via regex; calls `ebook-convert` (Calibre) for `.epub`. Both routes degrade gracefully when their preferred tools aren't available.

**The web route: `00h_probe_url.py`, `00i_extract_webfetch.py`, `00j_extract_chrome.py`, `00k_chrome_capture_adapter.py`.** This is the genuinely new design work, based directly on the CK3 dev-diary run.
- `00h_probe_url.py` does URL-pattern routing because the calling Claude session — not the script — actually makes the WebFetch call. The script encodes the empirically-discovered domain lists (`CHROME_PREFERRED_DOMAINS`, `KNOWN_CLOUDFLARE`, `WEBFETCH_PREFERRED_DOMAINS`) and returns a recommendation that the orchestrator follows.
- `00i_extract_webfetch.py` consumes a WebFetch saved temp file and applies the XenForo-aware boundary detection from the CK3 `extract_diary.py` — title regex covering all five title prefix variants, thread-starter line, reactions-block terminator, Written-by signature anchor.
- `00j_extract_chrome.py` consumes a Chrome-captured DOM-text body. Synthesizes the structural markers (title heading, Thread starter, Start date, Written by) that the file-based extractor expects, because Chrome's DOM-text strips XenForo's signature card and reactions sidebar. Records the synthesis in `notes_for_analyst`. Supports a `--partial` flag for the long-body-strategy=partial case.
- `00k_chrome_capture_adapter.py` is the thin shim equivalent of the CK3 `chrome_fetch_to_file.py`: write a WebFetch-shaped temp file from Chrome capture text so the WebFetch extractor path can be reused. Useful when the user wants both paths going through the same extractor for consistency.

**The artifact handler: `00f_annotate_artifacts.py`.** Implements Salter's "flag but don't alter" principle for the artifact taxonomy. Detects JSTOR cover sheets (using the structural match — Society heading + REFERENCES line in the top 10% of the document), bare page numbers (standalone digit lines), references sections (heading in the last 40%), and DRM footers (Bloomsbury, Routledge, ProQuest patterns). Each detection wraps the content in `<!-- artifact:type:start -->` / `<!-- artifact:type:end -->` comments without removing it.

**The validator: `00g_validate_markdown.py`.** Enforces well-formed YAML front-matter, non-empty body, balanced artifact-comment counts, and recognized `extraction_method`. Halts the pipeline with per-file diagnostics. The recognized-methods set is closed (`pdftotext_layout`, `tesseract_ocr`, `plaintext_passthrough`, `gutenberg_passthrough`, `html_strip_tags`, `ebook_convert`, `webfetch_xenforo_text_layer`, `claude_in_chrome_dom_capture`, `claude_in_chrome_partial_capture`, `unrecoverable_no_ocr`, `unrecoverable_no_ebook_convert`) so downstream code can rely on it.

**Files created in this stage:** 12.

**Provenance:** Every script in this stage maps to a specific failure mode encountered in either the Week 3 or CK3 run. Nothing here is speculative.

## Stage 3 — Salter Steps 1–7 analysis scripts (10 scripts)

Ported from the inline Python that ran during the Week 3 conversational walkthrough. Each script is generalized to read from any `corpus_md/` directory and to parse the per-file YAML front-matter, rather than the session-specific paths the Week 3 versions used.

**`01_bag_of_words.py`** — corpus-wide token counter that strips YAML front-matter and `<!-- artifact:* -->` blocks before tokenizing. Logs which artifact types were skipped so the analyst can audit. Supports `--include-artifacts` to override the default strip behavior for e.g. citation-pattern studies.

**`02_apply_stopwords.py`** — three-pass filter using the `references/stopwords-*.txt` lists. Each pass surfaces the top 60 surviving terms with bar visualizations so the function-word-to-content-word transition is visible (Salter's tutorial scripts this transition explicitly). Stopword lists are user-editable; the pass count is hardcoded at three to match Salter's pedagogical sequence.

**`03_tfidf.py`** — corpus-aggregated TF-IDF with `(1 + log(tf)) * log(N/df)` weighting. Defaults to `--min-df 4` and `--max-df-ratio 0.97` to suppress one-document outliers and universal function words. The Week 3 run's discovery that author surnames surface as "distinctive terms" motivated adding citation-pattern detection to the artifact stopword list — see `references/failure-modes.md`.

**`04_concept_network.py`** — sentence-level co-occurrence weighted by PMI. Defaults nodes to the top 40 TF-IDF terms; accepts `--nodes` for user-supplied character or concept lists. Filters edges by `--min-co 10` and `--min-pmi 0.4`; sorts by `PMI × log(weight)` to balance significance against support.

**`05_phrases.py`** — bigrams and trigrams with the document-frequency-and-DRM-blocklist filter that solved the Week 3 e-book-footer gotcha. Phrases containing tokens from a fixed DRM set (`bloomsbury`, `proquest`, `ebookcentral`, `ucf`, `docid`, etc.) are dropped regardless of frequency.

**`06_underwood_verify.py`** — the non-optional Step 8. For the top three terms by frequency, the top three concept-network edges, and the top three trigrams, the script greps the corpus for representative passages and surfaces them in `verification.json` for the report. This operationalizes Underwood's central caution that frequency does not equal endorsement.

**`render_wordcloud.py`** — d3-cloud SVG output as standalone HTML. Single-color scheme by default; user can override by editing `analysis/wordcloud.html` directly.

**`render_network.py`** — force-directed D3 graph as standalone HTML. PMI-weighted edge widths, square-root-scaled node radii.

**`render_phrases.py`** — Chart.js horizontal-bar chart for bigrams and trigrams in side-by-side panels.

**`build_report.py`** — final assembly. Combines corpus summary, top words, TF-IDF table, links to the three standalone viz HTMLs, the Underwood verification section, and the three caveat boxes (curation contingency, frequency-is-not-stance, iterations-are-the-work).

**Files created in this stage:** 10.

**Provenance:** Each script ports the inline Python from the Week 3 walkthrough conversation, with three generalizations: path-relative rather than session-specific, YAML-front-matter aware (Step 0 of the new pipeline), and configurable thresholds via CLI flags.

## Stage 4 — Reference documents (12 files)

**Stopword lists.** Three text files: `stopwords-english.txt` (NLTK-style basic), `stopwords-academic.txt` (discourse fillers), `stopwords-artifacts.txt` (publisher names, citation tokens). These are user-editable per project. Iterations during analysis go here, not into the scripts.

**`salter-methodology.md`.** Quotes the seven canonical prompts from Salter's tutorial; documents the three additions the skill makes (provenance corpus, Underwood pass, critique footer); states the iteration discipline as quoted from Salter directly.

**`underwood-critique.md`.** States the core caution ("patterns, not arguments"), describes how `06_underwood_verify.py` operationalizes it, names the Week 3 finding (authenticity is critiqued, not endorsed) that the verification step caught, and lists what even the verification step can't see (chronology, stance per se, citation lineage, voice).

**`failure-modes.md`.** The dozen-plus known issues from the Week 3 and CK3 runs, organized into file-source and web-source sections. Each entry names the symptom, the cause, and the fix. This is the most operationally important reference — when a downstream user hits one of these patterns, the entry gives them the exact diagnostic and remedy.

**`chrome-fallback-protocol.md`.** When to invoke Chrome MCP, the per-platform content-selector table (XenForo, Substack, Medium, WordPress, Discourse, Reddit), the long-body-strategy options, and pitfalls (tab pooling, cookie loss, reply confusion).

**`web-source-routing.md`.** The decision tree as an ASCII diagram plus prose decision criteria. Documents the three domain lists in `00h_probe_url.py` and invites users to extend them based on experience.

**Stubs.** `extraction-strategies.md`, `artifact-taxonomy.md`, `adapting-to-academic.md`, and `examples.md` were created as stubs pointing back at the substantive references. These should be populated during real-corpus usage when the skill encounters new patterns worth documenting.

**Files created in this stage:** 12.

## Stage 5 — Assets and templates (3 files)

**`markdown-template.md`.** The per-source `.md` skeleton showing the YAML front-matter schema and the inline-artifact-comment structure. Users editing extracted files by hand can refer to this for the expected shape.

**`style.css`.** Minimal academic-report styling — Inter sans-serif, generous line-height, muted color palette, distinct callout boxes for caveats (`#fff8e1` warm background, `#d97706` accent border), passage blocks in serif for readability against the body sans-serif.

**`report-template.html`.** The HTML scaffold with `{PLACEHOLDER}` tokens for the build step to fill in. Sections: corpus summary, top words, TF-IDF, viz links, themes, Underwood verification, three caveats. The actual report builder (`build_report.py`) currently emits inline HTML rather than templating from this file; the template exists as documentation of the intended structure for users who want to write a more sophisticated build step.

**Files created in this stage:** 3.

## Stage 6 — This CHANGELOG (1 file)

This document, recording what was built at each stage and the design rationale.

## Summary

| Stage | Component | Files | Lines (approx.) |
|---|---|---:|---:|
| 1 | Scaffold + SKILL.md | 1 | 140 |
| 2 | Step 0 extraction (12 scripts) | 12 | 800 |
| 3 | Steps 1–7 analysis (10 scripts) | 10 | 700 |
| 4 | References | 12 | 600 |
| 5 | Assets | 3 | 80 |
| 6 | CHANGELOG | 1 | this file |
| | **Total** | **39 files** | **~2,400 lines** |

## What's still needed (not blocking; for future iteration)

- **Worked examples in `references/examples.md`.** Five cases: Salter's *Frankenstein* (Use Case A simplest), Week 3 academic-PDF corpus (B), comparative pre/post-2013 split (C), CK3 dev-diary URL list (D), Step-0-only extraction with no analysis.
- **A `tests/` folder.** Each test runs the pipeline against a tiny fixture corpus and asserts the front-matter schema is correct, the artifact tags are balanced, and the analysis outputs aren't empty.
- **The `--long-body-strategy=slice` implementation in `00j_extract_chrome.py`.** Currently the partial-capture path is the default; the slice path is described in the docs but not wired up in code.
- **A reference implementation of comparative analysis (Use Case C).** Currently the skill describes it in the SKILL.md and plan, but no `07_comparative.py` script exists. Natural follow-on: a script that takes a grouping JSON (forum_id → group label) and runs each analysis step per group, emitting diff views.

## Provenance for reuse

This skill, while built from scratch as a packaged folder, depends heavily on patterns established in:

- **Week 3 academic-PDF distant read** — the artifact taxonomy, the iterative-stopwords discipline, the TF-IDF-with-citation-noise-removal pattern, the Underwood ground-truthing step, the PMI-weighted concept network, and the per-document caveats in the report's critique section.
- **CK3 dev-diary URL-list extraction** — the per-source adaptive routing model (text-layer probe → pdftotext / Tesseract; URL probe → WebFetch / Chrome), the XenForo boundary regexes, the artifact taxonomy for forum chrome / signatures / reactions / replies, the Chrome-display-truncation workaround with `--long-body-strategy`, and the failure-mode catalog.

Both prior runs are preserved in `Week 3/` as `distant_read_writeup.md`, `ck3_dev_diaries/MANIFEST.md`, and the 235 + 10 `.md` files. Future iterations of this skill can regression-test against them.
