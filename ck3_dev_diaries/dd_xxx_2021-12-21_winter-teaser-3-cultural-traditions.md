---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1503317/"
forum_thread_id: 1503317
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "Winter Teaser #3 - Cultural Traditions"
dd_date: 2021-12-21
author_handle: Trin Tragula
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 881
inline_image_count: 8
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1503317'
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
    location: raw_lines_~28_to_128
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_130_to_131
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_221_to_224
    action: preserved_and_flagged
    counts:
      Like: 129
      Love: 45
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_232_to_293
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_294_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Winter Teaser #3 - Cultural Traditions

<!-- artifact:thread_metadata:start -->
- Thread starter [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)
- Start date [Dec 21, 2021](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-3-cultural-traditions.1503317/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-3-cultural-traditions.1503317/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-3-cultural-traditions.1503317/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-3-cultural-traditions.1503317/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-winter-teaser-2-dynasty-legacy.1503282/ "CK3 Winter Teaser #2 - Dynasty Legacy") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-4-artifact-weapons.1504071/ "Winter Teaser #4 - Artifact Weapons")

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1816.jpg?1639500463)

# Winter Teaser #3 - Cultural Traditions

- Thread starter [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)
- Start date [Dec 21, 2021](https://forum.paradoxplaza.com/forum/developer-diary/winter-teaser-3-cultural-traditions.1503317/)

Hello and welcome to another winter teaser ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")  

In this short teaser today I bring you more cultural traditions as well as previews of some cultures we haven’t shown you before.  


**Chanson De Geste**  


![Image of the Chanson de Geste Cultural Tradition](https://forumcontent.paradoxplaza.com/public/773572/chansdegeste.PNG "Image of the Chanson de Geste Cultural Tradition")

In some cases cultural traditions are regional variants on more generically available one. Instead of the more widely available Martial Admiration tradition that we’ve shown previously the cultures that have a Frankish heritage will have access to the Chanson de Geste tradition. This both grants access to the Valets innovation when the Late Medieval era comes around and highlights the role of troubadours in the French region.  

**Performative Honor  


![Performative Honor Cultural Tradition](https://forumcontent.paradoxplaza.com/public/773575/performative_honor.png "Performative Honor Cultural Tradition")**​

For those that have Flavor Pack 1 the Shield Maiden related content is now connected to a new cultural tradition called Performative Honor, which is available for cultures of the North Germanic Heritage.  

**Persian Culture**  


![Image of the Philosopher Culture tradition](https://forumcontent.paradoxplaza.com/public/773587/philosopherculture.PNG "Image of the Philosopher Culture tradition")


One of the traditions of Persian culture highlights the prevalence of philosophical thought among its members, another gives access to a royal gardener court position. ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")  

**Butr Culture  


![Image of the Butr Culture and traditions](https://forumcontent.paradoxplaza.com/public/773589/butr_desert_ribats.png "Image of the Butr Culture and traditions")**​


Cultures with a Berber heritage and a presence in desert or dry lands will have access to the Desert Ribats tradition, which unlocks the Mulathamun Man at arms type among other things.  

**Catalan Culture  


![Image of the Catalan Culture and traditions](https://forumcontent.paradoxplaza.com/public/773590/catalan_culture.png "Image of the Catalan Culture and traditions")**​

Maritime Mercantilism is a tradition that makes coastal holdings more useful to a culture, as seen here in the lineup of Catalan Traditions.  

**Cisalpine Culture  


![Image of Cisalpine Culture and Traditions](https://forumcontent.paradoxplaza.com/public/773591/cisalpine.PNG "Image of Cisalpine Culture and Traditions")**​

Any culture that has the Roman culture somewhere in its ancestry can adopt the Republican Legacy tradition which is a special version of the more generally available Parochialism cultural tradition. This highlights the special Republican heritage in the italic sphere and will let you create a number of Republican vassals out of your counts who will become overseers, or Podestàs.  

**Mongol Culture  


![Mongol Culture and traditions](https://forumcontent.paradoxplaza.com/public/773592/mongols_steppe_tolerance.png "Mongol Culture and traditions")**​

The Steppe Tolerance tradition highlights that for some cultures what your subjects believe was not as important as it was for others…  



And that was all for this short winter teaser. These are some of my personal favorite traditions in the update, I hope you found them as interesting as I do! ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")

<!-- artifact:reactions:start -->
- 129 Like
- 45 Love
- 7 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)**
Role: Game Designer - Crusader Kings 3
Badges: 36
Reaction score: 16,644

*[Full game-badge icon list of 1 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
