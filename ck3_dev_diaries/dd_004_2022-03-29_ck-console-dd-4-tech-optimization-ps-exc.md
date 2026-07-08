---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1517990/"
forum_thread_id: 1517990
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 4
title: "CK Console DD #4: Tech Optimization & PS Exclusive Features"
dd_date: 2022-03-29
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
body_word_count: 1088
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1517990'
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
    location: raw_lines_178_to_180
    action: preserved_and_flagged
    counts:
      Like: 22
      (unlabeled — rendered as base64 data URI): 6
    note: Reactions block parsed; 1 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_188_to_257
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_258_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK Console DD #4: Tech Optimization & PS Exclusive Features

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Mar 29, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-4-tech-optimization-ps-exclusive-features.1517990/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-4-tech-optimization-ps-exclusive-features.1517990/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-4-tech-optimization-ps-exclusive-features.1517990/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-4-tech-optimization-ps-exclusive-features.1517990/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/console-dd-3-ui-ux-and-controls.1516699/ "Console DD #3: UI/UX and Controls") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-92-anatomy-of-a-game-from-report-to-resolution.1518991/ "CK3 Dev Diary #92: Anatomy of a Game: From Report to Resolution")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-4-tech-optimization-ps-exclusive-features.1517990/?prdxDevPosts=1)

# CK Console DD #4: Tech Optimization & PS Exclusive Features

- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Mar 29, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-4-tech-optimization-ps-exclusive-features.1517990/)

Howdy all!  

Today is the day for our Crusader Kings III release on Next-Gen Consoles! We are very excited and hope you are as well. Once again, our friends over at Lab42 have brought us some wisdom and insight into the process of how the game was created to reflect the performance standards for Xbox Series X|S and Playstation 5.  

Our team in Stockholm is hard at work on the next steps of the PC version and with gathering and taking action on the feedback we have received thus far. Hopefully we will have more information on that side of things for the near future! In the meantime, this Dev Diary is for Console news.  

Today, our Dev Diary will cover technical optimizations as well as console specific features for the Playstation 5. Hopefully this provides some useful information and brings further excitement to your day!  

Without further ado:  

**Technical Optimization and PS Exclusive Features:**  

The adaptation to console brings some natural technical optimisation that comes directly from the features of the current gen consoles. This includes quick loading, which is a welcome feature for Crusader Kings on console. Despite the latest consoles being powerful we still had to be wary of performance so our game held up and was an example of how things should be. As your kingdom grows you end up with a lot of “widgets” in play, so we made sure to focus on optimizing performance and UI flow to keep the game, and the gameplay, running as smoothly as possible. To get certified on consoles is definitely a challenge: quality is very important to our Partners and they are very exacting!  

Game Help & Activities have been utilized on Playstation 5 to assist with on-boarding and signposting for users in game. CK3 is not a linear mission based game, so the inclusion of Activities was not a straightforward implementation but something that was considered to be beneficial for the overall user experience. The use of Haptic feedback from the PS5 DualSense™ controller was implemented to add immersion to the game experience. Major in-game events were given apt haptic feedback and local controller audio, such as major Stress or Death. The longer term aim is to expand on this feature over time to further engage the user and add to the ambience and CK3 setting. The DualSense™ touchpad has also been used to allow the user to pause and un-pause game time as well as increasing and decreasing Game Speed.  

New achievements have been added to the console experience which are designed to add signposting to the game as well as new console specific game challenges. These new achievements are in addition to the wide variety of PC achievements that have been ported to the console game – and certainly provide a challenge for you in the Community to complete over the long term.  

In addition to the features described above, we’ve introduced some quality-of-life functionality that has been specifically designed for the console experience. The Quick Access Bar was introduced to enable seamless access to any active process. This includes fluid interaction with active wars, raised armies, building construction and upgrades, and schemes in progress. We’ve also added an Automated Warfare option which gives army control to the AI. This enables players who do not wish to manage wars manually to select the Automated option, allowing them to focus on alternate strategies like Dynasty building and Intrigue. Alerts and Suggestions are easily accessible through the Hints Menu that can be invoked through a single button press. For those players that want to dig down into the detail of the game, you can use the Auto Tooltips or Advanced Tooltip Mode to improve your knowledge of the CK3 world and refine your strategy and approach to gameplay.  


[https://www.youtube.com/embed/ovG4S_u-4hI?wmode=opaque](https://www.youtube.com/embed/ovG4S_u-4hI?wmode=opaque)

 

Last edited: Mar 29, 2022

<!-- artifact:reactions:start -->
- 22 Like
- 21 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)**
Role: Community Manager
Badges: 68
Messages: 119
Reaction score: 4,454

*[Full game-badge icon list of 16 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
