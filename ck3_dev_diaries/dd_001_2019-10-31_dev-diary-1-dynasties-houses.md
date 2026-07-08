---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1270519/"
forum_thread_id: 1270519
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 1
title: "CK3 Dev Diary #1 - Dynasties & Houses"
dd_date: 2019-10-31
author_handle: rageair
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1554
inline_image_count: 3
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1270519'
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
    location: raw_lines_198_to_200
    action: preserved_and_flagged
    counts:
      Like: 12
      Love: 7
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_208_to_307
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_308_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #1 - Dynasties & Houses

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Oct 31, 2019](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-1-dynasties-houses.1270519/)
<!-- artifact:thread_metadata:end -->

Greetings, and welcome to the first CK3 Feature Dev Diary!  

As this is the first DD we want it to be extra juicy, and showcase something that we’re excited about - namely what we’re doing with Dynasties! Dynasties are immaterial yet fundamentally important things that make Crusader Kings what it is - your line must follow an unbroken line of members from your Dynasty; if your Dynasty ends, so does your game.  

Now, the representation of Dynasties in CK2 was limited. A character belonged to a Dynasty, and that was that - you got a minor opinion boost with characters that were of the same one, and nothing more. In CK3, we really want to emphasize the power that Dynasties held, and their impact on the medieval world! We want you as the player to feel a bond with your Dynasty, and care for it. To achieve this, we’ve done a multitude of things!  

