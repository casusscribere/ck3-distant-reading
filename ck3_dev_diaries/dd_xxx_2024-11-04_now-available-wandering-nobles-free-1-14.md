---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1712944/"
forum_thread_id: 1712944
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "Now Available: Wandering Nobles & Free 1.14.0 \"Traverse\" Update"
dd_date: 2024-11-04
author_handle: PDX_Pelly
expansion: Wandering Nobles
patch: Patch 1.14
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1203
inline_image_count: 1
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1712944'
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
    location: raw_lines_~28_to_118
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_120_to_121
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_254_to_258
    action: preserved_and_flagged
    counts:
      Like: 64
      Love: 9
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_266_to_371
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_372_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Now Available: Wandering Nobles & Free 1.14.0 "Traverse" Update

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pelly](https://forum.paradoxplaza.com/forum/members/pdx_pelly.1739928/)
- Start date [Nov 4, 2024](https://forum.paradoxplaza.com/forum/developer-diary/now-available-wandering-nobles-free-1-14-0-traverse-update.1712944/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/now-available-wandering-nobles-free-1-14-0-traverse-update.1712944/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/now-available-wandering-nobles-free-1-14-0-traverse-update.1712944/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/now-available-wandering-nobles-free-1-14-0-traverse-update.1712944/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22945](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-159-active-living.1710659/ "Dev Diary #159 - Active Living") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-160-vision-and-art.1717586/ "Dev Diary #160 - Vision and Art")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/now-available-wandering-nobles-free-1-14-0-traverse-update.1712944/?prdxDevPosts=1)

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3394.jpg?1730734882)

# Now Available: Wandering Nobles & Free 1.14.0 "Traverse" Update

- Thread starter [PDX_Pelly](https://forum.paradoxplaza.com/forum/members/pdx_pelly.1739928/)
- Start date [Nov 4, 2024](https://forum.paradoxplaza.com/forum/developer-diary/now-available-wandering-nobles-free-1-14-0-traverse-update.1712944/)

Hello all! Today we are releasing the Event Pack, Wandering Nobles. Alongside this, we are also releasing Update 1.14.0 "Traverse". Wandering Nobles is available now on [Steam](https://store.steampowered.com/app/2671080/Crusader_Kings_III_Wandering_Nobles/) and [Microsoft](https://www.microsoft.com/store/productid/9N753L0KX15Q).  

Check out the release trailer just below this text, and then the changelog a bit further down!  

[https://www.youtube.com/embed/po5FKZ9vuNo?wmode=opaque](https://www.youtube.com/embed/po5FKZ9vuNo?wmode=opaque)


---


### Update 1.14.0 "Traverse" Changelog​

### Expansion Features (Paid)​

- New lifestyle, ‘Wandering,’ split into three new lifestyle trees
  * Inspector: Landed characters can survey and improve their realm; landless characters can specialize in a terrain type
  * Wayfarer: Travel to reduce stress and pursue fame for your exploits.
  * Voyager: Improve linguistic skills and live the life of a tourist and sightseer.
- Three new activities linked to the new lifestyle
  * Inspection: Inspectors can examine their realm and pursue improvements
  * Hike: Wayfarers can reduce stress with a walk in the wilderness
  * Monument Expedition: Voyagers can set forth to see special buildings in other realms
- New events connected to travel, new lifestyle trees, and the associated activities


### Free Features​

- Added a new set of buildings, ‘Breweries,’ available to Catholic temples, a building giving a lot of county-wide bonuses
- Added a new cultural tradition, ‘Brewing Culture,’ where you can unlock the Breweries building for cities of your culture
- Added new Court Position, ‘Court Brewmaster,’ related to the Breweries building line, with three Court Position tasks:
  * Empty the Cellars
  * Share with the Court
  * Experimental Brew
- Added a new decision to merge the kingdoms of France and Aquitaine in the 867 bookmark
- Added a new decision to restore the Bosporan Kingdom
- New Points of Interest, ‘Battle’
- Added 11 Historical Battle Points of Interest:
  * Battle of Yarmuk
  * Battle of Aror
  * Battle of Tours
  * Battle of Talas
  * Battle of Lechfeld
  * Battle of Svolder
  * Battle of Dandanaqan
  * Battle of Civitate
  * Battle of Stamford Bridge
  * Battle of Hastings
  * Battle of Manzikert
- Added dynamic Battle Points of Interest, where particularly large and bloody battles will be remembered and be able to be visited after the fact
- Added a salacious Grand Wedding event chain


### Bugfixes​

- Fixed an issue with adventurers checking distance incorrectly
- Fixed error with a wedding event not checking faith correctly
- Fixed errors in siege events with a scope that does not exist
- Fix flavorization title tier names for landless adventurers
- Tweaked some events animations/portraits
- Fixed a rare issue where the player loses all war progress after enemy liege dies
- Add raid block reason to map tooltip
- Fix raid immunity being applied to the wrong character
- Any plague that appears in a realm that shares a border with you (land or sea) will now show up in the nearby section
- Removed incorrect land loss notification when a Governor's county vassal is in line to inherit a Governorship
- Fixed many issues with the family chronicle event decision and story cycle
- Now the Pope will be referred to as the Pope rather than a King-Bishops in many events
- Adjusted some Hunt modifier icons so they are appropriately shown as mixed (yellow) instead of positive/negative


### Balance​

- Placing bets in a chariot race no longer grants or reduces stress.
- Journals are now a new type of inventory artifact. Only one journal can be equipped at any time. Many books that were previously trinkets are now considered journals
- Family chronicles are now generally better with more modifiers; they are also either considered books (if you have a court) or journals
- Artifacts that boost terrain advantage now give a more significant boost.
- The kingdom of Aquitaine is now a part of the De Jure kingdom of France in the 1066 bookmark
- Rebalanced inbred/pureblooded chance, due to inbreeding risk now being calculated based on the degree of relatedness instead of the number of missing ancestors

### Art​

- Added a cheers icon.
- Added a new court position icon, new court position task icons, and a new building icon. All related to the new brewery building.
- Added icon for new activity option inspection allocated funds.
- Added a new wanderer lifestyle icon.
- Added several art assets as well as GUI adjustments
- Added several new events backgrounds:
  * Hills (Winter)
  * Plains (Winter)
  * Wetlands (Winter)
  * Mountains (Winter)
  * Steppe (Winter)
  * Riverside
  * Coast
- Added new animations:
  * Survey with Walking Stick
  * Idle with Walking Stick

---

If you encounter any issues after today’s update, please disable all mods and ensure you’re playing on a fresh save file. If the issue persists, then please [submit a bug report via our Bug Report board](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143) here on the official forums.

<!-- artifact:reactions:start -->
- 64 Like
- 9 Love
- 9 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Pelly](https://forum.paradoxplaza.com/forum/members/pdx_pelly.1739928/)**
Role: Community Manager
Badges: 76
Messages: 744
Reaction score: 15,183

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
