---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1484098/"
forum_thread_id: 1484098
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "CK3 Summer Teaser #4"
dd_date: 2021-07-27
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
body_word_count: 684
inline_image_count: 5
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1484098'
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
    location: raw_lines_~28_to_135
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_137_to_139
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_236_to_240
    action: preserved_and_flagged
    counts:
      Like: 130
      Love: 10
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_317_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Summer Teaser #4

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Jul 27, 2021](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/)
- [2](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/page-3)
- [4](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/page-4)
[Next](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/page-2)

1 of 4

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/page-4 "Last")

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

- [Jul 27, 2021](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/post-27700194)


- [/forum/threads/ck3-summer-teaser-4.1484098/post-27700194](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/post-27700194)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27700194/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-4.1484098/post-27700194)

Greetings!  

I’ve got another set of traditions for you today. Do berar in mind that these are a work in progress and may be subject to change.  

![trad_charitable.png](https://forumcontent.paradoxplaza.com/public/731168/trad_charitable.png "trad_charitable.png")


*[Image of the Charitable cultural tradition]*  

![trad_parochialism.png](https://forumcontent.paradoxplaza.com/public/731169/trad_parochialism.png "trad_parochialism.png")


*[Image of the Parochialism tradition]*  

![trad_ting_meets.png](https://forumcontent.paradoxplaza.com/public/731170/trad_ting_meets.png "trad_ting_meets.png")


*[Image of the Ting-Meet tradition]*  

![trad_tribal_unity.png](https://forumcontent.paradoxplaza.com/public/731171/trad_tribal_unity.png "trad_tribal_unity.png")


*[Image of the Tribal Unity tradition]*  

![trad_warriors_of_the_dry.png](https://forumcontent.paradoxplaza.com/public/731172/trad_warriors_of_the_dry.png "trad_warriors_of_the_dry.png")


*[Image of the Warriors of the Dry tradition]*​


That’s it for today!

<!-- artifact:reactions:start -->
- 130 Like
- 10 Love
- 10 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
