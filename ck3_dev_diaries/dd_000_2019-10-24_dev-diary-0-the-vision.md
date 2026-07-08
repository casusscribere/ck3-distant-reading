---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1265472/"
forum_thread_id: 1265472
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 0
title: "CK3 - Dev Diary #0 - The Vision"
dd_date: 2019-10-24
author_handle: Doomdark
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 457
inline_image_count: 1
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1265472'
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
    location: raw_lines_173_to_177
    action: preserved_and_flagged
    counts:
      Like: 13
      Love: 5
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_185_to_295
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_296_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 - Dev Diary #0 - The Vision

<!-- artifact:thread_metadata:start -->
- Thread starter [Doomdark](https://forum.paradoxplaza.com/forum/members/doomdark.153/)
- Start date [Oct 24, 2019](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-0-the-vision.1265472/)
<!-- artifact:thread_metadata:end -->

![titus_gamevision.png](https://forumcontent.paradoxplaza.com/public/paradox/banners/titus_gamevision.png "")

  

Greetings friends!  

It’s my pleasure to finally be able to talk about what I’ve been working on ever since Stellaris came out (and before) - Crusader Kings III, of course! CK3 draws on the wisdom gained over CK2’s seven long years of expansions and patches - all the things we simply could not do in that game - and represents the natural evolution of Crusader Kings. Yes, CK3 is an evolution, not a revolution; it’s better across the board and does not alter the core CK experience. That said, we did not carry over everything from every expansion and update to CK2. Rather than trying to do full justice to the less appreciated systems, we decided to go deep rather than wide.  

The main design goals with Crusader Kings III were:  


- **Character Focus**: Crusader Kings is clearly and unequivocally about individual characters, unlike our other games. This makes CK most suited for memorable emergent stories, and we wanted to bring characters into all important gameplay mechanics (where possible.)
- **Player Freedom and Progression**: We want to cater to all player fantasies we can reasonably accommodate, allowing players to shape their ruler, heirs, dynasty and even religion to their liking - though there should of course be appropriate challenges to overcome.
- **Player Stories:** All events and scripted content should feel *relevant*, *impactful* and *immersive* in relation to the underlying simulation. That way, players will perceive and remember stories - their own stories, not the developers’ stories.
- **Approachability**: Crusader Kings III should be user friendly without compromising its general level of complexity and historical flavor. It’s nice if it’s easier to get into, but more than that, it should be clear what everything in the game is, what you might want to be doing, and how to go about it.
Now, you might say: “Cool, but I took the time to master CK2, bought all the expansions, and now it provides me an enormous breadth of options. Why should I buy CK3?”  

That’s a fair question! As I mentioned earlier, we decided not to carry over all features from CK2, so if you play CK2 primarily for, say, the nomads or the merchant republics (the only faction types that were playable in CK2 but not in CK3), you might be disappointed. There are likely other features and content that will be missed by some players, but, in return, we believe that everyone will find the core gameplay far more fun and rewarding! To be clear, CK3 is a vastly bigger game than CK2 was on release.  

I know this dev diary was short on details, but don’t despair - they will be revealed over the coming months!

<!-- artifact:reactions:start -->
- 13 Like
- 5 Love
- 5 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Doomdark](https://forum.paradoxplaza.com/forum/members/doomdark.153/)**
Role: Chief Creative Officer
Badges: 61
Reaction score: 11,384

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
