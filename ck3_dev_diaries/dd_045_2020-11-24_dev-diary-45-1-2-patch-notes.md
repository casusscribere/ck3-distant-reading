---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1444123/"
forum_thread_id: 1444123
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 45
title: "CK3 Dev Diary #45 - 1.2 Patch Notes"
dd_date: 2020-11-24
author_handle: rageair
expansion: Post-release patches
patch: Patch 1.2 (Argent)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 7832
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1444123'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1516.jpg?1606212736
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_151_to_153
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_668_to_673
    action: preserved_and_flagged
    counts:
      Like: 95
      Love: 45
      (unlabeled — rendered as base64 data URI): 2
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_681_to_752
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_753_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1516.jpg?1606212736)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #45 - 1.2 Patch Notes

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Nov 24, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-45-1-2-patch-notes.1444123/)
<!-- artifact:thread_metadata:end -->

Greetings!  

The 1.2 ‘Argent’ patch is soon released, but until you get home from work/school we thought that you might enjoy a peek at the Patch Notes! We hope that you’ll have lots of fun with the Ruler Designer and all the other new features. We’ve also fixed a whole heap of bugs, of course!  

These patch notes clock in at a whopping 2.6 [@blackninja9939](https://forum.paradoxplaza.com/forum/members/795679/) in length! One Blackninja should roughly equal one Groogy, for those who are more familiar with the old gold standard.  

Spoiler: 1.2 Patch Notes

###################  
# Free Features  
###################  
- Added a Ruler Designer where you can customize the ruler you’ll start with before the game starts. This works with achievements - but under certain restrictions.  
- Added a character Kill List to the character window  
- Added the functionality to attach your armies to another allied army located in the same province in order to follow the other army  

###################  
# Balance  
###################  
- Added a new game rule that controls the AI's willingness to do Matrilineal marriages.  
- Mercenaries are no longer guaranteed to include cultural men at arms; they're just likely to  
- Mercenary companies of cultures that have Camel Riders unlocked will no longer include tons of camels for no reason  
- Armored horsemen and war elephants can now appear in mercenary bands, but at lower numbers than other men at arms types  
- Holy Order regiment sizes are now smaller for War Elephants and similar  
- Holy Orders now consolidate their MaA regiments some rather than having a ton of 100-man MaA regiments  
- Cats and dogs now live a bit longer, appear slightly less often, and trigger events less frequently  
- Constructing a brand new Temple now gives your faith some fervor  
- Economically-inclined AI's now somewhat prefer upgrading Economic buildings  
- Founding a Holy Order now gives fervor to the affected Faith  
- GHW: A successful GHW will now reduce the attacking Faith's Fervor by 25 (down from 30), an unsuccessful GHW will only reduce Fervor by 15 (down from 30)  
- GHW: Invalidated GHWs now reduce Fervor by much less  
- GHW: The cooldown between Great Holy Wars has been increased to 30 years (up from 5), in practice this means that Fervor for bigger faiths should stay at higher levels for longer  
- GHW: The minimum fervor for launching a Great Holy War has been lowered to 65 (used to be 75), so that the increased cooldown between GHW's doesn't mean that too few are launched  
- Successful Holy Wars now affect fervor significantly less (minor Holy Wars reduce by 1, Duchy Holy Wars by 2, Kingdom Holy Wars by 5)  
- Unsuccessful Holy Wars no longer reduce the attacking Faith's fervor  
- Halved the impact of Fervor on the speed of the Convert Faith of County councilor task, converting a high-fervor faith as a low-fervor one should no longer be impossible (but still hard, of course!)  
- Greedy AI's are now less inclined to spend gold on their target during non-hostile schemes  
- Having a strong hook on your realm priest will now cause them to pay you maximum contribution as if they endorsed you with 100 opinion.  
- In independence wars, ticking warscore is now given to the revolters if they fully control all the revolters' domain, while the defender gets ticking warscore as long as they occupy at least one holding from the revolters' domain  
- It's no longer possible to send your court chaplain, spouse or concubines to a foreign court as a guardian  
- It's now easier to divorce openly incestuous spouses  
- Landless religious heads not of your faith will no longer show up in the marriage finder  
- MaA maintenance cost can no longer go below 10%  
- Made hostility due to conflicting wars a lot broader. Now it applies to defensive wars too, and propagates to vassals. In practice this should mean that you'll never be unable to siege a holding in a realm you're at war with due to it being occupied by a third party  
- Male/Female Only realm law now consistently blocks the other gender from inheriting claims  
- Only the holder of a holding can cancel construction now. No more canceling your vassals' constructions to get money  
- Peasant/Populist Revolt leaders can no longer marry  
- The AI should no longer choose to create Cadet Branches should that mean that the player's children, grandchildren or great-grandchildren would change house  
- The AI should now found more Holy Orders  
- The Arrogant trait now gives -10 Secrecy to owned schemes  
- The Craven trait now gives +10 Secrecy to owned schemes  
- The Crusader trait (Warrior of the Faith) now gives less Same Faith opinion and more Prowess  
- The block on granting de jure vassals independence is now based only on whether their primary title is de jure under a title you hold, rather than *any* title they hold being dejure under a title you hold  
- Great Holy Wars will now fail to launch if total projected attacker strength is less than 33% of projected defender strength  
- The defender in an Undirected Great Holy War (Crusade) can now gain up to 150% warscore from battles.  
- Warscore from battles in Undirected Great Holy Wars (Crusades) has been increased significantly. This should make defending less of a slog, especially in massive crusades (with 100k+ troops on each side) where battles should no longer give miniscule warscore values.  
- The ticking warscore in Undirected Great Holy Wars (Crusades) has been significantly increased. This allows a defender to more easily win if they manage to keep the entire targeted kingdom free from occupations.  
- The first army of the siege controller that has a commander now determines the siege commander  
- The first army to arrive at a siege now controls the siege  
- Third party occupations are now in the owner's favor for the purpose of ticking warscore. So for instance some Peasant Rebels or warring vassals occupying part of the war goal will now no longer mean that you as the defender stop getting ticking warscore against the realm trying to take that land from you  
- Titles with Male/Female Only/Preference will now get handed out according to Partition if your realm law is Partition and all your Partition Heirs are of the title's preferred gender  
- You can no longer manually add Gender Law exceptions to your held titles  
- Updated some scheme events’ impact on schemes  
- Vassals will no longer convert their capital when you demand their conversion  
- Buildings now give % modifiers to MaA stats rather than flat mods, this should prevent stat inflation and keep Cultural MaA variants competitive  
- Wandering characters no longer get absurd stats should they have immense amounts of gold to spend  
- Wandering characters of the player's dynasty no longer spend money on self-improvement, to prevent an exploit where you would load your heir with gold and kick them out of court  
- When Feudalizing, there's now a random chance for a City and/or a Temple to spawn in each tribal County. Higher development increases this chance.  
- When you push the claim of a foreign ruler in a claimant faction, they now become a vassal of the former holder of the title if that title becomes their new primary title  
- You can now arrange marriages for all of your descendants, not only your direct children  
- Reduced the overall effectiveness of Light Cavalry in the main phase of combat. They were simply too cost-effective for the stats they would bring. Light Cavalry units still excel during the aftermath, as well in their preferred terrain type.  
- Armored Horsemen now have an added penalty to Toughness and Pursuit in Wetlands like other cavalry units.  
- Blocked several uncommon situations where successful Populist Factions could seize all of the counties which belong to a vassal player, causing the player to Game Over immediately and without warning  
- Children can become more inclined to drink later in life if their guardians are a poor influence  
- Courtiers and guests no longer seek out new lovers when they already have a partner  
- Did a pass over character weight values and the traits that affects weight gain/loss  
- Granting a vassal to your liege now creates a two-way truce between you and your former vassal  
- Improved Mongol Empire disintegration  
- Increased the County Opinion bonus for putting down a Peasant or Popular Rebellion by 150%, and also increased the duration by 150%  
- Increased the penalties to the Seduce scheme's success change when the scheme target is married and loves their spouse  
- Just characters no longer gain Stress when they execute someone if they also have a faith with the Human Sacrifice tenet.  
- Reduced the amount of levies and taxes gained from Tribal Obligations. Vassals now provides 75% levies (down from 100%) and 40% taxes (down from 50%) on the highest level of fame.  
- Reduced the frequency of certain events intended to create friendships, rivalries, disease-outbreaks-by-way-of-corpse etc  
- Significantly slowed down Fabricate Claim task when targeting vassals  
- The Embassies perks now has a maximum number of skill points it can give out  
- The Sound Formation perk now has a maximum number of skill points it can give out  
- Updated and moved the Gold Mines of Mali special buildings to their respective county capital, allowing them to be built by tribals.  

###################  
# AI  
###################  
- AI will now consider breaking up with their AI lovers upon marriage  
- AI will now abandon sieges that are blocked by a bigger garrison  
- AI will now not take family members as concubines unless their faith allows for it or under rare circumstances  
- Gave the AI a few lessons on closely following the player's units and promptly joining battles, and that maybe it shouldn't take its toys and go elsewhere just because supply is briefly too low  
- Informed the AI that it might be a good idea to not count allied vassals or lieges when deciding whether to declare war or not, what with it being impossible to call them into your wars  
- Naval raiders can now raid along major rivers  
- Now better at picking tasks around the target province  
- Rebalanced AI goals. Effectively this should mean the AI is now more willing to feudalize its holdings or make a holy order  
- Several units can pick the same task as long as they keep under the supply limit  
- Taught the AI how to better balance its budget. It now distributes its money based on its net income rather than first distributing its income then removing military maintenance from its short-term pool of money. This should result in the AI building more buildings. When military maintenance is higher than income, it will now subtract the deficit from its war chest rather than short-term money  
- The AI now tries to quickly get a handful of Men at Arms, then afterwards slowly buys more Men at Arms until it feels like it is spending enough on them, rather than just stopping outright when it hits that minimal amount  
- The AI should be better at recruiting any cultural MaA variants they may have access to, while also recruiting less of the base unit of the same type (e.g. recruiting less Light Footmen if they have a cultural Skirmisher unit).  
- The AI is now going to prefer upgrading Duchy Buildings in its capital before doing so elsewhere in its domain  
- The AI is now more inclined to build buildings in its realm capital rather than evenly throughout its domain  
- To make a holy order it is now enough for the Pope to not simply dislike the AI, rather than needing 60+ opinion. The 60+ opinion requirement still persists for the player since we like to see the player grovel  
- Told the AI that even though a holding is of the wrong type for it to own, it is a good idea to build it so that it has one of each type in the county and can build the type it *really* wants  
- Told the AI that when it has multiple possible CB targets within a realm, it's probably a good idea to pick the one that's actually bordering it, rather than sometimes picking one that's just bordering the sea  
- Generally lowered the AI aggressiveness, this means that they’ll declare fewer wars overall  
- Told the AI to get over its phobia of hostile raiders  

###################  
# Interface  
###################  
- Player characters now get their weight target checked once a year rather than every three years, which should make things like "Lose Weight" feel more responsive  
- Toggling nudity is now a setting rather than a game rule, so you can toggle it on the fly  
- Reworked the dynasty window to include information about how house and dynasty heads are chosen.  
- Military strength can now also be seen and compared between house heads in the house list of a dynasty  
- The dynasty legacy area uses a more compact way to show which legacy tracks you have unlocked, how many steps are unlocked, and which ones you've finished  
- Reworked battle window for looks and functionality  
- The Coat of Arms of all human players are now decorated to make them stand out  
- When raising a rally point that'd result in an army above supply limit, the army will now be raised split into multiple armies and spread out to adjacent provinces. This should make dealing with supply of recently raised armies easier  
- Added the Grant to Low Noble button to the Title View like we have on the Holding View.  
- Added warnings when voting for a candidate that is not part of your dynasty.  
- Added a game concept link to the Special Contract header when modifying a feudal contract  
- Added a reactive advice for when you've reached the maximum bonus amount that a perk can give  
- Added a text on the war overview that hostages are going to be released after the war ends  
- Added an AI acceptance modifier for the different ransom interactions to clarify that they want more gold and won't accept the ransom if it is too small.  
- Added info to the realm map tooltip about expanding and collapsing realms through ctrl-clicking  
- Close claimants subwindow only when closing title window - allow browsing characters for example  
- Close title history subwindow when closing title window  
- ESC now only closes tooltips if you've got at least two tooltips open  
- Eliminated the map highlighting flickering when hovering over realm coat of arms  
- Fixed ESC having odd results when you're in a window that can be closed by ESC, and you've got tooltips open. Now it'll always cause the tooltips to close (unless you've got only one tooltip open)  
- Fixed a stray space in the secrecy breakdown  
- Fixed coat of arms that have changed from their default in some cases persisting in new campaigns or other saves if you go into that other campaign without shutting the whole game down  
- Fixed cycling through your armies in a province by clicking on the unit icon not working if there's a neutral or allied army in the province as well  
- Fixed doctrines like "Teachings of the Prophet" having unnecessary underlining of their name in the faith window  
- Fixed overlapping siege and battle indicators on map  
- Fixed province icons (including army icons) in some rare cases turning invisible. A small drawback of the fix is that the province icons no longer gradually fade out when you open the ESC menu, but instead disappear instantly  
- Fixed the on-map scaffolds shown when constructing buildings not being rotated in the same direction as the holding itself  
- Fixed the war interface claiming you're rank 0 for participation for all non-GHW wars  
- Improved main menu scaling on wide resolutions  
- Improved show/hide animation behaviour of sidebar windows  
- In wars that don't give out prestige or similar to war allies, the UI will no longer claim that you didn't do enough to be rewarded; that UI element will simply not be shown at all  
- Increased doctrine name’s space by 1 pixel, so that Fundamentalist doesn't get cut off  
- Make sure the list of titles is updated when opening the revoke title window while another one is already open  
- Make sure the raise local raiders can only be clicked when available  
- 'No Beard' is now the top option in the barbershop  
- Show why the player can't raise local raiders in the tooltip if the option is greyed out  
- The call to war button is no longer cut off when involved in multiple wars  
- The intrigue window is no longer empty when opening from an event  
- The revoke title window no longer contains the "show only recent titles" checkbox.  
- The siege notification now says who is besieging you, and the title states the location so that it's visible even when the notification is collapsed  
- The text area in toasts now provides the full toast text as a tooltip. Especially useful if the effects are too long to fully display  
- Ugly characters now have significantly more varied looks, and look more believably ugly  
- When an event kills you, the "you have died" screen only shows up after you click the event away  
- You can now set your childrens' education before age 6, it just won't have any effect before they turn 6  
- You now get a notification in the lower-right corner when a part of your realm gets sieged by someone you're hostile to  
- You now get a toast when you change your primary title  

