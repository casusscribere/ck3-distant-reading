---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1500937/"
forum_thread_id: 1500937
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 84
title: "CK3 Dev Diary #84 - Building a Court - A Tale of Code and Art"
dd_date: 2021-11-30
author_handle: Carlberg
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2841
inline_image_count: 31
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1500937'
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
    location: raw_lines_~28_to_143
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_142
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1801.jpg?1638283554
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_145_to_147
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_389_to_393
    action: preserved_and_flagged
    counts:
      Like: 130
      Love: 51
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_401_to_500
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_501_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1801.jpg?1638283554)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #84 - Building a Court - A Tale of Code and Art

<!-- artifact:thread_metadata:start -->
- Thread starter [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)
- Start date [Nov 30, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-84-building-a-court-a-tale-of-code-and-art.1500937/)
<!-- artifact:thread_metadata:end -->

### CK3 Dev Diary #84 - Building a Court - A Tale of Code and Art.​

Hello and welcome to Dev Diary #84, I’m [@Carlberg](https://forum.paradoxplaza.com/forum/members/940169/) , the 3D environment lead artist and today we will be having a closer look at the development of the Royal Court rooms. This is a feature that we’ve been working hard on and it represents a great new step in bringing this historical era to life. Big thanks to [@Alien-47](https://forum.paradoxplaza.com/forum/members/225407/) (code), Stella (3D environment art) and Linus (tech art) who's perspectives they've written down for this Dev diary, drawn from their experiences from both code and art in the making of this feature.  

*Heads up! -* A lot of the pictures in this post will be of old prototypes and iterations intermixed later with more recent images towards the end. So no need to worry about issues you may spot in the older images.​

### A new visual feature​

With the new 3D character systems implemented in CK3 we wanted to show the characters of the middle ages in a whole new dynamic way. So as we started laying down the foundations of the Royal Court we also wanted to bring the very courts to life and find continued use for these 3D characters. This new feature was a major step in that direction.  

The inspiration for the feature was partly scenes that hearken back to throne rooms seen in games of old where we wish they had been livelier, with more interaction and chances for us to impact the people and objects in them. We drew upon these concepts and ideas of our own to weave together a visualization of the courts hosted by the most prominent royal titles.​


---

#### The Prototyping​

At the beginning of the court development we knew that we were in for a challenge to stake out a new visual workflow within the engine that previously had not had any instances of contained 3D scenes and shared lighting systems within it. So we decided that to start off we needed a working prototype - laying a foundation and gradually adding more and more graphical features and complexity. Moving forward only when we’re sure the previous step succeeded.  

A natural starting point of exploration were the characters. We could already show beautiful animated portraits and the courtroom had to be able to show the same people so players could easily recognize their appearance. Could we reuse the same system that assembles characters - show appropriate body, apply transformation to show age, height, weight, apply the same clothing, hair, set the same animation? First step - success. The people in the courtroom look exactly the same as in portraits.  

Next step, is it possible to show many people at the same time in the same scene? This is quite different from portraits in the interface and events - those always have 1 person per image, even if the UI tries to combine them nicely together. With some optimization the room could now handle about 20 random characters, and even some objects. So the scene finally resembles a courtroom. Although a bit dark.​


