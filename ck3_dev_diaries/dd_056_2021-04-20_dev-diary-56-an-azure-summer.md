---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1468532/"
forum_thread_id: 1468532
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 56
title: "CK3 Dev Diary #56 - An Azure Summer"
dd_date: 2021-04-20
author_handle: rageair
expansion: Northern Lords
patch: Patch 1.4 (Azure)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2396
inline_image_count: 1
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1468532'
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
    location: raw_lines_~28_to_123
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_125_to_126
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_319_to_322
    action: preserved_and_flagged
    counts:
      Like: 9
      (unlabeled — rendered as base64 data URI): 1
      Haha: 3
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_399_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #56 - An Azure Summer

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Apr 20, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-iii-dev-diary-55-modding-improvements.1466888/ "Crusader Kings III Dev Diary #55 - Modding Improvements") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-57-an-eventful-summer.1470041/ "CK3 Dev Diary #57 - An Eventful Summer")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/?prdxDevPosts=1)

- [Apr 20, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/post-27450233)
- [Replies: 80](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/#posts)


- [/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/post-27450233](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/post-27450233)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27450233/bookmark "Bookmark")

### CK3 Dev Diary #56 - An Azure Summer​

Greetings!  

This week we have a few announcements to make! Firstly, as you saw in the last diary, we mentioned the number 1.3.X - this is the version number for an upcoming patch that we’re aiming to release around this summer (of course, the ‘X’ part will be an actual digit when it’s released, but for now we’ll just have to wait to see what it’ll be in the end!).  

As you already know, we tend to name our patches using heraldic terms. The Northern Lords release had the name ‘Corvus’ for example. As we’re hoping for clear blue skies this summer, we’ve dubbed this patch ‘Azure’!  

The Azure patch is a free patch, and there will not be any paid content coming out at the same time. It’ll focus on improving the stability of the game, fixing bugs, adding Quality of Life, balancing various systems, and adding some small features requested by the community. We’ll not go into many details in this diary, instead you can look forward to more info in some of the upcoming Dev Diaries!  

Until then, here is a first teaser of some of the improvements that you will find in the patch:  


- **War Declaration Window:** The war declaration UI flow will be revisited in order to better highlight your opponent’s strength and the different objectives available for a given Casus Belli
- **Starting Men at Arms:** Rulers will now start with a contingent of Men at Arms, depending on their income and culture. Default Men at Arms will also be generated when a Character is landed for the first time.


