---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1506926/"
forum_thread_id: 1506926
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 86
title: "CK3 Dev Diary #86 - Under the Banner"
dd_date: 2022-01-18
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
body_word_count: 739
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1506926'
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
    location: raw_lines_~28_to_150
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_149
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1839.jpg?1642588412
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_152_to_154
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_226_to_230
    action: preserved_and_flagged
    counts:
      Like: 87
      Love: 30
      (unlabeled — rendered as base64 data URI): 4
      Haha: 1
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_238_to_343
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_344_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1839.jpg?1642588412)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #86 - Under the Banner

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Chop](https://forum.paradoxplaza.com/forum/members/pdx_chop.1377369/)
- Start date [Jan 18, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-86-under-the-banner.1506926/)
<!-- artifact:thread_metadata:end -->

Well met!  

There is a possibility you have noticed the colourful banners decorating the halls of the upcoming Royal Court expansion and wondered just how they work. If so, you are in luck!  

As I’m sure you’ve heard if you follow these diaries, equippable Artifacts are returning to the franchise in a big way, and banners are one of the types of Court Artifact which can adorn your hall.  

![wall1.jpg](https://forumcontent.paradoxplaza.com/public/782467/wall1.jpg "wall1.jpg")



**Banners**  
There are currently three types of commissionable banner: Dynasty and House banners depict the respective arms of your family, while Realm banners display the arms of a specific title (generally the primary title of the commissioner). These banners are a cut above the standard colors carried by your armies and heralds; heirlooms in their own right.  

You may wonder what happens if the design of a crest changes during gameplay, such as after the Norman conquest, or when using the new [Coat of Arms designer](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-71-a-coat-of-arms-of-your-own.1489219/) to make ground-breaking contributions to the field of heraldry.  

Never fear, you will not need to commission new banners every time you nudge a fleur-de-lis; the Artifact’s designs are tied to their corresponding dynasty, house, or title, and will automatically reflect the results of your questionable artistic skills.  

![graphicdesign.jpg](https://forumcontent.paradoxplaza.com/public/782459/graphicdesign.jpg "graphicdesign.jpg")



All Courts begin the game with a House banner, and also with a Dynasty banner if the ruler is a Dynasty Head. Additional banners may be commissioned at any time if you employ an Antiquarian. You will also be presented with these banners upon gaining a Court for the first time if relevant, reflecting your new status as a King or Emperor.  

![wales.jpg](https://forumcontent.paradoxplaza.com/public/782463/wales.jpg "wales.jpg")



You can also see above that you must be a member of the respective family or cadet branch to gain the full benefits of a Dynasty or House banner. While you may gloat by displaying the banners of other families — acquired through war or subterfuge ***—*** doing so will only improve your Court’s grandeur.  

The three banner types grant different bonuses when equipped, with greater benefits from better quality Artifacts. While House and Realm banners use the same logic as other Artifacts to determine their quality (based on the skill of the weaver and other factors), Dynasty banners are their own breed.  

**Dynasty Banners**  
Each Dynasty will generally only have one banner in the world at any given time. Unlike House and Realm banners which can be commissioned at will, Dynasty banners can only be commissioned by Dynasty Heads, and only if one does not already exist within range of you.  

However, House Heads of a Dynasty will always have claims on their Dynasty’s banner, allowing them to duel or wage war for them at will.  

![jimena.jpg](https://forumcontent.paradoxplaza.com/public/782461/jimena.jpg "jimena.jpg")



In addition, the quality of a Dynasty banner is directly tied to its Dynasty’s Renown, granting greater benefits as your family’s fame grows.  

![famed.jpg](https://forumcontent.paradoxplaza.com/public/782464/famed.jpg "famed.jpg")



The highest tier is unlocked upon reaching Legendary Dynasty Renown level. You may be relieved to hear Dynasty banners will never lose tiers, only gain them.  

To avoid unnecessary headaches, the AI knows that a Dynasty banner really belongs to the Dynasty Head, and is inclined to return it to its proper place if it ends up elsewhere, even if they are from another House (as long as they have good relations with them).  

**War Banners**  
In addition to these creatable banners, there is also a type gained only by event: the War Banner.  

![byz.jpg](https://forumcontent.paradoxplaza.com/public/782465/byz.jpg "byz.jpg")



These captured banners can only be gained after battles, and will display the emblem of the defeated side’s primary title; perfect for commemorating your glorious victories.  

**Banner Relics**  
Lastly, there are also some historical banners knocking around, such as the Banner of Muhammad, and others of more dubious provenence may be found by adventurers.  

![thank.jpg](https://forumcontent.paradoxplaza.com/public/782466/thank.jpg "thank.jpg")



I hope this has temporarily sated your hunger for banner information. Until next time!

<!-- artifact:reactions:start -->
- 87 Like
- 30 Love
- 12 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Chop](https://forum.paradoxplaza.com/forum/members/pdx_chop.1377369/)**
Role: CK3 Game Designer
Badges: 1
Messages: 54
Reaction score: 2,021

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
