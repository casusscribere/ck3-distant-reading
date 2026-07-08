# Known failure modes and fixes

Every entry below was encountered during the Week 3 academic-PDF run, the CK3 dev-diary URL-list run, or both.

## File-source failure modes

### JSTOR cover-sheet false cut
JSTOR PDFs include a cover page with the word "REFERENCES" at the top (under "Linked references are available on JSTOR..."). A naive reference cutter triggers on this and chops the body. **Fix:** require the "References" heading to appear in the last 40% of the document before triggering the cut. Implemented in `00f_annotate_artifacts.py`.

### Image-only PDF returning zero words
`pdftotext` returns an empty file with exit code 0 for image-only PDFs. **Fix:** `00a_probe_pdf.py` detects this via low word count + low Latin-character ratio and routes to OCR via `00c_extract_ocr.py`.

### Tesseract low-confidence pages
Multi-column layouts, heavy figure overlay, or pre-1900 typography can produce garbled OCR. **Fix:** front-matter records `ocr_average_confidence` and lists `low_ocr_confidence` pages in `detected_artifacts` so the analyst can spot-check.

### Author-surname TF-IDF noise
In academic corpora, TF-IDF surfaces author surnames from in-text citations (Andrew, Matthew, Kapell, Elliott) as "distinctive terms." **Fix:** add to `stopwords-artifacts.txt`. Empirical: after pass 2, scan the top 50 TF-IDF terms for capitalized-in-original-case words with document frequency 4–15.

### DRM footer dominating trigrams
One heavily-paginated e-book whose every-page footer contains publisher boilerplate produces ~20 of the top 30 trigrams from just 3 documents. **Fix:** raise the trigram document-frequency threshold to ≥5 AND filter trigrams containing DRM tokens (`bloomsbury`, `proquest`, `ebookcentral`, etc.) — implemented in `05_phrases.py`.

## Web-source failure modes (added based on the CK3 dev-diary run)

### WebFetch truncated-inline response
For pages between WebFetch's "fully inline" and "too large, save to file" thresholds, the response is clipped mid-content with no temp file written. **Fix:** the URL probe detects this (canonical URL at top, navigation list at bottom, no body) and routes to Chrome MCP. See `chrome-fallback-protocol.md`.

### Cloudflare or similar bot challenge
The page returns a "Client Challenge" / "JavaScript is disabled" stub. **Fix:** Chrome MCP solves it — `navigate` + a 4-to-6-second wait lets the JavaScript challenge execute, then capture the rendered DOM. For known Cloudflare-fronted domains, pre-route to Chrome in `00h_probe_url.py`.

### Wrong-post capture from page-text extraction
Chrome's `get_page_text` uses a "largest article element" heuristic which, on a forum thread with short OP and long replies, returns the longest reply. **Fix:** use `javascript_tool` to scope the query to a platform-specific OP selector (XenForo: `.message-body .bbWrapper`; Substack: `article > .post-content`; etc.) — see `chrome-fallback-protocol.md` for the per-platform table.

### Chrome `javascript_tool` display-truncation cap
Tool results display ~1000 characters per call regardless of underlying data size. For OPs under ~1.5 KB this captures the full body cleanly; for longer ones, brute-force slicing in 1KB chunks works but is expensive. **Fix:** two pragmatic options — sliced chunking (slow), or partial capture with documented caveat (`extraction_method: claude_in_chrome_partial_capture`). Choose per `--long-body-strategy={slice,partial,skip}`.

### Synthesized author handle and missing reactions
Chrome's DOM-text capture doesn't include the XenForo signature card or reactions sidebar. **Fix:** `00j_extract_chrome.py` synthesizes a thread-starter line and `Written by` anchor with a placeholder author. The synthesized values are flagged in `notes_for_analyst` so a future analyst doesn't mistake them for real ones.

### Mixed-fetch corpus skew
When half the URLs in a corpus came via WebFetch and half via Chrome MCP, downstream analyses may see differences in punctuation (smart quotes preserved vs. ASCII-normalized), image-reference inclusion, or reaction counts. **Fix:** document the per-file extraction method in front-matter; downstream analysis can filter by `extraction_method` to check for systematic skew.

## Corpus-level failure modes

### Curation contingency
Findings describe *this collection*, not the field the collection samples from. **Fix:** the report's final section always includes a curation-contingency caveat. The MANIFEST.md makes the contingency concrete — readers see exactly which files were in the corpus.

### Mixed-format corpus
A folder of image-only scans + text-layer PDFs + .txt files + one .docx + a URL list — the manifest makes the variance visible; the downstream analysis can filter by `extraction_method` if the user wants to compare OCR'd vs. text-layer subsets.
