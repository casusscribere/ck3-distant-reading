---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1861437/"
forum_thread_id: 1861437
content_type: reply_thread
parent_dd_file: dd_187_2025-10-02_performance-optimization.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 187
title: "Dev Diary #187 - Performance & Optimization"
dd_date: 2025-10-15
expansion: All Under Heaven
patch: null
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 8
reply_count: 154
participant_count: 77
reply_date_first: 2025-10-15
reply_date_last: 2025-10-30
body_word_count: 12461
inline_image_count: 0
quoted_span_count: 105
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Dev Diary #187 - Performance & Optimization

*154 replies from 77 participants across 8 pages*

## Reply 1 — participant_001 · 2025-10-15 · post-30801634

Quick note: Ignore the posting time on this one. We created placeholder threads for a few dev diaries to give internal scheduling tools a URL to target.

## Reply 2 — participant_002 · 2025-10-15 · post-30801952

TLDR: Claiming mandate of heaven on a potato should be possible. PS: This is is a joke, potatoes already struggle with Doom. ;-)

## Reply 3 — participant_001 · 2025-10-15 · post-30801966

<!-- artifact:quote:start -->
> PatriotOfEldia said: TLDR: Claiming mandate of heaven on a potato should be possible. Click to expand...
<!-- artifact:quote:end -->
I wouldn't go that far. We have a TL;DR at the top of the dev diary for a reason.

## Reply 4 — participant_003 · 2025-10-15 · post-30801969

Finally less nobody shall be generated!

## Reply 5 — participant_004 · 2025-10-15 · post-30801984

Wow, so early I’m right under a JonZone meme Edit:

## Reply 6 — participant_005 · 2025-10-15 · post-30801988

Given that landless title logic of China was optimized by this DLC, are there any plans to revisit other landless title logic (Byzantine, landless bands, nomads) to further improve the game performance? I think you guys could get more speed improvements to counter balance Future DLC that Will also be CPU intensive ( like trade/republics, feudal rework, Warfare rework).

## Reply 7 — participant_006 · 2025-10-15 · post-30801990

Have these performance improvements made desynchronization less likely during multiplayer sessions? Also, has a resynchronization feature been added?

## Reply 8 — participant_007 · 2025-10-15 · post-30801992

