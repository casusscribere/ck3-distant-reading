---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1624620/"
forum_thread_id: 1624620
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 145
title: "Dev Diary #145 - Legends & Legitimacy"
dd_date: 2024-02-19
author_handle: PDX-Trinexx
expansion: Legends of the Dead
patch: Patch 1.12
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3966
inline_image_count: 31
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1624620'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2856.jpg?1708434011
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_449_to_453
    action: preserved_and_flagged
    counts:
      Like: 114
      Love: 113
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_461_to_520
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_521_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2856.jpg?1708434011)
<!-- artifact:thread_banner:end -->

# Dev Diary #145 - Legends & Legitimacy

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Feb 19, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-145-legends-legitimacy.1624620/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to the first of our feature breakdown Development Diaries! I'm a game designer on Crusader Kings 3 and I surely hope that you have a nice cup of coffee next to you and the will to read for a while, as today's entry is on the chonkier side! Today we will talk about Legends, Legitimacy, and the Art behind *Legends of the Dead*.  

So, let's get right into it! Legends!  


### Legends​


We've already covered the original reasoning behind legends in [our previous Vision Dev Diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-144-legends-and-lesions.1624034/), but to go over it quickly (and in a very oversimplified manner) again: medieval people really loved legends, and above all of them, rulers *really* loved legends. One of the first times we ever hear of King Arthur is in Geoffrey of Monmouth's *Historia Regum Britanniae*, which is, as the name says, a list of the kings of Britain.  

The Plantagenet kings of England quickly latched onto the figure of Arthur as a legitimizing tool. This was partly a reaction to the German and French (specially the Capetians), that exalted their connection to Charlemagne in this "race for historic-mythical sponsorship" as the medieval historian Jacques Le Goff writes. All across Europe, medieval monarchs scrambled to find an older, more heroic figure, that would secure the throne for their dynasty.  

And now, so can you!  

Legends have a Type and Quality level. Because no legend can be entirely mundane, they start at Famed, then Illustrious and finally Mythical, each of them giving out progressively more powerful rewards; you can increase the quality of the legend when it has spread far enough, including having to extend outside of your realm.  

