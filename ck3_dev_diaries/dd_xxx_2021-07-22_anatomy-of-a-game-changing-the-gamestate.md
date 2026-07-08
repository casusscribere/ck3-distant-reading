---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1483669/"
forum_thread_id: 1483669
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "Anatomy of a Game: Changing the Gamestate"
dd_date: 2021-07-22
author_handle: Meneth
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 4443
inline_image_count: 8
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1483669'
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
    location: raw_lines_345_to_348
    action: preserved_and_flagged
    counts:
      Like: 45
      (unlabeled — rendered as base64 data URI): 1
      Love: 17
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
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

# Anatomy of a Game: Changing the Gamestate

<!-- artifact:thread_metadata:start -->
- Thread starter [Meneth](https://forum.paradoxplaza.com/forum/members/meneth.265499/)
- Start date [Jul 22, 2021](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/)
- [2](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/page-3)
[Next](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/page-2)

1 of 3

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/page-3 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/?prdxDevPosts=1)

[![Meneth](https://forumcontent.paradoxplaza.com/data/avatars/s/265/265499.jpg?1427162636)](https://forum.paradoxplaza.com/forum/members/meneth.265499/)

#### [Meneth](https://forum.paradoxplaza.com/forum/members/meneth.265499/)

##### Crusader Kings 3 Programmer

**153 Badges**

Feb 9, 2011

10.056

5.413

[www.paradoxwikis.com](http://www.paradoxwikis.com/)

- ![Europa Universalis IV: Common Sense](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cs_forumicon.png "Europa Universalis IV: Common Sense")
- ![Crusader Kings II: Holy Knight (pre-order)](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_gold_forumicon.png "Crusader Kings II: Holy Knight (pre-order)")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: Sunset Invasion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sunset_invasion_forumicon.png "Crusader Kings II: Sunset Invasion")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MtGicon.png "Hearts of Iron IV: Expansion Pass")
- ![Steel Division: Normand 44 Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SDSignupicon.png "Steel Division: Normand 44 Sign-up")
- ![Stellaris: Digital Anniversary Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/plantoid.png "Stellaris: Digital Anniversary Edition")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Mount &amp; Blade: With Fire and Sword](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/WFAS.png "Mount &amp; Blade: With Fire and Sword")
- ![Mount &amp; Blade: Warband](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/WARBAND.png "Mount &amp; Blade: Warband")
- ![Magicka: Wizard Wars Founder Wizard](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MWW_EA_Forum_Icon.png "Magicka: Wizard Wars Founder Wizard")
- ![Hearts of Iron IV: Death or Dishonor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4DoD.png "Hearts of Iron IV: Death or Dishonor")
- ![Europa Universalis IV: El Dorado](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_eldorado_forumicon.png "Europa Universalis IV: El Dorado")
- ![Hearts of Iron IV: Colonel](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Col.png "Hearts of Iron IV: Colonel")
- ![Hearts of Iron IV: Field Marshal](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FM.png "Hearts of Iron IV: Field Marshal")
- ![Surviving Mars: Digital Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_DDE.png "Surviving Mars: Digital Deluxe Edition")
- ![BATTLETECH: Flashpoint](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BTFlashpoint.png "BATTLETECH: Flashpoint")
- ![Crusader Kings II: Conclave](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DLC_icon_Conclave.png "Crusader Kings II: Conclave")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![Cities: Skylines Industries](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/cslindustriesicon.jpg "Cities: Skylines Industries")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellnova.png "Stellaris: Galaxy Edition")
- ![BATTLETECH](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/battletech_standard.png "BATTLETECH")
- ![Hearts of Iron IV Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HOI_signup.png "Hearts of Iron IV Sign-up")
- ![Stellaris Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Stellaris_SignUp_icon.png "Stellaris Sign-up")
- ![Hearts of Iron IV: Cadet](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Cad.png "Hearts of Iron IV: Cadet")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Prison Architect](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Prisonicon.png "Prison Architect")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Cities: Skylines - Campus](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSLCampus.png "Cities: Skylines - Campus")
- ![Hearts of Iron IV: No Step Back](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/NSB_forum_icon_16x16.png "Hearts of Iron IV: No Step Back")
- ![BATTLETECH - Digital Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/battletech_Deluxe_icon.png "BATTLETECH - Digital Deluxe Edition")
- ![Crusader Kings Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/crusaderkings1.png "Crusader Kings Complete")
- ![Cities: Skylines - Parklife](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSLParkLife.png "Cities: Skylines - Parklife")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Age of Wonders III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoW3_forum_badge.png "Age of Wonders III")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")
- ![Europa Universalis IV: Cradle of Civilization](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EUIV_CoC.png "Europa Universalis IV: Cradle of Civilization")
- ![500k Club](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/500k_red.png "500k Club")
- ![Stellaris: Leviathans Story Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/leviathans.png "Stellaris: Leviathans Story Pack")
- ![Crusader Kings II: Reapers Due](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/reapers_due_forum_icon.png "Crusader Kings II: Reapers Due")
- ![Europa Universalis IV: Mandate of Heaven](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/moh_forum_icon.png "Europa Universalis IV: Mandate of Heaven")
- ![Europa Universalis III Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/in_nomine_icon_forum.gif "Europa Universalis III Complete")
- ![Cities: Skylines - Mass Transit](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CitiesSkylines_MassTransit_16x16.png "Cities: Skylines - Mass Transit")
- ![Europa Universalis III Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nap_icon.gif "Europa Universalis III Complete")
- ![Cities: Skylines - Green Cities](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSL_green_cities.png "Cities: Skylines - Green Cities")
- ![Teleglitch: Die More Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/teleglitch_icon.png "Teleglitch: Die More Edition")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")

