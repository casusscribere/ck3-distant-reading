---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1489882/"
forum_thread_id: 1489882
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 72
title: "Crusader Kings 3 Dev Diary #72 - Holding Court at Court in The Royal Court (in a courtly fashion)"
dd_date: 2021-09-07
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
body_word_count: 625
inline_image_count: 11
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1489882'
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
    location: raw_lines_~28_to_140
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_139
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1698.jpg?1631018079
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_216_to_220
    action: preserved_and_flagged
    counts:
      Like: 138
      Love: 89
      (unlabeled — rendered as base64 data URI): 4
      Haha: 4
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_228_to_336
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_337_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1698.jpg?1631018079)
<!-- artifact:thread_banner:end -->

# Crusader Kings 3 Dev Diary #72 - Holding Court at Court in The Royal Court (in a courtly fashion)

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Sep 7, 2021](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-72-holding-court-at-court-in-the-royal-court-in-a-courtly-fashion.1489882/)
<!-- artifact:thread_metadata:end -->

Welcome comrades! In today’s dev diary, we’ll be taking a gander at a neat part of the upcoming expansion: Holding Court. Per the usual, I’ll preface this by saying that the court scene is a work in progress, the UI of the court scene is a work in progress, and the art generally is work in progress; we also have some missing animations and camera perspectives, so take all the images here with a grain of salt.  

![001.png](https://forumcontent.paradoxplaza.com/public/741573/001.png "001.png")



As with any medieval ruler, monarchs in The Royal Court are vain creatures. It’s not enough to control the largest or best-developed realm, you have to have the largest palace, the fanciest food, the most renowned courtiers, and so on: after all, what’s the point of taxing the masses if you have to live like a peasant anyway?  

Sometimes, though, you can’t quite afford the fanciest feast, the latest fashion, or even just the shiniest artefact to spruce up your court.  

When times are that hard, and you really need just _immediate_ distraction from the flaws in your life, it’s important to spend some time indulging those with lives even harder than yours. Like nearly everyone else. For times when you feel like slumming it amongst the weird and wonderful characters of your realm, you can Hold Court.  

![002.png](https://forumcontent.paradoxplaza.com/public/741574/002.png "002.png")



This repeatable decision lets you hear a number of requests from various characters, listening to petitioners seeking your aid and legal ruling on many subjects. They might be guests, courtiers, neighbouring rulers, vassals, spies, the odd bumbling peasant…  

![003.png](https://forumcontent.paradoxplaza.com/public/741575/003.png "003.png")



At present, you’ll receive three such petitioners each time, with all events delivered in the new courtly event style (though follow-up may be character events or similar).  

![004.png](https://forumcontent.paradoxplaza.com/public/741576/004.png "004.png")



Some choices are easy…  

![005.png](https://forumcontent.paradoxplaza.com/public/741577/005.png "005.png")



… some choices are hard…  

![006.png](https://forumcontent.paradoxplaza.com/public/741578/006.png "006.png")



… and some are just weird.  

![007.png](https://forumcontent.paradoxplaza.com/public/741579/007.png "007.png")



After you’ve made your ruling in each case, in addition to the effects of each turn, you’ll gain some court grandeur to bolster your overall supply. We’ve got just shy of a hundred or so of these events alone, so there should be a goodly amount of variety for most playstyles.  

This system is something pretty dear to our hearts, as it models a task that would’ve been a pretty big part of the day-to-day for many rulers, and we’ve put a lot of effort into getting plenty of alternate events to keep it as varied as possible for as long as possible. We hope you find it a fun & proactive way to explore some of the smaller (and uhh, not so small) issues developing in your realm.  

Small dev diary, but that’s all from me for the mo. As ever, I’ll be around in the comments for an hour or so to answer questions, but otherwise, see y’all next diary!  

… Y’know what, let’s have a few more events to show off before we finish for the day.  

![008.png](https://forumcontent.paradoxplaza.com/public/741580/008.png "008.png")



![009.png](https://forumcontent.paradoxplaza.com/public/741581/009.png "009.png")



![010.png](https://forumcontent.paradoxplaza.com/public/741582/010.png "010.png")



![011.png](https://forumcontent.paradoxplaza.com/public/741583/011.png "011.png")

<!-- artifact:reactions:start -->
- 138 Like
- 89 Love
- 13 (unlabeled — rendered as base64 data URI)
- 4 Haha
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)**
Role: Former CK3 Experienced Game Designer
Badges: 83
Messages: 528
Reaction score: 15,169

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