![image-01.png](https://forumcontent.paradoxplaza.com/public/1074761/image-01.png "image-01.png")


*[Image: Rewards for completing a Famed Legitimizing legend]*  

![image-02.png](https://forumcontent.paradoxplaza.com/public/1074762/image-02.png "image-02.png")


*[Image: Rewards for completing a Mythical Legitimizing legend]*  

As for the Types, Legends can be Heroic, Holy or Legitimizing.  

Heroic legends give additional Prestige modifiers and other thematic rewards that reflect your heroism, like the decision of launching a Legendary Adventure, or Demand Local Submission.  

![image-03.png](https://forumcontent.paradoxplaza.com/public/1074763/image-03.png "image-03.png")


*[Image showing one of the special Heroic Legend rewards]*  

Holy legends are focused around Piety and are greatly inspired by medieval hagiographies, specifically the Golden Legend, allowing the Protagonist to even gain the Saint at the highest levels, if the appropriate Dynasty Perk has been unlocked.  

![image-04.png](https://forumcontent.paradoxplaza.com/public/1074764/image-04.png "image-04.png")


*[Image showing one of the Dynasty Perks for the new Heroic Bloodline Dynasty Legacy, focused on Legends]*  

Lastly, Legitimizing legends will give you double the amount of Legitimacy and allow you to get new, powerful claims to expand your realm, as shown in the rewards above.  

You also can, of course, choose the Legend Protagonist, the author of these heroic deeds. Among the possible options are your relatives (even if dead) and choosing someone other than yourself will also grant you extra Legitimacy, so you can dedicate your legend to your dragon-hunting grandpa.  

But how can you start a legend? Well, every legend is born from a Legend Seed. Some characters start with historical seeds on game start, like the Capetians *Heirs of Charlegmane*, or the *Hunnic Heritage*, available for Nomadic cultures that claim to be descended from Attila himself.  

![image-05.png](https://forumcontent.paradoxplaza.com/public/1074765/image-05.png "image-05.png")


*[Image: The Heirs of Charlemagne legend seed]*  

![image-06.png](https://forumcontent.paradoxplaza.com/public/1074766/image-06.png "image-06.png")


*[Image: Hunnic Heritage legend seed]*  

However, this is not the only way to get legend seeds, as winning important wars, hunting a legendary animal, and taking major decisions are also some of the most common ways of getting one.  

Even hiring a capable Court Chronicler and paying them enough gold can manage to… make an ancient document appear mentioning your long-lasting dynasty.  

![image-07.png](https://forumcontent.paradoxplaza.com/public/1074767/image-07.png "image-07.png")


*[Image: Mending the Great Schism will grant you a Holy Legend seed]*  

But supporting a legend is not only beneficial for its owner, as becoming a promoter (a much cheaper alternative) will also grant you special bonuses, as well as helping the legend spread on your lands - the higher quality the legend, the bigger the rewards for you too.  

![image-08.png](https://forumcontent.paradoxplaza.com/public/1074768/image-08.png "image-08.png")


*[Image: Promoter bonuses]*  

While you spread your legend, you'll get flavor events of both people reacting to your legend in different manners along with your Chronicler and courtiers fervently asking you to recount the story *just once more, my liege*, making it possible to introduce… ehem… minor alterations to the text.  

Use the new Court Position Tasks to make your Musicians and Poets sing your legend to make it easier to spread inside your realm, or get them to try and convince supporters abroad!  

![image-09.png](https://forumcontent.paradoxplaza.com/public/1074769/image-09.png "image-09.png")


*[Image: Court Musician performing the new Extol Domestic Legend task]*  

Turn your legend into an artifact, celebrate a feast in its honor, or simply enjoy the control boosts from having it spread over people that now believe you a hero. Legends were a core part of the medieval world, a powerful tool to root your power in something greater than you.  

*"Lineage and geste are synonymous, as the epic cycle constitutes itself according to a pattern of affiliation between families of heroes and families of poems."* (R. Howard Bloch, 1983: 94).  

![image-10.png](https://forumcontent.paradoxplaza.com/public/1074770/image-10.png "image-10.png")


*[And here it was written, Paradox Forum, 20th of February, 2024 AD.]*  


### Legitimacy​

For Legitimacy our aim was to put together a measurement of different systems that already existed in the game, but were not directly connected to each other: Short Reign penalties, Popular Opinion, Vassalization and Marriage acceptance, etc. The game was already trying to reflect how legitimate of a ruler you were, but was trying to do so with Prestige and Renown in non consistent ways. Prestige is a reflection of the social influence of the character, not an indication of them being the "right" person to the throne - you can be a highly prestigious king of the Capetian dynasty, but should you be the emperor of Byzantium?  

Legitimacy and its effects scale with title tier. It's not the same being a level 5 Emperor - where everyone expects you to be the right person for the job - than a level 5 Duke, where everyone is impressed with your overachieving.  

![image-11.png](https://forumcontent.paradoxplaza.com/public/1074771/image-11.png "image-11.png")

![image-12.png](https://forumcontent.paradoxplaza.com/public/1074772/image-12.png "image-12.png")


*[Images: Count with Legitimacy level 0 and 5]*  

![image-13.png](https://forumcontent.paradoxplaza.com/public/1074773/image-13.png "image-13.png")

![image-14.png](https://forumcontent.paradoxplaza.com/public/1074774/image-14.png "image-14.png")


*[Images: Emperor with Legitimacy level 0 and 5]*  

It's also easier to go up and down levels the lower your tier, as it's harder to convince people once they've formed an idea of who their king is.  

Legitimacy also scales with the in the game era, and the levels are smaller in the Tribal and Early Medieval eras.  

Legitimacy is calculated through a series of factors, mainly attached to who you are in relation to your title: the level of splendor of your dynasty, how long you've been on the throne, who your parents were (are you the child of kings or just random lowborns?), your traits, being a bastard, etc. When you die, a part of your legitimacy will be passed down to your heir, but they will get a calculation of their own based on who they are - it's not the same to have your firstborn inherit than a third cousin.  

![image-15.png](https://forumcontent.paradoxplaza.com/public/1074775/image-15.png "image-15.png")


*[Image: The Sayyid traits increases your Legitimacy]*  

Legitimacy can be gained through various means that will reassure the public opinion that you have the right to be in the throne: legends, for one, are one of the main ways to gain it. Holding activities, holding court, and doing what's expected of a ruler will also help increase it, as well as winning wars - but this will also be relative, as it's not the same to win a war against a Duke as an Emperor than be the Duke beating up the Emperor.  

Legitimacy can also be lost. Losing battles, especially to factions (and especially to Claimant factions) will make you look pretty bad, or even managing to have a Peasant Rebellion appear will signify that you're not taking good care of your subjects. Rulers were also blamed for plagues, as the representatives of God on earth, so allowing them to hit your capital will also make you appear less legitimate in the eyes of your vassals. Disinheriting or forcing kids to take the vows also exposes a ruler that doesn't take good care of their dynasty and will also make you lose Legitimacy.  

![image-16.png](https://forumcontent.paradoxplaza.com/public/1074776/image-16.png "image-16.png")


*[Image: Disinheriting your heir will cost you more Legitimacy]*  

Your vassals, of course, have Expectations of you. This is calculated based on your tier, era, and how long your family has ruled over theirs, besides their opinion and relationship to you. Not meeting your vassal expectations will make them discontent and more likely to join factions against you.  

![image-17.png](https://forumcontent.paradoxplaza.com/public/1074777/image-17.png "image-17.png")


*[Image: King with Legitimacy level 3]*  

As we've already seen in the tooltips, Legitimacy levels affect all sorts of things in the game: Casus Belli cost, Marriage and Alliance acceptance, Faction formation and even the counties necessary to create a title.  

![image-18.png](https://forumcontent.paradoxplaza.com/public/1074779/image-18.png "image-18.png")


*[Image: The art for the new Legitimacy Dynasty Legacy]*  

---

### The Lady of Shalott​

Hello! My name is Pavel Golovii and I am a senior illustrator at Paradox. I have been working on a number of illustrations for this expansion and today I am going to talk about processes behind the scenes of illustration work. As an example, I will take arguably the most challenging kind of illustrations we have in game - the loading screen. This illustration is the player's first introduction to the expansion and bears the responsibility of giving them a feeling of anticipation.  


### Ideation​

Every picture starts with an idea. With the introduction of epidemics in “Legends of the Dead” I regarded the opportunity to feature a physician, a healer as very fresh and appealing. It would be a positive, reassuring subject matter when compared to the intrigue, war and power struggles that dominate the themes of our other illustrations. Truth be told, a lot of inspiration was coming from “The Physician” movie and some orientalist’s paintings.  

![image-19.png](https://forumcontent.paradoxplaza.com/public/1074778/image-19.png "image-19.png")


*[Image: A couple of the initial ideas featuring an eastern theme with a physician.]*  

Another idea that was suggested and actively supported by game designers is the legend of [The Lady of Shalott](https://en.wikipedia.org/wiki/The_Lady_of_Shalott). This medieval themed story is a beautiful blend of tropes for both “legend” and “death” and provides a very suitable metaphor for the new expansion. At the same time this theme was depicted in many paintings by a number of renowned artists. It was especially popular in the Pre-Raphaelite era with a series of paintings by John Waterhouse featuring the legend. This potentially added to the challenge of making it relatively unique and unwittingly could bring up an unfavorable comparison with a master’s work. Somewhat reluctantly I took a stab at it and did some sketches.  

![image-20.png](https://forumcontent.paradoxplaza.com/public/1074780/image-20.png "image-20.png")


*[Image: Composition sketches for The Lady of Shalott theme.]*  

After discussing all of the above ideas with the team and the art director we decided to further develop the last (bottom one) variant as the most original and also well-fitting to present the *Legends of the Dead* DLC. Yet the physician theme was not trashed and made its way to become one of the story event illustrations. The composition of the chosen variant underwent a few changes afterwards following art-director’s feedback. We decided to get rid of the straight top down view in favor of a more traditional perspective and closer look at the character yet retaining dynamic shapes of the water weeds and flowing dress.  

![image-21.jpg](https://forumcontent.paradoxplaza.com/public/1074781/image-21.jpg "image-21.jpg")


*[Image: Final composition that was approved.]*  

In many ways decisions made at this early stage affect the overall success of the final image. A good outcome is not guaranteed of course, but if properly made it creates a firm foundation for further work. On the contrary, skipping crucial steps assuming these can be tackled at a later stage can turn the painting process into a struggle, even though digital medium allows to change things easily at any moment.  

### Color Explorations​

I rarely do color explorations before final shapes and values for the composition are established. But this time I started experimenting with colors a bit earlier using AI which gave me an extra bit of flexibility and an abundance of variations. A locally installed Stable Diffusion with Control Net was used for generating rough color thumbnails based on my composition sketches. Black & white composition images were used to restrict image generation to shapes defined in them. Another color image that just contained the color palette of my preference was fed to Control net to roughly define color to be applied. Text prompt was of little importance and I kept it very simple and basic. The results are pretty far from highly detailed crisp digital pictures that are usually expected from AI generated images. They are quite inconsistent and rough and have a great deal of randomness. But this is actually what I appreciate in these. I like that level of abstraction. Accidental interpretations of my composition ideas by AI provided me with extra inspiration. Not only the colors, but also values, shapes, edges and textures that start to loom in these thumbnails can give a new hint regarding a certain aspect of the artwork.  

![image-22.png](https://forumcontent.paradoxplaza.com/public/1074782/image-22.png "image-22.png")


*[Image: There was a sheer number of AI interpretations of my composition sketches.]*  

The major caveat with these AI generations is that you can do so many of them in a relatively short amount of time that you need to be quite decisive to stop that dopamine trap and move on. Otherwise they just pile up as photos on a mobile phone that you never return to.  

Now the chosen AI generated color samples need to be applied to composition with proper distribution of size, shapes and accent placement (here AI is not of much help, not yet at least).  

![image-23.png](https://forumcontent.paradoxplaza.com/public/1074783/image-23.png "image-23.png")


*[Image: AI generated color “blobs” and sketches painted after them.]*  

![lady_shalott_color_demo_low.gif](https://forumcontent.paradoxplaza.com/public/1074799/lady_shalott_color_demo_low.gif "lady_shalott_color_demo_low.gif")


*[Video: Creation of a color sketch based on an AI generated thumbnail.]*  

The animation above shows the process of turning a generated color thumbnail into a color sketch that is submitted for the art team review. The greenish-violet palette was acknowledged as the most appropriate for the theme, with a flavor of mystery and slight surreal feel of goldish light reflections in the water.  

### Painting​

After major decisions have been made it is time to make that final leap to the finished painting. Here the biggest challenge for me is to keep the overall image balance while adding details. Even when painting over a well defined sketch, the image inevitably changes during the process. Defining a hand gesture or dress design may change the flow of the shapes and force readjustments in other places. It is very easy to get carried away by a certain area of the picture and then realize that the detail you have just painted does not work when viewed from a distance or pops out too much and breaks the general balance of tonal values. Some elements of the image require more attention than the others. Character face is obviously a detail number one in that specific image’s hierarchy and it took me a while to paint it and find the proper expression. At the same time a number of secondary parts of the image I may have left untouched since the color sketch creation.  

A crucial role in that process of image balancing plays feedback from the art director and the team. Over time while working on an illustration I get less perceptive of it. And during the regular art reviews I can get a fresh view from my team that helps to notice mistakes and flaws or even to recognize the moment when it is time to stop and call the image done.  

![image-25-censored.png](https://forumcontent.paradoxplaza.com/public/1074792/image-25-censored.png "image-25-censored.png")


*[Image: Art director’s feedback suggesting perspective and tonal corrections.]  
[CM’s Note: Tastefully censored.]*  

Here at Paradox, we have regular drawing sessions where our artists can draw either live models or from references. While the primary purpose of this is to train general drawing skills (a kind of an art gym), this can also be used for more specific tasks. I can ask a model to take a specific pose or gesture that I am working on in my current assignment. This can be quite helpful to make characters in an illustration look more convincing, find a better gesture or just simply avoid crude drawing mistakes.  

![image-26-censored.png](https://forumcontent.paradoxplaza.com/public/1074793/image-26-censored.png "image-26-censored.png")


*[Image: A few examples of sketches and studies done with ongoing illustration assignments in mind.]  
[CM’s Note: Tastefully censored.]*  


### Conclusion​

On a final note, I have to confess that romanticized stories like the one about the Lady of Shalott are not that inspiring for me in general. The drama of these stories often seems too quixotic and naive to me. Yet one can find in their symbols and metaphors some true inspiring moments. For me in the case of the Lady of Shalott it was the contrast of young and flourishing life and premature death it was doomed for. I hope I managed to convey a bit of my sensations in the illustration.  

---

### Map Tables​

Hello! My name is Joacim Carlberg and I’m the 3D Environment Lead on CKIII.  

I’m going to introduce our new visual map tables, a feature we’ve wanted to add for a long time. With the new chapter a table scene will now appear as you lift your gaze higher from the map for an overview of the world. With the release of Legends of the Dead we have added two new map tables, the tables are chosen dynamically or if you have a preference you can also change the active one in the settings menu.  

![image-27.jpg](https://forumcontent.paradoxplaza.com/public/1074794/image-27.jpg "image-27.jpg")


*[Image: The map table as it appears in Legends of the Dead.]*  

If you do not have Legends of the Dead a base table will still be included with the accompanying patch, which can be seen below.  

![image-28.jpg](https://forumcontent.paradoxplaza.com/public/1074795/image-28.jpg "image-28.jpg")


*[Image: The map table as it appears without Legends of the Dead enabled.]*  

We think this will give a more immersive experience when overlooking the extent of your kingdom, the tendrils of plagues spreading the lands, and your legends spreading across the realms.  

For those that love visual mods or total conversion mods for the game will find that this framing is also quite moddable.  


### Legendary Buildings​

As you finish your legends you will find opportunities to add a new site in your kingdom that commemorates or relates to the legend you’ve sown and grown. These legendary locations provide bonuses, but also show up in the landscape of your realm.  

![image-29-32-combo.png](https://forumcontent.paradoxplaza.com/public/1074796/image-29-32-combo.png "image-29-32-combo.png")


*[Image: Legendary Statue, MENA Legendary Palace, India Legendary Palace, Legendary Runestone]*  

There’s more of these, but we’ll let you discover them in your own playthrough.  

### Instruments​

![image-33.jpg](https://forumcontent.paradoxplaza.com/public/1074797/image-33.jpg "image-33.jpg")


*[Image: Lute, Flute, Shawm, Hurdy Gurdy, Qanun in back]*  

While working with El Tyranos with the recent content creator pack the environment team also collaborated with him to bring a set of new instruments into the game for courtiers and rulers to bring some music and levity, and for minstrels to spread legends and great deeds.  

**Flute/Recorder**  
A ubiquitous instrument in many musical traditions, the flute has been a part of human history for millennia. While many of us first encounter music through the recorder, a flute variant, the broader family of flutes offers a diverse range of sounds. The flute's origins can be traced globally, with evidence of similar instruments found across various cultures. Its simple yet elegant design and versatility make it a staple in both classical and contemporary music.  

**Hurdy-Gurdy**  
The hurdy-gurdy, popular until the 19th century and experiencing a resurgence, is recognized for its distinctive drone. Its mechanism involves a rotating wheel running along the strings, making it a precursor to modern violins and influencing the design of the nyckelharpa.  

**Lute**  
A stringed instrument associated with minstrel songs of the Middle Ages, evolved from the medieval Islamic oud. It has a versatile range, transcending time and leaving a mark on musical history. The lute is synonymous with troubadours and courtly melodies.  

**Shawm**  
A woodwind instrument and precursor to the modern oboe, gained popularity from the later Middle Ages to the Renaissance. Its distinctive double reed and conical bore contributed to the development of subsequent woodwind instruments. The shawm's vibrant tones were integral to courtly festivities and religious ceremonies during its heyday.  

**Qanun**  
The qanun is an Arabic harp-like instrument with origins dating back to antiquity. It holds a significant place in the musical traditions of the middle east and has influenced a diverse array of musical instruments globally. The qanun's intricate design and delicate strings produce a sound that echoes with the rich history of ancient musical craftsmanship.  

All of these instruments will also be found as animation options in the barber shop.  


![image-34.jpg](https://forumcontent.paradoxplaza.com/public/1074798/image-34.jpg "image-34.jpg")


*[...Anyway, here’s wonderwall]*  

---

And with that it's time for us to wrap up today’s Dev Diary, more interesting things will be coming next week when we’ll be talking more about Plagues, the Black Death, Funerals, Mod support and showcasing new Character Art (that’d make Papa Nurgle proud).

<!-- artifact:reactions:start -->
- 114 Like
- 113 Love
- 9 (unlabeled — rendered as base64 data URI)
- 8 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753
<!-- artifact:op_signature:end -->
