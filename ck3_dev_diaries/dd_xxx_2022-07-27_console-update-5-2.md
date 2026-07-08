---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1536982/"
forum_thread_id: 1536982
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: CK3 - Console Update 5.2
dd_date: 2022-07-27
author_handle: PDX-Trinexx
expansion: Console Edition
patch: Crusader Kings III Console Edition
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1605
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1536982'
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
    location: raw_lines_~28_to_129
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_131_to_133
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_259_to_260
    action: preserved_and_flagged
    counts:
      Like: 10
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_284_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 - Console Update 5.2

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Jul 27, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/)
- [2](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/page-2)
[Next](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/page-2)

1 of 2

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/page-2 "Last")

[![PDX-Trinexx](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/BTDDAvatars/s/bt_avatar_dde_02.png)](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)

#### [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)

##### Community Manager

**Administrator**

**Paradox Staff**

**102 Badges**

Jan 31, 2022

642

17.753

- ![Europa Universalis IV: Call to arms event](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EU4_signupForumIcon_01.png "Europa Universalis IV: Call to arms event")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Europa Universalis 4: Emperor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_emperor.png "Europa Universalis 4: Emperor")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Europa Universalis IV: Golden Century](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gc_forum_icon.png "Europa Universalis IV: Golden Century")
- ![Europa Universalis IV: Dharma](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/dharmaicon.png "Europa Universalis IV: Dharma")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")
- ![Europa Universalis IV: Cradle of Civilization](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EUIV_CoC.png "Europa Universalis IV: Cradle of Civilization")
- ![Hearts of Iron IV: Death or Dishonor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4DoD.png "Hearts of Iron IV: Death or Dishonor")
- ![Europa Universalis IV: Third Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/third_rome_forum_icon.png "Europa Universalis IV: Third Rome")
- ![Europa Universalis IV: Mandate of Heaven](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/moh_forum_icon.png "Europa Universalis IV: Mandate of Heaven")
- ![Europa Universalis IV: Cossacks](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cossacks.jpg "Europa Universalis IV: Cossacks")
- ![Sengoku](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Sengoku.png "Sengoku")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Stellaris](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_base.png "Stellaris")
- ![Victoria 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2.png "Victoria 2")
- ![Cities: Skylines](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/csl.png "Cities: Skylines")
- ![BATTLETECH](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/battletech_standard.png "BATTLETECH")
- ![Hearts of Iron IV: Cadet](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Cad.png "Hearts of Iron IV: Cadet")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Empire of Sin - Premium Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eos-plat.png "Empire of Sin - Premium Edition")
- ![March of the Eagles](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/mote_icon.png "March of the Eagles")
- ![Magicka 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Magicka2_Icon.png "Magicka 2")
- ![Magicka](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/magickaIcon.png "Magicka")
- ![Age of Wonders: Planetfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aowstandard.png "Age of Wonders: Planetfall")
- ![Knights of Pen and Paper 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/kopp_2_icon.png "Knights of Pen and Paper 2")
- ![Sword of the Stars II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SOTS2.png "Sword of the Stars II")
- ![The Showdown Effect](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tse_forum.png "The Showdown Effect")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Crusader Kings II: Jade Dragon](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2jd_forumicon.png "Crusader Kings II: Jade Dragon")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Age of Wonders III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoW3_forum_badge.png "Age of Wonders III")
- ![Stellaris: Digital Anniversary Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/plantoid.png "Stellaris: Digital Anniversary Edition")
- ![Stellaris: Synthetic Dawn](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Syn_dawn_forum_icon.png "Stellaris: Synthetic Dawn")
- ![Cities: Skylines - Mass Transit](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CitiesSkylines_MassTransit_16x16.png "Cities: Skylines - Mass Transit")
- ![Stellaris - Path to Destruction bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Utopia.png "Stellaris - Path to Destruction bundle")
- ![Crusader Kings II: Monks and Mystics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/monksandmystics.png "Crusader Kings II: Monks and Mystics")
- ![Stellaris: Leviathans Story Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/leviathans.png "Stellaris: Leviathans Story Pack")
- ![Surviving Mars: Digital Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_DDE.png "Surviving Mars: Digital Deluxe Edition")
- ![Europa Universalis IV: Rights of Man](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rom_forum_icon.png "Europa Universalis IV: Rights of Man")
- ![Crusader Kings II: Reapers Due](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/reapers_due_forum_icon.png "Crusader Kings II: Reapers Due")
- ![Europa Universalis IV: Mare Nostrum](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_marenostrum.png "Europa Universalis IV: Mare Nostrum")
- ![Cities: Skylines - Snowfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/snowflake_16_4.png "Cities: Skylines - Snowfall")
- ![Crusader Kings II: Conclave](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DLC_icon_Conclave.png "Crusader Kings II: Conclave")
- ![Cities: Skylines - After Dark](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CS_AD_16x16_fotumicon.png "Cities: Skylines - After Dark")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Empire of Sin](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eos-silver.png "Empire of Sin")

[](javascript:;)

- [Jul 27, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/post-28395734)


- [/forum/threads/ck3-console-update-5-2.1536982/post-28395734](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/post-28395734)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28395734/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-5-2.1536982/post-28395734)

Hello Rulers!  

Today we're releasing **Update 5.2 for the Console Edition** of Crusader Kings III.  


This is a minor Update focusing on addressing stability issues affecting both Xbox and PS5 players. We've also addressed an issue that prevented the "Hook, Line and Sinker" achievement from unlocking. We've greatly appreciated all of your feedback and reports while our partners at Lab42 worked hard to resolve these issues, and we hope that this Update goes a long way towards making your time in the Middle Ages more enjoyable.  

**Changes in Update 5.2:**  


- [**PS5/Xbox**] Resolved an issue that prevented the "Hook, Line and Sinker" achievement from being obtainable. Obtaining a weak hook and a strong hook in one lifetime should now unlock this achievement properly.
- [**PS5/Xbox**] Improved stability by changing how the game handles larger save files.
- [**PS5**] Improved stability by updating how the game interacts with the PS5 suspend and resume menu.
- [**Xbox**] Resolved an issue that could cause a crash when opening the Prestige, Piety, or Renown tooltips.  

<!-- artifact:reactions:start -->
- 10 Like
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
