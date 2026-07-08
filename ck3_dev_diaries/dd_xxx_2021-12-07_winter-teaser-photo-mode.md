---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1502286/"
forum_thread_id: 1502286
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: CK3 Winter Teaser - Photo mode
dd_date: 2021-12-07
author_handle: Carlberg
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 406
inline_image_count: 6
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1502286'
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
    location: raw_lines_~28_to_143
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_142
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1809.jpg?1638886590
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_145_to_147
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_198_to_203
    action: preserved_and_flagged
    counts:
      Like: 86
      Love: 29
      (unlabeled — rendered as base64 data URI): 2
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_211_to_315
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_316_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1809.jpg?1638886590)
<!-- artifact:thread_banner:end -->

# CK3 Winter Teaser - Photo mode

<!-- artifact:thread_metadata:start -->
- Thread starter [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)
- Start date [Dec 7, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-winter-teaser-photo-mode.1502286/)
<!-- artifact:thread_metadata:end -->

### CK3 Winter Teaser #1 - Photo mode​

Salutations, I am Carlberg, the 3D environment art lead on CK3 and today we have a small teaser for that button you may have spotted down in the right corner on a lot of dev diaries. It is the button that will bring up the Photomode of the court, to make it easier to take memorable pictures of the events and happenings of your court! Along with this preview we also thought we’d show off some more artifacts in their natural habitat.​


![photomode_icon.png](https://forumcontent.paradoxplaza.com/public/771152/photomode_icon.png "photomode_icon.png")


*The camera might not have been invented in the dark ages, but don’t we all want clean screenshots?.*​


We’ve been confident for quite some time that our players would want to take some pictures of what happens in their court, the interesting courtiers interacting or from finally seeing your rival and vassal arrive to bend the knee. So for that purpose the Photo mode will give everyone the ability to pick what camera is currently active out of a curated selection. Some of these are camera angles that you’ve seen depending on different interfaces and some camera angles only available in the photo mode.  
​

![photomode_Screen.png](https://forumcontent.paradoxplaza.com/public/771154/photomode_Screen.png "photomode_Screen.png")


![photomode_Screen_Drop_Down.png](https://forumcontent.paradoxplaza.com/public/771155/photomode_Screen_Drop_Down.png "photomode_Screen_Drop_Down.png")


*In the photo mode you can select cameras from a dropdown, turn off courtiers for decoration focused shots, or the UI to get a clean picture with no interface.*​


And following, here are a few more court shots taken with the photo mode.​

![photomode_India.png](https://forumcontent.paradoxplaza.com/public/771157/photomode_India.png "photomode_India.png")


![photomode_Mena.png](https://forumcontent.paradoxplaza.com/public/771158/photomode_Mena.png "photomode_Mena.png")

***Edit:*** *We have been made aware of the flipped text of the banner, thanks for your keen eyes!*​


![photomode_medi.png](https://forumcontent.paradoxplaza.com/public/771159/photomode_medi.png "photomode_medi.png")


​
> *Trivia:
> Did you know that the natural camera, camera obscura, is an optical effect that can occur in a dark room with a small hole for the entry of light. This light causes a projection of the outside to occur within the dark room and has been observed and mentioned in Chinese written texts as early as 400 bce.*
>
> Click to expand...


We'll be back again next week with another teaser!

 

Last edited: Dec 7, 2021

<!-- artifact:reactions:start -->
- 86 Like
- 29 Love
- 20 (unlabeled — rendered as base64 data URI)
- 9 (unlabeled — rendered as base64 data URI)
- 2 Haha
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)**
Role: Senior Environment Artist
Badges: 40
Messages: 221
Reaction score: 2,288

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
