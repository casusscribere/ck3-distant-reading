---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1567601/"
forum_thread_id: 1567601
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 115
title: "Dev Diary #115 - Monumental Foundations"
dd_date: 2023-02-07
author_handle: Carlberg
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1189
inline_image_count: 12
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1567601'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2191.jpg?1675776407
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_260_to_265
    action: preserved_and_flagged
    counts:
      Like: 155
      (unlabeled — rendered as base64 data URI): 4
      Love: 42
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_273_to_383
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_384_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2191.jpg?1675776407)
<!-- artifact:thread_banner:end -->

# Dev Diary #115 - Monumental Foundations

<!-- artifact:thread_metadata:start -->
- Thread starter [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)
- Start date [Feb 7, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-115-monumental-foundations.1567601/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to this dev diary where we will be looking into some new map visuals that’ll be added in the future. As the team grows, we’ve had the opportunity for our new artists to warm up by sprucing up the map a little. Among the things we’ll show off today, chief is the Canterbury Cathedral and its evolution over time: made by our new Environment artist Joel, who’s written about his process and the research involved.  


## ​

## Building a Monument – Canterbury Cathedral​

### The Original Church - Tier 1​

When creating the first tier of the Canterbury Cathedral, which references the Anglo-Saxon church extant in the 867 & 1066 start dates, it was important to acknowledge the lack of available visual reference material. Historically speaking, the Anglo-Saxon church was burnt down in 1067, but we do have some conceptual renditions and blueprints of the estimated building layout to work from, courtesy of the archeologists (our heroes).  

![blueprint1.png](https://forumcontent.paradoxplaza.com/public/932765/blueprint1.png "blueprint1.png")

![blueprint2.png](https://forumcontent.paradoxplaza.com/public/932766/blueprint2.png "blueprint2.png")


*Sometimes luck strikes and blueprints or estimated ones can be found.*  

From this, I created a fairly basic interpretation of the church that serves well as the first/starting stage for the Canterbury Cathedral. Additional geometry, like pillars and an external house, was added to the building to create a more compelling in-game silhouette.  

![tier1.png](https://forumcontent.paradoxplaza.com/public/932767/tier1.png "tier1.png")


*The original Anglo-Saxon church - Tier 1*  


### ​

### The Norman Cathedral - Tier 2​

After the first fire, a second church was built in its place, distinctively making use of the Romanesque style. As we move forward in history, more references become available, and fortunately the church foundations are described as rather similar to the church of today. The more significant differences to modern Canterbury Cathedral are, for example, the front and main towers: they are still Romanesque.  

![tier2.png](https://forumcontent.paradoxplaza.com/public/932768/tier2.png "tier2.png")


*Canterbury Cathedral - Tier 2*  

**Romanesque and Gothic**  
If this happens to be your first time coming across these terms, some explaining might be in order. Romanesque and Gothic are two styles of architecture which defined buildings and churches throughout the Medieval era. Romanesque, the older of the two, emerged sometime around the year 1000 and lasted until around 1150. It’s a style arising from and defined by Germanic, Byzantine and old Roman influences, favoring circular Roman arches and a more solid-looking facade compared to later churches.  

![lessay.png](https://forumcontent.paradoxplaza.com/public/932769/lessay.png "lessay.png")


*Romanesque Abbaye de Lessay*  

From the Romanesque emerged the Gothic in the 12th-13th centuries. In Gothic architecture, Roman arches find themselves replaced by Gothic ones; we also see elaborate ribbed vaults, towering flying buttresses, and church interiors brightened by large stained glass windows.  

![chartres.png](https://forumcontent.paradoxplaza.com/public/932770/chartres.png "chartres.png")


*Chartres Gothic Cathedral*  

**Modeling**  
I technically started with the third tier of the structure of the Canterbury Cathedral, rather than the second tier. Because we work with modular pieces and texture atlases, I find it easier to work from the complete cathedral, then remove any additional geometry. It also meant that the last tier would have most of the same layout as the modern cathedral, minus some of the later additions.  

![modular.png](https://forumcontent.paradoxplaza.com/public/932771/modular.png "modular.png")


*Modular pieces used for building the Cathedral*  

With the modular pieces ready, it was then just a question of assembling the cathedral.  


### The Gothic Cathedral - Tier 3​

We could see in the final version of the Cathedral that a lot of areas had been raised since the time of the second, so I simply made minor tweaks to the height of some walls and roofs, while preserving the original UV. The back of the cathedral had also been extended and rebuilt, with the addition of two new structures. The south-west tower was rebuilt, but not the north-west tower as of yet: that happened later historically.  


![cathedral.jpg](https://forumcontent.paradoxplaza.com/public/932772/cathedral.jpg "cathedral.jpg")


*The cathedral with the towers in the front. The main tower however was a new construction past CK3’s timeline.*  

![tier3.png](https://forumcontent.paradoxplaza.com/public/932773/tier3.png "tier3.png")


*Canterbury Cathedral - Tier 3*  

The third tier takes on a Gothic style, with flying buttresses along the length of the cathedral, and it also puts a golden angel on the pinnacle of the main tower.  


**Basing and Decal**  
In order for us to be certain that our holdings will be placed correctly on the map, we extend the ‘basement’ of the mesh into the ground to accommodate for the map’s height differences.  
This ensures we have no areas free flying in the air. Usually this is a bigger issue for holdings than monuments, as monuments have a single specific place on the map where they exist.  

![decal-texture.png](https://forumcontent.paradoxplaza.com/public/932774/decal-texture.png "decal-texture.png")


*Decal texture in Substance Painter*  

We also create decals that show a more interesting ground variation around the structure. In my case, I painted out some roads to give life to the area. Some color variation to the grass to better blend in with the rest of the map, and darker areas where the cathedral would be located. The decal plane is on average twice the size of our building.  

![tiers1-3.png](https://forumcontent.paradoxplaza.com/public/932775/tiers1-3.png "tiers1-3.png")


*Anglo-Saxon church , Romanesque Cathedral, Gothic Cathedral T1 - T2 - T3*  

After all the buildings were done and I was happy with the progression from tier 1 to tier 2 and tier 3, I could finalize the UV’s. We use two UV maps to layout the textures: one is for the ambient occlusion that we bake in, and the other for the texture atlas. The texture atlas lets us reuse textures to save on performance. I did the baking in marmoset with a low poly to low poly set up. Normally you have a high poly to bake down to the low poly mesh, but I was only after the ambient occlusion.  


## ​

## Bonus Bridge Update​

A new set of cultural stone bridges will be added over the world, replacing some of the old wooden bridges and overall making it a bit clearer where the safer river crossings are. We will be adding a total of four standard bridge types, for Western Europe, the Mediterranean, the Middle East, and Indian regions.  


![bridges.png](https://forumcontent.paradoxplaza.com/public/932776/bridges.png "bridges.png")


These bridges have been based on historical examples sampled from these regions. The Western and Mediterranean bridges are based on arched bridges from Europe, with the appropriate local flairs. The Middle Eastern bridge is based upon Sassanid designs like the Marnan and Kohneh bridge, among others, and are mostly found in the regions around modern Iran and Iraq. The Indian bridges take their inspiration from the Athernala bridge in eastern India.

<!-- artifact:reactions:start -->
- 155 Like
- 48 (unlabeled — rendered as base64 data URI)
- 42 Love
- 12 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)**
Role: Senior Environment Artist
Badges: 40
Messages: 221
Reaction score: 2,288

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
