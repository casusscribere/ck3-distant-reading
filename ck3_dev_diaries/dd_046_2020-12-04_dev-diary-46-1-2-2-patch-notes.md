---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1446267/"
forum_thread_id: 1446267
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 46
title: "CK3 Dev Diary #46 - 1.2.2 Patch Notes"
dd_date: 2020-12-04
author_handle: rageair
expansion: Post-release patches
patch: Patch 1.2 (Argent)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2395
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1446267'
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
    location: raw_lines_~28_to_124
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_126_to_127
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_317_to_318
    action: preserved_and_flagged
    counts:
      Like: 10
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_395_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #46 - 1.2.2 Patch Notes

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Dec 4, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-45-1-2-patch-notes.1444123/ "CK3 Dev Diary #45 - 1.2 Patch Notes") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-47-happy-holidays.1448340/ "CK3 Dev Diary #47 - Happy Holidays!")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/?prdxDevPosts=1)

- [Dec 4, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/post-27147758)
- [Replies: 68](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/#posts)


- [/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/post-27147758](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/post-27147758)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27147758/bookmark "Bookmark")

Greetings!  

Patch 1.2 ‘Argent’ has been out for a while now, and we hope you’re enjoying it! It’s so much fun to see what fascinating creations you all create in the Ruler Designer!  

To round off the year, we’re planning to release a small patch early next week. Originally we wanted to release it this week, but some more issues were found that we wanted to address - such is the nature of software development! ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")  

The patch will address a number of bugs and issues, listed below:  

Spoiler: 1.2.2 Patch Notes

- You can now hold the Control-key when raising armies to not have them be split based on supply when you raise them  
- Fixed the Ruler Designer crashing when using the arrow keys to move sliders on machines with limited RAM  
- Fixed some characters not having access to Cultural Names when naming children because their Religion didn’t have any Religious names defined  
- Fixed a crash that could happen when randomizing Dynasty Names for certain cultures in the Ruler Designer  
- Fixed the Legacies button being hidden beyond the screen if both Dynasty and House modifiers are present  
- Fixed the AI not always supporting the player correctly when handling massive armies  
- Fixed not being able to build certain buildings when playing the game in spanish, esto ahora está arreglado  
- Fixed siege sounds sometimes persisting after you close the siege window  
- Removed the deprecated Nudity game rule, nudity is now toggled on/off in the settings menu, accessible in the same place as you toggle displaying graphical diseases  
- The lifestyle/focus button is no longer visible on characters that cannot have a lifestyle set  
- Kicking a player that is still inside the Ruler Designer will no longer block a multiplayer game from starting  
- When you Ruler Design a character, you will no longer lose all non-De Jure vassals that ruler had  
- Fixed not always having access to all hairstyles when Ruler Designing a character that is 18 years old or younger  
- You now get less points from being extremely old when Ruler Designing a character  
- Fixed the list of Faiths exceeding its limits when playing the game in a non-english language  
- Criminal rulers no longer get a free pass on imprisoning without impunity  
- Diplomacy perk modifiers are now added and subtracted properly (Sound Foundations and Friendly Counsel)  
- Fixed losing Piety when imprisoning generic Criminals, now properly only applies when imprisoning your Head of Faith  
- Fixed an issue with floating or sinking infant characters in the main menu, exorcism successful  
- Fixed a memory leak in the GUI editor  
- Fixed a memory leak for character portraits. This could have a significant effect in the Ruler Designer, and a lesser one during normal play  
- Fixed achievements sometimes being shown as unavailable even though they were available


