---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1728108/"
forum_thread_id: 1728108
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 163
title: "Dev Diary #163 - Medieval Monuments & Arctic Attire"
dd_date: 2025-02-06
author_handle: PDX-Trinexx
expansion: Khans of the Steppe
patch: Patch 1.16
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2939
inline_image_count: 29
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1728108'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3586.jpg?1739893592
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_394_to_398
    action: preserved_and_flagged
    counts:
      Like: 71
      Love: 36
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_406_to_517
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_518_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3586.jpg?1739893592)
<!-- artifact:thread_banner:end -->

# Dev Diary #163 - Medieval Monuments & Arctic Attire

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Feb 6, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-163-medieval-monuments-arctic-attire.1728108/)
<!-- artifact:thread_metadata:end -->

Hello everyone! We have an unusual dev diary today, in that it’s two dev diaries in one! PiGu, developer of Medieval Monuments, and Aj, developer of Arctic Attire both will give us a brief overview of the content they’re bringing to Crusader Kings III as well as the work that went into creating it.  

Let’s dive right into it with Medieval Monuments.  

---

### Medieval Monuments​

![1739888889247.png](https://forumcontent.paradoxplaza.com/public/1248615/1739888889247.png "1739888889247.png")



Hello everyone!  

I’m Pietro “PiGu” Cavalli, creator of the [Medieval Arts](https://steamcommunity.com/workshop/filedetails/?id=2452585382) mod, and today I have been granted the privilege to welcome you to this developer diary introducing the new Crusader Kings III Content Creator Pack: Medieval Monuments!  

I’ve been playing Paradox games for years, but Medieval Arts was my first modding experience.  
Developed in 2021 to represent the artistic and architectural achievements of the Middle Ages, it has grown and changed many times but it has always kept to its original mission. I have grown with it, learning several skills from scratch with help from the modding community, and falling particularly in love with 3D modeling, which has now become the core of the mod. Today Medieval Arts is an expanding collection of dozens of new monuments, all with their own unique art and flavor, backed by a wonderful and supportive community.  

### The Content Creator Pack​

Before delving into details, I would like to take a moment to explain the vision behind Content Creator Packs. They are meant as a nice way to support modders financially and enhance their skills, while at the same time providing the game with a product of higher quality than a modder would realistically be able to produce on their own free time, that is able to blend seamlessly into the game, and that is maintained in the future directly by Paradox.  

I was first approached this summer to pitch ideas and discuss the different shapes that an “architectural” cosmetic pack might take. While initially proposing a more regional focus, we ended up opting for a broader geographical scope, encompassing the whole map. I then spent a few weeks researching and thinning out options until reaching the final version of Medieval Monuments.  
To be clear about expectations then, this Content Creator Pack includes 20 brand new special buildings, each with their own 3D model, art, flavorful descriptions and modifiers.  

I feel so grateful to the people at Paradox Interactive for offering me this opportunity. I greatly enjoyed working with them, and I learned so much throughout the whole process. We had an honest and clear collaboration where my creative input was greatly respected, and guided when necessary to ensure a proper delivery to a community that has always been kind and supportive of my work.  

I can’t wait to read what you think!  

### The Monuments​

So, let’s have a look at some of the special buildings included in the pack! As previously mentioned there’s 20 of them, but I won’t spoil them all for you here, I’d like you to search the map and find where they are yourselves ; )  

One of the most difficult steps of the creative process was deciding just which monuments to actually portray. The overall “size” of the pack had already been determined previously, so I had to pick 20 out of the entire architectural production of the Middle Ages, a task easier said than done. To help make the best choice, I decided to keep a few priorities in mind:  

First of all I wanted the pack to represent the whole map, to make sure that wherever you may choose to play your next game, you’d always have at least one monument relatively close by. I’ve also tried to favor regions that are lacking unique map objects in the base game. This has granted me the opportunity to be very diverse in the styles, colors and shapes of the monuments, changing with the cultures and environments.  
These range from the frigid lands of the ‘Rus, where you’ll be able to construct the Holy Wisdom of Novgorod, the oldest church in Russia proper and a magnificent example of its unique art, to the humid heat of the Bengal delta, where the great university of Somapura were piously carved.  

![image-01.png](https://forumcontent.paradoxplaza.com/public/1248505/image-01.png "image-01.png")


*[The important church of the Holy Wisdom of Novgorod, one of the oldest in all of the Rus’ lands and inspired by the marvels of Constantinople, covered in winter snow]*  

![image-02.png](https://forumcontent.paradoxplaza.com/public/1248506/image-02.png "image-02.png")


*[Somapura has long been an important center of learning for India, attracting scholars to the fertile delta from afar]*  


Furthermore, another important distinction is temporal in nature. The Middle Ages lasted a thousand years, and even Crusader Kings’ more restricted time span still offers enormous variety in styles and functions and materials. Many monuments greatly changed throughout time, some were expanded, others torn down. I have tried to strike a balance between the centuries, favoring those buildings that belonged to the game’s era so that you may have a chance to build them yourself, but also adding some already constructed at the start, and whenever a monument changed form or function throughout time, I tried to represent a synthesis of its history, even if not always entirely faithful.  
You’ll therefore find buildings varying greatly in period, such as the ancient Umayyad mosque of Damascus, one of the holiest sites for the Abrahamic faiths whose millenarian story has very few equals, or the more “late game” castle and royal residence of Visegrad, which holds a very special place in the history of Central Europe.  

![image-03.png](https://forumcontent.paradoxplaza.com/public/1248507/image-03.png "image-03.png")


*[The Great Mosque of Damascus already has an incredibly fascinating history by CK3’s time]*  

![image-04.png](https://forumcontent.paradoxplaza.com/public/1248508/image-04.png "image-04.png")


*[With its strategic position yet unclaimed, constructing the fortress-palace of Visegrad is sure to give even the lowest of lords a great advantage]*  

In two select cases, because the architectural evolution was so profound, I chose to represent them as multiple tiers. The constructions of these buildings lasted decades, if not centuries, and you’ll be able to follow them with generations of your characters!  
The complex of the Duomo of Florence begins as the modest basilica of Santa Reparata, but with proper time and investment can evolve, over four different tiers, to include the baptistery, the cathedral and finally the masterpiece of the Cupola, the famous dome that heralded the Renaissance and is still triumphant over Florence’s skyline.  

![image-05.png](https://forumcontent.paradoxplaza.com/public/1248509/image-05.png "image-05.png")


![image-06.png](https://forumcontent.paradoxplaza.com/public/1248510/image-06.png "image-06.png")


![image-07.png](https://forumcontent.paradoxplaza.com/public/1248511/image-07.png "image-07.png")


![image-08.png](https://forumcontent.paradoxplaza.com/public/1248512/image-08.png "image-08.png")


*[The complex of the Duomo of Florence has gone from the small early Christian basilica of Santa Reparata to the colossal cathedral we see today, topped by a dome that has become symbol of the Renaissance]*  

Similarly, on the opposite side of the Alps, the lords and monks of Cluny will be able to expand their already considerable power base into the largest of the medieval churches, which unfortunately did not survive to our day.  

![image-09.png](https://forumcontent.paradoxplaza.com/public/1248513/image-09.png "image-09.png")


![image-10.png](https://forumcontent.paradoxplaza.com/public/1248514/image-10.png "image-10.png")


*[The monastery of Cluny was a powerful instrument in the reform of the Church, and the construction of its new Romanesque abbey was a testament to their great wealth and prestige]*  

Finally, I also wanted the monuments to vary in their function and aspect. The study of medieval architecture, especially in the West, has long been focused on cathedrals due to their scale and disproportionate rate of survival, but the world of Crusader Kings III had far more and many great works.  
For example, in Tunisia you will be able to see the basins of Kairouan, a monumental complex to guarantee water to the city no matter the climate, and in Barcelona you will be able to construct the Drassanes, industrial-scale shipyards that allowed the city’s rulers to expand their influence all over the Mediterranean.  

![image-11.png](https://forumcontent.paradoxplaza.com/public/1248515/image-11.png "image-11.png")


*[The basins of Kairouan are an impressive feat of engineering that provided fresh water to the growing city]*  

![image-12.png](https://forumcontent.paradoxplaza.com/public/1248516/image-12.png "image-12.png")


*[The shipyards of Drassanes were fortified to keep out intruders and protect the secrets that allowed the kings of Barcelona to rule the Western Mediterranean]*  

### Research and Realism​


To conclude I would like to spend a few words on creative freedom and historical accuracy. Although of course no comprehensive academic survey of all these diverse monuments exists, I took the time to research each of them individually to the best of my abilities to follow the standards upheld by Paradox and the developers of Crusader Kings and guarantee proper realism in all the models included in the pack.  
Sometimes I was lucky. When designing the Great Kyz Kala, an ancient fortified palatial complex in the oasis of Merv, Central Asia, I was able to draw from ancient representations and modern reconstructions, as well as of course from the ruins we see today, which allowed me to depict it with a fair degree of accuracy.  

![image-13.png](https://forumcontent.paradoxplaza.com/public/1248517/image-13.png "image-13.png")


*[The Great Kyz Kala is today an impressive ruin, but it used to be a magnificent palace blending Arab and Persian architectural traditions]*  

![image-14.png](https://forumcontent.paradoxplaza.com/public/1248518/image-14.png "image-14.png")


*[The ruins of ancient Merv have long been excavated and studied, yielding important information that allowed me to reproduce the Kyz Kala in-game. Furthermore, this silver gilt dish from the State Hermitage Museum, Saint Petersburg, shows a raid to a palace that likely resembled greatly the original appearance of the palace.]*  

Other times I was less lucky, and I had to use my own judgement to fit the monument into the game. I understand this is by no means a perfect choice, but to properly represent cultures and regions with scattered records some compromises had to be struck, and I want to assure you they were all properly thought out. Such was the case for the Jokhang temple - the holiest site in Tibet - or some of the monuments in West Africa.  

### Appreciations​

I would like to properly thank the kind people at Paradox Interactive for trusting me with this project. It was a wonderful experience that helped me improve my work considerably, and I have learned so much from it.  

Finally, I want to take the opportunity to thank you all for the amazing support you have shown me and Medieval Arts through the years, and I’m so excited to share this chapter with you!  

--Pietro  



---

### Arctic Attire​

![1739888912545.png](https://forumcontent.paradoxplaza.com/public/1248616/1739888912545.png "1739888912545.png")



Hey hey!  

I’m Aj, the 3D artist behind the Shogunate mod - and now the official *Arctic Attire* DLC! After months of telling my mod dev teams that “I’m busy” and that “I can’t help with compatch”, I can finally reveal what I’ve been working on (and be able to go back to work on the already compatibility patched mods completely guilt-free).  

*Arctic Attire* takes inspiration from the previous Content Creator Packs by El Tyrannos, but instead of adding just one aesthetic, it adds two aesthetics of slightly smaller scope.  

The Sámi are the indigenous people of northern Scandinavia and Kola. The Sámi garments depicted in Arctic Attire are primarily inspired by clothing of the Kautokeino region as depicted in photographs from the late 1800s, but some pieces take inspiration from other regions and are informed by research of Sámi in the middle ages.  
The Khanty are an indigenous people of Western Siberia living in Khanty-Mansi Autonomous Okrug-Yugra. Their traditional clothing is the primary inspiration for the Ugro-Permian set used across west Siberia.  
Both peoples traditionally live a nomadic lifestyle, herding reindeer and hunting, and have historically been involved in fur trade.  

I will now give a quick tour of the CCP and what is contained inside, with some commentary here and there.  

## The Khanty​


The main male Khanty winter garment is the Malitsa - here are variants for men including belt accessories. These take advantage of the pattern system to vary between reindeer antler, silver, and gold. There is also a version without a belt, not shown here.  

![image-15.png](https://forumcontent.paradoxplaza.com/public/1248609/image-15.png "image-15.png")


*[Khanty men's clothing - commoner and nobility. Also shows dynamic lowered hood gfx when hood headgear isn't worn.]*  

![image-16.png](https://forumcontent.paradoxplaza.com/public/1248608/image-16.png "image-16.png")


*[Khanty men’s clothing - commoner clothing, showcasing knife and belt details, and reference images - Estonian National Museum (Wikimedia Commons), German wood-engraving from 1895, Khanty belt from the British Museum]*  

![image-17.png](https://forumcontent.paradoxplaza.com/public/1248607/image-17.png "image-17.png")


*[Arctic armor posed with reference image from American Museum of Natural History]*  

Ugro-Permian armor is inspired by various Siberian armors, but primarily by Chukchi armor, since it seems to be quite representative of Siberian armor in general, and there wasn’t a lot of good period-appropriate reference material from Western Siberia. Plus, it’s a really cool design. Fun fact - the oldest lamellar in the world was found in Siberia, and it was made of bone. The practice of making bone armor in Siberia continued for a very long time after that, and bone armor will show up on Ugro-Permian commoners. The back shield design is also very old - Scythian armor employed this design as well.  

![image-18.png](https://forumcontent.paradoxplaza.com/public/1248606/image-18.png "image-18.png")


*[Armor work-in-progress images.]*  

![image-19.png](https://forumcontent.paradoxplaza.com/public/1248604/image-19.png "image-19.png")


*[Khanty women's clothing]*  

The main female Khanty winter garment is the Panitsa, or Sakh. The winter Sakh is quite elaborate and is outfitted with a lot of internal and external straps and ties to allow for a more precise fit. I chose to model winter clothing over summer clothing because it's very visually distinct from surrounding clothing styles, and I thought it would fit great with the new adventurer playstyle.  

![image-20.png](https://forumcontent.paradoxplaza.com/public/1248602/image-20.png "image-20.png")


*[Khanty women's clothing variant and headgear.]*  

![image-21.png](https://forumcontent.paradoxplaza.com/public/1248601/image-21.png "image-21.png")


*[Khanty women's clothing work-in-progress images.]*  

## The Sámi​


Most of the assets for *Arctic Attire* were made with cloth simulation in Marvelous Designer, then touched up in Blender, but hard-surface details like the knives or much of the armor were modelled entirely in Blender.  

![image-22.png](https://forumcontent.paradoxplaza.com/public/1248600/image-22.png "image-22.png")


*[Sámi women's clothing and cloaks with reference images - hand-colored photograph from the Nordic Museum, and photo from Heimbeck c.1900]*  

![image-23.png](https://forumcontent.paradoxplaza.com/public/1248599/image-23.png "image-23.png")


*[Sámi men's clothing, work-in-progress sculpt and reference photograph by Marcus Selmer.]*  

![image-24.png](https://forumcontent.paradoxplaza.com/public/1248598/image-24.png "image-24.png")


*[Sámi clothing selection, showcasing the lukha, a work-in-progress sculpt next to finished clothing.]*  

Sámi commoners have a lot of color variety - they have a lot of undyed or only slightly dyed clothing, or clothing made from leather or fishskins - fish hide clothing was actually very widespread in the arctic for a long time, and was produced by a variety of cultures. In Sámi culture, it seems to have been an option for the lower classes, while reindeer fur was reserved for the rich. Unfortunately I didn’t have time to make a bespoke fish skin pattern, so I represented it with a grey-colored leather pattern instead.  

![image-25.png](https://forumcontent.paradoxplaza.com/public/1248597/image-25.png "image-25.png")


*[Sámi commoner clothing and fish-skin clothes reference - from Norsk Folkemuseum, by G. Roche]*  

![image-26.png](https://forumcontent.paradoxplaza.com/public/1248595/image-26.png "image-26.png")


*[Posed Sámi travel coat with reference image.]*  

Sámi travel clothing - a big fur coat, based on some south and east Sámi beaskas.  

![image-27.png](https://forumcontent.paradoxplaza.com/public/1248594/image-27.png "image-27.png")


*[Posed Sámi council portrait, showing a selection of different garments.]*  

It’s been a great time working on this Content Creator Pack with Paradox, and I hope everyone enjoys the new accessories.  

That’s all from me for now. Back to modding, I guess!  

---



That’s all we have for today! A huge thank you goes out to PiGu and Aj both for their work on putting this dev diary together.  

*Medieval Monuments* and *Arctic Attire* both release on February 25th on Steam and Microsoft!

<!-- artifact:reactions:start -->
- 71 Like
- 36 Love
- 9 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
