---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1513522/"
forum_thread_id: 1513522
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 1
title: "CK Console DD #1: Vision and Goals!"
dd_date: 2022-03-01
author_handle: PDX_Pariah
expansion: Console Edition
patch: Crusader Kings III Console Edition
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 752
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1513522'
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
    location: raw_lines_~28_to_126
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_128_to_129
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_181_to_183
    action: preserved_and_flagged
    counts:
      Like: 27
      Haha: 9
      (unlabeled — rendered as base64 data URI): 5
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_191_to_293
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_294_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK Console DD #1: Vision and Goals!

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Mar 1, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-1-vision-and-goals.1513522/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-1-vision-and-goals.1513522/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-1-vision-and-goals.1513522/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-1-vision-and-goals.1513522/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-88-achievements.1508593/ "CK3 Dev Diary #88: Achievements") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-90-the-1-5-1-update.1514785/ "CK3 Dev Diary #90: The 1.5.1 Update")

# CK Console DD #1: Vision and Goals!

- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Mar 1, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-1-vision-and-goals.1513522/)

Howdy all!  

Community Manager Sonic Pariah here to inform you of some really cool news from the Crusader Kings team.  

While the entire Stockholm team is hard at work with Royal Court and making sure all the feedback, suggestions, and details are ironed out (specifically Patch 1.5.1 coming Soon™), we have had another team over at Lab42 doing what they do best:  
**BRINGING CRUSADER KINGS TO XBOX X AND S AS WELL AS PLAYSTATION 5!**  

Working with Paradox and Lab42 on the joint vision for an adaptation, and not just a port, of Crusader Kings III to consoles has been challenging and rewarding for everyone involved. The base vision was to bring the highly regarded Crusader Kings franchise to a new console audience, bringing enjoyment to as many people as possible.  

The Lab42 team has taken a flexible approach to development – responding to Paradox expertise and user testing & feedback, which has helped shape the development priorities throughout the adaptation. This approach will continue post launch, where Lab42 will continue to be flexible to allow consumer feedback to shape the flow of updates, patches and new features.  

While it wasn’t an easy task to bring everything to life on consoles, it was definitely fulfilling and highly satisfying to see once the first versions came to life. While work and progress is still being made on the console version, it is a process and still being worked on diligently by the Lab42 team. Certain features were easily adapted for the console setup while others needed to be completely reimagined from the ground up. As you can imagine, this requires quite a resourceful and dedicated team, and we are confident that the Lab42 Team have it well in hand!  

While the teams are hard at work on their respective projects, we will be more than happy to keep you up to date on news and any possible dates as they become available. In the meantime, please enjoy Royal Court and will have more info for you in the weeks to come!  

Cheers,  

-SP  

[https://www.youtube.com/embed/emobBLz5x2g?wmode=opaque](https://www.youtube.com/embed/emobBLz5x2g?wmode=opaque)

 

Last edited by a moderator: Mar 1, 2022

- 92

<!-- artifact:reactions:start -->
- 27 Like
- 9 Haha
- 5 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)**
Role: Community Manager
Badges: 68
Messages: 119
Reaction score: 4,454

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
