---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1580680/"
forum_thread_id: 1580680
content_type: reply_thread
parent_dd_file: dd_126_2023-05-02_modding-activities.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 126
title: "Dev Diary #126 - Modding Activities"
dd_date: 2023-05-02
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 3
reply_count: 42
participant_count: 33
reply_date_first: 2023-05-02
reply_date_last: 2023-05-20
body_word_count: 2308
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

# Reply thread — Dev Diary #126 - Modding Activities

*42 replies from 33 participants across 3 pages*

## Reply 1 — participant_001 · 2023-05-02 · post-28910546

Alright looks good! Lets go May 11th!

## Reply 2 — participant_002 · 2023-05-02 · post-28910551

- Custom loc can now have the "all" type which lets it match to any scope type. That's one of the biggest changes for me personally. Custom entities - any modded "thing" that's not a variant of an in-game thing like schools, knightly orders, offmap Mesoamerican city-states - can now properly have their own naming logic without so much duplication or awkwardly scoping from a relevant title or character.

## Reply 3 — participant_003 · 2023-05-02 · post-28910587

<!-- artifact:quote:start -->
> - Adds the hostile_county_attrition_raiding to modify the hostile county attrition of raiding armies. Will apply from both commanders and owners of armies. This IGNORES the regular lower limit of 10%, such that hostile county attrition for raiding armies can be reduced to 0. Go forth, land vikings! Pillage! Rule! Click to expand...
<!-- artifact:quote:end -->
Excellent. I always have the urge to raid Jerusalem and other landlocked locations of interest (when I have the manpower), but the attrition hits like a truck. Now I can dive even further into hostile territory in the reckless pursuit of shiny artifacts and less shiny but no less collectable nobles.

## Reply 4 — participant_004 · 2023-05-02 · post-28910588

Very nice that every aspect of the activity can be modded. Some talented modders will definitely do very creative things with this. As one of the people for whom these lines of codes could as well have been some sort of secret language, I'm a tiny bit disappointed we didn't see some achievements or some titbits like new loading screen art. But I guess, we don't have to wait much longer anymore. As always, thanks for your hard work and I'm very hyped for May 11th!

## Reply 5 — participant_005 · 2023-05-02 · post-28910624

Very nice. So as the modding is mostly the second to Last Dev Diary I assume the Patch Notes will be the last one before the launch?

## Reply 6 — participant_006 · 2023-05-02 · post-28910631

If I am reading this correctly, then I can now just save a trait in a scope and check if a character has an opposing trait to that? If so, then this will make my work *a lot* easier, because I don't need a giant table of all the personality traits and their opposites anymore when trying to give a character a new personality trait. Other interesting things that I would like to save in this way: -> Events. Right now, I just give the event-id as a parameter to a scripted effect and do "trigger_event = <namespace>.$ID$" inside it. This gets the job done, but if I had the choice, I would like to like to have events in scopes. -> Relations. I don't know if making it into a scope is the best way to go about it, but I would like to attach data to relations. If possible, I would also like a performant way to get a list of characters who have a one-sided relation with a particular character, specifically "Who has crush on this character?". I would also like to reiterate a feature request for officially supporting single event replacement. If would help a lot with compatibility between different event- and bugfix-mods.

## Reply 7 — participant_007 · 2023-05-02 · post-28910651

Good to know. Thanks for the dev diary.

## Reply 8 — participant_008 · 2023-05-02 · post-28910665

<!-- artifact:quote:start -->
> - Per modder request, replaced almost all instances of has_government with government_has_flag (and added relevant flags to each government type) to allow for easy hooking in of additional government types to vanilla content & systems, as well as better mod interoperability Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> - `set_location` effect now Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> now Click to expand...
<!-- artifact:quote:end -->
Yes yes yes! But please do the same with faith doctrines. I tried to split gender equality doctrine into separate doctrines for council, titles and so on, but found that you use has_doctrine everywhere instead of has_doctrine_parameter. And this doctrine parameters don't even work (for me at least): Code: men_can_have_multiple_spouses = yes men_can_have_consorts = yes women_can_have_multiple_spouses = yes women_can_have_consorts = yes Was there such an effect before? Also when will we get full language and feature specification? Wiki is incomplete, .info files feel like they are just sticknotes for Paradox programmers who already know how the game works. Would be nice to have typed parameters for scripted effects and triggers, and also powerful string and date manipulation effects similar to functions found in Javascript or Python.

