---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1509587/"
forum_thread_id: 1509587
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 89
title: "CK3 Dev Diary #89: 1.5.0 \"Fleur-de-Lis\" Patch Notes"
dd_date: 2022-02-08
author_handle: rageair
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 12465
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1509587'
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
    location: raw_lines_116_to_118
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_960_to_964
    action: preserved_and_flagged
    counts:
      Like: 133
      Love: 60
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_1007_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #89: 1.5.0 "Fleur-de-Lis" Patch Notes

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Feb 8, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/)
- [2](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/page-3)
- …
  
  #### Go to page
  
  Go

- [12](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/page-12)
[Next](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/page-2)

1 of 12

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/page-12 "Last")

[![rageair](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/obsolete/s/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/rageair.375731/)

#### [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)

##### CK3 Game Director

**Paradox Staff**

**43 Badges**

Sep 10, 2011

1.826

11.829

- ![Cities in Motion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/cim_forum_icon.png "Cities in Motion")
- ![Europa Universalis IV: Pre-order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_special_forumicon.png "Europa Universalis IV: Pre-order")
- ![War of the Vikings](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/warofthevikings_forum_icon.png "War of the Vikings")
- ![Victoria 2: Heart of Darkness](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v2hod_icon.png "Victoria 2: Heart of Darkness")
- ![Victoria 2: A House Divided](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2AHD_forumicon.png "Victoria 2: A House Divided")
- ![Victoria 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2.png "Victoria 2")
- ![Semper Fi](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/sefi.png "Semper Fi")
- ![Victoria: Revolutions](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/victoriarevolutions.gif "Victoria: Revolutions")
- ![Europa Universalis IV: Res Publica](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/respublica_icon.png "Europa Universalis IV: Res Publica")
- ![Magicka](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/magickaIcon.png "Magicka")
- ![Heir to the Throne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/httt_forum_icon.png "Heir to the Throne")
- ![Hearts of Iron III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi3_forum_icon.gif "Hearts of Iron III")
- ![For the Motherland](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FTM1.png "For the Motherland")
- ![Europa Universalis IV: Call to arms event](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EU4_signupForumIcon_01.png "Europa Universalis IV: Call to arms event")
- ![Europa Universalis IV: Wealth of Nations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_won_forumicon.png "Europa Universalis IV: Wealth of Nations")
- ![Europa Universalis IV: Conquest of Paradise](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cop_forumicon.png "Europa Universalis IV: Conquest of Paradise")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![A Game of Dwarves](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/agodicon.png "A Game of Dwarves")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Europa Universalis IV: Art of War](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aow_forum_icon.png "Europa Universalis IV: Art of War")
- ![Crusader Kings II: Rajas of India](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_rajas_of_india_forumicon.png "Crusader Kings II: Rajas of India")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Crusader Kings II: Sunset Invasion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sunset_invasion_forumicon.png "Crusader Kings II: Sunset Invasion")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Europa Universalis III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3_medal_silver.gif "Europa Universalis III")
- ![Europa Universalis III: Chronicles](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3_chronicles.png "Europa Universalis III: Chronicles")
- ![Europa Universalis III Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3_complete.gif "Europa Universalis III Complete")
- ![Divine Wind](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3DW_forumicon.png "Divine Wind")
- ![Shadowrun Returns](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Returns.PNG "Shadowrun Returns")
- ![The Showdown Effect](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tse_forum.png "The Showdown Effect")
- ![Shadowrun: Dragonfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Dragonfall.png "Shadowrun: Dragonfall")
- ![Stellaris Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Stellaris_SignUp_icon.png "Stellaris Sign-up")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Shadowrun: Hong Kong](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hongkong.PNG "Shadowrun: Hong Kong")
- ![Europa Universalis IV: El Dorado](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_eldorado_forumicon.png "Europa Universalis IV: El Dorado")
- ![500k Club](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/500k_red.png "500k Club")
- ![War of the Roses](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/wotr_icon.png "War of the Roses")
- ![Europa Universalis III Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nap_icon.gif "Europa Universalis III Complete")
- ![Europa Universalis III Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/in_nomine_icon_forum.gif "Europa Universalis III Complete")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")

[](javascript:;)

- [Feb 8, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/post-28062561)


- [/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/post-28062561](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/post-28062561)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28062561/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-89-1-5-0-fleur-de-lis-patch-notes.1509587/post-28062561)

Greetings! Today is the big day, and soon you will be granted audience to the Royal Court and everything therein. And not only that - we have a quite sizeable patch that goes along with the expansion, which we have dubbed Fleur-de-Lis. Below you will find the full changelog, which can hopefully tide you all over until the release later today!  

Everyone here from the DevTeam is very excited about the release, and hope that you’ll enjoy what we’ve spent so much time making!  

Spoiler: 1.5.0 "Fleur-de-Lis" Patch Notes

###################  
# Expansion Features  
###################  


- Royal Court: Kings and Emperors now have access to the Royal Court, a fully realized 3D throne room that houses the ruler, their courtiers, family, and vassals. Presented in four distinct graphical styles, each with several variations, as well as variations based on Grandeur!
  * Grandeur: Increase the Grandeur of your court and reap large diplomatic benefits, unlock new Council Jobs, gain special Traits, and more - but make sure to manage your expectations! Compare yourself against other courts, and try to have the grandest court in the world.
  * Amenities: Spend gold on Amenities to increase your Grandeur, while at the same time unlocking effects and events for your court.
  * Court Types: Select a Court Type based on your Cultural Ethos and gain benefits scaled by Grandeur depending on which one you choose.
  * Court Language: Select which language should be spoken at your court. Either choose the language of a grander court, leeching off their Grandeur to your own, or propagate the language you like and reap the benefits of having others adopt it.
  * Hold Court: Invite your vassals and subjects to air their grievances in front of the throne. Increase your Grandeur and gain many different benefits as you arbitrate on various problems and challenges.
  * Court Artifacts: Collect glorious artifacts and decorate your throne room with them to increase your Grandeur and gain other benefits. Dynasty banner court artifacts will see their effects increase as the fame of your dynasty grows.
  * Court Events: Experience courtly life inside the throne room, with events featuring those closest to you.
- Inspirations: Fund great works of art, legendary smiths, and daring expeditions to gain artifacts; from masterwork swords and opulent crowns to the Ark of the Covenant.
- Petition Liege: Bring a specific issue directly to your liege and have them use their might to help you. Use your skills to sway the decision of an unwilling liege in your favor.
- Pay Homage: Bring gifts or promises of loyalty before your liege, increasing the bond between you - increasing both of your reputations. Just make sure not to make a fool of yourself!
- Form Hybrid Culture: Meld two cultures together, creating a new one with aspects of both. Pick-and-choose between pillars and traditions to create a culture that can thrive.
- Diverge Culture: Break away from your culture by diverging a new one; select a new ethos and change your traditions to suit the situation you’re in.
- Reform Culture: Change existing Traditions, Ethos, or Pillars over a long period of time.
- New Council Tasks:
  * Bestow Royal Favor (Chancellor): Increase the Prestige of both you and a select vassal, while significantly increasing their opinion of you.
  * Convince De Jure Territory (Steward): Convince other rulers to relinquish to you what is yours by De Jure right, or face diplomatic consequences.
  * Manage Royal Guards (Marshal): Increase the effectiveness of your knights, while reducing the success chance of any schemes targeting your person.
- New Dynasty Legacy, Customs: A legacy focusing on peaceful coexistence and the running of a prosperous multicultural realm
- New Portrait Assets: A selection of opulent headgear for Kings and Emperors, such as the Iron Crown of Lombardy, the Crown of Justinian, and the Sassanid Crown.

###################  
# Free Features  
###################  