From script pov, in the event that handle murder scheme for AI (murder_scheme_maintenance_events.txt), there is an empty if block in the immediate with this note : Code: immediate = { # The peculiar arrangement with an empty if statement & a separate random_in_list is intentional; they save on performance. Somehow. ## #JustCodeThings. if = { limit = { build_murder_targets_trigger = yes } } Could you explain what this mean ? why setting an empty if block save some performance ?

## Reply 9 — participant_008 · 2025-10-15 · post-30802004

My problem with performance was really only with very large realms, due to too many vassal-liege type checks the lag could be severe during a WC. Especially bad with mongol empire playthrough with all its vassals. I mean if days take several seconds that's fine but it's the stutter/fps even when paused that killed it. Considering WC mongol empire is an achievement in the game and therefore an intended playtrough path, I hope that's better now.

## Reply 10 — participant_009 · 2025-10-15 · post-30802005

983d is best cpu for paradox game

## Reply 11 — participant_010 · 2025-10-15 · post-30802007

<!-- artifact:quote:start -->
> IngvarBS said: Given that landless title logic of China was optimized by this DLC, are there any plans to revisit other landless title logic (Byzantine, landless bands, nomads) to further improve the game performance? I think you guys could get more speed improvements to counter balance Future DLC that Will also be CPU intensive ( like trade/republics, feudal rework, Warfare rework). Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> NE_1217 said: Have these performance improvements made desynchronization less likely during multiplayer sessions? Also, has a resynchronization feature been added? Click to expand...
<!-- artifact:quote:end -->
The performance improvements to landless play should have an effect already across the board since the logic is to some extent shared between the new administrative realms and the Byzantine one. As for your second question - we're continuously looking at performance improvements for the CPU with new expansions. But it's easier to do after the features are added since they may expose new areas where older systems aren't keeping up with the scaling. And in that sense it's easier to fix the real performance killers first after we have a way to discover them. Performance improvements on the opposite actually have a tendency to decrease multiplayer stability. However we've also been working hard with specifically the out-of-synch problems which make hotjoin impossible. And yes I can confirm that Re-sync has been added so hopefully any remaining issues should be less annoying to deal with.

## Reply 12 — participant_011 · 2025-10-15 · post-30802014

S Tier dev diary right here. One thing I am a huge admirer of PDX for is being open and not treating the audience like idiots (even if that may be true in my case). Fantastic read and thanks for taking the time to run through it in so much detail, greatly appreciated.

## Reply 13 — participant_012 · 2025-10-15 · post-30802021

<!-- artifact:quote:start -->
> So we went and reduced or eliminated a bunch of ‘sources’ of characters that generate boring, useless, random or invisible characters that then linger in guest pools, the sidelines of courts of barons and counts, and that take up space and cost performance. At the same time we keep the more interesting characters that have a bit of history around longer, and we draw them into events more, often replacing a randomly generated nobody Click to expand...
<!-- artifact:quote:end -->
Having events feature characters who already exist in the world instead of randoms who were specifically created for the event is pretty good. That is assuming the characters who are chosen for the events actually fit in the role they're given.

## Reply 14 — participant_013 · 2025-10-15 · post-30802049

I'm really disappointed that the two worst offenders were not on the list of things fixed. 1. Suspension of Diplomatic Range when within the same realm - this is the big bad of the late-game performance. Don't believe me? Load the game, use the console to make everyone your vassal and then see how it affects performance. In the late-game there are fewer independent counts and much more blobs and this is the root cause of the late-game perf drag. Diplomatic range restricts the amount of rulers that are evaluated for interactions. But it doesn't matter if it's the same realm. This is what makes AGOT run so slow, because our mod starts with 900-county megablob, so we're already in the lategame from the very start. 2. Vassal contracts are evaluated every. single. frame. Seriously, whatever you put there in debug-mode is updated instantly. If you put there anything even remotely complicated, any "if" whatsoever, it is evaluated every frame for everyone on the map. This is constantly top1 in the script profiler. I'm surprised that you didn't switched it to daily, or at least every second update. Portraits suffered from similar issue but you switched them to update several times a second. But contracts were left as they were, and they are basically a Dev-trap for unsuspecting modders who put innocent ifs in there. EDIT: upon rereading my post i realized that i might've sounded ungrateful. I'm happy to see the other stuff, especially quick-triggers. Surprised to see some other stuff, like tiered AI evaluation tick (thought this is already handled by is_shown) and all in all this is the thing i'm most excited for AUH. But i was really sure you'll fix the internal diplo range issue.

## Reply 15 — participant_014 · 2025-10-15 · post-30802067

A couple of questions about the CK3 scripting language. Is the scripting language compiled or interpreted, or some hybrid? Would you consider creating detailed documentation describing the entire scripting language? The documentation on the Paradox Wiki is likely incomplete and not always up-to-date (I'd like the documentation to be similar to cppreference)? And speaking of C++, I'd like to see a lower-level modding API, so users could write mods in C++. While this would be more difficult for those unfamiliar with C++ (though easier for me), it would likely provide far more modding options and improve the performance of larger mods.

## Reply 16 — participant_015 · 2025-10-15 · post-30802069

This is fantastic to hear, please continue to try to make the game faster. I think that every time a new DLC is about to be released, a dev should be forced to play the game, with the new dlc installed, from 867 all the way to the end just to see what it's like. Not a playtester, an actual dev! Selected by lottery among the devs that don't have full plates maybe. Regardless, this dev diary fills me with hope that my laptop will still be able to play the game a year from now.

## Reply 17 — participant_016 · 2025-10-15 · post-30802070

<!-- artifact:quote:start -->
> Divine said: Eliminating Stray Nobodies One of the more commonly used mods out there to make the game faster is the “Population Control” mod - which starts eliminating people when the world’s population reaches a certain number. Now we haven’t done something exactly like that, but we have tried to combat the underlying issue: we accumulate characters that don’t do much - and after a couple of hundred years these can count in the tens of thousands. So we went and reduced or eliminated a bunch of ‘sources’ of characters that generate boring, useless, random or invisible characters that then linger in guest pools, the sidelines of courts of barons and counts, and that take up space and cost performance. At the same time we keep the more interesting characters that have a bit of history around longer, and we draw them into events more, often replacing a randomly generated nobody. This allowed us to trim the useless fat that accumulates in long-running games, reducing the strain that even relatively light non-ruler characters leave on the simulation systems. Click to expand...
<!-- artifact:quote:end -->
My jaw dropped on this one. Did you really sneak that in through a performance DD out of all things? People have been asking to STOP generating ppl for events because they're nobodies and you dont care in the slightest about them and there're bazillion wandering characters existing already! And you did it, you bastards! Although i must say, all your script improvements make me want to not update any of my modes for 1.17 because it's no longer a simple diff T_T

## Reply 18 — participant_017 · 2025-10-15 · post-30802076

<!-- artifact:quote:start -->
> darcinc said: A couple of questions about the CK3 scripting language. Is the scripting language compiled or interpreted, or some hybrid? Would you consider creating detailed documentation describing the entire scripting language? The documentation on the Paradox Wiki is likely incomplete and not always up-to-date (I'd like you to use cppreference as a reference)? And speaking of C++, I'd like to see a lower-level modding API, so users could write mods in C++. While this would be more difficult for those unfamiliar with C++ (though easier for me), it would likely provide far more modding options and improve the performance of larger mods. Click to expand...
<!-- artifact:quote:end -->
Script during game load is translated into a tree of callable objects in C++ code. There's no way we let anyone modify C++ game code directly. It's a security nightmare Some script documentation exists in the .info files and when you run "script_docs" console command. That's what we use ourselves internally. It's a compromise between time spent making tools and time spent actually using tools to make a game

## Reply 19 — participant_018 · 2025-10-15 · post-30802079

<!-- artifact:quote:start -->
> Alien-47 said: There's no way we let anyone modify C++ game code directly. It's a security nightmare Click to expand...
<!-- artifact:quote:end -->
Not untrue, though I always wondered how Civ V achieved it...

## Reply 20 — participant_019 · 2025-10-15 · post-30802081

"Feature steward"? Does this mean that there are plans to integrate DLC features together, or to add new features to old systems which were implemented after release?

## Reply 21 — participant_014 · 2025-10-15 · post-30802087

<!-- artifact:quote:start -->
> Alien-47 said: Script during game load is translated into a tree of callable objects in C++ code. There's no way we let anyone modify C++ game code directly. It's a security nightmare Some script documentation exists in the .info files and when you run "script_docs" console command. That's what we use ourselves internally. It's a compromise between time spend making tools and time spent actually using tools to make a game Click to expand...
<!-- artifact:quote:end -->
What if you make a banner during launch, stating that by using "native" mods you understand all the risks and take them on yourself?

## Reply 22 — participant_017 · 2025-10-15 · post-30802088

<!-- artifact:quote:start -->
> kuczaja said: 1. Suspension of Diplomatic Range when within the same realm - this is the big bad of the late-game performance. ... Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> kuczaja said: 2. Vassal contracts are evaluated every. single. frame. Seriously, whatever you put there in debug-mode is updated instantly. If you put there anything even remotely complicated, any "if" whatsoever, it is evaluated every frame for everyone on the map. This is constantly top1 in the script profiler. I'm surprised that you didn't switched it to daily, or at least every second update. Portraits suffered from similar issue but you switched them to update several times a second. But contracts were left as they were, and they are basically a Dev-trap for unsuspecting modders who put innocent ifs in there. Click to expand...
<!-- artifact:quote:end -->
Unfortunately it's part of core game design. Changes to that will mean revisiting every system on the level of how it's supposed to function, instead of just preserve functionality but faster. We have partial mitigations to that where it's most noticeable: interactions limit max number of targets, some script randomly discards recipients people inside big realms Can you elaborate? Only game UI may do things "every frame". Game logic does things daily or on some other intervals. If you can describe an example that I can reproduce on my machine, I'll be happy to take a look. What part of vassal contracts causes such performance issues for you? Is it validity of obligations? Something else? Also, naturally we are optimizing for the content our designers make. Making mods fast is nice, but can't be a priority when we still have to deliver an entire expansion of features.

## Reply 23 — participant_020 · 2025-10-15 · post-30802093

<!-- artifact:quote:start -->
> Benismann said: My jaw dropped on this one. Did you really sneak that in through a performance DD out of all things? People have been asking to STOP generating ppl for events because they're nobodies and you dont care in the slightest about them and there're bazillion wandering characters existing already! And you did it, you bastards! Although i must say, all your script improvements make me want to not update any of my modes for 1.17 because it's no longer a simple diff T_T Click to expand...
<!-- artifact:quote:end -->
I have to note here for the more correct picture - we have reduced them a lot, but they still will pop up with some frequency! Less, not gone.

## Reply 24 — participant_016 · 2025-10-15 · post-30802097

<!-- artifact:quote:start -->
> Divine said: And yes I can confirm that Re-sync has been added so hopefully any remaining issues should be less annoying to deal with. Click to expand...
<!-- artifact:quote:end -->
OMG thank you kind sire.

## Reply 25 — participant_021 · 2025-10-15 · post-30802102

Would also appreciate Native Support for Apple Silicon.

## Reply 26 — participant_010 · 2025-10-15 · post-30802109

<!-- artifact:quote:start -->
> kuczaja said: I'm really disappointed that the two worst offenders were not on the list of things fixed. 1. Suspension of Diplomatic Range when within the same realm - this is the big bad of the late-game performance. Don't believe me? Load the game, use the console to make everyone your vassal and then see how it affects performance. In the late-game there are fewer independent counts and much more blobs and this is the root cause of the late-game perf drag. Diplomatic range restricts the amount of rulers that are evaluated for interactions. But it doesn't matter if it's the same realm. This is what makes AGOT run so slow, because our mod starts with 900-county megablob, so we're already in the lategame from the very start. 2. Vassal contracts are evaluated every. single. frame. Seriously, whatever you put there in debug-mode is updated instantly. If you put there anything even remotely complicated, any "if" whatsoever, it is evaluated every frame for everyone on the map. This is constantly top1 in the script profiler. I'm surprised that you didn't switched it to daily, or at least every second update. Portraits suffered from similar issue but you switched them to update several times a second. But contracts were left as they were, and they are basically a Dev-trap for unsuspecting modders who put innocent ifs in there. EDIT: upon rereading my post i realized that i might've sounded ungrateful. I'm happy to see the other stuff, especially quick-triggers. Surprised to see some other stuff, like tiered AI evaluation tick (thought this is already handled by is_shown) and all in all this is the thing i'm most excited for AUH. But i was really sure you'll fix the internal diplo range issue. Click to expand...
<!-- artifact:quote:end -->
1. For gameplay reasons we unfortunately always need you to have access to actions within your own realm to avoid doom-spiraling large empires in ways outside of the players control when they would no longer be able to manage their empire title setups after inheritances/wars/whatever. I agree that larger realms are something that poses a problem in scaling since whenever we add inter-vassal interactions the complexity grows factorially with the size of the realm unless we find ways to mitigate that somehow. And complexity for liege-to-vassal interactions with additional objects will also grow exponentially. This is not an easy problem to solve but setting max ai evaluation targets is one of the ways that you may find to close the gap here. 2. Hmm it might not have been something we encountered due to having very light logic regarding vassal contracts. If you can hand us a minimal mod then we can take a look at profiling it. Definitely sounds like something we likely can update every 20th frame or something instead of every single frame if your suspicions are the correct diagnosis.

## Reply 27 — participant_016 · 2025-10-15 · post-30802110

Also - did boot times improve at all? Did you see that bugreport about mods slowing game load down dramatically, even empty ones (same for stellaris)?

## Reply 28 — participant_010 · 2025-10-15 · post-30802112

<!-- artifact:quote:start -->
> Musaab said: Would also appreciate Native Support for Apple Silicon. Click to expand...
<!-- artifact:quote:end -->
I can sadly confirm that we didn't manage to get Native Apple Silicon into the initial release of All Under Heaven but we're looking into it.

## Reply 29 — participant_013 · 2025-10-15 · post-30802115

<!-- artifact:quote:start -->
> Alien-47 said: Can you elaborate? Only game UI may do things "every frame". Game logic does things daily or on some other intervals. If you can describe an example that I can reproduce on my machine, I'll be happy to take a look. What part of vassal contracts causes such performance issues for you? Is it validity of obligations? Something else? Click to expand...
<!-- artifact:quote:end -->
The best way to reproduce it would be to put anything more complex than single number inside "levies = " parameter. If you'll put checking for opinion or some special circumstances, the performance drag will happen even if the game is still paused.

## Reply 30 — participant_022 · 2025-10-15 · post-30802116

<!-- artifact:quote:start -->
> Divine said: I’m Joel, and I’m the Technical Lead on the Crusader Kings III team. I’m at the start of my second decade working with Crusader Kings in various roles, having originally started out as a designer for CK2. Before we get into the details of how we’ve worked to achieve better simulation speeds, I’ll hand it over to Daan for a quick summary of our results. Straight-to-the-Point Summary So you want some quick info and conclusions up front? Let me try and summarize it for you! With All Under Heaven included, the game is about 30% to 40% bigger, in the sense of the amount of playable land, and playable living characters. We focused on reducing simulation tick duration to keep the experience as close to CK3 as it is now. Our numbers, measured on both low-spec and high-spec machines, indicate that we have reached tick speeds comparable to the current live version. Comparable means we are slightly slower in the early game, but on-par or slightly faster in the mid to late game, running at speed 5 over 150 to 250 years, starting in 1066. The following graph shows tick duration over 150 years compared to the current release (higher means longer tick duration, therefore slower): View attachment 1380971 [Rough Tick Duration Graph - Red: All Under Heaven, Yellow: Current Version] We also implemented GUI, 3D graphics, and memory-usage improvements, though they were a lower priority than simulation speed. Caveat: Results will vary by the world you create and the world the simulation creates around you! There is no single number or graph that covers all games, hardware, and play styles, but we have aimed to deliver a playable, stable, fast experience with All Under Heaven. That’s the short version. If you want more details, more graphs, and more insights, then please read on! Definitions Now let’s get back to the regular schedule and start digging into the details First, we need to define what we mean when we say speed or performance. Normally, when we talk about performance, we refer to two categories: rendering and simulation. When developing DLCs for Grand Strategy Games, we create more systems and objects to simulate over time. Graphical complexity will also increase with more development, but during DLC development it rarely causes new bottlenecks for us. However, increased simulation demands put more load on the CPU for calculations and data transformations due to new features and systems to keep track of. This makes the CPU our most common bottleneck when it comes to optimizing for simulation tick speed. So our most common task when it comes to optimizing the code for our games is to look at where our CPU-cycles are spent and where we can be more efficient, in order to keep down the average time-per-tick for a playthrough. This makes the time-per-tick measurement the most important metric for us to track throughout development, and the one we will be talking about the most in this Dev Diary. Measuring Performance So how do you get accurate measurements for tick speed when working with a complex simulation? There are many variables in play that will affect the final outcome. Examples of variables that affect results include: graphical settings, hardware, test length, early- or late-game state, background tasks, and random variation. All of these variables matter in analyzing how the game performs, but we also want to stress that most of our performance improvements are going to have a similar effect across the board of different hardware. For that reason, the most valuable test is early-game tick performance on fixed hardware with fixed settings and a fixed random seed. This gives us a test that we can quickly repeat to allow us to track the tick speed trends over time for different versions of the code during development and allows us to quickly spot degradations. With that said, there are some optimizations which don't fully benefit lower-core hardware as much: while the early-game simulation is generally just a throughput issue for the code, the end-game optimization will instead focus on trying to contain the growth in complexity. We do so by ensuring calculations scale well with a larger simulation in later stages of the game, for example with more characters or larger realms. For that reason it’s still important for us to do spot checks on low-spec machines and profiling of endgame saves to avoid focusing only on solutions that require more CPU cores to parallelize computations. Adaptation One saying in software engineering (and many other professions) is that “perfect is the enemy of good.” It’s a sure way to spend ages on a feature if we’re determined from the outset that it has to use the most perfect and streamlined code. This is especially true in game development, where we often start out with one design of a feature to later tweak and modify the feature to better fit with the rest of the game and gameplay feedback for what is a fun player experience. At times you can know from experience where we will have future performance problems and plan for a more thought-through data architecture to mitigate that, but most of the time the most important thing is to get features up and running to verify that they are fun. After that, we can identify which systems are not performing according to our requirements and start improving them from both a coherence and efficiency perspective. The Journey of a Thousand Miles Begins with One Step What I’ve so far described is our usual approaches to performance work for DLC projects. However with All Under Heaven this all gets upended by the scale. Beyond having more individual features than any prior DLC, the biggest challenge for simulation tick speed is the addition of two subcontinents. Both East Asia and Southeast Asia are massive additions to the world that we need to simulate for the game. This was going to be a larger challenge than any previous expansion we had done for CK3. In addition to the typical ~20% slowdowns we would see from unoptimized feature additions, we would now also need to deal with a 32% increase in baronies (and rulers) to the game. In our simulation, rulers are the smallest building block for moving the world forward: this is also linearly correlated with the amount of work the CPU must perform. This means that just by putting the rest of Asia on the map, we have immediately made the game slower by an equal amount of the size increase. In the planning stages for AUH we set aside additional time and resources compared to a normal expansion specifically for looking into how to make the game faster and offset the increased simulation scope. We also knew that we couldn’t just rely on easy wins by keeping new features in line with good practices. This time we had to look even deeper into what old systems we had that were holding us back. With that said, I’ll hand it over to two of our very talented Engineers, Anton and Carl-Henrik, to explain in more depth how we find underperforming components in the codebase and the methods we use to make the game perform according to the principle “gotta go fast.” Hello, I’m Anton, one of the Senior Programmers who has been on the Crusader Kings III team for many, many years. I’m going to talk a bit about how the code is structured and how we measure and think about performance improvements. Focusing on the Most Expensive Systems One approach to performance work is to look at various game systems and what it takes to simulate each system every daily tick. We start with the most expensive system, because optimizing it yields the largest impact compared to how much time we spend on it. Individual systems are also more self-contained and have only a limited number of connections with the rest of the game. It becomes easier to reason about it, and easier to focus on what matters right this moment. Our internal tools help us visualize various game features and compare the performance impact of each one. View attachment 1380972 [Example of a serial update performance graph] Here’s an example: 25 years of game time aggregated, with average time shown for the most expensive parts of the game. 63 different systems update every day; 44 of them take less than 0.3ms each, and can be ignored. For the 19 remaining, we show their names along with the average time and percentage they take each day. Some game systems will always be expensive. During development, different systems may appear with larger or smaller shares of time in the chart. We evaluate how reasonable it is for this or that system to take so much time per day. There were periods when succession or situation systems were at the top of this graph, a clear indication that something excessive was happening and that we needed to investigate it. Situations were updated too frequently when nothing really changed, and succession was running a very expensive script on too many people. As you can see now, both systems are now included in the “other” category and are mostly fine. Characters and modifiers are typically at the top; they are the core of the game and will always take more time than anything else. This is always a difficult question - how much faster can I make something that will always be expensive? Is it worth spending a few more days, or is it good enough and I should look for easier gains elsewhere? Average is not the only important number. This particular graph shows another problem. You can notice light orange columns (activities) sometimes spike disproportionately, making certain months much slower than average. We want both to have a low average time, and no big spikes when something important happens. This is a big advantage of such visualization techniques over just looking at the aggregate numbers. Activities will be a prime suspect for the next optimization. Parallel vs. Sequential Updates The previous graph showed the serial part of the daily tick. The next two graphs show parallel updates. View attachment 1380973 [Parallel AI update] View attachment 1380974 [Parallel pre-update of game systems] It’s very easy to reason about and develop a system with a single-threaded approach. You know things happen in order, things are predictable and repeatable. It makes development faster, and features can be tested and balanced sooner. Usually only after the feature's skeleton is ready and it starts working in the game, it gets connected with the rest of the systems, and after that, we may take another pass and make some of the work go in parallel. These two graphs show parallel work during a daily tick. You can still see total wall-clock time spent on the update every tick; it’s below 20ms for each graph. It’s drawn as a thick red line at the bottom of each graph; notice how much more work gets done in total in parallel. This example is on a PC with about 20 logical cores. Why not do everything in parallel? We need a deterministic order of observable changes in the game for multiplayer to work, so all clients have the same game state as everyone else. Another important part is again the ability to reason about the correctness of the game. Most changes in the game have propagating side effects. A Ruler conquering a new title means that another Ruler is going to lose a title. Loss of a title means changes in income and military power. A Ruler who gets weaker is more endangered by factions and other enemies. During any of those steps additional events may get triggered. A strictly determined order of actions and cascading side effects is necessary to understand and predict game outcomes. Keeping that in mind, we’d like to do as much work in parallel as possible. We have an internal framework that allows us to split parts of the feature into sequential and parallel steps. It was covered a long time ago in pre-release Dev Diary 36. The parallel part goes first and is called “pre-update”. During the pre-update, nothing observable changes in the game. Every parallel thread sees the same visible game state, like it’s frozen. In parallel various systems can do heavy lifting to independently calculate what should be changed during the next sequential step. Everyone calculates new income independently, every AI actor makes decisions independently, heavy logic, triggers, and math that can be done in advance are pre-calculated. All this is done to minimize the final amount of sequential changes - apply already known values instead of doing math, execute the final decision instead of making a whole decision-making process etc. Even during sequential updates, we still want to utilize more than one thread. And this part is extra risky and complex. If I can prove that certain modifications can be done irrespective of the order of operations, or if some actions guarantee to have only limited side effects, then it’s safe to do parallel work there. One more important note here: only a small fraction of the game is updated each day. Our updates are separated into daily, monthly, and yearly updates. Only very few crucial systems need to be updated every day. AI movement of units is one such case. Most systems are updated only once a month. It’s a compromise between frequency and efficiency. Every day only 1/30th of all people, all construction, all epidemics etc are updated. This spreads expensive updates equally over the entire duration of the game. Obvious drawback compared to older games - you never know for sure when it happens to you, the player. You don’t know the date when you get your personal monthly income, it just happens every 30 days. Applying Optimization to Specific Systems Let’s talk about more specific changes to the game - how it all applies to individual game systems. One example mentioned earlier was an expensive succession update. All Under Heaven introduces China, an enormous realm with unique succession mechanics; lots of people compete for counties, duchies, and kingdoms, and candidates are appointed according to their merit rank and score based on various properties of a person, their family, and events in their life. At some point it was the most expensive system to update daily, even when you take into account that we update succession very rarely, compared to other systems. That’s how expensive it was. Many individually reasonable decisions led to this outcome: China has lots of titles to appoint, and the design was to allow almost everyone to be a candidate for any county in the entirety of China. This is a quadratic problem that quickly grows out of control. What worked somewhat okay for big Byzantium, although already too slow, was no longer suitable for China. The first attempt was to change the order of operations: can we eliminate as many unsuitable candidates as quickly as possible, so we don’t have to run expensive logic and math on scoring? It’s much cheaper to find the best out of 100 than out of 4,000 people. Another obvious omission was a sequential scoring; doing appointment score math is an immutable operation, and can be safely done in parallel on all people at once rather than one at a time. This alone made it three times faster, but it was still not good enough. It remained the third-most-expensive system. The third step was to go and talk with our designers about their intent. Do we really care if every courtier in China can be a valid candidate for any county? Surely we can find some compromise. It’s important that any landless ruler has this chance. Every member of a proper noble family should be given a chance to serve the realm. But what about the lowborn? Can we somehow limit their participation to only titles where they personally live? This design step halves the number of candidates, yielding large performance gains while maintaining the same player experience. Players can still see important people all around the realm taking jobs and the system still feels competitive and alive, while taking even less time. It’s always important to keep in mind what we want to achieve with any game system: what matters to the player and what goals designers have. The fourth step was less impactful, but still valuable. After the previous 3 steps most of the succession update was spent doing scripted scoring math. I was lucky to get suspicious there and look deeper. It was just a single line of script that calculated holding income. One very old trigger was always fast enough, but with the introduction of governor efficiency for administrative realms, holding income is now affected by governor efficiency, which made it slower due to incorrect caching. What was supposed to be just a simple return of a precalculated value turned into a whole sequence of very expensive math on demand. With the change that made cached income always valid and available, succession became so fast that it disappeared from the graph and was included in the “other”. Also, any other script that was using holding income became faster overall. Lessons from System-Level Optimizations One more way to make the game faster is to do things less frequently or not do it at all. Turns out, AI for barons was trying to do lots of things that made little sense. Barons don’t have councils or court positions, yet they were still evaluating all of them; they no longer do that now. if it takes about three years to build a building when you have only a single holding, then they should only attempt new construction every three years; Barons now only attempt to start a construction every three years. Lots of game decisions and interactions can never be attempted by barons as they will fail various triggers, but what if we don’t have to run those triggers in the first place? A sweeping review of availability by ruler tier for those mechanics freed even more time, aaaand in the end the result was not that impressive. Overall 0.5-1ms of total daily tick time, which can be overshadowed by random fluctuations in hardware or the current game state. The main cause for it - proper rulers spend so much time doing heavy tasks, that optimizing barons was barely worth it. All AI decision-making already runs in parallel as well, so any performance gains end up being spread over multiple cores and are less noticeable as a result. That’s it from me. Thanks for letting me share my thoughts on performance. I’ll now hand over to Carl-Henrik who has also done a lot of performance work during the development of AUH. The Full Picture Dear Daily Tick Enthusiasts: I am Carl-Henrik, Principal Programmer on the team, and I have mostly been working on improving the performance and memory usage of Crusader Kings III! My personal hobby involves sizecoding on 8-bit and 16-bit CPUs in assembler, so working with performance is close to my heart. I even won a couple of size/performance coding competitions! I am also fairly new here, so I rely a lot on people around me including Daan, Joel, Jimmy, and Anton, as well as the design team and team partners! (I do cast a long shadow, however, as the mentor of Johan Andersson prior to his time at Paradox) Generally I have found that the code that I optimize works well, but we have since it was written introduced a large number of titles and characters. This means that the assumptions made at the time don’t hold up any longer and this is the opportunity to improve performance. No code has changed because it was in any way inferior. Loading My initial focus was on the game's load screen. As my personal computer at home falls below the minimum specifications for CK3, addressing this would significantly improve my ability to play the game. I was unprepared for the sheer volume of activity, and the only available performance measurement was debug logging, which was intertwined with all other processes occurring during this game phase. To better analyze load time, I made a new performance-tracking tool that can keep track of the whole sequence, shown in the image below. The graphs show what each CPU is busy loading or setting up and the black portions don’t necessarily indicate that a CPU was idle, they may have been too quick to show or not included in the loading functions. View attachment 1380975 [The streaming profiler tool, my current PDT (“Personal Development Time”) project] While we identified numerous areas for improvement, implementing those changes proved too extensive at the time. I aim to begin enhancing these systems soon. Memory Right around the release of Khans of the Steppe, we needed to save some RAM. The minimum spec computer was having trouble running the game and this had previously been researched by our console porting team. Bringing the entirety of Crusader Kings III to modern platforms is an impressive feat, and having access to their work meant we could make these memory improvements fast. One particular improvement was the memory usage for tooltips in the game, which was surprising. Bringing this one change to the PC version saved several gigabytes! We also looked at memory savings from the updated GUI code in Clausewitz, but those turned out to be too different to use for All Under Heaven. Performance With the memory improvements in place we also needed to look at code performance. Early measurements showed as much as one and a half times the performance degradation from our earlier DLC Khans of the Steppe. My approach prioritizes code improvements, while other team members, who specialize in design, focus on elements like scripts and character action frequency within the game. View attachment 1380976 [A performance sample over 100 years from a work computer (32 cores)] To monitor optimization progress and identify development-related issues, I run the performance analyzer daily for 100 years. This is done on both my high-spec computer (32 processors, 64 GB RAM, Windows 11) and a lower-spec machine (8 cores, 16 GB RAM). View attachment 1380977 [A performance sample over 100 years from a low spec (8 cores) test computer] From the graphs we can investigate any of a multitude of systems for performance issues. Once a system has been identified and the relevant (slow) code tracked down, we can start making improvements. Most of the time I find things updating other things that don’t all need to be updated. For example, in the performance graph for Pre Update, Script Variables was one of the top users. In Saved Variables/Script Variables we narrowed the check for variables that need to be updated, as they can time out, so instead of checking around 500,000 variables only a few hundred need to be tested for each tick. This change made the category disappear entirely from the graph! Rendering Graphics tend to be one of the largest performance categories for games, but even with the latest map updates Crusader Kings III is not significantly impacted in this area. To improve graphics performance, we introduced Adaptive Framerate. This new setting benefits computers with fewer than 10 processors by subtly lowering the rendering frame rate when there is minimal screen activity. It should be enabled with the low-quality graphics preset. Adaptive Frame Rate works together with the Maximum FPS setting, which has a new default option called “Display refresh rate”. Previously disabling VSync and leaving the max FPS off led to a significant decrease in performance due to the frame rate being uncapped by default. For optimal performance with minimal rendering impact, enable Adaptive Frame Rate and set the Maximum FPS to 30. The updated map and other improvements have increased the detail for the GPU to process. This may lead to longer frame processing times and a lower screen-update rate, potentially making the interface feel less responsive. While this does not affect the daily tick rate as the CPU and GPU work in parallel, we plan to investigate ways to better balance this workload. This optimization has not yet been prioritized alongside other planned improvements. Complexity Many optimizations are straightforward and easy to reason about, but sometimes you find something small and innocent looking that can drag you deep into a rabbit hole. There is a function that does a few checks and runs a script (if the checks are fine). This is about 30 lines of code but contained enough performance issues that the improvement took over 2 weeks. The slowest line of code was a call to IsScopeOK that basically just checks that the script scope (parameter) matches what the Trigger or Effect is expecting. Making some trivial improvements yielded no results which simply indicates that the compiler automatically did that work for us. Even though the function is not inherently slow, the sheer volume of scripts executed per tick makes this the most resource-intensive aspect of the entire game. The actual problem with this line turned out to be that to check the scope each Trigger generated a 128 bit flag field and compared that with a 128 bit flag field generated from the scope. Replacing this with simply comparing the numbers of the scopes greatly improved performance. Unfortunately Triggers and Effects can accept multiple kinds of scopes so ultimately if the initial check fails the bit flag test is necessary as a fallback but it is already a great improvement. In most cases Trigger and Effects return the scope number but there is also a concept of Links that only return the scope bit flags. I ended up spending two days going through all these classes and adding the missing functions. View attachment 1380978 [IsScopeOk code block rewrite that puts the less expensive checks at the top] The Trigger/Effect also seemed to suffer from cache misses and adding a cache prefetch helps a bit more. But this was just one line of the function. We have an in-game script profiler that we use extensively trying to improve performance of scripts. This should only have a performance cost when it is used so it required a bit more investigation. We need to remember the filename and the line of the file for the script and this particular data type had an inefficient implementation to store that information, so that helped quite a bit. However, this efficiency is still redundant when not in use. Therefore, employing an in-place new instead of the default constructor made this line acceptable. While time-consuming, each step of experimentation, testing, and profiling proved invaluable due to the significant performance improvements achieved. Click to expand...
<!-- artifact:quote:end -->
I mean not to detract from your diary(I don't even own CK3) but its totally up there with 'cool' knowing you enjoy ASM and 8 bit and 16 bit code. There is a old school ARPG that I work on, its abandonware and the beta client and server code is available, the server app is mostly written in 16 bit ASM and you don't really get much closer to working directly with the CPU than that. I grew up around those games but I've decided to just work in C#, it won't be nearly as efficient but it may give my brain more space to learn and seems to be going okay! Thanks for sharing a part of yourself with us anyway, I think it adds a much needed personal touch to some diaries across Paradox.

## Reply 31 — participant_023 · 2025-10-15 · post-30802117

In the future, what do you think about reducing the amount of random courtiers and focusing on small minor noble families at courts? I think there are too many random courtiers throughout the game that sometimes may have no purpose or may be of a single one time use and then forgotten. Noble families could persist and both participate and compete in the player's world by seeking to get titles, land, marriages, conspiring, etc. Random commoner courtiers should probably be more pervasive in baron and count courts than above.

## Reply 32 — participant_024 · 2025-10-15 · post-30802143

<!-- artifact:quote:start -->
> rodgerdavies said: One thing I am a huge admirer of PDX for is being open and not treating the audience like idiots (even if that may be true in my case). Click to expand...
<!-- artifact:quote:end -->
A thing Colossal Order could learn from, instead of going "our simulation is complex and we wont tell you how it works"

## Reply 33 — participant_010 · 2025-10-15 · post-30802146

<!-- artifact:quote:start -->
> Marusama said: "Feature steward"? Does this mean that there are plans to integrate DLC features together, or to add new features to old systems which were implemented after release? Click to expand...
<!-- artifact:quote:end -->
Feature stewards is a team-internal way of structuring decision making for what's important for the implementation of the features during dlc development. : )

## Reply 34 — participant_025 · 2025-10-15 · post-30802149

<!-- artifact:quote:start -->
> Metz said: In the future, what do you think about reducing the amount of random courtiers and focusing on small minor noble families at courts? I think there are too many random courtiers throughout the game that sometimes may have no purpose or may be of a single one time use and then forgotten. Noble families could persist and both participate and compete in the player's world by seeking to get titles, land, marriages, conspiring, etc. Random commoner courtiers should probably be more pervasive in baron and count courts than above. Click to expand...
<!-- artifact:quote:end -->
That's what they did. They made the number of random spawned in characters less. It's near the bottom of this dev diary

## Reply 35 — participant_025 · 2025-10-15 · post-30802151

Also, could someone please look at how saves effect loading times? The more saves you have in your save game folder, the longer it takes for the game to load? I dont know if its a fundamental part of the way the game is made but it's quite annoying having to wipe my savegames out if i want to bring back decent loadtimes. Sometimes it would even fully freeze the game when loading in!

## Reply 36 — participant_026 · 2025-10-15 · post-30802157

<!-- artifact:quote:start -->
> Divine said: Barons don’t have councils or court positions, yet they were still evaluating all of them; they no longer do that now Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> So we went and reduced or eliminated a bunch of ‘sources’ of characters that generate boring, useless, random or invisible characters that then linger in guest pools, the sidelines of courts of barons and counts, and that take up space and cost performance. Click to expand...
<!-- artifact:quote:end -->
afaict, family heads holding no landed titles have their ai reduced to barony level, so im a little worried about this, given that they DO have councils and court positions. i would hope im either wrong about this or that this has been accounted for. with the amount of unlanded family head titles that will have been added to model imperial chinese bureaucracy in auh, itd be very weird if they didnt matter much or do much of anything this i am extremely happy to hear about, however. im too dumb to fully understand much of anything technical mentioned in this dev diary, you guys say its better and ill just take your word for it, but this specifically is something ive been begging for since ck2 days. i am genuinely ecstatic to see this

## Reply 37 — participant_027 · 2025-10-15 · post-30802165

Great work, thanks for what is arguably the most interesting developer diary in a while. Could you please tell me how all these changes have affected save file sizes? Especially in the late game (300+ years).

## Reply 38 — participant_010 · 2025-10-15 · post-30802173

<!-- artifact:quote:start -->
> Doonyal said: Also, could someone please look at how saves effect loading times? The more saves you have in your save game folder, the longer it takes for the game to load? I dont know if its a fundamental part of the way the game is made but it's quite annoying having to wipe my savegames out if i want to bring back decent loadtimes. Sometimes it would even fully freeze the game when loading in! Click to expand...
<!-- artifact:quote:end -->
Right now we've focused on the tick-speed performance since that was our major challenge with this expansion. In the future we will have capacity to deal with other types of technical problems. I can't guarantee anything for future releases but I can say that we've heard your pleas of loadtimes related to saves and mods (and in general) and it's among our top things to look into at some point after All Under Heaven. It's also affecting our dev builds so it's also an efficiency factor for us internally when we boot the game dozens of time per day. ; ) The scaling load times with mods is the one that might prove a bit tricky though since it might be related to our structural choice of file-access which is not scaling well with a large increase in amount of virtual paths created by each individual mod-path - however I say this before I've actually had the time to analyze the problem fully.

## Reply 39 — participant_010 · 2025-10-15 · post-30802176

<!-- artifact:quote:start -->
> Gamshud said: Great work, thanks for what is arguably the most interesting developer diary in a while. Could you please tell me how all these changes have affected save file sizes? Especially in the late game (300+ years). Click to expand...
<!-- artifact:quote:end -->
I haven't looked at this for a while. The main changes of making the world larger should have a negative impact on saves. While our optimizations, mainly for not keeping unimportant characters around, should have a positive impact on the saves. Sadly I have not quick comparison at hand.

## Reply 40 — participant_028 · 2025-10-15 · post-30802185

Thanks a lot for your work and dev-diary! Have you considered also allowing player to choose playing on "old" version of map, or only in the east (or a couple of other variants of sub-maps) (just limiting the map for optimization). If I wanna play as little japanese shogun, i dont necessarily need simulating of europe and this would help a lot with optimization in late game, especially in late game

## Reply 41 — participant_029 · 2025-10-15 · post-30802194

Great thanks for developer diary. Especially for changes in administrative AI logics and using real wandering characters in events instead of generating new ones. But I have couple of questions. 1. Can you add more detailed info about graphical settings in game UI? Like, how much VRAM this setting uses or what impact it has on performance (at least approximately). 2. What about screen freezing for 1+ minutes when opening administrative succession menu with tons of candidates in late game? Is this fixed? Also, the same freezes appeared in themas menus, but less long (armies menu and general list). 3. Also, I would like to ask one specific question about setting called Mesh LOD Fade. From my observations, some game crashes happened during FPS jumps, so I limited it to 30. And also, I turned off this setting, because it may cause micro drops during map zoom. I have much less crashes from there. I just got lucky, or this change really made some difference?

## Reply 42 — participant_021 · 2025-10-15 · post-30802195

<!-- artifact:quote:start -->
> Divine said: I can sadly confirm that we didn't manage to get Native Apple Silicon into the initial release of All Under Heaven but we're looking into it Click to expand...
<!-- artifact:quote:end -->
Very glad to hear. Thanks for the great job on everything. This has been my most played game on Steam since it came out.

## Reply 43 — participant_019 · 2025-10-15 · post-30802204

<!-- artifact:quote:start -->
> JoeManyak said: Thanks a lot for your work and dev-diary! Have you considered also allowing player to choose playing on "old" version of map, or only in the east (or a couple of other variants of sub-maps) (just limiting the map for optimization). If I wanna play as little japanese shogun, i dont necessarily need simulating of europe and this would help a lot with optimization in late game, especially in late game Click to expand...
<!-- artifact:quote:end -->
The devs have talked about this before, it would be a lot of work to maintain separate map files in Clausewitz like this.

## Reply 44 — participant_010 · 2025-10-15 · post-30802220

<!-- artifact:quote:start -->
> JoeManyak said: Thanks a lot for your work and dev-diary! Have you considered also allowing player to choose playing on "old" version of map, or only in the east (or a couple of other variants of sub-maps) (just limiting the map for optimization). If I wanna play as little japanese shogun, i dont necessarily need simulating of europe and this would help a lot with optimization in late game, especially in late game Click to expand...
<!-- artifact:quote:end -->
We did consider it but the way we load our databases and map into the game it's pretty complicated to have a good player way to select only partial map parts. It was considered a very costly feature to make streamlined for the player experience of it. And additionally it is a maintenance nightmare having not only to make sure all new features work and take one world into account but all of the different combinations of map-setups into account. We definitely welcome any mods which would not have to suffer under the parts of handling the player selection after you're already in the main-menu of the game but rather just loading up the game with a different setup of the map. This is the better way of handling this in my opinion and doesn't let us hide with lower performance ambitions under a potential player choice of disbanding parts of the map.

## Reply 45 — participant_027 · 2025-10-15 · post-30802231

<!-- artifact:quote:start -->
> Divine said: I haven't looked at this for a while. The main changes of making the world larger should have a negative impact on saves. While our optimizations, mainly for not keeping unimportant characters around, should have a positive impact on the saves. Sadly I have not quick comparison at hand. Click to expand...
<!-- artifact:quote:end -->
I understand you were focusing on the game's tick rate, and if everything described in the diary actually works as described, these are very important and useful changes. I asked about save files for one simple reason: I recently wrote about performance issues with bureaucrats. And I ran into a funny problem: I simply couldn't upload a save file to the bug report on the forum because each of my late-game saves is about 60 MB in size. So this is more of a personal issue than a general problem, I guess. In any case, thanks for the response and the informative dev diary.

## Reply 46 — participant_030 · 2025-10-15 · post-30802233

Thank you for the helpful development diary. By the way, could you tell me the range of province numbers that will be added in AUH? Or even the range to avoid would be fine.

## Reply 47 — participant_010 · 2025-10-15 · post-30802243

<!-- artifact:quote:start -->
> okawfj said: Thank you for the helpful development diary. By the way, could you tell me the range of province numbers that will be added in AUH? Or even the range to avoid would be fine. Click to expand...
<!-- artifact:quote:end -->
Amount of baronies/landed provinces should be increased by around 32% in the AUH map compared to the previous patch.

## Reply 48 — participant_010 · 2025-10-15 · post-30802253

<!-- artifact:quote:start -->
> Gamshud said: I understand you were focusing on the game's tick rate, and if everything described in the diary actually works as described, these are very important and useful changes. I asked about save files for one simple reason: I recently wrote about performance issues with bureaucrats. And I ran into a funny problem: I simply couldn't upload a save file to the bug report on the forum because each of my late-game saves is about 60 MB in size. So this is more of a personal issue than a general problem, I guess. In any case, thanks for the response and the informative dev diary. Click to expand...
<!-- artifact:quote:end -->
Interesting problem. : ) I've forwarded a question to see if we can also increase the max-file size for uploads in the bug forums. Those saves definitely sounds useful for our QA department to get their hands on.

## Reply 49 — participant_003 · 2025-10-15 · post-30802270

Did you also do anything to appointment succession in Byz?

## Reply 50 — participant_031 · 2025-10-15 · post-30802273

Thank you for the DD and the work! I don't know if you documented a list of what sorts of changes you made to optimise script? Things like "simple triggers first", "iterate over smallest possible list", and maybe some of the less obvious ones; sharing the knowledge of that experience can help modders.

## Reply 51 — participant_017 · 2025-10-15 · post-30802280

<!-- artifact:quote:start -->
> tilly said: afaict, family heads holding no landed titles have their ai reduced to barony level, so im a little worried about this, given that they DO have councils and court positions. i would hope im either wrong about this or that this has been accounted for. with the amount of unlanded family head titles that will have been added to model imperial chinese bureaucracy in auh, itd be very weird if they didnt matter much or do much of anything Click to expand...
<!-- artifact:quote:end -->
That's not true. Landless noble family heads have full-scale AI and are capable of almost everything that they can afford

## Reply 52 — participant_017 · 2025-10-15 · post-30802283

<!-- artifact:quote:start -->
> tribnia said: Did you also do anything to appointment succession in Byz? Click to expand...
<!-- artifact:quote:end -->
Yes, as I described changes to appointment succession, at least half of it applies to Byzantium. It should be much faster

## Reply 53 — participant_017 · 2025-10-15 · post-30802299

<!-- artifact:quote:start -->
> kuczaja said: The best way to reproduce it would be to put anything more complex than single number inside "levies = " parameter. If you'll put checking for opinion or some special circumstances, the performance drag will happen even if the game is still paused. Click to expand...
<!-- artifact:quote:end -->
I think now I understand what you mean. Thank you for bringing it to our attention. Indeed, in base game we only use simple direct values for those properties, while script supports any math. It's already made significantly faster in AUH - those values in GUI are evaluated every 20 frames instead of every frame, and you can change this delay to be even bigger in the define. I expect any complex script math still to be very slow there, since it percolates to all vassals down to barony level, so x20 speedup may still be insufficient. If I were to design such system from scratch, I would forbid script math in obligations completely, and instead ask designers to be clever with modifiers. Maybe use scaled timed modifiers if they want customized obligations that much. In that case script math will be run only once, when modifier is created

## Reply 54 — participant_032 · 2025-10-15 · post-30802303

One of the most important dev diaries!

## Reply 55 — participant_033 · 2025-10-15 · post-30802325

Really appreciate the look under the hood, it's not something fans get with a lot of games. Could you guys help out your brothers and sisters in Cities Skylines 2 by chance? They are having some trouble over there. In all seriousness, I wish this type of communication and transparency was common across the gaming space. Really excited for AUH.

## Reply 56 — participant_034 · 2025-10-15 · post-30802335

Honestly I don't care about the performance too much. I mainly care if this fixes the system freezes.

## Reply 57 — participant_032 · 2025-10-15 · post-30802338

<!-- artifact:quote:start -->
> Krazel said: Really appreciate the look under the hood, it's not something fans get with a lot of games. Could you guys help out your brothers and sisters in Cities Skylines 2 by chance? They are having some trouble over there. In all seriousness, I wish this type of communication and transparency was common across the gaming space. Really excited for AUH. Click to expand...
<!-- artifact:quote:end -->
Yeah true, Creative Assembly should take notes

## Reply 58 — participant_010 · 2025-10-15 · post-30802360

<!-- artifact:quote:start -->
> Krazel said: Really appreciate the look under the hood, it's not something fans get with a lot of games. Could you guys help out your brothers and sisters in Cities Skylines 2 by chance? They are having some trouble over there. In all seriousness, I wish this type of communication and transparency was common across the gaming space. Really excited for AUH. Click to expand...
<!-- artifact:quote:end -->
It's a bit time-consuming but very fun to share detailed information about our dealings. Thank you all for participating and engaging in the conversations about in-depth code and game-design concepts. : )

## Reply 59 — participant_035 · 2025-10-15 · post-30802365

Awesome DD, though I do find it a tad amusing that people were complaining about Performance before East Asia was added, and now performance updates were made that should have made the old map buttery smooth! But are then mostly offset by the expansion of the game world by 32%. Still, even then it should be on average faster in late game as you show(which is the important bit), and its great that the apocalypse some of the anti-expansion folks were predicting was averted handily.

## Reply 60 — participant_010 · 2025-10-15 · post-30802388

<!-- artifact:quote:start -->
> KingMyrddin said: Honestly I don't care about the performance too much. I mainly care if this fixes the system freezes. Click to expand...
<!-- artifact:quote:end -->
So details here are that we still don't know fully what causes the OS to freak out with the newer updates. However we've also been affected by this on the developer-side. We have found a configuration to our threading task management for where we are no longer internally encountering any freezes in the dev builds. This change comes out with the All Under Heaven patch and I'm pretty hopeful that this will also help the system freezes you as players might encounter. So after the patch please let us know if the amount of system freezes when running CK3 is constant or has decreased.

## Reply 61 — participant_036 · 2025-10-15 · post-30802396

Very informative dev diary on performance and optimization.

## Reply 62 — participant_037 · 2025-10-15 · post-30802401

<!-- artifact:quote:start -->
> Divine said: Why not do everything in parallel? We need a deterministic order of observable changes in the game for multiplayer to work, so all clients have the same game state as everyone else. Another important part is again the ability to reason about the correctness of the game. Most changes in the game have propagating side effects. A Ruler conquering a new title means that another Ruler is going to lose a title. Loss of a title means changes in income and military power. A Ruler who gets weaker is more endangered by factions and other enemies. During any of those steps additional events may get triggered. A strictly determined order of actions and cascading side effects is necessary to understand and predict game outcomes. Click to expand...
<!-- artifact:quote:end -->
Great DD, really well-written, detailed, and actually puts my mind to ease a bit about the impact of the new areas/systems on existing performance. One thing that caught my eye: As someone who has basically never touched CK3 multiplayer (I like my own sandbox and mods can also make that very tricky regardless), how much of a difference is there between the sequential vs. parallel needs of the multiplayer versus the broader needs you describe for actions and cascading side effects? In other words, is the multiplayer stability bottleneck significant compared to the underlying sequence requirements of the game generally? I realize it's a pipe dream that almost certainly isn't in the cards given other priorities, but depending on how significant the multiplayer bottleneck is would a "singleplayer only" parallel system be practical?

## Reply 63 — participant_027 · 2025-10-15 · post-30802412

I also wanted to ask about multiplayer performance. I played with a friend at the game's release, and everything was relatively fine. But I played multiplayer relatively recently, specifically after Khans of the Steppe was released, and we were constantly experiencing crashes and desyncs, and the game overall felt more choppy, even when you were the host. Again, I understand this isn't what the dev diary was about, but have there been any stability improvements in multiplayer?

## Reply 64 — participant_017 · 2025-10-15 · post-30802417

<!-- artifact:quote:start -->
> TripleAgent said: I realize it's a pipe dream that almost certainly isn't in the cards given other priorities, but depending on how significant the multiplayer bottleneck is would a "singleplayer only" parallel system be practical? Click to expand...
<!-- artifact:quote:end -->
No, not really. It's already a significant mental overhead when developing multi-threaded logic. Whatever we exposed to design via script must be sequential, otherwise it will spread all the technical problems to their discipline. Lots of script runs conditions in triggers and uses the outcome to determine the effect. Almost always executed effect assumes that triggered outcome remains true until effect is finished. If some other effect in parallel can change game world, and potentially invalidate the condition, then logic starts to fall apart. It will cause so much defensive coding in script, it'll likely ruin any potential performance gain

## Reply 65 — participant_038 · 2025-10-15 · post-30802419

<!-- artifact:quote:start -->
> Divine said: So details here are that we still don't know fully what causes the OS to freak out with the newer updates. However we've also been affected by this on the developer-side. We have found a configuration to our threading task management for where we are no longer internally encountering any freezes in the dev builds. This change comes out with the All Under Heaven patch and I'm pretty hopeful that this will also help the system freezes you as players might encounter. So after the patch please let us know if the amount of system freezes when running CK3 is constant or has decreased. Click to expand...
<!-- artifact:quote:end -->
I have to commend the tech team for such an informative and transparent dev diary. I think most developers in the industry underestimate just how much the players are not aware of the subtleties and intricacies of the tech systems underlying a game. I am glad you and peers are not afraid to throw technical information at us, it is very good at controlling the misinformation out there. For example, I was ready to complain about the diplomatic range issue brought up earlier but the reply as to why this was the case made sense to me and calmed me down. I can imagine there are a thousand tiny pet causes and issues that cause anger in the players that a good technical reason (where it exists) would help deescalate the situation. So basically, I am saying that I would like a big fat juicy Performance dev diary for each DLC release.

## Reply 66 — participant_017 · 2025-10-15 · post-30802420

<!-- artifact:quote:start -->
> Gamshud said: I also wanted to ask about multiplayer performance. I played with a friend at the game's release, and everything was relatively fine. But I played multiplayer relatively recently, specifically after Khans of the Steppe was released, and we were constantly experiencing crashes and desyncs, and the game overall felt more choppy, even when you were the host. Again, I understand this isn't what the dev diary was about, but have there been any stability improvements in multiplayer? Click to expand...
<!-- artifact:quote:end -->
I can't promise you anything regarding MP stability - my other colleagues can do that, I was solely focused on game speed. But there were several unfortunate issues in main game UI that may cause nomadic realms to feel extra slow and lead to lower FPS. This should be addressed in AUH. Let's hope it will indirectly improve your MP experience.

## Reply 67 — participant_039 · 2025-10-15 · post-30802422

It's nice to see that you're saving some computational efficiency by prioritizing higher-tier AIs. The real question is, is there anyone actually working on expending these saved resources to make those higher-tier AIs behave more intelligently than the completely lifeless, brain-dead CK3 AI that the forum has pointed out for half a decade? Because if not, then there's really no point in saving any computational efficiency at all. We've been fed the line "working on it" for years with no meaningful improvement.

## Reply 68 — participant_031 · 2025-10-15 · post-30802425

<!-- artifact:quote:start -->
> Mindel said: It's nice to see that you're saving some computational efficiency by prioritizing higher-tier AIs. The real question is, is there anyone actually working on expending these saved resources to make those higher-tier AIs behave more intelligently than the completely lifeless, brain-dead CK3 AI that the forum has pointed out for half a decade? Because if not, then there's really no point in saving any computational efficiency at all. Click to expand...
<!-- artifact:quote:end -->
Making AI more intelligent is a different matter and I think the bottleneck isn't performance, but just the design of the game, with all decision moments being independent making strategy almost impossible.

## Reply 69 — participant_037 · 2025-10-15 · post-30802426

<!-- artifact:quote:start -->
> Revolution 11 said: So basically, I am saying that I would like a big fat juicy Performance dev diary for each DLC release. Click to expand...
<!-- artifact:quote:end -->
Yeah let these folks out of the coding mines more often, they're great to hear from!

## Reply 70 — participant_038 · 2025-10-15 · post-30802430

<!-- artifact:quote:start -->
> Mindel said: It's nice to see that you're saving some computational efficiency by prioritizing higher-tier AIs. The real question is, is there anyone actually working on expending these saved resources to make those higher-tier AIs behave more intelligently than the completely lifeless, brain-dead CK3 AI that the forum has pointed out for half a decade? Because if not, then there's really no point in saving any computational efficiency at all. Click to expand...
<!-- artifact:quote:end -->
That seems like a straw man to me. I am all for more intelligent AIs if you look at my CK3 posts, but there is value in just making the game faster. Plenty of people (not on the forum) play the game and are happy with it if it just ran faster on crappier hardware. Gains in performance are not invalidated because of preexisting flaws in game design. I do agree with you that the AI needs more "intelligence" and proactive behavior but more performance is still good, regardless of what the AI is doing.

## Reply 71 — participant_039 · 2025-10-15 · post-30802434

<!-- artifact:quote:start -->
> Keizer Harm said: Making AI more intelligent is a different matter and I think the bottleneck isn't performance, but just the design of the game, with all decision moments being independent making strategy almost impossible. Click to expand...
<!-- artifact:quote:end -->
Indeed, you may be right. But if so then the devs should be honest to us about it. Lessons should be clearly articulated and learned for CK4. And also, if so then what is there to celebrate about computational savings? A chess program that plays poorly but quickly isn't worth much in my book.

## Reply 72 — participant_040 · 2025-10-15 · post-30802439

<!-- artifact:quote:start -->
> Alien-47 said: Script during game load is translated into a tree of callable objects in C++ code. There's no way we let anyone modify C++ game code directly. It's a security nightmare Some script documentation exists in the .info files and when you run "script_docs" console command. That's what we use ourselves internally. It's a compromise between time spent making tools and time spent actually using tools to make a game Click to expand...
<!-- artifact:quote:end -->
How do you parse the scripts? One time I made simple parser and found several missing curly braces in common/genes and a such a line somewhere: value = 10'(note the single quote).

## Reply 73 — participant_041 · 2025-10-15 · post-30802440

I guess that's good news, a bit slower at the first 50 years which well runs fast enough to not be very noticeable and then a bit faster after that. I still curious to see how it's gonna run on my end, not implying that you guys are lying just as stated in the DD depends on hardware, playstyle and whatever happens on the world around. I would like to see some information on realm size, performance does get worse larger our realm is and I don't mean "my game gets slow when I conquer the world" more like a large but reasonable realm, let's say Byzantines with Italia type of thing. Also any changes on how scourge of the gods can affect performance? At least on my end performance can drop very noticeably if a scourge of the gods gets a massive blob nearby. Kinda interesting how the mongols don't affect the performance as bad as a tribal scourge of gods. Like if Dyre or Rurikid gets scourge of the gods and conquer the entire main land Europe, I can have a small Sweden realm and it lags the crap out of my game. I imagine it's related with the constant raise, move, disband large tribal armies and calculating how much levies they have? Idk. Do you guys have any data on these?

## Reply 74 — participant_042 · 2025-10-15 · post-30802442

So for adventurers we'll have to use duchy right ?

## Reply 75 — participant_043 · 2025-10-15 · post-30802460

It sounds like you made a great job. I hope Nvidia app will find the optimized settings for my setup.

## Reply 76 — participant_044 · 2025-10-15 · post-30802464

I’ve been very negative on the game lately, but it does feel nice to read something so comprehensive and well written. Do you think the game will benefit from RAM amounts larger than 16gigs?

## Reply 77 — participant_045 · 2025-10-15 · post-30802471

<!-- artifact:quote:start -->
> Divine said: 1. For gameplay reasons we unfortunately always need you to have access to actions within your own realm to avoid doom-spiraling large empires in ways outside of the players control when they would no longer be able to manage their empire title setups after inheritances/wars/whatever. I agree that larger realms are something that poses a problem in scaling since whenever we add inter-vassal interactions the complexity grows factorially with the size of the realm unless we find ways to mitigate that somehow. And complexity for liege-to-vassal interactions with additional objects will also grow exponentially. This is not an easy problem to solve but setting max ai evaluation targets is one of the ways that you may find to close the gap here. Click to expand...
<!-- artifact:quote:end -->
On the subject of addressing this issue through ai evaluation, is there any possibility of adding new ai_recipients categories to make this easier to do? I think the easiest set, and the set most in line with what you're already doing in other areas, would be to have versions of categories like vassals, neighboring_rulers, peer_vassals, and even realm_characters that filter based on minimum tier. Only problem with this is that thats potentially a lot of new types of recipient, though if the parser can handle it having a minimum tier parameter as an option within the ai_targets block could make it easier? It would also be nice if, particularly for realm_characters, we got a nearby_realm_characters option that either uses a define for distance (like nearby_domicile_owners) or based itself off of what diplomatic range would be if not for the shared realm. If going the route of using defines, it would be cool for their to be separate defines based on whether the target is a ruler or not (or even based on title tier), though I don't think thats at all necessary, particularly if the above option is added. Lastly, and this isn't a performance issue that comes up in Vanilla to my knowledge, but is a performance related thing for mods that relates to ai_recipients and similar predefined lists: would it be possible to make it so variable lists (either local or global) can be used for things like ai_recipients, province_filter, etc. I haven't actually ever decompiled the game's code, so I don't know if it'd even be possible without having to do time-consuming type conversions, but for province_filters in particular I've very frequently as a modder encountered situations where there is a very limited set of provinces that I want the AI/Player to be able to choose from (often even a list that is the same for all characters, such as the location of secular universities, of ruins to go dungeon delving in, of metropolis' to visit, etc.), but still wind up needing to use province_filter = all even for the AI.

## Reply 78 — participant_013 · 2025-10-15 · post-30802483

<!-- artifact:quote:start -->
> Alien-47 said: I think now I understand what you mean. Thank you for bringing it to our attention. Indeed, in base game we only use simple direct values for those properties, while script supports any math. It's already made significantly faster in AUH - those values in GUI are evaluated every 20 frames instead of every frame, and you can change this delay to be even bigger in the define. I expect any complex script math still to be very slow there, since it percolates to all vassals down to barony level, so x20 speedup may still be insufficient. If I were to design such system from scratch, I would forbid script math in obligations completely, and instead ask designers to be clever with modifiers. Maybe use scaled timed modifiers if they want customized obligations that much. In that case script math will be run only once, when modifier is created Click to expand...
<!-- artifact:quote:end -->
Thank you! Yes, in AGOT we optimized it by moving stuff from the contracts to modifiers. So for example vanilla perk fp2_urbanism_legacy_3 got "republic_government_levy_contribution_add = 0.15" and "republic_government_tax_contribution_add = 0.15" lines instead of checking for the perk inside republics contract. Might be worth moving it to the main game, so far i didn't found any side effects of that. But i'm really glad that this was made 1/20 frames instead of each frame. That will certainly let us add some math there if it's unavoidable

## Reply 79 — participant_017 · 2025-10-15 · post-30802496

<!-- artifact:quote:start -->
> Kcajkcaj99 said: Lastly, and this isn't a performance issue that comes up in Vanilla to my knowledge, but is a performance related thing for mods that relates to ai_recipients and similar predefined lists: would it be possible to make it so variable lists (either local or global) can be used for things like ai_recipients, province_filter, etc. I haven't actually ever decompiled the game's code, so I don't know if it'd even be possible without having to do time-consuming type conversions, but for province_filters in particular I've very frequently as a modder encountered situations where there is a very limited set of provinces that I want the AI/Player to be able to choose from (often even a list that is the same for all characters, such as the location of secular universities, of ruins to go dungeon delving in, of metropolis' to visit, etc.), but still wind up needing to use province_filter = all even for the AI. Click to expand...
<!-- artifact:quote:end -->
I personally would oppose to that if a designer suggests it. We managed to find cheaper alternatives for now. You can already use various set target effect, and secondary recipient lists - those exist to allow similar flexibility. I strongly doubt that allowing more script will save performance. In practice it's cheaper to find all potential targets and then run trigger, then use script to build partial list of targets, and then again run the rest of usual triggers on it

## Reply 80 — participant_046 · 2025-10-15 · post-30802514

<!-- artifact:quote:start -->
> Divine said: I can't guarantee anything for future releases but I can say that we've heard your pleas of loadtimes related to saves and mods (and in general) and it's among our top things to look into at some point after All Under Heaven. It's also affecting our dev builds so it's also an efficiency factor for us internally when we boot the game dozens of time per day. ; ) The scaling load times with mods is the one that might prove a bit tricky though since it might be related to our structural choice of file-access which is not scaling well with a large increase in amount of virtual paths created by each individual mod-path - however I say this before I've actually had the time to analyze the problem fully. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Load times are amazing with this mod. Playset without preserver (load times): 11 min Playset with preserver (load times): 3min & 15 seconds. I play with AGOT & have about 100 mods running Click to expand...
<!-- artifact:quote:end -->
Many users of CK3 Playset Preserver report significantly reduced game launch times when they use the tool to reduce their large (50+ mods, 5+ GB) playsets into one mod. One user said this: There's no reason just moving files from many folders into one folder ought to have such an effect. Hopefully, it would be pretty simple to have the game do some caching or pre-computing early during launch and pick up some easy performance gains. Lots of people play with lots of mods. Some users also report faster in-game ticks, so if they aren't hallucinating, maybe there are more easy performance gains down that road. If the script file system never changes while the game is running, then there ought to be caching during launch that isolates in-game code from getting slowed down by something like that.

## Reply 81 — participant_047 · 2025-10-15 · post-30802527

TLDR: "It's playable"...it's downhill from here. I'm super glad I didn't buy this expansion pass and I wonder if people who didn't buy it will somehow be affected by this "playable" performance as well...but I am guessing it will.

## Reply 82 — participant_048 · 2025-10-15 · post-30802544

How deep is the chronological implementation of titles and characters? In the history of Asian states, we encounter origins that stretch deep into antiquity. Will B.C.E. (or B.C.) years finally be added to the timeline, or will we see something similar to the Roman Empire, where Emperor Octavian Augustus is represented as a child and the title doesn't start until the beginning of the Common Era (C.E.)? In that case, the game's history will lose a huge number of great rulers, and many dynasties in Asia will be 'truncated,' meaning the Emperors of China and Japan won't have titles stretching back into B.C.E. years as they do in real history. I have also heard many tall tales that the code does not support B.C.E. years and that this allegedly causes problems, but this is only a half-truth, because it reliably supports history files. I myself can't remember how many times I've used B.C.E. years for my bookmark mod (oh yes, a huge number of times), and it works absolutely fine. In short, I would like to hear any news regarding this from you guys.

## Reply 83 — participant_049 · 2025-10-15 · post-30802557

What has been done against the growing Mod List Bug, introduced with 1.9? All Mods copy themself with every saving, causing the Game to think, that a Save Game has over 1.000 Mods, while in Reality only 30. This affects for sure the Performance.

## Reply 84 — participant_050 · 2025-10-15 · post-30802563

@Divine Thanks for the diary. I've been expecting something like this for a while, but unfortunately, I didn't see the problem I was expecting: the game has caching issues, at least on Windows systems, which cause problems with game loading speed, performance, stability, and responsiveness in a variety of scenarios. Mods are one of the most obvious examples to reproduce this bug: adding any modifications (even empty ones consisting only of a description file) significantly increases game loading times and gradually reduces performance and stability. The issue is demonstrated in the bug report linked below: Adding any mods (even empty ones) significantly reduces the game loading speed and also reduces overall performance. Information I have verifed my game files (Steam only) Yes I have disabled all mods Yes I am running the latest game update Yes Required Summary Adding any mods (even empty ones) significantly reduces the game loading speed and also reduces... forum.paradoxplaza.com I initially discovered this issue in Stellaris, but then, out of curiosity, I decided to test it in Crusader Kings 3 – it was reproducible, albeit less pronounced. Here's a link to a similar thread on Stellaris: Stellaris - Adding any mods (even empty ones) reduces the overall performance of the game [4.0.16] & [05ae] Description Adding any mods (even empty ones) reduces the overall performance of the game [4.0.16] & [05ae] Game Version [4.0.16] & [05ae] What version do you use? Steam What expansions do you have installed? I have the Subscription Do you... forum.paradoxplaza.com Here are links to comments from user AnCi420, who somehow determined that the issue was related to caching: Stellaris - Adding any mods (even empty ones) reduces the overall performance of the game [4.0.16] & [05ae] Description Adding any mods (even empty ones) reduces the overall performance of the game [4.0.16] & [05ae] Game Version [4.0.16] & [05ae] What version do you use? Steam What expansions do you have installed? I have the Subscription Do you... forum.paradoxplaza.com Stellaris - Adding any mods (even empty ones) reduces the overall performance of the game [4.0.16] & [05ae] Description Adding any mods (even empty ones) reduces the overall performance of the game [4.0.16] & [05ae] Game Version [4.0.16] & [05ae] What version do you use? Steam What expansions do you have installed? I have the Subscription Do you... forum.paradoxplaza.com Stellaris: Performance issues on MacBook Pro apple silicon Greetings, as the title suggests I'm running in quite serious performance issues in stellaris on my MacBook Pro M3 Max with 14 CPU cores and 30 GPU cores with 36 GB of unified memory The Stellaris version which I'm running is the 4.0.22... forum.paradoxplaza.com Could you please look into this issue? Mods are a very important part of the game, and I personally can't imagine playing without them. The issue isn't just caused by mods, but also by DLCs and the number of save games on the computer.

## Reply 85 — participant_007 · 2025-10-15 · post-30802575

<!-- artifact:quote:start -->
> Alien-47 said: Yes, as I described changes to appointment succession, at least half of it applies to Byzantium. It should be much faster Click to expand...
<!-- artifact:quote:end -->
I hope you've fixed all the bugs of administrative successions in the process ? - Wrong succession line for unasigned themes dispalyed on the UI - Possibility to spend influence on unasigned themes that are actually not handled in apointement succession (works like primogeniture) and are always innerited by the emperor/king heir - The player heir is buged when your primary heir is from your dynasty but not from your house, resulting loosing all your estate on succession etc.... And concerning performance did you fix the performance bug on decision UI with the fixedgridbox ?

## Reply 86 — participant_013 · 2025-10-15 · post-30802578

<!-- artifact:quote:start -->
> SargeantAvocado3 said: TLDR: "It's playable"...it's downhill from here. I'm super glad I didn't buy this expansion pass and I wonder if people who didn't buy it will somehow be affected by this "playable" performance as well...but I am guessing it will. Click to expand...
<!-- artifact:quote:end -->
Oh don't complain. Frankly the perf impact of larger map was vastly overblown by the community in the first place, so i expect the game to perform better than before and mods to have twice the gain.

## Reply 87 — participant_010 · 2025-10-15 · post-30802604

<!-- artifact:quote:start -->
> IoannesBarbarus said: Many users of CK3 Playset Preserver report significantly reduced game launch times when they use the tool to reduce their large (50+ mods, 5+ GB) playsets into one mod. One user said this: There's no reason just moving files from many folders into one folder ought to have such an effect. Hopefully, it would be pretty simple to have the game do some caching or pre-computing early during launch and pick up some easy performance gains. Lots of people play with lots of mods. Some users also report faster in-game ticks, so if they aren't hallucinating, maybe there are more easy performance gains down that road. If the script file system never changes while the game is running, then there ought to be caching during launch that isolates in-game code from getting slowed down by something like that. Click to expand...
<!-- artifact:quote:end -->
That's an interesting data-point. Thanks for sharing. We should definitely look into what is happening under the hood with our file handling system for this. It's not impossible that it would also slightly affect tick-speeds but it sounds pretty odd considering that my main assumption for the slowdown would be for file-conflict resolution between virtual paths - which mainly shouldn't happen while the game is active. I could see this slowing down auto-saves potentially though.

## Reply 88 — participant_051 · 2025-10-15 · post-30802626

<!-- artifact:quote:start -->
> Divine said: That's an interesting data-point. Thanks for sharing. We should definitely look into what is happening under the hood with our file handling system for this. It's not impossible that it would also slightly affect tick-speeds but it sounds pretty odd considering that my main assumption for the slowdown would be for file-conflict resolution between virtual paths - which mainly shouldn't happen while the game is active. I could see this slowing down auto-saves potentially though. Click to expand...
<!-- artifact:quote:end -->
This happens in Stellaris, too, for what it's worth, and is a bit of a hot topic over there right now. It seems that for both games, the number of mods impacts performance - not just load times - without regard for the content (even empty mods have an impact). Something to do with the file structure, I'm guessing?

## Reply 89 — participant_052 · 2025-10-15 · post-30802629

Do you have estimates for how the performance of the 867 and 1178 starts compares over the first several hundred years?

## Reply 90 — participant_052 · 2025-10-15 · post-30802658

<!-- artifact:quote:start -->
> Alien-47 said: Yes, as I described changes to appointment succession, at least half of it applies to Byzantium. It should be much faster Click to expand...
<!-- artifact:quote:end -->
Any ideas on how much faster a very wide Byzantium is? As well, I've noticed that Administrative Rulers can't generate republic and feudal baron vassals, they exist as Admin vassals. Does that have an impact on performance too?

## Reply 91 — participant_016 · 2025-10-15 · post-30802743

<!-- artifact:quote:start -->
> Alien-47 said: It's already made significantly faster in AUH - those values in GUI are evaluated every 20 frames instead of every frame, and you can change this delay to be even bigger in the define. I expect any complex script math still to be very slow there, since it percolates to all vassals down to barony level, so x20 speedup may still be insufficient. If I were to design such system from scratch, I would forbid script math in obligations completely, and instead ask designers to be clever with modifiers. Maybe use scaled timed modifiers if they want customized obligations that much. In that case script math will be run only once, when modifier is created Click to expand...
<!-- artifact:quote:end -->
Yea if only there was a "taxes to liege" modifier....

## Reply 92 — participant_053 · 2025-10-15 · post-30802828

<!-- artifact:quote:start -->
> Divine said: Obvious drawback compared to older games - you never know for sure when it happens to you, the player. You don’t know the date when you get your personal monthly income, it just happens every 30 days. Click to expand...
<!-- artifact:quote:end -->
Great job! More of a modding performance question: for character interactions, are is_shown and ai_potential done in parallel? If not, which one is done before the other? I don't think the order of trigger evaluation in a script is documented anywhere. It would be a nice addition for modders Would it be possible to have any character controlled by a player have their normal update date be changed to being the 1st of the month? This shouldn't affect performance much (even in multiplayer) as most characters are still evenly spread across the month. Just makes it easier as the player to know what date you have to wait for if you really need that extra monthly tick of gold, prestige, or etc

## Reply 93 — participant_054 · 2025-10-15 · post-30802839

I love these technical dev diaries and im glad to see more pdx dev teams talk about it. That should help make the talk about performance more specific and productive for all sides. The results are also better than I hoped/feared. I guess my hope that all under heaven would be possible thanks to the discovery of another "greek characters run checks if they can blind and castrate the entire world" type speedup was more accurate than not ahahaha

## Reply 94 — participant_055 · 2025-10-15 · post-30802994

Wow, I love this dev diary. I especially loved the section about getting into the nitty gritty for the optimization process on canidate selection. This is what makes PDX dev diaries the best! The reminded me of a small thing I was wondering about now that there are even more "Landless" (Landish?) characters, can we get a filter in the marriage and character finder that says "no Landless/Adventurer/Domicile" people. Oh, and when you are playing as landless adventurer, can we get a filter that is "Within Interaction range" because right now you can have people in "Diplo range" but not all interactions are available. (Mainly this came up when I was playing a travelling bard looking to recruit people to my party through seduction and realzied diplo range was not sufficient for CK3 tinder )

## Reply 95 — participant_010 · 2025-10-15 · post-30803064

<!-- artifact:quote:start -->
> Emperor 1997 said: What has been done against the growing Mod List Bug, introduced with 1.9? All Mods copy themself with every saving, causing the Game to think, that a Save Game has over 1.000 Mods, while in Reality only 30. This affects for sure the Performance. Click to expand...
<!-- artifact:quote:end -->
This is the first time I hear about this. Sure sounds like a nuisance but I can't see how that would impact any performance outside of maybe a very slight hit at reading the savegames while we load the save-game. We'll add it to our issue tracker but I don't think it should impact your overall experience with modded gameplay.

## Reply 96 — participant_010 · 2025-10-15 · post-30803074

<!-- artifact:quote:start -->
> Empocariam said: Wow, I love this dev diary. I especially loved the section about getting into the nitty gritty for the optimization process on canidate selection. This is what makes PDX dev diaries the best! The reminded me of a small thing I was wondering about now that there are even more "Landless" (Landish?) characters, can we get a filter in the marriage and character finder that says "no Landless/Adventurer/Domicile" people. Oh, and when you are playing as landless adventurer, can we get a filter that is "Within Interaction range" because right now you can have people in "Diplo range" but not all interactions are available. (Mainly this came up when I was playing a travelling bard looking to recruit people to my party through seduction and realzied diplo range was not sufficient for CK3 tinder ) Click to expand...
<!-- artifact:quote:end -->
I'll pop over the idea to our UX-designers to figure out what potential list-filters would make sense for the games current state. : ) Thanks for the improvement idea.

## Reply 97 — participant_056 · 2025-10-15 · post-30803080

<!-- artifact:quote:start -->
> As an important bonus point, this also allows us to make things be considered more frequently for higher tier AI rulers without losing performance due to lower tier characters - making the game AI more responsive - when it matters. Click to expand...
<!-- artifact:quote:end -->
Long time forum lurker here, this amazing dev diary has forced me to comment and congratulate the devs on a job well done! I really love the tier-based AI frequency but wonder if it can be taken a step further. A common playthrough of CK consists of going from count to emperor and at each stage the characters which matter to me are different. As a count, the most interesting characters I interact with are my top liege (the duke), fellow vassals of my duke and my direct vassals (barons). As I tier up, this changes so that my top liege is now the king, I compete with fellow dukes and have counts as my direct vassals etc. I think the AI frequency should depend further on my current title, so that these cast of characters I see often have more AI updates (and ideally have a more complex AI to interact with me) so that there's more emergent story telling. CK3 has long had an issue of other characters not mattering and this should fix that, so that at every game stage early, mid and late there's important characters leaving a memorable mark in my playthrough. With the current system, as a count my barons will be quite useless.

## Reply 98 — participant_057 · 2025-10-15 · post-30803117

<!-- artifact:quote:start -->
> Divine said: View attachment 1380973 [Parallel AI update] View attachment 1380974 [Parallel pre-update of game systems] Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Divine said: The performance improvements to landless play should have an effect already across the board since the logic is to some extent shared between the new administrative realms and the Byzantine one. As for your second question - we're continuously looking at performance improvements for the CPU with new expansions. But it's easier to do after the features are added since they may expose new areas where older systems aren't keeping up with the scaling. And in that sense it's easier to fix the real performance killers first after we have a way to discover them. Performance improvements on the opposite actually have a tendency to decrease multiplayer stability. However we've also been working hard with specifically the out-of-synch problems which make hotjoin impossible. And yes I can confirm that Re-sync has been added so hopefully any remaining issues should be less annoying to deal with. Click to expand...
<!-- artifact:quote:end -->
What the hell happened on that last year?? As for the topic, I foresee greatness... Bugs and greatness... But mostly greatness! I'm eager to play! This might be the best expansion. This last part should be in the DD. This is very important for MP people.

## Reply 99 — participant_058 · 2025-10-15 · post-30803140

<!-- artifact:quote:start -->
> Alien-47 said: Yes, as I described changes to appointment succession, at least half of it applies to Byzantium. It should be much faster Click to expand...
<!-- artifact:quote:end -->
Much appreciation and gratitude to the tech team that worked on all of these efforts and then wrote about them at such length. This is a lot of effort that could easily have been done unrecognized. I know there has been a lot of demand signal from the player base with the performance concerns that warranted a dev diary, it is still appreciated, and I hope the tech team gets some kudos for carrying this weeks dev diary. And hopefully encouraged / included in the future! Even if it's not as big an effort as the AUH overhaul (underhaul?) has been, these sort of under-the-hood 'this is how we approached things, this is what we see, and this is how we fixed it' are a good reminder to the audience of the sort of challenges and tradeoffs the team faces. This goes double for the post-publication engagements with some of the forumite questions, and arguably even triple for the 'we tried this but it didn't work' sections. It is interesting in its own right, but also gives the fanbase a better understanding of what is, or is not, reasonable to hope or ask for. A 'what we fixed' tech diary like this might be valuable / helpful every blue moon or so, as part of the realm management team's irregular updates on addressing longstanding issues. By extension, should this also apply to the elective stalls when opining the candidate lists? I am not clear how much functionality is shared between administrative and the elective formats. Elective has its own stalls when you try to pick up larger candidate lists. That's probably unavoidable with Tanistry in particular, but it'll be nice if the elective family benefits in general.

## Reply 100 — participant_057 · 2025-10-15 · post-30803150

<!-- artifact:quote:start -->
> Mingo_Slickgrin said: This is fantastic to hear, please continue to try to make the game faster. I think that every time a new DLC is about to be released, a dev should be forced to play the game, with the new dlc installed, from 867 all the way to the end just to see what it's like. Not a playtester, an actual dev! Selected by lottery among the devs that don't have full plates maybe. Regardless, this dev diary fills me with hope that my laptop will still be able to play the game a year from now. Click to expand...
<!-- artifact:quote:end -->
A Dev condemned to play. Forced to World Conquer by PDX henchmen.

## Reply 101 — participant_058 · 2025-10-15 · post-30803159

<!-- artifact:quote:start -->
> KAMCITY13 said: Yeah true, Creative Assembly should take notes Click to expand...
<!-- artifact:quote:end -->
Unironically, in one of their dev threads, point them this way. Ping their social media manager as well, or whoever their Trin equivalent is, and just ask for a tech dev diary. Depending on how the company filters such things, it can be a win-win-win-win audience engagement thing. The designer devs don't have to write a diary for a week (freeing up time for them to focus), the tech-devs get to write for a week (getting to publicize their efforts and get more tailored technical feedback), the community manager gets a relatively easy audience-desire success (and not have to come up with something they hope will be engaging), and the community gets a format for raising implementation as opposed to vision questions (opportunities to raise what is, rather than what may be in the future). Any easy wins / low-hanging fruit from the tech engagement tends to come back to the designers, as the project as a whole gets a better reputation. I've worked with various developer teams in multiple formats (and, less directly, across multiple games), and audience / user requests for engagement on the tech side are usually something that makes sense from both ends. People tend to be interested in talking about their work to an interested audience, and as long as the forum format isn't toxic, it's an easy win that can support fan interests and gives the tech devs an easy metric of success for their own internal admin purposes.

## Reply 102 — participant_010 · 2025-10-15 · post-30803182

<!-- artifact:quote:start -->
> pengoyo said: Great job! More of a modding performance question: for character interactions, are is_shown and ai_potential done in parallel? If not, which one is done before the other? I don't think the order of trigger evaluation in a script is documented anywhere. It would be a nice addition for modders Click to expand...
<!-- artifact:quote:end -->
TL;DR - Always always be as restrictive as you can with ai_potential (or the AUH replacement is_available) since that is a trigger we check early before we even evaluate target list building. Character interactions is a bit of an ever-evolving feature constantly getting extra sub-features and support so it's a bit tricky to document something that would always be true here. I'll do a list here of a quick glance at the code for the current iteration of the related code: * AI-frequency-filtering * is_available/ai_potential trigger with only the actor scope * build & filter target list * ai_target_quick_trigger for the actor/recipient combo * randomly shrink target list to fit ai_target:max * randomly exclude target by ai_target:chance * check if interaction is pending for actor/recipient combo * check cooldown for actor/recipient combo * check diplo range for actor/recipient combo * is_shown trigger for actor/recipient scope * is_valid_showing_only_failures for actor/recipient scope * is_valid for actor/recipient scope * setup secondaries (titles/artifacts/characters) * sanitycheck that all required targets exist * check if interaction is pending for actor/recipient combo * can_send for full scope * decide interaction option picks and evaluate recipient acceptance and auto acceptance If all of this passes then the AI can consider sending this interaction. With my glance I've probably also missed a few steps or missed to add details which makes some of these steps optional based on configurations.

## Reply 103 — participant_010 · 2025-10-15 · post-30803196

<!-- artifact:quote:start -->
> pengoyo said: Would it be possible to have any character controlled by a player have their normal update date be changed to being the 1st of the month? This shouldn't affect performance much (even in multiplayer) as most characters are still evenly spread across the month. Just makes it easier as the player to know what date you have to wait for if you really need that extra monthly tick of gold, prestige, or etc Click to expand...
<!-- artifact:quote:end -->
We have plenty of updates which are at several different offsets for each character even if the main idea is use some modulo of the character ID for spreading out the updates. One of our design ideas is also to have an event pacing that isn't going to hit you with several events at the very same game date so that part we do like and will likely not change. However I think I understand your idea as mainly being special player character handling for monthly income calculations? That may actually be more doable to do special handling. However without digging into it further I can't say if we would be able to avoid some late filtering out of player characters to avoid getting double income ticks - and such filtering would unfortunately have some performance impact. Could be something for us to look into at least.

## Reply 104 — participant_010 · 2025-10-15 · post-30803200

<!-- artifact:quote:start -->
> Evilcake911 said: Long time forum lurker here, this amazing dev diary has forced me to comment and congratulate the devs on a job well done! I really love the tier-based AI frequency but wonder if it can be taken a step further. A common playthrough of CK consists of going from count to emperor and at each stage the characters which matter to me are different. As a count, the most interesting characters I interact with are my top liege (the duke), fellow vassals of my duke and my direct vassals (barons). As I tier up, this changes so that my top liege is now the king, I compete with fellow dukes and have counts as my direct vassals etc. I think the AI frequency should depend further on my current title, so that these cast of characters I see often have more AI updates (and ideally have a more complex AI to interact with me) so that there's more emergent story telling. CK3 has long had an issue of other characters not mattering and this should fix that, so that at every game stage early, mid and late there's important characters leaving a memorable mark in my playthrough. With the current system, as a count my barons will be quite useless. Click to expand...
<!-- artifact:quote:end -->
Interesting idea. : ) We don't really do anything at this detailed level - however we have something somewhat related. For performance reasons as we've explained earlier we do certain frequency gating on several mechanics. But related to your idea we do take some extra care of the realm that the player is acting inside and we then make sure that we increase the frequency for certain UI/AI related logic in specifically the player's top-realm.

## Reply 105 — participant_059 · 2025-10-15 · post-30803204

I know this isn't really the processing performance of the game, but the number 1 thing that slows my game down is the annoying and meaningless events that pop up in my face that I either feel obligated to read (and get itritated by) or that I feel guilty about ignoring and clicking a random option so I can get back to the actual game. (But super happy about the processing speed updates)

## Reply 106 — participant_048 · 2025-10-15 · post-30803208

<!-- artifact:quote:start -->
> James Daff said: How deep is the chronological implementation of titles and characters? In the history of Asian states, we encounter origins that stretch deep into antiquity. Will B.C.E. (or B.C.) years finally be added to the timeline, or will we see something similar to the Roman Empire, where Emperor Octavian Augustus is represented as a child and the title doesn't start until the beginning of the Common Era (C.E.)? In that case, the game's history will lose a huge number of great rulers, and many dynasties in Asia will be 'truncated,' meaning the Emperors of China and Japan won't have titles stretching back into B.C.E. years as they do in real history. I have also heard many tall tales that the code does not support B.C.E. years and that this allegedly causes problems, but this is only a half-truth, because it reliably supports history files. I myself can't remember how many times I've used B.C.E. years for my bookmark mod (oh yes, a huge number of times), and it works absolutely fine. In short, I would like to hear any news regarding this from you guys. Click to expand...
<!-- artifact:quote:end -->
I really appreciate your work, but even if everything remains the same, I would still like to get any kind of answer from you to my question.

## Reply 107 — participant_010 · 2025-10-15 · post-30803215

<!-- artifact:quote:start -->
> CivMasters said: A Dev condemned to play. Forced to World Conquer by PDX henchmen. Click to expand...
<!-- artifact:quote:end -->
Haha RIP me when that responsibility would fall on me. I'm so bad at world conquests and mainly sit there micro-managing my small demesne grooming(/murdering) my heirs.

## Reply 108 — participant_010 · 2025-10-16 · post-30803220

<!-- artifact:quote:start -->
> James Daff said: How deep is the chronological implementation of titles and characters? In the history of Asian states, we encounter origins that stretch deep into antiquity. Will B.C.E. (or B.C.) years finally be added to the timeline, or will we see something similar to the Roman Empire, where Emperor Octavian Augustus is represented as a child and the title doesn't start until the beginning of the Common Era (C.E.)? In that case, the game's history will lose a huge number of great rulers, and many dynasties in Asia will be 'truncated,' meaning the Emperors of China and Japan won't have titles stretching back into B.C.E. years as they do in real history. I have also heard many tall tales that the code does not support B.C.E. years and that this allegedly causes problems, but this is only a half-truth, because it reliably supports history files. I myself can't remember how many times I've used B.C.E. years for my bookmark mod (oh yes, a huge number of times), and it works absolutely fine. In short, I would like to hear any news regarding this from you guys. Click to expand...
<!-- artifact:quote:end -->
The earliest entry I see for the Chinese Empire title is 25.8.5. I think we mainly resorted to CE due to the scale of the history setup and not having to bother with the UI potentially being hard to read with including BCE dates. I'm not the best at answering our decisions we made there but I'll let them know to possibly chime in with more details around this.

## Reply 109 — participant_048 · 2025-10-16 · post-30803228

<!-- artifact:quote:start -->
> Divine said: The earliest entry I see for the Chinese Empire title is 25.8.5. I think we mainly resorted to CE due to the scale of the history setup and not having to bother with the UI potentially being hard to read with including BCE dates. I'm not the best at answering our decisions we made there but I'll let them know to possibly chime in with more details around this. Click to expand...
<!-- artifact:quote:end -->
Yes, letting them know would be great.

## Reply 110 — participant_010 · 2025-10-16 · post-30803239

<!-- artifact:quote:start -->
> rasuuru said: How do you parse the scripts? One time I made simple parser and found several missing curly braces in common/genes and a such a line somewhere: value = 10'(note the single quote). Click to expand...
<!-- artifact:quote:end -->
Unfortunately it really depends on what area of the script you are in. There's a base concept of our parser to read 3 tokens which most commonly gives us easy parsing for assignments similar to stewardship >= 10. In the vast majority of our script we base our parsing around the principle that objects are defined with an ID and confined within curly brackets waterworks_07 = { ... }. Each object then usually contains several attributes which are then assigned within the curly bracket enclosed block. However while this is true for 95%+ of the script in the game we do have the power to customize and handroll the input from our parser for special syntax handling. Which we do in several places so the main principle is only going to get you the majority of the way. The missing curly braces or the single quote may or may not pose actual problems which fails to register for any of our error-handling. Hard to tell without inspecting the actual file/debugging the parsing. I'm more suspicious of the missing brackets however. The single quote probably won't block us from properly interpreting the correct number 10.

## Reply 111 — participant_010 · 2025-10-16 · post-30803254

<!-- artifact:quote:start -->
> Weyird said: I know this isn't really the processing performance of the game, but the number 1 thing that slows my game down is the annoying and meaningless events that pop up in my face that I either feel obligated to read (and get itritated by) or that I feel guilty about ignoring and clicking a random option so I can get back to the actual game. (But super happy about the processing speed updates) Click to expand...
<!-- artifact:quote:end -->
Our designers are balancing event pacing every now and then. Please make sure to let them know in discussions (or the bug forum for severe imbalances) if you have any particular event or group of events that you feel is especially inconsequential/frequent. This info is helpful for them to either take a look at the effects or frequency weightings. : )

## Reply 112 — participant_057 · 2025-10-16 · post-30803269

<!-- artifact:quote:start -->
> Marusama said: "Feature steward"? Does this mean that there are plans to integrate DLC features together, or to add new features to old systems which were implemented after release? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Divine said: Feature stewards is a team-internal way of structuring decision making for what's important for the implementation of the features during dlc development. : ) Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> ourg said: I hope you've fixed all the bugs of administrative successions in the process ? - Wrong succession line for unasigned themes dispalyed on the UI - Possibility to spend influence on unasigned themes that are actually not handled in apointement succession (works like primogeniture) and are always innerited by the emperor/king heir - The player heir is buged when your primary heir is from your dynasty but not from your house, resulting loosing all your estate on succession etc.... And concerning performance did you fix the performance bug on decision UI with the fixedgridbox ? Click to expand...
<!-- artifact:quote:end -->
Is there anyone checking for opportunities to add new content to old DLC when factoring new content? In Cities: Skylines 1, for an example, when DLC adds a new transportation method (i.e. Trams), it is usual that previous DLC receive new content with interactions for that content (i.e. a road with both Tram tracks and cycling lanes for owners of After Dark DLC, which added cycling). See this patch note for an actual example. CK3 is so great in scope that I see opportunities for additional content with many DLC. The ever growing complexity of the most recent DLC overshadows some of the previous, and make them look like bad value, in comparison. Also, it is nice to throw a bone at people supporting you for so long. This can also help amend terrible DLC, like coronations. Are there bug reports for these?

## Reply 113 — participant_056 · 2025-10-16 · post-30803300

<!-- artifact:quote:start -->
> Divine said: Interesting idea. : ) We don't really do anything at this detailed level - however we have something somewhat related. For performance reasons as we've explained earlier we do certain frequency gating on several mechanics. But related to your idea we do take some extra care of the realm that the player is acting inside and we then make sure that we increase the frequency for certain UI/AI related logic in specifically the player's top-realm. Click to expand...
<!-- artifact:quote:end -->
Thanks for the insight, perhaps the dev team that work on enhancing AI for characters "close" to the player (liege, fellow vassals, direct vassals etc.). I don't think anyone would mind what the duke of Iceland is doing while playing in China but characters that I see frequently should be trying to murder me, thwarting my plans and generally competing with me (based on their personality traits of course). This would provide a good middle ground of performance and a more alive game world.

## Reply 114 — participant_060 · 2025-10-16 · post-30803333

Personally, I would get rid of barons and their families and have placeholder art/buffs to represent them I bet that would improve performance a greatly

## Reply 115 — participant_030 · 2025-10-16 · post-30803381

<!-- artifact:quote:start -->
> Divine said: Amount of baronies/landed provinces should be increased by around 32% in the AUH map compared to the previous patch. Click to expand...
<!-- artifact:quote:end -->
Thank you for your response. However, what I wanted to know was the province number in definition.csv, etc.

## Reply 116 — participant_061 · 2025-10-16 · post-30803433

I think the CK3 dev diaries are required reading for anyone who is interested in any aspect of game design. Either every team member is a master communicator or the team processes bring it out of everyone. Each one goes into impressive detail while still being accessible to even many children, especially those who are already interested in game design. Code optimisation is also something that rarely gets touched upon, as it's not as cool - the last time I recall reading something about it was Syndicate, where the programmer behind the Amiga port was excited because he had improved optimisation by 20%. I've learned a lot from this one, especially the way multiple cores are used. RAM optimisations will definitely benefit parallel calculations which are stored in memory for older computers. People who are wanting to explore scripting for mods but don't know where to start can also use this as a start point and I assume quite a few have started to consider how they could possibly enhance game performance using scripts.

## Reply 117 — participant_016 · 2025-10-16 · post-30803490

Im a bit late with this but i heard no one asked about it before - did you do anything with house power calculations? Calculating it for each character in realm even if they're of the same house is quite wasteful. also also expose the funny influence modifier per rulers of your house in same realm to modders at least a bit pleaseee, i really wanna cut it down but i cant!

## Reply 118 — participant_050 · 2025-10-16 · post-30803495

<!-- artifact:quote:start -->
> Divine said: Our designers are balancing event pacing every now and then. Please make sure to let them know in discussions (or the bug forum for severe imbalances) if you have any particular event or group of events that you feel is especially inconsequential/frequent. This info is helpful for them to either take a look at the effects or frequency weightings. : ) Click to expand...
<!-- artifact:quote:end -->
Personally, I've always been bothered by the following events and their display as massive pop-ups, which typically only allow one choice: - 1) Murder schemes ("A Scheme at Court"), specifically, when I'm notified for some reason that some random guest is trying to kill another random guest. This doesn't happen often at the beginning of the game, but when the royal or imperial court appears, I can get up to five such events per month. I'd like these events to be displayed as massive pop-ups only if they affect the player character and their immediate family. - 2) The same applies to the events in the "A Snake at Court" series: I don't quite understand why the player should care if some random guest, or even a courtier, tries to seduce another guest or courtier. At the very least, it certainly shouldn't be displayed as a massive pop-up, unless, of course, it affects character and their immediate family. - 3) Marriage Accepted Letter: annoying when marrying off many courtiers at once. - 4) Conditions for Release Accepted Letter: You know beforehand whether a prisoner will accept your conditions; in fact, you can't release them if they won't. So why a pop-up saying they did? Annoying when mass releasing from a dungeon. - 5) And the most "tasty": the events "The Scandal" and "Out of Wedlock" - in 99% of cases, both trigger simultaneously and affect all characters; their number in the late game is simply off the charts. This seems even stranger if the religion doesn't consider adultery a crime. And even stranger when this event affects low-born characters. But I'd also like to reduce the overall frequency of events, especially the following series: - 1) Events involving wet nurses: No, seriously, they're so frequent that I've already made a fortune just selling my children's teeth. - 2) Minor epidemics: In most cases, I get a message from the doctor that "urgent action is necessary," but the epidemic itself ultimately doesn't even affect my lands. This isn't much of a concern for the 900-1000 year period, but later, when land development reaches very high levels, this event pops up very frequently. While minor epidemics generally don't have any negative effects, the constant massive pop-up notifications are annoying. - 3) Travel events, especially from the "Wandering Nobles" DLC: there are also a lot of them and they're constantly repeating. On the one hand, it's annoying, on the other, they create balance problems; if you really want to, you can abuse them so much that you can get several thousand free levies, a dozen excellent knights, and if you're lucky with the thief event, a lot of money and dread in a measly 10-15 years. - 4) The AI invites you to join a confederation. When playing as a tribe, I consistently receive this invitation every 1-3 years from each neighbor. This is too frequent. Need to either reduce the AI's propensity to invite players to join a confederation, or add an option to simply remove this option at the player's discretion. There used to be mods that fixed this, but most are either outdated and don't work, work poorly, or conflict heavily with other mods. For example, these mods: Steam Workshop::Less Event Spam [Crown Update] steamcommunity.com Steam Workshop::Less Event Spam: Affairs & Bastards 1.12.x steamcommunity.com Steam Workshop::Less Frequent Events steamcommunity.com

