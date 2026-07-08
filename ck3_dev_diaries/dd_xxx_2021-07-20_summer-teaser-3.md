---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1483461/"
forum_thread_id: 1483461
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "CK3 Summer Teaser #3"
dd_date: 2021-07-20
author_handle: Servancour
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 786
inline_image_count: 3
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1483461'
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
    location: raw_lines_~28_to_120
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_122_to_124
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_221_to_224
    action: preserved_and_flagged
    counts:
      Like: 160
      Love: 36
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_253_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Summer Teaser #3

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Jul 20, 2021](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/)
- [2](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/page-3)
- …
  
  #### Go to page
  
  Go

- [6](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/page-6)
[Next](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/page-2)

1 of 6

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/page-6 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/?prdxDevPosts=1)

[![Servancour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/obsolete/s/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/servancour.465268/)

#### [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)

##### Game Designer

**Paradox Staff**

**4 Badges**

Mar 15, 2012

1.606

9.949

- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![500k Club](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/500k_red.png "500k Club")
- ![Paradox Order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/pdx_order.png "Paradox Order")
- ![Stellaris Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Stellaris_SignUp_icon.png "Stellaris Sign-up")

[](javascript:;)

- [Jul 20, 2021](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/post-27688717)


- [/forum/threads/ck3-summer-teaser-3.1483461/post-27688717](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/post-27688717)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27688717/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/post-27688717)

Hello everyone!  

Welcome to the third summer teaser. This time around, I figured I would show you something quite different. As you may know already, minor titles will be returning alongside the upcoming expansion, Royal Court, allowing you to appoint a Court Jester, a Seneschal, and more! As you might expect, we’ll be adding a number of new events that make use of these appointed characters, but we are no strangers to also updating existing content if need be! We generally want features to be visible wherever it makes sense, and updating content can be a part of making old events have new and interesting options or additional variety and flavour.  

Here are a few examples of events that we’ve updated (or added, as in the last example):  

![teaser3_01_rebuild_walls.jpg](https://forumcontent.paradoxplaza.com/public/729210/teaser3_01_rebuild_walls.jpg "teaser3_01_rebuild_walls.jpg")


*[Image of the updated Martial Lifestyle event The Walls of a County]*  

![teaser3_02_lure_of_language.jpg](https://forumcontent.paradoxplaza.com/public/729211/teaser3_02_lure_of_language.jpg "teaser3_02_lure_of_language.jpg")


*[Image of the updated Diplomacy Lifestyle event The Lure of Language]*  

![teaser3_03_murder_outcome.jpg](https://forumcontent.paradoxplaza.com/public/729212/teaser3_03_murder_outcome.jpg "teaser3_03_murder_outcome.jpg")


*[Image of a potential murder outcome]*​


You can expect more details in a future Dev Diary!

<!-- artifact:reactions:start -->
- 160 Like
- 36 Love
- 11 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