- Court Positions: Hire on characters to serve in various roles in your court, giving them a salary in exchange for an effect. There are plenty of roles; from Seneschals to High Almoners, Bodyguards to Antiquarians. Look for skilled characters, as their Aptitude will determine how good they are at their job!
- Cultural Overhaul: The culture system has been completely reworked, cultures are now made up of several different components, making each and every one unique.
  * Acceptance: Cultures now have acceptance scores with all other cultures, determining how well they get along. The higher the acceptance, the lower the penalties, until they’re completely gone at 100% acceptance.
  * Ethos: The spirit of each culture lies in the ethos, which determines baseline cultural acceptance, and which Traditions are easier or harder to adopt.
  * Pillars: Heritage, Language, Aesthetics, Martial Tradition, and more. Pillars make up the foundation of a culture, and have a vast impact on its Acceptance towards other cultures.
  * Traditions: Traditions give each culture a unique flair, carrying modifiers, changes to rules, interactions, and much more. For each era a culture progresses through, more Traditions can be added.
  * As the Culture Head, add traditions to your culture over time.
- Personal Languages: Characters can now learn languages. Knowing a language cuts opinion penalties in half towards characters and counties speaking that language. A character can know a limited amount of languages.
  * Learn Language Scheme: A new scheme allows you to learn the language of another character. This scheme is improved through several Lifestyle perks and Dynasty Legacies.
- New Steward Council Task, Promote Cultural Acceptance: Increase the acceptance of a culture in your realm towards your own culture. This job is significantly more effective for Independent rulers.
- Artifacts/Inventory System: Characters can now carry Artifacts on their person. Equip a weapon, armor, regalia, headgear, and up to four trinkets.
  * Durability: Artifacts have durability, which decreases over time or when sieges/raids damage them. Pay gold to repair them, or reforge them into Court Artifacts if you own the Royal Court expansion.
  * Artifact Claims: Gain claims on artifacts carried by your predecessors, and go to war to reclaim lost heirlooms.
- Steal Artifact Scheme: A new scheme that allows you to retake lost artifacts, as long as you have a Claim on them.
- Challenge for Artifact Duel: Challenge those that hold artifacts that you claim, the winner takes it, the loser forfeits their claim.
- Commission Artifact: Pay gold to summon smiths and craftsmen to forge basic artifacts for your inventory.
- Coat of Arms Designer: Design your very own Coat of Arms and apply it to your House, Dynasty, or Title/s. Adjust existing designs, or create a CoA entirely from scratch. As with the Ruler Designer, CoA designs can also be copied to the clipboard and shared with others. You can also save the current CoA to disk as an image file, to show off to your friends.
- Added a new look for the Duel event window, where weapons will brandish their weapons against each other. If a character has an artifact, the look of their weapons will reflect that.
- Added a lot of new character animations
- You can now change the map color of titles you're allowed to rename
- You can now pick the map color of your new faith when you create a faith
- Added the Gardener Trait
- Added new Men at Arms - Monaspa, unlocked by the Caucasian wolves tradition (requires to be or descend from Georgian culture)
- Added new Men at Arms - Mulaththamun, unlocked by the tradition Desert Ribats for Berber heritage cultures
- Added new Men at Arms - Nile Archers, unlocked by the tradition Land of the bow, for East African heritage
- Added new Men at Arms - Garuda Warriors, unlocked by the Garuda Warriors tradition (Dravidian heritage)

###################  
# Game Balance  
###################  
- Added a Cultural Acceptance modifier to the Open Minded perk  
- Added an interaction that can be taken to claim one of your lieges higher-tier titles if you own 51% of its De Jure territory (unpressed claim)  
- Added three new Game Rules that control Hybrid & Divergent culture frequency and restrictions  
- Born in the Purple now gives a reduction to the Short Reign penalty but less prestige  
- Claimant Faction - Factions under Princely Elective care slightly less about cultural differences, as the empire is by nature multicultural  
- Claimant Faction - The AI is now less inclined to push the claims of Infirm claimants  
- Claimant Faction - The AI is now less likely to support a Claimant they hate just because they dislike their Liege  
- Claimant Faction - The AI now likes pushing the Claims of non-adults even less  
- Claimant Faction - The AI now looks at Cultural Acceptance instead of just preferring their own culture/heritage  
- Claimant Faction - The AI will now only prefer siding with an existing Claimant faction if the Claimant is of their faith/culture and they like them better than their current liege  
- Constantinople Holy Site gives Cultural Fascination instead of Direct Vassal Opinion  
- Culture Conversion is now much slower, though Hybrid Cultures can easily convert their parent cultures for a long while after forming  
- Executing random peasants no longer deduct 100 Piety, but the more reasonable 25 Piety  
- Fervor is now gained on a yearly basis rather than monthly  
- Fixed the Domestic Affairs maximum opinion being lower than it should if you had the Lifestyle or Dynasty perks unlocked  
- Insularism is no longer inherently polygamous. Instead, Irish, Welsh, and Gaelic support polygamy or concubinage as cultural traditions  
- Polygamy is now allowed for all Dharmic religions.  
- It's now somewhat stressful for certain characters to execute or torture their children  
- Made Counts more likely to convert to local culture if they're independent and do not have at least 50%+ acceptance with their capital culture  
- Made Spiritual Heads of Faith more likely to accept giving gold  
- Made the Mongols pay less for their Army Maintenance for a while after appearing  
- Made the Offer Vassalization interaction depend on Cultural Acceptance  
- Players will no longer be spammed with letter events when someone wants to invite their children to a playdate  
- Pushing the claim of a vassal of a vassal will no longer cause them to become your direct vassal unless they go up in tier  
- Rebalanced Dread from Executions, you should no longer get massive amounts of dread for executing random peasants  
- Relatives of landed characters give less Dread when executed  
- Slightly reduced the Dread gain for executing characters, unless you're executing an Emperor or your Head of Faith  
- Some Dynasty Legacies now give Grandeur bonuses  
- The Call Dynasty Member to War interaction no longer works on mercenaries and holy orders  
- The Illustrious, Exalted Among Men, and The Living Legend Prestige Levels are now harder to reach  
- The Offer Vassalization interaction now gain extra acceptance if you know the language of the target  
- The Open-Minded Perk no longer removes cultural opinion, but instead halves the penalty for already-known languages when using the Learn Language scheme  
- The opinion modifier the AI gets from pushing someone as a Claimant is now much higher  
- Torturing infidels as a zealous character is now relaxing  
- Tweaked Become the Greatest of Khans to be a bit harder to achieve, streamlined its rewards, and added a unique nickname for completing it  
- When the Papacy is dismantled, the Pope now loses all her cash  
- You can now grant land or vassals to your head of faith if they're independent  
- You will no longer get Dread for executing prisoners that have spent so much time in your prison that everyone's probably forgotten them by now  
- "Organize levies" is renamed "Organize armies" and now includes a bonus on army maintenance. The base value has been lowered from 5 to 1 for both effects.  
- "Train commanders" now increases knight effectiveness and Men-at-Arms damage and toughness overtime (from 0 to the martial skill of the Marshal, at a rate of 1% per month). Moreover, odds for positive outcome has been increased, now being equal to 50% of the Martial skill instead of 33%.  
- AI Byzantine emperors will no longer instantly take the Reclaim Constantinople decision if it would cause a vassalized player to game over  
- Characters with the Forgiving trait no longer gain stress when a rival, or a character they dislike, dies.  
- Form the Archduchy of Austria decision now requires you not be related to the emperor or hold the HRE, have a strong hook on the emperor, have at least High Crown Authority, and your culture must have reached the High Middle Ages era  
- Realms with no land nor sea connection now have penalties for accepting offers of vassalization  
- The Convert to Local Culture decision is now more expensive, but discounted based on how similar you are to the culture you want to adopt  
- Tweaked elective modifiers to make characters more likely to vote for themselves  
- Unite the Spanish Thrones decision now requires High Crown Authority  
- Halved prestige gain from Romance schemes, as they were the only way to gain the largest standard prestige chunk of 1500 in the title, and made it harder for tribals to romance non-tribals  
- Costs to hire guests has been tweaked. There is now a default cost of 20 gold, Commander traits adds 15 gold each and skill points above 12 adds 5 gold.  
- lowered the impact of the realm stability game rule  
- only increased the base cost of recruiting guests for Clans and Feudal governments.  
- prestige and piety gains from battle against peasants has been divided by 4  
- the "Saga set in Stone" achievement now also counts normal Religious Rune stone  
- It no longer costs piety to revoke leases of Holy Orders of other faiths  
- Updated how Conversion Cost and Penalty bonuses are applied, they now are successive percentage instead of additive percentage  

