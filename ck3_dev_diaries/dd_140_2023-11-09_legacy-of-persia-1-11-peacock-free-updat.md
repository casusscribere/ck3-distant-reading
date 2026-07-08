---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1606790/"
forum_thread_id: 1606790
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 140
title: "Dev Diary #140 - Legacy of Persia & 1.11 'Peacock' Free Update"
dd_date: 2023-11-09
author_handle: Trin Tragula
expansion: Legacy of Persia
patch: Patch 1.11
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3587
inline_image_count: 10
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1606790'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2672.jpg?1699303541
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_475_to_478
    action: preserved_and_flagged
    counts:
      Like: 70
      Love: 42
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_486_to_594
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_595_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2672.jpg?1699303541)
<!-- artifact:thread_banner:end -->

# Dev Diary #140 - Legacy of Persia & 1.11 'Peacock' Free Update

<!-- artifact:thread_metadata:start -->
- Thread starter [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)
- Start date [Nov 9, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-140-legacy-of-persia-1-11-peacock-free-update.1606790/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to this last development diary for Legacy of Persia!  

With the release drawing near, what I have to share today, apart from general excitement, is the list of upcoming achievements and the update notes for 1.11 ‘Peacock’! As with previous achievements our aim has been to have a good mix of achievements with a focus on new features, the new struggle and the focus region of the flavor pack itself.  


---

### Legacy of Persia Achievements​


### Easy Achievements​

#### Rich in Diversity​

![rich_in_diversity.jpg](https://forumcontent.paradoxplaza.com/public/1033644/rich_in_diversity.jpg "rich_in_diversity.jpg")


*As a character of a faith with the Jizya or Tax Nonbelievers doctrines, have ten vassals of other faiths.*  

#### Abbasid Might​

![abbasid_might.jpg](https://forumcontent.paradoxplaza.com/public/1033645/abbasid_might.jpg "abbasid_might.jpg")


*Take the Renewed Caliphate ending in the Iranian Intermezzo Struggle.*  

#### Royal Flush​

![royal_flush.jpg](https://forumcontent.paradoxplaza.com/public/1033646/royal_flush.jpg "royal_flush.jpg")


*As a character of a faith with the Fedayeen doctrine, dispose of a lowborn, a king, and an emperor.*  


### Hard Achievements​

#### Iranian Revival​

![iranian_revival.jpg](https://forumcontent.paradoxplaza.com/public/1033647/iranian_revival.jpg "iranian_revival.jpg")


*Take the Iranian Resurgence ending in the Iranian Intermezzo Struggle.*  

#### All Your Caliphate Are Belong To Us​

![caliphate_are_belong_to_us.jpg](https://forumcontent.paradoxplaza.com/public/1033648/caliphate_are_belong_to_us.jpg "caliphate_are_belong_to_us.jpg")


*Take the Dominate the Caliph foundation as part of the Abbasid Humiliation ending in the Iranian Intermezzo Struggle.*  

#### Shia Reborn​

![shia_reborn.jpg](https://forumcontent.paradoxplaza.com/public/1033649/shia_reborn.jpg "shia_reborn.jpg")


*Take the 'Found a New Caliphate' foundation as part of the Abbasid Humiliation ending in the Iranian Intermezzo Struggle.*  

#### Mulct Them Dry​

![mulct_them_dry.jpg](https://forumcontent.paradoxplaza.com/public/1033650/mulct_them_dry.jpg "mulct_them_dry.jpg")


*Loot four Illustrious-tier Vizier Extravagance modifiers from your Vizier.*  

#### Fiscal Responsibility​

![fiscal_responsibility.jpg](https://forumcontent.paradoxplaza.com/public/1033651/fiscal_responsibility.jpg "fiscal_responsibility.jpg")


*Fill five Tax Collector slots with excellent aptitude characters.*  


### Very Hard​

#### The Umayyad Strikes Back​

![umayyad_strikes_back.jpg](https://forumcontent.paradoxplaza.com/public/1033652/umayyad_strikes_back.jpg "umayyad_strikes_back.jpg")


*Starting as a member of the Umayyad dynasty, hold the Empire of Arabia and the Sunni Caliphate.*  

#### Darius Revenge​

![darius_revenge.jpg](https://forumcontent.paradoxplaza.com/public/1033653/darius_revenge.jpg "darius_revenge.jpg")


*As a character of Iranian heritage, hold the Empire of Persia, Kingdom of Thessalonika, and Kingdom of Hellas.*  


---


### 1.11 Peacock Changelog​

### Legacy of Persia Features​

- Added the Iranian Intermezzo Struggle covering the conflict in Iran between the Caliphate and resurgent Iranian dynasties. The struggle can be ended by fulfilling one of three decisions or by triggering the “Concession” ending phase. During the struggle supporters and detractors of the Caliph will have access to new rules, decisions, interactions and events.
- Added a new Dynasty Legacy: Brilliance, focusing on reclaiming the glory of the old dynasties of Persia.
- Added a new UI Skin for Iranian Heritage cultures and characters living in the region.
- New Portrait Assets: added new hairstyles, clothes, and beards in the Greater Iranian region.
- Added many new events, decisions and interactions when playing in the Greater Iranian area relating to the new Struggle, Zoroastrianism, Islam, Clan realms, characters traveling in the Iranian Region, Tax Collectors, and more.
- Added a number of new Cultural Traditions to Iranian culture: Fierce Independence, Pragmatic Creed, Jirga, Enlightened Magnates, Beacon of Learning, Irrigation Experts, and Frontier Warriors.
- Added new types of Men at Arms: Asawira (unlocks within the Brilliance dynasty legacy), Tarkhan (unlocks from Frontier Warriors), Zupin (unlocks from Pragmatic Creed), and Tawashi (unlocks from Fierce Independence).
- Added two Extra Tax Decrees when playing inside the Iranian region. Dehqan and Maguh. For more about tax decrees see Clan Vassals under Free Features.
- Added a new Court Scholar court position for cultures with the Beacon of Learning cultural tradition. When employed, court scholars will over time increase in skill and good or excellent Court Scholars can be sponsored to create a Research Project inspiration, resulting in new innovations for your culture or new modifiers for your clan. Court Scholars also have an increased chance of gaining the book or alchemy inspirations.
- Added a new Master Assassin court position which boosts murder schemes. Rulers with a faith that belongs to a faith with the Fedayeen tenet can recruit Master Assassins.
- Added 3 new struggle music tracks as well as 3 new Persian Region Mood Tracks.

### Free Features​

- Added a new bookmark page for Iran in 867, with recommended playable characters and biographies.
- House Unity is a new measure of the internal stability in the ruling house of a Clan realm. Unity comes in 5 levels, from Antagonistic to Harmonious and is shaped by the actions taken by clan members towards each other. Clans with high unity levels will enjoy a high level of internal stability while making conquest harder while those with a low unity level will be better at conquering new lands but be internally unstable. Each level unlocks special rules, decisions, interactions and abilities.
- Clan Vassals can now be assigned to Tax Jurisdictions, handled by a Tax Collector. Depending on the aptitude of the Tax Collector and what Tax Decree is assigned to the Jurisdiction the associated Vassals will provide and enjoy different benefits and penalties. The existing Vassal obligations, Ghazi, Iqta and Jizya, are now Tax Decrees in the new system.
- Viziers: Clan realms of duchy tier or above can now assign a landless character to be their Vizier. Viziers provide extra tax jurisdictions and their aptitude helps all tax collectors in the realm. The more empowered they are the bigger the benefits, though Viziers may also try to embezzle your funds. Vizier excesses can be fined via the Mulct interaction. A Vizier can also substitute your spouse in the confidant counselor position, if you desire.
- When starting in 867 the Turkic Seljuk dynasty will now invade Iran in the late 10th century, an associated game rule can regulate when the invasion happens.
- Added event chain for the Zanj Rebellion in lower Mesopotamia shortly after the start of the 867 campaign.
- Added a number of new special buildings in the Iranian region: The Minaret of Jam, the Walls of Gorgan, Alamut Castle, Falak-ol-Aflak Citadel, the Dome of Soltaniyeh, The Rainbow Mountains, the Imam Reza Shrine, the Sar-i Sang mines, the Ark of Bukhara, the Tomb of Batsheba, and Maharloo Lake Necropolis of Rostam, Tomb of Cyrus the Great, Palace of Ctesiphon, and the ancient Mines of Sar-i Sang.


### Balance​

- Cost for disinheriting bastard children or children with disputed heritage is lowered. If the illegitimacy is a secret and the father knows the secret, the cost is lowered and the secret is revealed.
- Certain Wars will now resolve quicker, as the warscore from battles and attacker occupations have been increased by 150%: conquests (county & duchy), holy war (county & duchy), subjugation, vassalization, struggle clash, border raid, expel interloper, and excommunication war.
- Conquest & Invasion CBs now have a dynamic cost scaling with realm size, this should make the CB's cheaper for smaller realms and more expensive for very large ones.
- Chthonic Redoubts are no longer impossible to convert in Mountains (-75% instead of -100%).
- De Jure CBs are now available one era earlier than before.
- Forming the HRE is now possible using any core Carolingian kingdom, not just East Francia, and the De Jure can now include the Empire of Francia if West Francia or enough Francian kingdoms are part of the realm of the one forming the HRE.
- Rebalanced the Piety & Prestige costs for Conquests and Invasions to make them more accessible for smaller realms.
- Reduced prestige gain from Amenities and exceeding your Grandeur level.
- Reduced prestige gain from the Marauder Accolade.
- Removed all sources of prestige % gain bonus from innovations to reduce inflation (total 20%).
- Significantly reduced Prestige gain from Artifacts (monthly gains, prestige per dread/knight, etc).
- Slightly reduced prestige % bonuses from Diplomacy lifestyle perks.
- Slightly reduced prestige from the Bodyguard position.
- Switched some innovations around for Arabic Heritage cultures so that the Caliph can revoke titles on game start.
- The AI should now have a much easier time forming the HRE from an 867 start.
- The AI no longer pays Prestige to revoke Court Positions, as they would never abuse court positions in the first place - and the prestige loss would cause them to fairly often be unable to declare wars.
- The Mongols now get better Siege Engineer characters.
- The Mongols now have a bonus to cavalry damage and toughness, to offset their lack of Stationing Bonuses.
- The Mongols now spawn with trebuchets instead of mangonels.
- Harm events will no longer target the player by default, only the AI.
- Increased the odds of successfully getting through harm events unscathed from 80:20/50:50/60:40 for poor/average/good options to 40:60/60:40/70:30.
- Reduced the overall likelihood of harm events of all kinds by an order of magnitude (except for the general incapability due to age chainlet), and of incapability foreboding events specifically by a further half again.
- Camel cavalry accolade only gives bonuses to camel cavalry.
- The Create Cadet Branch is now available for Clan Members only if they are in another realm than their House Head.
- Some common activity pulse actions now grant mystic lifestyle experience for pilgrimages and witch rites.
- If you have an epiphany about the sanctity of nature during a hunt you will also get some mystic lifestyle experience (this is another activity pulse action, though somewhat rarer than the very common one for pilgrimages).
- You will get Mystic Lifestyle experience for visiting points of interest in religious sites and wonders while traveling. This is not restricted to religious sites of your own religion, and it also means it's easier to get mystic XP once more grand cathedrals are built up later in the game.
- Added Mystic Lifestyle experience to some events, mainly travel ones that already had to do with mystics.
- Holding a mystical communion will grant some mystic xp.


### AI​

- Lowered the value of higher tier alliances and increased the penalty for Female above 30 years.

### Interface​

- Character modifiers can be now clicked and display an expanded view of all existing modifiers. Players can now see all modifiers on the character, and not only the first 10 items.
- Show a difficulty warning in the lobby for rulers in regency.
- Remove decision_custom_widget_container option from decision configuration window.
- Remove decision_has_second_step for decisions. Now if a decision needs to use the custom step, the decision must specify decision_to_second_step_button.
- The MaA stats shown in their tooltip in the military view now properly adds bonuses from being stationed, like they already do in the separate MaA window.
- Added steam rich presence for Iberian Struggle.
- Added steam rich presence for Persian Struggle.
- Clan Rulers now display their house crest instead of their main title coat of arms in the bookmark screen.
- Significantly reduced the amount of suggestions for hostages.


### Art​

- Added Managed Forest to the Barbershop backgrounds.
- Added Coat of Arms: 26 new coats of arms, between muslim and Iranian imagery and writing.
- Added 6 Event backgrounds (Bathhouse, Cave, Zoroastrian Temple, Iranian Courtyard, Iranian Docks and Iranian Throneroom).
- Added 3 Male Iranian Nobility Clothes (with low and high nobility variations).
- Added 3 Female Iranian Nobility Clothes (with low and high nobility variations).
- Added 1 Iranian Armor (male and female).
- Added 1 Iranian War Helmet (male and female).
- Added 2 Turkic-heritage headgear (Count and Duke level, male).
- Added 8 Iranian-Heritage headgear (Count, Duke, King and Emperor levels, both male and female).
- Added Disfigured Mask for Iranian and Turkic characters.
- Added 3 Iranian Beard Styles.
- Added 6 Iranian Hairstyles (3 male and 3 female).
- Added 8 patterns for Iranian clothes (with 8 trim variations).
- Added new Iranian Military Unit Models (3 levels).
- Added Iranian-Heritage holding 3D Meshes and Illustrations (Castles and Cities).
- Added Zoroastrian holding 3D Meshes and Illustrations (Temples).
- Added unique art for 6 Court artifacts (Sassanian Sword, Peacock Throne, Oxus Bracelet, Turkic Casket, Achaemenid Drinking Vessel, Incense Burner Cat Sculpture).
- Added 14 new Special Building Meshes (Minaret of Jam, Alamut Castle, Ark of Bukhara, Falak-ol-Aflak Citadel, Great Mosque of Samarra, Great Wall of Gorgan, House of Wisdom, Imam-Reza Shrine, Maharloo Lake, Mount Damavand, Palace of Ctesiphon, Rainbow Mountain, Soltaniyeh, Tomb of Cyrus).
- Trait Icons for Extolled by House, Accused of Decadence, Supporter and Detractor of the Caliphate.
- Added 6 Men-at-Arms icons and illustrations (Asawira, Mubarizun, Tarkhan, Tawashi, Zupin Spearmen, Ayyar).
- Added 11 Decision (and Story Event) Illustrations.
- Added New Loading Screen.
- Added 5 Icons for House Unity levels.
- Added Iranian Skin for the HUD.
- Added 8 Tax Decree Icons.
- Added Tax Collection alerts and icons.
- Added 2 Religious Tenet Illustrations (Communal Possessions and Fedayeen).
- Added 7 Cultural Tradition Illustrations (Frontier Warriors, Jirga, Beacon of Learning, Pragmatic Creed, Fierce Independence, Garden Architects, Irrigation Experts).
- Added Legacy Track Illustration (Brilliance).
- Art Script: Split up the portrait modifiers to different files with groups based on priority. Higher priority value means it will override any modifiers with lower priority. This way we don't have to weigh everything against everything else; instead, we can know with certainty that armors, for example, will always override regular clothes. Scripted characters are now found in the priority just above base modifiers, with priority 2.
- Art Script: Changed the old way of assigning accessories to scripted characters. Instead of per-accessory we now do per-character. So, each character has a single entry in a single file where all their accessories are added. This goes for developer characters as well.
- Fixed an issue where many western women wouldn't wear any headgear after the year 1300.
- For players with Northern Lords, those cloaks will now be used by more culture groups than just the Norse.
- Fixed certain millennials refusing to wear anything but filthy rags.
- Enforce Divorce interaction now has an icon.


### Audio​

- 3 new struggle music tracks.
- 3 new Persian region mood tracks.
- 1 new declare war music track for the Struggle.
- 2 new struggle ending effects for positive and negative outcomes.
- 3 new special building sound effects for the Persian special buildings.
- 2 new bookmark sound effects for the involved Struggle characters.

### Localization​

- Fixed Dutch patronymic surnames not being possessive for daughters.
- Fixed broken localization in some Right-Hand Man feed messages.
- Added localization when Influence Ward's Personality interaction is blocked by the Ward having too many traits already.
- Fixed missing text when accused of violating sumptuary law by your liege.
- Fixed row break issue for Simplified Chinese letter event.
- Various other minor localization fixes.


### Game Content​

- Added a new set of unique succession laws for Clan, activated by the Unity level.
- Jizya is now a Special Doctrine for most of the Islamic faith except: Alhomadism, Druze, Alevism, Alawite and Qarmatians. The former tenet still exists for custom faiths.
- Ashari now has Legalism instead of Jizya.
- Ismailism now has Mendicant Preachers instead of Jizya.
- Muladism now has Communal Identity instead of Jizya.
- Maturidi now has Legalism instead of Literalism and Adaptive instead of Struggle and Submission.
- Adjusted for community feedback about Life in Color event background, plus adjusted text to compensate.
- Added mother/father and bastard variations for child born memories.


### User Modding​

- Add on_action when realm capital is changed.
- Smug Kid is now judging you .
- Enable ignoring interaction recipient cooldowns.
- Added set_house_head effect.
- Added on_building_cancelled effect to the province on actions when construction of a building in the province is canceled.
- Added on_building_started effect to the province on actions when construction of a building begins in the province.
- Added on_canceled effect to building types to execute when construction of a building type is canceled.
- Added on_start effect to building types to execute when construction of a building type starts.
- Added paying character to building effect and on_actions.
- Renamed 'ai_war_chest' to 'war_chest_gold' for consistency.
- Renamed 'war_chest_gold', 'war_chest_prestige', 'war_chest_gold' to 'ghw_'+previous name for consistency.
- Inline values in comparison triggers using = only are now not valid, this is to prevent syntax ambiguity between a scope comparison and a scope change. You must use == for an inline comparison to be explicit.
- Added set_character_secret_faith to set a secret faith on a character.
- Added remove_character_secret_faith to remove the secret faith on a character.
- Added a simpler has_any_artifact_claim trigger and set it to be used by the artifact_war cb to lessen its performance impact.
- Changed bookmark field from default = yes/no to weight = scriptablevalue, used to determine default bookmark.


### Databases​

- Updated databases for landholders throughout Iran, ensuring that there are more historical characters to play as, and that all rulers have a suitable amount of vassals on start.
- Updated the 867 start date to better reflect the ongoing conflicts as part of implementing the Iranian Intermezzo struggle.
- Updated the cultural and faith setup of the Greater Iranian region, including adding the new Brahui culture.
- Armenian rulers in 867 and 1066 now start religiously protected, to avoid their faith disappearing much too quickly every game.
- Added Nestorian community to Suyab in Zhetysu in 867, representing their metropolitan see.
- Made the Karenids a cadet house of the ancient Arsacids, from which they descend.
- Merged Abbasids back into the Hashimid dynasty.
- Nizam al-Mulk now starts as Alp Arslan's vizier, and the two have a good working relationship.
- Made Upper/Lower Lotharingia the default duchy titles, with Lorraine a French variant, and added Krain as a German variant of Kranj.
- Added the Sayyid trait to some characters from the Hammudid house who were missing it.


### Bug Fixes​

- Temporal, for life doctrine does not allow for the unlimited firing of court chaplains anymore. Except for the first time after starting the game. That one is a freebee. Under the Temporal Clerical Appointment doctrine, the Realm Priest or Court Chaplain seat will not get auto-filled the moment the previous holder dies.
- Event Extracurricular Learning shall never clone or lose a herbalist
- Fixed an Out of Sync that can happen when joining a game where a character who was involved in a struggle has become the leader of a mercenary group.
- Fixed a crash related to expanding weight and prisoner modifiers.
- Fixed toast messages sometimes not showing up.
- Made sure Tournament environment backgrounds show up as they should (jungle was unused).
- You can no longer demand the conversion of someone you're at war with.
- Added missing nickname desc for "the Crownless", which an unnamed cheese-loving designer hid in a secret file away from the rest of the nicknames.
- Changed Tocharian color to differentiate them from the surrounding heritages a bit.
- Unlocked a load of struggle parameters that were previously hardlocked to the Iberian struggle in script, making them a bit more mod-friendly.
- Added a temporary fortification when trying to depose a Diarch with no fort level.
- County modifiers were never recalculated when a struggle ends, so they could keep positive or negative modifiers for a long time after the struggle has completed.
- Denouncing a dynasty member will now always apply the associated trait correctly.
- Fixed war declared overview window pausing observer mode.
- Fixed all instances of incorrect max level of aptitude.
- Fixed an issue where modifiers from vassal contracts were not fully applied correctly.
- Fixed the AI never considering giving gifts to a bankrupt liege in the Send Gift interaction.
- Fixed the filter window in the character list of the struggle involvement window not being clickable if it was sticking out of the main involvement window.
- Hostages will no longer appear as someone you can marry when using Find Spouse interaction.
- The Disrespected Elders modifier from getting yelled at by an old man during Meet Peers activity will now disappear much sooner.
- Adds clarifying text to Succession Law selection window explaining that special title succession laws always take precedence over realm succession laws.
- Children will no longer gain more than 1 childhood trait after turning 3 years old or when generated through templates.
- Fixed any ruler who had their capital as Mecca gaining the Hajjaj trait, instead of only Muslim rulers.
- Fixed incorrect values and loc in Invite to Activity rank difference modifiers.
- Invasion wars will highlight the correct counties in war overview.
- Invasion wars will highlight the correct counties that the attacker is going to win when victorious
- Temporary bride and groom modifiers are now removed if the Wedding is invalidated before completion.
- Reduced amount of AI wearing glasses.
- Fixed Educate Child message not containing any text.
- Fixed all cases where playable starting ruler's governments did not match their holding type.
- Fixed issues with avalanche in county letter event.
- Fixed it being possible to request wards or guardians from other courts if another is already traveling to the target.
- Fixed missing loc for hostile scheme reluctance modifier for own Head of Faith.
- Fixed stated kinswoman/man relations between lowborns with no shared family.
- Fixed traveling wards, guardians, and hostages who were invalidated not returning home.
- Mades some decision titles more stylistically consistent.
- Not returning a hostage upon reaching adulthood will now reduce your Prestige income from hostages, and the chance of other ruler's sending child hostages to you, for 10 years.
- Ensure random_list weights cannot get negative weights.
- Court event "Basileusophile" no longer displays an unlocalized line in the purple undergarment creation option.
- Fixed unavailable option tooltip in Under the Weather travel event.
- Ghazi Status CB piety reduction now only applies to holy wars.
- Removed a minor character from Austria, as their associated barony does not exist.
- Fixed an issue where calling a baron to an offensive war would deduct 700+ prestige.
- Infants will no longer get Wet Nurse events about child development.
- Incapable Clan Vassals will no longer demand your children.

<!-- artifact:reactions:start -->
- 70 Like
- 42 Love
- 5 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)**
Role: Game Designer - Crusader Kings 3
Badges: 36
Reaction score: 16,644

*[Full game-badge icon list of 48 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
