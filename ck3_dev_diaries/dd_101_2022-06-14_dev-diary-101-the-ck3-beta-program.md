---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1531127/"
forum_thread_id: 1531127
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 101
title: "CK3 Dev Diary #101: The CK3 Beta Program"
dd_date: 2022-06-14
author_handle: PDX_Pariah
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 475
inline_image_count: 2
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1531127'
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
    location: raw_lines_~28_to_149
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_148
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1982.jpg?1655307169
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_151_to_153
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_184_to_187
    action: preserved_and_flagged
    counts:
      Like: 40
      (unlabeled — rendered as base64 data URI): 2
      Love: 7
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_195_to_295
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

<!-- artifact:thread_banner:start -->
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1982.jpg?1655307169)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #101: The CK3 Beta Program

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Jun 14, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-101-the-ck3-beta-program.1531127/)
<!-- artifact:thread_metadata:end -->

Howdy all,  

The number #101 really set the expectations to be both the start of something new, as well as a continuation of a long standing tradition, right? So that is exactly what this entry will be about - the renewal of the Crusader Kings III Beta program.  

Our Beta program has been around since before the launch of the game. We have had people joining us in different periods over the years, and there are still people with us that have been around from the very start! Their feedback is not only super insightful and valuable, but has also helped shape the landscape of the game. These things can sometimes seem trivial, but can also sometimes be the difference between a successful piece of content and something that might otherwise have been well received in a different block of content. Their efforts truly are the backbone of the testing process as well as the voice of the people!  

As part of the continuous development of the program, we have now decided it’s time again to open up for new applicants!  

**What does it mean to be a Beta tester?**  

As a Beta tester you get access to content currently in development. The role is to play early versions, give feedback on experience playing with the new features and if you encounter any issues whilst playing. Since Crusader Kings is a Paradox game at its core, we have another layer in our beta program that is the Historical aspects of the game. Since we try to a large extent to be historically accurate, there is usually a lot of discussions and feedback on those areas of the game as well.  

From the Devs side, we are a group of people that interact with the program continuously. Reading through feedback and thoughts, similarly how we monitor the forum and social channels, but with content not yet available to the public. We value the interaction and feedback from you guys a lot, and the Beta program is an important part of the Player / Developer interaction.  

So, if you enjoy playing CK3 as much as we do, and perhaps have a niche knowledge that would benefit the group, such as a burning interest in the Kingdom of Ireland in 1101 or an extended knowledge of Medieval fashion choices in Iberia? Either way, if you think it sounds exciting to help us in the development process of upcoming content and love the Medieval period, we encourage you to send in your application to the program.  

Please fill out the form [**HERE**](https://www.surveymonkey.com/r/CD5YSB8), and we will get back to you shortly!  

Until then..  

Tess & Troy  


![Tess-name.png](https://forumcontent.paradoxplaza.com/public/837197/Tess-name.png "Tess-name.png")

![Troy-name.png](https://forumcontent.paradoxplaza.com/public/837198/Troy-name.png "Troy-name.png")

<!-- artifact:reactions:start -->
- 40 Like
- 9 (unlabeled — rendered as base64 data URI)
- 7 Love
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)**
Role: Community Manager
Badges: 95
Messages: 119
Reaction score: 4,454

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
