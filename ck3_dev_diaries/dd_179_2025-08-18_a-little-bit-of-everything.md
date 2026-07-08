---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1855760/"
forum_thread_id: 1855760
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 179
title: "Dev Diary #179 - A Little Bit of Everything"
dd_date: 2025-08-18
author_handle: PDX-Trinexx
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3268
inline_image_count: 27
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1855760'
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
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_457_to_461
    action: preserved_and_flagged
    counts:
      Like: 119
      Love: 45
      (unlabeled — rendered as base64 data URI): 3
      Haha: 1
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_469_to_549
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_550_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #179 - A Little Bit of Everything

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Aug 18, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-179-a-little-bit-of-everything.1855760/)
<!-- artifact:thread_metadata:end -->

Hello everyone! Studio Black is working at full capacity after the traditional Swedish Summer Break, so today’s dev diary is going to cover a broad range of topics from a few different members of our development team. We’ll be talking primarily about Celestial Government mechanics, but we’re also providing a bit more detail about Border Warfare and the new Wanua government’s unique mechanics.  

---

### Treasury Budgeting​

Goeiedag iedereen, Daan here! One of the new features we’ve been iterating on since the “Mechanics of China” Dev Diary is the Imperial Treasury (or just “Treasury” for short).  

A key thing we wanted to improve is how Treasury flows to parts of the Empire that don’t have their own tax income, such as Ministries. How much should a Ministry receive from the Emperor in Treasury? Well that would depend on the economy of the Empire, which is related to the size of the realm, its development, etc. Absolute numbers like “they get 10 Treasury per month” do not scale well, if at all.  
Other centralized numbers like Salaries suffered from similar issues - what makes a high salary in 876, is a paltry sum in 1178.  

To provide a more scalable number instead of a “fixed” modifier number, we have implemented a new set of laws that distribute the Treasury excess (called “Budget Capacity”) over a number of recipients.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1343149/image_01.png "image_01.png")


*[A window showing the Treasury Budgets before budget Enactment, with changes to Ministry and Salary Budget percentages, costs and effects WIP]*  

We have added three categories for this centralized Treasury Budget:  


- Salary Budget - Treasury which goes to all vassals and sub-vassals that should receive Salaries. It is given as Gold income
- Ministry Budget - Each of the Ministries will receive a slice of this budget as Treasury income
- Military Budget - Each of the holders of Military Province Types (circuit type) will get a slice from this budget as Treasury income (in addition to their regular Treasury income that is based on Taxes sent)
Any unallocated budget will be income for the general Treasury, to be spent by the Emperor as they please.  

You can run a budget Deficit too if you desire, but it will draw from your collected Treasury. Running a Deficit could prove potent, if you want to keep your Government happy and powerful. Don’t run out of Treasury though, as being in Treasury Debt will impact you similarly to being in Gold Debt.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1343151/image_02.png "image_02.png")


*[Part of the Budgeting Window showing what running a deficit looks like - WIP]*  

#### Calculating Budget Base Rates​


![image_03.png](https://forumcontent.paradoxplaza.com/public/1343152/image_03.png "image_03.png")


*[Game concept for the Budget Base Rate]*  

How this budget is distributed among the recipients is calculated via the Base Rate. It represents what one “standard” recipient of this type would receive. Each recipient can get more or less of this Base Rate, depending on things like their Title Rank and Merit Rank (in the case of Salaries), but also potentially any individual modifiers.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1343153/image_04.png "image_04.png")


*[Breakdown of a Governor’s Salary, based on the Base Rate, the Tier of their Primary Title, and their Merit Rank]*  

**Calculation example**: Say that you have a Budget Category that would get 100 Treasury allocated to it, and it has 8 recipients, of which 6 have a “Base Rate” of 100% and 2 have a “Base Rate” of 150%.  

6 * 1.0 = 6 base rate units  
2 * 1.5 = 3 base rate units  
Total: 9 base rate units (distributed over 8 recipients)  
100 / 9 = a Base Rate of **11.1**  

Each of the normal 6 recipients would receive 11.1 Treasury per month, and the two higher-rate recipients would receive 16.6.  

#### Enacting a Treasury Budget​


Now if this Base Rate was calculated continuously, your Treasury Budget would always be “perfectly balanced”. But that is not how Budget-setting usually works in the real world, and kind of boring.  
So instead Budgets get Enacted, which sets the Base Rate to a fixed number until a new Budget is Enacted in the future.  
Is the per-recipient payout (aka the Base Rate) significantly less than the previous Budget? People will get angry - an opinion malus. If they get more, they are happier!  
Lower and Higher levels of Budget allocation for each category will also provide additional effects. For example, setting your Salary Budget very low might encourage local corruption.  

