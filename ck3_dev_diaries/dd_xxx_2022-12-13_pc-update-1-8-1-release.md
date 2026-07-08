---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1561920/"
forum_thread_id: 1561920
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: CK3 - PC Update 1.8.1 - Release
dd_date: 2022-12-13
author_handle: pdxhr
expansion: Friends and Foes
patch: Patch 1.8 (Robe)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 745
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1561920'
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
    location: raw_lines_203_to_206
    action: preserved_and_flagged
    counts:
      Like: 44
      Love: 7
      (unlabeled — rendered as base64 data URI): 5
      Haha: 1
    note: Reactions block parsed; 3 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_244_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 - PC Update 1.8.1 - Release

<!-- artifact:thread_metadata:start -->
- Thread starter [pdxhr](https://forum.paradoxplaza.com/forum/members/pdxhr.1709208/)
- Start date [Dec 13, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/)
- [2](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/page-2)
[Next](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/page-2)

1 of 2

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/page-2 "Last")

[![pdxhr](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/Female_Advisors_EUIV/s/naval_reformer_female.png)](https://forum.paradoxplaza.com/forum/members/pdxhr.1709208/)

#### [pdxhr](https://forum.paradoxplaza.com/forum/members/pdxhr.1709208/)

##### Recruit

Nov 24, 2022

3

151

[](javascript:;)

- [Dec 13, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/post-28675614)


- [/forum/threads/ck3-pc-update-1-8-1-release.1561920/post-28675614](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/post-28675614)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28675614/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-pc-update-1-8-1-release.1561920/post-28675614)

Hi again,  

Let me bring forth the **Update 1.8.1**, which addresses some issues that have been reported by the community and the CK3 team. This will fix the frustrating issue of modals/pop-ups getting stuck on the screen and ensure height maps get rendered properly in some of our beloved community mods.  

As always, please keep us posted on your experiences, and thank you for constituting this group that is the beautiful community of CK3. Without your enthusiasm, eagle-eyed sense of detail, and sharp-tongued reminders of releasing the next update, we'd feel quite alone in the process of doing so. Well, that is me rambling again. To the list of changes:  


Spoiler: 1.8.1 changelog

###################  
# Fixes  
###################  


- Fixed an issue where tooltips were not affected by the tooltip unlock setting, leading to tooltips staying open for a prolonged period of time
- Achievements will no longer become disabled when going back from the pick any character screen
- Height maps should now be rendered as expected when generated (affected mod creation)
- Fixed an issue where any religion spawning a heresy could force the player to adopt that heresy, regardless of player religion
- Added missing localization for the Renderer settings tooltip
- The Truth is Relative perk no longer lowers the chance of finding real secrets significantly (except if the Spymaster has the Lazy trait...)
- Fixed incorrect localization for the “Become rivals with a rival’s family member” memory


-HR (Not the Dept. of Hermeneutic Research)

<!-- artifact:reactions:start -->
- 44 Like
- 7 Love
- 5 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->
