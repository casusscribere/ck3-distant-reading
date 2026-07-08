---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1772951/"
forum_thread_id: 1772951
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 174
title: "Dev Diary #174 - The Mechanics of China"
dd_date: 2025-06-09
author_handle: Joror
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 6953
inline_image_count: 34
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1772951'
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
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_718_to_723
    action: preserved_and_flagged
    counts:
      Love: 146
      Like: 97
      (unlabeled — rendered as base64 data URI): 3
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_731_to_841
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_842_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #174 - The Mechanics of China

<!-- artifact:thread_metadata:start -->
- Thread starter [Joror](https://forum.paradoxplaza.com/forum/members/joror.528107/)
- Start date [Jun 9, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-174-the-mechanics-of-china.1772951/)
<!-- artifact:thread_metadata:end -->

Welcome to the third dev diary for our upcoming major expansion - *All Under Heaven*!  

My name is Daan Broekhof, aka Joror, a programmer on the CK3 team, and also the “feature steward” for China. What does that title mean? Well, it roughly means I am responsible for design and coordination in this area, making sure that our initial vision gets translated into intriguing, immersive, and fun gameplay.  
This Dev Diary is about the gameplay mechanics for China; we will be trying to get into as many details as we can about what we have developed so far. Because yes - the DLC is very much still being developed and being iterated on right now, and we want to hear your thoughts on what we have so far.  

Since China is the biggest focus of this expansion, many others are working on it as well, some will chime in throughout this dev diary. Hold on to your hats - this is going to be a chonky one.  

(We might repeat some of the things revealed in the previous Dev Diaries #172 “The Full Medieval World” / #173 “The Map of China” - for clarity or cohesion; if anything seems contradictory please ask away and we will attempt to clarify!)  

### China - The Central State​

One key understanding of Imperial China in the medieval era is that it is a sophisticated bureaucracy. Organized and centralized in ways seen nowhere else in the world at this time.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1308916/image_01.png "image_01.png")


*[Default paper map of 1066, centered on the Song, showing English map names - exact map coloring, drawings, naming, borders, and translations still Work in Progress!]*  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1308917/image_02.png "image_02.png")


*[Eastern paper map of 1066, centered on the Song, showing Chinese map names - exact map coloring, drawings, naming, borders, and translations still Work in Progress!]*  

It has many layers, ranging from the lowly district head to county magistrates, prefects, and provincial governors. Yet those are but the arms of the bureaucracy; in the central capital we have the heart of power: the central Ministers, the Grand Chancellor, and finally - the Emperor.  

We want you, the player, to be able to rise up within this power structure, or perhaps even harder: challenge it from the inside - or the outside.  

---

### The Celestial Government​

The government type for China is the Celestial Government - “Celestial” here is a reference to the Mandate of Heaven, the right to rule, held by the Emperor, who is also known as the Son of Heaven.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1308918/image_03.png "image_03.png")



Unique to this government type is the way that titles under the Emperor (whose title is hereditary) are managed and distributed. Similarly to the existing Administrative Government type, these titles are given to the candidate who holds the highest score whenever such a title is vacated.  

In contrast to Byzantium, the scoring calculation in Celestial Governments is heavily dictated by the Merit Rank you hold. Your governmental accreditation level, if you will. You can still spend Influence, but you will not be able to obtain a higher position unless you have reached a sufficient Rank. Having reached a sufficient rank out of the nine ranks of merit will mean having access to (and being expected to fill) positions of a certain tier, with Prefectures (Counties), Provinces (Duchies) and Circuits (Kingdoms) requiring a higher and higher rank. The Duchy level does not usually exist this way in medieval China, but we add it here for gameplay reasons.  

As you have seen in previous dev diaries, the Chinese map also has de jure empires, but these will generally not exist in a stable era. Instead, the highest point in any career is the position of Minister, an Empire tier type of position that is covered in the following section.  
Since China is so large, the Son of Heaven relies on his bureaucracy to fill vacant positions. While he can directly intervene if the situation requires, positions will generally be directly filled upon being vacated through this rank system instead of titles reverting to the Emperor, like they would in Byzantium.  

### Imperial Ministries​

**Note**: This feature is still in very active development, so is more likely to be changed, scaled up, or perhaps scaled down!  

「君之視臣如手足，則臣視君如腹心。」- 孟子  
"If a ruler regards his ministers as his hands and feet, then his ministers will regard him as their heart and mind." - Book of Mencius, Li Lou II  
(Part of the “Four Books”, which were the foundation of the Imperial Examination system during the Song Dynasty)  

