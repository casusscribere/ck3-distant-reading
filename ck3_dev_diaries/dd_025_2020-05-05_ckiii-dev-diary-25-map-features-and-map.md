---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1388210/"
forum_thread_id: 1388210
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 25
title: "CKIII Dev Diary #25 - Map Features and Map Modes"
dd_date: 2020-05-05
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
body_word_count: 1303
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1388210'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1367.jpg?1588682046
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_241_to_245
    action: preserved_and_flagged
    counts:
      Like: 113
      Love: 67
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_253_to_363
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_364_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1367.jpg?1588682046)
<!-- artifact:thread_banner:end -->

# CKIII Dev Diary #25 - Map Features and Map Modes

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [May 5, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ckiii-dev-diary-25-map-features-and-map-modes.1388210/)
<!-- artifact:thread_metadata:end -->

Greetings everyone!  

Today I’m here to talk a bit about the map. Building on top of our early map related DD#2 (if you have yet to read it, [you can do so here](https://forum.paradoxplaza.com/forum/index.php?threads/ck3-dev-diary-2-the-medieval-map.1274052/)), I’ll expand that discussion by outlining additional features, new information, and how you interact with the map itself!  

**Terrain**  
Let’s start with the terrain, which has a significant impact on several parts of the game. Different terrain types allow for different buildings to be constructed. For example, farmland allows for superior economy buildings, while mountainous terrain unlocks rather impressive defensive structures. They also have an effect on development, making development change faster or slower over time. Expect it to be a massive undertaking of developing the Sahara, while developing the fertile fields of India will be a much easier task.  

As for combat, one of the most noticeable effects is that of combat width. When you are fielding a much larger army than your opponent, you will favour a high combat width, so you’ll want to seek to engage the enemy in plains or drylands. On the other hand, fighting in rough terrain like mountains or wetlands will restrict the number of units that can simultaneously engage the enemy, allowing small armies with powerful Men-at-Arms to truly excel. Terrain also affects army movement speed, along with the usual defensive bonus you would expect in rough terrain types, which is gained in the form of increased Advantage at the start of a battle.  

The terrain types we have available are the following:  
**Farmlands** - Has access to many different and powerful buildings, allowing you to easily customize your holding the way you want to. Paired with high development speed, farmland provinces are highly desirable to hold in your domain.  
**Floodplains** - Another desirable terrain type used in certain areas, such as along the Nile. Similar in power to farmlands, but with some minor differences.  
**Plains** - One of the most common terrain types, plains exist almost everywhere and provide a wide range of building options.  
**Drylands** - A variant of plains with slightly different buildings available.  
**Desert** - While deserts doesn’t offer a whole lot in terms of taxes, supply limit or development, it does have access to levies and a unique building chain increasing your number of available Knights.  
**Oasis** - These exist only in certain areas. The terrain has access to similar buildings as desert, but without the penalties in supply limit or development.  
**Steppe** - Mostly used by tribals on the wide steppe, this is where Horse Archers reign supreme. The steppe starts with low development, and has a significant penalty in development growth.  
**Forest** - Has lower combat width and supply limit, but offers great buildings for improving archers and skirmishers.  
**Taiga** - A variant found in the very northern parts of the map, with slightly lower combat width and supply limit than forest.  
**Jungle** - Mainly found in India and offers even less combat width and supply limit. It does, however, have access to a unique building chain for improving your Knights and heavy cavalry.  
**Hills** - Hills offers a small Advantage bonus in combat, and has access to both fortifications and decent tax buildings.  
**Mountains** - Has access to great fortifications and defensive buildings, making it a long and risky business to siege down holdings.  
**Desert Mountains** - Similar to mountains, but for desert areas (obviously), with lower supply limit, development growth, as well as a bonus that allows defending armies to take less casualties when retreating.  
**Wetlands** - While wetlands still allow for some decent buildings, it’s a terrain type you don’t want to fight battles in if you can avoid it. Especially if there’s a risk of being on the losing side...  

