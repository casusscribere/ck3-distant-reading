---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1474533/"
forum_thread_id: 1474533
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 60
title: "CK3 Dev Diary #60 - The Cost of Warfare"
dd_date: 2021-05-18
author_handle: Pdx_Meedoc
expansion: Northern Lords
patch: Patch 1.4 (Azure)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 664
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1474533'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1628.jpg?1621345200
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_219_to_223
    action: preserved_and_flagged
    counts:
      Like: 240
      Love: 55
      (unlabeled — rendered as base64 data URI): 5
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_231_to_339
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_340_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1628.jpg?1621345200)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #60 - The Cost of Warfare

<!-- artifact:thread_metadata:start -->
- Thread starter [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)
- Start date [May 18, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-60-the-cost-of-warfare.1474533/)
<!-- artifact:thread_metadata:end -->

Hello everyone!  

I’m back with more info about what’s coming in the 1.4 Azure patch! Today we are going to cover improvements around Warfare. We prepared a few more things in addition to the starting Men-at-Arms. I hope you will find them interesting!  


## Declare War Window 1.4​

In addition to the Quality of Life improvements we presented last week, we also revisited the war declaration interface.  

![[Image of the new Declare War window]](https://lh4.googleusercontent.com/NR85Sevrdsva50F5dsS5MqXO5x9eLUxNwp1gN_NYLhz0uBAGfsyRZOG1KREVtLGjnvTswQZEEov4opjcAwkfEQz5xxwxoPjahaqyxEYMcpR7xi0m6KT6zlw2SOcc2TljLIOxdij3 "[Image of the new Declare War window]")


*[Image of the new Declare War window]*​


As you can see, the information has been restructured and it should be easier now to:  


- Compare your strength with your target
- Estimate if your opponents will have the funds to hire mercenaries
- Select an available objective


## Dynamic Mercenary Cost​

When it comes to Mercenaries, we adjusted how their cost is calculated. The price of a company is now affected by a few parameters:  


- The primary title
- The size of the Realm
- The current Innovation Era

The dynamic price will make it easier for lower tier realms to rely on Mercenaries and fight back their bigger neighbours. And it will be harder for extremely rich emperors to deny access to mercenaries by hiring all of them for a small sum. After all, why would the Count of Ulster be expected to pay the same price as the Emperor of the Holy Roman Empire - if you're a mercenary captain and you see that your client clearly is rich, you might just increase your prices...  


## Dynamic Garrison​

Your upcoming war will have a quite different pace. From now on, the garrison will be depleted at the end of a successful siege. It means that a freshly captured territory will be defenseless for a while, making recapturing it faster. After a siege, the garrison will recover over months or years, and the speed can be increased by improving the Holdings.  

It will thus be easier to counter-attack and recover territories you lost recently, or to continue a war which was invalidated if you have another valid casus belli. This change will encourage you to defend your wargoals and the strategic territory with your armies.  


## Factions update​

In order to make your life harder when you start conquering the world, we tweaked the logic behind the creation of factions, and they should be more threatening now.  

One of the big changes is their ability to synchronise their declaration. The power they need before pushing their demand is now dynamic and reacts to the state of the other factions. If a faction is threatening you, or is already at war with a ruler, it will be easier for another faction to push their demands. It should create more challenging situations, and you might want to concede to some factions to avoid struggling with too many opponents.  

![FnRHEqmaDTMDSF-jw0oEroxDHGLGxt6qd2x9VlZWrY5YXacBGZGrJ3TXNsVXHz4nMNmeWny62rNUcpEyYvKzsI4LjoWyJD0Gl-kFMn_B1u_pJF21io6QTbHHjEBRx1pw-FB07GKQ](https://lh5.googleusercontent.com/FnRHEqmaDTMDSF-jw0oEroxDHGLGxt6qd2x9VlZWrY5YXacBGZGrJ3TXNsVXHz4nMNmeWny62rNUcpEyYvKzsI4LjoWyJD0Gl-kFMn_B1u_pJF21io6QTbHHjEBRx1pw-FB07GKQ "")


*[Image: The faction is not strong enough to push their demands despite a lowered threshold due to existing factions]*  

![QTSuP9IF5_BfIJqUWyl2E5nSlktMiGEl3yW3VFt0vSKZBnmVVDZVzqe784fLz2XkzD1pG83ZuyDyw-fWViOjdTWh_hI0_8kSgB8ywOzGf4zHG1TKCowA_e6_Ed8XlZHeQYw0pDec](https://lh5.googleusercontent.com/QTSuP9IF5_BfIJqUWyl2E5nSlktMiGEl3yW3VFt0vSKZBnmVVDZVzqe784fLz2XkzD1pG83ZuyDyw-fWViOjdTWh_hI0_8kSgB8ywOzGf4zHG1TKCowA_e6_Ed8XlZHeQYw0pDec "")


*[Image: After one of the other factions declared war, the faction is now strong enough and will push their demand while their ruler is fighting the others.]*​


In addition to that, characters will be more inclined to join an Independence Faction if they own enough territories outside of the de jure area of the primary title of their Liege. Again, fast conquest will be more challenging, and consolidating your Realm will be more important.  

And that’s it for today’s Dev Diary! But, before leaving you, a quick reminder: The [PDX Con](https://pdxcon.paradoxplaza.com/) will be held this week-end! You can join us on our dedicated [Discord Server](https://discord.com/invite/pdxcon)! There will be a lot of nice streams and announcements; stay tuned for some news about Crusader Kings III !  

Have a nice week, and see you soon!

<!-- artifact:reactions:start -->
- 240 Like
- 55 Love
- 23 (unlabeled — rendered as base64 data URI)
- 8 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)**
Role: Corporal
Badges: 66
Messages: 39
Reaction score: 2,254

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
