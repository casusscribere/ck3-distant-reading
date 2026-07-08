---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1532585/"
forum_thread_id: 1532585
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 102
title: "CK3 Dev Diary #102: Stabilizing the Iberian peninsula [1.6.1 patch notes]"
dd_date: 2022-06-21
author_handle: Pdx_Meedoc
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1552
inline_image_count: 1
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1532585'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1989.jpg?1655818545
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_151_to_153
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_311_to_314
    action: preserved_and_flagged
    counts:
      Like: 88
      Love: 7
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_322_to_399
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_400_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1989.jpg?1655818545)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #102: Stabilizing the Iberian peninsula [1.6.1 patch notes]

<!-- artifact:thread_metadata:start -->
- Thread starter [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)
- Start date [Jun 21, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-102-stabilizing-the-iberian-peninsula-1-6-1-patch-notes.1532585/)
<!-- artifact:thread_metadata:end -->

Hello there,  

We are wrapping up our work on Fate of Iberia as the summer break is on the horizon. We are releasing Update 1.6.1 today, which will notably contain:  


- [The content we revealed two weeks ago](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-100-a-royal-journey.1530040/)
- Tweaks to the Dissolution faction and a new set of game rules to tweak it for the Al-Andalus. You can now decide to either:
  * Activate it from the start
  * Block it until the death of the starting Caliph
  * Block it until 1020


