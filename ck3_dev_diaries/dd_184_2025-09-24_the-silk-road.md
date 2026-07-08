---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1860087/"
forum_thread_id: 1860087
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 184
title: "Dev Diary #184 - The Silk Road"
dd_date: 2025-09-24
author_handle: PDX_Chop
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2147
inline_image_count: 16
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1860087'
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
  - type: thread_metadata
    location: raw_lines_152_to_154
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_333_to_337
    action: preserved_and_flagged
    counts:
      Like: 79
      Love: 28
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_345_to_423
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_424_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #184 - The Silk Road

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Chop](https://forum.paradoxplaza.com/forum/members/pdx_chop.1377369/)
- Start date [Sep 24, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-184-the-silk-road.1860087/)
<!-- artifact:thread_metadata:end -->

Hello, Chop here again! Today we’ll be taking a closer look at one of the new Situations coming in All Under Heaven, so load up your camels because we’re exploring the Silk Road!  

---

**The Silk Road**  

Our aim with the Silk Road feature is to represent the movement of ideas and interconnectedness of the East and West. The Silk Road touches on commerce thematically, but it isn’t a trade system, even if it brings wealth and other benefits to participants.  

Though certain routes were more or less prevalent at different times, the famed Silk Road was in fact a myriad of routes that snaked across Asia, with the Hexi Corridor and the Tarim Basin among the best known. These routes carried goods, travelers, and innovations, and many adjacent regions benefitted from this flow indirectly.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1362371/image_01.png "image_01.png")


*[The Silk Road Situation and its associated map mode]*  

In *All Under Heaven*, the Silk Road Situation is split into six Regions: China, Central Asia, Tibet, Transcaspia, India, and the Occident. Each Region has a Phase, a Hub that serves as its regional center, and an active Silk Road Innovation. Let’s explore each of these in turn.  


**Phases**  
Regions within the Silk Road Situation fluctuate between three separate Phases: Exceptional Bounty, Steady Trading, and Hardship. As with the Great Steppe Situation, the Phase of each Region within the Silk Road Situation is tracked separately, with different passive effects for all Participants and counties in the region determined by the Phase. The active Phase determines the benefits received by Participants in the Situation, as well as the passive modifiers which apply to the regions as a whole.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1362372/image_02.png "image_02.png")


*[Steady Trading Phase modifiers for Lands Under Heaven Participants]*  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1362373/image_03.png "image_03.png")


*[Hardship Phase modifiers for Silk Road Domains Participants]*  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1362374/image_04.png "image_04.png")


*[Exceptional Bounty modifiers for Silk Road Realms Participants]*  

So, how do Phases change? As with some other Situations, actions and events can trigger Catalysts that push the Situation towards a new active Phase. Unique to the Silk Road Situation however, is that these Catalysts are applied to each Region separately. One region may be enjoying a boom even while another is hampered by constant war.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1362375/image_05.png "image_05.png")


*[An image of negative Silk Road Region Phase Catalysts]*  

Catalysts can be local, or wider-reaching. Because the Silk Road generally flows westward, upstream events (especially those in China) can impact regions downstream. A local conflict may be directly damaging to the Occident, but the collapse of the ruling Chinese dynasty will also be felt there indirectly.  

The Dynastic Cycle is a key driver of prosperity along the Silk Road: as long as it remains in a Stable phase, the prosperity of all regions will grow towards Exceptional Bounty. For this reason, the status of the Cycle is always shown at the bottom of the Silk Road window. In short, the benefits felt by those further west depends on the stability of all regions further east.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1362376/image_06.png "image_06.png")


*[The Silk Road routes around the Hub of Lahur in the India Region, and its active Silk Road Innovation]*  

The routes of the Silk Road in-game are marked by red arrows within the Situation map mode. These aren’t just for show; hostile acts such as raids along these routes reduce the affected region’s prosperity. This map mode also shows the Region’s active Innovation, as well as the progress towards its next movement.  

