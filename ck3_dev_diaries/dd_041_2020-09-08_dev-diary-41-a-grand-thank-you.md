---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1420381/"
forum_thread_id: 1420381
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 41
title: "CK3 Dev Diary #41 - A Grand Thank You!"
dd_date: 2020-09-08
author_handle: rageair
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2125
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1420381'
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
    location: raw_lines_122_to_123
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_291_to_293
    action: preserved_and_flagged
    counts:
      Like: 14
      Haha: 2
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_364_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #41 - A Grand Thank You!

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Sep 8, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-40-a-new-journey-begins.1414653/ "CK3 Dev Diary #40 - A new journey begins") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-42-1-1-patch-notes.1428193/ "CK3 Dev Diary #42 - 1.1 Patch Notes")

- [Sep 8, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/post-26885399)
- [Replies: 161](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/#posts)


- [/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/post-26885399](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/post-26885399)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/26885399/bookmark "Bookmark")

Greetings from all of us in the CK3 team!  

The game is finally released, and what a journey it has been! It’s truly humbling to see something that we’ve worked on for so long, and poured so much of our passion into, finally out in the wild. We’re overjoyed with the response we’ve gotten so far, it’s great that so many of you seem to enjoy the game. The amount of stories and experiences already being shared is nothing but mind-boggling, and lots of them are circulating throughout the team, putting many smiles upon our faces (especially all the memes!). We in the team wish to extend a grand ‘thank you’ to all of you for making this launch so fantastic.  

In the near future we’ll be looking at collecting and addressing as many of your issues as we can. The upcoming patch (release date TBD) is a mix of improvements that didn't make it into the release (including some really fancy UI upgrades!), and bug fixes based on your feedback. Patch notes will be posted closer in time to when the patch will be released. If you have an issue, make sure to report it [here](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1077/) so that it’s sure to be looked at!  

In the next few weeks there will be no Dev Diaries, as we’ll focus our efforts on working with the feedback we’re getting from all of you. When something of interest happens, we’ll of course be back! Until then, please keep enjoying the game, sharing your stories, and shaping the world to your liking!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/26885399/report)

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

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [9](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/page-9#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/page-2#posts)

1 of 9

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/page-9#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/?order=prdx_dd_reaction_score)

[![Zylathas](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/ck3/s/avatar_30.png)](https://forum.paradoxplaza.com/forum/members/zylathas.742909/)

#### [Zylathas](https://forum.paradoxplaza.com/forum/members/zylathas.742909/)

##### Lt. General

**76 Badges**

May 27, 2013

1.504

4.461

- ![Impire](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/impire_icon.png "Impire")
- ![Europa Universalis IV: Mare Nostrum](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_marenostrum.png "Europa Universalis IV: Mare Nostrum")
- ![Cities: Skylines - Snowfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/snowflake_16_4.png "Cities: Skylines - Snowfall")
- ![Cities: Skylines - Natural Disasters](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CS_ND_icon_16x16.png "Cities: Skylines - Natural Disasters")
- ![Cities: Skylines - After Dark](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CS_AD_16x16_fotumicon.png "Cities: Skylines - After Dark")
- ![Stellaris - Path to Destruction bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Utopia.png "Stellaris - Path to Destruction bundle")
- ![Europa Universalis IV: Pre-order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_special_forumicon.png "Europa Universalis IV: Pre-order")
- ![Crusader Kings II: Jade Dragon](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2jd_forumicon.png "Crusader Kings II: Jade Dragon")
- ![Europa Universalis IV: Third Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/third_rome_forum_icon.png "Europa Universalis IV: Third Rome")
- ![Victoria 2: Heart of Darkness](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v2hod_icon.png "Victoria 2: Heart of Darkness")
- ![Victoria 2: A House Divided](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2AHD_forumicon.png "Victoria 2: A House Divided")
- ![Europa Universalis IV: Res Publica](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/respublica_icon.png "Europa Universalis IV: Res Publica")
- ![Europa Universalis IV: Call to arms event](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EU4_signupForumIcon_01.png "Europa Universalis IV: Call to arms event")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Crusader Kings II: Rajas of India](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_rajas_of_india_forumicon.png "Crusader Kings II: Rajas of India")
- ![Europa Universalis IV: Wealth of Nations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_won_forumicon.png "Europa Universalis IV: Wealth of Nations")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![Crusader Kings II: Sunset Invasion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sunset_invasion_forumicon.png "Crusader Kings II: Sunset Invasion")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Cities in Motion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/cim_forum_icon.png "Cities in Motion")
- ![Europa Universalis IV: Art of War](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aow_forum_icon.png "Europa Universalis IV: Art of War")
- ![Europa Universalis IV: Conquest of Paradise](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cop_forumicon.png "Europa Universalis IV: Conquest of Paradise")
- ![Stellaris: Distant Stars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Distantstars.png "Stellaris: Distant Stars")
- ![Cities: Skylines - Parklife](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSLParkLife.png "Cities: Skylines - Parklife")
- ![Cities: Skylines - Green Cities](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSL_green_cities.png "Cities: Skylines - Green Cities")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")
- ![Europa Universalis IV: Dharma](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/dharmaicon.png "Europa Universalis IV: Dharma")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")
- ![Victoria 3 Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v3_signup_forum_icon.png "Victoria 3 Sign Up")
- ![Cities: Skylines Industries](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/cslindustriesicon.jpg "Cities: Skylines Industries")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Europa Universalis IV: Golden Century](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gc_forum_icon.png "Europa Universalis IV: Golden Century")
- ![Imperator: Rome Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ImperatorDeluxeicon.png "Imperator: Rome Deluxe Edition")
- ![Imperator: Rome Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorsignup.png "Imperator: Rome Sign Up")
- ![Cities: Skylines - Campus](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSLCampus.png "Cities: Skylines - Campus")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Europa Universalis 4: Emperor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_emperor.png "Europa Universalis 4: Emperor")
- ![Hearts of Iron IV: Cadet](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Cad.png "Hearts of Iron IV: Cadet")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Victoria 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2.png "Victoria 2")

[](javascript:;)

- [Sep 8, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/post-26885413)


- [/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/post-26885413](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/post-26885413)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/26885413/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-41-a-grand-thank-you.1420381/post-26885413)

Boo, really hoped we would've gotten a patch this week. This DD doesn't imply that is going to be the case.

 

- 102
- 46

<!-- artifact:reactions:start -->
- 14 Like
- 2 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
