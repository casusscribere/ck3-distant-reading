---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1541141/"
forum_thread_id: 1541141
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 107
title: "Development Diary #107: 1.7.0 \"Bastion\" Update Notes"
dd_date: 2022-09-08
author_handle: sidestep
expansion: Friends and Foes
patch: Patch 1.7 (Bastion)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 6117
inline_image_count: 3
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1541141'
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
    location: raw_lines_~28_to_117
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_119_to_120
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_532_to_537
    action: preserved_and_flagged
    counts:
      Like: 96
      Haha: 71
      Love: 22
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_545_to_613
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_614_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Development Diary #107: 1.7.0 "Bastion" Update Notes

<!-- artifact:thread_metadata:start -->
- Thread starter [sidestep](https://forum.paradoxplaza.com/forum/members/sidestep.1286696/)
- Start date [Sep 8, 2022](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-107-1-7-0-bastion-update-notes.1541141/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-107-1-7-0-bastion-update-notes.1541141/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-107-1-7-0-bastion-update-notes.1541141/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-107-1-7-0-bastion-update-notes.1541141/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dd-106-a-fistful-of-friends-foes.1540926/ "DD #106: A Fistful Of Friends &amp; Foes") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-108-dev-diary-scheduling-community-activities.1543480/ "Dev Diary #108: Dev Diary Scheduling &amp; Community Activities")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-107-1-7-0-bastion-update-notes.1541141/?prdxDevPosts=1)

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2053.jpg?1662646946)

# Development Diary #107: 1.7.0 "Bastion" Update Notes

