---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1545392/"
forum_thread_id: 1545392
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: CK3 - Update 1.7.2 - Release. Checksum [ba42]
dd_date: 2022-09-29
author_handle: PDX_Pariah
expansion: Friends and Foes
patch: Patch 1.7 (Bastion)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2232
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1545392'
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
    location: raw_lines_~28_to_120
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_122_to_124
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_336_to_336
    action: preserved_and_flagged
    counts:
      Like: 3
    note: Reactions block parsed; 1 of 1 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_360_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 - Update 1.7.2 - Release. Checksum [ba42]

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Sep 29, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/)
- [2](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/page-2)
[Next](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/page-2)

1 of 2

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/page-2 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/?prdxDevPosts=1)

[![PDX_Pariah](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/s/paradox5.png)](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

#### [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

##### Community Manager

Jul 21, 2020

119

4.454

[](javascript:;)

- [Sep 29, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28505991)


- [/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28505991](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28505991)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28505991/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28505991)

Howdy all!  

Today we are releasing a Minor Update to the game to help with stability and performance. While this is not a major Update and should not affect saved games, we always recommend that you make sure you have a fresh game ready to go with a new version.  

As stated, this is a relatively small Update, but also full of highly impactful changes reported by you in the Community! Here is the Changelog:  

Spoiler: 1.7.2 Changelog

- Fix offer vassalization being slow if you had too many neighbors and vassals due to evaluating opinion too many times too slowly.  
- Fix Out-Of-Sync issue  
- Fix AI feud seduction targeting wrong spouse


As always, keep those reports coming and if you see anything unusual, please let us know [HERE!](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1077/)  

-SP

 

[Reply](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/28505991/report)

[![IsakMDMA](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/new_avatars/s/shield_ser.png)](https://forum.paradoxplaza.com/forum/members/isakmdma.1566490/)

#### [IsakMDMA](https://forum.paradoxplaza.com/forum/members/isakmdma.1566490/)

##### Private

**6 Badges**

Sep 29, 2020

11

2

- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Mount &amp; Blade: With Fire and Sword](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/WFAS.png "Mount &amp; Blade: With Fire and Sword")
- ![Shadowrun Returns](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Returns.PNG "Shadowrun Returns")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")

[](javascript:;)

- [Sep 29, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28506093)


- [/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28506093](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28506093)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28506093/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28506093)

Thanks for the changelog!  
Is there any ETA on a bigger patch?

 

[Reply](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/28506093/report)

[![Prpht](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/synthetic_dawn/s/sd_robot_08.png)](https://forum.paradoxplaza.com/forum/members/prpht.1376951/)

#### [Prpht](https://forum.paradoxplaza.com/forum/members/prpht.1376951/)

##### Second Lieutenant

**52 Badges**

Nov 19, 2018

123

769

- ![Stellaris: Distant Stars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Distantstars.png "Stellaris: Distant Stars")
- ![Crusader Kings II: Monks and Mystics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/monksandmystics.png "Crusader Kings II: Monks and Mystics")
- ![Stellaris - Path to Destruction bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Utopia.png "Stellaris - Path to Destruction bundle")
- ![Europa Universalis IV: Mandate of Heaven](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/moh_forum_icon.png "Europa Universalis IV: Mandate of Heaven")
- ![Europa Universalis IV: Third Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/third_rome_forum_icon.png "Europa Universalis IV: Third Rome")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![Stellaris: Synthetic Dawn](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Syn_dawn_forum_icon.png "Stellaris: Synthetic Dawn")
- ![Europa Universalis IV: Cradle of Civilization](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EUIV_CoC.png "Europa Universalis IV: Cradle of Civilization")
- ![Crusader Kings II: Jade Dragon](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2jd_forumicon.png "Crusader Kings II: Jade Dragon")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")
- ![Surviving Mars: Digital Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_DDE.png "Surviving Mars: Digital Deluxe Edition")
- ![Stellaris: Leviathans Story Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/leviathans.png "Stellaris: Leviathans Story Pack")
- ![Europa Universalis IV: Dharma](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/dharmaicon.png "Europa Universalis IV: Dharma")
- ![Stellaris: Megacorp](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MegaCorp-ForumIcon.png "Stellaris: Megacorp")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Europa Universalis IV: Golden Century](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gc_forum_icon.png "Europa Universalis IV: Golden Century")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Europa Universalis 4: Emperor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_emperor.png "Europa Universalis 4: Emperor")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Europa Universalis IV: Res Publica](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/respublica_icon.png "Europa Universalis IV: Res Publica")
- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Crusader Kings II: Rajas of India](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_rajas_of_india_forumicon.png "Crusader Kings II: Rajas of India")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![Crusader Kings II: Sunset Invasion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sunset_invasion_forumicon.png "Crusader Kings II: Sunset Invasion")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Europa Universalis IV: Art of War](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aow_forum_icon.png "Europa Universalis IV: Art of War")
- ![Europa Universalis IV: Conquest of Paradise](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cop_forumicon.png "Europa Universalis IV: Conquest of Paradise")
- ![Europa Universalis IV: Wealth of Nations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_won_forumicon.png "Europa Universalis IV: Wealth of Nations")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Europa Universalis IV: El Dorado](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_eldorado_forumicon.png "Europa Universalis IV: El Dorado")
- ![Europa Universalis IV: Pre-order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_special_forumicon.png "Europa Universalis IV: Pre-order")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Europa Universalis IV: Common Sense](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cs_forumicon.png "Europa Universalis IV: Common Sense")
- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Europa Universalis IV: Cossacks](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cossacks.jpg "Europa Universalis IV: Cossacks")
- ![Crusader Kings II: Conclave](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DLC_icon_Conclave.png "Crusader Kings II: Conclave")
- ![Europa Universalis IV: Mare Nostrum](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_marenostrum.png "Europa Universalis IV: Mare Nostrum")
- ![Stellaris](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_base.png "Stellaris")
- ![Europa Universalis IV: Rights of Man](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rom_forum_icon.png "Europa Universalis IV: Rights of Man")

[](javascript:;)

- [Sep 29, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28506255)


- [/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28506255](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28506255)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28506255/bookmark "Bookmark")
- [#3](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-2-release-checksum-ba42.1545392/post-28506255)

> [IsakMDMA said:](https://forum.paradoxplaza.com/forum/goto/post?id=28506093)
>
> Thanks for the changelog!
> Is there any ETA on a bigger patch?
>
> Click to expand...

According to [Dev Diary #108](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-108-dev-diary-scheduling-community-activities.1543480/page-5#post-28489018):  

> As of the newly released 1.7.1, we’ve concluded the planned updates for this release, though if something significant appears, we’ll look into fixing it before the next update.
>
> Click to expand...

and  

> While we can say that Friends & Foes was the last paid content of the year, we’re hoping to have another smaller free update out before the year is over (no ETA for now). Additional clues about what we’re working on might appear over the next few months…
>
> Click to expand...

 

- 6

<!-- artifact:reactions:start -->
- 3 Like
<!-- artifact:reactions:end -->