How frequently you can and should Enact a budget is still something we’re balancing.  

**Example**: You have expanded your realm, and have more vassals without a corresponding increase in tax income? You might have to give more allocation to Salaries to keep everyone at the same level, but that comes out of someone else’s slice. Piss off all the Military Governors? Or the Ministers? A rough choice. Maybe running a small Deficit for a while can’t hurt?  

#### Manipulating the Treasury Budget as a Vassal​


In Imperial China, many would come with suggestions for the Emperor on how the budget should be distributed. Political Movements will push their agenda, and a wise Emperor should heed their advice.  
Of course you can also increase the relative budget of your own Ministry / Circuit / Salary by manipulating your Vassal Contract.  


---

### Dynastic Cycle​

[@PDS_Arky](https://forum.paradoxplaza.com/forum/members/1751294/) back with more news about everything China and one extra tidbit about a new feature that will affect the whole map.  

#### Emperor Playing Favors​


Let’s start with the Son of Heaven, His Grace, The Chinese Emperor. As a Player you will have access to 2 decisions that allow you to signal what Era and which Movement you Favor. Being in the Favored Movement has an impact on the Catalysts and increases the effectiveness of influencing others (through schemes or interactions). Similarly, the Favored Era also triggers Catalysts, while also affecting the pro-dynasty movement's members' behaviour and which Era will be established when getting out of Unstable Eras. The AI doesn’t use the decisions because the AI Emperor is more malleable and follows the most powerful Movement’s wishes. Only if the pro-dynasty movement is in power does the Emperor choose based on personality: civilian- or economy-oriented will choose Advancement, while militant rulers choose Expansion. For the Favored Movement, the AI Emperor decides based on the Debate activity outcomes; more about them and Player impact in the Debates section of this developer diary.  

![image_05-06.png](https://forumcontent.paradoxplaza.com/public/1343154/image_05-06.png "image_05-06.png")


*[Decisions to choose Favored Era and Movement]*  

Based on external and internal feedback we decided to change some names of the Eras, to avoid confusion with Era Types and to better convey the state of the Cycle. Thus the names of Eras and their Types are as follows:  


- Advancement - Stable
- Expansion - Stable
- Tension - Unstable
- Conquest - Unstable
- Division - Chaotic

#### Elder & Disciples update​


The Elder-Disciple relationship is an integral part of climbing the meritorious career ladder in China, and since Merit is currently used only in Governments with Domiciles an overview tab was added to the Estates. There you can manage your Disciples and your Elder. If the Elder has other Disciples besides you, you will see them there too. In order to kickstart it, the game will assign the relationships at game start randomly (based on merit and being in the same Movement or just realm proximity). In the next step we’ve added a few shorthand interactions to more easily break existing relations or establish new ones. If you didn’t like the starting bunch or were still under the limit, you can change them. Yes, now there is a limit to how many people you can mentor at once. One of the reasons for the limit is that Disciples always follow the Elder to be part of the same Movement, thus bringing your flock would significantly swing power and make the power struggle either trivial or volatile. However, the limit can be increased, mainly by domicile upgrades.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1343155/image_07.png "image_07.png")


*[Elder/Disciple view in Domicile window]*  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1343156/image_08.png "image_08.png")


*[Find Elder interaction accessible in the new view]*  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1343157/image_09.png "image_09.png")


*[Disciples following Elder if he is convinced to join another Movement]*  

#### Live the Bureaucratic Dream​

The career path wouldn’t be complete with an ultimate goal. You would like to become the new dynasty on the Heavenly Seat. How to achieve this without breaking the Cycle? We turned to existing mechanics to represent it. Creating a new variant of the Prime Ministership Diarchy (the existing one is Vizier), called the Grand Secretariat. The regent is called the Secretary Director and will be responsible for the administrative work of the Son of Heaven, keeping the Ministers busy throughout new Mandates. The Scales of Power will provide them a way to stage a coup, just as for the Vizier.  

What’s unique about this type of regency is that it is tied to the Grand Chancellor Minister by a new realm law, available only for the Celestial Government. The law makes it flexible and allows it to be changed to follow other ministers instead.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1343160/image_10.png "image_10.png")


*[Grand Secretariat, the new Diarchy for Celestial Government]*  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1343165/image_11.png "image_11.png")


