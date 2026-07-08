---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1540182/"
forum_thread_id: 1540182
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 105
title: "Development Diary #105: 1.7 \"Bastion\" Update"
dd_date: 2022-08-30
author_handle: Trin Tragula
expansion: Friends and Foes
patch: Patch 1.7 (Bastion)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2435
inline_image_count: 14
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1540182'
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
    location: raw_lines_~28_to_114
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_116_to_117
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_430_to_435
    action: preserved_and_flagged
    counts:
      Like: 191
      Love: 97
      (unlabeled — rendered as base64 data URI): 5
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_443_to_515
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_516_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Development Diary #105: 1.7 "Bastion" Update

<!-- artifact:thread_metadata:start -->
- Thread starter [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)
- Start date [Aug 30, 2022](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-105-1-7-bastion-update.1540182/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-105-1-7-bastion-update.1540182/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-105-1-7-bastion-update.1540182/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-105-1-7-bastion-update.1540182/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-104-ai-ai-ai.1539411/ "CK3 Dev Diary #104: AI AI AI") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dd-106-a-fistful-of-friends-foes.1540926/ "DD #106: A Fistful Of Friends &amp; Foes")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-105-1-7-bastion-update.1540182/?prdxDevPosts=1)

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2045.jpg?1661851489)

# Development Diary #105: 1.7 "Bastion" Update

- Thread starter [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)
- Start date [Aug 30, 2022](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-105-1-7-bastion-update.1540182/)

Hello and welcome to another Development Diary for Crusader Kings 3. Today I will talk a bit about the free 1.7 “Bastion” update and what new things it will bring to the game. Today we will not be talking about [REDACTED] which will be released together with the update.  

