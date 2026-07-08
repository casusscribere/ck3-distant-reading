---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1575051/"
forum_thread_id: 1575051
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 120
title: "Dev Diary #120 - Systemic Refinements"
dd_date: 2023-03-21
author_handle: rageair
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 6278
inline_image_count: 45
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1575051'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2250.jpg?1679403584
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_712_to_716
    action: preserved_and_flagged
    counts:
      Love: 488
      Like: 246
      (unlabeled — rendered as base64 data URI): 6
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_724_to_836
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_837_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2250.jpg?1679403584)
<!-- artifact:thread_banner:end -->

# Dev Diary #120 - Systemic Refinements

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Mar 21, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-120-systemic-refinements.1575051/)
<!-- artifact:thread_metadata:end -->

Greetings!  

Today, we’ll take a look at some of the smaller but numerous changes we’ve made to various systems, as well as some of the more notable quality-of-life changes. We want the game to stay challenging and immersive, especially now that we’re providing a host of new tools to deal with, for example, Vassal dissatisfaction - but we also want to tackle older balance issues, while weaving new solutions into upcoming changes! Of course, this includes us looking at a lot of community feedback from previous rounds of balancing (such as when we updated how the AI built Buildings in the Friends & Foes update).  

In this Diary, we will delve into Vassal Stances, Men-at-Arms Stationing, Domain Limit Rebalancing, the Building Slot Revamp, Rebalanced & New Buildings, the Improved Personality Tooltip, Rich Presence, Destroying Artifacts/Aniconism, and Improvements to the Current Situation. Grab a beverage of your choice and get comfortable, this is going to be a long one!  

There’s a lot to get to (and this isn’t everything that’ll be in the update - just a generous sample!), so without further ado:  

## Vassal Stances​

A common dilemma historically for CK has been Opinion inflation - after a while, your Vassals will like you so much by default that you won’t have internal problems anymore. It’s also very common that you’ll end up in a situation where all of your Vassals either hate you or love you - there’s very little nuance outside of having the odd rival. For this reason, we’ve introduced the concept of Vassal Stances.  

Every Vassal has a Stance that affects what they like or dislike, and the Stance they choose is dependent on their personality (and a few outside factors like Cultural ethos or Innovations). Depending on the constellation of Stances in your realm, you might have to consider what to do or not do much more seriously than before.  