*[New way to swing the scales of power by using Movement Power]*  

### Border Warfare​

#### Nibble Around the Edges​


Leaving China for a moment, I can share more details about Border Warfare.  

Imagine two scenarios:  


- A conqueror is rampaging nearby and swallowing lands that you have claims on, so you are left with three options: murder them, fight head-on, or roll over and die.
- You restored Rome, again. And didn’t choose the hard option, again. Now you are out of challenges and can either get to tediously conquer the world or start a new Rome restoration run.

We wanted to make both scenarios more interesting, so that living next to a powerful realm is not miserable while playing as it is still challenging.  

Let me introduce Border Policy Realm Law, which will simulate that the Top Liege is busy with courtly matters in the capital, and won’t pay attention to insignificant wars over backwater counties far away. This allows characters to declare wars on vassals of that Liege and forbids the top liege from intervening for 3 years. This will make larger realms less safe and stable. Keeping peripheral, weak vassals will make them easy targets for neighbouring rulers to attack and defeat them before their Top Liege can respond. Your vassals should manage this long without your help, right? Or you can win a war yourself, before the Emperor of China realizes what you are doing in his backyard.  

The law is toggled automatically based on set triggers. At least one of these has to be true for the law to toggle:  


- Top Liege is Hegemony Tier,
- Realm Size is larger than 160 (for context this means that the Holy Roman Empire is the only other realm, besides China, that starts the game in 1066 with the law enacted),
- Top Liege’s House unity is antagonistic,
- Top Liege is in a civil war.

![image_12.png](https://forumcontent.paradoxplaza.com/public/1343166/image_12.png "image_12.png")


*[Border Policy Realm Law]*  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1343167/image_13.png "image_13.png")


*[Warnings in Declare War interface when targeting a vassal]*  


---

### Debates & Examination Updates​

Hi, I’m PinkAxelotl (or your examiner if you fancy). I’ve written about the Examinations in previous diaries. Now, I want to introduce you to a new activity intended for the Dynastic Cycle: Debates.  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1343168/image_14.png "image_14.png")


*[Debate Event]*  

Debates allow you, a member of a movement in the dynastic cycle, to either seize leadership of your movement or duke it out scholar-style with another member to become the Dynastic Cycle’s favored movement. The events in this activity are all about the interplay existing between movements, as well as about gaining disciples or an elder to support you in your meritorious journey.  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1343170/image_15.png "image_15.png")


*[Examination Event]*  

Speaking of Merit, the Examinations are your be-all and end-all for accumulating this resource. This is most true for landless administrators. With the latest rework to the activity, you can now attend an exam while landed, for the purpose of helping your family and disciples to take their exams. The different exam levels have been further fleshed out, with the Provincial Examination now being its own activity as well. This is available to host for all governments that utilize Merit. The naming convention has been changed from Imperial Examinations to Civil Service Examinations, which is how they will be referenced henceforth.  

### Clothing and Headgear for Southeast Asia​

Since we have created a lot of character art for China and Japan, we have been asked what we are doing for Southeast Asia. I'm pleased to share that we are adding a set of clothes and headgear for both men and women within the present scope.  
We have decided to base it primarily on the Khmer Empire’s attire.  

#### Clothing/Headgear​

We are adding outfits and headgear based on some amazing preserved examples, as well as sculptural and relief depictions from the ruins of Angkor in present-day Cambodia.  

