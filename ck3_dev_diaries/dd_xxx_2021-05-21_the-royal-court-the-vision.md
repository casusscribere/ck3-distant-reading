---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1474818/"
forum_thread_id: 1474818
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "CK3: The Royal Court - The Vision"
dd_date: 2021-05-21
author_handle: rageair
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1939
inline_image_count: 1
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1474818'
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
    location: raw_lines_257_to_262
    action: preserved_and_flagged
    counts:
      Love: 256
      Like: 132
      (unlabeled — rendered as base64 data URI): 3
      Haha: 3
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_339_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3: The Royal Court - The Vision

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [May 21, 2021](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/)
- [2](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/page-3)
- …
  
  #### Go to page
  
  Go

- [15](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/page-15)
[Next](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/page-2)

1 of 15

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/page-15 "Last")

[![rageair](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/obsolete/s/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/rageair.375731/)

#### [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)

##### CK3 Game Director

**Paradox Staff**

**43 Badges**

Sep 10, 2011

1.826

11.829

- ![Cities in Motion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/cim_forum_icon.png "Cities in Motion")
- ![Europa Universalis IV: Pre-order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_special_forumicon.png "Europa Universalis IV: Pre-order")
- ![War of the Vikings](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/warofthevikings_forum_icon.png "War of the Vikings")
- ![Victoria 2: Heart of Darkness](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v2hod_icon.png "Victoria 2: Heart of Darkness")
- ![Victoria 2: A House Divided](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2AHD_forumicon.png "Victoria 2: A House Divided")
- ![Victoria 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2.png "Victoria 2")
- ![Semper Fi](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/sefi.png "Semper Fi")
- ![Victoria: Revolutions](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/victoriarevolutions.gif "Victoria: Revolutions")
- ![Europa Universalis IV: Res Publica](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/respublica_icon.png "Europa Universalis IV: Res Publica")
- ![Magicka](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/magickaIcon.png "Magicka")
- ![Heir to the Throne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/httt_forum_icon.png "Heir to the Throne")
- ![Hearts of Iron III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi3_forum_icon.gif "Hearts of Iron III")
- ![For the Motherland](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FTM1.png "For the Motherland")
- ![Europa Universalis IV: Call to arms event](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EU4_signupForumIcon_01.png "Europa Universalis IV: Call to arms event")
- ![Europa Universalis IV: Wealth of Nations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_won_forumicon.png "Europa Universalis IV: Wealth of Nations")
- ![Europa Universalis IV: Conquest of Paradise](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cop_forumicon.png "Europa Universalis IV: Conquest of Paradise")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![A Game of Dwarves](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/agodicon.png "A Game of Dwarves")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Europa Universalis IV: Art of War](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aow_forum_icon.png "Europa Universalis IV: Art of War")
- ![Crusader Kings II: Rajas of India](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_rajas_of_india_forumicon.png "Crusader Kings II: Rajas of India")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Crusader Kings II: Sunset Invasion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sunset_invasion_forumicon.png "Crusader Kings II: Sunset Invasion")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Europa Universalis III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3_medal_silver.gif "Europa Universalis III")
- ![Europa Universalis III: Chronicles](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3_chronicles.png "Europa Universalis III: Chronicles")
- ![Europa Universalis III Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3_complete.gif "Europa Universalis III Complete")
- ![Divine Wind](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3DW_forumicon.png "Divine Wind")
- ![Shadowrun Returns](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Returns.PNG "Shadowrun Returns")
- ![The Showdown Effect](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tse_forum.png "The Showdown Effect")
- ![Shadowrun: Dragonfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Dragonfall.png "Shadowrun: Dragonfall")
- ![Stellaris Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Stellaris_SignUp_icon.png "Stellaris Sign-up")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Shadowrun: Hong Kong](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hongkong.PNG "Shadowrun: Hong Kong")
- ![Europa Universalis IV: El Dorado](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_eldorado_forumicon.png "Europa Universalis IV: El Dorado")
- ![500k Club](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/500k_red.png "500k Club")
- ![War of the Roses](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/wotr_icon.png "War of the Roses")
- ![Europa Universalis III Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nap_icon.gif "Europa Universalis III Complete")
- ![Europa Universalis III Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/in_nomine_icon_forum.gif "Europa Universalis III Complete")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")

[](javascript:;)

- [May 21, 2021](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/post-27542143)


- [/forum/threads/ck3-the-royal-court-the-vision.1474818/post-27542143](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/post-27542143)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27542143/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-the-royal-court-the-vision.1474818/post-27542143)

![Social (FB_Twitter etc) (6).png](https://forumcontent.paradoxplaza.com/public/708537/Social (FB_Twitter etc) (6).png "Social (FB_Twitter etc) (6).png")


Greetings!  

What’s the most symbolic image of a medieval ruler you can think of? Maybe they’re riding a horse through a village, maybe they’re perched at the top of a tower overlooking their realm, or maybe they’re leading troops in battle… those are good, but there’s one thing that is depicted more than anything else, something quintessentially medieval, something that truly evokes the feeling of the era - *a ruler on a throne, surrounded by courtiers, vassals, and petitioners.*  

This is something brand new to the Crusader Kings series, an area we’ve wanted to improve upon for a long time. We have your ruler in the interface, we have your realm on the map - but what really connects them? Now you’ll be able to see your monarch, on their throne, actually ruling!  

Kings & Emperors will gain access to the Royal Court, a throne room where their loyal subjects can gather, where glorious artifacts can be put on display, and where the ruler can Hold Court in order to deal with the troubles and wishes of the realm. Similarly to medieval rulers of old, you can aspire to have the Grandest court in the world, or perhaps simply live up to the expectations put on you by your peers - no one respects a stingy monarch!  

With the Royal Court, we want to immerse you in the life of a medieval ruler by letting you take the reins and experience rulership first-hand. You’ll not only see your ruler occupy the same space as your family and subjects, but you’ll have the opportunity to engage with many new and exciting systems - sponsor projects, spend gold on lavish amenities, solve strife between squabbling courtiers, appoint jesters, and much more! How will you rule *your* realm?  

And what is a ruler without subjects, their people? After all, it's they who pay the taxes! Much like with faiths, cultures will be made more interesting and malleable - all in line with our vision of *Player Freedom and Progression.*  

Different cultures will have different traditions, different opinions of each other, and even shift and change with time. No longer will cultures be static and similar - we want to give you, the player, the freedom and possibility to shape your own culture and guide its progress in a variety of exciting ways. Of course, culture will change at a slower pace than Faiths do - it’ll be gradual over time, tradition by tradition. Though sometimes larger shifts can occur due to isolation, or as the result of two different cultures intermingling.  

Grow the acceptance between cultures in your realm, diverge your culture to adopt a new Ethos, or create a Hybrid between two cultures in your realm - adopting the language, traditions and aesthetic choices you find the most compelling. There are many possibilities to explore, and no two games will ever look the same again!  

All of this is a big undertaking, as it breaks new ground for the game in more than one way! It’s going to take a little bit longer, but as we get closer to launch we’ll start sharing many more details - both on what’s been mentioned here as well as other things coming in the expansion. We hope you’re excited to join us on this journey!  

You can expect the expansion to release later this year.

<!-- artifact:reactions:start -->
- 256 Love
- 132 Like
- 15 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 3 Haha
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
