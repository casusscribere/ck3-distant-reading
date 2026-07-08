---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1416565/"
forum_thread_id: 1416565
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: Patch 1.0.3. Out now! Checksum [935c]
dd_date: 2020-09-03
author_handle: PDX_Pariah
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 764
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1416565'
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
    location: raw_lines_~28_to_122
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_124_to_125
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_209_to_213
    action: preserved_and_flagged
    counts:
      Like: 116
      Love: 27
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_290_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Patch 1.0.3. Out now! Checksum [935c]

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Sep 3, 2020](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

Status
Not open for further replies.

- [1](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/)
- [2](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/page-3)
- …
  
  #### Go to page
  
  Go

- [9](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/page-9)
[Next](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/page-2)

1 of 9

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/page-9 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/?prdxDevPosts=1)

[![PDX_Pariah](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/s/paradox5.png)](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

#### [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

##### Community Manager

Jul 21, 2020

119

4.454

[](javascript:;)

- [Sep 3, 2020](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/post-26860826)


- [/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/post-26860826](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/post-26860826)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/26860826/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/patch-1-0-3-out-now-checksum-935c.1416565/post-26860826)

Hi everyone!  

We have just deployed a new (small) patch, version 1.0.3. It fixes various issues related to succession. On behalf of the Crusader Kings III team, we are sincerely grateful and humbled by all your feedback! We are working hard to investigate and address the issues that have been reported!  

Independent from this patch, we have pushed a potential fix for Steam users that couldn’t fire up the game. This means that next time you will start the game via Steam, you will get an installation step (like on a first-time installation), don’t worry, this is perfectly normal!  

If you want to know more about how to post a bug report, [check this thread!](https://forum.paradoxplaza.com/forum/threads/how-to-report-a-bug-read-me.1413860/)  

See you soon!  

Spoiler: Changelog

Rewrote the order of succession system.  
This fixes a variety of issue related to succession. Some examples include half-siblings from the wrong parent inheriting, distant relatives not inheriting, and some issues with who would inherit land in partition.

 

Last edited by a moderator: Sep 3, 2020

<!-- artifact:reactions:start -->
- 116 Like
- 27 Love
- 8 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
