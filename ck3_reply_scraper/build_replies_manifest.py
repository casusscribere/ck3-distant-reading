#!/usr/bin/env python3
"""build_replies_manifest.py — index the reply-thread corpus (parallels
build_corpus_manifest.py for the dev-diary corpus)."""
import re, pathlib, argparse, datetime

def parse_fm(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    fm = {}
    if m:
        for line in m.group(1).split("\n"):
            mm = re.match(r"^([a-z_]+):\s*(.*)$", line)
            if mm: fm[mm.group(1)] = mm.group(2).strip().strip('"').strip("'")
    return fm

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", required=True, type=pathlib.Path)
    args = ap.parse_args()
    files = sorted(f for f in args.corpus.glob("rt_*.md") if f.name != "MANIFEST.md")
    rows = [parse_fm(f) | {"file": f.name} for f in files]
    def I(r,k,d=0):
        try: return int(r.get(k,d))
        except: return d
    tot_replies = sum(I(r,"reply_count") for r in rows)
    tot_words   = sum(I(r,"body_word_count") for r in rows)
    tot_quotes  = sum(I(r,"quoted_span_count") for r in rows)
    by_exp = {}
    for r in rows: by_exp.setdefault(r.get("expansion","Unknown"), []).append(r)

    o=[]
    o.append("# Crusader Kings 3 Developer-Diary REPLY Threads — Markdown Corpus")
    o.append("")
    o.append(f"*Generated {datetime.date.today().isoformat()} by extract_replies.py (companion to the dev-diary corpus).*")
    o.append("")
    o.append("This corpus is the **community-voice counterpart** to the dev-diary corpus. "
             "For each dev diary, it captures the full reply thread — every reply post across "
             "every forum page — as one provenance-tagged Markdown file (`rt_*.md`) structured "
             "to mirror `dd_*.md`. Reply bodies are preserved verbatim; quoted text and reaction "
             "tallies are wrapped in `<!-- artifact:* -->` comments and excluded from word counts, "
             "so the two corpora can be distant-read and compared on equal terms.")
    o.append("")
    o.append("Each `rt_*.md` front-matter carries `parent_dd_file` linking it to its dev diary, "
             "plus `reply_count`, `participant_count`, `pages_captured`, `reply_date_first/last`, "
             "and `quoted_span_count`.")
    o.append("")
    o.append("## Corpus statistics")
    o.append("")
    o.append(f"- Reply threads: **{len(rows)}**")
    o.append(f"- Total replies captured: **{tot_replies:,}**")
    o.append(f"- Total reply body words (quotes excluded): **{tot_words:,}**")
    o.append(f"- Quoted spans flagged: **{tot_quotes:,}**")
    dts=[r.get("dd_date") for r in rows if r.get("dd_date")]
    if dts: o.append(f"- Date range: {min(dts)} to {max(dts)}")
    o.append("")
    o.append("## By expansion")
    o.append("")
    for e in sorted(by_exp, key=lambda k:-sum(I(r,'reply_count') for r in by_exp[k])):
        rs=by_exp[e]
        o.append(f"- **{e}** — {len(rs)} threads, {sum(I(r,'reply_count') for r in rs):,} replies, "
                 f"{sum(I(r,'body_word_count') for r in rs):,} words")
    o.append("")
    o.append("## Files (chronological)")
    o.append("")
    o.append("| File | Parent diary | Date | Replies | Participants | Words | Quotes |")
    o.append("|------|--------------|------|--------:|-------------:|------:|-------:|")
    for r in sorted(rows, key=lambda r:r.get("dd_date") or ""):
        o.append(f"| `{r['file']}` | `{r.get('parent_dd_file','—')}` | {r.get('dd_date','?')} | "
                 f"{I(r,'reply_count')} | {I(r,'participant_count')} | {I(r,'body_word_count')} | {I(r,'quoted_span_count')} |")
    (args.corpus/"MANIFEST.md").write_text("\n".join(o)+"\n", encoding="utf-8")
    print(f"Wrote {args.corpus/'MANIFEST.md'} — {len(rows)} threads, {tot_replies:,} replies, {tot_words:,} words")

if __name__ == "__main__":
    main()
