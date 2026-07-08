---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1495808/"
forum_thread_id: 1495808
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: Timing in Regards to Royal Court
dd_date: 2021-10-26
author_handle: PDX_Pariah
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 989
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1495808'
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
    location: raw_lines_~28_to_128
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_130_to_131
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_218_to_223
    action: preserved_and_flagged
    counts:
      Like: 210
      (unlabeled — rendered as base64 data URI): 35
      Love: 12
      Haha: 10
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_300_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Timing in Regards to Royal Court

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Oct 26, 2021](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/)
- [2](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/page-3)
- …
  
  #### Go to page
  
  Go

- [12](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/page-12)
[Next](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/page-2)

1 of 12

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/page-12 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/?prdxDevPosts=1)

[![PDX_Pariah](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/s/paradox5.png)](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

#### [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

##### Community Manager

Jul 21, 2020

119

4.454

[](javascript:;)

- [Oct 26, 2021](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/post-27863973)


- [/forum/threads/timing-in-regards-to-royal-court.1495808/post-27863973](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/post-27863973)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27863973/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/timing-in-regards-to-royal-court.1495808/post-27863973)

Howdy all,  

Friendly neighborhood Community Manager Troy here to bring you the brightest and freshest news regarding Royal Court!  

This year has been a long and interesting one, to be certain, but we are here all together to make sure that our fantastic community gets the product that we have all been waiting for and deserve. Earlier this year, we informed you all that we were working hard to make sure that Royal Court was up to our standards.  

Royal Court is not only the first expansion for CK3, but also a set of features entirely new to the CK series, including cultural evolution and language. It is very much breaking new ground,and as such, we are experimenting at every turn.  

With that in mind we are not, at the moment, entirely satisfied with Royal Court's progress, especially regarding its stability. There are a number of bugs we really need to iron out, and are taking more time to make sure it is in line with the standards you expect. We also understand the frustration that delays cause, but we would like to make sure we are always as forthcoming as possible and that you hear the news directly from us. It’s a tricky balance between sentiments like “It will release whenever we finish making sure it is ready” and things like giving exact timelines only to make necessary but upsetting changes to that timeline when we do actually need time to review and make those changes.  

**That being said, look forward to news about the 2022 release date Soon™!**  

In the meantime, you can catch up on all the previous points in our [Royal Court FAQ HERE](https://forum.paradoxplaza.com/forum/threads/ck3-royal-court-faq-developer-diaries-q-a-important-information.1475394/)!  

All of our team is hard at work following their projects through to completion and making sure that all the tasks that they started are fully realized and supported. This means they are going to keep up their hard work and make sure that Royal Court is the success that both their efforts and your expectations deserve.  

All that said, we are super grateful for all the dedication and passion you have shown for Crusader Kings III leading up to this point. Your thoughts and feedback on the systems, features, and integration of Royal Court have led to some interesting changes and alterations that we may or may not have otherwise considered! Without your input and support, this game and expansion would not be anywhere near what it is shaping up to be!  

Thank you from the bottom of our hearts! We appreciate your understanding and patience.  

Cheers,  
- Pariah

<!-- artifact:reactions:start -->
- 210 Like
- 89 (unlabeled — rendered as base64 data URI)
- 43 (unlabeled — rendered as base64 data URI)
- 35 (unlabeled — rendered as base64 data URI)
- 12 Love
- 10 Haha
<!-- artifact:reactions:end -->
