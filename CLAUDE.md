# CK3 Distant Reading — NEH Workshop Week 4

Distant reading of the Crusader Kings III dev diaries and community responses,
published as a live GitHub Pages site.

## Publishing workflow (IMPORTANT)

This repository IS the live site. GitHub Pages serves the `main` branch from the
repository root. **After any change to site content, commit and push to `main`
to deploy — do this automatically, without being asked, whenever site-visible
files change.**

```
git add -A
git commit -m "<describe the change>"
git push
```

The site updates ~1 minute after push. Site-visible files: `index.html`,
everything under `ck3_distant_reading/`, and anything else linked from the
landing page.

## Site structure

- `index.html` — landing page (CK3 parchment theme, links the three reports)
- `ck3_distant_reading/` — the three HTML reports plus their PNG/SVG/JSON assets
- `ck3-style-guide/` — CK3 visual theme tokens (`theme.css`) used by the landing page
- `ck3_dev_diaries/`, `ck3_dev_diary_replies/` — markdown corpus (source texts)
- `ck3_reply_scraper/`, `distant-reader/` — Python tooling that built the corpus and reports

## Conventions

- Corpus markdown files carry provenance YAML front-matter — never strip it.
- Reports are self-contained HTML; regenerate via the tooling in `distant-reader/`
  rather than hand-editing analysis numbers.
- Analysis follows the Salter eight-step method (see `salter_best_practices.md`).
