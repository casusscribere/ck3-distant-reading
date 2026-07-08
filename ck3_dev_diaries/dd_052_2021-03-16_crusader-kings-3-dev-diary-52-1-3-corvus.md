---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1462124/"
forum_thread_id: 1462124
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 52
title: "Crusader Kings 3 Dev Diary #52 - 1.3 ‘Corvus’ Patch Notes"
dd_date: 2021-03-16
author_handle: rageair
expansion: Northern Lords
patch: Patch 1.3 (Corvus)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 8629
inline_image_count: 10
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1462124'
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
    location: raw_lines_~28_to_120
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_122_to_123
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_763_to_763
    action: preserved_and_flagged
    counts:
      Like: 1
    note: Reactions block parsed; 1 of 1 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_806_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Crusader Kings 3 Dev Diary #52 - 1.3 ‘Corvus’ Patch Notes

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Mar 16, 2021](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-51-its-time-to-duel.1461029/ "Crusader Kings 3 Dev Diary #51 - It’s Time to Duel") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-53-northern-lords-content-rundown.1463785/ "Crusader Kings 3 Dev Diary #53 - Northern Lords Content Rundown")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/?prdxDevPosts=1)

- [Mar 16, 2021](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/post-27365479)
- [Replies: 321](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/#posts)


- [/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/post-27365479](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/post-27365479)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27365479/bookmark "Bookmark")

Greetings!  

Today is the release of Northern Lords, and with it the free 1.3 patch that we’ve dubbed ‘Corvus’ in honor of Odin’s ravens! We’ve teased parts of the patch notes in previous Dev Diaries, but this time we’ll post them all - roughly 13 pages of changes and fixes, and this time there won’t be any omissions or [REDACTED] text!  

There are some notable free additions we’ve not mentioned yet that we’d like to show off! Most of them would have been dead giveaways for the theme of the Flavor Pack, but as Freya’s cat is out of the bag now - let's get to it!  


