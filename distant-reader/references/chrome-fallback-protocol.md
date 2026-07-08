# Claude in Chrome fallback protocol

## When to invoke Chrome MCP

Three triggers:

1. **WebFetch returned a truncated inline response.** The fetched content shows the page header and navigation chrome but no body. Common on XenForo forums (Paradox, many gaming communities). The URL probe (`00h_probe_url.py`) flags this and the orchestrator routes to Chrome.

2. **WebFetch returned a Cloudflare challenge.** Content looks like `Client Challenge`, `JavaScript is disabled in your browser`, or a similar stub. Common on paradoxwikis.com, some Substack publications behind Cloudflare, certain news sites.

3. **Known-protected domain.** Pre-route to Chrome for domains where WebFetch fails consistently. The URL probe's `CHROME_PREFERRED_DOMAINS` and `KNOWN_CLOUDFLARE` lists encode the empirically-discovered set.

## The protocol

The calling Claude session executes the following sequence per URL:

1. `mcp__Claude_in_Chrome__navigate` to the canonical URL.
2. `mcp__Claude_in_Chrome__computer` with `wait` action for **4–6 seconds**. The Cloudflare challenge resolves in 2–5 seconds; padding to 6 is conservative.
3. `mcp__Claude_in_Chrome__javascript_tool` with a content-scoped query (see selector table below) rather than `get_page_text` (which uses a "largest article" heuristic and can grab the wrong post on forums).
4. If the captured body is under ~1500 chars, pass directly to `00j_extract_chrome.py`. If longer, choose the long-body strategy.

## Per-platform content selectors

| Platform | Selector for OP / article body |
|---|---|
| XenForo (Paradox forums, many gaming) | `.message-body .bbWrapper` (first instance) |
| Substack | `article .body, article > .post-content` |
| Medium | `article > section > div` |
| WordPress (most themes) | `article .entry-content`, `.post-content`, `.entry` |
| Discourse | `.topic-post:first-of-type .cooked` |
| Reddit (old) | `.usertext-body` (first) |
| Generic | `article`, `main`, `.content` (in order) |

For new platforms, inspect the rendered DOM and add the selector here.

## Long-body strategy

For bodies that exceed the ~1500-char per-tool-call display ceiling:

- `--long-body-strategy=slice` — retrieve in 1KB chunks via `window.__op.slice(N, N+1000)`. Slow but complete. Use when the analysis depends on full word counts or full-text concordance.
- `--long-body-strategy=partial` — capture the first chunk, set `extraction_method: claude_in_chrome_partial_capture`, document the actual underlying byte count in `notes_for_analyst`. Use when the analysis is thematic and a representative excerpt suffices. This is what the CK3 run used for 6 of 10 over-cap OPs.
- `--long-body-strategy=skip` — emit a stub `.md` with the URL preserved and `extraction_method: chrome_skipped_long_body`. Use when you'll fetch these separately for a focused analysis.

Default: `partial`. The skill makes the choice user-overridable per corpus.

## Pitfalls

- **Tab pooling.** Don't open one tab per URL; reuse a single tab via `navigate` calls. Chrome retains cookies between navigations, which helps Cloudflare trust the session over time.
- **Cookie loss.** If a session has been idle for >30 minutes, Cloudflare may re-challenge. Re-run the wait sequence.
- **Reply confusion.** Without the content-scoped selector, `get_page_text` will return the longest article-element on the page, which on a busy forum thread is a popular user reply, not the OP. Always use the platform selector table.
