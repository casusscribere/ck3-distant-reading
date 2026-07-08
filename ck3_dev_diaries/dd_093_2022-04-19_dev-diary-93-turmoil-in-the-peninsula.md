---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1521199/"
forum_thread_id: 1521199
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 93
title: "CK3 Dev Diary #93 - Turmoil in the Peninsula"
dd_date: 2022-04-19
author_handle: Pdx_Meedoc
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 650
inline_image_count: 5
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1521199'
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
    location: raw_lines_~28_to_146
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_145
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1923.jpg?1650464211
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_204_to_208
    action: preserved_and_flagged
    counts:
      Like: 185
      Love: 86
      (unlabeled — rendered as base64 data URI): 11
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_216_to_263
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_264_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

<!-- artifact:thread_banner:start -->
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1923.jpg?1650464211)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #93 - Turmoil in the Peninsula

<!-- artifact:thread_metadata:start -->
- Thread starter [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)
- Start date [Apr 19, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-93-turmoil-in-the-peninsula.1521199/)
<!-- artifact:thread_metadata:end -->

Greetings!  

Winter is slowly fading behind us (at least in the northern hemisphere), and spring is starting to take over. A new season calls for an announcement. I’m happy to present you with our next Flavor Pack: Fate of Iberia, due to be **released on the 31st of May!** We are obviously talking about Mediterranean Iberia, not the former Kingdom in Georgia.  

In addition to being one of the most played regions, the Iberian peninsula is interesting because of the complexity of the geopolitical situation, and the richness of the events occurring during the time period of Crusader Kings 3. It gives us a good opportunity to bring more flavor for both the Christians and Muslims living there.  

With this new flavor pack, we want to offer you the opportunity to truly decide the fate of the whole peninsula, either by reenacting history or creating an alternative that pleases you more. In order to model the complexity of the situation, we are introducing a new system, the Struggle. It will be changing the rules and increasing the challenge for the rulers within the Iberian peninsula. You can have an idea of how the game will be affected in the screenshot below. The effects will vary a lot depending on the stage of the struggle, but we will go into details in the next dev diary ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")  

![20220419131254_1.jpg](https://forumcontent.paradoxplaza.com/public/818029/20220419131254_1.jpg "20220419131254_1.jpg")


*The Struggle will both create new opportunities and add constraints for the rulers within Iberia.*  

A new 867 bookmark features a revamped Iberian cast of characters, giving players the perfect place to jump in and deflect history as they see fit. The Struggle will persist into the 1066 start date as well. The bookmark lets you choose between different vassals, either from the Christian Kingdoms, or Al-Andalus. Each of them offers different starting challenges and choices.. For instance, in the south, Emir Adanis and Ibn Marwan are both Dukes under the Sultanate of Al-Andalus. But they also are neighbors and rivals. Starting with one of them will certainly imply crossing swords and scheming against the other.  

![Screenshot of the new Iberian bookmark](https://forumcontent.paradoxplaza.com/public/818015/20220419103607_1.jpg "Screenshot of the new Iberian bookmark")

*The new 867 bookmark will be available for everyone, while being more interesting to experience if you own Fate of Iberia*  


We also seized the opportunity to update the map, refining the county and duchy divisions, as well as the cultures and faiths. This means the stage is more accurately set for the start of our game.  

![Screenshot of the new county division in Iberia](https://forumcontent.paradoxplaza.com/public/818017/20220419104207_1.jpg "Screenshot of the new county division in Iberia")


*We mostly focused on the Northern part of the region.*  

![20220419103731_1.jpg](https://forumcontent.paradoxplaza.com/public/818018/20220419103731_1.jpg "20220419103731_1.jpg")


*The new culture set up for the year 867*  


![20220419103821_1.jpg](https://forumcontent.paradoxplaza.com/public/818019/20220419103821_1.jpg "20220419103821_1.jpg")


*The new faith set up for the year 867*  


You might have noticed the addition of the Mozarabic faith, but again, we will detail that in a future dev diary, along with the rest of the content you can expect from a Flavor Pack!  

We are excited to go into the details and share all of this with you in the coming weeks! Until then, I wish you a lovely day and enjoy the trailer!  

[https://www.youtube.com/embed/yIYS2eOm-vw?wmode=opaque](https://www.youtube.com/embed/yIYS2eOm-vw?wmode=opaque)


Cheers,  

P.S.: While we do not expect the save versions to be incompatible, please make sure you wrap up your previous playthrough to ensure a seamless transition. If you encounter issues, you can of course roll these saves back to a previous version UNLESS you are playing in Ironman.

<!-- artifact:reactions:start -->
- 185 Like
- 86 Love
- 15 (unlabeled — rendered as base64 data URI)
- 13 (unlabeled — rendered as base64 data URI)
- 11 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)**
Role: Corporal
Messages: 39
Reaction score: 2,254
<!-- artifact:op_signature:end -->