###################  
# Art  
###################  
- Tribal holdings now look different between the major tribal regions on the map  
- Added another visual level of tribal walls for the lowest possible fort level  
- Ugly characters now look more ugly, to a reasonable extent, by distorting specific facial features more than before  
- Characters young enough to be sitting in the main menu will now sit in front of the others  
- Christian faiths with Vows of Poverty will now see their priests dress no more fancy than a simple monk or nun  
- Moved the Norfolk holding to a more accurate position  
- Reduced the threshold at which a unit gets improved visuals. Now only armies with the lowest Quality will have an unarmored unit, making armored units more common for increased variety.  

###################  
# Audio  
###################  
- Added more prominent SFX to the Top-bar notifications for Alerts, Reactive Advice and Diplomatic actions.  
- Added war-horns SFX to the 100% Warscore notification to increase the noticeability of it.  
- Fixed so that the hunt event theme SFX only plays during hunts and not during pilgrimages.  

###################  
# Localization  
###################  
- Added a title override for the Duchy of Brittany so that it is always known as a Duchy instead of a Petty Kingdom  
- Added content and fixed tense issues  
- Added information about student of knighthood traits in the tooltip about Knighthood innovation  
- Added link to game concept of council tasks in opinion tooltip and monthly piety/prestige overview  
- Added more information on the different types of allies you can call upon during war time  
- Changed some tenses from first to third person in interaction file.  
- Clarified the condition when attempting to usurp a title from someone that considers your faith to be Hostile or Evil.  
- Fixed a mix-up in the event "Information Brokering" which could claim that a woman was fathered by her own son, instead of correctly saying that her son was fathered by another man  
- Fixed assorted localization-issues reported by Betas  
- Fixed broken localization string about inviting warriors to court  
- Fixed broken trigger loc in some buildings  
- Fixed missing loc for the female version of the Royal Cloak  
- Fixed potential typo in The Spitting Image event  
- Independent Iranian Dukes now have custom title names based on their capital county  
- Made sure loc in temptation event is appropriately gendered for translation purposes  
- Renamed Suomenusko to Ukonusko  
- Replaced Boima_Konah with Boima Konah  
- Replaced Ibrahim_Abraham with Ibrahim Abraham  
- Replaced Jahan_Ara with Jahan Ara  
- The 'has_religion' trigger now uses adjective-form instead of noun-form for the name of the the religion  
- Updated Mend the Great Schism text to incorporate all Christian faiths  
- Updated Spanish name for Wrath of The Northmen bookmark  
- Updated broke Holy Order tooltip localization for Borrow Gold from Holy Order decision  
- Updated button text in child naming event  
- Updated loc as reported by betas and players  
- Updated scope used for loc on child event  
- Updated some Spanish locs strings that were using out-of-date game references  
- Updated the description text for the Clerical Function: Recruitment to be more specific that the modifier is applied to the clergy only  
- Updated the localization for the Religious Icon perk desc  
- Updated the unreformed combat advantage tooltip to properly display game concepts.  