So, what are these Silk Road Innovations?  

### Silk Road Innovations​

Silk Road Innovations are a new set of Innovations that exist alongside the existing base sets.. Each represents a different technology that was discovered in China earlier than elsewhere in the world and can be spread to other Cultures, usually via the Silk Road.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1362377/image_07.png "image_07.png")


*[The Fire Medicine Silk Road Innovation]*  

Although there are six Regions, only four Innovations are active at any time: China holds one, Tibet shares one with Central Asia, India shares one with Transcaspia, and Europe holds one. Every twelve years, each Region passes its active Innovation one step downstream. China then adopts a new active Silk Road Innovation at random from its pool of valid Innovations. As the Han Culture unlocks more advanced Silk Road Innovations, they are added to the pool that can be selected from by China.  

Cultures can gain access to these Innovations by:  


- Having Chinese Heritage
- Having a Ruler of that Culture hold a Hub while the Innovation is active in the Region
- Having the Sinophilic Tradition
- Using the Visit Silk Road Bazaar decision to visit a Hub

Chinese and Sinophilic cultures always have access to Han’s known Silk Road Innovations, without needing to participate in the Silk Road directly.  

That’s all well and good, but what *is* a Hub and how do you visit one?  

### Hub Buildings​

Each Region has a single Hub Special Building in a fixed location that represents a key regional center of trade, such as the Khrom of Lhasa in Tibet or Bazaar of Lahur in India. These hubs provide income and Phase-based regional benefits, and can be upgraded to a second tier to grant additional benefits to their holder. Building or upgrading a Hub also triggers a Catalyst that pushes the Region toward greater prosperity.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1362378/image_08.png "image_08.png")


*[The Marketplace of Chang’an Hub Special Building]*  

Hubs serve as sources of Innovations for their holders’ Cultures and as destinations for a new Decision: *Visit a Silk Road Market*.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1362379/image_09.png "image_09.png")


*[The Visit a Silk Road Market decision]*  

Every ten years, this decision allows you to spend gold to travel to a Hub where a Silk Road Innovation is active. By passing a Learning and Stewardship skill check, you bring this Innovation back and add it to your Culture’s pool of possible Innovations to research.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1362381/image_10.png "image_10.png")


*[The Visit a Silk Road Market decision event]*  

Alternatively, events representing economic opportunities can be encountered during the journey, allowing you to offset the cost of the journey and possibly even turn a profit in the process.  

Well, that about wraps up the Silk Road!  

---

**Innovations Rework**  
*(CM's note: Ellie originally wrote this section in comic sans. As this font is not available on our forums, I have chosen a similarly unpleasant font to use in its place.)*  

Hello everyone, my name is Ellie! The reason you haven’t seen me here before is because I accidentally got sucked into the Lost Realms for a couple of centuries. A word of advice: If you ever find yourself in the Swedish wilderness, do **not** approach any fairy circles, cairns, or haunted caverns, especially if they’re near a stranger that could reasonably be described as “mysterious.”  

The upside to my exile is that a wise gnome offered to mentor me in the legendary art of User Experience (UX)! Now that I'm back at the office, I intend to use that gnomish wisdom to make Crusader Kings III as good as possible. If you’ve played the short tutorial that we introduced a while back, then you’re already familiar with my work!  

(p.s. please forgive my writing, I know I use too many exclamation points in it (the tutorial) (and also in this section)).  

Anyway, as I was saying, I intend to carry on my mentor’s legacy. How? By fixing the parts that confuse first-time players.  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1362382/image_11.png "image_11.png")


*[The current Innovations panel]*  

This panel is fine in parts, but it does have several things we don’t like about it: The visual states are pretty unclear, it’s hard to tell what our current cultural Fascination is, which Innovations are already known isn’t immediately apparent, and so on. Experienced players can manage it well enough, but imagine for a moment that this is your very first time seeing this panel.  