## Reply 119 — participant_062 · 2025-10-16 · post-30803516

Glad you were able to keep performance stable without having to resort to drastic measures, like the infamous "turn off Baron AI" fix that came with Rajas of India for CK2.

## Reply 120 — participant_063 · 2025-10-16 · post-30803618

<!-- artifact:quote:start -->
> James Daff said: How deep is the chronological implementation of titles and characters? In the history of Asian states, we encounter origins that stretch deep into antiquity. Will B.C.E. (or B.C.) years finally be added to the timeline, or will we see something similar to the Roman Empire, where Emperor Octavian Augustus is represented as a child and the title doesn't start until the beginning of the Common Era (C.E.)? In that case, the game's history will lose a huge number of great rulers, and many dynasties in Asia will be 'truncated,' meaning the Emperors of China and Japan won't have titles stretching back into B.C.E. years as they do in real history. I have also heard many tall tales that the code does not support B.C.E. years and that this allegedly causes problems, but this is only a half-truth, because it reliably supports history files. I myself can't remember how many times I've used B.C.E. years for my bookmark mod (oh yes, a huge number of times), and it works absolutely fine. In short, I would like to hear any news regarding this from you guys. Click to expand...
<!-- artifact:quote:end -->
BCE dates can be made functional from a modding perspective, but are not currently supported internally to the extent necessary for release or even internal developmental purposes, because the game errors extensively when attempting to validate parent-child relationships with negative dates, resulting in an explosion of errors that parents have not yet been born at the time of their child's birth. The presence of errors like this may be able to be "safely" ignored from a modding perspective, but are not acceptable as part of the development process or a commercial release. This was something we had hoped to have time to look at in the course of AUH's development, but the scope of the expansion resulted in tasks more critical to the success and core functionality of the release having to take precedence, especially with the amount of time we've spent on performance optimization. We still plan to investigate further into what would be needed to make this fully supported, but for release the title histories will only be able to go back as far as the Roman history does now.

