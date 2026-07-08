---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1413269/"
forum_thread_id: 1413269
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 39
title: "Crusader Kings 3 Dev Diary #39 - Achievements Showcase"
dd_date: 2020-08-25
author_handle: Wokeg
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1613
inline_image_count: 56
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1413269'
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
    location: raw_lines_~28_to_142
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_141
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1441.jpg?1598358742
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_144_to_146
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_355_to_360
    action: preserved_and_flagged
    counts:
      Like: 120
      Love: 50
      (unlabeled — rendered as base64 data URI): 4
      Haha: 6
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_368_to_436
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_437_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1441.jpg?1598358742)
<!-- artifact:thread_banner:end -->

# Crusader Kings 3 Dev Diary #39 - Achievements Showcase

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Aug 25, 2020](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-39-achievements-showcase.1413269/)
<!-- artifact:thread_metadata:end -->

Greetings, dear friends, and welcome to the final pre-release dev diary! Today, we’ll be doing something nice and light, since we know you’re all hyped for the release next month, and couldn’t possibly stand the tension otherwise.  

So, with that in mind, let’s have a look at what achievements you can get, and the ways of getting them. As we’re so close to release, we’ll be taking a gander at the full list!  

… With apologies in advance for the puns. -_- They forced me to implement them.  

![a_house_of_my_own_achievement.png](https://forumcontent.paradoxplaza.com/public/600461/a_house_of_my_own_achievement.png "a_house_of_my_own_achievement.png")

![a_legacy_to_last_the_ages_achievement.png](https://forumcontent.paradoxplaza.com/public/600462/a_legacy_to_last_the_ages_achievement.png "a_legacy_to_last_the_ages_achievement.png")

![a_name_known_throughout_the_world_achievement.png](https://forumcontent.paradoxplaza.com/public/600463/a_name_known_throughout_the_world_achievement.png "a_name_known_throughout_the_world_achievement.png")

![a_perfect_circle_achievement.png](https://forumcontent.paradoxplaza.com/public/600464/a_perfect_circle_achievement.png "a_perfect_circle_achievement.png")

![above_god_achievement.png](https://forumcontent.paradoxplaza.com/public/600465/above_god_achievement.png "above_god_achievement.png")

![al_andalus_achievement.png](https://forumcontent.paradoxplaza.com/public/600466/al_andalus_achievement.png "al_andalus_achievement.png")


1. A House of my Own: create a cadet branch of your dynasty.
2. A Legacy to Last the Ages: complete an entire dynasty legacy path.
3. A Name Known Throughout the World: have your dynasty reach the highest possible level of renown.
4. A Perfect Circle: have only two distinct parents, grandparents, and great grandparents, counting absent ancestors as individual characters.
5. Above God: have a strong hook on your head of faith.
6. Al-Andalus: starting as an Iberian Muslim, control all of Iberia and take the Avenge the Battle of Tours decision.


![almost_there_achievement.png](https://forumcontent.paradoxplaza.com/public/600467/almost_there_achievement.png "almost_there_achievement.png")

![an_unfortunate_accident_achievement.png](https://forumcontent.paradoxplaza.com/public/600468/an_unfortunate_accident_achievement.png "an_unfortunate_accident_achievement.png")

![bad_blood_achievement.png](https://forumcontent.paradoxplaza.com/public/600469/bad_blood_achievement.png "bad_blood_achievement.png")

![beacon_of_progress_achievement.png](https://forumcontent.paradoxplaza.com/public/600470/beacon_of_progress_achievement.png "beacon_of_progress_achievement.png")

![blood_eagle_achievement.png](https://forumcontent.paradoxplaza.com/public/600471/blood_eagle_achievement.png "blood_eagle_achievement.png")

![carolingian_consolidation_achievement.png](https://forumcontent.paradoxplaza.com/public/600472/carolingian_consolidation_achievement.png "carolingian_consolidation_achievement.png")


1. Álmost There: as Álmos Árpád, form Hungary & convert to Christianity.
2. An Unfortunate Accident: inherit a title from someone via murder.
3. Bad Blood: go to war with one of your siblings over a claim.
4. Beacon of Progress: have your culture unlock all innovations, excluding regional and culture-specific innovations.
5. Blood Eagle: starting as any child of Ragnarr Lothbrok, conquer all of the British Isles.
6. Carolingian Consolidation: starting as a Karling, be the only independent Karling to hold a landed title.


![celebrity_achievement.png](https://forumcontent.paradoxplaza.com/public/600473/celebrity_achievement.png "celebrity_achievement.png")

![death_did_us_part_achievement.png](https://forumcontent.paradoxplaza.com/public/600474/death_did_us_part_achievement.png "death_did_us_part_achievement.png")

![dreadful_ruler_achievement.png](https://forumcontent.paradoxplaza.com/public/600475/dreadful_ruler_achievement.png "dreadful_ruler_achievement.png")

![end_of_an_era_achievement.png](https://forumcontent.paradoxplaza.com/public/600476/end_of_an_era_achievement.png "end_of_an_era_achievement.png")

![fine_print_achievement.png](https://forumcontent.paradoxplaza.com/public/600477/fine_print_achievement.png "fine_print_achievement.png")

![followed_by_shadows_achievement.png](https://forumcontent.paradoxplaza.com/public/600478/followed_by_shadows_achievement.png "followed_by_shadows_achievement.png")


1. Celebrity: reach the highest possible level of fame.
2. Death Did Us Part: murder your spouse.
3. Dreadful Ruler: have the maximum amount of dread.
4. End of an Era: play until 1453.
5. Fine Print: use a hook to modify a feudal contract.
6. Followed by Shadows: know ten secrets simultaneously.


![for_the_faith_achievement.png](https://forumcontent.paradoxplaza.com/public/600479/for_the_faith_achievement.png "for_the_faith_achievement.png")

![frankokratia_achievement.png](https://forumcontent.paradoxplaza.com/public/600480/frankokratia_achievement.png "frankokratia_achievement.png")

![from_rags_to_riches_achievement.png](https://forumcontent.paradoxplaza.com/public/600481/from_rags_to_riches_achievement.png "from_rags_to_riches_achievement.png")

![give_a_dog_a_bone_achievement.png](https://forumcontent.paradoxplaza.com/public/600482/give_a_dog_a_bone_achievement.png "give_a_dog_a_bone_achievement.png")

![going_places_achievement.png](https://forumcontent.paradoxplaza.com/public/600483/going_places_achievement.png "going_places_achievement.png")

![its_not_a_cult_achievement.png](https://forumcontent.paradoxplaza.com/public/600484/its_not_a_cult_achievement.png "its_not_a_cult_achievement.png")


1. For the Faith: take part in a successful Great Holy War, on either side.
2. Frankokratia: as a French Catholic, hold and completely control the Kingdom of Thessalonika without holding or being vassalised to the Byzantine Empire.
3. From Rags to Riches: starting as a count, lead your line to rule an empire.
4. Give a Dog a Bone: starting as Matilda of Tuscany, lead your dynasty to rule the Kingdom of Italy, have at least fifty living dynasty members, and found a Holy Order.
5. Going Places: as Haesteinn of Montaigu in 867, hold any kingdom-tier title.
6. It’s not a Cult: create a faith.


![keeping_it_in_the_family_achievement.png](https://forumcontent.paradoxplaza.com/public/600485/keeping_it_in_the_family_achievement.png "keeping_it_in_the_family_achievement.png")

![kings_to_the_seventh_generation_achievement.png](https://forumcontent.paradoxplaza.com/public/600486/kings_to_the_seventh_generation_achievement.png "kings_to_the_seventh_generation_achievement.png")

![know_your_place_achievement.png](https://forumcontent.paradoxplaza.com/public/600487/know_your_place_achievement.png "know_your_place_achievement.png")

![land_of_the_rus_achievement.png](https://forumcontent.paradoxplaza.com/public/600488/land_of_the_rus_achievement.png "land_of_the_rus_achievement.png")

![last_count_first_king_achievement.png](https://forumcontent.paradoxplaza.com/public/600489/last_count_first_king_achievement.png "last_count_first_king_achievement.png")

![monumental_achievement.png](https://forumcontent.paradoxplaza.com/public/600490/monumental_achievement.png "monumental_achievement.png")


1. Keeping it in the Family: have a child with the inbred trait.
2. Kings to the Seventh Generation: starting as Count Eudes of Anjou in 867, lead your dynasty to rule the Kingdom of France.
3. Know Your Place: defeat a faction in war.
4. Land of the Rus: starting as Rurik the Troublemaker in 867, lead your dynasty to rule the Empire of Russia.
5. Last Count, First King: starting as Duke Nuno of Portucale in 1066, form Portugal.
6. Monumental: fully upgrade a duchy building anywhere in your personal domain.


![mother_of_us_all_achievement.png](https://forumcontent.paradoxplaza.com/public/600491/mother_of_us_all_achievement.png "mother_of_us_all_achievement.png")

![moving_up_in_the_world_achievement.png](https://forumcontent.paradoxplaza.com/public/600492/moving_up_in_the_world_achievement.png "moving_up_in_the_world_achievement.png")

![non_nobis_domine_achievement.png](https://forumcontent.paradoxplaza.com/public/600493/non_nobis_domine_achievement.png "non_nobis_domine_achievement.png")

![norman_yoke_achievement.png](https://forumcontent.paradoxplaza.com/public/600494/norman_yoke_achievement.png "norman_yoke_achievement.png")

![not_so_feudal_system_achievement.png](https://forumcontent.paradoxplaza.com/public/600495/not_so_feudal_system_achievement.png "not_so_feudal_system_achievement.png")

![paragon_of_virtue_achievement.png](https://forumcontent.paradoxplaza.com/public/600496/paragon_of_virtue_achievement.png "paragon_of_virtue_achievement.png")


1. Mother of Us All: starting as Magajiva Daura, reform an African pagan faith, and convert all counties in Africa to it.
2. Moving up in the World: increase your rank.
3. Non Nobis Domine: found a holy order.
4. Norman Yoke: starting as William the Bastard in 1066, win the Norman Invasion, become English, and have only English Vassals below you in the Kingdom of England.
5. Not So Feudal System: use the claim throne scheme successfully.
6. Paragon of Virtue: have three or more virtuous traits.


![prolific_achievement.png](https://forumcontent.paradoxplaza.com/public/600497/prolific_achievement.png "prolific_achievement.png")

![reconquista_achievement.png](https://forumcontent.paradoxplaza.com/public/600498/reconquista_achievement.png "reconquista_achievement.png")

![rise_from_the_ashes_achievement.png](https://forumcontent.paradoxplaza.com/public/600499/rise_from_the_ashes_achievement.png "rise_from_the_ashes_achievement.png")

![royal_dignity_achievement.png](https://forumcontent.paradoxplaza.com/public/600500/royal_dignity_achievement.png "royal_dignity_achievement.png")

![saint_achievement.png](https://forumcontent.paradoxplaza.com/public/600501/saint_achievement.png "saint_achievement.png")

![seductive_achievement.png](https://forumcontent.paradoxplaza.com/public/600502/seductive_achievement.png "seductive_achievement.png")


1. Prolific: have one hundred living dynasty members.
2. Reconquista: starting as an Iberian Christian, convert all of Iberia to Christianity.
3. Rise from the Ashes: restore the Roman Empire.
4. Royal Dignity: starting as Vratislav Premyslid in 1066, lead your dynasty to rule the Kingdom of Bohemia & the Holy Roman Empire simultaneously.
5. Saint: reach the highest possible level of devotion.
6. Seductive: as any one character, successfully seduce ten people.


![seven_holy_cities_achievement.png](https://forumcontent.paradoxplaza.com/public/600503/seven_holy_cities_achievement.png "seven_holy_cities_achievement.png")

![sibling_rivalry_achievement.png](https://forumcontent.paradoxplaza.com/public/600504/sibling_rivalry_achievement.png "sibling_rivalry_achievement.png")

![stressful_situation_achievement.png](https://forumcontent.paradoxplaza.com/public/600505/stressful_situation_achievement.png "stressful_situation_achievement.png")

![the_emerald_isle_achievement.png](https://forumcontent.paradoxplaza.com/public/600506/the_emerald_isle_achievement.png "the_emerald_isle_achievement.png")

![the_emperors_new_clothes_achievement.png](https://forumcontent.paradoxplaza.com/public/600507/the_emperors_new_clothes_achievement.png "the_emperors_new_clothes_achievement.png")

![the_succession_is_safe_achievement.png](https://forumcontent.paradoxplaza.com/public/600508/the_succession_is_safe_achievement.png "the_succession_is_safe_achievement.png")


1. Seven Holy Cities: as a Hindu ruler, hold all seven Hindu holy sites at the same time.
2. Sibling Rivalry: starting as any of the Jimena siblings in 1066, become Emperor of Spain.
3. Stressful Situation: suffer a mental break.
4. The Emerald Isle: starting as an Irish ruler, hold the Kingdom of Ireland.
5. The Emperor’s New Clothes: while holding any empire title, be naked.
6. The Succession is Safe: have ten living children.


![the_things_love_does_for_us_achievement.png](https://forumcontent.paradoxplaza.com/public/600509/the_things_love_does_for_us_achievement.png "the_things_love_does_for_us_achievement.png")

![the_things_we_do_for_love_achievement.png](https://forumcontent.paradoxplaza.com/public/600510/the_things_we_do_for_love_achievement.png "the_things_we_do_for_love_achievement.png")

![trapped_in_the_web_achievement.png](https://forumcontent.paradoxplaza.com/public/600511/trapped_in_the_web_achievement.png "trapped_in_the_web_achievement.png")

![turning_to_diamonds_achievement.png](https://forumcontent.paradoxplaza.com/public/600512/turning_to_diamonds_achievement.png "turning_to_diamonds_achievement.png")

![until_death_do_us_part_achievement.png](https://forumcontent.paradoxplaza.com/public/600513/until_death_do_us_part_achievement.png "until_death_do_us_part_achievement.png")

![way_of_life_achievement.png](https://forumcontent.paradoxplaza.com/public/600514/way_of_life_achievement.png "way_of_life_achievement.png")


1. The Things Love Does for Us: have a lover save you from a murder attempt.
2. The Things We Do for Love: murder your lover’s spouse.
3. Trapped in the Web: have strong hooks on three direct vassals.
4. Turning to Diamonds: reach the highest possible stress level.
5. Until Death Do Us Part: marry another character.
6. Way of Life: obtain every perk in a lifestyle.


![what_nepotism_achievement.png](https://forumcontent.paradoxplaza.com/public/600515/what_nepotism_achievement.png "what_nepotism_achievement.png")

![wily_as_the_fox_achievement.png](https://forumcontent.paradoxplaza.com/public/600516/wily_as_the_fox_achievement.png "wily_as_the_fox_achievement.png")


1. What Nepotism?: have your dynasty rule ten independent realms of at least kingdom tier simultaneously.
2. Wily as the Fox: starting as Robert the Fox in 1066, rule the Kingdom of Sicily, hold either the Kingdom of Epirus, Hellas, or Thessalonika, and convert all of its original counties to Catholicism.

And with that, we come to the end of the showcase! Anything here that particularly caught your eye, or something you’d like to have seen? I’ll be hanging around in the comments for a couple of hours afterwards, per the usual, so feel free to tag me with any questions you may have.

<!-- artifact:reactions:start -->
- 120 Like
- 50 Love
- 9 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 6 Haha
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)**
Role: Former CK3 Experienced Game Designer
Badges: 92
Messages: 528
Reaction score: 15,169

*[Full game-badge icon list of 10 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
