---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1755412/"
forum_thread_id: 1755412
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 171
title: "Dev Diary #171 - Post-Release Support"
dd_date: 2025-05-20
author_handle: PDX-Trinexx
expansion: Khans of the Steppe
patch: Patch 1.16
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3219
inline_image_count: 11
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1755412'
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
    location: raw_lines_305_to_310
    action: preserved_and_flagged
    counts:
      Like: 114
      (unlabeled — rendered as base64 data URI): 5
      Love: 13
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_318_to_419
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_420_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #171 - Post-Release Support

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [May 20, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-171-post-release-support.1755412/)
<!-- artifact:thread_metadata:end -->

Hello everyone! I’m Jacob, the Community Manager with Paradox Studio Black.  

My role within the studio is to strengthen communication between us and you, the players, to ensure that we understand what you want from the game and that you understand what our intentions are for the future. While I’m just one part of the broader Community Team for Crusader Kings, I’m ultimately responsible for nearly every piece of public-facing communication we publish as a studio: dev diaries, feature breakdowns, chapter premiere videos, social media posts, etc. I’m also responsible for the reverse; every piece of feedback that ends up on a designer’s desk goes through me at some point in the process.  

Today, I’m going to talk about the release of *Khans of the Steppe* and the feedback we’ve received from players, as well as how we’re addressing it. After that I’ll give a brief overview of how our development cycles work, what the hell Post-Release Support even *is*, and then cap it off with a quick look at what our next steps are as a studio.  

I am a map gamer, so fair warning: There will be a good amount of graphs and charts in this dev diary.  

### State of Launch​

As you may or may not be aware, Khans of the Steppe and the 1.16 “Chamfron” Update were released on April 28th, and the initial response was fairly positive both from a technical perspective and a player sentiment one. However, we quickly noticed a spike in crash reports and commentary from players confirming this. Setting our lovely QA team to work, we quickly identified two major contributors to instability in 1.16 and pushed hotfixes to tackle both of them.  

These fixes have led to a significant reduction in crash rates, but we’re still seeing elevated levels, so we’re still working to identify and resolve the causes of these crashes.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1295681/image_01.png "image_01.png")


*[Crash rate analytics since the release of Khans of the Steppe. The 1.16.0.2 hotfix (circled in red) made a big difference, but there’s still work to be done.]*  

While there was an immediate spike in negative reviews due to stability issues, the response at large to *Khans of the Steppe* was quite positive right out of the gate. When you spend months working on a specific project, it’s always an immense relief to see that it went well and players were having fun with the new content, so everyone at the studio was elated at the response!  

Then the review score started dropping.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1295682/image_02.png "image_02.png")


*[Steam reviews for Khans of the Steppe. You can see the ratio of positive to negative reviews shrinking over time; In the “biz”, this is considered a Bad Thing. While the amount of people who leave reviews are a sliver of a fraction of the greater playerbase, this is still a valuable source of information for us.]*  

With all of our releases, we do a series of internal reports on the state of things at predefined intervals. There’s a Day 0 report, Day 1, Day 7, etc. While the Day 0 and Day 1 reports were initially positive, by the end of the week it became clear that there were outstanding problems that took some time to reach a breaking point for players.  

So, what were those problems? In order to figure that out, we have to do some basic analysis of the reviews themselves. To begin, I took every negative review on Steam and put them into a spreadsheet where they’re arranged, translated (we try to assess feedback from as many languages as we possibly can), and categorized based on what their main complaint is.  
(This isn’t the only way we analyze feedback, but reviews are fairly easy to explain so they make ideal content for demonstrating the point in this dev diary.)  

Once everything has been neatly categorized (a task I find immensely soothing, for the record), I can generate a quick chart showing which complaints are dominating the conversation. The main cause of stability complaints in the reviews were already addressed or being investigated, so we can skip that category and take a look at the next one in the list: Balancing.  


