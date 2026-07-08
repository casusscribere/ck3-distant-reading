---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1487491/"
forum_thread_id: 1487491
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 69
title: "Dev diary #69 - Nice, Throne Room Artifacts!"
dd_date: 2021-08-17
author_handle: Carlberg
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2651
inline_image_count: 12
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1487491'
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
    location: raw_lines_380_to_381
    action: preserved_and_flagged
    counts:
      Like: 25
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_458_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev diary #69 - Nice, Throne Room Artifacts!

<!-- artifact:thread_metadata:start -->
- Thread starter [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)
- Start date [Aug 17, 2021](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/ "CK3 Dev Diary #68 - Inspiration Never Dies") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-70-the-facts-about-artifacts.1488487/ "Dev Diary #70 - The Facts about Artifacts")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/?prdxDevPosts=1)

- [Aug 17, 2021](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/post-27739153)
- [Replies: 145](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/#posts)


- [/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/post-27739153](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/post-27739153)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27739153/bookmark "Bookmark")

Hello everyone!  

In this dev diary it is time for us to have a look at some of the artifacts that you may come across, steal or create yourself for your Royal Court. With the introduction of the new throne room scenes we are for the first time in Crusader Kings taking a step into the interiors of our courts. This has given us an opportunity to move artifacts from only being seen as 2D icons in an inventory screen like in CKII, to being visual 3D objects you can show off to increase the grandeur of your court, or give it your own flair.  

Also, as always, the pictures in this dev diary are of work in progress.  
​

## Artifacts presented in your court​

Within your court you will be able to show off the artifacts in your possession, from the smaller artifacts on pedestals and reliquaries holding the venerated remains of saints, to fine martial weapons forged or taken, to grand statues or fine furniture. These artifacts can be equipped in a number of slots around your court rooms for viewing of the ruler and his guests. Below is a small selection of the smaller artifacts, usually presented on different pedestals befitting your court.​