![many-people.png](https://forumcontent.paradoxplaza.com/public/768107/many-people.png "many-people.png")


*The scene could now show several people and items in the prototype*​


But what can we do with lights? The ambition for the court scene and requirement for lighting is much higher and more advanced than for regular portraits. We needed more simultaneous light sources. At the same time shadows naturally become much more complicated as well. People and objects can interfere with lights and it needs to be visible. Another issue was making sure characters and objects apply the lighting and shadows in the same way, so it’s easier for artists to manipulate the scene and develop the assets. After a bit of time and several iterations we had upgraded and made many improvements to the lighting system.​


![working-lights.png](https://forumcontent.paradoxplaza.com/public/768106/working-lights.png "working-lights.png")


*Lights and shadows in a shared scene — Proof that multiple lights work and blend as intended, if a bit rough still.*​


It was roughly at this time we felt we had confidence that the goal was within reach, and all technology was working as we intended. It was also clear that we could afford the desired complexity of the scene from a performance point of view. After all, players should have an enjoyable experience both on the map and in the court. We had built an understanding of how many people the scene could handle efficiently, how many light sources, and how many shadows we could allow (this is one of the most expensive parts).  

And so the prototype has been integrated as a proper feature of the game.  



![looking-good.png](https://forumcontent.paradoxplaza.com/public/768104/looking-good.png "looking-good.png")


*Scene with better lighting, assets, materials, people positions*​


From this point on work on the court room continued with multiple people from different disciplines working very closely together. More and more features waited to be implemented, so you can now see the beautiful results of all this effort.  

---

#### Concept art and vision​

Being worked alongside the prototype was the vision we had for the Royal Court-rooms. We began by looking at the four main cultural areas we would be covering in the expansion. The west European, Mediterranean, Middle-eastern and Indian courts. We wanted each of these areas to be distinct, having their own visual style through architecture and lighting so to give their own unique feeling.  

![mediterranean_front_wall_concept.jpg](https://forumcontent.paradoxplaza.com/public/768098/mediterranean_front_wall_concept.jpg "mediterranean_front_wall_concept.jpg")

![western_front_wall_concept1.jpg](https://forumcontent.paradoxplaza.com/public/768097/western_front_wall_concept1.jpg "western_front_wall_concept1.jpg")


![front_walls_concept_mena.jpg](https://forumcontent.paradoxplaza.com/public/768099/front_walls_concept_mena.jpg "front_walls_concept_mena.jpg")

![indian_front_walls_concept.jpg](https://forumcontent.paradoxplaza.com/public/768100/indian_front_walls_concept.jpg "indian_front_walls_concept.jpg")


*Concepts of the different walls aesthetics of the courts, Mediterranean, Western, Middle-East/North Africa and India.* ​


The west European court draws much of its inspiration from courtly interiors of England, Germany, France and neighboring areas. Darker rooms lit by fiery hearths, candles and chandeliers. In the Mediterranean more inspiration comes from the Byzantine courts and those found in Italy and other heirs of Rome. The rooms hint back at this grander past with larger roofs, domes and columns supporting the walls and arches.  

In the Middle-eastern courts we have a wider spread geographically, as these courts draw inspiration and cues from the courts all the way from Arabia to the architecture of Andalusia. In India we encountered an interesting split, as influences in architecture were pushing in from the west while there were still distinctly Indian courts. This was one of the reasons behind adding more court variants so that we could cover more of these visual flairs.  



![indian_side_walls_concept07.jpg](https://forumcontent.paradoxplaza.com/public/768190/indian_side_walls_concept07.jpg "indian_side_walls_concept07.jpg")

![indian_side_walls_concept08.jpg](https://forumcontent.paradoxplaza.com/public/768191/indian_side_walls_concept08.jpg "indian_side_walls_concept08.jpg")

![indian_side_walls_concept09.jpg](https://forumcontent.paradoxplaza.com/public/768192/indian_side_walls_concept09.jpg "indian_side_walls_concept09.jpg")


*Style variation exploration, more on those further down in the Dev Diary.*​


Each scene was broken down into components like walls, roofs, floors and key assets like thrones, chandeliers and fireplaces. While these were being designed from a plethora of references gathered from each culture we also created variants in the concepts. This was done both as exploration but also to add variance to the courts so that they don't all look the same all the time. You will most likely have seen some variants of these when we’ve shared screenshots in past dev-diaries.  


​

#### 1638205284220.png

*Different courts, different architectural styles, different lighting setups.*​


But the concept art phase did not end after the initial stages however, because once the scenes were being put together we returned to the concepts to try out the different lighting setups to help in the lighting of the rooms, giving our artists more ideas of where to focus the light and accentuate the scene further. Since the lighting system was being built alongside this in the prototype, the concept art took inspiration from contemporary game engines to help guide the prototyping, and not just the visual development.  

---

#### A room takes shape​

When starting the modeling of the actual assets for the throne rooms there were several constraints to keep in mind. We had decided to go with a modular workflow so we could easily swap out wall-types and materials, so the dimensions would have to be consistent and work with the plans and concepts we had decided to pursue. We were also making several visual variants for each culture, which meant that we had to try and keep the details of the walls and materials equally interesting for each different type.  

Another big limitation was the fact that we had never before made a scene within our engine like this, so that meant that there were a lot of uncertainties when it came to how much we could push the graphics and where the limits were. Since we were also going to have the artifact system we had to make sure we left enough room for the artifacts and banners without having the environment taking too much attention. This became a trial and error phase to find a good baseline for each throne room.  

![placement.png](https://forumcontent.paradoxplaza.com/public/768110/placement.png "placement.png")


*Early blocking out of the different artifact and furniture slots to be able to see where in the environments we had to make space.*​


To create variation we made sure to have the materials contrast with each other while still fitting together aesthetically so no culture would have throne rooms that all felt exactly the same. This along with changing some architectonic aspects helped the scenes be more distinct. We also worked on adding variation to the grandeur levels, here we wanted the difference to show in the cleanliness and brightness of the environment textures, as well as in the richness of detail in the geometry and amount of decorative props. *(Visual examples of this are shown in the final chapter)*  



![materials.png](https://forumcontent.paradoxplaza.com/public/768208/materials.png "materials.png")



![materials2.png](https://forumcontent.paradoxplaza.com/public/768113/materials2.png "materials2.png")


*Making sure the different materials work together to create a cohesive feeling for each culture, but still looking different from each other. Example images taken from the MENA culture throne rooms.*​


---

#### Lighting and FX​

A lot of our visual tech usually involves considerations for a top-down map, and since we didn’t have much need for full scale 3D room rendering & lighting in the past, we had to do a lot of rethinking to get this to work - we went from previously having 4 lights, moving up to 20 total light sources and expanding the light types available with new ones like area lights - adding sphere & disc area lights. This helps illuminate areas such as room filling bouncing light (seen to great effect in Mediterranean courts) and helps us with light coming in from the windows and other openings.  

![lighting.png](https://forumcontent.paradoxplaza.com/public/768164/lighting.png "lighting.png")


*A cozily lit interior.*​


Another technique we used was animated lights. They move a little, flicker in intensity - very useful for making the fireplace feel like it’s actually on fire and heating up the room a bit. To sell the atmospheric feeling in the room, we added some transparent particles with a little light fade on the sides of the windows and other select places. Even though it isn’t adding to the “real” light of the room, it helps give it that last piece of convincing magic touch. We also used particle systems for effects like the fireplace, candles and torches.  

The concept art helped us find the vision of what we wanted to do. Starting with just the room geometries, we used the color hues and general light level from the concepts to create a lit space that felt cohesive, which we then could tweak and modify until they felt comfortable to look at.  

---

#### Technical hurdles & Bloopers​

One of the hurdles throughout the development of the court scene were tools - a means for developers to manipulate the scene contents more efficiently - edit objects, characters, lights, change their positions, add or remove to have a toolset that allows more quick iteration and direct interaction. It took time to develop a solution that made this part of work less tiresome. One of the downsides of not having readily available tools - you have to do those yourself, and sometimes reinvent a wheel multiple times. But we’re lucky to have an internal tools team that came to rescue us, and it improved the processes immensely.  

We had plenty of funny bugs over the court of development, resolved by now of course.  



![not-a-clan.png](https://forumcontent.paradoxplaza.com/public/768103/not-a-clan.png "not-a-clan.png")


*It's not a cult! — Sometimes visual bugs can be quite fun*  

![bighead_bug.png](https://forumcontent.paradoxplaza.com/public/768101/bighead_bug.png "bighead_bug.png")


*Baby Bighead bug.*  

![nohead_court_bug.png](https://forumcontent.paradoxplaza.com/public/768102/nohead_court_bug.png "nohead_court_bug.png")


*They say you shouldn't lose your head in court, but this is ridiculous*​


---

### Finished courts and courtly variation​

With a working feature, concepts drawn and all the parts built we got to compositing together the scenes. There were a lot of iterative steps working on the textures, lighting and positioning to get all pieces to look their best. The environment team has made a set of three different variations of each cultural court type that each has their own architectural and/or decorative flair and visuals, the scenes differ more in geometry and configuration or the construction materials used. So there may be more windows and ample light, or a fireplace castings its warm light into your court.  

![western_1.png](https://forumcontent.paradoxplaza.com/public/768161/western_1.png "western_1.png")

![western_2.png](https://forumcontent.paradoxplaza.com/public/768162/western_2.png "western_2.png")

![western_3.png](https://forumcontent.paradoxplaza.com/public/768163/western_3.png "western_3.png")


*The western European inspired courts, with stone and plastered walls.*  

![medi_1.png](https://forumcontent.paradoxplaza.com/public/768212/medi_1.png "medi_1.png")

![medi_2.png](https://forumcontent.paradoxplaza.com/public/768213/medi_2.png "medi_2.png")

![medi_3.png](https://forumcontent.paradoxplaza.com/public/768214/medi_3.png "medi_3.png")


*The Mediterranean courts, drawing inspiration from the Roman past as well as the melding of surrounding cultures.*  

![mena_1.png](https://forumcontent.paradoxplaza.com/public/768152/mena_1.png "mena_1.png")

![mena_2.png](https://forumcontent.paradoxplaza.com/public/768151/mena_2.png "mena_2.png")

![mena_3.png](https://forumcontent.paradoxplaza.com/public/768150/mena_3.png "mena_3.png")


*The Middle Eastern courts, drawn on from architecture found in Arabia to Al-Andalus.*  

![indian_1.png](https://forumcontent.paradoxplaza.com/public/768157/indian_1.png "indian_1.png")

![indian_2.png](https://forumcontent.paradoxplaza.com/public/768158/indian_2.png "indian_2.png")

![indian_3.png](https://forumcontent.paradoxplaza.com/public/768159/indian_3.png "indian_3.png")


*The courts of India, greatly varying interiors.*​


Grandeur variants was a further change we added later in the development cycle, which helps give a little extra flavor to the progress of your court's grandeur. Lower court grandeur has less fancy details and furniture extras in the court than the higher level which sports more of them. The surfaces of the room have also been made to look more worn and less taken care of at a lower grandeur level, compared to the high grandeur which look their grandest.  

![Grandeur_low.png](https://forumcontent.paradoxplaza.com/public/767874/Grandeur_low.png "Grandeur_low.png")


*The Pomeranian kings court has seen better days, its painted plastered walls worn and peeling, the floor tiling tired, scraped and just slightly dirty.  
Little decorations or extra furniture have been afforded the kings halls.*  

![Grandeur_high.png](https://forumcontent.paradoxplaza.com/public/767872/Grandeur_high.png "Grandeur_high.png")


*After much investment in upping the level of grandeur, the court's floors are fresh and polished, extra candles and seats added to the court, and a long finely woven rug lines the path up to the throne.*​


---

### Wrapping up​

And with that we’ve come the full way from inception all the way to the finished scenes. We’ve been continuously tweaking and polishing stuff like camera angles, lighting and textures, and we do hope this is a great foundation for a feature that we can grow over time.  

So a big thanks from the court and environment team for checking into this Dev Diary, which will be the last one of the year, but fret not! We will still be bringing you weekly teasers all the way through December to the start of next year.  
These teasers will be smaller in scale and focus on some minor features and things we still want to show off, so keep your eyes out for it next week.

 

Last edited: Nov 30, 2021

<!-- artifact:reactions:start -->
- 130 Like
- 51 Love
- 12 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)**
Role: Senior Environment Artist
Badges: 40
Messages: 221
Reaction score: 2,288

*[Full game-badge icon list of 39 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
