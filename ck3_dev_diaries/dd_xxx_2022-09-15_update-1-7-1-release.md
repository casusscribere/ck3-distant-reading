---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1542515/"
forum_thread_id: 1542515
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: CK3 - Update 1.7.1 - Release
dd_date: 2022-09-15
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
body_word_count: 1122
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1542515'
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
    location: raw_lines_126_to_128
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_247_to_249
    action: preserved_and_flagged
    counts:
      Like: 51
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 1 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_309_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 - Update 1.7.1 - Release

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Sep 15, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/)
- [2](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/page-3)
[Next](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/page-2)

1 of 3

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/page-3 "Last")

[![PDX_Pariah](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/s/paradox5.png)](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

#### [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

##### Community Manager

Jul 21, 2020

119

4.454

[](javascript:;)

- [Sep 15, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/post-28477008)


- [/forum/threads/ck3-update-1-7-1-release.1542515/post-28477008](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/post-28477008)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28477008/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-update-1-7-1-release.1542515/post-28477008)

Howdy all!  

Today we have released Update 1.7.1 which includes a lot of changes to issues that you have been reporting and a few that we found on our own!  

Please note that we are aware of the "Missing Faces" issue that some of our Community are facing and while it is not being addressed with 1.7.1, there is an update [HERE!](https://forum.paradoxplaza.com/forum/threads/missing-faces-issue.1542526/)  

Without much further ado, here is the changelog:  

Spoiler: 1.7.1 Changelog

AI:  


- AI can no longer hire and fire court position in the same decision cycle, this should fix the issue where AIs could end up in massive prestige deficits

Balance:  


- Slightly relaxed requirements for Reviving Taltoism to make it not entirely impossible in 1066
- Crusade Targeting - Fixed so that Crusades check for current military strength when excluding target kingdoms instead of max military strength
- Crusade Targeting - Completely rebalanced Crusade Kingdom Selection; while Jerusalem will still be the most attractive target (for Christians), there will now be much more variation in targets and a faith will tend to defend what is assigned to be their Heartlands to a much greater degree
- Crusade Targeting - Distance is now a much greater factor when determining a crusade target
- Crusade Targeting - Catholic Crusades are now much less likely to select a kingdom in the African interior, and slightly less likely to pick a north African kingdom (if the Holy Land is taken, we want the crusades to focus on going deeper into the middle east rather than to die from attrition in the Sahara)

Bugfix:  


- Fixed crashes related to loading save files from previous game versions
- Crusade Targeting - Fixed so that Crusades cannot target an area below 5 counties in size
- AI House members in Feuds will now be much more likely to start schemes against their enemies
- Characters will now be more reluctant to allow Feud enemies to raise their children
- Characters will now be more likely to join schemes against Feud house members
- Added explanation of score tooltip when ending a Feud
- Feuds can now only be started against Houses with at least 5 adult members and with Heads within one title tier of your own
- Added 25 year cooldown between Feuds
- Reduced frequency of Feud start events
- Added explanation of Feud reward modifiers to encyclopedia entry
- Fixed Feuds starting from murders where the murderer is still a secret
- Fixed an issue where Unpredictable Economical AI's didn't build enough new holdings
- Handle dead/alive for memories more consistently
- Fixed an issue where Cautious Economical AI's weren't cautious enough in the early stages of the game
- Fixed yearly.9110 missing an equals sign, also adjusted down dynasty prestige
- Fixed a missing equals sign in the Loyalty trait definition
- Fixed bp1_yearly.5704 missing an is_adult check
- Fixed pilgrimage.6007 so it does not fire for blind characters
- Fixed issue where Feud scale tip tooltips would be repeated
- Added additional missing checks for the A Man in Our Bed event
- Fixed missing adult and other checks in the A Man in Our Bed event
- Fixed Guanche Vaulter Infantry leaping across the world as mercenaries
- Fixed rivals not being less likely to accept alliance proposals
- Fixed Vengeance event firing alongside At My Mercy for Norse characters who captured a rival in battle
- Fixed incorrectly displayed/repeating Coat of Arms during longer sessions

Localization:  


- Fixed MAX_RECURSIVE_DEPTH error in Chinese localization
- Fixed grammar of Ibn Marwan of Badajoz's bookmark character


With that out of the way, keep up the reports, keep checking out our socials for further info, and we will keep working hard on our next updates and news for the future!  

-SP

<!-- artifact:reactions:start -->
- 51 Like
- 14 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
