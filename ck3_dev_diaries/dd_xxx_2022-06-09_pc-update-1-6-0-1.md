---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1530285/"
forum_thread_id: 1530285
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: CK3 - PC Update 1.6.0.1
dd_date: 2022-06-09
author_handle: NicouLenny
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1562
inline_image_count: 1
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1530285'
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
    location: raw_lines_~28_to_125
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_127_to_129
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_255_to_257
    action: preserved_and_flagged
    counts:
      Like: 35
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 1 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_283_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 - PC Update 1.6.0.1

<!-- artifact:thread_metadata:start -->
- Thread starter [NicouLenny](https://forum.paradoxplaza.com/forum/members/nicoulenny.1478317/)
- Start date [Jun 9, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/)
- [2](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/page-3)
- [4](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/page-4)
[Next](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/page-2)

1 of 4

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/page-4 "Last")

[![NicouLenny](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/MagickaWizardWars/s/MWW Avatar (43).png)](https://forum.paradoxplaza.com/forum/members/nicoulenny.1478317/)

#### [NicouLenny](https://forum.paradoxplaza.com/forum/members/nicoulenny.1478317/)

##### Captain

**39 Badges**

Oct 22, 2019

459

3.074

- ![Surviving Mars: First Colony Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/greenplanet.png "Surviving Mars: First Colony Edition")
- ![Crusader Kings II: Jade Dragon](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2jd_forumicon.png "Crusader Kings II: Jade Dragon")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Stellaris: Distant Stars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Distantstars.png "Stellaris: Distant Stars")
- ![Surviving Mars: First Colony Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SpaceRace.png "Surviving Mars: First Colony Edition")
- ![Stellaris: Megacorp](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MegaCorp-ForumIcon.png "Stellaris: Megacorp")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Prison Architect](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Prisonicon.png "Prison Architect")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Age of Wonders: Planetfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aowstandard.png "Age of Wonders: Planetfall")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Stellaris: Leviathans Story Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/leviathans.png "Stellaris: Leviathans Story Pack")
- ![Stellaris: Digital Anniversary Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/plantoid.png "Stellaris: Digital Anniversary Edition")
- ![Stellaris](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_base.png "Stellaris")
- ![Crusader Kings II: Conclave](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DLC_icon_Conclave.png "Crusader Kings II: Conclave")
- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Mount &amp; Blade: With Fire and Sword](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/WFAS.png "Mount &amp; Blade: With Fire and Sword")
- ![Stellaris - Path to Destruction bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Utopia.png "Stellaris - Path to Destruction bundle")
- ![War of the Roses](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/wotr_icon.png "War of the Roses")
- ![Magicka](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/magickaIcon.png "Magicka")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Crusader Kings II: Rajas of India](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_rajas_of_india_forumicon.png "Crusader Kings II: Rajas of India")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![Crusader Kings II: Sunset Invasion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sunset_invasion_forumicon.png "Crusader Kings II: Sunset Invasion")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Stellaris: Synthetic Dawn](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Syn_dawn_forum_icon.png "Stellaris: Synthetic Dawn")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")

[](javascript:;)

- [Jun 9, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/post-28317130)


- [/forum/threads/ck3-pc-update-1-6-0-1.1530285/post-28317130](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/post-28317130)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28317130/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-6-0-1.1530285/post-28317130)

Hi everyone,  

We have released **Update 1.6.0.1 for PC** at 10am CEST this morning.  
The latter aims to fix the recent [**CPU Support Issue for Fate of Iberia *(AVX issue)***](https://forum.paradoxplaza.com/forum/threads/cpu-support-issue-for-fate-of-iberia.1529667/) that you have reported after the release of Flavor Pack 2.  

Update 1.6.1 will be released in the coming weeks, where we’re tweaking some balance, fixing issues found by you in the community, and also adding in a few new goodies ([*Sneak Peak Here*](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-100-a-royal-journey.1530040/)).  
Remember to pop by the [bug forums](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1077/) if you have a problem, so we can investigate and fix the issues you experience with CK3.  

**Some of the issues that will be fixed in 1.6.1:**  


- Crashes when changing Amenities in Tribal Royal Court
  * *At the moment the workaround is to change from Tribal to Feudal, we know it is not the best but we are working on it.*
- Northern Hairstyles are not available for Northern characters
- King of Asturias starts with negative prestige in 867 bookmark
- Achievement "History's best friends" is achieved upon seducing/romancing anyone
- More improvements & bug fixes
We are also adding a **new game rule for the Dissolution Faction in 1.6.1**, along with tweaks to the feature to rebalance it. Again, thank you for your feedback!  

Thanks for your time and patience,  

![Steam Spotlight (2108x460).png](https://forumcontent.paradoxplaza.com/public/835712/Steam Spotlight (2108x460).png "Steam Spotlight (2108x460).png")

 

Toggle signature

**Ex-Community Ambassador for Crusader Kings III  
►** *[Twitter Nicou](https://twitter.com/NicouLenny)*

<!-- artifact:reactions:start -->
- 35 Like
- 7 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
