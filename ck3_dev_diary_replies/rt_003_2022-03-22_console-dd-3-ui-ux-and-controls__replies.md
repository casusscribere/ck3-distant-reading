---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1516699/"
forum_thread_id: 1516699
content_type: reply_thread
parent_dd_file: dd_003_2022-03-22_console-dd-3-ui-ux-and-controls.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 3
title: "Console DD #3: UI/UX and Controls"
dd_date: 2022-03-22
expansion: Console Edition
patch: Crusader Kings III Console Edition
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 2
reply_count: 28
participant_count: 26
reply_date_first: 2022-03-22
reply_date_last: 2022-04-09
body_word_count: 1081
inline_image_count: 0
quoted_span_count: 9
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Console DD #3: UI/UX and Controls

*28 replies from 26 participants across 2 pages*

## Reply 1 — participant_001 · 2022-03-22 · post-28166477

The UI is looking pretty good for console

## Reply 2 — participant_002 · 2022-03-22 · post-28166488

Still hoping that we will eventually get some form of a cheat menu like how we can on PC use the dev console for cheats, would love something on the console version maybe in the form of a manu or a simplefied way of accessing the dev command. A lot of people use this for role playing so it would be very nice for those on the console version to get access to them.

## Reply 3 — participant_003 · 2022-03-22 · post-28166547

I like how a perfectly fine Console Dev Diary still gets "respectfully disagree" reactions even if there's a dev diary for PC published on the same day.

## Reply 4 — participant_004 · 2022-03-22 · post-28166579

NGL the UI looks pretty good wish there was an option to have similar UI on PC as well

## Reply 5 — participant_005 · 2022-03-22 · post-28166597

Round Character Portraits are back!!!

## Reply 6 — participant_006 · 2022-03-22 · post-28166708

I think this is the DD that should have been last week. This one is much more substantial. I don't play console, but this looks like it will work well there. It's a good UI for console.

## Reply 7 — participant_007 · 2022-03-22 · post-28166970

Now this is a console DD. Looks pretty good. These games just do not lend themselves to playing with controllers but you guys are doing a great job. I've said it before but I really wish you'd offer the console edition on steam once this is done. Playing CK3 on the steam deck would be excellent. T-Pain is a fun streamer. I hope he becomes a CK3 regular.

## Reply 8 — participant_008 · 2022-03-22 · post-28166978

Is mouse and keyboard enabled for this game on console?

## Reply 9 — participant_009 · 2022-03-22 · post-28167133

<!-- artifact:quote:start -->
> druez said: Is mouse and keyboard enabled for this game on console? Click to expand...
<!-- artifact:quote:end -->
No, mouse and keyboard will not be supported. Lab42 has completely rebuilt the UI for the console version, to the point where mouse and keyboard controls would not make sense even if support for it was added. Every part of the UI has been redesigned, reorganized, and remade with controller support in mind from the start. Implementing mouse and keyboard support is unfortunately more complicated than just flicking a switch. Having said that, it is something that might be investigated in the future based on demand.

## Reply 10 — participant_010 · 2022-03-22 · post-28167172

Will this UI be an option on PC for those that wish to use a controller or for playing on the steam deck?

## Reply 11 — participant_011 · 2022-03-22 · post-28167268

