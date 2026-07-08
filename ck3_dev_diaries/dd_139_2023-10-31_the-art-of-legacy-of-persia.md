---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1605823/"
forum_thread_id: 1605823
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 139
title: "Dev Diary #139 - The Art of Legacy of Persia"
dd_date: 2023-10-31
author_handle: Gertax
expansion: Legacy of Persia
patch: Patch 1.11
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2319
inline_image_count: 20
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1605823'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2651.jpg?1698743191
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_337_to_341
    action: preserved_and_flagged
    counts:
      Like: 94
      Love: 86
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_349_to_421
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_422_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2651.jpg?1698743191)
<!-- artifact:thread_banner:end -->

# Dev Diary #139 - The Art of Legacy of Persia

<!-- artifact:thread_metadata:start -->
- Thread starter [Gertax](https://forum.paradoxplaza.com/forum/members/gertax.1709175/)
- Start date [Oct 31, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-139-the-art-of-legacy-of-persia.1605823/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to the Developer Diary focusing on 3D Art for Crusader Kings III: Legacy of Persia. I’m Lucas Ribeiro, the Art Lead for the project. Before we move on to looking at some of the amazing 3D artwork the team has created for the Flavor Pack, I would like to give an overview of our decision-making process.  

When creating art for Legacy of Persia, we were looking for ways to represent the resurgence of the Iranian identity in the Iranian Intermezzo after two centuries of intermingling and struggling with the Arab and Turkic peoples. This meant we needed to give Persian characters their own new look and at the same time reinforce the visual identities of the Turks and Arabs.  

We focused on 8th - 11th century references, basing our work on the art produced by Iranians that were **inspired** by Sassanian and-or Zoroastrian sources while at the same time not looking anachronistic. The clothes we see in Legacy of Persia should be as close as possible to what we might see a 10th century Samanid Amir wear.  

To this end we created loads of new artifacts, buildings, military units, beards, hairstyles, clothes and of course **HATS** aimed mostly at the Iranian culture, while creating a few new key recognizable extra assets for the Turkic and Arab cultures.  

Now, onto the art!  


---

## Environment Art​


*Stina Arvidsson Rådestig was our main 3D Environment Artist for the project, and she’ll give us some nice insights into the process of creating Monuments, Holdings and Artifacts for Legacy of Persia*  

We had the honor of researching the artifacts, ruined structures, natural wonders, and special monuments of ancient Persia and providing a list of candidates to serve as the basis for court artifacts and special buildings for this flavor pack. Given the rich history of this region, and the large body of interesting and beautiful monuments; geographical variety; and the surviving works of art from this time period, it was a very difficult task to narrow the list down to the ones we would want to make it into the game.  

Our aim was to achieve variety - both from an aesthetic and game mechanical perspective - in order to create a balanced gameplay experience.  


**Court Artifacts**  

Court artifacts are amazing to work on, because they are based on real world historical artifacts - special items, works of art, or trinkets that have survived through the ages, impressing historians and laymen alike either with backstory, craftsmanship, or beauty. (Or, as in the case with the complaint letter to Ea-Nasir - just for being plain silly!). As 3D artists, apart from the technical constraints set by our game engine and triangle count, there are few things limiting our freedom to portray these beautiful and interesting artifacts as accurately as possible. We strive to do these items justice - while still keeping the assets practical and optimized - , so we make sure to gather a large body of verified references, including photographs, illustrations, and descriptive texts. We want the players to feel as if they are looking at the real thing - not just a bleak, filtered interpretation - that’s why our approach is to capture the form, the details, the ornamental patterns as accurately as possible, only omitting tiny details or making changes if necessary for practical reasons.  

Typically, we sculpt ornamental detail in Zbrush using either curve brushes, traditional sculpting brushes, or modeling tools. Sometimes taking a node-based approach in Substance Designer, or using image-based techniques. Each method has its own pros and cons - sometimes we even combine multiple methods for one asset.  



![image-01.png](https://forumcontent.paradoxplaza.com/public/1027351/image-01.png "image-01.png")


*[The image on the left shows a photograph of the Oxus Treasure Bracelet artifact. The middle and right images show the finalized 3D asset.]*  


![image-02.jpg](https://forumcontent.paradoxplaza.com/public/1027352/image-02.jpg "image-02.jpg")


*[Photograph of the Il-Khanid brass casket artifact]*  



![image-03.png](https://forumcontent.paradoxplaza.com/public/1027353/image-03.png "image-03.png")


*[Wireframe and final 3D asset]*  



![image-04.jpg](https://forumcontent.paradoxplaza.com/public/1027354/image-04.jpg "image-04.jpg")


*[A few other court artifacts that can be found throughout Persia: A Sassanian Sword, an Incense Burner Cat Sculpture, and an ancient drinking vessel.]*  



**Special Buildings**  

Making the special buildings present an entirely different challenge compared to court artifacts. Monuments are very small, and they use a premade texture atlas. Each time a new flavor pack is made, the texture atlas is changed to better fit with the building materials, and color scheme of the region. Details are minimalistic - but it works really well in game! This atlas is made using a texture-making software called Substance Designer. The challenge is to create a symbolic representation of the real world counterpart - yet to stay true to historical references! Much like with court artifacts, we look closely at references to find the answer to questions like: What did the entrance gate of this castle really look like? Did this fortress have a moat? What is the plan layout of this temple? And from there, we work to exaggerate the most visually distinct parts, whereas more redundant, less noteable details may be toned down.  
Another thing that we like to do is look for signs of old ruins and structures, and try to restore them in our models.  

Take a look at the comparisons below, to see the differences between some real-world locations and our monuments:  

![image-05.png](https://forumcontent.paradoxplaza.com/public/1027357/image-05.png "image-05.png")


*[Real-world Soltaniyeh Monument, and our interpretation of it in-game]*  


![image-06.png](https://forumcontent.paradoxplaza.com/public/1027358/image-06.png "image-06.png")


*[Current days Ark of Bukhara and our interpretation]*  

![image-07.jpg](https://forumcontent.paradoxplaza.com/public/1027379/image-07.jpg "image-07.jpg")


*[Ctesiphon ruins and our interpretation of what it might’ve looked like if restored.]*  

![image-08.jpg](https://forumcontent.paradoxplaza.com/public/1027361/image-08.jpg "image-08.jpg")


*[The texture atlas used when texturing all holding models and Special Buildings in Legacy of Persia.]*  


We like to take a modular approach whenever possible - this saves a lot of time! It means that we will make simple structures like a piece of a wall, a tower, a door, for example and model and texture them to completion, only to duplicate them later. Sometimes, we make use of symmetry and mirroring functions within my 3D software (usually Autodesk Maya), to model only a quarter of a model, and then instantly turn it into a whole model.  



**Holdings**  

Holdings are the fortresses, walls, temples, and cities of Crusader Kings III. Their visual design follows a specific formula and is usually based not on any one single existing building, but rather the general architectural style of the era.  

Zoroastrian temples are especially unique as they have smoke billowing out of them to represent the holy fires they might’ve had going inside.  

![image-09.jpg](https://forumcontent.paradoxplaza.com/public/1027360/image-09.jpg "image-09.jpg")





**Natural Wonders**  

We also had the chance to include a few unique natural wonders of the region. Such as the seasonally magenta Maharloo Lake, the breathtaking Rainbow Mountains and the sacred Mount Damavand, steeped in myth and legend.  

![image-10.jpg](https://forumcontent.paradoxplaza.com/public/1027362/image-10.jpg "image-10.jpg")




---

## Character Art​


*Let’s look through some of the many new assets that the team has created to make this region even more flavorful, with Elena Zenko as the main character artist on the project*  

The first step of making character assets is to collect references and gather information of how these assets should look like. And it was an extremely tricky though fun part of the FP3.  
Not that many historical depictions of how people dressed have survived until this day. That influenced us to be even more thorough in our attempt to be as accurate as possible. (Sharbush) Hats off to our Principal Character Artist Nils for helping out with research and concept work on these. It was definitely not easy to collect, contextualize and ascertain the validity and quality of our references.  

As inspiration we were using different sources like The Book of Fixed Stars, and plenty of surviving murals from different parts of ancient Persia, that nowadays are Iran, Tajikistan, Syria, Uzbekistan, Kazakhstan, Turkmenistan, Afghanistan, and even China. Sometimes we had just written descriptions from Encyclopaedia Iranica. We used these many sources as evidence to some of the new assets that would otherwise look like they were straight out of high fantasy!  

Let’s take a look at the new clothes:  

![image-11.png](https://forumcontent.paradoxplaza.com/public/1027363/image-11.png "image-11.png")



The images show the process of creating the asset from reference to concept to finished asset in the game. As a main reference we used wall paintings from one of the Ghaznavid palaces at Laškarī Bāzār in central Afghanistan. The men are wearing qabā, a mid calf-length coat that opens up in front with one side of the coat hanging on the chest. On the sleeves you can see ṭirāz in the form of armbands - those are Persian embroidery that are inscribed in the coat. One cool feature of the asset is many belts, and a humble artist cannot resist making them for the game. It brought some pain later on with testing animations, but we sacrifice ourselves for beautiful clothes.  

![image-12.png](https://forumcontent.paradoxplaza.com/public/1027364/image-12.png "image-12.png")



Another cool asset that is primarily based on kitāb suwar al-kawākib or The Book of Fixed Stars. The illustrations there are quite unique, and we had some moments of concern if these clothes existed in real life and how we recreate something like this in the game. Eventually, the temptation to make unique and sophisticated cloth was higher than common sense and time restriction, so we ended up making this. The asset contains the outer rich styled robe khaftān, that is made from silver or gold brocade or silk. The most interesting part of the asset is elaborately cut sleeves and the skirt decorated with ṭirāz that you may see present on the illustrations from The Book of Fixed Stars.  

![image-13.png](https://forumcontent.paradoxplaza.com/public/1027365/image-13.png "image-13.png")



This picture represents male and female cloth assets that are based on the real Seljuk robe of the 11-12th century. Another reference was a 10th century bowl with a Figure and Bird. Both of these assets have belts with ornamental discs that we’ve found present on the pictures of painted terracotta sarcophagus cover in the Monastery in Fondukistan.  

![image-14.png](https://forumcontent.paradoxplaza.com/public/1027367/image-14.png "image-14.png")



These pictures represent a female cloth asset based on stucco relief from the book Negar-e Zan that shows a, presumably, female attendant at the court of Kalhana. We also used a reference of the Seljuq Standing Figure that might depict a sultan or one of his vassals. Interestingly, female attendants at the court were supposed to wear men’s dress, which sometimes makes it hard to tell who is in the picture. As for the belt we returned back to The Book of Fixed Stars and found some interesting rectangular belt fittings that we sure added in our collection of Absolutely Historically Accurate belts.  



**Headgears**  

![image-15.png](https://forumcontent.paradoxplaza.com/public/1027370/image-15.png "image-15.png")



It’s a small, flattened cap with a diadem and a bow that is based on our favorite Book of Fixed Stars. This time we spent a significant amount of time making concepts and contemplating if the headgear had a cap or if it was some sort of the strap holding the diadem and pushing the hair.  

![image-16.png](https://forumcontent.paradoxplaza.com/public/1027371/image-16.png "image-16.png")



Another asset that we made was a Seljuk stiff cap edged with fur, with a metal plate over the forehead. Turkic characters of duke rank will be seen wearing this very recognizable asset!  

![image-17.png](https://forumcontent.paradoxplaza.com/public/1027372/image-17.png "image-17.png")



And here are new Persian crowns that sometimes seem out of fantasy, though they are indeed based on late Sasanian coins and 7-8th century murals. The most common type of royal headgear we found from the period was the winged crown. Additionally, the shape of the wings on the male crown resembles hands that we found fascinating. The depiction of these wings was found on the wall paintings of the Afrasiab murals, a rare example of Sogdian art.  

![image-18.png](https://forumcontent.paradoxplaza.com/public/1027373/image-18.png "image-18.png")



Here is another set of the new Imperial crowns that were based on our beloved Book of Fixed Stars. You can see another version of the winged crown, though this time the wings are bigger as fits an imperial figure. A well-known fact - with the big power comes big wings (and strong neck).  


![image-19.jpg](https://forumcontent.paradoxplaza.com/public/1027374/image-19.jpg "image-19.jpg")


![image-20.jpg](https://forumcontent.paradoxplaza.com/public/1027375/image-20.jpg "image-20.jpg")


We thankfully still have many surviving patterns on fabrics from the time period. Common motifs were mythological Iranian creatures such as the Simurgh or the Huma. Pheasants and ducks were also very popular imagery.  

Diving deep into the aesthetics of this twilight period in Iran was incredibly rewarding. We discovered beautiful imagery and pieces of craftsmanship that we were honored to interpret and combine into these 3D assets that gave Persia and its inhabitants their own unique look and feel.

<!-- artifact:reactions:start -->
- 94 Like
- 86 Love
- 5 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Gertax](https://forum.paradoxplaza.com/forum/members/gertax.1709175/)**
Role: Corporal
Badges: 10
Messages: 34
Reaction score: 1,184

*[Full game-badge icon list of 10 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
