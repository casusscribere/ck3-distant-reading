---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1482960/"
forum_thread_id: 1482960
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "Anatomy of a Game: Startup and Loading"
dd_date: 2021-07-15
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
body_word_count: 4812
inline_image_count: 3
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1482960'
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
    location: raw_lines_~28_to_120
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_122_to_123
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_387_to_390
    action: preserved_and_flagged
    counts:
      Like: 130
      Love: 44
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
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

# Anatomy of a Game: Startup and Loading

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [Jul 15, 2021](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/)
- [2](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/page-3)
- [4](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/page-4)
[Next](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/page-2)

1 of 4

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/page-4 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/?prdxDevPosts=1)

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

- [Jul 15, 2021](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/post-27680086)


- [/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/post-27680086](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/post-27680086)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27680086/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/post-27680086)

Hello everyone! My name is Matthew and I am a programmer on CK3, welcome to the first in a series of more technical focuses posts called Anatomy of a Game.  

In this series over the summer we are going to try and pull back the curtain of game development a bit and go into more detail on how our games actually work.  

What happens when you launch up the game? How do we make sure to load DLCs and mods? What actually goes on in a single day of gameplay? What makes the AI decide to brutally invade you?  

I hope to answer, or at the very least shed some light on, some of these questions and more over the course of this series.  

These posts are not a replacement for our more traditional Dev Diaries, and if you are looking for information or teasers related to upcoming content then this is not the thing for you. But if you are interested in the background of what makes games work or are an aspiring game developer then these should prove interesting to you!  

#### Game Setup​

In today’s post I am going to begin at well… the beginning! When you launch the game and load in to pick your character what is it that we are actually doing?  
It might sound like a simple question, as well obviously we load everything right? But how do we do that in a way that feels responsive and as fast as possible? What stuff do we actually load vs deal with later? How do mods and DLC files play into overriding things?  

At a high level the flow of starting the game is:  


1. Start some base functionality in the engine in order: file system, logging, threading task system
2. Load a library called SDL, which is a common library for accessing hardware in games
3. Load a ton of stuff for the engine to do its job, many as background tasks on threads
4. Create the window for the game
5. Load an even larger ton of stuff for the actual game itself
6. Game is now loaded and you can start playing
So why does step 1 do it sub-steps in that specific order? Its purely a dependency that makes sense if you think about it, a lot of systems do logging so but that of course needs files so we load the file system first, and we want to load a lot of things in background threaded tasks but that system is going to log so we need to do it after the logging and file system.  

This is a very high level set of steps and glosses over a lot of details of course, I will be glossing over numerous details in this but feel free to ask any specific questions. The bulk of interesting things happens in steps 3 and 5, they are the biggest part of our startup loading and where most of any optimization time goes.  

Why optimize load times you might ask? Well of course for you the end user whilst our load screens and main themes are great you’d probably rather be playing the game.  
For us, well we start the game up a lot during any given day. And every second spent waiting for the game to load is just wasted time and money. When we run the game we also do so without the compiler having done its heavier optimisations on our code, so ours is even slower than yours.  

It is of course not the core of our optimization times, we work much more on daily tick speed and framerate. But it is an area we keep in mind especially for our iteration speed payoffs in the day to day development.  

How does one even optimize a lot of these things? It's generally split between making more efficient use of CPU time and reducing the time spent waiting.  

For the CPU time that is a couple of things: multi-threading more work so more of the CPU is being used, optimize your lower level algorithms you use, and finally you can get really close to the hardware to optimize your CPU branch misprediction and memory cache misses.  

For waiting the goal is just to do less of it. Waiting is whenever your CPU has to wait to get access to a resource, wait for some threaded work to actually be done at its deadline, and even things like reading data from the disk since that does take in which your code is doing nothing itself.  

The one I am going to go into more detail here initially is higher level multithreading usage, as our loading of data on the game side is the one I’ve spent time optimizing at the beginning of the year and most of that was solved by introducing more multithreading capabilities and optimising things that were thread safe but not thread efficient.  

#### Something to look at​

Our very first goal with loading is that we want to get a load screen up ASAP so that you know the game hasn’t crashed and burned on you, so we show the main splash screen there.  


