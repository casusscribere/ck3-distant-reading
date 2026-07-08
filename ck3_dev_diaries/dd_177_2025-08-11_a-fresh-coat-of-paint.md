---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1854817/"
forum_thread_id: 1854817
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 177
title: "Dev Diary #177 - A Fresh Coat of Paint"
dd_date: 2025-08-11
author_handle: PDX-plundh
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2212
inline_image_count: 36
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1854817'
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
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_392_to_396
    action: preserved_and_flagged
    counts:
      Love: 145
      Like: 83
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_404_to_505
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_506_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #177 - A Fresh Coat of Paint

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-plundh](https://forum.paradoxplaza.com/forum/members/pdx-plundh.1282941/)
- Start date [Aug 11, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-177-a-fresh-coat-of-paint.1854817/)
<!-- artifact:thread_metadata:end -->

Welcome to another summer Dev Diary! As the Swedes are lazily shuffling in the door after vacations, we’ll be discussing the map visuals. My name is Petter Lundh. I’m the Art Director for Crusader Kings III for the last two years, previously 2D Lead (my work might be most familiar in the form of the Iberia, Tours, and Persia loading screens)  

For *All Under Heaven*, we're undertaking our most ambitious expansion yet: extending the map to encompass all of Asia. This represents a big undertaking that goes beyond just extending the geography.  

While the map has seen new assets trickle in since release, the overall look remains unchanged. During those five years we’ve filled a big bucket of visual ideas we’re eager to implement though, and this expansion proved the perfect opportunity to give the entire map a facelift.  

This is mainly an artistic reimagining and a modernizing of our workflow. It doesn’t involve fancy new engine tech—we’re using the same features that have been available to the modding community already. This means you’ll be able to put your own spin on these changes, provided you’re up for tinkering with shader code (or coerce ChatGPT to do it for you).  

We also plan to add additional documentation that will make it easier for new modders to get started, though this may come later. Moreover, we're adding optional settings for some of the larger changes that impact performance.  

### Terrain Workflow​

In the olden days (CK3 release), we painted heightmaps and terrain masks by hand. This took our team months to complete, and any increase in detail would exponentially increase the workload. This process leaves little room for iteration and course correction underway.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1338241/image_01.png "image_01.png")


![image_02.png](https://forumcontent.paradoxplaza.com/public/1338242/image_02.png "image_02.png")




The old mountains were created mostly from a tiling normal map. This technique results in visual noise in dense mountain regions—something especially apparent when extending the Himalayas eastward. We would rather have a more realistic appearance that mimics real erosion patterns. Mountains should feel more like real mountains.  

We adopted the terrain generation software Gaea to solve this problem. It’s a tool that creates realistic heightmaps and material masks through simulating real erosion patterns. We can generate complex terrain far more efficiently than with manual painting, and we no longer have to start from scratch when iterating on the general look.  

The scale of terrain features remains largely the same. There’s a few reasons for this:  


- We used the old heightmap as a base since the shape of the map also has gameplay implications.
- We find that the stylized scale of mountains look best when zoomed in, even though a more realistic scale can feel better zoomed out. If we adopted a real world scaling, most mountains would appear as noise when zoomed in (at the level where you can actually inspect the terrain).


![image_03.png](https://forumcontent.paradoxplaza.com/public/1338243/image_03.png "image_03.png")


![image_04.png](https://forumcontent.paradoxplaza.com/public/1338244/image_04.png "image_04.png")




Here’s what the process looks like:  


1. We divide the input heightmap ocean masks into tiles.
2. Each tile gets processed through Gaea, which outputs a final heightmap, overlay colormap and masks for the individual tiling materials.
3. All the output tiles are then stitched together, leaving us with large texture files that cover the entire map

As an extra complication we have divided the world into 7 biomes that each have their own set of tiling textures and material masks that define its character. The above steps are run individually for each biome, and stitched together at the very end to create the final map.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1338245/image_05.png "image_05.png")



For each biome, we’ll gather references and attempt to extract some unique color palette that makes it look different from other places.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1338246/image_06.png "image_06.png")



When we are iterating on the look, we work with a single tile. We'll pick a prototype tile that is representative of a particular biome and refine that particular tile - when we are happy with the result, we do a full build of the entire world, which can take up to 3 hours.  

Here is an anatomical diagram of sorts of the CK3 map:  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1338247/image_07.png "image_07.png")