![NewCoAandMottos.png](https://forumcontent.paradoxplaza.com/public/680585/NewCoAandMottos.png "NewCoAandMottos.png")


*[Image: Norse CoAs and Mottos]*  
We’ve added numerous new Coat of Arms elements for the norse to create even more variation! Worth noting is that most titles in Scandinavia will dynamically switch which CoA they use based on if the holder is pagan or not.  

There’s also a slew of new Norse mottos that refer to their pantheon of gods (the traits of the founder of a house heavily determines which one they pick).  



![CustomRelIcons.png](https://forumcontent.paradoxplaza.com/public/680586/CustomRelIcons.png "CustomRelIcons.png")


*[Image: Custom Faith Icons]*  
There are some new Norse-themed Custom religion icons for you to choose from when creating a new Faith, some which draw inspiration from other religions - something that might suit a faith created by a Norse ruler that’s left their home far behind!  



![NewSpecialBuildings.png](https://forumcontent.paradoxplaza.com/public/680587/NewSpecialBuildings.png "NewSpecialBuildings.png")


*[Image: Special Buildings]*  
We’ve added several new Special Buildings to Scandinavia and Eastern Europe - the full list is in the patch notes, but here’s three that start as constructed in the 1066 start date.  



![ChinGoatee.png](https://forumcontent.paradoxplaza.com/public/680588/ChinGoatee.png "ChinGoatee.png")


*[Image: Chin Goatee pic]*  
While restructuring the genetic system for Hair & Beards one of our artists stumbled upon a treasure - a lost beard! For some reason this magnificent piece of chin decoration had hidden itself well, but we dug it up, and now it’s available in-game!  



![ClearNotifications.png](https://forumcontent.paradoxplaza.com/public/680589/ClearNotifications.png "ClearNotifications.png")


*[Image: Clear Notifications]*  
When you hover the title of a notification, there’s now a button that you can right-click to dismiss all currently open notifications!  



![scotland_baronies_selected.png](https://forumcontent.paradoxplaza.com/public/680595/scotland_baronies_selected.png "scotland_baronies_selected.png")


*[Image: Baronies in Scotland]*  
As previously mentioned, there are a few more areas on the map that’s been given an update. We’ve added a few new baronies to the northern parts of Scotland. Greatly reducing the average barony size.  



![iceland.png](https://forumcontent.paradoxplaza.com/public/680596/iceland.png "iceland.png")


*[Image: Iceland]*  
Iceland now has a total of nine baronies spread across four counties, up from the previous five (and rather large) baronies in two counties.  



![sapmi_01_duchy.png](https://forumcontent.paradoxplaza.com/public/680598/sapmi_01_duchy.png "sapmi_01_duchy.png")


![sapmi_02_county.png](https://forumcontent.paradoxplaza.com/public/680599/sapmi_02_county.png "sapmi_02_county.png")


![sapmi_03_terrain.png](https://forumcontent.paradoxplaza.com/public/680600/sapmi_03_terrain.png "sapmi_03_terrain.png")


*[Images: Sápmi]*  
Finally, it felt like a good opportunity to also give Sápmi some attention, being in the same area as the theme of the Flavor pack and all. The duchy layout has been tweaked slightly, adding a new duchy and adjusting the shapes of the existing duchies. Then we’ve added a number of baronies, but in order to avoid having too many baronies per county, corresponding counties have been added as well. The average number of baronies in a given county should therefore be roughly the same as before. You can also spot some new lakes and rivers, increasing the visual variety of the area.  


Now heed the advice of Huginn and Muninn, and drink deep from the well of Mímir - here are the patch notes in all their glory:  

Spoiler: CK3 1.3 Corvus Changelog

###################  
# Free Features  
###################  


- Winter is coming to the map! Certain regions will now experience icy winters, ranging from mild to harsh. Snow will spread on the map, ranging from scattered patches of frost to snow-covered landscapes. Snow will blow in the wind with increasing intensity, and you’ll hear the ambience of winter adapt to the cold and harsh reality of the area you’re looking at.
  * Mild Winters will very slightly increase the supply use of your units.
  * Normal Winters will noticeably increase the supply use of your units.
  * Harsh Winters will see supplies drain quickly, more fatal casualties will be taken, and the defender of a battle will get an advantage.
- Added the Winter Soldier commander trait, which enhances warfare when fighting in provinces affected by winter. This new trait will appear naturally on characters who reside in wintery areas, or can be acquired through events.
- Men-at-arms can now come with bonuses or penalties for fighting in Normal or Harsh winter. Cavalry will generally do poorly, especially heavy cavalry, while special units such as Himalayan Mountaineers will excel.
- A new personal combat system has been added, which allows two characters to face off against each other in a multi-stage duel. Guide your character by selecting which attacks to go for, and hopefully best your opponent without getting too injured yourself! These duels can be to the death, or to first blood.
  * While this system has been hooked into several places, the most prominent change is that the ‘Stalwart Leader’ perk in the Chivalry Focus Tree now allows you to duel your Rivals. Winning/losing these duels adds stress to the loser and de-stresses the winner.
- Added the ‘Poet’ trait to the game. This trait can be acquired via events, and allows you to use an interaction to send poems to other characters. These poems have different themes, such as Strife, Legacy, Romance or Mourning. They cost prestige to send, and can increase your target’s opinion of you, should they accept. You can also send scathing poems about your rival’s Incompetence, to cause them stress!
- Enhanced the hair & beard inheritance gene system. Instead of inheriting specific haircuts from your parents, you now inherit a ‘hair type’ gene such as ‘straight’, ‘wavy’, ‘curly’ or ‘afro’. The actual haircut a character uses is now based upon their culture. This means that the King of France won’t braid his beard like a Viking just because his grandfather happened to be Norse!
  * NOTE: Existing characters from save games made before 1.3 might get a new haircut or become bald, and old ruler designer DNA data will not have hair/beard.
  * This system does not affect the Barbershop or Ruler Designer, where you’re still able to choose whatever hair you want.
- Added a vast number of new Coat of Arms for Norse rulers, including mechanics for having Scandinavian titles switch between their Norse and Christian CoA versions depending on the holder’s faith and culture.
- Added new Special Buildings in Scandinavia and Eastern Europe, including the Golden Gate of Kiev, Danevirke, Temple of Uppsala, and more!
- Added 8 new Norse-inspired Custom Faith icons, ranging from Midgard Serpents, to Thor’s Hammers, to runic versions of Crosses and Crescents.
- Added the ‘Chin Goatee’ beard variant

###################  
# Balance  
###################  


- Men-at-Arms, Special Troops and Mercenaries now have travel time and, like Levies, have a penalty to disband/re-raise during wars. Travel time is based on the distance to the realm capital. This should effectively stop being able to ‘teleport’ MaA across the map
- The renown cost of acquiring Dynasty Legacies has been overhauled. Instead a linear progression (1000, 2000, 3000… etc.) the cost is now dynamic. It should be much easier to unlock your first few Legacy perks, but significantly harder to unlock all Legacies in the game.
- All Dynasty Legacy perks have been rebalanced. Their effects should now be much more tangible and interesting.
- The Yearly Event pools have been restructured, and a lot of triggers loosened or removed outright. In practice this means that you’ll see more events when playing (roughly one random event from this pool every 4 years rather than every 5-6 years). This also means that some extremely rare events will now appear more frequently.
- The Infirm trait events have been moved from the Yearly pulse to the Health pulse. What this means is that all characters can now become infirm, not only rulers. It is also much more likely for elderly characters to actually get the trait.
- Increased cost for sale of titles from 150 to 500 prestige
- Increased cooldown on extort subjects from 2 to 5 years
- Hosting parties now give much more relative progress for gaining Reveler traits than attending parties hosted by others, and temperate characters do not get reveler progress for attending parties at all.
- Reduced acceptance bonus on Offer Vassalization from 'wide difference in rank' and 'rightful liege'
- Reduced fascination gain from learning from +2 to +1
- Blocked joining a tyranny war if you can't join a faction against your liege
- It is now possible to recruit children from prison as long as they're not heir to one of their liege's titles
- Reduced inherent health penalty on flagellant from -0.5 to -0.15
- Reduced chance of characters randomly contracting lover's pox & great pox
- Improved the candidate selection for republican mayors: they can be of the province culture as well as their liege’s culture, will prefer to be succeeded by members of their court, and women can be selected when it makes sense
- As the Patron of a holy order, you can now hire it even if it is already hired by someone else (except another player). You pay the full piety cost to the person who has already hired it, rather than the usual hiring it for free
- Being more than 5000 men above the supply limit now causes you to lose supply faster, will scale from 5/month at 5k to 10/month at 10k
- Buildings in holdings in the domain limit grace period are now disabled entirely
- Creating a Head of Faith title now requires 1 more holy site (2 for Spiritual, 3 for Temporal). Creating a Spiritual HoF title now costs 300g rather than 50 to 300g based on your income
- Fixed Absolute Control having no effect whatsoever on levies
- Grandchildren and Great-Grandchildren should no longer wander off, following the same rules as Children
- Having a truce on someone now prevents you from raiding them
- If you're ordering your Spymaster to find secrets in your liege's court and you are your liege's Spymaster and are Disrupting Schemes, you no longer disrupt your own Spymaster's scheming
- Imprisoning and Executing characters of no particular status (i.e. lowborns) now yield much less tyranny
- Married characters will no longer wander off if they are in a realm where they are subservient to the other part of the marriage, and their spouse is in the same court
- Non-republican Barons now get married and produce a family more consistently
- Reducing the size of MaA regiments can no longer give you Fame
- Siblings now inherit ahead of parents
- The Raid Speed modifier now affects armies you command rather than armies you own
- The Witch Coven modifier now gives Disease Resistance rather than Health
- When you convert faith, prisoners are no longer guaranteed to convert. They will only do so if they'd accept if they were free. Conversion of prisoners as a direct result of faith conversion no longer releases them from prison
- When you use Grant to Low Noble, the resulting baron now gets the +20 "Received Barony" opinion towards you
- You can now Disinherit people outside your diplomatic range
- You will no longer get stress from Parents or Siblings dying of old age when they're 65 or older (if they're friends or lovers you might still get stress, though)
- Your own player heir being the player heir of their host no longer prevents you from inviting them to your court
- Your rival flinging a corpse at your castle now gives you an imprisonment reason if they're your subject.
- AI rulers who form an alliance in the middle of a war now wait 1 month before calling their new ally to arms.
- Added a strait across Mälaren, between Sigtuna and Tälje.
- Adjusted the AI Acceptance for family members and vassals offering to educate their liege's children
- Feudalizing as a Tribe no longer requires all Tribal-Era innovations, now you only need 70% (9) of all Civic & Military Innovations
- Magyars now invade immediately in 867 by default
- Moved the Argentiera Mines in the county of Cagliari to the county capital, to put it directly under the county owner.
- Paulicianism's pluralism doctrine is now Fundamentalist instead of Righteous
- The AI's willingness to white peace out of long wars now scales with how far in debt they are
- The Estonian culture now starts with the Longboats innovation
- The Pope is now more willing to lift excommunications, but doing so costs the excommunicated a Level of Fame
- When a Claimant Faction succeeds in their goal, they will free their Claimant from prison if they were a prisoner of the old title holder
- Gave Haesteinn the adventurer trait, made him a bit less vulnerable to old age
- Adjusted the starting event troop Men-at-Arms of some important rulers, gave some event troops where they were lacking entirely, and added a few to Leon to stop Wessex gobbling them up all the time

###################  
# AI  
###################  


- A desperate AI will no longer ignore hostile attrition when selecting a new order target
- A unit stack trying to merge will take into account if the target unit stack is movement locked or retreating when selecting where to move
- Added a new stance for when AI is considered desperate
- All vassals are now able to declare war no matter how deep down in the vassal tree they are
- Counter-raid AI will now look at current strength rather than max strength when deciding if it has enough strength to fight raiders
- Counter-raid units will now check if their current strength is enough to attack a raiding unit
- Discouraged unit AI to switch to a new target closer by if it means heading away from current target
- Encouraged unit AI to stick with current target if being very close to it
- Encouraged unit AI to switch to a new target if passing very close to it
- Increased min strength required to fight raiders from 60% to 75%
- Lowered target selection bonus for neighboring friendly territory from 300 to 100
- Moved target score values for supporting a player unit into defines
- No longer avoids a river crossing due to threat only
- No longer avoids a river crossing if it will be defender in the following combat
- Rebalanced target scoring to focus more on continuing and lifting sieges and less on chasing after enemy units
- Removed target selection bonus for neighboring neutral territory
- Should now be more careful about nearby enemy units when selecting a target province to go to
- Target selection bonuses for friendly & neutral territory correctly added
- The AI is now better at supporting player units that lack strength to siege
- Told the AI that if it is a count and is above its domain limit, it might be a *really* good idea to create a duchy
- Told the AI that maybe it shouldn't build more holdings while it is already above its domain limit
- War coordinators will no longer support player units that go outside of relevant areas for the war
- When declaring wars, only count an ally's strength if the ally is at peace
- Will no longer be held up in sieges unless the units are necessary for the siege to progress
- Will prioritize adjacent targets when hunting nearby enemy units unless a target further away is at least four times bigger

###################  
# Interface  
###################  


- It’s now possible to dismiss all notifications at once. Hovering the title of a notification will make a button appear. Right-clicking this button will dismiss all notifications, left-clicking it will dismiss that specific notification.
- Updated the Current Situation widget with a fresh new coat of paint. It’s now darker with more muted colors, and some flavorful decor.
  * Current Situation entries now only show ‘X’ to close when hovered
- Hovering over the unit plate of a friendly unit now shows its full path. Great for seeing where your allies are going
- Players now receive a warning when their enemy in a war forms a new alliance
- Added a Current Situation item for hooks about to expire; it'll tell you when a hook expires in less than 3 months
- Added a message that lets the employer know if their councilors leave because of marriage or title inheritance
- Building a new holding will now in the Domain view say you're building the holding type (E.G., "Castle") rather than the name of the main building (E.G., "Motte")
- Ensured scheme success and secrecy modifiers show up as percentages in all cases
- Fixed "County of Byzantion becomes the new Realm Capital of Unlanded of"
- Fixed "Different Faith Popular Opinion" reductions being shown in red rather than green
- Fixed a case where we would show an event chance higher than 100%. Yes, you're so good at your job that you can brag you've got a 173% chance of success, we all know. 100% will have to do
- Fixed clicking on units in the outliner that are in battle not having any effects. Now it'll select the battle
- Fixed constructing a holding of a type you can't hold not giving you a notification when construction completes
- Fixed effect and triggers being localized incorrectly when you're observing a character, showing things like "you is" rather than "you are"
- Fixed holy orders not being included in some character strength breakdowns
- Fixed incorrect grammar in Offer to Join War for a war you've already joined
- Fixed it being possible to change your liege's spouse task
- Fixed right-clicking on a toast often not dismissing it. This also fixes right-clicking a toast with an army selected causing a move order to be issued
- Fixed scheme modifiers losing their name in success and secrecy breakdowns after saving and reloading
- Fixed some dynasty-named titles leaving out their rank. E.G., "Seljuk" instead of "The Seljuk Empire"
- Fixed the "Defender Advantage" bonus on buildings having the Command Modifier icon
- Fixed the "modify feudal contract" button showing up even if you're not feudal
- Fixed the "you're pledged in a GHW" warning saying you're pledged against the person you're trying to declare war on rather than the actual GHW defender
- Fixed the Assault Fort button not having a proper tooltip
- Fixed the Assault button being visible even when you're not the siege leader
- Fixed the Continue and Load buttons on the main menu having no tooltip if there's no save to load
- Fixed the Force Vote window saying that you'll use a weak hook twice
- Fixed the autosave indicator getting forever hidden until you restart the game if you open the pause menu
- Fixed the concubine buttons in the character window not being greyed out when not clickable. Fixed the concubine buttons always complaining about lack of a target. The concubine buttons now cleary tell you when there's no one available to serve as a concubine
- Fixed the game saying your tax is reduced due to control when you're actually getting a bonus thanks to Absolute Control
- Fixed the game sometimes showing you entirely spurious blockers about occupations in unrelated titles when you try to revoke a title
- Fixed the knight event tooltip in the battle summary being a semi-transparent mess
- Fixed the main building in the county view (E.G., "Castle") not showing you when it's disabled
- Fixed the main menu briefly showing the default characters when going into then back out of Load Save
- Fixed the on-map construction models disappearing after saving and reloading
- Fixed the reverse sort button in the Converting Vassals window having no effect
- Fixed the siege window showing an incorrect # of men when there's more than one sieging army
- Fixed the sorting of the candidate list resetting every time someone votes
- Fixed the time to supply state change estimate sometimes being negative, or being off by a month or two
- Fixed the title destruction cost being displayed incorrectly when the title has laws; now it shows the full cost accounting for law removal
- Fixed the war declaration screen not always showing all blockers on declaring war. E.G., it wouldn't tell you that you can't declare on a fellow vassal that's fighting your liege
- Fixed war borders not showing up when you select someone who is at war unless you too are at war
- If you're both married and betrothed, the game will no longer refer to your spouse as your betrothed
- Improved on the interaction tooltip, especially how it looks when the recipient won't accept. Also made minor improvements to acceptance breakdown both here and in the interaction window itself
- Included councillors to the Increase Opinion suggestion, even those who are unlanded
- Increased the # of decimals for Piety/Prestige per Dread gain to two
- Make sure Garrison tooltips don't show decimals for building contributions
- Opening the dynasty tree now pans to the house you opened it from. It'll center on the House Head, or if you're a member of the house, you
- Show correct denomination of time in the tooltip when destroying a title
- Split in Half now only selects the original army
- The "Mercenary Company Contract expiring" alert now tells you when it expires
- The Create MaA type list is now sorted by base type (E.G., Armored Horsement and Cataphracts will be together) then by name
- The Domain view now tells you when buildings/holdings will complete
- The army tooltip's supply info now has a tooltip; the same as shown for supplies in the army window
- The combat view no longer shows a "defensive buildings" note in the advantage breakdown, but instead shows the exact buildings and similar causing that advantage
- The first letter of a title name is now capitalized in the load save menu
- The holding tooltip of empty holdings now tells you about holding construction
- The marriage interaction's "chance of children" text now has a tooltip when the chance is None explaining why
- The outliner will no longer show dead characters' opinion of you
- Vassal contract modifiers like Council Rights Guaranteed are now consolidated in tooltips if there's multiple vassals with them. E.G., you won't get 5 entries in opinion tooltips saying "Council Rights Guaranteed: -2" but instead one entry saying "Council Rights Guaranteed: -10"
- Coat of arms are now visible in the outliner entries of holdings
- Moved Invite to Court Interaction to Vassals and Court Category
- The ‘Raise Runestone’ decision is now a major decision, so you don’t miss when it’s usable (both the vanilla and Northern Lords version)

###################  
# Art  
###################  


- Replaced anachronistic pineapple with historically-appropriate melon.
- Fixed numerous clipping issues for female ‘rational’ personality animations.
- Pregnant spymasters will no longer stab themselves
- Dead HRE emperors now have the Reichskrone in their portrait. Only emperors with the HRE as their primary title wear the Reichskrone
- Ensured raised knights always wear armor and helmets. Ensured councillors who are knights don't wear armor or helmets unless they're raised

###################  
# Localization  
###################  


- Fixed an issue where a doctrine text string would show up in Debug pink in Spanish
- Fixed missing loc for the Norwegian name for Oriel/Dun Dealgan
- Added Disgraced and Sinner levels to lists of prestige and piety levels
- Added elope scheme in the game encyclopedia
- Added localization for "Any Sub Realm County"
- Added missing "Traitor" opinion name
- Added some extremely important omitted relation strings, such as 'brother-consort' and 'mother-concubine'
- Cleaned up some decision text in Russian
- Fixed some instances of tooltips where title names were not being capitalized correctly
- Grammar fix in one of the death management texts
- Made sure the toasts for a beneficiary invalidating makes sense
- Removed faulty space in inheritance toast
- Updated broke Holy Order tooltip localization for Borrow Gold from Holy Order decision
- Updated first person -> second person in religious doctrine triggers file
- Updated scope used for localization in GHW event
- Updated scripted value used for long pilgrimages
- Updated the Liberian witch god's name
- We are now less excited about you clicking on important actions!
- Changed Sussex name to match other Saxon titles
- Text in character view no longer overflows in russian

###################  
# Game Content  
###################  


- All formerly inaccessible Religious Clothes/Headgear are now accessible in the Barbershop. You want to wear the Pope’s hat and Steppe Pagan robes? Go right ahead!
- Norse Houses now have access to a wider pool of Motto’s, focusing on their many gods. Deceitful characters can reference Loki, brave ones Thor, etc.
- Added a small interaction to pardon a subject’s crimes in exchange for opinion.
- Added a few new death reasons for berserkers to execute in battle, such as cleaving people in half or viciously dismembering them!
- A guardian might now get a hook on their ward, should they be of a greedy/deceitful persuasion
- You can now offer concubines and consorts to other characters!
- When Offering Vassalization to a feudal ruler, you may now offer a more lenient Contract to improve their chance of accepting.
- Changed the 'De Jure Vassal' modifier in the Offer Vassalage interaction to 'Rightful Vassal' for balance and clarity
- Clarified the maximum bonus from Military Strength in the Offer Vassalage interaction
- Added a narrative event for converting to a new Faith, as well as a notification for when your liege converts to a new Faith.
- Replaced Tengriism's 'Sky Burials' tenet with 'Warmonger' which is more accurate for the time-period
- Rulers with an active Vow of Poverty now wear appropriately drab clothing, regardless of rank
- You now get told properly when you inherit your first empire tiered title
- Your head of faith and religious peers will now care if you found a holy order
- Jakub's pet rock stolen by parties unknown
- Added a decision for independent Norse rulers to have their realm embrace local traditions
- Norse name lists now use standardised Old Norse spellings & contains significantly fewer late period Christian names, Norwegian name lists updated to the same plus various older Christian names

###################  
# User Modding  
###################  


- Implemented HUD skin support. Different HUD skins can now be triggered based on arbitrary triggers, such as player culture.
- Added winter_movement_speed modifier
- Added dynasty_num_unlocked_perks trigger that checks the number of unlocked dynasty perks
- The game now handles transitioning between updated map setups in a smoother way, this should make it easier to keep save compatibility between different versions, and makes it easier to update for example map mods
- Add force_character_skill_recalculation effect to immediately update a character's skills
- Added a trigger title_held_years to check how many years a title has been held if valid
- Add save_opinion_value as and save_temporary_opinion_value_as which function like the scope_value equivalent but save the opinion of the scoped object to the target to avoid recalculating opinion locally multiple times.
- Added console command set_date
- Added console commands Log.ClearErrorLog and Log.ClearAll
- Added effect debug_trigger_event, which will like the console command print out the trigger and immediate effects of the event
- Added trigger time_to_hook_expiry
- Allow mood music tracks to have an is_valid for it they should be considered when picking the next track.
- Allow mood music tracks to weight the chance of being picked.
- Fix generate_coa giving the same result on the same object, it is now more properly random.
- Fixed adding a modifier with a dynamic duration causing the effect to say it'll last 0 days
- Made ai_can_target_all_titles much cheaper for the AI
- Made the geographical_region trigger much cheaper
- Message types that are used by the code will now error if they are not present when initialising the game.
- Removed .dds extension in message icon paths, they are now assumed to be a .dds like other pathed texture databases.
- Split out defender_holding_advantage from defender_advantage, for use in defensive buildings and the like
- The debug_event console command now prints out the immediate effects of the event
- The effects to add timed modifiers now support a "desc" field. This is a dynamic description that'll be resolved when the modifier is added. It'll show in the tooltip for the modifier in places like the character window. You might still want a static description (modifier name + "_desc") for the sake of the tooltip when adding the effect
- The hostile_county_attrition modifier now also affects the minimum casualties
- You can now right-click Errorhoof to clear the error log
- target_is_vassal_or_below and is_vassal_or_below_of no longer consider non-rulers (E.G., courtiers) to be "vassals". target_is_liege_or_above and is_liege_or_above_of still work for courtiers

###################  
# Databases  
###################  


- William the Bastard is now clean-shaven, as per Norman tradition!
- Nizhny Novgorod is now independent in 1066, and held by a Mari Finnish pagan.
- Made more lands in Eastern Europe pagan on game start in 1066.
- Added a few new baronies to Scotland.
- Fixed the holding setup in the counties of Miran and Kumtag, both of which had more holdings than intended on game start.
- Iceland has been updated with new baronies and counties! Increasing the number of baronies to nine, from five, spread across four counties.
- Many important and significant holdings (such as London, Alexandria, or Baghdad) now start the game with additional buildings already constructed.
- Moved out Rurik's brothers to their own dynasty in order to avoid them floating around in the Rurikid dynasty tree.
- Overhauled the barony layout in Sapmi. A few new baronies were added, and existing borders have been updated and significantly improved.
- The Abbasids now have their capital in the historical capital of Samarra in 867.
- The De Jure capital of England is now set to Winchester in 867 and London in 1066.
- Updated Ireland with new baronies and counties for increased granularity! Certain baronies were much too large in size and have been split accordingly.
- Updated a number of counties across Italy by adding additional baronies, increasing the average number of baronies per county and greatly reducing the number of two-barony counties.
- Updated the county setup in Croatia and Serbia by splitting existing counties into new ones. A few counties had too many baronies, and these have been spread out across multiple counties.
- Vladimir & Yaroslavl are now vassals to Vsevolod of Pereyaslavl.
- Updated the traits for Robert of Apulia and his son Bohemond

###################  
# Bugfixes  
###################  


- Children should no longer incorrectly become Lowborn if at least one of their (known) parents carry a Dynasty
- The Pope will no longer grant himself Rome every year, and gain Piety for it
- Fixed several instances of wounds being applied using the wrong effect, causing them to never heal
- You will no longer get asked to contribute to wars multiple times in a row if you joined several of your ally’s wars at the same time (paying once is enough!)
- Regiments can no longer have modifiers stacked to the point where they reach 0 toughness, as that would break the combat code.
- 3rd party or allied armies will no longer prevent you from using Station Besiegers
- Don't show the mouse drag selection when entering the pause menu
- Ensured all the restrictions on concubinage are properly enforced
- Fixed "Different Faith Popular Opinion" having a significantly larger effect than stated
- Fixed Great Holy Wars invalidating rather than changing target if someone for instance takes the target's primary title
- Fixed a case where loading a save from an older patch could result in the holder of a county not holding the capital barony, leading to odd issues down the line
- Fixed a case where loading an old save would result in some map names being messed up (showing Iceland or Tibet in affected areas)
- Fixed a case where negotiating an alliance would cause it to expire instantly due to somehow picking two characters who are not married as the alliance reason
- Fixed a crash that could happen due to claims on nonexistent titles
- Fixed being vastly over your domain limit outright blocking building construction, rather than simply the effects of buildings
- Fixed claims not getting removed when a title completely ceases to exist and is gone forever
- Fixed cloud saves missing in main menu save list when running the Paradox Plaza version of the game
- Fixed cultural opinions, E.G., "Norwegian Opinion: +20" doing nothing if the person with the modifier is not a ruler
- Fixed holding incomes sometimes failing to update; now they'll be at most a month out of date
- Fixed in certain cases it being possible for units to join on the wrong side of a combat if they're in the province when the combat starts, and are hostile to one side rather than directly at war with them
- Fixed incomes often being significantly off after loading a save or starting a fresh campaign. This in some cases also significantly increases the starting gold of some characters, especially those with special buildings
- Fixed it being possible to set a childhood focus on an adult if they come of age while you have the focus window open. Now the window will close instead
- Fixed prestige and piety gains in extremely large battles (hundreds of thousands of troops on both sides) sometimes having an overflow issue causing them to go negative
- Fixed the Controlled Territory Defender Advantage modifier only working for provinces you personally control, and not those of your vassals
- Fixed the Diplomatic Range modifier not having any effects. Now range between two characters is based on the highest Diplomatic Range modifier of the two
- Fixed the game sometimes reassigning baronies on conquest to different people when it shouldn't
- Fixed the loss of your pet spoon removing your pet stone instead
- Getting married now only breaks your betrothal if it is to the person you're marrying, or you have no extra spouse slot due to polygamy
- Make sure the ransom amount for the primary heir is correct
- No longer possible for two identical claimant factions to exist
- Holding preview pictures are no longer distorted
- "A Reading in X" should no longer fire multiple times during a seduction and now also gives a more accurate result
- A faction will no longer lose some discontent just before disbanding
- AI Pannonian Migration is no longer allowed for Mogyer vassals of Mogyer rulers
- Added a river crossing in the county of Mantua, to connect the baronies to each other.
- Added missing scope check to hostile scheme owner discovery option tooltip
- Added spiritual head doctrine to Zurvanism
- Added two church holdings to Iceland in 1066 and made sure both rulers are tribal
- Adopt Special Succession is no longer a major decision, meaning it is not automatically suggested for you to do
- Andalusian culture no longer starts with camels
- Bookmark characters no longer have a randomized sexuality
- Characters under 18 will now hold council props
- Claim wars are invalidated in the cases when the claimant that's not the attacker dies, leaves court, or no longer is a vassal of the attacker
- Cleaned up event about your ward switching education focus
- Directed GHWs now display a warning in the Declare War interface when on cooldown, instead of disappearing entirely
- Effect tooltip for the Sound Foundations perk will now be written in correct perspective
- Elope schemes now invalidate if you break up with your partner
- Excluded the Faroe Islands and Iceland from the Scandinavian culture conversion event
- Fixed Friendly Counsel to work in the opposite direction in the uncommon case when someone befriends you instead of you befriending them
- Fixed a potential crash in a tooltip for the war overview
- Fixed an error-spam where no portrait background would be selected for a prisoner who moved to another geographical graphic region
- Fixed an issue where vassals created additional holdings throughout a liege's realm when becoming feudal or clan. They should now only create holdings within their own sub-realm.
- Hostile schemes are now invalidated when the target isn't within the owner's diplomatic range
- It is now much harder to imprison a claimant that has the support of a faction that has pressed demands
- It's now easier to imprison your own young children if they're unfortunate enough to be in your court
- Lake Peipus is now considered to be a lake, rather than a sea.
- Loot is now always visible in the siege window.
- Made sure title creation cost for action looks at scripted value to give correct number
- Non-hostile schemes end if target moves out of their diplomatic range
- Occupation should no longer be lost on succession due to another war targeting the same province being invalidated
- Pasture buildings of level 4 and above now properly apply the development growth bonus to the county.
- Peasants will no longer stress over bankruptcy in wars
- Removed duplications in the _character_interactions.info file
- Removed the secret tunnel between Cherchen and Gomoco, allowing armies to pass through the Kunlun Mountains.
- Removed the spouse from the list of potential fathers that may get a fathered a bastard event
- Rulers are now only blocked from imprisoning the claimant when at war with a claimant faction, as opposed to being blocked from imprisoning everyone in their court
- Seduction scheme and Befriend scheme now invalidates if you become lovers or friends during intended relationship scheme
- Theocratic vassals can no longer ask for reduced tax obligations because of how religious they are when their faith is a heretical or infidel one.
- Updated feast_default.1013 to use the correct toast in one of the options
- Updated open view effect in mercenary_contract_expiring alert
- Vassal refusing to surrender will no longer refer to themselves in third person
- You can no longer arrest people for legal sodomy/deviancy/witchcraft/cannibalism just because adultery happens to be illegal for their gender
- You can no longer be both reckless and cautious, you enigma you
- You can no longer become a double-drunkard in relation event
- You can now send your kid off to university properly and easier
- You will no longer be encouraged to raid your own liege or fellow vassals
- You will now be told WHY your vassal is glued to their council seat for 25 years
- You will now be told properly when your Right-Hand Woman/Man dies
- You will now inherit the court physician of your predecessor
- Your child will no longer be left without a personality because you tried to meddle too much
- Your sibling will no longer be seen as a bastard if your dad dies before your mom knows she's pregnant
- Added a minor cooldown to the Select Personal Deity decision
- Adjusted inbreeding game concept copy to match actual effects of Pure-Blooded
- The AI can now occasionally attempt to escape from prison
- Arrogant characters now fail to account for own incompetence when escaping prison
- Can no longer imprison your own courtiers when they're guests abroad
- Include Bosnia in the 'Unite the South Slavs' decision
- It is no longer possible to Divine the Stars twice at the same time
- Moved Norse holy sites in Frisia & Denmark to Russia & England respectively, slightly rebalanced power of Uppsala holy site
- Selecting a personal deity now requires at least 0 piety to spend
- Subjugation wars now return their prestige cost when invalidating
- Tribals can now adjust tribe-valid succession laws (i.e., gender, mostly) at limited tribal authority instead of needing to reform to feudal
- Fathers of secret bastards can now realize that they are the real father even when the mother is married
- Characters can now rip their shirts off without exposing their crotch
- Ended the Crocapocalypse


In the coming weeks we’ll do Dev Diaries where we dive deep into Northern Lords content to show the process & thinking that went into it.  

Northern Lords will be released today in a little over three-and-a-half hours. Just enough time to gear up and get ready to set sail!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27365479/report)

Click to expand...

[![rageair](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/obsolete/m/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/rageair.375731/)

Written by

### [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)

CK3 Game Director

Grand Stategy

***Paradox Staff******43 Badges***

-

Messages
1.826

-

Reaction score
11.829

- [1](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [17](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/page-17#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/page-2#posts)

1 of 17

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/page-17#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/?order=prdx_dd_reaction_score)

[![Hanekin](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/ck3/s/avatar_03.png)](https://forum.paradoxplaza.com/forum/members/hanekin.1009548/)

#### [Hanekin](https://forum.paradoxplaza.com/forum/members/hanekin.1009548/)

##### Corporal

**67 Badges**

Jun 7, 2015

30

25

- ![Europa Universalis IV: Third Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/third_rome_forum_icon.png "Europa Universalis IV: Third Rome")
- ![Europa Universalis IV: Pre-order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_special_forumicon.png "Europa Universalis IV: Pre-order")
- ![Europa Universalis IV: Wealth of Nations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_won_forumicon.png "Europa Universalis IV: Wealth of Nations")
- ![Europa Universalis IV: Art of War](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aow_forum_icon.png "Europa Universalis IV: Art of War")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Europa Universalis IV: Golden Century](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gc_forum_icon.png "Europa Universalis IV: Golden Century")
- ![Stellaris: Megacorp](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MegaCorp-ForumIcon.png "Stellaris: Megacorp")
- ![Cities: Skylines Industries](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/cslindustriesicon.jpg "Cities: Skylines Industries")
- ![Europa Universalis IV: Dharma](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/dharmaicon.png "Europa Universalis IV: Dharma")
- ![Stellaris: Distant Stars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Distantstars.png "Stellaris: Distant Stars")
- ![Cities: Skylines - Parklife](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSLParkLife.png "Cities: Skylines - Parklife")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")
- ![Cities: Skylines - Campus](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSLCampus.png "Cities: Skylines - Campus")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")
- ![Europa Universalis IV: Cradle of Civilization](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EUIV_CoC.png "Europa Universalis IV: Cradle of Civilization")
- ![Cities: Skylines - Green Cities](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSL_green_cities.png "Cities: Skylines - Green Cities")
- ![Stellaris: Synthetic Dawn](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Syn_dawn_forum_icon.png "Stellaris: Synthetic Dawn")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MtGicon.png "Hearts of Iron IV: Expansion Pass")
- ![Imperator: Rome Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorsignup.png "Imperator: Rome Sign Up")
- ![Hearts of Iron IV: Graveyard of Empires](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/goe_forum_icon.png "Hearts of Iron IV: Graveyard of Empires")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Hearts of Iron IV: La Resistance](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoILRicon.png "Hearts of Iron IV: La Resistance")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Hearts of Iron IV: Battle for the Bosporus](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/bftb.png "Hearts of Iron IV: Battle for the Bosporus")
- ![Europa Universalis 4: Emperor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_emperor.png "Europa Universalis 4: Emperor")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Hearts of Iron IV: By Blood Alone](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BBA_forum_icon_16x16.png "Hearts of Iron IV: By Blood Alone")
- ![Hearts of Iron IV: No Step Back](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/NSB_forum_icon_16x16.png "Hearts of Iron IV: No Step Back")
- ![Hearts of Iron IV: Arms Against Tyranny](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AAT_forum_icon_16x16.png "Hearts of Iron IV: Arms Against Tyranny")
- ![Hearts of Iron IV: Götterdämmerung](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gtd.png "Hearts of Iron IV: Götterdämmerung")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![For the Motherland](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FTM1.png "For the Motherland")
- ![Hearts of Iron III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi3_forum_icon.gif "Hearts of Iron III")
- ![Hearts of Iron III: Their Finest Hour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/TFH_forumicon.png "Hearts of Iron III: Their Finest Hour")
- ![Hearts of Iron III Collection](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi3col_medal.png "Hearts of Iron III Collection")
- ![Semper Fi](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/sefi.png "Semper Fi")
- ![Cities: Skylines](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/csl.png "Cities: Skylines")
- ![Cities: Skylines Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/csldelux.png "Cities: Skylines Deluxe Edition")
- ![Europa Universalis IV: El Dorado](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_eldorado_forumicon.png "Europa Universalis IV: El Dorado")
- ![Europa Universalis IV: Common Sense](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cs_forumicon.png "Europa Universalis IV: Common Sense")
- ![Cities: Skylines - After Dark](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CS_AD_16x16_fotumicon.png "Cities: Skylines - After Dark")
- ![Europa Universalis IV: Cossacks](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cossacks.jpg "Europa Universalis IV: Cossacks")
- ![Cities: Skylines - Snowfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/snowflake_16_4.png "Cities: Skylines - Snowfall")
- ![Europa Universalis IV: Mare Nostrum](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_marenostrum.png "Europa Universalis IV: Mare Nostrum")

[](javascript:;)

- [Mar 16, 2021](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/post-27366031)


- [/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/post-27366031](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/post-27366031)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27366031/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-52-1-3-corvus-patch-notes.1462124/post-27366031)

Looking forward to it.

 

- 1

<!-- artifact:reactions:start -->
- 1 Like
<!-- artifact:reactions:end -->
