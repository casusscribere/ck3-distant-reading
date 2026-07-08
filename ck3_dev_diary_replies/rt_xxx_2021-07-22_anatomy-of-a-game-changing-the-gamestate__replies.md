---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1483669/"
forum_thread_id: 1483669
content_type: reply_thread
parent_dd_file: dd_xxx_2021-07-22_anatomy-of-a-game-changing-the-gamestate.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "Anatomy of a Game: Changing the Gamestate"
dd_date: 2021-07-22
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 3
reply_count: 46
participant_count: 31
reply_date_first: 2021-07-22
reply_date_last: 2021-08-17
body_word_count: 5618
inline_image_count: 0
quoted_span_count: 23
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Anatomy of a Game: Changing the Gamestate

*46 replies from 31 participants across 3 pages*

## Reply 1 — participant_001 · 2021-07-22 · post-27692348

Good afternoon everyone! My name is Magne Skjæran, and I’m a senior programmer on Crusader Kings 3. I’m here to bring you the second entry in the Anatomy of a Game series. You can read the first entry by Matthew here on our Startup and Loading. Today’s topic will be how we change the gamestate. This is core to the whole simulation of the game, since if nothing changes there’s no real game to play. I’ll be covering three main topics here. First I’ll talk about the command system, which is how all interaction with the game happens. Then about how we determine what to change vs. how we actually change it. Then finally, about what out of syncs are and how they occur. What I cover here will all be based on CK3, but a lot of it applies to our other games as well. But there will be differences here and there; sometimes big ones! So don’t take any of this as gospel for our other games. Command System​The core of our game is a simulation. It runs on its own even if no agent (the player or AI) makes any changes to it. But a simulation you can’t influence is just a toy rather than an actual game. This is where commands come in. A command is a set of data on how to change the gamestate. A simple example would be a command to “queue movement of this unit to that province”, or “select this event option”. All interaction happening via command also makes it easy for us to find everything the player can influence, which makes a variety of bugs easier to debug, and makes it easier for us to reason about how the game works. { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" } [A command to disband an army] The command system also forms the basis of multiplayer. Anything a player does is communicated to the other players’ machines by sending a command over the network. Forcing all interaction into the system therefore makes multiplayer Just Work™ in the vast majority of cases without us having to write any MP-specific code. When a programmer implements a new system, it is rare to have to think much at all about much at all about multiplayer (while the designer probably needs to give it some thought to make sure the feature is fun both in SP and MP). The player’s interaction happens via the interface, unsurprisingly. The interface is a separate module from the actual game logic; it covers things like what to show, and how they’re interacted with. The game logic can’t see the existence of the interface at all in the code, which avoids a whole class of bugs where logic in some way depends on the interface, an issue that would occasionally happen in our older games. The interface is only able to read the gamestate, and this is enforced by the code systems we have. Commands are the only way for the interface to affect the gamestate. [The code to send a command from the UI] Since the gamestate cannot see the existence of the interface, this means that it is hard to communicate with the interface. Naturally, this can pose a problem. For instance, imagine something happens to the player and we want to send a notification about it; for instance if the player goes up a prestige level. Sure, the interface could store the player’s prestige level and then generate the notification when it changes, but this ends up duplicating a ton of state between the logic and the interface. So instead we have a system similar to commands for sending information from the logic to the interface, which we call “messages”. Like commands, these are specific pieces of information that the interface is to act upon in some manner. They get handled in the interface, so when the logic sends the message “player increased their prestige level”, the interface then takes care of actually showing that notification to the player. Now, that’s enough about the player. What about the AI? The AI plays by essentially the same rules. Anything that’s not happening via the simulation itself is done by command for the AI as well. Periodically, the AI considers the various actions it can take, and for each it decides to do it’ll send a command. Usually this is the exact same command a player would’ve sent; the player and AI will both use the same command for “move this unit to this province” for instance. The AI and the player using the same system makes it easier for us to ensure the two play by the same rules. Even more importantly, that the same attempted action gives the same result, avoiding subtle bugs due to differences between how the AI and the player interact with the game. [The AI sending a command] There’s not that much more to cover about how the AI interacts with the game without going into far more detail of the AI systems themselves, which could easily be a dev diary of its own, so I’ll move on now. Evaluation and execution​All changes to the gamestate can be considered to have two main parts: deciding what to do (evaluation) and actually doing it (execution). In a large number of cases, the thing that takes the most time is to figure out what to do, not to actually do it. For instance, choosing which event to fire out of hundreds available in a yearly pulse takes longer than applying the event we decide upon. Generally speaking, we can only execute one thing at a time (otherwise we get out of syncs; more on that later). We can however evaluate multiple things at the same time by using threads. So instead of each character individually in a row deciding what events to fire, we can consider 8 or more (depending on how many CPU threads the player has) characters’ events simultaneously. Each character then adds the events they’re going to fire to a queue. This part has to be synchronized as we can’t add two things to a list at the same time, but since the vast majority of the time is spent on the evaluation rather than adding to the list, we save huge amounts of time by distributing the work. Later we can then go through the queue and fire each event, removing any that’s no longer applicable for whatever reason (maybe a character involved died?) along the way. This split between evaluation and execution is one of the cornerstones of how we do threading on CK3. The gamestate is split up into various “managers” that are each responsible for one part of the game. For example there’s a Secrets Manager, an Event Manager, a Character Manager, and a Title Manager. The main part of how we progress the game a single day is split into two parts; the pre-update and the main update. In the pre-update, each manager does its own evaluations and makes notes of things to do later. No visible gamestate is allowed to change, so each manager can safely look at things they don’t manage (E.G., the title manager is allowed to look at the holder of a title, even though it doesn’t own characters). Instead they can only change things that are invisible to the rest of the game (like that event queue mentioned earlier). [Time spent in the various pre-update managers] The split makes it very easy for us to thread things, as there’s only one rule to follow (don’t modify any visible state). The threading on our older game came with far more rules to obey (only look at your own data, don’t look at this thing, don’t modify this other thing, etc.), meaning that for experienced and new programmers alike it was easy to make mistakes. With only a single rule mistakes are harder to make, easier to catch, and easier to fix. As a result we’re more productive, and CK3 is our most threaded game to date. The AI works very similarly. It’s run after the main update rather than before it, but works on the same principle. The AI is not allowed to change anything except certain pieces of purely AI-internal state, and instead just sends commands. The AI is split up into a variety of sub-tasks, composed together based on a frequency basis. E.G., an individual AI will check whether it should change its laws and whether it should leave a faction in the same task, as these happen at the same frequency. Each such grouping of tasks can happen simultaneously with any other grouping of tasks. The granularity of this means that the threading of the AI is very effective (known as “good load-balancing”) as one thread is unlikely to finish its work significantly earlier than another thread (which would leave it idling). [The AI updating a set of tasks] As mentioned earlier, the use of the command system means that the effects of the AI are nicely isolated from its decision-making process. This makes it easier to iterate upon, easier to reason about, and easier to optimize. Now, let's move on to the final topic of today: out of syncs. Out of Sync​If you play multiplayer in any of our games you’re aware of a particularly dreaded set of words: “game is out of sync”. When this happens you’re unable to continue playing, and depending on the game have to either rehost or resync. But what is an out of sync (OOS), beyond us programmers having a laugh at your expense? [CK3 going out of sync] To explain what an OOS is, I first need to explain how multiplayer itself works. In most games out there, the core of how multiplayer works is that the server (or a player’s machine acting as the server, if it is peer to peer) will tell all the clients the state of everything in the game. Where everything is, where it’s moving, how much health it has left, etc. Left out is usually only things that are static (what the map looks like in many games for instance). Competitive games often also leave out things that the client would have no way of knowing (like the position of another player on the other side of the map) to combat wallhack cheats and the like. This is generally a very sensible model, but it breaks down if there’s too much gamestate to send over the network several times a second. In a first person shooter with 10, 20, maybe even 100 players all this info can be stored in a few kB, but CK3 for comparison usually has around 20 thousand characters, never mind everything else. The full gamestate of CK3 takes around 30 to 100 MB to store uncompressed, and even with compression you’ll easily pass 10-20 MB once you’re far enough in. Clearly, this is not something we can send over the network repeatedly. So what do we do instead? We use an architecture known as “lockstep multiplayer”. This is common for strategy games. How this works is that instead of telling clients the state of everything (or a large subset of everything), we instead first provide them the initial state (in the form of a save), and then each client runs their own simulation. We send commands for player and AI interactions; everything else each client will calculate on their own. As a result far less info is sent over the network, since we only need to inform the clients of things that deviate from the natural flow of the simulation. But here’s the problem: this means we have to ensure every single client simulates the game the exact same way. Because if anything differs, no matter how small, that tiny change will eventually Butterfly Effect its way to causing drastic differences between what’s happening on each machine. So while one player just got declared war on by some Vikings, on another client this wouldn’t be happening at all. When anything differs, that’s an out of sync. At this point, major breakage is inevitable, and so we tell the players and force a rehost. This isn’t a great experience for anyone, so it is something we work hard on avoiding. So how do out of syncs happen in the first place? It generally comes down to a lack of determinism. Determinism is when the same input always leads to the same result. As long as that’s the case, out of syncs are impossible (except if some input is lost or corrupted due to, say, network issues). But determinism isn’t easy. It is simple enough if your game is single-threaded, but then it’ll also be slow. Any threading can introduce non-deterministic behavior if you’re not careful. The most common way is due to order issues. Let's say you’ve got the number X. It has a value of 10. Thread A wants to add 2 to it. Thread B wants to multiply it by 2. If Thread A happens to run first, the end result will be (10 + 2) * 2 = 24. But if Thread B runs first, it will be (10 * 2) + 2 = 22. So if for any reason threads run in a different order on two machines (maybe one CPU core was busy with something else for a split second), an out of sync will occur. This is a big reason why we usually only multi-thread evaluation. If nothing is changed, then order doesn’t matter. We sometimes thread things that change visible state too, but that’s much rarer and we’re far more careful to ensure that ordering doesn’t matter. Another cause of out of syncs that was far more common in our older games, was the interface influencing the gamestate in some manner. To take a simple example, imagine we have some value we only rarely update because it is really time consuming to update. But when the player looks at it, we want it to be fully up to date. It might be tempting to force it to update when the player opens the interface but oops… now you’ve introduced an out of sync. The way we’ve structured CK3 makes it far more difficult to make this mistake, as it’s much harder to modify the gamestate from the interface. We’d instead send a command to refresh the value, and/or maybe do the actual math for the new value just in the interface and leave the gamestate untouched. Similarly, it’s easy to introduce issues due to bits of game logic depending on if a character is the local player or not. E.G., we want to update the player’s predicted income daily rather than monthly to ensure the player’s info is up to date. The naive implementation here would mean that on each client the client’s character gets updated daily, but the other players get updated monthly. The game would thus be out of sync, as the player characters would have different cached incomes. In CK3 we avoid this by just checking that they’re a player rather than the person playing on this machine. Furthermore, we’ve made it deliberately harder to check “is this the local player” than to just check “is this any player”. We still need the former quite a bit (primarily for sending notifications), but it involves the programmer basically going “yes, I’m sure I know what I’m doing here”: [A notification being sent to the local player] Note the “ALLOW_GET_LOCAL_PLAYER_IN_SCOPE” here; that’s our way of making sure we only check who the local player is if we really need to. Otherwise, we’d easily end up with something only getting changed on a player character for the client actually playing that character. So that’s the long and short of what out of syncs are, why they happen, and some of what we do to avoid them. And with that, I’m done. I hope you found this post about how our gamestate works interesting! I am on vacation today but Matthew (@blackninja9939) will be here to answer any of your questions about this topic as well! And I may check in too!

## Reply 2 — participant_002 · 2021-07-22 · post-27692711

When I read "command system" I had the faint hope that you would finally fix the issue, that denies us to activate and deactivate debug_mode during a running game. (as in console commands) Like in the old PDS games. But no, we still need mods for that. *sigh*

## Reply 3 — participant_003 · 2021-07-22 · post-27692715

<!-- artifact:quote:start -->
> Dsingis said: When I read "command system" I had the faint hope that you would finally fix the issue, that denies us to activate and deactivate debug_mode during a running game. (as in console commands) Like in the old PDS games. But no, we still need mods for that. *sigh* Click to expand...
<!-- artifact:quote:end -->
Those things are entirely unrelated and this is a tech post we're not going to be listing anything really new we're giving explanation and info on how the game works. We've explained the reason behind the debug_mode toggle a bunch before. It is a bit annoying but also seeing as its easy to enable via a startup flag and not something users need by default it is not a high priority to rework our checksumming system to make it work in game compared to doing literally any other feature or fix for the game.

## Reply 4 — participant_002 · 2021-07-22 · post-27692737

<!-- artifact:quote:start -->
> blackninja9939 said: Those things are entirely unrelated and this is a tech post we're not going to be listing anything really new we're giving explanation and info on how the game works. We've explained the reason behind the debug_mode toggle a bunch before. It is a bit annoying but also seeing as its easy to enable via a startup flag and not something users need by default it is not a high priority to rework our checksumming system to make it work in game compared to doing literally any other feature or fix for the game. Click to expand...
<!-- artifact:quote:end -->
Like I said, I thought "command system" was about console commands initially, that's why I wrote this to express my disappointment when I realized it's not. That's the only reason why I mentioned it here. I know the reasoning behind it, and I know it's easy to "activate" just not to "re-activate" it once you disabled it ingame, then you gotta restart the game. (if you don't want to play in constant debug_mode with pink debug text everywhere. But again, I wasn't trying to start a discussion, just to say: "oh I thought command system was about console commands, shame it's not" that's it.

## Reply 5 — participant_004 · 2021-07-22 · post-27692741

Who is God? What does it mean when God is OOS?

## Reply 6 — participant_005 · 2021-07-22 · post-27692753

<!-- artifact:quote:start -->
> Meneth said: When anything differs, that’s an out of sync. At this point, major breakage is inevitable, and so we tell the players and force a rehost. This isn’t a great experience for anyone, so it is something we work hard on avoiding. Click to expand...
<!-- artifact:quote:end -->
Is there a reason you rehost rather than just pause and have the host send everyone a full game state to resync? I guess if things are going off the rails, you'd expect that even after a resync, they'd quickly diverge again?

## Reply 7 — participant_001 · 2021-07-22 · post-27692774

<!-- artifact:quote:start -->
> PrDelahaye said: Who is God? What does it mean when God is OOS? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Tiax said: Is there a reason you rehost rather than just pause and have the host send everyone a full game state to resync? I guess if things are going off the rails, you'd expect that even after a resync, they'd quickly diverge again? Click to expand...
<!-- artifact:quote:end -->
Just the name of a player. The main reason is that it is a feature that has to be built, tested, and maintained. With OOSes being something we try to minimize, that can be a difficult value proposition, which is why only some of our games have it.

## Reply 8 — participant_006 · 2021-07-22 · post-27692783

Another great read! As modders, are there things we should be particularly aware of regarding desyncs? Either pitfalls to avoid, or good practice to abide by? Or can't we cause desyncs anyway because the failsafes code-side prevent us from doing so in the first place?

## Reply 9 — participant_001 · 2021-07-22 · post-27692815

<!-- artifact:quote:start -->
> Chatoustikmou said: Another great read! As modders, are there things we should be particularly aware of regarding desyncs? Either pitfalls to avoid, or good practice to abide by? Or can't we cause desyncs anyway because the failsafes code-side prevent us from doing so in the first place? Click to expand...
<!-- artifact:quote:end -->
If a mod's causing a desync, it's a bug in the game, not the mod. If we had any known pitfalls we'd patch them rather than alert you to them. Except an alert if such a patch is a ways off. There's definitely a non-zero chance there's things mods could do that'd cause a desync that isn't currently done in vanilla (or is much rarer). If a mod is causing a lot of desyncs, that's something we'd love bug reports on.

## Reply 10 — participant_007 · 2021-07-22 · post-27692913

That was informative, even to a non-programmer who only dimly envisions what you’re describing. Thank you!

## Reply 11 — participant_008 · 2021-07-22 · post-27692961

Again, I can't understand most of this, but it sure is interesting.

## Reply 12 — participant_009 · 2021-07-22 · post-27693050

I really love all these dev dairies. I have been coding for a long time and one of my personal fascinations are the whole game engine architecture, all of the tricks to gain more performance, the way multithreading is done. It's also great seeing some code snippets in these posts, because they are very clean with their variable names, it's good to look at

## Reply 13 — participant_010 · 2021-07-22 · post-27693168

re: AI and interface I've been curious, how does AI handle scripted guis? If, say, I add an sgui button to the county view, does AI "see" a button for every county they own? And would it be bad for performance? I'd really like to see a DD on AI, that sounds interesting.

## Reply 14 — participant_011 · 2021-07-22 · post-27693260

Honestly a really nice read for someone studying CS hoping to get into gamedev proper (not just modding) at some point. Really hope you guys continue the series for a while as there's so much I wanna ask about it's hard to pick any specific topic ^^

## Reply 15 — participant_001 · 2021-07-23 · post-27693570

<!-- artifact:quote:start -->
> Agamidae said: re: AI and interface I've been curious, how does AI handle scripted guis? If, say, I add an sgui button to the county view, does AI "see" a button for every county they own? And would it be bad for performance? I'd really like to see a DD on AI, that sounds interesting. Click to expand...
<!-- artifact:quote:end -->
The AI doesn't know about scripted GUIs unless you make an AI will do section for it. In which case, it is about equivalent to a decision. Note that what's available is just the AI character; not info from the interface. It's pretty limited. (This is based on a cursory look at the code; the scripted GUI system is something I have very little experience with so I might be wrong here)

## Reply 16 — participant_012 · 2021-07-23 · post-27693728

These posts are pure gold. When I read them and see that beautiful C++ and thnigs like the command system, I wish I had been given the opportunity in life to work on projects like these as my main job instead of just doing C++ as a hobby in my spare time.

## Reply 17 — participant_013 · 2021-07-23 · post-27694501

<!-- artifact:quote:start -->
> Meneth said: There's definitely a non-zero chance there's things mods could do that'd cause a desync that isn't currently done in vanilla (or is much rarer). If a mod is causing a lot of desyncs, that's something we'd love bug reports on. Click to expand...
<!-- artifact:quote:end -->
This is very good to know! Is there any particular kind of information that would be useful to provide in an mod game OOS bug report, or do you just want the oos folder logs directly? I imagine that going through what a given desyncing mod actually does would be a herculean task, but would you still want the full mod files (as they were at the time of the desync) included in a bug report? I recently got some oos logs submitted from my players and identified that the only distinction in the game state was that one province had a supply_limit_mult modifier of 0.25 and the other did not, but there's no information as to what is causing it. As far as I can tell the only static modifier that could achieve this on its own is the vanilla coastal_province_modifier modifier, but that is not utilized anywhere in script - neither in vanilla nor in the mod itself. I imagine relevant info for a modder to provide is stuff like the fact that this particular province is actually lacking pixels on the map (Its ID was allocated to a region for cartography work but it was never actually used) and so the question of whether it is coastal is actually poorly defined in this particular mod. View attachment 742645 Once I know what to include, I'll make a proper bug report.

## Reply 18 — participant_001 · 2021-07-23 · post-27694737

<!-- artifact:quote:start -->
> Tobbzn said: This is very good to know! Is there any particular kind of information that would be useful to provide in an mod game OOS bug report, or do you just want the oos folder logs directly? I imagine that going through what a given desyncing mod actually does would be a herculean task, but would you still want the full mod files (as they were at the time of the desync) included in a bug report? I recently got some oos logs submitted from my players and identified that the only distinction in the game state was that one province had a supply_limit_mult modifier of 0.25 and the other did not, but there's no information as to what is causing it. As far as I can tell the only static modifier that could achieve this on its own is the vanilla coastal_province_modifier modifier, but that is not utilized anywhere in script - neither in vanilla nor in the mod itself. I imagine relevant info for a modder to provide is stuff like the fact that this particular province is actually lacking pixels on the map (Its ID was allocated to a region for cartography work but it was never actually used) and so the question of whether it is coastal is actually poorly defined in this particular mod. View attachment 742645 Once I know what to include, I'll make a proper bug report. Click to expand...
<!-- artifact:quote:end -->
Chances are that we would need to reproduce it internally in order to deal with it. So any info on how to reproduce it would be helpful. If the saves only have minor differences there's a chance that can be useful, but most of the time we need to reproduce OOSes internally to deal with them. We'd want the mod files, yes. That very specific modifier difference does sound pretty intriguing, and might be enough of a starting point for us to investigate.

## Reply 19 — participant_014 · 2021-07-23 · post-27695168

Thanks for the post. Soo interesting! : ) Please do keep posting!) "We send commands for player and AI interactions" I wonder why AI interactions are sent over. With so many AI players this seems like a lot of data to transfer. Given I have a particular game state And I launch two game instances with the same state When I execute a particular set of player-commands on each game instance And next evaluation happens Will the generated AI commands on one instance differ from those on the other? In a single player game, I know the game is never the same even if I perform the same set of actions. I assume there is some randomness involved to spice the game up. But if a "randomness key" could serve as an additional startup/day input, and all random evaluations are run against that key, one can get the same result. Or so I think : )