That is raw, unfiltered User Experience. Our mission is to make it *good*. We want you to have a good time clicking buttons and seeing numbers change. We want the game and all of our different panels and buttons to make sense. They should feel cool, intuitive, and understandable while communicating their information effectively to the player.  

Are we always successful in this? Well, no. I can only hope to one day be as talented as my gnomish mentor from the Lost Realms. Either way, for the Innovations panel specifically, there are issues. Since we’re already working on the Silk Road, we decided this was a good time to give this panel some extra attention. Here’s what we’ve done to increase the user experience value of this panel in *All Under Heaven*:  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1362383/image_12.png "image_12.png")


*[The new-and-improved Innovations panel]*  

The Innovations panel now states four things at a glance: your current Fascination, your Culture’s active Spread target and remaining time, the next predicted Spread, and a per-Innovation status label that provides a clear visual distinction between each Innovation’s current status. The changes surface the interface states that were previously easy to miss.  

Quite a bit has changed here, but here comes the hardest part of a UX designer’s job: How do we know that the result is actually good? How do we know we didn’t just make a bunch of changes that end up making the experience worse? Well… we test it! We put it in front of someone and measure whether the panel performs better than before on the outcomes we care about. There’s always room for more improvement though, so if you have ideas or suggestions for other panels then let us know!  

One of the biggest changes? Innovations have associated skills now! If you have a high Diplomacy skill, then you’ll discover Diplomacy Innovations faster (if you set them as your Fascination, of course). We also renamed Exposure to Spread, and made it a little more visible by placing it next to Fascination at the top of the panel along with the time remaining. We’ve also made it so you can discover Innovations outside of the Era you’re currently in, although progress will be quite slow until your Culture enters the Era that Innovation belongs to.  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1362384/image_13.png "image_13.png")


*[An Era which has not yet been reached in the Innovations panel]*  

When you browse an Era that your Culture hasn’t reached, the panel makes the gate explicit and Innovations from that era show a long ETA when selected as a Fascination, clarifying that research outside of your Era is slow but *possible*.  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1362385/image_14.png "image_14.png")


*[Progress breakdown tooltip]*  

The Progress tooltip breaks down the monthly chance to gain Progress into its individual contributing factors, letting you diagnose why an Innovation’s research rate is fast, slow, or completely stalled.  

Pretty cool stuff!  

Now, let’s show how this works in practice and unlock some new gunpowder units. Our first step will be taking the *Visit a Silk Road Market* Decision that we covered earlier. Once we take the Decision, we actually have to travel all the way over there!  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1362386/image_15.png "image_15.png")


*[Our Travel Route from Florence to Lhasa]*  

It'll take a while, but a few years spent on the road is a small price to pay for gunpowder. Once we arrive, we have to pass the Learning and Stewardship checks mentioned earlier.  

![image_16.png](https://forumcontent.paradoxplaza.com/public/1362387/image_16.png "image_16.png")


*[The Innovations panel with the Fire Medicine Innovation unlocked]*  

Poor Matilda got sick during the journey, but we passed the skill checks and got the brand new *Fire Medicine* Innovation added to the pool of Innovations available to our Culture! Now we can select the newly unlocked Innovation as our Fascination, eventually completing it and unlocking the ability to make some gunpowder units. Can we be trusted with this? Absolutely not. Are we going to do it anyway? Of course.  

Anyway, that’s it for this week! Remember to pet dogs and stay away from wizards who tempt you with promises of eternal youth and limitless power.

<!-- artifact:reactions:start -->
- 79 Like
- 28 Love
- 23 (unlabeled — rendered as base64 data URI)
- 13 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Chop](https://forum.paradoxplaza.com/forum/members/pdx_chop.1377369/)**
Role: CK3 Game Designer
Badges: 1
Messages: 54
Reaction score: 2,021

*[Full game-badge icon list of 18 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
