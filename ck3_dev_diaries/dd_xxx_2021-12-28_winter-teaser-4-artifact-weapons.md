---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1504071/"
forum_thread_id: 1504071
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "Winter Teaser #4 - Artifact Weapons"
dd_date: 2021-12-28
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
body_word_count: 709
inline_image_count: 8
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1504071'
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
    location: raw_lines_~28_to_129
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_131_to_132
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_215_to_219
    action: preserved_and_flagged
    counts:
      Like: 96
      Love: 38
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_227_to_331
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_332_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Winter Teaser #4 - Artifact Weapons

<!-- artifact:thread_metadata:start -->
- Thread starter [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)
- Start date [Dec 28, 2021](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-4-artifact-weapons.1504071/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-4-artifact-weapons.1504071/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-4-artifact-weapons.1504071/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-4-artifact-weapons.1504071/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-3-cultural-traditions.1503317/ "Winter Teaser #3 - Cultural Traditions") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-5-mendicant-mystics-making-a-mess.1505616/ "Winter Teaser #5 - Mendicant Mystics Making a Mess")

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1820.jpg?1641802852)

# Winter Teaser #4 - Artifact Weapons

- Thread starter [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)
- Start date [Dec 28, 2021](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-4-artifact-weapons.1504071/)

### Winter Teaser #4 - Artifact Weapons​

 *On the First day of Christmas  
My good lord brought to me  
A sword with a gilded filigree.*​


Hello and happy holidays! Hope you’ve had a grand time celebrating, or maybe you’re already preparing for the new year?  

With the Royal Court a plethora of new weapon looks will be made available. They can be carried into duels, or shown off in your courts where they will be placed prominently on weapon stands for all to view. In this teaser we’ll be showing off a few more of them up close.​


*![1.jpg](https://forumcontent.paradoxplaza.com/public/775438/1.jpg "1.jpg")


The King of France, Charles II, trying to live up to his ancestor Charles Martel “The Hammer” name in battle, wielding the signature weapon.*​


![2.jpg](https://forumcontent.paradoxplaza.com/public/775439/2.jpg "2.jpg")



When they are crafted or generic weapons are wielded the game will pick an appropriate weapon from either the culture of the character's origin. So any weapon a character has acquired and equipped in their personal inventory will be wielded.​


![swords.jpg](https://forumcontent.paradoxplaza.com/public/775440/swords.jpg "swords.jpg")


*Swords and sabers, elegant and a way of showing off one's wealth  

![daggers.jpg](https://forumcontent.paradoxplaza.com/public/775441/daggers.jpg "daggers.jpg")


Daggers may not have reach, but they’re much more up close and personal. Et tu, Brute?  

![axes.jpg](https://forumcontent.paradoxplaza.com/public/775442/axes.jpg "axes.jpg")


What self respecting berserker would be caught without his axe?  

![maces.jpg](https://forumcontent.paradoxplaza.com/public/775443/maces.jpg "maces.jpg")


Mace, for chasing off attackers since before recorded history.  

![spears.jpg](https://forumcontent.paradoxplaza.com/public/775444/spears.jpg "spears.jpg")


For the experienced spearman.*  
​

And with that its a wrap for this short teaser, hope your holidays have been a great one and until next time, Happy new years!

<!-- artifact:reactions:start -->
- 96 Like
- 38 Love
- 7 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)**
Role: Senior Environment Artist
Badges: 40
Messages: 221
Reaction score: 2,288

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
