---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1556674/"
forum_thread_id: 1556674
content_type: reply_thread
parent_dd_file: dd_005_2022-11-15_console-dd-free-update-ruler-designer.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 5
title: CK3 Console DD - Free Update/Ruler Designer
dd_date: 2022-11-15
expansion: Console Edition
patch: Crusader Kings III Console Edition
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 3
reply_count: 57
participant_count: 33
reply_date_first: 2022-11-15
reply_date_last: 2023-01-27
body_word_count: 2731
inline_image_count: 0
quoted_span_count: 28
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — CK3 Console DD - Free Update/Ruler Designer

*57 replies from 33 participants across 3 pages*

## Reply 1 — participant_001 · 2022-11-15 · post-28615445

Howdy all! As we recently announced, we are proud to release Northern Lords this coming Thursday (11/17) which will be accompanied by a Free Update which will of course include Ruler Designer. Without much further delay, we will let the team from Lab42 tell you what to expect with their own words: Ruler Designer: The Ruler Designer is coming to CK3 console. Now you can terrorize and bemuse the inhabitants of the world with your unique and overpowered godlike rulers. Despite looking far different from the original, it plays as well. The menus and navigation have been re-designed to guarantee a smooth experience across the board. They have been revamped and restructured – much like the base game – to be suitable for consoles. Which has been a major undertaking for the LAB42 team, and we appreciate all the work our developers have put into making it what it is now. When adapting the Ruler Designer from PC to console, the core challenge was the main screen of the Ruler Designer. When you open it on pc this is what you see: { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" } Although suitable for PC, it is clear that a significant amount of work was required to make the transition from PC to console. This was a key area of focus for the team. To start with, we made the conscious decision to follow the same design philosophy that resonates throughout the console adaptation. By keeping the controls identical to what players already know and by keeping a structure that is already familiar, we hope that getting familiar with this new extensive feature will be an easy and quick process. Our first step was to separate the menu into categories. We looked at various UI elements present in the menu and tried to group them into tabs with a consistent theme or logic. Apart from the elements marked as meta information, all other groupings were turned into tabs. Each with two or more subtabs to better separate and organize the different parts of the customization process. As an example, for the character details tab, we added three sub tabs: Sex & Sexual Orientation, Age & Weight, Name & family (all self-explanatory). The same organizational process was used on the Change Appearance options, with the slight difference that we used the already existing buttons (Head, Neck, Eyes, etc) as the base for the tabs. All the small selectable icons in the base game were changed to buttons and arranged in their respective categories. For example, the Venus and Mars symbols were made into selectable buttons that players can select to change the sex of their ruler. We’ve kept the sliders where they were, adding a glow around them so you know which one is currently highlighted. Because the sliders were originally made to be used with a mouse, we had to change the way console players interact with them, by adding incremental speed to the slider itself. Single presses will move the slider one value, while holding down left/ right direction on the d-pad or left analog stick, will move the slider faster and faster. The colour picker was a unique UI element, which meant it had to be designed from scratch. The main challenge with this tool was the fact that it needed to “capture input” meaning that when in use, no other UI element could be interacted with – in other words, no other UI element in the menu can be accessed or interactable while the colour picker is active. This was not an easy task, as it required us to disable all interactions outside the square that makes the colour picker – something not necessary in the PC version, where interactions determined by the location of the mouse on the screen. This led to many occasions where, after selecting the colour picker, players were still able to navigate the rest of the UI elements while picking a colour. We eventually figured out a way to implement the colour picker, so it locked all controls outside of itself. Which then led to one of the funnier bugs we’ve had during the development of Northern Lords: the noisy colour picker. This bug was a simple fix, and it came down to a repeating sound that was caused by the colour picker emulating a UI button behind the scenes. Which meant that every time a new colour was picked, A.K.A the cursor was moved to a different position/ colour, the game interpreted it as a new button being highlighted, playing the sound cue for it. This led to the sound being repeated constantly for as long as players scrolled through the colours. We did have a bit of fun with it. The Faith and Culture lists were transformed into a big list of dropdown menus, where players can expand and collapse the dropdowns as they wish and highlight each one of the cultures/ faiths and see their tooltip for information on it. The Traits were one of the more interesting parts to re-design, as they required multiple types of interactions. In the end, we decide to follow the true tested method of making a list. Each category of traits (Education, Personality, Other Traits) has a button that players can select to open a list with the respective traits of that category. In situations where you can pick multiple traits from the list, it will stay open until you decide to close it with a press of the Back Button. If during the selection players accidentally pick something they don’t want, they can backout of the list and remove that trait from the group of selected traits, by highlighting the trait and pressing the select button. With the Skills we decided to separate the base level of the skill from the bonuses it gets from selected traits. This decision came as a result of very high skill levels, from player created characters, showing a skill of 100 and players still being able to press the Add Point button, increasing the total score of the character without increasing the total value of the skill (since the cap is 100). Because this could easily be interpreted as a bug, we decided to separate the two values. It not only solved that issue, but also worked to organize the skill points in an easier to understand format. Don’t worry, you can use the Advanced Tooltips Mode to check where all the points in the bonus value are coming from. And that pretty much sums up our experience developing the Ruler Designer into a console ready menu for your enjoyment. We hope you all have as much fun playing around with it as we have working on it. Now, go forth and create your own rulers!

## Reply 2 — participant_002 · 2022-11-15 · post-28624361

Absolutely cannot wait for this.

## Reply 3 — participant_003 · 2022-11-15 · post-28624395

Does this mean PC is not getting a dev diary today? Edit: Guess not then, disappointing.

## Reply 4 — participant_004 · 2022-11-15 · post-28624563

Can’t wait to create my lustful chaste god emperor of Scandinavia who praises Zeus

## Reply 5 — participant_005 · 2022-11-15 · post-28625322

<!-- artifact:quote:start -->
> DaBombXXX said: Does this mean PC is not getting a dev diary today? Edit: Guess not then, disappointing. Click to expand...
<!-- artifact:quote:end -->
Let us console players have a win for once, lmao sit back on your fancy computer and enjoy your significant jump on updates and content that we have yet to even get a clue of an ETA.

## Reply 6 — participant_006 · 2022-11-15 · post-28625424

Excited for character creator, but will this update fix "norman yoke" and "black widow" trophies?

## Reply 7 — participant_007 · 2022-11-15 · post-28625460

Nice write-up on all the changes required to convert a PC user interface (UI) to a Console-friendly UI. Will we be receiving a detailed set of release notes as well tomorrow or Thursday? Looking forward to a long list of bug fixes and new functionality, hopefully including the ability to assault forts ().

## Reply 8 — participant_008 · 2022-11-16 · post-28626151

If its true , you will get your 5 star review on xbox live ! From Lübeck i will rule over the baltic states , hopefully !

## Reply 9 — participant_009 · 2022-11-16 · post-28626665

<!-- artifact:quote:start -->
> :HiroshimaXl96 said: Excited for character creator, but will this update fix "norman yoke" and "black widow" trophies? Click to expand...
<!-- artifact:quote:end -->
The only one with a problem is the Norman Yoke achievement. The decision is bugged out. I'm guessing the reason you are not getting the Black Widow achievement is because you are playing as a male. To get the achievement you need to be a female, reflecting an actual black widow. Unfortunately for those who suffer problems with this achievement, there is no "male black widow" in nature.

## Reply 10 — participant_010 · 2022-11-17 · post-28627861

Really hope this fixes bugs * not getting agreed on rasom gold * can't view titles, claims, alliances on character screen * ally armies break dancing between two points instead of fighting * Norman Yoke doesn't work - vassals do not automatically covert to English

## Reply 11 — participant_008 · 2022-11-17 · post-28628362

When will the update be released today ?

## Reply 12 — participant_011 · 2022-11-17 · post-28628378

9:45 no update? Taking the piss here

## Reply 13 — participant_010 · 2022-11-17 · post-28628526

It's 4 am in California no update yet lol

## Reply 14 — participant_012 · 2022-11-17 · post-28628539

19:42 in beijing ， still no upgrade

## Reply 15 — participant_013 · 2022-11-17 · post-28628552

5:56 am where I live, no update……

## Reply 16 — participant_011 · 2022-11-17 · post-28628665

Community team said 5pm uk time, may be sooner may be longer

## Reply 17 — participant_014 · 2022-11-17 · post-28628674

Do we know if the DLC is purchasable separate to the expansion pass? Or do you have to have that

## Reply 18 — participant_015 · 2022-11-17 · post-28628773

<!-- artifact:quote:start -->
> nicktrainor8 said: Community team said 5pm uk time, may be sooner may be longer Click to expand...
<!-- artifact:quote:end -->
So they drop an update and then call it a night? That doesn't seem wise.

## Reply 19 — participant_010 · 2022-11-17 · post-28628975

<!-- artifact:quote:start -->
> KCalo said: So they drop an update and then call it a night? That doesn't seem wise. Click to expand...
<!-- artifact:quote:end -->
Considering who we're dealing with I'd say it's par for the course

## Reply 20 — participant_016 · 2022-11-17 · post-28629186

I was going to try this before work. Well I work at 12:30pm est and it is not there yet. Guess later tonight.

## Reply 21 — participant_010 · 2022-11-17 · post-28629711

Is it out yet or should I give up for the day

## Reply 22 — participant_017 · 2022-11-17 · post-28629974

When can the Ruler Designer be used in multiplayer?

## Reply 23 — participant_008 · 2022-11-17 · post-28629985

Thank you now you got 5 stars on the ck3 page !

## Reply 24 — participant_018 · 2022-11-18 · post-28630380

It took you guys this long to do that...?

## Reply 25 — participant_019 · 2022-11-18 · post-28630688

Great update. however could it be that something changed with marriages? Could be the effect of Northern lords as well maybe I am not certain. When playing yesterday everytime i got marriaged automatically when having no wife at that moment multiple times as I was divorcing everytime. I was playing with ruler designer and the DLC Norhern lords,.

## Reply 26 — participant_020 · 2022-11-18 · post-28630837

<!-- artifact:quote:start -->
> :HiroshimaXl96 said: Excited for character creator, but will this update fix "norman yoke" and "black widow" trophies? Click to expand...
<!-- artifact:quote:end -->
This achievements works perfect what are you on about ?

## Reply 27 — participant_020 · 2022-11-18 · post-28630840

Guys what is happening with Xbox achievements for Northern Lords. PS players have them why not us ?

## Reply 28 — participant_021 · 2022-11-18 · post-28630842

Hello, first of all I like to thank you for releasing ruler designer, but there is still a major bug, that is present from release of the base game, that is that you cant´t view all your titles on character screen, the tooltip on titles icon says "select to expand" but it canť be selected. { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" }

## Reply 29 — participant_022 · 2022-11-18 · post-28630911

Do you already have information for the PS5 players who are unable to install the DLC? The error code seems to be related to the Playstation APP when downloading from the APP. Unfortunately, all previous instructions for the error code that I have found do not work. many thanks for your help

## Reply 30 — participant_019 · 2022-11-18 · post-28630966

<!-- artifact:quote:start -->
> :dolmusch said: Do you already have information for the PS5 players who are unable to install the DLC? The error code seems to be related to the Playstation APP when downloading from the APP. Unfortunately, all previous instructions for the error code that I have found do not work. many thanks for your help Click to expand...
<!-- artifact:quote:end -->
Hi I had the same issue it kept saying this CE-something when trying to download it turns out it was somehow allready downloaded with the update I guess this is because the seaonpass was allready installed, so my guess is that it was downloading and installing this together with the update

## Reply 31 — participant_022 · 2022-11-18 · post-28630975

<!-- artifact:quote:start -->
> thomas4545459 said: Hi I had the same issue it kept saying this CE-something when trying to download it turns out it was somehow allready downloaded with the update I guess this is because the seaonpass was allready installed, so my guess is that it was downloading and installing this together with the update Click to expand...
<!-- artifact:quote:end -->
many thanks for your response. So it just shows as purchased but not installed? It would be great if it was already installed anyway (my weekend is saved ) i will test it as soon as i get home

## Reply 32 — participant_019 · 2022-11-18 · post-28631129

<!-- artifact:quote:start -->
> :dolmusch said: many thanks for your response. So it just shows as purchased but not installed? It would be great if it was already installed anyway (my weekend is saved ) i will test it as soon as i get home Click to expand...
<!-- artifact:quote:end -->
Yes that is the case it will show as purchased but somehow you can't see it is installed and if you try to instal it gives an error I was really sad yesterday so I decided to just try it and it worked.

## Reply 33 — participant_023 · 2022-11-18 · post-28631162

<!-- artifact:quote:start -->
> thomas4545459 said: Great update. however could it be that something changed with marriages? Could be the effect of Northern lords as well maybe I am not certain. When playing yesterday everytime i got marriaged automatically when having no wife at that moment multiple times as I was divorcing everytime. I was playing with ruler designer and the DLC Norhern lords,. Click to expand...
<!-- artifact:quote:end -->
Thank you for reporting, I will pass this on to the devs!

## Reply 34 — participant_024 · 2022-11-18 · post-28631212

<!-- artifact:quote:start -->
> 728090 said: Hello, first of all I like to thank you for releasing ruler designer, but there is still a major bug, that is present from release of the base game, that is that you cant´t view all your titles on character screen, the tooltip on titles icon says "select to expand" but it canť be selected.View attachment 913021 Click to expand...
<!-- artifact:quote:end -->
Nor can you view your titles via the radial menu, which only shows your highest title. It seems like the only way to view all your titles, clumsily enough, is to go to 'Grant titles' to another character. Someone please feel free to correct me...

## Reply 35 — participant_025 · 2022-11-18 · post-28631387

<!-- artifact:quote:start -->
> thomas4545459 said: Great update. however could it be that something changed with marriages? Could be the effect of Northern lords as well maybe I am not certain. When playing yesterday everytime i got marriaged automatically when having no wife at that moment multiple times as I was divorcing everytime. I was playing with ruler designer and the DLC Norhern lords,. Click to expand...
<!-- artifact:quote:end -->
They also made it so you can't divorce your wife and make her a concubine for some odd reason

## Reply 36 — participant_025 · 2022-11-18 · post-28631393

<!-- artifact:quote:start -->
> Portable Grump said: Thank you for reporting, I will pass this on to the devs! Click to expand...
<!-- artifact:quote:end -->
Can you pass along these other concerns * Not Seeing Option to create Mediterranean Empire * Not seeing Option to create North Sea Empire * Not seeing raise runestones as Norse * Not seeing choose a God as Norse * Not seeing Vangarian Adventure unlike on PC where you could leave your home land behind to conquer another land * Harald Tanglehair isn't straight now despite the Sagas and History saying he had children when I try to romance or seduce my wife the game says "The Bonds of Marriage are enough" * can't divorce wife and make her a concubine

## Reply 37 — participant_023 · 2022-11-18 · post-28631626

<!-- artifact:quote:start -->
> Lord_Nekro said: Can you pass along these other concerns * Not Seeing Option to create Mediterranean Empire * Not seeing Option to create North Sea Empire * Not seeing raise runestones as Norse * Not seeing choose a God as Norse * Not seeing Vangarian Adventure unlike on PC where you could leave your home land behind to conquer another land * Harald Tanglehair isn't straight now despite the Sagas and History saying he had children when I try to romance or seduce my wife the game says "The Bonds of Marriage are enough" * can't divorce wife and make her a concubine Click to expand...
<!-- artifact:quote:end -->
Will do, thanks for the reports!

## Reply 38 — participant_026 · 2022-11-18 · post-28631632

<!-- artifact:quote:start -->
> Lord_Nekro said: They also made it so you can't divorce your wife and make her a concubine for some odd reason Click to expand...
<!-- artifact:quote:end -->
That was an exploit they patched out.

## Reply 39 — participant_025 · 2022-11-18 · post-28631698

<!-- artifact:quote:start -->
> Portable Grump said: Will do, thanks for the reports! Click to expand...
<!-- artifact:quote:end -->
Also wheres the Viking music? Its the same music as before, I was looking forward to hearing some war jams to raid and battle to.

## Reply 40 — participant_025 · 2022-11-18 · post-28631710

<!-- artifact:quote:start -->
> kawamuratc said: That was an exploit they patched out. Click to expand...
<!-- artifact:quote:end -->
And it makes 0 sense. If she's at my court she should be able to be made concubine like anyone else

## Reply 41 — participant_026 · 2022-11-18 · post-28631762

<!-- artifact:quote:start -->
> Lord_Nekro said: And it makes 0 sense. If she's at my court she should be able to be made concubine like anyone else Click to expand...
<!-- artifact:quote:end -->
Sure, but that change prevented dirty exploiters like me (and, from the sounds of it, you too ) from marrying a person who would never willingly leave their court outside of the guarantees of marriage, making them a concubine, then repeating the process until we had 3 weirdly good nobles as concubines.

## Reply 42 — participant_025 · 2022-11-18 · post-28631766

<!-- artifact:quote:start -->
> kawamuratc said: Sure, but that change prevented dirty exploiters like me (and, from the sounds of it, you too ) from marrying a person who would never willingly leave their court outside of the guarantees of marriage, making them a concubine, then repeating the process until we had 3 weirdly good nobles as concubines. Click to expand...
<!-- artifact:quote:end -->
I'm not seeing an issue with any of that

## Reply 43 — participant_026 · 2022-11-18 · post-28631777

<!-- artifact:quote:start -->
> Lord_Nekro said: I'm not seeing an issue with any of that Click to expand...
<!-- artifact:quote:end -->
Sure, but it wasn’t working as intended. That’s why it got patched out. Exploits are fleeting. Appreciate the time you had with the exploit, don’t mourn its loss, and go off and find more exploits.

## Reply 44 — participant_027 · 2022-11-18 · post-28632013

So was this play tested? I mean how was varangian adventures messed up? Also is there any reason they didn't add the CoA designer to this update? I mean there's so much you can add I don't see why it needs to be following the PCs boot prints.

## Reply 45 — participant_025 · 2022-11-18 · post-28632028

<!-- artifact:quote:start -->
> kawamuratc said: Sure, but it wasn’t working as intended. That’s why it got patched out. Exploits are fleeting. Appreciate the time you had with the exploit, don’t mourn its loss, and go off and find more exploits. Click to expand...
<!-- artifact:quote:end -->
Or you could let people who have things removed that they found fun express those gripes without jumping in every thread telling people how YOU play it

## Reply 46 — participant_028 · 2022-11-19 · post-28632711

Don't use Xbox but wanted to say it's huge you're doing this. Rule Designers adds so many more hours into this game.

## Reply 47 — participant_029 · 2022-11-22 · post-28638287

Hi, i have installed the Royal Court DLC for PS5. But there is no Throneroom. does the game have a throneroom for the ps5? Will there be an update? Thanks for your help

## Reply 48 — participant_030 · 2022-11-22 · post-28639251

This was a really interesting read! I'm impressed with the console team's ability to rework such a dense interface for console inputs.

## Reply 49 — participant_031 · 2022-11-30 · post-28653294

<!-- artifact:quote:start -->
> DukeofWellington2 said: Hi, i have installed the Royal Court DLC for PS5. But there is no Throneroom. does the game have a throneroom for the ps5? Will there be an update? Thanks for your help Click to expand...
<!-- artifact:quote:end -->
I highly doubt you have it installed because it hasn't been released yet on console. You may have bought the season pass, which will give you access to the Royal Court DLC, but it needs to be released on consoles before you can actually use it.

## Reply 50 — participant_031 · 2022-11-30 · post-28653303

<!-- artifact:quote:start -->
> Lord_Nekro said: Also wheres the Viking music? Its the same music as before, I was looking forward to hearing some war jams to raid and battle to. Click to expand...
<!-- artifact:quote:end -->
i have the same issue: there's no new music in the PS5 DLC. Elope scheme also isn't possible

## Reply 51 — participant_032 · 2022-12-08 · post-28667951

<!-- artifact:quote:start -->
> kawamuratc said: Sure, but it wasn’t working as intended. That’s why it got patched out. Exploits are fleeting. Appreciate the time you had with the exploit, don’t mourn its loss, and go off and find more exploits. Click to expand...
<!-- artifact:quote:end -->
Yo hello can I have sum help with the ruler design because its not appearing for me I would like sum help if u could

## Reply 52 — participant_033 · 2023-01-26 · post-28739489

<!-- artifact:quote:start -->
> Hydro SKY0 said: Yo hello can I have sum help with the ruler design because its not appearing for me I would like sum help if u could Click to expand...
<!-- artifact:quote:end -->
I have been experiencing the same problem, Ruler designer hasn’t updated on console (PS5). I came here hoping for an answer but got nothing.

## Reply 53 — participant_031 · 2023-01-26 · post-28739764

<!-- artifact:quote:start -->
> Childish_Kai said: I have been experiencing the same problem, Ruler designer hasn’t updated on console (PS5). I came here hoping for an answer but got nothing. Click to expand...
<!-- artifact:quote:end -->
update your game. Open your game and pick select any ruler (top left corner) after the loadscreen select anywhere you want to play ... then in the pop-up menu you'll see the option to create your own ruler.

## Reply 54 — participant_033 · 2023-01-27 · post-28741484

This is false, the game still has the old designer. I have uninstalled and reinstalled the game. I had individually downloaded add ons and deleted them to see if it were bugged. This is just a rip off, no northern lords no new ruler designer. I want my money back

## Reply 55 — participant_026 · 2023-01-27 · post-28741564

<!-- artifact:quote:start -->
> Childish_Kai said: This is false, the game still has the old designer. I have uninstalled and reinstalled the game. I had individually downloaded add ons and deleted them to see if it were bugged. This is just a rip off, no northern lords no new ruler designer. I want my money back Click to expand...
<!-- artifact:quote:end -->
What do you mean by “the old designer”? Do you mean you have no ruler designer and can only pick already generated rulers on the map?

## Reply 56 — participant_033 · 2023-01-27 · post-28741692

<!-- artifact:quote:start -->
> kawamuratc said: What do you mean by “the old designer”? Do you mean you have no ruler designer and can only pick already generated rulers on the map? Click to expand...
<!-- artifact:quote:end -->
My ruler designer doesn’t look like the one that’s advertised.

## Reply 57 — participant_033 · 2023-01-27 · post-28741694

<!-- artifact:quote:start -->
> Childish_Kai said: My ruler designer doesn’t look like the one that’s advertised. Click to expand...
<!-- artifact:quote:end -->
Actually looking at it now, I was comparing my PC version to PS5 version. Which was why I was confused

