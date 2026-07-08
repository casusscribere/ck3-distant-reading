---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1484301/"
forum_thread_id: 1484301
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "Anatomy of a Game: Simulation Optimization"
dd_date: 2021-07-29
author_handle: blackninja9939
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 5096
inline_image_count: 12
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1484301'
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
    location: raw_lines_~28_to_116
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_118_to_119
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_422_to_425
    action: preserved_and_flagged
    counts:
      Like: 46
      (unlabeled — rendered as base64 data URI): 1
      Love: 18
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_487_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Anatomy of a Game: Simulation Optimization

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [Jul 29, 2021](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/)
- [2](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/page-2)
[Next](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/page-2)

1 of 2

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/page-2 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/?prdxDevPosts=1)

[![blackninja9939](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/s/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)

#### [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)

##### Former Senior Programmer - Crusader Kings 3

**99 Badges**

Aug 28, 2013

2.414

8.575

- ![BATTLETECH: Heavy Metal](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BTHvymtlicon.png "BATTLETECH: Heavy Metal")
- ![Hearts of Iron IV: Death or Dishonor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4DoD.png "Hearts of Iron IV: Death or Dishonor")
- ![Age of Wonders III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoW3_forum_badge.png "Age of Wonders III")
- ![Cities: Skylines - Green Cities](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSL_green_cities.png "Cities: Skylines - Green Cities")
- ![Cities: Skylines - Mass Transit](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CitiesSkylines_MassTransit_16x16.png "Cities: Skylines - Mass Transit")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Stellaris: Digital Anniversary Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/plantoid.png "Stellaris: Digital Anniversary Edition")
- ![Surviving Mars: Digital Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_DDE.png "Surviving Mars: Digital Deluxe Edition")
- ![BATTLETECH - Digital Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/battletech_Deluxe_icon.png "BATTLETECH - Digital Deluxe Edition")
- ![Cities: Skylines - Parklife](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSLParkLife.png "Cities: Skylines - Parklife")
- ![Cities: Skylines Industries](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/cslindustriesicon.jpg "Cities: Skylines Industries")
- ![BATTLETECH: Flashpoint](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BTFlashpoint.png "BATTLETECH: Flashpoint")
- ![Cities: Skylines - Snowfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/snowflake_16_4.png "Cities: Skylines - Snowfall")
- ![Cities: Skylines - Campus](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSLCampus.png "Cities: Skylines - Campus")
- ![BATTLETECH: Season pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BTUrbanwarfare.png "BATTLETECH: Season pass")
- ![Age of Wonders: Planetfall Season pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aowseasonpass.png "Age of Wonders: Planetfall Season pass")
- ![Age of Wonders: Planetfall - Revelations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoWrevelationsicon.png "Age of Wonders: Planetfall - Revelations")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Cities: Skylines Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/csldelux.png "Cities: Skylines Deluxe Edition")
- ![Hearts of Iron IV: No Step Back](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/NSB_forum_icon_16x16.png "Hearts of Iron IV: No Step Back")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Hearts of Iron IV: By Blood Alone](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BBA_forum_icon_16x16.png "Hearts of Iron IV: By Blood Alone")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Hearts of Iron IV: Battle for the Bosporus](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/bftb.png "Hearts of Iron IV: Battle for the Bosporus")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Island Bound](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/paib.png "Island Bound")
- ![Europa Universalis 4: Emperor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_emperor.png "Europa Universalis 4: Emperor")
- ![Empire of Sin](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eos-silver.png "Empire of Sin")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Imperator: Rome - Magna Graecia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MagnGraeciaIcon.png "Imperator: Rome - Magna Graecia")
- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")
- ![Crusader Kings II: Rajas of India](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_rajas_of_india_forumicon.png "Crusader Kings II: Rajas of India")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Europa Universalis IV: Rights of Man](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rom_forum_icon.png "Europa Universalis IV: Rights of Man")
- ![Europa Universalis IV: Cradle of Civilization](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EUIV_CoC.png "Europa Universalis IV: Cradle of Civilization")
- ![Stellaris: Synthetic Dawn](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Syn_dawn_forum_icon.png "Stellaris: Synthetic Dawn")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![BATTLETECH](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/battletech_standard.png "BATTLETECH")
- ![Europa Universalis IV: Mandate of Heaven](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/moh_forum_icon.png "Europa Universalis IV: Mandate of Heaven")
- ![Crusader Kings II: Monks and Mystics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/monksandmystics.png "Crusader Kings II: Monks and Mystics")
- ![Tyranny: Archon Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tyr_com.png "Tyranny: Archon Edition")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")
- ![Crusader Kings II: Reapers Due](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/reapers_due_forum_icon.png "Crusader Kings II: Reapers Due")
- ![Hearts of Iron IV: Colonel](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Col.png "Hearts of Iron IV: Colonel")
- ![Stellaris Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Stellaris_SignUp_icon.png "Stellaris Sign-up")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")