## Reply 121 — participant_048 · 2025-10-16 · post-30803621

<!-- artifact:quote:start -->
> Cordelion said: BCE dates can be made functional from a modding perspective, but are not currently supported internally to the extent necessary for release or even internal developmental purposes, because the game errors extensively when attempting to validate parent-child relationships with negative dates, resulting in an explosion of errors that parents have not yet been born at the time of their child's birth. The presence of errors like this may be able to be "safely" ignored from a modding perspective, but are not acceptable as part of the development process or a commercial release. This was something we had hoped to have time to look at in the course of AUH's development, but the scope of the expansion resulted in tasks more critical to the success and core functionality of the release having to take precedence, especially with the amount of time we've spent on performance optimization. We still plan to investigate further into what would be needed to make this fully supported, but for release the title histories will only be able to go back as far as the Roman history does now. Click to expand...
<!-- artifact:quote:end -->
Thank you for the timely response. Many of us are really hoping that a feature like this can be implemented in the future.

## Reply 122 — participant_017 · 2025-10-16 · post-30803627

<!-- artifact:quote:start -->
> Benismann said: Im a bit late with this but i heard no one asked about it before - did you do anything with house power calculations? Calculating it for each character in realm even if they're of the same house is quite wasteful. also also expose the funny influence modifier per rulers of your house in same realm to modders at least a bit pleaseee, i really wanna cut it down but i cant! Click to expand...
<!-- artifact:quote:end -->
That's not how house power system works. Can you describe an experiment that can confirm your findings? Where do you observe that perceived repeated calculation for every character?