[](javascript:;)

- [Jul 22, 2021](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/post-27692348)


- [/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/post-27692348](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/post-27692348)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27692348/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-changing-the-gamestate.1483669/post-27692348)

Good afternoon everyone! My name is Magne Skjæran, and I’m a senior programmer on Crusader Kings 3. I’m here to bring you the second entry in the Anatomy of a Game series. You can read the first entry by Matthew here on our [Startup and Loading](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-startup-and-loading.1482960/).  
Today’s topic will be how we change the gamestate. This is core to the whole simulation of the game, since if nothing changes there’s no real game to play.  

I’ll be covering three main topics here. First I’ll talk about the command system, which is how all interaction with the game happens. Then about how we determine what to change vs. how we actually change it. Then finally, about what out of syncs are and how they occur.  

What I cover here will all be based on CK3, but a lot of it applies to our other games as well. But there will be differences here and there; sometimes big ones! So don’t take any of this as gospel for our other games.  


## Command System​

The core of our game is a simulation. It runs on its own even if no agent (the player or AI) makes any changes to it. But a simulation you can’t influence is just a toy rather than an actual game. This is where commands come in.  

A command is a set of data on how to change the gamestate. A simple example would be a command to “queue movement of this unit to that province”, or “select this event option”.  
All interaction happening via command also makes it easy for us to find everything the player can influence, which makes a variety of bugs easier to debug, and makes it easier for us to reason about how the game works.  