[](javascript:;)

- [Jul 29, 2021](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/post-27703648)


- [/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/post-27703648](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/post-27703648)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27703648/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-simulation-optimization.1484301/post-27703648)

Hello everyone and welcome back to Anatomy of a Game, I’m Matthew a programmer on Crusader Kings 3 and today I am going to be talking about some optimisations I’ve done for 1.5 to put some of the higher level examples we’ve shown off in the previous two posts in a more concrete context.  

I’ve cherry picked these examples to show off a variety of different optimisation techniques and areas to apply to. None of them alone is a groundbreaking thing to speed up everything, and often fixing one slowdown will reveal more ones anyway but every little helps. We’re already quite fast in the simulation and have most of the “easy” things done, but these should still provide some nice improvements both in early and late game.  


## Measure Measure Measure​

Doing optimisations means nothing if you are not profiling and measuring your code, you cannot just eyeball it and hope your new code is faster you have to get concrete numbers to prove it.  
At Paradox we use a variety of tools for this, many common in the industry as a whole, as either third party applications or things integrated into our engine.  

For lower level more isolated cases we’ve got an integrated version of Google Benchmark in Clausewitz, this is excellent for measuring the impact of changes to very isolated pieces of code. Usually not very useful for our games since we rarely have easily isolatable chunks, but it is something I make frequent use of when doing optimisations to our engine’s more foundational types like our array and hashmap classes or our string and text utilities.  

For wider application level profiling we use more general profilers. They usually come in two types, instrumental and sampling. Instrumental profiling requires you to manually decorate your code with macros to instruct the profiler to measure in a given section. A sampling profiler periodically queries the entire application to see what is happening.  

For instrumented profiling we make use of an integrated version of Optick where we decorate some of our code and can get results based on varying categories and across different threads.  

