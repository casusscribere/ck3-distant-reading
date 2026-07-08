---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1507899/"
forum_thread_id: 1507899
content_type: reply_thread
parent_dd_file: dd_087_2022-01-25_dev-diary-87-royal-modding.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 87
title: "CK3 Dev Diary #87: Royal Modding"
dd_date: 2022-01-25
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 10
reply_count: 181
participant_count: 87
reply_date_first: 2022-01-25
reply_date_last: 2022-02-14
body_word_count: 19842
inline_image_count: 0
quoted_span_count: 174
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — CK3 Dev Diary #87: Royal Modding

*181 replies from 87 participants across 10 pages*

## Reply 1 — participant_001 · 2022-01-25 · post-28034524

First! Check the FAQ Royal Court if you have any question about the upcoming CK3 Expansion! And if you have a question for the developers regarding Modding, drop them here

## Reply 2 — participant_002 · 2022-01-25 · post-28034543

Gay mariages as a game rule is the best way of implementing it imo, doesn't affect those who don't want to play around with it, much easier to have it on in mp games (than if it was a mod). Quick questions : - will the AI do it or just players ? - Does it work with all mariage types (monogamy, polygamy, consorts etc) - How is it unlocked ?

## Reply 3 — participant_003 · 2022-01-25 · post-28034544

*(no text body — reaction-only or media-only post)*

## Reply 4 — participant_004 · 2022-01-25 · post-28034548

<!-- artifact:quote:start -->
> Which has been very useful as in 1.5 we’ve greatly expanded upon modifier support in buildings, now buildings can not only apply modifiers to you in general but they can also apply specific modifiers based on culture parameters which are applied by traditions. These can be used in the modifiers affecting the character, province, county and duchy_capital_county modifiers. Click to expand...
<!-- artifact:quote:end -->
Hell yeah, modding changes! I suppose not as you'd otherwise have explicitely said it, but does it also apply to doctrine parameters?

## Reply 5 — participant_005 · 2022-01-25 · post-28034551

I wounder If its possibly for modders to make tribal Courts and tiny Courts for counts and dutchys

## Reply 6 — participant_006 · 2022-01-25 · post-28034561

Can we get date_types.log?

## Reply 7 — participant_007 · 2022-01-25 · post-28034572

Glitterhoof says: 4808 errors and 31 FPS on a dev PC Do we need to worry?

## Reply 8 — participant_008 · 2022-01-25 · post-28034603

So just to confirm about same sex marriage - in vanilla, it can either be toggled on to be globally possible, or toggled off entirely, correct? Meaning we'd need mods to implement something like culture or religion based acceptance of same sex marriage? Super happy with these additions in general, release day can't come soon enough!

## Reply 9 — participant_009 · 2022-01-25 · post-28034610

<!-- artifact:quote:start -->
> JonathanViking said: I wounder If its possibly for modders to make tribal Courts and tiny Courts for counts and dutchys Click to expand...
<!-- artifact:quote:end -->
Yes, it's possible

## Reply 10 — participant_009 · 2022-01-25 · post-28034615

<!-- artifact:quote:start -->
> JasonSTGer said: Glitterhoof says: 4808 errors and 31 FPS on a dev PC Do we need to worry? Click to expand...
<!-- artifact:quote:end -->
I see several questionable assumptions with this question. First, devs have different PC, not all of them super-powerful, some are just normal. Second, it's a court scene with lots of people on high graphics settings, so you can go faster just by tuning graphics down a bit. Third, 30 FPS for a graphically rich but not very dynamic scene in a strategy game on a machine that matches graphics settings with its hardware capabilities is considered acceptable. In short - no, no need to worry

## Reply 11 — participant_010 · 2022-01-25 · post-28034623

Sorry if I am OT, but may I know if the question of the prefixes to the names of the Houses and Dynasties has been resolved?

## Reply 12 — participant_011 · 2022-01-25 · post-28034625

I can't wait to see a song of ice and fire mod making use of this.

## Reply 13 — participant_012 · 2022-01-25 · post-28034634

Question: In regards to the Cultural traditions, could we mod in say polygamy for that culture even if they follow a religion that practices monogamy?

## Reply 14 — participant_013 · 2022-01-25 · post-28034649

Glad that there is going to be an editor tool specifrically for courts. CKIII might be the most modder-friendly Paradox title yet.

## Reply 15 — participant_014 · 2022-01-25 · post-28034760

The addition of same-sex marriage is a welcome one. It's something I doubt I will make use of but it's great to have that type of flexibility for the people that want it Choice should be king in a sandbox game. If you can bang your brother-husband, Michael should be able to marry Joe.

## Reply 16 — participant_015 · 2022-01-25 · post-28034767

Good stuff, thanks for this week DD.

## Reply 17 — participant_016 · 2022-01-25 · post-28034778

i can not wait to mod the game again

## Reply 18 — participant_017 · 2022-01-25 · post-28034789

Speaking of modifiers and cultures playing in different ways (and the whole focus on culture in the DLC), will there finally be an opinion modifier for a culture group (heritage after the rework)? They were a thing in CK2 but so far in CK3 there are only opinion modifiers for individual cultures.

## Reply 19 — participant_018 · 2022-01-25 · post-28034799

<!-- artifact:quote:start -->
> blackninja9939 said: Hello everyone and welcome to the 87th CK3 Dev Diary! I’m Matthew, one of the Programmers on the CK3 team, and today I am going to talk to you about a variety of improvements and changes we’ve done to modding for the 1.5 patch which will be accompanying the Royal Court Expansion. We’ve added a variety of mod support in 1.5 so I’m not gonna cover everything, but I will give a few big ticket items that will let mods do a lot more fun custom things as well a few smaller fun ones. I’ve also attached the output of script_docs on 1.5 at the end so modders curious about the new triggers and effects in game can get a bit of a sneak peek for the release. The Royal Court​Of course the Royal Court itself is open to mods, it is all defined in the gfx/court_scene folder though the majority of the complex scene_settings itself is best built using the in-game editor that we are shipping with the court scene. It lets you position and change objects and switch between different settings much faster than trying to edit them all by hand. Trust me, cause I remember the time whilst the editor was work in progress and doing changes by hand crushed my soul. View attachment 798174 I am not going to go into a huge amount of detail on the royal court modding because it is actually pretty straightforward with the editor, you position things and pick the assets you need for a configuration and then it just puts things there. One aspect I will go into a bit more info on quickly is the character positioning, because the rest of the positioning is set within the editor but the characters are not positioned individually because of course not every court has the King of England to reference. Instead the character positions are given a set of valid roles, and you pick a position where someone who has one of those roles may go. For example the two guards you see in the back are two positioned instances of the guard and knight role, which has a variety of rules of who it should pick. If you have a bodyguard or champion court position appointed for example then it tries to use them as a special guard, but if you do not then it will fallback to picking any of your knights instead. You can also have some more special roles such as if you have a court jester or poet appointed then they can show up in your court too. View attachment 798189 Characters can not show up in multiple different roles and it is a “greedy” picking of first come first served in who is taken up, but you can write some fairly complex rules to decide who can go where as well as what animations they can choose from! Same-Sex Marriage​Coming with 1.5 is support for same-sex marriage, not only just in mods either but as a new game rule alongside the Same-Sex relations game rule so you can use it in un-modded games too. We've updated a variety of AI logic and interactions and content to take that into account when playing. View attachment 798177 Mods are of course able to implement this into their different worlds without it having to be a game rule, it can be based on different cultures or anything in the game world at all. This is something that we’re very happy to be able to put into the game and have support in the game rules for unmodded games too, it is something that a lot of the team and community wanted and we are glad it is finally going to be shipped in 1.5. Scripted Widgets​CK3 is one of our most moddable games yet, not just in terms of the content that can be added but the system's mods can script. And our new UI system is the most open we’ve had in terms of what custom UIs mods can add and edit, but one issue it had was letting you add brand new things entirely and keeping compatibility nicely. In 1.5 there is a new system called “scripted widgets”, what they allow for in essence is a mod to define their own brand new windows in the gui files and then add an entry into the gui/scripted_widgets folder with the name of their gui file and the main window. For example: gui/test_custom_widget.gui = my_first_cool_test_widget gui/test_custom_widget.gui = my_second_cool_test_widget Then with that simple line of script their window will appear in the game in the same way any of the windows we support in code do. Now of course there are some limitations, the windows do not have any special data context like a code one does but it can access anything that is set globally or on the local player character which covers more than enough cases normally. View attachment 798178 This may not sound hugely impactful, but it means that mods going forward can easily create large systems which can then more easily be compatible with other mods that add systems or if they feel brave enough even with larger Total Conversions if they do not cross over in incompatible design choices. I am really excited to see the new UIs that mods end up making for their gameplay systems and getting to try a few different mods together. Hopefully their windows have a bit more functionality and effort put into it than my testing one… Value Breakdowns​Another bit of UI functionality that mods could not nicely mimic is getting breakdowns of their numbers in the same way we break down a value like your prestige income or how much piety it’s gonna cost to start that war in their own UI. In 1.5 we’ve added the GetScriptValueBreakdown UI function which lets you specify the name of the script_value you want to break down and the scope context to do it on and it gives you the exact same data as if we’d natively done it from code. For example in my custom widget I’ve made the button tooltip give a breakdown of the cost if I were to increase my crown authority entirely separate from the usually needed button to evaluate that cost in the realms UI. View attachment 798179 We hope this will let mods better explain their own custom values in a more clear way, be that something like your mana in a fantasy mod or custom score for a special event chain. Events and Localization​To make life easier for our modders and designers to work with events we’ve added and reworked a few debug buttons in the event window. Now every event has these five icons in the top right corner. View attachment 798176 In order they let you: Regenerate the event contents, useful if you’ve changed something that cannot hot reload. Toggle the data system globally, this makes most everything in square brackets show exactly what you typed instead of localizing to some output, this is available via the console commands too Copy the event text to your clipboard Shows you the trigger evaluation that had to be true for you to get this event Debug info about the current scope context and how keys used to build the description We’ve found that having easy access to these makes it a lot simpler to debug events and iterate on content. Though do be warned that toggling off the data system can give you some truly cursed looking windows since now instead of seeing the number 4 you see the joyous underlying constructs such as this monstrosity of a window: View attachment 798175 In a more mechanical improvement we’ve also added a boilerplate reduction for having events on a cooldown, instead of needing to manually check and juggle flags and variables yourself you can now specify a cooldown on the event in days/weeks/months/years as some value and it will automatically handle applying a flag that will clear after that time blocking the event from being fired on a character. Console Commands​We have added a variety of new console commands in 1.5 to help make creating and testing mods a bit easier, and instead of explaining them myself I am just gonna cheat and rip their change log entries out! Added console command "bypass_requirements" (alias "bypass") that lets you do decisions, interactions, schemes, laws, and title creation despite the requirements not being met Added console command "instasiege" Added console command "save_every" and startup parameter "-save_every=x". These will make a save every x years, and ensure they do not get overwritten by normal autosaves Added console command AI.try_send_decision Added console command AI.try_send_interaction Added console command Ironman.ToggleIgnore. When ignored, saves will act as if they're not ironman, including that when you hit save it'll result in a non-ironman save. This can be toggled during gameplay Added console command ToggleShowAllKillers Added console command complete_schemes, guaranteed_scheme_success/failure, and guaranteed_scheme_secrecy_success/failure. The success/secrecy ones only affect the player Added console command set_date Added console command show_regions_in_tooltip Added console command toggle_keys_on_map Added console commands "yesmen_instant" (AKA "ymi") and "instant_responses". The yesmen button in the console can now be right-clicked to run "yesmen_instant" The bypass and save_every commands have been especially helpful in setting up scenarios to test scripts and make sure it works exactly as you had intended in your mods. As are the forcing the AI to try out an interaction instead of waiting for them to do it of their own free will. Modifiers Everywhere​In 1.5 we’ve made some improvements to modifiers so if you use an invalid modifier type somewhere it will error and let you know its not going to work. Which has been very useful as in 1.5 we’ve greatly expanded upon modifier support in buildings, now buildings can not only apply modifiers to you in general but they can also apply specific modifiers based on culture parameters which are applied by traditions. These can be used in the modifiers affecting the character, province, county and duchy_capital_county modifiers. In addition there is a province_terrain_modifier which can apply a modifier based optionally on: terrain type, being coastal, being by a river, and by culture parameter. So traditions can really matter in your mods and let cultures play in vastly different ways. View attachment 798190 Clock’s a ticking​Release day is coming soon and we’re very excited to see what mods are going to do with Royal Court, especially with the court scene itself which we hope in the future to see some fantastic 3D scenes especially from fantasy mods. I’m gonna get back to the last minute release period scramble, thank you for reading and I hope you’re looking forward to Royal Court’s release and the great mods we’re gonna be able to see in the future too! Click to expand...
<!-- artifact:quote:end -->
Can I have a promise that same sex modding being allowed by the script won't cause it to happen with the rule turned off. Like how in ck2 you could have same sex lovers marry via the event chain with coming across lovers whilst the gates were lowered, in vanilla

## Reply 20 — participant_019 · 2022-01-25 · post-28034807

<!-- artifact:quote:start -->
> blackninja9939 said: Same-Sex Marriage​Coming with 1.5 is support for same-sex marriage, not only just in mods either but as a new game rule alongside the Same-Sex relations game rule so you can use it in un-modded games too. We've updated a variety of AI logic and interactions and content to take that into account when playing. View attachment 798177 Mods are of course able to implement this into their different worlds without it having to be a game rule, it can be based on different cultures or anything in the game world at all. This is something that we’re very happy to be able to put into the game and have support in the game rules for unmodded games too, it is something that a lot of the team and community wanted and we are glad it is finally going to be shipped in 1.5. Click to expand...
<!-- artifact:quote:end -->
Well, how about pregnancy? I mean a woman gets another pregnant (by mod, of course)

## Reply 21 — participant_018 · 2022-01-25 · post-28034815

<!-- artifact:quote:start -->
> luanmameili[LM] said: Well, how about pregnancy? I mean a woman gets another pregnant (by mod, of course) Click to expand...
<!-- artifact:quote:end -->
Ck2 had child pregnancy due to the queen of Jerusalem being married whilst underage in one bookmark

## Reply 22 — participant_020 · 2022-01-25 · post-28034838

<!-- artifact:quote:start -->
> Salazard260 said: Gay mariages as a game rule is the best way of implementing it imo, doesn't affect those who don't want to play around with it, much easier to have it on in mp games (than if it was a mod). Quick questions : - will the AI do it or just players ? - Does it work with all mariage types (monogamy, polygamy, consorts etc) - How is it unlocked ? Click to expand...
<!-- artifact:quote:end -->
Wait a second. I think I'd have to disagree on your first point. I mean if you reform your religion to accept same sex relationships shouldn't characters (of that religion, in a realm of that religion) be able to marry that way? You literally made it accepted and it won't affect people who don't make a religion like that. No gamerule-editing required and ironman-compatible. Seems the logical option in my eyes at least.

## Reply 23 — participant_021 · 2022-01-25 · post-28034862

<!-- artifact:quote:start -->
> Salazard260 said: Gay mariages as a game rule is the best way of implementing it imo, doesn't affect those who don't want to play around with it, much easier to have it on in mp games (than if it was a mod). Quick questions : - will the AI do it or just players ? - Does it work with all mariage types (monogamy, polygamy, consorts etc) - How is it unlocked ? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> LeSingeAffame said: I suppose not as you'd otherwise have explicitely said it, but does it also apply to doctrine parameters? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> JasonSTGer said: Glitterhoof says: 4808 errors and 31 FPS on a dev PC Do we need to worry? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> luanmameili[LM] said: Well, how about pregnancy? I mean a woman gets another pregnant (by mod, of course) Click to expand...
<!-- artifact:quote:end -->
When the game rule is on the AI will also do it yeah, its enabled as changing the setup of the world. It should work with all other marriage types, it is integrated through the normal interactions for marriage and all partnership types. I don't believe so no Haha no no need to worry, as was already answered about the FPS everyone has a different spec. In this case its not great in addition because I am on a bad laptop remote desktoping into my PC. The errors themselves are from me making a script mistake in my example modded windows which then of course give a bunch of errors every frame until I fixed it, I just forgot to clear the errors before. No same-sex pregnancy currently, a lotttt of code and even more script makes very strong assumptions about parentage that would need a bigger pass to integrate it and not just lead to a lot of bug reports. But never say never though, I know folks on the team have looked at it before though hence why we saw it was a bit more of a challenge.

## Reply 24 — participant_022 · 2022-01-25 · post-28034877

<!-- artifact:quote:start -->
> blackninja9939 said: When the game rule is on the AI will also do it yeah, its enabled as changing the setup of the world. It should work with all other marriage types, it is integrated through the normal interactions for marriage and all partnership types. I don't believe so no Haha no no need to worry, as was already answered about the FPS everyone has a different spec. In this case its not great in addition because I am on a bad laptop remote desktoping into my PC. The errors themselves are from me making a script mistake in my example modded windows which then of course give a bunch of errors every frame until I fixed it, I just forgot to clear the errors before. No same-sex pregnancy currently, a lotttt of code and even more script makes very strong assumptions about parentage that would need a bigger pass to integrate it and not just lead to a lot of bug reports. But never say never though, I know folks on the team have looked at it before though hence why we saw it was a bit more of a challenge. Click to expand...
<!-- artifact:quote:end -->
Is there adoption in the game?

## Reply 25 — participant_023 · 2022-01-25 · post-28034880

Thank you, thank you for making same-sex marriage a game rule! I would never have expected a game about this time period to be so women- and queer-friendly but it's absolutely wonderful and the reason I keep playing. So few games even acknowledge anything other than straight and sometimes gay - making CK3 the only game that has ever allowed me to be explicitly ace. It means so much to me and I'm so glad to see y'all continuing to be inclusive in the vanilla game, where it's available to everyone now if only we could be trans and nonbinary...

## Reply 26 — participant_024 · 2022-01-25 · post-28034892

<!-- artifact:quote:start -->
> blackninja9939 said: Same-Sex Marriage​Coming with 1.5 is support for same-sex marriage, not only just in mods either but as a new game rule alongside the Same-Sex relations game rule so you can use it in un-modded games too. We've updated a variety of AI logic and interactions and content to take that into account when playing. View attachment 798177 Click to expand...
<!-- artifact:quote:end -->
I hope this is only for modders and not ingame as it makes no sense historically!

## Reply 27 — participant_025 · 2022-01-25 · post-28034935

<!-- artifact:quote:start -->
> Prometheus_1 said: I hope this is only for modders and not ingame as it makes no sense historically! Click to expand...
<!-- artifact:quote:end -->
It is a game rule you can turn on, of couse it is not historical and never pretended to be.

## Reply 28 — participant_026 · 2022-01-25 · post-28034937

Excellent, excellent, excellent! Lots of great tools for skilled modders and noobs like myself. Can we increase the number of Slots? For example, the court room editor shows 3 slots for wall_big. Can we add wall_big_4, 5, etc? Is there a maximum number of slots we can add? Can it be changed by code only, or can it be edited by script and/or court room editor? You said that character slots have limitations in terms of which characters the game will slot in. But can we physically move the character slots? For example, if we want to add a Player Heir throne on the ruler's right, is that scriptable and/or editable with court room editor? What's the max number of slots we can create?

## Reply 29 — participant_027 · 2022-01-25 · post-28034938

<!-- artifact:quote:start -->
> Prometheus_1 said: I hope this is only for modders and not ingame as it makes no sense historically! Click to expand...
<!-- artifact:quote:end -->
It says it's a gamerule in your own quote.

## Reply 30 — participant_020 · 2022-01-25 · post-28034945

<!-- artifact:quote:start -->
> Prometheus_1 said: I hope this is only for modders and not ingame as it makes no sense historically! Click to expand...
<!-- artifact:quote:end -->
what are you talking about? This is a game about rewriting history. If you rewrote it in such a way that your religion accepts same sex relationships (which you can already do) then you should obviously be able to marry that way too. It also makes no sense historically that I can migrate as a norse tribe into India. These games live from the way they allow players to play with the timeline.

## Reply 31 — participant_021 · 2022-01-25 · post-28034949

<!-- artifact:quote:start -->
> Anonymous01 said: Excellent, excellent, excellent! Lots of great tools for skilled modders and noobs like myself. Can we increase the number of Slots? For example, the court room editor shows 3 slots for wall_big. Can we add wall_big_4, 5, etc? Is there maximum number of slots we can add? Can it be changed by code only, or can it be edited by script and/or court room editor? You said that character slots have limitations in terms of which characters the game will slot in. But can we physically move the character slots? For example, if we want to add a Player Heir throne on the ruler's right, is that scriptable and/or editable with court room editor? What's the max number of slots we can create? Click to expand...
<!-- artifact:quote:end -->
Yep you can add as many things as you want (well within reason I'm sure we'll run out of memory eventually) and these can all be done in the edtitor. You can move the character positions around and add more all with the editor too, and you can add new roles in the script files too for different logic of who fills them.

## Reply 32 — participant_028 · 2022-01-25 · post-28034951

<!-- artifact:quote:start -->
> Same-Sex Marriage​ Click to expand...
<!-- artifact:quote:end -->
The existence of this non-default game rule that I will never use and can entirely ignore the existence of causes me to feel a vast and terrible rage that no reason or sense can hope to penetrate. [beat] ...to be clear, that was a a joke. Seriously, though, you just saved at least two mods taking place in worlds where gay marriage is canon a lot of work. So if I understand correctly, default rules will be "even gay-tolerant societies won't have gay marriage, they'll just not worry about those relations", and outright permitting marriage will be an optional rule? Will it be possible for gay marriage to be a thing that is "earned", e.g. by founding a heretical faith and fighting for a foothold, while starting in a more historically accurate situation?

## Reply 33 — participant_009 · 2022-01-25 · post-28034963

<!-- artifact:quote:start -->
> Anonymous01 said: Excellent, excellent, excellent! Lots of great tools for skilled modders and noobs like myself. Can we increase the number of Slots? For example, the court room editor shows 3 slots for wall_big. Can we add wall_big_4, 5, etc? Is there maximum number of slots we can add? Can it be changed by code only, or can it be edited by script and/or court room editor? You said that character slots have limitations in terms of which characters the game will slot in. But can we physically move the character slots? For example, if we want to add a Player Heir throne on the ruler's right, is that scriptable and/or editable with court room editor? What's the max number of slots we can create? Click to expand...
<!-- artifact:quote:end -->
Thrones are a bit special, and strictly limited to ruler and spouse. It's an unfortunate limitation, but there's already enough complexity with spawning right objects close to the right people, with right animations etc. Also remember that ruler throne gets a currently equipped court throne artifact, if it exists. If it helps, you're free to redefine ruler and spouse roles in any way you wish and let any 2 scripted people take the chairs/seats.

