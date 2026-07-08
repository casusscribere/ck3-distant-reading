---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1527558/"
forum_thread_id: 1527558
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 98
title: "CK3 Dev Diary #98: the Castle's foundation"
dd_date: 2022-05-24
author_handle: Pdx_Meedoc
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2250
inline_image_count: 14
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1527558'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1959.jpg?1653397938
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_320_to_324
    action: preserved_and_flagged
    counts:
      Like: 108
      Love: 43
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_332_to_440
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_441_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1959.jpg?1653397938)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #98: the Castle's foundation

<!-- artifact:thread_metadata:start -->
- Thread starter [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)
- Start date [May 24, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-98-the-castles-foundation.1527558/)
<!-- artifact:thread_metadata:end -->

Hello there,  

The release is approaching and before sharing the release notes with you next week we have a few topics to cover! Today we will be focusing on what is going to be added in the free update "Castle" released along Fate of Iberia. For the modders, you will also find the updated documentation attached to this post, in case you want to have an early look at the new functionality!  


## Clan Contract​

Since Iberia in 867 has several clan realms that play big parts in the region, we wanted to add some new options to clan contracts:  


- Marriage Favor: the goal is to get benefits in exchange for a promise. Not fulfilling it will have consequences though..
- Ghazi: encourage your vassals to wage holy wars, but get less levies from them
- Iqta: less tax and levies but better synergy for Men-At-Arns for both parties
- Jizya: unlocked by the Tenet of the same name, this is a specific contract for people of a different faith, increasing their tax but lowering the levies their liege receives

