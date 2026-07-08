---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1283865/"
forum_thread_id: 1283865
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 4
title: "CK3 Dev Diary #04 - Development & Buildings"
dd_date: 2019-11-19
author_handle: rageair
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 896
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1283865'
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
    location: raw_lines_~28_to_144
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_146_to_148
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_190_to_192
    action: preserved_and_flagged
    counts:
      Like: 6
      Love: 3
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_200_to_264
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_265_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #04 - Development & Buildings

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Nov 19, 2019](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-04-development-buildings.1283865/)
<!-- artifact:thread_metadata:end -->

Greetings!  

This week's Dev Diary is all about your holdings on the map - Baronies and counties, what they do for you, and what you can do with them! As seen in the map DD, Baronies are now physically present on the map. A group of Baronies makes up a greater unit, called a County.  

![DD4CountyView.jpg](https://forumcontent.paradoxplaza.com/public/514101/DD4CountyView.jpg "DD4CountyView.jpg")

  

While certain things are still on a per-Barony level, such as buildings, two of the most important values you have to deal with are on a per-County basis - Development and Control!  

Development is the measurement of technological advancement and general infrastructure in a County. Development directly increases taxes and levies you get out of the holdings, and it also unlocks some other special options. Development increases very slowly across the duration of the game, and radiates outwards from high-development Counties to those nearby. For example, Constantinople *(aka the City of the World’s Desire)*, starts with a very high Development level. This will slowly spread outwards, reaching the most remote areas much slower than their Greek heartland. Naturally, there are other ways to increase your development, such as through the Steward’s ‘Increase Development’ task, although this is a fairly slow process, and usually only worth doing in certain Counties. Having terrain such as Farmland or Floodplains in your Counties make them ideal candidates for development, and when they have gotten some levels of development you can just sit back and enjoy, as it slowly spreads throughout the rest of your realm!  

Control, on the other hand, directly represents the power you have over the County. This naturally decreases during sieges and by forcefully seizing territory, taking the place of the ‘new Administration’ modifiers from CK2. If you don’t pace yourself, and use your Marshal to increase Control in newly conquered territories, you might find yourself with a slew of useless land. This also increases the importance of keeping peasant rabble and similar nuisances out of your lands…  

Each County also has an opinion of their holder, referred to as the ‘Popular Opinion’. This represents the sentiment of the local peasants, and tends to decrease if you’re not of their culture or faith, promoting the use of ‘local lords’, vassals of the local culture/faith, to handle such territory for you - as converting it will take quite some time. Unhappy Counties tend to cause problems down the line… more on this in another DD.  

Now, on to the Holdings themselves! Each County will have a certain amount of slots available for Baronies, with some being constructed at the start, and others not. The three core types of holdings remain unchanged - Castles, Cities and Temples make up the majority of holdings on the map, each with their own main purpose. Castles provide levies and fortifications, cities provide taxes with a secondary focus on Development, and temples provide an even mix of taxes and levies with a secondary focus on increasing Control. This means that if you want a County to develop really fast, building many Cities might be the thing for you. If you want a resilient domain perhaps you’d prefer Castles, etc.  

![DD4Holding.jpg](https://forumcontent.paradoxplaza.com/public/514100/DD4Holding.jpg "DD4Holding.jpg")

  

Based on the terrain of the province, each Holding has access to a number of buildings. Regular buildings primarily focus on increasing taxes and levies, with some secondary effects such as increasing fortifications or increasing supply. These are usually straight upgrades, and are long-term investments that you should always consider, much like in our other games.  

![DD4Buildings.jpg](https://forumcontent.paradoxplaza.com/public/514102/DD4Buildings.jpg "DD4Buildings.jpg")

  

To spice things up, we've also introduced the concept of Duchy Capital Buildings. These buildings can only be built in the capital Barony of any De Jure Duchy, limiting their availability across the map. To build them and have them be active, you need to hold their associated Duchy title personally - this way you can’t simply hoard Counties in which you can build these special buildings, as just like in CK2 you will get severe penalties for holding too many Duchies personally. The buildings themselves are very expensive, but come in many flavors - allowing you to tailor your experience. The Military Academies track of buildings increases the effectiveness of your Knights and allows you to have more of them, establishing marches will make the entire Duchy more defensible, the Siege Workshops will increase the effectiveness of your trebuchets, and so on!  

![DD4DuchyCapitalBuildings.jpg](https://forumcontent.paradoxplaza.com/public/514099/DD4DuchyCapitalBuildings.jpg "DD4DuchyCapitalBuildings.jpg")

  

We also have the concepts of special buildings. These aim to represent historical buildings, both ancient and those built during the time period. Placed in predetermined baronies on the map, you have the usual suspects such as the Pyramids or Colosseum, along with more fringe or lesser-known constructions such as Offa’s Dyke or the Buddhas of Bamiyan. Some of these will be possible to construct during the course of the game, such as the Tower of London or the Alhambra. All of these constructions provide unique and interesting bonuses, with some of them being represented with 3D models on the map.  

That’s it for this time! Stay tuned for the next DD, where we will tell you about the new scheme mechanics!

<!-- artifact:reactions:start -->
- 6 Like
- 3 Love
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 2 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
