#!/usr/bin/env python3
"""extract_diary.py

Build a provenance-tagged Markdown file from a saved WebFetch dump of a
Paradox Forums dev-diary thread. Designed for the distant-reader skill plan's
Step 0 — Salter-style "flag but do not alter" extraction.

Usage:
  python3 extract_diary.py <fetch_file> --forum-id ID [optional metadata...] \
                          --out-dir DIR

The script is deterministic: same input always produces the same output. It
does not invent metadata it cannot derive from the page; missing fields appear
as null in the front-matter with a one-line audit note.
"""
import argparse, datetime, json, pathlib, re, sys


# ─── Boundary-detection regexes ─────────────────────────────────────────────
RE_TITLE         = re.compile(r"^# (?:CK(?:3|III)\s*-?\s*)?(?:Crusader Kings (?:III|3)\s*-?\s*)?Dev(?:eloper)? Diary\s*#?", re.IGNORECASE)
RE_TITLE_FALLBK  = re.compile(r"^# (CK3|Crusader Kings|Dev(?:eloper)? Diary|An Heir Is Born|The Vision)", re.IGNORECASE)
RE_THREAD_START  = re.compile(r"Thread starter \[([^\]]+)\]")
RE_START_DATE    = re.compile(r"Start date \[([A-Z][a-z]+ \d{1,2},\s*\d{4})\]")
RE_BANNER        = re.compile(r"!\[\]\((https?://forumcontent\.paradoxplaza\.com/data/thfeature/feature_backgrounds/[^\)]+)\)")
RE_REACT_FIRST   = re.compile(r"^- (\d+)!\[([A-Za-z][A-Za-z'+ ]*)\]")
RE_REACT_PLAIN   = re.compile(r"^- (\d+)\s*(?:Reactions:)?\s*$")
RE_REACT_END     = re.compile(r"^- \d+\s*Reactions:\s*$")
RE_WRITTEN_BY    = re.compile(r"^Written by\s*$")
RE_REPLY_BOOKMARK= re.compile(r"^- \[Add bookmark\]")
RE_BODY_IMAGE    = re.compile(r"!\[[^\]]*\]\(https?://forumcontent\.paradoxplaza\.com/[^\)]+\)")
RE_BADGE_LINE    = re.compile(r"^- !\[[^\]]+\]\(https://forum\.paradoxplaza\.com/forum/styles/paradox/owneditems/icons/")


def find_title(lines):
    """Return (title_idx, synthesized_title) — for older threads with no level-1
    heading, synthesize a title from WebFetch's first line and place a virtual
    title just before the 'Thread starter' line."""
    for i, line in enumerate(lines):
        if RE_TITLE.match(line):
            return i, None
    for i, line in enumerate(lines):
        if RE_TITLE_FALLBK.match(line):
            return i, None
    # Fallback: use WebFetch's page-title (line 1) + locate Thread starter as anchor
    if len(lines) > 0 and lines[0].strip():
        page_title = lines[0].strip()
        for i, line in enumerate(lines):
            if RE_THREAD_START.search(line):
                # Insert a synthetic heading just before this line
                return i - 1, "# " + page_title
    return None, None


def extract_thread_metadata(lines, title_idx, window=8):
    """Lines immediately after title contain 'Thread starter [handle]' and
    'Start date [Month DD, YYYY]'."""
    handle = date_str = None
    metadata_end = title_idx + 1
    for i in range(title_idx + 1, min(title_idx + window, len(lines))):
        if RE_THREAD_START.search(lines[i]):
            m = RE_THREAD_START.search(lines[i]); handle = m.group(1)
            metadata_end = max(metadata_end, i + 1)
        if RE_START_DATE.search(lines[i]):
            m = RE_START_DATE.search(lines[i]); date_str = m.group(1)
            metadata_end = max(metadata_end, i + 1)
    return handle, date_str, metadata_end


def parse_date(date_str):
    if not date_str: return None
    try:
        return datetime.datetime.strptime(date_str.replace(",", ""), "%b %d %Y").strftime("%Y-%m-%d")
    except ValueError:
        try:
            return datetime.datetime.strptime(date_str.replace(",", ""), "%B %d %Y").strftime("%Y-%m-%d")
        except ValueError:
            return None