![DD2.png](https://forumcontent.paradoxplaza.com/public/509765/DD2.png "DD2.png")

  

Firstly something that we know will especially please CK2 players, we’ve redefined what a Dynasty actually is - not a monolithic entity, but a collection of Houses. No longer will Dynasties have just one name, one Coat of Arms, and one identity - instead several Houses (aka Cadet Branches!) will be collected under the umbrella that is the Dynasty, working together (theoretically…) towards bringing renown upon the Dynasty!  

**So, what is a House?**  
Each Dynasty will have a Founding House (usually of the same name as the Dynasty), which is the first House of that Dynasty. As the game progresses, ruling Dynasty members that are distant by blood to the current House Head (more on this below) may choose to create a Cadet Branch - effectively creating a new House under the Dynasty. Creating a Cadet Branch makes the character creating it House Head (with the most powerful House Head becoming Dynast), and by extension free from the direct influence of their old House Head.  

Making your own Cadet Branch requires quite a bit of prestige, that you do not stand to inherit your House Head’s titles, and that all of your Dynastic ancestors are dead (your father can’t be alive, for example). Cadet Branches/Houses come with a lot of flavor: their own names, Coat of Arms and Mottos, usually inspired by the location in which they are founded, and the founding character. For example, if a ruler of the Jimena Dynasty would create a Cadet Branch in southern France, they might be called the Toulouse-Jimenas, and so on.  

![DD1.png](https://forumcontent.paradoxplaza.com/public/509771/DD1.png "DD1.png")

  

**Now, what is a House Head or a Dynast?**  
Within a House there is always a leader, a House Head, that wields power over the rest of the members. A House Head has the power to legitimize bastards, call House members to war, and demand that they adhere to their Faith (refusal to convert will result in them creating a new Cadet Branch). The House Head also has inherent leverage on all House members born after they were made head, by virtue of getting a Hook on them (more on Hooks in another DD). They also gain passive prestige based upon the number of members in their House. House leadership follows the succession of the House Head, so that if you’re the leader of your House you will most likely keep that title on succession.  

The Dynast, on the other hand, wields significantly more power than a House Head - with their power encompassing the members of all Houses of the entire Dynasty! The Dynast is always the most powerful House Head of a Dynasty, with leadership being updated on the death of the old Dynast. In addition to everything the House Head can do, the Dynast can also Disinherit/Restore Inheritance, Denounce/Forgive members of the Dynasty (which affects opinion in a major way), personally Claim titles held by Dynasty members, and make Dynasty members end wars they have against each other. All of these powers work against every member of the Dynasty, not just the House they’re a part of. The Dynast also gains prestige for every living member of the Dynasty. Being the Dynast is very powerful indeed, but you have to carefully weigh the powers against other benefits, as they cost Renown.  

**So what is Renown?**  
Renown is a resource accumulated by a Dynasty, and is used for several things. Firstly, all renown earned by a Dynasty counts towards its Level of Splendor. The Level of Splendor is the outward perception of the Dynasty, how well it is perceived in the eyes of the world, and affects the prestige you get on birth, the prestige when marrying into it, and the maximum long reign opinion you can get. Having a high level also makes it much easier to arrange marriages, especially with Dynasties below your level. Regardless of if Renown is spent or not, the Level of Splendor won’t decrease. The higher your Dynasty’s Level of Splendor, the more impressive its Coat of Arms frame will look. Peasant Dynasties will start at a negative Splendor level, which means that you’ll actually lose prestige for marrying them.  

Renown itself is a spendable currency, representing the clout your Dynasty holds over itself. Its use is twofold; firstly it can be used for the most powerful Dynast interactions (getting claims, disinheriting, etc.) and secondly for unlocking Dynasty Legacies (more on this below).  

The way you get Renown encourages you to mimic a ‘playstyle’ that was common in reality, but that wasn’t very practical in CK2 - spreading your Dynasty far and wide! You will gain renown for every ruler of your Dynasty that isn’t a subject under another member of your Dynasty. This is based on tier, which means that a King will give more Renown than a Duke, and so on. Marrying in such a way that your Dynasty ends up on the throne of a foreign realm is therefore useful for other reasons than to just murder them until *you* inherit their lands. Having your Dynasty spread out will give you more Renown, and thus a more powerful Dynasty overall. For example, if you’re playing as the King of England you will NOT gain renown from your landed vassal brother, but you WILL gain renown from your Dynastic cousin ruling a Duchy in the Holy Roman Empire. You will also gain renown from marrying away your dynasty to be spouses of powerful rulers, symbolizing your newfound influence in their realms. This gives you a reason to carefully plan the marriages of your kinsmen, even if you are not in need of an alliance!  

**So, what are Dynasty Legacies?**  
We all know that the playing field in Crusader Kings is a very volatile one, you might be Emperor of the World as one character, while being reduced to Count of Norfolk as the next. Dynasty Legacies offer some permanence in this otherwise very wild world, in the form of modifiers and unlocks that affect every member of your Dynasty. Essentially, by using Renown you get to shape what your Dynasty is known for. There’s a myriad of Legacies to choose from, all divided into tracks with an appropriately thematic name, such as ‘Kin’, ‘Guile’ or ‘Blood’. These aim to represent notions the world had (or has) about certain dynasties, i.e., that the Seljuks are warriors, the Abbasids lawmakers, the Habsburgs diplomats (and, ahem, prone to marrying their own kin), etc. Each Legacy track contains five unlocks, each costing a progressively higher amount of Renown to unlock.  

![DD3.png](https://forumcontent.paradoxplaza.com/public/509767/DD3.png "DD3.png")

  

In this Dev Diary we will go into details on one of these tracks, “Blood” (which also happens to be my favorite). This track is designed for those of you who enjoy breeding traits into your family line, with the first few unlocks all focusing on increasing the chance of inheritance, emergence, and reinforcement of genetic traits (more on genetic traits in another DD). The last few unlocks will reduce the chance of negative traits appearing (essentially allowing for more.. ‘risky’ marriages), give you the chance to choose a genetic trait to be more common among your kin (i.e. beautiful, intelligent and strong… but also giant or dwarf. No matter how much I pleaded with art I couldn’t get a ‘Habsburg chin’ trait, though!), and finally rounding off with an increase to your Dynasty members Life Expectancy (which increases both their average age, and average fertility - this even means that women of your dynasty remain able to bear children for longer!).  

Legacies take a long time to unlock, and you will have to work hard toward unlocking even one full track - though their power more than makes up for the wait. Legacies are chosen and unlocked by the Dynast, so make sure that you’re in control of your Dynasty.  

That’s all for this time! We won’t spoil any more of the Legacy tracks for now, but rest assured that they all offer very interesting opportunities for you to shape your dynasty as you would like it! Next up we have a sneak preview of the map, stay tuned for the next DD.

<!-- artifact:reactions:start -->
- 12 Like
- 7 Love
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 37 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