## Reply 34 — participant_026 · 2022-01-25 · post-28034971

<!-- artifact:quote:start -->
> blackninja9939 said: Yep you can add as many things as you want (well within reason I'm sure we'll run out of memory eventually) and these can all be done in the edtitor. You can move the character positions around and add more all with the editor too, and you can add new roles in the script files too for different logic of who fills them. Click to expand...
<!-- artifact:quote:end -->
Amazing! Thanks for your excellent work!

## Reply 35 — participant_029 · 2022-01-25 · post-28034977

<!-- artifact:quote:start -->
> xking said: Is there adoption in the game? Click to expand...
<!-- artifact:quote:end -->
Historically it would make sense to expand on the in-game ward system, say if your wards parents die you would have an option of making him your legal heir or something like that...

## Reply 36 — participant_030 · 2022-01-25 · post-28034982

<!-- artifact:quote:start -->
> TheGrinningMan said: Will it be possible for gay marriage to be a thing that is "earned", e.g. by founding a heretical faith and fighting for a foothold, while starting in a more historically accurate situation? Click to expand...
<!-- artifact:quote:end -->
+1 I'd also like to see this functionality implemented in a way that is not either a choice of being completely historical or completely ahistorical, allowing it to be a feature of heresies you create in-game.

## Reply 37 — participant_031 · 2022-01-25 · post-28034985

As a gay man, I am so happy we're adding in an option for same-sex marriage. Naturally, I will never enable it because sleeping with all five of the Pentarchs is much more fun when it's illegal, but thanks guys!

## Reply 38 — participant_032 · 2022-01-25 · post-28035005

My body is ready. So is potato jesus.

## Reply 39 — participant_033 · 2022-01-25 · post-28035007

I haven’t been this excited since a male painted bunting visited my garden a couple summers ago! . Thank you, all of you!

## Reply 40 — participant_003 · 2022-01-25 · post-28035016

<!-- artifact:quote:start -->
> Azhcristokos said: As a gay man, I am so happy we're adding in an option for same-sex marriage. Naturally, I will never enable it because sleeping with all five of the Pentarchs is much more fun when it's illegal, but thanks guys! Click to expand...
<!-- artifact:quote:end -->
It would be very cute having a gay character who starts his own religion just so he can marry his partner.

## Reply 41 — participant_026 · 2022-01-25 · post-28035018

Can the court room editor generate a script file? So that when the player makes changes with the in-game editor, they can export it to a script file that they can then copy/paste to mod folders? This question is for any modder, player, or dev who might know. It would be a huge game changer for noob modders obviously.

## Reply 42 — participant_031 · 2022-01-25 · post-28035021

<!-- artifact:quote:start -->
> riadach said: It would be very cute having a gay character who starts his own religion just so he can marry his partner. Click to expand...
<!-- artifact:quote:end -->
It would be even cuter if that new religion were a warmongering fundamentalist church with a crusade-happy ruler. <3

## Reply 43 — participant_003 · 2022-01-25 · post-28035036

<!-- artifact:quote:start -->
> Azhcristokos said: It would be even cuter if that new religion were a warmongering fundamentalist church with a crusade-happy ruler. <3 Click to expand...
<!-- artifact:quote:end -->
Everyone has a fetish.

## Reply 44 — participant_020 · 2022-01-25 · post-28035045

<!-- artifact:quote:start -->
> Azhcristokos said: It would be even cuter if that new religion were a warmongering fundamentalist church with a crusade-happy ruler. <3 Click to expand...
<!-- artifact:quote:end -->
see? THIS is the kind of ck3 we need.

## Reply 45 — participant_021 · 2022-01-25 · post-28035061

<!-- artifact:quote:start -->
> Anonymous01 said: Can the court room editor generate a script file? So that when the player makes changes with the in-game editor, they can export it to a script file that they can then copy/paste to mod folders? This question is for any modder, player, or dev who might know. It would be a huge game changer for noob modders obviously. Click to expand...
<!-- artifact:quote:end -->
That is exactly how it works already, the editor outputs a script file you then get to work with.

## Reply 46 — participant_034 · 2022-01-25 · post-28035066

<!-- artifact:quote:start -->
> riadach said: It would be very cute having a gay character who starts his own religion just so he can marry his partner. Click to expand...
<!-- artifact:quote:end -->
Wouldn't be all that far away from what Henry VIII did so he could divorce Katherine of Aragon, and marry Anne Boleyn...

## Reply 47 — participant_035 · 2022-01-25 · post-28035084

<!-- artifact:quote:start -->
> blackninja9939 said: Coming with 1.5 is support for same-sex marriage, not only just in mods either but as a new game rule alongside the Same-Sex relations game rule so you can use it in un-modded games too.​ Click to expand...
<!-- artifact:quote:end -->
Sounds useful, I just hope it won't cause too many branches of the family to marry in non-productive ways.

## Reply 48 — participant_020 · 2022-01-25 · post-28035100

<!-- artifact:quote:start -->
> blackninja9939 said: Same-Sex Marriage​Coming with 1.5 is support for same-sex marriage, not only just in mods either but as a new game rule alongside the Same-Sex relations game rule so you can use it in un-modded games too. We've updated a variety of AI logic and interactions and content to take that into account when playing. Click to expand...
<!-- artifact:quote:end -->
Actually I have some questions in regard to this. If I enable the same-sex-marriage gamerule, but not the same-sex-relations gamerule, will it result in such a way that I and the AI can marry same-sex but only after having allowed same-sex relations via religion? Or would people just marry same-sex disregarding acceptance of same-sex-relationships? Also how does the sexual orientation of a character factor into this? The AI should only initiate a marriage that way if the character in question has the particular inclination, right?

## Reply 49 — participant_036 · 2022-01-25 · post-28035105

<!-- artifact:quote:start -->
> blackninja9939 said: Hello everyone and welcome to the 87th CK3 Dev Diary! I’m Matthew, one of the Programmers on the CK3 team, and today I am going to talk to you about a variety of improvements and changes we’ve done to modding for the 1.5 patch which will be accompanying the Royal Court Expansion. We’ve added a variety of mod support in 1.5 so I’m not gonna cover everything, but I will give a few big ticket items that will let mods do a lot more fun custom things as well a few smaller fun ones. I’ve also attached the output of script_docs on 1.5 at the end so modders curious about the new triggers and effects in game can get a bit of a sneak peek for the release. The Royal Court​Of course the Royal Court itself is open to mods, it is all defined in the gfx/court_scene folder though the majority of the complex scene_settings itself is best built using the in-game editor that we are shipping with the court scene. It lets you position and change objects and switch between different settings much faster than trying to edit them all by hand. Trust me, cause I remember the time whilst the editor was work in progress and doing changes by hand crushed my soul. View attachment 798174 I am not going to go into a huge amount of detail on the royal court modding because it is actually pretty straightforward with the editor, you position things and pick the assets you need for a configuration and then it just puts things there. One aspect I will go into a bit more info on quickly is the character positioning, because the rest of the positioning is set within the editor but the characters are not positioned individually because of course not every court has the King of England to reference. Instead the character positions are given a set of valid roles, and you pick a position where someone who has one of those roles may go. For example the two guards you see in the back are two positioned instances of the guard and knight role, which has a variety of rules of who it should pick. If you have a bodyguard or champion court position appointed for example then it tries to use them as a special guard, but if you do not then it will fallback to picking any of your knights instead. You can also have some more special roles such as if you have a court jester or poet appointed then they can show up in your court too. View attachment 798189 Characters can not show up in multiple different roles and it is a “greedy” picking of first come first served in who is taken up, but you can write some fairly complex rules to decide who can go where as well as what animations they can choose from! Same-Sex Marriage​Coming with 1.5 is support for same-sex marriage, not only just in mods either but as a new game rule alongside the Same-Sex relations game rule so you can use it in un-modded games too. We've updated a variety of AI logic and interactions and content to take that into account when playing. View attachment 798177 Mods are of course able to implement this into their different worlds without it having to be a game rule, it can be based on different cultures or anything in the game world at all. This is something that we’re very happy to be able to put into the game and have support in the game rules for unmodded games too, it is something that a lot of the team and community wanted and we are glad it is finally going to be shipped in 1.5. Scripted Widgets​CK3 is one of our most moddable games yet, not just in terms of the content that can be added but the system's mods can script. And our new UI system is the most open we’ve had in terms of what custom UIs mods can add and edit, but one issue it had was letting you add brand new things entirely and keeping compatibility nicely. In 1.5 there is a new system called “scripted widgets”, what they allow for in essence is a mod to define their own brand new windows in the gui files and then add an entry into the gui/scripted_widgets folder with the name of their gui file and the main window. For example: gui/test_custom_widget.gui = my_first_cool_test_widget gui/test_custom_widget.gui = my_second_cool_test_widget Then with that simple line of script their window will appear in the game in the same way any of the windows we support in code do. Now of course there are some limitations, the windows do not have any special data context like a code one does but it can access anything that is set globally or on the local player character which covers more than enough cases normally. View attachment 798178 This may not sound hugely impactful, but it means that mods going forward can easily create large systems which can then more easily be compatible with other mods that add systems or if they feel brave enough even with larger Total Conversions if they do not cross over in incompatible design choices. I am really excited to see the new UIs that mods end up making for their gameplay systems and getting to try a few different mods together. Hopefully their windows have a bit more functionality and effort put into it than my testing one… Value Breakdowns​Another bit of UI functionality that mods could not nicely mimic is getting breakdowns of their numbers in the same way we break down a value like your prestige income or how much piety it’s gonna cost to start that war in their own UI. In 1.5 we’ve added the GetScriptValueBreakdown UI function which lets you specify the name of the script_value you want to break down and the scope context to do it on and it gives you the exact same data as if we’d natively done it from code. For example in my custom widget I’ve made the button tooltip give a breakdown of the cost if I were to increase my crown authority entirely separate from the usually needed button to evaluate that cost in the realms UI. View attachment 798179 We hope this will let mods better explain their own custom values in a more clear way, be that something like your mana in a fantasy mod or custom score for a special event chain. Events and Localization​To make life easier for our modders and designers to work with events we’ve added and reworked a few debug buttons in the event window. Now every event has these five icons in the top right corner. View attachment 798176 In order they let you: Regenerate the event contents, useful if you’ve changed something that cannot hot reload. Toggle the data system globally, this makes most everything in square brackets show exactly what you typed instead of localizing to some output, this is available via the console commands too Copy the event text to your clipboard Shows you the trigger evaluation that had to be true for you to get this event Debug info about the current scope context and how keys used to build the description We’ve found that having easy access to these makes it a lot simpler to debug events and iterate on content. Though do be warned that toggling off the data system can give you some truly cursed looking windows since now instead of seeing the number 4 you see the joyous underlying constructs such as this monstrosity of a window: View attachment 798175 In a more mechanical improvement we’ve also added a boilerplate reduction for having events on a cooldown, instead of needing to manually check and juggle flags and variables yourself you can now specify a cooldown on the event in days/weeks/months/years as some value and it will automatically handle applying a flag that will clear after that time blocking the event from being fired on a character. Console Commands​We have added a variety of new console commands in 1.5 to help make creating and testing mods a bit easier, and instead of explaining them myself I am just gonna cheat and rip their change log entries out! Added console command "bypass_requirements" (alias "bypass") that lets you do decisions, interactions, schemes, laws, and title creation despite the requirements not being met Added console command "instasiege" Added console command "save_every" and startup parameter "-save_every=x". These will make a save every x years, and ensure they do not get overwritten by normal autosaves Added console command AI.try_send_decision Added console command AI.try_send_interaction Added console command Ironman.ToggleIgnore. When ignored, saves will act as if they're not ironman, including that when you hit save it'll result in a non-ironman save. This can be toggled during gameplay Added console command ToggleShowAllKillers Added console command complete_schemes, guaranteed_scheme_success/failure, and guaranteed_scheme_secrecy_success/failure. The success/secrecy ones only affect the player Added console command set_date Added console command show_regions_in_tooltip Added console command toggle_keys_on_map Added console commands "yesmen_instant" (AKA "ymi") and "instant_responses". The yesmen button in the console can now be right-clicked to run "yesmen_instant" The bypass and save_every commands have been especially helpful in setting up scenarios to test scripts and make sure it works exactly as you had intended in your mods. As are the forcing the AI to try out an interaction instead of waiting for them to do it of their own free will. Modifiers Everywhere​In 1.5 we’ve made some improvements to modifiers so if you use an invalid modifier type somewhere it will error and let you know its not going to work. Which has been very useful as in 1.5 we’ve greatly expanded upon modifier support in buildings, now buildings can not only apply modifiers to you in general but they can also apply specific modifiers based on culture parameters which are applied by traditions. These can be used in the modifiers affecting the character, province, county and duchy_capital_county modifiers. In addition there is a province_terrain_modifier which can apply a modifier based optionally on: terrain type, being coastal, being by a river, and by culture parameter. So traditions can really matter in your mods and let cultures play in vastly different ways. View attachment 798190 Clock’s a ticking​Release day is coming soon and we’re very excited to see what mods are going to do with Royal Court, especially with the court scene itself which we hope in the future to see some fantastic 3D scenes especially from fantasy mods. I’m gonna get back to the last minute release period scramble, thank you for reading and I hope you’re looking forward to Royal Court’s release and the great mods we’re gonna be able to see in the future too! Click to expand...
<!-- artifact:quote:end -->
Well its about time we get meat.

## Reply 50 — participant_037 · 2022-01-25 · post-28035109

I have a few questions in regards to this new same-sex marriage game rule: What is the default setting for this game rule? On, off, or something else? Will changing this game rule away from the default setting disable achievements? What is the prevalence of same-sex marriages in the game when the game rule is on? Do the AI rulers often - or only very rarely marry the same sex?

## Reply 51 — participant_038 · 2022-01-25 · post-28035116

With same sex marriage, how a player's character is supposed to have heirs? There is some "concubinage" system to allow the characters to "do their dynastic duty" while still being married to someone of the gender they like more? Or it's necessary to rely upon other family members?

## Reply 52 — participant_039 · 2022-01-25 · post-28035121

<!-- artifact:quote:start -->
> blackninja9939 said: Same-Sex Marriage Coming with 1.5 is support for same-sex marriage, not only just in mods either but as a new game rule alongside the Same-Sex relations game rule so you can use it in un-modded games too. We've updated a variety of AI logic and interactions and content to take that into account when playing. Mods are of course able to implement this into their different worlds without it having to be a game rule, it can be based on different cultures or anything in the game world at all. This is something that we’re very happy to be able to put into the game and have support in the game rules for unmodded games too, it is something that a lot of the team and community wanted and we are glad it is finally going to be shipped in 1.5. Click to expand...
<!-- artifact:quote:end -->
Does that include possible pregnancy from futa/hermaphrodite characters like it was in CK2?

## Reply 53 — participant_021 · 2022-01-25 · post-28035156

To clarify the same-sex marriage and same-sex relation game rules here is how it works: That is if you turn on same-sex marriage it is for everyone whose faith supports same-sex relations, if you want that for everyone in the game then you can turn both rules to be on!

## Reply 54 — participant_035 · 2022-01-25 · post-28035176

<!-- artifact:quote:start -->
> Cassilda said: With same sex marriage, how a player's character is supposed to have heirs? There is some "concubinage" system to allow the characters to "do their dynastic duty" while still being married to someone of the gender they like more? Or it's necessary to rely upon other family members? Click to expand...
<!-- artifact:quote:end -->
Presumably "hope your brothers, sisters, and cousins get busy". :|

## Reply 55 — participant_033 · 2022-01-25 · post-28035192

<!-- artifact:quote:start -->
> Cassilda said: With same sex marriage, how a player's character is supposed to have heirs? There is some "concubinage" system to allow the characters to "do their dynastic duty" while still being married to someone of the gender they like more? Or it's necessary to rely upon other family members? Click to expand...
<!-- artifact:quote:end -->
“Same-sex marriage and concubinage is available for everyone whose Faith accepts it, and whose culture practices concubinage.”—from the game-rule for same-sex marriage in blackninja’s post above. (Edit: so males could take a female concubine for breeding purposes, and females a male concubine.) Player characters in monogamous marriages could also have a bastard or two and legitimize one, at the cost of losing opinion, etc.

## Reply 56 — participant_040 · 2022-01-25 · post-28035195

<!-- artifact:quote:start -->
> Prometheus_1 said: I hope this is only for modders and not ingame as it makes no sense historically! Click to expand...
<!-- artifact:quote:end -->
This isn't exactly true, depending on how one defines such things. Sub Saharan Africa cultures had (has?) very different ideas of what gender meant.

## Reply 57 — participant_041 · 2022-01-25 · post-28035208

On the topic of console commands, will there be commands to add/remove cultural pillars/traditions like the commands to add/remove faith tenets and doctrines?

## Reply 58 — participant_042 · 2022-01-25 · post-28035212

<!-- artifact:quote:start -->
> blackninja9939 said: To clarify the same-sex marriage and same-sex relation game rules here is how it works: View attachment 798387 That is if you turn on same-sex marriage it is for everyone whose faith supports same-sex relations, if you want that for everyone in the game then you can turn both rules to be on! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Prometheus_1 said: I hope this is only for modders and not ingame as it makes no sense historically! Click to expand...
<!-- artifact:quote:end -->
This is really great, even better than I was hoping for. You guys put to rest those doubts I expressed months ago. I hope someone also makes a mod for a new doctrine option for Same-Sex relations (Criminal, Shunned, Accepted, Marriages) so a player who wants a sense of achievement for it must reform a religion to allow it. (Though at the very least for non-concubinage religions one must have that first so a reformation will still be required for some religions) This argument again? Is making a Viking matriarchal hedonistic incestual nudist cannibalistic sex religion of Jerusalem historical? No, but it's possible in the game, so what's your point?

## Reply 59 — participant_043 · 2022-01-25 · post-28035238

Will it be possible to add rooms like a Throne Room through mods? For example, a dungeon or an observatory

## Reply 60 — participant_044 · 2022-01-25 · post-28035241

I just wish we could mod a titles coat of arms and still get achievements

## Reply 61 — participant_045 · 2022-01-25 · post-28035266

Love the inclusion of same-sex marriage and the thought put into it. Thanks, devs.

## Reply 62 — participant_007 · 2022-01-25 · post-28035280

Is it possible to implement an graphic option to turn off Animation specifically for the Court scenes? Sadly I am in a position where my potato pc can render the animations in map mode sufficiently but it will certainly not be capable to render the court scenes.

## Reply 63 — participant_035 · 2022-01-25 · post-28035283

<!-- artifact:quote:start -->
> Daghost52 said: I just wish we could mod a titles coat of arms and still get achievements Click to expand...
<!-- artifact:quote:end -->
We appear to have a coat of arms editor *in game*, so editing the coat of arms outside the game should no longer be necessary.

## Reply 64 — participant_031 · 2022-01-25 · post-28035307

<!-- artifact:quote:start -->
> Koocai said: What is the default setting for this game rule? On, off, or something else? Click to expand...
<!-- artifact:quote:end -->
The default settings for these things (gender equality, sexuality attitudes, etc.) are usually (always?) historical, meaning that a default game will see the vast majority of religions taking a dim view of same-sex relations. According to the screenshot a dev posted, enabling same-sex marriage will disable achievements actually, while keeping the setting default will allow achievements.

## Reply 65 — participant_040 · 2022-01-25 · post-28035336

<!-- artifact:quote:start -->
> blackninja9939 said: No same-sex pregnancy currently, a lotttt of code and even more script makes very strong assumptions about parentage that would need a bigger pass to integrate it and not just lead to a lot of bug reports. But never say never though, I know folks on the team have looked at it before though hence why we saw it was a bit more of a challenge. Click to expand...
<!-- artifact:quote:end -->
Are you saying it takes a lot of work for one woman to be considered the "real father" by the game or for her to be considered the father by characters in game, or both? I can't speak for everyone else but I really just want the latter as that's what I've read. I was kind of thinking about making a couple of traits one for the female husband and the other for her wives/concubines such that they can't get the fornicator/adulterer traits (nor the events). I don't know if that would work, I'm not that talented. but then that's just the first step.

## Reply 66 — participant_004 · 2022-01-25 · post-28035339

<!-- artifact:quote:start -->
> Daghost52 said: I just wish we could mod a titles coat of arms and still get achievements Click to expand...
<!-- artifact:quote:end -->
Are you talking about that? https://forum.paradoxplaza.com/foru...-diary-71-a-coat-of-arms-of-your-own.1489219/

## Reply 67 — participant_046 · 2022-01-25 · post-28035353

<!-- artifact:quote:start -->
> blackninja9939 said: Same-Sex Marriage​Coming with 1.5 is support for same-sex marriage, not only just in mods either but as a new game rule alongside the Same-Sex relations game rule so you can use it in un-modded games too. We've updated a variety of AI logic and interactions and content to take that into account when playing. Mods are of course able to implement this into their different worlds without it having to be a game rule, it can be based on different cultures or anything in the game world at all. This is something that we’re very happy to be able to put into the game and have support in the game rules for unmodded games too, it is something that a lot of the team and community wanted and we are glad it is finally going to be shipped in 1.5. Click to expand...
<!-- artifact:quote:end -->
I'm very curious as a modder who will be specifically be adding features for same-sex marriage, how it works with patrilinear and matrilinear marriages (as these determine the dominant partner in the marriage based on sex, for example who moves to whose court, and could be useful for mod specific thing like adopting). Also I can see it there are two main cases to cover, when selecting a marriage and when displaying/implementing the marriage. When selecting a marriage I'm guessing it would work something along the line of if you have the matrilinear marriages box checked, then for women it show marriages where they will be the dominant partner (whether same-sex or not) and for men marriages where they won't be the dominant partner (and if you have the matrilinear marriages unbox checked it's the opposite). For displaying/the game remembering who the dominant partner is seems harder to me. Obviously just seeing matrilinear marriage on a marriage between two men or two women doesn't really tell you much (we don't know after the fact who initiated the marriage, which was used to solve the problem above). The one I've thought of it to mark the marriage in a way more useful way is that the older or younger partner is defined to being the dominant partner, but I'm sure there are other ways to resolve this problem. And I'm assuming you already came up with a system, so I'm currious what that is? Also, I'm really glad to see it is being implemented as a game rule Plus really happy to see all the other bits of modding support Great job! Edit: The only thing that would make me more happy than a game rule is if some level above accepted for crime doctrines, like in my mod, existed in the base game. That way I could reform a faith to have gay marriage without a mod (plus all the flavour that could be added for the other doctrines). But I understand there are a lot of other things to work on before something like this is tackled by the devs (and I can't wait to see what you all have in store for us next). Edit2: Fixed example scenario