![image_03.png](https://forumcontent.paradoxplaza.com/public/1295683/image_03.png "image_03.png")


*[Outside of stability issues, balancing concerns make up the majority of complaints about Khans of the Steppe.]*  

With my chart prepared, I can go to the design team and our Game Director to tell them “Players think the balancing is wonky, and here’s data to prove it.” From there, we can actually go through feedback to identify specific pain points and begin to address them in our first post-release support update (more on what that specific term means later).  

If you’re only interested in what’s next for Khans of the Steppe, then I’ll summarize here and save you some time: We know that players have concerns with the DLC and we’re working to address as many of these concerns as we can within the time we have allotted for post-release support before anything else is pushed off to Realm Maintenance.  

If you want to know more about how our communication pipeline from player to developer works, and how we act on what we hear from you, then read on! I intend to ramble for a bit longer.  

### Player Feedback​

In order to properly explain how we turn comments on the internet into changelog entries, I first need to talk about how we collect and parse feedback from all of our supported platforms.  

### Pre-Release Feedback​

Our handling of player feedback for *Khans of the Steppe* started quite a while back, before the announcement of Chapter 4 in fact. Our [preview dev diary back in February](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-162-steppe-by-steppe.1728107/) was published so far ahead of the normal schedule specifically so that we could gather information about player desires and expectations regarding a Nomad-focused DLC. The feedback we received from that DD is directly responsible for a variety of changes that made it into the release version of Khans of the Steppe, such as expanding the new Nomadic government type to certain non-steppe regions.  

Additionally, we run a persistent closed beta program of roughly 100 people from our community. This includes members of various high-profile mod teams, historians, members of the community with a history of sending detailed and actionable feedback, and a small pile of content creators. The point of this program is to get direct player feedback on upcoming content as early into the development process of an update as we can (For Khans of the Steppe, this began roughly a year ago). As development progresses, more of the design is solidified and becomes more difficult to change in response to feedback, so this program is considered vital to us.  

Once the development version has progressed far enough that we’re able to announce it publicly, we begin a fresh dev diary cycle. These serve to inform the playerbase of what we’re working on while giving us a chance to get broader opinions and suggestions about the upcoming content. Our companion videos that are released on our YouTube channel are also helpful here, since viewer retention stats can inform us which sections within a given dev diary are of particular interest to viewers.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1295684/image_04.png "image_04.png")


*[Retention graph for Dev Diary 166; the bump at the 11 minute mark shows that viewers were particularly interested in the “Blessings of the Blue Sky” segment]*  

Finally, in the last month or so before releasing Khans of the Steppe, we ran a separate preview group to get a final round of feedback. This is essentially a time-limited version of our persistent beta, and has a similar selection criteria for participation. During this stage, we essentially throw the flood gates open and pull in as many people as we think we can manage while maintaining some semblance of operational security. Mod team representation increases dramatically during this stage in order to give them a head start on compatibility patching their mods, and any content creator too slow to outrun our Influencer Relations Manager is also pulled into this time-limited program. Before you ask: Yes, that youtuber you’re thinking of is in this program. Yes, that one is too. Yes, them as well.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1295685/image_05.png "image_05.png")


*[A snippet from the aforementioned preview group. Yes, we run this through Discord.]*  

The goal here is to make sure that the content we’re working on matches the expectations of our players as closely as possible ahead of release; the persistent beta program allows us to do this in broader strokes while the DLC is still taking shape, and the preview program allows us to catch more issues that would have slipped through the net (as well as giving us a head start on our first post-release support update).  

### Post-Release Feedback​

That’s all well and good, but what do we do about feedback *after* something is released?  

After a major release, gathering immediate feedback from players is crucial to ensure that any critical issues that made it through testing phases are swiftly handled, and that our post-release support cycle is focused on addressing player pain points with the new content. We actively collect this feedback from a wide variety of places; our own forums, Facebook, Steam, YouTube, Twitter, Reddit, Discord, QQ Guild, Bilibili, Tieba, among others. Essentially, if it’s posted on a publicly visible platform, odds are that we’re going to see it one way or another.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1295686/image_06.png "image_06.png")


*[The pc-feedback channel on our official Discord server is one of several “primary” feedback channels we use. Voting systems make it easier to tell at a glance which posts are more important to the community there. Sadly, Reddit votes aren’t as useful for this purpose.]*  

To facilitate the collection of this amount of information, we have a set of Community Ambassadors (or “CAs”) who act as additional support for the bridge between our players and the development team.  

One of the main responsibilities of our CAs revolves around collecting player sentiment and feedback, monitoring discussions, and identifying pressing issues that players report post-release. You’ve said it? They’ve probably read it. They help cast the net as far as possible to ensure no significant feedback slips through. After a major release drops, they immediately begin scouring for reactions then compile them into a detailed Day 1 post-release report for the studio.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1295687/image_07.png "image_07.png")


*[A snippet from the Day 1 report for Khans of the Steppe. These initial reports are crucial for identifying standout issues that need to be handled as soon as possible]*  

They condense hundreds of discussion threads, suggestions, and reports into a more digestible format to quickly identify what the community finds most pressing. As you can see above, crashing was the most prevalent issue highlighted in the Day 1 report, while balance issues weren’t widely reported until after the Day 1 report period.  

Feedback gathered this way is used to determine what the priorities of the development team should be during the post-release cycle, which finally brings us to the namesake of this dev diary…  

### Post-Release Support​

Our studio is structured into various internal teams, with each one focusing on specific updates or expansions. We have a team for *Khans of the Steppe*, *All Under Heaven*, *Coronations*, and others we can’t discuss quite yet. Post-Release Support (PRS) is the final stage of development for a Major Update before the team assigned to that update is dissolved and its members moved to other teams within the studio.  

The main objective of the PRS stage is to address any outstanding issue that may have slipped through the pre-development cycle. This includes fixing bugs, tweaking gameplay balances, and implementing various improvements or alterations to systems based on player feedback. The goal is to essentially “finalize” the DLC, but this doesn’t mean we cease work on the DLC outright. Any further updates or fixes that aren’t able to be implemented during the PRS stage go towards Realm Maintenance to be integrated into future updates rather than having their own dedicated release.  