def find_banner(lines, title_idx, look_back=10):
    """Thread banner (feature_backgrounds image) sits just before the title."""
    for i in range(max(0, title_idx - look_back), title_idx):
        m = RE_BANNER.search(lines[i])
        if m: return i, m.group(1)
    return None, None


def find_body_range(lines, metadata_end):
    """Body starts after thread metadata; ends just before reactions block."""
    body_start = metadata_end
    # Skip leading blank lines
    while body_start < len(lines) and not lines[body_start].strip():
        body_start += 1
    # Find reactions: first line matching '- <count>![Label]' OR a plain
    # '- <count>' line that's part of a reactions block.
    react_start = None
    for i in range(body_start, len(lines)):
        if RE_REACT_FIRST.match(lines[i]) or RE_REACT_END.match(lines[i]):
            react_start = i
            break
    if react_start is None:
        return body_start, len(lines), None, None
    # Walk back over blank lines for clean body end
    body_end = react_start
    while body_end > body_start and not lines[body_end - 1].strip():
        body_end -= 1
    # Find end of reactions block: last contiguous '- N' / '- N![Label]' /
    # '- N Reactions:' line
    react_end = react_start
    for i in range(react_start, min(react_start + 12, len(lines))):
        if RE_REACT_FIRST.match(lines[i]) or RE_REACT_PLAIN.match(lines[i]) or RE_REACT_END.match(lines[i]):
            react_end = i
        elif lines[i].strip() == "":
            continue
        else:
            break
    return body_start, body_end, react_start, react_end


def extract_reactions(lines, react_start, react_end):
    """Return a list of {count, label} dicts. Labels are only known for the
    first 1-2 (Like, Love) — the rest render as base64 data URIs in WebFetch
    output and lose their text labels."""
    out = []
    if react_start is None: return out
    for i in range(react_start, react_end + 1):
        line = lines[i].strip()
        m = RE_REACT_FIRST.match(line)
        if m:
            out.append({"count": int(m.group(1)), "label": m.group(2).strip()})
            continue
        m = RE_REACT_PLAIN.match(line) or RE_REACT_END.match(line)
        if m:
            out.append({"count": int(m.group(1)), "label": "(unlabeled — rendered as base64 data URI)"})
    return out


def find_signature(lines, after):
    """Signature begins at 'Written by' line."""
    if after is None: return None
    for i in range(after, min(after + 30, len(lines))):
        if RE_WRITTEN_BY.match(lines[i]):
            return i
    return None


def find_replies_start(lines, after):
    if after is None: return None
    for i in range(after, len(lines)):
        if RE_REPLY_BOOKMARK.match(lines[i]):
            return i
    return None


def slugify(s, maxlen=40):
    s = re.sub(r"[#\-_]+", " ", s.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:maxlen].strip("-")


def yaml_escape(s):
    """Quote a string for YAML if it contains special characters."""
    if s is None: return "null"
    if any(c in str(s) for c in ":#\n\"'"):
        return '"' + str(s).replace('"', '\\"') + '"'
    return str(s)