## Reply 68 — participant_033 · 2022-01-25 · post-28035383

<!-- artifact:quote:start -->
> DreadLindwyrm said: We appear to have a coat of arms editor *in game*, so editing the coat of arms outside the game should no longer be necessary. Click to expand...
<!-- artifact:quote:end -->
Yes, here’s the dev diary, A Coat of Arms of Your Own. (Edit: sorry, @LeSingeAffame - your post wasn’t showing for me when I made this one. )

## Reply 69 — participant_033 · 2022-01-25 · post-28035408

<!-- artifact:quote:start -->
> junassa said: Are you saying it takes a lot of work for one woman to be considered the "real father" by the game or for her to be considered the father by characters in game, or both? I can't speak for everyone else but I really just want the latter as that's what I've read. I was kind of thinking about making a couple of traits one for the female husband and the other for her wives/concubines such that they can't get the fornicator/adulterer traits (nor the events). I don't know if that would work, I'm not that talented. but then that's just the first step. Click to expand...
<!-- artifact:quote:end -->
If you play in debug mode, I believe you can use the pregnancy console command to impregnate one female with another—I’ve accidentally self-impregnated a character, so that she was the secret, real father of her own child. Those poor creatures all mysteriously died , and I didn’t play around with this...feature, but it might be a ...fruitful area to explore. (Edit: you could probably reveal the secret & use console commands to remove any undesired traits like bastard, fornicator, or adulterer. And you’d have a two-mothers child.)

## Reply 70 — participant_047 · 2022-01-25 · post-28035419

<!-- artifact:quote:start -->
> pengoyo said: Edit: The only thing that would make me more happy than a game rule is if some level above accepted for crime doctrines, like in my mod, existed in the base game. Click to expand...
<!-- artifact:quote:end -->
Yeah, this would be really nice since it removes the need for modding, and it would be better in terms of RP, but the fact that they added it as a game rule is already more than what I expected so I'm not going to complain.

## Reply 71 — participant_048 · 2022-01-25 · post-28035475

<!-- artifact:quote:start -->
> Prometheus_1 said: I hope this is only for modders and not ingame as it makes no sense historically! Click to expand...
<!-- artifact:quote:end -->
and some how conquering the whole european continent makes it historical?

## Reply 72 — participant_049 · 2022-01-25 · post-28035496

<!-- artifact:quote:start -->
> pengoyo said: That way I could reform a faith to have gay marriage without a mod Click to expand...
<!-- artifact:quote:end -->
Already possible, because the same-sex marriage game rule applies only to characters whose faith accepts same-sex relations. So if you set your game rules to same-sex marriage enabled, same-sex relations historical, you won't have access to same-sex marriage until you reform your faith to allow it. You need a mod only if you want both states (same-sex marriage allowed/same-sex relations accepted but not allowed to marry) to exist for different faiths in the same game.

## Reply 73 — participant_046 · 2022-01-25 · post-28035531

<!-- artifact:quote:start -->
> Gulsen said: Yeah, this would be really nice since it removes the need for modding, and it would be better in terms of RP, but the fact that they added it as a game rule is already more than what I expected so I'm not going to complain. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> bfrobin446 said: Already possible, because the same-sex marriage game rule applies only to characters whose faith accepts same-sex relations. So if you set your game rules to same-sex marriage enabled, same-sex relations historical, you won't have access to same-sex marriage until you reform your faith to allow it. You need a mod only if you want both states (same-sex marriage allowed/same-sex relations accepted but not allowed to marry) to exist for different faiths in the same game. Click to expand...
<!-- artifact:quote:end -->
100% agree. I thought same-sex marriage was going to be just a modding featur. So it already being in game is way more than I was expecting. I figure something like what I'm doing with my mod won't come until they the devs feel the have the main part of the game covered and start to go more into the realm of supporting alt-history. Which I can totally get behind. There are many features, like trade, that I'd like to see first before alt-history starts getting serious support. Yeah, I guess my wording wasn't the most precise (edit: and reading comprehension skills either lol, see edit below). Because for say Catholicism you are totally right, But if I play as faith that accepts homosexuality, like Mullwadism, with the game rule on, then that faith starts the game with same-sex marriage (which is something I'm glad is an option). But I then don't have the option to take that accepting faith, as it historically was with no same-sex marriage, and reform it to now have same-sex marriage. This is where having a doctrine level above accepted would be nice, as it would allow your to start in the historical scenario with any faith and move to an alt-history scenario where same-sex marriage happened a lot earlier (or at least more prominently based on what you accept as historical instances of same-sex marriage). edit: Just realized that you covered this in your closing sentence. So yeah I agree. But this is a pretty niche scenario, so I'm not complaining that it isn't in the game.

## Reply 74 — participant_042 · 2022-01-25 · post-28035547

<!-- artifact:quote:start -->
> bfrobin446 said: Already possible, because the same-sex marriage game rule applies only to characters whose faith accepts same-sex relations. So if you set your game rules to same-sex marriage enabled, same-sex relations historical, you won't have access to same-sex marriage until you reform your faith to allow it. You need a mod only if you want both states (same-sex marriage allowed/same-sex relations accepted but not allowed to marry) to exist for different faiths in the same game. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pengoyo said: Because for say Catholicism you are totally right, But if I play as faith that accepts homosexuality, like Mullwadism, with the game rule on, then that faith starts the game with same-sex marriage (which is something I'm glad is an option). But I then don't have the option to take that accepting faith, as it historically was with no same-sex marriage, and reform it to now have same-sex marriage. Click to expand...
<!-- artifact:quote:end -->
There are a few faiths that already qualify (quite a bit less than I initially suspected so most of them will have to be reformed to either Accepted same-sex relations, concubinage or both). These are (assuming their tenets and doctrines are not changed in patch 1.5): -Adamitism -Nangchos -Vajrayana -Gyur Bön -Khyarwé Bön -Bori -Yoruba -Kushitism -Hellenism While you are right that it has Accepted Same-sex Relations, you still need Concubinage for it. I'm aware may feel odd but I guess you can RP it as only after reformation when you include concubinage that same sex marriages were allowed or something.

## Reply 75 — participant_046 · 2022-01-25 · post-28035583

<!-- artifact:quote:start -->
> GoldenSilver said: While you are right that it has Accepted Same-sex Relations, you still need Concubinage for it (which I'm aware may feel odd but I guess you can RP it as only after reformation when you include concubinage same sex marriages were allowed or something). Click to expand...
<!-- artifact:quote:end -->
I think the wording of the game rule is a bit ambiguous, but I took the "and whose cultures practice concubinage" to be a qualifier on the concubinage part of the previous clause, not the marriage part. Especially since they mention in the next sentence that to enable it for everyone you just need to make same-sex relations accepted in every faith, but that wouldn't be true if concubinage was also required. Also gating it behind concubinage seems weird design choice as polygamy can easily get around the problem of an heir too. But even monogamous faiths can use seduction or just letting your titles pass to your siblings are valid option for a ruler with a same-sex spouse (or you can hope to get the adoption court event they showed off previously). So I'd be surprised if Paradox did that and then also failed to mention it in their main post announcing the feature.

## Reply 76 — participant_028 · 2022-01-25 · post-28035605

Just realized something. I recall discussion on the After the End CK3 Discord, about how they intended to implement gay marriage. Their idea was to divide "accepted" into "tolerated" and "accepted". The thought was that the former would work like vanilla CK3, providing no maluses to people in homosexual relationships but also not permitting gay marriages, with only the latter actively allowing gay marriage. The former would be for the more tolerant, live-and-let-live post-apocalyptic pagans, while the latter would be for hippie/new age descendants like the Gaians. And of course, moving from "criminal" to "tolerated" would be cheaper than "criminal" to outright "accepted", which makes sense. I'm wondering if they'll still be able to implement that level of granularity.

## Reply 77 — participant_042 · 2022-01-25 · post-28035612

<!-- artifact:quote:start -->
> pengoyo said: I think the wording of the game rule is a bit ambiguous, but I took the "and whose cultures practice concubinage" to be a qualifier on the concubinage part of the previous clause, not the marriage part. Especially since they mention in the next sentence that to enable it for everyone you just need to make same-sex relations accepted in every faith, but that wouldn't be true if concubinage was also required. Also gating it behind concubinage seems weird design choice as polygamy can easily get around the problem of an heir too. But even monogamous faiths can use seduction or just letting your titles pass to your siblings are valid option for a ruler with a same-sex spouse (or you can hope to get the adoption court event they showed off previously). So I'd be surprised if Paradox did that and then also failed to mention it in their main post announcing the feature. Click to expand...
<!-- artifact:quote:end -->
Now that you mentioned it, it does seem a bit odd. I had a look at the culture ethos and traditions and saw nothing related to concubinage, so I guess they still mean the faith concubinage marriage type? No clue about the enable for everyone part however...

## Reply 78 — participant_046 · 2022-01-25 · post-28035616

<!-- artifact:quote:start -->
> TheGrinningMan said: Just realized something. I recall discussion on the After the End CK3 Discord, about how they intended to implement gay marriage. Their idea was to divide "accepted" into "tolerated" and "accepted". The thought was that the former would work like vanilla CK3, providing no maluses to people in homosexual relationships but also not permitting gay marriages, with only the latter actively allowing gay marriage. The former would be for the more tolerant, live-and-let-live post-apocalyptic pagans, while the latter would be for hippie/new age descendants like the Gaians. And of course, moving from "criminal" to "tolerated" would be cheaper than "criminal" to outright "accepted", which makes sense. I'm wondering if they'll still be able to implement that level of granularity. Click to expand...
<!-- artifact:quote:end -->
It's definitely implementable, I have done so in my mod, Celebrate Crimes (though I renamed the base game doctrine level of "accepted" to "allowed" and the more tolerant level above that I called "celebrated"). For mods, 1.5 will just allows same-sex marriage, rather than just same-sex concubines, to be implementable now however the modder chooses. edit: clarity

## Reply 79 — participant_046 · 2022-01-25 · post-28035621

<!-- artifact:quote:start -->
> GoldenSilver said: Now that you mentioned it, it does seem a bit odd. I had a look at the culture ethos and traditions and saw nothing related to concubinage, so I guess they still mean the faith concubinage marriage type? No clue about the enable for everyone part however... Click to expand...
<!-- artifact:quote:end -->
Yeah, I don't know what to really make about the culture part of the quote.

## Reply 80 — participant_050 · 2022-01-25 · post-28035676

Can you allow us to actually change the names of titles for clan rulers? As of now, it only shows dynasty names on the map and even if you manually change the title name, nothing happens. For example, when i change the "Arabian Empire" in 867 to "Abbasid Caliphate", it still shows "Abbasid", no matter what. I know you can do this by changing the dynasty name, but i think being able to change the actual title name fits better.

## Reply 81 — participant_039 · 2022-01-25 · post-28035682

<!-- artifact:quote:start -->
> White_Drake said: Will it be possible to add rooms like a Throne Room through mods? For example, a dungeon or an observatory Click to expand...
<!-- artifact:quote:end -->
If that's the case, where does the Throne Room end and it becomes a castle (and so what's the point of the throne room, instead of a barony)? Another problem would be the modelling... But I do sort of like that idea. Maybe it would open up some Merchant Republic ideas, which btw, I never bought Paradox's excuse on they "didn't like the succession" argument. If they didn't like elective successions, why is does Scandinavian or Princely Elective exist?

## Reply 82 — participant_051 · 2022-01-25 · post-28035690

<!-- artifact:quote:start -->
> Barron of Gondor said: I can't wait to see a song of ice and fire mod making use of this. Click to expand...
<!-- artifact:quote:end -->
I can't wait to see it even without use of this. With this I guess we'll wait longer.

## Reply 83 — participant_052 · 2022-01-25 · post-28035727

Same sex marriages sound like a surefire way for AI dynasty to go extinct even more and create chaos.

## Reply 84 — participant_046 · 2022-01-25 · post-28035764

<!-- artifact:quote:start -->
> Ixal said: Same sex marriages sound like a surefire way for AI dynasty to go extinct even more and create chaos. Click to expand...
<!-- artifact:quote:end -->
I could also see it create larger realms as partitioned lands are reconsolidated by some of the siblings engaging in same-sex marriages. Really depends on how the AI has been programed to consider these marriages.

## Reply 85 — participant_053 · 2022-01-26 · post-28035820

<!-- artifact:quote:start -->
> Ixal said: Same sex marriages sound like a surefire way for AI dynasty to go extinct even more and create chaos. Click to expand...
<!-- artifact:quote:end -->
I personnaly would like the AI to only use it under conditions : already having two or more heirs, or not possessing nor inheriting titles. Just with that, I think it would be ok. Maybe for polygamous or concubinage, you could allow it as long as you have at least one fertile marriage/concubine, or at the very least you would have room to allow one (fertile).

## Reply 86 — participant_054 · 2022-01-26 · post-28035901

This is really awesome, simply perfectly done. 1.5 and Royal Court is an update that offers an incredible evolution of the game. Cant wait to play it, will be long multiplayer sessions. My custom mod set already has a witch ritual as a mean of gaining children without a suitable partner. But will adoption be coming with 1.5?

## Reply 87 — participant_055 · 2022-01-26 · post-28036061

Just wondering, if Same-sex Marriage is set too off, that means only by a mod it can be enabled correct? Because it'd be very immersion breaking for games which one wants to have realism in.

## Reply 88 — participant_046 · 2022-01-26 · post-28036089

<!-- artifact:quote:start -->
> Sirsquier said: Just wondering, if Same-sex Marriage is set too off, that means only by a mod it can be enabled correct? Because it'd be very immersion breaking for games which one wants to have realism in. Click to expand...
<!-- artifact:quote:end -->
It's definitely a game rule, not a mod, that now determines if same-sex marriages are possible in a play through. But I assume it works how the gender equality, same-sex acceptance, and sexuality distribution game rules already do in game; where there are set to the historical values by default. So they are opt-in game rules for those who want them.

## Reply 89 — participant_056 · 2022-01-26 · post-28036104

All this looks amazing. I was wondering, is it possible for the team to add a page to the ledger that lists the accumulated renown for each dynasty in the game (ideally along with other information about each dynasty, like number of living members, etc)

## Reply 90 — participant_046 · 2022-01-26 · post-28036107

<!-- artifact:quote:start -->
> blackninja9939 said: Now every event has these five icons in the top right corner. View attachment 798176 In order they let you: Regenerate the event contents, useful if you’ve changed something that cannot hot reload. Toggle the data system globally, this makes most everything in square brackets show exactly what you typed instead of localizing to some output, this is available via the console commands too Copy the event text to your clipboard Shows you the trigger evaluation that had to be true for you to get this event Debug info about the current scope context and how keys used to build the description Click to expand...
<!-- artifact:quote:end -->
I am very happy to hear about this new functionality for debugging events. But is it possible to toggle these symbols on and off in debug mode? I like using debug to easily launch new events for screen shots of my mods. But would prefer not to have distracting symbols in the corner.

## Reply 91 — participant_002 · 2022-01-26 · post-28036209

<!-- artifact:quote:start -->
> Daghost52 said: I just wish we could mod a titles coat of arms and still get achievements Click to expand...
<!-- artifact:quote:end -->
You will be able to with royal court. https://forum.paradoxplaza.com/foru...-diary-71-a-coat-of-arms-of-your-own.1489219/

## Reply 92 — participant_022 · 2022-01-26 · post-28036226

<!-- artifact:quote:start -->
> pengoyo said: It's definitely implementable, I have done so in my mod, Celebrate Crimes (though I renamed the base game doctrine level of "accepted" to "allowed" and the more tolerant level above that I called "celebrated"). For mods, 1.5 will just allows same-sex marriage, rather than just same-sex concubines, to be implementable now however the modder chooses. edit: clarity Click to expand...
<!-- artifact:quote:end -->
I have your mod, It's pretty cool.

## Reply 93 — participant_057 · 2022-01-26 · post-28036243

One other thing I'd like to see be moddable is dead characters coming back to life

## Reply 94 — participant_046 · 2022-01-26 · post-28036317

<!-- artifact:quote:start -->
> xking said: I have your mod, It's pretty cool. Click to expand...
<!-- artifact:quote:end -->
Thanks, I'm glad you like it. I'm looking forward to what I can do with it after RC comes out.

## Reply 95 — participant_021 · 2022-01-26 · post-28036394

<!-- artifact:quote:start -->
> Grekopithikos said: One other thing I'd like to see be moddable is dead characters coming back to life Click to expand...
<!-- artifact:quote:end -->
Not likely to happen, once someone is dead we delete large amounts of data about them which putting back together would be rather complicated. And likely introduce bugs into the base game of unintended necromancy.

## Reply 96 — participant_058 · 2022-01-26 · post-28036517

<!-- artifact:quote:start -->
> blackninja9939 said: Not likely to happen, once someone is dead we delete large amounts of data about them which putting back together would be rather complicated. And likely introduce bugs into the base game of unintended necromancy. Click to expand...
<!-- artifact:quote:end -->
i will copy character and start new game . how can i do this easily ? I tried dna but it didn't work game crashed . and i'm going to change the DNA of a few of my favorite characters.

## Reply 97 — participant_024 · 2022-01-26 · post-28036585

<!-- artifact:quote:start -->
> blackninja9939 said: Hello everyone and welcome to the 87th CK3 Dev Diary! I’m Matthew, one of the Programmers on the CK3 team, and today I am going to talk to you about a variety of improvements and changes we’ve done to modding for the 1.5 patch which will be accompanying the Royal Court Expansion. We’ve added a variety of mod support in 1.5 so I’m not gonna cover everything, but I will give a few big ticket items that will let mods do a lot more fun custom things as well a few smaller fun ones. I’ve also attached the output of script_docs on 1.5 at the end so modders curious about the new triggers and effects in game can get a bit of a sneak peek for the release. The Royal Court​Of course the Royal Court itself is open to mods, it is all defined in the gfx/court_scene folder though the majority of the complex scene_settings itself is best built using the in-game editor that we are shipping with the court scene. It lets you position and change objects and switch between different settings much faster than trying to edit them all by hand. Trust me, cause I remember the time whilst the editor was work in progress and doing changes by hand crushed my soul. View attachment 798174 I am not going to go into a huge amount of detail on the royal court modding because it is actually pretty straightforward with the editor, you position things and pick the assets you need for a configuration and then it just puts things there. One aspect I will go into a bit more info on quickly is the character positioning, because the rest of the positioning is set within the editor but the characters are not positioned individually because of course not every court has the King of England to reference. Instead the character positions are given a set of valid roles, and you pick a position where someone who has one of those roles may go. For example the two guards you see in the back are two positioned instances of the guard and knight role, which has a variety of rules of who it should pick. If you have a bodyguard or champion court position appointed for example then it tries to use them as a special guard, but if you do not then it will fallback to picking any of your knights instead. You can also have some more special roles such as if you have a court jester or poet appointed then they can show up in your court too. View attachment 798189 Characters can not show up in multiple different roles and it is a “greedy” picking of first come first served in who is taken up, but you can write some fairly complex rules to decide who can go where as well as what animations they can choose from! Same-Sex Marriage​Coming with 1.5 is support for same-sex marriage, not only just in mods either but as a new game rule alongside the Same-Sex relations game rule so you can use it in un-modded games too. We've updated a variety of AI logic and interactions and content to take that into account when playing. View attachment 798177 Mods are of course able to implement this into their different worlds without it having to be a game rule, it can be based on different cultures or anything in the game world at all. This is something that we’re very happy to be able to put into the game and have support in the game rules for unmodded games too, it is something that a lot of the team and community wanted and we are glad it is finally going to be shipped in 1.5. Scripted Widgets​CK3 is one of our most moddable games yet, not just in terms of the content that can be added but the system's mods can script. And our new UI system is the most open we’ve had in terms of what custom UIs mods can add and edit, but one issue it had was letting you add brand new things entirely and keeping compatibility nicely. In 1.5 there is a new system called “scripted widgets”, what they allow for in essence is a mod to define their own brand new windows in the gui files and then add an entry into the gui/scripted_widgets folder with the name of their gui file and the main window. For example: gui/test_custom_widget.gui = my_first_cool_test_widget gui/test_custom_widget.gui = my_second_cool_test_widget Then with that simple line of script their window will appear in the game in the same way any of the windows we support in code do. Now of course there are some limitations, the windows do not have any special data context like a code one does but it can access anything that is set globally or on the local player character which covers more than enough cases normally. View attachment 798178 This may not sound hugely impactful, but it means that mods going forward can easily create large systems which can then more easily be compatible with other mods that add systems or if they feel brave enough even with larger Total Conversions if they do not cross over in incompatible design choices. I am really excited to see the new UIs that mods end up making for their gameplay systems and getting to try a few different mods together. Hopefully their windows have a bit more functionality and effort put into it than my testing one… Value Breakdowns​Another bit of UI functionality that mods could not nicely mimic is getting breakdowns of their numbers in the same way we break down a value like your prestige income or how much piety it’s gonna cost to start that war in their own UI. In 1.5 we’ve added the GetScriptValueBreakdown UI function which lets you specify the name of the script_value you want to break down and the scope context to do it on and it gives you the exact same data as if we’d natively done it from code. For example in my custom widget I’ve made the button tooltip give a breakdown of the cost if I were to increase my crown authority entirely separate from the usually needed button to evaluate that cost in the realms UI. View attachment 798179 We hope this will let mods better explain their own custom values in a more clear way, be that something like your mana in a fantasy mod or custom score for a special event chain. Events and Localization​To make life easier for our modders and designers to work with events we’ve added and reworked a few debug buttons in the event window. Now every event has these five icons in the top right corner. View attachment 798176 In order they let you: Regenerate the event contents, useful if you’ve changed something that cannot hot reload. Toggle the data system globally, this makes most everything in square brackets show exactly what you typed instead of localizing to some output, this is available via the console commands too Copy the event text to your clipboard Shows you the trigger evaluation that had to be true for you to get this event Debug info about the current scope context and how keys used to build the description We’ve found that having easy access to these makes it a lot simpler to debug events and iterate on content. Though do be warned that toggling off the data system can give you some truly cursed looking windows since now instead of seeing the number 4 you see the joyous underlying constructs such as this monstrosity of a window: View attachment 798175 In a more mechanical improvement we’ve also added a boilerplate reduction for having events on a cooldown, instead of needing to manually check and juggle flags and variables yourself you can now specify a cooldown on the event in days/weeks/months/years as some value and it will automatically handle applying a flag that will clear after that time blocking the event from being fired on a character. Console Commands​We have added a variety of new console commands in 1.5 to help make creating and testing mods a bit easier, and instead of explaining them myself I am just gonna cheat and rip their change log entries out! Added console command "bypass_requirements" (alias "bypass") that lets you do decisions, interactions, schemes, laws, and title creation despite the requirements not being met Added console command "instasiege" Added console command "save_every" and startup parameter "-save_every=x". These will make a save every x years, and ensure they do not get overwritten by normal autosaves Added console command AI.try_send_decision Added console command AI.try_send_interaction Added console command Ironman.ToggleIgnore. When ignored, saves will act as if they're not ironman, including that when you hit save it'll result in a non-ironman save. This can be toggled during gameplay Added console command ToggleShowAllKillers Added console command complete_schemes, guaranteed_scheme_success/failure, and guaranteed_scheme_secrecy_success/failure. The success/secrecy ones only affect the player Added console command set_date Added console command show_regions_in_tooltip Added console command toggle_keys_on_map Added console commands "yesmen_instant" (AKA "ymi") and "instant_responses". The yesmen button in the console can now be right-clicked to run "yesmen_instant" The bypass and save_every commands have been especially helpful in setting up scenarios to test scripts and make sure it works exactly as you had intended in your mods. As are the forcing the AI to try out an interaction instead of waiting for them to do it of their own free will. Modifiers Everywhere​In 1.5 we’ve made some improvements to modifiers so if you use an invalid modifier type somewhere it will error and let you know its not going to work. Which has been very useful as in 1.5 we’ve greatly expanded upon modifier support in buildings, now buildings can not only apply modifiers to you in general but they can also apply specific modifiers based on culture parameters which are applied by traditions. These can be used in the modifiers affecting the character, province, county and duchy_capital_county modifiers. In addition there is a province_terrain_modifier which can apply a modifier based optionally on: terrain type, being coastal, being by a river, and by culture parameter. So traditions can really matter in your mods and let cultures play in vastly different ways. View attachment 798190 Clock’s a ticking​Release day is coming soon and we’re very excited to see what mods are going to do with Royal Court, especially with the court scene itself which we hope in the future to see some fantastic 3D scenes especially from fantasy mods. I’m gonna get back to the last minute release period scramble, thank you for reading and I hope you’re looking forward to Royal Court’s release and the great mods we’re gonna be able to see in the future too! Click to expand...
<!-- artifact:quote:end -->
Could you add please the ability to enable achievements also for localization mods ? Since Paradox doesn't want to translate into Italian or other important languages perhaps could be nice if you allowed localization mods to not invalidate the checksum.

