---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1484918/"
forum_thread_id: 1484918
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "Anatomy of a Game: The Script System"
dd_date: 2021-08-05
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
body_word_count: 4790
inline_image_count: 9
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1484918'
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
    location: raw_lines_399_to_401
    action: preserved_and_flagged
    counts:
      Like: 31
      (unlabeled — rendered as base64 data URI): 15
      Love: 7
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_478_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Anatomy of a Game: The Script System

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [Aug 5, 2021](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/)
- [2](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/page-2)
[Next](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/page-2)

1 of 2

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/page-2 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/?prdxDevPosts=1)

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

- [Aug 5, 2021](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/post-27715913)


- [/forum/threads/anatomy-of-a-game-the-script-system.1484918/post-27715913](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/post-27715913)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27715913/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/anatomy-of-a-game-the-script-system.1484918/post-27715913)

Hello everyone and welcome back to Anatomy of a Game. I’m Matthew, a programmer on Crusader Kings 3. Today I am going to be talking about the Script System and how it works to let our Content Designers and modding community create their wonderful events and mechanics.  

Firstly I am going to discuss the reason we even have this system and its soft goals for usage and how we grow it over time.  
Then I will go into the implementation behind it and how we use it both from the game team side and the more foundational library side of it in Jomini which is our shared grand strategy library we use alongside our Clausewitz engine.  


## The why​

So why do we have this, you saw me last week complaining about the performance of it so gotta be a good reason we have it right?  

It is much quicker to change things in script and makes those changes easier to maintain in a controlled environment. It also is generally easier to use a controlled scripting language than make everyone learn how to code in C++. We’ve got a wide set of roles on the team and forcing all of them to also be programmers to do small changes would be crazy,  
So we want some reasonably straightforward way for people to add new things without needing to know C++ and edit and recompile the game. This is very common across most games and engines.  

Our key goals with the the scripting language is:  


1. Help our Content Designers do their job
2. Straightforward plain english with minimal complex syntax
3. Easy to extend with new content and features over time
4. No foot guns, one should not be able to cause catastrophic issues from the script

Really everything is just a subset of goal 1 there but it's good to list some more concrete things. For our scripting language specifically it's sort of evolved over time, it bears some superficial similarities to JSON but predates it by a few years and is less formally structured, which can be a blessing and a curse.  
We have full control of it but it's also unique to us so nobody comes pre-trained in it and how we operate with it nor is it formally structured enough that there isn’t a delightful set of edge cases. One of our Content Designers likes to describe it a bit like the American legal system, a whole lot of case law and precedents set as opposed to a more well codified instruction set.  

And you’ll also notice that I’ve not mentioned modders in those bullet points, and the reason for that is whilst we do want our modding community to use this and we regularly add things for them specifically it is never to be things that come at the cost of the key goals. I’ve received a lot of mod requests for things we could add but would complicate the language to a large extent making it harder for our Content Designers and coders to reason about its setup. That isn’t to say just because it isn’t used in vanilla means we shouldn’t add it, but we’ve got to keep our key goals in mind that this language exists for a specific job not to be some generic game making tool as there are other pieces of software dedicated to that task.  

So with that out of the way let's jump into some more details about our scripting language internals specifically.  


## What is a scope?​

A scope is pretty simply just some game object such as a character, province, or faith. Each scope object is basically an instance of two values: scope type and identifier. The scope type is some number that represents if it is a character or province and then combined with the identifier we can then work out which specific object is represented by the scope.  
So a scope object with type 5 and id 50 might be the King of England, whereas a scope with type 6 and id 50 could be Paris.  

When do we make something a scope type then? That is also pretty simple, it needs to fit the following rules generally:  


- Read data from it (evaluate triggers)
- Write data to it (execute effects)
- Move from one object to another (links and lists)

If it doesn’t meet at least two (preferably all 3) of these requirements then making it a scope type is an overhead and burden we would prefer not to do so.  

Implementing something as a scope type is mostly tying it into a few places, we have conversion functions to go back and forth between the abstract scope object and a real game object, this is where we tell it that type 5 means character and how to use id 50 to find a character. For most of our gameplay objects they use a system where each object has an id, so we must look up that object at that id and get the real game object.  

Now there are some exceptions to this rule, namely what we call the primitive scope types. That is things like boolean values (yes/no), numbers (4/2.5), and flags (flag:cool_flag). They are special in that they do not meet any of the previous requirements and are instead simply the piece of raw data themselves as they are so simple, so their ID is actually a raw representation of their information.  
Why are these primitives even scopes? Mainly to make things easier, it means when we want to store a scripted variable on a character we can use the exact same mechanism for storing and comparing some number as we do for storing their favourite teddy bear’s name as we do for storing the character they owe money to in some event.  

