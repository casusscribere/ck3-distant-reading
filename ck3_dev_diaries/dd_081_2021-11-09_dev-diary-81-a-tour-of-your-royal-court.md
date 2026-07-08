---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1496879/"
forum_thread_id: 1496879
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 81
title: "CK3 Dev Diary #81 - A tour of your Royal Court (Interface)"
dd_date: 2021-11-09
author_handle: Mrop
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1558
inline_image_count: 22
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1496879'
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
    location: raw_lines_~28_to_148
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_147
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1770.jpg?1636369826
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_150_to_152
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_337_to_342
    action: preserved_and_flagged
    counts:
      Like: 127
      Love: 58
      (unlabeled — rendered as base64 data URI): 7
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_350_to_460
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_461_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1770.jpg?1636369826)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #81 - A tour of your Royal Court (Interface)

<!-- artifact:thread_metadata:start -->
- Thread starter [Mrop](https://forum.paradoxplaza.com/forum/members/mrop.638192/)
- Start date [Nov 9, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-81-a-tour-of-your-royal-court-interface.1496879/)
<!-- artifact:thread_metadata:end -->

Hello there, and welcome to the eighty-first CK3 Dev Diary!  

Today we are going to look at the experience of admiring your Royal Court, one of the paid features of the Expansion with the same name.  

Most of the actual mechanics of the expansion should already be familiar to you if you have read [previous Dev Diaries](https://forum.paradoxplaza.com/forum/threads/ck3-royal-court-faq-developer-diaries-q-a-important-information.1475394/). I will refer back to these Dev Diaries where appropriate, so you can see this as a bit of a summary of what it means to preside over your own Royal Court.  

That being said, we are going to talk a bit about Court Types, a minor feature for your Royal Court  

### Visiting your Royal Court​

When you reach the rank of King or Emperor as a Feudal or Clan Ruler, you have laid the foundation for your Royal Court. You can now go to it via a button in the main interface.  

This button highlights if there is something interesting to do in your Royal Court at this moment, such as if you have new Court Artifacts.  

![pasted image 0 (1).png](https://forumcontent.paradoxplaza.com/public/759347/pasted image 0 (1).png "pasted image 0 (1).png")



You can also view anyone else’s Royal Court via a button next to their Character.  

![pasted image 0.png](https://forumcontent.paradoxplaza.com/public/759348/pasted image 0.png "pasted image 0.png")



### The Throne Room​

Your Royal Court is split into three segments: Throne Room, Court Grandeur, and Court Artifacts  

When you enter your Royal Court, you end up in your Throne Room.  

![pasted image 0 (2).png](https://forumcontent.paradoxplaza.com/public/759349/pasted image 0 (2).png "pasted image 0 (2).png")



Here you can see various petitioners or other goings-on in your Court, and you can choose to interact with them. These types of events are described in [Dev Diary 75](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-75-in-the-event-of-court-events.1492792/). If any Inspired Characters are present or have projects in progress, they are also shown here, on the left side of the screen.  

![2021_11_08_2.png](https://forumcontent.paradoxplaza.com/public/759350/2021_11_08_2.png "2021_11_08_2.png")



If there is not enough going on here, you can also choose to Hold Court, inviting Courtiers and Vassals across the Realm to grovel before you (which was shown in [Dev Diary 72](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-72-holding-court-at-court-in-the-royal-court-in-a-courtly-fashion.1489882/)).  

![pasted image 0 (3).png](https://forumcontent.paradoxplaza.com/public/759352/pasted image 0 (3).png "pasted image 0 (3).png")



![pasted image 0 (4).png](https://forumcontent.paradoxplaza.com/public/759354/pasted image 0 (4).png "pasted image 0 (4).png")



If this is your Liege’s Court, you can even approach them to hear your reasonable requests, as seen in [Dev Diary 74](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-74-please-kaiser-can-i-have-some-more.1491791/).  

![pasted image 0 (5).png](https://forumcontent.paradoxplaza.com/public/759356/pasted image 0 (5).png "pasted image 0 (5).png")



### Grandeur and Amenities​

Moving on to the second part of your Royal Court, which is an overview of your Court Grandeur. How much you have, various factors affecting it, and so on.  

Grandeur was explained a while ago, in [Dev Diary 61](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/). Basically, it is a measure of how well known your Court is, and each Level gives you further benefits.  

Your current Grandeur, Grandeur Baseline, and unlocked Grandeur Levels are shown on the large bar in the center.  

In the image below, we can see we are gaining Grandeur every month due to being below our Baseline.  

![pasted image 0 (6).png](https://forumcontent.paradoxplaza.com/public/759357/pasted image 0 (6).png "pasted image 0 (6).png")



Our current Level is 4: while we do not have enough Grandeur to maintain this Level, we had unlocked it before, and it will thus stay unlocked for 6 months, regardless how much Grandeur we have.  

![pasted image 0 (7).png](https://forumcontent.paradoxplaza.com/public/759358/pasted image 0 (7).png "pasted image 0 (7).png")



We can also see that our expected Grandeur Level is 7, which we are nowhere near fulfilling.  

![pasted image 0 (8).png](https://forumcontent.paradoxplaza.com/public/759359/pasted image 0 (8).png "pasted image 0 (8).png")



Grandeur is also reflected in other ways. If you have high Grandeur, the UI looks more luxurious, and new (non-Artifact) furniture appears in your court.  

![pasted image 0 (9).png](https://forumcontent.paradoxplaza.com/public/759360/pasted image 0 (9).png "pasted image 0 (9).png")



![pasted image 0 (10).png](https://forumcontent.paradoxplaza.com/public/759361/pasted image 0 (10).png "pasted image 0 (10).png")



A large source of Grandeur is which Amenities are available to your Courtiers and visitors to your court. Providing excellent Amenities is sure to make your name well known across the world.  

![pasted image 0 (11).png](https://forumcontent.paradoxplaza.com/public/759362/pasted image 0 (11).png "pasted image 0 (11).png")



![pasted image 0 (12).png](https://forumcontent.paradoxplaza.com/public/759363/pasted image 0 (12).png "pasted image 0 (12).png")



There are two other factors affecting Grandeur, Court Language and Court Types. Court Language was already explained in [Dev Diary 78](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-78-taking-language-to-court.1495106/), so let’s talk about Court Types.  

### Court Types​

With Court Types, you can choose which kind of Royal Court you want to foster. Perhaps one where martial prowess is admired, or where there is a whisper around every corner and a lover behind every curtain.  

You always have the choice between two Court Types, based on the Ethos of your Culture, and changing it costs Prestige. If your Culture changes, you can still keep your old Court Type.  

The type of Royal Court affects two things: what you get from your Grandeur Level, and what your Courtiers get from being part of the Court.  

While some Grandeur Levels you reach are always the same regardless of your Court Type, some change somewhat. So, in a Diplomatic Court, Grandeur Level 4 may see you gaining less Tyranny, while in a Warlike Court, you may gain more Levies.  

### pasted image 0 (13).png


As for Courtiers, each Courtier who stays at an especially Grand Royal Court for a certain period of time (5 years) will gain a special Courtier Trait based on the Court Type  

![pasted image 0 (14).png](https://forumcontent.paradoxplaza.com/public/759365/pasted image 0 (14).png "pasted image 0 (14).png")



Each Trait of this type has two different levels. If your Court is at Grandeur Level 5, Courtiers get the first level, while the second level will appear at Grandeur Level 8. The second level comes with extra bonuses and can be especially useful for those you plan to be your Vassals.  

![pasted image 0 (15).png](https://forumcontent.paradoxplaza.com/public/759366/pasted image 0 (15).png "pasted image 0 (15).png")



### Court Artifacts​

Last but certainly not least, are the Court Artifacts. We showed a few of them off in [Dev Diary 69](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-69-nice-throne-room-artifacts.1487491/).  

In short, Court Artifacts are a special type of Artifacts. These are large furniture and other decorative items you display inside your Royal Court. This makes them distinct from your Inventory Artifacts described in [last week's Dev Diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-80-is-that-a-dagger-in-your-pocket.1496381/) as you are not hauling them around everywhere.  

When entering this part of the Royal Court, you can see all spots where you can place Court Artifacts  

![2021_11_09_1.png](https://forumcontent.paradoxplaza.com/public/759367/2021_11_09_1.png "2021_11_09_1.png")



Just like Inventory Artifacts, they give you a bonus if they are actively on display in your Royal Court. The primary purpose of Court Artifacts is to increase your Court Grandeur, but some have additional effects.  

![pasted image 0 (16).png](https://forumcontent.paradoxplaza.com/public/759368/pasted image 0 (16).png "pasted image 0 (16).png")



For most Court Artifacts, there is more than one slot to place them. Perhaps that tapestry would look better on that other wall?  

![swap.gif](https://forumcontent.paradoxplaza.com/public/759369/swap.gif "swap.gif")



### End of the Tour​


That is all for this week, thank you for reading!

 

#### Attachments

- [![2021_11_08_2.png](https://forumcontent.paradoxplaza.com/thumbnail/public/759103/2021_11_08_2.png)](https://forum.paradoxplaza.com/forum/attachments/2021_11_08_2-png.771623/)
  
  2021_11_08_2.png
  2,8 MB

 · Views: 0

- [![2021_11_08_2.png](https://forumcontent.paradoxplaza.com/thumbnail/public/759324/2021_11_08_2.png)](https://forum.paradoxplaza.com/forum/attachments/2021_11_08_2-png.771844/)
  
  2021_11_08_2.png
  2,8 MB

 · Views: 0

- [![2021_11_09_1.png](https://forumcontent.paradoxplaza.com/thumbnail/public/759325/2021_11_09_1.png)](https://forum.paradoxplaza.com/forum/attachments/2021_11_09_1-png.771845/)
  
  2021_11_09_1.png
  2,6 MB

 · Views: 0

<!-- artifact:reactions:start -->
- 127 Like
- 58 Love
- 18 (unlabeled — rendered as base64 data URI)
- 10 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Mrop](https://forum.paradoxplaza.com/forum/members/mrop.638192/)**
Role: good with computer
Badges: 61
Messages: 255
Reaction score: 1,291

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
