#!/usr/bin/env python3
"""extract_replies.py — companion to extract_diary.py.

Where extract_diary.py captures ONLY the opening post of a CK3 dev-diary thread
and discards every reply, this script captures the FULL response thread: every
reply post across every page of the thread, preserved as one provenance-tagged
Markdown file structured to mirror the dev-diary corpus so the two can be
distant-read comparatively (developer voice vs community voice).

It follows the same Salter-style "flag but do not alter" discipline as
extract_diary.py: reply bodies are preserved verbatim; quoted text, reaction
blocks, post signatures, and forum chrome are wrapped in <!-- artifact:* -->
comments and logged in YAML front-matter rather than deleted.

INPUT
  One or more saved page dumps for a single thread (WebFetch text or Claude-in-
  Chrome get_page_text capture), in page order. Same dump format extract_diary.py
  consumes: a short header (page title, urls, content-type), a blank line, then
  the page's text-rendered Markdown.

USAGE
  python3 extract_replies.py PAGE1.txt [PAGE2.txt ...] \
      --forum-id 1279641 --wiki-number 3 --date 2019-11-12 \
      --title "CK3 Dev Diary #3 - War" --expansion "Base game" \
      --parent-dd dd_003_2019-11-12_dev-diary-3-war.md \
      --out-dir ./ck3_reply_threads

The script is deterministic: same input dumps always produce the same output.

POST SEGMENTATION (see references at top of file)
  XenForo renders each post as a recurring block. We segment on the author
  profile heading that XenForo emits once per post, then locate within each
  block the timestamp/permalink, the message body, quoted material, the
  reactions line, and the per-post control row (Add bookmark / Report / Share).
  Markers are the SAME vocabulary extract_diary.py keys off; they live in the
  REGEX section below and are the one place to adjust after the first real
  capture if a forum theme change shifts the rendering.
"""
import argparse, datetime, json, pathlib, re, sys

# ─── Segmentation / boundary regexes (XenForo text rendering) ───────────────
# A post's author card: '### [Handle](https://.../forum/members/handle.12345/)'
RE_AUTHOR_CARD   = re.compile(r"^#{1,4}\s*\[([^\]]+)\]\((https://forum\.paradoxplaza\.com/forum/members/[^)]+)\)\s*$")
# Per-post permalink / id: '#post-123456' or '/post-123456'
RE_POST_ID       = re.compile(r"(?:#|/)post-(\d+)")
# Post timestamp as XenForo renders it in text, e.g. 'Nov 12, 2019' or
# 'Nov 12, 2019 at 4:05 PM' (also ISO-ish fallbacks).
RE_TIMESTAMP     = re.compile(r"\b([A-Z][a-z]{2,8}\s+\d{1,2},\s*\d{4})(?:\s+at\s+\d{1,2}:\d{2}\s*[AP]M)?\b")
# Reaction tally line(s): '- 14![Like](...)' or '- 14 Reactions:' or '- 14'
RE_REACT_FIRST   = re.compile(r"^- (\d+)!\[([A-Za-z][A-Za-z'+ ]*)\]")
RE_REACT_PLAIN   = re.compile(r"^- (\d+)\s*(?:Reactions:)?\s*$")
# XenForo quote rendering: a 'X said:' header and a 'Click to expand...' footer,
# and/or markdown blockquote lines beginning with '>'.
RE_QUOTE_HEAD    = re.compile(r"^\s*([A-Za-z0-9_\- ]{2,40})\s+said:\s*$")
RE_QUOTE_EXPAND  = re.compile(r"Click to expand\.\.\.")
RE_BLOCKQUOTE    = re.compile(r"^\s*>")
# Per-post control row that ends a post's visible body.
RE_CONTROL_ROW   = re.compile(r"^\s*-?\s*\[(Add bookmark|Report|Share|Quote|Reply|Like|\+Quote)\]")
RE_REPLY_BOUNDARY= re.compile(r"^- \[Add bookmark\]")
# Forum chrome / pagination we never treat as a post.
RE_PAGINATION    = re.compile(r"^\s*(Prev|Next|Page \d+ of \d+|\d+\s*$)")
RE_BODY_IMAGE    = re.compile(r"!\[[^\]]*\]\(https?://[^\)]+\)")
RE_OP_SIG_ROLE   = re.compile(r"^(Paradox|Community|Game|Lead|Senior|Content|Studio|Programmer|Designer|Producer)\b", re.I)


