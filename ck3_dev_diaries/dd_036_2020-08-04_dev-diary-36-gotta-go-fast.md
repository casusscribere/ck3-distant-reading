---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1408620/"
forum_thread_id: 1408620
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 36
title: "CK3 Dev Diary #36 - Gotta Go Fast"
dd_date: 2020-08-04
author_handle: Meneth
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2846
inline_image_count: 3
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1408620'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1430.jpg?1596544276
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_248_to_251
    action: preserved_and_flagged
    counts:
      Like: 93
      Love: 87
      (unlabeled — rendered as base64 data URI): 7
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_259_to_369
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_370_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1430.jpg?1596544276)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #36 - Gotta Go Fast

<!-- artifact:thread_metadata:start -->
- Thread starter [Meneth](https://forum.paradoxplaza.com/forum/members/meneth.265499/)
- Start date [Aug 4, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-36-gotta-go-fast.1408620/)
<!-- artifact:thread_metadata:end -->

Good afternoon everyone,  

I’m Magne “Meneth” Skjæran, one of the programmers on Crusader Kings 3. You might know me from my work on CK2 and the Paradox Wikis. Of particular relevance today is my work on performance and AI in CK2. Today I’m going to talk about how we’ve worked with these two areas in CK3 to ensure a better game experience than CK2.  

**Performance**  
Let's start off by talking about performance.  
Over the course of CK2’s lifecycle we made numerous improvements to performance, and when Holy Fury released it was the best it has ever been. The release version today feels like molasses compared to how the game performs after its long and venerated life.  
CK2 has been a standout amongst PDS’ games when it comes to performance, which means we have a lot we have to live up to. As such performance has been a priority throughout the development of CK3, and especially as it has neared release. Our approach to a number of tech systems differ from CK2 for the sake of performance, and this has given us some great results.  

The two systems that differ the most from CK2 for the sake of performance are threading and rendering. The two are heavily intertwined, so much so that you can’t really talk about one without talking about the other.  
In CK2 our approach was pretty simple. The game as a whole was structured around the main thread. The main task of the main thread was to update the gamestate so the game progresses. In order to render frames so the users can see what’s going on, it would periodically stop updating the gamestate in order to make a frame instead. The rendering would then take over entirely until done with the frame.  
During gamestate updates it would thread a large number of different operations. The way we structured this in CK2 was largely based around the characters themselves. The daily update for characters were split into a handful of segments with different rules for parallelization. For instance, during one part it would be illegal for one character to check any information that belongs to another character. During another, it would be illegal for it to change any information it owns that is visible to other characters. These restrictions meant that these updates could be done in parallel; each thread doing the same section for a different character. In practice it worked reasonably well; CK2 is a heavily parallel game and has had significant speed gains from increased parallelization. Similar setups were applied to other objects too, like titles, plots, etc.  
However, there were also some significant drawbacks. The biggest one being the various rules on what the programmer can and cannot do in each update. Violating one of these rules would generally result in an OOS, breaking the multiplayer experience. Occasionally it could even crash the game. There was also a significant overhead in having to process every character in the game with most checks just resulting in “we have no need to do this part of the update”.  

So in CK3 we replaced this system entirely. We moved from object-level parallelism to system-level parallelism. Now instead of processing several characters at the same time we instead process several different systems. For instance, we might update the scheme system at the same time as the opinion system. This allowed us to simplify the rules of what you can and cannot do massively: now during parallelism the only limitation is that we can’t change any visible information; we must instead store the changes we want to do and then apply them a bit later in series. Simplifying the rules means that fewer bugs are introduced, in particular OOSes. And it tends to be easier to identify what could be parallelized than it was in CK2, resulting in more work being done in parallel than before.  


![pasted image 0.png](https://forumcontent.paradoxplaza.com/public/591665/pasted image 0.png "pasted image 0.png")


[A chart of time spent on most of the parallel updates]  

Furthermore, this works great with CK3’s new approach to rendering. In CK3 rendering is a separate thread rather than done on the main thread. It still needs to synchronize a lot with the main thread, as we can’t be checking an object that’s being changed. So we have a system of locks; when the render thread needs to access the gamestate, the gamestate isn’t allowed to change itself, and when the gamestate is changing itself, the render thread must wait until it can access the gamestate. Similarly to CK2, the gamestate will while updating itself periodically check if the render thread needs access, in which case it’ll hand off control for a short while. But the big difference is that a significant part of the work done on the render thread does not require any access to the gamestate, and can thus be done in parallel with the gamestate update.  
And do you remember the rule I mentioned earlier? The parallel updates to the gamestate aren’t allowed to change visible state, so during these updates it is safe to update the render thread. So overall the section where the render thread might have to wait is pretty small, and it ends up doing most of its work at the same time as the gamestate.  
Now, we do still have some object-level parallelism left, most notably the AI. But the AI in CK3 is set up to never change the gamestate directly, so rendering can continue while the AI figures out what to do.  

Overall these changes have meant that CK3 has better thread utilization than CK2, a more stable framerate, and that it is harder for programmers to make threading mistakes that lead to bugs, OOSes, and crashes.  

For a point of comparison, I did a quick test on my machine comparing CK2 and CK3. I simply let the game run at full speed for a minute, and compared the frame rate and how far the game progressed. Both games got equally far in; starting in September 1066 they both got to April 1069. However, CK3’s frame rate was much higher and more stable than CK2’s. Considering CK3’s far better graphics, these results are exactly what I was hoping for.  

Let's take a look at the difference threading makes. I set up a simple test; I ran the game for 1 minute on my machine at max speed, first with threading fully enabled, then with threading disabled. You can see it for yourself below. Left is with threading, right is without:  


[https://www.youtube.com/embed/bsMcG6aRr24?wmode=opaque](https://www.youtube.com/embed/bsMcG6aRr24?wmode=opaque)

The red line you see in the video is the time between each frame. For 60 FPS it should be at or below the green horizontal line.  
As you see, the difference is staggering. Without threading the framerate is dreadful, and the game progresses far more slowly. With threading the game progressed 958 days, while without it only progressed 546 days. That is, it ran 75% faster with threading, and with a far far better framerate.  
The machine I’m running this on is my home PC, which at the time of recording had an i7 4770K, a GTX 1080, and 16 GB of 2400 MHz RAM, running at the highest graphical settings. The CPU and RAM are both quite old and by this point far outperformed by newer models, though the GPU is still solid. Max speed on this is high enough that I almost never use it in normal play, instead mostly using speed 3 and 4.  

So beyond what has been mentioned, how do we work with performance on CK3? We periodically dedicate time to ensuring that any new performance issues are dealt with, and investigating opportunities for further improvement. This often means increased threading, or reworking systems to be more performant. One of my favorite ways to make the game faster however, is by slightly modifying the design to avoid expensive calculations that the player won’t be affected by. To take one example we update the progress of the player’s council tasks every single day. But for the AI we only do so once a month. The player is unlikely to ever notice the difference, but this way we reduce the cost of these updates to 1/30 of what they otherwise would be. Optimizations like this are all over the place in CK3 (and to some extent in CK2); there are a lot of small shortcuts that can be done that have a huge impact on performance but little or no impact on the player experience.  

**AI**  
Now it is time to talk a bit about the AI as well.  
The person who has been in charge of AI for most of CK3’s development is Niklas “Captain Gars” Strid, but he’s currently on parental leave. For the last year or so I’ve been helping out with the AI, and now in his absence the full responsibility of it has fallen on me.  
Since I didn’t design the AI, this is going to be briefer than it might’ve been if Niklas was here to write it, but I’ll cover some of the basic ideas behind how we’ve handled the AI in CK3.  

Our main goal with the AI has been that it should make the game more fun for the player. This has several aspects to it:  


- It should provide some level of challenge, because steamrolling from the get go isn’t fun
- It should avoid doing things that are frustrating, even if it would make it “smarter”
- It should feel as if it’s a plausible actor within a Medieval world
These goals all have both overlap, and parts where they’re in opposition to one another. For instance, avoiding frustration does result in a slightly less challenging AI, but that’s often a sacrifice that makes sense.  

One of the biggest structural changes in CK3’s AI is how it deals with its military. In CK2, if there were multiple AIs on the same side in a war, they would essentially act independently from one another with some systems for coordination. This usually worked fine, but sometimes it’d lead to a lack of coordination between allies and the AI taking odd decisions.  
In CK3 we’ve designed the system from the ground up to handle multiple AIs on the same side. Instead of each AI commanding their own troops, they assign their troops to a war coordinator that handles all decision making; the individual decision making is just what troops to assign (which kicks in if there’s more than one war they could participate in).  
As such AIs tend to act in a much more coordinated manner.  
However, that doesn’t address coordination with the player. CK2’s approach here in the end was to introduce an AI order system where you’d simply tell the AI what to do. We don’t currently have that in CK3, but the AI still has a focus on assisting the player. Generally speaking the AI will try to keep its armies very close to the player, and help out in battles even if those battles will be lost with its help. An AI order system like in CK2 might still improve this further, but the gap is much smaller than in CK2 so we decided it would not be a priority for release. Additionally, the existence of the order system in CK2 significantly complicated the AI code, making further development of it more difficult, so there’s a tradeoff to be considered when it comes to the # of bugs it’ll introduce, and the slowdown to AI development it would be likely to cause.  

So that covered “provide some level of challenge”, but what about avoiding frustration? There’s a lot of small things here and there designed to do that, but let’s talk about a couple of concrete examples. In CK3 the AI has a system I tend to call “stand and fight”. If the player (or any other enemy) is near its army, will beat it, and there’s no real hope of winning the war as all its troops are already gathered, then instead of running away the AI will find a nearby defensive location and wait there for up to a month for the enemy to wipe it out. This way instead of dragging its demise out it makes a last stand in a good location. The result is that the player doesn’t have to chase down armies nearly as much as in CK2, but that it only tends to kick in for wars the player is clearly going to win regardless.  
Similarly, often the game design itself is created with the AI at least partially in mind. We’ve talked about the fort mechanics earlier, but the quick recap is that walking deep into enemy territory without sieging first is going to kill most of your troops. The AI will thus virtually never do it, so when you’re behind your own lines you have the time to regroup and figure out what to do. Similarly, there’s little temptation to try to chase down the AI deep into its territory. This helps keep the focus more on siege warfare, which is very fitting for the era.  
It contributes to every goal I’ve mentioned: The AI ends up better due to there being fewer options available, so we could make it smarter in picking between those. The player gets less frustrated. And it emphasises a historical aspect of the era, while avoiding silly chases halfway around the world.  

Now, that’s been a whole lot of talk about military AI. What about the rest of it? The overall approach there’s generally pretty similar to CK2, though rebuilt from scratch. The AI will periodically check a variety of possible actions, and take them if they make sense. There’s some randomization, and AI personality affects a variety of actions, to ensure that the game feels alive rather than deterministic.  
More of the AI can be modded than in CK2, as the interaction system has far less hardcoding. There’s still parts that are hardcoded, such as actions that aren’t interactions, but overall it should be possible to influence a bit more of the AI than in CK2.  
Reduced hardcoding has also meant that balancing the AI is easier for us than in CK2, as a programmer doesn’t always have to be involved. Especially once we get feedback from a large player base after release, this and various architectural improvements in the code compared to CK2 should make iterating on the AI easier than before.  
Huge parts of what other characters do is also handled by events and so on to a greater extent than in CK2.  

Generally speaking, the goal of the non-military AI is to make the world feel alive. This has occasionally meant needing some restrictions to ensure the player doesn’t get overwhelmed. For instance, we’ve had to on numerous occasions restrict seduction against the player so that they don’t get absolutely spammed if they happen to play one of the few female rulers around at game start.  

Overall the AI should in many ways feel similar to in CK2, but with more of a focus on making the best possible experience for the player. After release it should be easier for us to further improve on the AI than it was in CK2.  **PC Upgrade**  


![20200727_221955 (1).jpg](https://forumcontent.paradoxplaza.com/public/591667/20200727_221955 (1).jpg "20200727_221955 (1).jpg")


[My newly upgraded PC]  
Funnily enough, between when I first wrote this dev diary and when it was set to go out, I decided that it was finally time to upgrade my PC. I replaced my aging i7 4770K with a nice modern Ryzen 9 3900X, and my 16 GB of 2400 MHz RAM with 32 GB of 3600 MHz RAM.  
So I re-recorded my 1 minute test with full threading, which you can see here:  


[https://www.youtube.com/embed/w68n9w-l9Xo?wmode=opaque](https://www.youtube.com/embed/w68n9w-l9Xo?wmode=opaque)


As you can see, this runs the game at a level I can only describe as unplayably fast. In a minute it progressed 1498 days, 56% further than my old CPU. The framerate is also more stable than before, so I’m quite happy with the results.  

![pasted image 0 (1).png](https://forumcontent.paradoxplaza.com/public/591666/pasted image 0 (1).png "pasted image 0 (1).png")


[My new machine running the game at 1000 FPS. Only while paused in one particular corner of the map though]  

That’s all for today, folks!  
Next week we’ll be back to talk more about modding.

<!-- artifact:reactions:start -->
- 93 Like
- 87 Love
- 22 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Meneth](https://forum.paradoxplaza.com/forum/members/meneth.265499/)**
Role: Crusader Kings 3 Programmer
Badges: 153
Reaction score: 5,413

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