## Reply 123 — participant_017 · 2025-10-16 · post-30803651

<!-- artifact:quote:start -->
> DeanTheDull said: By extension, should this also apply to the elective stalls when opining the candidate lists? Click to expand...
<!-- artifact:quote:end -->
No changes to elections

## Reply 124 — participant_064 · 2025-10-16 · post-30803712

<!-- artifact:quote:start -->
> ArpoMo6 said: Personally, I've always been bothered by the following events and their display as massive pop-ups, which typically only allow one choice: Click to expand...
<!-- artifact:quote:end -->
Agree with your list, especially A Scheme at Court and A Snake at Court (which shouldn't even be allowed to fire while I'm traveling). I'd also like to add the "name a dynasty member" popup. I know this was added post-1.0 by request, but I literally don't care what name random unlanded nobodys of my dynasty hanging around my court have (or even my nieces and nephews to be honest, I always have a large dynasty). Once I'm on my third ruler, I start seeing this popup maybe 30 times an hour which is a lot for campaigns that last well over 50 hours. Give me the option to only name my direct kids and let everyone else figure it out themselves. I'm not going to interact with 90% of those characters anyway.

## Reply 125 — participant_065 · 2025-10-16 · post-30803742

Late to the party but these are some things that I see on a very regular basis as I try to squash major bugs in my sandbox and help out with a major bug fixing mod, they affect the stability of the game and pollute the error log with thousands of lines of error reporting that make it hard to find useful information in the logs and also, given that writing to the logs must take cpu cycles and i/o cycles must be a candidate for performance enhancements tooltipping errors related to yet to be created/defined variables, scopes, objects, etc. You gave us a band aid with hidden_effect_new_object which I find myself spamming throughout script but are unfortunately not usable in triggers due to it being a effect. Is it not possible to address this tooltipping issue, perhaps turning off future evaluation in some way? schemes with no owner or target are increasing since 1.13, it is not possible to start a scheme without an owner so something is happening somewhere that is nuking the owner/target. I have squashed most of this by adding exists gates for owner and target in the scheme's valid trigger but that is only ending the schemes, so effectively hiding the problem not resolving it. task contracts with no owner, target or scheme, for this you can refer to what I said about schemes Seriously when those errors occur they spam the error log with thousands upon thousands of junk and hide the other more useful/informative errors and as I said, must have an impact on performance.