<!-- artifact:quote:start -->
> PDX_Pariah said: Howdy y'all! We are glad to announce that we have a fantastic Dev Diary from our friends at Lab42 where we will cover the long anticipated and much sought after UI and UX for the Console version releasing soon! Lab42 have been hard at work and there is not much time left until release, so we hope you enjoy the information and vision they have presented for you. Now with screenshots! As you would expect, user interface and controls were core components of the adaptation from PC to console. One of the main aims was to create a UI that was easily accessible and facilitated fluid gameplay. There is no set standard for UI and controls for Grand Strategy Games on console, with most approaches being subjective and as a consequence we’ve taken an approach that suited the unique Crusader Kings Gameplay. View attachment 821188 [Map Overview and controls] This started with a control hierarchy that marries UI and button control placement, for example ... using shoulder buttons for the top tier menus – the Command Bar – and bumpers to tab between sub-menus within the main menus. In addition, the decision was taken to assign controls to unique game functions rather than using lots of contextual buttons. Control prompts specific to each menu, screen / game context are displayed at the bottom of the screen to assist the user. The aim is to provide the player with a lexicon of controls that when learnt facilitate fluid interaction with the game UI and functionality. View attachment 821190 [Earl Alfred Character View] We could've taken a very conservative approach to development, but this was not what Lab42 or Paradox wanted. For example, the conundrum of turning a PC control system and UI into a viable console offering could've involved retaining the PC UI and using the controller thumbstick as a virtual mouse, but this approach was dismissed out of hand. User research also showed how popular the D-Pad was as a means of game navigation, especially when dealing with menus. Moving away from the use of a virtual mouse and freeing up the D-Pad for game navigation (as opposed to invoking menus as used in other console strategy games) presented a new set of challenges to overcome. View attachment 821198 [Family Tree] The UI and controls we've adopted is a hybrid approach, leaning on best in class examples as reference and applying them to the unique CK game framework (e.g. top level onscreen menus (the Command Bar), Radials (Character and Maps), and quality of life shortcuts (e.g. Quick Access Bar, Hints, Notifications). View attachment 821189 [Council Tab in Top Menu] When looking at the Crusader Kings user interface it was clear that most of the community want as much information at their fingertips as possible in order to form and execute game strategy. Flicking between menus, the map and popups is a feature of the PC title that we wanted to retain on console. This is also enhanced by the Radials to access your Character Wheel and another that introduces the Map View Radial accessible at any time from the main gameplay window. Allowing you to quickly change between Map Modes and easily accessing your character features without in-depth menu navigation. View attachment 821191 [Radial Map Wheel] Avoiding the use of lots of fullscreen menus that potentially break the immersion of gameplay was a driver here, and this led to the concept of switching focus being introduced. This essentially allows the gamer to quickly move between any open screen elements as well as allowing easy Map Interaction – a critical component of Crusader Kings gameplay. View attachment 821200 [Start Date map] View attachment 821201 [Martial View] View attachment 821202 [Martial View] That does it for the Console portion of the Developer Diary fresh and hot from the Lab42 presses! Click to expand...
<!-- artifact:quote:end -->
The Ui looks pretty well done, I hope that we won't be fighting the thumbstick to use the radial. Will we be able to get trophies, and a platinum (and it's Xbox equivalent)?

## Reply 12 — participant_012 · 2022-03-22 · post-28167300

Thank you very much that you don´t spoil PC-Version with Console Interface, but create for every version different amazing UI

## Reply 13 — participant_013 · 2022-03-23 · post-28167863

<!-- artifact:quote:start -->
> Leyrann said: I like how a perfectly fine Console Dev Diary still gets "respectfully disagree" reactions even if there's a dev diary for PC published on the same day. Click to expand...
<!-- artifact:quote:end -->
people will never be happy lol

## Reply 14 — participant_013 · 2022-03-23 · post-28167865

I for one, find this very amusing. now to wait for the gameplay video

## Reply 15 — participant_014 · 2022-03-23 · post-28168612

I'm going to say something controversial, I actually want that top of the screen bar in the PC version. It's a better, cleaner version of what we currently have.

## Reply 16 — participant_015 · 2022-03-25 · post-28173227