## Reply 20 — participant_015 · 2021-07-23 · post-27695206

Thank you for the informative post. As a programmer I appreciate your candor. Using commands is something I remember from a game framework I made nearly 25 years ago when writing code for a Diplomacy (the game) applet.

## Reply 21 — participant_016 · 2021-07-23 · post-27695242

Thanks for the explanation. If I'm understanding this correctly if I ransom a character back to another ruler in multiplayer, then a command to change the game state would only fire when the other ruler accepts my ransom demand. And if the other rulers is AI then this all happens on my computer (until the command is sent out), while if the other ruler is a player they'd be sent a notification to respond to. Did I get that correct?

## Reply 22 — participant_001 · 2021-07-23 · post-27695271

<!-- artifact:quote:start -->
> pengoyo said: Thanks for the explanation. If I'm understanding this correctly if I ransom a character back to another ruler in multiplayer, then a command to change the game state would only fire when the other ruler accepts my ransom demand. And if the other rulers is AI then this all happens on my computer (until the command is sent out), while if the other ruler is a player they'd be sent a notification to respond to. Did I get that correct? Click to expand...
<!-- artifact:quote:end -->
You sending the interaction is one command. The other ruler accepting is another if they're a player. If they're an AI, acceptance is handled without a second command.

## Reply 23 — participant_016 · 2021-07-23 · post-27695276