The central government of a Hegemony-tier Celestial Government is an impressive feat of bureaucracy, and where some say the true power of the Chinese Empire was found.  
Throughout Chinese medieval history there were many Departments and Ministries that made up this central bureaucracy, and we’re opening up their leaders as titles and positions that players can vie for as the crown achievement of power in their civilian career! Only those with a very high Merit Rank will even be allowed to put their name forward.  

These Department heads and Ministers will replace the regular Council of the Emperor, and they will work similarly but also differently to Councillors. First off, Ministers are not appointed by the Emperor directly when vacated. Instead, they also are filled by the same mechanics that select Governors for administrative vassal titles in the Empire. You can lobby to make yourself the next Minister of Revenue, but there might be many other powerful political entities competing for these titles.  

The balance of power and the exact titles that existed for these varied during our time period. Generally speaking, the “Three Departments and Six Ministries” system existed from the Sui Dynasty (~580) to the Yuan Dynasty (~1271), and that is what we have taken as the main structure for the ministers. Additionally, we have selected two other powerful titles to be present: the Grand Chancellor and the Imperial Censor.  

Mechanically, these positions will have landless titles of the Empire Rank, to signify their power under only the Emperor himself.  

### The Wheels of Bureaucracy​

These positions will act as go-betweens between the governors and the Emperor, representing the delegated power of the Administration; the Emperor will often interact more directly with his ministers than specific governors, of which he has many. Many interactions that usually would target your liege will instead target a minister in Imperial China!  

One way for these Ministers (and the Grand Chancellor / Imperial Censor) to influence the state, is through Great Projects - which are collaborative projects that characters can start and others can contribute to. (More about this in a later Dev Diary!)  
For example, the Minister of Works could start an infrastructure improvement project targeting multiple Circuits, or the Minister of War could start a great project to start preparing for a big military campaign.  

Ministers will of course get funds - Treasury, and a salary to be effective administrators, which they can use to pursue projects or agendas.  

#### The Grand Chancellor​


![image_04.png](https://forumcontent.paradoxplaza.com/public/1308919/image_04.png "image_04.png")


*[Very initial work-in-progress view of the Grand Chancellor in the Council View]*  

Also called the “Prime Minister” or “Zai Xiang” 宰相, the Grand Chancellor is one of the most powerful political positions in Imperial China; they were the head of the entire civil administration and effectively served as the Emperor’s chief executive officer resulting in them often being seen as the highest-ranking official below the Emperor.  

This title gives many powers, and in some situations is on an equivalent level to the Emperor. This title is also at the top of the Diarch Regency list, stepping in when the Emperor is unavailable.  

#### The Imperial Censor​


![image_05.png](https://forumcontent.paradoxplaza.com/public/1308920/image_05.png "image_05.png")


*[Very initial work-in-progress view of the Imperial Censor in the Council View]*  

Leading an oversight institution called the Censorate, this role has the responsibility to investigate corruption, abuse of power, and nepotism. They also offer advice to the Emperor, and uniquely, they could challenge ministers, the Grand Chancellor, or even the Emperor himself.  

This role is very similar to the Spymaster but lifted up even more in power by the ability to publicly challenge anyone in the bureaucracy, in both matters of illegal behavior but also moral behavior.  

#### The Ministers​

These roles are less powerful than the Grand Chancellor, but more powerful than any other official in the administration of Imperial China.  


- **Minister of Personnel  
  * Oversees civil service appointments, evaluations, promotions and dismissals.**
- **Minister of Revenue  
  * Handles census data, taxation, land distribution, and state finances**
- **Minister of Rites  
  * Manages state ceremonies, rituals, foreign relations (including tributaries), and the Imperial Examination system**
- Minister of War
  * Directs military appointments, strategy, logistics and defence
- **Minister of Justice  
  * Administers laws, judicial review, prisons, and punishment**
- **Minister of Works  
  * Oversees public worlds, construction, engineering and infrastructure**

![image_06.png](https://forumcontent.paradoxplaza.com/public/1308921/image_06.png "image_06.png")


*[Very rough initial work-in-progress view of the Ministries in the Council View - yes they’re not very skilled, we know! Not all weights are in place yet]*  

#### Favor of the Emperor​

The Emperor is not without power towards his ministers & top officials of course - he can even bestow the status of “Favored Minister” on any of them, granting them more Treasury to work with, and other benefits.  

### Province/Circuit Types​

Similar to the Administrative system used in Byzantium and introduced in Roads to Power, the Celestial Government has “Province Types”; designations you can give titles (such as the kingdom sized Circuits) that specialize it for a specific purpose. In contrast to the Byzantine system, the number of each of these that you can have is often limited by the Circuit Type itself, the Dynastic Cycle Era, or specific Laws.  

We have created two primary categories of Circuit Types: Civilian and Military. These correspond to the two career paths you can choose within the machinery of the Chinese state.  

The main difference between these two categories is that the Civilian types will not have any Men-at-Arms, while the Military types will have (title bound) Men-at-Arms. When Civilian or Military governors need military assistance (for example from peasant uprisings, or worse), they can call in Military governors as allies in wars, usually requested via the Minister of War.  

Different Circuit Types will also look different on your government “CV” - your Merit. Governing these titles will grant more or less Merit, depending on their tax base size, or size of armies.  

**Note: We’re still heavily tweaking the advantages and disadvantages of each of these Circuit Types! These values are not final and definitely will be tweaked.**  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1308922/image_07.png "image_07.png")


*[Screenshot of the Chinese city holding background illustration]*  


#### Standard (Civilian)​

This is the most common type within the Empire and designates an area that is governed primarily by civilian rule. It does not usually have access to personal Men-at-Arms, or Title-bound Men-at-Arms.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1308923/image_08.png "image_08.png")


*[Tooltip of a Standard Administration circuit type - very basic, and values are placeholder]*  

#### Industrial (Civilian)​

An area of industry! Focused on production and long-term development. You can have only a limited amount of them active. It does not provide any Title Men-at-Arms.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1308924/image_09.png "image_09.png")