![The image shows the new special contract for Clan Government](https://forumcontent.paradoxplaza.com/public/830359/20220524102616_1.jpg "The image shows the new special contract for Clan Government")

*There are now cool options to get the most of out your vassals as Clan Liege now.*  

We are looking forward to working more on clan governments in future updates as this was a first step to making them as complex and interesting as they were historically.  


## Dissolution Faction​

To model some of the big historical shake-ups in Iberia, we’ve introduced a new faction type. The Dissolution Faction will aim to destroy the primary title of the top liege of the realm, as well as any other same tier title. This makes all vassals independent, shattering a kingdom or empire. In FP2, this means that the Umayyads can collapse as they did in history, but it also means that any large realms in decline will face this challenge.  

Anything detracting from a realm’s unity will increase the risk of a Dissolution Faction forming. That means short reigns, low cultural acceptance, war losses, and unallied vassals will all be dangerous to King and Empire tier rulers.  

Realms where the vassals either like the heir or can elect their own are less likely to face a Dissolution Faction. And if a vassal can make a claim for the title themselves, they’ll do that instead.  

![The image shows the Enforce Demands of the new Dissolution faction: the primary title will be destroyed, granting independence to all the vassals of the target](https://forumcontent.paradoxplaza.com/public/830361/20220524103823_1.jpg "The image shows the Enforce Demands of the new Dissolution faction: the primary title will be destroyed, granting independence to all the vassals of the target")

*There is a high chance of the Umayyad falling when starting in 867*  

## Map update​

To go along the theme of the flavor pack, we’ve updated the map for Iberia. The map changes are fairly small in scope this time around though, and the focus was to update northern Iberia, more specifically the kingdom of Aragon.  

In order to improve the overall accuracy we added new counties such as Rossello and Pallars. For a better depiction of the area, existing baronies were moved around and new ones added in order to increase the granularity of the area.  

![The image is a close up to the area that changed the most, showing the new county set up](https://forumcontent.paradoxplaza.com/public/830362/20220524102803_1.jpg "The image is a close up to the area that changed the most, showing the new county set up")

*In addition to the county set up, the terrain type of some provinces also changed.*  

In addition to the changes in Aragon, we added cultural naming variations for many Berber and Arabic cultures to many titles across Iberia.  

## Shared Head of Faith​


Heads of faith can now be set as characters of a different faith. This is done through script, rather than manually in-game. This means for insular Christians, Conversos, and Mozarabs, the Pope will be their Head of Faith, even though they are of a different faith.  

![The image shows that the Insular faith now have the Pope as their Head of Faith](https://forumcontent.paradoxplaza.com/public/830364/20220524104557_1.jpg "The image shows that the Insular faith now have the Pope as their Head of Faith")



Historical faiths can be emulated by using the Rite tenet. Provided you don’t meet certain red lines for your old Head of Faith, at the cost of a tenet slot, you can keep your old faith’s Head of Faith while converting.  
Ecumenical Christians taking this decision keep ecumenism, making them “astray” from the Catholic perspective.  

![The image shows the tooltip of the new Rite tenet ](https://forumcontent.paradoxplaza.com/public/830365/20220524104626_1.jpg "The image shows the tooltip of the new Rite tenet ")



Islam now has a bespoke system for choosing the correct caliph: though Shias are still fairly split between several caliphates and imamates, the mainline Sunnis (Ashari, Muwalladi, and Maturidi) now share the Sunni caliph as a Head of Faith. Muslims who share a Head of Faith view each other as ”righteous”.  
Influential members of an Islamic faith whose Head of Faith doesn’t share their faith can attempt to Appoint a Righteous Caliph, claiming (and creating) the caliphate for themselves and splintering the Ummah.  

![The new decision allowing to appoint a new Caliph](https://forumcontent.paradoxplaza.com/public/830397/20220524123130_1.jpg "The new decision allowing to appoint a new Caliph")



Once splintered, a faith cannot be brought back into the fold. Islam is stronger together, but its differences often become irreconcilable.  

New temporal Sunni and Shia faiths cannot appoint themselves as caliphs immediately if there’s a caliph available (either the orthodox version or their prior faith’s caliph). Instead, they must show submission to an existing caliph from whom they derive their authority, even in rebellion, and then follow the path to Appoint a Righteous Caliph themselves. Characters intending to do this all along can get a little boost on the path.  

## History Changes (and friends!)​

### Visigothic is Visigone​

As I’m sure some of you have noticed in the streams and such, we’ve removed Visigothic from the map 867, starting Iberia off pre-split between the 1066 cultures (save for Aragonese, which now emerges as part of the creation of the Kingdom of Aragon).  

There’s a few reasons for this - Visigothic was always a bit of a wonky culture, a holdover from CK2’s Charlemagne DLC that made mapping 9th century Iberia very inexact but which added some fun flavour to the region. Since cultures before 1.5 were mostly cosmetic, it didn’t really affect actual gameplay much, even if it fudged history somewhat (not least by making the Visigoths hang around long after they’d diverged or hybridised).  

The release of Royal Court changed that situation, making playing in Iberia a very weird flow. You start, you have one set of traditions, then within a few decades an event shifts your culture and you almost certainly end up with a radically different set of traditions with no feasible way to do much about it.  

This, plus just being bad history, clinched it for Visigothic, and we had it taken out to the block and given the ol’ Royal Anti-Pardon. As with Suebi and co before it, Visigothic will continue to exist in the files, along with its associated namelist, where it remains useable for history and in mods and such.  

![The image shows the new culture set up in Iberia. Andalusian in the south, and the north is split between Galician, Astruleonese, Castilian, Basque, and Catalan](https://forumcontent.paradoxplaza.com/public/830366/20220524104714_1.jpg "The image shows the new culture set up in Iberia. Andalusian in the south, and the north is split between Galician, Astruleonese, Castilian, Basque, and Catalan")



### Fresh Faces & Further Foes​

Further on from this, we’ve updated, added, and occasionally removed hundreds and hundreds of characters all across Iberia (as well as a smattering in Occitania - if we never read about another character named Bernard, we’ll be happy), adjusting relations, lifespans, traits, and dynasties.  

This’ll add a bit of life in both major bookmark dates, but most importantly, it’ll be a bit of colour for those of us who enjoy spelunking the history databases and checking to see if titles in-game have their Migration Period rulers properly associated. Title-nerds need love too. On that note, the Visigothic Kings now have a titular historical title to give them their correct royal dignity & regnal numbers.  

For folks who like actual gameplay more than interactive reading, we’ve added the Mozarabic strand of Christianity - Arabicised Catholics who carry on the strongly independent liturgical and ecclesiastic traditions of pre-Islamic Iberia but view the Pope as their Head of Faith (with the aid of the Rite tenet).  

Squeezed between the Catholic North and the Islamic South, the Mozarabs struggle to preserve their way of life, and since you can see a lot more of them in 867 than 1066, you can probably guess how it’s going for them.  

Previously, we’ve portrayed the sparsely-regulated Leonese portion of Iberia’s Inner Plateau as being, variously, either under nominal Andalusian control (since they notionally held it) or nominal Asturian control (since they grabbed it soon after the Andalusians stopped caring about it).  

Neither of these were quite perfect solutions, and relied on fictitious local characters either way, so we’ve now given this rural area over to a collection of minor Mozarabic characters. Abandoned by their Islamic overlords, eyed greedily by their orthodox brethren, these minor landholders soldier on as they have for centuries. At least, they try to, but it’s a difficult life being a one-county minor wedged between larger realms…  

It’s not all doom’n’gloom for Iberia’s new minors though, because, on the subject of those larger realms, we’ve also split them up a tad! Asturias has lost Portucale, which they’re actually only in the process of trying to snatch, whilst Andalusia has been given a reality check. Both Portucale and Toledo, whilst paying nominal homage to Cordoba, were functionally independent, with Toledo in particular resisting repeated military expeditions and attempts at taxation.  

![The image shows the new Realm set up for Iberia. There are now more independent Kingdom between Al-Andalus and Asturia](https://forumcontent.paradoxplaza.com/public/830367/20220524102525_1.jpg "The image shows the new Realm set up for Iberia. There are now more independent Kingdom between Al-Andalus and Asturia")



Andalusia is in the process of making a play to subjugate Toledo more firmly in 867, with Portucale also being on the books, so we represent this as a brace of wars on start. Andalusia is trying to quell its powerful border districts of Toledo and Portucale, keeping them in the realm, whilst Asturias tries to snatch Portucale mid-rebellion.  

Finally, Asturias has been tweaked, losing its starting title law of feudal elective. The current king’s father decisively abolished the notion of the nobility electing their kings in the short term, and his son carried that on, so they start sans-title law now. In addition to this, Castile also starts with de jure territory in 867, making it creatable in the earlier bookmark - if Castile actually is created for any reason, Asturias is reduced to Leon. If Asturias is able to de jure drift Castile into itself before Castile can be created, then the union is preserved and Asturias earns its right to perpetually exist for 867 starts.  


## Achievements​

And last but not least, they are not part of the free update, but the community poll spoke:  

![The result of the community poll on twitter. Having achievements today won with 38.4% against 34.9%](https://forumcontent.paradoxplaza.com/public/830386/twitter_poll.png "The result of the community poll on twitter. Having achievements today won with 38.4% against 34.9%")



The result being tight, they will be hidden in a spoiler field, so you can keep the surprise for next week if you prefer ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")  

(Please be mindful of people’s choice and don’t spam the comments with the achievements or such)  

Spoiler: The new achievements

### Easy​

![The list of the easy achievements](https://forumcontent.paradoxplaza.com/public/830385/achievement_easy.jpg "The list of the easy achievements")


### Medium​

![The medium difficulty achievements](https://forumcontent.paradoxplaza.com/public/830387/achievement_medium.jpg "The medium difficulty achievements")



### Hard​

![The list of the hard achievements](https://forumcontent.paradoxplaza.com/public/830389/achievement_hard.jpg "The list of the hard achievements")


### Very Hard​

![The very hard achievements](https://forumcontent.paradoxplaza.com/public/830390/achievement_very_hard.jpg "The very hard achievements")



And that concludes today’s Dev Diary!  
See you next week for the release note! Until then, you can follow Hugo and Ola’s adventure in Iberia in [**tomorrow’s stream**](https://www.twitch.tv/paradoxinteractive), 2:30pm CEST ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")  

Cheers,  

![image (21).png](https://forumcontent.paradoxplaza.com/public/830382/image (21).png "image (21).png")

 

#### Attachments

- [/forum/attachments/1-6-0-scriptdocs-zip.842916/](https://forum.paradoxplaza.com/forum/attachments/1-6-0-scriptdocs-zip.842916/)
  
  1-6-0-scriptdocs.zip
  81,5 KB

 · Views: 0

<!-- artifact:reactions:start -->
- 108 Like
- 43 Love
- 10 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)**
Role: Corporal
Badges: 95
Messages: 39
Reaction score: 2,254

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
