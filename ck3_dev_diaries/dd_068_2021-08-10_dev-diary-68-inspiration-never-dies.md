---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1485460/"
forum_thread_id: 1485460
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 68
title: "CK3 Dev Diary #68 - Inspiration Never Dies"
dd_date: 2021-08-10
author_handle: Servancour
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2262
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1485460'
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
    location: raw_lines_317_to_319
    action: preserved_and_flagged
    counts:
      Like: 6
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 1 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_347_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #68 - Inspiration Never Dies

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Aug 10, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/ "CK3 Dev Diary #67 - A View to a Map") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/ "Dev diary #69 - Nice, Throne Room Artifacts!")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/?prdxDevPosts=1)

- [Aug 10, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/post-27724167)
- [Replies: 174](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/#posts)


- [/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/post-27724167](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/post-27724167)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27724167/bookmark "Bookmark")

**CK3 Dev Diary #68 - Inspiration Never Dies**​


As you may already know, artifacts are making a triumphant return in Royal Court. The artifacts themselves will be familiar to those of you who have used them in CK2, but how you actually get your hands on them will be slightly different. As such, I won’t talk much about the artifacts themselves for now, but I’ll be going over one of the major ways of how you will acquire artifacts.  

Characters throughout the world can gain what we call an *inspiration*. Inspirations come about as a character is seeking to create something extraordinary, resulting in the character wanting to pursue the means of realizing their inspiration. They may want to write a great tome of knowledge, weave a tapestry, or forge a magnificent crown! There are many different kinds of inspirations, all resulting in various types of artifacts upon completion. An inspiration can be broad, such as someone wanting to merely forge a weapon, or very specific like a character wanting to forge a sword.  

![01_inspiration.jpg](https://forumcontent.paradoxplaza.com/public/734299/01_inspiration.jpg "01_inspiration.jpg")


*[Image of a character with an active inspiration]*​


Inspirations only occur for landless characters. We want to extend the immersion of guests and courtiers by making them valuable to you even if you have no desire to push their claims, or use their skills as a councillor. Inspired characters will travel the world, from court to court, seeking a wealthy monarch to sponsor them and their creation. Realms with a high grandeur will be able to attract inspired characters more frequently than those with low grandeur. Granting them a higher chance at receiving skilled craftsmen that will be able to forge an artifact to meet your expectations.  

Once an inspired character arrives at your court, you can choose to sponsor them by giving them the gold they ask for. A skilled character will demand larger amounts of gold, but will also yield better results in creating an artifact. *Most* of the time at least. No one is infallible after all. The skill that is relevant depends on the type of artifact they want to make. For example, a weapon and the quality it gets is dependent on the character’s Martial and Prowess skill. Writing a book, on the other hand, scales with Learning.  

![02_fund_inspiration.jpg](https://forumcontent.paradoxplaza.com/public/734300/02_fund_inspiration.jpg "02_fund_inspiration.jpg")


*[Image of the Fund Inspiration interaction]*​


After funding an inspiration, it will take some time for the character to create the artifact. During the creation progress various situations can happen, such as the character asking for better materials to work with. Below you’ll find such an example, in which my inspired character finds excellent material at the local market. Approve their request and pay for the material, and you’ll increase the overall quality of the artifact they’ll produce.  

![03_highest_quality.jpg](https://forumcontent.paradoxplaza.com/public/734301/03_highest_quality.jpg "03_highest_quality.jpg")


*[Image of an inspiration event: Highest Quality]*​


An inspiration gains progress similar to that of a scheme. You’ll gain progress depending on a chance each month, making the actual time it takes to complete vary. Once the inspiration reaches full progress, the character will approach you to present their creation.  

![04_inspiration_realized.jpg](https://forumcontent.paradoxplaza.com/public/734302/04_inspiration_realized.jpg "04_inspiration_realized.jpg")


*[Image of an inspiration being completed]*​


Mind you, this is not the only way in which you can get an artifact. Inspirations exist to serve as the most significant means of doing so, since they will generally grant you artifacts of a higher quality. You can still get artifacts by other means, such as getting them in events. I hope you enjoyed this brief look into how an artifact can come about. Stay tuned for more information regarding the Royal Court!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27724167/report)

Click to expand...

[![Servancour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/obsolete/m/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/servancour.465268/)

Written by

### [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)

Game Designer

***Paradox Staff******4 Badges***

-

Messages
1.606

-

Reaction score
9.949

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [9](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/page-9#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/page-2#posts)

1 of 9

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/page-9#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/?order=prdx_dd_reaction_score)

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

- [Aug 10, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/post-27724559)


- [/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/post-27724559](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/post-27724559)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27724559/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/post-27724559)

Don't forget to have a look at our [**FAQ Royal Court**](https://forum.paradoxplaza.com/forum/threads/ck3-royal-court-faq-developer-diaries-q-a-important-information.1475394/), containing all the current known details about the upcoming CK3 Expansion!

 

Toggle signature

**Ex-Community Ambassador for Crusader Kings III  
►** *[Twitter Nicou](https://twitter.com/NicouLenny)*

- 10

<!-- artifact:reactions:start -->
- 6 Like
- 3 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
