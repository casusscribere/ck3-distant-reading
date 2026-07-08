---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1566109/"
forum_thread_id: 1566109
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 114
title: "Dev Diary #114 - And the Winner is…"
dd_date: 2023-01-27
author_handle: rageair
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 304
inline_image_count: 1
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1566109'
extraction_rationale: |
  XenForo forum page rendered server-side; WebFetch's native
  HTML-to-Markdown conversion preserves the OP body, image
  references, and paragraph structure cleanly. Boundary
  detection performed by deterministic regex against the saved
  fetch output.
detected_artifacts:
  - type: webfetch_metadata
    location: raw_lines_1_to_~27
    action: discarded_from_output
  - type: forum_chrome
    location: raw_lines_~28_to_158
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_157
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2180.jpg?1674826716
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_160_to_162
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_189_to_193
    action: preserved_and_flagged
    counts:
      Like: 93
      Love: 16
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_201_to_282
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_283_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

<!-- artifact:thread_banner:start -->
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2180.jpg?1674826716)
<!-- artifact:thread_banner:end -->

# Dev Diary #114 - And the Winner is…

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Jan 27, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-114-and-the-winner-is.1566109/)
<!-- artifact:thread_metadata:end -->

Greetings!  

The polls are closed, and the winner is…  

**Wards and Wardens**  

Which I’m very excited about! Not only because it was the theme I *personally* liked the best, but because there’s a lot of interesting history to explore! We’ll definitely aim to make both rearing and playing as children more historically immersive, while also adding timeless content such as the (sometimes tenuous, sometimes wholesome) relations between parent and child.  

As mentioned in the previous Dev Diary, this event pack will be worked on later this year, after the next expansion is finished. For now, we will slowly start drawing out plans of content we’d like to make, and areas that’d be fun to explore - and here you can help!  

If you have a specific topic you’d like to see made into an event, or a situation you’d like to see expanded upon, please reply in this thread!  

For example, a specific topic might be *‘I’d like to see an event about one of my foreign wards missing their home’* or *‘I’d like an event where I as a child can become best friends with a vassal child’.*  

Examples of situations you’d like to see improved could be *‘I’d like to have the ability to impose a specific personality trait on a ward’*, or *‘I’d like if educating another ruler’s child would have more diplomatic benefits/complications’.*  

Finally, I’d like to leave you with another small teaser for the expansion. Last time some of you came extremely close to the truth, to the point where we had the artist of the image giggling with excitement… we’re hoping this one will throw you off a bit.  

![teaser2.png](https://forumcontent.paradoxplaza.com/public/929233/teaser2.png "teaser2.png")


[Image - Teaser2]

<!-- artifact:reactions:start -->
- 93 Like
- 16 Love
- 6 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 19 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
