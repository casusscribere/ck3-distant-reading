---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1516699/"
forum_thread_id: 1516699
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 3
title: "Console DD #3: UI/UX and Controls"
dd_date: 2022-03-22
author_handle: PDX_Pariah
expansion: Console Edition
patch: Crusader Kings III Console Edition
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1144
inline_image_count: 9
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1516699'
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
    location: raw_lines_215_to_218
    action: preserved_and_flagged
    counts:
      Like: 34
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 1 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_226_to_326
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_327_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Console DD #3: UI/UX and Controls

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Mar 22, 2022](https://forum.paradoxplaza.com/forum/developer-diary/console-dd-3-ui-ux-and-controls.1516699/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/console-dd-3-ui-ux-and-controls.1516699/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/console-dd-3-ui-ux-and-controls.1516699/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/console-dd-3-ui-ux-and-controls.1516699/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-91-update-1-5-1-1.1516821/ "CK3 Dev Diary #91: Update 1.5.1.1") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-4-tech-optimization-ps-exclusive-features.1517990/ "CK Console DD #4: Tech Optimization &amp; PS Exclusive Features")

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1897.jpg?1647899089)

# Console DD #3: UI/UX and Controls

- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Mar 22, 2022](https://forum.paradoxplaza.com/forum/developer-diary/console-dd-3-ui-ux-and-controls.1516699/)

Howdy y'all!  

We are glad to announce that we have a fantastic Dev Diary from our friends at Lab42 where we will cover the long anticipated and much sought after UI and UX for the Console version releasing soon! Lab42 have been hard at work and there is not much time left until release, so we hope you enjoy the information and vision they have presented for you. Now with screenshots!  

As you would expect, user interface and controls were core components of the adaptation from PC to console. One of the main aims was to create a UI that was easily accessible and facilitated fluid gameplay. There is no set standard for UI and controls for Grand Strategy Games on console, with most approaches being subjective and as a consequence we’ve taken an approach that suited the unique Crusader Kings Gameplay.  

![CK3_XBOXSX_10_Papermap.png](https://forumcontent.paradoxplaza.com/public/808670/CK3_XBOXSX_10_Papermap.png "CK3_XBOXSX_10_Papermap.png")


[Map Overview and controls]  

This started with a control hierarchy that marries UI and button control placement, for example ... using shoulder buttons for the top tier menus – the Command Bar – and bumpers to tab between sub-menus within the main menus. In addition, the decision was taken to assign controls to unique game functions rather than using lots of contextual buttons. Control prompts specific to each menu, screen / game context are displayed at the bottom of the screen to assist the user. The aim is to provide the player with a lexicon of controls that when learnt facilitate fluid interaction with the game UI and functionality.  

![CK3_XBOXSX_02_EarlAlfred.png](https://forumcontent.paradoxplaza.com/public/808672/CK3_XBOXSX_02_EarlAlfred.png "CK3_XBOXSX_02_EarlAlfred.png")


[Earl Alfred Character View]  

We could've taken a very conservative approach to development, but this was not what Lab42 or Paradox wanted. For example, the conundrum of turning a PC control system and UI into a viable console offering could've involved retaining the PC UI and using the controller thumbstick as a virtual mouse, but this approach was dismissed out of hand. User research also showed how popular the D-Pad was as a means of game navigation, especially when dealing with menus. Moving away from the use of a virtual mouse and freeing up the D-Pad for game navigation (as opposed to invoking menus as used in other console strategy games) presented a new set of challenges to overcome.  

![CK3_XBOXSX_06_FamilyTree.png](https://forumcontent.paradoxplaza.com/public/808680/CK3_XBOXSX_06_FamilyTree.png "CK3_XBOXSX_06_FamilyTree.png")


[Family Tree]  

The UI and controls we've adopted is a hybrid approach, leaning on best in class examples as reference and applying them to the unique CK game framework (e.g. top level onscreen menus (the Command Bar), Radials (Character and Maps), and quality of life shortcuts (e.g. Quick Access Bar, Hints, Notifications).  

![CK3_XBOXSX_05_Council.png](https://forumcontent.paradoxplaza.com/public/808671/CK3_XBOXSX_05_Council.png "CK3_XBOXSX_05_Council.png")


[Council Tab in Top Menu]  

When looking at the Crusader Kings user interface it was clear that most of the community want as much information at their fingertips as possible in order to form and execute game strategy. Flicking between menus, the map and popups is a feature of the PC title that we wanted to retain on console. This is also enhanced by the Radials to access your Character Wheel and another that introduces the Map View Radial accessible at any time from the main gameplay window. Allowing you to quickly change between Map Modes and easily accessing your character features without in-depth menu navigation.  

![CK3_XBOXSX_08_RadialMapWheel.png](https://forumcontent.paradoxplaza.com/public/808673/CK3_XBOXSX_08_RadialMapWheel.png "CK3_XBOXSX_08_RadialMapWheel.png")


[Radial Map Wheel]  

Avoiding the use of lots of fullscreen menus that potentially break the immersion of gameplay was a driver here, and this led to the concept of switching focus being introduced. This essentially allows the gamer to quickly move between any open screen elements as well as allowing easy Map Interaction – a critical component of Crusader Kings gameplay.  

![CK3_XBOXSX_01_StartDate_Character.png](https://forumcontent.paradoxplaza.com/public/808682/CK3_XBOXSX_01_StartDate_Character.png "CK3_XBOXSX_01_StartDate_Character.png")


[Start Date map]  

![CK3_XBOXSX_03_LifestyleMartial.png](https://forumcontent.paradoxplaza.com/public/808683/CK3_XBOXSX_03_LifestyleMartial.png "CK3_XBOXSX_03_LifestyleMartial.png")


[Martial View]  

![CK3_XBOXSX_09_LifestyleDiplomacy.png](https://forumcontent.paradoxplaza.com/public/808684/CK3_XBOXSX_09_LifestyleDiplomacy.png "CK3_XBOXSX_09_LifestyleDiplomacy.png")


[Martial View]  

That does it for the Console portion of the Developer Diary fresh and hot from the Lab42 presses!  

[https://www.youtube.com/embed/tEi0to_urrE?wmode=opaque](https://www.youtube.com/embed/tEi0to_urrE?wmode=opaque)

 

Last edited by a moderator: Mar 22, 2022

<!-- artifact:reactions:start -->
- 34 Like
- 27 (unlabeled — rendered as base64 data URI)
- 12 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)**
Role: Community Manager
Badges: 79
Messages: 119
Reaction score: 4,454

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