## Reply 98 — participant_059 · 2022-01-26 · post-28036640

I’d like to see a robust in-game adoption system to provide heirs for same-sex couples, tbh.

## Reply 99 — participant_052 · 2022-01-26 · post-28036641

<!-- artifact:quote:start -->
> horngeek said: I’d like to see a robust in-game adoption system to provide heirs for same-sex couples, tbh. Click to expand...
<!-- artifact:quote:end -->
Please no. If you could easily adopt children the whole idea of curating and spreading your dynasty gets diluted and that is a central part of the game.

## Reply 100 — participant_010 · 2022-01-26 · post-28036651

<!-- artifact:quote:start -->
> horngeek said: I’d like to see a robust in-game adoption system to provide heirs for same-sex couples, tbh. Click to expand...
<!-- artifact:quote:end -->
I think it is more practical to appoint a nephew, brother or cousin of your own House or Dynasty as an heir.

## Reply 101 — participant_060 · 2022-01-26 · post-28036670

Any information for modding of artifacts?

## Reply 102 — participant_054 · 2022-01-26 · post-28036678

<!-- artifact:quote:start -->
> blackninja9939 said: Not likely to happen, once someone is dead we delete large amounts of data about them which putting back together would be rather complicated. And likely introduce bugs into the base game of unintended necromancy. Click to expand...
<!-- artifact:quote:end -->
Its true you cant keep all data and you cant put it back together. But you could add a selective variant even if it is only for modders. Meaning you only keep the data of characters flagged for this. Like a dead.2 state, they dont die and run through the death handler clearing them from the game instead they are keep but considered dead. This could be used for example to add prerequisites like a ritual to add not immortality but an unliving state (necromancy, vampires etc.) to characters by player action or to create events that ask the players in chase of an important persons death if they want to try to ressurect them (if they have the means to do so). It can of course also be used as a cheat or a failsave to events. There could also be a state on how long this data will be keept to futher customize amount and usage of ressources depending on what you are trying to do. For example keeping the data of dead characters for 1 ingame month should not cause massive trouble or keeping the data of a small group for a longer time.

## Reply 103 — participant_024 · 2022-01-26 · post-28036684

<!-- artifact:quote:start -->
> Ixal said: Please no. If you could easily adopt children the whole idea of curating and spreading your dynasty gets diluted and that is a central part of the game. Click to expand...
<!-- artifact:quote:end -->
I would like to see adoption may be for kids of the same dinasty that do not have parents, but not to see same sex couples make offsprings .

## Reply 104 — participant_002 · 2022-01-26 · post-28036708

<!-- artifact:quote:start -->
> horngeek said: I’d like to see a robust in-game adoption system to provide heirs for same-sex couples, tbh. Click to expand...
<!-- artifact:quote:end -->
That's what nephews are for (see Frederick the Great, or the current king of Cambodia)

## Reply 105 — participant_010 · 2022-01-26 · post-28036718

<!-- artifact:quote:start -->
> Prometheus_1 said: I would like to see adoption may be for kids of the same dinasty that do not have parents Click to expand...
<!-- artifact:quote:end -->
The option of freely appointing an heir already exists when the fourth level of Crown Authority is achieved.

## Reply 106 — participant_022 · 2022-01-26 · post-28037099

<!-- artifact:quote:start -->
> Leonello d'Este said: The option of freely appointing an heir already exists when the fourth level of Crown Authority is achieved. Click to expand...
<!-- artifact:quote:end -->
Really?

## Reply 107 — participant_061 · 2022-01-26 · post-28037136

<!-- artifact:quote:start -->
> JasonSTGer said: Is it possible to implement an graphic option to turn off Animation specifically for the Court scenes? Sadly I am in a position where my potato pc can render the animations in map mode sufficiently but it will certainly not be capable to render the court scenes. Click to expand...
<!-- artifact:quote:end -->
Yes, they've said you have the option to disable animations for the court such that the scene is rendered once and then is a static scene allowing you to limit graphic usage if you find your computer doesn't handle it well.

## Reply 108 — participant_062 · 2022-01-26 · post-28037208

I'd have wanted Paradox Development studio to spend their (clearly) limited dev time on actual content for the game, or at least balancing it in such a way that major AI powers could actually pose any sort of challenge to the player past the first 10-20 years of the game as OPM rather than modding in gay marriage, but whatever floats their boat I guess.

## Reply 109 — participant_021 · 2022-01-26 · post-28037254

<!-- artifact:quote:start -->
> Draky said: I'd have wanted Paradox Development studio to spend their (clearly) limited dev time on actual content for the game, or at least balancing it in such a way that major AI powers could actually pose any sort of challenge to the player past the first 10-20 years of the game as OPM rather than modding in gay marriage, but whatever floats their boat I guess. Click to expand...
<!-- artifact:quote:end -->
Well thankfully for all of us you aren't in charge of how we spend our time!

## Reply 110 — participant_063 · 2022-01-26 · post-28037485

<!-- artifact:quote:start -->
> blackninja9939 said: Well thankfully for all of us you aren't in charge of how we spend our time! Click to expand...
<!-- artifact:quote:end -->
Apologies, but the user you replied to has brought up a rather important point, despite being rather uncouth about it. While I see the advantages of the gay marriage mechanic for modding and do not have any problems with it, I do question whether it was something the game needs at the moment. Does this highly optional mechanic really help with the various problems this game has at the moment, which Royal Court doesn't seem to really fix? Warfare being rather terrible, Peacetreaties being very binary and uninteractible, Factions being completely out of control for the AI yet still boring to the player, your dynasty not actually really mattering and a general lack of flavour, which after thinking about the dev diaries a bit more, isn't really going to be fixed if the events are all that are shown. It kinda feels like Homosexual Marriage would have been better put aside until later, when the main gameplay functions properly. Honestly, the only part I really am interested in in this DLC is the new Culture system, but even there I am afraid that this will merely cause the remaining cultures to get even blander, with how the assignment of events to the new cultures seems rather unclear. And honestly, seeing this reaction:"Well thankfully for all of us you aren't in charge of how we spend our time!" being used really leaves a bad taste in my mouth, even if it was to that post.

## Reply 111 — participant_064 · 2022-01-26 · post-28037491

<!-- artifact:quote:start -->
> blackninja9939 said: Well thankfully for all of us you aren't in charge of how we spend our time! Click to expand...
<!-- artifact:quote:end -->
I'm not sure what's worse, the audacity of a developer talking down to a player that expressed his opinion without being rude or the crowd cheering the Dev statement as if it was proper behavior.

## Reply 112 — participant_010 · 2022-01-26 · post-28037496

<!-- artifact:quote:start -->
> xking said: Really? Click to expand...
<!-- artifact:quote:end -->
Yes. When you have unlocked the fourth level of Crown Authority you need to consult the succession window.

## Reply 113 — participant_021 · 2022-01-26 · post-28037535

<!-- artifact:quote:start -->
> chelvo said: Apologies, but the user you replied to has brought up a rather important point, despite being rather uncouth about it. While I see the advantages of the gay marriage mechanic for modding and do not have any problems with it, I do question whether it was something the game needs at the moment. Does this highly optional mechanic really help with the various problems this game has at the moment, which Royal Court doesn't seem to really fix? Warfare being rather terrible, Peacetreaties being very binary and uninteractible, Factions being completely out of control for the AI yet still boring to the player, your dynasty not actually really mattering and a general lack of flavour, which after thinking about the dev diaries a bit more, isn't really going to be fixed if the events are all that are shown. It kinda feels like Homosexual Marriage would have been better put aside until later, when the main gameplay functions properly. Honestly, the only part I really am interested in in this DLC is the new Culture system, but even there I am afraid that this will merely cause the remaining cultures to get even blander, with how the assignment of events to the new cultures seems rather unclear. And honestly, seeing this reaction:"Well thankfully for all of us you aren't in charge of how we spend our time!" being used really leaves a bad taste in my mouth, even if it was to that post. Click to expand...
<!-- artifact:quote:end -->
Your comment actually is in good faith unlike the initial user, hence why they get sass and you get genuine answer. You're not thinking about scale, reworking some code and script to enable gay marriage is infinitely less time than any of the reworks you proposed. They require new designs, overhauling UIs, new art, plenty of new code and content. Spreading over the course of likely weeks for any larger rework. Adding in a fairly highly requested modding feature that only needs two disciplines and in very focused areas? Much less time. And I'm gonna be incredibly blunt here, nobody is complaining we added scripted widgets as mod support. Or made a court scene editor that mods can use too. Or any of the other bits of mod support we added. Or about any other of the myriad of reworks and changes coming in 1.5 and Royal Court of which plenty enable incredibly ahistorical behaviour on top of the options already provided. But gay marriage gets singled out for complaints? Lets not pretend that is for any remotely genuine reason or concern in where we spend our time developing the game, because we all know it isn't.

## Reply 114 — participant_065 · 2022-01-26 · post-28037538

<!-- artifact:quote:start -->
> EarlKonrad said: I'm not sure what's worse, the audacity of a developer talking down to a player that expressed his opinion without being rude or the crowd cheering the Dev statement as if it was proper behavior. Click to expand...
<!-- artifact:quote:end -->
Implementing same sex marriage was a requested feature and there are many people further up in this thread happy it will be in the game options soon. That poster said "how dare you work on stuff I don't like, you should only be focusing on what's important to ME". You don't think this is rude behavior?

## Reply 115 — participant_034 · 2022-01-26 · post-28037540

<!-- artifact:quote:start -->
> AWDMANOUT said: Implementing same sex marriage was a requested feature and there are many people further up in this thread happy it will be in the game options soon. That poster said "how dare you work on stuff I don't like, you should only be focusing on what's important to ME". You don't think this is rude behavior? Click to expand...
<!-- artifact:quote:end -->
I can take or leave Gay marriage. But it's there for those who want it, and as a Game Rule, I believe, so those who don't want it don't have to have it. More freedom of choice is always better than less freedom of choice...

## Reply 116 — participant_063 · 2022-01-26 · post-28037565

<!-- artifact:quote:start -->
> blackninja9939 said: Your comment actually is in good faith unlike the initial user, hence why they get sass and you get genuine answer. You're not thinking about scale, reworking some code and script to enable gay marriage is infinitely less time than any of the reworks you proposed. They require new designs, overhauling UIs, new art, plenty of new code and content. Spreading over the course of likely weeks for any larger rework. Adding in a fairly highly requested modding feature that only needs two disciplines and in very focused areas? Much less time. And I'm gonna be incredibly blunt here, nobody is complaining we added scripted widgets as mod support. Or made a court scene editor that mods can use too. or any of the other bits of mod support we added. Or made any other of the myriad of reworks and changes coming in 1.5 and Royal Court of which plenty enable incredibly ahistorical behaviour on top of the options already provided. But gay marriage gets singled out for complaints? Lets not pretend that is for any remotely genuine reason or concern in where we spend our time developing the game, because we all know it isn't. Click to expand...
<!-- artifact:quote:end -->
Good to hear that. Wasn't exactly sure how much code would have needed to be changed for it to work, but it seemed to really not be comparable to the large reworks I thought about. Thanks for the clarification.

## Reply 117 — participant_017 · 2022-01-26 · post-28037872

