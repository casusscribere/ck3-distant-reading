---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1855069/"
forum_thread_id: 1855069
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 178
title: "Dev Diary #178 - A Vision in Gold"
dd_date: 2025-08-13
author_handle: PDX-Trinexx
expansion: Coronations
patch: Patch 1.17
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1533
inline_image_count: 8
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1855069'
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
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_254_to_258
    action: preserved_and_flagged
    counts:
      Like: 95
      Love: 30
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_266_to_347
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_348_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #178 - A Vision in Gold

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Aug 13, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-178-a-vision-in-gold.1855069/)
<!-- artifact:thread_metadata:end -->

Crown-wearing kings and regalia-bearing queens,  

As you read these very words, you might - by claim of blood or right of conquest - be happily nesting in a Crusader Kings III throne. Perhaps you’re just about to become king, just about to plop one of our lovingly rendered crowns on your most worthy head. Congratulations! That’s one heck of a moment to celebrate.  

Enter: the Coronation Activity. This first, and very likely most iconic, sacral moment of kingship is the centerpiece of our laser-focused new event pack. Our fans have long yearned to see this ceremony realized in digital cathedrals and in virtual flesh. I, humble Brother Jason of the design scriptorium, am here to give you a sense of the kingly activity to come.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1339337/image_01.png "image_01.png")


*[Spoilers, I guess?]*  

## Vision​

With this event pack, we tried something a little different from the formula employed in *Wandering Nobles*, *Wards & Wardens* and *Friends & Foes*: where these prior event packs scattered little tasty flavor treats throughout the game, Coronations is instead one single, discrete bundle of highly visible and mechanically impactful content. You will not have to search it out. This DLC presents itself to you, in fanfare and anticipation, the moment… you die. Or, well, the moment you graduate to kingship. Either one is good.  

So, yes, this DLC is focused squarely on the beginning of a new reign, on your initial years as a sovereign. They’re often dramatic years, aren’t they? With factions, claimants, new friends, councillors and rivals, new goals to set, and new boundaries to gaze upon. Your ruler’s Coronation won’t take place in isolation from these fresh horrors and newfound delights, no: our intent is that the Activity helps them situate themselves in their new position. It should highlight your new foes and help you identify the sources of your new character’s strength. By holding a Coronation, you might hope to - without the strain of war - address the teething problems of new rule that we all know well (factions, claimants, etc). This might end, however, in your coronation being a venue for your humiliation and, even, deposition. Don’t fear, though. Such a debacle would require a few significant political miscalculations on your part.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1339338/image_02.png "image_02.png")


*[These vassals don’t seem to like me very much]*  

Conversely, if your succession is smooth as butter on warm toast, then Coronations become a fine exercise in patting yourself on the back. A beloved, highly capable ruler has every right to pull through with fresh modifiers, currencies and incentives in hand!  

A soon-to-come developer diary will dig deeper into the mechanics of the Coronation Activity and the Oaths on offer. What I present to you now is a top-level overview.  

## The Coronation Activity​

Coronations are a new Activity type available to Kings and Emperors. They are accompanied by a new Realm Law, which states whether your ruler is Crowned or Uncrowned. While Uncrowned, you suffer Opinion and Legitimacy maluses; the only way to become Crowned is to host a Coronation. Both the Activity and the new laws are DLC-only content, and will not affect players who don’t own this event pack.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1339341/image_03.png "image_03.png")


*[Soon, soon you will be crowned and these modifiers will be history…]*  

You may only host a Coronation when first becoming a King or Emperor: thus, a Coronation host must either be a new heir succeeding to the throne, or a ruler who has just increased their title tier. The majority of CK sovereigns will only ever hold one Coronation, but this DLC strongly incentivizes everyone king-tier and above to host a Coronation.  

The Coronation Activity brings together courtiers, vassals and neighboring rulers to witness the creation of a new sovereign, to socialize, and to politic frenetically in the shadows. Equipped with an array of Intents for hosts and attending characters, and with a wide range of events, Coronation is a relatively reliable source of Legitimacy, Opinion and Prestige (for the host), but can be employed towards many other ends as well.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1339343/image_04.png "image_04.png")