## Reply 9 — participant_009 · 2023-05-02 · post-28910710

This is a great DD for modders. Also, please do one more thing. Can't you add a trigger to check if other mods are loaded? Is it possible to create a trigger that checks the mod name (or ID), for example "loaded_mod = { Elder Kings 2 }" ? I've always struggled with compatibility when I was making some mods and wish there was a trigger like this.

## Reply 10 — participant_010 · 2023-05-02 · post-28910760

After you fed us the biggest, meanest and most amazing DD's over weeks, today feels like an appetizer.

## Reply 11 — participant_008 · 2023-05-02 · post-28910771

<!-- artifact:quote:start -->
> I’d love to know what types you’d like added as scopes Click to expand...
<!-- artifact:quote:end -->
Marriages. I really want to mod them that is why I ask about marriages in every DD. I don't know how grand weddings are implemented but I would like to see something like: Code: create_marriage = { root = <character> root_matchmaker = <character> spouse = <character> spouse_matchmaker = <character> ... } random_marriage = { limit = { phase = betrothal } save_scope_as = marriage } scope:marriage ?= { confirm = yes # from now on only "divorce" effect can be used cancel = yes # no "former spouse" status as you have with "divorce = yes" cancel = { reason = <reason> } set_date = <date> # new date set_date = { date = <date> reason = <reason> } delay_for = { years = <number> months = <number> days = <number> reason = <reason> } } Of cource there can probably be race conditions when two events try to modify the same marriage. It should support marriages where characters marry multiple characters at once.

## Reply 12 — participant_011 · 2023-05-02 · post-28910783

One thing I'd like to see is for it to be possible for religions to have different virtues and sins for the sexes.

## Reply 13 — participant_008 · 2023-05-02 · post-28910799

<!-- artifact:quote:start -->
> CorneliusBottomly said: One thing I'd like to see is for it to be possible for religions to have different virtues and sins for the sexes. Click to expand...
<!-- artifact:quote:end -->
I believe there will be update and DLC for religion one day. With saints, pantheons, clerical hierarchy and other things.

## Reply 14 — participant_012 · 2023-05-02 · post-28910811

<!-- artifact:quote:start -->
> rasuuru said: I believe there will be update and DLC for religion one day. With saints, pantheons, clerical hierarchy and other things. Click to expand...
<!-- artifact:quote:end -->
And Gregorian reform! (with religious system before/after...)

## Reply 15 — participant_013 · 2023-05-02 · post-28910819

I have no idea what any of this means...but I like it.

## Reply 16 — participant_014 · 2023-05-02 · post-28910928

Please add the name of the game to the dev diary titles again. That was a really neat QoL feature for the forum main page.

## Reply 17 — participant_015 · 2023-05-02 · post-28910945

Looks great and flexible. I asked a question about this on the tournaments diary but it ended sandwiched between two dev responses so I think it could have been buried. Would it be possible to set certain events for tournaments or activities to specific terrain. Such as rowing or climbing in tournaments for coastal or mountain terrain or fishing/whaling for a hunt activity on coastal or sea tiles?

## Reply 18 — participant_016 · 2023-05-02 · post-28910953

I love modding Dev Diaries I never read them but them being posted means the patchnotes are coming soon

## Reply 19 — participant_017 · 2023-05-02 · post-28911125

Any news on achievement compatibility with (cosmetic) mods?

## Reply 20 — participant_018 · 2023-05-02 · post-28911263

I'm sure lots of important stuff was said in this dev diary. I just held my eyes and said lalalalalala... Thanks to the modders who do what they do!

## Reply 21 — participant_019 · 2023-05-02 · post-28911322