![1_Instrumental_Profiling.png](https://forumcontent.paradoxplaza.com/public/731631/1_Instrumental_Profiling.png "1_Instrumental_Profiling.png")


[Function with profiling instrumentation]  

Here you can see that in our in-game interface when we update the open windows and view we profile the entire function as well as specific name subsections.  

For sampling profilers common ones we use on CK3 are Very Sleepy and Intel’s VTune. You attach them to your process and run them over the course of X amount of time then they compile together some results for you. Here is an example output from Very Sleepy in my recent debug build run.  

![2_Sampling_Profiling.png](https://forumcontent.paradoxplaza.com/public/731632/2_Sampling_Profiling.png "2_Sampling_Profiling.png")


[Part of the daily tick serial calls]  

![3_Sampling_Profling_Second.png](https://forumcontent.paradoxplaza.com/public/731633/3_Sampling_Profling_Second.png "3_Sampling_Profling_Second.png")



[A closer look at the council task’s functions and time]  

To monitor trends over time we also have automated tests running the game every night and outputting to log files performance metrics which the test system then gives us a nice graph for. These tests are for more specifically our daily tick and render times as opposed to application wide. Usually one sees the test showing a problem then digs into it more specifically with a profiler.  

These tools all help us to identify bottlenecks and then validate if we’ve solved them or not.  


## Script System​

One of the slowest operations you can do in the game is going into the script system, especially if you do it frequently and make use of more complex effects launching on actions and events which do even more logic.  

This is a balancing act we are constantly dealing with, because of course we want our Content Designers (and modding community) to be able to change loads of the systems in our game and fill it with great content. But exposing too much or in inefficient ways can really hurt us in terms of speed.  

In 1.5 I spent some time optimising some systems that were handled heavily in script but were very isolated and could easily be moved into a more performant code system, which for some issues entirely eliminates them from the profiler.  


### Character weight​

One thing that was a small chunk of the time but showed up proportionally hugely more than it should have was how much time we spent applying and removing the modifiers for when characters gained and lost weight and were considered obese or malnourished. This was a primary example of the slowness of the script system compared to code.  

Every couple of years we’d update the weight of a character and trigger an on action that their weight changed, from there we’d trigger events to add or remove the obese and malnourished modifiers based on two constant values we’d compare against. A very simple operation, but because of how many characters we have and all of them going into the script system it was actually showing up as a large part of a character’s yearly update.  

My solution was to simply move this to be done in code, the events and on action is now removed and instead there are two defines for the thresholds of gaining and losing the modifiers. As an upside to this by doing it in code we would now always correctly update and apply the modifiers automatically when the change_current_weight is used so it feels more responsive to special events.  

![4_Weight_Defines.png](https://forumcontent.paradoxplaza.com/public/731634/4_Weight_Defines.png "4_Weight_Defines.png")


[New weight defines]  


![5_Weight_Apply.png](https://forumcontent.paradoxplaza.com/public/731635/5_Weight_Apply.png "5_Weight_Apply.png")


[Weight modifiers being added based on current weight]  

### Combat phase events​

Something that was in script but required a larger rework was our combat events, every few days during a combat in the main phase we would run events for the commander and all the knights on both sides of the combat. These would then sometimes pick weighted random events to have such as a knight being wounded or your commander dying.  

However these too went through the on action system and into the event script, so they had to be done in serial. Which as mentioned in Meneth’s previous post on the setup of our game state is not what we want, especially for something like this where the heavy part is computing which outcomes to have not to apply the effects of the outcome.  

So I made a bespoke system for this which eliminates a large amount of its overhead, previously the combat manager took 12.5% of our serial tick update and now it's down to under 5%.  

This bespoke system is that we now have a common/combat_phase_events database which scripts in the different entries containing their triggers, weight to happen, and effects if picked. Then in the combat manager threaded pre-update we can in parallel evaluate the triggers and relative changes of these happening for all the involved characters and queue them up to be executed in the main update. And if nothing is picked, which is a very common case for combats as we do not do something every single day it'd be spammy, then we just do nothing for that character in that daily tick and skip them entirely saving us even more work.  


### Dynamic coat of arms​

Another system handled heavily in script that I moved to a bespoke code system is our usage of dynamic coats of arms. For a variety of titles, primarily those in the British Isles and Scandinavia though also some specific historical cases like Norman vs Saxon England, we had special coats of arms that would switch in and out based on different conditions.  

As another system in script this was missing the ability to do quicker evaluation and application of changes. I added a new system in common/coat_of_arms/dynamic_definitions which allows scripting a method of picking different coat of arms for a title based on triggers.  

To call an update you just need to run the update_dynamic_coa = yes effect on a title when you change something that has a good chance of needing an update, the advantage of changing it to this approach is that for the majority of titles we know they have no special coat of arms so can early out very quickly and do nothing, for titles that do we can check the conditions in code which is quicker than trying to from other pieces of script and then apply the changes. We can then only trigger the UI refresh if we actually changed to something else instead of triggering it too often.  

![6_Dynamic_CoA.png](https://forumcontent.paradoxplaza.com/public/731636/6_Dynamic_CoA.png "6_Dynamic_CoA.png")


[England's dynamic coat of arms definition]  

Here is the definition for England of whether it should switch to the French or Norman patterns, if it should go to neither then it uses the default coat of arms for the title which is the Saxon variant.  


## Cache Misses​

One of the more lower level types of performance problems you can get is cache misses, to explain this requires a brief lesson in how a computer’s memory works (don’t worry I’ll aim to keep it straightforward!)  

The basic idea is that in modern computers there are different types of memory, smaller quicker ones and larger slower ones. The bigger slow ones are your main memory, it can contain a lot of information but fetching data from it is hugely slow.  
So to save you on that it will fetch data from main memory and put it into increasingly faster yet smaller caches, called things like the L1, L2 or L3 cache with 1 being the smallest but fastest, so you can access it quickly.  
The smallest thing your processor uses are its registers that contain truly small values (just 32/64 bits of data) but are super fast to access for temporary storage in functions.  

When you access a piece of data not in your cache your CPU will fetch it for you, and try to smartly get surrounding data with it as chances are you want to use that too, and put it into the cache for you to use. This is a cache miss and it can be very slow if it needs to dig through all your caches and go to main memory.  

![7_Caches.png](https://forumcontent.paradoxplaza.com/public/731637/7_Caches.png "7_Caches.png")


[Image showing caches vs main memory I found off of google cause my photoshop skills are too bad to make this myself]  

Why is this an issue? Well to put it into perspective things can be measured in CPU cycles, how long it takes your CPU to do one simple operation. Getting a register is basically nothing, going to L1 cache is 3 or 4 cycles, L2 is 20+, then going to something like main memory is 200+ cycles.  
In comparison to actual CPU operations: something like adding two values is 1 cycle, an operation like sqrt which is costly and often avoided where possible is only around 15 cycles, your sin/cost/tan operations are often similar in terms of a main memory read which for an operation is a lifetime.  

To put it into an analogy, imagine you are baking a chocolate brownie and you need to get a piece of chocolate. A register is you having a piece of chocolate in your hand, L1 cache would be a piece of chocolate on your kitchen counter, L2 cache would be a chocolate bar on your counter you need to unwrap and break a piece off, L3 cache would be walking over to your cupboard to find a chocolate bar to use, and going to main memory would be you leaving and going to the store to buy some chocolate.  

(Can you tell I was kinda hungry for chocolate whilst writing this post?)  

So cache misses can hurt you, and I actually noticed that as part of our character manager pre-update we were having some piece of fairly benign code show up as really really slow despite being a simple operation.  
Every character can have scripted variables which is something that the script system can manipulate for their events, in the pre-update we would build a list of all characters with active variables so that in the serial update we could tick them and if they timed out remove them.  

Getting to those scripted variables however involved us doing a lot of pointer chasing, a pointer is just something that points to another location in memory that you can get data from and often it's a location somewhere very far away from where you already are. So as we just learnt that is likely a cache miss as you’ve got to bring the data it points at into cache before working on it.  

We were following a chain of 5 pointers for that, whoops...  

The solution to this was to pull out the scripted variable handling for all game objects into a new manager. This manager would have the data directly so in its pre-update of determining which to update we would get much less cache misses and also balance the load better since the character manager no longer had to handle it and they could be done at the same time. It would also then apply this smarter skipping of updating empty variable storage to all objects instead of just the characters manually doing it as an extra win. The game objects now simply have a lightweight stable handle to their variables for when they need to look it up in script execution and evaluation.  

![8_Variable_Manager.png](https://forumcontent.paradoxplaza.com/public/731638/8_Variable_Manager.png "8_Variable_Manager.png")


[The new script variable manager]  

For the serial update we could then also take advantage of the fact we know that all the variables are independent of each other and do this part of the serial update heavily threaded as well. With a handy utility to make a class opt into getting and storing/loading from saves the data updating all our variables into one unified and more performant system was great.  

Overall it took all of our serial variable updating down from 5.5% of the serial tick to 1.4%, the new pre-update was negligible in cost and it removed this slow down entirely from the character manager’s pre-update. So a nice win overall and demonstrates well that you’ve gotta keep in mind the actual hardware you work on and its limitations as well as the software. We're not writing code and games for some abstract machine despite what the C++ specification might claim we are doing, we are writing it for actual hardware sets which come with their own set of constraints and data to work with.  


## The Bare Necessities​

It might sound a bit obvious but the less and more simple code the computer has to execute the quicker it is at doing so. One area we’ve applied this to a lot in recent years is our usage of text, as anyone who is familiar with our game’s script files we’ve got a lot of text… like no really a LOT of text files.  

And two of the problems with text read in from files is that it can be really really long and be meant to represent things other than a real word as alas things like integers, floating points and booleans exist and in code we want to just store the real value 42 not the text string “42”.  

Most anything dynamic in length requires an unpredictable amount of memory, and we have to ask the operating system to give us that amount of memory dynamically at run time and when we’re done we give it back. Doing this is much slower compared to knowing what we want up front or using local registers and stack memory to store such things. And text can be unpredictably long especially from files of unknown length, so we always need to have this dynamic memory… or do we?  

Turns out that we use a lot of the same key words all the time and having duplicates in memory of that is often not needed, so something we make fairly regular use of to reduce string memory usage is a global lookup table. It will store one instance of the string and give us some numeric identifier we can use to get the text again whenever we need it, as its a global resource it is guarded by a mutex but it uses a smarter read-write mutex because the majority of the time we are reading the text from it not adding a new one and multiple people can read it at the same time.  

This helps to save out on unnecessary copies of text when storing things. Another utility for this is called a string view, it is a super small type which just contains a read only view of the text and a size. With that we can pass around lightweight views of full strings without needing to make copies of the dynamic text every single time, we can read from it just fine but we cannot modify it which is often exactly what we want as we’ve got no reason to modify text we read in from a file. We can also alter the view we have such as splitting based on some delimiter, which if you've seen our script for chaining between different objects you'll see we use this and split on "." in something like "root.father.mother".  

Now of course as I said at the beginning of this one must always measure these things, since strings vs views is a very isolated piece of code I could make use of the prior mentioned google benchmark to make sure that this theory holds up in practice.  

![9_String_Benchmark.png](https://forumcontent.paradoxplaza.com/public/731639/9_String_Benchmark.png "9_String_Benchmark.png")


[Functions to benchmark, notice one uses another string the other uses a view otherwise they are identical]  


![10_Benchmark_Results.png](https://forumcontent.paradoxplaza.com/public/731640/10_Benchmark_Results.png "10_Benchmark_Results.png")


[Timing output of this benchmark in nano seconds]  

As you can see, making a string view is much much much faster than making a full copy despite how similar the code of the two look. And in most use cases that is all we need so we’ve proliferated that throughout our code base a lot.  

The other case I mentioned is converting from a string to the number it is trying to represent, which is not a monumentally huge problem nor unsolved. Various coding languages and standard libraries have functions to convert from a string to an integer and back again. However often they do so in a non optimal manner of scanning text and taking into account different text locales or when converting to text by making full strings that as we’ve just seen are comparatively slow and with complicated instructions under the hood.  

C++17 introduced the idea of a set of minimal overhead functions to do these conversions that would do no dynamic memory usage and be as simple as possible in their conversion for plain ASCII text. Now we don’t use C++17 yet (soon though I hope) due to some third party dependencies that have not updated and that we’ve not replaced. But nothing in this C++17 code required any features that C++14 does not provide, so I took a round at implementing it (with solid inspiration from various C++17 implementations) and also tied it into some of our custom numeric types.  

Of course I also unit tested its various success and failure cases:  


![11_From_Chars.png](https://forumcontent.paradoxplaza.com/public/731641/11_From_Chars.png "11_From_Chars.png")


[Extract from unit test code handling the string conversion odd cases and how they should fail]  

Aand thankfully the thing everyone wants to see pops up for me when running these tests, making me happy that my code isn't total trash (just somewhat trash in some places).  


![12_Unit_Test_Pass.png](https://forumcontent.paradoxplaza.com/public/731642/12_Unit_Test_Pass.png "12_Unit_Test_Pass.png")



This proved to be much better at crunching numbers from our text files compared to what we had used before, not as big a win as other startup optimisations since too much in serial is more of a blocker than some allocation and parsing slowness, but getting it out of the way made other issues with our text parsing easier to notice since it was now not bloated up by our general string usage here.  
I also wrapped it into a more convenient interface of taking in/returning one of our aforementioned string views since the actual to/from_chars implementation is more of a low level building block and most of the time when consuming it we don’t care why it failed just that it gave us a number or not as an optional value.  

And that is all for this week folks! Next week I will be digging into the script system as a whole and how that works to let our Content Designers and modding community make all the cool stuff they do which fills our game up with fun things!

 

Toggle signature

Former Senior Programmer on Crusader Kings 3  

My mostly empty [Twitter account](https://twitter.com/Matt_Clohessy)

<!-- artifact:reactions:start -->
- 46 Like
- 23 (unlabeled — rendered as base64 data URI)
- 18 Love
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