![image_16-19.png](https://forumcontent.paradoxplaza.com/public/1343171/image_16-19.png "image_16-19.png")


*[Reference for male and female outfits]*  

Below is an example of a WIP female crown. The abundance of detail makes working with these a dream come true for 3D artists. (or nightmare if you’re on a tight deadline! )  

![image_20.png](https://forumcontent.paradoxplaza.com/public/1343173/image_20.png "image_20.png")


*[Female crown]*  

#### Ethnicities & General Improvements​

On top of the overall improvements to East Asian ethnicities and the addition of Chinese, Japanese, and Koreans, we are including new ethnicities for mainland Southeast Asia as well as the islands.  

Some work has also been done on base head textures and render settings which should help to improve character appearances all over the map.  

---

### Bartering​

Heyo! Chaddling here. You might have seen me writing about design choices previously, but I’m here now to talk about a new coded system we’re implementing for Wanua government: Bartering. Before you get ahead of yourselves, let’s be clear–this isn’t a trade system. Rather, it’s a unique mechanic we’ve made for Wanua characters to reflect the historical merchants of the region. All values in the subsequent screenshots will change as we balance the feature.  

![image_21.png](https://forumcontent.paradoxplaza.com/public/1343174/image_21.png "image_21.png")


*[A window showing a Bartering Army]*  

Wanua characters will be able to raise a Bartering Army that can go Barter with other characters on the map. When arriving in a Barony that has Loot, Bartering Armies exchange their Barter Goods (a new currency for Wanua characters) for that Barony’s Loot.  

The Barony then gets a nice timed modifier reducing its Loot to 0, but increasing things such as Development. Upon returning home, the Bartering Army exchanges their Loot for Gold.  

![image_22.png](https://forumcontent.paradoxplaza.com/public/1343175/image_22.png "image_22.png")


*[A WIP representation of detailed icons in the new Bartering map mode]*  

![image_23.png](https://forumcontent.paradoxplaza.com/public/1343176/image_23.png "image_23.png")


*[A WIP window showing Bartering action progress]*  

![image_24.png](https://forumcontent.paradoxplaza.com/public/1343177/image_24.png "image_24.png")


*[An interface notification showing player-facing information available when a Bartering army returns home and exchanges their Loot for Gold]*  

This is the primary way for Wanua characters to earn Gold. Most of their Buildings, Vassals, and Tributaries will not provide Gold income, but Barter Goods. Men-at-Arms will cost Gold to recruit, but Barter Goods to maintain.  

![image_25.png](https://forumcontent.paradoxplaza.com/public/1343178/image_25.png "image_25.png")


*[A tooltip showing the monthly income breakdown for Barter Goods]*  

![image_26.png](https://forumcontent.paradoxplaza.com/public/1343180/image_26.png "image_26.png")


*[Men-at-Arms detailed tooltip showing maintenance paid in Barter Goods]*  

Raiders are hostile to Bartering Armies outside the latter’s home realm and can engage them in combat to seize their Loot.  

![image_27.png](https://forumcontent.paradoxplaza.com/public/1343182/image_27.png "image_27.png")


*[A debug tooltip for showing how Bartering Armies are considered hostile for Raiding Armies and vice-versa]*  

This whole system is unlocked by a new government rule, which can be added to any government should modders wish to do so. In tandem with that there are a slew of new defines and script support, including triggers, effects, and on-actions that are available to customize the system.  

Hope you’ve enjoyed this quick look at our unique mechanic for Wanua characters in Southeast Asia! Chad out.  

### Administrative Window Updates​

Hello, Jens here. Even though we’re mainly working on the Eastern parts of the world this time around, this UI update will change all of our Administrative realms, including Byzantium.  

![image_28.png](https://forumcontent.paradoxplaza.com/public/1343183/image_28.png "image_28.png")


*[A window for administrative governments displaying a list of all titles in the realm and what actions you can take in its subwindow as you select one of them]*  

Here we’ve reduced the size of the Coat of Arms to make space for additional details, and we’ve added a couple of shortcut buttons, such as changing the vassal directive. Opening a title’s details here now lets you control its Thematic Army directly, which was previously possible only through the Military View.  

The Noble Families tab looks fairly similar, with the addition of displaying the % of counties the house is ruling over within the realm.  

![image_29.png](https://forumcontent.paradoxplaza.com/public/1343184/image_29.png "image_29.png")


*[A tab in the administrative government window displaying a list of all noble families in the realm with the most important characters featured at the top]*  

Additionally, we’ve added the “Your Family” tab! This will be the window’s primary tab when opened. Here you gain a quick overview of your family members and can easily plan and manage their title appointments from each character’s perspective. Previously the only way was to first select a title and then scroll to your preferred candidate.  

![image_30.png](https://forumcontent.paradoxplaza.com/public/1343185/image_30.png "image_30.png")


*[A tab in the administrative government window displaying a list of all your family members where you can manage their title appointments]*  

![image_31.png](https://forumcontent.paradoxplaza.com/public/1343186/image_31.png "image_31.png")


*[A tab in the administrative government window displaying a list of all titles in the realm your selected family member could be appointed to. Clicking a title opens up a subwindow where you can influence their candidate score.]*  


---


And that’s all we have for today! We hope you’ve enjoyed this brief look at some of the things we’re currently working on for All Under Heaven. We’ll be back on Thursday to discuss more about our other DLC coming out soon, Coronations, so be sure to check back then for a detailed breakdown.

<!-- artifact:reactions:start -->
- 119 Like
- 45 Love
- 12 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 18 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
