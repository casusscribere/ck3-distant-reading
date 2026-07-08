---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1601384/"
forum_thread_id: 1601384
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 136
title: "Dev Diary #136 - Our Vision for Persia"
dd_date: 2023-10-11
author_handle: rageair
expansion: Legacy of Persia
patch: Patch 1.11
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1752
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1601384'
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
    location: raw_lines_~28_to_149
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_148
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2603.jpg?1696959192
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_151_to_153
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_263_to_267
    action: preserved_and_flagged
    counts:
      Like: 149
      Love: 74
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_275_to_378
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_379_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2603.jpg?1696959192)
<!-- artifact:thread_banner:end -->

# Dev Diary #136 - Our Vision for Persia

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Oct 11, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-136-our-vision-for-persia.1601384/)
<!-- artifact:thread_metadata:end -->

Greetings!  

It is time to dive into the upcoming Flavor Pack - *Legacy of Persia* - giving a brief overview of the **why** and the **what**! The region has a rich and vibrant history making it both exciting and interesting to work with, not the least because it differs significantly from the regions we've chosen to cover in the past - Persia lies at the crossroads of the world, with a multitude of external influences combined with strong local traditions. Naturally while our focus has been on the Persian region itself, we've also aimed to shake up a portion of the world at large by revising how the Clan government works, so even if you're not playing in the Persian region there's something new and exciting to experience.  

Co-writing this Dev Diary with me is Lucas Ribeiro - our skilled and multitalented 2D Art Lead at PDX Studio Black, who has been deeply involved with many of the features of this pack!  


