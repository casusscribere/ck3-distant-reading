---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1506337/"
forum_thread_id: 1506337
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 85
title: "CK3 Dev Diary #85 - An Artifact's Life"
dd_date: 2022-01-11
author_handle: Areysak
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 856
inline_image_count: 14
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1506337'
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
    location: raw_lines_~28_to_149
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_148
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1826.jpg?1641894791
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_151_to_153
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_236_to_240
    action: preserved_and_flagged
    counts:
      Like: 97
      Love: 39
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_248_to_353
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_354_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1826.jpg?1641894791)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #85 - An Artifact's Life

<!-- artifact:thread_metadata:start -->
- Thread starter [Areysak](https://forum.paradoxplaza.com/forum/members/areysak.1200721/)
- Start date [Jan 11, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-85-an-artifacts-life.1506337/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to Dev Diary 85 for Crusader Kings III!  
This is Areysak, Content Designer (some of you might remember me from Imperator).  

As the release date draws nearer and nearer, I’m here to talk to you about Artifacts. Again?! - you are probably thinking. YES, because artifacts still have more to offer! Let’s take a closer look.  

First, you probably know by now that artifacts are an investment that requires time and gold. An inspired character makes them for you, but how can you make them feel like they are really yours?  

… Why not inscribe your name on them!  

While an inspired character is hard at work making a fancy artifact for you, they might ask for your input on dedications: do you want this artifact to preserve the glory of your name for posterity? Or maybe you want to impress your lover, memorialize your deceased soulmate, or even make the artifact testify to your faith. A dedication is forever!  

![Event to add dedications to artifacts in the making](https://forumcontent.paradoxplaza.com/public/780585/artifact_1.png "Event to add dedications to artifacts in the making")



![Event to add dedications to artifacts in the making](https://forumcontent.paradoxplaza.com/public/780586/artifact_2.png "Event to add dedications to artifacts in the making")



![Dedicated artifact](https://forumcontent.paradoxplaza.com/public/780587/artifact_3.png "Dedicated artifact")



Occasionally, an inspired character might also seek your input on what functionalities you expect out of their artifact. Should your armor shine so bright that all your knights are inspired to greatness on the battlefield whenever you lead them, or should it favor practicality and make you more effective in mountain areas? You can choose an angle for your artifact that will make certain modifiers more likely to appear at creation.  

![Event to set the artifact’s focus](https://forumcontent.paradoxplaza.com/public/780588/artifact_4.png "Event to set the artifact’s focus")



On a separate topic, artifacts don’t exist in a void, but are living items in a living world, meant to be used, exchanged, stolen… and damaged. With use and time, an artifact’s durability lowers. What happens when your grandpa’s armor gets rusty, or your sword loses its edge? You need an expert! The Antiquarian at your court specializes not only in maintaining but also in repairing your artifacts. With just a couple of clicks (and some gold) your artifacts will be as good as new!  

![Repair interface](https://forumcontent.paradoxplaza.com/public/780589/artifact_5.png "Repair interface")



Sometimes, however, just repairing an artifact doesn’t really strike your fancy… Grandpa’s armor has seen its fair share of adventures, but it’s ancient, and you have newer and cooler stuff to wear! Before you hit a flea market to get rid of it (and possibly have Grandpa curse you from his grave), you have another choice: reforge! By reforging an inventory artifact, you change it into a pedestal artifact to expose in your court. Of course, its modifiers will change accordingly - wearing armor might make you tougher to kill, but it will hardly be of any help if it stays on a stand by your throne! On the other hand, your courtiers might be impressed by its fine decoration.  

![Reforge interface](https://forumcontent.paradoxplaza.com/public/780590/artifact_6.png "Reforge interface")



![Reforged armor](https://forumcontent.paradoxplaza.com/public/780591/artifact_7.png "Reforged armor")



![Reforged weapon](https://forumcontent.paradoxplaza.com/public/780592/artifact_8.png "Reforged weapon")



In some cases, however, you might not care enough about an artifact to repair or reforge it… When artifacts reach 0 durability they get destroyed and disappear from the game. Before that happens, however, other possibilities might open up for you through events. Perhaps a scrap collector will offer to buy it in exchange for some gold (don’t expect too much, though, they collect scraps, not riches!), or your antiquarian might find a way to repurpose it.  

![Event for decaying artifacts](https://forumcontent.paradoxplaza.com/public/780593/artifact_9.png "Event for decaying artifacts")



![Event for decaying artifacts](https://forumcontent.paradoxplaza.com/public/780594/artifact_10.png "Event for decaying artifacts")



Finally, some artifacts gain a reputation or a story through time! The sword of an often-triumphant general will be remembered as a fearsome weapon, while the crown that sat on the heads of your dynastic predecessors for generations will be recognized as a symbol of your people. But be careful, because if either you or your artifact gain an ominous reputation, your artifact might be known as a cursed item!  

![Crown with a reputation](https://forumcontent.paradoxplaza.com/public/780595/artifact_11.png "Crown with a reputation")



![Event from an artifact's life](https://forumcontent.paradoxplaza.com/public/780596/artifact_12.png "Event from an artifact's life")



![Armor gains a reputation](https://forumcontent.paradoxplaza.com/public/780597/artifact_13.png "Armor gains a reputation")



![An artifact can gain a reputation](https://forumcontent.paradoxplaza.com/public/780598/artifact_14.png "An artifact can gain a reputation")



That’s it for today! I hope you enjoyed this DD, and are looking forward to next month’s release as much as we are!

<!-- artifact:reactions:start -->
- 97 Like
- 39 Love
- 8 (unlabeled — rendered as base64 data URI)
- 8 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Areysak](https://forum.paradoxplaza.com/forum/members/areysak.1200721/)**
Role: Content Designer
Badges: 61
Messages: 38
Reaction score: 1,367

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