def read_dump(path):
    """Strip the dump header (page title / urls / content-type), return body."""
    raw = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    # header ends at first blank line after the 'Content-Type:' line, else line 4
    m = re.search(r"Content-Type:[^\n]*\n\n", raw)
    body = raw[m.end():] if m else raw
    # Chrome captures sometimes append a 'Tab Context:' trailer — drop it
    t = re.search(r"\n\s*Tab Context:", body)
    if t: body = body[:t.start()]
    return body


def find_replies_region(lines):
    """Return index after the OP+signature where replies begin.

    Strategy: the OP is the first author card; its body ends at the first
    '- [Add bookmark]' control row. Replies are everything after that first
    control row. If no boundary is found, fall back to the 2nd author card.
    """
    first_ctrl = None
    for i, ln in enumerate(lines):
        if RE_REPLY_BOUNDARY.match(ln):
            first_ctrl = i
            break
    if first_ctrl is not None:
        return first_ctrl + 1
    # fallback: second author card
    cards = [i for i, ln in enumerate(lines) if RE_AUTHOR_CARD.match(ln)]
    return cards[1] if len(cards) > 1 else (len(lines))


def segment_posts(lines, start):
    """Split lines[start:] into post blocks, one per author card."""
    idxs = [i for i in range(start, len(lines)) if RE_AUTHOR_CARD.match(lines[i])]
    blocks = []
    for n, i in enumerate(idxs):
        end = idxs[n + 1] if n + 1 < len(idxs) else len(lines)
        blocks.append((i, end))
    return blocks


def parse_quotes(body_lines):
    """Wrap XenForo quote spans in artifact:quote markers without deleting.
    Returns (wrapped_lines, quote_count)."""
    out, qcount, i = [], 0, 0
    n = len(body_lines)
    while i < n:
        ln = body_lines[i]
        if RE_QUOTE_HEAD.match(ln):
            # quote runs until 'Click to expand...' or a blank gap
            j = i
            closed = False
            while j < n:
                if RE_QUOTE_EXPAND.search(body_lines[j]):
                    closed = True; j += 1; break
                j += 1
                if j - i > 60: break
            out.append("<!-- artifact:quote:start -->")
            out.extend(body_lines[i:j])
            out.append("<!-- artifact:quote:end -->")
            qcount += 1
            i = j
            continue
        if RE_BLOCKQUOTE.match(ln):
            j = i
            while j < n and (RE_BLOCKQUOTE.match(body_lines[j]) or not body_lines[j].strip()):
                j += 1
            out.append("<!-- artifact:quote:start -->")
            out.extend(body_lines[i:j])
            out.append("<!-- artifact:quote:end -->")
            qcount += 1
            i = j
            continue
        out.append(ln)
        i += 1
    return out, qcount


def parse_post(lines, a, b):
    """Parse one post block lines[a:b] → dict."""
    m = RE_AUTHOR_CARD.match(lines[a])
    author = m.group(1).strip()
    author_url = m.group(2).strip()
    blk = lines[a + 1:b]
    # post id + timestamp (search whole block; take earliest)
    post_id = None; ts = None
    for ln in blk:
        if post_id is None:
            pm = RE_POST_ID.search(ln)
            if pm: post_id = pm.group(1)
        if ts is None:
            tm = RE_TIMESTAMP.search(ln)
            if tm: ts = tm.group(1)
        if post_id and ts: break
    # body = block minus leading role/meta lines, minus trailing reactions/controls
    # find body end: first reactions line or control row at/after some content
    # Body begins after the post-meta line. XenForo order per post is:
    #   author card -> forum rank/title -> [join date/msgs] -> timestamp+permalink -> body
    # So the permalink line is the cleanest body anchor; everything up to and
    # including it is per-post chrome (rank, timestamp) that we keep out of the body.
    meta_idx = -1
    for i, ln in enumerate(blk):
        if RE_POST_ID.search(ln):
            meta_idx = i; break
    if meta_idx < 0:
        for i, ln in enumerate(blk):
            if RE_TIMESTAMP.search(ln) and len(ln.strip()) < 40:
                meta_idx = i; break
    body_start = meta_idx + 1 if meta_idx >= 0 else 0
    while body_start < len(blk) and not blk[body_start].strip():
        body_start += 1
    if meta_idx < 0 and body_start < len(blk):
        s = blk[body_start].strip()
        if s and len(s.split()) <= 3 and not s.endswith((".", "!", "?", ":")):
            body_start += 1  # drop a bare forum-rank line e.g. 'Field Marshal'
        while body_start < len(blk) and not blk[body_start].strip():
            body_start += 1
    react = []
    body_end = len(blk)
    for i in range(body_start, len(blk)):
        if RE_REACT_FIRST.match(blk[i]) or RE_REACT_PLAIN.match(blk[i]):
            body_end = i
            # collect contiguous reaction lines
            for j in range(i, min(i + 10, len(blk))):
                rm = RE_REACT_FIRST.match(blk[j])
                if rm: react.append({"count": int(rm.group(1)), "label": rm.group(2).strip()})
                else:
                    rm = RE_REACT_PLAIN.match(blk[j])
                    if rm: react.append({"count": int(rm.group(1)), "label": "(unlabeled)"})
            break
        if RE_CONTROL_ROW.match(blk[i]):
            body_end = i; break
    body_lines = blk[body_start:body_end]
    # trim blanks
    while body_lines and not body_lines[0].strip(): body_lines.pop(0)
    while body_lines and not body_lines[-1].strip(): body_lines.pop()
    body_wrapped, qcount = parse_quotes(body_lines)
    # word count excludes quoted spans
    in_q = False; words = 0
    for ln in body_wrapped:
        if ln.startswith("<!-- artifact:quote:start"): in_q = True; continue
        if ln.startswith("<!-- artifact:quote:end"): in_q = False; continue
        if not in_q: words += len(re.findall(r"\w+", ln))
    images = sum(len(RE_BODY_IMAGE.findall(ln)) for ln in body_wrapped)
    return {
        "author": author, "author_url": author_url, "post_id": post_id,
        "timestamp": ts, "body": body_wrapped, "reactions": react,
        "quote_count": qcount, "word_count": words, "image_count": images,
    }