![1655813767894.png](https://forumcontent.paradoxplaza.com/public/839795/1655813767894.png "1655813767894.png")



The full update notes are available at the end of this post. You can scroll through if you are impatient.  

I wanted to seize the opportunity to thank you for your feedback on Fate of Iberia. We learned a lot through reading your threads and comments on our forum, as well as the discussions had on other platforms. We also enjoyed the funny anecdotes and were (happily) surprised by your love for cheese and the other stories you shared.  

Most of all, your comments and feedback regarding the Struggle itself have been invaluable and will continue to help us in the future. If you have any grievances, or wishes regarding the system, please discuss them on our forum! While we are not always able to respond directly, we do keep a keen eye on what is being discussed!  

Cheers,  

P.S.: A crash was identified recently, which we were unfortunately not able to resolve in this update. We are however working on a resolution for this issue, which we will release as soon as possible.  

The crash occurs if you let a Court Event sit in your Royal Court unanswered, meaning the game will crash when the event would time out.  
This can be worked-around by answering your Court Events before they time out.  

Spoiler: 1.6.1 Changelog

###################  
# Expansion Features  
###################  


- Additional events about Conversos, Sephardic Jews, and other religious themes for owners of Fate of Iberia

###################  
# Free Features  
###################  


- West African pagans now have an alternative path to feudalism, allowing them to obtain it by building successful kingdoms rather than requiring faith reformations
- New content related to the Canary Islands
  * The Guanche Culture has been added
  * Found the Kingdom of Canarias Decision
  * A new Megalith Tenet
  * A new Pagan Faith: Achamanism
- New game rule to control the fall of the Umayyads. You can choose between:
  * From game start
  * Only after the death of the initial Caliph
  * Only after 1020
- Added more Andalusian Arabic names to the database

###################  
# Game Balance  
###################  


- Hostility ending conditions were modified. You can now either own 2 kingdoms or unite the Spanish Thrones. Moreover, uniting the spanish thrones lower the conversion of counties to 75% instead of 100%
- Added Prestige to the King of Asturia in 867 to avoid starting with -600 prestige
- Adjusted the weight gain from Feasts
- Lowered the cooldown between 2 games of chess from 5 to 1 year
- Readjusted education tier threshold to make the level 4 more likely to happen while still being rare
- Improved the balancing of the Dissolution faction
- Blocked the demands from Claimant if the Realm is managing Civil Wars which could lead to a loss of territory
- Târgoviste is now the de-jure capital of Wallachia
- Galician now uses Monastic Communities instead of Agrarian
- The Struggle Clash CB now has a cost after the Struggle ended
- Adjusted the reward for Secure the Mediterranean
- Adjusted the chance for the poetry to be lauded / mocked in order to improve with your Diplomacy instead of worsening
- The Sephardi culture is now Involved in the Struggle
- Refined the odds and cooldown for the new events


###################  
# AI  
###################  


- They will wage holy wars again
- Added a blocker for the AI to not give away their relics
##################  
# ART  
##################  


- Visual updates for some legacy clothing, armor and headgear assets. This should not cause any issues except for potentially some assets that were renamed.
- For hairstyles and beards, we switched from using separate meshes/entities for hat combinations to using blend shapes now defined in the .asset file of the hairstyle/beard.
  * Removed the additional pdxmeshes and entities from each asset file so that there is only the base mesh and entity there.
  * Added all of the different blend shapes to that entity. For many of the older assets this means we re-exported the mesh variants as blend shapes instead of entirely separate meshes.
  * Removed unneeded mesh files from the game folders.
  * Removed the scripted reference to hairstyle and beard variants from each asset in the "accessories" script.
- All headgear should now set its appropriate tag to be used to deform hairstyles and beards with the corresponding blend shape. The tags are crown, cap, hat, helmet, hood, chinstrap.
- Additionally, some headgears add a secondary tag to reduce clipping in certain combinations. These are snug_headgear, nose_guard, hood_beard and mask_hat (added to headgear which can be used together with the Disfigured mask).

###################  
# Bugfixes  
###################  

- Fixed crash when hovering unavailable court amenity upgrades in Tribal Court
- Restored the missing assets from Northern Lords in the Barbershop
- Reduced crippling empathy in characters receiving stress when their dying rival/nemesis has ANY ritual best friend anywhere
- Fixed a bug when University (and all special buildings) doesn't apply county holder character modifiers (county_holder_character_modifier)
- Reviving Adoptionism now grants you the heresiarch trait
- Fixed some map names being displaced
- Adjusted the culture of the two Visigothic characters that snuck back in after Visigothic was removed
- Regnal numbers will no longer appear after the first *word* in a first name, instead appearing after the entire first name
- Conquest CB now provides more feedback about it's requirements during the struggle
- Added de jure kingdom splitting logic for edge case where there are kings which don't hold their capital duchy
- Fixed Map Mode in struggle interface not being localized
- There is a proper feedback if you don't have enough money to wage in a board game
- Rite tenet now actually reduces hostility with same-HoF faiths to Astray, instead of leaving you hopelessly enamored of a Head of Faith who still says you're a heretic
- Fixed Portugal going to Hispania when created after Compromise
- Fixed edge cases where empires were created for competing kings, due to order of kingdom creation
- Improved script logic of Status Quo de jure transfers and title creation
- Elvira Jimena is definitely unlanded now
- Removed the remains of debug option in the “By Another Man” event
- You can now choose to banish El Cid even if he becomes your vassal. Doing so will make you a tyrant and may lead to becoming rivals or worse with El Cid.
- The Secret to Freedom is now more likely to trigger. Prisoners may earn stress if they are the kind that does not usually reveal secrets.
- Fixed a bug which caused tall characters to float over MENA and Indian thrones
- You can now challenge someone to chess, even if they have an active event they need to answer to.
- The break truce catalyst now works against Count as well
- Demanding payment works against any involved Ruler (or any other use of a hook)
- Titles which will be destroyed by the Dissolution Faction are properly displayed
- We now keep the chosen education traits for custom children rulers
- An indecent event has been blocked against children
- All non-muslim iberian culture uses the Mediterranean Court Room now instead of fallbacking on the Indian Court Room
- Added a cooldown to "invite to activity" to avoid spamming and weird edge cases
- Removed redundant option in fp2_struggle.2050 if el cid is your vassal
- Displays the activity cost in the interaction window for "Invite to Activity"
- Properly displays the icon and related description for the Share Secret interaction
- Split the Involvement and Phase conditions for the Ending Decision into two to avoid being involved as an implicit condition
- Only trigger the development gain for city holdings for the Prestigious Development Perk
- Lubb Musa is now properly described as having a clan government in the bookmark screen
- Holy order are properly ignored for Struggle Ending Decisions
- Iberian Foothold is available when owning the land for 15 years or more, not only for 15 years only
- Fixed issue where betting land causes the county to get permanently set as "in wager"
- Enforce Truce can properly be enforced post-Struggle
- Bells of Santiago is now active for Iberian cultures once the Struggle ends
- The new Dynasty track stays available after ending the struggle for Dynast living in Iberia or with an Iberian Heritage culture.
- Fixed some clipping issues
- Fixed a localization error in the tooltip of the hybridization cost
- Fixed an error in an option’s tooltip for the Meet Peers event “Playing House”
- Fixe Out of Syncs due to players having different languages
- The Iberian sword will be held properly and without its stand during duels
- History’s best friends is now only triggered when seducing / romancing your best friend
- Children cannot become Thief-Slayers anymore: they are forbidden from dueling
- Adjusted the margin in the character window to allow hovering over and lock tooltips
- Fixed connectivity issues between counties
- The missing name "Ató" (for occitan0066) is now in the list of names
- Lots of localization fixes in the different languages

<!-- artifact:reactions:start -->
- 88 Like
- 7 Love
- 7 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)**
Role: Corporal
Badges: 19
Messages: 39
Reaction score: 2,254

*[Full game-badge icon list of 19 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