<!-- artifact:quote:start -->
> blackninja9939 said: Your comment actually is in good faith unlike the initial user, hence why they get sass and you get genuine answer. You're not thinking about scale, reworking some code and script to enable gay marriage is infinitely less time than any of the reworks you proposed. They require new designs, overhauling UIs, new art, plenty of new code and content. Spreading over the course of likely weeks for any larger rework. Adding in a fairly highly requested modding feature that only needs two disciplines and in very focused areas? Much less time. And I'm gonna be incredibly blunt here, nobody is complaining we added scripted widgets as mod support. Or made a court scene editor that mods can use too. Or any of the other bits of mod support we added. Or about any other of the myriad of reworks and changes coming in 1.5 and Royal Court of which plenty enable incredibly ahistorical behaviour on top of the options already provided. But gay marriage gets singled out for complaints? Lets not pretend that is for any remotely genuine reason or concern in where we spend our time developing the game, because we all know it isn't. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> AWDMANOUT said: Implementing same sex marriage was a requested feature and there are many people further up in this thread happy it will be in the game options soon. That poster said "how dare you work on stuff I don't like, you should only be focusing on what's important to ME". You don't think this is rude behavior? Click to expand...
<!-- artifact:quote:end -->
When you were introducing same-sex concubinage in Azure, you made it very clear that same-sex marriage had to be delivered at a later date due to "larger technical risks" and overall resource-related infeasibility to release something of that scope in 1.3.X (and that remained the case even after Azure itself grew in scope and changed from patch 1.3.X to full 1.4). Now, maybe it's still smaller in scope than literally every single example that both @Draky and @chelvo talked about. Which, for the record, I find doubtful in and of itself because things like "make warfare less terrible" are rather vague and open-ended. And as such leave room for starting with smaller changes. Kinda why even small mods like those lowering replenishment rate were already met with positive response in the recent thread on the state of warfare. Either way, it still feels like you're downplaying the scope of this change compared to your previous statements on the issue. The third paragraph is where you jump the shark though. The comparison to court window is rather missed, because it's directly related to the DLC, so I'm not sure why it would be met with complaints. Even scripted widgets, which essentially add custom windows for custom systems in and expansion that adds new systems with their windows is still somewhat related. Yet when it comes to same-sex marriage, because you went with a game rule option instead of unlocking it with a cultural perk of the cultural rework, it doesn't really connect to this specific DLC in the same your other examples do. So yeah, not the best comparison Yet that part of your third paragraph is still monumentally better than its second half, because that's where your remark about good faith posting dives head first into the realm of irony. First of all, the bit about ahistorical nature of this particular modding tool is a misrepresentation of the post you found worthy of your sass, as it didn't mention anything of the sort. Secondly, the argument that no one is complaining about the non-modding changes to "any other of the myriad of reworks and changes" coming in 1.5 and the DLC makes no sense in the context of a dev diary related to modding. What, do you want people to post off-topic here? Given how that's against forum rules, that would be a rather weird thing for PDX employee to do. Thirdly, to cover all bases here, since you didn't actually limit your claim of how there's no criticism of other parts of 1.5 and Royal Court to this thread alone, it also warrants pointing out that people had most certainly been complaining about other aspects of 1.5 and Royal Court in their relevant Dev diaries. Even though, weirdly enough, none of the previous dev diaries had anything to do with same-sex anything. Hell, people complained about not being able to change aspects of a culture without using divergence or hybridisation so much you devs changed your mind about it. And on top of that we have a whole plethora of user-made threads critical about various aspects of the incoming update, starting with the court itself. Some are right on the first forum page right now. And before you project your questionable "everyone that questions our priorities on this is a bigot" at me as well, let me point out that I didn't question it myself. Because I have no problem with this change myself. Nor do I have a problem with gay people themselves, as you'd may like to insinuate. Instead I attended pride parades in support of their rights (in a country that doesn't really respect them) and while I'm not gay myself I fall on another part of the LGBTA spectrum. But hey, maybe questioning the devs in any capacity is also bigotry and I didn't know it. Except that's not what happened? At no point did they phrase their complaint in "how dare they" manner. And they literally ended their post with "but whatever floats their boat", which is attitude pretty much opposite to "you should only be focusing on what's important to ME". Maybe their behavior was rude anyway. But you having to completely twist what they said around makes a rather poor case for that argument.

## Reply 118 — participant_066 · 2022-01-26 · post-28037927

<!-- artifact:quote:start -->
> SauronGorthaur said: At no point did they phrase their complaint in "how dare they" manner. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Draky said: actual content [...] rather than modding in gay marriage Click to expand...
<!-- artifact:quote:end -->
I don't know how you usually carry yourself, but sounds pretty "how dare they" to me, pretending gay marriage isn't actual content, and belittling it further by calling the development process "modding [it] in". That's disrespectful to both those who want such a feature, and the devs. You might have other priorities when it comes to the direction the game should take; there are many aspects where CK3 could (or maybe should) be improved, expanded or even revamped; the reaction you get depends on how you say it.

## Reply 119 — participant_017 · 2022-01-27 · post-28037949

<!-- artifact:quote:start -->
> Nawjak said: I don't know how you usually carry yourself, but sounds pretty "how dare they" to me, pretending gay marriage isn't actual content, and belittling it further by calling the development process "modding [it] in". That's disrespectful to both those who want such a feature, and the devs. You might have other priorities when it comes to the direction the game should take; there are many aspects where CK3 could (or maybe should) be improved, expanded or even revamped; the reaction you get depends on how you say it. Click to expand...
<!-- artifact:quote:end -->
Being dismissive of a feature you don't like is not equal to accusing the devs of "daring" to introduce it to me, no. It's just a rather weak way to phrase an argument about different priorities (which was the whole gist of the post at hand), which is a different thing. And, for the record, that itself could be construed as rude behavior, as it could be argued such argumentation is reductive and intellectually dishonest. Like I said, I'm not ruling out the possibility of that post being rude (and rude or not, I agree with your overall premise that it could have been worded better), but the other reply I quoted is still a misrepresentation in my eyes. But all of this is getting kinda off-topic. Personally I'd still like to know if we'll be able to have culture group (heritage) wide opinion modifiers on traits etc. like we could in CK2 instead of just culture-wide ones. Because the work-around for that is rather annoying.

## Reply 120 — participant_042 · 2022-01-27 · post-28038109

<!-- artifact:quote:start -->
> SauronGorthaur said: The third paragraph is where you jump the shark though. The comparison to court window is rather missed, because it's directly related to the DLC, so I'm not sure why it would be met with complaints. Even scripted widgets, which essentially add custom windows for custom systems in and expansion that adds new systems with their windows is still somewhat related. Yet when it comes to same-sex marriage, because you went with a game rule option instead of unlocking it with a cultural perk of the cultural rework, it doesn't really connect to this specific DLC in the same your other examples do. So yeah, not the best comparison Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: Yet that part of your third paragraph is still monumentally better than its second half, because that's where your remark about good faith posting dives head first into the realm of irony. First of all, the bit about ahistorical nature of this particular modding tool is a misrepresentation of the post you found worthy of your sass, as it didn't mention anything of the sort. Secondly, the argument that no one is complaining about the non-modding changes to "any other of the myriad of reworks and changes" coming in 1.5 and the DLC makes no sense in the context of a dev diary related to modding. What, do you want people to post off-topic here? Given how that's against forum rules, that would be a rather weird thing for PDX employee to do. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: Thirdly, to cover all bases here, since you didn't actually limit your claim of how there's no criticism of other parts of 1.5 and Royal Court to this thread alone, it also warrants pointing out that people had most certainly been complaining about other aspects of 1.5 and Royal Court in their relevant Dev diaries. Even though, weirdly enough, none of the previous dev diaries had anything to do with same-sex anything. Hell, people complained about not being able to change aspects of a culture without using divergence or hybridisation so much you devs changed your mind about it. And on top of that we have a whole plethora of user-made threads critical about various aspects of the incoming update, starting with the court itself. Some are right on the first forum page right now. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: And before you project your questionable "everyone that questions our priorities on this is a bigot" at me as well, let me point out that I didn't question it myself. Because I have no problem with this change myself. Nor do I have a problem with gay people themselves, as you'd may like to insinuate. Instead I attended pride parades in support of their rights (in a country that doesn't really respect them) and while I'm not gay myself I fall on another part of the LGBTA spectrum. Click to expand...
<!-- artifact:quote:end -->
So, I'll try my best to explain the context (or at least my understanding of it) behind his post. Out of the modding changes explained in the first post it seems only the royal court scene editor and position is "DLC-only", so I don't see how his comparisons were "not the best" as you say. We have scripted UI widgets and tooltip functionality, improvements to the debug mode, at least 12 console commands, and better error logging. Some of these could even have been left hardcoded for Paradox developing softwares but was added as an improvement to all modders. I'm willing to guess all of these took some development time, yet curiously, there are no complaints about any of these. Even more so considering not everyone uses mods, and not everyone that uses mods will use a mod that will be affected by these, so these changes may only affect a small amount of players. All of these seem to be able to be used by modders for anything, not just things related to royal court. And this being added as a main rule is not relevant to the context of his post because this negativity about same-sex marriage always happened even when it was only going to be a change for modders. This is not the first time that same-sex marriage is the only thing picked on for the "time and resources argument" after a list of several changes. Check Dev Diary #55 for the mere mention of it already getting negative reactions (and no other changes mentioned there did so). You can also see the historicity arguments BlackNinja also mentioned on his post (which was not used much on this current thread, but I guess he wanted to take the opportunity to debunk those as well). Or, if you want even more of this just go to the "Legalize Gay Modding" thread in the User Mods section, that one is quite long and it got a lot of negativity even before Paradox participated. There is no need for "off-topicness" here; there are other things in this dev diary that took time to develop and are not relevant for everyone, yet only one of them is singled out. Let's take a look at Dev Diary #21 about Faith Reformation. The Carnal Exaltation and Ritual Cannibalism tenets are visible in screenshots, yet there are no dislikes. The only concerns are about the prevalence of reformation (and just by Roxas15 on page 6 and Larque on page 15, historical concerns), but nobody asked (neither did Roxas15 or Larque) these tenets not to be included in the game or complained about the development time of adding them in. Ironically when user MetalGearDaner asked in page 12 if same-sex marriage was possible, another user replied right after that it would ahistorical, and a larger discussion started about it in page 13. So that was an example of pre-release dev diary about ahistorical content and almost no complaints, why? Why when same-sex marriage is mentioned then these arguments appear? Why were people then not concerned about the development time? Why are people ignoring the other ahistorical content possible in the game? (With or without DLC) What does this even have to do with anything? The context of his post is not that people "only complain about same-sex marriage", it's that people keep complaining about it with double standards. Even then, have the features you mentioned been complained about their development time or historicity? A DLC that is taking almost 8 months to finish since announcement and that allows you to create a Mongol-African or Indian-Icelandic culture? In your examples the complaints are about implementation rather than on these two grounds. This is not relevant but just a quick heads up, LGBT+ groups can be bigoted towards other groups of the LGBT+ community, lesbian TERFs are an example. Anyway, when the same arguments keep being used, even after debunked, and these same arguments are not applied to other aspects of the game or its development process it can lead one to think the issues the posters have lie elsewhere.

## Reply 121 — participant_046 · 2022-01-27 · post-28038112

<!-- artifact:quote:start -->
> SauronGorthaur said: Now, maybe it's still smaller in scope than literally every single example that both @Draky and @chelvo talked about. Which, for the record, I find doubtful in and of itself because things like "make warfare less terrible" are rather vague and open-ended. And as such leave room for starting with smaller changes. Kinda why even small mods like those lowering replenishment rate were already met with positive response in the recent thread on the state of warfare. Either way, it still feels like you're downplaying the scope of this change compared to your previous statements on the issue. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: The third paragraph is where you jump the shark though. The comparison to court window is rather missed, because it's directly related to the DLC, so I'm not sure why it would be met with complaints. Even scripted widgets, which essentially add custom windows for custom systems in and expansion that adds new systems with their windows is still somewhat related. Yet when it comes to same-sex marriage, because you went with a game rule option instead of unlocking it with a cultural perk of the cultural rework, it doesn't really connect to this specific DLC in the same your other examples do. So yeah, not the best comparison Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: Thirdly, to cover all bases here, since you didn't actually limit your claim of how there's no criticism of other parts of 1.5 and Royal Court to this thread alone, it also warrants pointing out that people had most certainly been complaining about other aspects of 1.5 and Royal Court in their relevant Dev diaries. Even though, weirdly enough, none of the previous dev diaries had anything to do with same-sex anything. Hell, people complained about not being able to change aspects of a culture without using divergence or hybridisation so much you devs changed your mind about it. And on top of that we have a whole plethora of user-made threads critical about various aspects of the incoming update, starting with the court itself. Some are right on the first forum page right now. Click to expand...
<!-- artifact:quote:end -->
For the replenishment rate, keep in mind there is also the problem of finding a value that is generally liked and not having to redo it when other things are updated. So a mod can just put in a value the modder likes, and then people who agree can download the mod, and people who don't have to download the mod. But Paradox has to find a value that works for everyone, which is a lot more work at it requires multiple different people test multiple different values (while I personally would like to see replenishment rates lowered, I do know there are some who don't, or only slightly lowered, as they see it as a mechanic that just forces needless weighting). Now I'm sure someone will mention game rules, so let me just head that off. If they add a game rule they still need to find something at works for most people, to set as the default, and then need to figure out what and how many options there are for the game rule. So in someways game rules creates more work, at least when there aren't obvious choices for what the game rule options would be. The other is that they do all this work to change the replenishment rate, but they still haven't overhauled the war system. But when they overhaul the war system later, as is being requested here, they would probably need to go back a figure out the optimal replenishment rates for the new war system. Meaning they would have to do the same thing twice. This is why the devs often like to cover interconnect systems as a whole, because it reduces the amount of redundant work. And as I haven't heard any major calls for overhauling the marriage system, this doesn't really apply to gay marriage (as any changes to the marriage system are likely to be minor or are very far off). So if complaining about the devs not focusing on "actual content for the game", the new mod tools probably make more fitting targets as they require you to download something and aren't available in the vanilla game, unlike gay marriage which can now be accessed without mods. Also the lack of connection to culture isn't true. The game rules for gay marriage does actually mention culture "...and whose cultures practice concubinage". So just because you don't see how things might be connected, doesn't mean they aren't there. Also more importantly, gay marriage is probably a system that for the most part is pretty isolated. Such systems are easy to do even if not connect to the main theme of the update. Another thing that fall into this category is many types of bug fixes. You don't see people complaining about the devs wasting time fixing a bug because it doesn't match the theme of the update. So the problem is for the war improvements people want to see is that they are very interconnected and so due to the redundancy problem mentioned earlier they are best tackled as a whole. I feel this is taking things out of context. This in the context of this dev diary and specifically the devs wasting their time. So for instance your mention of complaints about not liking the implementation of certain things, like how there was no way to change certain aspects of culture without hybridization or divergence which isn't a complaint about he devs wasting their time, thus don't apply. Also personally, I find how people complain about the devs wasting their time on certain features interesting. For example with complaint about how the royal court itself, the person making the complain generally feels the need to give the reasoning behind that complaint. But with gay marriage the reasoning for why it is a waste of time is usually left off. Now I'm not saying everyone complaining about the addition of gay marriage being a waste of time is bigot, and I don't think blackninja9939 was either. But I do agree with their statement that it is more likely to get singled out as a waste of time whenever the topic comes up (and this isn't the first time the topic of gay marriage has come up on these forums among other features and for some reason it draws the most ire). And the reason for that is that bigots inflate the number of claimants about gay marriage being a waste of time and make it the topic of conversation for those who have non-bigoted reasons to complain. edit: clarity

## Reply 122 — participant_067 · 2022-01-27 · post-28038344

<!-- artifact:quote:start -->
> JonathanViking said: I wounder If its possibly for modders to make tribal Courts and tiny Courts for counts and dutchys Click to expand...
<!-- artifact:quote:end -->
Wait Tribal Kings don't get courts?

## Reply 123 — participant_068 · 2022-01-27 · post-28038793

Excellent there will be the addition of checking the triggers for events. As far as gay modding, I am not going to be political correct and rest assured I am not a biggot at all but even then, given the scope of the game, it is mostly a waste of resources better spent coding other event types that provide content for the different mechanics in the game - for instance have x good situational events that address dread, prestige, renown, piety, stress, more dilemmas in management of the realm, etc. In the same cathegory, the same goes with cannibalism, btw. Another waste of resources. Hopefully there will be no Sunset Invasion anytime soon... As far as the actual 3D depiction of the Royal Court goes, I feel it is yet another big waste of resources. Hopefully the whole 1.5 patch in its entirety will bring more meaningful changes to the gameplay. To end in a positive note, I'd say I am fired up for the culture changes. And now getting ready for the downvotes!

## Reply 124 — participant_069 · 2022-01-27 · post-28038903

<!-- artifact:quote:start -->
> blackninja9939 said: Your comment actually is in good faith unlike the initial user, hence why they get sass and you get genuine answer. You're not thinking about scale, reworking some code and script to enable gay marriage is infinitely less time than any of the reworks you proposed. They require new designs, overhauling UIs, new art, plenty of new code and content. Spreading over the course of likely weeks for any larger rework. Adding in a fairly highly requested modding feature that only needs two disciplines and in very focused areas? Much less time. And I'm gonna be incredibly blunt here, nobody is complaining we added scripted widgets as mod support. Or made a court scene editor that mods can use too. Or any of the other bits of mod support we added. Or about any other of the myriad of reworks and changes coming in 1.5 and Royal Court of which plenty enable incredibly ahistorical behaviour on top of the options already provided. But gay marriage gets singled out for complaints? Lets not pretend that is for any remotely genuine reason or concern in where we spend our time developing the game, because we all know it isn't. Click to expand...
<!-- artifact:quote:end -->
Thank you for your support, and for standing up for your LGBT fans and colleagues! <3

## Reply 125 — participant_014 · 2022-01-27 · post-28039174

EDIT: This can be deleted I found the answer on page 3 with the picture of the game rule.

## Reply 126 — participant_070 · 2022-01-27 · post-28039190

Speaking of gay stuff and choice... Is there a chance Harald Fairhair will not be gay in the next patch? Like, I get it, some players want to rewrite history in this game, but some may prefer to stick to more historical scenarios. I would like to let Harald's sons to become a problem for my kingdom, but him being gay makes it hard to have so many children.

## Reply 127 — participant_014 · 2022-01-27 · post-28039202

It's clear the vast majority of the fanbase is in favor of the homosexual rule addition but I still find the bad faith arguments against it frustrating. I would consider myself mostly anti-woke and think most identity politics are cancerous. But there are absolutely no good reasons that the devs should ignore a highly requested and easily provided feature that expands roleplaying options for all players. I've been critical of snippy devs before but in this event they have every reasons to be.

## Reply 128 — participant_002 · 2022-01-27 · post-28039209

<!-- artifact:quote:start -->
> Dewiles said: Speaking of gay stuff and choice... Is there a chance Harald Fairhair will not be gay in the next patch? Like, I get it, some players want to rewrite history in this game, but some may prefer to stick to more historical scenarios. I would like to let Harald's sons to become a problem for my kingdom, but him being gay makes it hard to have so many children. Click to expand...
<!-- artifact:quote:end -->
The last character I played was gay, his wife was a lesbian and they had 4 sons, probably missing something else if you really have a hard time having kids with a gay character. Maybe take the seduction perk that boosts fertility ? It's the first one on the tree.

## Reply 129 — participant_042 · 2022-01-27 · post-28039241

<!-- artifact:quote:start -->
> Torredebelem said: Excellent there will be the addition of checking the triggers for events. As far as gay modding, I am not going to be political correct and rest assured I am not a biggot at all but even then, given the scope of the game, it is mostly a waste of resources better spent coding other event types that provide content for the different mechanics in the game - for instance have x good situational events that address dread, prestige, renown, piety, stress, more dilemmas in management of the realm, etc. In the same cathegory, the same goes with cannibalism, btw. Another waste of resources. Hopefully there will be no Sunset Invasion anytime soon... As far as the actual 3D depiction of the Royal Court goes, I feel it is yet another big waste of resources. Hopefully the whole 1.5 patch in its entirety will bring more meaningful changes to the gameplay. To end in a positive note, I'd say I am fired up for the culture changes. And now getting ready for the downvotes! Click to expand...
<!-- artifact:quote:end -->
As long as you're consistent and don't have double standards I think it seems fine. However, I get the impression (since you didn't explain why you think it's a waste) that you consider either things you're not interested in or at the very least ahistorical things (which RC isn't, and I'm pretty sure Paradox would never disallow ahistorical features or possibilities using these features) a waste of development resources. I at least don't see it that way; I don't consider stuff I'm not interested in as a waste of development resources because I don't just think of stuff I want — I know other players would be happy having those features even if it's something that doesn't make a difference to me. For example I never played multiplayer and never will but I don't mind when multiplayer gets worked on. Not related to your post but I also realized that I don't think anyone ever said another feature was a waste of development resources and asked same-sex marriage to be implemented instead of it, so it's also something to think about.

## Reply 130 — participant_061 · 2022-01-27 · post-28039395

I think the question of whether or not something is considered a "waste of resources" is less a matter of "what I want" or "what I don't like" and more a matter of what will actually improve the game... at least for most people here. Yes, there will be some complaining because they don't like gays. Yes, there will be some complaining because they don't like feature X. But when it really comes down to it, most complaining aren't really complaining for those reasons, but instead because these changes really don't improve the game in a meaningful way. Yes, people who want gay marriage will consider it an improvement. And it is an improvement for them. However, will adding it draw in more players? Will it get more people playing the game again who have stopped playing? I'd say any increase in numbers due to that change will be minimal. On the other hand, features and changes that people list as reasons why they stopped playing the game or consider the game to be "shallow" will have a far greater impact on those very important numbers. The dev did point out that dev time for some of the important changes and features like improving AI warfare are far more time consuming to do and I get that. Many of these features and changes that will have a high impact on bringing players back to the game are going to take a lot of time and effort. However, one of the things that reviews of RC have brought up already are that the events aren't great and are repetitive (meaning not enough of them). Adding new events or reworking existing events to better use characters who make sense or to use characters that are meaningful to the player is really not that difficult or time consuming except if you talk about adding a lot of them as more = more time. That alone would have more impact on more players than gay marriage, which being as it is a rule will end up being used by a limited (though not necessarily small) number of players. Other changes can also be made in stages, allowing you to make a change that will improve, for example, AI warfare somewhat without having to take the time to completely rework it. There are certainly ways to take things that are keeping people from enjoying the game and adding them in without needing a significant amount of dev time to do so if they wanted to do it. And as was pointed out, the devs specifically said adding in gay marriage would be a challenge as it impacts a lot of parts of the game and would need a lot of testing and work to get it working properly. So the suggestion that it isn't a big deal to add by the dev is a bit inconsistent and probably not very accurate. Personally, I think any feature (even highly requested ones) that does not actually improve gameplay value of the game should be held off until a later time while they work on getting the game up to a level where players don't get tired of it so quickly. And to be clear, just because gay marriage is a gameplay item doesn't mean it actually improves gameplay value. If that isn't in the game, will it prevent a player from enjoying the game? No. They may prefer it to be there, but if it's not there, they will either enjoy or not enjoy the game the same as if it was there because it really doesn't affect anything in gameplay unless they find it fun to try and convert the entire map to be gay or something. Otherwise it's just a "novelty" (and I am not meaning to use that in any rude way, but just as a definition of something that has little meaningful impact to the game). This is true for any similar feature that may be added. Compare this to adding in something (yes, this is a big feature) like regency in a way that's improved over CK2's regency mechanic, which would actually improve an aspect of gameplay and that's honestly a pretty minor issue in the game overall. Look at it this way, if you added gay marriage to the game separate from anything else so that you aren't impacting the results by other features, you might draw in some players who had stopped playing the game who want the feature, but they'll play a game or two and remember that the game itself gets old quickly because it's missing so much content that they'll put it down again because gay marriage doesn't actually fix any of the real issues in the game. As a side note, I also think RC would have been far better off to be added at a later date as well. I like RC and it has some really interesting aspects to it (I even like the court even if many do not). But I really don't think anything other than cultures will bring people back to the game and it's yet to be seen how well they managed to get the cultures working. I think another DLC might have been better at this stage than RC... something that would add a significant boost to the gameplay value of the game.

## Reply 131 — participant_052 · 2022-01-27 · post-28039456

I have played a lot of fantasy mods for CK2 and all had the problem that when you introduce different races which were infertile to each other you could not tell the AI that and it often married infertile partners resulting in the extinction of their family line and even dynasty. Granted, gay marriage will likely happen less often (hopefully), but I am still wary about the AI ruining their dynasty through infertile marriages.

## Reply 132 — participant_017 · 2022-01-27 · post-28039553

<!-- artifact:quote:start -->
> GoldenSilver said: So, I'll try my best to explain the context (or at least my understanding of it) behind his post. Out of the modding changes explained in the first post it seems only the royal court scene editor and position is "DLC-only", so I don't see how his comparisons were "not the best" as you say. We have scripted UI widgets and tooltip functionality, improvements to the debug mode, at least 12 console commands, and better error logging. Some of these could even have been left hardcoded for Paradox developing softwares but was added as an improvement to all modders. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> GoldenSilver said: This is not the first time that same-sex marriage is the only thing picked on for the "time and resources argument" after a list of several changes. Check Dev Diary #55 for the mere mention of it already getting negative reactions (and no other changes mentioned there did so). You can also see the historicity arguments BlackNinja also mentioned on his post (which was not used much on this current thread, but I guess he wanted to take the opportunity to debunk those as well). Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> GoldenSilver said: There is no need for "off-topicness" here; there are other things in this dev diary that took time to develop and are not relevant for everyone, yet only one of them is singled out. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> GoldenSilver said: Let's take a look at Dev Diary #21 about Faith Reformation. The Carnal Exaltation and Ritual Cannibalism tenets are visible in screenshots, yet there are no dislikes. The only concerns are about the prevalence of reformation (and just by Roxas15 on page 6 and Larque on page 15, historical concerns), but nobody asked (neither did Roxas15 or Larque) these tenets not to be included in the game or complained about the development time of adding them in. Ironically when user MetalGearDaner asked in page 12 if same-sex marriage was possible, another user replied right after that it would ahistorical, and a larger discussion started about it in page 13. So that was an example of pre-release dev diary about ahistorical content and almost no complaints, why? Why when same-sex marriage is mentioned then these arguments appear? Why were people then not concerned about the development time? Why are people ignoring the other ahistorical content possible in the game? (With or without DLC) Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> GoldenSilver said: What does this even have to do with anything? The context of his post is not that people "only complain about same-sex marriage", it's that people keep complaining about it with double standards. Even then, have the features you mentioned been complained about their development time or historicity? A DLC that is taking almost 8 months to finish since announcement and that allows you to create a Mongol-African or Indian-Icelandic culture? In your examples the complaints are about implementation rather than on these two grounds. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> GoldenSilver said: This is not relevant but just a quick heads up, LGBT+ groups can be bigoted towards other groups of the LGBT+ community, lesbian TERFs are an example. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pengoyo said: For the replenishment rate, keep in mind there is also the problem of finding a value that is generally liked and not having to redo it when other things are updated. So a mod can just put in a value the modder likes, and then people who agree can download the mod, and people who don't have to download the mod. But Paradox has to find a value that works for everyone, which is a lot more work at it requires multiple different people test multiple different values (while I personally would like to see replenishment rates lowered, I do know there are some who don't, or only slightly lowered, as they see it as a mechanic that just forces needless weighting). Now I'm sure someone will mention game rules, so let me just head that off. If they add a game rule they still need to find something at works for most people, to set as the default, and then need to figure out what and how many options there are for the game rule. So in someways game rules creates more work, at least when there aren't obvious choices for what the game rule options would be. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pengoyo said: The other is that they do all this work to change the replenishment rate, but they still haven't overhauled the war system. But when they overhaul the war system later, as is being requested here, they would probably need to go back a figure out the optimal replenishment rates for the new war system. Meaning they would have to do the same thing twice. This is why the devs often like to cover interconnect systems as a whole, because it reduces the amount of redundant work. And as I haven't heard any major calls for overhauling the marriage system, this doesn't really apply to gay marriage (as any changes to the marriage system are likely to be minor or are very far off). Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pengoyo said: Also more importantly, gay marriage is probably a system that for the most part is pretty isolated. Such systems are easy to do even if not connect to the main theme of the update. Another thing that fall into this category is many types of bug fixes. You don't see people complaining about the devs wasting time fixing a bug because it doesn't match the theme of the update. So the problem is for the war improvements people want to see is that they are very interconnected and so due to the redundancy problem mentioned earlier they are best tackled as a whole. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pengoyo said: I feel this is taking things out of context. This in the context of this dev diary Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pengoyo said: So for instance your mention of complaints about not liking the implementation of certain things, like how there was no way to change certain aspects of culture without hybridization or divergence which isn't a complaint about he devs wasting their time, thus don't apply. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pengoyo said: Also personally, I find how people complain about the devs wasting their time on certain features interesting. For example with complaint about how the royal court itself, the person making the complain generally feels the need to give the reasoning behind that complaint. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pengoyo said: But with gay marriage the reasoning for why it is a waste of time is usually left off. Now I'm not saying everyone complaining about the addition of gay marriage being a waste of time is bigot, and I don't think blackninja9939 was either. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pengoyo said: But I do agree with their statement that it is more likely to get singled out as a waste of time whenever the topic comes up (and this isn't the first time the topic of gay marriage has come up on these forums among other features and for some reason it draws the most ire). And the reason for that is that bigots inflate the number of claimants about gay marriage being a waste of time and make it the topic of conversation for those who have non-bigoted reasons to complain. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Anschau said: Wait Tribal Kings don't get courts? Click to expand...
<!-- artifact:quote:end -->
And out of everything you listed the specific comparisons blackninja actually used were the royal court scene that you yourself just admitted is directly related to the DLC and the widgets, which as I argued is at least tangentially related to the type of UI mechanics already used in the DLC. I already mentioned the Azure patch dev diary myself so there's no need for you to act as if I were somehow unaware of it. I outright quoted the relevant part of their post in the text of my paragraph you're replying here and it explicitly brought up lack of complaints about changes brought in the upcoming DLC going beyond the scope of this thread. So you should direct the remark about there being no need for off-topicness at them. If you think people are ignoring not only other ahistorical content but these specific examples just because they weren't complained about in a pre-release dev diary, you're not really paying much attention to the forums. Things like incest, nudity or cannibalism are common targets of criticism about CK3 being ahistorical or "pandering to memers", while what people arguing that consider more important content is being ignored. Also, quoting pre-release dev diary is just apples to oranges comparison here in the first place. For two reasons. First, people were much more optimistic then and willing to give Paradox the benefit of the doubt. Now with Royal Court development having a crawling pace and other issues, the overall attitude on the forum turned more sour from what I've observed. Secondly, during the development of the base game things were still up in the air one way or another. But came release, (lack of) gay marriage was something that was already hard-coded into the game, which then had to be undone to make it work. Which by Paradox's own admission, required enough work to do that it couldn't even been done in a major patch like 1.4. Not exactly the case with cannibals, is it now? Yeah, no, you made that "context" up. Such remark is nowhere to be found in either blackninja's comment (which simply talks about gay marriage being singled out for complaints, period) nor the post they were replying to. Instead that post literally called the complaint at hand "an important point", that's simply worded in an "uncouth" manner. And the other half of this tangent of yours is just a false. I've seen people call the whole culture rework as something that doesn't give enough gameplay for how large it is, as in their eyes you'll only interact with it just a few times during a campaign and then forget about (and I've seen that complaint numerous times). While calling culture-changing parts of it in particular more "meme content". Which kinda falls squarely under the umbrella of wasted development time and ahistorical content. And the court itself has not only been called a waste of development time, it's been outright accused of being the culprit behind the very 8 month development time you brought up. There's no needs for a heads up for something obvious. There is a reason why I brought up that bit last. Which is simply an issue of testing and not the kind of the more intensive work described in blackninja's post. And changing a hard-coded element also requires plenty of testing, albeit more of the QA variety. As for doing it via game rules, I don't see why Paradox shouldn't just keep the current one as the default if they went with this route to tackle this subject. They picked the current rate in the first place for a reason. And I'd wager the casual players are at this point a majority so the default would be aimed at them, while the minority asking for harder warfare wouldn't be overwhelmed with rules. As I already pointed out, what was actually being requested in the post blackninja replied to there was simply to make "warfare not terrible". Which is extremely vague and open to interpretation, because of how completely subjective it is. Which is precisely why such a demand could be technically fulfilled with even a small change like my example. Which, admittedly, is one of the plethora of reasons why there is little value in "X is terrible" as a criticism. Not how Paradox itself made it look like during Azure's development. And bug fixes are standard part of any version release and fixing bugs is pretty much expected of software developers, because customers are paying for software that works properly. So it's probably the worst comparison you could have made. Especially in context of Paradox, especially-ier in context of CK3 team in particular, which hadn't released even a minor bug patch in seven months. As such major patches are the only time left for them to release bug fixes. Like I said, I was just being thorough. If what you're saying is the case, things only revert to my previous point about how an argument about lack of complaints about non-modding parts of the upcoming update in a thread dedicated to the modding changes makes no sense. Because it relies on portarying people not posting off-topic as somehow something wrong. Which is not only a rather fallacious argument, but it'd require people to outright break forum rules. Which would be a weird sentiment coming from an employee of Paradox. That one specific aspect of the culture overhaul? Sure. Other aspects of it, including the new system as a whole? I've seen criticism of them that essentially amounts to there being too much time spent on those compared to how much culture matters in game. And technically, there actually was a poster talking about devs wasting time in the dev diary about the change of direction in regards to changing existing cultures. It's just they portrayed the dev diary itself as a waste of time. And yet there's a post complaining about the court (or at least it's art aspect) being a waste of time without giving a reason as to why just two posts below your comment. Rather ironic coincidence. No, it's pretty much exactly what they said. Their claim was that gay marriage gets singled out for complaints about how dev time is allocated and that it's not for any genuine reason. Which, even putting aside how the claim about it being singled out is disproved even by the next DLC's very namesake, is pretty explicit. You can try to soften it with how it was about only posters who give no reasons as to why this is a waste of time while they give reasons in other cases or even how it was about only comments made by German albinos, during a blood moon, while the Wild Hunt was running through the sky, but that's not actually there in blackninja's post. The phrase "more likely" is also nowhere to be seen in their comment. If that was their actual claim, I wouldn't have objected to it, even if you can see more of bad faith criticism in the dev diary about same sex concubinage than this one (though to be fair, a handful of posts here had been removed and the one I did notice before it was gone was rather bad). Not by the base game rules, no.

## Reply 133 — participant_071 · 2022-01-27 · post-28039570

<!-- artifact:quote:start -->
> Ixal said: Granted, gay marriage will likely happen less often (hopefully), but I am still wary about the AI ruining their dynasty through infertile marriages. Click to expand...
<!-- artifact:quote:end -->
I think it's safe to even with the option turned on, het AI characters (the default majority) are never going to marry a same-sex partner, ace AI characters almost never, and bi AI characters pretty rarely. So it seems likely to only be a meaningful problem if the player goes out of their way to choose settings that make it a problem.

## Reply 134 — participant_068 · 2022-01-27 · post-28039574

<!-- artifact:quote:start -->
> GoldenSilver said: As long as you're consistent and don't have double standards I think it seems fine. However, I get the impression (since you didn't explain why you think it's a waste) that you consider either things you're not interested in or at the very least ahistorical things (which RC isn't, and I'm pretty sure Paradox would never disallow ahistorical features or possibilities using these features) a waste of development resources. I at least don't see it that way; I don't consider stuff I'm not interested in as a waste of development resources because I don't just think of stuff I want — I know other players would be happy having those features even if it's something that doesn't make a difference to me. For example I never played multiplayer and never will but I don't mind when multiplayer gets worked on. Not related to your post but I also realized that I don't think anyone ever said another feature was a waste of development resources and asked same-sex marriage to be implemented instead of it, so it's also something to think about. Click to expand...
<!-- artifact:quote:end -->
The basis of the game is historical in nature and all that happens there should strive to conform to the social, ethical, anthropological and scientifical of the past ages it represents. Heavily developing the gay angle of the gameplay or having cannibalism as a trait plus all the accompanying implementarions only steals resources from developing a better simulation of the ancient times whose lifes are depicted in the game. This being said, I am happy we are finally finished with the "legalize gay modding" meme, more happy even that it is optional (unfortunately contrary to cannibalism) and hopefully looking forward to have more substantial content than these gameplay tangents in the future.

## Reply 135 — participant_070 · 2022-01-27 · post-28039601

<!-- artifact:quote:start -->
> Riamus said: I think the question of whether or not something is considered a "waste of resources" is less a matter of "what I want" or "what I don't like" and more a matter of what will actually improve the game... at least for most people here. Yes, there will be some complaining because they don't like gays. Yes, there will be some complaining because they don't like feature X. But when it really comes down to it, most complaining aren't really complaining for those reasons, but instead because these changes really don't improve the game in a meaningful way. Yes, people who want gay marriage will consider it an improvement. And it is an improvement for them. However, will adding it draw in more players? Will it get more people playing the game again who have stopped playing? I'd say any increase in numbers due to that change will be minimal. On the other hand, features and changes that people list as reasons why they stopped playing the game or consider the game to be "shallow" will have a far greater impact on those very important numbers. The dev did point out that dev time for some of the important changes and features like improving AI warfare are far more time consuming to do and I get that. Many of these features and changes that will have a high impact on bringing players back to the game are going to take a lot of time and effort. However, one of the things that reviews of RC have brought up already are that the events aren't great and are repetitive (meaning not enough of them). Adding new events or reworking existing events to better use characters who make sense or to use characters that are meaningful to the player is really not that difficult or time consuming except if you talk about adding a lot of them as more = more time. That alone would have more impact on more players than gay marriage, which being as it is a rule will end up being used by a limited (though not necessarily small) number of players. Other changes can also be made in stages, allowing you to make a change that will improve, for example, AI warfare somewhat without having to take the time to completely rework it. There are certainly ways to take things that are keeping people from enjoying the game and adding them in without needing a significant amount of dev time to do so if they wanted to do it. And as was pointed out, the devs specifically said adding in gay marriage would be a challenge as it impacts a lot of parts of the game and would need a lot of testing and work to get it working properly. So the suggestion that it isn't a big deal to add by the dev is a bit inconsistent and probably not very accurate. Personally, I think any feature (even highly requested ones) that does not actually improve gameplay value of the game should be held off until a later time while they work on getting the game up to a level where players don't get tired of it so quickly. And to be clear, just because gay marriage is a gameplay item doesn't mean it actually improves gameplay value. If that isn't in the game, will it prevent a player from enjoying the game? No. They may prefer it to be there, but if it's not there, they will either enjoy or not enjoy the game the same as if it was there because it really doesn't affect anything in gameplay unless they find it fun to try and convert the entire map to be gay or something. Otherwise it's just a "novelty" (and I am not meaning to use that in any rude way, but just as a definition of something that has little meaningful impact to the game). This is true for any similar feature that may be added. Compare this to adding in something (yes, this is a big feature) like regency in a way that's improved over CK2's regency mechanic, which would actually improve an aspect of gameplay and that's honestly a pretty minor issue in the game overall. Look at it this way, if you added gay marriage to the game separate from anything else so that you aren't impacting the results by other features, you might draw in some players who had stopped playing the game who want the feature, but they'll play a game or two and remember that the game itself gets old quickly because it's missing so much content that they'll put it down again because gay marriage doesn't actually fix any of the real issues in the game. As a side note, I also think RC would have been far better off to be added at a later date as well. I like RC and it has some really interesting aspects to it (I even like the court even if many do not). But I really don't think anything other than cultures will bring people back to the game and it's yet to be seen how well they managed to get the cultures working. I think another DLC might have been better at this stage than RC... something that would add a significant boost to the gameplay value of the game. Click to expand...
<!-- artifact:quote:end -->
I'd say that frustration comes from a fact that there was no new content for quite a while. Many perceive that in a negative way clearly because devs used this time to make a feature just for a certain part of community. And at this moment, when the game has very little to offer to core CK fans, devs decision to add some social justice only emphasizes old problems with the game. So yeah, I agree, a minor DLC would work for community better than this.

## Reply 136 — participant_017 · 2022-01-27 · post-28039611

<!-- artifact:quote:start -->
> Bobwoodword said: EDIT: This can be deleted I found the answer on page 3 with the picture of the game rule. Click to expand...
<!-- artifact:quote:end -->
Just a heads up but you can delete your own posts. It's in the three dots menu next to the report button.

## Reply 137 — participant_044 · 2022-01-27 · post-28039633

<!-- artifact:quote:start -->
> LeSingeAffame said: Are you talking about that? https://forum.paradoxplaza.com/foru...-diary-71-a-coat-of-arms-of-your-own.1489219/ Click to expand...
<!-- artifact:quote:end -->
No I was talking about being able to use this mod and still get achievements.

## Reply 138 — participant_042 · 2022-01-27 · post-28039694

<!-- artifact:quote:start -->
> Torredebelem said: The basis of the game is historical in nature and all that happens there should strive to conform to the social, ethical, anthropological and scientifical of the past ages it represents. Heavily developing the gay angle of the gameplay or having cannibalism as a trait plus all the accompanying implementarions only steals resources from developing a better simulation of the ancient times whose lifes are depicted in the game. This being said, I am happy we are finally finished with the "legalize gay modding" meme, more happy even that it is optional (unfortunately contrary to cannibalism) and hopefully looking forward to have more substantial content than these gameplay tangents in the future. Click to expand...
<!-- artifact:quote:end -->
As much as you have the right to think this is what the game is supposed to be and wish for it to go on that direction, what the game actually is will be defined by Paradox's vision for the product. I'm not Paradox but it's very obvious that CK series was never meant to be a 100% strict realistic medieval simulation. CK3 isn't, CK2 certainly wasn't (immortality, aztecs, demon cults etc), and I don't think CK4 will be. My advice is to either change your expectations or look for another game that actually is what you envision otherwise you may be forever disappointed.

## Reply 139 — participant_005 · 2022-01-27 · post-28039763

<!-- artifact:quote:start -->
> Anschau said: Wait Tribal Kings don't get courts? Click to expand...
<!-- artifact:quote:end -->
Only feudal kings and emperors gets it and the goverment muslims got

## Reply 140 — participant_068 · 2022-01-27 · post-28039836

<!-- artifact:quote:start -->
> GoldenSilver said: As much as you have the right to think this is what the game is supposed to be and wish for it to go on that direction, what the game actually is will be defined by Paradox's vision for the product. I'm not Paradox but it's very obvious that CK series was never meant to be a 100% strict realistic medieval simulation. CK3 isn't, CK2 certainly wasn't (immortality, aztecs, demon cults etc), and I don't think CK4 will be. My advice is to either change your expectations or look for another game that actually is what you envision otherwise you may be forever disappointed. Click to expand...
<!-- artifact:quote:end -->
Certainly it is up to Paradox to define where to go with the game. I never claimed otherwise, isn't it? Mine is just one in a sea of different opinions that Paradox can take into account. But more on that later in my closing sentence. It's curious that immortality, aztecs and demon cults were things I never delve into CK2, while having great fun playing and modding the game to my heart's (and thousands of other hearts) content. After all CK2 was much, much more than about fantasy scenarios and memes while having such content as totally optional. Regarding CK3, I can also underscore the seminal interview of @Doomdark, the lead game designer of the game, where he claimed that things out of normal such as immortality (and I guess aztecs and demon cults also fit the bill) were not meant to be introduced in vanilla gameplay. Regarding your advice I clearly will not follow it as CK3, conveniently modded, is my favourite game at the moment! So, quite wide of the mark on reading me, I guess... Finally and going full circle addressing your subject matter, based on the recent poll and its content that Paradox launched to those that stopped playing the game, I can only point out that Paradox is still grasping for where the game will go from here.

## Reply 141 — participant_040 · 2022-01-27 · post-28039897

<!-- artifact:quote:start -->
> “Among the Langi of northern Uganda,” writes Sylvia Tamale, dean of the faculty of Law at Makerere University Uganda, “the mudoko dako, or effeminate males, were treated as women and could marry men.” There were also the Chibados or Quimbanda of Angola, male diviners whom, some scholars have argued, were believed to carry female spirits through anal sex. For centuries, woman-to-woman marriages in pre-colonial African societies seemed to indicate to Europeans that the strong correspondence between male to man and female to woman was not prevalent in Africa. This practice of same-sex marriage was documented in more than 40 precolonial African societies: a woman could marry one or more women if she could secure the bridewealth necessary or was expected to uphold and augment kinship ties. The idea that a female could be a husband perplexed Europeans, and often lead to fantastical conclusions. Click to expand...
<!-- artifact:quote:end -->
The “Deviant” African Genders That Colonialism Condemned - JSTOR Daily European travellers and anthropologists found that their gendered worldview didn’t easily map onto the societies they encountered. daily.jstor.org

## Reply 142 — participant_046 · 2022-01-27 · post-28040153

<!-- artifact:quote:start -->
> SauronGorthaur said: Which is simply an issue of testing and not the kind of the more intensive work described in blackninja's post. And changing a hard-coded element also requires plenty of testing, albeit more of the QA variety. As for doing it via game rules, I don't see why Paradox shouldn't just keep the current one as the default if they went with this route to tackle this subject. They picked the current rate in the first place for a reason. And I'd wager the casual players are at this point a majority so the default would be aimed at them, while the minority asking for harder warfare wouldn't be overwhelmed with rules. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: As I already pointed out, what was actually being requested in the post blackninja replied to there was simply to make "warfare not terrible". Which is extremely vague and open to interpretation, because of how completely subjective it is. Which is precisely why such a demand could be technically fulfilled with even a small change like my example. Which, admittedly, is one of the plethora of reasons why there is little value in "X is terrible" as a criticism. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: Not how Paradox itself made it look like during Azure's development. And bug fixes are standard part of any version release and fixing bugs is pretty much expected of software developers, because customers are paying for software that works properly. So it's probably the worst comparison you could have made. Especially in context of Paradox, especially-ier in context of CK3 team in particular, which hadn't released even a minor bug patch in seven months. As such major patches are the only time left for them to release bug fixes. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: Like I said, I was just being thorough. If what you're saying is the case, things only revert to my previous point about how an argument about lack of complaints about non-modding parts of the upcoming update in a thread dedicated to the modding changes makes no sense. Because it relies on portarying people not posting off-topic as somehow something wrong. Which is not only a rather fallacious argument, but it'd require people to outright break forum rules. Which would be a weird sentiment coming from an employee of Paradox. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: That one specific aspect of the culture overhaul? Sure. Other aspects of it, including the new system as a whole? I've seen criticism of them that essentially amounts to there being too much time spent on those compared to how much culture matters in game. And technically, there actually was a poster talking about devs wasting time in the dev diary about the change of direction in regards to changing existing cultures. It's just they portrayed the dev diary itself as a waste of time. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: And yet there's a post complaining about the court (or at least it's art aspect) being a waste of time without giving a reason as to why just two posts below your comment. Rather ironic coincidence. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: No, it's pretty much exactly what they said. Their claim was that gay marriage gets singled out for complaints about how dev time is allocated and that it's not for any genuine reason. Which, even putting aside how the claim about it being singled out is disproved even by the next DLC's very namesake, is pretty explicit. You can try to soften it with how it was about only posters who give no reasons as to why this is a waste of time while they give reasons in other cases or even how it was about only comments made by German albinos, during a blood moon, while the Wild Hunt was running through the sky, but that's not actually there in blackninja's post. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: The phrase "more likely" is also nowhere to be seen in their comment. If that was their actual claim, I wouldn't have objected to it, even if you can see more of bad faith criticism in the dev diary about same sex concubinage than this one (though to be fair, a handful of posts here had been removed and the one I did notice before it was gone was rather bad). Click to expand...
<!-- artifact:quote:end -->
I was never arguing it was a monumental tasks, just that it isn't trivial (and more work for Paradox than a modder specifically). This was just to tie into the point of not wasting time redoing things. And I gave a reason for why your particular example doesn't make sense to do yet. The point is there are a lot of little things paradox could do, but doing them haphazardly would mean they'd have to spend time redoing things, and that time adds up. Like I personally would also like to see the effect of development increased. But as I also want to see the economy and trade overhauled, such a change makes more sense to do when reworking them, rather than doing the change twice. Also your example change would make "warfare not terrible" as being requested, it would make warfare less terrible, which is an entirely different beast. If just arguing that Paradox should do something for war, than I'd argue that is already the case as they have add more culture specific feature for war (which gives some more variety) and added the ability to hire specific commanders (which gives more control). There probably are some bug fixes too. So if all you want is some kind of improvement to be done then that is already the case. But I highly doubt those complaining about the war system will be satisfied with just a tiny change. Isolated as in mostly isolated for other systems that are being over hauled in the future. Obviously it is very integrated with the marriage system. But as I mentioned the marriage system seems to be okay in players' eyes and so an overhaul of it is unlikely any time soon, if ever. Also I noticed you never responded to my points that culture is connected to gay marriage. So even if you don't think it's not isolated, that should make it connect in with DLC as you were ultimately complaining it wasn't. So I don't know why you are trying to argue just this aspect, when the other is also counter the argument that marriage doesn't make sense to work on for a culture focused update. Also releasing separate patches versus what to work on in patch are two different beasts. Everything I'm talking about is related to working within a patch. Releasing things as separate patches create extra work (mainly for QA). But I'm not here to defend Paradox's decision on no bug patch since Azure's release, as I personally think it would have been worth the extra work given the amount of time between patches (though as a modder not having to worry about updating for patches is nice). Edit: You also mention that blackninja9939 made points not related to the original comment that sparked the conversation, but I don't think the comment you were responding to was specifically talking about that one comment anymore. For this part "Or about any other of the myriad of reworks and changes coming in 1.5 and Royal Court of which plenty enable incredibly ahistorical behaviour on top of the options already provided.", I viewed this as the one point he opened it up (but definitely not in terms of the type of complaint), but personally I took it to mean people talking outside this dev diary thread and complaining about the gay-marriage in this dev diary as being the cause of their desired feature missing, when they could have complained about anything. As I have seen, and assumed blacknija9939 has too. But I'll admit this is not the only way I think this could be read. But I don't think there is any interpretation where your example of people complaining about the implementation of a feature makes sense. I don't read blacknija9939's comment as arguing against that existing, but sure if that's how you see it, then yes they were hyperbolic. The point still stands that gay marriage draws more hate for wasting time than when compared to other features given the amount of development time it took (the court scenes and culture rework definitely took a lot more time than gay marriage so they are not on comparable time scales). Actually I wouldn't be surprised if that post was crafted that way specifically because of my comment, as it reads as comment informed by the discussion at hand (also to be clear, I'm not calling that comment out; while I don't agree with everything they said, that's just difference of opinion). But either way I never said it doesn't happen, just that the rate of lack of reasoning is higher for gay marriage. My point that bigots make gay marriage the topic of conversation for non-bigots with legitimate complaint, just now focused at gay marriage specifically, would still meet a harsh understanding of blacknija9939's as for why gay marriage gets singled out and still have it be rooted in bigotry. The key is blacknija9939 is talking about the process of it being singled out, not every comment. If you interpret it as referring to every comment, I can see more where you are coming from, but that is just your interpretation (you might be right, but if that was the case I think they would have just said that). Also for someone whose problem with second to last paragraph is that a very literal interpretation of their comment is not strictly true, I find to weird that you seem to be willing to fill in a lot of gaps for the last paragraph. Okay, I think interpreting gets singled out, as the only thing people ever complain about is a bit uncharitable. But even, if I agree to that, their overall point still stands. And you could have just said you thought he was being hyperbolic. But your comment reads more as his entire point is moot, especially since you never mention anywhere that gay-marriage or same-sex concubines have received undue hate like you are now or that it might make sense with in a specific context (despite the fact you have said you were just being through). So you are getting made at them for not including nuance when you yourself also failed to include nuance. On the post being removed aspect, this actually happens a lot in threads with gay marriage/concubines and it's often more than a handful that end up being removed (as there are sometimes multiple waves of removal). Edit: Also happens when some argue non-straight characters, historical or not, shouldn't even be in the game edit: clarity

## Reply 143 — participant_072 · 2022-01-28 · post-28040408

<!-- artifact:quote:start -->
> DreadLindwyrm said: Just say you don't want gay people represented and be done with it. Click to expand...
<!-- artifact:quote:end -->
Homosexual, bisexual and asexual people are already represented in the game.

## Reply 144 — participant_061 · 2022-01-28 · post-28040575

I ran out of time earlier when I posted because of having to go to work, so I'll just add this second part of my thoughts here... I have an issue with the dev post earlier commenting that people didn't complain about the widgets and other modding features and suggesting that those were unimportant things and so people should be complaining about those like they were about gay marriage and stating that because they weren't, it was proof that the person who was being quoted was only complaining because it related to gays. This is a real problem coming from a dev to suggest that the modding features are equally unimportant in the scheme of things as gay marriage. Modding is an extremely important part of the game and the devs should know that. Either the post was from someone who doesn't understand how important modding is to the game or else they were purposefully being disingenuous. Here's the thing with modding features. Will widgets have a huge impact for every player? No, especially if the player doesn't use any mods. However, if modding support wasn't part of this game, you'd have at least 25-50% less sales and that many fewer active players. Note that this is my estimate without actual data to back it up, but I'm sure it's accurate. If not, it is still a significant number. Whether or not gay marriage is in the game will not have any noticeable impact on sales or active players. So to suggest that if people want to complain about gay marriage that they can't be complaining about it because it's a minor thing that isn't really that important just because they aren't also complaining about modding features is ridiculous. Now, you may say that I'm referring to the entirety of modding and so it's an unfair comparison. The problem with that argument is that each and every modding feature that is added has an unknown value behind it until modders get ahold of it and start coming up with interesting ways of using it. Are window widgets going to end up offering much value to the game? We don't really know. They may end up being rarely used by any popular mods or they may end up being the one thing that lets a modder create a mod that is worlds above anything we've seen before. It will depend on what the modders come up with when they have access to that feature (and the others). We aren't able to judge how any individual modding feature will turn out until after they are made available, so the best option is to make them available and then see what comes of it. The only reason to complain about modding features being added to the game, no matter what they are, is if you never plan to use a mod. Otherwise, every single modding feature has potential to make this game significantly better if the modders come up with a good use for the feature. In the end, few features have as much potential to improve the game than modding features. At least for people who use mods. And to be clear, I haven't really used mods in CK3 other than one that color-coded the sexuality icon to depict the gender because of the difficulty when the game first came out to differentiate genders in some cases. That's no longer needed with the improvements to the characters, but it was very helpful in the beginning. Other than that, I haven't used mods because I tried them in CK2 and never found any that I liked. But CK3 does offer so much more modding support that I'm sure I'll find some great mods that I will like once I decide to start looking for them (I'll definitely be adding in the community flavor pack!). So I'm not supporting modding features due to being a modder (I'm not one) or using mods all the time (as I said, I don't). I'm supporting modding features because without them, this game would very likely only have a few DLC before PDX stops updating the game due to lack of players. Modding is the reason that the game will receive a lot of improvements because it's what keeps a very significant number of players playing the game. So I really am not happy with the dev suggesting that modding features were unimportant or comparing their value with that of what really doesn't impact the game in any meaningful way. As I said in my post earlier today, I'm fine with them adding this or similar types of minor features, especially if they are popularly requested features. But I think they need to save those for a couple years from now once the game itself is in a more playable state. Time now should be focused on improving the core game (that includes modding features) and not worrying about minor things like gay marriage. And as I said, I think RC would have been far better later as well as other than the culture changes, it really isn't doing anything to significantly improve the game compared to other DLC they could have started with. And I like RC and even like the court, which many are complaining about. I just think it's not the right time for something that will have little impact on the main gameplay (other than cultures). Of course, with cultures, it's left to be seen if they will be really that useful for the game. Faiths and custom faiths seemed to be amazing when we were told about them. But once you deal with being constantly holy warred and crusaded because you wanted a custom faith, it very quickly lost it's interest and ended up being a side note that really has little impact on the game. I'm hoping cultures won't turn out the same way.

## Reply 145 — participant_073 · 2022-01-28 · post-28040643

On the subject of mods, how will the 3D court interact with mods that add 2D character images?

## Reply 146 — participant_046 · 2022-01-28 · post-28040729

<!-- artifact:quote:start -->
> Riamus said: I think the question of whether or not something is considered a "waste of resources" is less a matter of "what I want" or "what I don't like" and more a matter of what will actually improve the game... at least for most people here. Yes, there will be some complaining because they don't like gays. Yes, there will be some complaining because they don't like feature X. But when it really comes down to it, most complaining aren't really complaining for those reasons, but instead because these changes really don't improve the game in a meaningful way. Yes, people who want gay marriage will consider it an improvement. And it is an improvement for them. However, will adding it draw in more players? Will it get more people playing the game again who have stopped playing? I'd say any increase in numbers due to that change will be minimal. On the other hand, features and changes that people list as reasons why they stopped playing the game or consider the game to be "shallow" will have a far greater impact on those very important numbers. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Riamus said: The dev did point out that dev time for some of the important changes and features like improving AI warfare are far more time consuming to do and I get that. Many of these features and changes that will have a high impact on bringing players back to the game are going to take a lot of time and effort. However, one of the things that reviews of RC have brought up already are that the events aren't great and are repetitive (meaning not enough of them). Adding new events or reworking existing events to better use characters who make sense or to use characters that are meaningful to the player is really not that difficult or time consuming except if you talk about adding a lot of them as more = more time. That alone would have more impact on more players than gay marriage, which being as it is a rule will end up being used by a limited (though not necessarily small) number of players. Other changes can also be made in stages, allowing you to make a change that will improve, for example, AI warfare somewhat without having to take the time to completely rework it. There are certainly ways to take things that are keeping people from enjoying the game and adding them in without needing a significant amount of dev time to do so if they wanted to do it. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Riamus said: And as was pointed out, the devs specifically said adding in gay marriage would be a challenge as it impacts a lot of parts of the game and would need a lot of testing and work to get it working properly. So the suggestion that it isn't a big deal to add by the dev is a bit inconsistent and probably not very accurate. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Riamus said: Personally, I think any feature (even highly requested ones) that does not actually improve gameplay value of the game should be held off until a later time while they work on getting the game up to a level where players don't get tired of it so quickly. And to be clear, just because gay marriage is a gameplay item doesn't mean it actually improves gameplay value. If that isn't in the game, will it prevent a player from enjoying the game? No. They may prefer it to be there, but if it's not there, they will either enjoy or not enjoy the game the same as if it was there because it really doesn't affect anything in gameplay unless they find it fun to try and convert the entire map to be gay or something. Otherwise it's just a "novelty" (and I am not meaning to use that in any rude way, but just as a definition of something that has little meaningful impact to the game). This is true for any similar feature that may be added. Compare this to adding in something (yes, this is a big feature) like regency in a way that's improved over CK2's regency mechanic, which would actually improve an aspect of gameplay and that's honestly a pretty minor issue in the game overall. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Riamus said: Look at it this way, if you added gay marriage to the game separate from anything else so that you aren't impacting the results by other features, you might draw in some players who had stopped playing the game who want the feature, but they'll play a game or two and remember that the game itself gets old quickly because it's missing so much content that they'll put it down again because gay marriage doesn't actually fix any of the real issues in the game. As a side note, I also think RC would have been far better off to be added at a later date as well. I like RC and it has some really interesting aspects to it (I even like the court even if many do not). But I really don't think anything other than cultures will bring people back to the game and it's yet to be seen how well they managed to get the cultures working. I think another DLC might have been better at this stage than RC... something that would add a significant boost to the gameplay value of the game. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Riamus said: I ran out of time earlier when I posted because of having to go to work, so I'll just add this second part of my thoughts here... I have an issue with the dev post earlier commenting that people didn't complain about the widgets and other modding features and suggesting that those were unimportant things and so people should be complaining about those like they were about gay marriage and stating that because they weren't, it was proof that the person who was being quoted was only complaining because it related to gays. This is a real problem coming from a dev to suggest that the modding features are equally unimportant in the scheme of things as gay marriage. Modding is an extremely important part of the game and the devs should know that. Either the post was from someone who doesn't understand how important modding is to the game or else they were purposefully being disingenuous. Here's the thing with modding features. Will widgets have a huge impact for every player? No, especially if the player doesn't use any mods. However, if modding support wasn't part of this game, you'd have at least 25-50% less sales and that many fewer active players. Note that this is my estimate without actual data to back it up, but I'm sure it's accurate. If not, it is still a significant number. Whether or not gay marriage is in the game will not have any noticeable impact on sales or active players. So to suggest that if people want to complain about gay marriage that they can't be complaining about it because it's a minor thing that isn't really that important just because they aren't also complaining about modding features is ridiculous. Now, you may say that I'm referring to the entirety of modding and so it's an unfair comparison. The problem with that argument is that each and every modding feature that is added has an unknown value behind it until modders get ahold of it and start coming up with interesting ways of using it. Are window widgets going to end up offering much value to the game? We don't really know. They may end up being rarely used by any popular mods or they may end up being the one thing that lets a modder create a mod that is worlds above anything we've seen before. It will depend on what the modders come up with when they have access to that feature (and the others). We aren't able to judge how any individual modding feature will turn out until after they are made available, so the best option is to make them available and then see what comes of it. The only reason to complain about modding features being added to the game, no matter what they are, is if you never plan to use a mod. Otherwise, every single modding feature has potential to make this game significantly better if the modders come up with a good use for the feature. In the end, few features have as much potential to improve the game than modding features. At least for people who use mods. And to be clear, I haven't really used mods in CK3 other than one that color-coded the sexuality icon to depict the gender because of the difficulty when the game first came out to differentiate genders in some cases. That's no longer needed with the improvements to the characters, but it was very helpful in the beginning. Other than that, I haven't used mods because I tried them in CK2 and never found any that I liked. But CK3 does offer so much more modding support that I'm sure I'll find some great mods that I will like once I decide to start looking for them (I'll definitely be adding in the community flavor pack!). So I'm not supporting modding features due to being a modder (I'm not one) or using mods all the time (as I said, I don't). I'm supporting modding features because without them, this game would very likely only have a few DLC before PDX stops updating the game due to lack of players. Modding is the reason that the game will receive a lot of improvements because it's what keeps a very significant number of players playing the game. So I really am not happy with the dev suggesting that modding features were unimportant or comparing their value with that of what really doesn't impact the game in any meaningful way. As I said in my post earlier today, I'm fine with them adding this or similar types of minor features, especially if they are popularly requested features. But I think they need to save those for a couple years from now once the game itself is in a more playable state. Time now should be focused on improving the core game (that includes modding features) and not worrying about minor things like gay marriage. And as I said, I think RC would have been far better later as well as other than the culture changes, it really isn't doing anything to significantly improve the game compared to other DLC they could have started with. And I like RC and even like the court, which many are complaining about. I just think it's not the right time for something that will have little impact on the main gameplay (other than cultures). Of course, with cultures, it's left to be seen if they will be really that useful for the game. Faiths and custom faiths seemed to be amazing when we were told about them. But once you deal with being constantly holy warred and crusaded because you wanted a custom faith, it very quickly lost it's interest and ended up being a side note that really has little impact on the game. I'm hoping cultures won't turn out the same way. Click to expand...
<!-- artifact:quote:end -->
This is just your conjecture. Ironically I've already read comments mentioning same-sex marriage as a reason for them to get back into CK3. Now that might be anecdotal evidence, but so is yours. One of the points blackninja9939 made is that it only took two disciplines to add same-sex marriage, and that many of the features people are requesting require more than that. Now I don't know for sure what those disciplines are but they probably are the same ones that script in events. So you have to figure out a feature that the devs who worked on same-sex marriage could have done instead rather than just any feature you feel would make the game better. Plus I find it interesting you mention they should have made more events. As other places on this forum, one of the complaints I commonly hear about RC is that it is too event focused. So even the feature you are arguing for is argued against else where. So I wouldn't be so quick to presume which features are the ones that would draw the most players back to the game. The thing you are referring to is a post about way back when same-sex concubines got removed as thing mods could do by 1.3 due to another dev's bug fix also disabling the feature for mods. That post just said it was too involved to be quick change and that as it was mod support, it was lower priority. Then sometime after that, it was announced that the ability to mod in same-sex concubines would be back in for 1.4 and in the future (if all went well) 1.5 would allow same-sex marriage to be modded in (no mention of it being difficulty). Nothing in that thread mentioned it as a challenging problem that impacted lots of the game, just that there was more involved then just undoing a simple bug fix someone had done (especially since that would mean the bug they had fixed would be back in the game). So the area between quick change and overhauling an entire system is vast. So there is plenty of space for same-sex marriage to be in there. Plus most of the wait was mentioned being due to being low priority, rather than the time involved in fixing it, so I wouldn't be surprised if it was schedule as a task for them to do when they couldn't work on what you'd considered more impactful tasks. It's not uncommon for these more narrow scope tasks to be used to fill in the gaps for devs who otherwise don't have a larger project to work on because they either need someone earlier in the chain to finish working on it, or need another coworker(s) to finish their current task so they can work on the next major thing together (a common example of this is art assets unrelated to an expansion being added because the expansion didn't have enough art related work to keep the artists busy). It might be a novelty for you, but it isn't for everyone. Also it does add a new way to play the game because it will add the challenge of a marriages with no children (and since your character is gay you can't easily seduce your way out of that issue either). And it's an interesting and new challenge I look forward to. Also I don't think your idea of not adding requested features to the game, even highly requested ones, will bring players back. Especially since by virtue of being highly requested means it has gameplay value. They improve the game though the fact people wanted them in the game. And people having features in the game they like and find enjoyable will make them want to play the game for longer. Also with your regencies, you have to find a task the devs who worked on same-sex marriage could have worked on instead and regency isn't one of them. Plus from my personal point of view, regencies are something that would be nice, but would not get me to start playing the game regularly again, unlike the culture update and gay marriage (heck I personally prefer court rooms and artifacts over regencies). So again different people will have different feature that will make them enjoy and play CK3 more. Couple things to keep in mind is that the Paradox forums tend to be more negative and critical of the game then the average player (in part because forum posters make up a tiny portion of the fan base). And even with that there are plenty who on these forums have mentioned looking forward to having artifacts, courts and/or the culture update (or say there is no major problem with the game). I myself like the idea of the court and artifacts, but will admit it's not my first choice (but who knows maybe they will surprise me, but I'm not gonna judge them too harshly until I try it). But I am supper excited for the culture update. Also even on these forums people who say there is a problem with the game can't agree what it is. I seen people argue it's warfare, economy, characters, lack of interactions, challenge level, content, variety, etc. and then argue it's not one of the other reasons I just mentioned (and some these the update/DLC will help address). My point is that Paradox has a juggling act they have to do as there are many different people who play CK3 for many different reasons. And so naturally people will want different things out of the game. And since you seem to be worried about the games overall players, why not rejoice that the game just added a reason that some people have said would get them to start playing again (and it's in an optional way so it won't detract from the game play of those who don't want it; which can't be said for something like a warfare overhaul, which can't be optional and there will surely be some who won't like the changes). I find this ironic since same-sex marriage was first announced as a mod feature (and it still was complained about). There's a reason the announcement of it was part of the modding dev diary. Also same-sex marriage is a feature many of the highly anticipated mods like Elder Scrolls, After the End, and Game of Thrones have mentioned wanting (I'll admit not their top choice, but I think you are down playing how many popular mods will make use of same-sex marriage). This is again another reason it was put in the modding dev diary, as it is seen as being an asset to mods. Also blackninja9939 was definitely not dissing mods. Also, since you are worried about player numbers, I should probably tell you that most players don't use mods. The most used mod on steam (The Community Flavor Pack) has less than 250,000 subscribers. There are estimated to be between 1.3 and 5 million people who own CK3. So even taking the generous low ball figure, that's less than a fifth of the fan base use the most popular mod. Now obviously not every one who uses mods uses the most popular one. But even if we add in the next 2 most popular mods (Nameplates and Daddy Pika's Cheat Menu) we still only get less than 600,000. This is assuming no one who use one of theses mods uses another one too. But even with that dubious assumption we still aren't even half way to the low ball estimate for the number of people who own CK3. Now I'm not dissing mods either (I'm a modder myself after all). But the fact is, a feature being in the game makes it way more accessible to players than being in a mod (and makes it way easier for mods to use it and still be compatible). So the very fact same-sex marriage is an in game feature now gives it more impact than many modding only features.

