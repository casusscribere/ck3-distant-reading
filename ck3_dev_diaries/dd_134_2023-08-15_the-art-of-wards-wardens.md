---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1596291/"
forum_thread_id: 1596291
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 134
title: "Dev Diary #134 – The Art of Wards & Wardens"
dd_date: 2023-08-15
author_handle: PDX-Trinexx
expansion: Wards and Wardens
patch: Patch 1.10
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 892
inline_image_count: 14
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1596291'
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
    location: raw_lines_~28_to_144
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_143
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2498.jpg?1692096536
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_146_to_148
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_250_to_254
    action: preserved_and_flagged
    counts:
      Like: 90
      Love: 25
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_262_to_364
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_365_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2498.jpg?1692096536)
<!-- artifact:thread_banner:end -->

# Dev Diary #134 – The Art of Wards & Wardens

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Aug 15, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-134-the-art-of-wards-wardens.1596291/)
<!-- artifact:thread_metadata:end -->

As the release date of “Wards & Wardens” draws near, we're taking a moment to reflect on the artistic endeavors that have brought it to life. This time our focus is on animations and some of the 2D icons and illustrations.  

---


### Icons​

Hey there! I'm Nicolas, 2D artist working on this royal game CK3.  

I'm pretty sure many of you checking out this dev diary must get pretty stoked about game designers writing about numbers going up and down, but as cool as it is to dive into the game's new meta, my piece of this dev diary is all about the art! Let me tell you a bit about creating game icons - in particular, how I went about creating the new icon for the eccentric personality trait!  

Alright, let's break it down in a kinda rough step-by-step. First things first, the game designers sent me a short brief describing what they needed, as well as ideas of what the icon might look like. Luckily for me, I was given the idea that the icon could depict a bag of marbles of various colors. I think it’s a pretty fitting metaphor for an eccentric individual, embodying their propensity for collecting unconventional ideas and perspectives, much like the colorful assortment of marbles within the bag.  

A guideline we try to adhere to when creating icons is to not necessarily create an image that literally depicts what the function/meaning of the icon will be. Instead, we want to be more figurative in our approach. For example, the icon for craven doesn't show a person being cowardly, but instead shows a frantic chicken, a symbol of cowardice.  

![image-01.png](https://forumcontent.paradoxplaza.com/public/1000909/image-01.png "image-01.png")


Starting off, I create a handful of initial sketches outlining the basic composition and values. These sketches don't require fine detailing; their purpose is solely for experimentation and estimating the best read of the image.  

![image-02.png](https://forumcontent.paradoxplaza.com/public/1000910/image-02.png "image-02.png")


When I have decided (When my art director decides which one he likes the most), I move on to making a more refined value render of the image. Paying close attention to the values and how they aid in the composition. For example, how the image goes from brighter in the focal point in the middle of the icon out to a much darker value on the edges, forming a vignette of sorts.  


![image-03.png](https://forumcontent.paradoxplaza.com/public/1000911/image-03.png "image-03.png")


Quite a straightforward step, adding colors to the image. Going over color theory is beyond my paygrade, so let's just say that these colors of warm red/yellow and cool blue look good together!  

![image-04.png](https://forumcontent.paradoxplaza.com/public/1000912/image-04.png "image-04.png")


Now it is time for my favorite part of the process - the refining stage! Now, I fine-tune the image, adding those last touches of light, textures, intricate details, and any minor adjustments to give the icon that final polished look. Make it feel like “candy”, like an old art director of mine used to say.  

![image-05.png](https://forumcontent.paradoxplaza.com/public/1000913/image-05.png "image-05.png")


And there you have it: resize it to the appropriate size and slap a border on it and we have anew, fresh personality icon! Hopefully the trait is good according to the meta, so people will actually see and appreciate it sometimes!  

Here are also a few interesting images of game concepts that depict the same thing, but in various styles - depending on the context in the UI.  

![image-06.jpg](https://forumcontent.paradoxplaza.com/public/1000914/image-06.jpg "image-06.jpg")


![image-07.png](https://forumcontent.paradoxplaza.com/public/1000915/image-07.png "image-07.png")



### Illustrations​


Naturally, we are also adding some new scene illustrations. With the option to pursue education as an adult, we've incorporated a University setting tailored for your scholarly characters. Additionally, we've added a Nursery and several scenes that enrich the cultural diversity of some existing locations.  

![image-08.png](https://forumcontent.paradoxplaza.com/public/1000917/image-08.png "image-08.png")


*[University]*  

![image-09.png](https://forumcontent.paradoxplaza.com/public/1000918/image-09.png "image-09.png")


*[Courtyard]*  

![image-10.png](https://forumcontent.paradoxplaza.com/public/1000919/image-10.png "image-10.png")


*[Nursery]*  

![image-11.png](https://forumcontent.paradoxplaza.com/public/1000921/image-11.png "image-11.png")


*[Tavern - MENA variation]*  

![image-12.png](https://forumcontent.paradoxplaza.com/public/1000922/image-12.png "image-12.png")


*[Study - Indian variation]*  

### Animations​

For this Event Pack we have added child-related animations, such as playing with toys. Among our new props we have a ball, a doll, stickhorses, and wooden swords, which all get used in the animations.  

![gif-01.gif](https://forumcontent.paradoxplaza.com/public/1000946/gif-01.gif "gif-01.gif")



![gif-02.gif](https://forumcontent.paradoxplaza.com/public/1000948/gif-02.gif "gif-02.gif")



Nothing more comforting when running a kingdom than your favorite toy!  

---

That’s it for this time. Stay tuned for next week's update as we gear up for the release of "Wards & Wardens" on August 22nd!

<!-- artifact:reactions:start -->
- 90 Like
- 25 Love
- 7 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 48 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