###################  
# Game Content  
###################  
- A schemer is no longer safe from discovery until the scheme executes. If a scheme is discovered, there’s now an ongoing chance that the schemer will be exposed and the scheme ended!  
- Added four new murder outcomes  
- Added 2 more child-murder outcomes, you monsters!  
- Added the Turumic faith, a new faith to replace Suomenusko in Siberia  
- Added additional Claim Throne scheme events  
- Added additional Fabricate Hook scheme events  
- Added additional Seduction Scheme events  
- Added two additional game concepts for Hostages and Prisoners of War.  
- Added two more ongoing murder events  
- People will now be a bit miffed if you raid them  
- The Religious Relations task now gives a Same Faith opinion boost in cases where one's faith has layman clergy and no head of faith  
- Updated Qarmatianism's tenets and doctrines to better match their historical practices  
- When using Demand Conversion on a vassal ruler, they may now request a favor instead of only accepting cold hard cash  
- You can now become Infirm  
- Added Unimportant tag to some Actions to mark them as less interesting to the player  

###################  
# User Modding  
###################  
- When starting the game in debug mode (with the -debug_mode command line argument), the game will watch many loaded files for changes, and reload the relevant parts of the game. This works with core game files as well as files in mods. Note that it is a debug & development tool. The reload doesn’t work for everything, and might not be 100% reliable or stable. You should always verify that everything still works after a proper restart of the game.  
- Added a flag entry for flavorization checks to require the context character has a variable/flag of that name set.  
- Added data function PlaySfxEvent  
- Added define CB_SCORE_MULT_NEIGHBOR_TITLE  
- Added define WEIGHT_UPDATE_YEAR_INTERVAL_PLAYER  
- Added frontend data functions Get(Heir/Main/Secondary)CharacterAge  
- Added GetCouncilTitleFirstName  
- Added hired_stack_size setting for MaA types  
- Added hook_strength_max_opinion parameter for lease contracts.  
- Added is_council_task_valid trigger, analogous to set_council_task effect  
- Added list builders *_faith_character, *_faith_ruler, and *_faith_playable_ruler  
- Added modifier owned_scheme_secrecy_add  
- Added modifiers ignore_negative_opinion_of_culture = yes and ignore_opinion_of_different_faith = yes. Makes you ignore your opinion of others rather than others ignore their opinion of you  
- Added more MEN_AT_ARMS_EXPENSE related AI defines  
- Added scripted rule buildings_enabled  
- Added set_pregnancy_gender effect to overwrite the gender of an unborn child.  
- Added support for Custom localization on stories  
- Added trigger has_holding so you can easily check for empty holdings  
- Added trigger is_landless_ruler  
- Added ugliness_portrait_extremity_shift system for more believable ugliness  
- AI can now parse and evaluate CB effects inside hidden_effect blocks  
- can_be_exposed_by now returns false if the secret's already been exposed  
- Fixed some cases where you couldn't inline script math. E.G., in opinion triggers  
- make_pregnant now checks that the character can actually get pregnant and errors if they can't. Added make_pregnant_no_checks which bypasses these  
- Mercenary and holy order sizing now uses defines based on # of sub-regiments in stead of # of men  
- on_alliance_removed, on_alliance_added, and on_alliance_broken now have an unset root and instead uses scope:first for that character. This avoids issues with triggering events for dead people  
- Renamed can_call_ally_liege_vassal_check_trigger to can_join_war_liege_vassal_check_trigger  
- Renamed recipient_not_already_in_another_war_with_any_target_war_participants_trigger to joiner_not_already_in_another_war_with_any_target_war_participants_trigger  
- set_holding_type now works on empty holdings  
- Updated color palette comments to correctly reflect the fact that color palette textures are 16-wide, not 4-wide  
- You can now use attacker/defender_wargoal_percentage of zero to mean "at least one occupation  