*[Why thank you, pointy hat man]*  

Mechanically, the Coronation Activity focuses on replayability, on reactivity to your current situation, and on agency for both the attendees and host. Through time and across space, coronation ceremonies tended to hit many of the same beats, to use many of the same ideas and phrases, but the context of their words were ever-changing, and we designed with that mutability in mind. These moments were never merely ceremonial. They were always also political.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1339344/image_05.png "image_05.png")


*[Plenty of opportunities for the new sovereign to get to know their vassals]*  

Our guiding principle for Coronation flavor was to create content that feels truly regal, truly historic, worthy of Charlemagne, Chinggis, and mighty Baldwin of the great and righteous Latin Empire (is it Splintered Crusade o’clock?). Indeed, because Coronations can only be held by king and emperor-tier rulers… if someone’s disrespecting a host at their own Coronation, that someone is going to have a damn good reason, and is very likely going to pay dearly for their poor manners.  

The main regional flavor focuses of this DLC are Christian and Western European. Therein are found the most widely-recognized symbols of medieval coronation, and furthermore - the rites of coronation across Christendom, though varied in order and form, were honestly quite surprising to me in their relative uniformity. That’s not to say there aren't triggered events and flavor for different faiths and government types! These are just a little harder to spot than our orbus cruciger activity icon.  

## Magnificence​

As I mentioned, Coronations can either be an absolute cakewalk or a rough ride, based on the competence of your ruler, the wealth at your disposal, and the opinion of your attendees. Magnificence, the measure of a Coronation’s success, is the main metric we use to determine how troubled and unflattering your Coronation is becoming - or how majestic and glorious! It’s drawn from the Coronation’s setup, from the actions of the host, *and* the maneuvering of the most significant friendly and hostile attendees.  

All I’ll say right now is… you probably don’t want to skimp on the Activity Options, unless you really have to.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1339345/image_06.png "image_06.png")


*[Keep things feeling magnificent and you won’t be disappointed]*  

## Host & Guest Interplay​

A King is made by the assent of the church, of his nobles, and *I guess* the common people. Coronations aim to highlight all these relationships, and give both host and guest the means to explore them. To aid in this, we have added a widget to the Coronation Activity interface to help you track the most powerful Supporters (characters who like you, the Host) and Detractors (jerks) at your Coronation. These groupings don’t mean anything beyond the Activity, but have a significant impact on its outcomes.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1339347/image_07.png "image_07.png")


*[Major Supporters and Detractors are shown on the right. These are the attendees best able to affect a Coronation’s successfulness]*  

Attendees may use their Intents to support the new sovereign, to undermine the Coronation, or - most often - to push forward their own interests. Hosts, meanwhile, use Intents mainly to focus on one group of attendees over another, and manage the members of that group.  

## Imperial Anointment​

The Coronation Activity can be held as a regular old Coronation, or a more special type: Anointment.  

Only available to emperor-tier rulers of appropriate faiths, Anointment is a grander ceremony that features your Head of Faith as crowning officiant. It must be held at a Holy Site, and has some additional requirements which weed out sinners and illegitimate sovereigns. Anointment offers additional bonuses, particularly where Legitimacy and the Opinion of others are concerned.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1339348/image_08.png "image_08.png")


*[Behold: the Pope oiling you up]*  

## Oaths​

Though, as I’ve said earlier, the body of this DLC is firmly rooted in the early reign, its arms reach out across your ruler’s years on the throne. During Coronations, you will be called upon to select an Oath, a timed Decision that is in essence an objective for your rule. Sometimes, the transition from one PC to another can dull a player’s sense of purpose and stagger the momentum of their game. Committing your new ruler to an Oath sets you on a new path, and may serve to get things rolling again!  

More info to come on Oaths soon.  

## Bye, For Now!​

I bid you farewell, friends, kings, queens, and gamers. Until next I may write of crowns and royal heads and downwards, placing-type motions of the hands.  

If you have any thoughts or ideas about Coronations in CK3, do sound off in the comments!

<!-- artifact:reactions:start -->
- 95 Like
- 30 Love
- 13 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 17 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