###################  
# AI  
###################  
- Added logic for transferring siege weapons from a subunit to the main subunit  
- Added small bonus to current location when selecting a target province to avoid units switching places  
- All vassals are now able to declare war no matter how deep down in the vassal tree they are  
- Allowed the AI to assign the Spouse to a specific domain when their skill is strong enough, and even more if the Ruler is unskilled them self  
- Allowed the AI to assign their Spymaster to support their scheme if there are ongoing murder or abduct attempt, and if the Spymaster is skilled enough  
- Certain AI's will now try to murder infertile spouses if they have no heirs  
- CB:s can now have a scripted score that is added to the hard-coded one  
- Changed CB base score to be title's Tier^3 instead of Tier^2  
- Fixed a case where the AI would get stuck in a loop trying to siege  
- Fixed opinion of self overtaking the base score of many CB:s  
- Fixed the AI being unable to upgrade special buildings and duchy capital buildings  
- Moved CB score multipliers to defines  
- Organize army is used by default and receive a small boost if at war or negative income (+10) AND is forced to try to get out of debt  
- Subunit stacks will be more hesitant to split off siege weapons  
- The AI will now switch away from titular titles as its primary if it has a non-titular title of the same tier. It will also prefer its primary be a head of faith title if possible  
- The AI will now try to prioritize swaying characters in a faction targeting them. They will continue swaying them until they leave the faction.  
- The main subunit stack will never split off its best siege weapons  
- The score of potential CB:s are no longer scaled with the strength of the target  
- Told the AI that even if it can't get to the war goal due to attrition, sieging something near it to open a path is a pretty good idea  
- Told the AI that when selecting a new siege target, it shouldn't pretend that any siege target more than a brisk walk away is a bad choice because it is further away than its current target: the province it just finished sieging. All else being equal the AI will still prefer to siege things closer to its army, but that's no longer further intensified when the AI is picking a new siege target after finishing its current one "  
- Train commanders is used when the AI saved enough money, and the motivation depends on the Marshal's skill  
- Tweaked down de jure multipliers for scoring titles when evaluating CB:s  
- Units should ignore strait penalties and hostile attrition if helping another unit  
- Units should ignore strait penalties if going into an ongoing combat  
- Units with siege weapons will now try to relieve or help sieging units without siege weapons  
- When declaring wars, only count an ally's strength if the ally is at peace  
- Will be more hesitant pushing a claimant's CB over its own  
- Will focus more on CB:s that target a title of a higher tier than its current primary title  
- Will no longer push a claimant's CB if it targets a title the AI has a claim on  
- Will now hunt nearby enemy units even in hostile attrition territory if it deems it worthy  
- Willingness to attack a stronger target now scale the more wars the target is in  
- Willingness to attack a stronger target now scale with attacker's boldness  
- The AI will no longer send poems to the player as often  
- The AI will now convert provinces more logically, considering things such as Jizya tax, and hostility level of the target faith  
- The AI will now sometimes try to murder faction claimants, this is more likely for rational AI's, especially if they focus on Skulduggery  
- The AI is now heavily inclined to convert to a local culture if it's a hybrid culture of their culture  
- The AI is now less adamant about always asking faith conversion of righteous and astray vassals  
- Paranoid AI's will now sometimes try to murder claimants to their titles  
- Fixed combat evaluation incorrectly used on sea zones, leading to many naval invasions being impossible.  

