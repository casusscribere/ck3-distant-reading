---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1491791/"
forum_thread_id: 1491791
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 74
title: "CK3 Dev Diary #74 - Please Kaiser, Can I Have Some More?"
dd_date: 2021-09-21
author_handle: PDX_Chop
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 831
inline_image_count: 6
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1491791'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1712.jpg?1632227554
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_212_to_216
    action: preserved_and_flagged
    counts:
      Like: 156
      Love: 85
      (unlabeled — rendered as base64 data URI): 5
      Haha: 2
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_224_to_323
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_324_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1712.jpg?1632227554)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #74 - Please Kaiser, Can I Have Some More?

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Chop](https://forum.paradoxplaza.com/forum/members/pdx_chop.1377369/)
- Start date [Sep 21, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-74-please-kaiser-can-i-have-some-more.1491791/)
<!-- artifact:thread_metadata:end -->

Greetings counts and dukes! Today we will be looking at The Royal Court from a different perspective: *your* perspective!  

While being a queen or emperor is great and all, sometimes it can be a bit of a drag to manage all those vying subjects. Sometimes, you just want to rule a small corner of a mightier realm, and enjoy the benefits of the Emperor’s protection, and while a duchess doesn’t have their own Royal Court, they can interact with their Liege’s via two new decisions.  

**Petition Liege**  
Player vassals can approach their King-or-above ranked Liege with a Petition at any time through a new decision, providing they have enough Prestige, there is something they can ask for, and they haven’t done so in the last 5 years. Lieges will currently only interact with this content if they happen to have a player as their vassal and they make their own—no doubt outrageous—requests.  

The possibilities include asking for a position on your Liege’s Council, asking for a Title you hold a claim on, or dismantling an unruly Faction in your own realm. There are currently 14 different options, each having some equivalent in the Hold Court events brought to Lieges by AI vassals, ranging from helping you convert your lands to paying off your debts.  

![petition.png](https://forumcontent.paradoxplaza.com/public/745874/petition.png "petition.png")



This will allow you to ask for things directly without resorting immediately to war, which can remain a last resort for when you need to topple that king whose tolerance of border-gore clearly proves their illegitimacy.  

![letter.png](https://forumcontent.paradoxplaza.com/public/745875/letter.png "letter.png")



It is up to the Liege whether to receive a Petitioner, though outright refusing will damage relations and be seen as slightly tyrannical. The request itself may also be rejected once heard, and the odds of acceptance by the AI will be tipped more in your favor if you make reasonable requests and maintain good relations; after all, your boss doesn’t want to be seen as unreasonable.  

![liege.png](https://forumcontent.paradoxplaza.com/public/745876/liege.png "liege.png")



If they are astute, your Liege may also ask for something in return for granting your Petition, such as a Favor Hook or a bit of Gold—a counter you can of course reject, leaving you both empty-handed.  

![second2.png](https://forumcontent.paradoxplaza.com/public/745893/second2.png "second2.png")



If a Liege is not being very forthcoming, you can also attempt to convince or outsmart a trusted advisor as a last resort, at the cost of some Prestige. You will need to pass a skill check in a relevant area, usually against one of your Liege’s councillors, or have an ally near to the throne—the King’s wife perhaps—whose assent will force your Liege’s hand.  

**Pay Homage**  
Homage represents the formal pledge of loyalty by a feudal lord to their Liege, and provides Opinion, Renown, and Prestige to both parties, providing the occasion goes smoothly. This decision is also available to AI as well as players.  

![homage.png](https://forumcontent.paradoxplaza.com/public/745880/homage.png "homage.png")



This decision costs some Prestige to initiate, is only available to Feudal and Clan vassals, and can only be undertaken once per Liege. If the ruler changes or dies, you can make a new pledge of allegiance to their replacement.  

As with Petition Liege, this decision can be rejected outright, and is not totally without risk even if they let you through the door. There is a great deal of pressure for such an important event to go well, and not all lords and ladies are made for public speaking.  

Things can go awry in a variety of ways, depending on the Petitioner’s skills and other factors: Have you put in the hours to learn Norman, or merely practised a few key lines the night before on the road to Windsor? Will your Shah empathise with your stammer, or imitate it in front of the entire Persian court? Will you forever more be called ‘the Clumsy’ by your vindictive Sultan, simply because you lost your balance once?  

![vassal.png](https://forumcontent.paradoxplaza.com/public/745881/vassal.png "vassal.png")



If something does go wrong, it is up to the Liege to decide if they will let it go—giving your rival the opportunity to publicly mock your clumsiness might not be the best idea. If they do decide to embarrass you, you will lose some Prestige and Opinion with your Liege, instead of gaining them.  

Regardless of the outcome, both your Dynasties will gain a small amount of Renown, and the rewards are increased by offering gifts in addition to your pledge, such as a Contract change in favor of your Liege.  

That broadly covers these two new decisions, so I’ll leave it there for now!

 

Last edited: Sep 21, 2021

<!-- artifact:reactions:start -->
- 156 Like
- 85 Love
- 11 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Chop](https://forum.paradoxplaza.com/forum/members/pdx_chop.1377369/)**
Role: CK3 Game Designer
Badges: 1
Messages: 54
Reaction score: 2,021

*[Full game-badge icon list of 39 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
