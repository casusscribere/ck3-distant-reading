---
name: distant-reader
description: |
  Builds a provenance-tagged Markdown corpus from PDFs, Gutenberg .txt,
  .epub, .html, or URLs, then conducts AI-assisted distant reading
  following Salter's eight-step method (preprocess, bag of words,
  iterated stopwords, word cloud, themes, concept network, frequent
  phrases, Underwood verification). Per-source Step 0 routing:
  pdftotext for text-layer PDFs, Tesseract for image-only PDFs,
  WebFetch for clean web pages, Claude in Chrome MCP for Cloudflare-
  challenged or truncated pages. All extraction methods and detected
  artifacts (page numbers, headers, JSTOR covers, DRM footers, forum
  chrome, signatures, replies, references) are flagged in YAML
  front-matter and inline comments, never silently removed. Use when
  the user asks to "distant read", "analyze this corpus", "find
  themes", "make a word cloud", "OCR this folder", "scrape this forum
  thread", "extract these URLs to markdown", "build a markdown
  corpus", or uploads a Gutenberg .txt, a PDF folder, a URL list, or
  a forum thread.
metadata:
  author: NEH AI Workshop project
  version: 0.3.0
  methodology-source: https://anastasiasalter.net/HumanitiesAI/weekfour.html
  theoretical-grounding: https://digitalhumanities.org/dhq/vol/11/2/000317/000317.html
  validated-against: CK3 dev-diary corpus (245 web sources, Oct 2019 - May 2026)
compatibility: |
  Requires pdftotext + pdftoppm (poppler-utils), Tesseract OCR for
  image-only PDFs, Python 3.10+ standard library. Web extraction also
  uses WebFetch (Cowork built-in) and Claude in Chrome MCP fallback.
  Optional: ebook-convert (Calibre) for .epub. Visualizations use
  d3-cloud and Chart.js via CDN.
---

# distant-reader

This skill conducts AI-assisted distant readings of texts and corpora following Anastasia Salter's Week 4 methodology, hardened with Ted Underwood's ground-truthing discipline. It produces two deliverables: a citable, provenance-tagged Markdown corpus, and an HTML report with embedded visualizations and an interpretive critique.

## When to invoke

The skill fires on any request for distant reading or scholarly analysis of a corpus. Triggers include: *"distant read"*, *"distant reading"*, *"analyze this corpus"*, *"what are the themes in these texts"*, *"computational text analysis"*, *"Moretti-style distant reading"*, *"Salter's distant reading method"*, *"Underwood-style analysis"*, *"convert these PDFs to markdown"*, *"OCR this folder"*, *"scrape this forum thread"*, *"build a markdown corpus"*. The single-Gutenberg-novel Salter tutorial case is the simplest invocation; the academic-PDF corpus, the URL-list, and the comparative subset are routine extensions.

## Mode selection

Before running any analysis, choose the corpus shape:

- **Single text** — one Gutenberg .txt, one PDF, one URL. The skill treats this as a degenerate corpus of size 1 and runs the same pipeline.
- **Local multi-document corpus** — a folder of PDFs, .txt, .html, .epub. Routes to the PDF/text branch of Step 0.
- **Web-source corpus** — a URL or list of URLs. Routes to the WebFetch / Chrome MCP branch of Step 0.
- **Comparative** — any of the above plus a grouping (date range, author, treatment-vs-control). Runs the standard pipeline per subset plus a diff view.

Confirm the mode with the user before proceeding if it's ambiguous. Default to the most conservative reading of the request.

## Step 0 — Build the provenance-tagged Markdown corpus

This is the foundational step. Everything downstream depends on it being right.

**0.1 — Inventory inputs.** List every file in the input directory or every URL in the input list; classify by source type; compute SHA-256 hashes (for files) or canonical URLs (for web sources).

**0.2 — Per-source probe and routing.** For each input, run the appropriate probe:
- *PDFs:* `scripts/00a_probe_pdf.py` checks for text layer via pdftotext on the first two pages. Returns `text-layer-extraction`, `ocr-required`, or `mixed`.
- *URLs:* `scripts/00h_probe_url.py` does one WebFetch and classifies the response: `server-rendered-clean`, `inline-truncated`, `cloudflare-challenge`, `js-rendered-empty`. Returns the routing decision.
- *Plain text / HTML / epub:* no probe needed; route directly.

Each probe's reasoning is recorded in the resulting `.md`'s YAML front-matter so a human can audit the choice.

**0.3 — Run the chosen extractor.** Dispatch to one of:
- `00b_extract_pdftotext.py` for text-layer PDFs
- `00c_extract_ocr.py` for image-only PDFs (Tesseract via pdftoppm)
- `00d_extract_plaintext.py` for `.txt`/`.md`
- `00e_extract_html_epub.py` for `.html`/`.epub`
- `00i_extract_webfetch.py` for clean web pages
- `00j_extract_chrome.py` for JS-rendered, Cloudflare-challenged, or WebFetch-truncated pages

Each extractor writes a `corpus_md/<source-stem>.md` with the full YAML front-matter schema (see `references/extraction-strategies.md` for the schema).