![startscreen.png](https://forumcontent.paradoxplaza.com/public/727495/startscreen.png "startscreen.png")


This wonderful logo is covering up us trying to load everything we can and make you not think it is all crashing and burning. After we have it up we start loading some necessary game components up front like the mouse textures and the bare minimum UI files like how our text should look to show the proper load screen.  

Another thing we try to load ASAP is the music database so we can get that main theme playing, cause just staring at a load screen in silence is less fun than having our composer’s wonderful music to tide you over the loading. Even though ironically one of our goals is to make you hear as little of that main theme as possible. Sorry Andreas…  

Incidentally in other games if you see an un-skippable cutscene like someone opening a door to walk through, or one that you can only skip part of the way through, then in reality that is just a very pretty loading screen hiding a lot of work being done under the hood.  

Thankfully games these days account for the fact that hardware gets better and lets you skip a lot of them once the loading is done, but if you go back to older games that was not a thought so many long scenes hiding a load cannot be skipped.  

To take a modern example of that, the elevator rides in Mass Effect 1 where you had wonderful party banter in places like the Citadel were just loading screens hidden with narrative exposition on top, but even when running the game on modern hardware it would not let you skip them.  
In the recently released Mass Effect Legendary Edition remaster they added a skip button during those scenes now as modern hardware can load everything quickly, you can of course still opt into hearing the great banter between your squad mates.  

We’ve loaded a lot of stuff multithreaded until now, but from here on out everything we’re loading is threaded in the game side. And we load a lot now, things like the rest of files for the UI, data for our 3D entities, the map data, our game logic files, and then the front end and its UIs.  

All of this loading is done whilst the main thread keeps making sure we intermittently render the load screen and poll the operating system for input events and promptly ignore them all.  

The latter being because Windows will give you the dreaded application not responding pop up if you fail to poll the events it provides, since we are loading we cannot really do anything meaningful with any inputs so we just take and ignore them to make Windows sure we haven’t secretly crashed.  

![RIP_Windows.png](https://forumcontent.paradoxplaza.com/public/727496/RIP_Windows.png "RIP_Windows.png")



Also worth noting that for a good amount of stuff we don’t actually have it loaded even by the time you are at the main menu, because the average user is going to maybe decide what save they want, be a bit slow on clicking something etc. and all of that does not require us to have everything loaded. So we aim to continue loading other lower priority things in the background until we really truly need it.  

One example of that is our history database, it is very large but also something we know that we do not need to get to the main menu and even then we only need if we are starting a new game. As saves contain their own history from the play time. So we keep that loading in the background giving us some nice extra free time to the point where it's probably loaded even if you do start a new game eventually anyway.  

#### Database Loading​

So that has been a lot of words about the things we load and some reasons behind the priorities. Now I am going to pivot into a more specific example, loading our game and mod files into the various databases.  

So how we get DLC and mod files working in the same level as the game is actually quite straightforward. For our file system we use an integrated and modified version of PhysicsFS, or PhysFS for short, which works very nicely by letting you mount multiple directories under one logical hierarchy you can then search through to find individual files or multiple files in the hierarchy to load from.  

During startup when we set up our file system we mount our base directories for the core game, and then when we load DLCs and mods we look in the user directory and check what is enabled and then mount those directories into the same path. So searching for a folder like “common/landed_titles” we will look in both the game install directory and the directories of enabled downloaded mods and treat them as the same from the code’s perspective when we load that data into the landed title database.  

So how do we actually load these databases? In the currently released version of CK3 we load them all on one of our background tasks and one by one load them in order, with the order having support for defining dependencies as some systems need to reference another. Which for a long time was “good enough”, but as we’ve added more and more scripted systems and more and more content in sheer volume to load that started to show its flaws.  

It was the biggest amount of time on all our threaded loading tasks and dominated by a lot meaning that we were waiting on just that one chunk of work even after the other things were done, and in terms of optimisation opportunities it was very good because in theory the databases can be formalised in a very strict layout and we then know what we can and cannot load simultaneously.  

To note this idea of loading databases in parallel would not have been doable without the work that one of our other programmers, [@MatRopert](https://forum.paradoxplaza.com/forum/members/1324992/) the Tech Lead on HoI4, did when he was on Stellaris which improved our PhysFS file system to operate a lot better in a heavily threaded environment. As if file operations entirely were a threading bottleneck then we’ve had no gains by trying to do this anyway, that is a common problem that one bottleneck hides many others. I’d recommend checking out his blog post on it [here](https://mropert.github.io/2020/07/26/threading_with_physfs/), though note it is aimed at programmers more directly than this post.  

So what was it that I did here? First step was formalising our database dependencies into a proper graph object in code that I could then operate on. Be that dumping it to disk as an image to cry at our dependencies, running automated tests on it to ensure that changes and additions do not break everything, or doing the actual loading of it all so we can play the game.  

Setting up the dependency graph is straightforward, every database’s code can be analysed to see if it needs a strict dependency or not. Generally that means if the reading of the script file directly needs to then reference another database, such as reading in a key and looking it up, then it needs a strict relation to be added.  

Here is the dependency graph I captured recently for just our logic, no interface or databases with icons present, and it's already quite the monster.  

[View attachment Logic_Dependencies.png](https://forumcontent.paradoxplaza.com/public/727499/Logic_Dependencies.png)  

The loading of this graph is where we get our performance gains, since we know exactly what databases depend on what we can load in parallel databases that do NOT depend on each other, which is the bulk of databases. Then when something is loaded it can notify things dependent on it that it has been completed and if it was the last thing they needed they can start their loading and so on.  

Anything with threading is always easier said than done, you’ve got to make sure your operations really don’t go around competing with each other or introduce exclusive ownership or atomic operations where necessary so things stay synchronized. And when doing so make sure that the speed ups you are doing don’t then get wiped out by all of the synchronization that you are doing.  

So of course then queue up a lot of discovering of hidden dependencies I had to formalise, fixing dreaded circular dependencies, plenty of threading problems, optimizing a few more systems, and doing some iterations to squeeze all the performance we could out of it and we managed to get some nice gains!  

So for some actual numbers of these changes, and others done by myself and [@Meneth](https://forum.paradoxplaza.com/forum/members/265499/):  


- Internal debug builds this section took over 20 seconds to load and now it's down to under 4 seconds.
- In the release builds it took this section down from about 7 seconds down to under a second.
So it won’t suddenly make the game load instantly and deprive you of the wonderful main theme, but it definitely should save you some time and saves us a lot of time we can then spend actually making the game instead of browsing twitter for memes or making XKCD posts proud…  

![compiling.png](https://imgs.xkcd.com/comics/compiling.png "")



#### History into reality​

Once we’re at the main menu we can do the final part of getting you into the game, loading a save or starting a new game. Of which both are pretty similar hence I am bundling them together.  

Loading a save is at a high level a simple one, we create our base game state and then simply run through your save game file and read in different sections which fill in different data for every part of the game. Our saves, and all files in our games really, operate on a fairly simple syntax of data that we read in.  

The saves can get pretty big, since our simulations can store a lot of numbers and data, so for a lot of things we either try to not write it to save games if it's a default value or we just cache it in game internally so it never appears in saves.  

An example of this is the full modifiers that apply to a character from all sources, we do not actually write those in our normal save games because it's just so much data and is something we can rebuild entirely from the rest of the save. We only write them when performing an out of sync check and want to compare them directly to make sure none of the values differ or that our caches are incorrect.  

Starting a new game is actually really just the process of making a new save based on the start date you pick and then loading that save. If you select a bookmark character then we fast track you through the lobby to that character when loading, but if you select play as anyone then really we just load up the save game and put the pick a character lobby up to you.  

The initial save generation is mostly just a lot of reading history files and then filling in default data. We also do a lot of semi-randomised startup content so that not every detail of every play session is always identical, though nothing on the level of something like Stellaris where the entire starting scenario changes every time since we do want to keep a fairly consistent historical background to the playthroughs.  

![1626283387163.png](https://forumcontent.paradoxplaza.com/public/727501/1626283387163.png "1626283387163.png")



Reading and loading all 15 MB and the near 600 files...  

If you are a modder you may notice that we've got a lot less small history files these days and instead bunch them into bigger ones. This is due to the fact that on Windows the system for opening a file is not as fast as on something like Linux or OSX so we instead aim to open fewer but bigger files. Especially since we try to do a lot of our loading more aggressively in parallel now its a boon to not be waiting on the file system, hence less tiny little files these days.  

#### We made it!​

So we’ve made it into the game! Nice! Time to actually play it, or if you’re me doing optimisations, close it, change some code, and launch it up again a few times to measure more...  

I hope you’ve enjoyed this little (can one consider like 8 pages in google docs little?) dive into some of the backing of the game and technical details of it. I’ve tried to stay fairly high level because most of you are likely not software engineers, but please do give feedback on if it's too high level or getting a bit too technical so I can adapt for the future posts!  

I wanted to do a series like this because game development is a bit of a black box knowledge wise to our end users compared to other forms of entertainment like books, television or music. Everyone knows roughly what goes into writing a book or how difficult it can be to play a musical instrument, in many countries we have to study such things in school.  

But game development is not like that, it is the largest entertainment industry in the world but most of the consumers don’t really know what goes into it leading to misconceptions, and I think the more we can try to reduce some of the mystique of it the easier time we’ll have being able to communicate with our fans overall. And hopefully get a few people interested in maybe pursuing a career in it.  

So that is all for this week folks! Feel free to ask questions here of any technical level and I will try my best to answer them!

 

Toggle signature

Former Senior Programmer on Crusader Kings 3  

My mostly empty [Twitter account](https://twitter.com/Matt_Clohessy)

<!-- artifact:reactions:start -->
- 130 Like
- 44 Love
- 40 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