As usual with the modding DDs there's nothing for me, but I'm glad the game is as mod friendly as it is. I hope all the people whose eyes don't glaze over when they see code are really happy

## Reply 22 — participant_020 · 2023-05-02 · post-28911340

There are still 10 days before the release of the DLC, any news about new achievements?

## Reply 23 — participant_021 · 2023-05-02 · post-28911466

Can a leveled trait be configured so that XP degrades in reverse? That is: XP increases over time, up to a maximum?

## Reply 24 — participant_022 · 2023-05-02 · post-28911488

<!-- artifact:quote:start -->
> For example, in a Tour the final phase is “Journey Home” is predefined and has a scripted selection of always taking you to your capital province, so you return home. Click to expand...
<!-- artifact:quote:end -->
I can't escape the Software Engineer that I am. I noticed something reading the blog: Question: Since the Capital province can change for various reasons (loosing territory in a war, succession, or just changing it), what happens if, while traveling back to your Capital province, the location changes? [I'm hoping the answer is "yes, we thought of that, it will never definitely probably never OOS..."]

## Reply 25 — participant_023 · 2023-05-02 · post-28911561

<!-- artifact:quote:start -->
> rasuuru said: Yes yes yes! But please do the same with faith doctrines. I tried to split gender equality doctrine into separate doctrines for council, titles and so on, but found that you use has_doctrine everywhere instead of has_doctrine_parameter. Click to expand...
<!-- artifact:quote:end -->
I want to second this. My Celebrate Crimes mod would become much more compatible if I didn't have to overwrite a lot of events and other scripts that use has_doctrine instead of has_doctrine_parameter (not to mention makes my life easier, as there would be less files I need to check for any changes each update). Additionally it would mean new modders wouldn't copy this bad habit when creating their own mods. Also would be nice if there was a way to overwrite a single event without having to overwrite the entire file. Edit: see @rasuuru 's response below

## Reply 26 — participant_008 · 2023-05-02 · post-28911586

<!-- artifact:quote:start -->
> pengoyo said: Also would be nice if there was a way to overwrite a single event without having to overwrite the entire file. Click to expand...
<!-- artifact:quote:end -->
There is. You just define new event with the same name within the namespace with the same name. For example: Code: # 00_vanilla_events.txt namespace = vanilla vanilla.0001 = { # vanilla code } vanilla.0002 = { # vanilla code } Code: # my_events.txt namespace = vanilla vanilla.0001 = { # my code } You can also override scripted effects, triggers and many other things (like defines, cultures, religions, maa etc.): Code: # 00_vanilla_effects.txt vanilla_effect_1 = { # vanilla code } vanilla_effect_2 = { # vanilla code } Code: # my_effects.txt vanilla_effect_1 = { # my code }

## Reply 27 — participant_023 · 2023-05-02 · post-28911600

<!-- artifact:quote:start -->
> rasuuru said: There is. You just define new event with the same name within the namespace with the same name. For example: Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> rasuuru said: You can also override scripted effects, triggers and I guess many other things: Click to expand...
<!-- artifact:quote:end -->
I swear I tried that a while ago. But thanks , I'll give it another try Yeah, I already make heavy use of this, but thanks anyways Edit: word

## Reply 28 — participant_024 · 2023-05-03 · post-28912560

<!-- artifact:quote:start -->
> powerofvoid said: Can a leveled trait be configured so that XP degrades in reverse? That is: XP increases over time, up to a maximum? Click to expand...
<!-- artifact:quote:end -->
No. This is currently not supported.

## Reply 29 — participant_025 · 2023-05-03 · post-28912723

<!-- artifact:quote:start -->
> So modders reading this: I’d love to know what types you’d like added as scopes and what triggers and effects that take database keys you’d like to see take scopes. I’ve already got traits done for a future patch, so I am interested in others I can do! Click to expand...
<!-- artifact:quote:end -->
Idk, maybe you already did it, since buildings got update, but just in case. It would be cool to have things like Code: every_building = { limit = { level_building = 1} upgrade_level_by = 1 } etc And also not about scopes, but about buildings still, we need triggered names for bulidings.

