---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1478364/"
forum_thread_id: 1478364
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 63
title: "CK3 Dev Diary #63 - 1.4.0 “Azure” Patch Notes"
dd_date: 2021-06-08
author_handle: pdx_snob
expansion: Northern Lords
patch: Patch 1.4 (Azure)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 4539
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1478364'
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
    location: raw_lines_~28_to_144
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_146_to_148
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_506_to_509
    action: preserved_and_flagged
    counts:
      Like: 146
      Love: 56
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_517_to_627
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_628_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #63 - 1.4.0 “Azure” Patch Notes

<!-- artifact:thread_metadata:start -->
- Thread starter [pdx_snob](https://forum.paradoxplaza.com/forum/members/pdx_snob.1589970/)
- Start date [Jun 8, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-63-1-4-0-azure-patch-notes.1478364/)
<!-- artifact:thread_metadata:end -->

Hello crusaders!  

Nice meeting you all, it was only last year that I joined the Crusader Kings III production team so it is with great pleasure that I write my first Dev Diary - to share with you the final changelog of the Azure patch, and some news on the Multiplayer open beta.  

Everything went well since the last diary so the patch will drop **today** as promised. It packs a mix of new features, new events, balance improvements, AI improvements, modding improvements and fixes to bugs reported by our great community.  

Check the Dev Diaries below for a refresher on what has been mentioned about Azure so far:  
[CK3 Dev Diary #55 - Modding improvements](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-iii-dev-diary-55-modding-improvements.1466888/)  
[CK3 Dev Diary #57 - An eventful summer](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-57-an-eventful-summer.1470041/)  
[CK3 Dev Diary #58 - Stre(ss)tching the traits](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-58-stre-ss-tching-the-traits.1472092/)  
[CK3 Dev Diary #59 - Fantastic presets and where to save them](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/)  
[CK3 Dev Diary #60 - The Cost of Warfare](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-60-the-cost-of-warfare.1474533/)  
[CK3 Dev Diary #62 - Monarch’s journey unleashed](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/)  

The changelog  

So here is the final changelog if you feel like scrolling through 10 pages of additions and fixes:  

Spoiler: CK3 1.4.0 "Azure" Changelog

1.4.0 “Azure” Changelog  

###################  
# Free Features  
###################  


- Game rule presets can be created! You can now easily switch between different configurations depending on your mood. The last configuration is used by default for future games.
- Character finder presets can be created. Finding future spouses, wards, councillors,... will be easier than ever! When creating a new preset, you can save almost everything! Dynamic objects however won’t be memorized (custom faiths, specific Dynasties and Houses)
- Men at arms can be raised independently of levies, either to the first existing rally point or from a specific one. It will allow you to crush small rebellions or wage small wars without calling all your levies.
- At game start, rulers now start with a decent amount of men at arms already hired, based on their income. Upon becoming landed, newly landed rulers will also receive men at arms.
- Dynamic garrisons for holdings have been introduced. Garrisons now have a max and min capacity. When a siege is won, the garrison is depleted and set to its min value. Each month, the current garrison reinforces until it reaches its max capacity. The reinforcement rate is improved by upgrading the holding.
- Unlocked the Monarch's Journey cosmetic items for all players (Hennin, Chaperon, Jester's Hat, Wizard's Beard, Miller, Miller Highlights, Jeanne d'Arc, Pageboy, and Mullet)
  * Jeanne d'Arc haircut will be used by some Frankish women
  * Mullet haircut will be used by some Scottish men
  * The Chaperon hat will be used by some Western mayors after 1300
  * The Hennin hat will be used by some Noble women after 1300
- Added new Lifestyle events:
  * One for Learning: Scholarship
  * One for Martial: Strategy
  * An Event Chain for Martial: Authority
- Added the Meet Peers activity for children. The activity allows them to forge relationships with other kids and maybe learn from unexpected situations. Explore a dozen new events for a more diverse childhood, allowing you to take control of your destiny.
- Some traits have access to new Interactions and Decisions:
  * Arbitrary: can remove a hook by paying prestige and gaining Tyranny
  * Deceitful: can take a decision improving the ongoing hostile schemes if they are above the stress level 1
  * Diligent: can take a decision that will increase the development of the Capital but increase their stress
  * Forgiving: can consume a hook to lose stress and gain opinion
  * Impatient: can take a decision to immediately advance all their on going scheme if they are above the stress level 1
  * Vengeful: can fabricate hooks on their rival without unlocking the perk.
  * Wrathful: can duel criminals to enforce the punishment.
  * Irritable: can duel who they want if they are at the stress level 1 or above. It will generate dread and tyranny



###################  
# Balance  
###################  


- You can now hire mercenaries of your culture from further away. It will allow Iceland to have access to mercenaries.
- The Norman culture now has access to the Regional innovation from the Norse Culture from the start of the game
- Some traits were updated:
  * Ambitious: they now gain stress when signing a White Peace
  * Arrogant: they now gain stress when signing a White Peace
  * Craven: added hostile scheme resistance and intrigue
  * Fickle: added +1 intrigue and increased diplomacy from 1 to 2
  * Generous: loses stress when organizing activities and gifting money
  * Gluttonous: they have a high chance to avoid being murdered if the Poison food method is chosen
  * Greedy: they have a weaker monthly income bonus but an increasing monthly income depending on their stress level
  * Gregarious: they gain stress if they fail at swaying someone
  * Honest: they can lose stress by exposing a secret
  * Just: they can lose stress by exposing a secret
  * Lazy: they have a stronger stress loss bonus
  * Shy: they do not suffer from stress when starting a personal scheme anymore. BUT they have a huge penalty on personal scheme power.
- Overall faction dynamic has been updated:
  * The power threshold is more dynamic: it will be decreased by other factions and their state.
  * There will be no factions created by AI Vassals in the first years of the game to give enough time to stabilize existing realms.
    + 1 year for Dukes
    + 5 years for Kings
    + 10 years for Emperors
  * Faith modifiers are more impactful for Zealous characters and weaker for Cynical
  * Intimidated characters will not be afraid of joining a faction above its power threshold
  * Terrified vassals have a small chance of joining a faction above its power threshold
  * Characters with an opinion of 80+ will never join a faction
- Independence faction modifiers have been updated:
  * Characters will join a suitable Populist faction if they exist instead of creating a new Independence faction
  * Electors are less likely to join or create a faction
  * Vassals that have more than 50% of their territory outside of the De Jure primary title will be more likely to join or create the faction
    + The bigger their realm size, the more likely they are
  * Counts are less likely to join or create a faction
  * Kings are more likely to join or create a faction
  * Characters can be more motivated to join if one of their neighbour is in the faction
- Claimant faction modifiers have been updated
  * Powerful vassals are more likely to create Claimant factions if they have a negative opinion
  * Vassals with a different culture are more likely to join than before
  * Vassals are less likely to create a Claimant if they are not a De Jure vassals. They will instead prefer to create an Independence faction
  * Characters are more likely to join a faction if the Claimant is their De Jure liege
  * Characters are more interested in Claimant faction concerning title above their and in their De Jure hierarchy
- Defeating or dealing with Scandinavian Adventurers now gives a temporary reprieve proportional to size, with smaller realms gaining a larger break whilst larger realms become valid targets again faster
- Embarkation costs can no longer be reduced more than 90%
- Faiths with concubines no longer give Counts a prestige-penalty for not having them, and now only expect dukes to have 1 rather than 2
- Fire and Blood event now adds loot to your raid army, not directly to your treasury, and fires a little less often
- Founding the Capital of the Rus now gives a more mild development level boost, as well as a reasonably hefty boost over time, rather than immediately catapulting you to Constantinople-levels
- Increased the amount of money everyone starts the campaign with by 50%
- Raiders no longer take attrition when raiding next to major rivers
- Scandinavian Adventurers now stagger their attacks through the year instead of ritually attacking on January 1st
- Scandinavian Adventurers will now stop so consistently starving to death at sea before they reach their target
- Scandinavian Adventurers' event MaA are now inheritable
- The cost of mercenary and holy orders now slowly goes up based on the size of your realm
- The cost of mercenary now increases with the tier of the primary title with each Era
- The Tribal government now gives a small amount of prestige each month. This helps avoid situations where new rulers have virtually no prestige gain
- Upped the truce time on for raid-trade events from 5 years to 10
- Stress is now lost when a Rival loses a title
- Updated the stress impact of organizing a Grand Blot
  * Greedy and Shy never lose stress and suffer a progressive stress impact depending on who is invited: the merrier, the bigger the stress impact.
  * Generous and Gregarious never loses stress and suffers a progressive stress impact depending on who is invited: the lesser, the bigger the stress impact.

###################  
# AI  
###################  


- Your children and grandchildren can now get married off by their liege if their liege is their parent or grandparent and is allowed to marry on their own
- Added logic for transferring siege weapons from a subunit to the main subunit
- Added small bonus to current location when selecting a target province to avoid units switching places
- All vassals are now able to declare war no matter how deep down in the vassal tree they are
- CB:s can now have a scripted score that is added to the hard-coded one
- Changed CB base score to be title's Tier^3 instead of Tier^2
- Fixed opinion of self overtaking the base score of many CB:s
- Moved CB score multipliers to defines
- Subunit stacks will be more hesitant to split off siege weapons
- The main subunit stack will never split off its best siege weapons
- The score of potential CB:s are no longer scaled with the strength of the target
- Told the AI that it shouldn't be avoiding running into stronger enemies when it is explicitly trying to help out one of its own units dealing with stronger enemies
- Told the AI that just because it cannot fit its entire army in a single province, that doesn't mean it should stop resupplying
- Told the AI that just because its units are in a separate stack, that doesn't mean it shouldn't help out in a combat it is losing 2 provinces away
- Told the AI to keep its stacks a bit smaller so that it has an easier time resupplying
- Tweaked down de jure multipliers for scoring titles when evaluating CB:s
- Units should ignore strait penalties and hostile attrition if helping another unit
- Units should ignore strait penalties if going into an ongoing combat
- Units with siege weapons will now try to relieve or help sieging units without siege weapons
- Will be more hesitant pushing a claimant's CB over its own
- Will focus more on CB:s that target a title of a higher tier than its current primary title
- Will no longer push a claimant's CB if it targets a title the AI has a claim on
- Will now hunt nearby enemy units even in hostile attrition territory if it deems it worthy
- Willingness to attack a stronger target now scale the more wars the target is in
- Willingness to attack a stronger target now scale with attacker's boldness
- Lowered the odds of creating a Cadet Branch for Counts and Ruler serving a liege of the same Dynasty
- Feudal and clan rulers will not declare war to tribal rulers if they have Tribal holding to convert in their realms
- Vassals’ Holy War will be declared only to direct neighbours to protect smaller realm from the Byzantine empire bigger realms
- Feudal and clan rulers will never start a Vassalization war of a tribal ruler.
- Kings and Emperors are less likely to accept Faction’s demand if they are not at war already.


###################  
# Interface  
###################  


- The Declare War window has been restructured to allow for a better comparison between the two side and ease the access to the Objectives attached to a casus belli
- Fixed some historical characters changing hairstyle or beard upon death
- Fixed the mass prisoner actions in some cases acting on far fewer characters than they should
- Fixed the "Only X Faiths" checkbox in the Other Faiths list in the Faith window being inverted
- Faction members do not hide the opinion of other faction members anymore
- Fixed Send Poem sometimes saying it has 0% chance of success when it actually has 1% chance
- If someone is your ally in a war and your enemy at the same time, they now show as your enemy since walking into them will cause combat. This does not solve the underlying issue of conflicting wars being possible in rare cases
- Fixed typing something into the newborn naming box that matches a localization key causing the text in the box to be replaced with that localization. E.G., in German typing "He" would get replaced with "Er"
- Added missing tooltip when taking a concubine for the chance of children
- All former spouses are now shown in the character window, not just those that are former due to death
- Fixed a bug where a vassal player would not be correctly warned when their own vassals' counties had formed a populist faction against their liege
- Fixed an issue that could cause numerous duplicate interaction notifications to appear
- Fixed unlocked innovations in some cases being hidden due to being impossible to get if you didn't already have them. This could for instance happen to Longships when creating Norman culture
- Fixed sidebar clipping with open windows
- Fixed marriages in some cases giving you a notification about the other party's arranger (E.G., their court owner) getting married, rather than about the alliance formed by the marriage
- Fixed the prestige breakdown incorrectly claiming that army cost modifiers apply to army prestige cost. E.G., the breakdown would say "Tribal: -50%" despite the prestige cost of armies being unaffected

###################  
# Game Content  
###################  


- Defenders of Rod now require a Holy Site without an existing special building
- Game Over loc will now mention any big empire/kingdom you've formed/reformed/unified through the existing big decisions
- Beating a significant amount of landless Scandinavian Adventurers now rewards unique nicknames
- Challenging your Ruler for their title now uses the SCE
- Courtiers who carry a rotting trophy now give off an off-putting smell
- Having a trading ceasefire with a former raid target will now occasionally give both parties access to recruitable notable immigrants
- Poet trait now has a runestone memorialisation
- Raised Voices at the Ting Meet event now has several issues, rather than literally always being the same squabble
- Scandinavian Adventurers may now be paid off or given land preemptively rather than always needing to be fought to the end
- Winter commanders can now auto-win at competitive skiing
- Harsh Winter now has a concept in the encyclopedia
- You can now pay for a runestone your child defaced yourself, though they'll take the lesson to heart
- Dynast can now enforce a divorce or ask a divorce for any member of their Dynasty within their Realm
- Adding new piety icons for Zoroastrianism and Judaism
- Added a follow-up event to a Stewardship: Wealth Lifestyle event which had empty options
- Olympus replaces Sparta as a Holy Site for Hellenism
- Added some extra events around raiders forming a trade relationship with their potential-victims

###################  
# User Modding  
###################  

# Deprecations  


- GetDummyMale and GetDummyFemale are now deprecated. Modifying them in script is no longer possible. Their use-cases have been replaced with GetGlobalVariable and GetGlobalList. They will be removed completely in 1.5 to ensure script and code that is more maintainable in the long-term.

# Changes  


- Add CloseGameView data function so mods can close specific in game views.
- Add garrison_reinforcement_factor. The param is used for set how fast current garrison size is increasing
- Add GetTraitFromGroup and GetTraitGroupLevel data functions on Character.
- Add GetTraitGroup( 'tag' ) and Trait.GetGroup data functions to get trait groups.
- Add HasTrait and HasTraitFromGroup data functions to Character.
- Add GetGlobalVariable and GetGlobalList data functions for getting data saved from script.
- Add MakeScopeValue, MakescopeFlag, and MakeScopeBool to create scope objects out of primitive types directly since they are not automatically creatable via the MakeScope member on complex types like Character.MakeScope.
- Add ScriptValue data function to scope objects which will evaluate a script value just with that scope object as root.
- Made the Localize data function allow the key it references to also call other data functions in it like SelectLocalization does.
- Add AddList data function for GuiScope, it is to add_to_list what AddScope is to save_scope_as.
- Added data functions GetTraitsWithFlag and GetTraitsWithoutFlag
- Added datamodel GetTraits on TraitGroup
- Added defines NMercenary::REALM_SIZE_MULT and NHolyOrder::REALM_SIZE_MULT
- Added effect deactivate_holy_site
- Added effect remove_dynasty_perk
- Added effect remove_innovation = innovation_key
- Added effect set_army_location
- Added effects clear_traits and copy_traits
- Added effects set_age and change_age
- Added list builder x_culture_global
- Added modifiers army_siege_value_mult, army_damage_mult, army_toughness_mult, army_pursuit_mult, and army_screen_mult
- Added trigger has_innovation_flag
- Added trigger perks_in_<lifestyle>, to query how many perks exist in a given lifestyle (rather than how many a specific character has)
- Building_garrison was renamed to building_max_garrison
- CBs now support the "icon" parameter to have them use a different icon key
- Character interactions now support the "icon" parameter to have them use a different icon key
- Create_betrothal now logs an error rather than silently failing when something's wrong
- Ensured that laws are always stored in database order, so that it is predictable how they will override one another
- Fixed replace_path in mod descriptors having no effect
- Fixed hot-reload for linux
- Make_concubine now supports same-sex concubinage
- Rename garrison param to max_garrison for building configs
- Spawn_army will now only spawn levies if scripted to do so
- The assign_council_task effect now properly errors when the old councillor cannot be fired, rather than just silently doing nothing

###################  
# Bugfixes  
###################  


- Populist factions can no longer usurp a player's primary title if it is their only title of their tier
- Fixed spiritual head succession not always properly applying, leading to the spiritual head of faith passing on to temporal rulers. In rare cases that could lead to the player game-overing on death as a result of having inherited the head of faith title
- Removed occurrence of game over despite having a heir
- Theocratic rulers will keep their government after converting to a faith with the Theocratic doctrine
- The “Return Roma” decision now always return it to the Pope
- Elective heir from Primary title sets only for the title and doesn't affect others. Succession is tied to each title individually, so that changing succession in one doesn't affect other titles.
- Fix a bug when temple holdings get disabled randomly
- Fix an issue where on the MS Store/Gamepass version on some systems the launcher would get stuck during startup and never show up
- Fix random crash/freeze when accessing the military view
- Fixed a rare case where the game would completely freeze
- Fixed AI being able to declare war directly on someone else's vassal
- Fixed an issue that causes unavailable culture innovation can be chosen
- Fixed hiring a holy order charging you piety in cases where the interface tells you it will be free
- Fixed the Straight Medium Beard and Straight Pointy Beard missing from the Barbershop
- Forbid a Scandinavian Adventurer to start a war against someone if they have a Truce with one of their Liege
- Potentially fixed a way you could get booted into observe mode upon succession rather than getting to play as your heir
- Scandinavian Adventurers now receive a loan to ensure they don't start out in debt
- Securing the High Kingdom of the North Sea now requires *you* to hold the relevant kingdom titles, not just any randomer
- Spouses of rulers will now once again wear clothes based on their spouse's culture
- The Make Shieldmaiden interaction now correctly checks for Content and Humble traits.
- Updated the localization to better explain why the "different faith" modifier is applied in the context of a Marriage acceptance
- Lingering Resentment event is not triggered anymore if the kid do not have a crush
- Bubonic plague will now only occur after 1346
- Liege-less children can be recruited
- Fixed eye skinning issue in males and females models
- First of the Crusader Kings achievement is now properly tagged as impossible after the first Crusade started
- Removed the list of Crusade and Jihad participants on the left-hand side of the Declare War window
- Fixed a typo in the Danevirke description
- Remove incorrect Courtier Left message when inviting a courtier
- Fixed a case where your concubine would go to another court due to someone in their close family getting landed
- Character selection list filters player is not get correctly
- Concubines can always be dismissed, even when they are out of the diplomatic range
- Corrected color code used by some icons to match the correct level color code
- Varangian Adventurer will stop having new lovers appearing randomly
- Domestic affairs task do not display the loss of crown authority as a potential negative side effect
- Fixed a typo in the Hunter’s Stable description
- Fixed a typo in Malcolm’s name in the Fate of England bookmark description
- Partners will now be less likely to cheat when they have high opinion
- The rightful liege condition now is verify the whole hierarchy instead just the n+1 title only
- Added additional checks to make sure all needed scopes exists before generating tooltip about funding holy order
- Arabic High Nobility will now use the Scholar's Turban and Caliphs will use the Caliphal Robes
- Corrected a trigger incongruity that stopped Adventure and Pillage dynasty legacies being unlocked by valid non-Norse characters (e.g., Swedes, Estonians, etc.)
- Corrected your opponent's weapon teleporting into your hand if they concentrated hard enough during a bout
- Event wars are now counted for the purposes of raising runestones
- Exiling a character as a nithing now causes them to hate you, not themselves
- Fix console window being invisible on some startups on Linux and macOS (even in debug mode)
- Fixed hiring new courtiers in a holy order always belong to that holy's order faith
- Fixed map flashing on macOS when zooming between the terrain map and the flat map while advanced shader effects were enabled
- Fixed the End of an Era achievement not unlocking; now unlocks a month before the end date
- Fixing the issue with "Promote Culture finished" task not displaying what county was converted.
- Fixed inconsistent month formatting in Simplified Chinese localization
- Gift-Givers legacy now has a tooltip explaining that it makes you more likely to get trade-raid events
- If an unlanded character is used in a Conversion event, they will wear the proper religious clothes
- Landless Scandinavian Adventurers now correctly usurp duchies & may raise conquest runestones
- The 'Spindly' Trait will not make people's limbs too thin anymore
- The AI is now rewarded for fighting well/cunningly in duels even if the player isn't involved
- The control rebate received when winning a Varangian Adventure now has a tooltip
- Upped the likelihood for the Grandmaster of the Jomsvikings to rip their shirt off and come at you for your impiety & assorted faults
- Upped the likelihood of the Jomsvikings to harass anyone who isn't an unreformed Norse pagan
- The Mellow Spirit now applies opinion to parents instead of the liege
- When revoking a title, the acceptance modifier from the military strength is clamped to +20
- Stopped adding a weak hook on top of a weak hook if the expiration date is the same.
- Vassals under the de facto claimed title holder in a war are transferred even if the holder is not the top liege.
- Children cannot fight the Troll anymore, and thus cannot become Wolf/Moose/Lynx/Bear/Wolverine-Slayers
- Armies won’t suffer from the starving penalty when the army is not using supplies
- The Logistician traits now affect supply duration at sea and in friendly territories
- The winter supply modifiers do not subtract bonus from “in friendly territory” anymore
- Tutorial texts have been updated to reflect the map update
- The “I need to know” event will not be spammed anymore when a character has a lot of lovers
- The countdown timer for council tasks are now properly updated
- A Life to Remember refers to the right character’s relationship with the deceased.
- When trying to join a private server, password are not displayed in clear anymore
- La Cerda cadet branch localisation has been repaired
- Participants of a civil war can now all be punished without incurring Tyranny
  * In case of white peace, they can only be imprisoned and their titles revoked
  * In case of them being defeated, they can also be banished or executed
- Avoid a notification spam of Alliance Proposal after reloading a save file
- The Temple tooltip now tells Rulers with a Theocratic Doctrine that they will be leased to the Realm Priest after the construction.



Otherwise, in addition to all the changes already covered in the previous Dev Diaries, here are some highlights:  

Faction behavior  

Whoever said the life of a medieval ruler was only an infinite series of conquests? Maintaining good relations with the key Vassals and the integrity of the realm is an intricate diplomatic dance. Azure introduces changes in the faction behavior to make it more realistic and more impactful on the ruler experience. We look forward to hearing back from you and collecting your feedback on the new behavior! Our intention is to focus the CK3 experience on the complex life of a medieval ruler - full of political dilemmas - beyond painting the map.  

Bug fixing  

You have spoken and we are always listening! Much focus was put on fixing issues reported in the forum, so please continue helping us by posting about bugs and reacting to the ones that matter the most to you, it helps us prioritize them for fixing.  

MP open beta  

We are planning to roll out an updated multiplayer Open Beta on Steam soon after today’s release. The open beta will have the same functionality as Azure but will include network stability improvements that we need your support on testing. You can find more information in the [dedicated open beta subforum](https://forum.paradoxplaza.com/forum/threads/steam-multiplayer-open-beta-1-4-1-updated-for-azure.1478356/). We want to thank you all for your continued support and please keep on sending us your very useful feedback.  

In the coming weeks we’ll continue sharing more details about the Royal Court as it progresses and grows into the graphically rich expansion we are preparing for you.  

Until then enjoy an Azure summer (or winter if you’re in that part of the world) ![:cool:](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Cool    :cool:")  

Cheers!

 

Last edited by a moderator: Jun 8, 2021

<!-- artifact:reactions:start -->
- 146 Like
- 56 Love
- 10 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [pdx_snob](https://forum.paradoxplaza.com/forum/members/pdx_snob.1589970/)**
Role: CK3 Experienced Producer
Badges: 134
Messages: 2
Reaction score: 365

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
