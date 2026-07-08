---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1498075/"
forum_thread_id: 1498075
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 82
title: "CK3 Dev Diary #82 - Court Type Content"
dd_date: 2021-11-16
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
body_word_count: 599
inline_image_count: 10
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1498075'
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
    location: raw_lines_~28_to_160
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_159
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1783.jpg?1637069467
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_162_to_164
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_250_to_254
    action: preserved_and_flagged
    counts:
      Like: 95
      Love: 27
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_262_to_314
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_315_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1783.jpg?1637069467)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #82 - Court Type Content

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Nov 16, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-82-court-type-content.1498075/)
<!-- artifact:thread_metadata:end -->

Howdy, y'all!  

Once again shadow posting for our wonderful Dev, CC! Who could this mysterious figure be who I am ghostwriting for? We may never know the answer to that. However, we do know that the info from today will be quite interesting for those of you following along with Royal Court updates and information!  

Without further ado, may I present:  

**Court Type Events:**  
Hello and welcome to another Dev Diary. We talked about the Court Types system [last week](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-81-a-tour-of-your-royal-court-interface.1496879/), and continuing on that, this week we’ll showcase the different types of content you might experience depending on your chosen court type!  

![1.png](https://forumcontent.paradoxplaza.com/public/761664/1.png "1.png")


[image showing a petition court event about an offensive monument; more common in diplomatic or administrative courts]  

![2.png](https://forumcontent.paradoxplaza.com/public/761665/2.png "2.png")


[image showing a petition court event about funding a cadastre; more common in administrative courts]  

If your court is known as a place of learning, then you can expect events concerning scholarly matters to be more common. If it’s a place famed for its administrative nature, then events related to that will be more frequent.  

These “court event weighings” don’t eliminate events from the pool, they just alter their “weights.” It’s not just petition events that are affected either, but the court events too.  


![3.png](https://forumcontent.paradoxplaza.com/public/761666/3.png "3.png")


[image showing court event about reselling a neighbouring country’s fashion; more common in diplomatic courts]  

And if you think that the events are limited to the court room alone, nay nay. We’ve added court type weighted events outside of court as well. Nothing is sacred, nowhere is safe.  


![4.png](https://forumcontent.paradoxplaza.com/public/761667/4.png "4.png")


[image of event where an academic disagreement is happening; more common in scholarly courts]  




Likewise, some new content is based off of your grandeur level and even your amenities. For instance, if your lodgings are low enough that you’re struggling to house everyone, that does give a _rather_ convenient excuse to evict guests and other scroungers from a cramped castle.  


![5.png](https://forumcontent.paradoxplaza.com/public/761668/5.png "5.png")


[order mass eviction decision]  


![6.png](https://forumcontent.paradoxplaza.com/public/761669/6.png "6.png")


[order mass eviction event]  

On the inverse side of things, having so many rooms that you don’t know what to do with them gives a bit of uhhh… space for experimentation.  

![7.png](https://forumcontent.paradoxplaza.com/public/761670/7.png "7.png")


[exoticise a grand hall decision]  

Redecorating in the style of a glamorous court is a bit on the nose, but not a bad way to crank up your own court’s grandeur.  

![8.png](https://forumcontent.paradoxplaza.com/public/761671/8.png "8.png")


[exoticise a grand hall event]  

Of course, for the _rustic_ look, you could redecorate after a less-than-fashionable court...  

![9.png](https://forumcontent.paradoxplaza.com/public/761672/9.png "9.png")


[exoticise a grand hall event, less grand court tooltip]  

And, to round off, rulers whose courts lack grandeur that are willing to hold their nose a little can even burn some of their remaining dignity in exchange for skilled staff, rounding out their courts with experience even without pedigree.  

![10.png](https://forumcontent.paradoxplaza.com/public/761674/10.png "10.png")


[scraping the barrel event]

<!-- artifact:reactions:start -->
- 95 Like
- 27 Love
- 12 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)**
Role: Community Manager
Badges: 139
Messages: 119
Reaction score: 4,454
<!-- artifact:op_signature:end -->
