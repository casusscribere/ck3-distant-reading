---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1503282/"
forum_thread_id: 1503282
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "CK3 Winter Teaser #2 - Dynasty Legacy"
dd_date: 2021-12-14
author_handle: PDX_Pariah
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 710
inline_image_count: 9
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1503282'
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
    location: raw_lines_~28_to_165
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_164
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1814.jpg?1639484045
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_167_to_169
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_249_to_253
    action: preserved_and_flagged
    counts:
      Like: 143
      Love: 46
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_261_to_369
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_370_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1814.jpg?1639484045)
<!-- artifact:thread_banner:end -->

# CK3 Winter Teaser #2 - Dynasty Legacy

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Dec 14, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-winter-teaser-2-dynasty-legacy.1503282/)
<!-- artifact:thread_metadata:end -->

 Code:

```
Howdy all,

Pariah here, posting on behalf of @rageair who is on a well deserved vacation!

Without further ado:
```

  

Greetings!  

By this point most of the team is on vacation (including me, this is a scheduled post!). However, we still want to tease something that we think you’ll like!  

With the Cultural Rework we’re making it more viable to rule a large and culturally diverse empire, as you all surely know. To enhance this playstyle we’ve devised a new Dynasty Legacy that focuses on strengthening multicultural realms! If you own the Royal Court expansion, you’ll get access to the new ‘Customs’ Dynasty Legacy!  

![1639483550535.png](https://forumcontent.paradoxplaza.com/public/773435/1639483550535.png "1639483550535.png")


[Image of the Legacy Track Art]  

Let's take a look at the Legacies themselves:  


![1639483565681.png](https://forumcontent.paradoxplaza.com/public/773436/1639483565681.png "1639483565681.png")


[Image of the first legacy]  
The first legacy reinforces the link between learning languages and acceptance by adding a Cultural Acceptance bonus on completion for members of your dynasty. Quite a powerful opener, as it gives you a tool for improving acceptance with cultures outside your own realm (albeit a small one, though depending on how spread out your dynasty is it can be more or less powerful!)  

![1639483581482.png](https://forumcontent.paradoxplaza.com/public/773437/1639483581482.png "1639483581482.png")


[Image of the second legacy]  
The second legacy improves the effectiveness of the Council Job, simple but effective. Having an extra slot for Learn Language schemes means that you can always have one running, while keeping your ‘normal’ personal scheme slot open for Swaying vassals or Seducing siblings.  

![1639483595923.png](https://forumcontent.paradoxplaza.com/public/773439/1639483595923.png "1639483595923.png")


[Image of third legacy]  
When you land a ruler of a culture in the lands of their culture, you already get a Cultural Acceptance bonus. This legacy makes it an even more viable strategy to do this, as you also get a hook that you can use for all kinds of things. This pairs well with the new grant options that you’ll find at the end of this DD.  

![1639483611697.png](https://forumcontent.paradoxplaza.com/public/773441/1639483611697.png "1639483611697.png")


[Image of fourth legacy]  
The fourth legacy unlocks a special Court Position, the Cultural Emissary. This isn’t a cheap position to fill, but it brings great benefit to realms with a diverse cast of vassals as it increases Different Culture opinion by up to 20! It also grants a lot of prestige, as an additional bonus.  

![1639483627840.png](https://forumcontent.paradoxplaza.com/public/773443/1639483627840.png "1639483627840.png")


[Image of the Cultural Emissary Court Position]  
Here are some details on how the position itself looks.  

![1639483640852.png](https://forumcontent.paradoxplaza.com/public/773444/1639483640852.png "1639483640852.png")


[Image of fifth legacy]  
The last legacy focuses less on building acceptance, and more on reaping its benefits! It gives you access to a decision that, while expensive to take, improves the lands of all your realm; presuming the culture has 75%+ acceptance with yours. This can be a truly massive bonus for a large realm. Not pictured here is that it also gives you prestige.  

![1639483652195.png](https://forumcontent.paradoxplaza.com/public/773446/1639483652195.png "1639483652195.png")


[Image of the main modifier from the Side-by-Side decision]  
The main modifier of the above decision, in its current incarnation.  

![1639483664492.png](https://forumcontent.paradoxplaza.com/public/773447/1639483664492.png "1639483664492.png")


[Image of the new Grant To buttons]  
Now, one of the hardest things to do if you want to have self-rule in your lands is actually finding someone of the correct culture. To remedy this problem, we’ve added two new buttons to the ‘Grant to…’ window. When giving away a County or Barony, you can now choose to grant it to a noble of your culture, or a noble of the local culture (faith, for now, always follows your own). If you choose either of these options, the game will firstly look for an appropriate wanderer, and if it can’t find anyone, generate a new character.  

If you grant land to a local noble, you will clearly see just how much acceptance you’ll get for the act.

<!-- artifact:reactions:start -->
- 143 Like
- 46 Love
- 15 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)**
Role: Community Manager
Badges: 58
Messages: 119
Reaction score: 4,454

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