![1-vassal-stance-summary.png](https://forumcontent.paradoxplaza.com/public/946831/1-vassal-stance-summary.png "1-vassal-stance-summary.png")


*[Image - Vassal Stance summary in the Realm Tab]*  

The Vassal Stances are Courtly, Parochial, Glory Hound, Zealot, Minority, and Minor Landholder. Note that they are not political groups, but rather a common outlook on things - a shared view on how a realm should be governed. For example, while all Parochial Vassals will gain an Opinion boost whenever you build or upgrade a Holding and lose Opinion every time you declare a non-trivial war (when you attack someone that has 80%+ of your Military strength) - it doesn’t mean that they like each other any better, just that they like the same things in a Liege.  


![2-temples.png](https://forumcontent.paradoxplaza.com/public/946832/2-temples.png "2-temples.png")


*[Image - Parochials and Zealots like when you build or upgrade Temples]*  


Every Stance also prefers one specific Heir, and if that heir succeeds you, they’ll get an Opinion boost… but you’ll also get an Opinion penalty with every Vassal who preferred someone else.  


![3-preferred-unpreffered.png](https://forumcontent.paradoxplaza.com/public/946833/3-preferred-unpreffered.png "3-preferred-unpreffered.png")


*[Image - Preferred/unpreferred opinions]*  


Stances prefer Heirs based on a variety of reasons, but most often they either want a Liege similar to them - or one that they believe would serve their interests. They will naturally trend away from children and Heirs of non-preferred genders, unless they don’t like any of the alternatives.  


![4-heir-preferred.png](https://forumcontent.paradoxplaza.com/public/946834/4-heir-preferred.png "4-heir-preferred.png")


*[Image - Fortunately, the oldest son is preferred by three Stances]*  


It is possible to see what Stance a character has directly in the character window. If it’s your Vassal, it’ll show an icon next to their Opinion; if the character is not your Vassal, you can still see their Stance by looking at the expanded personality tooltip (more on this later).  


![5-vassal-stance-characterview.png](https://forumcontent.paradoxplaza.com/public/946835/5-vassal-stance-characterview.png "5-vassal-stance-characterview.png")


*[Image - Vassal stances in the character view]*  


The different Vassal Stances are as follows:  


- **Courtly**
  * Courtly Vassals believe in nobility and tradition, and wish to preserve existing hierarchies. Social or compassionate Vassals often adopt this Stance.
  * Courtly Vassals like when their Liege:
    + Gives them Court Positions
    + Creates new Titles
    + Invites them to Feasts
  * Courtly Vassals dislike when their Liege:
    + Gives Titles to Lowborn characters
    + Disinherits non-disputed Heirs
  * They prefer social and compassionate Heirs with a high Diplomacy skill
- **Parochial**
  * Parochial Vassals want stability, decentralization, and peace, and for the realm to stay out of outside affairs. Honorable or reserved Vassals often adopt this Stance
  * Parochial Vassals like when their Liege
    + Constructs or upgrades Holdings
    + Makes them Guardians of Close Family
    + Uses the Domestic Affairs council task
  * Parochial Vassals dislike when their Liege:
    + Has High Crown Authority
    + Declares non-trivial Wars (Attacks someone with 80%+ of their military strength)
  * They prefer honorable and rational Heirs with a high Stewardship skill
- **Glory Hound**
  * Glory Hound Vassals care about standing and Prestige, and showing the world the strength of the realm they're part of. Bold or uncompassionate Vassals often adopt this Stance
  * Glory Hound Vassals like when their Liege:
    + Has any Partition succession law
    + Achieves Victory in offensive Wars
    + Invites them to Hunts
  * Glory Hound Vassals dislike when their Liege:
    + Has high Crown Authority
    + Signs Defeat or White Peace in Wars
  * They prefer bold and brave Heirs with high Martial skill
- **Zealot**
  * Zealot Vassals are focused on matters of the Faith, and are swayed by pious actions. Zealous or vengeful Vassals often adopt this Stance, as do the Clergy
  * Zealot Vassals like when their Liege:
    + Constructs or upgrades Temples
    + Succeeds with the Learn Language scheme
    + Has Virtuous Traits
    + Goes on Pilgrimages
  * Zealot Vassals dislike when their Liege:
    + Asks the Head of Faith for Gold
    + Has Sinful Traits
  * They prefer zealous and virtuous Heirs with a high Learning skill
- **Minority**
  * Minority Vassals feel that their Faith or Culture is marginalized by their Liege. Vassals of Hostile Faiths or Cultures with less than 30% acceptance often adopt this Stance
  * Minority Vassals like when their Liege
    + Uses the Promote Cultural Acceptance task (as they will often change Stance when above 30% Cultural Acceptance)
  * Minority Vassals dislike when their Liege
    + Converts the Faith or Culture of a County
    + Has high Crown Authority
  * They prefer honorable and compassionate Heirs, preferably of another Faith or Culture than their current Liege
- **Minor Landowner**
  * Minor Landowner Vassals wish for freedom and low taxes. All Baron-tier rulers will adopt this Stance
    + Minor Landowner Vassals like when their Liege:
      - Has low Crown Authority
    + Minor Landowner Vassals dislike when their Liege
    + Revokes Baronies
    + Has high Crown Authority
  * They prefer generous and compassionate Heirs

There’s also some nuance in how these Stances are affected by various systems in the game - Crown Authority, for example: Courtly Vassals care less about high Crown Authority, but are also less pleased than other Vassals with low Crown Authority. Glory Hounds and Courtly Stances care a lot about Court Grandeur, and so on. It’s very likely that we’ll add more things that the Stances like or dislike in the future.  

When landing a new Vassal, there’s a preview telling you which Stance they’ll take, adding an extra layer of consideration to your choices.  


![6-stance-adoption.png](https://forumcontent.paradoxplaza.com/public/946836/6-stance-adoption.png "6-stance-adoption.png")


*[Image - Landing a lowborn character will upset Courtly Vassals (based on amount of titles given), you can also see that they’ll adopt the Zealot Stance]*  


In addition, we’ve replaced almost all instances of Vassal Opinion with new Stance Opinions, which should make choices much more interesting. We’ve also replaced quite a few instances of other Opinion types that more often than not were equivalent to ‘general Opinion’, for example, a lot of same-faith Opinion has been replaced with Zealot Vassal Opinion.  

Many Personality traits have been updated to have positive and negative Vassal Stance Opinions as well, to make certain strong traits a bit weaker, and some weak traits stronger (within reason). You will also see Opinion with Vassal Stances feature in new content!  


![7-patient.png](https://forumcontent.paradoxplaza.com/public/946837/7-patient.png "7-patient.png")


*[Image - Patient now specifically pleases two Stances, rather than every Vassal]*  

## Men-at-Arms Stationing​

Another thing we’ve wanted to solve for some time now is Men-at-Arms modifier stacking - Buildings used to give global bonuses to various MaA types, which would either be very underwhelming (the bonuses are quite low individually) or extremely overpowered (Building barracks everywhere and having nothing but Heavy Infantry MaA would let you defeat anything and anyone). For this reason, we’ve introduced Men-at-Arms Stationing.  

You can now station your MaA regiments in Domain Holdings, which gives them bonuses. Each Holding can have one stationed MaA regiment, so you’ll have to choose wisely which regiments you station where. Stationing is entirely optional, and in case of conquest or inheritance you will not lose your units - they’ll simply become unstationed.  

There are a lot of Buildings that give bonuses, both generic and to specific types - this means that you might have a Holding that is especially good at boosting Pikemen or Archers, for example. With time and effort, you’ll be able to specialize Holdings to well and truly boost a specific type of MaA, making your units the envy of the world - more on this later in the Dev Diary.  


![8-maa-bonus-building.png](https://forumcontent.paradoxplaza.com/public/946838/8-maa-bonus-building.png "8-maa-bonus-building.png")


*[Image - Example of a Building with a MaA bonus]*  


To station a unit, you go to them in the Military interface, where you’ll find a station button (there’s also a new Current Situation item that takes you there - along with a new tutorial explaining in detail how to station them).  


![9-unstationed.png](https://forumcontent.paradoxplaza.com/public/946839/9-unstationed.png "9-unstationed.png")


*[Image - Unstationed MaA regiment]*  


When stationing, you can see exactly what bonuses you would get from stationing them in a specific Holding, making your choice easy. It also shows where other regiments are already stationed by coloring the province blue.  


![10-stationing-mapmode.png](https://forumcontent.paradoxplaza.com/public/946840/10-stationing-mapmode.png "10-stationing-mapmode.png")


*[Image - Stationing mapmode]*  


After you’ve stationed a unit you can see where they’re stationed in their card, along with the bonuses and a breakdown of sources. You can re-station a unit at any time, except when it’s raised, you’re at war, or the Holding is besieged or occupied.  


![11-stationed.png](https://forumcontent.paradoxplaza.com/public/946841/11-stationed.png "11-stationed.png")


*[Image - A stationed regiment]*  


You can also see from the province interface whether a unit is stationed there, along with a handy button to go to them, should the Holding be yours.  


![12-stationing-provinceview.png](https://forumcontent.paradoxplaza.com/public/946842/12-stationing-provinceview.png "12-stationing-provinceview.png")


*[Image - Stationing in the province view]*  


All of this feeds directly into the following two sections:  

## Domain Limit Rebalance & Building Slot Revamp​

After the big economical AI update that came in the Friends & Foes update, one point of feedback that came up frequently was that it felt like rulers had too few vassals left - this is obviously an issue in a game about personal relationships. We don’t want to limit the AI in arbitrary ways, so we took a look at the game and one of the things we found was that Domain Limits, on average, were very high, even for mediocre rulers. Most of the ‘problematic’ Domain Limits we found to be coming from Innovations, which gave a total of 4 Domain limits over the course of the game. Stacking Stewardship was also a bit too good compared to any other skill.  

Because of this, we’ve removed two instances of Domain Limit increase from Innovations (you now get +1 Domain Limit in the Tribal era, and +1 in late medieval), and we’ve increased how many points of Stewardship you need for +1 Domain Limit to 6 from 5… **BUT!**  


![13-updated-innovation.png](https://forumcontent.paradoxplaza.com/public/946843/13-updated-innovation.png "13-updated-innovation.png")


*[Image - One of the Innovations that have been changed]*  


We know that a lot of players enjoy the ‘gardening’ aspect of having a large Domain, and we didn’t want to just lower the Domain Limit and make the game less fun for those players - instead we’ve opted for a different solution, where each Holding grows in power and ‘gardening potential’ with time as Innovations are unlocked. As an added benefit this makes the Building/economical game feel different between the early and late eras.  


![14-no-slot-innovation.png](https://forumcontent.paradoxplaza.com/public/946844/14-no-slot-innovation.png "14-no-slot-innovation.png")


*[Image - A fresh 867 starting County Capital Holding, with a Culture that hasn’t unlocked any +Building Slot Innovations]*  


For those of you who still want to have a higher/lower Domain Limit, we’ve added a game rule where you can modify all rulers in the world by +3/+2/+1 or -1/-2/-3 Domain Limit, should you desire.  


![15-domain-limit.png](https://forumcontent.paradoxplaza.com/public/946845/15-domain-limit.png "15-domain-limit.png")


*[Image - The new Domain Limit game rule]*  


Holdings currently have 3-4 Building Slots in the live version of the game. We’ve lowered the base limits by -2 - which means that, without any Innovations, a primary Holding has 2 Building Slots, and a secondary Holding 1. Innovations can increase this limit by +4, making the maximum amount of Buildings in the same Holding 6 - two more than the previous maximum.  


![16-lategame-holding.png](https://forumcontent.paradoxplaza.com/public/946846/16-lategame-holding.png "16-lategame-holding.png")


*[Image - A late-game Holding with 6 Building Slots, a duchy Building Slot, and a special Building Slot, quite spectacular]*  


These changes should, while keeping Domains a tad smaller than before, increase the potential for ‘gardening’ - as now you can improve and specialize your Holdings over time. Instead of locking in your Building choices within the first few years of each game, you will now make choices throughout the entire duration - and there are even Buildings that don’t unlock until later eras. Building Slots are kept on a per-Culture basis, but a Holding can never lose any Building Slots they’ve gained, should the Culture change.  

Of course, just increasing the number of Building Slots isn’t very fun if there’s nothing interesting to build, which leads us to…  

## New Buildings & Building Balance​

Firstly, we took a look at Buildings from a holistic perspective - while it’s fun to build, you easily hit a point where it becomes trivial to build whatever you want because of how much gold income you have. For this reason, we’ve revamped the cost progression of all Buildings - there are still Buildings that are cheap, expensive, and so on, but overall costs will go up significantly in the mid to late game. While it might look like individual economic Buildings might not repay their cost on paper, the truth is that there are so many sources of compounding income in the game - from development, lifestyles, traits, and other Buildings adding on tax % multipliers - that they always do, especially with smart planning. Costs at the start of the game (the first two Building levels) are still static, so the early buildup phase isn’t disturbed too much, but later on, the curve will start going up markedly - making your choices more meaningful and adding additional layers of risk to managing your gold.  


![17-cost-difference.png](https://forumcontent.paradoxplaza.com/public/946847/17-cost-difference.png "17-cost-difference.png")


*[Image - Example cost difference between level one and level five Farms & Fields]*  


Secondly, we’ve revamped a lot of Buildings - especially Military Buildings - to be more interesting and worthwhile to build. We want there to be a reason to deliberate your choice of Buildings, and not always go for the best economic Buildings in every Holding you own. Military Buildings now make use of the new MaA Stationing bonuses, they have effects on Travel Danger, and almost always have secondary and tertiary bonuses unlocked for later Building levels. We’ve also lowered/removed several sources of Levy % boosts (such as from skill and council jobs) to make levies from Buildings more important, and as overall MaA damage is going to be much higher, Levy Reinforcement Rate is also going to be more important than before. There are way too many changes to go over, so here are two examples:  


![18-military-buildings-updated.png](https://forumcontent.paradoxplaza.com/public/946848/18-military-buildings-updated.png "18-military-buildings-updated.png")


*[Image - Updated versions of level 1, 3, and 5 of two older Military Buildings]*  


We’ve also made an effort to normalize the different Buildings so that going for Heavy Infantry Buildings/bonuses isn’t a no-brainer choice.  

Older economic/fortification Buildings are mostly the same, with some notable exceptions/changes - all fortification Buildings now give Travel Danger reduction and some MaA bonuses depending on their type, and most combat-oriented bonuses have been replaced on economic Buildings.  


![19-building-updates.png](https://forumcontent.paradoxplaza.com/public/946849/19-building-updates.png "19-building-updates.png")


*[Image - Hunting Grounds no longer give cavalry bonuses, and Fortifications give small MaA stationing bonuses]*  


Practically all Duchy Buildings have been updated to account for the new modifiers, providing a further specialized boost to MaA should you choose a line such as Jousting Grounds. Many of them also tie in with various Activities and with Travel.  


![20-crown-smithies.png](https://forumcontent.paradoxplaza.com/public/946850/20-crown-smithies.png "20-crown-smithies.png")


*[Image - Crown Smithies (formerly known as Blacksmiths) now provide several new bonuses]*  


As there are now many more Building slots to fill, we want there to be plenty to choose from! We’ve added 10 new Building lines, some generally available and some in specific terrains, that allow you to specialize your Holdings to your heart's content. Here we’ll present a random Building level for each, along with a short explanation of their uses. First up, the generally available ones!  

The Stables line of Buildings replace the Hunting Grounds in boosting light and heavy cavalry. They also have an added tactical benefit of making your armies slightly faster - allowing you to more easily counter an enemy army in terrain favorable to you. In addition to this, Stables make your travels faster, and also unlock the ‘Superior Mounts’ Travel Option at Building level 4+.  


![21-stables.png](https://forumcontent.paradoxplaza.com/public/946851/21-stables.png "21-stables.png")


*[Image - Stables, Building lvl 4]*  


Blacksmiths are the jack-of-all-trades MaA-boosting Building, being one of very few Building lines that boost any unit type stationed in the Holding. Blacksmiths are also an ‘economy compounding’ line, granting a tax % boost to the Holding. This line also focuses on Levy Reinforcement Rate, which as mentioned before is more important now. At Building level 5+, Blacksmiths also boost Artifact quality (which is extra relevant now, as we’ve replaced the limitation on the Commission Artifact decision to only produce Common items with a flat -20 quality decrease - blacksmiths can help offset this). To avoid confusion, the Duchy Building line has been renamed ‘Crown Smithies’.  


![22-blacksmiths.png](https://forumcontent.paradoxplaza.com/public/946852/22-blacksmiths.png "22-blacksmiths.png")


*[Image - Blacksmiths, Building lvl 5]*  


Depending on where in the world you are, the regional ‘hardy warriors’ were famed for either having stalwart infantry (example; Scotland, Tibet, Southern India) or merciless cavalry (example; Spain, Anatolia, the Steppe). Hilly and Mountainous terrain now allow you to construct one of two Building lines, depending on the geographical region, to represent the fact that warriors from there are exceptionally hardy. Tribal rulers can also construct these lines.  

Hillside Grazing lands are a military-economy hybrid Building that boosts all kinds of cavalry, making it perfect to combine with the Stables or Camelry line of Buildings (and the Horse Herds one if located in the Steppe). You can also use this to improve the economy of an otherwise rather poor terrain type.  


![23-hillside-grazing.png](https://forumcontent.paradoxplaza.com/public/946853/23-hillside-grazing.png "23-hillside-grazing.png")


*[Image - Hillside Grazing, Building lvl 5]*  


Warrior Lodges are a pure Military Building line, giving a lot of levies and bonuses to all kinds of infantry. Combining this line with Blacksmiths and either Barracks or Military Camps can make for fearsome soldiers - especially since stationing regiments here will give them the Pursuit statistic, if they didn’t already have it.  


![24-warrior-lodges.png](https://forumcontent.paradoxplaza.com/public/946854/24-warrior-lodges.png "24-warrior-lodges.png")


*[Image - Warrior Lodges, Building lvl 5]*  


The next Building line is regional in nature - limited to India, for Cultures with the Wootz Steel Innovation, and only in coastal/riverside Holdings at that. Representing a fantastic technique of forging, the Wind Furnaces are incredibly powerful. Not only is it a military/economy hybrid line, but it boosts any type of MaA stationed there with the highest possible Building bonus we’re willing to hand out. The rarity of this Building line makes Holdings that can construct them well-worth fighting over. Oh, and they also boost Artifact quality of Weapon and Armor inspirations!  


![25-wind-furnace.png](https://forumcontent.paradoxplaza.com/public/946855/25-wind-furnace.png "25-wind-furnace.png")


*[Image - Wind Furnaces, Building lvl 5]*  


For the Steppe, there’s a unique Building line that, you guessed it, boosts cavalry. It is possible to combine this Building with others, making Steppe rulers truly fearsome. With enough of these built, steppe armies will ride (and raid) along the steppe at blazing speeds. Tribal rulers can also construct this line.  


![26-horse-herds.png](https://forumcontent.paradoxplaza.com/public/946856/26-horse-herds.png "26-horse-herds.png")


*[Image - Horse Herds, Building lvl 8 - note the Genghis Khan quote in the description]*  


Next up, we have four late-game Buildings. These are unlocked by Innovations in the High Medieval Era, which allows us to make them stand out and be more powerful than a Building you can construct in 867. These Buildings allow you to massively specialize your provinces, or unlock new ways to utilize your MaA. They’re well worth saving a slot (or two) for.  

Firstly we have the Workshops Building line, unlocked by the Advanced Bowmaking Innovation. This line has an income bonus similar to a standard economy line, but can be constructed in any terrain. It also boosts siege weapons, and will eventually reduce the cost of archers and skirmishers. It also adds a flat siege value to any unit stationed there, making it good not only for stationing siege weapons but also units of low-quality MaA.  


![27-workshops.png](https://forumcontent.paradoxplaza.com/public/946857/27-workshops.png "27-workshops.png")


*[Image - Workshops, Building lvl 4]*  


The following three Building lines are very powerful because of their compounding effect on the local economy. They all have different criteria for being built, based on geographical region and terrain. There are a few holdings in the world that can build two or even three of these - keep an eye out for those, as they have the potential of being incredibly good Capitals. For example, Dumiyat in Egypt.  


![28-building-lines.png](https://forumcontent.paradoxplaza.com/public/946858/28-building-lines.png "28-building-lines.png")


*[Image - Dumiyat can build all three Building lines]*  


First out we have Windmills... Which are unlocked by the Windmills Innovation! They are the most powerful economy and development Building in the game and are common throughout places such as Europe and India - commonly built on flatlands or coasts.  


![29-windmills.png](https://forumcontent.paradoxplaza.com/public/946859/29-windmills.png "29-windmills.png")


*[Image - Windmills, Building lvl 1]*  


Watermills are a bit less powerful, but still well worth it. They, too, are unlocked by the Windmills Innovation. Commonly built in hills, mountains, forests, or next to rivers, they make further construction in the Holding easier, while boosting the economy of the entire County.  


![30-watermills.png](https://forumcontent.paradoxplaza.com/public/946860/30-watermills.png "30-watermills.png")


*[Image - Watermills, Building lvl 3]*  


The Caravanserai, while the weakest at boosting Development, have a whole host of interesting effects. They are unlocked by the Guilds Innovation. Reducing the cost of mercenaries and MaA alongside bonuses to Artifact quality and defensibility, they fill a different niche while still being extremely strong economically. They are commonly built in deserts or drylands.  


![31-caravanserai.png](https://forumcontent.paradoxplaza.com/public/946861/31-caravanserai.png "31-caravanserai.png")


*[Image - Caravanserai, Building lvl 4]*  


Finally, here’s an example of what you can achieve in the late-game if you tailor your economy well. This regiment of Heavy Cavalry costs 3,4k gold to recruit, and these are their stats after spending roughly 20k gold on Buildings in their stationed holding - hardly a trivial amount, and one that took a lot of careful planning to achieve.  


![32-lategame-heavycav.png](https://forumcontent.paradoxplaza.com/public/946862/32-lategame-heavycav.png "32-lategame-heavycav.png")


*[Image - Late-game Heavy Cavalry stationed in a near-perfect Holding]*  

We hope that these updated and new Buildings will breathe some fresh life into the management part of the game, and we look forward to seeing just how you will specialize your Holdings!  

## Improved Personality Tooltip​

As you saw in one of the earlier screenshots we've also given the AI personality tooltip an overhaul so that it is now much more informative: each line can be looked at and gives an explanation of how the AI will act in a bit more detail.  


- **Character Personality**: How they are likely to act based on their character traits.
- **Economical Archetype**: Only for rulers, how they are likely to spend their money, reflects the changes from Friends & Foes in how the AI will build up or save.
- **Vassal Stance**: Only for Vassal rulers, what Vassal Stance they are in.

![33-personality-tooltip.png](https://forumcontent.paradoxplaza.com/public/946863/33-personality-tooltip.png "33-personality-tooltip.png")


*[Image - Personality Tooltip]*  


The character personality tooltip specifically now gives a bit more of an explanation as to what being an Evil Blackguard *actually* means for how this character is likely to act:  


![34-blackguard.png](https://forumcontent.paradoxplaza.com/public/946864/34-blackguard.png "34-blackguard.png")


*[Image - Evil Blackguard personality]*  


Here are a few more examples of different personalities that will now be explained a bit more:  


![35-paragon.png](https://forumcontent.paradoxplaza.com/public/946865/35-paragon.png "35-paragon.png")


*[Image - Fearless Paragon personality]*  


![36-thinker.png](https://forumcontent.paradoxplaza.com/public/946866/36-thinker.png "36-thinker.png")


*[Image - Compassionate Thinker personality]*  


And an example of how the economical archetype tooltip looks:  


![37-cautious.png](https://forumcontent.paradoxplaza.com/public/946867/37-cautious.png "37-cautious.png")


*[Image - Cautious economical archetype]*  

## Rich Presence​

A smaller but fun change that is also coming is that we've enabled "Rich Presence" in Steam. This means that when you or your friends are playing the game, you’ll be able to see a little flavor in your Steam friends list, indicating what specifically they are doing in the game. Are they on a Grand Tour across the realm visiting their vassals? Maybe they are scheming to make a new friend? Or maybe they've just murdered their brother and are known as a dishonorable Kinslayer!  

Generally we made the flavor text prioritize temporary ongoing actions first before falling back to interesting things about your character and realm before going on to describe the more mundane.  
We've made sure that any flavor which could reveal your more nefarious actions in progress ***are not shown*** if you are in a multiplayer game, so no need to worry about your murder schemes being exposed to your friends in multiplayer.  

Of course, there is also an option to disable this information entirely and simply display that you are playing Crusader Kings III, as before.  

Here are a few examples of the flavor text we've added, and we’d love to see some suggestions from you too!  


![38-rich-presence.png](https://forumcontent.paradoxplaza.com/public/946868/38-rich-presence.png "38-rich-presence.png")


*[Image - Rich Presence examples]*  

## Destroy Artifact / Aniconism​

A much-requested feature will make it into the next update - if you’re fighting (and winning) in a lot of Tournaments you will inevitably end up with a pile of prizes and no room to show them! Or you might be in a lot of wars looting Artifacts from sieges that you’ll never use. Sometimes it’d be nice to simply break down an Artifact for its monetary value - and now you can do so with the Destroy Artifact button.  


![39-destroy-artifact.png](https://forumcontent.paradoxplaza.com/public/946869/39-destroy-artifact.png "39-destroy-artifact.png")


*[Image - Destroying a common Artifact]*  


Any ruler can destroy Common and Masterwork Artifacts, as they create a lot of clutter. When doing so, you’ll get an amount of gold that is a little bit less than half of what it’d cost to commission such an Artifact in the first place.  

To destroy Famed and Illustrious Artifacts you have to follow a Faith with the Aniconism tenet. Aniconists like Qarmatians (which didn’t have this tenet before) and Iconoclasts gain piety when destroying artifacts, and an especially strong boost to piety if they destroy religious relics of any Faith. This puts an interesting and immersive spin on an otherwise quite uninteresting tenet!  


![40-destroy-aniconist.png](https://forumcontent.paradoxplaza.com/public/946870/40-destroy-aniconist.png "40-destroy-aniconist.png")


*[Image - Destroying an illustrious artifact as an Aniconist]*  


![41-aniconism-updated.png](https://forumcontent.paradoxplaza.com/public/946871/41-aniconism-updated.png "41-aniconism-updated.png")


*[Image - New Aniconism tenet effects]*  

## Current Situation Improvements​

A tool that everyone uses, both new players and veterans, is the Current Situation widget - a handy collection of information, both pressing and not, that helps you decide what to do. Until now, this interface has not been as informative as it could be - with entries lacking information, and visual recognizability being quite low. We’ve made an effort to remedy that and make each and every entry as visually distinct and informative-at-a-glance as possible.  


![42-current-situation-updated.png](https://forumcontent.paradoxplaza.com/public/946872/42-current-situation-updated.png "42-current-situation-updated.png")


*[Image - Example of a game-start Current Situation list]*  


As you can see, we’ve added icons to all entries, which relate to the category they fall under. All Alliance situations will use the Alliance flag icon, for example. Where possible we’re adding information directly into the entries: for example, anything regarding marriage will state their relation to you, age, and place in your line of succession. Potential inheritances will state whether or not the title is within your realm, making you instantly aware if it’s something you should care about or not. The list goes on and on and on.  

Potential Wars will now show whether or not the potential target is much weaker (green), roughly the same strength (gray), or much stronger (red).  


![43-war-situations.png](https://forumcontent.paradoxplaza.com/public/946873/43-war-situations.png "43-war-situations.png")


*[Image - War situations]*  


Alliances have been expanded to include everyone you can form an alliance with (previously it only showed close family) and it’s been split in two - those who would accept and those who can be convinced. It also shows how strong they are, and if they are within your realm or not.  


![44-alliance-situations.png](https://forumcontent.paradoxplaza.com/public/946874/44-alliance-situations.png "44-alliance-situations.png")


*[Image - Alliance situations]*  


Here you can see that the opinion of the realm priest is shown directly in the entry. There’s also a new situation for when the Pope would grant you a claim on a relevant Duchy+ title (neighboring Duchy, or any Kingdom).  


![45-various-situations.png](https://forumcontent.paradoxplaza.com/public/946875/45-various-situations.png "45-various-situations.png")


*[Image - Various situations]*  


In fact, there are so many changes to the Current Situation list that it’ll be easier to show the update notes in full:  


- Added a 'You can ask the Pope for Claims' Current Situation item, showing you any Duchies+ that you could get a Claim on
- Excluded Barons from the 'Powerful Vassal demands Council Position' Current Situation as you legitimately don't have to care that much for them
- Excluded parents, grandparents, and great-grandparents from the 'Family can Marry' Current Situation as marrying away your widowed mother isn't something we want to motivate the player to do
- Expanded the 'Child needs Guardian' Current Situation to include valid grandchildren and great-grandchildren
- Expanded the 'Low County Control' Current Situation to trigger when control is at or below 90 Control, and it now shows the Control level directly in the entry
- Made the Current Situation widget slightly wider and fixed multiple instances of buttons that you weren't clickable everywhere
- The 'Call Ally', 'Call House Member' and 'Call Dynasty Member' Current Situation entries will now state their Tier and Troop Count directly in the entry
- The 'Declare War' Current Situation will now show the amount of troops your potential target has
- The 'Demand Payment' Current Situation now states how much gold they have compared to the amount you demand, so you know before clicking
- The 'Family can Marry' Current Situation has been updated to show what place in the line of succession they hold, to avoid you doing unfavorable marriages
- The 'Few Knights' Current Situation now states how many knights you have, and what's your maximum
- The 'Hire Court Physician' Current Situation is now marked as dangerous/high prio, as being without one is indeed quite dangerous
- The 'In Line of Succession for Title' Current Situation Item will now only appear for titles outside your realm, as it would in 90% of cases mainly show titles you were about to inherit from newly-created Vassals
- The 'In line for Title' Current Situation now states if the title is inside or outside your realm, so you can better plan your nefarious murder schemes
- The 'Negotiate Alliance' Current Situation description now explains that allied Vassals can't join factions if the ally is within your realm, or how many troops you'd get if the ally is outside your realm
- The 'Negotiate Alliance' Current Situation now states if the target is inside or outside your realm, so you can make a better call at a glance if they'll be able to join your wars or not
- The 'Negotiate Alliance' Current Situation now states the potential targets relation to you (son, brother, etc) and their Military strength
- The 'Not Endorsed by Realm Priest' Current Situation now opens the Sway interaction, as that's what you want 99% of the times you click it
- The 'Not Endorsed by Realm Priest' Current Situation now shows the Opinion your Realm Priest has of you
- The 'Powerful Vassal demands Council Position' Current Situation now shows the Opinion the Vassal has of you in the entry, so you can easily avoid assigning positions to already-happy Vassals if you want
- The 'Prisoner can be Ransomed' Current Situation now shows if they have enough gold to pay their ransom directly in the entry
- The 'Propose Alliance' Current Situation has been expanded to include more valid targets for alliances, such as anyone married to one of your extended family members
- The 'Realm will Lose Land if Vassal Inherits Title' Current Situation will now state exactly which title would cause the damage, along with its tier
- The 'Wrong Holding Type' Current Situation will now state in the entry what type of Holding they are
- Added a Current Situation for when one of your first three Heirs are imprisoned so that you can easily pay their Ransoms
- Added a Current Situation for when you can Pay Ransom for one of your Vassals and gain a Hook on them
- Added a Current Situation item for Pardoning Criminals
- Added icons and updated texts for most Current Situations
- Most Current Situation entries that has to do with titles will now state the tier and show an icon of the tier Crown to aid in identification

We were going to write about some more things… but at this moment the document we’re working with is almost 50 pages long, so we’ll save some of the other QoL changes for another Dev Diary further down the line!  

Having covered Vassal Stances, Men-at-Arms Stationing, Domain Limit Rebalancing, the Building Slot Revamp, Rebalanced & New Buildings, the Improved Personality Tooltip, Rich Presence, Destroying Artifacts/Aniconism, and Improvements to the Current Situation - that's it for now! Next week we’ll delve into the Activity system, and take a look at some of the reworked activities in detail. Until then!

<!-- artifact:reactions:start -->
- 488 Love
- 246 Like
- 9 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