**0.4 — Annotate artifacts.** `scripts/00f_annotate_artifacts.py` reads each markdown body and wraps Salter-style extraneous content in `<!-- artifact:<type> -->` comments **without removing it**. The artifact taxonomy is fixed (see `references/artifact-taxonomy.md`) and covers: `bare_page_number`, `running_header`, `running_footer`, `jstor_cover_page`, `drm_footer`, `publisher_boilerplate`, `references_section`, `appendix`, `low_ocr_confidence`, `figure_caption`, `table_data`, `forum_chrome`, `op_signature`, `reactions_block`, `thread_metadata`, `replies`, `thread_banner`.

**0.5 — Validate.** `scripts/00g_validate_markdown.py` enforces well-formed front-matter, non-empty body, no unclosed artifact comments, and recognized `extraction_method`. Failures halt the pipeline with a per-file diagnostic.

**0.6 — Emit corpus manifest.** `corpus_md/MANIFEST.md` lists every source with its extraction method, OCR confidence (if applicable), page count, word count, artifact summary, and any warnings.

Step 0 is also a valid **standalone deliverable**. If the user only asks for extraction, the skill stops here.

## Steps 1–7 — Salter's pipeline

Each runs against the Markdown corpus.

**Step 1 — Bag of words.** `scripts/01_bag_of_words.py` parses each `.md`'s YAML front-matter, strips inline `<!-- artifact:* -->` comments before tokenizing, logs which artifact types were skipped. Outputs `bag_raw.json` (top 5000 terms with frequencies and document-frequencies). Show the user the top 40 raw tokens with their counts so the function-word dominance is visible — this motivates Step 2.

**Step 2 — Stopwords, iterated.** `scripts/02_apply_stopwords.py` applies three passes by default: English basic (NLTK-style), academic discourse fillers, and publisher / citation artifacts. After each pass display the top 60 surviving terms. Iterate further if the user requests. Stopword lists are in `references/stopwords-*.txt` and are user-editable per project.

**Step 3 — Word cloud.** `scripts/render_wordcloud.py` produces an SVG word cloud sized by frequency, colored by user-supplied conceptual clusters (default: derive clusters from TF-IDF themes).

**Step 4 — Themes and genre.** `scripts/03_tfidf.py` computes corpus-aggregated TF-IDF. Cluster top distinctive terms into 5–12 themes. For each theme, retrieve 3–5 representative passages from the corpus for grounding. Characterize the corpus's "genre" (scholarly, fictional, journalistic, official, mixed).

**Step 5 — Concept or character network.** `scripts/04_concept_network.py` builds a PMI-weighted sentence-level co-occurrence network. For fiction corpora use character names; for academic corpora use concept keywords; for mixed corpora let the user decide. Render with `render_network.py`.

**Step 6 — Frequent phrases.** `scripts/05_phrases.py` extracts bigrams and trigrams. Filter by document frequency ≥ 3, drop publisher/DRM token sequences via the artifact stopword list. Render top 20 of each with `render_phrases.py`.

**Step 7 — Underwood verification.** **Non-optional.** For the top three claims in the analysis (the most-frequent terms, the strongest concept-network edges, the top trigrams), grep the markdown corpus for representative passages. Surface the passages alongside the claims. Flag any claim that the grep does not support. This is the discipline that distinguishes scholarship from frequency reporting — see `references/underwood-critique.md`.

## Step 8 — Critique and report

Assemble the report (`scripts/build_report.py`) with: corpus summary, ten thematic clusters, all five visualizations, the Underwood verification section, and an honest "what this analysis got right, what to be suspicious of, and what it cannot see" section. The corpus curation contingency goes in the report: a line acknowledging that findings describe *this collection*, not the field the collection samples from.

## Examples

Examples live in `references/examples.md`. Five worked cases: Salter's *Frankenstein* (Use Case A simplest invocation), the Week 3 academic-PDF corpus (Use Case B), the comparative pre-/post-2013 split of Week 3 (Use Case C), the CK3 dev-diary URL list (Use Case D), and a Step-0-only extraction with no analysis.

## Troubleshooting

See `references/failure-modes.md` for the dozen-plus known issues. Most-common: JSTOR cover sheet false-cuts, image-only PDFs needing OCR, author-surname TF-IDF noise, DRM footers dominating trigrams, WebFetch truncated inline responses, Cloudflare bot challenges, wrong-post capture from page-text DOM extraction, Chrome `javascript_tool` display-truncation cap. Each has a diagnostic and a fix.

## Critical reminders

- **Never silently strip artifacts.** Flag them with `<!-- artifact:<type> -->` comments and document them in YAML front-matter. The downstream analysis can choose to skip them; the source corpus preserves everything.
- **Stance is not endorsement.** A high frequency of "authenticity" doesn't mean the corpus values authenticity — it means it discusses authenticity. The Underwood pass exists to catch this.
- **Curation determines findings.** Always note in the report that findings describe the supplied corpus, not the field it samples from.
- **The iterations are the work.** Salter's tutorial says "keep refining until you are happy with your results." Stopword iterations, artifact rules, the choice of network nodes — all of these are part of the analysis, not embarrassments to hide.