## Reply 126 — participant_066 · 2025-10-16 · post-30803770

It being about the same is pretty disappointing. Performance is atrocious as is. So if it's still going to be atrocious after being improved, that's a big mark against the DLC. Really should have included an option to remove parts of the world to actually get performances that's somewhat less terrible. Really hope there will be further improvements soon.

## Reply 127 — participant_017 · 2025-10-16 · post-30803873

<!-- artifact:quote:start -->
> A lowborn Emperor said: Tooltipping errors related to yet to be created/defined variables, scopes, objects, etc. You gave us a band aid with hidden_effect_new_object which I find myself spamming throughout script but are unfortunately not usable in triggers due to it being a effect. Is it not possible to address this tooltipping issue, perhaps turning off future evaluation in some way? Click to expand...
<!-- artifact:quote:end -->
Okay, I'll need more details on that, please. Assume I know nothing of the issue, and guide me through it step by step. Are you tooltipping the errors, or are there errors in tooltips? What exactly are you trying to achieve and what does/doesn't work? I would like to have those illegal schemes and contracts be fixed as well. Unfortunately, bugs have priorities, and it looks like these 2 were considered non-critical. Maybe some day.

## Reply 128 — participant_065 · 2025-10-16 · post-30804111

<!-- artifact:quote:start -->
> Alien-47 said: Okay, I'll need more details on that, please. Assume I know nothing of the issue, and guide me through it step by step. Are you tooltipping the errors, or are there errors in tooltips? What exactly are you trying to achieve and what does/doesn't work? I would like to have those illegal schemes and contracts be fixed as well. Unfortunately, bugs have priorities, and it looks like these 2 were considered non-critical. Maybe some day. Click to expand...
<!-- artifact:quote:end -->
Shame they are classed as non critical, considering they make up so much of the interactive game content, so when the owner/target mysteriously disappear the whole interaction sequence becomes void and in some cases the outcome event/effect does not check for values that would have been set in the schemes, so they just give a positive outcome to the players. But no problem, I'll just stick to invalidating the schemes with the valid trigger in my sandbox so they silently fail instead of flooding my error log. As for the tooltipping problem. This is an example In fund_inspiration.1061 and fund_inspiration.1071 I had to wrap the whole IF ladder in a hidden_effect_new_object to clear the error spam Code: # throws error # Script system error! (while building tooltip/description) # Error: Undefined event target 'newly_created_artifact' hidden_effect_new_object = { # Add a dedication to the description - fund_inspiration.7001 if = { limit = { scope:inspiration_owner = { has_variable = artifact_dedication_a_var } } scope:inspiration_owner = { var:artifact_dedication_a_var = { save_scope_as = dedication_a } } scope:newly_created_artifact = { set_artifact_description = artifact_dedication_inscribed_a } } else_if = { limit = { scope:inspiration_owner = { has_variable = artifact_dedication_b_var } } scope:inspiration_owner = { var:artifact_dedication_b_var = { save_scope_as = dedication_b } } scope:newly_created_artifact = { set_artifact_description = artifact_dedication_inscribed_b } } Or ep3_laamps.5005 I had to wrap the nickname assignment in a hidden_effect_new_object Code: # Plus give 'em a nickname. # throws Script system error! (while building tooltip/description) # throws Error: untyped trigger [ Scoped object of type 'character' is not valid (null weak (Character - 4294967295)!) ] hidden_effect_new_object = { scope:priest = { assign_random_nickname_effect = yes } } And in triggers I can't use hidden_effect_new_object so have to use exists, such as in adultery_0001_unfaithful_trigger Code: any_secret = { secret_type = secret_lover # Script system error! (while building tooltip/description) # Error: Event target link 'secret_target' returned an unset scope # # This spews out nearly a thousand errors and that was with a very short game run # Can't use hidden_effect_new_object because this scripted trigger is used in the event's trigger # tried to fix with ?= which didn't work, so now trying with exists exists = secret_target secret_target = {