*[Tooltip of an Industrial Administration circuit type - values are temporary and will change!]*  

#### Metropolitan (Civilian) - Advancement Era​

A Circuit type which is focused on efficient administration of urban areas and urban development. It does not provide any Title Men-at-Arms. It can only be assigned when the Dynastic Cycle is in the Advancement Era, and is limited in number.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1308925/image_10.png "image_10.png")


*[Tooltip of a Metropolitan Administration circuit type - values are temporary and will change!]*  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1308926/image_11.png "image_11.png")


*[Screenshot of the Chinese castle holding background illustration]*  

#### Military Administration (Military)​

This administration type focuses on raising and maintaining Title Men-at-Arms and military defensiveness. Development growth is hampered, and you can have only a limited amount of them. They would usually be set on border-circuits.  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1308927/image_12.png "image_12.png")


*[Tooltip of a Military Administration circuit type - values are temporary and will change!]*  

#### Protectorate Administration (Military) - Expansion Era​

This circuit type is focused on creating a more independent military entity that could sustain and operate by itself. It can even independently expand its own realm on orders of the Emperor. It is only available if the Dynastic Cycle is in the Expansion Era, and is also limited in number.  

Usually reserved for areas further away from the Chinese core lands.  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1308928/image_13.png "image_13.png")


*[Tooltip of a Protectorate Administration circuit type - values are temporary and will change!]*  

### Your Career: Merit & Examinations​

How do you prove that you would make a good Confucian ruler? Well, just like in the modern era, you have to take your exams! Exams are the way to get started on your career within Imperial China, and other realms that have copied the system from them.  

You also get to choose your career path type: Civilian or Military. This choice determines what type of positions in the Empire you will be considered for. The Civilian path usually starts by obtaining a Civilian governorship at a low title tier, and goes all the way up to the Grand Chancellor, the right hand man of the Emperor.  

The Military path will see you sent off to defend the borders of the Empire, first in Military governorships, and later perhaps coming to the capital as the Minister of War. The Military path is also one where you will be commanded by the Emperor to wage wars or campaigns on their behalf.  

We have taken the traditional Chinese 9-rank system for Merit - which results in a reverse of the usual numbering, going from Rank 9 (starting rank) to Rank 1 (best rank).  

Historically in Imperial China, there was a Candidacy Grade (資品), which was used for exams, and the Service Grade (官品), which was used when in office. We have combined the two for simplicity.  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1308929/image_14.png "image_14.png")


*[Merit Rank of a highly successful Governor, with placeholder icons to show which examination types have been successfully completed]*  

#### Examinations​

Hi, I’m Axel, or [@PinkAxelotl](https://forum.paradoxplaza.com/forum/members/1880684/) , and I am one of the designers working on Examinations.  

As previously mentioned, Merit is key to securing government office. A character’s Merit score indicates how appropriate they are as an official in Meritorious East Asian administrative government types. It represents their documented achievements and moral conduct according to Confucian ideals. An official with a high Merit Level has a higher candidate score and (if employed) a higher salary. Characters who are not yet employed as governors can attempt to increase their merit by attending examinations.  
The rank of merit also directly corresponds to how high a position a character can hold.  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1308930/image_15.png "image_15.png")


*[Screenshot of the Imperial Examination activity in progress]*  