![25_01_wetlands.jpg](https://forumcontent.paradoxplaza.com/public/561430/25_01_wetlands.jpg "25_01_wetlands.jpg")



![25_01_farmlands.jpg](https://forumcontent.paradoxplaza.com/public/561429/25_01_farmlands.jpg "25_01_farmlands.jpg")



**Context Sensitive Selection**  
We want it to be easy to gain information directly from the map. Whenever you change map modes, or have something “selected”, we update the map accordingly and allow you to often interact with the map itself. Clicking on the map on any given realm, will open that ruler’s character view. This in turn allows you to see rulers he is at war with, his allies, or direct vassals. All of this is shown directly on the map and is selectable, though you do not have to rely on finding it on the map; we still show relations and everything in the interface as well.  

![25_02_ruler_selection.jpg](https://forumcontent.paradoxplaza.com/public/561431/25_02_ruler_selection.jpg "25_02_ruler_selection.jpg")



This applies to everything we show on the map. Regardless of your map mode, you can always click to select the “entity” you are looking at. If you have the faith map mode active, you can click on a faith to open the interface for it, as well as seeing where its holy sites are located.  

**Realm Map Mode**  
Your bread and butter map mode is what we simply call the Realm map mode.  
When zoomed in you’ll encounter what we call the detail level, and will see the map for what it is. Terrain of individual baronies, rivers, and holding graphics are all clearly visible.  

![25_03_realm_1.jpg](https://forumcontent.paradoxplaza.com/public/561432/25_03_realm_1.jpg "25_03_realm_1.jpg")



Zoom out a bit and you’ll transition into the Realms layer, your typical political map mode. Realms are clearly highlighted with their colour, allowing you to easily see all independent realms at a glance, while still showing the coat of arms of your direct vassals, to allow for easy realm management.  

![25_04_realm_2.jpg](https://forumcontent.paradoxplaza.com/public/561433/25_04_realm_2.jpg "25_04_realm_2.jpg")



Zoom out further and you’ll enter the paper map. This is the place to go for a rather fancy overview of the world (or excellent screenshots)! Only independent realms are shown, without any vassal breakdowns. For now, I’ll just tease you with a partial picture, as we’ll show the entire thing in a later DD. And yes, we got the mandatory sea monsters!  

![25_05_realm_3.jpg](https://forumcontent.paradoxplaza.com/public/561434/25_05_realm_3.jpg "25_05_realm_3.jpg")



**Other Map Modes**  
Our other map modes remain consistent in the information they show as you zoom in and out, and do not have the level dependency of Realms. If you have the faith map mode open, you are gonna want to see faiths regardless of your zoom level. You’ll still get the spectacular paper map when you zoom further out, but the information shown on the map will remain the same.  

**De Jure** - As you’d expect, we have dedicated map modes for showing the De Jure areas of duchies, kingdoms, and empires.  

**Faiths** - Allows you to easily see what faiths are spread out around the world.  

**Cultures** - For that nifty culture overview.  

**Houses** - Since it’s a game about characters and dynasties, we want it to be easy to see which house is governing the different realms.  

**Counties** - Highlights individual counties in their respective colour.  

**Terrain** - Shows all terrain types in different colours, for that quick and easy overview of the dominant terrain in any given area. Very useful if you have several Men-at-Arms options available with different terrain bonuses.  

**Governments** - The map mode for viewing what kind of government rulers have.  

**Development** - Gives you an overview of what the development level is across the map.  

![25_06_house_map_mode.jpg](https://forumcontent.paradoxplaza.com/public/561435/25_06_house_map_mode.jpg "25_06_house_map_mode.jpg")



That’s it for today! I’ll be back next week with another map related entry. Where I plan to simply show you, well, everything regarding the scope of the map and how different parts of the world looks!

<!-- artifact:reactions:start -->
- 113 Like
- 67 Love
- 18 (unlabeled — rendered as base64 data URI)
- 10 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)**
Role: Game Designer
Badges: 4
Reaction score: 9,949

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
