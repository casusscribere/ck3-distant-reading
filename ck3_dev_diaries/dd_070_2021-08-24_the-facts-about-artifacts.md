---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1488487/"
forum_thread_id: 1488487
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 70
title: "Dev Diary #70 - The Facts about Artifacts"
dd_date: 2021-08-24
author_handle: Baron von Shoes
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1161
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1488487'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1683.jpg?1629826845
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_203_to_207
    action: preserved_and_flagged
    counts:
      Like: 166
      Love: 140
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_215_to_308
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_309_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1683.jpg?1629826845)
<!-- artifact:thread_banner:end -->

# Dev Diary #70 - The Facts about Artifacts

<!-- artifact:thread_metadata:start -->
- Thread starter [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)
- Start date [Aug 24, 2021](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-70-the-facts-about-artifacts.1488487/)
<!-- artifact:thread_metadata:end -->

Hello everyone! Shoes here, back to talk about what is genuinely my favorite feature of The Royal Court — Artifact generation! One of the goals we had for Artifacts in CK3 was to ensure that the artifacts your rulers acquire will feel truly distinct from another. No longer will you have a royal treasury filled with identical swords — now you will have a royal treasury filled with an assorted variety of different swords!  


## Artifact Features​

All Artifacts in the game can have a set of Features that determine both how they were created as well as what they were made from. For example, ‘Oak’, ‘Ash’, and ‘Pine’ are all features of the ‘Wood’ type, which is used to make wooden furniture, spear shafts, book covers, etc., while ‘Engraved’, ‘Filigreed’, and ‘Painted’ are ‘Decoration’-type features which skilled craftspeople can use to decorate artifacts to make them more suitable for royalty.  

The main use of Features is to create immersive descriptions for the artifact. Whenever a new artifact is created (such as from an [Inspiration](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/)), it will gain a set of appropriate Features based on various factors including culture, geography, craftsmanship quality, wealth of the capital city, and event decisions made during the creation process. These Features are then used by the artifact’s description to emphasize any distinctive characteristics that it has! Note that that these Features will not be represented in the 2D and 3D art of the Artifact, as we have far more varieties of Feature than we could reasonably produce art for.  

![ArtifactExamplesItalian2.png](https://forumcontent.paradoxplaza.com/public/737854/ArtifactExamplesItalian2.png "ArtifactExamplesItalian2.png")


A screenshot containing 6 example Artifacts. NOTE:Under active development. Values and content subject to change.​


The thing I love about this system is not just that it will generate and display differences between two different axes your ruler commissions from a blacksmith — it is that those differences will be even more pronounced between Artifacts created in the different regions of the world. This means Artifacts that you loot from your defeated foes while on crusade or during overseas raids will be far more distinct from other Artifacts in your treasury, serving as a memento of the great distances you or your ancestors traveled on their journeys.  

Of course, we have many types of Artifacts apart from weapons, and some of the material and craftsmanship differences become truly pronounced when you start looking at the type of Artifacts that are created explicitly for rulers to show off with! For example, a crown crafted in Afghanistan might feature pieces of its legendary lapis lazuli, while one made in the Baltic region could instead feature an impressive chunk of amber as a centerpiece. Different varieties of gemstones, cloth, lumber, shells, and animal horns… the range of possible combinations is truly vast!  

![ArtifactExamples2.png](https://forumcontent.paradoxplaza.com/public/737855/ArtifactExamples2.png "ArtifactExamples2.png")


A screenshot containing 6 example Artifacts. NOTE:Under active development. Values and content subject to change.​

## Artifact Modifiers​

As you probably noticed in the above screenshots, every Artifact has a set of character modifiers which are applied to their owner while they have them equipped. Unlike in CK2, there are no ‘slotless’ Artifacts, so in order to gain any benefit from owning an Artifact at all you must have it equipped in one of your personal slots (Weapon, Armor, Regalia, Crown, Trinket) or court slots (Lectern, Throne, Wall Hanging, etc.). By ensuring you can only have a set number of artifacts benefiting a character at once, it becomes much easier for us to balance Artifacts and avoid the massive bonuses characters could gain in CK2 by accumulating vast libraries of forgotten lore, new inventions, and piles of statues.  

One guiding principle we used while designing these Artifact Modifiers is the “no overtly supernatural effects” rule that guided us during the base game’s development. For example, a masterfully-forged weapon granting Prowess is straightforward and sensible, as characters fight better with a good weapon in hand. That same weapon boosting Advantage or Army Gold Maintenance is maybe less obvious, but can still be explained by serving as a symbol of hope and inspiration for the soldiers in an army and boosting their morale. Something like No Penalty For Crossing Rivers is nonsensical for an Artifact weapon though — we are not giving rulers access to the equivalent of a fully-functional Staff of Moses! Modders, of course, can add whatever modifiers they wish to an Artifact.  

## Historical Artifacts and Trinkets​


Of course, not all Artifacts will be artisanal masterpieces! The important thing for Artifacts is that they are meaningful to their owner in some way — this meaning doesn’t need to be purely economic or functional!  

Instead, some Artifacts may have great historical value despite a plain appearance, such as Charlemage’s Throne. Other Artifacts might only hold sentimental value, such as a good-luck charm or a locket given to you by a lover which reduces Stress. Finally, some Artifacts may instead be relics of a rather… dubious provenance, yet still useful for those who believe in their power (or at least claim to).  

![bones3.png](https://forumcontent.paradoxplaza.com/public/737856/bones3.png "bones3.png")



## Growing Pains​


Work on the Royal Court expansion is progressing, and it's looking better each day that passes. Now, we want to be upfront and say that it's going to take longer than many of us expect for the expansion to be released. There are many reasons for this; the expansion is very technically challenging and we're doing things we've never done before from the ground up. We want a Royal Court that looks as grand as the mechanics that support it.  

We've also had the recent organizational changes that affect how we work, as many of you know we've split into three studios - and with change comes a period of adaptation. The team has grown significantly in recent times. A lot of time has been spent onboarding new members to the team, and we've onboarded more people than we ever have before. While it may have a negative short-term impact, it's definitely going to be a solid investment for the future of CK3, not only for the release of Royal Court, but also our future expansions, and beyond. Of course the extended period of working from home makes things take longer than expected. This is something we have touched on before due to how the working conditions have been recently.  

Rest assured that we're still working as hard as we can and things are progressing nicely, and are aiming for a release later this year. We will of course have more exciting details to share in upcoming dev diaries.  

For now we’ll leave you with this little extra teaser:  


![teaser.png](https://forumcontent.paradoxplaza.com/public/737857/teaser.png "teaser.png")

<!-- artifact:reactions:start -->
- 166 Like
- 140 Love
- 10 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)**
Role: Content Designer
Badges: 35
Messages: 65
Reaction score: 2,138

*[Full game-badge icon list of 35 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