## Reply 30 — participant_026 · 2023-05-03 · post-28912732

<!-- artifact:quote:start -->
> Asterios_III said: This is a great DD for modders. Also, please do one more thing. Can't you add a trigger to check if other mods are loaded? Is it possible to create a trigger that checks the mod name (or ID), for example "loaded_mod = { Elder Kings 2 }" ? I've always struggled with compatibility when I was making some mods and wish there was a trigger like this. Click to expand...
<!-- artifact:quote:end -->
That is unfortunately easier said than done, different players in MP can have different mods loaded so that would be a very quick out of sync

## Reply 31 — participant_023 · 2023-05-03 · post-28912804

<!-- artifact:quote:start -->
> Asterios_III said: Also, please do one more thing. Can't you add a trigger to check if other mods are loaded? Is it possible to create a trigger that checks the mod name (or ID), for example "loaded_mod = { Elder Kings 2 }" ? I've always struggled with compatibility when I was making some mods and wish there was a trigger like this. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> blackninja9939 said: That is unfortunately easier said than done, different players in MP can have different mods loaded so that would be a very quick out of sync Click to expand...
<!-- artifact:quote:end -->
One work around is to have the mod on game start create a global variable that can be checked for by other mods. I use this to keep my Celebrate Crimes and Adoption Options mods compatible as they both try to overwrite the same files. Unfortunately this method relies on modders putting these global variables in and doesn't work with mods added partway through a campaign. Could make it so this check for other mods only works on mods that change the check sum. Such mods would have to be shared in MP anyways

## Reply 32 — participant_027 · 2023-05-03 · post-28913093

A little tangential, but would it be possible for the game to tell me my checksum before loading into it? My PC and my mate's takes a long time to load the game and it's a little annoying having waited for the game to load to realise you have to close it and reload it because the checksum isn't the same.

## Reply 33 — participant_028 · 2023-05-03 · post-28913264

Can we have XP degradation enabled via game rule?

## Reply 34 — participant_012 · 2023-05-03 · post-28913293

<!-- artifact:quote:start -->
> boorkie said: Can we have XP degradation enabled via game rule? Click to expand...
<!-- artifact:quote:end -->
I think not...

## Reply 35 — participant_028 · 2023-05-03 · post-28913337

<!-- artifact:quote:start -->
> Duzgun said: I think not... Click to expand...
<!-- artifact:quote:end -->
The answer you've quoted is about modding xp to degrade into positive rather than towards a 0 value My question is about enabling degrading as it is via a game rule so I can play with it enabled in ironman without mods

## Reply 36 — participant_012 · 2023-05-03 · post-28913359

<!-- artifact:quote:start -->
> boorkie said: The answer you've quoted is about modding xp to degrade into positive rather than towards a 0 value My question is about enabling degrading as it is via a game rule so I can play in ironman without mods Click to expand...
<!-- artifact:quote:end -->
You are right, sorry for misunderstanding.

## Reply 37 — participant_029 · 2023-05-03 · post-28913841

This might be off topic, but I have a question about some of the code used/shown in the dev diary, is: Code: highest_held_title_tier = More or less efficient performance wise than: Code: primary_title.tier = Or are they basically the same regarding performance? I always felt that having to go through all titles to see which one was the highest and then checking the tier would have a higher drawback/time consumption than just going directly to their primary and scoping to the tier but I don't really know.

## Reply 38 — participant_030 · 2023-05-04 · post-28914625

Hi, I don't speak English and I'm using google translator, I think it's necessary to specify (I'll try to be clear). I've been thinking for a long time that it's hard to believe that there is less content in ck3 than in its predecessor. At least in specific aspects. I think having fewer game rules takes things away from the base game, and that's annoying. I understand that they want to improve them for ck3 (for example, the nomade government), but in the meantime they should be available so that they can improve later. in order of priority... is it too much to ask for more game rules without having to resort to a mod? Being able to configure and randomize everything allows you to enjoy unique games. That allows you not to get bored quickly and get desperate for new content. In ck2 you had various things to do and now you don't. I don't expect to get an answer, nor do I think it's the place for this comment. I just leave it. It can be said that I do not ask for more content, I only ask for what was there before.