## Reply 147 — participant_074 · 2022-01-28 · post-28041159

<!-- artifact:quote:start -->
> blackninja9939 said: Adding in a fairly highly requested modding feature that only needs two disciplines and in very focused areas? Much less time. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> blackninja9939 said: And I'm gonna be incredibly blunt here, nobody is complaining we added scripted widgets as mod support. Or made a court scene editor that mods can use too. Or any of the other bits of mod support we added. Or about any other of the myriad of reworks and changes coming in 1.5 and Royal Court of which plenty enable incredibly ahistorical behaviour on top of the options already provided. But gay marriage gets singled out for complaints? Lets not pretend that is for any remotely genuine reason or concern in where we spend our time developing the game, because we all know it isn't. Click to expand...
<!-- artifact:quote:end -->
Out of interest is this retroactive legitimation, or can a popular thread / change dot org petition get the developers to prioritise a desirable mechanic. E. G. Steppe nomads Why are you so dismissive of criticism when there are numerous threads and posts complaining about royal court as a whole and specifics like the 3d court room? what-is-the-point-of-the-court.1507912 will give you a few examples

## Reply 148 — participant_075 · 2022-01-28 · post-28041237

Thread closed for moderation. Edit: Thread cleaned up and opened again, but any further homophobia will result in more infractions, banning and a permanent closure of the thread. There will be no more discussion surrounding the validity of LGBT+ people, in-or-out of the game.

