---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1542092/"
forum_thread_id: 1542092
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: CK3 - DD Delay - September 13, 2022
dd_date: 2022-09-13
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
body_word_count: 508
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1542092'
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
    location: raw_lines_176_to_178
    action: preserved_and_flagged
    counts:
      Like: 32
      (unlabeled — rendered as base64 data URI): 12
    note: Reactions block parsed; 1 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_206_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 - DD Delay - September 13, 2022

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Sep 13, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-dd-delay-september-13-2022.1542092/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-dd-delay-september-13-2022.1542092/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-dd-delay-september-13-2022.1542092/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-dd-delay-september-13-2022.1542092/add-reply)

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

- [Sep 13, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-dd-delay-september-13-2022.1542092/post-28472235)


- [/forum/threads/ck3-dd-delay-september-13-2022.1542092/post-28472235](https://forum.paradoxplaza.com/forum/threads/ck3-dd-delay-september-13-2022.1542092/post-28472235)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28472235/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-dd-delay-september-13-2022.1542092/post-28472235)

Howdy all!  

Today there is no Dev Diary while we prioritize the issues you have been so kind as to report after the launch of Bastion (i.e. 1.7) and Friends & Foes. There are a ton of helpful points of feedback, questionable issues, and things we can work on to make the general quality of life better.  

With that being said, we are working on that list of reports and should have some actions to finish moving forward. In the meantime, look forward to the next Update from us as it should have more information on the work we have been doing!  

Until then, Cheers,  

- SP

<!-- artifact:reactions:start -->
- 32 Like
- 26 (unlabeled — rendered as base64 data URI)
- 12 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
