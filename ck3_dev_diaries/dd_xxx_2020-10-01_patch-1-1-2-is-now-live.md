---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1429954/"
forum_thread_id: 1429954
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: Patch 1.1.2 is now live!
dd_date: 2020-10-01
author_handle: PDX_Pariah
expansion: Post-release patches
patch: Patch 1.1 (Chevron)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 740
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1429954'
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
    location: raw_lines_126_to_127
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_210_to_215
    action: preserved_and_flagged
    counts:
      Like: 156
      Love: 43
      (unlabeled — rendered as base64 data URI): 2
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_291_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Patch 1.1.2 is now live!

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Oct 1, 2020](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/)
- [2](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/page-3)
- …
  
  #### Go to page
  
  Go

- [6](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/page-6)
[Next](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/page-2)

1 of 6

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/page-6 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/?prdxDevPosts=1)

[![PDX_Pariah](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/s/paradox5.png)](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

#### [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

##### Community Manager

Jul 21, 2020

119

4.454

[](javascript:;)

- [Oct 1, 2020](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/post-26975421)


- [/forum/threads/patch-1-1-2-is-now-live.1429954/post-26975421](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/post-26975421)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/26975421/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/patch-1-1-2-is-now-live.1429954/post-26975421)

Greetings Crusaders,  

We have been working hard to ensure you have the best gaming experience possible! As such, we now have Patch 1.1.2 close on the heels of our latest Monster Big Patch™ complete with Patch Notes to follow.  

In addition to this Patch, we have also fixed the issues regarding the Mother of us All achievement on Steam! Make sure you restart your game to take advantage of these fixes!  

This Patch will affect all available platforms but may take slightly longer for Paradox Plaza users.  

Spoiler: Patch 1.1.2 Notes!!!

###################  
# Bugfixes  
###################  
- Fixed male/female dominated doctrine blocking all claims for the other sex, rather than just implicit claims. The behavior should now be identical to how it was previously.  
- Fixed various display issues in the Russian localization  
- Fixed tyranny being gained from rightful revocations when you had a claim on the title in question  
- Independence Faction wars no longer require the defender to occupy the entire domain of the rebelling vassals to stop ticking warscore  
- Reinstated Central Germanic and West Slavic name lists that had accidentally been removed

<!-- artifact:reactions:start -->
- 156 Like
- 43 Love
- 7 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->