The examinations can be taken from the age of six via the Children’s Examination. You can set your children up for success by having them take the test, which increases their likelihood of attending higher level examinations. Next is the Provincial level, another local examination, represented in game as a multi-layered Decision. Successfully passing this test allows you to be considered for county-level appointments. More ambitious characters might set their sights on the prestigious higher-level examinations. The Imperial Examination is an in-game open activity hosted in the capital, it starts with the Metropolitan examination, from which the top ten entrants will move on to the exclusive Palace Examination, hosted by the Huangdi (Emperor) himself.  

Apart from being generally gifted, being a good student of Confucius is important to secure a good score at the examinations.  
In order to prepare, the obtaining and leveling of the Confucian Scholar trait can be achieved via studying at a university in China, or by finding a Confucian elder. More about elders and disciples later in this diary!  

Lastly, there are also other ways to succeed if you are not very gifted or you do not trust that the time you spent studying the confucian classics will be enough. There were Examinees that were known to try to bend the rules, if not outright cheat, by for instance trying to get to know their examinators in advance.  

### Your Family Estate​

When playing inside of China you will hold a family estate - to be built up over generations as a place to call your home. In some ways this is similar to your family estate in the Administrative government form from Roads to Power. This is where you can invest in permanent things that will keep benefitting your family in future generations - unlike the governorship lands which you only improve on behalf of the emperor. Unlike in Byzantium there will also be a different focus for what kind of benefits you may want. As an example, while you cannot guarantee a high merit score for your children, you can ensure that in your estate they are well educated (tracked through the Confucian education trait) as they grow up so that they may do well in the examinations.  

