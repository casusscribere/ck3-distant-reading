---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1624034/"
forum_thread_id: 1624034
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 144
title: "Dev Diary #144 - Legends and Lesions"
dd_date: 2024-02-12
author_handle: PDX-Trinexx
expansion: Legends of the Dead
patch: Patch 1.12
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1078
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1624034'
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
    location: raw_lines_~28_to_140
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_139
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2844.jpg?1707829257
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_220_to_224
    action: preserved_and_flagged
    counts:
      Like: 138
      Love: 46
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_232_to_335
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_336_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2844.jpg?1707829257)
<!-- artifact:thread_banner:end -->

# Dev Diary #144 - Legends and Lesions

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Feb 12, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-144-legends-and-lesions.1624034/)
<!-- artifact:thread_metadata:end -->

Hello everybody! Welcome to this Developer Diary explaining the creative vision behind Crusader Kings III’s first Core Expansion: *Legends of the Dead*, courtesy of one of our talented game designers (and resident historian on medieval plagues!)  


---


*In the year of the lord 1346 the Crimean port of Caffa was being besieged by the Golden Horde. The contemporary Italian notary de Mussis writes down that diseased corpses were thrown over its walls and thus, the Black Plague entered Europe. That same year, Edward III of England defeated the forces of king Philip VI of France in Crecy. Two years later, Edward would try to create the Order of the Round Table, inspired by the heroic deeds of King Arthur, and later transformed into the Order of the Garter.*  

As our Game Director already mentioned in [last week's Chapter III overview](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-143-the-next-chapter.1623007/), we're exploring a new type of expansion focusing on systems that affect the whole map, rather than just adding flavor to a specific region. We didn’t have a name for it at the beginning, but we knew we wanted to do something bigger with the time we had, while planning the next Major Expansion.  

We've been wanting to cover Plagues since approximately the 12th of January 2021. We still have the early designs stored somewhere, but we put that aside for a while in order to develop the huge endeavor that was Tours & Tournaments. However, the team stayed highly passionate about plagues throughout the entire time (as many of us have fond memories of The Reaper's Due), and we knew it was something that we wanted to tackle again.  

Soon after the release of Tours & Tournaments it became apparent that it was the moment to pick up plagues again, but that presented its own challenges, among them a very important one - how to make this distinct from its Crusader Kings II version?  

We were also very aware of the circumstances of the world, so we decided it was important to have some hope spreading across the map as well.  

![image-01.png](https://forumcontent.paradoxplaza.com/public/1072687/image-01.png "image-01.png")



When researching the way medieval people saw plagues, we noticed that on many occasions they moved towards blaming the monarchs; If they're a representative of divine power on earth, and God is punishing us, then it must be because the representative is doing a bad job, right? That made us think of the impact that would have on a ruler's Legitimacy... and then we started thinking about Legitimacy itself.  

Sure, we already had Prestige in the game, but that felt like a representation of what you've done and how you present yourself, rather than "are you fit to rule?", "do people believe in you?", "are you really the right person for this?" Legitimacy was born as a way to represent these questions within the game, which raised the question: *how do you prove your rule is legitimate?*  

Soon, we thought of the medieval royal genealogies, tracing back the lineages to Trojan heroes, Charlemagne, mythological kings and even gods. Proving that you're the descendant of Aeneas is the easiest way to say, "I *am* the right person to rule."  

"To be noble," the medieval historian George Duby notes, "is to be able to refer to a genealogy."  

This, obviously, led us to Legends, and legends certainly did spread during the Middle Ages. King Arthur and his knights became so popular that they soon received translations and new material in French, German, Spanish and Italian. Legends got out of control, changed and expanded through the centuries, creating new stories that had little to do with their original purpose.  

In *Legends of the Dead*, we unite the brightest and darkest moments of humanity - tales of greatness illuminating a devastated land. Desolation and despair, but also the hope that comes after.  

Plagues will ravage your realm, causing development to plummet, and kill characters indiscriminately, for Death knows no master. In addition to our existing diseases, you'll be able to suffer from Holy Fire, Bloody Flux, and Measles. Holy Fire was the medieval name for ergotism, while outbreaks of dysentery (frequently occurring in the wake of passing armies) were known as Bloody Flux. Measles in particular is a danger to infants, and could be a dynasty killer if players aren't careful.  

We’ll cover these in more detail when we talk about Plagues in a later Dev Diary, however.  

![image-02.png](https://forumcontent.paradoxplaza.com/public/1072688/image-02.png "image-02.png")


![image-03.png](https://forumcontent.paradoxplaza.com/public/1072689/image-03.png "image-03.png")


*[Image: A Consumption outbreak follows the coast of the English Channel]*  

![image-04.png](https://forumcontent.paradoxplaza.com/public/1072690/image-04.png "image-04.png")


*[Image: New (and full body!) graphics for measles]*  

Legends will allow you to write down the heroic deeds of your ancestors or sing about your own glory. Cover the map in the stories that you create, gaining powerful control and skill boosts, among other effects.  

It’s not just the likes of Hercules who get their own legends, however; being a faithful devotee can also spawn legendary tales of martyrdom and sacrifice. And, of course, you'll be able to trace your Legend back to the most legitimate monarchs of the past. Spreading a Legend (and increasing its quality) will give you unique rewards, such as special Decisions or new Buildings. In such a highly systemic expansion with both Plagues and Legitimacy, Legends also allow for some nice historical flavor and roleplay elements.  

![image-05.png](https://forumcontent.paradoxplaza.com/public/1072691/image-05.png "image-05.png")


*[Image: The* Custody of the Holy Site *legend spreads over Galicia]*  

![image-06.png](https://forumcontent.paradoxplaza.com/public/1072692/image-06.png "image-06.png")


*[Image: A Legendary Statue built to commemorate a hero's legend]*  

![image-07.png](https://forumcontent.paradoxplaza.com/public/1072693/image-07.png "image-07.png")


*[Image: A legend turned into an artifact]*  



We will touch more on Legends and Legitimacy and how they work in-game next week, in addition to a deep dive into the heroic (and sometimes grimy) art created for this expansion! And worry not, Plagues - the most famous of them all in particular - will receive some more attention soon after.

<!-- artifact:reactions:start -->
- 138 Like
- 46 Love
- 9 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 41 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