## Reply 39 — participant_031 · 2023-05-04 · post-28916193

<!-- artifact:quote:start -->
> herniluter said: Hi, I don't speak English and I'm using google translator, I think it's necessary to specify (I'll try to be clear). I've been thinking for a long time that it's hard to believe that there is less content in ck3 than in its predecessor. At least in specific aspects. I think having fewer game rules takes things away from the base game, and that's annoying. I understand that they want to improve them for ck3 (for example, the nomade government), but in the meantime they should be available so that they can improve later. in order of priority... is it too much to ask for more game rules without having to resort to a mod? Being able to configure and randomize everything allows you to enjoy unique games. That allows you not to get bored quickly and get desperate for new content. In ck2 you had various things to do and now you don't. I don't expect to get an answer, nor do I think it's the place for this comment. I just leave it. It can be said that I do not ask for more content, I only ask for what was there before. Click to expand...
<!-- artifact:quote:end -->
Having a lot of game rules can make it difficult to make the game balanced for people who use all of them as compared to those who leave all of them at default - and as compared to those who only change a subset of rules. If you have 4 rules, each of which has two options you have 16 different scenarios to test. If you have 30 rules, each of which has three options you have 27 000 different scenarios to test (although some may have no game play effect, like setting all titles to use Baron/Count/Duke/King/Emperor, or setting all cultures to use the territory titles, rather than dynastic naming - and thus making "Andalusia" be named that instead of "Ummayad"). It creates a gradual build up of more and more different situations that have to be tested, and potentially makes it harder to code in other things that the game will rely on being available if a feature is to be referenced by a later DLC.

## Reply 40 — participant_013 · 2023-05-04 · post-28917140

<!-- artifact:quote:start -->
> DreadLindwyrm said: Having a lot of game rules can make it difficult to make the game balanced for people who use all of them as compared to those who leave all of them at default - and as compared to those who only change a subset of rules. If you have 4 rules, each of which has two options you have 16 different scenarios to test. If you have 30 rules, each of which has three options you have 27 000 different scenarios to test (although some may have no game play effect, like setting all titles to use Baron/Count/Duke/King/Emperor, or setting all cultures to use the territory titles, rather than dynastic naming - and thus making "Andalusia" be named that instead of "Ummayad"). It creates a gradual build up of more and more different situations that have to be tested, and potentially makes it harder to code in other things that the game will rely on being available if a feature is to be referenced by a later DLC. Click to expand...
<!-- artifact:quote:end -->
This. Game rules are definitely a great innovation, but if they get overused they could make the game harder and harder to balance, and we end up with an EU IV situation where the devs have to have like 5-6 different balancing scenarios.

## Reply 41 — participant_032 · 2023-05-06 · post-28920061

Very exciting

## Reply 42 — participant_033 · 2023-05-20 · post-28954828

<!-- artifact:quote:start -->
> rasuuru said: There is. You just define new event with the same name within the namespace with the same name. For example: Code: # 00_vanilla_events.txt namespace = vanilla vanilla.0001 = { # vanilla code } vanilla.0002 = { # vanilla code } Code: # my_events.txt namespace = vanilla vanilla.0001 = { # my code } Click to expand...
<!-- artifact:quote:end -->
Are you certain about this? Doing this throws errors in error.log and doesn't seem to consistently replace the event. Example of error: Code: [15:58:14][jomini_eventmanager.cpp:423]: Duplicated event ID 'combat_event.1001' found. New Location: ' file: events/war_events/combat_events.txt line: 586', Previous Location: ' file: events/war_events/combat_events.txt line: 586' For most scripted effects and triggers and such you can replace single entries with no fuss, but events seem different. (Yes, I know the error.log claims the duplicates are in the same file on the same line, you're going to have to trust me that's not the case, my modded event is in a differently named file in a different location). Thus, for events specifically, I've always had to resort to overwriting the entire event file, which is less than ideal.

