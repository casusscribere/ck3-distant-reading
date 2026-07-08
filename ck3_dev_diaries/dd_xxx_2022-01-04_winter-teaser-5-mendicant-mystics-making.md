---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1505616/"
forum_thread_id: 1505616
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "Winter Teaser #5 - Mendicant Mystics Making a Mess"
dd_date: 2022-01-04
author_handle: Wokeg
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 735
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1505616'
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
    location: raw_lines_~28_to_118
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_120_to_121
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_193_to_198
    action: preserved_and_flagged
    counts:
      Like: 81
      Love: 25
      Haha: 20
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_206_to_308
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_309_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Winter Teaser #5 - Mendicant Mystics Making a Mess

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Jan 4, 2022](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-5-mendicant-mystics-making-a-mess.1505616/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-5-mendicant-mystics-making-a-mess.1505616/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-5-mendicant-mystics-making-a-mess.1505616/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-5-mendicant-mystics-making-a-mess.1505616/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-4-artifact-weapons.1504071/ "Winter Teaser #4 - Artifact Weapons") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-85-an-artifacts-life.1506337/ "CK3 Dev Diary #85 - An Artifact's Life")

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1825.jpg?1641294906)

# Winter Teaser #5 - Mendicant Mystics Making a Mess

- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Jan 4, 2022](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-5-mendicant-mystics-making-a-mess.1505616/)

Welcome comrades! We’ve not got anything major on the docket for the day’s dev diary, so we’ll be taking a little peak at a cultural tradition that’s dear to my heart instead. Just to whet the appetite for more content a little.  

![001.PNG](https://forumcontent.paradoxplaza.com/public/778830/001.PNG "001.PNG")



Mendicant Mystics is a moderately uncommon tradition, one that synergises well with faiths that already boost the mystic lifestyle. Moreover, though, there’s something that just _speaks_ to me, personally, about the idea of impassioned people wandering the world, sharing their wisdom and message.  

Consequently, I’ve spruced it up a little bit, adding some flavour to the idea of living in a culture where wandering know-it-all is a valid career choice. To reflect this, the following events will all _try_ to grab characters from the pool first, so wandering characters of such a culture are often at risk of deciding to become a mystic once they hit the road, and if a mystic breaks in to annoy you once, there’s every chance the same mystic might come knocking a second time down the line...  

![002.PNG](https://forumcontent.paradoxplaza.com/public/778831/002.PNG "002.PNG")



After all, who better than a stranger covered in twigs and mud to teach your children some valuable life lessons?  

![003.PNG](https://forumcontent.paradoxplaza.com/public/778832/003.PNG "003.PNG")



Or, indeed, yourself.  

![004.PNG](https://forumcontent.paradoxplaza.com/public/778833/004.PNG "004.PNG")



Really, they’re altruists...  

![005.PNG](https://forumcontent.paradoxplaza.com/public/778834/005.PNG "005.PNG")



… of course, for some folks, the wandering may get too much eventually.  

![006.PNG](https://forumcontent.paradoxplaza.com/public/778835/006.PNG "006.PNG")



Hmmm, can’t really put my finger on why I like the idea of mendicant mystics so much. Something about them just seems delightfully familiar to me, I guess. Ah well.  

Thanks for reading folks, and we’ll see you next dev diary!

<!-- artifact:reactions:start -->
- 81 Like
- 25 Love
- 20 Haha
- 4 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)**
Role: Former CK3 Experienced Game Designer
Badges: 76
Messages: 528
Reaction score: 15,169

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
