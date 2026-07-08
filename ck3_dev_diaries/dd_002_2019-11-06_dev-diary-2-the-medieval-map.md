---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1274052/"
forum_thread_id: 1274052
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 2
title: "CK3 Dev Diary #2- The Medieval Map"
dd_date: 2019-11-06
author_handle: Servancour
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 919
inline_image_count: 5
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1274052'
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
    location: raw_lines_~28_to_148
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_150_to_152
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_198_to_200
    action: preserved_and_flagged
    counts:
      Like: 7
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 1 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_208_to_305
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_306_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #2- The Medieval Map

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Nov 6, 2019](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-2-the-medieval-map.1274052/)
<!-- artifact:thread_metadata:end -->

Hello everyone!  

I would like to take a moment to talk about the map of Crusader Kings 3, what the vision for the map is, and how it is different from Crusader Kings 2.  

Let’s start with our ambitions. CK2 had several parts of the map that was outdated, and to be frank, a bit underdeveloped. When we started to update the map for CK3, we knew that we wanted to take a pass at everything, do additional research, and update the different areas accordingly. This goes for the entire De Jure title hierarchy, so there are several new kingdoms and duchies present. In terms of scope, the map will roughly match that of CK2. I know I will disappoint those of you hoping for China, but, sadly, it will not be on the map. We will however, have a few new additions: the entirety of Tibet will be present, unlike CK2 where the most eastern parts were excluded, and sub-Saharan Africa is also extended, where we’ve gone all the way to the Nigerian coast.  

When setting the map visuals, province layout, rivers, and more, the focus has always been on clarity. The map should be easy to read and get information from. For example, you should be able to read most of the terrain simply by looking at the map, without the need to click on the province, or tooltip it, in order to find that out, while rivers should be easy to see and let you know if you will cross one when moving armies around.  

We represent the map on three different zoom levels. When zoomed far out, the map will turn into an actual paper map, allowing for an easy overview and stylish screenshots. Zoom in a bit and you will have the 3D map, with the typical political overlay, great for interacting with your vassals and other realms. Zoom in even further and you’ll see the names of all the counties along with the terrain, as we strip away the realm colors. Perfect for moving armies around and knowing where to pick your battles, without the need to switch around to different map modes (but don’t worry, we still have several map modes for easily accessing different information).  

One of the most notable changes is how we handle Baronies. In CK2, Counties were the smallest entity we had on the map, a province if you will, with several Baronies represented through the interface of the County view. In CK3, we took the next logical step and made Baronies into their own provinces. We have been able to create a map with much more granularity and better accuracy. Most Counties will normally consist of two to five Baronies, with some exceptions. The amount of provinces will be noticeable when waging war, as it offers a larger degree of movement for you armies (more on that in the future).  

![dd_02_baronies.png](https://forumcontent.paradoxplaza.com/public/510962/dd_02_baronies.png "dd_02_baronies.png")

  

To give you a good idea of the increased province density, here is a comparison of the British Islands in CK2 and CK3, being on the left and right side, respectively:  

![dd_02_ck2_ck3_comparison.png](https://forumcontent.paradoxplaza.com/public/510963/dd_02_ck2_ck3_comparison.png "dd_02_ck2_ck3_comparison.png")

  

Before you all go nuts about playable baronies: No. You cannot play as a Baron. The lowest playable rank will still be that of a Count. The emphasis will therefore be on the Counties rather than the individual Baronies. As such, Baronies exist with a few things in mind. For example, they can never leave a county. This means Counties stay the same over time, avoiding weird splits where a single barony goes independent or to another realm (reducing that hideous border-gore ever-so-slightly). The number of Baronies within a County is one factor that represents its wealth and how “good” it is. Another important factor is the terrain. A County with a lot of Desert will not be as beneficial as one with a lot of Farmlands for example.  

Speaking of terrain, we have several different terrain types spread out across the map. Instead of having a single terrain spread out across large areas of the map, we differentiate between similar terrain types by separating them, such as Forest and Taiga, or Plains and Drylands. Not only does it make the map look and feel distinct in different parts of the world, they also have a different impact on gameplay.  

![dd_02_england.png](https://forumcontent.paradoxplaza.com/public/510960/dd_02_england.png "dd_02_england.png")

  

![dd_02_maghreb.png](https://forumcontent.paradoxplaza.com/public/510959/dd_02_maghreb.png "dd_02_maghreb.png")

  

Then we have Impassable Terrain. These are far more frequent, and in many cases much larger, than you will be used to from CK2. We’ve essentially used these for any area that we consider uninhabited enough to warrant it not being part of an existing County. Some areas have plenty of smaller impassable provinces, such as the mountains surrounding Bohemia, while others have fewer and far larger pieces of inhospitable land, such as the deserts of Arabia and Syria. Impassable Terrain cannot be traversed by armies, often creating bottlenecks that you’ll have to pass through or perhaps even choose to go around, should it be heavily fortified.  

![dd_02_impassable.png](https://forumcontent.paradoxplaza.com/public/510961/dd_02_impassable.png "dd_02_impassable.png")

  

That’s it for now. I hope you enjoyed this early sneak peak of the map and I'll be sure to show more to you in the future!

<!-- artifact:reactions:start -->
- 7 Like
- 2 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)**
Role: Game Designer
Badges: 4
Reaction score: 9,949

*[Full game-badge icon list of 37 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
