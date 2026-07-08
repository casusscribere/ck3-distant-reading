---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1730576/"
forum_thread_id: 1730576
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 164
title: "Dev Diary #164 - Realm Maintenance"
dd_date: 2025-03-06
author_handle: rageair
expansion: Khans of the Steppe
patch: Patch 1.16
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 13729
inline_image_count: 38
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1730576'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3624.jpg?1741691916
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_1166_to_1169
    action: preserved_and_flagged
    counts:
      Love: 213
      Like: 116
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_1177_to_1238
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_1239_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3624.jpg?1741691916)
<!-- artifact:thread_banner:end -->

# Dev Diary #164 - Realm Maintenance

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Mar 6, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-164-realm-maintenance.1730576/)
<!-- artifact:thread_metadata:end -->

Greetings!  

This Dev Diary is about the upcoming free update, which we’ve dubbed 1.15.0 ‘Crown’! Similarly to free updates of the past, the Crown update will be pretty big - it has reworked systems, new features, and a myriad of bugfixes and balance changes.  

All of the changes that I’ll go over stem from the fact that we spend a lot of time updating, tweaking, and bugfixing existing systems and features as part of our parallel development track setup - depending on the status of an individual track, people from that track are assigned to what we call ‘Realm Maintenance’, where we focus on improving areas of the game that we either feel aren’t good enough, or that you in the community are asking for us to change. Usually a lot of Realm Maintenance time happens at the start of a new development track, as there are few bugs in newly developed content during, for example, the concepting or pre-production phases. During Realm Maintenance we have Improvement Days where we add as many smaller improvements and quality of life changes as we can, and some time is also used to polish promising projects from the Black Forge Jam (an internal sort-of game jam where we experiment with new CK3 features). The Crown update contains over 4 months worth of Realm Maintenance, including 200+ bugfixes.  

I won’t have time to go over everything in detail, so I’ll focus on a few highlights!  

---

### Court Position Rework​

Last year we teased a Court Position rework, and since then we’ve refined it and added even more improvements. In short; the rework aims to make Court Positions more interesting and engaging, adding tools, adjusting costs, improving quality-of-life, and making the UI less of a hassle to use. The intent is for Court Positions to be more widely used by giving them new effects and tasks that allow you to deal with many different situations.  