## Reply 129 — participant_007 · 2025-10-16 · post-30804154

<!-- artifact:quote:start -->
> CivMasters said: Are there bug reports for these? Click to expand...
<!-- artifact:quote:end -->
Yes for a long time. But Bug forum section is a no paradox staff member's land

## Reply 130 — participant_067 · 2025-10-16 · post-30804582

A return to pre-Khans of the Steppe performance would be the ideal, but I guess considering a >30% bigger map, even parity to previous performance levels is an admirable achievement.

## Reply 131 — participant_068 · 2025-10-16 · post-30804748

<!-- artifact:quote:start -->
> Presedentex201 said: Personally, I would get rid of barons and their families and have placeholder art/buffs to represent them I bet that would improve performance a greatly Click to expand...
<!-- artifact:quote:end -->
I was also wondering if something like this was possible. Alternatively a game rule setting which would let you limit the Barons to tend towards a specific count of influential/powerful barons as "relevant" (Sorta like how adventurers can be limited to 25-200 currently) and have rest be "minor barons" with dummy AI.

## Reply 132 — participant_069 · 2025-10-16 · post-30804777

Well, if anyone is interest in late-game lags or freezing... this mod is must have: https://steamcommunity.com/sharedfiles/filedetails/?id=2276469612. Just right at the game start I use it as decision, just one click and that's it. It will even help you in the middle of gameplay.