###################  
# Databases  
###################  
- Added a number of additional nicknames to historical characters, such as Yaroslav the Wise or Constantine the Great.  
- Alexios Komnenos had a very diverse personality for a ten year old. He now starts with less personality traits.  
- Extended Insularism a little into the Scottish Highlands in 867  
- Extended the Dutch presence slightly, to include a couple of counties in Flanders and Brabant.  
- Fixed a number of marriage issues in history. There were multiple cases of characters being married to the same character, or characters having several spouses without practicing a polygamous faith.  
- Karen is now a vassal to the Tahirid in 867.  
- Made several improvements to the setup in Denmark, 1066. Two historically important characters are now landed; Asbjörn Jarl Ulfson (brother of king Svend) has been given the county of Lolland-Falster, while Thrugot Ulfsen has been given the duchy of Jylland, making both characters playable. Meanwhile, the county of Skåne is now in the hands of Bishop Egino of Lund, to better simulate the importance of the church.  
- Renamed various titles to more closely match history  
- Roger de Hainaut is now a Theocratic vassal and Prince-Bishops of Chalons in 1066.  
- The Cucumber King is no longer unintentionally a kinslayer, due to a wrongly assigned father.  

###################  
# Bugfixes  
###################  
- Fix more cases of various war and realm borders that remain forever on the map after big inheritance or ended wars  
- "Coastal Borders" now properly works with dynamic option, and always show/hide no longer requires game restart  
- A guardian's personality will now have a larger impact on the ward's personality  
- Accepted marriage will now always lead to a friendly greeting  
- Fixed events that were causing married characters to become lovers with another character even when they should have been loyal to their spouse  
- Added a modifier that reduces the risk of AI spouses taking a player's potential heir as their concubine  
- Added a perspective to the warning about a character being a pledged attacker in a GHW  
- Added a recently converted trigger so that less flip-flopping happens in heresy events  
- Added a toast for if you granting titles leads to your vassal becoming a fellow vassal of your liege  
- Added a trigger to a befriending event, making sure that the target isn't picked as the third person in the event  
- Added age trigger for becoming a drunkard event  
- Added an OR to university-check trigger  
- Added clearer loc for if your wife is employed by your liege  
- Added custom warning for Christians trying to create the Empire of Germania  
- Added information in tenet tooltip on the conversion speed penalty for Syncretic Folk Traditions  
- Added missing title to message about obtaining witch secret  
- Added notification if a courtier is invited to another court  
- Added the title on some outcome toasts when seducing a target  
- Added two church holdings to Iceland in 1066 and made sure both rulers are tribal  
- AI characters will no longer be able to join GHWs against their liege  
- ALL vassals will now get new shiny buildings if you adopt feudalism  
- Allied provinces have the same supply limit rules as your own  
- Allies can no longer be considered hostile due to raid mechanics  
- Armies that should get wiped are now properly so after combat  
- As a host you will now be told if someone fails to seduce a guest  
- Characters are no longer angry at their new friends  
- Characters can no longer invite the bishops of foreign realms to give up all of their temporal power and holdings in order to join them as a lowly courtier instead  
- Charlemagne is now lustful - the dude sure got around  
- Claimant factions are now more cautious about sending demands when the claimant is in prison  
- Cleaned up building requirement tooltip for Universities  
- Cleaned up effects and loc in rivalry event  
- Cleaned up how concubines/consorts are shown in the arrange marriage interaction  
- Cleaned up Roman restoration decision  
- Cleaned up tooltip for blocked Modify Vassal Contract interaction  
- Clear the alerts when entering the observer mode, so they don't persist when selecting another character later  
- Compassionate character are now told that blackmailing people is stressful  
- Control-clicking titles in the Grant Title Window will no longer select invalid titles and lock up the rest of the titles  
- Councilors will now wear armor when leading armies  
- Counties can only join claimant factions for titles in their de jure hierarchy, and are less likely to join factions for foreign claimants  
- Discovering a Non-Believer secret now gives a strong hook on clergy  
- Duchy buildings and similar that give fort level now only give it to holdings that have fort level to begin with; no more having to siege down temples and such  
- Eastern Christian denominations now wear more appropriate clerical garb  
- Elective titles with male/female only law will now properly exclude the other sex  
- Electors now correctly evaluate how scared they are of their liege's Dread when casting votes, rather than how scared their own vassals are of them  
- Establish Bactrian Supremacy decision will no longer display for invalid government forms  
- Excommunicated characters can no longer become Pope, Court Chaplains, or inherit the role of being Spiritual Heads  
- Executing an independent ruler will no longer give them an opinion penalty towards you since, you know, they'll be dead.  
- Factions will no longer count on the support of their liege when deciding if they should send an ultimatum or not  
- Fix an issue on Linux that could cause stutters every few seconds by disabling gamepad polling. Gamepad polling for debug purposes can now be enabled by passing in the command line flag "-handle_controller_input"  
- Fixed "years of fertility" not actually making women fertile for longer  
- Fixed a bug that caused Irish characters to be able to Revoke False Conversion when starting a game with the tutorial enabled  
- Fixed a bug that caused rulers to pay substantially less gold than they should for the ransom of a prisoner whose captor has the 'Golden Obligations' perk  
- Fixed a child's favorite toy crashing the entire game  
- Fixed a crash when loading a save game that included pet whose name contained a space  
- Fixed a few instances of the player getting friend/rival relations set without them knowing of it  
- Fixed a number of cases where the domain or vassal limit could fail to update, leaving you for example with a domain limit of 1 instead of 5 until something caused it to recalculate. Fixes old saves too  
- Fixed a rare crash that could happen when wars become invalidated  
- Fixed a rare crash caused by very specific timing of game updates  
- Fixed being able to Offer To Join War for some unintended wars, causing invalidation of other wars  
- Fixed broken scope in Accuse of Heresy Decision event  
- Fixed broken tooltip in hunt event  
- Fixed Clan Invasion wars sometimes invalidation when they shouldn't  
- Fixed confused toast message when a Claim Throne scheme succeeds  
- Fixed Designated Heirs completely breaking Seniority succession. Now it makes your Designated Heir first in line as you would expect  
- Fixed electors sometimes believing that a lower-tier candidate would 'rule from abroad'  
- Fixed holdings not going out of the domain limit grace limit when leased out  
- Fixed holy orders being unable to hold cities  
- Fixed Holy Orders not expanding their diplomatic range based on their leased titles. This could lead to them being out of range of the person they're leasing from  
- Fixed incorrect text coloring for some Holy Order troops  
- Fixed invalid sieges in some cases continuing to completion  
- Fixed it being possible in some cases to marry someone you're already married to  
- Fixed it being possible to siege holdings that you're hostile to (due to a liege war or conflicting war). Now you can only siege hostile *occupations* or for wars you're actually personally involved in  
- Fixed it in rare cases being possible for one or more units to be left out of a combat due to both sides arriving at the exact same time  
- Fixed it in some cases being impossible to retake an occupied holding due to it no longer having a fort. Now when a fort goes away we ensure that the holding gets occupied by the county controller. This fixes the issue in old saves as well  
- Fixed it in some cases being impossible to siege vassals of your war enemy due to your war enemy being the vassal of someone you're allied with in another war  
- Fixed it in some cases being possible to end up with Head of Faith Law despite not even being the head of faith. This would cause you to game over as you end up with no heirs  
- Fixed not being able to disinherit your own children, grandchildren and great-grandchildren if they weren't at court  
- Fixed old saves where someone's the parent of someone who no longer exists (due to incorrectly having been pruned from the game) crashing on load  
- Fixed several issues with the description of the suspected bastardy Secret in Intrigue view  
- Fixed so that holding tooltips show holding type concept instead of just name  
- Fixed some crashes that could happen while loading saves or viewing the save list  
- Fixed some traits not being assigned to a category  
- Fixed special buildings sometimes appearing in regular building slots when you convert from Tribal. This could even lead to duplicates of these special buildings  
- Fixed the first level of Hunting Grounds not having any levies  
- Fixed the forming of Austria event to not feature the HRE twice  
- Fixed the game in rare cases completely erasing members of your family from existence after their death. Look, we all hated uncle Bob, but we can't just pretend he never existed  
- Fixed the inverted liege culture for the Hungarian migration decision  
- Fixed the rulers of cities sometimes ending up with Clan government rather than Republic government  
- Fixed the trigger for showing an alternative text in an befriend scheme event  
- Fixed the vassal limit not updating when vassals are transferred as a result of their liege title changing holder  
- Fixed the vassal limit sometimes resetting to 1 for a single day  
- Fixed three achievements that would unlock even when they weren't playing with the required character for the achievement, as long as they didn't reload the game  
- Fixed Tribal Law in some cases not disappearing when you become Feudal  
- Fixed typo in battle tutorial  
- Fixed wars not always transferring when the war target becomes the vassal of someone else. This could lead to weirdness like a war targeting someone's vassal despite the attacker having the same liege as the defender's liege; would now transfer to the defender's liege instead  
- Former Heads of Faith now keep their clothes on, presuming they held the HoF title at the time of their death  
- Franconian culture now uses German names  
- Friendly counsel now has a cap of how many stat bonuses the perk can give (5)  
- Game rules and ironman mode are now reset when starting the game as a tutorial game.  
- Golden Obligations no longer increases ransom prices  
- Good things now happen to good chancellors  
- Guardians will now properly return to where they came from if their ward finishes their education or dies  
- Head of Faith will now wish you luck in your holy wars no matter what size they are  
- Heads of Faith will no longer grant requests for claims on theocratic lessees  
- Holy order succession now checks if the character is a member of your court correctly  
- If you convert to feudalism ALL your vassals will now jump on the hype-train  
- If you demand someones conversion multiple times they will now keep their anger to one opinion modifier  
- If you try to make too many children your wards you'll now be told off in a strongly worded letter  
- If you're trying to blackmail someone over something that, according to them, isn't shunned or criminal you will now be told that properly  
- Intelligent women no longer confront their pregnant lesbian lover to ask if they are the father of that child. Stupid women however, still have a chance to ask that question.  
- It is now criminal to refuse conversion even if the religions aren't the same  
- Knights in an army should now also gain the Crusader trait (Warrior of the Faith)  
- Made sure bully event has complete loc  
- Made sure Liberty Wars aren't immediately followed by more factions  
- Made sure spouse event saves agent scope properly  
- Made sure the refund you get if a character refuses to take the vows is the same amount of piety you spent asking them  
- Made sure the warnings displayed when asking someone to join a Holy Order are correct  
- Make sure that holdings no longer have a count of 0 and instead have a minimum of 1  
- Make sure that the save name overwrite dialog box shows up regardless of case sensitivity  
- Make sure that tooltip delay timer option works correctly  
- Make sure the call to war window in the observer mode doesn't require user input and doesn't pause the game  
- Mercenaries and holy orders are now correctly counted when calculating max military strength  
- Obfuscating a learning challenge outcome since the learning skill might be different than what's shown in the tooltip if they gain learning+1 before the learning challenge  
- Offering Guardianship to an underage ruler will now pre-fill them as the ward  
- Offering vassalization to neighboring realms will no longer sometimes claim that they are far from your realm  
- Peasant Leaders now wear appropriately filthy clothing while they are leading a revolt, or are landless  
- People are no longer scared of you if you fail to imprison someone  
- People will no longer be less keen on marrying into your family if you have useless alliances  
- Performing executions when you have the Human Sacrifice tenet will now have the victim's death reason say that they were sacrificed, rather than just executed.  
- Physicians can now treat themselves, and they're also more likely to "mess up" your treatment if they're trying to murder you  
- Playing as Daurama and embracing your son as your heir will now move him to your court  
- Previously discovered Innovations are now carried over when a character takes the Form Portugal decision and becomes Portuguese  
- Raiders should no longer appear in provinces outside of their range  
- Removed attempted use of non-existent game concept from loc  
- Removed outcome events for Convert Faith and Promote Culture council tasks since you also get notifications  
- Removed the 3 day delay on executing the abduction scheme  
- Removed unnecessary spacing in Hunt decision and cleaned up the loc file  
- Removed unnecessary triggered event from imprisonment logic that was causing errors in the error log  
- Removing the same dynasty requirement from elective succession close and extended family members.  
- Resolved a logical mismatch that caused the game to simultaneously recommend and forbid revoking a title from allied vassals  
- Robert I of France now correctly belongs to House Robertine instead of House Capet  
- Ruler now gets notified when they receive an unpressed claim as a result of a foreign chancellor's blunder  
- Scheme event now shows the name of the spy in toast instead of nothing (or the target's name in German)  
- Someone else imprisoning people fairly will no longer make you relieved about not gaining tyranny yourself  
- Spouses and lovers will only act as your wingman if they're ok with you bedding someone else  
- Subtle Desire perk now correctly removes the penalty applied against seducing the spouse of someone of a higher rank  
- The "Murderer at court" story cycle will now end if you send the courtier responsible away  
- The 'Few Spouses' warning will now only appear if you're lacking spouses for your tier  
- The AI will now dump all of their lovers that are far far away when they marry  
- The Amnesty for False Conversions decision now gives correct tooltip about dread requirements  
- The amount one gets from demanding payment is capped to 50 gold or based on how much ransom worth they have if less than 50 gold  
- The cost for legitimizing a bastard in your dynasty is now collected in the right place  
- The disembarked penalty is correctly applied and carried over when splitting an army or merging them  
- The Earl of Desmond will now slip your net and avoid capture in combat during the tutorial  
- The Greenhouse and Sicilian Parliament now gives tax as they should  
- The Matrilineal Checkbox will now default to the correct state based on the character being married off when playing an equal faith  
- The outliner will now be properly hidden when selecting a councillor task  
- The realm you're in will no longer be described as "a faraway place" in pilgrimage event  
- The retracting vassals interaction now gives tyranny if declined  
- The University can now be founded in Fes, the Almohadi Holy Site was moved to the neighboring barony as to not cause conflicts  
- The Vassalization and Subjugation CB's are now properly usable by non-independent players  
- Trying to divorce your House head no longer confuses your House Head as much  
- Uniting the West Slav Kingdoms as an Empire now drifts the kingdoms to your primary title  
- Unjustified imprisonment now results in tyranny even if the imprisonment is declined  
- Unlanded characters blocked from trying to raid  
- Unlocked the "Inspire Opus Francigenum" decision for Frankish cultures as well  
- Updated a bubonic event to not show the court physician twice  
- Updated Jarl Haesteinn's age in the bookmarks to match the one in-game  
- Updated personality and treason modifiers for characters accepting imprisonment  
- Updated portrait position of vassal in a hunt event to be in the lower_right if they are not participating in the hunt but can receive a trophy gift  
- Updated Slavia region borders. Added West Slavia and South Slavia as custom regions.  
- Updated some event-backgrounds to be more appropriate  
- Updated the Druze marriage doctrine from polygamous to monogamous  
- Updated the Norman Yoke achievement so that it can be unlocked by descendants of William as well  
- Visual traits like Blind or Disfigured now show up on children  
- Wards and Guardians should now move in a way that makes sense, and properly go home if things doesn't work out  
- When Asking a Spiritual HoF for Gold, they will now factor ongoing County-level and Kingdom-level Holy Wars into their considerations (instead of only Duchy-level Holy Wars)  
- When you attempt to ransom yourself for whatever gold you have (but is unable to pay the full amount) the AI will now agree if you have at least half of the necessary gold, as long as the AI isn't too greedy and want all of it.  
- When you embrace english culture all your vassals will now join in on the hug  
- Whether you can imprison a vassal that refuses conversion or not is now made clearer in the interaction  
- While considering whether to become your vassal or not characters will now consider their distance to you, not your liege  
- Yemeni now uses East African ethnicity  
- Your bastards will no longer sneak out of your court  
- You can no longer convince the Grandmaster of a Holy Order to convert  
- You can no longer declare war when you're behind bars  
- You can no longer mistake your infant child for a serial killer  
- You can no longer promise a Holy Order some land and then NOT give it after they give you cash for it  
- You can no longer see two versions of your bored daughter sitting under a pavilion  
- You can no longer take your daughter as concubine, unless your faith is cool with it of course  
- You can now denounce and disinherit dynasty members that are not of your faith  
- You can now hire a physician even if you have the black death  
- You can now legitimize bastards of your house as the dynasty head  
- You can now name children born in your court that are of your dynasty  
- You can now try to convert people to witchcraft even if they're not of your "faith"  
- You cannot confide in friends you do not have  
- You no longer have to have negative learning to condemn your vassal's sins  
- You now have to actively scheme to convert someone to witchcraft to discover that they're already a witch  
- You now make sure that you CAN spy on your spouse before you do  
- You will no longer be able to randomly lose a level of devotion if you're a religious head  
- You will no longer be advised to Grant Titles to dead characters  
- You will no longer be told about your bishop breaking their betrothal  
- You will no longer be urged to imprison a vassal's random courtier  
- You will no longer call people "vile" as a friendly greeting  
- You will no longer refer to yourself as your wife's ex-husband if you marry her when she's your concubine  
- You will no longer revert to confederate partition succession if you have primogeniture when you reform the Roman Empire  
- You will no longer switch to the Reichskrone if Byzantium is your main title  
- You will no longer think of your angry spouse as your vassal  
- You will now be told clearly that you will gain no tyranny from executing a starving man  
- You will now be told if a secret you're using for blackmail is exposed  
- You will now be told in very clear words what will happen if you try to imprison the Pope  
- You will now get more feedback and faster results when trying to gain/lose weight  
- You will now only get an op. boost of Order Members and Crusaders if you're of the same faith  
- You're no longer advised to increase control in a county your marshal is already working on  
- Your court physician will now actually get some gold for taking up the knife  
- Your friend will no longer support your scheme to claim their throne  
- Your gender succession law no longer gets reset when converting from one gender-equal faith to a different gender-equal faith  
- Your once upon a time bastard child will no longer be a bastard if they convert to your faith that doesn't believe in them  
- Your overly talkative agent's arms will no longer clip through their clothes  
- Your portrait will now only show once even if you ransom yourself from prison  
- Your soulmate will no longer be peeved about you sleeping around if you have the polyamory tenet  
- Your spymaster will no longer fabricate a secret about themselves  
- Your vassals will no longer be less likely to accept a marriage because you have too many alliances already


The checksum for 1.2 is: **d5f5**  

Now the winter holidays are almost upon us, so Dev Diaries will slow down once again. We’ll be back next year!

<!-- artifact:reactions:start -->
- 95 Like
- 45 Love
- 12 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 Haha
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 9 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