### ​

### Surface Polish​

The improvements go beyond the heightmap and terrain textures. We have taken a careful look at the lighting and shaders for all map elements. Subtle tweaks are added to most elements to improve readability and make them aesthetically blend together in a nicer way.  

- Map text now has a subtle texture and softer appearance - it should feel less digital and easier on the eyes.
- The Political Map has a higher res texture with less apparent tiling.
- The water now has more varied detail and color in different parts of the world. There are improved wave patterns along the shore, and overall the scale and wave texture has been balanced for a more realistic feel.
- Effects blend more naturally between zoom levels, removing some long-standing pop-in and glitches that were noticeable in the transition between paper map, political and terrain map modes. Speaking of zoom, you can now zoom in closer than before!

![image_08.png](https://forumcontent.paradoxplaza.com/public/1338248/image_08.png "image_08.png")


![image_09.png](https://forumcontent.paradoxplaza.com/public/1338249/image_09.png "image_09.png")


### Lighting​

Lastly, we have reworked the terrain lighting. Terrain and map objects now have separately adjustable parameters that let us tweak their values individually, allowing us an easier time making them both look great. The map is generally brighter and important interactable objects should pop more.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1338250/image_10.png "image_10.png")



We've added cloud shadows that creep across the landscape. To top it all off, we're adding a Terrain Map Mode that lets you view the entire world in this enhanced visual style.  

We hope you’ll like it!  

(If you don’t, you can disable cloud shadows and some of the other shader-based changes in the game settings)  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1338251/image_11.png "image_11.png")


![image_12.png](https://forumcontent.paradoxplaza.com/public/1338252/image_12.png "image_12.png")


*[Iceland before-and-after]*  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1338253/image_13.png "image_13.png")


![image_14.png](https://forumcontent.paradoxplaza.com/public/1338254/image_14.png "image_14.png")


*[Spain before-and-after]*  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1338255/image_15.png "image_15.png")


