---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1515647/"
forum_thread_id: 1515647
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 2
title: "CK Console DD #2: Discovery in the Crusader Kings Experience"
dd_date: 2022-03-15
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
body_word_count: 834
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1515647'
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
    location: raw_lines_160_to_162
    action: preserved_and_flagged
    counts:
      Like: 13
      Haha: 7
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_170_to_231
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_232_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK Console DD #2: Discovery in the Crusader Kings Experience

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Mar 15, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-2-discovery-in-the-crusader-kings-experience.1515647/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-2-discovery-in-the-crusader-kings-experience.1515647/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-2-discovery-in-the-crusader-kings-experience.1515647/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-2-discovery-in-the-crusader-kings-experience.1515647/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-90-the-1-5-1-update.1514785/ "CK3 Dev Diary #90: The 1.5.1 Update") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-91-update-1-5-1-1.1516821/ "CK3 Dev Diary #91: Update 1.5.1.1")

# CK Console DD #2: Discovery in the Crusader Kings Experience

- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Mar 15, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck-console-dd-2-discovery-in-the-crusader-kings-experience.1515647/)

Howdy all! Another week, another Developer Diary  

One of the most engaging features of the Crusader Kings franchise is the path of discovery that the user is taken on as they immerse themselves in the unique CK3 gameplay. This is a grand strategy game with an RPG twist as the underlying sandbox nature of the game allows gamers to define their own goals and objectives rather than following a linear path. It’s all about the success of your Dynasty rather than a specific ruler. Dying is not failure... nor is losing wars... the most important aspect is the continuation of a Dynasty through the ages. This can be achieved in many ways, allowing you to carve their own path to power over generations through the use of military expansion, strengthening bloodlines and alliances through marriage, or through the dark arts of subterfuge.  

Exercising power during the Medieval period was a complex business and this is reflected in the core gameplay of CK3. Many actions within CK3 require experimentation in order to discover the most successful strategies that suit the user defined goals. For example – starting a war against a perceived enemy requires a number of steps to be completed before war can be declared. This may often involve the acquisition of a Casus Belli (Legal Cause for War), which may require the fabrication of a claim through your head of faith. These steps and other methods of political maneuvering towards are part of the rich gameplay tapestry of Crusader Kings and the route to discovery is a core component of gameplay that should be celebrated and enjoyed when playing the game.  

Onboarding for a game with CK3’s level of complexity and depth is a challenge. The PC tutorial has been integrated into the console game with adjustments for the target platform, which will help if you are new to console gameplay coming into the game. The balance is always between giving the community enough information to allow them to play the game vs overloading the user with too much detail. The nature of this title demands that there will need to be some experimentation and discovery along the way, and that’s one of the features of the game that should be celebrated. After all, as stated earlier, having a ruler die or losing a war is not the end of the game... it’s the beginning. Securing your Dynasty over time is the main objective, but there is also the flexibility for the user to define their own objectives and paths through gameplay.

 

- 78

<!-- artifact:reactions:start -->
- 13 Like
- 7 Haha
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)**
Role: Community Manager
Badges: 10
Messages: 119
Reaction score: 4,454

*[Full game-badge icon list of 10 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
