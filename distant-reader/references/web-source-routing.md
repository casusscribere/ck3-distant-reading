# Web-source routing decision tree

```
INPUT: URL
  │
  ▼
 ┌──────────────────────────┐
 │ 00h_probe_url.py — URL   │
 │ pattern matching         │
 └─────────────┬────────────┘
               │
       ┌───────┴────────┐
       │                │
       ▼                ▼
  Pre-routed to    Default: try
  Chrome (known    WebFetch first
  Cloudflare or
  XenForo)
       │                │
       │                ▼
       │       ┌─────────────────┐
       │       │ WebFetch returns│
       │       └────────┬────────┘
       │                │
       │       ┌────────┴──────────────────┐
       │       │            │              │
       │       ▼            ▼              ▼
       │   saved temp   complete       truncated
       │   file (full   inline OK      inline OR
       │   server-      under 80KB     Cloudflare
       │   render)                     stub
       │       │            │              │
       │       └────────────┴──────────────┤
       │                                   │
       ▼                                   ▼
  00j_extract_chrome.py            00i_extract_webfetch.py
  (Chrome path)                    (WebFetch path)
       │                                   │
       └─────────────────┬─────────────────┘
                         │
                         ▼
                  corpus_md/*.md
```

## Decision criteria

A page is **server-rendered-clean** if WebFetch returns either:
- A "too large, saved to file" stub with a complete page body in the saved temp file, OR
- A complete inline response under ~80 KB.

A page is **inline-truncated** if WebFetch returns an inline response that ends mid-content (no closing tags, body cut off after navigation chrome). This is the failure mode that affects some XenForo threads.

A page is **cloudflare-challenge** if the response contains the strings "Client Challenge", "JavaScript is disabled in your browser", or "Please enable JavaScript to proceed".

A page is **js-rendered-empty** if the response is structurally valid but the body section is empty (the JavaScript that would have populated it didn't run).

## Pre-routing

The skill maintains two lists in `00h_probe_url.py`:

- `CHROME_PREFERRED_DOMAINS` — domains where WebFetch is unreliable enough that going straight to Chrome saves a tool call.
- `KNOWN_CLOUDFLARE` — domains that always challenge.
- `WEBFETCH_PREFERRED_DOMAINS` — domains where WebFetch is reliable and Chrome would just add overhead.

These lists grow with experience. Encourage users to PR additions back when they encounter new patterns.
