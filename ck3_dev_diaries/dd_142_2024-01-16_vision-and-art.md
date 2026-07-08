---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1621511/"
forum_thread_id: 1621511
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 142
title: "Dev Diary #142 - Vision and Art"
dd_date: 2024-01-16
author_handle: El Tyranos
expansion: Legacy of Persia
patch: Patch 1.11
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1668
inline_image_count: 9
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1621511'
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
    location: raw_lines_~28_to_142
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_141
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2800.jpg?1705392129
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_144_to_146
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_253_to_257
    action: preserved_and_flagged
    counts:
      Like: 130
      Love: 53
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_265_to_372
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_373_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2800.jpg?1705392129)
<!-- artifact:thread_banner:end -->

# Dev Diary #142 - Vision and Art

<!-- artifact:thread_metadata:start -->
- Thread starter [El Tyranos](https://forum.paradoxplaza.com/forum/members/el-tyranos.519435/)
- Start date [Jan 16, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-142-vision-and-art.1621511/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to this developer diary introducing the Crusader Kings III Content Creator Pack: North African Attire, I’m Pierre “El Tyranos” Azuelos and you might already play with some of my work in the Community Flavor Pack mod.  

I have been playing Crusader Kings franchise since 2012 and mod my favorite games since 2004. I naturally switched to CK modding as soon as 3D characters were announced. Since then, I have made over 260 models for my mod: headgear, clothes, artifacts, royal courts, ships, props, etc. I also broadcasted several video tutorials to help beginner artists to make their way inside the 3D engine.  

Today, Paradox Interactive gives me the opportunity and immense privilege to release an official cosmetic pack for our favorite game, so let’s jump into it in detail!  

---

## Introducing the Content Creator Pack​

The Content Creator Pack is an initiative that started at PDXCON 2022 when I submitted the idea directly to the Game Director for CKIII. The decision to make “North African Attire” came after a process where I pitched different concepts for a Content Creator Pack, developing the philosophy, expectations, interests, risks and scope for 4 options. We then had a meeting diving deeper into what a cultural clothing pack would look like, this time with regional suggestions, and North Africa stood out from the rest. I documented for a few weeks until the project was finally ready to enter production.  

The key objective of the project was to create something that added value to the game compared to a mod and blend in seamlessly with the rest of the content. Over the last 4 years, Community Flavor Pack received about 6 original clothings, the remaining ones are vanilla model retextures. Over the 260-ish models from the mod, clothing only represents a dozen. Why? The time and energy investments are barely worth it when you’re doing this for fun and for free. For example, I submitted 8 turbans in this Content Creator Pack that I never did before, because of their complexity. I dedicated more than 2 weeks just to manage to make the first one, see illustration below.  

![afr_devdiary_0.jpg](https://forumcontent.paradoxplaza.com/public/1063964/afr_devdiary_0.jpg "afr_devdiary_0.jpg")


[From left to right: first trial, understanding the workflow, final sculpt of one of the models]  

The Content Creator Pack, which becomes officially part of Crusader Kings III, comes with a higher quality standard: more attention to visuals, better optimization, models have all their blendshapes, there is a lot more time spent per asset. Paradox provides Quality Assurance and will offer official support for the content as well.  

Why am I saying this? Paradox Interactive trusted me with an ambitious project when I submitted something I still had to prove I could do. Our collaboration was honest and benevolent, my creativity was respected and I tried to do my best in return, they guided me to achieve better visuals all while supporting my initiatives. I've done my best to push the sliders as far as possible, with the weight of not disappointing the community that has always supported my work and within the inherent limit to a commercial project.  


## Character Art​

The first thing to note is that documentation is woefully lacking, there is, to my knowledge, no surviving artifact but a pair of 11th century shoes. Another terrible fact is that medieval art shows almost no women and no other Berber than Andalusians… used in Fate of Iberia’s documentation!  

Fortunately, Berber culture is very unique as it kept its own decorations and fashions all the way up from high antiquity all while being permeable to other cultures it met. This is the concept of “Berber permanence” (Gabriel Camps, 1987) and it helped a lot in the outlining of this DLC. Some simple examples: the traditional woman dress is a Greek peplum, the filigree silver work is Phoenician, the enamel techniques are Roman. Some geometric symbols can even be traced up to the Neolithic! There is obviously a deeper blending after Islamic conquests but no replacement, it is even considered that the Islamic art built upon the Berber abstracted symbols in its early stages.  

What you will see below is only an abstract of the content pack, not everything is presented. As a matter of numbers, the production took 6 months - on top of my work and family life - and there are 33 new models added to the game.  

I have done my best to represent an authentic version of the Berbers in the Middle Ages, with obvious biases due to the lack of sources. I hope you'll be able to get past my misinterpretations.  

![afr_devdiary_1.jpg](https://forumcontent.paradoxplaza.com/public/1063965/afr_devdiary_1.jpg "afr_devdiary_1.jpg")


[Photos: Berber Arts Museum of Marrakech; “Berber memories: women and jewelry in Morocco”, Michel Draguet, 2020.]  

This is a typical North African attire from the Atlas: the loubane amber necklace is prominent and the massive silver fibulas are holding the elhaf together, striking the eye with beautiful abstract engravings. The elhaf is a Dorian-style peplum and the appearance of this type of fibula dates back to the Bronze Age in the Maghreb (Camps-Fabrer, 1964). The tamizart cloak is stripped, similar to a 4-6th century BC artwork found in the Tumulus of Djorf Torba in Algeria (illustration).  


![afr_devdiary_2.jpg](https://forumcontent.paradoxplaza.com/public/1063966/afr_devdiary_2.jpg "afr_devdiary_2.jpg")


[Photos by Michel Draguet, 2020; Illustration by Emile Galois, 1946]  

At the royalty tier, the look is largely different. She wears a shirt under her elhaf, the fibulas are featuring enamel and complex silver filigree, representative of the Souss valley. The circlet is a talgamout with three hinged silver plates and glass cabochons, representative of the Tagmout tribe located in the central anti-atlas. Anti-atlas has always been a refuge against persecutions. It’s considered as a conservatory of the Berber culture as the weather is harsh and access is difficult, allowing vernacular forms of dress and ornamentation to survive. The top right image is a high-definition sculpture I made from the reference.  


![afr_devdiary_3.jpg](https://forumcontent.paradoxplaza.com/public/1063967/afr_devdiary_3.jpg "afr_devdiary_3.jpg")


[Photos: Michel Draguet, 2020]  

Imperial headwear (left) is a Taounza, again from the Souss valley while high nobility’s coin diadem is from Dadès valley in the High Atlas. As you can see the styles are completely different. Actually, there are so many styles with their own uniqueness and beauty that it was a nightmare to decide which one should make it into the project and at what tier.  


![afr_devdiary_4.jpg](https://forumcontent.paradoxplaza.com/public/1063968/afr_devdiary_4.jpg "afr_devdiary_4.jpg")



Knights outfit was way more straight forward. It is based on a wall painting of muslim knights during the conquest of Majorca, created around 1285 and conserved in Barcelona. The sword is a Tuareg takouba. Current learned opinion is that these swords are a distinct and entirely indigenous African type, although speculations of possible influence from Spain via the Almoravides in the 11th Century (Nicolaisen, 1997).  

![afr_devdiary_5.jpg](https://forumcontent.paradoxplaza.com/public/1063969/afr_devdiary_5.jpg "afr_devdiary_5.jpg")


[Illustrations: Arab bearded scribe. He wears a turban tied around a conical cap. Cappella Palatina, Palermo, Sicily (1131-1140) and Drawing of Man with Lamp, Fustat, Fatimid Egypt, 11th Century. Keir Collection No. 75781]  

Commoners wear a pointy hat with a tassel, held in place by a turban. Conical hats are widespread across North Africa, as seen on those paintings.  


![afr_devdiary_6.jpg](https://forumcontent.paradoxplaza.com/public/1063970/afr_devdiary_6.jpg "afr_devdiary_6.jpg")


[Illustrations: Spanish Codices, 11th and 12th century; Men-at-Arms N°348, Osprey editions, 2001; “Costumes of Morocco”, Jean Besancenot, 1990]  

Low nobles wear two kinds of wicker hats called tarazas. One is Algerian and the other one featured here is moroccan. The hat is carried above the turban. This is a unisex fashion, and the oldest representations are in Andalusian art (Weiditz, 1530). The tunic is a jillaba, a long, loose-fitting unisex outer robe with full sleeves. Almost all djellabas of both styles (men or women) include a baggy hood called a qob. The hood has a different color and the cut is one of a city dweller, the most widespread.  


![afr_devdiary_7.jpg](https://forumcontent.paradoxplaza.com/public/1063971/afr_devdiary_7.jpg "afr_devdiary_7.jpg")


[Illustrations: Sala de Los Reyes, Alhambra, 14th century]  

This sultan carries a Tuareg tagelmust or litham with a golden plate showing his wealth, the litham became a distinctive sign of the Almoravids, meaning its wearer should be treated with honor and respect.  
He also wears a kaftan based on the surviving marlota of Boabdil (Nasrid Dynasty). Interestingly, the modern “style of Rabat” kaftan looks a lot like it. In Morocco, the kaftan is a very old tradition, deeply rooted in the country's clothing habits. It is an unisex clothing that soon became a symbol of power and wealth among the moors, worn by royals, even up to the queen Isabella as she conquered Granada in 1492. However, the evolution and adaptation as a ceremonial dress for women has made it a very different garment from the Persian and Ottoman ones.  


![afr_devdiary_8.jpg](https://forumcontent.paradoxplaza.com/public/1063972/afr_devdiary_8.jpg "afr_devdiary_8.jpg")



The pack finally includes a new feature (special_genes) which allows headgears to deform when a character has a long beard. It allows for models to get out of the way, reduces the amount of clipping and gives them a more organic look.  

---

While I can only invite you to read and learn about this extremely rich culture, I hope you enjoy looking at characters’ garments during your next playthrough in North Africa.  

Finally, I’d like to thank Paradox Interactive for the trust they put in this project as well as for the opportunity to bring my work to the next level. I extend all my gratitude to the members of the community, your support over the last few years helped me to continue working and honing my skills.  

--Pierre

<!-- artifact:reactions:start -->
- 130 Like
- 53 Love
- 14 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [El Tyranos](https://forum.paradoxplaza.com/forum/members/el-tyranos.519435/)**
Role: 3D bot
Badges: 139
Messages: 304
Reaction score: 2,225

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
