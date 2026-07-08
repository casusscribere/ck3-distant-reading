---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1565308/"
forum_thread_id: 1565308
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 113
title: "Dev Diary #113 - Community Choice Event Pack"
dd_date: 2023-01-17
author_handle: rageair
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 709
inline_image_count: 2
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1565308'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2170.jpg?1674040070
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_188_to_192
    action: preserved_and_flagged
    counts:
      Like: 106
      (unlabeled — rendered as base64 data URI): 2
      Love: 25
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_200_to_312
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_313_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2170.jpg?1674040070)
<!-- artifact:thread_banner:end -->

# Dev Diary #113 - Community Choice Event Pack

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Jan 17, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-113-community-choice-event-pack.1565308/)
<!-- artifact:thread_metadata:end -->

Greetings!  

We’re all back, gathered from the holidays, and ready to set sail for 2023! Actually, most of us have been back for a few weeks by this point, working away on this year's big release, but we're not going to be talking about that just yet. That's not to say we're not going to in the future, but until we are ready to, we want to give you something to dig your teeth into as a community. This is the first of a small series of Dev Diaries about some more minor things, teasers, and today, about a brand-new community initiative!  
But first, here’s a small teaser of something coming in the expansion:  


![teaser1.png](https://forumcontent.paradoxplaza.com/public/926629/teaser1.png "teaser1.png")


[Image - Teaser]  

Later this year, after we’ve released the next big expansion and before we start working on the next large project, we’ll have a period where we have the time and opportunity to work on an event pack. For the last event pack we chose ‘friends and foes’ as the core theme, as it was something practically everyone in the team felt strongly about, and something that needed more content in the game. Since then, we’ve had *so many ideas* for future event packs, both from within the team and outside, and this time it’s harder to choose…  

Therefore we’d like to invite all of you to help us decide which theme to pick! We have three themes that we’ve curated, which means a few things; each theme has designers on the team that are passionate about them, and we know *roughly* what free feature we’d like to add to the update that will accompany the event pack: generally we'll be aiming for something with a similar size and impact as Friends & Foes' Memories system, which heavily ties into the events we're making but is relevant across the game as a whole.  

We don’t have final names for the event packs yet, but as we enjoy alliteration here’s what we’re calling them and a very brief description of each:  

**Wards & Wardens** - Anything childhood-related, with themes such as: playing as a child, being a guardian, handling children in court, and so on. A deep dive into what being a child in the Middle Ages was actually like, and what guardianship meant in practical terms.  

**Love & Lust** - An exploration of more intimate relationships, with themes such as: expanded seduction, romance, married life, and so on. This would be a great time to allow lovers and spouses to take on a larger role in the game.  

**Villains & Vagabonds** - Events and content around Dread and Tyranny, exploring what it means to be dreaded, leveraging your fearsome reputation, making dread more visible, and the consequences and opportunities of being a tyrant. It’d also be interesting to explore the other side of the coin from Dread - fairness, and honor.  

Even though this event pack is something we’ll work on later this year, it’s good to get your input now - this way we can start working on it without delay as soon as the next big expansion is out! As we have a lot of talented event-crafters on the design team, we feel quite confident that we can adapt to whatever theme you, as a community, choose.  

If this turns out to be a popular activity, it is possible that we will do it again in the future! The themes that do not get chosen this time will likely make a comeback, alongside some new challengers.  

The poll to vote is located in a separate forum thread [**here**](https://forum.paradoxplaza.com/forum/threads/ck3-community-choice-event-pack-poll.1565251/). Voting will begin today and you will have until **January 27, 8am CET** to discuss the different themes and cast your vote. We’re looking forward to seeing which theme you like the most!  

[**Vote Now**](https://forum.paradoxplaza.com/forum/threads/ck3-community-choice-event-pack-poll.1565251/)​


[![EventPackThemeVote.png](https://forumcontent.paradoxplaza.com/public/926630/EventPackThemeVote.png "EventPackThemeVote.png")](https://forum.paradoxplaza.com/forum/threads/ck3-community-choice-event-pack-poll.1565251/)

<!-- artifact:reactions:start -->
- 106 Like
- 27 (unlabeled — rendered as base64 data URI)
- 25 Love
- 2 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