![Disband_Army_Command.png](https://forumcontent.paradoxplaza.com/public/729803/Disband_Army_Command.png "Disband_Army_Command.png")


[A command to disband an army]  

The command system also forms the basis of multiplayer. Anything a player does is communicated to the other players’ machines by sending a command over the network. Forcing all interaction into the system therefore makes multiplayer Just Work™ in the vast majority of cases without us having to write any MP-specific code. When a programmer implements a new system, it is rare to have to think much at all about much at all about multiplayer (while the designer probably needs to give it some thought to make sure the feature is fun both in SP and MP).  

The player’s interaction happens via the interface, unsurprisingly. The interface is a separate module from the actual game logic; it covers things like what to show, and how they’re interacted with. The game logic can’t see the existence of the interface at all in the code, which avoids a whole class of bugs where logic in some way depends on the interface, an issue that would occasionally happen in our older games. The interface is only able to read the gamestate, and this is enforced by the code systems we have. Commands are the only way for the interface to affect the gamestate.  

![Posting_Commands.png](https://forumcontent.paradoxplaza.com/public/729804/Posting_Commands.png "Posting_Commands.png")


[The code to send a command from the UI]  

Since the gamestate cannot see the existence of the interface, this means that it is hard to communicate with the interface. Naturally, this can pose a problem. For instance, imagine something happens to the player and we want to send a notification about it; for instance if the player goes up a prestige level. Sure, the interface could store the player’s prestige level and then generate the notification when it changes, but this ends up duplicating a ton of state between the logic and the interface. So instead we have a system similar to commands for sending information from the logic to the interface, which we call “messages”. Like commands, these are specific pieces of information that the interface is to act upon in some manner. They get handled in the interface, so when the logic sends the message “player increased their prestige level”, the interface then takes care of actually showing that notification to the player.  

Now, that’s enough about the player. What about the AI? The AI plays by essentially the same rules. Anything that’s not happening via the simulation itself is done by command for the AI as well. Periodically, the AI considers the various actions it can take, and for each it decides to do it’ll send a command. Usually this is the exact same command a player would’ve sent; the player and AI will both use the same command for “move this unit to this province” for instance.  
The AI and the player using the same system makes it easier for us to ensure the two play by the same rules. Even more importantly, that the same attempted action gives the same result, avoiding subtle bugs due to differences between how the AI and the player interact with the game.  

![AI_Posting_Command.png](https://forumcontent.paradoxplaza.com/public/729805/AI_Posting_Command.png "AI_Posting_Command.png")


[The AI sending a command]  

There’s not that much more to cover about how the AI interacts with the game without going into far more detail of the AI systems themselves, which could easily be a dev diary of its own, so I’ll move on now.  


## Evaluation and execution​

All changes to the gamestate can be considered to have two main parts: deciding what to do (evaluation) and actually doing it (execution). In a large number of cases, the thing that takes the most time is to figure out what to do, not to actually do it. For instance, choosing which event to fire out of hundreds available in a yearly pulse takes longer than applying the event we decide upon.  

Generally speaking, we can only execute one thing at a time (otherwise we get out of syncs; more on that later). We can however evaluate multiple things at the same time by using threads. So instead of each character individually in a row deciding what events to fire, we can consider 8 or more (depending on how many CPU threads the player has) characters’ events simultaneously. Each character then adds the events they’re going to fire to a queue. This part has to be synchronized as we can’t add two things to a list at the same time, but since the vast majority of the time is spent on the evaluation rather than adding to the list, we save huge amounts of time by distributing the work. Later we can then go through the queue and fire each event, removing any that’s no longer applicable for whatever reason (maybe a character involved died?) along the way.  

This split between evaluation and execution is one of the cornerstones of how we do threading on CK3. The gamestate is split up into various “managers” that are each responsible for one part of the game. For example there’s a Secrets Manager, an Event Manager, a Character Manager, and a Title Manager. The main part of how we progress the game a single day is split into two parts; the pre-update and the main update. In the pre-update, each manager does its own evaluations and makes notes of things to do later. No visible gamestate is allowed to change, so each manager can safely look at things they don’t manage (E.G., the title manager is allowed to look at the holder of a title, even though it doesn’t own characters). Instead they can only change things that are invisible to the rest of the game (like that event queue mentioned earlier).  

![Pre_Update_Managers.png](https://forumcontent.paradoxplaza.com/public/729806/Pre_Update_Managers.png "Pre_Update_Managers.png")


[Time spent in the various pre-update managers]  

The split makes it very easy for us to thread things, as there’s only one rule to follow (don’t modify any visible state). The threading on our older game came with far more rules to obey (only look at your own data, don’t look at this thing, don’t modify this other thing, etc.), meaning that for experienced and new programmers alike it was easy to make mistakes. With only a single rule mistakes are harder to make, easier to catch, and easier to fix. As a result we’re more productive, and CK3 is our most threaded game to date.  

The AI works very similarly. It’s run after the main update rather than before it, but works on the same principle. The AI is not allowed to change anything except certain pieces of purely AI-internal state, and instead just sends commands. The AI is split up into a variety of sub-tasks, composed together based on a frequency basis. E.G., an individual AI will check whether it should change its laws and whether it should leave a faction in the same task, as these happen at the same frequency. Each such grouping of tasks can happen simultaneously with any other grouping of tasks. The granularity of this means that the threading of the AI is very effective (known as “good load-balancing”) as one thread is unlikely to finish its work significantly earlier than another thread (which would leave it idling).  

![AI_Threaded_Work.png](https://forumcontent.paradoxplaza.com/public/729808/AI_Threaded_Work.png "AI_Threaded_Work.png")


[The AI updating a set of tasks]  

As mentioned earlier, the use of the command system means that the effects of the AI are nicely isolated from its decision-making process. This makes it easier to iterate upon, easier to reason about, and easier to optimize.  
Now, let's move on to the final topic of today: out of syncs.  


## Out of Sync​

If you play multiplayer in any of our games you’re aware of a particularly dreaded set of words: “game is out of sync”. When this happens you’re unable to continue playing, and depending on the game have to either rehost or resync. But what is an out of sync (OOS), beyond us programmers having a laugh at your expense?  

![OOS_Message.png](https://forumcontent.paradoxplaza.com/public/729809/OOS_Message.png "OOS_Message.png")


[CK3 going out of sync]  

To explain what an OOS is, I first need to explain how multiplayer itself works. In most games out there, the core of how multiplayer works is that the server (or a player’s machine acting as the server, if it is peer to peer) will tell all the clients the state of everything in the game. Where everything is, where it’s moving, how much health it has left, etc. Left out is usually only things that are static (what the map looks like in many games for instance). Competitive games often also leave out things that the client would have no way of knowing (like the position of another player on the other side of the map) to combat wallhack cheats and the like.  
This is generally a very sensible model, but it breaks down if there’s too much gamestate to send over the network several times a second. In a first person shooter with 10, 20, maybe even 100 players all this info can be stored in a few kB, but CK3 for comparison usually has around 20 thousand characters, never mind everything else. The full gamestate of CK3 takes around 30 to 100 MB to store uncompressed, and even with compression you’ll easily pass 10-20 MB once you’re far enough in. Clearly, this is not something we can send over the network repeatedly.  

So what do we do instead? We use an architecture known as “lockstep multiplayer”. This is common for strategy games. How this works is that instead of telling clients the state of everything (or a large subset of everything), we instead first provide them the initial state (in the form of a save), and then each client runs their own simulation. We send commands for player and AI interactions; everything else each client will calculate on their own. As a result far less info is sent over the network, since we only need to inform the clients of things that deviate from the natural flow of the simulation.  

But here’s the problem: this means we have to ensure every single client simulates the game the exact same way. Because if anything differs, no matter how small, that tiny change will eventually Butterfly Effect its way to causing drastic differences between what’s happening on each machine. So while one player just got declared war on by some Vikings, on another client this wouldn’t be happening at all.  

When anything differs, that’s an out of sync. At this point, major breakage is inevitable, and so we tell the players and force a rehost. This isn’t a great experience for anyone, so it is something we work hard on avoiding.  

So how do out of syncs happen in the first place? It generally comes down to a lack of determinism. Determinism is when the same input always leads to the same result. As long as that’s the case, out of syncs are impossible (except if some input is lost or corrupted due to, say, network issues). But determinism isn’t easy.  
It is simple enough if your game is single-threaded, but then it’ll also be slow. Any threading can introduce non-deterministic behavior if you’re not careful. The most common way is due to order issues. Let's say you’ve got the number X. It has a value of 10. Thread A wants to add 2 to it. Thread B wants to multiply it by 2. If Thread A happens to run first, the end result will be (10 + 2) * 2 = 24. But if Thread B runs first, it will be (10 * 2) + 2 = 22. So if for any reason threads run in a different order on two machines (maybe one CPU core was busy with something else for a split second), an out of sync will occur.  

This is a big reason why we usually only multi-thread evaluation. If nothing is changed, then order doesn’t matter. We sometimes thread things that change visible state too, but that’s much rarer and we’re far more careful to ensure that ordering doesn’t matter.  

Another cause of out of syncs that was far more common in our older games, was the interface influencing the gamestate in some manner. To take a simple example, imagine we have some value we only rarely update because it is really time consuming to update. But when the player looks at it, we want it to be fully up to date. It might be tempting to force it to update when the player opens the interface but oops… now you’ve introduced an out of sync.  
The way we’ve structured CK3 makes it far more difficult to make this mistake, as it’s much harder to modify the gamestate from the interface. We’d instead send a command to refresh the value, and/or maybe do the actual math for the new value just in the interface and leave the gamestate untouched.  

Similarly, it’s easy to introduce issues due to bits of game logic depending on if a character is the local player or not. E.G., we want to update the player’s predicted income daily rather than monthly to ensure the player’s info is up to date. The naive implementation here would mean that on each client the client’s character gets updated daily, but the other players get updated monthly. The game would thus be out of sync, as the player characters would have different cached incomes.  
In CK3 we avoid this by just checking that they’re a player rather than the person playing on this machine. Furthermore, we’ve made it deliberately harder to check “is this the local player” than to just check “is this any player”. We still need the former quite a bit (primarily for sending notifications), but it involves the programmer basically going “yes, I’m sure I know what I’m doing here”:  

![Local_Player_Access.png](https://forumcontent.paradoxplaza.com/public/729810/Local_Player_Access.png "Local_Player_Access.png")


[A notification being sent to the local player]  

Note the “ALLOW_GET_LOCAL_PLAYER_IN_SCOPE” here; that’s our way of making sure we only check who the local player is if we really need to. Otherwise, we’d easily end up with something only getting changed on a player character for the client actually playing that character.  

So that’s the long and short of what out of syncs are, why they happen, and some of what we do to avoid them.  
And with that, I’m done. I hope you found this post about how our gamestate works interesting!  

I am on vacation today but Matthew ([@blackninja9939](https://forum.paradoxplaza.com/forum/members/795679/)) will be here to answer any of your questions about this topic as well! And I may check in too!

 

Toggle signature

~ Magne Skjæran - Crusader Kings 3 programmer  
[Follow me on **Twitter**](https://twitter.com/Meneth_) for out of context quotes from Paradox

<!-- artifact:reactions:start -->
- 45 Like
- 31 (unlabeled — rendered as base64 data URI)
- 17 Love
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