![image_16.png](https://forumcontent.paradoxplaza.com/public/1338256/image_16.png "image_16.png")


*[Arabia before-and-after]*  

![image_17.png](https://forumcontent.paradoxplaza.com/public/1338257/image_17.png "image_17.png")


![image_18.png](https://forumcontent.paradoxplaza.com/public/1338258/image_18.png "image_18.png")


*[Britannia before-and-after]*  

![image_19.png](https://forumcontent.paradoxplaza.com/public/1338259/image_19.png "image_19.png")


![image_20.png](https://forumcontent.paradoxplaza.com/public/1338261/image_20.png "image_20.png")


*[India before-and-after]*  

![image_21.png](https://forumcontent.paradoxplaza.com/public/1338263/image_21.png "image_21.png")


![image_22.png](https://forumcontent.paradoxplaza.com/public/1338264/image_22.png "image_22.png")


*[Italy before-and-after]*  

![image_23.png](https://forumcontent.paradoxplaza.com/public/1338265/image_23.png "image_23.png")


*[Japan in All Under Heaven]*  


---

### Paper Map​

Hey, this is Lucas Ribeiro, 2D Art Lead. As some might’ve noticed from our previous dev diaries, we have a new illustrated paper map for *All Under Heaven*. This asian-folklore inspired map covers the entirety of the game world and will be used by default by most east asian cultures. Our original paper map has also been extended all the way to the east. Besides cultural triggers, players will also be able to pick which paper map style they’d rather use in the graphics tab of the settings menu.  

![image_24.png](https://forumcontent.paradoxplaza.com/public/1338266/image_24.png "image_24.png")



Let’s have a look at some snapshots from the new illustrated map:  
Around Japan we can observe the Kappa, the Ushi-oni and the Baku (Or… is that the Bulgasari by the east coast of the Korean peninsula?).  

![image_25.png](https://forumcontent.paradoxplaza.com/public/1338267/image_25.png "image_25.png")



Between Korea and China, Cholima streaks across the sky. Surrounding China we can observe the Fenghuang bird and the first of our cardinal direction beasts, the Azure Dragon of the East. More of these beasties are appropriately positioned in the map…  

![image_26.png](https://forumcontent.paradoxplaza.com/public/1338268/image_26.png "image_26.png")



…Such as the Vermillion Bird of the South, under India…  

![image_27.png](https://forumcontent.paradoxplaza.com/public/1338269/image_27.png "image_27.png")



…the White Tiger of the West by the Iberian Peninsula …  

![image_28.png](https://forumcontent.paradoxplaza.com/public/1338270/image_28.png "image_28.png")



…and finally, the Black Turtle of the North by Scandinavia.…  

![image_29.png](https://forumcontent.paradoxplaza.com/public/1338271/image_29.png "image_29.png")



We have endeavored to represent the terrain features of the world in a style more reminiscent of Chinese paintings and Shan Shui, with bold paint strokes and intricate natural patterns. The leafy steep mountains should reflect this very clearly.  

![image_30.png](https://forumcontent.paradoxplaza.com/public/1338272/image_30.png "image_30.png")



For the original map extension, we kept the style inspired in the Olaus Magnus Carta Marina. The familiar mountain, forest, desert, etc. patterns have been extended all the way to the East as well.  

![image_31.png](https://forumcontent.paradoxplaza.com/public/1338273/image_31.png "image_31.png")



---

### Title Changes​


Hello, [@Cordelion](https://forum.paradoxplaza.com/forum/members/1759707/) here, one of the Game Designers currently working on *All Under Heaven!* The look of the map isn't the only thing that has been getting an update: borders and names have been, as well! The de jure structure of China has changed and evolved significantly over the summer as we've processed the tremendous outpouring of incredibly valuable feedback that we've received since the reveal, both internally (with many thanks to our fantastic beta testers) and externally (with many thanks to all of you!). So let's dive in!  

At the empire tier, the main change you may notice now is that the names were previously inspired by dynasties that once ruled these lands in ancient times, but are now significantly more regional than dynastic in flavor. Liang is now Zhongyuan, Wu has become Jingyang, Yue changed to Lingnan, Shu transformed into Liangyi, and Qin evolved into Yongliang.  

These names are, to be clear, more for general reference and suitability as labels for unformed de jure empire tier: anyone who comes to rule one of these as an independent entity still may adopt one among a range of proper venerable dynastic names!  

![image_32.png](https://forumcontent.paradoxplaza.com/public/1338274/image_32.png "image_32.png")



The kingdom structure has undergone some changes, also - you may note the replacement of the phonetically repetitive Jingdongdong with Qingxu, while the previous northern de jure kingdom of Yanyun has been divided into Raole, Daibei, and Youji, allowing for more historical assignments and more piecemeal northern reclamation - or southward expansion, if you happen to be a nomadic dynasty!  

![image_33-Corrected.png](https://forumcontent.paradoxplaza.com/public/1338304/image_33-Corrected.png "image_33-Corrected.png")



As the terrain map has been refined, so too has the distribution of impassable terrain - the Sichuan basin is ringed with strategically challenging peaks and ranges, reflecting its historically significant natural geographic barriers, while coastal Fujian also exhibits a significant mountain presence - eight parts mountain, one part water, one part fields, as at least one book I consulted put it.  

![image_34.png](https://forumcontent.paradoxplaza.com/public/1338276/image_34.png "image_34.png")



![image_35.png](https://forumcontent.paradoxplaza.com/public/1338277/image_35.png "image_35.png")



I’m also here with something else new: the county-tier map of China, which wasn’t quite ready to show off the last time we talked about this new part of the game world, but that I’m more than happy to give you a better look at today. For those of you who may be unfamiliar with the obvious preponderance of -zhou, it’s a standard administrative suffix for this level of jurisdiction throughout Chinese history - one that remains an element of many major cities, such as Hangzhou and Suzhou, even up to the present day!  

![image_36-Corrected.png](https://forumcontent.paradoxplaza.com/public/1338303/image_36-Corrected.png "image_36-Corrected.png")



That’s all that I have for you today - hopefully you’ve enjoyed this brief look at how this part of the map is coming along. I’d love to share even more of what I’ve been working on with you, but that information is reserved for dev diaries to come and I’ll not be the one to spoil them ahead of time: next week we’ll be back with something a bit more sizable for you to dig into! Thanks for stopping by, and I’m very much looking forward to seeing you explore and experience everything that *All Under Heaven* has to offer yourselves soon enough!

<!-- artifact:reactions:start -->
- 145 Love
- 83 Like
- 15 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-plundh](https://forum.paradoxplaza.com/forum/members/pdx-plundh.1282941/)**
Role: CK3 Art Director
Badges: 17
Messages: 4
Reaction score: 461

*[Full game-badge icon list of 41 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