The changes to Factions and AI have previously been covered in posts by [@Servancour](https://forum.paradoxplaza.com/forum/members/465268/) and [@rageair](https://forum.paradoxplaza.com/forum/members/375731/) and I will therefore not mention them again, but I recommend checking out their diaries if you missed them before: [AI, AI, AI](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-104-ai-ai-ai.1539411) and [Let's Talk Populist Factions](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/)  

#### Character Memories:​


While the characters often get up to quite memorable things in our games there has up to now not been a way to keep track of exactly what, when and with whom each character has had a particular experience. What we have done in the new update in order to show more clearly how alive the game world is, is to introduce memories to characters. Characters will remember things that happened to them, from important things like the births of their children, important battles, deaths of close ones, and succession, to more mundane things like the event interactions with other characters during their childhood.  

![Image - Log of the most recent memories of the player Maharaja](https://forumcontent.paradoxplaza.com/public/859628/owncharactermemories.png "Image - Log of the most recent memories of the player Maharaja")


[Image - Log of the most recent memories of the player Maharaja]  

At any time you can view the memories of your character as well as non-private memories of other characters. This lets you quickly get an idea of not only what a character is like, but also how they got there. One can think of it as a feature somewhat similar to the character history that we had in EU:Rome many years ago.  

One important difference to a character history though is that over time some memories will fade away, while others will remain. For player characters and characters likely to become player characters we err on the side of keeping memories longer, mostly because you are more likely to have a need of them as the game progresses.  

Memories can be viewed at any time by opening the Memory Viewer from the character window, via a button in the same place as the Kill List, Inventory, and Lifestyle.  

![Image - Log of the Public Memories of a non-player Character](https://forumcontent.paradoxplaza.com/public/859629/othercharactermemories.png "Image - Log of the Public Memories of a non-player Character")


[Image - Log of the Public Memories of a non-player Character]  

Memories are not only there as a log for the player to enjoy, however. The new system allows us to make use of memories that a character has both to trigger content and to make use of in events. This means that you may now find memories used in content that previously had to be vague, an assassin might now actually cite a specific slight you committed against their employer, for instance.  

What this also means is that we are now able to create new content that is based entirely on your character having a certain type of memory or sharing a memory with another character.  
Last of all I should mention that it is possible to export the memories of a character to clipboard in order to share it outside of the game for those that want others to know of their character’s exploits.  

Example of an exported memory list:  

> `
> 6 February, 1246
> My mother Têcappukal died in childbirth.
>
> 15 April, 1262
> I married Maharani Atittapatâriyâr.
>
> 13 October, 1263
> My grandfather Sadashiva died of old age.
>
> 20 February, 1264
> My first child Sangappai, a beautiful girl, was born.
>
> 16 November, 1264
> My father Neetimarga died of heart failure.
>
> 16 November, 1264
> I became the ruler of the Kingdom of Karnata.
>
> 14 January, 1265
> I married Maharani Pertal.
>
> 20 February, 1265
> I married Samrajni Lasthiyavva.
>
> 23 April, 1265
> I became friends with Maharaja Maurayadhwaj of the Vigrahapalid Kingdom.
>
> 2 February, 1267
> My grandmother Sattiyavvai died in captivity.
>
> 15 January, 1268
> I imprisoned Mâtevapattan Chola.
>
> 15 January, 1268
> I imprisoned Satyasraya Karhade.
>
> 15 January, 1268
> I won a war against Mâtevapattan Chola.
>
> 24 March, 1268
> I became the ruler of the Kingdom of Tamilakam.
>
> 29 August, 1268
> My daughter Chandaladevi was born.
>
> 10 October, 1269
> I journeyed to Kanchipuram on a pilgrimage.
>
> 30 January, 1270
> I became friends with Akkadevi Akkadevi.
>
> 22 January, 1271
> My carefully-written words guided Mahasamanta Mangalesi as he learned to read.
>
> 15 November, 1272
> My friends Akkadevi and Maurayadhwaj threw me a surprise birthday party.
>
> 1 January, 1273
> I married Samrajni Gandharavati.
>
> 12 November, 1273
> My son Rachamalla was born.
>
> 5 June, 1275
> My daughter Gayatri was born.
>
> 29 August, 1276
> My son Butuga was born.
>
> 21 January, 1279
> I became the ruler of the Kingdom of Andhra.
>
> 3 September, 1279
> My son Jayasimha was born.
>
> 7 June, 1280
> I became friends with Mahasamanta Narasanayaka of the Akkadevi Raj.
>
> 22 July, 1280
> My friend Maharaja Maurayadhwaj of Vigrahapalid drank himself to death.
>
> 24 September, 1283
> I started a war against Rajkumar Achugi of Telingana.
>
> 13 November, 1283
> I became friends with Rajkumar Rachamalla of the Hoysala Empire.
>
> 5 December, 1284
> My sister Gangambika died Gout Ridden.
>
> 30 January, 1285
> I won a war against Rajkumar Achugi of Telingana.
>
> 20 August, 1285
> I became the ruler of the Kingdom of Telingana.
>
> 19 December, 1285
> My brother Govinda died from Smallpox.
>
> 30 January, 1286
> I started a war against Rajkumar Arthapathi of Maharastra.
>
> 19 April, 1287
> My wife Pertal died of old age.
>
> 1 May, 1287
> I married Damapatni Prabhavatigupta.
>
> 27 August, 1288
> My wife Atittapatâriyâr died in her sleep.
>
> 24 February, 1289
> I became the ruler of the Kingdom of Maharastra.
>
> 24 February, 1289
> I won a war against Rajkumar Arthapathi of Maharastra.
>
> 26 June, 1289
> I became the ruler of the Deccan Empire.
>
> 27 November, 1289
> Rajkumar Rachamalla of the Hoysala Empire and I became rivals.
>
> 17 June, 1290
> I started a war against Mahasamantadhipati Kassapa II of the Vijayabahu Kingdom.
>
> 4 April, 1292
> I became friends with Mahasamanta Nayanadevi of Vidharba.
>
> 22 September, 1292
> I won a war against Mahasamantadhipati Kassapa II of the Vijayabahu Kingdom.
>
> 22 October, 1293
> Me and Rajkumar Rachamalla of Asika let go of our grudges and stopped being rivals.
>
> 30 August, 1295
> My daughter Vijamba was born.
>
> 11 August, 1297
> I married Samrajni Nattadevi.
>
> 7 November, 1297
> Mahanaga Vijayabahu and I became rivals.
>
> 13 August, 1298
> My daughter Mahadevi was born.
>
> 6 September, 1298
> My wife Lasthiyavva died of old age.
>
> 11 February, 1299
> I married Samrajni Orbei.
>
> 30 November, 1299
> I became friends with Samanta Narasanayaka of Tagadur.`
>
> Click to expand...


#### Relationship Reasons:​

![friendreason.png](https://forumcontent.paradoxplaza.com/public/859573/friendreason.png "friendreason.png")

![Friendreason2.png](https://forumcontent.paradoxplaza.com/public/859574/Friendreason2.png "Friendreason2.png")

![friendreason3.png](https://forumcontent.paradoxplaza.com/public/859575/friendreason3.png "friendreason3.png")


[Image - 3 Examples of friendship reasons from an ongoing game]  

Another addition coming with this update to further open up how things are connected in the game’s world is that we have wanted to make it clearer which characters are your friends, enemies, nemeses, etc, as well as clearer why a character has a special relationship with that particular character. This is accomplished by a new set of icons in the interface to highlight relationships.  

Additionally whenever a relationship is formed the game notification will now not only say that it happened but also why it happened. The reasons for relationships will then always be visible in its tooltip: clearly telling you how they became friends, lovers, best friends, nemeses, etc. In cases where a more advanced relation (such as best friend or nemesis) exists we will show the reason for both the basic relationship and the more advanced one, so a best friend will keep track of both how you originally became friends and when you actually became best friends.  

Together with character memories this should now make it more clear what has led you to the current point in your game, a small change that brings a surprising amount of context, highlighting parts of the interpersonal simulation that can right now be a bit hidden away.  


![rivalreason.png](https://forumcontent.paradoxplaza.com/public/859576/rivalreason.png "rivalreason.png")

![rivalreason2.png](https://forumcontent.paradoxplaza.com/public/859577/rivalreason2.png "rivalreason2.png")


[Image - 2 Examples of Rivalry reasons from an ongoing game]  


#### ​

#### Revamped Childhood Events:​


![Image - Childhood event where you can get Diligent, Gregarious, or Temperate. Child's perspective](https://forumcontent.paradoxplaza.com/public/859583/childhood2.png "Image - Childhood event where you can get Diligent, Gregarious, or Temperate. Child's perspective")


[Image - Childhood event where you can get Diligent, Gregarious, or Temperate. Child's perspective]  

![Image - Childhood event where your ward can get Diligent, Gregarious, or Temperate. Guardian's perspective.](https://forumcontent.paradoxplaza.com/public/859581/childhood1.png "Image - Childhood event where your ward can get Diligent, Gregarious, or Temperate. Guardian's perspective.")


[Image - Childhood event where your ward can get Diligent, Gregarious, or Temperate. Guardian's perspective.]  

Another thing that we wanted to revisit in order to improve on how we deal with characters in the game world is the revamping of all existing childhood personality events as well as the addition of 12 new ones. This will significantly alter what personality trait combinations are likely to appear and will open up some combinations that were previously impossible simply due to how the old events for growing up worked.  

The ambition apart from adding more content to the childhood period is to have the choices you make as a guardian be more interesting, avoiding any easy best choices in any single childhood event.  

The new trait combinations that will be pitted against each other are:  


- diligent, gregarious, temperate
- zealous, ambitious, sadistic
- shy, paranoid, craven
- lazy, gluttonous, compassionate
- lustful, chaste
- just, greedy, callous
- humble, cynical, content
- vengeful, deceitful, calm
- generous, fickle, arrogant
- forgiving, trusting, patient
- honest, arbitrary, impatient
- brave, stubborn, wrathful

![Image - Childhood event where you can get Generous, Fickle, or Arrogant. Child's perspective](https://forumcontent.paradoxplaza.com/public/859580/childhood.png "Image - Childhood event where you can get Generous, Fickle, or Arrogant. Child's perspective")


[Image - Childhood event where you can get Generous, Fickle, or Arrogant. Child's perspective]  

![Image - Childhood event where your ward can get Generous, Fickle, or Arrogant. Guardian's perspective.](https://forumcontent.paradoxplaza.com/public/859582/childhood3.png "Image - Childhood event where your ward can get Generous, Fickle, or Arrogant. Guardian's perspective.")


[Image - Childhood event where your ward can get Generous, Fickle, or Arrogant. Guardian's perspective.]  

#### The Loyal and Disloyal Traits:​


![Image - Character with the Disloyal Trait](https://forumcontent.paradoxplaza.com/public/859631/disloyaltrait.png "Image - Character with the Disloyal Trait")


[Image - Character with the Disloyal Trait]  

![Image - Character with the Loyal Trait](https://forumcontent.paradoxplaza.com/public/859627/loyaltrait.png "Image - Character with the Loyal Trait")


[Image - Character with the Loyal Trait]  

Last but not least for today is the addition of two new traits with the upcoming update. Through their actions (or indeed as they are subjected to the actions of others) characters can now gain traits for having loyal or disloyal personalities, which among other things will impact how likely they are to cheat on their spouse, join factions or plot against their liege. The traits are also integrated as sins/virtues and can be more valued or common depending on cultural traditions.  

That was all for today. The new update will also bring new bug fixes, event pictures, and things that I have not brought up today but this was a sneak peak of what is to come.  
Next week [@PDS_Noodle](https://forum.paradoxplaza.com/forum/members/1394234/) will be talking some more about what the future will bring.

<!-- artifact:reactions:start -->
- 191 Like
- 97 Love
- 13 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)**
Role: Game Designer - Crusader Kings 3
Badges: 36
Reaction score: 16,644

*[Full game-badge icon list of 12 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
