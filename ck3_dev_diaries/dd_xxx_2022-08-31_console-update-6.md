---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1540343/"
forum_thread_id: 1540343
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: CK3 - Console Update 6
dd_date: 2022-08-31
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
body_word_count: 1329
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1540343'
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
    location: raw_lines_241_to_243
    action: preserved_and_flagged
    counts:
      Like: 6
      (unlabeled — rendered as base64 data URI): 5
      Love: 2
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_272_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 - Console Update 6

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Aug 31, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/)
- [2](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/page-3)
[Next](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/page-2)

1 of 3

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/page-3 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/?prdxDevPosts=1)

[![PDX_Pariah](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/s/paradox5.png)](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

#### [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

##### Community Manager

Jul 21, 2020

119

4.454

[](javascript:;)

- [Aug 31, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/post-28446406)


- [/forum/threads/ck3-console-update-6.1540343/post-28446406](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/post-28446406)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28446406/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-console-update-6.1540343/post-28446406)

Howdy all!  

As you know, our team at Lab42 has been hard at work compiling and addressing all the feedback and reports that you have made in the past few months. While not every single report makes into production, we have been keeping track and working on making sure as many issues as possible are being addressed.  

With that in mind, we are proud to announce that Console Update 6 is now available! As always, we recommend that you finish your current game before updating and make sure your saves are fresh when you start a new game after updating.  

Without further ado, here is your Changelog:  


Spoiler: Console Update 6 Changelog

- A fix has been implemented to the war armour of the characters in the barbershop so they are sharper and more defined.
- Improved the Notifications in the Notification Panel sometimes showing the wrong tooltip after exiting advanced tooltip mode.
- Fix for "Open Legacies" text in the Dynasty window. Should now be more readable as the text is larger and white.
- Updated "Search for Physician" decision popup window to display the correct colour and font.
- Fixed the text in the "House" tab in the "Dynasty" window. Text is now clearer and "Dead House" text and background now fits the window correctly.
- Fix for text colour and general small UI fixes in the Dynasties window. Text is now clearer, fixed some overlapping UI for the Progress Bars on the legacies and along the bottom of the scrollbar.
- Updated the Tenets in Create Faith to help navigate the menu, such as which Tenet you have selected and which one isn't available to select
- Minor visuals updates of the 'Holy Sites'.
- Minor visual updates to the "Other Faiths" screen have been made.
- Updated the text and UI of the Fervor section in the Other Faiths tab to be easier to navigate.
- Made several small visual improvements to the Domain menu.
- The Martial heading value now displays correct skill total value, previously was displaying the value for Stewardship instead.
- Increased size of skill header and set the text to be bold to improve readability, and set the bracketed text to be gray italic to match our design documents.
- Moved base skill value text into the same block as the other skill value modifiers to match our design documents.
- Changed Base: "value" text to be bold white, was originally bold gray.
- Added bullet points to the skill value and effects breakdowns to make it clear that they are part of a list and to match our design documents.
- A visual update has been made to the Grant Vassal menu.
- Minor update on the visuals of the "Host as Honored Guest" screen.
- Added in a new dim background that shifts focus to the message box when a new player joins the multiplayer game.
- Added in a new dim background that shifts focus to the message box when attempting to kick a player.
- Updated the Exit Window for Multiplayer so it is much clearer to see.
- Updated the UI in the Create Faith menu to remove purple lines that were present when viewing the menu.
- Updated the scroll bars in the barbershop drop down menus to ensure they are the correct size.
- Made the text in the Letter Event popup scrollable with the right analogue stick.
- Update text on "Out of Storage" window, while saving the game.
- Updated the settings screen to reduce the empty space above the `Controls` button.
- Fixed an issue where the player couldn't close the Faith Conversion window unless they were highlighting the Convert to Faith button.
- Fixed the layouts of the Mass Action buttons in the Prisoners tab so they are no longer scrambled.
- Fix for Japanese play as any ruler Text. The text appearing on the right panel in play as any ruler screen with no character selected now wont overflow the window and be more readable.
- Updated localization for various languages to include if a player has an active raid in the raid tooltip or the player has reached the end.
- Updated the New Game screen to ensure the date tab animations display correctly.
- Fixed the Demand Council Position window so it is gamepad navigable.
- Improved the formatting of texts in the Military sub menu to make it easier to read.
- Visual update for Military Tab in Active Wars Banner
- Visual update for Change Title Name Popup
- Visual update for Changed Title Popup text.
- Visual update for background of title in Titles Menu
- Added a backing box for 'Capital' in the titles tab.
- Visual update for Changed Title Popup text.
- Visual update for background of title in Titles Menu
- Added a backing box for 'Capital' in the titles tab.
- Added Support for JP localization to all SKUs.

With all that in mind, we are still gathering your input and feedback and making sure we address them, so keep that feedback flowing! Until then, we look forward to all the fantastic adventures and interesting tales you have from game.  

Cheers for now,  

-SP

<!-- artifact:reactions:start -->
- 6 Like
- 5 (unlabeled — rendered as base64 data URI)
- 2 Love
<!-- artifact:reactions:end -->