![image 01.png](https://forumcontent.paradoxplaza.com/public/1254592/image 01.png "image 01.png")


*[Image - The new layout]*  

The new layout allows you to see more positions at once, and presents them in a more immersive way. All of the information is still there, of course: most of what you don’t need to see at all times has just moved into the tooltip. What you need to know at a glance is still visible.  

![image 02.png](https://forumcontent.paradoxplaza.com/public/1254593/image 02.png "image 02.png")


*[Image - Unavailable Court Positions]*  

At the bottom of the list we’ve added a new foldable category that reveals all positions that you could potentially have. It’ll exclude anything you cannot possibly get, such as Adventurer Officers for landed characters and vice-versa. The tooltips will tell you what you can do in order to get them.  

![image 03.png](https://forumcontent.paradoxplaza.com/public/1254594/image 03.png "image 03.png")


*[Image - Court Position automation]*  

Now when it’s more important than ever to keep certain positions filled, we’ve added the option of choosing to fill the position automatically. This comes in three flavors, depending on your preference: an event giving you the option to choose between a few good candidates in your court, auto-assign the highest aptitude courtier, or auto-assign with an event notifying you if there are no candidates. This can be toggled per Court Position, and different positions can have different settings.  

![image 04.png](https://forumcontent.paradoxplaza.com/public/1254595/image 04.png "image 04.png")


*[Image - Seneschal Tooltip]*  

A lot of court positions were never used because it was hard to justify spending gold on their salaries, so we decided to transfer part of the costs into prestige, and we also lowered salaries across the board (the salary pictured in the screenshot is from the late medieval era, roughly 150 years in from 1066). Prestige is a resource most players are more willing to part with, but as there up until now has existed very few ‘prestige income sinks’ you need to be careful so you don’t spend it all…  

All of the new tasks have costs; some of them prestige, some gold, and some even cost piety. It's these tasks where the brunt of the cost will come from, but they are naturally opt-in, and you can use them to handle tricky situations, toggling them on/off as you see fit.  

Most positions now also come with an interesting effect for the holder of the position, such as the 20% stewardship experience pictured above. This also means that we’ve opened up a lot more positions to be held by vassals, which is interesting because:  

![image 05.png](https://forumcontent.paradoxplaza.com/public/1254596/image 05.png "image 05.png")


*[Image - Request Court Position]*  

You can now request Court Positions from your liege, allowing you to reap some of the benefits that they convey, such as Royal Architect now reducing your build time/build cost, or the Court Poet now reducing your stress gain, general opinion, and diplomacy lifestyle xp.  

![image 06.png](https://forumcontent.paradoxplaza.com/public/1254597/image 06.png "image 06.png")


*[Image - Grant Court Position]*  

You can also grant court positions directly via a character interaction now, making it easier to, for example, appease angry vassals with ceremonial positions.  

![image 07.png](https://forumcontent.paradoxplaza.com/public/1254598/image 07.png "image 07.png")


*[Image - A handful of the new tasks]*  

There are way too many new Court Position Tasks for me to go through them in detail, but above is a small sample of what you’re going to see. Most Court Positions now have three tasks to choose from, with a few having one or two - these tasks cover a wide variety of things you might want, from Wet Nurses instilling virtues into your children, to your Antiquarian searching for rumors about locations of rare Artifacts, to your High Almoner promoting the opinion of Zealous Vassals, among many, many more things.  

Many of the things you can now do didn't have any tools before; such as reducing the stress of characters other than yourself (which can be achieved via the Entertain Courtiers task for the Jester). You can also use various positions and tasks to slowly increase your Legitimacy; the Seneschal gives a small passive trickle, the Court Poet can give you Legitimacy % Gain Modifiers as part of the Write Poetry Task, and the Court Musicians Bolster Legitimacy Task (the Court Musician is now available to Duke-tier characters and no longer requires Royal Court to have!). It’s worth noting that all tasks that increase stat points, such as ‘Exercise with Ruler’, are balanced in such a way that you cannot gain skills unless the holder of the position is better at the skill than you are.  

We’ve also taken this opportunity to move the entire Hunt Sighting system into these tasks. If you want hunt sightings to improve the success chance of your hunts, you now choose what your Master of the Hunt should focus on finding - this makes the system less random and gives you more agency.  

There’s more that I’ve not talked about, to see the full extent of changes I refer to the full changelog at the end of this diary!  

### Automated Armies​

Another feature we teased last year was the addition of Automated Armies, an opt-in feature where the AI takes control of your armies and fights wars for you. The intent behind this feature is to allow you to focus on other things while engaged in trivial wars, and to allow players unfamiliar or uninterested in warfare to enjoy the game more. If you are an experienced player we still recommend that you control your armies yourself, but give it a spin if you’re just cleaning up those three counts bordering your empire!  

![image 08.png](https://forumcontent.paradoxplaza.com/public/1254600/image 08.png "image 08.png")


*[Image - Automated Armies Settings]*  

Now, there are two crucial parts to this feature working well: seeing what the AI is thinking, and for the AI to play well. There’s nothing that differentiates Automated Armies from how the AI normally plays, so improving one improves the other. Both of these areas will be covered in the two sections below:  

### AI Ally Info​

Sometimes you have an ally in a war that you have no idea what they are thinking - perhaps they’re just standing there, moving erratically, or being generally unhelpful. Quite often this is because of something that you’re not aware of; perhaps they are resupplying their armies, perhaps they are guarding a siege, etc. To make it more transparent what an army is doing, we’ve added icons with descriptions that explicitly tell you what the AI is up to.  

![image 09.png](https://forumcontent.paradoxplaza.com/public/1254601/image 09.png "image 09.png")


*[Image - Exposed Ally Thinking]*  

This is also applied to your own armies if they’re automated, giving you an overview of what they’re doing.  

![image 10.png](https://forumcontent.paradoxplaza.com/public/1254603/image 10.png "image 10.png")


*[Image - Exposed automation thinking]*  

In the above screenshot, the right army is actively besieging while the left one is guarding the siege while standing in a province with enough supply limit to support it.  

There are a multitude of different states for the AI to show; moving, attacking, moving to siege, supporting the player, etc. Hopefully this’ll clear up most uncertainties regarding why they’re doing things that might otherwise appear inexplicable.  

### Warfare AI Fixing/Updates​

We’ve been working a lot with warfare AI in an effort to make it better. We’re not promising miracles, but we have spent over two months of programmer time in an effort to nail down bugs, improve sub-par behavior, and change behavior that, while intended, didn’t feel ‘right’.  

This includes a lot of cases where the AI would be indecisive, passive, or ‘dance’ between provinces, which was often caused by various competing systems trying to avoid attrition, match supply limits to stack sizes, and edge-case bugs. These fixes in combination with the exposed AI ally logic above results in much more clear warfare where it’s easier to understand what the AI is up to.  

We’ve also taught the AI about War Score, making them pursue what would give them score, rather than arbitrarily choosing actions based on a set of circumstances that were always fixed. For example; when you’re fighting a war as a player, you’re less likely to pursue battles if you know that the siege you’re currently about to finish would win you the war, and you’re also less likely to pursue battles if you’re already capped on battle warscore (usually war score for battles is capped at +50% for most CB’s). They’re now also much more likely to siege using stacks with Siege Weapons, and will try to shuffle their siege stacks around in such a way that their ongoing sieges aren’t broken.  

Now, there are going to be edge cases where unwanted behavior still happens, and we’ll keep fixing bugs as we find them. Hopefully you won't notice as much strange AI behavior any more.  

An area of the game where the ‘normal’ war AI does not perform as well is during Crusades, so we decided to take a suggestion from the community and give these Great Holy Wars some special treatment. The ‘one size fits all’ philosophy out the window, the AI now has a set of special procedures they follow during these grand-scale wars in particular.  

Firstly there’s a set of smaller tweaks; the AI cares less about attrition and supply until they’ve made some headway, and they will try to ‘boat hop’ less often (take short sea paths). When you’re going from well-supplied Europe by boat disembarking into low-supply drylands with an army of potentially hundreds of thousands of men there’s no way you can find enough supply for all of them - the AI now knows this, and when they start assaulting the war target they will temporarily ignore attrition until they’ve gotten enough of a beachhead that they can support the size of their units, this makes the initial phase of a crusade more likely to succeed as the attacking AI won’t desperately shuffle their troops around to find supply. By ‘boat hopping’ less they will prefer land routes to their targets, avoiding the -30 advantage penalty.  

Now for the meat of the changes; the attacker in a GHW will first find a ‘Gathering Area’, and then move their armies to a ‘Staging Area’.  

![image 11.png](https://forumcontent.paradoxplaza.com/public/1254604/image 11.png "image 11.png")


*[Image - AI armies gathering in Roma before sailing to Jerusalem]*  

For the first stage of a Great Holy War the attacking AI will find a good-supply area where they can gather their forces. As stacks of units are raised across a large part of the world they need some time to gather, and should do so in a safe place. In this example we have a crusade against Jerusalem, so Roma with its surrounding counties is deemed both safe and close enough to the target to be designated the Gathering Area. You will see an icon on allied AI units with a text that says where they intend to gather, so that you can follow them there. They will gather for several months before setting off to the next step of the journey: the Staging Area.  

![image 12.png](https://forumcontent.paradoxplaza.com/public/1254605/image 12.png "image 12.png")


*[Image - AI armies staging in Issus after having gathered in Roma]*  

The Staging Area is the closest friendly or neutral area to the war target, in this example it’s in Byzantium. The attacking forces will make their way there before starting their assault, which means that they will arrive as a much more unified force. This also means that they won’t immediately attack from the water, avoiding disembarkment penalties and ensuring that their stacks have an acceptable degree of supply. Instead they will most likely march in via land, taking a modicum of attrition along the way, but ultimately mustering a more successful assault.  

Now, the testing that we’ve done reveals that the attackers are usually more successful, but can still lose. Though now when they lose it’s less because they frustratingly trickle in across several years with disembarkment penalties and no supply, and more because the defenders have a homeland advantage - as it should be.  

### Character Interaction UI Update​

The character interaction menu has received a facelift, with the intent of cleaning it up and making interactions more intuitive.  

![image 13.png](https://forumcontent.paradoxplaza.com/public/1254606/image 13.png "image 13.png")


*[Image - Cleaned-up interaction menu]*  

Several categories have been removed and merged into other categories to keep the overall number down. We’ve added colors to these categories so it’s easier to glance at the one you need.  

You can now easily see if a scheme is personal, hostile, or political - with the predicted scheme difficulty shown next to it, making it easier to see what you could be pursuing without having to delve into each interaction.  

![image 14.png](https://forumcontent.paradoxplaza.com/public/1254607/image 14.png "image 14.png")


*[Image - Favorite button]*  

As we’ve moved several interactions to no longer be common and only shown in sub-menus, we’ve added a way for you to select ‘favorite’ interactions. Favorite interactions will be shown in their own category at the top of the interaction menu, allowing you to see what you think is important first.  

![image 15.png](https://forumcontent.paradoxplaza.com/public/1254608/image 15.png "image 15.png")


*[Image - Favorites in action]*  

Wherever it makes sense we’ve now added a quick-interaction button that contains a collection of relevant interactions for that context. These buttons have been added in various places, such as for your head of faith, on your Administrative liege, or on administrative governors in the theme view. If you’re a modder you can easily make more custom contexts.  

![image 16.png](https://forumcontent.paradoxplaza.com/public/1254609/image 16.png "image 16.png")


*[Image - Head of Faith custom interaction category]*  


### Right-click to Raise Armies​


![image 17.png](https://forumcontent.paradoxplaza.com/public/1254610/image 17.png "image 17.png")


*[Image - UI for raising armies anywhere]*  

You can now right-click to raise your armies in a specific area, so you no longer have to move a rally point there first. This simplifies the act of raising armies and prevents the mistake where you can accidentally raise your armies on the wrong side of your empire just because you moved your rally point there during your last war… It’s not impossible that we’ll remove and replace the rally point system entirely in the future.  

![image 18.png](https://forumcontent.paradoxplaza.com/public/1254611/image 18.png "image 18.png")


*[image - Tooltip for Raise Armies]*  

### Administrative Government Additions​

![image 19.png](https://forumcontent.paradoxplaza.com/public/1254612/image 19.png "image 19.png")


*[Image - Eparch]*  

Going hand-in-hand with the Court Position rework, a new Court Position has been added for independent rulers of Administrative realms: the Eparch. The Eparch focuses on improving your capital in various ways; the tasks are expensive, but the effects are significant! Being the Eparch is also very attractive for vassals, as they get a significant influence boost…  

![image 20.png](https://forumcontent.paradoxplaza.com/public/1254613/image 20.png "image 20.png")


*[Image - Eparch Tasks]*  

Going hand-in-hand with the Eparch is the new Capital Magistracy building, which improves the aptitude of the Eparch among other things. It can only be built in the capital of an Administrative realm.  

![image 21.png](https://forumcontent.paradoxplaza.com/public/1254614/image 21.png "image 21.png")


*[Image - A tier 1 Capital Magistracy building]*  

Not everything will be easier for Administrative realms - we also thought that it was way too easy for them to hold on to their lands, even when engaged in civil wars or otherwise weakened. We’ve added a new CB that can only be used on Administrative realms, ‘Seize Peripheral Duchy’, that allows you to take any duchy that is outside of the empire's De Jure for a very low prestige cost. This CB has 3x the Siege and battle warscore for the attacker, and a significantly faster ticking warscore, making it the perfect way to reclaim lands from an otherwise preoccupied empire.  

![image 22.png](https://forumcontent.paradoxplaza.com/public/1254616/image 22.png "image 22.png")


*[Image - The Seize Peripheral Duchy CB]*  

Alongside this we’ve also reworked the "Order Mass Arrests" decision to be a character interaction. You can now use this on all noble families, and not just powerful families, as long as their estate is located in the capital. We’ve also tweaked the options for when you restore the Roman Empire, such as offering a path to become Hellenic without activating Roman Hard More, as well as making said mode more enjoyable by tweaking event frequencies and removing parts of it that made little sense (such as increased diseases).  

### Clan Government Tweaks​

The Clan government is one that is both fairly underplayed (according to telemetry) and that the AI struggles in playing well (often underperforming significantly). This prompted us to look into doing something to make them more interesting and less frustrating to play - when managing Tax Jurisdictions it’s a constant battle to find competent Tax Collectors. All you have at your disposal are your unlanded courtiers and a decision with a fairly long cooldown, which leads to a frustrating time as you often end up in a combination of not having anyone to assign, and if you do have someone, they’re more often than not terrible. The various tax decrees also felt underwhelming with the vast majority of players simply opting for the Zakat (luxury tax) one as it increased your gold income.  

All of this has prompted a host of changes to the feature.  

![image 23.png](https://forumcontent.paradoxplaza.com/public/1254618/image 23.png "image 23.png")


*[Image - Updated Tax Jurisdiction UI]*  

Alongside a general facelift of the UI, we’ve opened up the possibility for Vassals to be Tax Collectors - this makes it significantly easier to find tax collectors, and to find good ones. Similarly to how we handle Court Positions, landed tax collectors get a penalty to their aptitude, but on average it’s much easier to find good tax collectors because of this change.  

Clan rulers now also don’t have to worry about being allied to ALL their vassals, as only powerful vassals will expect to be allied to their liege. This makes you able to focus on pleasing a select few characters in the realm without having to suffer a permanent -20 opinion with every vassal. You also no longer gain a legitimacy penalty for marrying lowborn characters as secondary wives (and to pre-empt exploits we’ve also made it so that switching to a lowborn spouse as your primary spouse triggers the lowborn marriage penalties). This means that as long as your main spouse is highborn, the remaining ones can be lowborn. The AI has been updated to always try to set the spouse with the best stats as their primary one, as long as that doesn’t trigger the lowborn spouse marriage penalties.  

![image 24.png](https://forumcontent.paradoxplaza.com/public/1254619/image 24.png "image 24.png")


*[Image - Updated tax decrees]*  

All Tax Decrees have been updated to have more interesting and modern effects, including systems that have been added since Tax Decrees were added, like Legitimacy, Danger, and Plague Resistance, and enabling systems that are logically connected to the decree, like raiding for Ghazi.  

These changes match the Clan realm's more volatile nature, providing bonuses that are more relevant and interesting to choose between. They should now more closely be able to match the power that Feudal realms can muster with their Vassal Contracts.  

### Tiered Commander Traits​

All commander traits are now tiered traits that are leveled up by taking actions related to the trait.  

![image 25.png](https://forumcontent.paradoxplaza.com/public/1254621/image 25.png "image 25.png")


*[Image - A levelled Logistician trait]*  

Commander traits now start out less impactful, with effects weaker than they currently are. Through war, battles, and siege, you can now level them up - potentially reaching heights that were not previously possible. A fully levelled Military Engineer reduces siege phase times by 40%, a fully levelled Flexible Leader reduces enemy defensive bonuses by 80%, and so on.  

To level the traits you need to do whatever makes sense: to level up Aggressive Attacker you win offensive battles, to level up Military Engineer you complete sieges, and so on. The higher the commander's Martial skill, the faster they will level up their traits. This also means that a commander with a high-level commander trait can be extremely valuable, as replacing their accumulated knowledge of warfare is not a trivial task.  

### Barbershop Fixes/Updates​

The Barbershop has been updated with several new categories, and items have been re-shuffled to allow for a greater degree of customization. Many items previously not accessible has been added, such as some Byzantine and Jain clothing, and you are now allowed to freely change eye items, face items, crests, veils, and special crowns.  

![image 26.png](https://forumcontent.paradoxplaza.com/public/1254624/image 26.png "image 26.png")


*[Image - New barbershop categories]*  

We’ve made extra care to address pain points such as not being able to remove glasses or veils, while simultaneously allowing you to create combinations you weren’t able to before. More customization is better customization!  

![image 27.png](https://forumcontent.paradoxplaza.com/public/1254625/image 27.png "image 27.png")


*[Image - New Crests, Veils, & Special Crowns category]*  

Use responsibly!  

![image 28.png](https://forumcontent.paradoxplaza.com/public/1254628/image 28.png "image 28.png")


*[Image - a distinctly cursed barbershop creation]*  

### Minor/Misc Changes​

#### AI Promote Culture Tweaks​

Late-game culture maps are often quite boring, with the culture map gradually becoming more and more populated by small divergences. This is fine in the case where these divergences lead to interesting new cultures expanding their presence on the map, but often it is not so. We’ve tweaked the AI to be more inclined to promote their cultures under certain circumstances.  

Central Germanic heritage cultures within the HRE will now want to promote culture in Sorbian-culture counties, very small cultures will want to grow (if they are below 10 counties), 'Imperious' cultures (cultures with a powerful culture head, realm of 30+ counties and King+ tier) will want to grow to a decent size (35 counties, about the size of French at 1066 start), smaller (<5 counties) divergent/hybrid cultures with no existing culture head are more likely to be promoted by other cultures (with the intent of reducing the amount of small and orphaned cultures by the end of the game). This makes the culture map more dynamic and existing, with interesting results every game.  

![image 29.png](https://forumcontent.paradoxplaza.com/public/1254629/image 29.png "image 29.png")


*[Image - Saxon slowly being promoted in Polabian lands]*  

#### Game Rule Updates​

We’ve added several new options to the Realm Stability Game Rule, based on community feedback - and a few extra for good measure! You can now set stability to only affect AI’s, and there’s an additional setting that avoids changing the frequency of peasant and populist factions as those could become too frequent or infrequent depending on your setting.  

![image 30.png](https://forumcontent.paradoxplaza.com/public/1254630/image 30.png "image 30.png")


*[Image - New Realm Stability settings]*  

For those that enjoy the occasional Scourge of the Gods Conqueror but think that 5% is too much we’ve added an additional rule; *Low Random*, with a 0.5% chance of it happening.  

![image 31.png](https://forumcontent.paradoxplaza.com/public/1254632/image 31.png "image 31.png")


*[Image - Conqueror Low Random setting]*  

#### New Message Setting Options​

The message settings window now has a history log of all feed messages, so you can browse through them at a later time.  

![image 32.png](https://forumcontent.paradoxplaza.com/public/1254633/image 32.png "image 32.png")


*[Image - Message Settings log]*  

We’ve also added two community-requested message settings: scheme advantages and non-dynastic courtiers coming of age.  

![image 33.png](https://forumcontent.paradoxplaza.com/public/1254634/image 33.png "image 33.png")


*[Image - Scheme Advantage message setting]*  

![image 34.png](https://forumcontent.paradoxplaza.com/public/1254636/image 34.png "image 34.png")


*[Image - Non-dynastic courtier coming of age]*  

#### Guardian Status in Courtiers UI​

There are now new indicator texts and filter options for finding children without guardians in your court. This is present both in the right-hand-side Court window and in the character view.  

![image 35.png](https://forumcontent.paradoxplaza.com/public/1254638/image 35.png "image 35.png")


*[Image - Guardian indicators]*  

#### New Major Decisions​

Two new major decisions have also made their way into this update, both focusing on forming new empires - Beth Nahrain for rulers of Syriac heritage, and the Empire of Hindustan.  

![image 36.png](https://forumcontent.paradoxplaza.com/public/1254640/image 36.png "image 36.png")


*[Image - Beth Nahrain creation decision]*  

When adding new decisions for creating new empire titles in Crusader Kings there are two different things we look for. One could be an interesting alternative history empire for a historical group or region, like Beth Nahrain, another is to look for what great empires existed during the historical timeline but which currently cannot be formed in the game.  

![image 37.png](https://forumcontent.paradoxplaza.com/public/1254641/image 37.png "image 37.png")


*[Image - Hindustan creation decision]*  

The Islamic Conquest of India is not something that happens in every game, but when it happens we rarely ever get something like the actual Delhi Sultanate. The new decision lets a muslim ruler who controls a fair chunk of the north, move his capital to Delhi or Lahore, while creating a new empire title that incorporates any held line in the 3 Indian Empires. If you have Roads to Power it will also give you the Administrative government, though one with a hereditary succession instead of acclamation.  

#### Commanded by Ruler Banner​


![image 38.png](https://forumcontent.paradoxplaza.com/public/1254642/image 38.png "image 38.png")


*[Image - ‘Commander by Ruler’ banner]*  

You can now see if the enemy war leader is in an army, as they’ll be marked with a crown banner stating ‘Commanded by Ruler’.  

---


That’s it for this Dev Diary! The 1.15.0 ‘Crown’ update will soon be in your hands, and we hope that it’ll be to your liking! You can find the full changelog below. Cheers for now!  

Spoiler

### 1.15.0 “Crown” Update Changelog​


### Paid content:​

### “Crowns of the World” - Chapter IV instant unlock bonus​

- Added support, DLC icon and descriptions for Crowns of the World
- Content of Crowns of the World:
  * Hairstyles:
    + Chivalric Curls (m)
    + Scribe’s Braid (m)
    + Noblewoman’s Locks (f)
    + Turkic Lady’s Hair (f)
  * Beards:
    + Steppe Conqueror’s Beard (m)
    + Mustache of Vladimir the Great (m)
  * Headgear:
    + Timurid Emir’s Turban (m)
    + Crown of Vladimir the Great (m)
    + Reliquary Crown of Charlemagne (m)
    + Timurid Princess’ Crown (f)
    + Crown of Princess Olga of Kyiv (f)
    + Crown of Princess Blanche of England (f)

### Free content:​

### Game content:​

- **Court Position Rework**:
  * Reworked the Court Position window layout.
    + The goal of this rework is to make it easier to see several of the court positions at the same time, and being easier to navigate
    + We have now split the court position window into two parts:
      - Available court positions, where you can see all the court positions you can hand out (you might not have a fitting character for the position though)
      - Unavailable court positions, where you can see all the court positions you don’t have access to right now, but you could have access to through changes to culture, religion, or gender
    + Added a new Court Position interaction (under Courtier) where you can hand out a Court Position to a character, as an alternative to granting it from the Court Position window. This should make it easier to easily use court positions as a tool to increase vassal opinion.
    + Added a new character interaction (under Liege) to request a specific Court Position from your liege.
    + Added a new type of flavorization where we can rename Court Position names based on any kind of criteria, be that culture, religion, or whatever else.
      - For this update, we renamed Court Poet to Court Skald for the North Germanic culture group
  * Added Automation for vacated Court Positions
    + You can now define what should happen when a specific court position is vacated, to make it easier for you to keep key court positions filled at all times
    + Four options, with different degrees of automation:
      - Do nothing (default, as before) - the court position is vacated, a toast message is displayed
      - Show event - Pop up an event when it vacates, with up to two suggested characters from your court that could fill the court position, picked by their aptitude
      - Best aptitude character - Auto-fill the court position with the highest aptitude character, show toast message with replacement
      - Best aptitude character, with event if none are available - Same as above, but if there is no one available, show a popup event for the player
  * Reworked court positions, changing their costs and effects, and adding tasks for most of them.
    + Notable changes:
      - Gold costs are generally lower across the board than what they used to be, but most positions come with a new monthly prestige cost
      - Most court positions now have a positive effect on the court position holder, similar to council positions
        * E.g. The Royal Architect now get reduced building construction time, cost, and a stewardship lifestyle experience boost
      - Opened up more Court Positions to be handed out to landed vassals
      - Court Tutors will now effectively take the role as a Guardian for every child without a Guardian at court
      - Court Jester events are no longer random, but rather a decision (‘Be Entertained by the Court Jester’) where you choose to opt-in to them
      - Master of the Hunt now have tasks where you can opt-in to finding specific kinds of Sightings, e.g. looking for regular game vs dangerous game vs legendary game
      - Master of the Horse is now available to rulers of Duchy tier rank, instead of only to Kingdom tier rank rulers, and affects how many Knights you have access to
        * We have reduced the amount of Knights you generally have access to from your Title Tier, and have moved some of those numbers to the Martial stat, and some of them to this Court Position
      - Court Artificers have new tasks where you can choose what type of artifact inspirations they should get, so you can focus them on what you want
      - Removed Court Grandeur modifiers from many of the Court Positions, and replaced it with something more interesting
    + New Court Position tasks:
      - Note that some of these tasks require the character filling the court position to fulfil certain prerequisites, such as having a certain level of skill (for example; to use ‘Fuel the Rumor Mill’ the Court Jester needs 12 intrigue skill). Some tasks also require you as the liege to fulfil certain prerequisites, such as owing a certain type of artifact or being of a specific tier (for example; to use ‘Exhibit Illustrious Artifacts’, you need to own an illustrious court artifact).
      - Active Court Position tasks are now remembered in case the holder of the court position dies or is replaced.
      - Royal Architect:
        * Fortify Lands - Increase fort level and garrison size
        * Public Works - Development Growth
      - Executioner
        * Terrify Court - Increase Dread and decrease opinion
      - Cup-Bearer
        * Collect Tallage - Courtly Vassal tax increase, Courtly Vassal opinion decrease
        * Flatter Dignitaries - Personal scheme improvements
      - Chief Qadi
        * Lead Public Sadaqah - Control growth and popular opinion
      - Food Taster
        * Brew Poisons - Scheme secrecy increased, hostile scheme potential increased
        * Keep an Ear to the Ground - Scheme discovery chance, monthly intrigue lifestyle experience
      - Personal Champion
        * Improve Skills - Chance of getting Hastiluder Trait XP or Prowess skills
        * Compete in Name - Increase Prestige gain
        * Exercise with Ruler - Chance for ruler to gain Prowess skill every month
      - Court Poet
        * Write Poetry - Random modifier giving either legitimacy, piety, advantage, or attraction for 3 years
      - Caravan Master
        * Stock up for Travels - Safety and Speed increased next travel
        * Prepare Armies - Increase army movement speed and supply limit
        * Improve Skills - Chance of getting traveler trait XP, martial skill, or stewardship skill
      - Court Jester
        * Entertain Courtiers - Reduce stress of random courtiers
        * Fuel the Rumor Mill - Reduce enemy schemes
        * Abuse the Jester - Increase dread, lowers the jesters health and opinion
      - Court Physician
        * Improve Skills - Chance of getting physician trait XP or learning skill for the physician
      - Master of the Hunt
        * Track Regular Game - Chance of getting sighting
        * Track Dangerous Game - Chance of getting sighting
        * Track Legendary Game - Chance of getting sighting
      - Seneschal
        * Organize Court - Increase Aptitude of other court positions
        * Manage Domain - Increase control growth
        * Handle the Estate - Domicile bonuses
      - Court Artificer
        * Create Weapons/Armor - Gain Inspiration
        * Create Books/Tapestries - Gain Inspiration
        * Create Crowns/Sculptures - Gain Inspiration
      - Court Tutor
        * Teach Court - May improve characters at court
        * Educate Children - May improve children at court
      - Antiquarian
        * Improve Artifacts - May improve artifacts
        * Exhibit Illustrious Artifacts - Improve stewardship and court grandeur
        * Search for Rare Artifacts - May gain adventure inspiration
      - Wet Nurse
        * Instill Virtue - Children may gain a virtuous trait
        * Promote Friendship - Children at court may become better friends
        * Encourage Competition - Children may gain intrigue skill or prowess skill, but at the cost of opinion with one another
      - Court Musician
        * Bolster Legitimacy - Gain legitimacy
      - Master of the Horse
        * Oversee Breeding - Gain army pursuit
        * Warhorse Grooming - Advantage when commanding own armies
      - High Almoner
        * Divine Charity - Gain piety
        * Appease Zealots - Improve zealot vassals
    + Added a new court position for administrative emperors: Eparch
      - The eparch acts as the chief administrator of your capital, improving your Governor Efficiency and that of any Estate owner who has their Estate in the capital.
      - The Eparch has access to four different tasks:
        * Appease Populace - Improving the popular opinion in the capital
        * Support Troops - Improving any Men-at-Arms stationed in the capital
        * Enforce Public Order - Increases monthly control growth in the capital
        * Develop Capital - Increases development in the capital
      - Eparchs may receive assorted events regarding the capital, able to bestow the capital with various boons.
- Added the Automated Armies feature
  * You can now choose to let the AI control all your Armies, allowing you to focus your attention elsewhere if you’re involved in smaller wars, or to help you out if you’re unfamiliar with how warfare works in the game (manual control is still recommended for experienced players)
  * The AI will, if allowed, raise, disband and control your Armies
  * You have options to tweak this behavior:
    + You can choose if the AI also sets Commanders
    + You can let the AI control Raiding
    + You can let the AI hire Mercenaries, Holy Orders and Imperial Armies
  * All AI controlled Armies, including Allies, have a segment in their tooltip stating their intents
- Allied units and automated player armies will now display an icon to make the player aware of what they are doing, such as ‘Attacking *location*’, ‘Resupplying’, or ‘Defending Siege in *location*’, among many others. This should make it more clear why the AI is making certain decisions.
- Added a method for raising your troops in a specific location that is not one of your predefined rally points by right-clicking the various ‘Raise all troops’ buttons, and then clicking on a map location
- Made the following changes to the Restore the Roman Empire decision as Byzantium.
  * Added a new option where you can choose to adopt Hellenism without activating "hard mode" - Giving you the possibility to go full role play mode if you want to. The option for hard mode remains available.
  * When choosing the "hard mode" option, extra plagues will no longer appear. This didn't make that much sense and wasn't very interesting.
  * Instead of always converting, vassals now have a chance to convert when you adopt Hellenism.
  * Significantly reduced the chances of "hard mode" content to appear, as it was extremely frequent.
  * Fixed an issue in the event "Misguided Governing", where firing the governor wouldn't actually remove them from office as expected.
- Added a new building line uniquely available for independent admin rulers: the Capital Magistracy. It may only be constructed in the capital.
  * It improves the aptitude of your Eparch
  * It also improves the county's gold income, and provides the ruler with increased influence and prestige gain
- Added a new Syriac Cultural Major Decision allowing you to create the empire of Beth Nahrain in Jazira and Mesopotamia. The decision also helps you spread Syriac culture and the Nestorian faith in the region.
- Added a new decision for Muslim realms in India to form the empire of Hindustan, which is based on the Sultanate of Delhi. If playing with Roads to Power this also makes you administrative with primogeniture.
- Added an 'AI Only' option to the various settings of the Realm Stability game rule.
- Added versions of the Realm Stability game rule settings that only affect vassal-led factions (so, peasants and populists are unaffected).
- Reworked the "Order Mass Arrests" decision to be a character interaction. You can now use this on all noble families, and not just powerful families, as long as their estate is located in the capital.
- Added a decision to found a new duchy, if you have high enough prestige or legitimacy.
- Added a decision to set the de jure capital of your duchy/kingdom/empire.
- Added a Low Random setting to Conquerors, with a 0.5% chance of spawning an extreme conqueror.
- Added new mayor title flavorization for cultures outside of Europe that previously always used the feudal baron title for all baron tier land holders.
- Changed all the Command traits to be tiered traits that can be leveled up, becoming more powerful and changing the names of the trait. The base strength of each trait is lower, so simply having a commander trait is not as strong, but their maximum strength is stronger. Traits are leveled up by doing relevant things, such as completing sieges as a Military Engineer, etc. As an example:
  * Raider
    + Raid Speed: +40%
    + Hostile County Attrition: -30%
  * Marauder:
    + Raid Speed: +80%
    + Hostile County Attrition: -60%
  * Reaver:
    + Advantage: +1
    + Raid Speed: +120%
    + Hostile County Attrition: -90%
  * Terror:
    + Advantage: +3
    + Martial: +1
    + Raid Speed: +160%
    + Hostile County Attrition: -120%

### Bugfixes:​

- Fixed issue where first-time-viewed male characters were assumed to have a 'max bald' gene for a number of frames (in sympathy for those afflicted, presumably), and then getting their hair back a second later
- Made sure that the Jain religious robe appears in the barbershop.
- Added the Royal/Imperial Loros to the barbershop (note that they are meant for use in combination with specific Byzantine clothes).
- Made sure that Byzantine commoner headgear appears in the barbershop.
- Added missing royalty clothes for Byzantines to the barbershop.
- Made sure the Torque with Barbette is visible in the barbershop.
- The Grain Dole decision is now available when you restore the Roman Empire. As long as your capital is located in Rome or Constantinople.
- Improved the text in the "Mass Arrests: A Plea" event.
- The option to place a candidate first in line in the Influence Candidate interaction is no longer available if the selected candidate is already first.
- Reworked the ‘Tomb Raiders’ event to be more interesting
- Hermit travel events now set the right weights for follow-up events based on what prophecy you received.
- Changed the text of the event “A strange sailor” and gave the sailor char a nickname.
- Improved effects and parsability of the “trampled underfoot” court event.
- Put a cooldown on the event where you find a doll when you are out raiding.
- Added additional triggers for a few events that have the option to turn counties into republics. Republics should appear a bit less "randomly" as a result, and mainly appear for cultures where it makes sense. Such as cultures with the Parochialism tradition.
- Changed "The Deserters" event chain from authority martial lifestyle to be a single event with better purpose and structure.
- Added cooldowns to the romance scheme ongoing events.
- Fixed repeated name in the Court Event “Unpleasant Pleasantries”.
- Fixed courtiers staying naked after the “A Compromising Position” event.
- Fixed mismatched artifact type names in the Exotic Arms event.
- Fixed broken option in Contrite stress event No Time for Myself.
- Fix for possibility of Harrying of the North Pacification and Resistance negative values.
- Visit Settlement-lock is now checked and removed when moving your camp.
- Adventurers can no longer Evangelize in highly developed or happy counties, holy sites, or counties held by a Head of Faith.
- Made Visit Holding variable time out if long enough time passes.
- Fixed not receiving Mayor's gold in “Popular with the People event”.
- Fixed The Gallant Knight event wrongly referring to Akolouthos.
- Fixed miscalculation of ransom cost where only mothers and fathers recognized their primary heir as their primary heir.
- Fixed an issue where the Iranian culture wouldn’t display all tiers of siege models.
- Changed the localization to just be a generic instrument in the legend event “At the Service of a Lord/Lady” instead of the custom localization since matching the displayed instrument was not working.
- Fixed cases where other character's court position employees would be referred to as your employees.
- Fixed 1st Bodyguard being replaced when hiring a 2nd bodyguard via an event.
- Fixed hunt sighting events firing for landless adventurers.
- Fixed rare case where spouse child naming event could fire after parent's death.
- Fixed is_valid script for all factions, so that it no longer blocks faction creation when it shouldn’t.
- Replaced old outdated mentions of "Court Physician" with "Personal Physician".
- The estate can no longer be moved to the same location it's already located in, which should prevent you from spending gold and activating the cooldown by mistake.
- Fixed an issue where you would get two separate messages for gaining the Traveler trait upon visiting a point of interest. You now only get one.
- Fixed a wrong scope that would fail to turn rulers into landless adventurers if they lost their titles in a war on some occasions.
- Landed characters can now become adventurers if they lose all of their titles as the result of a war they didn't directly participate in.
- Titles held by administrative vassals are now named correctly after the top liege. As a result, a duchy tier province will be called "theme" in Byzantium regardless of the holder's culture.
- The Master Assassin court position now correctly reduces the duration of your hostile schemes, instead of increasing it. Buffed the values slightly as well, to a maximum of 15 days faster at highest aptitude level.
- The children of a co-emperor of the Byzantine emperor now correctly gain the Born in the Purple trait when applicable.
- The Army breakdown tooltip will now show when hovering on the total count of soldiers in the Selected Army view.
- Fixed all triggers checking current scheme phase duration that were checking too small values or advantages.
- Removed the "Landless Rulers" tab from the advanced start screen if you are unable to play as one.
- If a required guest is not available for activities (such as if your betrothed has a deadly contagious disease before a Grand Wedding), you will now be told exactly why rather than be told they are already involved in another activity.
- Adjusted so that the event “Forgetting” can no longer refer to memories that are secret to the other character.
- The event "Bound Together" will no longer produce incestuous couplings.
- In the "Fallen Rival" event, you will no longer visibly grieve the demise of your rival in battle.
- The event "Flight of Fancy" will no longer state that you've received a different trait from the actual outcome.
- The event "Danger: A Fearsome Beast!" will no longer select children for you to sacrifice for your safety.
- Prevented travel_events.4037 (“Religion and Faith”) from treating your own faith as a foreign faith.
- Added a warning message to the "Empower Sicilian Parliament" decision, so the player knows that only one Special Building can be active at a time.
- Disabled the “Empower Sicilian Parliament” decision if there are no available Special Building Slots.
- Fixed a rare occasion where characters would be stuck endlessly in the end travel event.
- Fixed an issue where feasts could check murder requirements on yourself instead of your guest.
- The modifier Treatise on Management House Modifiers is now positive and not negative.
- Corrected some general issues with the "Eminent Eunuch" story cycle.
- Populist wars will no longer incorrectly vassalize all landless adventurers who joined the faction and helped to win the war.
- Added a missing value for the Border Dispute scheme, which prevented governors from scheming to take back their de jure counties when owned by other governors.
- Fixed an error in the outliner if you had the domicile panel expanded while playing as a character without a domicile.
- Added localisation for the predicted cost for hosting a Chariot Race.
- Updated the cost for Chariot Races. The predicted cost now matches the actual cost more closely
- Updated the text regarding Varangian Guard and Akolouthos on the Palace Politics cultural tradition to reflect actual functionality. Any emperor with this tradition is able to use the decision to found their own Varangian Guard.
- Updated the text on the Garden Architect tradition to make the Court Gardener tooltipable, allowing you to see what the court position does before having access to it.
- Fixed the decision to adopt feudal ways as admin to no longer attempt to change the government of vassal theocratic Head of Faith.
- Corrected missing character reference in tooltip in "The Cadastre".
- You no longer have a chance of becoming your own friend in "The Child Preacher".
- Courtiers, when sent to a Holy Order, will now actually do as they're told and join them.
- The duchy building slot for Connacht now properly appears in its capital county.
- University education will now benefit children with focuses other than Diplomacy.
- The event "Looking for Work" will now display all viable options, instead of just one.
- Fixed several instances where epidemics could still be spawned by events even when disabled by game rules.
- When forming New England, you will now correctly adopt the government form specified in the tooltip.
- Crusades diverted against Byzantium should no longer choose Christian vassals of the Byzantine emperor as their leader.
- Fixed a bug where the notification "You can station a Men-at-Arms Regiment" would not disappear if you stationed Thematic armies.
- You will now properly gain stress if your siblings die young and you don't profoundly dislike them.
- Independence Wars will now invalidate if the defender is no longer the attacker's liege.
- Ensured that characters that become domicile owners while traveling don't get "stuck" with a far-away domicile.
- Adjusted the Soulmate Legend motivation toast message to work better if it is referring to yourself.
- Added a check to make sure the Court Chronicler has to be alive before giving the player a legend seed in legend_events.0001.
- Adjusted the decision illustration for Expand the Assassins.
- It is no longer possible to get stuck away from your home location after ending a Fight Corruption contract early.
- “The Worth Ichor” tournament event no longer gives you the wounded trait if you choose to quench a weapon in your own blood, allowing you to still participate in the tourney — instead, you gain a flesh wound modifier with an equivalent health malus for two years.
- Beating up a local knight in “A Duel Demanded” now always wounds them if successful.
- Attempting to change your Province Administration, or that of your vassals, without actually making a change now disables the interaction and a tooltip tells you why.
- Added tooltip to Defensive Negotiations perk, informing the player that it unlocks the Purchase Truce interaction.
- Corrected some niche minor flavour around the Religious Pronouncements tenet.
- Fixed the holy site of Kerala in southern India not applying its conversion bonus as expected.
- The Estate UI will now automatically propose the next upgrade if there is no branch to choose.
- Fixed the All-Things innovation not increasing the prestige cost as intended for Imperial Bureaucracy when it's on cooldown.
- The AI will no longer consider all existing traits in the game when deciding to become landless adventurers, but only the traits they actually have.
- Fixed a niche issue where the Byzantines flipping between Iconoclasm & Orthodoxy repeatedly could cause the reigning faith to lose ecumenism.
- You can no longer purchase a truce if you're out of gold and would be paying with debt.
- Creating a faith with the Rite tenet will now properly preserve your old Head of Faith if you happen to hold a Holy Site.
- Penalties are now properly applied when you have a lowborn character marry you, rather than only when you marry a lowborn character.
- Fixed an issue in court event “A Knight's Declaration” where a character could start a scheme against themselves.
- Fixed petition event “Indirect Espionage” so it actually reveals secrets
- Fixed an issue where a modifier wouldn't be applied to the scheme in the event “Token of Favor”
- The priest in the event for converting faith will no longer wear a random religious clothing set.
- Offer Vassalization will no longer think that you waged war with the target if they purchased a truce from you.
- Fixed broken toast message in schemes when scheme target dies.
- The Eminent Eunuch story cycle will now show the correct ending events if the eunuch is killed, imprisoned, landed, or exiled.
- Fixed not all triggers checking for 'roman empire hard mode' being chosen or not, resulting in peasant factions targeting the top liege even if the player opted out.
- The Conduct Census contract can now only be issued by rulers with 2+ domain size to avoid deadlocks.
- Places that check for overweight/underweight values in events will now use significant numbers (50/-50) rather than being above/under 0.
- Fixed incorrect stress gain for characters with Brave trait in hunt.8510 event.
- Fixed your actions not having any consequences in the rakish_brothel_night_effect.
- Fixed women sometimes claiming that they are the father of their unborn child.
- The balanced setup option for Abduct contracts now uses the correct set of agents.
- You can now only choose to start a Raid Estate scheme against house heads with an estate.
- Legitimists can now construct the Lockwagon upgrade.
- Fixed broken string in the event “Chronicler: A Legend Found”.
- Event “Legend's Herald” can no longer target characters already promoting your legend.
- Fixed scoping issues in the travel event “The Holy Tree”.
- The Master of Spoils Camp Officer will now increase the chance of stealing artifacts during sieges as intended.
- Fixed the AI not declaring wars using the following Casus Bellis: Claim, Ducal Conquest, any De Jure, Subjugation, and a few minor CB types.
- Fixed Alchemy inspirations not getting quality added from the inspired persons skills properly.
- Added several missing pulse action events to tournaments.
- Fixed text issue in "The Shadow Behind The Throne" event option.
- The event "Runaway or Lost?" will now make sure the individual running away is at least old enough to walk.
- Made a fix for the Varangian Guard to loot their employer's palace regardless of title. They will now be happy to loot the palace of anyone who founds them, and not just Byzantium.
- Corrected duplication inside tooltip and trigger conditions for the event "Runaway or Lost?".
- Corrected underlying scope behind confusing tooltip in the event "Whispered Words.".
- Corrected minor animation scope issue in Funeral activities.
- Updated the text for the Ducal Conquest perk for Appointment succession score and made the name tooltipable.
- Stopped regents from being able to increase your Imperial Bureaucracy as a governor, since the level is set by your top liege.
- Fixed some Governor Issues triggering the incorrect follow-up event, when the issue wanted you to travel but you were at the designated location already.
- When using Petition Liege (Sponsored Priests) will now increase Convert Faith in County Council Task.
- The Province Modifier for Inconclusive Inspection is now increasing the % of failed Inspection Activity.
- Aged Immortals will no longer suffer from baldness.
- The event "In the Bud" will no longer fire when opening the Noble Families interface immediately after starting a new game.
- Courtier tasks won't be shown if you don't satisfy the requirements.
- Iconoclast priests should no longer hypocritically wear robes with icons on them.
- Fixed a crash that occurs when hovering on the spot where Legitimacy usually is while in the Character View of an Administrative Governor.
- You can no longer unilaterally arrange the marriage of your grandchildren and great-grandchildren without being their top liege, house head, or dynasty head.
- The Hunt event "The Lovers" will now be rather more selective about who it pairs up.
- Fixed crash that could occur during AI calculations.
- Fixed crash when loading a save game
- Fixed crash with opinion on character being murdered in multiplayer
- Fixed not being able to form Liberty Factions against Tribal Rulers.
- Fixed an issue with governors who were granted a Noble Family title always becoming the house head. The governor will now only become house head if it makes sense. Otherwise, they will create a cadet branch instead.
- "The Witenagemot" Realm Priest opinion modifier now displays its tooltip properly.
- The Scheme Success Chance progress bar will now correctly display the current success chance, taking into account the max chance for the scheme.
- The Court Gardener and Charioteer Court Positions will now state the correct tradition (with link) in their requirements.
- Changed foreign guest to foreign ward in “Sad Hostage” event.
- No-income landless adventurers challenging people to boardgames now wager their actual amassed gold.
- You can no longer plea to yourself in “Commander of the Faithful”.
- The Army tooltip will no longer show weird supply limit numbers on water provinces.
- Fixed double are/is in Wolf Slayer nickname.
- Fixed the Discontent Soldiers governor issue being able to spawn without a valid neighboring governor, causing broken loc.
- Beardless eunuchs should no longer get the nickname "the Bearded.".
- The Hold Court event "A Call to War" will no longer use children where it references an adult.
- Discouraged child rulers from adopting other children as their heirs in the event "A Child of the Court".
- Fixed broken and excessively long texts in event "A New Face in Camp".
- The killer in Rival's End now needs a higher intrigue skill than the victim.
- The cooldown for bloody weddings now has a 1 year duration, preventing bloody weddings from being unavailable if you back out of one once.
- Fixed several instances of scheme modifiers not having visible icons.
- Fixed Pulse Actions in Chariot Races sometimes not fetching any characters.
- Fixed several instances where children could become deviants or sodomites.
- Fixed so that the most appropriate gfx for Estate Buildings is used for each culture (such as Iranian now using the Arabic gfx).
- Adventurer character views will no longer describe them as 'realms'.
- Fixed event “Commander Promoted?” having an inverted diplomacy duel.
- Fixed the event “Your X Married Y” sometimes failing to find anyone for an entourage member to marry.
- Fixed tooltip errors in “Drifting Apart”.
- Fixed the early prevention plague event not showing the correct text if your character had the mystic trait.
- Fixed broken loc in the “Concerning Tutelage” event.
- Fixed several Tour and Tournament events where you as a player could unwittingly give away Hooks without knowing it.
- Fixed strong obligation hooks not reducing court position salaries.
- Fixed granting titles not always giving the cultural acceptance that it should.
- Fixed Adventurer recruitment gold costs not scaling in “the Recruits” event, making very good characters extremely cheap.
- Fixed incorrect portraits and triggers of the “The Necromancer” event.
- Fixed adding opinion of self in the last option of the event “A Common Enemy”.
- Fixed checking gifts on the incorrect scope in the event “Something Expensive”.
- Fixed incorrect scopes in “The Legendary X” hunt event.
- Fixed court positions sort order property.
- Fixed gaining renown and prestige as house head for adventurers.
- Fixed hook checkbox in declare war interaction.
- The Tax Collector Tab no longer warns in cases where you actually have no untaxed Vassals.
- Men-At-Arms images in tooltips now maintain their aspect ratio.
- Fixed the Co-Co-Co-Co-Co-Co-Co… when forming an alliance with your Co-Ruler.
- Choose Favorite Child and Remove Favorite Child now appears for the appropriate people (your children!)
- The markers on the Scheme progress bar now have the correctly associated tooltip.
- The event “The Last Day” always uses a blade instead of a blunt weapon for an assassination attempt.
- Grand Wedding promise is broken and penalties applied if declaring war on promised wedding target.
- Fixed hunt activity ending for landless characters when selecting to not pay for rights to hunt.
- Fixed event cameras in An Attempt on My Life event.
- Fixed Too Slow Joust Event from firing when for characters not participating in the Joust.
- Managed “A Moment Alone” weightings to avoid the event spamming.
- Fixed mismatching event effects for landless characters in What’s the Point? Event.
- Grand Wedding: Into the Night will now show the correct tooltip % chance when overhearing the servants.
- Shortened descriptions for a few overly long events from Landless Adventurer Schemes.
- Removed the name Gargamel from the French Culture List.
- Fixed lessee targeting interactions, which prevented revoking holy order locations
- The Tree Automata now stands on a tall pedestal, rather than a short one, in the throne room.
- Fixed recessive genetic traits not being passed on as they should.
- Fixed the "No valid successor" icons being incorrect on game start until the title screen is opened
- Fixed certain Danger Events not actually having any effects. For example; it’s now actually dangerous to travel in deserts as you risk dehydration.
- Fixed it not being possible to grant certain counties with temple holdings
- Fixed Negative Percentage modifiers affecting monthly piety in reverse if they were negative
- Fixed an OOS caused by vassal contract levels.
- Fixed an OOS caused by army names.
- Fixed a crash relating to top lieges when loading certain older save files.
- Fixed a rare crash related to icons on the map.


### Interface:​

- Added several new categories and options to the Barbershop, which should allow you to mix & match more items, access previously unavailable veils, and also enables the removal of spectacles/veils/face masks if desired.
- Added a dotted outline to hovered locations when selecting a new destination to travel to with your adventurer camp
- Polished the interaction panel. Added new icons for sway and murder scheme. Adjusted which icons are displayed when looking at game concepts for sway, murder, personal scheme.
- Interaction category colors have been tweaked and Favorite icon has been added.
- Your units on the map no longer show the rally point banner, but your Coat of Arms instead. The rally point banner wasn’t very useful, and we thought it more immersive to see your CoA.
- The Discovered Secret Schemes section of the Intrigue Panel has been fixed.
- Added new icons for Character Interactions.
- Fix to event header backgrounds being too contrasty making it hard to read the text.
- Added colours to travel delay/progress tooltips.
- Admin characters will now be warned when standing to lose their primary titles, and when invested characters don't stand to be appointed.
- Added simple breakdown for Legend Spread chance when hovering provinces in Legend view mode.
- Made it so that Appointment succession laws show up in the UI for administrative realms.
- Added portrait of the ward in the educator death message.
- The "Petition Liege" decision is no longer categorized as a Major Decision.
- The "Become Adventurer" decision is no longer categorized as a Major Decision.
- Grand Activities are no longer, by default, set to notify you when they become available.
- Added a "Commanded by Ruler" indicator to the Army Map Icon.
- Adjusted margins on regular tooltips to be more balanced.
- Corrected tooltip anchors in the Character View.
- Delayed Reactive advice for many features.
- Fixed missing mention of administrative government in Royal Court Reactive Advice.
- Added Current Situation Entry for if you can form a Hybrid Culture.
- Added Scheme Odds to items in the Character Interaction Menu and renamed Scheme Odds to Predicted Scheme Difficulty.
- Added Inheritable Traits filter to Character Finder.
- Made Change Succession Law panel properly display full description.
- Fixed incorrect description for how to add Artifacts to the Cabinet of Curiosities Manor Upgrade Slot.
- Scheme Phase Length is now mostly expressed in months.
- Added information if a Scheme is Personal, Hostile or Political to the Character Interaction Menu.
- Replaced the big text box about your effect from being on your Liege's Council with an icon with a tooltip.
- Fixed the Customize Route window having its Apply button covered by another interface.
- The auto-invite agents setting for schemes now persists between games.
- Renamed various Character Interactions relating to Administrative Government, House Banners and Struggles to be more consistent.
- Added foldable groups to activities view and grouped unavailable activities together.
- Province tooltip now better displays terrain and shows tiered title information in a cleaner way.
- Removed the Administrative Category in the Character Interaction Menu in favor of an Appointment Category and using already existing categories.
- The Character Interaction Menu now scrolls if you have lots of interactions added by mods.
- Character Interaction Categories now adapt their name to the target, i.e. if they are your Liege, Vassal, Governor, etc.
- Removed the Clan Category in the Character Interaction Menu in favor using already existing categories.
- Fixed bug where UI would have warnings about untaxed jurisdictions even when said jurisdictions had no Taxpayers.
- Fixed bug where using the Reset option in the Current Situation menu also reset finished Reactive Advice.
- Added colors to each category in the Character Interaction Menu.
- You can now mark Character Interactions as favorite, making them appear in a special spot in the Character Interaction Menu.
- Court Position Type tooltip now show requirements instead of showing a courtier's fulfillment of the requirements.
- Added new message for scheme advantages 5/10/15/20 threshold met.
- Added new message for non-dynasty courtier coming of age in your court.
- Added the "Reclaim Troops" button directly to the main interface in the military view, making it a lot easier to take back your troops when borrowed by other governors.
- Added the missing "+" sign on the Create Men-at-Arms Regiment button for title MaAs.
- Added list of all DLCs owned by the host once you join or start a multiplayer lobby.
- Added number of Artifact Claims on buttons that open the Artifact Claim List.
- Added History Log to Message Settings.
- Fixed the Player Outliner entries overflowing if names were too long, added a tooltip stating the full player name in case it’s too long to fit.
- If you can unlock a capstone trait in a Lifestyle, the perk icon will now have a pulsating glow to indicate that it's clickable.
- Toast titles will no longer use dark colors on a dark background, making them more readable.
- Declare war panel adjusted to fit more languages in complex casus belli.
- Fixed hitboxes on the domicile building list.
- Fixed overflow on popup window message.
- Toasts do not block windows under it anymore.
- Incoming diplomatic interactions will now use the correct text colors on the paper background, making game concepts readable.
- The Ruler Designer will no longer try to convince you that you need Ironman to unlock Achievements.
- Updated the description on the fifth Bureaucracy legacy perk, to reflect the changes made to "Order Mass Arrests".
- Reduced the amount of interaction buttons for Prisoners, Administrative Governors and your Liege in Administrative Government in favor of a popout menu
- Added access to religious interactions with your Head of Faith in the Faith View
- Replaced Reactive Advice for forming a Hybrid Culture with an entry in Current Situation, so it can reappear multiple times for each opportunity.
- The selected building now closes when you start construction
- Restricted notifications regarding new Guests arriving at your court to only neighboring title claimants.
- Added Important Actions suggestions for when you can elevate a child to co-ruler.
- Main HUD: Added the Scales of power level on the button for Power Sharing, showing the current level you have unlocked
- Character View: The Power sharing Icon now shows up on your Liege if the selected character is power sharing with them
- Character View and tooltip: For characters with no special relation to you, it will say that they are the Diarch of someone. Although other relations still take precedence sometimes
- Fixed bug where there was a "-1" step at the end of the scales of power progressbar
- Special Buildings are now visible when using the Economy Map Mode in the Lobby
- Added an Important Action for when you can elevate a child to co-ruler
- The Courtiers list will now show a text saying ‘No Guardian’ so you can easily see who you should assign guardian too while browsing children in your court.
- Added sort and filter options for children’s guardian status in the Courtiers window

### AI:​

- Fixed numerous bugs that caused unwanted behavior such as unit ‘dancing’, getting stuck, and being passive (it can still happen, but should be significantly reduced in frequency)
- Made the defending side in wars prioritize defending the war goal more if they’re feeling outnumbered.
- Subunit stacks will now abandon peripheral sieges if a lack of Siege Weapons would delay the main unit stack for too long. This removes the behavior where an AI could spend months sieging a holding without using their Siege Weapons.
- Unless needed, the AI will no longer respond with all nearby troops when one of their units gets attacked if they are active in a siege, reducing the chance for the AI to break sieges that they are about to win.
- Fixed the defending AI war coordinator never being able to pick the offensive stance.
- When merging two unit stacks, the AI will now prioritize moving stacks that aren’t actively sieging. This should make them abandon advanced sieges less often (if both stacks are sieging, the one with the least progressed siege will move).
- When spreading out units into surrounding provinces, AI will no longer select provinces that would trigger a hit of hostile attrition.
- The AI will no longer try to re-route via another province to avoid a bad supply situation if the next province on path is the target province. This should reduce instances of AI stacks moving around in circles when close to their intended target.
- The AI will no longer try to re-route via another province to avoid a bad supply situation if that would trigger a hit of hostile attrition.
- Peripheral unit stacks will now move into the target province if the main sieging unit has too few soldiers to beat the garrison and carry on the siege alone.
- Made the AI more hesitant to pursue enemy units the less war score it can gain from battles. The closer they are to the cap of warscore from battles, the more inclined they will be to siege holdings rather than hunt enemy units and pursue battles.
- If the AI is close to victory in a war and has ongoing sieges it can gain war score from, they will now prioritize keeping those sieges.
- If the AI is close to victory in a war and they can gain war score from battles, they will prioritize hunting enemy units more strongly.
- In a Great Holy War the attacking AI will first gather all units at a gathering point before starting to move towards the war target. This should make the AI go towards the GHW area in a more organized fashion.
- In a Great Holy War, after gathering its units, the attacking AI will try to find a good staging point in friendly or neutral territory close to the war target where all units will meet up before commencing the attack. This should make the AI force more capable, avoiding things such as disembarkment advantage penalties.
- Made the AI more tolerant of low supply limits during great holy wars, where they'll allow themselves to be over supply cap for unit stacks by roughly twice the normal supply limit.
- Made the AI ignore hostile attrition hits in Great Holy Wars when moving towards the goal area. This should hopefully make the AI no longer sail around Arabia to get to Jerusalem during Great Holy Wars.

### Game Balance​

- Enabled Primogeniture and Ultimogeniture for independent administrative rulers. This should provide options in the late game, allowing rulers to switch away from Acclamation.
- Rebalanced several aspects of the Clan Government:
  * Removed the 'Not Allied with Liege' opinion penalty for non-Powerful Vassals
  * Secondary Spouses no longer trigger Vassal Stance or Legitimacy penalties
  * Changing your primary spouse via interaction now does trigger Vassal Stance and Legitimacy penalties
  * The AI will now want the best sum of all skills spouse to be their primary, unless they are lowborn
  * Vassals can now be assigned as Tax Collectors, although at a lower aptitude (similar to Court Positions)
  * Buffed all Tax Decrees
    + Basic Taxes are now +20% Tax / +20% Levies
    + Zakat is now +40% Tax / +20% Levies
    + Jizya is now +100% Tax
    + Ghazi is now +10% Tax / 0% Levies
      - Ghazi now can Raid
      - War Income mult has been replaced with Zealot Opinion +1
      - Vassal bonuses have been changed:
        * Piety mult % -> Flat Piety +0.5
        * War income 5% -> 10%
        * County Control Growth + 0.25
        * Army Siege +15%
        * Raid Speed +15%
        * ai_zeal + 50
        * ai_energy +25
        * ai_war_chance + 100%
        * ai_war_cooldown -50%
    + Deqhan is now a better 'Basic Taxes'
      - +35% Tax / +35% Levies
      - Removed prestige penalty, added Legitimacy gain +1%
      - The AI will use more Deqhan decrees
    + Maguh +0% Tax
      - Vassal now gains:
        * Capital Dev +0.1
        * Holding/Building Gold Cost -10%
        * opinion_of_liege +15
    + Muqata +0% Tax / +0% Levies
      - Vassal Gains:
        * county opinion +10
        * epidemic resistance + 10
        * danger -5
  * Restricted all tax collector events so they only happen to AI tax collectors
  * Updated Tax Collector GUI to be more intriguing
- The AI will now be more inclined to use the Promote Culture Council Task under certain circumstances:
- Central Germanic heritage cultures within the HRE will now want to promote in Sorbian-culture counties
- Very small cultures will want to grow (below 10 counties)
- 'Imperious' cultures (cultures with a powerful culture head, realm of 30+ counties and King+ tier) will want to grow to a decent size (35 counties, about the size of French at 1066 start)
- Smaller (<5 counties) divergent/hybrid cultures with no existing culture head are more likely to be promoted by other cultures
- The AI is now unwilling to promote over Basque culture if it's <=5 counties
- Egalitarian or Xenophobic cultures will be more unlikely to promote
- The gold required for the AI to start developing counties has been reduced from 3 years of income to 2 years of income
- The gold required for the ai to start promoting culture has been lowered from 5 years of income to 3 years of income
- Made border disputes usable against counts.
- Made the triggers on the Promote scheme less restrictive.
- You can now build Elephant Pens in jungles outside India if the culture in the County has the Lords of the Elephant Tradition.
- The Ancient Miners cultural tradition correctly enables quarry construction in any terrain for counties with the tradition's culture.
- Rebalanced event "The Seed Merchant", reducing the overall stress gains and lowering the amount of gold paid.
- Succeeding with the Inspection activity as an administrative governor will now provide some Governor trait experience.
- Changed Orti Iniga from a courter to a prisoner of Qurtubah, discouraging him from converting to Islam.
- Monastic characters and members of holy orders will no longer be designated as Great Holy War beneficiaries.
- Updated the Acclamation succession law scoring with the following: house members of the emperor now have their score affected by the popular opinion in the capital. Making it easier for popular emperors to keep the throne within their house.
- Reduced the chance for the AI to castrate their close family members.
- Updated several candidate score gains for the Appointment succession law to no longer be based on Governor Efficiency. The impact of it was not enough to really be noticeable. Increased the base values slightly as a result.
- Independent admin rulers wanting to become feudal no longer have to be emperors.
- Vassals with a very high opinion of you will no longer join the rebel side in title revocation revolts.
- Revised the range of potential characters for which you will receive notifications regarding extramarital fornication.
- It's now possible to accidentally sire children by visiting brothels.
- Replaced the Syncretic Folk Traditions doctrine for Kuzarites so they no longer get a +60 opinion of themselves.
- Opened up the possibility for kingdom tier administrative vassals to create and join independence factions. This should give you an easier way to splinter off into your own administrative realm. Made AI admin vassals slightly less likely to join independence factions.
- One of the options in the activity event "The Guest Speaker" will no longer stack stress on top of stress.
- Set up starting truces between King Salamon of Hungary and his cousins.
- Rebalanced Haunted Manor travel event outcomes slightly.
- The Wet Nurse now also triggers events for your grandchildren and great-grandchildren if they're in your court.
- You can now search for a Wet Nurse even if you have no children at court.
- Using the interaction to change the primary spouse will now trigger lowborn marriage penalties if you're switching from a noble to a lowborn spouse.
- Slightly debuffed the positive modifiers from the event A Greater Armada.
- Added the Purchase Truce interaction to the Astute Diplomats cultural tradition.
- Added the Military Assistance interaction to the Swords for Hire cultural tradition.
- The Military Assistance interaction now requires the target to be either at least equal tier or have a larger realm than the offering party, and emperors may no longer take it.
- Added a new CB 'Seize Peripheral Duchy' that allows a non-Admin realm to take a duchy off an Admin realm, presuming said duchy is located outside the Admin realms De Jure area. This CB has 3x the Siege and Battle warscore for the attacker, and 3x the ticking warscore.
- Tribal holdings are now valid to hold for Theocracies, preventing issues where heads of faith would turn tribal.
- Being King+ is now an alternative criteria to prestige/piety levels for duchy-level holy wars/conquests; this should make larger realms start fewer inconsequential wars.
- You are now allowed to use the isolate/seclude decisions when a plague is next to your capital.
- Added a cooldown of 5 years on the Order Mass Arrests interaction, to prevent potential exploits by arresting several houses at the same time.
- Stopped the AI from demanding artifacts from you, unless they are stronger than you or a higher tier than you
- The "No End Date" Game Rule will no longer block achievement from being earned. Hunt as long as you like!

### User Modding​

- It’s now possible to script and trigger ‘War Stances’ for the AI to use. In the base game only ‘Balanced Offensive’ and ‘Balanced Defensive’ are used (alongside some special ones for Great Holy Wars).
- Added define NAI::GREAT_HOLY_WAR_SUPPLY_LIMIT_TOLERANECE.
- Added define NAI::MIN_STACK_SIZE_THRESHOLD
- Added define NAI::STRONGEST_OPPONENT_SIZE_MULTIPLIER
- Added define NAI::STACK_SIZE_SPLIT_THRESHOLD
- Added define NAI::IDEAL_ENEMY_POWER_TO_TARGET
- Added define NAI::HOSTILES_UNIT_PRIORITY_MULTIPLIER
- Added define NAI::RAIDER_UNIT_PRIORITY_MULTIPLIER
- Added define NAI::WANTED_POWER_RATIO_AGAINST_ENEMY_FOR_WAR_PLAN
- Added define CLOSE_TO_VICTORY_REMAINING_BATTLE_WAR_SCORE
- Added define CLOSE_TO_VICTORY_WAR_SCORE
- Added define CLOSE_TO_VICTORY_REMAINING_OCCUPATION_WAR_SCORE
- Added define TARGET_WILL_BREAK_ONGOING_SIEGE
- Added define CLOSE_TO_VICTORY_REMAINING_BATTLE_MULTIPLIER
- Added define CLOSE_TO_VICTORY_REMAINING_OCCUPATION_MULTIPLIER
- Added define APPLY_TARGET_WILL_BREAK_ONGOING_SIEGE_RATIO
- Added AI define UPDATE_WAR_STANCE_TICK
- Added AI define UPDATE_SPLIT_MERGE_TICK
- Added AI define UPDATE_TARGETS_TICK
- Added AI define UPDATE_TARGETS_TICK_LOPSIDED
- Added trigger 'months_from_game_start'.
- Added trigger 'participated_wars'.
- Added current_raised_military_strength trigger to character scope.
- The reroute_to_home effect has been removed and replaced with a return_home effect in character scope, which acts the same if the character has a current travel plan or forces a new travel plan home if not.
- The start_travel_plan effect now has a can_cancel_planning parameter that, if set to false, forces a human player to follow through on starting to travel to the destination
- Added defines for max points per skill.
- Add debug info in portrait tooltip for DNA accessories.
- Add debug info for holding building key and description.

### Localization​

- Remove wide gap in known languages tooltip.
- Corrected typo in text in "Eminent Eunuch" event.
- Corrected lowercase letter at start in sentence in the "Pillar of the Community" event.
- The event "Rites of Passage: The Cleansing" will no longer reference the wrong gender in text.
- The Lifestyle section of the tutorial states the right number of lifestyles if the player has Wandering Nobles enabled.
- Corrected broken localization in "Incoming Legitimist Payment" toast.
- Tooltips for the achievements "Birthright" and "Mio Cid" now display correctly when in-game.
- Tooltip for court_events.3100 now mentions the scheme modifier being added to the initiated scheme.
- Corrected description of effects in "Ebb and Flow" modifier tooltip.
- Modifying the Administration of your Theme as a vassal now displays the correct cooldown countdown.
- Added localization for rare instances where an interaction may be temporarily blocked due to being in a special event chain.
- Fixed localization for learning a language in the past tense.
- Added missing string for judaism_opinion.
- Updated text for hosting Feasts to be in line with other activities.
- Corrected a tooltip issue for the cooldown after choosing to Recruit a Chief Eunuch.
- Your memory of completing the Hajj by moving your capital to Mecca will now correctly name Mecca.
- Slightly shortened the text in the event "Till the Bitter End" to better fit the window.
- Renamed the barony of Arun to the more terrestrially appropriate Arundel.
- Fixed broken loc in Hunt event for Participants with the “Slay Beast” Intent.
- Fixed missing location name in “Shedding This Mortal Coil” event.
- Fixed tooltip with reason why vassal cannot be granted to Liege.
- Fixed loc in activity event where Host dies.
- Fixed incorrect flavor title in “Loyalty or Fear” for female landless.

### Databases​

- Adjusted age for the lover of Antso IV of Navarra.
- Gave Přemysl the Ploughman his historical nickname.
- Changed the default name of Olavinlinna to a more historically appropriate Savo.
- Corrected birth date & added mother to Bernard Aton IV de Trencavel.
- Infante Sancho of Portugal will now be married to his historical spouse in 1178.
- Corrected the Vermandois dynasty to a Robertine house.
- Resurrected Basil the Macedonian's brother and delivered his father to his eternal rest.
- Removed the ahistorical Hunchbacked trait from Roger Borsa, Robert Guiscard's son.
- Changed Conan I of Brittany's name to Konan for consistency, and created a name equivalency between Conan and Konan.
- Made the future Canute VI of Denmark one year older to start as an adult (it's ambiguous enough to work) and slightly adjusted his traits.
- Renamed the historical Přemysl Otakar I from Přemysl to Otakar, as he is more commonly remembered. Also changed his underaged wife to betrothed.
- Assigned the Devoted trait to Kaiser Heinrich IV's sisters, Adelaide and Beatrix, the historical princess-abbesses of Quedlinburg.
- Slightly adjusted the age of Pope Alexander II and set Matilda of Tuscany as friends with her mother.
- Slightly revised the traits of Gottfried the Bearded and his wife, and set his wife as a friend of the pope.
- Saladin can now speak Kurdish and Turkish.
- Filled in the history of the kings of Sweden between 1066 and 1178.
- Minor corrections to the Ediz and Yaghlakar family trees.

<!-- artifact:reactions:start -->
- 213 Love
- 116 Like
- 8 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829
<!-- artifact:op_signature:end -->
