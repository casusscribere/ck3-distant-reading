---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1528613/"
forum_thread_id: 1528613
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 99
title: "CK3 Dev Diary #99: It is time to decide the Fate of Iberia"
dd_date: 2022-05-31
author_handle: pdx_snob
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2724
inline_image_count: 3
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1528613'
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
    location: raw_lines_~28_to_154
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_153
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1964.jpg?1654002295
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_156_to_158
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_426_to_430
    action: preserved_and_flagged
    counts:
      Like: 110
      Love: 33
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_438_to_487
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_488_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1964.jpg?1654002295)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #99: It is time to decide the Fate of Iberia

<!-- artifact:thread_metadata:start -->
- Thread starter [pdx_snob](https://forum.paradoxplaza.com/forum/members/pdx_snob.1589970/)
- Start date [May 31, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-99-it-is-time-to-decide-the-fate-of-iberia.1528613/)
<!-- artifact:thread_metadata:end -->

![event_struggle_hostility.jpg](https://forumcontent.paradoxplaza.com/public/832642/event_struggle_hostility.jpg "event_struggle_hostility.jpg")



Buenos días Crusaders!  

The time has finally come to decide the Fate of Iberia.  

Everything went according to plan since the last diary (phew!), so today we are really excited to release our new Flavor Pack.  

[https://www.youtube.com/embed/w0Av16wx6Y8?wmode=opaque](https://www.youtube.com/embed/w0Av16wx6Y8?wmode=opaque)


In today’s Dev Diary, I’ll be sharing with you the final Release Notes and some news on the release of the last installment of the Royal Edition.  

For a refresher on what has been mentioned about this release so far, check out the past diaries below:  

[CK3 Dev Diary #98: the Castle's foundation](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-98-the-castles-foundation.1527558/unread)  
[CK3 Dev Diary #97: Event Illustration Showcase and Workflow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-97-event-illustration-showcase-and-workflow.1524206/unread)  
[CK3 Dev Diary #96 - Fate of Iberia 3D Art Showcase](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-96-fate-of-iberia-3d-art-showcase.1524239/unread)  
[CK3 Dev Diary #95 - Flavor of Iberia](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-95-flavor-of-iberia.1522983/unread)  
[CK3 Dev Diary #94 - Anatomy of a Struggle](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-94-anatomy-of-a-struggle.1522115/unread)  
[CK3 Dev Diary #93 - Turmoil in the Peninsula](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-93-turmoil-in-the-peninsula.1521199/unread)  

**Release Notes**  

Feeling curious about what’s included in Fate of Iberia? Scroll to your heart’s content through the many pages of Release Notes that we’ve prepared for you:  

Spoiler: CK3 1.6.0 “FATE OF IBERIA” RELEASE NOTES

###################  
# Flavor Pack Features  
###################  

- Added the Iberian Struggle: decide the fate of the peninsula. The Struggle is divided into phases, each opening unique opportunities and leading to different endings. Use the new content (interactions, casus belli and decisions) to dominate the peninsula, or to find a more peaceful alternative.
- Added a new set of iberian artifacts:
  * Chalice of Dona Urraca
  * Santiago aquamanile
Bells of Santiago de Compostela. Upon capture, they are melted down into an aquamanile. Upon recapture, they are melted down. Upon re-recapture, they are melted down. Etc.  


- Visigothic votive crown
- Armillary sphere
- Andalusian aquamanile
- Chessboard for 2 players
- Chessboard for 4 players
- Added new models for the Cities and Castles of Iberia
- Added new models for Christian and Muslim temples in Iberia
- Added a new set of special “buildings” on the map
  * Aljaferia
  * Alhambra
  * Basilica de Santiago
  * Tower of Hercules
  * Rock of Gibraltar
  * Alcázar de Segovia
  * City walls of Toledo
  * Roman walls of Lugo
- New Portrait Assets: added a bunch of new headgear, clothes, hairstyle and beards for both the Muslim and Christian fashion of Iberia
- New unit models for Iberian Heritage cultures.
- New Dynasty legacies
  * The Metropolitan legacy focuses on the development of the Realm’s cities.
  * The Coterie legacy focuses on the collaboration between the members of the House.
- New flavor events drawing on Iberian cultures as well as struggle-specific events
- New Cultural Traditions: State Ransom, Ritualized Friendship, Tabletop Warriors, and Malleable Subjects
- New UI Skin for Iberian Heritage cultures and characters living in the peninsula
- New audio cues when waging war in Iberia and progressing the Struggle.
- New mood tracks have been added for Iberian cultures
- Added a wandering monk with a small dream

###################  
# Free Features  
###################  

- You can now convert to Era Zaharrak when you're an established Basque-cultured sinner in your current faith
- Several faiths can now have the same Head of Faith:
  * Several Islamic faiths now share a Head of Faith at game start, temporal Islamic faiths need to decide on creation which existing caliph they'll submit to (optional for Muhakkima & Zandaqa)
  * Conversos, Mozarabic, Insular and Catholic all have the Pope as their Head of Faith
- Added Rite tenet, allowing theocratic faiths to retain their old Head of Faith on creation if they don't differ too heavily from their mother faith
- Added Mozarabic Christianity as a Rite-faith, sharing their Head of Faith with Catholicism
- Reworked the Found Aragon decision to create Aragonese culture, be more frequent, and allow for slight varieties in Aragonese
- Reworked the Avenge the Battle of Tours decision: it now shifts Aquitaine under the De Jure of Hispania when taken as it’s hard to accomplish.
- Reworked the Form Portugal Decision: it can now be taken during the opportunity phase of the Struggle without being independent.
- Added new special contracts for Clans: Marriage Favor, Jizya, Iqta, and Ghazi
- Added a new faction type: the Dissolution faction will destroy the primary titles of their target, removing a Realm from the map
- Added a new 867 Bookmark for Iberia: play one of the influential vassals and forge the destiny of your dynasty!
- Added a dozen of new emblems for Coat of Arms and new patterns for Iberian cultures
- Added a new field “Face item” for the Barbershop to, well, customize the character’s face

###################  
# Game Balance  
###################  

- Insular Christians now have the Rite tenet rather than the Pastoral Isolation tenet
- Removed blockers to invite close/extended family children from foreign courts (they still have to accept though, most useful for getting wayward children of your own back to court)
- Tribals with a Royal Court are no longer penalized for having too few Servant Amenities when Hunting
- Gave Haesteinn the existing learning lifestyle health buffs & reduced his base health to match the extra health gained, *then* shaved off a little more, hopefully making him a bit less likely to consistently live to over 100
- Characters will now evaluate their friendship with opponent when answering a call to war from an ally
- Martial Custom is once again dictated by Faith if the Royal Court expansion is not enabled.
- All Slavic cultures in 867 now start with a decent degree of mutual cultural acceptance, representing their still being very similar to each other in the earlier bookmark
- Converted Sayyid, Saoshyant, Saoshyant Descendant, & Chakravarti to use the new specific religious opinion modifiers, rather than same-faith opinion
- Historical artifacts no longer iterate through every ruler in the game on start 20+ times, Excalibur(s) can now spawn in a much broader range of Western Europe, simply preferring Arthurian heartlands, Norse paganism can now actually spawn its magical branch artifacts
- Made the March special contract available in the Tribal Era, tied to the Bannus innovation, allowing historical marches to be modeled or emulated
- Increased the overall stats of the Callaberos MAA
- Told Haesteinn to chill about invading kingdoms that cannot possibly outlast his death (looking at you, Viking East Francia), *unless* Vikings are set to Apocalyptic, in which case he'll only attack at least kingdom-tier realms
- You can now benefit from the bonuses of the Salamanca university by being the County holder

###################  
# Game Content  
###################  


- Islamic, Jewish, & Christian Syncretism tenets now allow the syncretising faith to use artifacts from the religion they're syncretizing with at full benefit
- Castille & Leon will now generally eventually be created in 867 starts, unless Asturias successfully integrates Castille completely
- Added Basque Pagan faith, with no counties at game start but able to be brought into favor via decision
  * Also added the Chthonic Redoubts tenet, providing benefits to faiths in mountainous areas.
- Added Hafizi faith to diversify the number of Shias who obey the Ismaili caliph
- Added Purchase Truce interaction, accessible via the Defensive Measures perk or being in a Struggle
- Added a decision for Islamic rulers whose head of faith is not the same faith as them to splinter off into their own caliphate (newly created temporal Sunni and Shia faiths generally have to use this to get their own HoFs)
- Cartagena now spawns rather than Cieza as the city holding for Murcia
- Added Malleable Subjects, Ritualized Friendship and Tabletop Gamers to the Andalusian culture. Malleable Subjects replaces Xenophile.
- Added Ritualized Friendship to the Basque
- Added Ritualized Friendship to the Castillian, and replaced Hit and Run by Tabletop Gamers
- Added Ritualized Friendship to the Catalan
- Added Ritualized Friendship to the Portuguese
- Added Ritualized Friendship and Malleable Subjects to the Visigothic
- Added Ritualized Friendship to the Galician
- Added Ritualized Friendship to the Asturleonese
- Added State Ransoming to the Aragonese, and replaced Wedding Ceremonies with Ritualized Friendship

###################  
# AI  
###################  

- The AI now desires less strength on its side in a war, calling fewer allies if it doesn't have to  
- adjusted involved struggle AI to variously focus less on uninvolved/interloper characters (or more for some aggressive actions) when picking marriage targets, murder/seduction targets, and certain types of war  
- The AI is now further motivated to press claims for its family members  
- The AI is now significantly more inclined to prioritize warring for their De Jure land  
- The AI now more strongly prefers warring for neighboring territories  
- The AI receives an agenda when participating in the Iberian Struggle that will motivate them to take actions tied to the different Catalyst: They will either aim for escalating the struggle, or de-escalating it.  


###################  
# Art  
###################  


- Updated the color of the Seljuk Empire to be closer to Persia
- Updated the color of Majorca to be easier to distinguish from the Umayyad Caliphate
- Updated the color for Asturias (k_asturias and d_asturia)
- 'El Cid' will be more handsome
- King Adelfonso III of Asturias is better looking now
- King Garzia and his wife did a relooking
- The Sultan Muhammad and his wife also went to the hairdresser
- Improved some of the facial animations

###################  
# Interface  
###################  

- The Martial Custom Pillar within the Culture Window is no longer shown if the Royal Court expansion is not enabled.  
- Transformed the "player changed" popup into a feed message  

###################  
# Localization  
###################  


- Adding faith discount tooltip when converting to an involved faith in the Iberian Struggle
- Added various Andalusian cultural names to titles in Iberia
- Dynasty title naming disabled within Iberia to allow for more recognisable (and appropriate) cultures
- Independent Muslim dukes within Iberia will now use (or rather, have used _for_ them) the title of "Taifa" for their realm tier title
- Jazzed up the Christian heaven-hell alternate locs a little
- Removed several niche anachronistic references to smoking

###################  
# Usermodding  
###################  

- Add dynamic modifiers for religious family, religion, and faith opinions.
- Allowed titles to be the head of multiple different faiths
- Enabled to script bookmark characters dynasty or dynasty house to be used in bookmark screen
- Remove bypass requirements from impacting law validity as it would cause issues in succession and other code by applying laws that make no sense.
- Rework custom modifiers in faith’s sins and virtues, now must specify the key of a static modifier instead of trying to read a modifier inline.
- Added a new type of modifier for the buildings: county_dynasty_modifier. You can now check for the county’s holder dynasty perk to unlock modifiers
- Added a new modifier for building to apply them directly on the county holder: county_holder_character_modifier
- Added a bunch of functionality allowing to implement new Struggles

###################  
# Bugfixes  
###################  

- Eased up the triggers for a variety of book topics.
- East Francia in 867 will now mostly split into de jure Bavaria and de jure East Francia on the death of Ludwig II, rather than a tiny Bavaria materializing between two giant slabs of East Francia
- Fixed duplicated price and counter entries for the Lenkas MAA. They should now have the right price and properly relate to archers and pikemen rather than to pikemen and light cavalry.
- Gave a more concrete sense of (Franconian) cultural identity to the single remaining generic German character in the title
- Provinces without forts occupied by allies no longer change color to war leader after several days
- Fixed some historical characters not being bastard founders, leading to strange dynasties/inheritance
- The AI will stop endless loop of hiring / firing court positions
- Vassals joining Populist faction will now properly gain independence
- Fixed a localization bug in Spanish for the Scheme secrecy value
- Fixed a typo causing Christianity & Taoism to look for "adjerents" rather than "adherents"
- Fixed the typo for Sjælland
- Fixed the death icon status for dead characters: they will not be displayed a dying anymore
- Fixed several instances of characters referring to themselves (eg: spymaster revealing secrets about themselves or ruler kneeling in front of themselves)
- The AI can now properly select the Council task “Develop Country” task from the Steward
- The side effects of Manage Royal Guard will be properly triggered now
- Death icons are color-coded again
- Petition Liege now requires at least 1 valid option, that will automatically be selected instead of defaulting on “ask for a Council position”
- Historical Bernards should be where they belong now. We hope.
  * Also axed one _false_ Bernard.
- Several clipping issues for female children haircut have been fixed
- You can now romance your incestuous lover: the tabou penalty is not applied if you are already a lover of the target
- Elvira Jemina now receives a proper holding and will be harder to marry
- The opinion penalty from Warmonger is now properly applied

###################  
# Database  
###################  


- Added historic Kingdom of the Visigoths for tracking assorted old Visigothic kings from before 720 - there's no practical function for this, we just think it's neat
- Added detail to a bunch o'Castilians, exiled a single Castilian to Occitan
- Added Basque culture to two counties on the French side of the Pyrenees
- Renamed the Tigris river to actually be called, eh, Tigris.
- Updated the map in the duchies of Barcelona and Aragon, adding new counties and new baronies to improve the overall level of detail along the Pyrenees.
- Visigothic split now happens before game start, rather than during gameplay
- Added & improved hundreds and hundreds of name equivalencies, chiefly (though not exclusively) within or related to Iberia in some fashion
- Added & updated various historic Portuguese characters, as well as updates for one historic Suebi character
- Added a raft of new Asturleonese characters
- Added new Aragonese characters, moved a handful of mislabelled Aragonese characters to French
- Added or reworked numerous (Iberian) Galician characters
- Added or reworked various Catalan characters, shuffled a few Catalan/Catalan-adjacent characters out to Occitan & French
- Added or reworked various minor historical characters across half a dozen cultures only related to Iberia in a secondary capacity (spouses, parents, concubines, etc.)
- Added pre-scripted Head of Faith title for Muwalladis, available via decision in 867 and for recreation in 1066
- Deprecated titular Duchy of Zaragoza title, made Duchy of Aragon pull double functional duty as both Aragon and Zaragoza, with some shenanigans for changing the current name (this means that the rulers of Zaragoza are now actually regarded as the rightful rulers of... Zaragoza, and the area around it)
- Moved a load of folks who were ruling caste members *over* Andalusians from Andalusian and into Bedouin, Berber (either), Mashriqi, or Yemeni
- Moved an errant Armenian character hiding amidst the Greeks out to Armenian
- Shuffled various characters that got lumped into Bedouin into Yemeni, Mashriqi, and Andalusian
- Shuffled various historical personages out of or into Basque
- Shuffled various misc minor characters out from Berber to Mashriqi, Bedouin, Andalusian, and the _other_ Berber


**Garments of the Holy Roman Empire… for all!**  

You have spoken and we are always listening! We are throwing in a little something alongside this release that we hope you will enjoy.  

Many of you have requested a way to buy the collection of Garments of the Holy Roman Empire, so we have decided to make it available from today to all players for free. This is a collection of outfits for commoners, warriors and rulers of Central Europe, for your full HRE immersion.  

![HRE-chars.jpg](https://forumcontent.paradoxplaza.com/public/832643/HRE-chars.jpg "HRE-chars.jpg")


**Bug Fixing**  

As always, we strive to fix as many of those pesky bugs as possible. Thank you all for helping out by reporting them in the forum and reacting to those that matter the most to you. It does help us prioritize fixing so keep them coming!  

Oh well, it is time to stop reading and start struggling over Iberian territory. I hope you enjoy playing Fate of Iberia as much as we’ve enjoyed creating it.  

Cheers,  


![Mariana_DD_99.jpg](https://forumcontent.paradoxplaza.com/public/832644/Mariana_DD_99.jpg "Mariana_DD_99.jpg")

 

Last edited by a moderator: May 31, 2022

<!-- artifact:reactions:start -->
- 110 Like
- 33 Love
- 6 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [pdx_snob](https://forum.paradoxplaza.com/forum/members/pdx_snob.1589970/)**
Role: CK3 Experienced Producer
Messages: 2
Reaction score: 365
<!-- artifact:op_signature:end -->
