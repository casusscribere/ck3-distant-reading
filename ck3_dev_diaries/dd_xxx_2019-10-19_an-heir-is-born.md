---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1261140/"
forum_thread_id: 1261140
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: An Heir Is Born!
dd_date: 2019-10-19
author_handle: HottestRod
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 877
inline_image_count: 1
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1261140'
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
    location: raw_lines_~28_to_114
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_116_to_118
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_210_to_211
    action: preserved_and_flagged
    counts:
      Love: 3
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_286_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# An Heir Is Born!

<!-- artifact:thread_metadata:start -->
- Thread starter [HottestRod](https://forum.paradoxplaza.com/forum/members/hottestrod.1325925/)
- Start date [Oct 19, 2019](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/)
- [2](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/page-3)
- …
  
  #### Go to page
  
  Go

- [32](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/page-32)
[Next](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/page-2)

1 of 32

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/page-32 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/?prdxDevPosts=1)

[![HottestRod](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/s/MotE_dev.png)](https://forum.paradoxplaza.com/forum/members/hottestrod.1325925/)

#### [HottestRod](https://forum.paradoxplaza.com/forum/members/hottestrod.1325925/)

##### Associate Product Marketing Manager

May 14, 2018

358

730

[](javascript:;)

- [Oct 19, 2019](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/post-25912864)


- [/forum/threads/an-heir-is-born.1261140/post-25912864](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/post-25912864)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/25912864/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/an-heir-is-born.1261140/post-25912864)

![Generic_Titus_Banner_1200x630.png](https://forumcontent.paradoxplaza.com/public/paradox/banners/Generic_Titus_Banner_1200x630.png "")

  
*Crusader Kings III* is the newest generation of Paradox Development Studio’s beloved medieval role-playing grand strategy game. Expand and improve your realm, whether a mighty kingdom or modest county. Use marriage, diplomacy and war to increase your power and prestige in a meticulously detailed map that stretches from Spain to India, Scandinavia to Central Africa.  

[https://www.youtube.com/embed/YlOXhOxEum0?wmode=opaque](https://www.youtube.com/embed/YlOXhOxEum0?wmode=opaque)


But uneasy lies the head that wears a crown! Your cunning is your greatest weapon, and intelligence is the key to all successful strategy. Guard your life and the future of your dynasty, because enemies foreign and domestic envy your status. Engage in espionage, join political factions, punish heretics or use assassins to make sure your throne passes safely to the next generation.  

*Crusader Kings III* is the medieval strategy role-playing experience that you have been waiting for.  


-  **Shape Your Dynasty:** Guide unique characters through history, choosing lifestyles best suited to their personalities and your ambitions.
-  **Rewrite Medieval History:** Dynasties will change and adapt to changes in family and politics, swimming in a rich world of religious faith and royal pageantry.
-  **Build a Mighty Kingdom:** Use cold steel or warm words to expand your realm; war backed by cunning, and diplomacy that unites bloodlines.
-  **Experience High Drama:** Stranger than fiction stories leap off the screen, as characters plot against you and events push you to extremes.
-  **Learn as You Go:** Guided advice helps newcomers and veterans navigate a rich medieval world. In-game suggestions tip you off to paths you might not have considered.
-  **The Usual Crusader Kings Fun:** Keep a stubborn council in line, scheme against your overbearing uncle or marry rich duchesses for their land and legacy.

Prepare yourself to secure the throne in Crusader Kings III **[here](https://pdxint.at/316PE50)**!

 

Toggle signature

Associate Product Marketing Manager | PDX CMTY Team Alumni: Crusader Kings, Imperator: Rome (Community Developer), Europa Universalis IV & Hearts of Iron (Community Manager) | Writer, Gamer & Reader  

"La vie est bizarrement faite. Elle se contrefout souverainement des convenances, de la décence et des bonnes manières."

<!-- artifact:reactions:start -->
- 3 Love
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
