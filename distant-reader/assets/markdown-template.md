---
source_file: "{FILENAME}"           # or source_url for web sources
source_sha256: {SHA256}              # 64-char hex hash
wiki_index_source: null              # optional URL of an index pointing at this source
title: "{TITLE}"
author_handle: {AUTHOR_OR_NULL}
date: {YYYY-MM-DD}
expansion: null                      # optional grouping for comparative analysis
patch: null                          # optional finer grouping
extraction_method: pdftotext_layout  # one of the known methods (see 00g_validate_markdown.py)
extraction_command: "{COMMAND}"
extraction_date: {YYYY-MM-DD}
fetched_at: {YYYY-MM-DD}
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: {N}
inline_image_count: {N}
detected_artifacts:
  - type: bare_page_number
    occurrences: {N}
  - type: running_header
    pattern: "{HEADER_TEXT}"
    occurrences: {N}
notes_for_analyst: |
  Any non-routine observations about this extraction — image-only pages, OCR
  quality dips, manual corrections, etc.
---

<!-- artifact:thread_banner:start -->
{Banner / cover image if present}
<!-- artifact:thread_banner:end -->

# {TITLE}

<!-- artifact:thread_metadata:start -->
{Optional metadata block — thread starter, date links}
<!-- artifact:thread_metadata:end -->

{The body — preserved verbatim. Page numbers, running headers, etc. are
inline-wrapped in <!-- artifact:type --> comments without being removed.}

<!-- artifact:references_section:start -->
{Reference list goes here if present}
<!-- artifact:references_section:end -->
