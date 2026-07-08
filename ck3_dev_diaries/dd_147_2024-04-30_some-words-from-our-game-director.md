---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1673686/"
forum_thread_id: 1673686
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 147
title: "Dev Diary #147 - Some Words from Our Game Director"
dd_date: 2024-04-30
author_handle: rageair
expansion: Legends of the Dead
patch: Patch 1.12
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1486
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1673686'
extraction_rationale: |
  Captured via Claude in Chrome (mcp__claude_in_chrome__get_page_text)
  because WebFetch could not retrieve full body (truncated inline). XenForo
  structural markers were synthesized by process_chrome_capture.py to let
  extract_diary.py's boundary regexes work on the cleaner DOM-text input.
detected_artifacts:
  - type: webfetch_metadata
    location: raw_lines_1_to_~27
    action: discarded_from_output
  - type: forum_chrome
    location: raw_lines_~28_to_5
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_7_to_9
    action: preserved_and_flagged
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
  Chrome-captured fetch: author_handle is synthesized because the
  XenForo signature card isn't present in DOM text. inline_image_count
  reflects body-text image references only. Reactions block absent.
---

# Dev Diary #147 - Some Words from Our Game Director

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/synthetic.0/)
- Start date [Apr 30, 2024](https://forum.paradoxplaza.com/forum/threads/.1673686/)
<!-- artifact:thread_metadata:end -->

Greetings! This Dev Diary will be a mixed bag of various things - there's a lot going on, and therefore a lot to talk about. I want to take this opportunity to address feedback, talk design philosophy, shine some light on how we're working, set some expectations for Roads to Power, tease some things coming in the future, and show off the 1.12.5 changelog for a free update happening on May 8th. In other words, this will be a big and a little bit all-over-the-place diary, but bear with me.

To start off, let's talk about Community Feedback!

There's a lot of feedback coming in for the features of Legends of the Dead, and we're doing our best to collect it. We try to find as much feedback as we can from as many different sources (forums, Reddit, videos, reviews, etc, etc.) as we can - even if you feel like we're not there, I promise that we read everything - or we try to - and have it in the back of our minds. That said, let's start off with Plagues.

Plagues
Plagues is the feature that has been the easiest to collect and action feedback for - even if various types of feedback are sometimes conflated and need to be untangled for us to know what we should change. Your sentiment is somewhat split between plagues either being too easy or too hard, but uniformly they are perceived as annoying by the sheer amount of events they can summon (especially in larger realms).

For Plagues, we're looking into having balance changes go out together with an update on the 8th of May. The full changelog can be found at the end of this post.

The vast majority of the 'event spam' was due to one seemingly-innocent bug in the Alms event; it didn't have a cooldown set. This means that regardless of our intentions, it'd always be valid to fire, which is of course not as intended. In fact, a lot of the events were set up to simulate negative consequences of unchecked plagues - but as many of you have rightfully pointed out, the general negative modifiers to development and other things are more than enough to represent this. That said, increasing the cooldowns significantly for most of the events that either have easy-to-happen triggers or major negative effects should go a long way in making this feel better.

The second part of making sure the events you get are relevant for you was to make it so they only happen if they're near an area you care about: if you're the emperor of a world-spanning empire, you don't care about the goings-on of a distant backwater, or even if you're just the King of France you don't necessarily care what's going on in the very southernmost parts of Aquitaine - after all, the risk of the plague reaching your lands from there isn't that great. It seemed that the most common feedback here was to limit the events by distance, so that's exactly what we did - they can now only happen if the plague is in your domain or within a certain distance from your capital (roughly one Ireland, it's less than you might think).

Alongside this, we've reduced the overall frequency of plague events and shifted the ratio between minor/major/apocalyptic plagues away from minor and towards major/apocalyptic in an effort to make the content you receive more impactful - this should mean that you get fewer plagues overall, but the ones that happen are more significant. We've also removed the block on achievements when you lower the frequency, and added an additional option where you can choose to disable plagues (minus the black death) entirely should you wish.

Another recurring point of feedback is difficulty, or rather the lack of challenge - it is felt like the AI is much worse at handling plagues than the player, and this I agree with. While the AI will never be as responsive as the player when it comes to isolating or secluding, they should all treat it as a threat to be countered - choosing to defend themselves shouldn't be dependent on minor quirks of personality; only truly major ones.

Currently, larger Counties (with more Baronies) are better at defending against plagues - and that was never our intention, as this is literally the opposite of what happened historically - therefore we've shifted the plague resistance granted by buildings from County-wide to Barony-wide. This should encourage an alternative playstyle of having fewer-barony Counties in your domain in order to protect development. This is also much more of a challenge for players than it will be for the AI, evening the playing field a bit.

The full changelog for the 1.12.5 update can be found at the very end of this Dev Diary.

Legends
Legends are a completely different beast altogether, and are much harder to collect feedback for - opinions on what to do or change differ wildly at this point in time. Of course we're aware of the general sentiment surrounding the feature, which is why we're still looking at as much feedback as we can. The update we deployed close to the release targeted some of the widely agreed-upon points of feedback, such as adding a Legend Library where you can see completed legends forever, and more reactive variations in chapter texts to things your character does (such as winning battles, having children, etc.), among other things. For this update, we've mainly improved the Legends mapmode as we found it uninspiring and not pleasant to look at due to its limited color palette (and similar colors tended to blend together).

[Image - New legend colors]

The feedback we're collecting now is hard to act upon. As I mentioned, opinions vary greatly - from thinking that they are underpowered and useless, too overpowered and way too good, or that they should be something else altogether. Some of you are bringing up the example of CK2 Bloodlines (which is interesting to me, seeing as I designed them back in the day.) The Bloodlines of CK2 were designed to be more of a 'fantasy' feature, where great, lasting reputations were built by people *actually doing* the great and/or implausible deeds the reputations spoke of - this would then be literally transferred in their blood to either a patrilineal or matrilineal lineage (with some convoluted breeding necessary to 'stack' multiple lines on the same character). On the contrary, Legends in CK3 were designed to mimic what medieval rulers actually did; embellish otherwise mundane stories into epics of great renown - all in order to bolster their legitimacy in the eyes of their subjects or the renown of their dynasty. Which of the two approaches is the best can be debated, and I think there's merit to both. We wanted to go for the more true-to-history one for CK3 - if nothing else - because it's something we hadn't done before.

Truth be told though, I think the problem with Legends lies less in the feature itself and more in how we communicated them in Dev Diaries and similar - we weren't clear enough what they were going to be. This is something we can act upon. Going forward, any Dev Diary we're making on a feature will aim to be less open for interpretation. As with diaries of old, we'll try to describe features in as much detail as possible. We don't want any misconceptions about what the features are or how they work. You can expect the diaries for Roads to Power to be detail-filled behemoths when they start.

Bettering the Game
Next up, I'd like to share some details on how we work to make the game better over time. No matter if we're working on an expansion, free update, or other type of release, we always try to improve the game by doing various initiatives and looking at feedback.

How We Work
There are different ways we're doing this, such as through the dedicated Balance Days we have every three weeks - for which we keep a big sheet of 'game balance areas' that we review and add to.

Currently, these days are focused on improving some of the older content we've released, as well as doing balance passes on resources such as Prestige and game components such as Cultural Traditions. The main philosophy we're following when reviewing old content is to balance it for fun. If a piece of content isn't already engaging, flavorful, interesting, or fulfilling a specific purpose, then it needs to at l

Written by

### [rageair](https://forum.paradoxplaza.com/forum/members/synthetic.0/)

Paradox Staff