## Reply 149 — participant_076 · 2022-01-28 · post-28041559

<!-- artifact:quote:start -->
> AvengedK1ng said: Out of interest is this retroactive legitimation, or can a popular thread / change dot org petition get the developers to prioritise a desirable mechanic. E. G. Steppe nomads Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> AvengedK1ng said: Why are you so dismissive of criticism when there are numerous threads and posts complaining about royal court as a whole and specifics like the 3d court room? what-is-the-point-of-the-court.1507912 will give you a few examples Click to expand...
<!-- artifact:quote:end -->
You can pretty easily find a thread asking for modding support for gay marriage (and a couple of extras) that: - Has been around since less than a week after the game was released, and - Has over 500 reactions, with a bit over 75 % of them being in favour (as of me writing this, there's 242 Agrees and 155 Likes to 118 Respectful Disagrees; there's also eight total reactions not belonging to any of those categories). I'd say that qualifies as "Fairly highly requested", and that there's nothing retroactive about it... particularly as the thread in question has been on the devs' radar for a long time, with a statement that at least modding support for gay marriage was coming in 1.5 having been made quite far back (blackninja9939 personally posted about that in the relevant thread, so he'd most certainly know...). As for the other half of the question, the devs tend to take note of popular suggestions (at least any that aren't deemed completely unfeasible and that don't cross any hard lines they don't want to cross...), and a popular and good suggestion could conceivably affect the likelihood of something happening sooner rather than later, if not necessarily right away; e.g. I'd imagine they already have narrowed down what the next content pack will focus on quite a bit, so even a truly outstanding suggestion related to something else would probably not take precedence over that. A popular suggestion that was less well-written or -researched would probably also have a decent shot, but less so. I'd imagine the specific example you mentioned would involve more work and disciplines than gay marriage did -- at least assuming you're looking for art/interface stuff, flavour, unique mechanics, etc. as part of it -- and thus would be harder to find the time for alongside other stuff that's planned in an update, but a decently popular smaller suggestion -- or an important piece of the puzzle that's missing -- would be reasonably likely to end up on a "Do this in the next version!" list or reasonably high on a "Do this if there's time left!" list. I think it's fair to grant that assorted things not in the dev diary have been complained about in various places... but as far as the contents of the dev diary goes the complaints have really been focused on the gay marriage, and even disregarding the homophobic phrasing in quite a lot of the posts that got deleted I don't think there's much doubt that many of the complaints about it have a lot more to do with it being gay marriage than it being ahistorical regardless of whether the latter is being brought up, particularly as other pretty ahistorical content isn't being complained about as much (or necessarily by the same people...) and as the dev diary that went over how sexuality was being modelled way back when also seemed to attract a good amount of complaints (at least some of them deleted...) along similar lines, which I rather doubt anyone honestly thinks is a random coincidence...

## Reply 150 — participant_027 · 2022-01-28 · post-28041608

People keep using Islam as an example here, but I seem to recall a very popular thread from when homosexuality being in the game was first announced regarding that male lovers were not uncommon in Andalucia. Here are a couple of lengthy askhistorians comments on the topic: Islam's historical relationship with homosexuality (This in particular is actually a good example of what IIRC @grommile was saying regarding historical practices not necessarily fitting cleanly into our modern definitional paradigm) A response in the same thread regarding lesbianism in particular. In other words: Stop using Islam as an example of how crazy and ahistorical certain features are. Note: I'm not suggesting these were common, widespread, acceptable within religious law, or that marriages occurred. Simply that Islam isn't a universally fundamentalist bulwark you can throw up to discredit behavior we see as modern or which inherently makes certain things being in the game entirely implausible in any timeline. EDIT: also doesn't make something like this being in the game unjustifiable, particularly when it was a much requested feature.

## Reply 151 — participant_072 · 2022-01-28 · post-28041674

<!-- artifact:quote:start -->
> IndigoRage said: People keep using Islam as an example here, but I seem to recall a very popular thread from when homosexuality being in the game was first announced regarding that male lovers were not uncommon in Andalucia. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> IndigoRage said: In other words: Stop using Islam as an example of how crazy and ahistorical certain features are. Click to expand...
<!-- artifact:quote:end -->
Lovers, yes. How common were marriages?

## Reply 152 — participant_027 · 2022-01-28 · post-28041678

<!-- artifact:quote:start -->
> Baron Bratwurst said: Lovers, yes. How common were marriages? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> IndigoRage said: Note: I'm not suggesting these were common, widespread, acceptable within religious law, or that marriages occurred. Simply that Islam isn't a universally fundamentalist bulwark you can throw up to discredit behavior we see as modern or which inherently makes certain things being in the game entirely implausible in any timeline. Click to expand...
<!-- artifact:quote:end -->
I mean the thread I brought up mentions varying punishments up to and including death for female homosexuality as well as completely ignoring it and letting it slide on the other end of the spectrum. With that in mind I don't think you're reading what I've said the way I've intended.

## Reply 153 — participant_077 · 2022-01-28 · post-28041741

<!-- artifact:quote:start -->
> DebbieElla said: Thread closed for moderation. Edit: Thread cleaned up and opened again, but any further homophobia will result in more infractions, banning and a permanent closure of the thread. There will be no more discussion surrounding the validity of LGBT+ people, in-or-out of the game. Click to expand...
<!-- artifact:quote:end -->
Any chance you could clean up the Steam forums a bit too? Some really extreme homophobia going on there, including people saying that homosexual people are basically animals.

## Reply 154 — participant_035 · 2022-01-28 · post-28041802

<!-- artifact:quote:start -->
> Zewp said: Any chance you could clean up the Steam forums a bit too? Some really extreme homophobia going on there, including people saying that homosexual people are basically animals. Click to expand...
<!-- artifact:quote:end -->
That might be a different moderation team, but it could certainly do with being brought to that team's attention if it's that bad.

## Reply 155 — participant_078 · 2022-01-28 · post-28041876

I would prefer you fix core issues with the game and not spend time on adding things that are not core to the experience of a historical game. The release was already behind, really trying to understand why you would think its a good idea to delay a release to add in non core features to the game.

## Reply 156 — participant_033 · 2022-01-28 · post-28041911

<!-- artifact:quote:start -->
> druez said: I would prefer you fix core issues with the game and not spend time on adding things that are not core to the experience of a historical game. The release was already behind, really trying to understand why you would think its a good idea to delay a release to add in non core features to the game. Click to expand...
<!-- artifact:quote:end -->
What do you think caused the devs to delay the release of The Royal Court? Are you saying that you believe adding the features mentioned in this dev diary are what caused the delay? Because that’s not what I understood to be the cause, at all. If I have time, I’ll dig up the relevant dev posts. Edit: delay was due to stability & quality issues, & bugs.

## Reply 157 — participant_078 · 2022-01-28 · post-28041931

<!-- artifact:quote:start -->
> Flockingbird said: What do you think caused the devs to delay the release of The Royal Court? Are you saying that you believe adding the features mentioned in this dev diary are what caused the delay? Because that’s not what I understood to be the cause, at all. If I have time, I’ll dig up the relevant dev posts. Click to expand...
<!-- artifact:quote:end -->
What I'm saying is that there is only so much time. You can choose to spend that time how you want. I would prefer they spent the time on things that are core to the game. That is it. They said that originally that gay marriage was much more complex then people thought and it was one reason it wasn't included. They would have to have the ai modified for it and modify other systems as well. So, yes obviously this took additional time, it would be naïve to think it didn't and they themselves said it would be complex to add. I also dont want them to spend time adding in glitterhoof or immortality etc... All of these things are fine to add when we are years into the game, but right now there are still core features missing from the game and the AI still needs a ton of work, especially combat ai. We still don't have ai that plays differently based on their personality traits. We still don't have republics. So, yes I do believe doing this feature added to their development and testing queues and helped to delay the game. No, I don't think they would ever come out and say adding this feature added to the backlog and helped to delay the game. Just expressing my opinion. Overall, I love ck3 and thing long term it will be a great game but they still are missing core features and I would like for them to focus on that first.

## Reply 158 — participant_033 · 2022-01-28 · post-28041954

<!-- artifact:quote:start -->
> druez said: What I'm saying is that there is only so much time. You can choose to spend that time how you want. I would prefer they spent the time on things that are core to the game. That is it. They said that originally that gay marriage was much more complex then people thought and it was one reason it wasn't included. They would have to have the ai modified for it and modify other systems as well. So, yes obviously this took additional time, it would be naïve to think it didn't and they themselves said it would be complex to add. I also dont want them to spend time adding in glitterhoof or immortality etc... All of these things are fine to add when we are years into the game, but right now there are still core features missing from the game and the AI still needs a ton of work, especially combat ai. We still don't have ai that plays differently based on their personality traits. We still don't have republics. So, yes I do believe doing this feature added to their development and testing queues and helped to delay the game. No, I don't think they would ever come out and say adding this feature added to the backlog and helped to delay the game. Just expressing my opinion. Overall, I love ck3 and thing long term it will be a great game but they still are missing core features and I would like for them to focus on that first. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> blackninja9939 said: You're not thinking about scale, reworking some code and script to enable gay marriage is infinitely less time than any of the reworks you proposed. They require new designs, overhauling UIs, new art, plenty of new code and content. Spreading over the course of likely weeks for any larger rework. Adding in a fairly highly requested modding feature that only needs two disciplines and in very focused areas? Much less time. And I'm gonna be incredibly blunt here, nobody is complaining we added scripted widgets as mod support. Or made a court scene editor that mods can use too. Or any of the other bits of mod support we added. Or about any other of the myriad of reworks and changes coming in 1.5 and Royal Court of which plenty enable incredibly ahistorical behaviour on top of the options already provided. But gay marriage gets singled out for complaints? Lets not pretend that is for any remotely genuine reason or concern in where we spend our time developing the game, because we all know it isn't. Click to expand...
<!-- artifact:quote:end -->
Did you read post#114? Or the subsequent discussion about the comparative difficulty of adding different features? Because the points you are making have been made earlier in the thread. Ask yourself, please, why you named gay marriage, out of all the things in this dev diary.

## Reply 159 — participant_078 · 2022-01-28 · post-28042189

Umm because it isn't core to the game. Mod support has always been core to paradox games. If this dev diary would of been about the adding of glitterhoof, I would of said the same thing. I would prefer they add things that are core to the game. Anyway, I've made my point. Have a good day; we can just agree to disagree.

## Reply 160 — participant_071 · 2022-01-28 · post-28042224

<!-- artifact:quote:start -->
> druez said: Umm because it isn't core to the game. Mod support has always been core to paradox games. Click to expand...
<!-- artifact:quote:end -->
And modders want to be able to have gay marriage in their mods, so they made the necessary changes to allow mods to have it. And while they were there, they added a game rule (which disables achievements when set to "yes") so that you don't need to have a mod to turn it on.

## Reply 161 — participant_042 · 2022-01-28 · post-28042250

<!-- artifact:quote:start -->
> grommile said: And modders want to be able to have gay marriage in their mods, so they made the necessary changes to allow mods to have it. And while they were there, they added a game rule (which disables achievements when set to "yes") so that you don't need to have a mod to turn it on. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> druez said: If enough people want it, then of course they should do it. It isn't like I'm going to be upset if they add it. I wouldn't ever use the feature, unless it was included in one of the major mods like CK2++ or HIP or GoT. Click to expand...
<!-- artifact:quote:end -->
And he was already complaining back when the feature was going the be modding-only lol. Or even when it was only people asking for it to be mod only. I like how a lot of people wanted it, and you say you wouldn't be upset if they get it... except when they do you get so upset that one of your posts had to be moderated.

## Reply 162 — participant_079 · 2022-01-28 · post-28042272

I applaud the teams openness and encouragement of modding. Absolutely spiffing.

## Reply 163 — participant_071 · 2022-01-28 · post-28042284

Moving on to all the other awesome t hings in this post, I'm liking the look of Scripted Widgets, even though I have no mod plans of my own. UI customization for the win!

## Reply 164 — participant_080 · 2022-01-28 · post-28042315

<!-- artifact:quote:start -->
> druez said: Umm because it isn't core to the game. Mod support has always been core to paradox games. If this dev diary would of been about the adding of glitterhoof, I would of said the same thing. I would prefer they add things that are core to the game. Anyway, I've made my point. Have a good day; we can just agree to disagree. Click to expand...
<!-- artifact:quote:end -->
HOW DARE YOU. Glitterhoof is core to the game! Here is our beloved Glitterhoof as Pope whom sadly died from horsing around. " " being crowned default Grand Tournament Champion since you can't defeat a horse in jousting you fools. And finally, there is Glitterhoof getting it on spreading its horse culture.

## Reply 165 — participant_016 · 2022-01-29 · post-28042444

<!-- artifact:quote:start -->
> druez said: Umm because it isn't core to the game. Mod support has always been core to paradox games. If this dev diary would of been about the adding of glitterhoof, I would of said the same thing. I would prefer they add things that are core to the game. Anyway, I've made my point. Have a good day; we can just agree to disagree. Click to expand...
<!-- artifact:quote:end -->
this (gay marriages) was one of the most requested modding features. so by your logic core to the game.

## Reply 166 — participant_042 · 2022-01-29 · post-28042496

<!-- artifact:quote:start -->
> SauronGorthaur said: And out of everything you listed the specific comparisons blackninja actually used were the royal court scene that you yourself just admitted is directly related to the DLC and the widgets, which as I argued is at least tangentially related to the type of UI mechanics already used in the DLC. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: I already mentioned the Azure patch dev diary myself so there's no need for you to act as if I were somehow unaware of it. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: I outright quoted the relevant part of their post in the text of my paragraph you're replying here and it explicitly brought up lack of complaints about changes brought in the upcoming DLC going beyond the scope of this thread. So you should direct the remark about there being no need for off-topicness at them. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: If you think people are ignoring not only other ahistorical content but these specific examples just because they weren't complained about in a pre-release dev diary, you're not really paying much attention to the forums. Things like incest, nudity or cannibalism are common targets of criticism about CK3 being ahistorical or "pandering to memers", while what people arguing that consider more important content is being ignored. Also, quoting pre-release dev diary is just apples to oranges comparison here in the first place. For two reasons. First, people were much more optimistic then and willing to give Paradox the benefit of the doubt. Now with Royal Court development having a crawling pace and other issues, the overall attitude on the forum turned more sour from what I've observed. Secondly, during the development of the base game things were still up in the air one way or another. But came release, (lack of) gay marriage was something that was already hard-coded into the game, which then had to be undone to make it work. Which by Paradox's own admission, required enough work to do that it couldn't even been done in a major patch like 1.4. Not exactly the case with cannibals, is it now? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: And the other half of this tangent of yours is just a false. I've seen people call the whole culture rework as something that doesn't give enough gameplay for how large it is, as in their eyes you'll only interact with it just a few times during a campaign and then forget about (and I've seen that complaint numerous times). While calling culture-changing parts of it in particular more "meme content". Which kinda falls squarely under the umbrella of wasted development time and ahistorical content. And the court itself has not only been called a waste of development time, it's been outright accused of being the culprit behind the very 8 month development time you brought up. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: Yeah, no, you made that "context" up. Such remark is nowhere to be found in either blackninja's comment (which simply talks about gay marriage being singled out for complaints, period) nor the post they were replying to. Instead that post literally called the complaint at hand "an important point", that's simply worded in an "uncouth" manner. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> blackninja9939 said: And I'm gonna be incredibly blunt here, nobody is complaining we added scripted widgets as mod support. Or made a court scene editor that mods can use too. Or any of the other bits of mod support we added. Or about any other of the myriad of reworks and changes coming in 1.5 and Royal Court of which plenty enable incredibly ahistorical behaviour on top of the options already provided. But gay marriage gets singled out for complaints? Lets not pretend that is for any remotely genuine reason or concern in where we spend our time developing the game, because we all know it isn't. Click to expand...
<!-- artifact:quote:end -->
Sorry it took a while for me to reply, your post is longer so I had to set aside some time so I waited for friday. Except there were also the console commands, error logging and the widgets that might not be necessary to have the DLC for them so it's not DLC related. The DLC might use these themselves but a modder or player without the DLC can still benefit from it; this fits more as a 1.5 free patch content than DLC content. A user without RC very likely will not use the editor, that seems more like DLC content to me. Yet you did not address the negativity when it was only a modding feature. That post is also an example to the previous quote above that these were modding improvements not related to the RC DLC and yet they were not singled out. BlackNinja's post context takes into mind months of what happened on this forum as well, not just a simple response to a particular user. And yet there were people opposed to it that argued in this thread about historicity before his post like Prometheus_1 did on page 2 (and failed to compare to other ahistorical content from the game or from RC), and more recently other users did after his post. So the historicity of features is relevant to the dev-diary and not off-topic if people are using it to argue against one of the features of said dev-diary. Ahistorical and "memey" content has been present since CK2 (can't say about CK1 as I never played it) and it has become almost a staple of the series; I do not see such opposition to this as you claim. Especially since cannibalism religion (not the other two you mentioned) and a same-sex marriage feature would require player intervention to become commonplace in the game world, so people should complain about these even less. As was clear in this dev diary (or when it was a modding feature) same-sex marriage is not enabled by default and yet people keep complaining about its historicity but rarely that of a cannibalism religion (or a religion with the most "memey" tenets possible). For the second part, about the historicity argument his complaints are still valid because people are not raising concerns about historicity of RC content even if the community is as soured up as you say. Comparing the pre-release dev-diary to RC we can see in both cases people are ignoring historicity concerns except when same-sex marriage is mentioned (this even happened on that pre-release dev-diary), which is also something he mentioned on his post. For the last two sentences about development time, (he complained of this in his post as well, last paragraph), how common are the complaints about development time of ahistorical features in RC? And for the technical aspects specifically only they can respond since we don't know the internal mechanics of the game or what exactly they changed. As for cannibalism, there is a trait, events, crime type, a secret for it, a hook for it, character opinion, execution method, stress impact and events, and maybe more. While these are expected implementations for such a specific trait, all these have to be accounted for when a religion has it as a tenet and great virtue so it might require reasonable amount of work to implement. How it compares to same-sex marriage, only Paradox can say, but BlackNinja seemed to mention it was not that much work compared to other things. If you want to know if it was either too complicated or there was some other reason why it was not in patch 1.4, only they can clarify it, if they wish. For people complaining about feature depth is more of a implementation criticism; I was only responding to historicity and development time. Either way for the culture-change feature in particular, as is understandable now from the previous dev-diaries, you can use it either historically or ahistorically so it being deep or not or how often it'll be used makes no difference for historicity. Same-sex marriage can only be used ahistorically by most accounts here, yet several other things in the game can also; a cannibalism kingdom even if with a lot of depth would not be historical. But almost nowhere in these threads where same-sex marriage comes up have I seen "this RC dlc is so ahistorical you can make whatever crazy culture, get the hairsack of the pope as an artifact, have a nudist court, and also same-sex marriage lol". It's more like: "GRRRRR same-sex marriage AHISTORICAL, why have ahistorical things in my game??? These STUPID dev diaries that ONLY talk about same-sex marriages and NO OTHER FEATURES that took time to develop!!!! Gonna make my HISTORICAL nudistic incestual CANNIBAL KINGDOM just to MURDER ALL who have same-sex accepted!!!!!". Still, from what I saw at least the culture-changing feature seems to be one of the most anticipated features of RC. As an example (anecdotal sure, but there are plenty around the forum), even a very historically focused and strict player like Torredebelem we can see in his first post on this thread he is looking forward to it. If people are indeed complaining that much about the development time of RC, then it's indeed good to see some consistency. But even still there seems to be a difference in the level of opposition to the development time of what is a minor feature (even when it was just a modding improvement) compared to what is pretty much the main feature of the RC DLC. I made it up? Let me quote his last two paragraphs here and explain what I understood: I said: "The context of his post is not that people "only complain about same-sex marriage", it's that people keep complaining about it with double standards" He says in that first paragraph that nobody is complaining about the historicity and development time of ahistorical features of RC besides same-sex marriage. And on the last he says that same-sex marriage is singled out (singled out as in argued against with the same arguments). On the last sentence he frustratedly doubts that these are the real reasonings for the opposition because he thinks they have double standards. To me at least, that is the context, not just that "which simply talks about gay marriage being singled out for complaints, period". If you understood that differently, then I guess you should just ask him more clarification or wait for him to respond directly if he wants to. I think at this point we are just getting in circles; I don't even know if I have anything else relevant to add.

## Reply 167 — participant_081 · 2022-01-29 · post-28043463

also you can easily inherit entire kingdoms or empires for your children as a count or duke simply by abusing the ai's terrible marriage acceptance behaviour lets say there is an emperor, he has a son, who is heir to the empire, and that son has a son. The emperor does not let you matrilineally marry his son because that is his primary heir and doing so will just kick his dynasty off the throne. But he will let you marry the 2nd in line to the throne, his grandson because he is not directly the heir and so the AI does not factor this is in, which it did within ck2, so within 100 years your dynasty would be the powerhouse by doing nothing but marrying someones grandson because they're too stupid to check the line of succession

## Reply 168 — participant_033 · 2022-01-29 · post-28043509

<!-- artifact:quote:start -->
> christisking1992 said: my question wasn't "why is it being added" my question was "why is it being added when the game is so barebones and both gameplay and rp are repetitive and unenjoyable after a few playthroughs" Grommile. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> blackninja9939 said: reworking some code and script to enable gay marriage is infinitely less time than any of the reworks you proposed. Click to expand...
<!-- artifact:quote:end -->
Even that has been answered—by the dev who wrote this diary. Simply put, because it was a much-requested feature that they were able to put in at this time. Quoting from post#114 again, To reiterate his final point in that post, this dev diary announced the following features: in-game court editor same-sex marriage scripted widgets value breakdowns event and localization debug buttons new console commands modifiers everywhere Why, out of these seven features, do you single out only one? The one that’s been asked for the most, as far as I know? Edit: one that adds rp possibilities, too! I’ll add here, that several posters have implied that only LGBQT+ players want or will use this feature. I am not LGBTQ+, but I will happily rp with this; I’m looking forwards to it. I’m expecting it to make for some interesting succession scenarios and stories!

## Reply 169 — participant_082 · 2022-01-31 · post-28045833

I'm relatively new to Paradox games. Stellaris got me hooked. I'm obsessed. Crusader King III has been on my Wishlist for weeks. Thanks to the Steam sale, I finally found the budget to buy the game yesterday. And I'm loving it! I played for almost eight hours straight. While playing, I was hoping that my bisexual Iberian King can seduce one of those Viking Warlords of the north. I was disappointed that I couldn't. Then I saw this Dev Diary. Let me tell you: I. Cannot. Wait. I'm excited for King Arnau Miro Ponc de Minerva to rule the land and sea with his Viking, Irish, and Byzantine husbands.

## Reply 170 — participant_035 · 2022-01-31 · post-28046591

<!-- artifact:quote:start -->
> thevirgo said: While playing, I was hoping that my bisexual Iberian King can seduce one of those Viking Warlords of the north. I was disappointed that I couldn't. Click to expand...
<!-- artifact:quote:end -->
It's hard, but if you can find a bisexual or gay Viking Warlord, the world is your oyster.

## Reply 171 — participant_072 · 2022-01-31 · post-28046928

<!-- artifact:quote:start -->
> DreadLindwyrm said: It's hard, but if you can find a bisexual or gay Viking Warlord, the world is your oyster Oysteinn. Click to expand...
<!-- artifact:quote:end -->
FTFY

## Reply 172 — participant_082 · 2022-01-31 · post-28046963

<!-- artifact:quote:start -->
> DreadLindwyrm said: It's hard, but if you can find a bisexual or gay Viking Warlord, the world is your oyster. Click to expand...
<!-- artifact:quote:end -->
With that strong naval tradition, there's bound to be one or two, right? If it proves difficult, then that, my friend, will be my King's quest. The goddess Frigg will light the way.

## Reply 173 — participant_083 · 2022-02-03 · post-28052557

a lot of really depressing posts in this thread so i just wanted to mention i think the same sex marriage implementation owns. For a game where part of the fun of it is shaping medieval society according to your own modern ideals (or contrary to them, or even completely arbitrarily), this is a big deal for making more varied fantasies possible.

## Reply 174 — participant_007 · 2022-02-03 · post-28052596

I think the reason why same sex marriage is debated hotly in this diary is just a misunderstanding between devs and customers. As far I remember correctly is that one patch made same sex marriages impossible to mod. This made some angry even accusing paradox to be homophobic. Now they braught that back as a game rule. This made some angry again because of the delay, and that game rule alone appears so isolated and random they couldn't understand why devs are bringing that up so suddenly.

## Reply 175 — participant_084 · 2022-02-04 · post-28055291

<!-- artifact:quote:start -->
> JasonSTGer said: I think the reason why same sex marriage is debated hotly in this diary is just a misunderstanding between devs and customers. As far I remember correctly is that one patch made same sex marriages impossible to mod. This made some angry even accusing paradox to be homophobic. Now they braught that back as a game rule. This made some angry again because of the delay, and that game rule alone appears so isolated and random they couldn't understand why devs are bringing that up so suddenly. Click to expand...
<!-- artifact:quote:end -->
Wow, this thread does not disappoint in a lot of sad ways... I think it's awesome that the Devs implemented the same-sex marriage in the way the diary describes, way to go <3 You are in fact not remembering correctly. A patch broke some mods regarding same-sex concubines. There is no misunderstanding. Same-sex marriage mods were never possible in CK3 because of the way the game was coded. These changes have been hugely requested by the community and there is a very long thread about it here on the forum. Eventually, the devs committed to making those changes and they were supposed to come up with the Royal Court patch, which is why they are talking about it in the modding-focused dev diary. It is neither random nor sudden but anticipated and from what I saw in the original thread about these changes, it's no surprise to see sad and bigoted comments here. If someone was not interested in a feature like this in the first place, maybe they don't see the reason why it is mentioned here so in-depth but that is not an excuse to be a jerk about it.

## Reply 176 — participant_085 · 2022-02-08 · post-28062055

<!-- artifact:quote:start -->
> blackninja9939 said: Added console command "bypass_requirements" (alias "bypass") that lets you do decisions, interactions, schemes, laws, and title creation despite the requirements not being met Click to expand...
<!-- artifact:quote:end -->
Does this console command allow us to choose any tradition when diverging our culture? If not, is there a code that allows absolute freedom in choosing traditions? Or is this simply achieved by the prestige cheat, and you can access any tradition at exorbitant cost?

## Reply 177 — participant_062 · 2022-02-09 · post-28065662

<!-- artifact:quote:start -->
> blackninja9939 said: Well thankfully for all of us you aren't in charge of how we spend our time! Click to expand...
<!-- artifact:quote:end -->
Well thankfully for the actual "us", our shared community that is, your players are still very capable of accurately evaluating your decisions on what to and what not to spend your valued time on, at least judging by the user review score on steam that is

## Reply 178 — participant_035 · 2022-02-09 · post-28065768

<!-- artifact:quote:start -->
> Draky said: Well thankfully for the actual "us", our shared community that is, your players are still very capable of accurately evaluating your decisions on what to and what not to spend your valued time on, at least judging by the user review score on steam that is Click to expand...
<!-- artifact:quote:end -->
Unfortunately you don't speak for the universal "us". I like the DLC and accompanying patch since they feel like they need to be considered together, and although it's not entirely what I'd have chosen to go with first, I'm getting to grips with it. And most of the reviews I've read so far don't even relate to the content as such. It's pretty much all complaining about price point and time.

## Reply 179 — participant_082 · 2022-02-10 · post-28070315

One would think that being a gay guy living in a mostly conservative country that I would be used to casual homophobia but it still feels like a pinch in the heart to read some of the comments about this patch, especially the ones pertaining to same-sex game options. For me, playing CK3 and other similar games is like a dream fulfillment where I can shape history based on how I wish it was. English is my third language and I can't seem to find the right combination of words to emphasize how incredible and empowering it is to be able to play a game where it is possible to play a king who can marry a man and have a court full of both queer and straight knights and vassals. There's a sense of amusement and healing to be able to play a gay king who has the approval of both his religion and culture. In my case, it provides a good escape away from the oppressiveness of the current state of reality for queer people like myself. And this is why it sucks to read some of the comments minimizing the value of the same-sex game options included in this patch. It's painful to see that people who love the same game that I do be so hostile and dismissive of a game option that means a lot to people like me. The comments saying that the devs should've put these game options to the bottom of the list are so depressingly similar to the rhetoric of the people against any LGBTQIA+ rights. It is just another disheartening way for them to trivialize and devalue over and over and over again, in many ways, the needs and wants of queer folks like me. Ooooof. Writing that last part just made me all of a sudden feel so little and sad. My original goal when I opened the forums was to just post that I really enjoyed the patch and played all afternoon yesterday. So that's the happy note I'll just end this.

## Reply 180 — participant_086 · 2022-02-11 · post-28073130

Instasiege console command does not work also ToggleShowAllKillers also doesnt work

## Reply 181 — participant_087 · 2022-02-14 · post-28079115

<!-- artifact:quote:start -->
> Added console command Ironman.ToggleIgnore. When ignored, saves will act as if they're not ironman, including that when you hit save it'll result in a non-ironman save. This can be toggled during gameplay Click to expand...
<!-- artifact:quote:end -->
Hey, so, quick question: Does this mean that this particular console code is available during Ironman gameplay? And if so, can it be used to de-Ironman a game in progress? (like if I've finished an Achievement run and just want to kick back and have fun with the save?)

