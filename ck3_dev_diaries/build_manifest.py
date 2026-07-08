#!/usr/bin/env python3
"""Parse the CK3 Developer_diaries wikitext into a per-diary manifest JSON.

Input: wikitext (mediawiki source) on stdin or as a file argument.
Output: manifest.json with one row per forum-linked entry.

Each row: {forum_id, wiki_number, title, date, expansion, patch, section}.
- Forum-linked entries only (skips YouTube videos).
- Dedupes by forum_id (Northern Lords has 1478364 twice, with different titles).
- Console Edition gets expansion='Console Edition' to keep it separable.
- Unnumbered entries (wiki col '—' or '-') get wiki_number=None.
"""
import json, pathlib, re, sys

# Section heading: ==Expansion Name==
SECTION = re.compile(r"^==([^=]+)==\s*$")
# Patch subheading: ; Patch X.Y (Name) — captures the patch label
PATCH   = re.compile(r"^;\s*(Patch\s+[\d.]+(?:\s*\([^)]+\))?|Crusader Kings III(?:\s*Console Edition)?)\s*$")
# Table row with forum link:
#   | NUM || [[forum:ID|Title]] || desc || YYYY-MM-DD
# NUM can be a digit, '—', '-', '', or have a missing space; titles can contain pipes-inside-brackets.
ROW = re.compile(
    r"^\|\s*([\dxX—\-]*)\s*\|\|\s*\[\[forum:(\d+)\|([^\]]+?)\]\]\s*\|\|\s*(.*?)\s*\|\|\s*(\d{4}-\d{2}-\d{2})\s*$"
)
# Looser row (handles the "Stabilizing the Iberian peninsula [1.6.1 patch notes]]" weirdness)
ROW_LOOSE = re.compile(
    r"^\|\s*([\dxX—\-]*)\s*\|\|\s*\[\[forum:(\d+)\|(.+?)\]\](?:\s*\|\|\s*(.*?))?(?:\s*\|\|\s*(\d{4}-\d{2}-\d{2}))?\s*$"
)

def parse(text):
    section = None
    patch = None
    rows = []
    seen_ids = set()
    skip_section = False

    for line in text.splitlines():
        line = line.rstrip()
        m = SECTION.match(line)
        if m:
            section = m.group(1).strip()
            patch = None
            skip_section = section.lower() == "videos"
            continue
        if skip_section:
            continue
        m = PATCH.match(line)
        if m:
            patch = m.group(1).strip()
            continue
        if not line.startswith("|"):
            continue
        m = ROW.match(line) or ROW_LOOSE.match(line)
        if not m:
            continue
        wiki_num_raw = m.group(1).strip()
        forum_id = m.group(2)
        title = m.group(3).strip()
        desc = (m.group(4) or "").strip() if m.lastindex >= 4 else ""
        date = m.group(5) if m.lastindex >= 5 else None
        # Skip entries whose date didn't parse
        if not date:
            continue

        # Normalize wiki number
        if wiki_num_raw in ("", "—", "-", "x", "X"):
            wiki_num = None
        else:
            try:
                wiki_num = int(wiki_num_raw)
            except ValueError:
                wiki_num = None

        # Dedupe — first occurrence wins, but note the dupe
        if forum_id in seen_ids:
            continue
        seen_ids.add(forum_id)

        rows.append({
            "forum_id": forum_id,
            "wiki_number": wiki_num,
            "title": title,
            "date": date,
            "expansion": section,
            "patch": patch,
            "description": (desc if desc and desc != "....." else None),
            "source_url": f"https://forum.paradoxplaza.com/forum/threads/.{forum_id}/",
        })
    return rows

def main():
    if len(sys.argv) >= 2:
        text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()
    rows = parse(text)
    # Sort by date ascending so older diaries come first
    rows.sort(key=lambda r: (r["date"], int(r["forum_id"])))
    print(json.dumps(rows, indent=2, ensure_ascii=False))
    print(f"\n# Parsed {len(rows)} unique forum-linked entries", file=sys.stderr)

    # Stats
    expansions = {}
    for r in rows:
        expansions[r["expansion"]] = expansions.get(r["expansion"], 0) + 1
    print("# By expansion:", file=sys.stderr)
    for k in sorted(expansions, key=lambda e: expansions[e], reverse=True):
        print(f"#   {expansions[k]:>3}  {k}", file=sys.stderr)
    numbered = sum(1 for r in rows if r["wiki_number"] is not None)
    print(f"# Numbered: {numbered}  Unnumbered: {len(rows) - numbered}", file=sys.stderr)
    print(f"# Earliest: {rows[0]['date']} ({rows[0]['title']})", file=sys.stderr)
    print(f"# Latest:   {rows[-1]['date']} ({rows[-1]['title']})", file=sys.stderr)

if __name__ == "__main__":
    main()
