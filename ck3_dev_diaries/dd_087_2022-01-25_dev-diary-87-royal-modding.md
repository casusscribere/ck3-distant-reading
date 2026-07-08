---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1507899/"
forum_thread_id: 1507899
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 87
title: "CK3 Dev Diary #87: Royal Modding"
dd_date: 2022-01-25
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
body_word_count: 2198
inline_image_count: 8
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1507899'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1843.jpg?1643103083
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_345_to_350
    action: preserved_and_flagged
    counts:
      Like: 104
      Love: 60
      (unlabeled — rendered as base64 data URI): 1
      Haha: 5
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_358_to_457
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_458_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1843.jpg?1643103083)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #87: Royal Modding

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [Jan 25, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-87-royal-modding.1507899/)
<!-- artifact:thread_metadata:end -->

Hello everyone and welcome to the 87th CK3 Dev Diary!  

I’m Matthew, one of the Programmers on the CK3 team, and today I am going to talk to you about a variety of improvements and changes we’ve done to modding for the 1.5 patch which will be accompanying the Royal Court Expansion.  

We’ve added a variety of mod support in 1.5 so I’m not gonna cover everything, but I will give a few big ticket items that will let mods do a lot more fun custom things as well a few smaller fun ones. I’ve also attached the output of script_docs on 1.5 at the end so modders curious about the new triggers and effects in game can get a bit of a sneak peek for the release.  


## The Royal Court​

Of course the Royal Court itself is open to mods, it is all defined in the gfx/court_scene folder though the majority of the complex scene_settings itself is best built using the in-game editor that we are shipping with the court scene. It lets you position and change objects and switch between different settings much faster than trying to edit them all by hand.  

Trust me, cause I remember the time whilst the editor was work in progress and doing changes by hand crushed my soul.  


