---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1470041/"
forum_thread_id: 1470041
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 57
title: "CK3 Dev Diary #57 - An Eventful Summer"
dd_date: 2021-04-27
author_handle: Heptopus
expansion: Northern Lords
patch: Patch 1.4 (Azure)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 752
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1470041'
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
    location: raw_lines_~28_to_154
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_153
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1612.jpg?1619526702
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_156_to_158
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_224_to_229
    action: preserved_and_flagged
    counts:
      Like: 165
      Love: 34
      (unlabeled — rendered as base64 data URI): 1
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_237_to_342
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_343_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1612.jpg?1619526702)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #57 - An Eventful Summer

<!-- artifact:thread_metadata:start -->
- Thread starter [Heptopus](https://forum.paradoxplaza.com/forum/members/heptopus.1269016/)
- Start date [Apr 27, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-57-an-eventful-summer.1470041/)
<!-- artifact:thread_metadata:end -->

### CK3 Dev Diary #57 - An Eventful Summer​


Hello everyone!  

I hope you’re enjoying the warmer days, and that you are looking forward to hearing a bit more about the free patch, Azure, that we’re releasing this summer.  

Before we get into the meat of today's Dev Diary I want to clarify something regarding the Azure patch; it's being made by a smaller group of CK3 devs in a Strike Team setup, which means that not everyone on the CK3 Dev team is working on the patch. We hope that we'll still be able to address quite a few of your concerns, but we won't have time to address everything. Still, keep sending us feedback, as it helps us prioritize!  

This dev diary will focus on one area of the patch and as a Content Designer I am – unsurprisingly – here to talk about events and such. More specifically I am here to talk about some new content that we’re including in Azure, and joining me in this dev diary is one of our new Content Designers: Isabella! As developers we all have areas of the game that we would like to expand upon and flesh out a bit, and two areas are now getting some love: **childhood** and **lifestyle events**.  


### Childhood​

Children always want to grow up fast, and no child feels this more actually than the one that just inherited the entire realm at the mature age of six. Oh woe, what can a young king do to pass the long days ahead until he can scheme and murder to his heart’s content? Play with other young rulers, of course! Azure includes a new activity for children called Meet Peers that will make childhood more interesting and full of experiences.  

![gathering.png](https://forumcontent.paradoxplaza.com/public/697058/gathering.png "gathering.png")


*[Image of the start event for the Meet Peers activity]*  

Meet Peers is an activity available for children where they can gather all young rulers and courtiers in the realm to just play and forget about the dreariness of life as a child in medieval times. All participants will lose stress and increase their opinion of the host, and the children attending the playdate can find themselves in fun and educational situations!  

![brave.png](https://forumcontent.paradoxplaza.com/public/697059/brave.png "brave.png")


*[Image of an event that can appear when you Meet Peers]*  

Of course, there may also be any number of less… wholesome consequences from bringing that many children together.  

![playing_rough.png](https://forumcontent.paradoxplaza.com/public/697060/playing_rough.png "playing_rough.png")


*[Image of an event that can appear when you Meet Peers]*  

And if socializing just isn’t your thing and friends are easiest made (and killed) through schemes we’ve also reduced the age restrictions for Sway and Murder slightly. All to enable you to live out your scheming rule from as young an age as possible!  


### Lifestyle events​

Or, if your children just can’t wait to grow up, you could let them try their fate fighting against grown soldiers in a tournament. In this patch, we have a couple of new lifestyle events coming your way, including the Tantrum Tourney event chain for Martial Authority characters.  


![tantrumtourneyhighres.PNG](https://forumcontent.paradoxplaza.com/public/697074/tantrumtourneyhighres.PNG "tantrumtourneyhighres.PNG")


*[Image of the starting event from the Tantrum Tourney event chain]*  

‘Hym repented that he came there!’ - 14th Century Romance Richard Coer de Lyon on grown dukes and lords regretting each moment as they get impaled by a lance manned by an adolescent child.  

A trope of romances detailing the life of Richard the Lionheart likes to exaggerate the dates of his reign to present him as a King who was a child monarch. This seems to be done almost exclusively so he can be presented as perhaps the greatest demon of a child who ever lived. Child Richard is shown ordering all of his noblemen to fight him in a tournament - on pain of death, and beating everyone who turns up to a pulp.  

Will you allow your baby’s first bloodlust to be unleashed upon your knights, who certainly did not sign up for this?  

Keep your eyes peeled while your character is studying their Lifestyle! You might see a few new moments cropping up. Especially if you have war elephants… but what are you doing if you don’t already have war elephants?  


---


That’s it for this week, thank you all for reading!

<!-- artifact:reactions:start -->
- 165 Like
- 34 Love
- 26 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 1 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Heptopus](https://forum.paradoxplaza.com/forum/members/heptopus.1269016/)**
Role: Content Designer
Badges: 2
Messages: 47
Reaction score: 917

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
