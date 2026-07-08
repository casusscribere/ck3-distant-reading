---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1312112/"
forum_thread_id: 1312112
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 10
title: "CK3 Dev Diary #10 - Lifestyle Events"
dd_date: 2020-01-21
author_handle: Baron von Shoes
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 773
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1312112'
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
    location: raw_lines_190_to_191
    action: preserved_and_flagged
    counts:
      Like: 5
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_199_to_246
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_247_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #10 - Lifestyle Events

<!-- artifact:thread_metadata:start -->
- Thread starter [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)
- Start date [Jan 21, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-10-lifestyle-events.1312112/)
<!-- artifact:thread_metadata:end -->

Greetings and salutations!  

I am one of the Content Designers at Paradox, where I have been working on Crusader Kings III for the past 2 years. You may have seen me poking around our Discord channel on occasion, or here on the forms in the last Dev Diary. Today I am here with the next installment in the Lifestyles series, where I will be talking about Lifestyle Events.  

We have already covered a good deal of how Lifestyles work from a systemic point of view, but how do they influence your character’s story? What does your Lifestyle mean to your ruler beyond some bonus skill points and a handful of perks?  

Much like in CK2, when you pick a Lifestyle Focus you will begin getting events related to that Focus. Unlike in CK2, however, these events are not mere stepping stones toward acquiring a Lifestyle Trait, as that progression is handled by the perk system. Instead, Lifestyle Events in CK3 represent the various opportunities (or crises!) that have arisen as a result of the extra time and attention your ruler has been devoting to their Focus.  

For example, if you pick the ‘Stewardship - Domain’ Focus, you will begin receiving events about the management of your ruler’s domain and the holdings within it. You can choose to be strict or lenient, fair or corrupt, generous or greedy, etc. While there is rarely a ‘correct’ answer, the choices you make here will influence the prosperity of your realm, the size of your treasury, and how your ruler will be remembered in history books.  

![events_01-wm.jpg](https://forumcontent.paradoxplaza.com/public/527593/events_01-wm.jpg "events_01-wm.jpg")

  

Then again, you might prefer to take the ‘Intrigue - Temptation’ Focus, where you will receive events about seduction, desires, and covertness. You can lead your courtiers and vassals on, manipulating them into doing favors for you or interceding with others on your behalf. You can sustain long-term affairs, planting agents in foreign courts who will do your bidding when the time is right. Or, just maybe, you’re simply the type of person who wants to have a good time, seducing every lady or lord you desire, indulging in a wild revelry of stress-relieving hedonism and debauchery? The choice is yours to make!  

![events_03-wm.jpg](https://forumcontent.paradoxplaza.com/public/527594/events_03-wm.jpg "events_03-wm.jpg")

  

There are many more Focuses besides these two, of course, such as ‘Learning - Scholarship’, where you will get the chance to delve into old books to study natural philosophy and run questionable experiments — here you can decide just how far you will go in the search for knowledge, and if it is worth it to push the boundaries of church doctrine to discover the secrets of nature...  

![events_02-wm.jpg](https://forumcontent.paradoxplaza.com/public/527595/events_02-wm.jpg "events_02-wm.jpg")

  

...as well as the more practical ‘Diplomacy - Family’ Focus, where your attention to your family will give you opportunities to improve relations between relatives, enhance the prestige of your dynasty, and even take a more active role in molding your heir to be a worthy successor for your great legacy!  

![events_04-wm.jpg](https://forumcontent.paradoxplaza.com/public/527596/events_04-wm.jpg "events_04-wm.jpg")

  

In addition, your rulers are savvy individuals (or would at least like to think so); they won’t just single-mindedly pursue their Focus at the expense of all else. You will also receive occasional events pertaining to other Focuses within the same Lifestyle, representing various opportunities you have discovered that you weren’t necessarily pursuing, but would still be foolish to ignore. This will help mix things up a little and make keeping the same Focus for a long time more interesting.  

Taken all together, Lifestyle Events become an integral part of the Lifestyles system in CK3 that define how your current ruler lives their life and what impact that has on their realm and dynasty. Many of the choices you will have to make have both pros and cons, which means what you decide to do as one ruler may be very different from what you do as another. Since each of your rulers will have different reasons for picking a Focus, this will lead to varied and interesting gameplay across multiple generations, as each subsequent ruler is presented with a wide variety of new and changing situations to take advantage of in pursuit of their ambitions.  

That's all for now, but be sure to join us next week for an in-depth dive into the Intrigue Lifestyle, featuring the Seducer and Torturer perk trees!

<!-- artifact:reactions:start -->
- 5 Like
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)**
Role: Content Designer
Messages: 65
Reaction score: 2,138
<!-- artifact:op_signature:end -->
