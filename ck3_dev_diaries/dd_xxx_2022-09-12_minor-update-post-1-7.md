---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1541873/"
forum_thread_id: 1541873
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: CK3 Minor Update - Post 1.7
dd_date: 2022-09-12
author_handle: PDX_Pariah
expansion: Friends and Foes
patch: Patch 1.7 (Bastion)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 600
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1541873'
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
    location: raw_lines_~28_to_125
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_127_to_129
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_187_to_189
    action: preserved_and_flagged
    counts:
      Like: 30
      (unlabeled — rendered as base64 data URI): 6
      Love: 3
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_266_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Minor Update - Post 1.7

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Sep 12, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-minor-update-post-1-7.1541873/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-minor-update-post-1-7.1541873/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-minor-update-post-1-7.1541873/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-minor-update-post-1-7.1541873/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[![PDX_Pariah](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/s/paradox5.png)](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

#### [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

##### Community Manager

Jul 21, 2020

119

4.454

[](javascript:;)

- [Sep 12, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-minor-update-post-1-7.1541873/post-28469893)


- [/forum/threads/ck3-minor-update-post-1-7.1541873/post-28469893](https://forum.paradoxplaza.com/forum/threads/ck3-minor-update-post-1-7.1541873/post-28469893)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28469893/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-minor-update-post-1-7.1541873/post-28469893)

Howdy all,  

This Update is, technically speaking, very minor and should not affect save games in any way. There are also no other changes made as you can tell from this super beefy changelog:  

Spoiler: Changelog

Fixed the following issue:  

- CK3 - Stability - Game doesn't launch when starting the game on an older CPU (non-AVX)



We have received numerous reports after the release of the 1.7 “Bastion” Update regarding an issue affecting certain older CPUs without support for AVX functionality. Since we wanted to make sure this got the proper attention it required and was not rushed, we took the weekend to test and make sure our Update was fully ready to release.  

While the number of players affected by this issue was relatively low, it was still a very high priority issue and something that we wanted to address to make sure we had a solid process for before releasing it. As of now, this Update is live and should resolve these issues. If you are still facing issues or need any assistance, keep reporting issues [**HERE**](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1077/) and we will be glad to assist.

<!-- artifact:reactions:start -->
- 30 Like
- 6 (unlabeled — rendered as base64 data URI)
- 3 Love
<!-- artifact:reactions:end -->