<!-- artifact:quote:start -->
> Meneth said: You sending the interaction is one command. The other ruler accepting is another if they're a player. If they're an AI, acceptance is handled without a second command. Click to expand...
<!-- artifact:quote:end -->
Okay thanks. That makes sense.

## Reply 24 — participant_017 · 2021-07-24 · post-27696296

This was really fascinating. Thanks for posting it.

## Reply 25 — participant_018 · 2021-07-25 · post-27696955

<!-- artifact:quote:start -->
> Dsingis said: When I read "command system" I had the faint hope that you would finally fix the issue, that denies us to activate and deactivate debug_mode during a running game. (as in console commands) Like in the old PDS games. But no, we still need mods for that. *sigh* Click to expand...
<!-- artifact:quote:end -->
Logged in just to upvote this. It really is disappointing to a player who is used to quickly toggling debug on and off in various PDX games. It wouldn't matter for achievement hunters but it really is strange how CK3 (such a roleplay focused game) doesn't allow us to freely tweak some things as we play like many of the other games, and forces users to fall back onto mods to do basic things I am amazed at how the game was released without a console (that's able to be conveniently used without having to completely close the game). Is this a nit-pick? I don't know. It's something I use very often so I may be biased.

## Reply 26 — participant_019 · 2021-07-25 · post-27697636

Thanks for the post! This is super insightful. Any chance you can tell something about how the map is displayed visually in-game? Though I'd understand, if that is something Paradox would rather keep to itself!

## Reply 27 — participant_020 · 2021-07-25 · post-27697802

I really appreciate the transparency and it certainly helped me understanding the challenges in managing a massive game state like CK3 and why OOS occurs even as a non-programmer (though with strong technical affinity).

## Reply 28 — participant_021 · 2021-07-25 · post-27697946

On the topic of desyncs: my friend and I are experiencing desyncs maybe every 50 years or so in our two-player game. We’ve been trusting that using the multiplayer beta is enough to make sure you get adequate information about the problems we encounter. Is this a safe assumption?

## Reply 29 — participant_022 · 2021-07-25 · post-27697981

Desyncs have plagued paradox games of the past, like in hoi4 (also happens far too often in similar in games like Civ). Nice to see that it's much less of a problem in CK3, and cool that you're explaining how it happens. Multiplayer adds a new dimension to the games

## Reply 30 — participant_017 · 2021-07-25 · post-27698152

Having thought about this, I've got three technical questions: In multiplayer, how do you deal with different computers having different amounts of computing power? On an older, slower machine those evaluation calculations are going to take longer and have fewer threads to spread the work across. So how do the games sync up the update step to a heartbeat so that everyone stays on the same date? As far as updating the game state, did you consider and reject a design where the change sets are check-pointed and then committed using transactional memory? Or is the update step so quick that it just isn't relevant for performance? Since so much time is spent on doing the update calculations, do you compile the game scripts into byte-code or some other internal data structure in order to keep the interpreter from becoming a bottle neck?

## Reply 31 — participant_023 · 2021-07-26 · post-27698349

<!-- artifact:quote:start -->
> contentand said: Given I have a particular game state And I launch two game instances with the same state When I execute a particular set of player-commands on each game instance And next evaluation happens Will the generated AI commands on one instance differ from those on the other? In a single player game, I know the game is never the same even if I perform the same set of actions. I assume there is some randomness involved to spice the game up. But if a "randomness key" could serve as an additional startup/day input, and all random evaluations are run against that key, one can get the same result. Or so I think : ) Click to expand...
<!-- artifact:quote:end -->
Yeah, this part was left out, or if it wasn't I didn't fully understand it. The "easiest" implementation would be to just have one PC (the host's machine) do all the AI decisions, then pass that data to all the other players. Otherwise I don't have a clue how you could ever keep the gamestate sane, even if you tried to make the majority of the processing deterministic; eventually you'd have the same AI entity (character, army, or whatever) on two machines making a different decision at the same time.

## Reply 32 — participant_024 · 2021-07-26 · post-27698510

This is probably not for general audience but the article is very informative and enlightening. I highly appreciate it. "day" can be easily translated into "turn" making the engine perfect for turn-based character-centered simulation. I look forward to more of these tech blogs.

## Reply 33 — participant_003 · 2021-07-26 · post-27698598

<!-- artifact:quote:start -->
> Daniel Brauer said: On the topic of desyncs: my friend and I are experiencing desyncs maybe every 50 years or so in our two-player game. We’ve been trusting that using the multiplayer beta is enough to make sure you get adequate information about the problems we encounter. Is this a safe assumption? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> MHC said: Having thought about this, I've got three technical questions: In multiplayer, how do you deal with different computers having different amounts of computing power? On an older, slower machine those evaluation calculations are going to take longer and have fewer threads to spread the work across. So how do the games sync up the update step to a heartbeat so that everyone stays on the same date? As far as updating the game state, did you consider and reject a design where the change sets are check-pointed and then committed using transactional memory? Or is the update step so quick that it just isn't relevant for performance? Since so much time is spent on doing the update calculations, do you compile the game scripts into byte-code or some other internal data structure in order to keep the interpreter from becoming a bottle neck? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> gamerk2 said: Yeah, this part was left out, or if it wasn't I didn't fully understand it. The "easiest" implementation would be to just have one PC (the host's machine) do all the AI decisions, then pass that data to all the other players. Otherwise I don't have a clue how you could ever keep the gamestate sane, even if you tried to make the majority of the processing deterministic; eventually you'd have the same AI entity (character, army, or whatever) on two machines making a different decision at the same time. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> jiruoan said: This is probably not for general audience but the article is very informative and enlightening. I highly appreciate it. "day" can be easily translated into "turn" making the engine perfect for turn-based character-centered simulation. I look forward to more of these tech blogs. Click to expand...
<!-- artifact:quote:end -->
Make sure to go and leave a bug report with your out of sync's information and dump to! If someone lags behind too much we slow down the speed selected for the whole session or even pause to let them catch up, with our min spec and not entirely useless internet you should be able to run at a decent speed in an MP session with that. The effects of most commands is not the bottleneck of our simulation, its much more the general daily tick of the simulation instead of any specific command actions. They are read in once into internal data structures at load time and then we just go over them for evaluation and execution never needing to go back to the file system or interpreting the scripting language. Exactly this, which is why they use the commands. Only the host machine actually posts the AI commands to the session which then update the rest of the clients with the AI's actions. I mean there is not a huge amount of difference between real time with pause and turn based anyway in that regard, both end up in the scenario where there is a hypothetical infinite amount of time between the updates so have some tick based system. Real time with pause just does it as ticks at an interval whereas turn based is tick on demand only. There is plenty of gameplay considerations of course, and you'd want to work your updates differently, but the very core is not massively worlds apart.

## Reply 34 — participant_017 · 2021-07-26 · post-27699150

Thanks for the answers. I hope you make more of these types of posts, they are very insightful.

## Reply 35 — participant_025 · 2021-07-26 · post-27699363

When Paradox had no free community manager, so they put a coder to entertain people.

## Reply 36 — participant_020 · 2021-07-26 · post-27699434

<!-- artifact:quote:start -->
> Col. W. T. Philmore said: When Paradox had no free community manager, so they put a coder to entertain people. Click to expand...
<!-- artifact:quote:end -->
I'm ok with this.

## Reply 37 — participant_003 · 2021-07-26 · post-27699575

<!-- artifact:quote:start -->
> Col. W. T. Philmore said: When Paradox had no free community manager, so they put a coder to entertain people. Click to expand...
<!-- artifact:quote:end -->
Well our community team aren’t writing our regular dev diaries or summer teasers either They have the much less fun job of listening to my dumb ideas and collecting feedback and managing the socials and planning Though thankfully Troy was very receptive and excited when I pitched this idea to him, both cause he’s nice and doesn’t want to kill my hopes and dreams and cause it’s a new type of content for us we can explore different areas of the game and our roles to those who are interested!

## Reply 38 — participant_026 · 2021-07-27 · post-27699913

This was a really cool dev diary, albeit, I couldn't understand most of it it is interesting!

## Reply 39 — participant_027 · 2021-07-27 · post-27700646

Amazing post overall. Just not sure if you really want to repost it to Steam.

## Reply 40 — participant_028 · 2021-07-27 · post-27701155

Keep these series going

## Reply 41 — participant_029 · 2021-07-30 · post-27706042

Paradox, Thanks for your hard work on a game we all love. Keep it up! NolaSaint

## Reply 42 — participant_030 · 2021-08-12 · post-27728506

<!-- artifact:quote:start -->
> Meneth said: The interface is only able to read the gamestate, and this is enforced by the code systems we have. Click to expand...
<!-- artifact:quote:end -->
Out of curiosity, how do you enforce this? If another system wants to get data from the game state, can it just read that data directly? If so, assuming you're passing by reference, could the outside system then (inadvertently, perhaps) write directly into the game state?

## Reply 43 — participant_003 · 2021-08-12 · post-27728637

<!-- artifact:quote:start -->
> Splorghley said: Out of curiosity, how do you enforce this? If another system wants to get data from the game state, can it just read that data directly? If so, assuming you're passing by reference, could the outside system then (inadvertently, perhaps) write directly into the game state? Click to expand...
<!-- artifact:quote:end -->
The function to get write access to the game state is not compiled into the interface module, so through using the "proper" functions you cannot get write access to data unless you start const casting things at which point all bets are off and you should feel bad anyway. So its super hard to do accidental writes to the game state from the interface module.

## Reply 44 — participant_030 · 2021-08-13 · post-27731125

<!-- artifact:quote:start -->
> blackninja9939 said: The function to get write access to the game state is not compiled into the interface module, so through using the "proper" functions you cannot get write access to data unless you start const casting things at which point all bets are off and you should feel bad anyway. So its super hard to do accidental writes to the game state from the interface module. Click to expand...
<!-- artifact:quote:end -->
Interesting! If the interface wants to fetch and display some state variable (e.g. character gold, or something), what's the official way to get it? Does the state module expose safe getter functions that return read-only versions of the various parts of the game state?

## Reply 45 — participant_003 · 2021-08-13 · post-27731266

<!-- artifact:quote:start -->
> Splorghley said: Interesting! If the interface wants to fetch and display some state variable (e.g. character gold, or something), what's the official way to get it? Does the state module expose safe getter functions that return read-only versions of the various parts of the game state? Click to expand...
<!-- artifact:quote:end -->
Yeah it uses the read only function to get a read only version of the game state so it can get read access to everything

## Reply 46 — participant_031 · 2021-08-17 · post-27738752

This is an amazing post! I think I understand, but i think I have conflicts in my understanding. 1. There’s an initial phase during which all players are simultaneously deciding what to do for the next update, and it might include decisions which are made daily, monthly, yearly, whatever. This phase also includes updating UI. It’s a read-only phase. 2. The next phase allows actions that alter the game state to be carried out. Actions which are no longer valid are skipped. During phase 1, if there’s an action that impacts game state that’s only visible to the one character, then it gets triggered immediately instead of getting added to the queue which is executed during phase 2. Do I have that right? thanks again, really insightful post!