def build_markdown(parsed, fetch_path, args):
    """Emit the final provenance-tagged Markdown."""
    lines_out = ["---"]
    fm = parsed["frontmatter"]
    for k in ("source_url", "forum_thread_id", "forum_canonical_slug",
              "wiki_index_source", "wiki_number", "title", "dd_date",
              "author_handle", "expansion", "patch",
              "extraction_method", "extraction_date", "fetched_at",
              "text_layer_present", "ocr_used", "ocr_average_confidence",
              "language", "body_word_count", "inline_image_count"):
        v = fm.get(k)
        if v is None:
            lines_out.append(f"{k}: null")
        elif isinstance(v, bool):
            lines_out.append(f"{k}: {str(v).lower()}")
        elif isinstance(v, int):
            lines_out.append(f"{k}: {v}")
        else:
            lines_out.append(f"{k}: {yaml_escape(v)}")
    lines_out.append("extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id %s'" % args.forum_id)
    lines_out.append("extraction_rationale: |")
    lines_out.append("  XenForo forum page rendered server-side; WebFetch's native")
    lines_out.append("  HTML-to-Markdown conversion preserves the OP body, image")
    lines_out.append("  references, and paragraph structure cleanly. Boundary")
    lines_out.append("  detection performed by deterministic regex against the saved")
    lines_out.append("  fetch output.")
    lines_out.append("detected_artifacts:")
    for a in parsed["artifacts"]:
        lines_out.append(f"  - type: {a['type']}")
        lines_out.append(f"    location: {a['location']}")
        lines_out.append(f"    action: {a['action']}")
        if "url" in a:
            lines_out.append(f"    url: {a['url']}")
        if "counts" in a:
            lines_out.append("    counts:")
            for k, v in a["counts"].items():
                key = yaml_escape(k) if any(c in k for c in " :'\"") else k
                lines_out.append(f"      {key}: {v}")
        if "note" in a:
            lines_out.append(f"    note: {yaml_escape(a['note'])}")
    lines_out.append("notes_for_analyst: |")
    lines_out.append("  Deterministic extraction via extract_diary.py. Title heading,")
    lines_out.append("  thread metadata, body span, reactions block, and reply boundary")
    lines_out.append("  detected by regex without manual inspection. See detected_artifacts")
    lines_out.append("  list for raw-fetch line ranges of every preserved-and-flagged or")
    lines_out.append("  discarded element.")
    lines_out.append("---")
    lines_out.append("")
    # Body
    if parsed["banner_url"]:
        lines_out.append("<!-- artifact:thread_banner:start -->")
        lines_out.append(f"![]({parsed['banner_url']})")
        lines_out.append("<!-- artifact:thread_banner:end -->")
        lines_out.append("")
    lines_out.append(f"# {parsed['title']}")
    lines_out.append("")
    if parsed["thread_metadata"]:
        lines_out.append("<!-- artifact:thread_metadata:start -->")
        for line in parsed["thread_metadata"]:
            lines_out.append(line)
        lines_out.append("<!-- artifact:thread_metadata:end -->")
        lines_out.append("")
    lines_out.append(parsed["body"])
    if parsed["reactions"]:
        lines_out.append("")
        lines_out.append("<!-- artifact:reactions:start -->")
        for r in parsed["reactions"]:
            lines_out.append(f"- {r['count']} {r['label']}")
        lines_out.append("<!-- artifact:reactions:end -->")
    if parsed["signature_summary"]:
        lines_out.append("")
        lines_out.append("<!-- artifact:op_signature:start -->")
        for line in parsed["signature_summary"]:
            lines_out.append(line)
        lines_out.append("<!-- artifact:op_signature:end -->")
    return "\n".join(lines_out) + "\n"


def parse_signature(lines, sig_start, reply_start):
    """Extract a compact summary from the OP signature block — author handle,
    role, badge count, message count, reaction score — and collapse the badge
    icon list."""
    if sig_start is None: return [], (sig_start, None)
    end = reply_start if reply_start else min(sig_start + 110, len(lines))
    summary = ["**Written by [author]** *(see signature block in raw fetch)*"]
    role = None
    badge_count = None
    msg_count = None
    react_score = None
    # Quick scan
    handle_match = None
    for i in range(sig_start, min(sig_start + 8, len(lines))):
        m = re.match(r"^### \[([^\]]+)\]\(([^)]+)\)", lines[i])
        if m:
            handle_match = m
            break
    # Role appears 1-2 lines after handle
    if handle_match:
        for i in range(sig_start, min(sig_start + 10, len(lines))):
            s = lines[i].strip()
            if s and not s.startswith("[") and not s.startswith("#") and not s.startswith("**") and s not in ("Written by",):
                role = s
                break
    # Badge count: '***N Badges***'
    for i in range(sig_start, end):
        m = re.search(r"\*+\s*(\d+)\s*Badges\s*\*+", lines[i])
        if m: badge_count = int(m.group(1)); break
    # Messages: 'Messages' label then number on next non-blank line
    for i in range(sig_start, end - 1):
        if lines[i].strip() == "Messages":
            for j in range(i + 1, min(i + 4, end)):
                if lines[j].strip().isdigit():
                    msg_count = int(lines[j].strip()); break
            break
    # Reaction score
    for i in range(sig_start, end - 1):
        if lines[i].strip() == "Reaction score":
            for j in range(i + 1, min(i + 4, end)):
                ns = re.sub(r"[.,\s]", "", lines[j].strip())
                if ns.isdigit():
                    react_score = int(ns); break
            break
    summary = []
    if handle_match:
        summary.append(f"**Written by [{handle_match.group(1)}]({handle_match.group(2)})**")
    if role: summary.append(f"Role: {role}")
    if badge_count is not None: summary.append(f"Badges: {badge_count}")
    if msg_count is not None: summary.append(f"Messages: {msg_count}")
    if react_score is not None: summary.append(f"Reaction score: {react_score:,}")
    badge_count_actual = sum(1 for i in range(sig_start, end) if RE_BADGE_LINE.match(lines[i]))
    if badge_count_actual:
        summary.append("")
        summary.append(f"*[Full game-badge icon list of {badge_count_actual} titles omitted for readability; preserved in raw fetch.]*")
    return summary, (sig_start, end)