![1628166095643.png](https://forumcontent.paradoxplaza.com/public/733239/1628166095643.png "1628166095643.png")


## Changing scopes​

There are two ways of changing scopes, a 1-1 link and a 1-many list. An easy example being liege-vassal relations as a character has one direct liege but can have multiple vassals to whom they are the sole direct liege.  

For 1-1 changes you can chain multiple of these links together for example to get to your father’s father (your paternal grandfather) in one jump. In our backend near everything taking some object from script lets you do these multiple chaining of links so you don’t need to have cursed things like CK2’s big prevprevprev chains or constructs like root_fromfrom if any of you modders remember that bit of suffering.  

![1628166152858.png](https://forumcontent.paradoxplaza.com/public/733241/1628166152858.png "1628166152858.png")



You can also save a reference to a scope object with a given name to then use later in an unbroken context (more on these contexts later) which lets you save a more complex chain of links into one simpler named thing for a direct lookup. We do this liberally in vanilla since often a named thing is easier to understand than a long chain of links, this is also what we use when we set up the things involved in an on action so that scope:actor and scope:recipient are specific things with a name and meaning instead of just pushing everything into root, from, and fromfrom etc like CK2 did.  

Lists operate in a similar fashion, you use some list name in a trigger or effect and it will iterate on all things meeting the criteria. In our backend we only register a list builder which then generates the any_xxx, every_xxx, random_xxx and ordered_xxx versions of it so that every list can be used in the same manner everywhere which removes the issues our older games sometimes had of missing one of those types despite the logic in theory being the same everywhere.  

![1628166279468.png](https://forumcontent.paradoxplaza.com/public/733244/1628166279468.png "1628166279468.png")


## Triggers and Effects​

Onto the meat of the script system: our triggers and effects.  

These really are the core of it as they give you a way to check and modify different objects, in code they are fairly simple to register as they mostly just map to calling a specific function on the object type as we aim to avoid doing complex logic directly in the triggers and effects so they don’t diverge from the logic we do in code (though there are some exceptions of course). The rest of the code for them is a standard bit boiler plate to register them correctly.  

![1628166328322.png](https://forumcontent.paradoxplaza.com/public/733245/1628166328322.png "1628166328322.png")



Implementation wise they use dynamic polymorphism, which is just a fancy way of saying one type can dispatch to do different things. Jomini only knows it's storing a collection of triggers, only at run time when it tries to evaluate one does it then figure out it's specifically an is_alive trigger.  

Registering them is all well and good but we need to use them. We read in triggers and effects as part of our database objects which will just try to match what you typed to the list of registered things, if it cannot find the specifically named thing then it tries to see if it's a dynamic thing.  
To make my paternal grandfather example from before, we do not register a specific trigger called “father.father” we just see that nothing matches that so then one of our dynamic fallbacks is seeing does this text fit the pattern to be a scope change which it does so make an instance of that trigger with the broken up scope change to traverse.  
If it had not met that pattern then we would see if it's a scripted trigger and make an instance of the scripted trigger type with a reference to that specifically named one.  

Once we’ve read them in then we're done with the actual text files and just use what we’ve got now in memory. From there it is up to the code to decide when to actually use this data.  

We build some context for the usage, called a top scope, which contains the root object, a random seed, and optionally a group of saved scope references as I spoke of before.  
Then pass that context into the trigger and effect, for triggers we get a return boolean of if the evaluation was true or not and for effects we just execute their contents directly.  
This ties into what Meneth mentioned in the “Changing the Gamestate” post, triggers are just reading information so we can do these in parallel very easily with other triggers whereas effects must be executed serially as they can touch all manner of information throughout the whole game.  

![1628166415394.png](https://forumcontent.paradoxplaza.com/public/733246/1628166415394.png "1628166415394.png")



Another aspect of these is the visual side in tooltips, we need to tell you what is going to happen or why you cannot press that button after all. At a high level it works the same as running them for execution, we pass in some context and get some output.  

For effects it is simplest, we pass in the context and if it's something that has already happened and then we build up the text description of what will or has happened based on the context. So which character that decision will kill or how much gold you paid for something in some notification.  

Triggers are more complex to build up as we have to keep track of the logic inversions and groupings of going through all these nots, and ors as well as recording which things you passed or did not pass to show in different ways as most of the time we just want to show you what you are missing but sometimes we want to show you the full breakdown of the trigger including things you do fulfill.  

With both of them though they undergo a simplification process to try and make the breakdown in text look nicer, we skip redundant information such as entirely hidden contents and try to condense down repeated actions to one object into a group. As we want to show things happening to the player in the first person: “I will lose 50 gold” and “I need at least 50 piety” Whereas for other characters we want to group repeated actions so instead of saying:  
King John will lose 50 gold  
King John will lose 100 piety  
King John will lose 100 prestige  

We can show combined:  
King John:  
Will lose 50 gold  
Will lose 100 piety  
Will lose 100 prestige  

So that we reduce redundant information and keep related things together.  


## Events and On Actions​

Events and on actions are where a large amount of triggers and effects get used, they make up the foundation of content and narrative in CK3 weaving together little stories into your overarching narrative of each character and ruler.  

The events themselves are from the code side rather straightforward, it is what one does inside of them in script that brings complexity, as all we do is read in the various information like requirements and text and the options and give them a pretty display in game.  

Unlike in CK2 events do not trigger themselves by being regularly polled to see if they can, it was a performance drain, interruptive and made dispersing content nicely difficult so it has long since been removed and instead we use on actions for everything so that most content feels more like it comes from set actions or scenario you are in and paced a bit better.  

On actions are one of the main ways we communicate from code to the script, we notify that something has happened such as the year ticking over or a character being born and then script can jump off from there to run content. An on action can contain various groupings of events and other on actions to run to pick out what content is needed.  
From the code side adding a new on action is incredibly easy, we just register it with a name and then call for that on action in the appropriate place with a top scope containing the relevant information passed in.  

![1628166458189.png](https://forumcontent.paradoxplaza.com/public/733247/1628166458189.png "1628166458189.png")


![1628166568359.png](https://forumcontent.paradoxplaza.com/public/733248/1628166568359.png "1628166568359.png")


## Modifiers​

Key values we need to check are a big part of the game, we use modifiers as the system for this so we can get out things like a character's diplomacy or advantage in combat from multiple sources in one place.  

At the start of July I overhauled the internals of our modifier system to be better divided which will make explaining their parts a bit easier as the word “modifier” is one of the most overloaded words in our script system (the other being flag). But hopefully I can explain our divide a bit better now!  

In code we register what is called a modifier definition which contains some constant identifier (we use an enum since it's mostly a finite set) and then a token that is used in the script side to link to that modifier definition.  
This definition contains information about how we treat and display values for it, such as if it's a boolean or not and how many decimal places it should show or if it should be considered good or bad to have more of this value. Previously we did this formatting in code but as part of the rework it is exposed to script now so that adding or removing a decimal place now doesn’t need code time.  

![1628166596759.png](https://forumcontent.paradoxplaza.com/public/733249/1628166596759.png "1628166596759.png")



Everything that the script deals with is called a modifier instance which is a group of pairs of definitions and values. So when you define the effects of having say the majesty focus selected to be adding diplomacy and monthly_prestige it is reading that into an instance.  
We rarely operate on instances directly since getting values from them is often not particularly useful as they are static data, we do often build tooltips from them however so that we can list all the changes that they will cause from something like a focus or a trait.  

Under the hood we store them as two sorted arrays of modifier definition and value. They are sorted such that the index into the definition array matches the index into the value array to get the value for that definition.  
We do it like this instead of using something like a hashmap because we have a lot of modifier instances around in the game from a lot of sources and do not want the overhead of the hashmap’s bookkeeping. We have them sorted since then we can use the faster binary search instead of linear search to get data out of them to make up for not having them in a hashmap. Though after the rework that may change if the overhead looks to not be too bad any longer.  

Modifier collections are what each character has that determines the values we get. It contains references to all the modifier instances that are its sources as well as a cached instance representing the total of all the applied modifiers.  

The key invariants we have with a modifier collection is that every single instance added to it must have a stable memory address and a name we can display from. We require a stable address because we do not want to copy all this data around, most modifiers do have a stable location anyway as they come from some scripted database which is stable, for those that do not then we give them a stable address through other means such as in an array we do not resize or from an allocator that provides stable storage.  

We rebuild this when we have to if some operation has marked it dirty, as rebuilding it is not the fastest thing as it's a lot of data we just flag modifiers as dirty and rebuild on the next day instead of having every operation rebuild it right away as generally it being a bit out of date is not a large concern.  
There are some exceptions to this mainly centered around the player, as they will notice values about their character being out of date. So for the player we will flag it as dirty with a priority so that at the end of the next command posted we rebuild it which keeps the player up to date. Sometimes we will apply this prioritized behaviour to other characters if it's in a player interaction with them where they will notice it being wrong very quickly too.  

When building tooltips for the collections we do not dump out the entire thing but we get the values for a specific modifier definition and list its sources. This is why we assert that every instance added must have a name set, otherwise if we later try to get it we’ll have no idea where it came from and what values it is meant to represent which can lead to some very useless tooltips.  

![1628166666220.png](https://forumcontent.paradoxplaza.com/public/733250/1628166666220.png "1628166666220.png")



And that concludes our quick tour of the script system! Thanks for reading!

 

Toggle signature

Former Senior Programmer on Crusader Kings 3  

My mostly empty [Twitter account](https://twitter.com/Matt_Clohessy)

<!-- artifact:reactions:start -->
- 31 Like
- 15 (unlabeled — rendered as base64 data URI)
- 7 Love
<!-- artifact:reactions:end -->