![StartingMaA.png](https://forumcontent.paradoxplaza.com/public/694062/StartingMaA.png "StartingMaA.png")


[Image of Duchess Matilda's starting MaA]  

We hope to release Azure this summer, before the vacation season (the summer vacation usually starts late June and ends by the end of July) - but depending on how our plans work out, it might release during late summer.  

***  

Another thing we’re actively working with is improving Multiplayer stability, although this is separate from the upcoming Azure patch. We’re currently collecting as much data as we can, and it’s a process that’ll take time - at this point we’d not want to release the improvements as a patch.  

Instead we’re aiming to release an Open Beta on Steam where you can get access to some of the Multiplayer stability improvements early. We highly recommend using this Open Beta when playing with your friends. This version of the game will have extra Multiplayer logging enabled, so that any remaining issues can be found more easily. As a side effect of these additional logs, the game will run a bit slower both in multiplayer and in singleplayer. If you notice the slowdown, you might want to switch back from the Open Beta for your singleplayer sessions. More specific info will be posted as the Open Beta is released.  

This Open Beta will be available sometime in the near future for Steam users.  

***  

Now, as most of you have already figured out, the first big Expansion will be revealed during PDXCon in May! We’re looking forward to then, and to be able to share more details with you!  

During the week of PDXCon we’ll have a DevDiary where we go into some detail about parts of the Expansion (we know that you’ll be hungry for more info after seeing the show!). After that diary, there will be some more Azure patch diaries before we start writing further Expansion diaries - just a heads up, so you know what to expect!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27450233/report)

Click to expand...

[![rageair](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/obsolete/m/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/rageair.375731/)

Written by

### [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)

CK3 Game Director

Grand Stategy

***Paradox Staff******43 Badges***

-

Messages
1.826

-

Reaction score
11.829

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/page-3#posts)
- [4](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/page-4#posts)
- [5](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/page-5#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/page-2#posts)

1 of 5

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/page-5#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/?order=prdx_dd_reaction_score)

[![Voy](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/Wiki_patron/s/TopPatronBadge.png)](https://forum.paradoxplaza.com/forum/members/voy.478583/)

#### [Voy](https://forum.paradoxplaza.com/forum/members/voy.478583/)

##### Wiki Royalty

**52 Badges**

Apr 20, 2012

3.978

8.039

- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Sengoku](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Sengoku.png "Sengoku")
- ![Magicka](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/magickaIcon.png "Magicka")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Stellaris - Path to Destruction bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Utopia.png "Stellaris - Path to Destruction bundle")
- ![Cities: Skylines - Mass Transit](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CitiesSkylines_MassTransit_16x16.png "Cities: Skylines - Mass Transit")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![Crusader Kings II: Jade Dragon](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2jd_forumicon.png "Crusader Kings II: Jade Dragon")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Cities: Skylines - Parklife](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSLParkLife.png "Cities: Skylines - Parklife")
- ![Crusader Kings II: Holy Fury Pre-order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holyfuryPO.png "Crusader Kings II: Holy Fury Pre-order")
- ![Stellaris: Distant Stars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Distantstars.png "Stellaris: Distant Stars")
- ![Stellaris: Megacorp](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MegaCorp-ForumIcon.png "Stellaris: Megacorp")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Imperator: Rome Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ImperatorDeluxeicon.png "Imperator: Rome Deluxe Edition")
- ![Cities: Skylines - Natural Disasters](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CS_ND_icon_16x16.png "Cities: Skylines - Natural Disasters")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Imperator: Rome - Magna Graecia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MagnGraeciaIcon.png "Imperator: Rome - Magna Graecia")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Victoria 3 Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v3_signup_forum_icon.png "Victoria 3 Sign Up")
- ![Crusader Kings II: Conclave](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DLC_icon_Conclave.png "Crusader Kings II: Conclave")
- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")
- ![500k Club](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/500k_red.png "500k Club")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Cities: Skylines - After Dark](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CS_AD_16x16_fotumicon.png "Cities: Skylines - After Dark")
- ![Crusader Kings II: Monks and Mystics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/monksandmystics.png "Crusader Kings II: Monks and Mystics")
- ![Cities: Skylines - Snowfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/snowflake_16_4.png "Cities: Skylines - Snowfall")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellnova.png "Stellaris: Galaxy Edition")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellgalaxy.png "Stellaris: Galaxy Edition")
- ![Crusader Kings II: Reapers Due](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/reapers_due_forum_icon.png "Crusader Kings II: Reapers Due")
- ![Tyranny: Archon Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tyr_com.png "Tyranny: Archon Edition")
- ![Major Wiki Contributor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/WikiModicon.png "Major Wiki Contributor")
- ![Stellaris: Digital Anniversary Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/plantoid.png "Stellaris: Digital Anniversary Edition")
- ![Stellaris: Leviathans Story Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/leviathans.png "Stellaris: Leviathans Story Pack")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Crusader Kings II: Rajas of India](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_rajas_of_india_forumicon.png "Crusader Kings II: Rajas of India")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![Tyranny - Tales from the Tiers](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Tyr_TftT.png "Tyranny - Tales from the Tiers")
- ![Stellaris: Synthetic Dawn](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Syn_dawn_forum_icon.png "Stellaris: Synthetic Dawn")
- ![Stellaris](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_base.png "Stellaris")

[](javascript:;)

- [Apr 20, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/post-27451196)


- [/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/post-27451196](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/post-27451196)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27451196/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-56-an-azure-summer.1468532/post-27451196)

Thanks, we stan Devdiaries of substance.

<!-- artifact:reactions:start -->
- 9 Like
- 8 (unlabeled — rendered as base64 data URI)
- 3 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
