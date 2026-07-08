---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1389565/"
forum_thread_id: 1389565
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 26
title: "CKIII Dev Diary #26 - Map Scope"
dd_date: 2020-05-12
author_handle: Servancour
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1339
inline_image_count: 35
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1389565'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1373.jpg?1589286826
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_151_to_153
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_337_to_341
    action: preserved_and_flagged
    counts:
      Love: 109
      Like: 88
      (unlabeled — rendered as base64 data URI): 6
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_349_to_447
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_448_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1373.jpg?1589286826)
<!-- artifact:thread_banner:end -->

# CKIII Dev Diary #26 - Map Scope

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [May 12, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ckiii-dev-diary-26-map-scope.1389565/)
<!-- artifact:thread_metadata:end -->

Salutations!  

As a continuation from last week, I will be talking about the scope of the map and, perhaps more importantly, showing you how it all actually looks. Get ready for a *very* screenshot heavy DD!  

**Europe**  
Europe has been reworked from the ground up. We made sure to give all of Europe proper attention when painting baronies and counties. It was important for us to make sure we have a good and consistent quality level across the map. I’m sure you’ll find eastern Europe in particular fleshed out with a lot more detail than what you may be used to in CK2.  

![26_01_kiev.jpg](https://forumcontent.paradoxplaza.com/public/563871/26_01_kiev.jpg "26_01_kiev.jpg")



![26_02_novgorod.jpg](https://forumcontent.paradoxplaza.com/public/563872/26_02_novgorod.jpg "26_02_novgorod.jpg")



Since we’ve already shown bits and pieces of Europe in screenshots and videos, let’s have a look at a few specific locations, and what special buildings they have available. Starting with France, it felt like an obvious choice to include Notre-Dame, one of the most recognizable cathedrals of the time period.  

![26_03_notre-dame.jpg](https://forumcontent.paradoxplaza.com/public/563873/26_03_notre-dame.jpg "26_03_notre-dame.jpg")



![26_04_northern_france.jpg](https://forumcontent.paradoxplaza.com/public/563874/26_04_northern_france.jpg "26_04_northern_france.jpg")



![26_05_aquitaine_burgundy.jpg](https://forumcontent.paradoxplaza.com/public/563875/26_05_aquitaine_burgundy.jpg "26_05_aquitaine_burgundy.jpg")



Next up, Iberia. Featuring two major rivers, plenty of hills and a few special buildings. In the county of Granada you’ll find Alhambra. While merely an old ruin at game start, it can be upgraded to offer some of the highest fortifications in the game.  

![26_06_northern_iberia.jpg](https://forumcontent.paradoxplaza.com/public/563876/26_06_northern_iberia.jpg "26_06_northern_iberia.jpg")



![26_07_southern_iberia.jpg](https://forumcontent.paradoxplaza.com/public/563877/26_07_southern_iberia.jpg "26_07_southern_iberia.jpg")



![26_08_alhambra.jpg](https://forumcontent.paradoxplaza.com/public/563878/26_08_alhambra.jpg "26_08_alhambra.jpg")



Speaking of special buildings. The city of the world’s desire, features not one, but *two*, special buildings. This makes Constantinople a very spectacular holding, and if that isn’t enough, it also has the highest development level in the game.  

![26_09_theodosian_walls.jpg](https://forumcontent.paradoxplaza.com/public/563879/26_09_theodosian_walls.jpg "26_09_theodosian_walls.jpg")

![26_10_hagia_sophia.jpg](https://forumcontent.paradoxplaza.com/public/563880/26_10_hagia_sophia.jpg "26_10_hagia_sophia.jpg")



![26_11_greece_anatolia.jpg](https://forumcontent.paradoxplaza.com/public/563881/26_11_greece_anatolia.jpg "26_11_greece_anatolia.jpg")



Before moving on, I’ll just leave this culture screenshot right here:  

![26_12_what_cultures_now.jpg](https://forumcontent.paradoxplaza.com/public/563882/26_12_what_cultures_now.jpg "26_12_what_cultures_now.jpg")



**The Middle East**  
The Middle East has seen the same level of attention and rework as Europe, with some particular attention spent on updating history across the region. For example, the Seljuks control a vast empire in 1066, properly representing their historical borders. They have a plethora of different cultures as their subjects and may fall apart if not careful.  

![26_13_seljuk.jpg](https://forumcontent.paradoxplaza.com/public/563883/26_13_seljuk.jpg "26_13_seljuk.jpg")



Development in the region is above your average starting levels. Baghdad, for example, starts out with one of the highest levels of development in the game — bested only by a few other locations such as Constantinople! Baghdad also has one of the single most impressive special buildings available, the House of Wisdom.  

![26_15_house_of_wisdom.jpg](https://forumcontent.paradoxplaza.com/public/563885/26_15_house_of_wisdom.jpg "26_15_house_of_wisdom.jpg")



![26_16_baghdad.jpg](https://forumcontent.paradoxplaza.com/public/563886/26_16_baghdad.jpg "26_16_baghdad.jpg")



![26_17_nishapur.jpg](https://forumcontent.paradoxplaza.com/public/563887/26_17_nishapur.jpg "26_17_nishapur.jpg")



![26_18_jerusalem.jpg](https://forumcontent.paradoxplaza.com/public/563888/26_18_jerusalem.jpg "26_18_jerusalem.jpg")



**Africa**  
Africa has seen some of the greatest additions to the map. No longer cut in half, the Sub-Saharan kingdoms have plenty of space to expand in as we have included the entire Nigerian coast.  

![26_19_west_africa.jpg](https://forumcontent.paradoxplaza.com/public/563889/26_19_west_africa.jpg "26_19_west_africa.jpg")



We have a total of five different pagan faiths to play as, giving you plenty of different options. A solid first pick would be Benin, within the Niger delta. They start off with a decent development level and access to a special building: The massive construction that is the Walls of Benin.  

![26_20_faiths_west_africa.jpg](https://forumcontent.paradoxplaza.com/public/563890/26_20_faiths_west_africa.jpg "26_20_faiths_west_africa.jpg")



![26_21_benin.jpg](https://forumcontent.paradoxplaza.com/public/563891/26_21_benin.jpg "26_21_benin.jpg")



![26_22_walls_of_benin.jpg](https://forumcontent.paradoxplaza.com/public/563892/26_22_walls_of_benin.jpg "26_22_walls_of_benin.jpg")



Some cultures will start with the ability to sail major rivers, allowing them to use the Niger to quickly ferry troops back and forth. The coast on the other hand, will be open for everyone to use. You won’t be able to sail around the African coast to reach Europe however, or vice versa. That route is blocked by impassable sea, since it was often difficult, if not impossible, to sail along the western coast due to storms and rough seas. No viking raids in Africa, I’m afraid!  

![26_23_ghana_niger.jpg](https://forumcontent.paradoxplaza.com/public/563893/26_23_ghana_niger.jpg "26_23_ghana_niger.jpg")



![26_24_coast_of_guinea.jpg](https://forumcontent.paradoxplaza.com/public/563894/26_24_coast_of_guinea.jpg "26_24_coast_of_guinea.jpg")



![26_25_impassable_sea.jpg](https://forumcontent.paradoxplaza.com/public/563895/26_25_impassable_sea.jpg "26_25_impassable_sea.jpg")



Let’s not forget the Horn of Africa. Expanded to include Mogadishu, the area offers more space to play in, with christian, muslim, jewish, and pagan rulers all wanting a piece of each other.  

![26_26_ajuraan.jpg](https://forumcontent.paradoxplaza.com/public/563896/26_26_ajuraan.jpg "26_26_ajuraan.jpg")



![26_27_ajuraan_close_up.jpg](https://forumcontent.paradoxplaza.com/public/563897/26_27_ajuraan_close_up.jpg "26_27_ajuraan_close_up.jpg")



Finally, let's mention Egypt. A rich area that has a lot of floodplains, good development levels, and even a couple of special buildings. All encompassed by the Nile, a major river with green and lush vegetation.  

![26_28_egypt.jpg](https://forumcontent.paradoxplaza.com/public/563898/26_28_egypt.jpg "26_28_egypt.jpg")



![26_29_pyramids.jpg](https://forumcontent.paradoxplaza.com/public/563899/26_29_pyramids.jpg "26_29_pyramids.jpg")



**The Far East**  
Looking east, the map has been expanded to include the entirety of Tibet, along with a small extension of Mongolia, accompanied by a whole set of new cultures and faiths!  

Starting with Tibet, the area has a whole bunch of independent realms since the Tibetan Empire is long gone by the time of our two start dates. There’s a wide range of rulers of different faiths and cultures spread out across the plateau. The two most prominent faiths being Bön and Nangchos, a Buddhist faith syncretized with different Tibetan beliefs and practices.  

![26_30_tibet.jpg](https://forumcontent.paradoxplaza.com/public/563900/26_30_tibet.jpg "26_30_tibet.jpg")



![26_31_tibetan_faiths.jpg](https://forumcontent.paradoxplaza.com/public/563901/26_31_tibetan_faiths.jpg "26_31_tibetan_faiths.jpg")



![26_32_lhasa.jpg](https://forumcontent.paradoxplaza.com/public/563902/26_32_lhasa.jpg "26_32_lhasa.jpg")



Turning to Mongolia, there is a powerhouse present in both bookmarks. In 867, you have the Kirghiz Khanate, and Great Liao in 1066. Counties and provinces include Karakorum and the entire area surrounding lake Baikal.  

![26_33_baikal_867.jpg](https://forumcontent.paradoxplaza.com/public/563903/26_33_baikal_867.jpg "26_33_baikal_867.jpg")



![26_34_mongolia_1066.jpg](https://forumcontent.paradoxplaza.com/public/563904/26_34_mongolia_1066.jpg "26_34_mongolia_1066.jpg")



Expanding Tibet and Mongolia left us with a small empty space in the south, and we really couldn’t have that, now could we? So we went ahead and filled out Myanmar (or Burma) down to the Gulf of Martaban with brand new baronies and counties. Which gives you two rather interesting starting options. In 1066, you’ll be able to play as king Anawrahta of the Pagan Kingdom. Starting shortly after his conquest of the Mon kingdoms to the south, most of the area will already be under his control, giving you a great opportunity to push into India! Alternatively you can start as Pagan in 867, yet a small and upstarting kingdom, allowing you to play with the unique faith of Ari Buddhism.  

![26_35_pagan.jpg](https://forumcontent.paradoxplaza.com/public/563905/26_35_pagan.jpg "26_35_pagan.jpg")



![26_36_shwedagon.jpg](https://forumcontent.paradoxplaza.com/public/563906/26_36_shwedagon.jpg "26_36_shwedagon.jpg")



I’ll wrap it up here. Otherwise I’ll end up posting screenshots all day. Do you think I missed an important area somewhere? Let me know and maybe, just maybe, I’ll see if I can’t share some more.

<!-- artifact:reactions:start -->
- 109 Love
- 88 Like
- 22 (unlabeled — rendered as base64 data URI)
- 9 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)**
Role: Game Designer
Badges: 4
Reaction score: 9,949

*[Full game-badge icon list of 38 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
