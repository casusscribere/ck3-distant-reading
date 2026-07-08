---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1448340/"
forum_thread_id: 1448340
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 47
title: "CK3 Dev Diary #47 - Happy Holidays!"
dd_date: 2020-12-15
author_handle: PDX_Pariah
expansion: Post-release patches
patch: Patch 1.2 (Argent)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 217
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1448340'
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
    location: raw_lines_~28_to_144
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_146_to_148
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_164_to_169
    action: preserved_and_flagged
    counts:
      Like: 117
      Love: 22
      (unlabeled — rendered as base64 data URI): 7
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_177_to_238
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_239_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #47 - Happy Holidays!

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Dec 15, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-47-happy-holidays.1448340/)
<!-- artifact:thread_metadata:end -->

Howdy all!  

What a wild ride this entire year has been so far! We launched the game, brought the Ruler Designer to a new generation of CK fans, created a wholesome and welcoming community, and had a ton of fun.  

While there is still a bit of time left in the year, we will be following in the footsteps of the long time-honored Paradox tradition of taking some time off around the holidays to give the teams a chance to recuperate and relax. This will also make sure that we are able to continue bringing you first class content in the new year! That being said, most of the team will be out spending time enjoying their holidays from this week until sometime early January 2021.  

Without all of you in the Community, we would not be able to live our dreams of bringing Crusader Kings to life and share with you all. So, from the bottom of our hearts, THANK YOU for the wonderful memories during a truly trying year and may we see you all again in the new year.  

**There won’t be a Dev Diary until Mid-January at the very earliest, so keep an eye out for news on when they will return after the new year.**  

Happy Holidays to all!

<!-- artifact:reactions:start -->
- 117 Like
- 22 Love
- 10 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)**
Role: Community Manager
Badges: 46
Messages: 119
Reaction score: 4,454

*[Full game-badge icon list of 9 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