<!-- artifact:quote:start -->
> PDX_Pariah said: Howdy y'all! We are glad to announce that we have a fantastic Dev Diary from our friends at Lab42 where we will cover the long anticipated and much sought after UI and UX for the Console version releasing soon! Lab42 have been hard at work and there is not much time left until release, so we hope you enjoy the information and vision they have presented for you. Now with screenshots! As you would expect, user interface and controls were core components of the adaptation from PC to console. One of the main aims was to create a UI that was easily accessible and facilitated fluid gameplay. There is no set standard for UI and controls for Grand Strategy Games on console, with most approaches being subjective and as a consequence we’ve taken an approach that suited the unique Crusader Kings Gameplay. View attachment 821188 [Map Overview and controls] This started with a control hierarchy that marries UI and button control placement, for example ... using shoulder buttons for the top tier menus – the Command Bar – and bumpers to tab between sub-menus within the main menus. In addition, the decision was taken to assign controls to unique game functions rather than using lots of contextual buttons. Control prompts specific to each menu, screen / game context are displayed at the bottom of the screen to assist the user. The aim is to provide the player with a lexicon of controls that when learnt facilitate fluid interaction with the game UI and functionality. View attachment 821190 [Earl Alfred Character View] We could've taken a very conservative approach to development, but this was not what Lab42 or Paradox wanted. For example, the conundrum of turning a PC control system and UI into a viable console offering could've involved retaining the PC UI and using the controller thumbstick as a virtual mouse, but this approach was dismissed out of hand. User research also showed how popular the D-Pad was as a means of game navigation, especially when dealing with menus. Moving away from the use of a virtual mouse and freeing up the D-Pad for game navigation (as opposed to invoking menus as used in other console strategy games) presented a new set of challenges to overcome. View attachment 821198 [Family Tree] The UI and controls we've adopted is a hybrid approach, leaning on best in class examples as reference and applying them to the unique CK game framework (e.g. top level onscreen menus (the Command Bar), Radials (Character and Maps), and quality of life shortcuts (e.g. Quick Access Bar, Hints, Notifications). View attachment 821189 [Council Tab in Top Menu] When looking at the Crusader Kings user interface it was clear that most of the community want as much information at their fingertips as possible in order to form and execute game strategy. Flicking between menus, the map and popups is a feature of the PC title that we wanted to retain on console. This is also enhanced by the Radials to access your Character Wheel and another that introduces the Map View Radial accessible at any time from the main gameplay window. Allowing you to quickly change between Map Modes and easily accessing your character features without in-depth menu navigation. View attachment 821191 [Radial Map Wheel] Avoiding the use of lots of fullscreen menus that potentially break the immersion of gameplay was a driver here, and this led to the concept of switching focus being introduced. This essentially allows the gamer to quickly move between any open screen elements as well as allowing easy Map Interaction – a critical component of Crusader Kings gameplay. View attachment 821200 [Start Date map] View attachment 821201 [Martial View] View attachment 821202 [Martial View] That does it for the Console portion of the Developer Diary fresh and hot from the Lab42 presses! Click to expand...
<!-- artifact:quote:end -->
The one reason why I will not get this game on Console and instead I got on pc is because there is no link between the two and I would have had to buy two times the same game and dlcs, also even if gamepass offers it among its line of games, it won't offer the dlcs, so its completely useless to buy there. This is the reason why I goton pc rather than on console. Despite I would really have liked more to play it on console than pc .

## Reply 17 — participant_016 · 2022-03-25 · post-28173631

<!-- artifact:quote:start -->
> PDX_Pariah said: Howdy y'all! We are glad to announce that we have a fantastic Dev Diary from our friends at Lab42 where we will cover the long anticipated and much sought after UI and UX for the Console version releasing soon! Lab42 have been hard at work and there is not much time left until release, so we hope you enjoy the information and vision they have presented for you. Now with screenshots! As you would expect, user interface and controls were core components of the adaptation from PC to console. One of the main aims was to create a UI that was easily accessible and facilitated fluid gameplay. There is no set standard for UI and controls for Grand Strategy Games on console, with most approaches being subjective and as a consequence we’ve taken an approach that suited the unique Crusader Kings Gameplay. View attachment 821188 [Map Overview and controls] This started with a control hierarchy that marries UI and button control placement, for example ... using shoulder buttons for the top tier menus – the Command Bar – and bumpers to tab between sub-menus within the main menus. In addition, the decision was taken to assign controls to unique game functions rather than using lots of contextual buttons. Control prompts specific to each menu, screen / game context are displayed at the bottom of the screen to assist the user. The aim is to provide the player with a lexicon of controls that when learnt facilitate fluid interaction with the game UI and functionality. View attachment 821190 [Earl Alfred Character View] We could've taken a very conservative approach to development, but this was not what Lab42 or Paradox wanted. For example, the conundrum of turning a PC control system and UI into a viable console offering could've involved retaining the PC UI and using the controller thumbstick as a virtual mouse, but this approach was dismissed out of hand. User research also showed how popular the D-Pad was as a means of game navigation, especially when dealing with menus. Moving away from the use of a virtual mouse and freeing up the D-Pad for game navigation (as opposed to invoking menus as used in other console strategy games) presented a new set of challenges to overcome. View attachment 821198 [Family Tree] The UI and controls we've adopted is a hybrid approach, leaning on best in class examples as reference and applying them to the unique CK game framework (e.g. top level onscreen menus (the Command Bar), Radials (Character and Maps), and quality of life shortcuts (e.g. Quick Access Bar, Hints, Notifications). View attachment 821189 [Council Tab in Top Menu] When looking at the Crusader Kings user interface it was clear that most of the community want as much information at their fingertips as possible in order to form and execute game strategy. Flicking between menus, the map and popups is a feature of the PC title that we wanted to retain on console. This is also enhanced by the Radials to access your Character Wheel and another that introduces the Map View Radial accessible at any time from the main gameplay window. Allowing you to quickly change between Map Modes and easily accessing your character features without in-depth menu navigation. View attachment 821191 [Radial Map Wheel] Avoiding the use of lots of fullscreen menus that potentially break the immersion of gameplay was a driver here, and this led to the concept of switching focus being introduced. This essentially allows the gamer to quickly move between any open screen elements as well as allowing easy Map Interaction – a critical component of Crusader Kings gameplay. View attachment 821200 [Start Date map] View attachment 821201 [Martial View] View attachment 821202 [Martial View] That does it for the Console portion of the Developer Diary fresh and hot from the Lab42 presses! Click to expand...
<!-- artifact:quote:end -->
Thank you sincerely for adapting this Masterpiece for consoles. You are geniuses.

## Reply 18 — participant_017 · 2022-03-25 · post-28173728

<!-- artifact:quote:start -->
> X_FloW said: NGL the UI looks pretty good wish there was an option to have similar UI on PC as well Click to expand...
<!-- artifact:quote:end -->
Indeed. Anything that reduces number of unnecessary clicks would be a good thing for PC in my opinion *cough mapmodes + button cough* That radial looks neat.

## Reply 19 — participant_018 · 2022-03-26 · post-28174643

Thanks for posting this update. It is looking very good. I for one can’t wait and looking forward to the 29th! Have a couple days work booked off so I’m ready to go when you are LOL. Part of the “allure” and love/hate it of these games is the interface and menus... it wouldn’t be the same without them and this so far looks in keeping with and preserving the feel of PC play nicely.

## Reply 20 — participant_007 · 2022-03-28 · post-28177820

I like these menu's a lot. Very well done. I kind of hope an option to have your ruler in a circle up in the corner like this could be brought to the PC. It looks clear and clean!

## Reply 21 — participant_019 · 2022-03-29 · post-28179572

<!-- artifact:quote:start -->
> klopkr said: I like these menu's a lot. Very well done. I kind of hope an option to have your ruler in a circle up in the corner like this could be brought to the PC. It looks clear and clean! Click to expand...
<!-- artifact:quote:end -->
Same. Going on a CK2 binge and I'd love to have a "CK2-Style" round portrait as an option. Honestly this whole UI looks very clean.

## Reply 22 — participant_020 · 2022-03-30 · post-28181883

Hello! It looks great. Any plan if this console ui will be put on pc when you plug in the controller ? Have a nice day

## Reply 23 — participant_021 · 2022-03-31 · post-28184344

Can you please fix the navigation issues. Multiple screens are not accessible as the d pad navigation skips over them. For example on console you have no way of seeing who some one is allied with so any war can be a gamble. I literally started a war for 1 County which only had 200 levies and 1 ally. Turned out that ally had 5k troops who showed up and slapped me all over. Not good right at the start of a game. Kind of ruins the whole experience when any military expansion becomes a big gamble on who you will have to fight in the end

## Reply 24 — participant_022 · 2022-03-31 · post-28185644

Breaking Bug Found (PLEASE FIX): On the Character Information Panel you cannot expand the Titles, Claims or Alliances labels which means you cant see other character alliances, titles nor claims. This is game breaking.

## Reply 25 — participant_023 · 2022-04-01 · post-28185871

<!-- artifact:quote:start -->
> phil123r46 said: Can you please fix the navigation issues. Multiple screens are not accessible as the d pad navigation skips over them. For example on console you have no way of seeing who some one is allied with so any war can be a gamble. I literally started a war for 1 County which only had 200 levies and 1 ally. Turned out that ally had 5k troops who showed up and slapped me all over. Not good right at the start of a game. Kind of ruins the whole experience when any military expansion becomes a big gamble on who you will have to fight in the end Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> ElFroweey said: Breaking Bug Found (PLEASE FIX): On the Character Information Panel you cannot expand the Titles, Claims or Alliances labels which means you cant see other character alliances, titles nor claims. This is game breaking. Click to expand...
<!-- artifact:quote:end -->
It's not very intuitive, but I believe the way to see these is to select another character, then press LT to bring up the left radial menu, then select Titles to see claims and titles, or War & Peace (I think) to see alliances.

## Reply 26 — participant_024 · 2022-04-01 · post-28186796

Found a bug, when trying to declare war, if you immediately select the conquest of the county (the smallest territory), the screen becomes darkened but nothing else appears. If you first choose to capture the duchy and then switch to the county, then everything is correct. If need can make screen. XBOX SX.

## Reply 27 — participant_025 · 2022-04-04 · post-28191706

For the life of me, I cannot figure out how to destroy one of my titles. I am not sure if there is a bug, if it is completely missing from the console UI, or if it is just unintuitive.

## Reply 28 — participant_026 · 2022-04-09 · post-28202513

Yeah it looks good, but can you explain, how we can revoke the leased domain from a holy order? I can saw button with the X but I can't get there