That's all for now! Have a great winter!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27147758/report)

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

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/page-3#posts)
- [4](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/page-4#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/page-2#posts)

1 of 4

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/page-4#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/?order=prdx_dd_reaction_score)

[N](https://forum.paradoxplaza.com/forum/members/nmcj1996.188142/)

#### [nmcj1996](https://forum.paradoxplaza.com/forum/members/nmcj1996.188142/)

##### Captain

**83 Badges**

Jan 1, 2010

311

784

- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")
- ![Europa Universalis IV: Third Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/third_rome_forum_icon.png "Europa Universalis IV: Third Rome")
- ![Stellaris - Path to Destruction bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Utopia.png "Stellaris - Path to Destruction bundle")
- ![Europa Universalis IV: Mare Nostrum](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_marenostrum.png "Europa Universalis IV: Mare Nostrum")
- ![Europa Universalis IV: Pre-order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_special_forumicon.png "Europa Universalis IV: Pre-order")
- ![Victoria 2: Heart of Darkness](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v2hod_icon.png "Victoria 2: Heart of Darkness")
- ![Victoria 2: A House Divided](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2AHD_forumicon.png "Victoria 2: A House Divided")
- ![Semper Fi](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/sefi.png "Semper Fi")
- ![Europa Universalis IV: Res Publica](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/respublica_icon.png "Europa Universalis IV: Res Publica")
- ![The Kings Crusade](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lionheart.png "The Kings Crusade")
- ![Heir to the Throne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/httt_forum_icon.png "Heir to the Throne")
- ![Hearts of Iron III Collection](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi3col_medal.png "Hearts of Iron III Collection")
- ![Hearts of Iron III: Their Finest Hour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/TFH_forumicon.png "Hearts of Iron III: Their Finest Hour")
- ![Hearts of Iron III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi3_forum_icon.gif "Hearts of Iron III")
- ![For the Motherland](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FTM1.png "For the Motherland")
- ![Europa Universalis IV: Call to arms event](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EU4_signupForumIcon_01.png "Europa Universalis IV: Call to arms event")
- ![Europa Universalis IV: Conquest of Paradise](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cop_forumicon.png "Europa Universalis IV: Conquest of Paradise")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Crusader Kings II: Rajas of India](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_rajas_of_india_forumicon.png "Crusader Kings II: Rajas of India")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![Crusader Kings II: Sunset Invasion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sunset_invasion_forumicon.png "Crusader Kings II: Sunset Invasion")
- ![Europa Universalis III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3_medal_silver.gif "Europa Universalis III")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Europa Universalis III: Chronicles](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3_chronicles.png "Europa Universalis III: Chronicles")
- ![Divine Wind](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3DW_forumicon.png "Divine Wind")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Europa Universalis IV: Wealth of Nations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_won_forumicon.png "Europa Universalis IV: Wealth of Nations")
- ![Europa Universalis IV: Art of War](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aow_forum_icon.png "Europa Universalis IV: Art of War")
- ![Surviving Mars: First Colony Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/greenplanet.png "Surviving Mars: First Colony Edition")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Europa Universalis IV: Golden Century](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gc_forum_icon.png "Europa Universalis IV: Golden Century")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Surviving Mars: First Colony Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SpaceRace.png "Surviving Mars: First Colony Edition")
- ![Hearts of Iron IV: Götterdämmerung](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gtd.png "Hearts of Iron IV: Götterdämmerung")
- ![Europa Universalis IV: Dharma](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/dharmaicon.png "Europa Universalis IV: Dharma")
- ![Stellaris: Distant Stars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Distantstars.png "Stellaris: Distant Stars")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/manthegunsPO.png "Hearts of Iron IV: Expansion Pass")
- ![Surviving Mars: Digital Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_DDE.png "Surviving Mars: Digital Deluxe Edition")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Hearts of Iron IV: La Resistance](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoILRicon.png "Hearts of Iron IV: La Resistance")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Hearts of Iron IV: Battle for the Bosporus](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/bftb.png "Hearts of Iron IV: Battle for the Bosporus")
- ![Europa Universalis 4: Emperor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_emperor.png "Europa Universalis 4: Emperor")

[](javascript:;)

- [Dec 4, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/post-27147770)


- [/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/post-27147770](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/post-27147770)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27147770/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-46-1-2-2-patch-notes.1446267/post-27147770)

Don't suppose you have any idea when you're aiming to have dev diaries back? Hoping for first week of January but maybe thats just me being too optimistic for news of the first expansion! Hope you all have a great winter too though!

<!-- artifact:reactions:start -->
- 10 Like
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