def parse_ts_to_iso(ts):
    if not ts: return None
    for fmt in ("%b %d %Y", "%B %d %Y"):
        try: return datetime.datetime.strptime(ts.replace(",", ""), fmt).strftime("%Y-%m-%d")
        except ValueError: pass
    return None


def slugify(s, maxlen=40):
    s = re.sub(r"[#\-_]+", " ", s.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:maxlen].strip("-")


def yaml_escape(s):
    if s is None: return "null"
    if any(c in str(s) for c in ":#\n\"'"):
        return '"' + str(s).replace('"', '\\"') + '"'
    return str(s)


def build_markdown(meta, posts, args, pages):
    L = ["---"]
    for k, v in meta.items():
        if v is None: L.append(f"{k}: null")
        elif isinstance(v, bool): L.append(f"{k}: {str(v).lower()}")
        elif isinstance(v, int): L.append(f"{k}: {v}")
        else: L.append(f"{k}: {yaml_escape(v)}")
    L.append("extraction_command: 'python3 extract_replies.py <pages...> --forum-id %s'" % args.forum_id)
    L.append("extraction_rationale: |")
    L.append("  Full reply thread captured across %d page dump(s). Each XenForo" % pages)
    L.append("  post segmented on its author card; timestamp, permalink, body,")
    L.append("  quoted material, and reaction tally located by deterministic regex.")
    L.append("  Quotes and reactions preserved-and-flagged, never deleted, so the")
    L.append("  community body text can be distant-read alongside the dev-diary corpus.")
    L.append("detected_artifacts:")
    L.append("  - type: quoted_text")
    L.append("    action: preserved_and_flagged")
    L.append("    note: XenForo quote spans wrapped in artifact:quote; excluded from reply word counts.")
    L.append("  - type: reactions")
    L.append("    action: preserved_and_flagged")
    L.append("  - type: forum_chrome")
    L.append("    action: discarded_from_output")
    L.append("    note: pagination, control rows (Add bookmark/Report/Share), badge icon lists.")
    L.append("notes_for_analyst: |")
    L.append("  Reply corpus parallel to the dev-diary corpus. Body text is the union")
    L.append("  of all reply post bodies (OP excluded — see parent_dd_file). Strip")
    L.append("  YAML + artifact comments before tokenizing, exactly as for dd_*.md.")
    L.append("---")
    L.append("")
    L.append(f"# Reply thread — {meta['title']}")
    L.append("")
    L.append(f"*{meta['reply_count']} replies from {meta['participant_count']} participants*")
    L.append("")
    for n, p in enumerate(posts, 1):
        head = f"## Reply {n} — {p['author']}"
        bits = []
        if p["timestamp"]: bits.append(p["timestamp"])
        if p["post_id"]: bits.append(f"post-{p['post_id']}")
        if bits: head += " · " + " · ".join(bits)
        L.append(head)
        L.append(f"<!-- post_author_url: {p['author_url']} -->")
        L.append("")
        L.extend(p["body"] if p["body"] else ["*(no text body — reaction-only or media-only post)*"])
        if p["reactions"]:
            L.append("")
            L.append("<!-- artifact:reactions:start -->")
            for r in p["reactions"]:
                L.append(f"- {r['count']} {r['label']}")
            L.append("<!-- artifact:reactions:end -->")
        L.append("")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Capture the full reply thread of a CK3 dev-diary forum thread.")
    ap.add_argument("pages", nargs="+", type=pathlib.Path, help="Saved page dumps, in page order")
    ap.add_argument("--forum-id", required=True)
    ap.add_argument("--wiki-number", default=None)
    ap.add_argument("--title", default=None)
    ap.add_argument("--date", default=None, help="DD publication date YYYY-MM-DD (for filename parity)")
    ap.add_argument("--expansion", default=None)
    ap.add_argument("--patch", default="Crusader Kings III")
    ap.add_argument("--parent-dd", default=None, help="Filename of the corresponding dd_*.md")
    ap.add_argument("--method", default="webfetch_xenforo_text_layer",
                    choices=["webfetch_xenforo_text_layer", "claude_in_chrome_dom_capture"])
    ap.add_argument("--out-dir", type=pathlib.Path, required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    posts = []
    for pg in args.pages:
        lines = read_dump(pg).split("\n")
        # Page 1 carries the OP (Thread starter / signature); skip it. Later
        # pages are entirely replies, so segment every author card from the top.
        is_op_page = any(re.search(r"Thread starter \[", ln) for ln in lines)
        start = find_replies_region(lines) if is_op_page else 0
        for a, b in segment_posts(lines, start):
            p = parse_post(lines, a, b)
            posts.append(p)

    # de-dupe by post_id (pages can overlap); keep order
    seen, uniq = set(), []
    for p in posts:
        key = p["post_id"] or (p["author"], tuple(p["body"][:1]))
        if key in seen: continue
        seen.add(key); uniq.append(p)
    posts = uniq

    participants = sorted({p["author"] for p in posts})
    dates = [parse_ts_to_iso(p["timestamp"]) for p in posts]
    dates = [d for d in dates if d]
    total_words = sum(p["word_count"] for p in posts)
    total_imgs = sum(p["image_count"] for p in posts)
    total_quotes = sum(p["quote_count"] for p in posts)

    title = args.title or f"Thread {args.forum_id}"
    title_for_slug = re.sub(r"^(?:CK3|Crusader Kings (?:III|3))\s*-?\s*", "", title, flags=re.I)
    title_for_slug = re.sub(r"^Dev(?:eloper)? Diary\s*#?\s*\d*\s*[-—]?\s*", "", title_for_slug, flags=re.I)
    slug = slugify(title_for_slug)
    wnum = (args.wiki_number or "x")
    wnum_file = wnum.replace("-", "x").zfill(3) if wnum not in ("x", "-", None) else "xxx"
    date_file = args.date or "unknown-date"
    filename = f"rt_{wnum_file}_{date_file}_{slug}__replies.md"

    meta = {
        "source_url": f"https://forum.paradoxplaza.com/forum/threads/.{args.forum_id}/",
        "forum_thread_id": args.forum_id,
        "content_type": "reply_thread",
        "parent_dd_file": args.parent_dd,
        "wiki_index_source": "https://ck3.paradoxwikis.com/Developer_diaries",
        "wiki_number": int(args.wiki_number) if (args.wiki_number or "").isdigit() else None,
        "title": title,
        "dd_date": args.date,
        "expansion": args.expansion,
        "patch": args.patch,
        "extraction_method": args.method,
        "extraction_date": datetime.date.today().strftime("%Y-%m-%d"),
        "fetched_at": datetime.date.today().strftime("%Y-%m-%d"),
        "text_layer_present": True,
        "ocr_used": False,
        "language": "en",
        "pages_captured": len(args.pages),
        "reply_count": len(posts),
        "participant_count": len(participants),
        "reply_date_first": (min(dates) if dates else None),
        "reply_date_last": (max(dates) if dates else None),
        "body_word_count": total_words,
        "inline_image_count": total_imgs,
        "quoted_span_count": total_quotes,
    }

    md = build_markdown(meta, posts, args, len(args.pages))
    out_path = args.out_dir / filename

    print(f"=== thread {args.forum_id} :: {title!r} ===")
    print(f"  pages parsed:    {len(args.pages)}")
    print(f"  replies:         {len(posts)}")
    print(f"  participants:    {len(participants)}")
    print(f"  reply words:     {total_words:,}  (quotes excluded; {total_quotes} quote spans flagged)")
    print(f"  date range:      {meta['reply_date_first']} → {meta['reply_date_last']}")
    print(f"  output:          {out_path}")
    if args.dry_run:
        print("  --dry-run: not written")
    else:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")
        print(f"  written:         {out_path.stat().st_size:,} bytes")
    return 0

if __name__ == "__main__":
    sys.exit(main() or 0)
