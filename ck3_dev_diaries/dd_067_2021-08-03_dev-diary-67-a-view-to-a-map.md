---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1484762/"
forum_thread_id: 1484762
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 67
title: "CK3 Dev Diary #67 - A View to a Map"
dd_date: 2021-08-03
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
body_word_count: 1940
inline_image_count: 5
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1484762'
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
    location: raw_lines_~28_to_126
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_128_to_129
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_311_to_312
    action: preserved_and_flagged
    counts:
      Like: 55
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_389_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #67 - A View to a Map

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Aug 3, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/ "CK3 Dev Diary #66 - A Fresh Coat of Paint") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/ "CK3 Dev Diary #68 - Inspiration Never Dies")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/?prdxDevPosts=1)

- [Aug 3, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/post-27711878)
- [Replies: 161](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/#posts)


- [/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/post-27711878](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/post-27711878)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27711878/bookmark "Bookmark")

**CK3 Dev Diary #67 - A View to a Map**​


Greetings!  

The team is slowly coming back together after a well deserved summer vacation. Today, let’s have a look at what we’ve been doing to the culture setup and some small scale map tweaks. Most of the work we’ve spent on cultures has naturally gone into the cultural overhaul itself, but we have made some general improvements as well, most notably over in India.  

Starting with a small culture addition in southern Europe, and that some of you keen eyed readers noticed back in a previous dev diary, we’ve added back a fan favorite from CK2; Carantanian. The culture is quite extensive on game start and covers most of south-eastern Bavaria. From a historical point of view, the culture is of a west slavic origin, but as they got cut off from their ancestral brethren in the Carpathian Basin, they became gradually closer to the south slavic peoples. We represent this by Carantanian having a West Slavic Heritage, but speaking a South Slavic Language.  

![01_carantanian.jpg](https://forumcontent.paradoxplaza.com/public/732728/01_carantanian.jpg "01_carantanian.jpg")


*[Image of Carantanian culture]*​


Next, I’ll hand it over to our local India expert, [@Trin Tragula](https://forum.paradoxplaza.com/forum/members/18587/), to talk about (you guessed it) India!  

**Indian Culture Changes**  
The culture rework has been a good opportunity to rework the cultures in India a bit. The current setup here is one we inherited from Crusader Kings 2 and it was in some ways not entirely appropriate for our era. To better reflect the diversity of the subcontinent we have added two new cultures, changed the old ones a bit and also added a great number of potential culture names for when the large starting cultures diverge.  

First of all we have gotten rid of Hindustani culture, and two new cultures have been broken away from what it used to cover in the south. The core part of the culture covers the Gangetic plain, and is now known as Kannauji after the Imperial city of Kannauj (Kanyakubja) which was the main prize of the region and often gave its name to it.  

Hindustani itself is still around in a way, as a possible name for a cultural hybrid between an Iranian or Turkic culture with one of the north indian cultures.  

![02_cultures_in_india.jpg](https://forumcontent.paradoxplaza.com/public/732729/02_cultures_in_india.jpg "02_cultures_in_india.jpg")


*[Image of the cultures in northern India]*​


Starting in the central parts of India the newly added Gond culture has been carved out of areas that were previously Hindustani, Marathi or Oriya. In 1066 most Gond counties are under the control of the Cedi kingdom and many of these counties are now also tribal at start. This culture covers a region that was in an odd place in the old setup, at the border of several cultures but not quite belonging to either of them.  

![03_gond.jpg](https://forumcontent.paradoxplaza.com/public/732730/03_gond.jpg "03_gond.jpg")


*[Image of the Gond culture]*​


Covering the Malwa plateau as well as some of the adjacent regions that were previously considered Hindustani. This new culture shares a language with the Rajasthani and Gujarati cultures, Gurjar Apabhramsa. The existing Rajput culture has been renamed to Rajasthani (since Rajput as a cultural distinction does not really fit our start date) and Assamese is now known as Kamrupi.  

![04_malvi.jpg](https://forumcontent.paradoxplaza.com/public/732731/04_malvi.jpg "04_malvi.jpg")


*[Image of the Malvi culture]*​


**Indian History and Title Improvements**  
While looking over the subcontinent it was also clear that in some areas the title setup was also better suited for the early modern era, rather than the medieval era around Crusader Kings III start dates. A number of baronies have been renamed and reorganized into new counties, and a number of new vassals have been scripted in, especially for the 1066 start.  
The starting presumptions about who controlled what in 1066 have also been revisited to bring things better in line with history and create a more interesting start. There are now more starting characters, both independent and vassals, and most kings will no longer start above their domain limit.  

Some things like the crisis of the Chola empire should also be a bit better represented in the initial setup, with strong and somewhat unruly Pandya vassals, a much stronger Lankan revolt and the Chera Raja now independent (with his historical vassals to support him). You can now also play as the future king, Kulottunga.  
There are also other, minor changes, such as revisiting the extent of cultures like Kashmiri, and Telugu, and assigning a number of tribal counties in the eastern-central part of the subcontinent.  

![05_sinhalese_rebellion.jpg](https://forumcontent.paradoxplaza.com/public/732732/05_sinhalese_rebellion.jpg "05_sinhalese_rebellion.jpg")


*[Image of the Sinhalese rebellion in 1066]*​


That concludes today’s dev diary. Until next time!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27711878/report)

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

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [9](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/page-9#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/page-2#posts)

1 of 9

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/page-9#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/?order=prdx_dd_reaction_score)

[![TheMind](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/ck3/s/avatar_30.png)](https://forum.paradoxplaza.com/forum/members/themind.1417396/)

#### [TheMind](https://forum.paradoxplaza.com/forum/members/themind.1417396/)

##### Major

**12 Badges**

Apr 8, 2019

581

1.299

- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![Age of Wonders III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoW3_forum_badge.png "Age of Wonders III")
- ![Surviving Mars: Digital Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_DDE.png "Surviving Mars: Digital Deluxe Edition")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Imperator: Rome Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorsignup.png "Imperator: Rome Sign Up")
- ![Imperator: Rome - Magna Graecia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MagnGraeciaIcon.png "Imperator: Rome - Magna Graecia")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")

[](javascript:;)

- [Aug 3, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/post-27712107)


- [/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/post-27712107](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/post-27712107)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27712107/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/post-27712107)

Great improvements!  
One question: when we will know something more detailed about the Royal Court itself?

<!-- artifact:reactions:start -->
- 55 Like
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