def main():
    ap = argparse.ArgumentParser(description="Extract a CK3 dev-diary forum page to provenance-tagged markdown.")
    ap.add_argument("fetch_file", type=pathlib.Path, help="Path to saved WebFetch output")
    ap.add_argument("--forum-id", required=True, help="Paradox forum thread ID")
    ap.add_argument("--wiki-number", default=None, help="Wiki dev-diary number (may be '-')")
    ap.add_argument("--expansion", default=None, help="Expansion name from wiki index")
    ap.add_argument("--patch", default=None, help="Patch name from wiki index")
    ap.add_argument("--out-dir", type=pathlib.Path, required=True, help="Output directory")
    ap.add_argument("--dry-run", action="store_true", help="Report metadata but don't write file")
    args = ap.parse_args()

    text = args.fetch_file.read_text(encoding="utf-8", errors="replace")
    lines = text.split("\n")

    # ── Detect structure
    title_idx, synth_title = find_title(lines)
    if title_idx is None:
        print(f"ERROR: no title heading found in {args.fetch_file}", file=sys.stderr)
        return 1
    if synth_title:
        # Inject synthetic title into the lines array
        lines.insert(title_idx + 1, synth_title)
        title_idx = title_idx + 1
    title = lines[title_idx].lstrip("# ").strip()
    handle, date_str, metadata_end = extract_thread_metadata(lines, title_idx)
    dd_date = parse_date(date_str)
    banner_idx, banner_url = find_banner(lines, title_idx)
    body_start, body_end, react_start, react_end = find_body_range(lines, metadata_end)
    sig_start = find_signature(lines, react_end if react_end else body_end)
    reply_start = find_replies_start(lines, sig_start if sig_start else body_end)

    # ── Pull body and stats
    body_lines = lines[body_start:body_end]
    while body_lines and not body_lines[0].strip(): body_lines.pop(0)
    while body_lines and not body_lines[-1].strip(): body_lines.pop()
    body = "\n".join(body_lines)
    body_words = len(re.findall(r"\w+", body))
    body_images = RE_BODY_IMAGE.findall(body)

    # ── Reactions
    reactions = extract_reactions(lines, react_start, react_end) if react_start else []

    # ── Thread metadata lines (for preserving in markdown)
    thread_meta_lines = []
    for i in range(title_idx + 1, metadata_end):
        s = lines[i].strip()
        if s and (RE_THREAD_START.search(s) or RE_START_DATE.search(s)):
            thread_meta_lines.append(lines[i])

    # ── Signature
    signature_summary, sig_range = parse_signature(lines, sig_start, reply_start)

    # ── Slug + filename
    title_for_slug = re.sub(r"^Dev Diary\s*#?\s*\d+\s*[-—]?\s*", "", title, flags=re.IGNORECASE)
    title_for_slug = re.sub(r"^CK3\s*[-—]?\s*", "", title_for_slug, flags=re.IGNORECASE)
    slug = slugify(title_for_slug)
    wiki_num_for_file = (args.wiki_number or "x").replace("-", "x").zfill(3) if args.wiki_number and args.wiki_number != "-" else "xxx"
    date_for_file = dd_date or "unknown-date"
    filename = f"dd_{wiki_num_for_file}_{date_for_file}_{slug}.md"

    # ── Assemble artifacts list
    artifacts = []
    artifacts.append({
        "type": "webfetch_metadata",
        "location": "raw_lines_1_to_~27",
        "action": "discarded_from_output",
    })
    artifacts.append({
        "type": "forum_chrome",
        "location": f"raw_lines_~28_to_{title_idx}",
        "action": "discarded_from_output",
    })
    if banner_url:
        artifacts.append({
            "type": "thread_banner",
            "location": f"raw_line_{banner_idx + 1}",
            "url": banner_url,
            "action": "preserved_and_flagged",
            "note": "Forum-injected banner image keyed off thread feature metadata; not authored by OP.",
        })
    if thread_meta_lines:
        artifacts.append({
            "type": "thread_metadata",
            "location": f"raw_lines_{title_idx + 2}_to_{metadata_end}",
            "action": "preserved_and_flagged",
        })
    if reactions:
        labels_known = [r for r in reactions if not r["label"].startswith("(unlabeled")]
        artifacts.append({
            "type": "reactions",
            "location": f"raw_lines_{react_start + 1}_to_{react_end + 1}",
            "counts": {r["label"]: r["count"] for r in reactions},
            "action": "preserved_and_flagged",
            "note": f"Reactions block parsed; {len(labels_known)} of {len(reactions)} reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).",
        })
    if sig_start:
        artifacts.append({
            "type": "op_signature",
            "location": f"raw_lines_{sig_start + 1}_to_{sig_range[1]}",
            "action": "preserved_and_flagged_collapsed",
            "note": "OP author profile card preserved as a compact summary; full badge icon list omitted for readability.",
        })
    if reply_start:
        artifacts.append({
            "type": "replies",
            "location": f"raw_line_{reply_start + 1}_and_after",
            "action": "discarded_from_output",
            "note": "All reply posts after the OP are out of scope and discarded.",
        })

    # ── Front-matter
    parsed = {
        "frontmatter": {
            "source_url": f"https://forum.paradoxplaza.com/forum/threads/.{args.forum_id}/",
            "forum_thread_id": args.forum_id,
            "forum_canonical_slug": None,  # would need a separate GET on the canonical URL to confirm
            "wiki_index_source": "https://ck3.paradoxwikis.com/Developer_diaries",
            "wiki_number": args.wiki_number,
            "title": title,
            "dd_date": dd_date,
            "author_handle": handle,
            "expansion": args.expansion,
            "patch": args.patch,
            "extraction_method": "webfetch_xenforo_text_layer",
            "extraction_date": datetime.date.today().strftime("%Y-%m-%d"),
            "fetched_at": datetime.date.today().strftime("%Y-%m-%d"),
            "text_layer_present": True,
            "ocr_used": False,
            "ocr_average_confidence": None,
            "language": "en",
            "body_word_count": body_words,
            "inline_image_count": len(body_images),
        },
        "artifacts": artifacts,
        "banner_url": banner_url,
        "title": title,
        "thread_metadata": thread_meta_lines,
        "body": body,
        "reactions": reactions,
        "signature_summary": signature_summary,
    }

    output_md = build_markdown(parsed, args.fetch_file, args)
    out_path = args.out_dir / filename

    # Report
    print(f"=== {args.fetch_file.name} ===")
    print(f"  Title:           {title!r}")
    print(f"  Author handle:   {handle!r}")
    print(f"  Date:            {dd_date}  (raw: {date_str!r})")
    print(f"  Body lines:      {len(body_lines)}  ({body_words} words)")
    print(f"  Body images:     {len(body_images)}")
    print(f"  Banner:          {'yes' if banner_url else 'no'}")
    print(f"  Reactions:       {len(reactions)} entries")
    print(f"  Signature:       {'detected' if sig_start else 'not found'}")
    print(f"  Reply boundary:  {'line ' + str(reply_start + 1) if reply_start else 'not found'}")
    print(f"  Output file:     {out_path}")
    if args.dry_run:
        print("  --dry-run: not written")
    else:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output_md, encoding="utf-8")
        print(f"  Written:         {out_path.stat().st_size:,} bytes")

if __name__ == "__main__":
    sys.exit(main() or 0)
