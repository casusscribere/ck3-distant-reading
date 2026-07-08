---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1543480/"
forum_thread_id: 1543480
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 108
title: "Dev Diary #108: Dev Diary Scheduling & Community Activities"
dd_date: 2022-09-20
author_handle: rageair
expansion: Friends and Foes
patch: Patch 1.7 (Bastion)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 751
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1543480'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2069.jpg?1663686451
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_185_to_187
    action: preserved_and_flagged
    counts:
      Like: 36
      Haha: 2
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_195_to_283
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_284_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2069.jpg?1663686451)
<!-- artifact:thread_banner:end -->

# Dev Diary #108: Dev Diary Scheduling & Community Activities

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Sep 20, 2022](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-108-dev-diary-scheduling-community-activities.1543480/)
<!-- artifact:thread_metadata:end -->

Greetings!  

It’s been (almost) two weeks since the release of Friends & Foes, and the sheer amount of reactions and feedback to it and the accompanying Bastion Update has been fantastic to see! From the many emergent stories that have been posted around the Internet (one about a peasant crush ascending to the position of councilor and subsequently being murdered by a noble out of spite comes to mind) to the impressive screenshots of vast Mongol Empires and powerful AI realms - it’s great to see how many of you returned to the game and think that it got a breath of new life. In fact, despite the smaller size of this update, more of you came back to the game and ran a longer campaign than ever before!  

Of course, if you’re experiencing any issues, pop over to the Bug Forums and report them: [Link](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1077/)  
As of the newly released 1.7.1, we’ve concluded the planned updates for this release, though if something significant appears, we’ll look into fixing it before the next update.  

As for the future, we’re hard at work on upcoming content, and we’ve been for quite some time. Previously we’ve explained that we run our projects in parallel - what we’re working on in the Stockholm studio has been in the works since before Friends & Foes (but it’s bound to take some time yet, do not expect anything too soon). Our sister studio in Thalassic is also hard at work heading up the work on upcoming content and updates, this too in parallel with work in Stockholm. While we can say that Friends & Foes was the last paid content of the year, we’re hoping to have another smaller free update out before the year is over (no ETA for now). Additional clues about what we’re working on might appear over the next few months…  

A change we want to make going forward is to be more transparent with our Dev Diary schedule. We don’t want to post so-called ‘filler’ Dev Diaries, and with the cycles being longer between updates we instead want to use this time for other kinds of activities with the community. For the sake of full transparency, for smaller updates (such as free patches or event packs) we’ll have at most two Dev Diaries. For larger updates (such as Flavor Packs) we’ll have around four, while Expansions will have roughly 2-4 months' worth of Dev Diaries.  

So what will we do instead? A variety of things - we might have Discord AMA’s, hangout streams with Devs, or sometimes we might post a Dev Diary about something not related to an update - for example, about how we work or plans we have for the future.  

If you want to partake in some of this, here’s where you can find us:  

[Discord](https://discord.gg/ck3): Chat with your fellow Community members, staff members, Modders, and other Content Creators. Also a perfect place if you want tips or a game to join!  

[Twitch](https://www.twitch.tv/paradoxinteractive): We stream weekly and go through all the latest and greatest content that we have. This is also a great place to chat with others and ask questions of our team.  

[YouTube](https://www.youtube.com/c/ParadoxGrandStrategy): If you haven’t happened to catch our Streams or just want to see a collection of all our videos, this is your one stop shop for all Crusader Kings III official videos.  

[Twitter](https://twitter.com/crusaderkings): Our latest and greatest spot for news and interaction with our Community. We are always online, as they always say. Feel free to follow us and see what we have going on from day to day.  

[Facebook](https://www.facebook.com/Crusaderkings/): Just a nice relaxed place to hang out and socialize with our Community and see what everyone is up to.  

[Reddit](https://www.reddit.com/r/CrusaderKings/): If Facebook isn’t your speed, we also have a great resource in Reddit for conversations and more detailed threads regarding the game and any questions you might possibly have.  

[Steam Workshop](https://steamcommunity.com/app/1158310/workshop/): While we do not control the content of Steam Workshop, it does contain a great number of highly interesting and resourceful Mods from our Community and has a ton of troubleshooting and technical information.

 

- 134
- 41

<!-- artifact:reactions:start -->
- 36 Like
- 2 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 26 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