![DD69_tome.jpg](https://forumcontent.paradoxplaza.com/public/736266/DD69_tome.jpg "DD69_tome.jpg")


*A Pratiharan volume about revelry.*  

![DD69_reliquary.jpg](https://forumcontent.paradoxplaza.com/public/736268/DD69_reliquary.jpg "DD69_reliquary.jpg")


*A reliquary containing a piece of the crown of thorns, you think.*  

![DD69_urn.jpg](https://forumcontent.paradoxplaza.com/public/736270/DD69_urn.jpg "DD69_urn.jpg")


*A fine urn taken from the Abbasid court.*  

![DD69_ivory_box.jpg](https://forumcontent.paradoxplaza.com/public/736271/DD69_ivory_box.jpg "DD69_ivory_box.jpg")


*A chest of valuables made in the finest of ivory*  
​

## Designing artifacts of the middle ages​

The artifacts we’ve added to the game cover a variety of different categories, small and large, and even to adorn your walls. The creation of these artifacts have gone through a few stages of development before making it into the Royal Court.  

**Research**  
As in all our games we go through a stage of historical reference hunting to find artifacts relevant to the time period and within the cultures we are depicting. This can be both easy at times and complicated at others depending on the amount of material that has survived the decay or been documented since the middle ages.​


![DD69_ivory_chest_references.jpg](https://forumcontent.paradoxplaza.com/public/736272/DD69_ivory_chest_references.jpg "DD69_ivory_chest_references.jpg")


*Carved and painted Ivory chests.*​


During this stage we both look at the aesthetics and historical references we can find and verify. When references are sparse, we still try to extrapolate good looking and aesthetically plausible designs. However in some cases like in the Middle East and other areas there is for example close to no and at best sparse levels of statues or paintings of people. Depending on where this can be for religious or cultural reasons and in those cases where other cultures would show human statues, we’ve instead shifted to area appropriate symbolisms, patterns and art.  
​

![DD69_statue.jpg](https://forumcontent.paradoxplaza.com/public/736275/DD69_statue.jpg "DD69_statue.jpg")

![DD69_birdie.jpg](https://forumcontent.paradoxplaza.com/public/736274/DD69_birdie.jpg "DD69_birdie.jpg")


*A marble statue from southern Europe, and an islamic golden falcon.*  
​

**Creation**  
While using reference images is an easy task to do, we must also consider the original state of the artifact, since a reference from today could be of a possibly 800 years or more old object. So grime, damage and aging needs to be reconsidered and balanced, while still keeping the object in a used looking state. An artifact could still be owned by a ruling family for long enough to become an antique in its own time.  

*![DD69_cabinet.jpg](https://forumcontent.paradoxplaza.com/public/736276/DD69_cabinet.jpg "DD69_cabinet.jpg")


An icon clad cabinet, don't tell the iconoclasts!*  
​

### Dynamic objects​

Banners and some other items in the court have shader support to show the ruler's own flair, since they would be made to the ruler's specifications. The banners below for example read in the primary title held by the ruler to show off your heraldry.​


![DD69_banners_a.jpg](https://forumcontent.paradoxplaza.com/public/736277/DD69_banners_a.jpg "DD69_banners_a.jpg")

![DD69_banners_b.jpg](https://forumcontent.paradoxplaza.com/public/736278/DD69_banners_b.jpg "DD69_banners_b.jpg")


*What is a lord without his banner to display his Coat of Arms?*  
​

There are also tapestries, where we use a similar system to the clothing shaders to generate interesting patterns and designs to adorn those stone walls in your great halls.​


![DD69_tapestry_a.jpg](https://forumcontent.paradoxplaza.com/public/736279/DD69_tapestry_a.jpg "DD69_tapestry_a.jpg")

![DD69_tapestry_b.jpg](https://forumcontent.paradoxplaza.com/public/736281/DD69_tapestry_b.jpg "DD69_tapestry_b.jpg")


*Bringing some color to the hard stone walls in your halls.*  
​

And that brings this dev diary to an end, we will be showing off more of the courts in the future!  

​

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27739153/report)

Click to expand...

[![Carlberg](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/m/pdx_avatar_big.png)](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)

Written by

### [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)

Senior Environment Artist

***Paradox Staff******40 Badges***

-

Messages
221

-

Reaction score
2.288

- [1](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [8](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/page-8#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/page-2#posts)

1 of 8

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/page-8#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/?order=prdx_dd_reaction_score)

[![Trunting](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/majesty2_avatars/Heroes/s/majesty2_avatar_63.png)](https://forum.paradoxplaza.com/forum/members/trunting.476240/)

#### [Trunting](https://forum.paradoxplaza.com/forum/members/trunting.476240/)

##### General

**95 Badges**

Apr 14, 2012

1.943

4.742

- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Semper Fi](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/sefi.png "Semper Fi")
- ![Rome Gold](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/RomeGold.png "Rome Gold")
- ![Hearts of Iron III Collection](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi3col_medal.png "Hearts of Iron III Collection")
- ![Hearts of Iron III: Their Finest Hour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/TFH_forumicon.png "Hearts of Iron III: Their Finest Hour")
- ![For the Motherland](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FTM1.png "For the Motherland")
- ![Hearts of Iron III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi3_forum_icon.gif "Hearts of Iron III")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Age of Wonders: Planetfall - Revelations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoWrevelationsicon.png "Age of Wonders: Planetfall - Revelations")
- ![Imperator: Rome Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorsignup.png "Imperator: Rome Sign Up")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Europa Universalis IV: Dharma](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/dharmaicon.png "Europa Universalis IV: Dharma")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")
- ![Europa Universalis IV: Cradle of Civilization](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EUIV_CoC.png "Europa Universalis IV: Cradle of Civilization")
- ![Age of Wonders II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoW2_forum_badge.png "Age of Wonders II")
- ![Age of Wonders](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoW1_forum_badge.png "Age of Wonders")
- ![Age of Wonders III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoW3_forum_badge.png "Age of Wonders III")
- ![Tyranny - Bastards Wound](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Tyr_bw.png "Tyranny - Bastards Wound")
- ![Hearts of Iron IV: Death or Dishonor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4DoD.png "Hearts of Iron IV: Death or Dishonor")
- ![Europa Universalis IV: Mandate of Heaven](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/moh_forum_icon.png "Europa Universalis IV: Mandate of Heaven")
- ![Crusader Kings II: Monks and Mystics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/monksandmystics.png "Crusader Kings II: Monks and Mystics")
- ![Hearts of Iron IV: Together for Victory](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4Tfv.png "Hearts of Iron IV: Together for Victory")
- ![Stellaris: Leviathans Story Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/leviathans.png "Stellaris: Leviathans Story Pack")
- ![Hearts of Iron IV: Battle for the Bosporus](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/bftb.png "Hearts of Iron IV: Battle for the Bosporus")
- ![Hearts of Iron IV: No Compromise No Surrender](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/NCNS.png "Hearts of Iron IV: No Compromise No Surrender")
- ![Hearts of Iron IV: Graveyard of Empires](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/goe_forum_icon.png "Hearts of Iron IV: Graveyard of Empires")
- ![Hearts of Iron IV: Götterdämmerung](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gtd.png "Hearts of Iron IV: Götterdämmerung")
- ![Hearts of Iron IV: Arms Against Tyranny](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AAT_forum_icon_16x16.png "Hearts of Iron IV: Arms Against Tyranny")
- ![Hearts of Iron IV: No Step Back](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/NSB_forum_icon_16x16.png "Hearts of Iron IV: No Step Back")
- ![Hearts of Iron IV: By Blood Alone](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BBA_forum_icon_16x16.png "Hearts of Iron IV: By Blood Alone")
- ![Victoria 3 Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v3_signup_forum_icon.png "Victoria 3 Sign Up")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Age of Wonders: Planetfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aowstandard.png "Age of Wonders: Planetfall")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Imperator: Rome - Magna Graecia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MagnGraeciaIcon.png "Imperator: Rome - Magna Graecia")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Hearts of Iron IV: La Resistance](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoILRicon.png "Hearts of Iron IV: La Resistance")
- ![Tyranny: Archon Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tyr_arc.png "Tyranny: Archon Edition")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Age of Wonders: Planetfall Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/planetfallsignup.png "Age of Wonders: Planetfall Sign Up")
- ![Tyranny: Gold Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tyr_ove.png "Tyranny: Gold Edition")
- ![Darkest Hour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DHicon.gif "Darkest Hour")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Victoria 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2.png "Victoria 2")
- ![Warlock 2: The Exiled](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/warlock2_forum_icon.png "Warlock 2: The Exiled")

[](javascript:;)

- [Aug 17, 2021](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/post-27739383)


- [/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/post-27739383](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/post-27739383)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27739383/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/post-27739383)

The throne room is here!  

The artifacts look really nice.  

Is there an artifact limit per ruler?

<!-- artifact:reactions:start -->
- 25 Like
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