- Thread starter [sidestep](https://forum.paradoxplaza.com/forum/members/sidestep.1286696/)
- Start date [Sep 8, 2022](https://forum.paradoxplaza.com/forum/developer-diary/development-diary-107-1-7-0-bastion-update-notes.1541141/)

Heya everyone!  
This is your friendly neighborhood Tech Lead Zack. Someone made the rather unwise decision to allow me to write this dev diary for the "Bastion" update ( I think everyone else was sick ) and I intend to milk it as much as I can. "Bastion" goes live later today with Friends & Foes and I'm so happy to finally be able to share it with you. I'm the Tech Lead "in charge" of Friends & Foes which means that I work with the team to determine what tech ( see: code ) we can actually add to the update, that it works as it should and that we at the end of the day have a functioning build to deliver to you ( among other things, I also sit in a lot of meetings where I usually have a lot of wise and important things to say ![;)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Wink    ;)") ). This is the first Event Pack that we have done for CK3 so me and the team have been treading a lot of new ground, which has been very exciting, and I also think that it's the best one so far!

![badum tsss.jpg](https://forumcontent.paradoxplaza.com/public/861912/badum tsss.jpg "badum tsss.jpg")



![medal meme for ff.jpg](https://forumcontent.paradoxplaza.com/public/861914/medal meme for ff.jpg "medal meme for ff.jpg")



"Fun" tidbits from the development of F&F:  


- We collected a bunch of name suggestions for the update and voted but I forgot which one we decided on and just picked "Bastion" because that was my favorite. It was probably the winner anyway, right?
- The '&' in Friends & Foes caused technical issues in one specific backend system due to it being a special character, so it had to be redone...but I wasn't here then so Joel had to do it for me instead ( funny ).
- We had a technical issue that only happened when saving saves with an even number of characters, it worked with an odd number. I thought it was funny, QA did ***not***. Then when I realized I had to fix it I didn't find it funny anymore but ***then*** QA suddenly thought it was funny, so I guess it evened out.
- We had a merge that got screwed up so bad that it broke our changelog generation, therefore I had to manually find a lot of entries ( needle, haystack, fun ). Doing the merge itself was also a lot of fun, I'll be releasing a book about it titled "Zack and the Merge That Never Ended" and I'm forcing the design team ( who no doubt made fun of me during the ordeal ) to write it for me, good luck.
- We added a new jungle event image that had so many hidden monkeys that we kept finding new ones throughout the dev cycle, we probably haven't found them all yet.
- The gallows art is very well done, but also weirdly "upbeat" according to the design team. Proper gallows-humour right there.

Jokes and tidbits aside; it has been super fun working on Friends & Foes, I could absolutely not have done it without the rest of the team and I hope you all enjoy it. Below you can find what you were actually looking for in this thread. Thanks for reading and playing, and remember: an enemy is just another potential lover that is slightly harder to woo!  


Spoiler: 1.7.0 Bastion Update Notes

###################  
# Expansion Features  
###################  


- Over one hundred new events and event chains which expand upon the relationships you have with your family, friends, rivals, best friends, and nemeses. Experience a much more varied pool of random events every year, as well as specific heart-wrenching (or heart-stabbing!) reactive content for when you, as an example, lie dying, or when someone close to you takes part in a foreign battle.
  * New events for finding and living with spouses: spoil your partners and suffer the consequences, deal with multiple rival spouses pushing their children to be first in the line of succession, rein in (or allow) an overly-zealous spouse from burning books to ensure your children remain pure, and seek out a potential partner who must first be defeated in combat before they will allow you to take their hand in marriage!
  * Manage life as a parent: deal with squabbles between children vying for their line in succession, correspond with a married-off offspring, and assuage the doubts and jealousy of the child of a concubine who wishes to be treated equally to their siblings.
  * Navigate the pitfalls of life as a Medieval child: make a friend at a bonfire, fend off would-be fratricide or sororicide from envious siblings, and swear eternal vengeance on bullies after they break your favorite toy.
  * Explore the joys of friendship: share war stories with an old friend and make a new one at the bathhouse. Resist the temptations of a dead friend’s spouse throwing amorous glances your way, forgive your gluttonous best mate for eating you out of house and home, stage an intervention for a companion when they are far too fond of a drink, attempt to matchmake for a lonely confidant, and attempt to ease the suffering of a friend as they pass on from this life.
  * Discover the depths of rivalry with your rivals: get into brawls on the wharf and in the pub, arm-wrestle to prove a point, burn their artifacts in front of them, wait until a bitter nemesis dies and then dig them up and defile their body to get back at them even after death. Sleep with your rivals’ offspring, or even sleep with them! Be careful of the consequences…
  * From small storylets to larger event chains, this content will weave new dramatic narratives about friendships, vengeance, feuds between houses, memories of the past, and much, much more.
- New mood music focusing on the Middle East, the Western sphere, and some that fit regardless of where you play


###################  
# Free Features  
###################  


- Added an additional set of 12 new Childhood Personality Events, this will make certain personality trait combinations much more likely to appear, and also makes certain combinations possible that previously weren’t. The trait combinations are balanced in such a way that the choice for you as a guardian should be more interesting:
  * diligent, gregarious, temperate
  * zealous, ambitious, sadistic
  * shy, paranoid, craven
  * lazy, gluttonous, compassionate
  * lustful, chaste
  * just, greedy, callous
  * humble, cynical, content
  * vengeful, deceitful, calm
  * generous, fickle, arrogant
  * forgiving, trusting, patient
  * honest, arbitrary, impatient
  * brave, stubborn, wrathful
- When a Friend, Best Friend, Rival, Nemesis, Lover, or Soulmate relation is formed, a reason will now be stated. For example: “Kaiser Heinrich and King Philippe shared an excellent feast in Aachen” or “Basileus Andreas swore to avenge the death of Aristarchos, who was slain in battle by Ulf Munk”. These reasons can be viewed for any character in the Relationships tab in the Character Window, presuming the relation is public.
- Added relationship icons on character portraits so you can see who is your friend/rival/lover at a glance, along with an informative tooltip
- Characters now have Memories of things happening in their lives (children born, battles won, rivals killed, etc etc.). These memories are used in events and other content. For example, if you are murdered your assassin might cite a grievance that your killer had against you. These memories might fade with time, and are usually lost on death. For certain characters memories are preserved longer or even forever (such as rulers the player has controlled, and high tier rulers).
- Memories can be viewed by opening the Memory Viewer from the character window, via a button in the same place as the Kill List, Inventory, and Lifestyle.
  * Memories are listed chronologically alongside the date they were added (you can flip direction with a toggle).
  * Private memories will not be visible unless it’s your own character, or you are in Observer mode. (private memories such as gaining a lover or murdering someone).
  * You can view the public memories of any character in the world.
  * Memory lists can be copied to the clipboard via a button and shared outside the game.
  * For convenience you can pin the Memory Viewer to one character, or browse through different characters while keeping the Memory Viewer open.
  * Memories are collected up during game play time, but some characters may start with some already in place.
- Added the Loyal/Disloyal Traits, which affect how likely a character is to join factions, cheat on their spouse, etc. These traits are integrated as Sins/Virtues, hooked into Cultural Traditions, and can be gained through new events.
- Reworked Populist Factions in order to improve their functionality, especially in regards to how they interact with player vassals:
  * Vassals directly affected by a Populist Revolt now get a letter from the revolt leader, asking the vassal how they will respond to their demand. The vassal may:
    + Join the war and help their liege
    + Convert to the faction's culture and/or faith and join the war on the side of the rebels
    + Stay out of the war and do nothing (though still risk losing land if the liege loses the war)
  * AI vassals are most likely to join the war on the side of their liege, but can in rare cases pick either of the other two options
  * Made it so that AI lieges will never accept the faction demand if a player vassal is targeted by the faction (this will finally allow player vassals to intervene and help protect their own realm)
  * Greatly increased the military strength of Populist Factions, to compensate for the fact that vassals can join the war:
    + Populist armies now spawn a few basic Men-at-Arms in addition to levies
    + Populist armies spawn Siege Weapons depending on their culture's innovations, allowing them to better scale into the late game
    + Populist factions now generate a few commanders to lead their troops
  * The populist leader will now get some extra gold upon victory, to ensure that they can afford creating titles and Men-at-Arms
  * Reduced the rate at which factions gain discontent for being over the military power threshold. In practice, this will give rulers a longer time to react before factions press their ultimatum (especially when the faction is only slightly stronger than their target)
  * A successful Populist Faction will no longer usurp or create an existing title if they don't control at least 50% of its De Jure (this is to prevent titles from being usurped too easily)
  * Increased the restrictions for a successful Populist Faction to create custom kingdoms and duchies. They will primarily attempt to create a title without a holder or usurp an existing title
  * Rulers participating in a Populist Faction will now become independent if they have too high a rank to be vassalized by the populist leader, instead of remaining a vassal to their old liege
  * The leader of a successful Populist Faction should no longer steal counties from rulers joining the revolt
- Added 14 new event illustrations
  * Food Cellar
  * Crossroads with Inn
  * Hills
  * Plains
  * Bonfire
  * Kitchen (Western)
  * Jungle
  * Desert/Drylands
  * Docks (Tribal)
  * Castle Corridor Day/Night (Indian)
  * Courtyard (Indian)
  * Courtyard (MENA)
  * Relaxing Room
  * Wetlands
- 7 new character animations for events
  * Assassination pose with raised knife
  * Eavesdropping
  * Eye Rolling
  * Laughing
  * Drinking from Goblet
  * Holding Lantern
  * Toast Using Tankard

###################  
# Balance  
###################  
- 'Domestic Affairs' now also increases the rate in which you lose tyranny  
- A lot of interactions that used to consider max military strength will now consider current military strength  
- AI Muslim rulers with Jizya active no longer indiscriminately convert Apostolics if they aren't zealous  
- AI counts will no longer complain that their capital county is under their De Jure when you're revoking their titles  
- AI rulers will now elect to end their offensive wars should the defender end up being inherited by the Mongol Empire  
- AI rulers with Religious Taxation active no longer convert faiths within their own religious group without being somewhat zealous first  
- Added AI weights and a longer cooldown to the Latrine Disaster event  
- Baltic Pagans are now much more unlikely to spontaneously convert to an organized faith  
- Caliphal Subjugation is now based on adherence to Head of Faith, rather than same faith (which means that the Sunni caliph can subjugate Ashari, Maturidi, and Mutazili, for example)  
- Changed yearly.8200 to be based on your gold values rather than the priests  
- Clans can now offer religious exemption when vassalizing  
- You can now ask for religious exemption when swearing fealty to a clan  
- Common rarity artifacts are now more likely to get damaged in sieges than stolen  
- Craven, Content and Trusting AI's are now more likely to say yes to title revocation and vassal retraction  
- Generous characters now lose stress by giving away titles  
- Harold Godwinson will no longer get alliances within the first 5 years of the game, to let the battle for England play out first  
- If you have your temporal Head of Faith vassalized, you can now direct GHW's if they're enabled  
- Isolationist Cultures are now harder to vassalize  
- Norse characters will now tend to convert to their divergent scandinavian cultures if appropriate  
- Offer Vassalization - Added 20 acceptance for having an alliance  
- Offer Vassalization - Added 20 acceptance for offering to a realm encircled by yours, without access to the coast  
- Offer Vassalization - Added a penalty for Feudals trying to vassalize Tribals, and vice versa  
- Offer Vassalization - Added a penalty for being a year or more in debt  
- Offer Vassalization - Added an acceptance modifier based on how well-liked you are by your Powerful Vassals, ranging between -20 to +20  
- Offer Vassalization - Base acceptance changed to -50 from -45  
- Offer Vassalization - Being the Rightful Liege/Unrighful Liege is now +20/-20, changed from +10/-25  
- Offer Vassalization - Increased the claimant modifier to -20  
- Offer Vassalization - Increased the rivalry modifier to -100  
- Offer Vassalization - Lover/Soulmate now gives +10/+20 acceptance  
- Offer Vassalization - The 'I am a King', 'We just fought against each other', and 'I fought an independence war against you' negative reasons have been increased, to offset the new positive reasons (you shouldn't be able to vassalize kings easily!)  
- Offer Vassalization - The 'Wide difference in rank' modifier is now 10, up from 5  
- Offer Vassalization - The Ambitions, Arrogant, Paranoid, Fickle, and Stubborn traits now reduce acceptance by -10/-20  
- Offer Vassalization - The Opinion Modifier now matter twice as much for clans (up to a potential +70 from +35), to make up for the fact that they can't offer better vassal contracts  
- Offer Vassalization - The Trusting and Content traits increase acceptance by 5  
- Reduced the vassalization acceptance bonus from the Diplomatic Court Type  
- Lowered the effect of True Ruler from 25 to 20  
- Significantly lowered the chances of artifacts getting damaged during feasts  
- Slightly loosened the requirements of pagan conversions for the AI so that less scattered pagan realms persist into the very late game  
- Steppe rulers will no longer automatically feudalize when converting to a non-pagan religion, to preserve the steppe tribal for longer  
- Rulers of Successor Khanates (Golden Horde, Chagatai, etc) are now much less likely to be sick, infirm, underage, of an ill-fitting culture, etc, while also now favoring highly skilled characters.  
- Significantly revised how the Successor Khanates spawn, patching many holes where they would fail to form, and ensuring that their borders are more logical and contiguous  
- Successor Khanate heirs will now switch to a majority faith of their new realm if they are Pagan upon succession  
- Successor Khanates now start with 100 dread to help them survive the first few years  
- Successor Khanates now start with High Partition  
- Successor Khanates will now be given a De Jure area depending on what they hold, within reason (the Ilkhanate will not shift all of persia, don't worry)  
- The 'guardian of my relative' opinion modifier now stacks  
- The AI is now slightly more willing to give up land or vassals that belong to their liege's primary title's capital duchy (i.e. Valois for the Kingdom of France)  
- The AI will now tend to not attempt imprisonments of landed vassals when chances are exceedingly low, unless they're lunatics  
- Patched an exploit where you could give the same artifact to multiple people, now only one will get it  
- The Gift Artifact interaction is now instant  
- The Gift Artifact interaction no longer shares opinion modifier with Send Gift, so you can do both to the same character  
- The Greatest of Khans trait and Modifiers now give Horse Archer and Light Cavalry siege speed bonuses  
- The Mongol Empire now starts with High Tribal Authority  
- The Mongol Empire will now always spawn as Tribal  
- The Mongol successor states (Chagatai, golden Horde, ilkhanate, etc.) now get some event troops and a little bit of gold to prevent them from instantly collapsing  
- The Mongols are now much less likely to gallop their horses into the mountains of Tibet  
- The Mongols now do not get Peasant Factions while a Great Khan is ruling them  
- The Mongols now get more dread from devastating provinces  
- The Mongols now have a chance to devastate counties when subjugating rulers in war, even if they do not siege them directly  
- The Royal Armory Duchy Building now also gives an army maintenance % reduction  
- The Seneschal position now provides slightly less control growth  
- The rivalry set by stress_threshold_prison.1031 is now applied when let out of prison for the AI, to avoid having a steady source of rivals to execute for stress loss for the player  
- The stress impact from revoking titles with the Generous trait has been lowered  
- There's now a chance to steal artifacts from barons in sieges, should they have any  
- Tyranny Reducing effects from Artifacts are now less powerful  
- When embracing the English culture, all children and all vassal's children will now also convert to the English culture  
- When vassalizing someone, they'll now gain an opinion modifier that prevents them from joining Independence and Dissolution factions  
- You as the liege no longer lose a piety level for choosing not to imprison the guilty party in secret reveal events  
- You can no longer seize the gold from realm priests through banishment, and any gold that former realm priests hold will be transferred to the new realm priest if possible  
- You now get more opinion when gifting greedy characters artifacts  
- You now only need 1 Holy Site to create or recreate a Head of Faith title  
- AI vassals are now more likely to offer a gift when paying homage  
- Boosted the control gain from requesting Bailiffs from your Liege in a Petition  
- Children that are 10+ years old at game start will now always be assigned a sexuality  
- Non-landed children will now more often get bullies, victims, friends, and crushes  
- k_naples is now a valid title for the Wily as the Fox achievement  

###################  
# AI  
###################  
- AI characters are now much less likely to convert to Adamitism, only truly irrational characters will consider it  
- AI characters will now more often accept imprisonment and revoke title demands made by Genghis Khan  
- AI rulers will now hire and preserve a Seneschal Court Position if they have Counties with low control, regardless of debt level (if at peace)  
- AI's with the Peacemaker perk or the Stalwart Defenders tradition will now end wars earlier  
- Barons will now use more of their gold on building buildings  
- City Barons in Drylands and Deserts now prefer economic buildings over building camel farms  
- Depending on personality, the AI will now much more aggressively pursue control through revocation of Counties in its primary title's capital duchy as long as it has room in its domain, taking on a modicum of tyranny when doing so. This makes the AI better at consolidating a powerbase for their realm.  
- Make attacker Dukes, Kings and Emperors raise their armies in a safe county close to the war goal county that is closest to their capital.  
- Make defending Dukes, Kings and Emperors raise their armies in a safe county close to the war goal county that is closest to their capital.  
- Players are fickle on the best of days and dishonorable on the worst! No longer shall we depend on their assistance when we declare our righteous wars for [GetWarReason]! They may still interfere with our plans, so we will still be weary of enemy player alliances.  
- Removed the restriction on Shy and Callous characters on using the Sway scheme  
- Slightly lowered the AI's preference to buy MaA over buildings  
- The AI is now choosier when using the interaction to select who to seduce/romance; they will tend to want fertile characters close to their own age, unless there are special circumstances (deviants will seduce anyone, lustful/temptation focus characters have a larger age span, temptation focused characters want to seduce vassals/liege/realm priests, only irrational and lustful/incestuous characters may seduce much older family members, and everyone is free to seduce their own spouse/s). Note that this does not affect seductions/romances started via events.  
- The AI is now more inclined to use the Organize Army task when bankrupt if they're rational  
- The AI now attempts vassalizations more frequently  
- The AI now slightly favors building the really good economic buildings (Farm Estates, Orchards, Cereal Fields, Quarries, Logging Camps, Regimental Camps)  
- The AI will be better at using the Support Schemes council task when they are performing murder schemes  
- The AI will no longer accept a negotiated alliance from someone they want to revoke land from in their primary duchy  
- The AI will no longer launch directed great holy wars/Jihads on an area where they would get less than 5 counties  
- The AI will no longer spend time swaying non-councillor barons  
- The AI will now always construct Farm Estates or Orchards before constructing Trade Posts  
- The AI will now join defensive Holy Wars if they're decently Zealous and Bold, with enough gold to support their armies for a time  
- The AI will now more aggressively use the fabricate hook scheme on vassals with modifiable contracts, especially if the vassal's spymaster is poor (and thus the success chance is higher)  
- The AI will now much more aggressively pursue control through revocation of its primary title's de jure capital county and duchy.  
- The AI will now not want to build Duchy Capital or Special buildings before they've filled all regular building slots  
- The AI will now only consider Artifact Wars against close rulers  
- The AI will now recreate destroyed temporal Head of Faith titles (such as the caliphates) much more frequently  
- The AI will now send spare children to be educated by vassals in order to increase their opinion  
- The AI will now spend more of its money on Buildings and MaA, depending on stage of the game and personality. Early on, most AI's will want to develop the buildings in their capital quickly, and later in the game their willingness to spend gold will in large parts depend on which personality archetype of these they fall into: Warmonger, Cautious, Builder, or Unpredictable. The AI boldness value also plays a big part.  
- AI's with an 'Builder' personality will now prefer filling free building slots with Economic buildings  
- The AI will now target their Realm Priest with the Sway scheme much more frequently  
- The AI will now tend to sway unhappy vassals for longer  
- The AI will now try to appoint a righteous caliph (the decision to create your own caliphate as for example Muwhalladi) much more often  
- The AI will now try to educate their children in languages that their future subjects will speak, to prepare them for rulership  
- The AI will now use Commission Artifact, Hunt, and Feast less often when they don't have a lot of spare gold, and even less if they're of an 'Economic Boom' personality archetype  
- The AI will now use Disrupt Schemes when appropriate (paranoid, threatened by siblings, targeted by an exposed scheme, etc)  
- The AI will now use the Befriend, Romance, and Learn Language schemes somewhat more frequently  
- The AI will now use the Develop Capital and Expedite Schemes decisions  
- The AI will now use the Find Secrets council task if they are sufficiently devious/dishonorable  
- The AI will now use the Sway scheme much more frequently  
- The AI will now use the stress reducing decision granted by stress traits more often (except for the ones where they wound themselves or spend a lot of gold, those remain rarer)  
- The AI will now vastly prefer building all tier 1 buildings in its capital county before starting on secondary holdings  
- The AI will now want to build all tier 1 buildings in a province before upgrading them  
- The AI will now want to revoke secondary baronies that it can hold if it's below domain limit  
- The Mongol Empire and its successor khanates are now less likely to simply give in to faction demands without a fight  
- The Mongols will now never give in to Dissolution or Independence wars, they will always fight  
- The Mongols will now prefer invading eastern european lands over the byzantine empire (no guarantees, though!)  
- Zealous AI's will now attempt to get their children educated by their head of faith  
- Zealous AI's will now sometimes send gifts to the defender in a GHW if they're nearing bankruptcy  
- The AI will no longer Bestow Royal Favor on vassals of vassals  
- Fixed combat evaluation incorrectly used on sea zones, leading to many naval invasions being impossible.  

###################  
# Interface  
###################  
- Added a handful of icons to core character interactions  
- Added another decimal point to the display of Development Growth  
- Added missing icon to 'Tamer of Horses' modifier  
- Duchy Buildings will now properly tell the reader why they're disabled  
- Made the old event 'Ecstatic Peasantry' nicer  
- The 'Gift Artifact' interaction now only shows unequipped artifacts, to make it easier to give away excess artifacts  
- The 'Offer Ward' interaction now lists children with existing guardians, so you don't have to manually remove the old guardian before sending them to a new guardian  
- The Coming of Age events now use more interesting/telling animations and backgrounds  
- The GHW CB's now use a more appropriate icon, and are listed at the top of the CB list  
- The Learn Language scheme will no longer say it's invalidated when it's succeeded  
- The Rags to Riches 1066 bookmark is now the default bookmark again  
- The Sway invalidated toasts should now look decent  
- Viewing a Barony title that is not created yet will show terrain type in background  
- Characters in events will now animate even if dead to allow for spooky content  
- Heir icon should now always be visible when relevant  
- Rivals should now always appear in the character screen  

###################  
# Localization  
###################  
- Added text for a missing string in the Pagan Syncretism tenet  
- Fixed French description of Pontic Whispers travel inspiration event  
- Fixed Spanish issue of Grant Vassal interaction  
- Fixed localization of Zoroastrian Witch god pronouns  
- Fixed misleading information in Culture Encyclopedia entry and Divergent Cultures concept  
- Fixed missing explanation tooltip for Grant Titles interaction when recipient was invalid  
- Fixed missing trigger description for Promote Christian Settlers decision  
- Fixed oaf insult being pink sometimes  
- Fixed religion tooltip of Forge Jomsvikings decision  
- Fixed saying goodbye when recruiting prisoners to your court  
- Simple fix to ensure babies are not speaking in an adult's voice. I had to take a guess at the age at which a baby starts speaking coherently. I was advised not to put "15+", even though it's true.  
- Fixed numerous translation issues with Spanish Lady/Lord  
- The translations for Primogeniture and Ultimogeniture are now correct  
- Fixed mongol succession event not getting heir name correctly  
- Fixed Spanish Contract Assistance interface localization  
- Fixed Spanish al/la localization issues in character greetings  

###################  
# Game Content  
###################  
- Reduced likeliness of AI engaging in incest as part of the "Something More" event where one might become romantically interested in a friend.  
- Reworked the 'A Growing Shadow' childhood event  
- Reworked the 'Always On My Mind' childhood event  
- Reworked the 'Concern of a Friend' childhood event  
- Reworked the 'Destruction of the Toy' childhood event  
- Reworked the 'Diligent parent lazy child' childhood event  
- Reworked the 'Get a Bully' childhood event  
- Reworked the 'Get a Crush' childhood event  
- Reworked the 'Get a Friend' childhood event  
- Reworked the 'Get a Victim' childhood event  
- Reworked the 'Harsh Punishment' childhood event  
- Reworked the 'Make your bully stop being such a bully' childhood event  
- Reworked the 'Parent increases stress' childhood event  
- Reworked the 'Parent is your educator' childhood event  
- Reworked the 'Parent reduces stress' childhood event  
- Reworked the 'The Way of the Heart' childhood event  
- Reworked the 'Unconventional Coping' childhood event  
- Reworked the 'Your friendship can turn into a crush' childhood event  
- Reworked the various 'Child gets a pet' childhood events  
- Reworked the various 'Child studies X skill' childhood events  
- You can now get a crush on an actual peasant character in one of the sexuality events that references one  
- Added opt-out options and a chance for gaining Best Friend to the friendship.2001 and friendship.2004 events  
- Condensed the effects of friendship.2007, and added a small chance of getting a best friend  
- Rebalanced friendship.3006 and added stress impacts  
- Tweaked and improved friendship.0003  
- Tweaked and improved friendship.1006 where you get war support from your friend, you now generally get more money, and can extort your friends for even more money if you wish  
- Added a bit more cool stuff to the mystical animal hunt  

###################  
# User Modding  
###################  
- Add current_military_strength trigger.  
- Add powerful_vassal list builder.  
- Added ignore_titularity_for_title_weighting to titles. This means a title can now be specified to utilize the regular title weighing rules on titular titles when the AI selects a primary title.  
- Added more AI gold budget manipulation potential. For each gold budget ('reserved', 'war_chest', 'short_term', 'long_term') there now exist effects: 'remove_*_gold', 'pay_*_gold', 'pay_*_income', 'add_*_gold'. Can now also pump money between budgets with 'move_budget_gold', allowing party-dukes to dip into the war chest for "essentials".  
- Renamed 'ai_war_chest' to 'war_chest_gold' for consistency  
- Renamed 'war_chest_gold', 'war_chest_prestige', 'war_chest_gold' to 'ghw_'+previous name for consistency  
- For each AI budget type there is now a trigger '*_gold', '*_gold_maximum'/'ai_*_gold_maximum'  
- You can now set the 'reserved' budget maximum via 'set_reserved_gold_maximum' in script, allowing for non-Popes and non-Holy Orders to create exclusive special budgets.  
- Added a realm_law_use_tribal_authority scripted trigger, separate from the realm_law_use_crown_authority scripted trigger, so that new authority law types can be added without overwriting vanilla authority laws  
- History character and title effects are now actually executed on the date they're defined at  
- The bypass_requirements console cheat was removed for Laws, because it messed up succession logic. Changed the cheat a bit so it will not cheat you out of your succession.  
- Memory retention on death can be defined by character tier in script defines, but beware of chonky save game file sizes this might cause.  

###################  
# Databases  
###################  
- Added a few traits to Basileios Basileios  
- Chagatai is now known as such, not 'The Chagatai'  
- Genghis Khan now starts with Athletic  
- Removed color2 definitions from landed titles database, as they are not used for anything.  
- The Golden Horde now has the correct historical capital set, Itil  
- The Mongol Successor Khanates will no longer be named after dynasties (so that you will see 'Golden Horde', etc)  
- The Sunni, Shia, and Muwhalladi Caliphates now have a capital county defined so that their AI's know which area to consolidate  
- Satisfied community thirstiness for Bohemond  

###################  
# Bugfixes  
###################  
- Characters will no longer consider members of their own faith Astray  
- AI's will now focus on one Dynasty Legacy track while valid for the Fate of Iberia legacies  
- Adoptionism can no longer appear as a regional heresy without first being revived through nebulous means  
- Event lover.7002 will now set the lover relation if you are already potential lovers  
- Faiths with Syncretic tenets should now never end up with negative faith conversion progress  
- Fixed an issue where you could give imprisoned children as wards  
- Fixed broken loc string in toast when a child learns a parent's language  
- Fixed incorrect localization scope in event tribal.1203  
- Landless rulers (Holy Orders, mainly) should now never be valid for forming hybrid cultures  
- Mozarabics are now considered part of the Western Christian block for the purposes of heresy generation  
- Recreated temporal Head of Faith titles will now correctly get the Temporal Theocratic title law set  
- Spouses of your children should no longer become wanderers  
- The AI will no longer go to war over personal artifact claims lower than Famed  
- The AI will no longer start sway schemes against characters that have 100 opinion of them  
- The Golden Horde, Chagatai, and Ilkhanate will now claim a more historical area when the Successor Khanates spawn  
- The potential friend and lover in fund_inspiration.7003 can no longer be the same person  
- Changed the name of the "is_diplomatically_available" trigger, which was... slightly misleading compared to its contents  
- Corrected typo in board game game concept loc  
- Fixed issue where you would receive war banners after creating a kingdom  
- Fixed positive outcome for Seduction failure in A Walk in Town event  
- Fixed possibility of character duplication in Out with the Old inspiration event  
- No longer possible to build Cities and Temples before they are invented by Petitioning your Liege  
- Properly display the liege title requirement for the "Consolidate the Canaries" decision  
- Properly apply the Priesthood Slaughtered modifiers on the different counties for the Toledan Nights event  
- The Petition event “Personal Matter” should no longer fire in a way that has you accusing yourself of infidelity  
- The Petition event “Sanctuary” now properly checks whether the deposed ally is suitable for it  
- The Court Event “Murder Holes and Priest Holes” is now more rare  
- The Court Event “Getting a Head” will no longer generate brilliant lunatics  
- The yearly event “Roughhousing” will no longer start the “Murders at Court” chain  
- Rectified the weight multipliers for the Petition event “A shadow in the Night”  
- The Petition event “A child of the Court” will no longer be able to pick your own child.

<!-- artifact:reactions:start -->
- 96 Like
- 71 Haha
- 22 Love
- 19 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [sidestep](https://forum.paradoxplaza.com/forum/members/sidestep.1286696/)**
Role: Blue Flame Provider
Badges: 44
Messages: 134
Reaction score: 826

*[Full game-badge icon list of 8 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