## Reply 133 — participant_007 · 2025-10-16 · post-30805002

As I've already said in the past. There is a lot of characters created just for event that are not deleted after with death and vanish reason, which populate the character pool. They doesn't really use actions but take some memory.

## Reply 134 — participant_069 · 2025-10-16 · post-30805013

<!-- artifact:quote:start -->
> ourg said: As I've already said in the past. There is a lot of characters created just for event that are not deleted after with death and vanish reason, which populate the character pool. They doesn't really use actions but take some memory. Click to expand...
<!-- artifact:quote:end -->
Well, I sometimes try to get them to my court. In the events we can meet interesting persons.

## Reply 135 — participant_037 · 2025-10-16 · post-30805035

<!-- artifact:quote:start -->
> XtoraX said: I was also wondering if something like this was possible. Alternatively a game rule setting which would let you limit the Barons to tend towards a specific count of influential/powerful barons as "relevant" (Sorta like how adventurers can be limited to 25-200 currently) and have rest be "minor barons" with dummy AI. Click to expand...
<!-- artifact:quote:end -->
Yeah, honestly I kinda struggle to see the point of barons in CK3? They don't do anything, they never even really matter for internal politics or factions, they just seem to exist to take up space and processing power. When was the last time that anyone had a baron do anything substantive that wouldn't be done just as effectively by a landless courtier or adventurer? Legitimately curious because barons are pretty much invisible to me in my playthroughs.

## Reply 136 — participant_070 · 2025-10-16 · post-30805048

<!-- artifact:quote:start -->
> kouccarter said: Well, if anyone is interest in late-game lags or freezing... this mod is must have: https://steamcommunity.com/sharedfiles/filedetails/?id=2276469612. Just right at the game start I use it as decision, just one click and that's it. It will even help you in the middle of gameplay. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Divine said: Eliminating Stray Nobodies One of the more commonly used mods out there to make the game faster is the “Population Control” mod - which starts eliminating people when the world’s population reaches a certain number. Now we haven’t done something exactly like that, but we have tried to combat the underlying issue: we accumulate characters that don’t do much - and after a couple of hundred years these can count in the tens of thousands. So we went and reduced or eliminated a bunch of ‘sources’ of characters that generate boring, useless, random or invisible characters that then linger in guest pools, the sidelines of courts of barons and counts, and that take up space and cost performance. At the same time we keep the more interesting characters that have a bit of history around longer, and we draw them into events more, often replacing a randomly generated nobody. This allowed us to trim the useless fat that accumulates in long-running games, reducing the strain that even relatively light non-ruler characters leave on the simulation systems. Click to expand...
<!-- artifact:quote:end -->
You may want to read this part of the dev diary again:

## Reply 137 — participant_069 · 2025-10-16 · post-30805101

<!-- artifact:quote:start -->
> Granty said: You may want to read this part of the dev diary again: Click to expand...
<!-- artifact:quote:end -->
I am sorry. My mistake. I somehow missed it.

## Reply 138 — participant_030 · 2025-10-17 · post-30805506

It's always great when officially useful mods get the equivalent of official treatment. It's good that mods can solve problems, but managing countless mods is a pain.

## Reply 139 — participant_071 · 2025-10-17 · post-30805726

<!-- artifact:quote:start -->
> Kapi96 said: It being about the same is pretty disappointing. Performance is atrocious as is. So if it's still going to be atrocious after being improved, that's a big mark against the DLC. Really should have included an option to remove parts of the world to actually get performances that's somewhat less terrible. Really hope there will be further improvements soon. Click to expand...
<!-- artifact:quote:end -->
You could get a mod that removes the new landmass and gain an enormous amount of performance compared to now I bet. Don't forget, it's roughly the same performance with a 33% increase in locations and characters.

## Reply 140 — participant_072 · 2025-10-17 · post-30806224

<!-- artifact:quote:start -->
> Kapi96 said: Really should have included an option to remove parts of the world Click to expand...
<!-- artifact:quote:end -->
There is literally no reason for Paradox to do that (actually pretty big, if you want it to work well and be smoothly integrated) pile of work, when modders will provide "No East Asia" mods within a week or two of the DLC release just like they already provide "No India" mods.

## Reply 141 — participant_073 · 2025-10-17 · post-30806812

this is just a joke. but it would be nice if the Mongol Empire could be Hegemony even if it only lasted for a while. because the Mongol Empire had a huge impact on the entire Eurasian history. numerous dynasties and empires fell, making way for new ones. During the peace of the Mongol Empire, many technologies/concepts traveled along the Silk Road. The Mongol Empire inspired many other conquerors. etc. + I believe the Yuan Dynasty is a Hegemony, so if the Mongols conquer China, will the world be without any Hegemony? Or would it be better for the Mongols to be temporarily Hegemony until the Yuan Dynasty re-establishes Chinese Hegemony. If the basis of Hegemony is to be a state that has influence over all the states around it, I believe that the Mongol Empire should be a Hegemony. I appreciate everything that Paradox is adding to the game with this DLC and if Mongol Hegemony doesn't fit the theme I understand that.

## Reply 142 — participant_016 · 2025-10-17 · post-30806908

<!-- artifact:quote:start -->
> KalevaTietäjäKuningas said: even if it only lasted for a while Click to expand...
<!-- artifact:quote:end -->
But the whole point of hegemonies is that they lasted quite a while...

## Reply 143 — participant_073 · 2025-10-17 · post-30806932

<!-- artifact:quote:start -->
> Benismann said: But the whole point of hegemonies is that they laster quite a while... Click to expand...
<!-- artifact:quote:end -->
The Mongol Empire lasted only a short time, but its consequences have lasted for centuries to this day. numerous dynasties and empires fell, making way for new ones. During the peace of the Mongol Empire, many technologies/concepts traveled along the Silk Road. The Mongol Empire inspired many other conquerors. etc. + I believe the Yuan Dynasty is a Hegemony, so if the Mongols conquer China, will the world be without any Hegemony? Or would it be better for the Mongols to be temporarily Hegemony until the Yuan Dynasty re-establishes Chinese Hegemony.

## Reply 144 — participant_050 · 2025-10-18 · post-30807658

<!-- artifact:quote:start -->
> TripleAgent said: Yeah, honestly I kinda struggle to see the point of barons in CK3? They don't do anything, they never even really matter for internal politics or factions, they just seem to exist to take up space and processing power. When was the last time that anyone had a baron do anything substantive that wouldn't be done just as effectively by a landless courtier or adventurer? Legitimately curious because barons are pretty much invisible to me in my playthroughs. Click to expand...
<!-- artifact:quote:end -->
I agree. We have a rather strange, clearly simplified system in which, for some reason, exactly one priest governs all the temples, but at the same time, there's a separate baronial system, in which one baron governs one city. Perhaps we should unify these governance systems and give one baron the power to govern all cities (we'll consider him a representative of the barons/cities). At the same time, we could add another council seat with its own special features and tasks specifically for barons, if desired. This would reduce the number of barons, especially in large powers and among rulers with many domains, while still retaining the barons and making them less faceless.

## Reply 145 — participant_074 · 2025-10-18 · post-30808321

Not sure I agree. Barons do provide the majority of your Council Positions and Court Positions too. I would hate to see that utility taken away...

## Reply 146 — participant_053 · 2025-10-18 · post-30808480

<!-- artifact:quote:start -->
> Divine said: We have plenty of updates which are at several different offsets for each character even if the main idea is use some modulo of the character ID for spreading out the updates. One of our design ideas is also to have an event pacing that isn't going to hit you with several events at the very same game date so that part we do like and will likely not change. However I think I understand your idea as mainly being special player character handling for monthly income calculations? That may actually be more doable to do special handling. However without digging into it further I can't say if we would be able to avoid some late filtering out of player characters to avoid getting double income ticks - and such filtering would unfortunately have some performance impact. Could be something for us to look into at least. Click to expand...
<!-- artifact:quote:end -->
Yeah, I'm not talking about when events fires and other background processes. More like stuff the UI shows the player are happening each and every month and thus sometimes you the player are waiting for the monthly tick on it So having the various currency numbers on the top right of the screen update the same time of the month regardless of which character you are playing (or started date, IIRC some of them currently change based on start date) would be much appreciated. But totally understand it might not be feasible. Thanks for looking into it

## Reply 147 — participant_075 · 2025-10-18 · post-30808594

Hello! I wonder when the effects.log and triggers.log will be posted? Thank you!

## Reply 148 — participant_013 · 2025-10-19 · post-30810355

<!-- artifact:quote:start -->
> Benismann said: But the whole point of hegemonies is that they lasted quite a while... Click to expand...
<!-- artifact:quote:end -->
is it? Because India wasn't unified until Mughals came in 1500s so in CK3 timespan it lasted exactly 0 years. Devs seem to be okay with accepting alternate history for the hegemonies, so why not something that actually existed for few decades? Inb4 "but it existed, only later!", yeah, but if that's an argument then where are British, French and Spanish hegemonies? India got it's hegemony because of geographical convenience, and the same should apply to Great Steppe.

## Reply 149 — participant_076 · 2025-10-20 · post-30811342

The bigger problem with performance is that Barons should probably not even exist in this game. All of the restrictions on game mechanics to Barons make them irrelevant. The density of the map is way too high, leading to much of one's player court character's doing absolutely nothing. If Barons only check for their build queue once per 3 years, does this mean if I gift a baron money they will not bother starting construction until 3 years later? This will make it so that players have to only have dukes in order to actually develop their countries, and AI countries will fall even further behind vs players even if the player decides to gift those characters money. There also needs to be a way to increase the calculation frequency per character from once per month to much higher for notable characters vis a vis the player. Again the sandbox just feels way too dead right now.

## Reply 150 — participant_016 · 2025-10-20 · post-30811381

<!-- artifact:quote:start -->
> Limith said: Why do barons not bother to fill their council when a player can, this creates an uneven advantage for the user. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Divine said: Barons don’t have councils or court positions, yet they were still evaluating all of them; Click to expand...
<!-- artifact:quote:end -->
I suggest you re-read the whole Lessons from System-Level Optimizations part, barons seem to not be that heavy to begin with.

## Reply 151 — participant_071 · 2025-10-20 · post-30811485

<!-- artifact:quote:start -->
> Limith said: The bigger problem with performance is that Barons should probably not even exist in this game. All of the restrictions on game mechanics to Barons make them irrelevant. The density of the map is way too high, leading to much of one's player court character's doing absolutely nothing. If Barons only check for their build queue once per 3 years, does this mean if I gift a baron money they will not bother starting construction until 3 years later? This will make it so that players have to only have dukes in order to actually develop their countries, and AI countries will fall even further behind vs players even if the player decides to gift those characters money. Why do barons not bother to fill their council when a player can, this creates an uneven advantage for the user. There also needs to be a way to increase the calculation frequency per character from once per month to much higher for notable characters vis a vis the player. Again the sandbox just feels way too dead right now. Click to expand...
<!-- artifact:quote:end -->
Are you perhaps confusing barons for counts?

## Reply 152 — participant_076 · 2025-10-20 · post-30811521

<!-- artifact:quote:start -->
> Benismann said: I suggest you re-read the whole Lessons from System-Level Optimizations part, barons seem to not be that heavy to begin with. Click to expand...
<!-- artifact:quote:end -->
Cause they do nothing supposedly which then reinforces why are they even there if they do nothing

## Reply 153 — participant_076 · 2025-10-20 · post-30811522

<!-- artifact:quote:start -->
> Duchy-2 said: Are you perhaps confusing barons for counts? Click to expand...
<!-- artifact:quote:end -->
Ah yes you are right. Though counts also barely do anything either but that's not in the dev diary but only visible in the codebase.

## Reply 154 — participant_077 · 2025-10-30 · post-30833777

Turns out there's a huge performance oversight - AMD GPU Linux + Mac users (which also means Vulkan users) are seeing extremely low frame rates. Kudos on keeping the tick rate from dying horribly, but 7900 and 9070 GPUs should not be struggling to render this game

