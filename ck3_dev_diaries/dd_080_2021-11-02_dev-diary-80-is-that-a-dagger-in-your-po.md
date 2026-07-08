---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1496381/"
forum_thread_id: 1496381
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 80
title: "CK3 Dev Diary #80 - Is That a Dagger in Your Pocket…?"
dd_date: 2021-11-02
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
body_word_count: 780
inline_image_count: 9
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1496381'
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
    location: raw_lines_~28_to_158
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_157
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1764.jpg?1635860280
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_160_to_162
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_274_to_277
    action: preserved_and_flagged
    counts:
      Like: 161
      Love: 76
      (unlabeled — rendered as base64 data URI): 7
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_285_to_342
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_343_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1764.jpg?1635860280)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #80 - Is That a Dagger in Your Pocket…?

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Nov 2, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-80-is-that-a-dagger-in-your-pocket.1496381/)
<!-- artifact:thread_metadata:end -->

### Is that a dagger in your pocket…?​

or  


### Inventory System/Commission Artifact:​

### ​

Howdy all,  

Your Friendly Local Community Manager here to introduce this week's Developer Diary! While it was not my article, it was written by our ever mysterious Content Designer, CC! So sit back, relax, and enjoy some neat new features from the team and we can't wait to hear your thoughts and feedback!  

***Without further ado:***  


### ​

Greetings!  

Let’s talk about artifacts and the systems surrounding it.  

Artifacts can be divided into two categories, inventory and court, which is also where the items are stored. This dev diary will focus on the former one, so the inventory.  


#### Inventory system​

Feast thine eyes on the inventory screen! Instead of putting all of the goodies into a big pile, we’ve made an inventory window showing what’s currently equipped and how many of each category you can “wear”.  

![1.png](https://forumcontent.paradoxplaza.com/public/757558/1.png "1.png")


[image of inventory screen]  

Equipable artifacts fall into the following categories; crown, regalia, weapon, armor, and lastly, trinkets. Most of these categories speak for themselves but trinkets, so what are they you may ask? The answer is a myriad of things; they can be brooches, dried flowers, even a worm on a string.  

You can also sort after these categories, making it easy to find what you’re looking for when you want to equip, repair, or just browse your inventory.  

![2.png](https://forumcontent.paradoxplaza.com/public/757559/2.png "2.png")


[image of inventory screen: artifact section]  


In the Artifact Details, you can read the artifact’s history, as well as see what people are claimants. Watch out - some of these people may be looking to steal the artifact away from you…  


![3.png](https://forumcontent.paradoxplaza.com/public/757560/3.png "3.png")


[image showing artifact details: history tab]  

Of course, it goes both ways! Did your stupid brother inherit the family heirloom? You can duel, declare war, or steal it — as long as you have a claim.  

![4.png](https://forumcontent.paradoxplaza.com/public/757561/4.png "4.png")


![5.png](https://forumcontent.paradoxplaza.com/public/757562/5.png "5.png")


[image showing artifact details: claimants tab]  

Artifacts wear down when on your person versus when they are on display in the court. So keep that in mind as it can be costly in the long run to equip everything for the bonuses if you're not making full use of them.  

Since the Antiquarian is such a vital figure in maintaining and making full use of your artifacts, there’s a shortcut to recruiting or just looking at who has that position in your court.  

![6.png](https://forumcontent.paradoxplaza.com/public/757563/6.png "6.png")


[image showing the Antiquarian court position info]  

As shown in the image, the Antiquarian unlocks the ability to Reforge and Repair, as well as Commissioning Artifacts.  


![7.png](https://forumcontent.paradoxplaza.com/public/757564/7.png "7.png")


[image showing the Reforge Artifact interaction]  


### Commission Artifacts​

Inspirations are fickle like creativity, so if you have the gold and you want something commissioned, you can get in touch with local artisans through the Commission Artifact decision.  

An additional benefit of commissioning an artifact is that you get to decide what’s being made.  

![8.png](https://forumcontent.paradoxplaza.com/public/757565/8.png "8.png")


[image showing the commission artifact decision; artifact selection]  

Now you might wonder, “why would I ever subject myself to the whims and possible long time for a person to become inspired if I can just go to the local artisans and get what I want?”  
You see, even if inspirations appear as fickle as love during springtime, it’s that little extra spice — a creator’s passion — that permeates through the final product. It’s that warm feeling of love for the craft that the beholder can feel just by looking at it, it’s something that’s not always present in a commissioned piece.  

Ah, my apologies, I appeared to have been carried away there for a brief moment by my muse.  

What I meant to say is that in gameplay terms, that means that inspired people can create artifacts of higher quality while the commission artisans will do the bare minimum and therefore be of the lowest quality.  


![9.png](https://forumcontent.paradoxplaza.com/public/757566/9.png "9.png")


[image showing the inspiration progress]  

Whether a passion project or not, creating something takes time. We ask for your understanding and hope that you continue to enjoy Crusader Kings 3!  

This Dev Diary was ghostwritten by the mysterious CC.

<!-- artifact:reactions:start -->
- 161 Like
- 76 Love
- 12 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)**
Role: Community Manager
Badges: 21
Messages: 119
Reaction score: 4,454
<!-- artifact:op_signature:end -->