![image3.jpg](https://forumcontent.paradoxplaza.com/public/1017501/image3.jpg "image3.jpg")



**So, why Persia?**  

For starters, our data pointed out that Persia is already a very popular starting location for our players. The region is within the **top ten most picked starting locations** and the **most popular one outside of Europe.**  
Despite originally not having much flavor dedicated to the area and no bookmark characters attached to it, our players were still going for Persia playthroughs. There’s no better endorsement of the interest in the region than that!  

But, player data aside, all history enthusiasts know how rich and interesting Persia is, even more so during Crusader Kings III’s time period. We saw this as a chance to create very interesting gameplay opportunities.  
At the 867 game start, the Abbasid Caliphate is reeling from the Anarchy at Samarra. A moment in history when many Caliphs fell victim to a deadly struggle for power while insurrectionists raged up and down the Tigris and the Euphrates, such as the **Kharijite and the Zanj Rebellions**. Meanwhile in the east, Iranian rulers rose to challenge the Abbasid Authority. This time period, known as the **Iranian Intermezzo** saw a partial revival of Iranian culture with the ascension of the Saffarid and Samanid dynasties. About a century after the start date of 867, the Iranian Daylamite Buyids came to power, subjugating the Abassid Caliphate.  
This Iranian comeback is then cut short by the **Seljuk Invasion**. A dynasty of turkic warrior nomads take over Persia and the Levant, submitting both Arabs and Iranians to their rule. Further on the east the **Ghaznavids** defeat the Samanids, cementing the end of the Iranian Intermezzo and leading into the state of Persia as we see in the 1066 start. The Buyids are not playable on the 867 start, as their founder, a warrior from the mountains of Daylam had yet to leap into history. But a last holdout of the dynasty can be found in Shiraz at the 1066 start.  


![image2.jpg](https://forumcontent.paradoxplaza.com/public/1017502/image2.jpg "image2.jpg")



**Clan Government Rework**  

Since the area of the flavor pack is almost entirely made up of Clan Rulers, for *Legacy of Persia*, we have decided to reimagine how the Clan government works.  

Our aim is to more closely represent the familial struggles of the powerful clans of the time and the bureaucratic apparatus that backed their interests.  

The Clan government is now directly tied to how your house members interact with each other. Each house will have a Unity Level that can be changed by intervention of the house head and by its members treating each other kindly or badly. A harmonious clan will have a consolidated succession, while an antagonistic one, not so much!  

Clan rulers employ an office of bureaucrats, their Tax Collectors, to levy troops and coin from their vassals. The competence of a Tax Collector will dictate how much they manage to extract from the vassals assigned to them. Each Tax Collector manages a Jurisdiction with an associated Tax Decree. For example: You might want to place all your non-muslim vassals in a Jurisdiction with the Jizya Decree and maximize your gold income.  

More details on the Clan Government design on a future dev diary.  


![image6.jpg](https://forumcontent.paradoxplaza.com/public/1017503/image6.jpg "image6.jpg")



**Iranian-Heritage Cultures**  

Persia and its surrounding areas are populated by a variety of different iranian-heritage cultures. We strived to give each one of them an original combination of cultural traditions that allow for a variety of new playstyles. The Kurds with their hard-to-convert culture and mountain cavalry, the Daylamites with their two-pronged spear wielding mercenaries and so on.  
Persian culture, of course, received special attention. With new traditions about their famous scholarly pursuits and elaborate systems of water cooling and irrigation.  

Iranian cultures have also received new clothes, headgears, hairstyles, beards and unit models, making them more appropriately distinct from the Arabic cultures. Also, due to their importance in the region, Turkic cultures have also received some sorely-missed assets, such as the Sharbush hat and the very recognizable Seljuk braids.  


![image4.jpg](https://forumcontent.paradoxplaza.com/public/1017504/image4.jpg "image4.jpg")



**Islam and Zoroastrianism**  


In Crusader Kings’ 3 starting date of 867, Islam has been the dominant religion of the upper classes in Persia for over a century. Still, Zoroastrian practices are still very much alive and widespread in the peasantry. We’ve done a general pass on religion in the region, adjusting provinces and characters to a more accurate historical representation. Tenets and doctrines for both Islam and Zoroastrianism have also received lots of adjustments and tweaks. Jizya, for example, has been moved to a tax jurisdiction type unlocked for muslim clan rulers. Both religions have received new decisions and events to flesh them out some more. They’re also strongly tied to the Struggle system in the region, speaking of which…  


![image1.png](https://forumcontent.paradoxplaza.com/public/1017506/image1.png "image1.png")


![image7.png](https://forumcontent.paradoxplaza.com/public/1017507/image7.png "image7.png")



**A New Struggle, the Iranian Intermezzo**  

With Legacy of Persia, we are bringing a new Struggle, the **Iranian Intermezzo**.  

This struggle seeks to represent the historical dissolution of the Caliphal authority over Persia and the ascension of new, powerful, Iranian Rulers In the 9th and 10th centuries. It also reflects a shorter historical period when compared to Fate of Iberia’s Struggle, so it is likely to be resolved more briefly and intensely.  

Unlike Fate of Iberia, participant characters are clearly divided into factions. **The Caliphal Supporters against the Detractors**. A lot of new interactions are unlocked by this dynamic, such as convincing a character to switch sides, sponsoring turkic invasions against supporters, or waging war to install Caliphal Supporters.  

The struggle has three phases, Unrest, Stabilization and Concession. The Concession phase is of a new type, a so-called **Ending Phase**. If a struggle gets to an Ending Phase, it will instantly trigger an ending. So, unlike **Struggle Ending Decisions**, where there is a dominant character that pushes the button to trigger it, every involved character can contribute to an Ending Phase by triggering relevant catalysts.  

We have designed four struggle endings (three as decisions, one as an ending phase), which can be pursued in different ways, depending on the personal perspective of your character.  

Will the Caliph be able to reestablish their power over the region? Will a powerful Shia ruler overtake the Sunni, creating a new Caliphate? Maybe an Iranian ruler will usher in an era of Persian dominance, forever boosting cultures of Iranian-heritage? Or, a Sunni Caliphal Detractor might oust the Caliph and take their place as head of faith?  

In the **Iranian Intermezzo Struggle** we went for a more nuanced, granular approach, where the endings are subdivided into options that have different effects, according to your character’s culture, religion and whether they are part of the Supporter or Detractor faction.  


![image5.jpg](https://forumcontent.paradoxplaza.com/public/1017508/image5.jpg "image5.jpg")



**New 867 Bookmark**  

With *Legacy of Persia* we are adding a new bookmark, the **Persian Revival**, with five Iranian-heritage characters to choose from. These were picked both for their historical importance and to provide for a wide variety of gameplay styles.  

In the mountains of Daylam we see a fan favorite, **Rostam Bavandid**, one of the last Sassanids in the game and a secret Zoroastrian. A great character if you are going for a “Sassanian Restoration” style playthrough.  

In the southern reaches of Persia, **Muhammad of the Tahirids** is a loyal vassal and supporter of the Caliphate. His nephew, though, rules an independent emirate in Khorasan and is desperate for help against the invading Saffarids. This character was a great pick for us, since he’s split between internal and external conflicts in the Caliphate.  

Since we mentioned Saffarids, we have **Yaqub**, the coppersmith. This lowly peasant rose to power through extraordinary military prowess. In one of his many battles, he was swordstruck and horribly disfigured. But, despite all these difficulties, this upstart is pushing back against the might of the Abbasids. He was an obvious choice for us, since he is an interesting historical figure and a sort of folk hero of the Iranian traditions, having restored Persian as the official dialect of the region (after it was supplanted by Arabic).  

Next, we have one that will be familiar to the achievement hunters, **Suri of the Ghurids**. Although historically Suri is mostly known for running away from the Saffarids and hiding at his buddy Abdullah Habbari’s court, his dynasty eventually grew into a huge Empire. Being Tajik and Mahayana, he’s stuck between the Muslim and the Buddhist world, creating opportunities for interesting gameplay. There’s also a lot of juicy mines in the region that Suri can go claim and fuel his future conquests. Good luck to all players out there going for the “Rise of the Ghurids” achievement!  

Lastly, we have **Ismail of the Samanids**. Despite being distant in the line of succession, historically Ismail came to supplant all of his relatives and assume control of his brother’s Emirate. The Samanids under Ismail grew into a true empire, only to be overtaken later by the Ghaznavids and the Seljuks. An interpretation of Ismail’s likeness can now be seen stamped on the Tajikistani currency, the Somoni, which is named after his dynasty.  

---

That's it for this time! More details will follow soon!

<!-- artifact:reactions:start -->
- 149 Like
- 74 Love
- 19 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 41 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
