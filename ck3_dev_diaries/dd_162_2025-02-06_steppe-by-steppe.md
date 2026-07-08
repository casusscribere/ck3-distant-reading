---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1728107/"
forum_thread_id: 1728107
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 162
title: "Dev Diary #162 - Steppe by Steppe"
dd_date: 2025-02-06
author_handle: hattusa
expansion: Khans of the Steppe
patch: Patch 1.16
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2927
inline_image_count: 15
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1728107'
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
    location: raw_lines_~28_to_152
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_151
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3574.jpg?1739278250
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_154_to_156
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_401_to_406
    action: preserved_and_flagged
    counts:
      Love: 201
      Like: 134
      (unlabeled — rendered as base64 data URI): 4
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_414_to_524
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_525_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3574.jpg?1739278250)
<!-- artifact:thread_banner:end -->

# Dev Diary #162 - Steppe by Steppe

<!-- artifact:thread_metadata:start -->
- Thread starter [hattusa](https://forum.paradoxplaza.com/forum/members/hattusa.1800793/)
- Start date [Feb 6, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-162-steppe-by-steppe.1728107/)
<!-- artifact:thread_metadata:end -->

[*Note: You can listen to today's Dev Diary here!*](https://youtu.be/xk2Tf8Vp2lA)  

Өглөөний мэнд!  

I am here to welcome you to a special kind of Development Diary – It's the first of a series, but the rest will come later and not in the following weeks. We're working on a comprehensive system for the Nomads of the Steppe, and while we are knee-deep in the production of the expansion, we still want to introduce you to the features as soon as possible, with the aim of collecting feedback and acting on it during our approaching iteration phase.  

For that reason we are showing screenshots **earlier than usual**, so do keep in mind that all shown here is still a **work in progress**.  

Therefore, some small caveats:  


- Layouts, visuals, and other aspects of the UI may change as we continue to refine these systems.
- The map set up is also not final and we are open to feedback.
- All values and numbers are still subject to balancing, and some of them are mere placeholders while we work on the features.
- This is an overview of the next DLC. The following Dev Diaries will go more in depth about all features at a later date – we need time to act on the feedback we get from you, so dev diaries for this update will not be releasing weekly just yet.

---

### Nomadic Government​

At the core of this update lies the new Nomadic Government. This new government type is heavily inspired by the rulers of the Eurasian Steppe, and puts a heavy emphasis on **herd, might, and land**.  

![image-01.png](https://forumcontent.paradoxplaza.com/public/1245277/image-01.png "image-01.png")


*[Initial distribution in 1178.]*  

But what do we mean by that?  

### Herd​

Your cattle and horses are represented by **a new currency only available to Nomads called "Herd"**. In the Steppe, Herd is incredibly valuable and plays a big role in how other Nomads perceive you: it can be used for ransoming, dowry, bribes and even be stolen via a scheme or raiding. It controls who the Cultural Head is and serves as a gate for increasing Dominance (we will talk more about this later in this Diary).  

Herd is obtained both through the land by exploiting its Fertility and through your Nomadic subjects via their contracts, since Nomads don't have a stable income. We will talk more in depth about this in the "Land" section below.  

One of the main changes when it comes to Nomads is that they do not use levies. Instead, **they transform a percentage of their Herd into Horde Riders**.  

Horde Riders are the most basic type of Men-at-Arms that Nomads have access to. However, these **Riders can be then upgraded to better MAAs types**, such as Horse Archers, for a cost of gold. These numbers don't come from a vacuum, however; if I want to create 100 Horse Archers, then I will lose 100 Horde Riders as they are converted into the new unit.  

Basic Horde Riders don't have an associated maintenance cost, but the other MAAs do in the form of monthly prestige.  

We've opted for this change because warring was an essential part of the Steppe life, and levies did not exist per se, as every able warrior would be called when the time was needed. From a more mechanical standpoint, we wanted Nomads to have fewer, but stronger and more significant, MAAs.  

![image-02.png](https://forumcontent.paradoxplaza.com/public/1245278/image-02.png "image-02.png")



The percentage depicted in the screenshot above represents what percentage of your Herd can be converted into Horde, as not all of them are mounts suitable for war. This percentage can be affected by yurt buildings, dynasty perks, character modifiers and other factors.  

![image-03.png](https://forumcontent.paradoxplaza.com/public/1245279/image-03.png "image-03.png")


*[Extremely WIP, we are aware of some issues like the Maintenance cost not being displayed]*  

To reflect the importance of your people, the names on a Nomadic map are also different from our regular naming conventions. **It is the *Borjigin Mongols* that move across the map, not the *Duchy of Örgöö*.**  

The Cultural Head gets to take the cultural name (The Mongols), while the smaller rulers have a combination of their House Name + Culture (The Borjigin Mongols). To better reflect the dynamics of the Steppe, we have also changed the way that the Cultural Head is selected in Nomadic governments: the ruler with the biggest Herd becomes the Head instead, independently of their title.  

The names on the map, as well as this naming convention using culture are still work in progress, and we are open to hear your suggestions.  

![image-04.png](https://forumcontent.paradoxplaza.com/public/1245280/image-04.png "image-04.png")


*[Note that we may remove the "The" to make the titles more readable.]*  

---

### Might​

In the Steppe, might makes right. Titles are not as important as actual strength, and to reflect this we've made a series of changes that only affect Nomads.  

**Nomadic rulers have access to Dominance**, a measurement of their perceived power. Low Dominance implies a relatively insignificant chieftain, while the maximum Dominance represents the rise of Genghis Khan.  

Dominance is a fixed scale, a mountain that Nomads have to climb, with each level being a hard-achieved goal that each ruler must work towards. Only those who have a Herd of a significant enough size are allowed to reach the next level.  

Dominance affects things such as Vassal and Domain limits, with the lower levels having a very reduced number of both, but with higher levels offering impressive bonuses. Dominance also governs the tiers that you are allowed to target during your migration (more on this in "Land"), access to special Men-at-Arms, title and vassal revocation, settlement outside of the Steppe, flavourful decisions and more.  

### Obedience​

You'll need loyal followers if you're going to take over the world – and it does not matter by what means you've ensured their loyalty.  

Obedience is a binary state – either you are obedient or not. Every character that's a subject or courtier has Obedience towards their overlord. Obedience works as a threshold; if a character is below the threshold then they will be unruly, plotting against their overlord or just having general acceptance maluses to various interactions. However, if a character is above the threshold then they will not form factions, start hostile schemes against their liege, and – more importantly – will take their side during the Kurultai succession by voting for whichever heir was your preferred one. The Kurultai is formed by special members of your Council, and having them on your side is extremely important for Nomads.  

Obedience is calculated based on several parameters like the relationship with the other character, friendship, their traits and whether you have granted them a Kurultai or Court Position.  

![image-05.png](https://forumcontent.paradoxplaza.com/public/1245281/image-05.png "image-05.png")



---

### Land​

**Nomads grow their Herd by extracting Fertility from the land**. Thus, migrating becomes an important part of their loop in the early stages of the game, when their realms are not big enough to accommodate the horde.  

County Fertility is calculated primarily based on the terrain type. Nomads deplete Fertility of the counties they hold until it stabilises at a fixed number where the Herd can be maintained. This number is mostly affected by the domain size, but Stewardship, dynasty perks, yurt buildings and other character modifiers can affect it.  

![image-06.png](https://forumcontent.paradoxplaza.com/public/1245282/image-06.png "image-06.png")



### Migration ​

When the Domain Fertility is depleted, **it's time to migrate**.  

Migration targets de jure titles, and the available title tiers you can target depend on your level of Dominance. A Nomadic ruler of Dominance level 2 can only target counties and duchies, whereas someone with level 3 can target kingdoms as well.  

This means that smaller rulers should migrate frequently, either find abandoned lands occupied by Herders, or subjugate themselves before bigger rulers. Bigger rulers in the Steppe should, on the other hand, adopt a more sedentary way of life and demand Obedience and Tribute from rulers in their sphere.  

![image-07.png](https://forumcontent.paradoxplaza.com/public/1245283/image-07.png "image-07.png")


*[This panel is subject to reorganizations and reworks.]*  

The migration screen allows you to negotiate with the local rulers. If two or more independent rulers occupy the same de jure territory, then the ruler with the highest Herd leads the negotiations with you. You can use gold, herd, or a hook to bribe them, and their acceptance depends on their relationship with you, your Dominance level relative to theirs, your Prestige, Prowess, Herd size, their traits, and other minor factors.  

**If they accept, you will start a travel plan that will take you and your herd to the desired location**. If the location had already been suggested by perhaps a courtier you may get some extra bonuses for following the desires of your people.  

![image-08.png](https://forumcontent.paradoxplaza.com/public/1245284/image-08.png "image-08.png")



However, many nomads may refuse to give up their lands, especially if they have a high level of Dominance and find themselves pretty comfortable where they are. In those cases, **one must resort to war**.  

![image-09.png](https://forumcontent.paradoxplaza.com/public/1245285/image-09.png "image-09.png")


*[Total soldiers aren't being calculated in this screenshot. Keep in mind that this is from a development build!]*  

Migration wars allow the attacker to take the lands by means of force.  

The targeted ruler will be either displaced to their other lands if they hold any titles outside of the de jure, or be made landless – similar to Administrative Noble Families or Adventurers. While landless, Nomads keep their yurts and upgrades but can't grow their Herd due to the lack of stable access to Fertility. They roam the Steppe in search of a new place to set up their tents.  

No matter how you choose to migrate, your Obedient vassals will follow you, while non obedient ones will keep their titles and lands and stay where they were. The lands that you leave behind will be occupied by someone else entirely…  

### Herders​

Nomads are not the only rulers that inhabit the Steppe. **A new unplayable government type called "Herder"** populates the map with shepherds that wander small counties. Herders replenish Fertility over time, and are extremely easy to displace, given their lack of armies. They are the ones occupying those counties left behind by migrations.  

Having a Herder as a subject is still possible, however, and they will pay a small, fixed rate of herd based on their county's fertility.  

One may also choose to voluntarily abandon one of their counties to a local herder, in the hopes that they will replenish Fertility quick enough for them to seize it back. The Steppe is not merciful, however, and another Nomad ruler may be faster than you.  

![image-10.png](https://forumcontent.paradoxplaza.com/public/1245286/image-10.png "image-10.png")


*[We indeed have several sheep variations.]*  

---

### The Great Steppe​

Life in the Steppe is not easy, and being at the mercy of the weather and pasture quality is something that nomads have had to adjust to since time immemorial (up to this day, in fact). To reflect this, we've created a seasonal system that governs the general climate of the steppe.  

The Great Steppe is divided into three subregions: Western, Central and Eastern, each of them with their own season.  

![image-11.png](https://forumcontent.paradoxplaza.com/public/1245287/image-11.png "image-11.png")


*[Another very WIP screenshot, artpass pending.]*  

**Seasons affect the Fertility of the subregion**, as a White Zud creates a thick layer of snow that prevents the animals from grazing, while a more moderate and warm weather offers the perfect climate for pastoring.  

That’s not the only effect they have though, as different seasons also change the general mood within Nomads. If a ruler extorts their vassals for Herd during an Abundant Grazing season, then they will receive more than usual, and a Severe Drought will promote characters to migrate even more than usual.  

The two special and rare seasons of Havsarsan Zud and the Blessing of the Blue Sky explore these effects even further, with the Blessing amply increasing the Fertility of the subregion and the terrible Havsarsan Zud allowing rulers to take a desperate stance, making all of their subjects obedient and getting an invasion CB on settled people. One of the academic reasons given for the Mongolian Invasion is, after all, the lack of pasture in the Steppe at that point in time.  

Your Stargazer can also help predict the next season depending on their aptitude. More on this in upcoming diaries!  

### The Gurkhan​

Only one character in the entire Steppe can go on to the highest level of Dominance and become the Greatest of Khans, but we will provide you with tools to stop them.  

**The Gurkhan is whoever has the largest Herd within the Great Steppe**. They are on their way to reach the highest Dominance and are a threat to all. Confederations may form to target them, while hostile scheming and wars may target them more frequently, and the Gurkhan will have to prove that they deserve their seat.  

---

### Your Yurt​

Nomads have no buildings. Whatever they build is carried with them when they migrate. To represent this, Nomadic Holdings cannot have any other buildings than some basic corrals, but in turn they have access to a new domicile type: the Yurt Settlement.  

Yurt Settlements have a main yurt that can be upgraded internally, and several other specialised buildings that give upgrades to pasture management, warfare, diplomacy, raiding, and more.  

![image-12.png](https://forumcontent.paradoxplaza.com/public/1245288/image-12.png "image-12.png")


*[Names and art are **not** final]*  

### Tributaries​

During this Development Diary, you may have observed my careful use of "Subject" instead of "Vassal", and here is the reason why.  

**Tributaries are a new and looser type of subject introduced with this expansion.** Nomadic Tributaries specifically have some unique qualities to them.  

The Tributary Contract governs the levels of Obligations (or Tribute) that they may pay to their Suzerain. While the tribute is being, sent all is well and a truce is held between the two of them. The tributary relationship is even inherited across generations.  

However, tributaries may become unruly over time, and if the suzerain doesn't look that threatening to them then they may eventually opt to stop paying tribute. To bring them back into the fold, a former suzerain can bring them back under tribute by force, pacifying them and extracting both resources and prestige to a greater extent.  

Nomadic Tributaries offer a payment in herd, while settled tributaries give gold to their Nomadic suzerains.  

![image-13.png](https://forumcontent.paradoxplaza.com/public/1245289/image-13.png "image-13.png")


![image-14.png](https://forumcontent.paradoxplaza.com/public/1245290/image-14.png "image-14.png")


*[Art and map visualization are still in progress.]*  

Tributaries can be obtained through a Character Interaction to Demand Tribute or through a Casus Belli. A ruler may also voluntarily offer themselves as Tribute to a Nomadic Ruler to ensure that their lands are spared from destruction.  

As with the other features covered in this dev diary, we will do a deep dive on the Tributary system at a later date.  

### Confederations​

With the rise of all these powerful and dangerous khans in the Steppe, lower-tier Nomadic rulers may decide to band together against a bigger enemy through forming a Confederation.  

For those in a Confederation, an assault on one member is an affront against all members, so everyone in a Confederation joins defensive wars being fought by fellow members. This potent defensive power is balanced against checks on expansion: as long as they belong to their Confederation, members cannot increase their Dominance or create new titles.  

### Raid Intents​

Raiding is one of the main ways Nomads have to get access to Gold. Given the importance that raiding had in their society, we have decided to expand this feature by adding Raid Intents.  

A Raid Intent allows to set a desired outcome of the raiding: you may want to raid to capture interesting characters, steal your neighbors' cattle, or simply burn their property to the ground.  

![image-15.png](https://forumcontent.paradoxplaza.com/public/1245291/image-15.png "image-15.png")


*[Art and names are placeholder, so are the intents themselves as we may change or tweak them.]*  

Some of the Raid Intents will also be available for Tribal characters, while others need specific Nomadic unlocks.  

### Nomadic Flavor​

Lastly, we are adding a number of new Character Interactions, Decisions, Activity Types, a new Vassal Stance, Events, and more focused on unique Nomadic flavour. Genghis Khan's famous storyline and Mongolian specific events will, of course, also make an appearance.  

Expect to see a Kurultai, Blood Brotherhoods, Paizas and Kublai Khan's famous Pleasure Dome. More on this to come.  

There are many things that we have left out of this Diary because **our focus is on the main mechanical features** introduced with this expansion, but we will come back to all of this in more detail in the future.  

Thanks for reading. **We are eagerly awaiting your thoughts and feedback.**

<!-- artifact:reactions:start -->
- 201 Love
- 134 Like
- 18 (unlabeled — rendered as base64 data URI)
- 13 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [hattusa](https://forum.paradoxplaza.com/forum/members/hattusa.1800793/)**
Role: Game Designer
Badges: 66
Messages: 31
Reaction score: 1,907

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