![image_16.png](https://forumcontent.paradoxplaza.com/public/1308931/image_16.png "image_16.png")


*[Screenshot of a simple Chinese family estate]*  

Another difference from the old domicile for administrative realms is that the things you can add to your family estate in a Celestial realm will depend on what titles and offices you currently hold. Some things you will only be able to build if you achieve specific things in your career, such as reaching the position of Minister in the central government.  

Like many other things in the diary, the estate itself is still under development, and if you have suggestions for things you think we should cover here then please let us know!  

### The Imperial Treasury & Salaries​

In Imperial China, Governors do not “own” the territory they rule over; they govern on behalf of the central government, and by extension, the Emperor. The tax you levy is not yours, they are the Empire’s. You are not supposed to spend all that on building out your estate, or to have many fancy feasts. That would be corruption; and quite illegal!  

In this organized state, taxes are instead sent to the central government, which sends back resources earmarked for government use: a budget. Governors would receive salaries, which they could spend as they please.  

To represent this central flow of money, we have implemented a new “gold flow” that is used by the Celestial government: the Imperial Treasury system. It uses a new resource called Treasury.  

![image_17.png](https://forumcontent.paradoxplaza.com/public/1308932/image_17.png "image_17.png")


*[Tooltip describing the Treasury resource]*  

It works as follows:  


1. As a vassal in the Empire, all taxes you collect from your sub-vassals and domain are sent upward to your liege, and they will send it upward similarly, until it reaches the Emperor. To contrast, Feudal Vassals send only a relative percentage up to their liege, and keep the rest.
2. The Emperor will convert a large percentage of this vassal income into Treasury, a new resource that represents liquid assets that are supposed to be spent only on governmental tasks and investments. Whatever the Emperor does not convert is added to the Emperor's own coffers of gold. (Treasury has a 1-to-1 relationship to Gold, if they ever are converted.)
3. Then the Emperor sends Treasury downward to all their governors (vassals), based on the taxes collected by each governor, plus any adjustments specific for the title they govern. Those vassals send down Treasury to their sub-vassals, etc. This could mean you might receive more Treasury from the central government than the taxes you were able to collect. For example, Military Governors in a Protectorate border circuit out in the barren desert might receive more, since they are paying for a sizable army.

At some point during the development of this system we created this flowchart, which I tweaked a bit for the Dev Diary! People like flowcharts, right?  

![image_18.png](https://forumcontent.paradoxplaza.com/public/1308933/image_18.png "image_18.png")


*[Example flowchart presenting how Taxes flow up to the Top Liege, and Treasury flow down from there]*  

What can you spend Treasury on then? All official government business! In the Celestial Government this translates to: All holding buildings, Provincial Men-at-Arms regiment costs, levy upkeep, most Great Project contributions, a few Activities, and any salaries you have to pay to your sub-vassals.  

Conversely, all the things that belong to you privately, are paid for with Gold: Estate Buildings, quite a few Activities, personal Men-at-Arms regiments, Schemes, a lot of Court Positions.  
At any given moment, you can also put your own Gold into the Treasury of your primary title, but beware, you cannot take it out again as Gold!  

Additionally, Treasury belongs to the primary title of the receiver - so if you were to lose that title, that Treasury would move away with it.  

So building up personal wealth is harder in a centralized system; you have your Estate, your Salary, and any other “shenanigans” to get Gold. Of course, there is also outright corruption - schemes and the like, and some shady Decisions. Whenever you or another governor of the Empire does so, the Dynastic Cycle slides more towards corruption.  

We have rebalanced gold costs for various existing systems to better reflect that Circuit Governors aren’t actually as rich as Kings, even though they are the same title tier.  

### The Mandate of Heaven​

The Emperor has a new Legitimacy Type - called the Mandate of Heaven, which has some additional triggers and expectations. It’s not always easy to receive the approval of the Heavens.  
Should this Legitimacy be lower than expected, then the Mandate of Heaven is in doubt - and change is in the air.  

---

### The Dynastic Cycle​

As stated in our Vision Dev Diary, the Dynastic Cycle represents the ongoing cyclical nature of Dynasties and power within Imperial China.  

![image_19.png](https://forumcontent.paradoxplaza.com/public/1308934/image_19.png "image_19.png")


*[In-development version of the Dynastic Cycle window, showing the currently active Era and Era Type]*  

The Dynastic Cycle is the tool we use to represent various different periods and ambitions of China in our game. The key periods that we want to be able to represent are:  


- **The Tang Dynasty** - An expansionist China, with more powerful independent military governors
- **The Five Dynasties & Ten Kingdoms Period** - A divided China, where many states tried to claim the Mandate of Heaven, and re-unite China
- **The Song Dynasty** - An inward looking China, where Merit, innovation, prosperity, and scholarship were held in high regard
- **The Yuan Dynasty** - A China that was conquered by an outside force, which then tried to adopt and adapt the imperial system
- **The Early Ming Dynasty** - A stronger defensive China, where the Emperor held more power over the Government, with a revival of exams and cultural writings

Since we create an alternative history from the moment we unpause the game, we want these different Dynasties and their policies and politics to be able to organically form and evolve. To do this, we created a new Situation (a type of persistent geographically bounded system) called The Dynastic Cycle, which can be in one of several possible Eras (Situation Phases), that can represent both the cyclical nature, and different types of China that existed.  

Additionally, this Situation gives China a mechanism that encourages it to be united again more easily under the Mandate of Heaven - because if we add a force that encourages a cyclical fall, it needs a counter component for a cyclical rise.  

**Historical Note**: The Dynastic Cycle is a concept that was formalized during the period that CK3 represents - and its cyclical nature was discussed in depth. For example Zhu Xi (1130-1200), a scholar during the Southern Song Dynasty, argued that the Dynastic Decline was not inevitable, and that the loss of moral virtue and ethical discipline could be prevented - if there is a structured society led by scholars, who were guided by principle and moral clarity.  

### What can each Era change?​

Each Era affects those within China in various significant ways. Aside from the usual modifiers on characters and counties, our aim is to also give each Era things that are unlocked by them, that are distinct and useful.  

These things can be:  


- Additional laws and policies that can be enacted
- New Province (Circuit) types
- New interactions towards others in China
- Great Projects that can change society/warfare/infrastructure significantly
- New Casus Belli

They can also take away some things to reflect a different nature of the realm, such as:  


- Restricting certain types of Casus Belli
- Limiting or forbidding personal Men-at-Arms

For example, in the Expansion Era, the “Grand Expansionist Command” Army Command structure law option is available, which enables larger Title Men-at-Arms armies, at the cost of a heavy burden on the vassals of China.  

**Disclaimer**: Not all effects are shown in the screenshot; also all mechanics are not final and have not yet been balanced!  

![image_20.png](https://forumcontent.paradoxplaza.com/public/1308935/image_20.png "image_20.png")


*[Example of the Army Command Structure Law, where the last option is unlocked if you are in the Expansion Era]*  

### Eras and Their Effects​

Each Era is sorted into one of the three following categories, or types:  


- **Stable Era Type**
  * Each of these represent a prosperous age - the Empire is stable, and the Mandate of Heaven is strongly held. These Eras enable extra-specialized laws, activity options, and represent to a certain extent the **stated ambition of the government and Emperor**. If the Emperor does not fulfill the ambition set forward by the Stable Era, they will suffer catalysts that drive the Era to an Unstable Era. Stable Eras generally can transition only into Unstable Eras, and not into other Stable Eras directly.
- **Unstable Era Type  
  * Whenever the Mandate of Heaven is not strongly held, and the Empire is not operating at its peak, the Dynastic Cycle is considered to be in an Unstable Era type. These Eras signify that the cycle is turning downward, but it can still be turned around with a lot of effort. If you are an ambitious servant of the Empire and you think that you can fulfill the Mandate of Heaven better than the current Emperor - now might be the time to consider your options.**
- **Chaotic Era Type  
  * Whenever the Mandate of Heaven is completely lost, the Empire is shattered, and the Dynastic Cycle is rotated to an Era full of uncertainty, wanton violence, regional independence, and potential.**

#### Advancement Era (Stable Era Type)​

In this Era, the Empire is focusing on improving itself by looking inward: through Innovations, cultural excellence, prosperity of the people, and good Meritorious Confucian governance.  

Offensive wars are more limited, preferring instead to establish Tributaries and other relationships. Great Projects can be completed faster, with the focus of the Empire being directed inward. Imperial Exams can focus on producing the best Governors that the Empire has ever seen.  

Historically the Northern Song period (960-1127) would be in this Era, and this is what China has at the 1066 start date. We also consider the Southern Song period (1127-1279) to be in this Era, even though they suffered a great loss of territory to the north, it is teetering on the edge of an Unstable Era. As such, this is also the Era active in our later start date - 1178.  

**Note**: These effects are not final! We’re still tweaking here, especially around the limitations of Wars.  

![image_21.png](https://forumcontent.paradoxplaza.com/public/1308936/image_21.png "image_21.png")


*[Screenshot with effects of the Advancement Era]*  

#### Expansion Era (Stable Era Type)​

In this Era, the Empire is focusing on growing stronger through looking outward: pacifying frontiers, expanding its reach through military force, Tributaries, and the Silk Road.  

The Empire has more tools in its belt to expand - new Casus Belli, more armies, the Imperial Exams can focus on generating great Military Strategists, and a specialized Protectorate Administration circuit type is unlocked.  

On the flip side, there are some downsides to this Era: Vassals that are not Administrative might war among themselves, it is harder to integrate lands into an ever expanding Empire. Rebellions and unrest are more likely.  

Historically the Early and High Tang periods (618-756) could be considered to be in this Era. The Early Ming period (1368-1424) could perhaps also be considered to be in this Era, until it turned more isolationist.  

**Note**: These effects are not final! We’re still tweaking here, especially around the types of Wars.  

![image_22.png](https://forumcontent.paradoxplaza.com/public/1308937/image_22.png "image_22.png")


*[Screenshot with effects of the Expansion Era]*  

#### Instability Era (Unstable Era Type)​

The Mandate of Heaven is seen as wavering; either through corruption, popular unrest, foreign invasions, the Emperor acting against their own stated ambitions, non-Meritous behavior, or all of the above.  

This is the general Era that China can be in when things are uncertain. The bureaucratic apparatus is stuttering - bringing in less taxes, corruption is easier to commit and more common, populist and peasant factions are more likely to express their discontent through violence. Distant parts of the Empire might drift away or even declare independence.  

Historically, the Late Tang Era (756-907) could be considered to be in this Era, pushed into it by the massive An Lushan Rebellion. This means that our early start date 867 is in this Instability Era.  

**Note**: These effects are not final! We are also considering creating a separate ‘Reform’ Unstable era to represent an Era willing entered into to reform from one Stable Era type to another; or might keep that concept included within this Era.  

![image_23.png](https://forumcontent.paradoxplaza.com/public/1308938/image_23.png "image_23.png")


*[Screenshot with effects of the Instability Era]*  

#### Conquest Era (Unstable Era Type)​

The Mandate of Heaven has been taken by a force that is not inherently China. This Era is specifically triggered when the Hegemony of China title falls into the hands of someone who does not have the Celestial Government or a Cultural Heritage that is not Chinese. Their Government Type will become Celestial when the Title is taken, regardless.  

This Era presents a time when the cultural cohesion of China is shaken, and with it, the Mandate of Heaven. This “foreign” Emperor can try to adopt and earn the Mandate of Heaven, and steer China into another Stable Era, or they can fall into a Chaotic Era where multiple forces strive for dominance.  

A Conquest Dynasty like this is also able to exert an aggressive outward expansion, since that is what most likely got them here in the first place. Additionally, they can try and make their Culture dominant by preferring those of their own Culture to hold governorships.  

Historically, the Yuan Dynasty period (1271-1294), which started when the Mongols under Kublai Khan conquered the majority of Southern Song, would be of this Era type.  

**Note**: These effects are not final! We’re likely to add more rebellions/uprisings, and some other minuses similar to the Instability Era.  

![image_24.png](https://forumcontent.paradoxplaza.com/public/1308939/image_24.png "image_24.png")


*[Screenshot with effects of the Conquest Era]*  

#### Chaos Era (Chaotic Era Type)​

“The Empire, Long United, Must Divide.”  

When this Era starts, the Hegemony of China title is destroyed, and all direct vassals of the Emperor become independent. Those ambitious enough can declare their own intent to claim the Mandate of Heaven and adopt a Dynastic name for their realm. The Celestial Government type is continued to be valid for these realms, but no true Emperor exists. The bureaucracy continues, but decentralized and less strong. Alliances are quickly drawn up between those sympathetic to one another or merely out of necessity.  

Historically, the Five Dynasties and Ten Kingdoms period (907-960) would be in this Era. (If you start in the early start date of 867, when the Tang is in the Instability Era, you are very likely to end up here as well, if this is your cup of tea.)  

![image_25.png](https://forumcontent.paradoxplaza.com/public/1308940/image_25.png "image_25.png")


*[Screenshot with effects of the Chaos Era]*  

What is Divided can be Re-united, however, through new Casus Belli that allow for wars to be plentiful; all in the name of the people and the Mandate of Heaven.  

![image_26.png](https://forumcontent.paradoxplaza.com/public/1308941/image_26.png "image_26.png")


*[Screenshot with the “Consolidate Land Under The Heaven” Casus Belli]*  

If one ruler achieves to control 75% of the de-jure Hegemony of China title, they can Claim the Mandate of Heaven via a Decision, and start a new Imperial Dynasty!  

They will be able to select their Imperial Dynasty Name (if they have not done so already), and select one of the five Wuxing elements for their Dynasty, coloring China on the map in one of five possible colors.  

A new Stable Era of their choosing is started, and the Dynastic Cycle turns once more!  

### Catalysts of Era Change​

We have talked about all the different Eras now, but haven’t really told you how they would flow into each other, and how you could influence this!  

Similar to Struggles from our other DLCs, the Dynastic Cycle uses Catalysts - triggered events with specific point values - to push Eras from one to another. The Dynastic Cycle usually turns relatively slowly, and Eras might last a hundred years if you balance things right.  

The general flow of Era change is: Stable Era > Unstable Era > Chaotic Era > Stable Era > etc. There are some exceptions of course!  

Unstable Eras can lead back to Stable Eras, if the tide is turned, but this generally speaking is not easy. Some Eras might trigger from circumstances; Conquest Eras specifically are usually triggered when a large war for the title of China is lost.  

Catalysts come into play primarily in the Stable and Unstable Eras, and here are some examples from the Advancement Era towards the Instability Era.  

Some Catalysts are immediate triggers for a new Era because of their weight:  


- The Hegemon loses the Mandate of Heaven - their Legitimacy is at rank zero
- A new House inherits the Hegemony title

One-off Catalysts are things that you can cause yourself:  


- The Hegemon loses a War
- The Imperial Capital is Raided or Besieged
- An Imperial House member is murdered
- A Governor embezzles from the central government

Others are more symptoms of corruption and/or incompetence:  


- The Imperial Treasury is empty
- The Hegemon appoints a Low Merit Councillor (/Minister)
- Failing to hold Imperial Exams

Yet others are political in nature - an opposing Movement is strong  


- Yearly Drift: The Expansion Movement has the most Movement Power

Our intent with these Catalysts is to give players more tools to directly start or stop catalysts from happening, so that even though the Eras might change slowly, inevitably, you can help things along or delay them significantly.  

**Note**: These catalysts are still very much under development, we’re very likely to remove/add/rebalance many of them!  

![image_27.png](https://forumcontent.paradoxplaza.com/public/1308942/image_27.png "image_27.png")


*[List of some catalysts to enter the Instability Era, from the Advancement Era]*  

### **Political Movements**​

Hi, I’m Arkadiusz, or [@PDS_Arky](https://forum.paradoxplaza.com/forum/members/1751294/) , and I am one of the designers working on the Dynastic Cycle and China. One of the new mechanics I’ve been responsible for is the Political Movements in China.  

Unlike in Byzantium, Chinese Governors can share values that transcend their personal goals. Using the Situation Participant Group feature we’ve created 4 distinct political movements in the Dynastic Cycle Situation:  


- **Pro-dynasty** - Characters in this group support the Emperor in everything,
- **Expansion** - They want to change the Dynastic Cycle to the Expansion Era,
- **Advancement** - They want to change the Dynastic Cycle to the Advancement Era,
- **Conservative** - This movement seeks to resist reform, instill a moral hierarchical order, and empower scholar-official elites.

There is also an **Unaligned** group that doesn't have any unique mechanics and doesn't represent any values, but its members are susceptible to being persuaded to join other Movements.  

In history, during the Song Dynasty, the notable reformer Wang Anshi would be the leader of the Advancement Movement (“Reformers”), and Sima Guang leader of the Conservative Movement. They would debate policy before the Emperor, eventually leading to the implementation of Wang Anshi’s “New Policies”. These two Movements would clash for over 40 years in “ethical factionalism” with ruthless purges of each other.  

![image_28.png](https://forumcontent.paradoxplaza.com/public/1308950/image_28.png "image_28.png")


*[Screenshot of Political Movements in Dynastic Cycle UI]*  

Each movement is affected by the Dynastic Cycle Eras in a different way, through character modifiers and unique unlocks. Movements will support their members by using friendly interactions and schemes between each other (and hostile against other movements), and have access to unique interactions, decisions, etc. or unique options inside them. Some of those will trigger a catalyst that will move the Dynastic Cycle in a certain direction. When in Stability, catalysts will push towards Instability, while in Instability they can either push to Chaos or back to Stability.  

![image_29.png](https://forumcontent.paradoxplaza.com/public/1308944/image_29.png "image_29.png")


*[Screenshot of interactions available towards a member of a different Movement]*  

Each movement has a Leader. A Movement Leader has access to the Emperor and can issue a unique petition via decision to further their movements goals or help fellow members. In order to become a leader, you have to prove yourself in front of other members and defeat the current leader in a political debate. As a Leader you can engage in another type of Debate in front of the Emperor to win Imperial favor, leading to your Movement becoming Empowered, granting it more powers to grow the Movement and change the Dynastic Cycle Eras.  

![image_30.png](https://forumcontent.paradoxplaza.com/public/1308945/image_30.png "image_30.png")


*[Screenshot with Make Movement’s Petition Decision by Movement Leader]*  

The Movement’s clout is expressed in a Movement Power value, which is a collection of Personal Movement Powers of all its members. There are various ways to increase the power, some permanent (gaining merit, governor trait experience, age) while others temporary (political schemes, military strength, disciples).  

![image_31.png](https://forumcontent.paradoxplaza.com/public/1308946/image_31.png "image_31.png")


*[Screenshot with list of Expansion Movement members and tooltip over Personal Movement Power]*  

![image_32.png](https://forumcontent.paradoxplaza.com/public/1308947/image_32.png "image_32.png")


*[Screenshot with Movement Power game concept tooltip]*  

We have also added a new type of relation: Elder and Disciple, to further highlight the social connections and hierarchy. The relation is tied to Merit; a Disciple needs to have less Merit than the Elder, otherwise the relation cannot be established or ends amicably. Two main ways of acquiring Disciples is to convince them to join your Movement or mentor them directly through a new political scheme. Disciples also lend their Movement Power to the Elder.  

![image_33.png](https://forumcontent.paradoxplaza.com/public/1308948/image_33.png "image_33.png")


*[Screenshot with Disciples relation in Character window and Disciple game concept tooltip]*  

![image_34.png](https://forumcontent.paradoxplaza.com/public/1308949/image_34.png "image_34.png")


*[Screenshot with Request Mentorship interaction showcasing a character becoming a Disciple]*  

In the Chaos Era, the Movements disband, but the relation prevails. The connections you made will help you keep the power base and quickly reestablish the Mandate of Heaven in your favor.  

Movements will contest each other, and a wise Emperor will make sure that there is a balance between them, less they create a Movement with so much power it could operate the Empire without him.  

---

### And More To Come​

We try to limit our dev diary size somewhat to not info-dump too much all at once, so we’ll keep it here for now… but I will post a little teaser here for more China-related mechanics that we handle in the near future:  


- **Hegemonic Tributaries** - Tributaries that are formed when outside rulers acknowledge the Hegemony, and in turn receive recognition, economic benefits - and more.
- **Great Projects** - We did not mention the Great Wall or the Grand Canal, or other obviously Chinese great projects - but rest assured, we will get there
- **Border Warfare** - We are experimenting with allowing realms to wage war on sub-vassals of big realms in certain circumstances, without immediately drawing in the top liege. This gives larger empires like the Chinese Empire more local military delegation, and also a new type of threat.
Please let us know what you think of all of these features! Many are still work-in-progress, and the more we hear from you, the better we can adjust them.  

Our next Dev Diary will be about Japan, its territories, and various mechanics. See you all next time, and 谢啦, 祝你愉快! (Thank you, I wish you happiness!)  
/Joror

<!-- artifact:reactions:start -->
- 146 Love
- 97 Like
- 17 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Joror](https://forum.paradoxplaza.com/forum/members/joror.528107/)**
Role: Second Lieutenant
Badges: 10
Messages: 187
Reaction score: 1,493

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
