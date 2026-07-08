---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1590033/"
forum_thread_id: 1590033
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 130
title: "Dev Diary #130 – Wards and Wardens - The Vision"
dd_date: 2023-06-15
author_handle: Paradoksalny Kierownik
expansion: Wards and Wardens
patch: Patch 1.10
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1294
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1590033'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2418.jpg?1686839761
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_235_to_239
    action: preserved_and_flagged
    counts:
      Like: 165
      Love: 89
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_247_to_346
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_347_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2418.jpg?1686839761)
<!-- artifact:thread_banner:end -->

# Dev Diary #130 – Wards and Wardens - The Vision

<!-- artifact:thread_metadata:start -->
- Thread starter [Paradoksalny Kierownik](https://forum.paradoxplaza.com/forum/members/paradoksalny-kierownik.1725641/)
- Start date [Jun 15, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-130-wards-and-wardens-the-vision.1590033/)
<!-- artifact:thread_metadata:end -->

Hello all!  

It's been a few weeks since we spoke but it feels like longer, what with all of you having been busy traveling, touring, tournamenting and the rest! It is time for us, nonetheless, to leave behind that world for now and take a look ahead at what we have coming up next.  


**Vision**  

Our first Event Pack, Friends & Foes, gave us something of a chance to experiment. Since then, we’ve had the chance to take a look at exactly what direction we want to start moving in with these packs, and build on what worked.  

One area that we hit upon was diversity of content and how the player experienced the game. Events are the ink that we daub on to the fabric of the narrative, but it’s how, what and why these events happen that govern their efficacy. Introducing new avenues for that content to reach the player is a great thing, provided it’s done in an unobtrusive way.  

With that in mind, we’re going to outline a few of the new features that you’ll find in Wards & Wardens (the event-pack that you voted for last January) and its accompanying patch - both available on August 22nd. Some of them we’ll talk about more in the future, so don’t expect anything too exhaustive here, but let’s start off with…  


**Captivating features**  

Hostages aren’t quite what you’d think of when you hear the term. Rather than forced holding of a person to ransom, hostageship in the Middle Ages was a political and legal status that was absolutely widespread.  

Put simply, hostages were generally given, not taken. They were, essentially, transactional guarantees. In this case, we’ve zeroed in on the most common reason for hostages to be exchanged: as a means to guarantee a peace treaty.  

In Wards & Wardens, hostages are a new type of relation somewhere between a prisoner and a foreign court guest. They reside at your court as a guest would, but cannot leave of their own accord, nor can they become knights. They are generally - though not always - children, and have found themselves in such a predicament due to their liege exchanging them away as a guarantee of non-hostility following a war, or exchanged via interaction during peacetime. Such an arrangement not only eases the mediation process, but also gives both sides some peace of mind.  

![hostage_window.png](https://forumcontent.paradoxplaza.com/public/984238/hostage_window.png "hostage_window.png")



Hostages are essentially living non-aggression pacts. Harming a hostage is a significant diplomatic incident, but it’s also a way to deter your former enemies from getting any more bright ideas about exactly to whom that border county belongs. Any ruler that you have a hostage from will suffer significant debuffs and penalties should they try and attack you - and any wardens attacking home courts also suffer similar debuffs - so hostages present one of the strongest forms of deterrent possible.  

The hostages themselves are kept in line via something else new and shiny:  


**In Perpetuity**  

We have two types of Hook extant in the game already: Strong and Weak. The latter are the type of hooks you’d get if you were to, for example, manipulate a person in some way. They are single-use, and can be refused at cost. Strong hooks, on the other hand, can be used multiple times and in a range of scenarios, but are also much rarer.  

Perpetual Hooks are a new sort of hook, which wardens can get on hostages who they treat well, and represent something of a middle ground. They are refuseable like Weak hooks, but also permanent like a Strong hook. At the moment hostages (and those that have previously been hostages) are the only characters you’d expect to see with a Perpetual hook, but just as Memories were built with expansion in mind for Friends & Foes, so too should you not be surprised if in the future you find more and wider examples of Perpetual hook usage.  


**What An Odd Fellow!**  

One of the spots that we’ve been somewhat hamstrung by in CKIII is in mediating the existence of characters that don’t quite… fit the mould, as it were.  

![eccentric_trait.png](https://forumcontent.paradoxplaza.com/public/984239/eccentric_trait.png "eccentric_trait.png")



In CKII, you’d have insane and possessed characters who did all kinds of wacky things - immortal horse chancellors and such; you know how it goes. CKIII’s takes a more grounded approach to how traits are represented: Lunatic, for example, was used increasingly loosely in CKII, ending up as an umbrella for anything ranging from slightly kooky to genuine mental illness, but CKIII sticks much more rigidly to the latter.  

This is where the Eccentric trait comes in, as a trait dedicated to the slightly odd. This allows us to group some of the more unusual situations you’d find under this new personality trait, giving them both more reason to happen for a certain character but, critically, also barring those characters who wouldn’t engage in such strange distractions from doing so. We’ll talk about this more in the coming weeks!  


**A Midwife Crisis**  

As you might expect given how hostageship skews very much towards the young, a fair percentage of what we’ve been working on has been filling out the experience of non-adult existence in Crusader Kings III. We’ve come some way in this regard since release, with Friends & Foes adding a swathe of new events and a revamp of childhood personality traits, as well as of course the Regency mechanic giving a whole new layer of intrigue to a child navigating the dangerous Medieval world.  

In Wards & Wardens, we’ve added to this with another fresh layer of childhood content - in no small part focused on hostages and their experiences - but also the addition of a Wet Nurse court position. Wet nurses held an interesting status amongst the medieval court, and adding this court position adds another layer of intricacy to the trials and tribulations of raising a child.  

![wet_nurse.png](https://forumcontent.paradoxplaza.com/public/984237/wet_nurse.png "wet_nurse.png")




**Mature Students**  

We have been delighted to read just how much you all have been enjoying all the new - and the old! - activities in CKIII since the release of Tours & Tournaments. With this in mind, we’ve attempted to utilize it to approach something that’s previously been static in Crusader Kings: education as an adult.  

![university_visit.png](https://forumcontent.paradoxplaza.com/public/984240/university_visit.png "university_visit.png")



Previously, once you had come of age, an education type and rank was assigned to you and that was that. You, aged 16, were as educated as you’d ever become! Now, whilst properly reflecting the rate at which humans grow as people as they age is something of an impossible task for a game, the current system felt a little too rigid for our liking. As such, the Adult Education activity now gives players a chance to tickle their brains at a center of learning, in hope that they can actually upgrade their education trait to a higher level!  

But what of those of us who enter adulthood with the finest education life has to offer? What steps can those people take to better themselves in adulthood?  

Worry not. We have a plan for that, too, but it will have to wait!  


**Goodbye For Now**  

Thankfully, however, you won’t have to wait all too long. Whilst we’re saying bye for now, next week [@Areysak](https://forum.paradoxplaza.com/forum/members/1200721/) will be taking us through the Adult Education Activity in CKIII from top to bottom. Hope to see you all then!

<!-- artifact:reactions:start -->
- 165 Like
- 89 Love
- 10 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Paradoksalny Kierownik](https://forum.paradoxplaza.com/forum/members/paradoksalny-kierownik.1725641/)**
Role: Corporal
Badges: 41
Messages: 27
Reaction score: 1,566

*[Full game-badge icon list of 41 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
