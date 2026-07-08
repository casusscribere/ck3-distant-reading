#!/usr/bin/env python3
"""Scan corpus_md/ and emit a MANIFEST.md index of every extracted diary."""
import re, pathlib, json, datetime

CORPUS = pathlib.Path("/sessions/eager-zealous-hawking/mnt/26_NEH_WORKSHOP/Week 3/ck3_dev_diaries")
WIKI_MANIFEST = pathlib.Path("/sessions/eager-zealous-hawking/mnt/outputs/ck3_extractor/manifest.json")
OUT = CORPUS / "MANIFEST.md"

# Parse YAML front-matter from each .md
def parse_fm(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m: return {}
    fm = {}
    for line in m.group(1).split("\n"):
        m2 = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m2:
            k = m2.group(1)
            v = m2.group(2).strip().strip('"').strip("'")
            fm[k] = v
    return fm

files = sorted([f for f in CORPUS.glob("dd_*.md") if f.name != "MANIFEST.md"])
rows = [parse_fm(f) | {"file": f.name} for f in files]
rows = [r for r in rows if r.get("title")]

# Load the wiki manifest for tracking missing entries
wiki_manifest = json.load(WIKI_MANIFEST.open())
extracted_ids = {r.get("forum_thread_id") for r in rows if r.get("forum_thread_id")}
missing = [e for e in wiki_manifest if e["forum_id"] not in extracted_ids]

# Group by expansion
by_expansion = {}
for r in rows:
    by_expansion.setdefault(r.get("expansion", "Unknown"), []).append(r)

# Build the MANIFEST.md
out = []
out.append("# Crusader Kings 3 Developer Diaries — Markdown Corpus")
out.append("")
out.append(f"*Generated {datetime.date.today().isoformat()} by the distant-reader skill plan's Step 0 pipeline.*")
out.append("")
out.append("This corpus contains provenance-tagged Markdown extractions of CK3 developer diaries posted on the Paradox Interactive forums since the game's announcement in October 2019. Each `dd_*.md` file is a Salter-style \"flag but do not alter\" extraction: the OP body is preserved verbatim, with forum infrastructure (banners, thread metadata, reactions, signature blocks, navigation chrome, replies) recorded in YAML front-matter and inline `<!-- artifact:* -->` comments rather than silently filtered.")
out.append("")
out.append("**Source index:** https://ck3.paradoxwikis.com/Developer_diaries (245 forum-linked entries in the wiki manifest as of the extraction date).")
out.append("")
out.append("## Corpus statistics")
out.append("")
out.append(f"- Extracted diaries: **{len(rows)}** of 245 wiki manifest entries ({len(rows)*100//245}% coverage)")
out.append(f"- Date range: {min(r['dd_date'] for r in rows if r.get('dd_date'))} to {max(r['dd_date'] for r in rows if r.get('dd_date'))}")
out.append(f"- Total body words: ~{sum(int(r.get('body_word_count', 0)) for r in rows):,}")
out.append(f"- Total inline images preserved: {sum(int(r.get('inline_image_count', 0)) for r in rows)}")
out.append("")

out.append("## By expansion")
out.append("")
for exp in sorted(by_expansion):
    diaries = by_expansion[exp]
    n = len(diaries)
    words = sum(int(d.get('body_word_count', 0)) for d in diaries)
    out.append(f"- **{exp}** — {n} diaries, ~{words:,} words")
out.append("")

out.append("## Files (chronological)")
out.append("")
out.append("| File | Date | Title | Author | Expansion | Words | Imgs |")
out.append("|------|------|-------|--------|-----------|------:|-----:|")
for r in sorted(rows, key=lambda r: r.get("dd_date", "")):
    out.append(f"| `{r['file']}` | {r.get('dd_date','?')} | {r.get('title','?')[:60]} | {r.get('author_handle','?')} | {r.get('expansion','?')} | {r.get('body_word_count','?')} | {r.get('inline_image_count','?')} |")
out.append("")

out.append("## Missing entries (in wiki manifest but not yet extracted)")
out.append("")
out.append(f"{len(missing)} entries in the wiki index remain unfetched. They were skipped due to conversation-context constraints during the initial run, not because of source-side problems. The deterministic pipeline can re-attempt all of them via the URLs below:")
out.append("")
out.append("<details><summary>Show missing entries</summary>")
out.append("")
out.append("| Wiki # | Date | Title | Expansion | Forum URL |")
out.append("|-------:|------|-------|-----------|-----------|")
for e in missing:
    num = e['wiki_number'] if e['wiki_number'] is not None else '—'
    out.append(f"| {num} | {e['date']} | {e['title']} | {e['expansion']} | {e['source_url']} |")
out.append("")
out.append("</details>")
out.append("")

out.append("## Provenance and pipeline")
out.append("")
out.append("Every `.md` file's YAML front-matter records:")
out.append("- `source_url`, `forum_thread_id`, `wiki_index_source`, `wiki_number`")
out.append("- `extraction_method` (always `webfetch_xenforo_text_layer` in this run — no OCR was needed)")
out.append("- `extraction_date`, `fetched_at`")
out.append("- `body_word_count`, `inline_image_count`, `language`")
out.append("- A structured `detected_artifacts` list with line ranges and per-artifact actions")
out.append("- `notes_for_analyst` describing extraction quirks")
out.append("")
out.append("Pipeline scripts that produced this corpus (all in this folder):")
out.append("- `build_manifest.py` — parses the wiki page's wikitext into a per-diary manifest JSON")
out.append("- `extract_diary.py` — deterministic XenForo OP-body extractor with boundary regexes and artifact tagging")
out.append("- `orchestrate.py` — matches saved WebFetch outputs to manifest rows and runs the extractor in bulk")
out.append("- `build_corpus_manifest.py` — emits this `MANIFEST.md`")
out.append("")
out.append("To continue extraction in a fresh session, run `WebFetch` on each missing URL above, then run `orchestrate.py`. The orchestrator is idempotent — it will only re-extract diaries whose temp files exist and whose manifest entry hasn't been written.")
out.append("")

OUT.write_text("\n".join(out), encoding="utf-8")
print(f"Wrote MANIFEST.md ({OUT.stat().st_size:,} bytes, {len(rows)} extracted entries, {len(missing)} missing)")
