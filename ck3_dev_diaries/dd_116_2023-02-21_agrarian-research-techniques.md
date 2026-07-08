---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1569914/"
forum_thread_id: 1569914
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 116
title: "Dev Diary #116 - Agrarian Research Techniques"
dd_date: 2023-02-21
author_handle: Wokeg
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 301
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1569914'
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
    location: raw_lines_~28_to_146
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_145
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2205.jpg?1676902996
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_209_to_213
    action: preserved_and_flagged
    counts:
      Like: 101
      Haha: 45
      (unlabeled — rendered as base64 data URI): 3
      Love: 5
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_221_to_329
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_330_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2205.jpg?1676902996)
<!-- artifact:thread_banner:end -->

# Dev Diary #116 - Agrarian Research Techniques

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Feb 21, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-116-agrarian-research-techniques.1569914/)
<!-- artifact:thread_metadata:end -->

![116_EyesLeft.png](https://forumcontent.paradoxplaza.com/public/936493/116_EyesLeft.png "116_EyesLeft.png")


![116_EyesRight.png](https://forumcontent.paradoxplaza.com/public/936494/116_EyesRight.png "116_EyesRight.png")


... Anyone watching? No? Good.  

Ok, just you and me. Great, because I've only got a few wee lil morsels today and I don't want to share them with *too* many people. So let's all just keep this quiet and, if anyone asks, the dev diary was about how we research thirteenth century agrarian techniques in rural France. Got it? Good.  

I want you to tell me what this historical character...  


![116_Char1.PNG](https://forumcontent.paradoxplaza.com/public/936495/116_Char1.PNG "116_Char1.PNG")


... *this* historical character...  


![116_Char2.PNG](https://forumcontent.paradoxplaza.com/public/936496/116_Char2.PNG "116_Char2.PNG")


... and *this* historical character all have in common.  


![116_Char3.PNG](https://forumcontent.paradoxplaza.com/public/936497/116_Char3.PNG "116_Char3.PNG")


Figured it out? Yes? No? Waiting for someone else to scan through every character in the game before you hazard a guess? Ok, well, to be a bit fairer, it's got something to do with this:  


![116_ListCensoredv2.png](https://forumcontent.paradoxplaza.com/public/936498/116_ListCensoredv2.png "116_ListCensoredv2.png")


Spoiler: Hint #1

The list includes all the interactions in a particular category. You would not see all of them at the same time like this.

Spoiler: Hint #2

![:D](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Big Grin    :D") This has nothing to do with Wards & Wardens.


Finally, none of them are directly connected to this chap:  


![116_Char4v2.PNG](https://forumcontent.paradoxplaza.com/public/936499/116_Char4v2.PNG "116_Char4v2.PNG")



Alright, that's all I've got for you today, but I expect to be going over that list again soon. And in *detail*. If anyone asks, remember: rural France, agriculture, thirteenth century, yada yada.  

Till next time!

 

- 159

<!-- artifact:reactions:start -->
- 101 Like
- 45 Haha
- 13 (unlabeled — rendered as base64 data URI)
- 5 Love
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)**
Role: Former CK3 Experienced Game Designer
Badges: 83
Messages: 528
Reaction score: 15,169

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
