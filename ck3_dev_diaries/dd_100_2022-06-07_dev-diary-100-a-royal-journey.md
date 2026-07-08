---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1530040/"
forum_thread_id: 1530040
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 100
title: "CK3 Dev Diary #100: A Royal Journey"
dd_date: 2022-06-07
author_handle: rageair
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 515
inline_image_count: 6
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1530040'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1974.jpg?1654605270
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_198_to_202
    action: preserved_and_flagged
    counts:
      Like: 108
      Love: 29
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_210_to_317
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_318_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1974.jpg?1654605270)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #100: A Royal Journey

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Jun 7, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-100-a-royal-journey.1530040/)
<!-- artifact:thread_metadata:end -->

Greetings!  

Fate of Iberia was released just last week, and we hope you’re all enjoying shaping the peninsula according to your own ideas and ideals! Are you dominating it by force, or trying to reconcile the inhabitants’ differences? Have any of you encountered the elusive *wandering monk* yet?  

Anyhow, we’re hard at work with the 1.6.1 update, where we’re tweaking some balance, fixing issues found by you in the community, and also adding in a few new goodies (more on that below). We’re also working on a fix for those of you who can’t start the game (the AVX issue), which will come out before the full 1.6.1 update. Remember to pop by the [bug forums](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1077/) if you have a problem: it’s the best way to make sure we know about your game issues!  

With Fate of Iberia in your hands, we’ve now concluded the Royal Edition, and we’re overjoyed to see so many of you playing and enjoying the game. Please, keep sending us great feedback, we appreciate it a lot - your thoughts are very valuable to us!  

We are now setting our eyes on the future. We have many plans, both big and small - I cannot go into detail as it’s too early yet, but rest assured that we have many exciting things coming up! We’re taking a long, hard look at what we’ve done and achieved since the release of CK3; we’re evaluating, adjusting, and setting a course that we’re sure will be to your liking!  

Now, to round this Dev Diary off, we’d like to tease some new content coming along with the 1.6.1 update:  

For owners of Fate of Iberia, we’re adding a few religiously-flavored events about Sephardic Jews, Conversos, the direction of mosques, and so on - with interesting choices on how to handle various situations. Here’s one example (don’t want to spoil them all!)  


![mosque.png](https://forumcontent.paradoxplaza.com/public/835150/mosque.png "mosque.png")



Outside of Hispania, but still in the vicinity, we’re doing a small update to the Canary Islands, who will, among other things, receive their own pagan faith and some monolithic ambitions.  


![Guanche.png](https://forumcontent.paradoxplaza.com/public/835151/Guanche.png "Guanche.png")


![canaries.png](https://forumcontent.paradoxplaza.com/public/835152/canaries.png "canaries.png")


![megalith.png](https://forumcontent.paradoxplaza.com/public/835153/megalith.png "megalith.png")



We’re adjusting how feudalization works in the West African sphere, enabling rulers to transition out of the tribal government while retaining their native faiths without requiring them to reform those faiths. This is to better model methods of urbanization and centralization in West Africa, though they will also retain access to the old path too.  


![westafrica.png](https://forumcontent.paradoxplaza.com/public/835154/westafrica.png "westafrica.png")



That's it for this time, cheers for now!  


![Alex_Illustration.png](https://forumcontent.paradoxplaza.com/public/835155/Alex_Illustration.png "Alex_Illustration.png")

<!-- artifact:reactions:start -->
- 108 Like
- 29 Love
- 11 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