###################  
# Interface  
###################  
- Add checkbox for hiding the hair and beard from the portrait in the Ruler Designer, if hidden they will still be applied when finalizing but this allows hiding them to edit the facial structure more easily.  
- Add setting to enable/disable automatic camera rotation back to neutral after rotating it with the right mouse button.  
- Added a way to filter direct vassals in the search results  
- Added a way to filter search results based on a character's sexuality  
- Added missing breakdown entry in loot tooltip. Breakdown now matches end value  
- Added should_create_alert for holding Grand Blot so if the decision is tracked, an alert isn't made unless the player has the minimum amount of money for the cheapest blot option  
- Added some missing tooltip links in The Grand Festival event  
- All former spouses are now shown in the character window, not just those that are former due to death  
- Clicking on a dynasty CoA now opens the house+dynasty view rather than the dynasty legacies view  
- Corrected the description of Forder claiming it affects the disembark penalty  
- Decisions now support a two page setup  
- Disabling assign button in character list when changing councilor, if current councilor cannot be fired  
- Ensured that after a combat ends, the army always gets reselected. If the end of combat starts a siege, the siege gets selected  
- Ensured that winning a siege always sends you a notification  
- Event timeouts in MP with no effect now clearly say "No effects" instead of the notification being empty  
- Fixed a localization string to make sure the tooltip for the kill list also shows up in German  
- Fixed all combat prediction dates being off by 1 day  
- Fixed building costs sometimes lacking a breakdown tooltip despite being modified  
- Fixed buildings disabled by the domain limit grace period claiming they'll be re-enabled next month rather than telling you the real reason they're disabled  
- Fixed flavor names like "Pope" sometimes not ending up used, showing things like "King-Bishop" instead  
- Fixed having ironman saves in some cases messing up hosting MP from save  
- Fixed holding Switzerland causing every single one of your titles to be referred to as Confederation  
- Fixed imprisonment reasons not being shown to you when your liege attempts to imprison you  
- Fixed incorrect grammar in known criminal tooltips  
- Fixed liege wars always showing the CoA of the war attacker, even if your liege is on the attacking side. Now shows the war leader of the side opposed to your liege  
- Fixed on-map siege units disappearing if you zoom all the way out then all the way back in. Also fixed them sometimes being abnormally large or small  
- Fixed repeated notifications about event timeouts in multiplayer  
- Fixed saving search filters that include a name search not working  
- Fixed skill/trait items on event options sometimes being wrong if more than one skill/trait can trigger the option  
- Fixed sliders in the Ruler Designer being partially offscreen in Russian  
- Fixed some tooltips that have text in the upper-right corner being rather cramped  
- Fixed some unnecessary indentation in some modifier breakdowns  
- Fixed text in certain tooltips and similar being selectable for no apparent reason  
- Fixed that there in the Hooks and Secrets list for the hook counts there's a small gap between the number and icon where there's no tooltip, and the number and icon have differently oriented tooltips  
- Fixed that tyranny decay in the interface didn't account for modifiers to Tyranny Loss. The decay rate was properly affected, but this wasn't accounted for in the UI  
- Fixed the Invite button in schemes thinking you're able to give gifts and use hooks on *everyone*, and thus being at times wildly optimistic about how many people you can get to join your scheme  
- Fixed the character tooltip in the character window being offset so far to the right that it is very difficult to move into  
- Fixed the checkbox for "Only X Faiths" in the Other Faiths list being inverted  
- Fixed the council task tooltip for the currently assigned task not saying your councillor is assigned to that task  
- Fixed the game in some cases failing to count raised troops as part of your overall army size  
- Fixed the opinion breakdowns in Liege's Council showing the breakdown of their opinion of you, rather than your liege  
- Fixed the title name of dead people being centered rather than left-aligned  
- Gave the scheme predicted time to completion widget in the intrigue window a decent tooltip. Improved a bit on the one in Start Scheme to match  
- Hovering over any holding in a county will now highlight the county in Domain Holdings in the outliner  
- If you have no saved character search filters, the dropdown now tells you as much rather than giving you no list at all  
- Letter events that time out in multiplayer now say who they were from in the notification instead of just having a blank event name  
- Loading a save will now set the game speed to the speed you had when you made that save. So if you save at speed 4, you'll load at speed 4 rather than the default speed of 3  
- Pushing the claim of a vassal of a vassal that will go independent no longer claims they'll also become your vassal  
- Removed the Hook option from Educate Child if you are the one both requesting and accepting the Interaction  
- Reorganized the Option in the Vassalization Interaction so that the Current Situation item shows up when it should  
- Rulers now only use the title of their spouse for naming if they're vassals (or below) of their spouse, rather than if they're lower tier  
- Schemes segmented progress bar now matches the progress value  
- Send a feed message when an event times out containing the effects of the picked options.  
- Show List with displayable artifact for selected slot  
- Small static portraits in places like the character finder now refresh on a yearly basis so that they don't get horrifically out of date, like showing a toddler in place of a 25 year old  
- The "base" # of days in the building construction time tooltip now says "x days" rather than just "x"  
- The Promote Culture task map mode no longer does unnecessary striping of the culture colors with your own culture's color  
- The age tooltip for dead people now also shows their date of birth, not just their date of death  
- The character tooltip for people you're not the liege of now shows their council and court positions  
- The event timeout notification in multiplayer now no longer leaves out some of the effects of the event (those that happen before you even select an option)  
- The faith creation window now shows what's blocking you from making the faith a bit more clearly  
- The intensity of the cursor highlight on the map can now be set by the user  
- The menu to show additional map modes in the lobby no longer disappears when you try to hover over it  
- The relation string now shows "commander" if relevant: "Your Marshal, Vassal, and Commander"  
- The spinning icon in the top-left of loading screens now actually spins  
- The war tooltip in the character window now only shows at most 6 people on each side of the war, with the overflow listed as "x more allies", to avoid the tooltip becoming ludicrously large in Great Holy Wars and similar  
- Updated artifact tooltip depending on artifact status, Storage, Displayed, Displayed in selected slot  
- When creating a faith, the "Theocracy" section on the right now only shows up if you actually change your Clerical Tradition  
- When there's no Current Situation items, it now says "none available"  
- Your choice of icon in the Create Faith window will no longer get reset if you close and reopen the window  
- Zoom to slot  
- fixed faith tooltip flavor description formatting.  
- selection army commander window now should open faster for large realms  
- Fixed mismatches between construction cost breakdowns and actual cost  
- Fixed the game rules window's "reset to defaults" button being visible when the rules are not possible to change  
- Made culture head a bit more predictable. Now if all else is equal (# of culture counties, tier) the player will be preferred as culture head. When no player is involved, the current head will be preferred. This should ensure that the culture head does not arbitrarily change  
- The draggabble part of the scrollbar is now sized based on the length of the list  
- When creating a new faith, it now gets a color similar to your old faith, rather than a completely random one  
- Using the revoke title interaction when a subject only has one title now automatically selects the title if it can be revoked.  
- the Character Finder no longer resets the sort option upon changing the filters and reopening the window.  
- When your liege wins/loses a war, the toast now displays both characters  
- Added letter event informing the (now former) holder when Constantinople is taken from them by the Reclaim Constantinople decision  
- The game will now list the reason for all recent increases or decreases to Fervor in the Fervor tooltip.  
- The Court Physician has been removed from “Your Court” view and can now be found within the “Court Positions” view.  
- Scheme Types now have Cooltips.  
- Fix to close button disappearing behind statue in War Overview  
- Prison bars made smaller to fit tighter around character in War overview  
- Fix to House tab being anchored in the center of the window instead of top causing problems when playing on some resolutions  
- Fixes to Grant Titles, County and Ruler Designer where texts in Russian was pushing UI elements out of bounds  
- Fix to Other Faiths window having content being out of bounds when playing in Russian, Spanish and French  
- Fix to former spouse text overlapping Coat of Arms icon in Character View  
- Fix to buttons being pushed out of the Military window when playing as a Tribal Ruler.  
- Fix to long Primary Titles pushing UI elements out of bounds  
- Fix to Sins and Virtues Trait icons in tooltips being out of bounds in Faith View  
- Fix to wrong camera being used when there is multiple characters in an event  

###################  
# Art  
###################  
- Removed some invisible lakes in Scandinavia and Tibet  
- Fixed several unit locators where fighting units would end up inside mountains  
- Improved the Marshal’s animation  
- Fixed two impassable terrain provinces (in Anatolia and Tibet) having the same ID.  
- Solved numerous clipping issues for characters between clothes, headgear and hairstyles  
- Minor texture improvements to certain clothes, headgears and hairstyles  
- Small adjustments of a few gene attributes  
- Added AO textures for reducing the AO effect on character faces, to remove unnatural dark shadows around eyes and mouth  
- Adjusted the look of the Asian ethnicity  
- Minor tweaks to other ethnicities  
- Added body shapes which will give subtle variation of proportions between shoulders, waist, hips, arms and legs for characters  
- Reduced an issue which made eyelashes look really bright in some lighting situations  
- Fixed a number of issues with the “Customize Appearance” sliders in the Ruler Designer  
- Fixed an issue which gave partly clothed or undressed characters very skinny limbs  
- Adjusted Camera positions for the character view window, which should give more consistency in showing the correct relative height of characters  
- Fixed many issues of clipping caused by various animations when combined with clothes, body deformations etc.  
- Changed the marshal animation to hold the sword properly by the hilt and not by the blade  
- Fixed incorrect scale and animation placement of a few weapons  
- Fixed some strange deformations on the female undergarment  
- Adjusted skirts for a lot of clothes to work better with sitting animations  
- Fixed an issue of incorrect animation of the area around the right eye on many characters  
- Character portraits now have FXAA applied when any anti-aliasing is enabled in settings  

###################  
# Localization  
###################  
- Added tooltips for Artifact Claims, Personal Artifact Claims, and House Artifact Claims  
- Corrected a usage of 'marriage' to 'union' in an infidelity event where it could refer to either a spouse or a concubine.  
- Fixed Reclaimed Britannia modifier percentage in Russian  
- Fixed a pronoun disagreement (my & your) in the post-battle prisoner of war notifications  
- Fixed broken place-name in Grand Blot decision event  
- Fixed scope issue in temple building tooltip  
- Fixed type on Holy War conversion suggestion  
- Made sure that all custom loc entries have written loc keys  
- Made the current construction text in the realm overview more concise  
- Updated Commit Suicide Decision descriptive text to better reflect why the decision is available  
- Updated Invite to court acceptance tooltip to always use second person  
- Updated the bastard secret text to include the bastard  
- Updated title in event to name dynasty child to reflect twins  
- Witch event option tooltip is now clear on what poor soul you're trying to convert to the dark side  
- You will no longer call your grandson your grandmother when you bury him  
- Your friend will no longer confuse their other, better, friend for their rival  
- capitalized title articles and changed title effect text to avoid title redundancies  
- changed Assyrian culture to be named Syriac, to be more neutral and slightly more historically appropriate (if a bit drier)  
- Fixed some typos in witch events  
- Fixed typo in the English in hunting ground building  

###################  
# Game Content  
###################  
- Added a random childhood event where a ward can pick up their guardian's language  
- Added an event for Meet Peers decision about language  
- Added an event for children to learn the language of their parent through observation.  
- Added event option to pick your court position champion in a trial by combat  
- Added events to rename East and West Francia to Germany and France, respectively, should they pass from the hands of the Karling dynasty.  
- Added functionality to pre-defined culture splits (such as the Norse to Swedish/Norse/Danish one) so they more closely mirror dynamic divergent and hybrid cultures  
- Changed the Outremer name list  
- Favored Electors are now dynamically selected once the HRE is reformed  
- Hunt activity can now generate artifacts for characters with a royal court  
- Marriage acceptance letter will now be more flavorful  
- Converted Northern Lords content to be tied to a set of new Norse Cultural Traditions  
- The option to grow an orchid during a seduce event is now also available to those with the gardener trait  
- Trials-by-Combat are now tied to a cultural tradition rather than hardscripted to certain cultures  
- Added decision to form the Kingdom of Bene Israel  
- A number of older events have been updated to make use of new features such as court positions and artifacts.  

###################  
# User Modding  
###################  
- "titles" in flavorization for titles now means it'll only apply to those titles, rather than being applied if the holder has at least one of those titles  
- Add CloseGameView data function so mods can close specific in-game views.  
- Add GetScriptValueBreakdown which returns a value breakdown for use in the UI to breakdown the desc entries of a named script value.  
- Add GetTraitFromGroup and GetTraitGroupLevel data functions on Character.  
- Add GetTraitGroup( 'tag' ) and Trait.GetGroup data functions to get trait groups.  
- Add HasTrait and HasTraitFromGroup data functions to Character.  
- Add culture object saving ability to try_create_important_action.  
- Add days_since_joined_court trigger.  
- Add event chain progress custom UI, allows displaying how far through an event chain one is.  
- Add set_destroy_on_gain_same_tier. Uses for marking a title to be deleted when character gains or create a new title with the same tier  
- Add support for custom loading of scripted widgets from mods via the gui/scripted_widgets folder where pairs of folder path and widget names will cause widgets to be created in gameplay.  
- Add the scripted_animation database, it handles collections of triggered and scripted animations for use within event portraits.  
- Add the combat_phase_events database, it handles running effects during the main phase of combat on the commander and knights in a performant manner. As such the on_commander_combat_pulse and on_knight_combat_pulse have been removed due to their performance issues.  
- Add the common/coat_of_arms/dynamic_defintions which replaces the event system for overwriting coat of arms based on different triggers for custom displays based on faith or culture. Increases performance by a lot.  
- Add the is_decision_on_cooldown trigger.  
- Added "play_sound_effect" effect to play sound effects  
- Added MaA base type modifiers for maintenance and recruitment cost  
- Added a map mode that shows visual geographical area for debugging purposes  
- Added add_same_sex_spouse history effect  
- Added alternative strings faith localization, useful for non-English translations  
- Added character modifier men_at_arms_recruitment_cost  
- Added character modifier no_disembark_penalty  
- Added console command "bypass_requirements" (alias "bypass") that lets you do decisions, interactions, schemes, laws, and title creation despite the requirements not being met  
- Added console command "instasiege"  
- Added console command "save_every" and startup parameter "-save_every=x". These will make a save every x years, and ensure they do not get overwritten by normal autosaves  
- Added console command AI.try_send_decision  
- Added console command AI.try_send_interaction  
- Added console command Ironman.ToggleIgnore. When ignored, saves will act as if they're not ironman, including that when you hit save it'll result in a non-ironman save. This can be toggled during gameplay  
- Added console command ToggleShowAllKillers  
- Added console command alias "trait" to add traits  
- Added console command complete_schemes, guaranteed_scheme_success/failure, and guaranteed_scheme_secrecy_success/failure. The success/secrecy ones only affect the player  
- Added console command instaraid  
- Added console command set_date  
- Added console command show_regions_in_tooltip  
- Added console command toggle_keys_on_map  
- Added console commands "yesmen_instant" (AKA "ymi") and "instant_responses". The yesmen button in the console can now be right-clicked to run "yesmen_instant"  
- Added console-command show_region  
- Added data function "HasParameterByKey" to the "Faith" type  
- Added data functions GetTraitsWithFlag and GetTraitsWithoutFlag  
- Added data system function GetMaA  
- Added data system/loc command [Faith.CustomLoc( 'key' )]. Works as .Custom does for things like Character. The different name is due to Custom already being in use for faith-specific localization  
- Added debug interactions Take Domain and Take Realm  
- Added define MINIMUM_DYNASTY_NAMES so that you can have errors generated if cultures exist with too few dynasty names  
- Added effect clear_claimant for wars  
- Added effect deactivate_holy_site  
- Added effect remove_dynasty_perk  
- Added effect remove_innovation = innovation_key  
- Added effect run_interaction  
- Added effect set_army_location  
- Added effects clear_traits and copy_traits  
- Added effects learn_language, unlearn_language, learn_language_of_culture, and unlearn_language_of_culture  
- Added effects set_age and change_age  
- Added effect remove_building  
- Added extremely basic profiling for CBs. ai_cbs.csv will tell you how much time the AI spent on each CB. It does not have any categorization  
- Added field 'minimum_cost' for decisions. Works exactly like 'cost' with one exception: it won't actually get applied. Useful for when you have the player choose between different options after taking the decision, and only charging the cost at that point  
- Added link last_played_character  
- Added links calc_culture_dominant_faith and calc_culture_dominant_religion  
- Added list builder *_culture_county to get to all counties of a specific culture  
- Added list builder played_character  
- Added list builder x_culture_global  
- Added list builders opposite_sex_spouse_candidate and same_sex_spouse_candidate  
- Added modifier coastal_advantage  
- Added modifier prowess_no_portrait so that you can add prowess to someone without making them visibly more muscular  
- Added on actions yearly_culture_pulse and three_yearly_culture_pulse  
- Added on-action on_building_completed  
- Added support for era-specific MaA bonuses via the "era_bonus" parameter in MaA types  
- Added terrain based construction cost modifiers  
- Added terrain based development modifiers for characters, so a trait or what have you can make someone get better development growth in specific terrains  
- Added terrain modifiers for supply_limit, supply_limit_mult, tax_mult, and levy_size  
- Added the following console command aliases: faith, renown, add_renown, legacies, dynasty_perks, give_all_legacies, perks, culture, faith, usurp, diplomacy, martial, stewardship, intrigue, learning, prowess  
- Added title data function GetDefinitiveName; will insert a "the" at the start if the title isn't already of a definitive form  
- Added trigger <lifestyle>_unlockable_perks  
- Added trigger can_fire_position for council tasks  
- Added trigger culture_overlaps_geographical_region  
- Added trigger has_innovation_flag  
- Added trigger has_prisoners  
- Added trigger knows_language  
- Added trigger num_of_known_languages  
- Added trigger perks_in_<lifestyle>, to query how many perks exist in a given lifestyle (rather than how many a specific character has)  
- Added triggers total_army_siege_value, damage, toughness, pursuit, and screen  
- CBs now support the "icon" parameter to have them use a different icon key  
- Character interactions now support the "icon" parameter to have them use a different icon key  
- Characters and counties can now have region-specific modifiers for development growth  
- Characters no longer have to be rulers to be invited to an activity  
- Characters no longer have to be rulers to spawn an activity; any alive character can now own activities  
- CloseGameView global data function added.  
- Concubines and Consorts are now both referred to as Concubines to make same-sex concubinage work better  
- Council tasks now have a monthly_on_action field. This is a more performant way to have them trigger on-actions once a month  
- Custom loc keys can now have variants. These simply use the logic of a parent custom loc key, and add a suffix to the resulting localization key  
- Custom loc will now log an error if a loc key is missing. log_loc_errors = no can be used on individual bits of custom loc to suppress this  
- Eliminated a bunch of culture parameters that had no effect, E.G., "tribal_name" or "dukes_called_kings"  
- Eliminated some unused hardcoded modifiers  
- Eliminated title_to_title_neighboring_barony and title_to_title_neighboring_and_across_water_barony, but made the other variants significantly faster by optimizing based on only counties and above being allowed  
- Ensured an error gets logged when trying to add a scripted relation that already exists  
- Ensured that activities are removed from dead people within a day. This causes on_invalidate to run  
- Ensured that on_game_start events actually happen on game start rather than the next day  
- Events can now take a "cooldown" field to make event cooldowns simpler to script. The debug functionality that shows the event trigger fulfillment in the event window will completely ignore the cooldown  
- Fixed <holding_type>_holding_build_piety_cost and prestige cost not working for building a new holding  
- Fixed a number of console commands not working in observe mode (even when observing a character), such as "gold"  
- Fixed potential load order issues with number_maa_of_base_type and number_maa_soldiers_of_base_type  
- Fixed the "name" field in character creation templates doing nothing; it'd only work to use it in the create_character effect itself  
- Fixed the save_on and save_every console commands not working in observe mode  
- Fixed using "current_date" and other date triggers in weird ways causing overflow. Now gives the # of days since year 0  
- Geographical regions are now a proper database in map_data/geographical_regions. This means you can split it across multiple files, and means we can more easily add more region-based functionality  
- GetDynastyByID global data function added.  
- GetDynastyHouseById global data function added.  
- GetFaithByKey global data function added.  
- GetImprisonmentReasons, GetBanishReasons, etc. now take a character parameter as context, rather than basing itself on the player's character  
- GetReligionByKey global data function added.  
- GetScriptedCharacterByHistoryID global data function added.  
- GetTitleByKey global data function added.  
- GetTraitsWithFlag global data function added.  
- GetTraitsWithoutFlag global data function added.  
- GetScheme('scheme_type') global data function added.  
- Having an interaction with send_options_exclusive and an option with can_be_changed now logs an error, since there's no sensible way for this to work for mutually exclusive options  
- Hid dynasty and inherited trait info for same-sex marriage. Done in GUI script, so can be modded  
- In debug mode there's now a button in the event window to reload it; this will cause all the text to be regenerated, the background reselected, etc.  
- In debug mode there's now a button in the event window to run Localization.ToggleSkipDataSystemInLocOutput and reload the window. There's also a button for copying the event text  
- In debug mode, the event window now displays a widget showing if the trigger is fulfilled or not. Hovering over it will give you a trigger breakdown  
- MaA now have a can_recruit trigger. They will be available if the trigger is met, or if unlocked by innovation. You can't both unlock by innovation *and* have a trigger. Removed unlocking by dynasty legacy since you can now do that by trigger  
- Make on_title_destroyed run when a title is destroyed for any reason.  
- Make shortcuts moddable  
- OpenGameViewData global data function added.  
- OpenGameViewglobal data function added.  
- Rally points are now consistently called that everywhere in code and script, rather than occasionally being called "banners"  
- Remove the on_weight_changed on action, weight modifiers are now known to code and applied directly based on the new OBESE_WEIGHT_VALUE and MALNOURISHED_WEIGHT_VALUE defines. Usage of the change_current_weight effect will now correctly update and apply the modifiers automatically as well now. Increases yearly tick performance by removing weight calculation overhead.  
- Rewrote the "complex blocker trigger should have custom localization" warning to be easier to understand  
- Same-sex marriage is now supported; gender-based restrictions are now entirely handled in script  
- A title/titles history can be verified for gaps using the verify_title_history and verify_title_history_all console commands  
- Schemes now support custom icons, using the standard "icon" syntax. Note that the icons for the scheme interactions are still handled separately  
- Setting a trait group on a trait, but no level, will no longer crash the game on startup; it'll now just log an error  
- Significantly improved upon the event_log.txt file. Now written as a spreadsheet itself to event_log.csv, and it now includes the # of times each event has been checked, and the # of times each option has gotten picked. It'll also automatically write on shutdown if enabled  
- Skill/trait items are now generated on every event display rather than the first one. That means if you make use of trigger_if or similar, you can ensure only the relevant one actually shows up  
- The "take title" debug interactions now let you pick what title to take  
- The AI is now able to use interactions with mutually exclusive options when none of the options show, just like the player. No mutually exclusive options showing up no longer executes the effects as if the first option was selected (all the send option scopes return false now, instead of the first being true)  
- The AI profiling now also profiles AI decisions, putting those in ai_interactions.csv  
- The custom_tooltip trigger now localizes properly. The custom_tooltip effect now allows other effects to be inside it (and thus hidden). Both now allow you to override the subject  
- The game will now log an error on startup when a modifier is used in a place where it won't work. E.G., using "diplomacy = 2" in a county modifier  
- The game will now log on startup if there's any event themes or background referenced that do not actually exist  
- The object explorer now includes activities, schemes, wars, stories, factions, and council tasks  
- The object explorer now includes global variables  
- The random effect now gives an actually useful error message when you forget the 'chance' field  
- The set_sexuality console command now has tab-completion for its parameter  
- The trigger number_of_election_votes now uses "target" rather than "title" for consistency  
- The triggers join_faction_chance and title_join_faction_chance now use "target" rather than "faction" for consistency  
- The various allowed_for triggers for CBs no longer provide the defender. This allows for some significant optimizations. Use allowed_against if you need the defender  
- Title keys for the title and its dejure lieges are now shown in the province tooltip, title tooltip, and realm tooltip in debug mode  
- We now log errors if there's any province that can have a holding that isn't in a visual geographical area  
- You can now put "ai = no" on CBs to make the AI ignore them  
- consume_imprisonment_reasons and similar will now error if the target is dead  
- custom_description will now log an error on startup if the referenced effect/trigger loc doesn't actually exist  
- debug_log_scopes = yes now also logs temporary scopes  
- mercenary_count_mult no longer needs to be an integer number. We now calculate the total # of companies (rounded) then distribute them between the sizes available (smaller preferred if equal distribution is impossible), rather than requiring the same # of companies at each size. So a culture getting (1, 1, 1) companies will with a +50% modifier get (2, 2, 1) companies  
- modifiers.log (generated by the console-command script_docs) now tells you what objects every single modifier can be used for. E.G, "character", or "character, province, and county"  
- open_interaction_window can now take a target_title field so as to pre-fill the target title. Note that this does not validate the title at all; if it isn't selectable it'll just not be selected  
- player_heir_position now uses "value" instead of "position" to reduce code duplication  
- send_interface_message now also supports temporary scopes in its descriptions  
- set_title_name, set_title_prefix, set_house_name, and set_dynasty name now all log an error if their loc key does not exist  
- spawn_army will now only spawn levies if scripted to do so  
- independent_primary_defender_advantage_add. Gives advantage in combat when the commander is the primary defender in the war.  
- same_heritage_county_advantage_add. Gives advantage in combat when the commander has the same cultural heritage as the province of the battle.  
- Added support for “unique” and “pick” within random_list. This allows for the list to pick multiple options X times, and can force them to be unique. “Pick” defaults to 1 and “unique” defaults to false.  
- Added support for non-uniform bone scaling  


###################  
# Databases  
###################  
- Added Gond culture to the game, it exists in central/eastern India.  
- Added new coat of arms for the following dynasties: Rashtrakuta, Paramara, Pallava, Talakad Ganga, Goa Kadamba, Ratta, Kakatiya, Pala, and Candras  
- Updated history for both start dates in India, adding more properly playable vassal rulers as well as their spouses  
- Updated dynasty trees for a number of Indian dynasties  
- Added the Carantanian culture  
- Added strait between Kutch and Satyapura  
- Fixed wrong family for some Tsongkhapa Bodpas, and made it a house of the Pugyel dynasty  
- Gave the Duchy of Ghur to the Ghurid dynasty in 867 and 1066  
- Improved historical setup of the HRE  
- Improved setup of the county of Grisons  
- Krajna is now Pomeranian rather than Polish  
- Landed Suleyman Seljuk in Samosata  
- Odo is now correctly Count of Bayeux in 1066, rather than Robert de Conteville  
- Ramnulf II is now correctly Count of Poitou in 867, rather than Bernard II of Barcelona  
- Renamed Taghlib dynasty to Tawfid, to avoid overlap with Banu Taghlib  
- Renamed anachronistic Petropavolsk to Kyzylzhar  
- Simeon of Bulgaria now is quick rather than lisping  
- Some holdings in central/eastern India are now tribal.  
- Split Twelver Shiite Caliphs out of Shia Caliphate history and into their own Imamist title  
- The County of Zollern is now held by Friedrich I of the Hohenzollern dynasty in 1066.  
- Tweaked starting setup of some dynasties to reflect their relation to other pre-existing dynasties (as cadet branches)  
- Updated some dynasties to use the new Gond culture  
- Yapaniya Jainism now has the vows of poverty tenet  
- Yapaniya Jainism now no longer has the Natural Primitivism tenet, their monks will however still be naked  
- Increased Germanization of Austria in 1066  
- A number of baronies have been moved to different counties in India. Some counties and baronies have also been renamed to better fit the historical period the game is set in.  
- Norway's de jure capital will no longer jump around to match its historic de facto capital, preferring Nidaros throughout instead  
- Capital of Idrisids in 867 is now Fes instead of Marrakesh  
- Grand Clan empire tier name and Padishah empress title for Muslim Indians changed to Empire and Shahbanu respectively  
- Qarmatians are now Monogomous and have Equal Gender (actual gender roles were more complex, but Equal is a suitable abstraction)  
- Removed duplicate trigger within Headgear  

###################  
# Bugfixes  
###################  
- Significantly improved Multiplayer stability  
- Added a setting for users with slower internet speeds to throttle savegame transfer speeds (improves multiplayer stability)  
- Improve startup load times across the board by heavily threading database loading, reducing allocations, and reducing lock contention  
- Remove redundant file IO operations to improve loading times  
- Rework script variable storage to improve daily tick performance and lower cache misses  
- Added clarity tooltips on what will happen to duchy titles after Duchy Conquest wars  
- Added notification when a Spiritual Head of Faith titles can be created  
- All CBs now cause conquered land to lose control, rather than only some  
- Capturing a revolting vassal will no longer remove them from the faction (and war) "  
- Characters now don armor to fight duels - unless they are both tribal - and remove their billowing cloaks  
- Claim Liege Title interaction from notification now properly opens on an available title  
- Clan Invasion will no longer take all kingdom titles from the defender if the attacker and defender are kings  
- Counties in Populist factions must now always have the same faith as the faction  
- De Jure Duchy casus belli prestige costs will now only count titles held by the enemy  
- Ensured destroying a regiment always destroys associated raised armies  
- Ensured that electors that are powerful vassals of someone other than the title holder don't get extra voting power  
- Fixed "Allow Marriage" not always taking effect  
- Fixed A Dangerous Business achievement unlocking within Europe  
- Fixed Bhakti gods changing after creating a new Hindu faith  
- Fixed Create Title notification affordability checks  
- Fixed Cultural Barony names only showing after a Holding is built  
- Fixed Demand Conversion interaction bypassing the Negotiate Release conversion option by disabling it for characters you have imprisoned  
- Fixed Establish Bactrian Supremacy being unavailable for clan governments  
- Fixed Guardians sometimes being impossible to replace, even with a hook  
- Fixed Halq event at the end of a Hajj not firing as often as it should  
- Fixed Khitan not sharing color scheme of other Mongolic cultures  
- Fixed North Sea Empire decision resulting in a Danish inspired flag when formed by the holder of the Daneland  
- Fixed Seduce schemes against close family critically failing despite having the Graceful Recovery perk or Unrestricted Marriage doctrine  
- Fixed Sobiesalv typo of Sobieslav Slavic name  
- Fixed a bug in which the real father of a bastard child resulted in a localization error  
- Fixed a case where a new head of faith could end up Feudal  
- Fixed a rare crash that could happen when hovering over a Current Situation item that ceases to be relevant  
- Fixed an OOS where the War Coordinator's update_targets_tick could differ for hotjoining players  
- Fixed becoming head of faith in some cases leading to your government changing despite your current government still being valid  
- Fixed being able to grant religious titles to wrong gender based on faith clerical gender  
- Fixed cases where factions were disbanding and reforming constantly  
- Fixed changing culture not instantly removing you as the culture head of your own culture  
- Fixed cities not being valid holy order HQs  
- Fixed claimant wars where the claimant dies getting invalidated the day after becoming a Depose war. Now the Depose war should continue properly  
- Fixed coat of arms of the duchies of Upper and Lower Silesia  
- Fixed events timing out in some cases causing an invalid option to be picked  
- Fixed fertility and health sometimes being wrong for a while after gaining a modifier to them  
- Fixed feudal contracts in the HRE being unmodifiable at start  
- Fixed holders of the Duchy of Verona having access to Seniority succession from start  
- Fixed interface bug where players could get stuck within a war with reversed war leaders, unable to end it "  
- Fixed it being possible for an agent to join the same scheme more than once  
- Fixed loc error in player council appointment message as liege  
- Fixed mountain split between Taurus and Tianshan  
- Fixed not being able to grant theocratic titles to clerical gender of your faith if dominant gender was different  
- Fixed pilgrimage location selection event options repeating in mysterious ways  
- Fixed priests of some faiths wearing clothes of other religions  
- Fixed ruler designed children under the age of 3 being able to accumulate more personality traits than is fair  
- Fixed sneaky person's odd fashion style in Intriguing Prospect event  
- Fixed some African and Eastern religions not using the correct priest clothes  
- Fixed suggestion to create head of faith title not appearing when possible  
- Fixed the game crashing if you randomize the dynasty name of a Frankish character twice in the Ruler Designer  
- Fixed the imprisonment chance from difference in miliary strength not actually being capped at 20, despite it claiming it is  
- Fixed the witch secrets of children in houses with covens not being properly given out to parents or house heads  
- Fixed two Request Divorce interactions appearing for same dynasty spouses who share a religion head  
- Fixed warning about Runestone destruction when granting titles appearing even when there was no stone present  
- Fixing a bug when dead ruler continues to hold the original land after adventuring Casus Belli  
- Forming the Archduchy of Austria now makes it dejure part of the same empire as the Duchy of Austria (the HRE unless dejure drift has occurred)  
- Giving a landless army commander a title will no longer automatically remove them from command "  
- Giving a landless councillor a title will no longer automatically remove their council position  
- Granting a vassal now only gives a truce when it's granted to your liege (and thus becomes someone you can declare war on)  
- Great Holy Wars should now invalidate if both sides follow the same faith  
- Hiding Early Great Pox from showing in the encyclopedia  
- Integrate Title doesn't require a diplomatic genius for Chancellor anymore  
- Liege's realm no longer shows as potential ally in offensive war, even if they are allied to you  
- Lubsko CoA no longer features a camel  
- Made performance improvements to the frame rate when you have a large empire  
- Meet peer events will be generated for guests as well  
- Migrate to Pannonia casus belli is now inherited by heir if not undertaken  
- Norse characters will no longer be forced to adopt Swedish culture merely by virtue of owning land in Scandinavia  
- Northmen Armies won't come knocking every year on exactly the same date anymore  
- Now linebreaks properly when multiple reasons block declaring war  
- Piety cost for kinslaying from accepted to dynastic criminal has been corrected  
- Players can now arrange marriages with single mayors in their area  
- Reducing speed using the [-] key now produces a consistent sound  
- Removed Disabled Building notifications in cases where buildings cannot be enabled due to religion  
- Sayyid is now removed if a real father reveal shows it should not have been inherited  
- Sayyid trait is now removed if a child is revealed to have a disputed heritage  
- Strait and ford tooltips now correctly refer to the connecting baronies in all circumstances "  
- Temple holdings constructed by Theocratic faiths are now immediately leased to the clergy upon completion "  
- The AI will now disband Holy Orders of other faiths in their realm  
- The Alans won't start anymore in 1066 with Early Medieval innovations despite being still Tribal  
- Titles which can be created info in Current Situation should now match actual title costs  
- Tribal Muslims with a tribal liege will now become Clan if they feudalise  
- Trimming the Dynasty option won't overflow anymore in case of several skills valid as trigger  
- Unreformed Doctrine now tells the player that it allows them to raid. Also converted raiding into a doctrine parameter for more flexibility.  
- Vassals revolting that get imprisoned before the end of war can now be punished without incurring tyranny when demand is enforced  
- Vassals who refuse your title revocation while imprisoned by another character and lose the following war are now forced to concede a title  
- Very Strong Warhorses are now even better than Strong Warhorses  
- When using the Gender Equality game rule, your vassals no longer complain you're not a man for a couple of days before getting over it  
- You can no longer feudalize a county with an ongoing construction  
- created a scripted effect to homogenize the consequences when revoking the lease of a Holy Order  
- no more pretending to legitimize the children of another lover when you marry one of your lovers  
- now you will know clearly why you can't restore the Roman Empire  
- when an excommunication war invalidates due to excommunication being lifted, the formerly excommunicated is no longer deposed  
- "Guardian of your Relative" opinion modifier is no longer removed when only one of two ward relatives is removed  
- A courtier will no longer curse themselves with a nithing pole  
- AI Child Rulers can now assign Guardians to themselves  
- Added an adult check to prevent kids from insulting or seducing foreign rulers  
- Added stricter checks for an event. Now disallowing prisoners, deadly sick, incapable, etc  
- Added text to cooldown for establishing new cultural traditions  
- Attacker's allies should now join a directed GHW  
- Being an adjacent realm that is the de jure liege of an island nation will no longer trigger the "distant realm" opinion malus  
- Candidates for Elective succession who only have a weak claim no longer get bonuses for having both a weak and a strong claim  
- Celebration in XXX scheme event now use the target's correct location  
- Characters will now dislike you for demanding a favor even if you "ransom" them and not only if you "negotiate their release"  
- Children as a result of incest now appear as valid candidates in the election window  
- Dynasty legacies introduced in Northern Lords can now unlock the A Legacy To Last the Ages achievement  
- Enabled a lover yearly event that was orphaned  
- Fixed AI being able to declare war directly on someone else's vassal  
- Fixed CoA emblem not showing correctly on continue game button after changing graphics settings  
- Fixed Court Chaplains who are appointed for life by doctrine from using their Hooks to ensure they are not fired from the Council  
- Fixed Galician and Basque cultures being missing as retainable options based on geography in the Visigothic split event  
- Fixed a bug with the Krstjani holy site of Visoki which prevented it from ever being active. Also updated the localization to be more clear.  
- Fixed a number of cases where modifiers were being used on the wrong scope.  
- Fixed excessive chance for children to drown during playdates  
- Fixed faulty event id for the slav uniter decision  
- Fixed non-familial clan vassal opinion tooltip in Balance of Power event  
- Fixed spouse event that would incorrectly target the spouse when trying to put in a good word for their spouse  
- Fixed the AI being unable to offer vassalization to certain types of rulers  
- Fixed the Decision to restore the Holy Roman Empire being blocked by the existence of France  
- Fixed the max number of Embassies bonuses that can stack (5)  
- Fixed the tenet Natural Primitivism to properly increase the law cost by 50% as intended.  
- Fixed tooltips for the adventurer inspiration's finish event  
- Fixing alpha issue on the screenshots from Royal Court  
- Fixing issue with Russian being upper lower case dependent in character search  
- Friendly Counsel now counts the friendships from before the perk is gained  
- Hale, Robust, and Herculian/Amazonian are now hidden at birth, and revealed at age 5  
- If your spymaster discovers a scheme targeting them they will no longer discuss the situation in third-person  
- It is no longer possible to Blackmail multiple characters at the same time  
- Jews and Muslims will no longer hunt boars  
- Like a Viper & Tire Opponent moves now actually make your opponent more likely to injure themselves & you less likely to injure yourself (respectively), plus both moves apply only once rather than for the rest of the bout  
- Made sure the invalidation message for you befriend scheme properly tells you that you're already friends with the target  
- Made sure you can always extort a murderer if you walk in on them killing someone during a feast  
- Made sure your dead vassal can't return from the dead to praise your cool new temple  
- Make sure council task progress speed in counties is the same when you start it or load from save game  
- No longer possible to fabricate hooks on characters you already got a hook on.  
- Populist Revolt wars no longer invalidate as soon as any county member is annexed by a foreign power  
- Priest now wear armor when actively serving in an army as a knight or commander  
- Removed broken tooltips from a couple of murder outcome events  
- Ruler Designed characters who are married at game start don't get the wedding event  
- Sacrifices for Grand Blots no longer spawns the event of them skipping out on festivities  
- The Dog/Cat story cycle events no longer trigger when you're imprisoned  
- The Heresiarch trait is now removed upon conversion to another faith  
- The Pilgrim trait is now removed upon conversion to a faith of another religion  
- The Rise of the Scots culture event will no longer fire immediately in the 867 start, but become more likely as the 11th century approaches  
- The Unite the Slavs decision will now correctly add the kingdom of Vladimir dejure to the empire of Slavia instead of Permia  
- The rise of the Mongol Temujin will no longer occur if a player is Mongol cultural head with a realm size over 100  
- The traits given to descendants of the character consecrating family is now properly given despite having a different religion  
- Tightened restrictions on what allies can be called into a holy war  
- Updated commander trait tooltip in potential battle tooltip  
- Updated tooltip text to better communicate that the accept criteria for marriage proposals are affected by gained prestige.  
- Vassals no longer become independent if they inherit new primary  
- Vassals no longer become independent if they inherit new primary title from an independent ruler  
- Vassals who will rebel due to the tyrannical actions opinion are now also displayed in the list of who will join the revolt  
- Warnings about giving away titles and thereby destroying runestones now work properly  
- Women/Men present in line of succession for male/female only title  
- You are no longer blocked from fabricating dirty secrets about your fellow witches  
- You can no longer offer to educate the children of someone you're at war with  
- You can no longer try to murder characters that doesn't exists during hunts  
- You will no longer be encouraged to search for a peasant that you're already scheming against  
- You will no longer be raided by your vassals for slaves  
- You will no longer be told that you can't befriend your new friend just because they're now your friend  
- You will no longer magically know that a prisoner killed a family member, but they might accidentally confess if they're stupid  
- You're no longer blocked from offering guardians if recipient has two wards  
- You're now clearly told why you cannot abduct your own child since decency evidently isn't enough  
- Your Catholic wife will no longer try to set you up with a barmaid  
- Your child will no longer avoid your religious conversions just because they're out learning stuff  
- Your child will no longer beat themselves up to spite you because they're your rival  
- Your intrigue mentor will no longer torture themselves  
- Your spymaster can now find secret bastards even if your religion is cool with adultery  
- Your vassal will no longer give up all their counties to renegotiate their contract  
- corrected a grammatical issue when challenging other characters to single combat  
- disinheriting someone if you are not the dynasty head (e.g., via event) now has a default opinion penalty with your dynasty head  
- fixed GHW targeting script, upped chance for retribution crusade targeting you after HumSac'ing a HoF  
- fixed Seek Aid of the Spirits decision cooldown  
- fixed missing possible effects tooltip for baron-tier marshals in the organize levies task  
- Added available adult checks to some triggers that were missing them  
- now revoking the lease of a Holy Order always have the same cost and consequences  
- restructured Promote Culture and Convert Faith tasks modifier to avoid having negative progresses.  
- Harsh winter now correctly increases provincial casualties and tooltip correctly reflect this.  
- Piety cost for faith conversion is now applied properly.  
- Post-battle window now shows correct resource gain properly when fighting as an ally, would show Fame or Devotion when it actually gave Prestige or Piety.  
- Missing tooltip inside Claim Liege Title window has been found.  
- Fixed edge case where upon loading a save and attempting to select an army which on that same day started a siege would make the army unselectable.  
- Moving unit graphics are now prioritized over other unit graphics when they occupy the same position.  
- Fixed a bug when big disjoint groups of provinces were missing parts of their borders

<!-- artifact:reactions:start -->
- 133 Like
- 60 Love
- 10 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
