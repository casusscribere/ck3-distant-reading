---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1297711/"
forum_thread_id: 1297711
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 8
title: "CK3 Dev Diary #08 - Courts, Guests, and Wanderers"
dd_date: 2019-12-17
author_handle: Virvatuli
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 745
inline_image_count: 3
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1297711'
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
  - type: thread_metadata
    location: raw_lines_146_to_148
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_182_to_183
    action: preserved_and_flagged
    counts:
      Like: 6
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_191_to_301
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_302_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #08 - Courts, Guests, and Wanderers

<!-- artifact:thread_metadata:start -->
- Thread starter [Virvatuli](https://forum.paradoxplaza.com/forum/members/virvatuli.1067644/)
- Start date [Dec 17, 2019](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-08-courts-guests-and-wanderers.1297711/)
<!-- artifact:thread_metadata:end -->

Hello everyone!  

To most of you I’m a new “face”, so let me introduce myself. I was a Content Designer on CK2 for Reaper’s Due, Monks & Mystics and Jade Dragon, where my most important contribution was essential [cat content](https://forum.paradoxplaza.com/forum/index.php?threads/ck2-dev-diary-17-crusader-cats.960813/) (yes, I also wrote the [Spymaster Mittens](https://forum.paradoxplaza.com/forum/index.php?threads/mittens-the-kitten.1008414/) event chain, and yes, the cat portrait in CK2’s animal kingdom is based on my real-life furbaby). Since JD, I’ve been on the excellent CK3 team and we can’t wait for you to see everything we’ve worked on! Sadly, I don’t have any cat news for you today, but I have something that is nearly as exciting: the Court, Guests, and Wanderers.  

The courts of CK3 are very similar to those in CK2. The Court consists of your landless subjects, such as some of your Family, Knights, and Councillors. However, you will generally have fewer Courtiers than in CK2. Courtiers who don’t have any duties or other reasons for staying will eventually decide to leave in pursuit of other opportunities. Fear not – they will let you know before they go. Courtiers leaving might feel like a bad thing, but I promise, it’s actually a part of a really neat feature (more on that further down). In addition to enabling the *neat feature*, this also means your remaining Courtiers will be more relevant to you than before. No more random strangers at the dinner table!  

![court_01.jpg](https://forumcontent.paradoxplaza.com/public/520628/court_01.jpg "court_01.jpg")



Your Court will still be a bustling place, full of new acquaintances. In addition to the Courtiers, the core members of your court, you will also have Guests paying you visits. These individuals will interact with your Courtiers and appear in events. Guests stay for a few years before they leave. If you want a Guest to stick around, you can recruit them. Just remember to give them a reason to stay! Giving them a spot on the council or a shiny title never fails, but seducing them also does the trick.  

![court_03.jpg](https://forumcontent.paradoxplaza.com/public/520629/court_03.jpg "court_03.jpg")



Guests look for opportunities and will be more likely to visit if they think you might recruit them. For example, Claimants will seek you out if you are strong enough to press their Claims, and suitors might appear if you or your adult children are unmarried. The interface will give you a handy overview to easily identify Guests with special Skills, Traits and Claims. You also have some influence over the type of Guests you attract. There are Invitation Decisions you can take to increase the chance of having good Knights and Claimants visiting, and there is a Dynasty Perk to increase the likelihood of useful Guests.  

![court_02.jpg](https://forumcontent.paradoxplaza.com/public/520631/court_02.jpg "court_02.jpg")



But where do all these Guests come from? You see, when a mommy and a daddy love each other very much… Oh, you meant “where are they before they appear in my court”? Well, characters without a permanent home wander around on the map, and visit Courts along the way. This is where characters leaving your court comes in - they will become Wanderers! For example, a son or daughter who is too far down in the line of succession to inherit might become a Wanderer to find a new Liege to press their Claims. Characters might also find themselves on the road by being banished or losing all their land.  

All of this means that your guests often have interesting backstories. Many of them have families and relationships, and they keep developing during their journeys. If you check in on a family member who is out wandering, you might find that they have married or picked up some new skills (or a juicy secret…) since they left your Court. Perhaps they’ve even become a Mercenary Captain or the head of a Holy Order!  

In the world of CK3, your ruler is the main character, but it is our hope that courtiers, guests, and wanderers will become a great supporting cast. I’m looking forward to hearing about all the little subplots you will discover.  

That is all for this Development Diary my friends. Take care and we’ll see you in 2020!

<!-- artifact:reactions:start -->
- 6 Like
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Virvatuli](https://forum.paradoxplaza.com/forum/members/virvatuli.1067644/)**
Role: Private
Badges: 45
Messages: 22
Reaction score: 440

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