![The in-game editor tool for the royal court 3d scene](https://forumcontent.paradoxplaza.com/public/785656/court_scene_editor.png "The in-game editor tool for the royal court 3d scene")


I am not going to go into a huge amount of detail on the royal court modding because it is actually pretty straightforward with the editor, you position things and pick the assets you need for a configuration and then it just puts things there.  

One aspect I will go into a bit more info on quickly is the character positioning, because the rest of the positioning is set within the editor but the characters are not positioned individually because of course not every court has the King of England to reference.  

Instead the character positions are given a set of valid roles, and you pick a position where someone who has one of those roles may go. For example the two guards you see in the back are two positioned instances of the guard and knight role, which has a variety of rules of who it should pick.  

If you have a bodyguard or champion court position appointed for example then it tries to use them as a special guard, but if you do not then it will fallback to picking any of your knights instead. You can also have some more special roles such as if you have a court jester or poet appointed then they can show up in your court too.  


![The script for the poet court scene role](https://forumcontent.paradoxplaza.com/public/785671/poet_court_scene_role.PNG "The script for the poet court scene role")



Characters can not show up in multiple different roles and it is a “greedy” picking of first come first served in who is taken up, but you can write some fairly complex rules to decide who can go where as well as what animations they can choose from!  


## Same-Sex Marriage​

Coming with 1.5 is support for same-sex marriage, not only just in mods either but as a new game rule alongside the Same-Sex relations game rule so you can use it in un-modded games too. We've updated a variety of AI logic and interactions and content to take that into account when playing.  


![Same-sex marriage between the Duke of Brittany and his husband](https://forumcontent.paradoxplaza.com/public/785659/same_sex_marriage.png "Same-sex marriage between the Duke of Brittany and his husband")


Mods are of course able to implement this into their different worlds without it having to be a game rule, it can be based on different cultures or anything in the game world at all.  

This is something that we’re very happy to be able to put into the game and have support in the game rules for unmodded games too, it is something that a lot of the team and community wanted and we are glad it is finally going to be shipped in 1.5.  


## Scripted Widgets​

CK3 is one of our most moddable games yet, not just in terms of the content that can be added but the system's mods can script. And our new UI system is the most open we’ve had in terms of what custom UIs mods can add and edit, but one issue it had was letting you add brand new things entirely and keeping compatibility nicely.  

In 1.5 there is a new system called “scripted widgets”, what they allow for in essence is a mod to define their own brand new windows in the gui files and then add an entry into the gui/scripted_widgets folder with the name of their gui file and the main window.  

For example:  
gui/test_custom_widget.gui = my_first_cool_test_widget  
gui/test_custom_widget.gui = my_second_cool_test_widget  

Then with that simple line of script their window will appear in the game in the same way any of the windows we support in code do. Now of course there are some limitations, the windows do not have any special data context like a code one does but it can access anything that is set globally or on the local player character which covers more than enough cases normally.  


![A scripted widget making a new example window with a testing button](https://forumcontent.paradoxplaza.com/public/785660/scripted_widgets.png "A scripted widget making a new example window with a testing button")


This may not sound hugely impactful, but it means that mods going forward can easily create large systems which can then more easily be compatible with other mods that add systems or if they feel brave enough even with larger Total Conversions if they do not cross over in incompatible design choices.  

I am really excited to see the new UIs that mods end up making for their gameplay systems and getting to try a few different mods together. Hopefully their windows have a bit more functionality and effort put into it than my testing one…  


## Value Breakdowns​

Another bit of UI functionality that mods could not nicely mimic is getting breakdowns of their numbers in the same way we break down a value like your prestige income or how much piety it’s gonna cost to start that war in their own UI.  
In 1.5 we’ve added the GetScriptValueBreakdown UI function which lets you specify the name of the script_value you want to break down and the scope context to do it on and it gives you the exact same data as if we’d natively done it from code.  

For example in my custom widget I’ve made the button tooltip give a breakdown of the cost if I were to increase my crown authority entirely separate from the usually needed button to evaluate that cost in the realms UI.  


![Example of custom value break downs in custom UIs](https://forumcontent.paradoxplaza.com/public/785661/value_breakdowns.png "Example of custom value break downs in custom UIs")


We hope this will let mods better explain their own custom values in a more clear way, be that something like your mana in a fantasy mod or custom score for a special event chain.  


## Events and Localization​

To make life easier for our modders and designers to work with events we’ve added and reworked a few debug buttons in the event window.  
Now every event has these five icons in the top right corner.  


![The 5 debug icons in the event window](https://forumcontent.paradoxplaza.com/public/785658/event_utils.png "The 5 debug icons in the event window")


In order they let you:  


- Regenerate the event contents, useful if you’ve changed something that cannot hot reload.
- Toggle the data system globally, this makes most everything in square brackets show exactly what you typed instead of localizing to some output, this is available via the console commands too
- Copy the event text to your clipboard
- Shows you the trigger evaluation that had to be true for you to get this event
- Debug info about the current scope context and how keys used to build the description
We’ve found that having easy access to these makes it a lot simpler to debug events and iterate on content.  

Though do be warned that toggling off the data system can give you some truly cursed looking windows since now instead of seeing the number 4 you see the joyous underlying constructs such as this monstrosity of a window:  


![The character window with the localization data system disabled showing the raw function calls](https://forumcontent.paradoxplaza.com/public/785657/disabled_data_system.png "The character window with the localization data system disabled showing the raw function calls")


In a more mechanical improvement we’ve also added a boilerplate reduction for having events on a cooldown, instead of needing to manually check and juggle flags and variables yourself you can now specify a cooldown on the event in days/weeks/months/years as some value and it will automatically handle applying a flag that will clear after that time blocking the event from being fired on a character.  


## Console Commands​

We have added a variety of new console commands in 1.5 to help make creating and testing mods a bit easier, and instead of explaining them myself I am just gonna cheat and rip their change log entries out!  


- Added console command "bypass_requirements" (alias "bypass") that lets you do decisions, interactions, schemes, laws, and title creation despite the requirements not being met
- Added console command "instasiege"
- Added console command "save_every" and startup parameter "-save_every=x". These will make a save every x years, and ensure they do not get overwritten by normal autosaves
- Added console command AI.try_send_decision
- Added console command AI.try_send_interaction
- Added console command Ironman.ToggleIgnore. When ignored, saves will act as if they're not ironman, including that when you hit save it'll result in a non-ironman save. This can be toggled during gameplay
- Added console command ToggleShowAllKillers
- Added console command complete_schemes, guaranteed_scheme_success/failure, and guaranteed_scheme_secrecy_success/failure. The success/secrecy ones only affect the player
- Added console command set_date
- Added console command show_regions_in_tooltip
- Added console command toggle_keys_on_map
- Added console commands "yesmen_instant" (AKA "ymi") and "instant_responses". The yesmen button in the console can now be right-clicked to run "yesmen_instant"
The bypass and save_every commands have been especially helpful in setting up scenarios to test scripts and make sure it works exactly as you had intended in your mods. As are the forcing the AI to try out an interaction instead of waiting for them to do it of their own free will.  


## Modifiers Everywhere​

In 1.5 we’ve made some improvements to modifiers so if you use an invalid modifier type somewhere it will error and let you know its not going to work.  

Which has been very useful as in 1.5 we’ve greatly expanded upon modifier support in buildings, now buildings can not only apply modifiers to you in general but they can also apply specific modifiers based on culture parameters which are applied by traditions. These can be used in the modifiers affecting the character, province, county and duchy_capital_county modifiers.  

In addition there is a province_terrain_modifier which can apply a modifier based optionally on: terrain type, being coastal, being by a river, and by culture parameter. So traditions can really matter in your mods and let cultures play in vastly different ways.  


![The script for various culture tradition based modifiers on buildings](https://forumcontent.paradoxplaza.com/public/785672/building_culture_modifiers.PNG "The script for various culture tradition based modifiers on buildings")


## Clock’s a ticking​

Release day is coming soon and we’re very excited to see what mods are going to do with Royal Court, especially with the court scene itself which we hope in the future to see some fantastic 3D scenes especially from fantasy mods.  

I’m gonna get back to the last minute release period scramble, thank you for reading and I hope you’re looking forward to Royal Court’s release and the great mods we’re gonna be able to see in the future too!

 

#### Attachments

- [/forum/attachments/effects-log.798182/](https://forum.paradoxplaza.com/forum/attachments/effects-log.798182/)
  
  effects.log
  288,5 KB

 · Views: 0

- [/forum/attachments/event_scopes-log.798183/](https://forum.paradoxplaza.com/forum/attachments/event_scopes-log.798183/)
  
  event_scopes.log
  302 bytes

 · Views: 0

- [/forum/attachments/event_targets-log.798184/](https://forum.paradoxplaza.com/forum/attachments/event_targets-log.798184/)
  
  event_targets.log
  22,2 KB

 · Views: 0

- [/forum/attachments/modifiers-log.798185/](https://forum.paradoxplaza.com/forum/attachments/modifiers-log.798185/)
  
  modifiers.log
  58,9 KB

 · Views: 0

- [/forum/attachments/on_actions-log.798186/](https://forum.paradoxplaza.com/forum/attachments/on_actions-log.798186/)
  
  on_actions.log
  35,7 KB

 · Views: 0

- [/forum/attachments/triggers-log.798187/](https://forum.paradoxplaza.com/forum/attachments/triggers-log.798187/)
  
  triggers.log
  195,8 KB

 · Views: 0

<!-- artifact:reactions:start -->
- 104 Like
- 60 Love
- 27 (unlabeled — rendered as base64 data URI)
- 5 Haha
- 5 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)**
Role: Former Senior Programmer - Crusader Kings 3
Badges: 99
Reaction score: 8,575

*[Full game-badge icon list of 39 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