During a PRS stage, we step up our Quality Assurance (QA) efforts by bringing in additional specialists to assist with PRS. These specialists work closely with the development team to review bug reports and ensure that as many reported issues as possible are investigated, identified, and assigned to a member of the development team to be addressed. If you’re reporting bugs on our official forums during a PRS stage, these are the people replying to and tagging your posts.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1295688/image_08.png "image_08.png")


*[As an aside, the tags are there to signal to other members of the team that a post has been looked at; this reduces the chances of us wasting time by going over threads that are already being handled.]*  

Another important aspect of the PRS stage is taking care of issues that were “locked out” of the initial release for one reason or another. Two of the main reasons this could happen are *feature freeze* and *loc freeze*. During feature freeze, no new mechanics can be added to a DLC; anything that needs to be tacked on after feature freeze must target a future update. Similarly, a loc freeze means that no new player-facing text can be added, as localization into all of our supported languages takes a significant amount of time; any content that requires new or updated text after localization freeze must be scheduled for a future update. While these freezes mean that our response to feedback can sometimes be delayed, they ultimately help ensure that updates actually release when they’re intended to.  

In most cases, the aforementioned future update will be one of the “point releases” during PRS. Each PRS stage typically has time allocated for two or three of these updates, with the expectation that we’ll need them to tackle issues that cropped up after feature/loc freeze or issues reported by the community. Additionally, we allocate time for hotfixes as necessary to allow emergency updates.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1295689/image_09.png "image_09.png")


*[It’s a bit messy to look at, but you can see here how certain commits by the development team are sent to different branches depending on their contents. We have a lot of internal development branches.]*  

Post-Release Support is an essential part of the development cycle in that it allows us to address player feedback as it’s submitted to us, but also to set the stage for future development by giving us a stronger idea of what players expect and want from the game.  

### Next Steps​

So, what has the feedback we’ve gotten since *Khans of the Steppe* been about, and what do players want from the game?  

Mainly, that the balancing is wonky and that our more dedicated players want the game to be harder. We’ve released Update 1.16.1 and 1.16.2 already to tackle the former, and I’ve been working directly with our Game Director to implement something to help us address the latter; this will take the form of **Hard** and **Very Hard** difficulty modes releasing alongside Update 1.16.2.1 sometime later this week.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1295690/image_10.png "image_10.png")


*[Highly experimental! Mostly untested! Probably imbalanced! Try it out later this week and tell us what you think.]*  

As we’ve said in the past, we want difficulty and challenge to be something that arise organically from how our mechanics interact, and think that giving flat buffs to the AI or penalties to the player for arbitrary reasons isn’t an ideal solution. That said, our community has made it clear that we’re not meeting our objective, and doing something is better than doing nothing. So while we intend to continue pursuing our goal of emergent challenge in the long term, we’re introducing these new difficulties for players who want the game to be harder *right now*.  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1295691/image_11.png "image_11.png")


*[A small collection of some of the bonuses AI characters will receive in Hard/Very Hard difficulties.]*  

We’ve also heard quite a few people asking for a passive herd decay mechanic. To go ahead and rip the bandaid off: We’re not planning on implementing this. Put simply, the system wasn’t designed with this in mind and is instead built around discrete reductions. Too much of the game goes off the rails when it tries to deduct what doesn’t exist, and herd decay ultimately impacts AI rulers far more than it impacts players (compounding balance/difficulty concerns). With the PRS stage for *Khans of the Steppe* coming to an end, we don’t have the time or resources available to rework a core aspect of the DLC to this degree. Additional adjustments to this system are still possible in Realm Maintenance updates, but these are unlikely to fundamentally rework the system itself.  

Aside from that, we’ve heard we still have bugs to squash! AI asking you for paizas should be significantly reduced in the next update, the steppe region map mode should be properly colored in again, etc etc etc. We’ll have a full changelog of what’s been fixed releasing alongside the update itself later this week.  

After that, we’ll have a period of relative stability where mod authors can update their mods and players can finish a longer campaign without worrying about another update dropping and causing them grief. We’ll still be working on bugs and other issues that get reported (or already have been), but they’ll be packaged up alongside the release of our next piece of Chapter IV.  

---

While this is far from a comprehensive overview of development cycles, post-release support, or even feedback loops, I hope this gives you a stronger understanding of how these systems work at a glance. I’m always happy to talk at length about damn near anything involving Studio Black (as anyone subjected to one of my rants on our Discord can attest), so if you have any specifics you’d like to know more about then feel free to drop a comment and I’ll answer them as best I can!  

That’s all we have for this week, but be sure to come back next Tuesday; we’ll be talking about the design vision for a small piece of content we’re working on called *All Under Heaven*.

<!-- artifact:reactions:start -->
- 114 Like
- 41 (unlabeled — rendered as base64 data URI)
- 24 (unlabeled — rendered as base64 data URI)
- 13 Love
- 5 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 39 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
