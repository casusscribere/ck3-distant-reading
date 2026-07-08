---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1494388/"
forum_thread_id: 1494388
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 77
title: "CK3 Dev Diary #77 - Becoming a Polyglot"
dd_date: 2021-10-12
author_handle: rageair
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1081
inline_image_count: 15
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1494388'
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
    location: raw_lines_~28_to_162
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_161
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1740.jpg?1634115339
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_164_to_166
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_307_to_312
    action: preserved_and_flagged
    counts:
      Like: 145
      Love: 62
      (unlabeled — rendered as base64 data URI): 6
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_320_to_432
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_433_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1740.jpg?1634115339)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #77 - Becoming a Polyglot

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Oct 12, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-77-becoming-a-polyglot.1494388/)
<!-- artifact:thread_metadata:end -->

Greetings!  

As you all know, one of the new Cultural Pillars each Culture has is their native Language. Now, what effect does language have? At its very core, Languages affect the Baseline acceptance between cultures - if two Cultures share the same Language Pillar, they’ll like each other better. But that’s not all, characters can also learn additional languages!  

So, why do you want to learn a language? Knowing a language cuts the (rather hefty) opinion penalties for Different Culture in half, both for Characters and Counties. Planning on conquering a foreign kingdom? Start your conquest by mastering their language, making subsequent control of your new subjects just that much easier! The less accepted your culture is, the more impact learning a language will have.  

Now for the more pertinent question, how do you learn another language? You learn new languages through scheming!  


![SchemeInteraction.png](https://forumcontent.paradoxplaza.com/public/752058/SchemeInteraction.png "SchemeInteraction.png")


[Image showing the Learn Language interaction]  

![LanguageSchemeStart.png](https://forumcontent.paradoxplaza.com/public/752059/LanguageSchemeStart.png "LanguageSchemeStart.png")


[Image showing the Start Scheme window]  

‘Learn Language’ is a Learning-based scheme, where progress and chance of success are primarily derived from how scholarly your character is. This scheme is available to everyone, even young children (who have a vastly increased chance of success/progress, by virtue of being young, less tired, and having working brains). It targets someone who natively speaks the language, having you try to emulate them. While the exact target you choose is less important than in other types of schemes, you might still get opportunities to interact with them.  

Now, learning languages takes quite some time. Though it’s possible to significantly speed up the process by employing a Court Tutor!  


![CourtTutor.png](https://forumcontent.paradoxplaza.com/public/752060/CourtTutor.png "CourtTutor.png")


[Image of a Court Tutor]  

You will also find that bonuses for this scheme have been added throughout the existing Lifestyle trees. Some examples:  


- Adaptive Traditions - Unlocks an additional Learn Language Scheme
- Embassies - Increases Scheme Power
- Chains of Loyalty - Increases Scheme Power
- Pedagogy - Increases Scheme Success Chance
- Open-Minded - Increases the Language Limit
- Smooth Operator - Increases the Language Limit

If the scheme is invalidated by, for example, the target dying, your progress is retained and you get the opportunity to choose a new target.  


![InvalidationEvent.png](https://forumcontent.paradoxplaza.com/public/752061/InvalidationEvent.png "InvalidationEvent.png")


[Image of Invalidation Event]  

When we first talked about languages, we had some people (rightfully) point out that decreasing the chance of success the more languages you know isn’t very logical. We still needed a way to prevent characters from knowing all the languages in the world, and thus we introduced the concept of a Foreign Language Limit. This represents how many languages a character can comfortably remember.  

![KnownLanguages.png](https://forumcontent.paradoxplaza.com/public/752062/KnownLanguages.png "KnownLanguages.png")


[Image of Language Limit]  

If a character exceeds their Foreign Language Limit, they will start getting events about feeling overwhelmed, giving you the choice between forgetting a language or gaining stress. In a sense, this system is very similar to how we handle characters having too many lovers.  

Of course, a character can never forget the language that is native to their culture, and that language isn’t included in the limit (as you can see in the above screenshot, Telugu isn’t included in the limit as it is his native language).  

The Foreign Language Limit is affected by many things, but primarily by a character’s Learning score, where every 5 attribute points increases the limit by one.  

With this change, we’ve made it so that the more languages you know, the higher your success chance is for learning additional languages. You have the basics down already, after all.  


![LanguageSuccessChance.png](https://forumcontent.paradoxplaza.com/public/752063/LanguageSuccessChance.png "LanguageSuccessChance.png")


[Image of a success chance breakdown]  

Now, the process of learning a language can be quite entertaining. There are many events that can happen along the way; being helped by friends or family, opposed by rivals, and so on. Here are a handful of examples of what can happen during the course of learning a language:  

![LearnLanguageEvent1.png](https://forumcontent.paradoxplaza.com/public/752064/LearnLanguageEvent1.png "LearnLanguageEvent1.png")


[Image of your Court Tutor helping you]  

If you have a particularly good Court Tutor, they can guide your efforts along very speedily.  

![LearnLanguageEvent2.png](https://forumcontent.paradoxplaza.com/public/752065/LearnLanguageEvent2.png "LearnLanguageEvent2.png")


[Image of a rival ruining your notes]  

Beware your rivals, lest they release ink-soaked birds in your study...  

![LearnLanguageEvent3.png](https://forumcontent.paradoxplaza.com/public/752066/LearnLanguageEvent3.png "LearnLanguageEvent3.png")


[Image of a very amorous misunderstanding]  

Sometimes learning a language doesn’t result in what you’d expect...  

![LearnLanguageEvent4.png](https://forumcontent.paradoxplaza.com/public/752067/LearnLanguageEvent4.png "LearnLanguageEvent4.png")


[Image of the Byzantine Emperor with a “It’s just a prank, bro”-smile]  

Sometimes your target might find your efforts laughable, and try to make fun of you.  

![LearnLanguageEvent5.png](https://forumcontent.paradoxplaza.com/public/752068/LearnLanguageEvent5.png "LearnLanguageEvent5.png")


[Image of a merchant offering you a book]  

Of course, there is an opportunity to gain a trinket-slot item that’ll help your efforts along.  

![LearnLanguageEvent6.png](https://forumcontent.paradoxplaza.com/public/752069/LearnLanguageEvent6.png "LearnLanguageEvent6.png")


[Image of someone offering to help]  

As learning a language isn’t secret, sometimes you’ll get offers from other rulers to help you… for a price.  

When the scheme completes, you have a chance of success and failure. If you’re brave, you might even choose to test your new abilities right away by penning a letter to your target!  


![SuccessEvent.png](https://forumcontent.paradoxplaza.com/public/752070/SuccessEvent.png "SuccessEvent.png")


[Image of a successful scheme]  

![FailEvent.png](https://forumcontent.paradoxplaza.com/public/752072/FailEvent.png "FailEvent.png")


[Image of a failed scheme]  

Of course, you might find that others are emulating you in their efforts to learn your language. This gives you the opportunity to praise their efforts, or perhaps you’d rather ridicule them?  


![SomeoneLearnedYourLanguage.png](https://forumcontent.paradoxplaza.com/public/752073/SomeoneLearnedYourLanguage.png "SomeoneLearnedYourLanguage.png")


[Image of someone learning your language]  

That’s it for this week! Now, this isn’t the only way languages are used in the game… next week we will dive into another use for them, something which ties directly into the mechanics of the Royal Court!

 

Last edited by a moderator: Oct 18, 2021

<!-- artifact:reactions:start -->
- 145 Like
- 62 Love
- 10 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
