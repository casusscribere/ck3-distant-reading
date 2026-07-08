---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1397140/"
forum_thread_id: 1397140
content_type: reply_thread
parent_dd_file: dd_030_2020-06-09_crusader-kings-3-dev-diary-30-event-scri.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 30
title: "Crusader Kings 3 Dev Diary #30 - Event Scripting"
dd_date: 2020-06-09
expansion: Base game
patch: Crusader Kings III
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 5
reply_count: 88
participant_count: 59
reply_date_first: 2020-06-09
reply_date_last: 2020-09-05
body_word_count: 5741
inline_image_count: 0
quoted_span_count: 65
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Crusader Kings 3 Dev Diary #30 - Event Scripting

*88 replies from 59 participants across 5 pages*

## Reply 1 — participant_001 · 2020-06-09 · post-26642721

*(no text body — reaction-only or media-only post)*

## Reply 2 — participant_002 · 2020-06-09 · post-26642730

<!-- artifact:quote:start -->
> the two angriest and orneriest from amongst them Click to expand...
<!-- artifact:quote:end -->
well you found me...

## Reply 3 — participant_003 · 2020-06-09 · post-26642732

The best development diary thus far

## Reply 4 — participant_004 · 2020-06-09 · post-26642735

Helpful for modders I guess, but not much for the rest of us who hunger for CK3 info.

## Reply 5 — participant_005 · 2020-06-09 · post-26642741

DOES THIS MEAN WE STILL HAVE BEARS IN CK3？

## Reply 6 — participant_006 · 2020-06-09 · post-26642745

Very glad of these improvements on the scripts.This will make CK3 more moddable than CK2 and easier.Keep up the good work.

## Reply 7 — participant_007 · 2020-06-09 · post-26642758

The thing I'm most excited about is that French culture is referred to as french, and not frankish

## Reply 8 — participant_008 · 2020-06-09 · post-26642766

I stopped reading after secret_bear_people

## Reply 9 — participant_009 · 2020-06-09 · post-26642768

This is really cool. Question: do we have variables in ck3 to work with

## Reply 10 — participant_010 · 2020-06-09 · post-26642772

<!-- artifact:quote:start -->
> prismaticmarcus said: Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> treb said: well you found me... Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Veldmaarschalk said: The best development diary thus far Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> magriboy0750 said: Very glad of these improvements on the scripts.This will make CK3 more moddable than CK2 and easier.Keep up the good work. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Atalvyr said: Helpful for modders I guess, but not much for the rest of us who hunger for CK3 info. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Gandalf_The_Black said: The thing I'm most excited about is that French culture is referred to as french, and not frankish Click to expand...
<!-- artifact:quote:end -->
<3 You're not wrong, though I hope it's still interesting for people who like to see how the sausage is made, but modders deserve love too! ^^ Well, I'm happy that ye're happy.

## Reply 11 — participant_011 · 2020-06-09 · post-26642774

So if, in the future, you(or modders) would like to utilize one "minor inline trigger" for another seperate script. Would it be best to referense to that file, create an identical inline trigger or edit it out from the original and move the trigger to an shared file?

## Reply 12 — participant_012 · 2020-06-09 · post-26642781

<!-- artifact:quote:start -->
> Naggym said: So if, in the future, you(or modders) would like to utilize one "minor inline trigger" for another seperate script. Would it be best to referense to that file, create an identical inline trigger or edit it out from the original and move the trigger to an shared file? Click to expand...
<!-- artifact:quote:end -->
Assuming the new use case is in a separate file, you'd move the trigger to a shared scripted trigger database (for maximum Script Hygiene).

## Reply 13 — participant_010 · 2020-06-09 · post-26642787

<!-- artifact:quote:start -->
> vyshan said: This is really cool. Question: do we have variables in ck3 to work with Click to expand...
<!-- artifact:quote:end -->
Yes! We have a set_variable function with a fairly broad amount of utility, which can act as an ordinary variable (taking value from a number of places), a boolean, a flag, or a few other sundry options.

## Reply 14 — participant_013 · 2020-06-09 · post-26642824

Is long-term gameplay now viable for players with low spec laptops? Ck2 runs well the first hundred years but after that it runs as well as a hundred year old horse. Probably has something to do with the amount of courtiers. Will the game have the same performance at the beginning of the game until the very end?

## Reply 15 — participant_009 · 2020-06-09 · post-26642832

<!-- artifact:quote:start -->
> LordMune said: Assuming the new use case is in a separate file, you'd move the trigger to a shared scripted trigger database (for maximum Script Hygiene). Click to expand...
<!-- artifact:quote:end -->
Databases? Does this mean that CK3 has actual legit database connections? or am I just misunderstanding things and you meant to refer to the Commons Folder where scripted triggers are stored now?

## Reply 16 — participant_014 · 2020-06-09 · post-26642836

Cool, though I hope error logging is improved, in CK2 crash's are bascilly impossible to diagnose by modders without trial and error as the error logs are basically completely useless and never give any hint as to what area the error occurred in.

## Reply 17 — participant_015 · 2020-06-09 · post-26642844

This is all very cool and I look forward to seeing what cool things you have used it for in the game! Also can't wait to see what modders come up with, and I imagine this will make it easier to add more and more interesting events in ongoing development/dlc.

## Reply 18 — participant_016 · 2020-06-09 · post-26642847

<!-- artifact:quote:start -->
> Gandalf_The_Black said: The thing I'm most excited about is that French culture is referred to as french, and not frankish Click to expand...
<!-- artifact:quote:end -->
Wasn't this change made in CK2 already? Frankish (in Germanic group) eventually turns into French (Latin group).

## Reply 19 — participant_007 · 2020-06-09 · post-26642861

<!-- artifact:quote:start -->
> Nyrael said: Wasn't this change made in CK2 already? Frankish (in Germanic group) eventually turns into French (Latin group). Click to expand...
<!-- artifact:quote:end -->
But the id for French culture is frankish in CK2 instead of French

## Reply 20 — participant_012 · 2020-06-09 · post-26642903

<!-- artifact:quote:start -->
> vyshan said: Databases? Does this mean that CK3 has actual legit database connections? or am I just misunderstanding things and you meant to refer to the Commons Folder where scripted triggers are stored now? Click to expand...
<!-- artifact:quote:end -->
I'm afraid I just mean the plaintext files in the /common folder. They're nominally databases...

## Reply 21 — participant_010 · 2020-06-09 · post-26642923

<!-- artifact:quote:start -->
> Edith The Wisest said: Is long-term gameplay now viable for players with low spec laptops? Ck2 runs well the first hundred years but after that it runs as well as a hundred year old horse. Probably has something to do with the amount of courtiers. Will the game have the same performance at the beginning of the game until the very end? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> HandicapdHippo said: Cool, though I hope error logging is improved, in CK2 crash's are bascilly impossible to diagnose by modders without trial and error as the error logs are basically completely useless and never give any hint as to what area the error occurred in. Click to expand...
<!-- artifact:quote:end -->
Afraid I'm not really a great person to answer hardware questions. I understand the vague principles of the magic thinking rock, but its nuances are arcane to me. I like to think so! I'm unsure how much extra logging detail we'll have available at launch, but we have improved debug_log, debug_log_date, & debug_log_scopes effect commands from CK2's, so debugging is pretty customisable from a script-perspective. I've also used the debugger a lot both as QA & as a Content Designer, and I generally find it to be very helpful and precise most of the time. As ever, though, these things are a process, so we'll be adding to it as patches go on!

## Reply 22 — participant_017 · 2020-06-09 · post-26642942

Interesting diary. Can we hear modders first look opinion, how flexible new event system (in comparison with old)? Is other part of games fully moddable too? Can new 3D-models be exported and used in game (more precise question - will we see Warhammer overhauls with shyed orcs)? How it'd works with new genetic system? Or more about it in next dev diaries?

## Reply 23 — participant_018 · 2020-06-09 · post-26642946

These ordered_lists and the math will be quite nice. And the first_valid trigger is neat as well. Is there something similar for the scene background? Also, is it possible to save a list somewhere? Say I have a list of the "most important unlanded random courtiers in the world", could I reference it in different events, potentially adding "important" characters to it? Is there an "overwrite/update" functionality for events? In Ck2, when 2 mods try to access the same file to do a minor change in one line, it breaks compatiblity. Would be nice if you could specify an event with "overwrite = true", or something like that in a seperate file. And speaking of all those fancy new triggers, commands and on_actions: What are your favourite new additions when compared to CK2?

## Reply 24 — participant_019 · 2020-06-09 · post-26642975

Alright it seems that Rise To Power will be coming to CK3 after all. Great job guys I cannot wait to try them out! One question and request before release though...If there is one thing that I miss the most from coming to CK2 from Stellaris are the "Timed Flags" I.e "set_timed_country_flag" as an actual "command/effect". Are you guys going to port that feature over from Stellaris? Pleaaaaassssseeeee???? (And no those "had_flag" conditions checks dont count

## Reply 25 — participant_018 · 2020-06-09 · post-26642976

<!-- artifact:quote:start -->
> Wokeg said: Finally, options. Options behave similarly to CK2, with a minimum of one per visible event Click to expand...
<!-- artifact:quote:end -->
Wait a minute. Does that mean that they can have more than 4 options (or that the "more" option to cycle through is automatically generated)?

## Reply 26 — participant_020 · 2020-06-09 · post-26642996

<!-- artifact:quote:start -->
> arlekiness said: Interesting diary. Can we hear modders first look opinion, how flexible new event system (in comparison with old)? Click to expand...
<!-- artifact:quote:end -->
Very cool. Are events still limited to a max of 4 options? Later games aren't, so I suppose we can have more in CK2, but I'd like to be sure Hard to say without delving into it, but it seems to be more flexible than CK2. The new descriptions look a lot like custom_localization keys, and they're nice to play with so that's an improvement. Custom on_actions are very nice, I think it could replace some "tombola" systems we had in CK2 (that's what societies use to give you content). I don't know how I feel about having scripted triggers defined within the event file itself, as I much prefer to have them all within the common/scripted_triggers folder itself. But that's a personal preference. alternative_limit look a like preferred_limit, not sure exactly what the difference is however. ordered_in_list looks like it has quite a lot of potential, so that's nice. It seems that the ai_chance is much easier to play with, which is a very good improvement. Edit: Completely forgot about the first change, the event type and its id have exchanged their place. That's really cool. The event id is much more important than the event type, and so having the later more obvious than the former was a bit strange. Some changes will take some time to get used to, but overall I'm rather excited about it. So kudos Paradox!

## Reply 27 — participant_010 · 2020-06-09 · post-26643031

<!-- artifact:quote:start -->
> arlekiness said: Is other part of games fully moddable too? Can new 3D-models be exported and used in game (more precise question - will we see Warhammer overhauls with shyed orcs)? How it'd works with new genetic system? Or more about it in next dev diaries? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Lordy's said: These ordered_lists and the math will be quite nice. And the first_valid trigger is neat as well. Is there something similar for the scene background? Also, is it possible to save a list somewhere? Say I have a list of the "most important unlanded random courtiers in the world", could I reference it in different events, potentially adding "important" characters to it? Is there an "overwrite/update" functionality for events? In Ck2, when 2 mods try to access the same file to do a minor change in one line, it breaks compatiblity. Would be nice if you could specify an event with "overwrite = true", or something like that in a seperate file. And speaking of all those fancy new triggers, commands and on_actions: What are your favourite new additions when compared to CK2? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> mightnight said: Alright it seems that Rise To Power will be coming to CK3 after all. Great job guys I cannot wait to try them out! One question and request before release though...If there is one thing that I miss the most from coming to CK2 from Stellaris are the "Timed Flags". Are you guys going to port that feature over from Stellaris? Pleaaaaassssseeeee???? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Lordy's said: Wait a minute. Does that mean that they can have more than 4 options (or that the "more" option to cycle through is automatically generated)? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> LeSingeAffame said: Very cool. Are events still limited to a max of 4 options? Later games aren't, so I suppose we can have more in CK2, but I'd like to be sure ... The new descriptions look a lot like custom_localization keys, and they're nice to play with so that's an improvement. ... Some changes will take some time to get used to, but overall I'm rather excited about it. So kudos Paradox! Click to expand...
<!-- artifact:quote:end -->
I'm afraid that, for now, it is a mystery is the only answer I can give to that. There isn't currently a first_valid system for anything but triggered copy, as far as I know, I'm afraid. As for lists, certainly! We've got scripted lists (per the diary), temporary lists (existing for a single block of script), & global lists (as you're wanting here). Currently, we do not have an overwrite/update function. As for which is my favourite, gosh, difficult. I didn't get a chance to show it off this dev diary, but I think I'd have to say random_in_list is the one that I personally get the most use out of! Filter through a load of appropriate characters for an event, add them to a list, then pick a random character from that list according to a set of weights I tweak to my preference for interest. Want to grab all your vassals, courtiers, close family, then pick out the one with the most and largest claims? Boom, simple, easy, robust. Want to do the same but instead find the one that has the best murder/attempted murder secret against someone important to you? Same list, different weights, only marginally more difficult. Want to find the character in that list with the most missing body-parts and infectious diseases? Easy, doable. Lots of flexibility, and let's you put in just so much drama tailored to your personal preference. I'm afraid I've not scripted in Stellaris, particularly, I'm firmly a medieval kind of chap, but we do have specific or random time limits available on any set_variable command, which includes flag functionality et al, if that's what you mean. *WINNER!* ^^ Waiting for this one to come up. Although the "more" option is not automatically generated, we do not have a hard limit of four options, though the base title certainly prefers to remain at four options or less without a more cycle. Per my above answer, nope! No 4-option max. Certainly a valid confirmation ask! We also have custom_loc keys, for the record . Glad you like it.

## Reply 28 — participant_021 · 2020-06-09 · post-26643044

On modding wise im more intrested how much hard coding is still in game? How much room we have mod define files. This question is mostly based on CK2 define file where Define in definefile there were defined 2 modifers for divine blood. Lunatic and inbreed but there were no room to add other modifers, like weak, strong, harelip, dwarf or anything else. Also in same case alot of other modifers were limited, will it stays same way in CK3 or its avaible for full moding.

## Reply 29 — participant_022 · 2020-06-09 · post-26643065

Speaking of technical topics... Will there be any major changes to AI character behavior? Specifically, will AI characters be able to make more complex long-term judgments, such as deciding that Lord X is becoming too powerful in the realm and therefore needs to have hooks dug up against him to keep him under control?

## Reply 30 — participant_020 · 2020-06-09 · post-26643067

<!-- artifact:quote:start -->
> Wokeg said: Per my above answer, nope! No 4-option max. Certainly a valid confirmation ask! We also have custom_loc keys, for the record . Glad you like it. Click to expand...
<!-- artifact:quote:end -->
Quick question for the custom_localization! Currently the keys don't seem to be evaluated until the game is started. That means that putting a custom_loc key as the name of a trait or a title will result in the key not being localized until the game starts. It is visible in the ruler selection window for the custom titles (something like [Root.GetKing]), and for the traits in the ruler designer (something like [Root.GetCraven]). Is it still the case? It's very much an edge case but the question sprung into my mind

## Reply 31 — participant_023 · 2020-06-09 · post-26643092

Do you use a GUI of some kind to manage all these, and visualize the relationships? Or are they all hand-crafted in an editor?

## Reply 32 — participant_019 · 2020-06-09 · post-26643129

<!-- artifact:quote:start -->
> Wokeg said: I'm afraid I've not scripted in Stellaris, particularly, I'm firmly a medieval kind of chap, but we do all specific or random time limits on any set_variable command, which includes flag functionality et al, if that's what you mean. Click to expand...
<!-- artifact:quote:end -->
Yup that'll do! Thank you!

## Reply 33 — participant_018 · 2020-06-09 · post-26643148

<!-- artifact:quote:start -->
> Wokeg said: Want to find the character in that list with the most missing body-parts and infectious diseases? Easy, doable. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> y8r4G0xz3fFkXdGXyJ4V said: Do you use a GUI of some kind to manage all these, and visualize the relationships? Or are they all hand-crafted in an editor? Click to expand...
<!-- artifact:quote:end -->
I also hope that certain things are no longer hardcoded. Like the instant game over for unplayable government types, whereby they cannot be made playable by mods, and unplayable barons. Certainly a very common desire. But these list types seem really great. I remember cycle through characters with a given trait with a while loop and flags because there was no corresponding list and the trait scope only gives a random member. That was buggy as hell, so I'm very glad to see these powerful tools. Are the ai_values the same ones as in CK2? And what's their value range? I never used them in CK2 because I didn't knew what a rationality of x means. So apparently we might have another dev diary on scripted math and one on 3d and gui modding? As far as I know they only use Sublime. I've no idea how they manage to keep track of all the thousands of different event IDs, although the new name spaced event header might help a little. In an earlier dev diary about life styles there was the perk that prolongs your life for another year in case you die of old age. I wonder how that is handled in script. Is there a "death = not_today" command for the on_death on_action?

## Reply 34 — participant_024 · 2020-06-09 · post-26643199

<!-- artifact:quote:start -->
> Arona said: On modding wise im more intrested how much hard coding is still in game? How much room we have mod define files. This question is mostly based on CK2 define file where Define in definefile there were defined 2 modifers for divine blood. Lunatic and inbreed but there were no room to add other modifers, like weak, strong, harelip, dwarf or anything else. Also in same case alot of other modifers were limited, will it stays same way in CK3 or its avaible for full moding. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Lordy's said: In an earlier dev diary about life styles there was the perk that prolongs your life for another year in case you die of old age. I wonder how that is handled in script. Is there a "death = not_today" command for the on_death on_action? Click to expand...
<!-- artifact:quote:end -->
Well I mean there is still plenty of hard coded things in the sense we have a lot of compiled C++ code into the executable obviously but as the DD here mentions we've aimed at putting a lot of things in script so it can be modded, for your specific mention there of modifiers we've tried to generalise them more than before with auto registering modifiers based on database entries for some of them, those ones you mention in CK2 were just rather old ones to solve a specific use case in CK2. Its actually pretty simple, when the gods of RNG decide its time for them to pass on we trigger an on action for getting a second chance at life, that then fires an event notifying you that your time is up and then sends an event roughly a year later which does then kill you properly. Modifying the RNG to try and get it to give you an extra year and in advance know that year would be way to difficult due to the well... R for randomness RNG so this was the solution I went with to keep it simple and effective.

## Reply 35 — participant_010 · 2020-06-09 · post-26643216

<!-- artifact:quote:start -->
> Arona said: On modding wise im more intrested how much hard coding is still in game? How much room we have mod define files. This question is mostly based on CK2 define file where Define in definefile there were defined 2 modifers for divine blood. Lunatic and inbreed but there were no room to add other modifers, like weak, strong, harelip, dwarf or anything else. Also in same case alot of other modifers were limited, will it stays same way in CK3 or its avaible for full moding. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Mindel said: Speaking of technical topics... Will there be any major changes to AI character behavior? Specifically, will AI characters be able to make more complex long-term judgments, such as deciding that Lord X is becoming too powerful in the realm and therefore needs to have hooks dug up against him to keep him under control? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> LeSingeAffame said: Quick question for the custom_localization! Currently the keys don't seem to be evaluated until the game is started. That means that putting a custom_loc key as the name of a trait or a title will result in the key not being localized until the game starts. It is visible in the ruler selection window for the custom titles (something like [Root.GetKing]), and for the traits in the ruler designer (something like [Root.GetCraven]). Is it still the case? It's very much an edge case but the question sprung into my mind Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> y8r4G0xz3fFkXdGXyJ4V said: Do you use a GUI of some kind to manage all these, and visualize the relationships? Or are they all hand-crafted in an editor? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Lordy's said: Are the ai_values the same ones as in CK2? And what's their value range? I never used them in CK2 because I didn't knew what a rationality of x means. So apparently we might have another dev diary on scripted math and one on 3d and gui modding? Click to expand...
<!-- artifact:quote:end -->
Hugely sorry, but I'm afraid I'm going to have to keep mum on a lot of that for the moment, as my dev diary was only cleared to discuss events, and defines aren't one of my areas of expertise. Modifiers (character, county, house, etc.) are fully moddable, though I'm not quite sure how much of an improvement we have over CK2 in that regard, as CK2 was already fairly flexible there. There are a whole slew of new modifier effects to use, especially for new CK3 features, but as those have to be created manually by Code, I'm afraid I can't promise the Moon on that one. Afraid that's not quite my bailiwick. As a CD, I do work with the AI, but my province is mostly teaching it to use standard functionality in the short (and occasionally mid) term, so I can't really give you a decent answer. If I'm understanding you correctly, then actually, yes! We use this functionality pretty extensively, so there are a lot of traits which will have a default/fallback name, and then a customised name that changes with the circumstances (for instance, the trait that script refers to as "viking" has a default name of "Raider", but if you have the longships innovation, it changes to "Viking"). Hand-crafted in the editor, m'friend. Which editor varies according to personal taste (as long as it works), but the most common ones by far are Sublime & Notepad++. I believe we have a couple of new ones, though I think it's outside my purview to discuss which ones. The range is -100 to +100. Afraid I can make no promises on future dev diary content, just that there'll be more dev diaries.

## Reply 36 — participant_025 · 2020-06-09 · post-26643223

How moddable are on_actions? Can you mod so that events are called from a weekly pulse instead of monthly and monthly pulse instead of yearly (like a hypothetical Lion King mod, where most characters would grow up in 3 years and live for a decade or two)?

## Reply 37 — participant_020 · 2020-06-09 · post-26643230

<!-- artifact:quote:start -->
> Wokeg said: If I'm understanding you correctly, then actually, yes! We use this functionality pretty extensively, so there are a lot of traits which will have a default/fallback name, and then a customised name that changes with the circumstances (for instance, the trait that script refers to as "viking" has a default name of "Raider", but if you have the longships innovation, it changes to "Viking"). Click to expand...
<!-- artifact:quote:end -->
So if you pick the Raider trait in the RD (if there's one in CK3, I can't remember exactly) it'll show as Raider (since it's the fallback name) and not [Root.GetRaider] (that's the current behavior in CK2)? Neat!

## Reply 38 — participant_026 · 2020-06-09 · post-26643263

Not really following most of this DD, since I'm not a modder and don't do scripting. However, from what little I do now, it looks like Events in CKIII will be much more moddable and much less prone to unspeciuficed errors than they were in CKII, which is good for everyone.

## Reply 39 — participant_027 · 2020-06-09 · post-26643285

Not a dev diary that will be relevant to most people, but for modders - especially those who work a lot with events - this is a very fascinating one. The greater flexibility with, for instance, random_in_list as the equivalent of random_courtier, is appreciated. A few questions, if you don't mind (probably a lot more but this is off the top of my head and skimming through my current code for my CK2 modding work): - Is event_target still around and has there been any important changes to how it works? - Is there still a basic yearly, bi-yearly, every five years, etc. on_actions in vanilla, as well as a a startup on_actions in vanilla that will allow us to trigger events at the start of the game? - Are pre-triggers still in? - On a related vein, in CK2 a common scripting sleight of hand was to have the Pope trigger certain maintenance or narrative events since he's always around - will CK3 use a similar system or is there something in-built to take care of those kinds of situations? - Does the code for creating characters differ in CK3 from CK2 significantly, and/or has any new functionalities been added to it? Thanks again for a good dev diary and answering questions so far, it's very enlightening for us modders.

## Reply 40 — participant_024 · 2020-06-09 · post-26643337

<!-- artifact:quote:start -->
> cybrxkhan said: - Is event_target still around and has there been any important changes to how it works? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> cybrxkhan said: - Is there still a basic yearly, bi-yearly, every five years, etc. on_actions in vanilla, as well as a a startup on_actions in vanilla that will allow us to trigger events at the start of the game? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> cybrxkhan said: - Are pre-triggers still in? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> cybrxkhan said: - On a related vein, in CK2 a common scripting sleight of hand was to have the Pope trigger certain maintenance or narrative events since he's always around - will CK3 use a similar system or is there something in-built to take care of those kinds of situations? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> cybrxkhan said: - Does the code for creating characters differ in CK3 from CK2 significantly, and/or has any new functionalities been added to it? Click to expand...
<!-- artifact:quote:end -->
They are called saved scopes these days, mainly cause event target got conflated with what that means in code and script documentation, they function pretty much the same you do save_scope_as = name to save them and then scope:name to find them. We've got those sorts of pulses and startup on actions still yes No, they proved to be fairly unnecessary when you don't use mean time to happen for everything so aren't checking lots of things regularly all the time to the point that going into the script system to evaluate triggers becomes a noticeable overhead. There is a yearly_global_pulse which is fired one on Jan 1st every year and has no scope set as root or any saved scopes, that can be used as a master caller to run maintenance effects and trigger events reliably instead of needing to use a character as a dummy stand in like the Pope. There are a fair few more bells and whistles on it, mainly to make it generate better random characters in an entire culture group or inheriting a dynasty into a new house and being able to be given random traits from a list of valid ones. To make it a bit easier to generate nicer random characters more easily there is also a new database of scripted character templates so you can make something like new_warrior_character as a template and give them a list of things you want them to be able to get for example always giving them a martial education and a lifestyle trait that is military or fighting based as well as being able to specify some min-max bounds for martial skill and prowess. The rest of the character's info will be determined via defaulting to whoever employs them for things like faith or specified/overridden in the create_character invocation in script.

## Reply 41 — participant_028 · 2020-06-09 · post-26643347

I understood very little of all this but what I understood looks good, the life and history of our characters can be more entertaining and the mods will be much better done. I do not understand people who complain or who say it is useless, this affects gameplay a lot.

## Reply 42 — participant_029 · 2020-06-09 · post-26643368

I, uh, am having an increasingly hard time keeping my expectations to a reasonable level. Given the way event IDs are now defined, I wonder if something was done about the override of individual events. In CK2, this would require overriding the entire event file, with produces a lot of pointless incompatibilities and maintenance. Being able to redefine an event from scratch, by simply reusing its ID in another file, would already be a huge improvement. I have a similar question about scripted triggers/effects/scores. In CK2, all scripted blocks with the same name would be appended together by file load order, which allowed for some hacks but was just clunky and counterintuitive more often than not. Is there any change in that regard? Finally, it appears that the new inline scripted blocks are tied to files. Wouldn't it make more sense for them to be assigned to the namespace instead?

## Reply 43 — participant_030 · 2020-06-09 · post-26643383

We'll all spend countless hours playing mods and total conversions. So this Dev Diary just tells me that these mods will be even better due to the enhanced scripting. And what not. Now this excites me more than CK3 itself.

## Reply 44 — participant_020 · 2020-06-09 · post-26643384

<!-- artifact:quote:start -->
> blackninja9939 said: There is a yearly_global_pulse which is fired one on Jan 1st every year and has no scope set as root or any saved scopes, that can be used as a master caller to run maintenance effects and trigger events reliably instead of needing to use a character as a dummy stand in like the Pope. Click to expand...
<!-- artifact:quote:end -->
Thanks a lot for that!

## Reply 45 — participant_027 · 2020-06-09 · post-26643436

<!-- artifact:quote:start -->
> blackninja9939 said: They are called saved scopes these days, mainly cause event target got conflated with what that means in code and script documentation, they function pretty much the same you do save_scope_as = name to save them and then scope:name to find them. We've got those sorts of pulses and startup on actions still yes No, they proved to be fairly unnecessary when you don't use mean time to happen for everything so aren't checking lots of things regularly all the time to the point that going into the script system to evaluate triggers becomes a noticeable overhead. There is a yearly_global_pulse which is fired one on Jan 1st every year and has no scope set as root or any saved scopes, that can be used as a master caller to run maintenance effects and trigger events reliably instead of needing to use a character as a dummy stand in like the Pope. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> blackninja9939 said: There are a fair few more bells and whistles on it, mainly to make it generate better random characters in an entire culture group or inheriting a dynasty into a new house and being able to be given random traits from a list of valid ones. To make it a bit easier to generate nicer random characters more easily there is also a new database of scripted character templates so you can make something like new_warrior_character as a template and give them a list of things you want them to be able to get for example always giving them a martial education and a lifestyle trait that is military or fighting based as well as being able to specify some min-max bounds for martial skill and prowess. The rest of the character's info will be determined via defaulting to whoever employs them for things like faith or specified/overridden in the create_character invocation in script. Click to expand...
<!-- artifact:quote:end -->
THanks for the quick responses, looks all good to me! The yearly_global_pulse seems like a simple but good solution for the Pope sleight of hand. Couple follow up questions to this: - So if I understand it there won't be the CK2 system where it's create_character and then five different types of create_character for every attribute/education type (i.e. create priest, create soldier, etc.), and instead I can make a custom create_character like, for example, "new_hot_character" which will make a character that always as a minimum has traits to make them attractive? - When you say there's a database of scripted character templates, do you mean there's a unique file or folder that is focused purely on scripting new character creation templates, or this is more just a standard scripted effect? Thanks again for the response!

## Reply 46 — participant_031 · 2020-06-09 · post-26643503

Will the Pope be given more to do?: As of CK2, he only seems to Call for Crusades-something he can only do once every ten years, I think-and Excommunicate Rulers. If the Pope is given more things to do every year, he might Excommunicate less...

## Reply 47 — participant_032 · 2020-06-09 · post-26643546

Question: Can the upcoming game handle properly special letters, like Ő, Ű or č? If I remember correctly CK2 couldn't handle them.

## Reply 48 — participant_033 · 2020-06-09 · post-26643570

<!-- artifact:quote:start -->
> Wokeg said: secret_bear_people Click to expand...
<!-- artifact:quote:end -->
*(no text body — reaction-only or media-only post)*

## Reply 49 — participant_034 · 2020-06-09 · post-26643644

This, while certainly useful, is NOT the thing you should feed to the fans you are already blueballing harshly by lack of any new materials not even 3 months before release. Edit: Wow, just wow. Your hype denial is over 9000 at least.

## Reply 50 — participant_030 · 2020-06-09 · post-26643684

<!-- artifact:quote:start -->
> Vanhal said: NOT the thing you should feed to the fans you are already blueballing harshly by lack of any new materials Click to expand...
<!-- artifact:quote:end -->
Dunno this is pretty great because it reinforces the fact that modding will be expanded upon in CK3. I guess if you don't use mods its not exciting. Not sure about the lack of new materials thing though, all the dev diaries so far have been quite good. And thats coming from someone who read all the previews and watched all the videos of CK3.

## Reply 51 — participant_035 · 2020-06-09 · post-26643729

<!-- artifact:quote:start -->
> Vanhal said: This, while certainly useful, is NOT the thing you should feed to the fans you are already blueballing harshly by lack of any new materials not even 3 months before release. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> LordofLight said: Dunno this is pretty great because it reinforces the fact that modding will be expanded upon in CK3. I guess if you don't use mods its not exciting. Click to expand...
<!-- artifact:quote:end -->
This dev diary isn't just an indication of new modding features (though they are extremely exciting for the many modders and their many more players) but also a general indication of CK3's new scripting capabilities, hygiene, and performance over CK2. Exciting news for anyone interested in (script-related) performance improvements, new capabilities, ease of future bug fixing, integration of future features with existing content (I'm looking at you personal combat skill rebalancing), and the ability of both Paradox and modders to make as much quality content as possible in a given time period that will require as little revisiting in the future to be integrated with later additions. Some parts of the line-by-line might not be relevant to everyone, sure, but the gist of the information presented here is something for everyone to be excited about

## Reply 52 — participant_020 · 2020-06-09 · post-26643855

<!-- artifact:quote:start -->
> Vanhal said: This, while certainly useful, is NOT the thing you should feed to the fans you are already blueballing harshly by lack of any new materials not even 3 months before release. Click to expand...
<!-- artifact:quote:end -->
Wrong.

## Reply 53 — participant_036 · 2020-06-09 · post-26643980

Well, this is an interesting dev diary. So it is cleaner version compared to CK2. This is always nice. Good job and I am looking forward how this will pan out. It should also make modding a bit easier I guess. Maybe I should reactivate my rusty script skills to mod my wish for the three-way-split for the Soumensko faith in that I wanted. Edit: I just realized that there is no post about this on twitter? Also looked at facebook. Is the Social Media team asleep with this DD?

## Reply 54 — participant_037 · 2020-06-09 · post-26644215

<!-- artifact:quote:start -->
> Atalvyr said: Helpful for modders I guess, but not much for the rest of us who hunger for CK3 info. Click to expand...
<!-- artifact:quote:end -->
Thing is modders are extremely important to many aspects of the CK community. Those groups need to know if they will be able to transition from one game to the next.

## Reply 55 — participant_024 · 2020-06-09 · post-26644459

<!-- artifact:quote:start -->
> cybrxkhan said: - So if I understand it there won't be the CK2 system where it's create_character and then five different types of create_character for every attribute/education type (i.e. create priest, create soldier, etc.), and instead I can make a custom create_character like, for example, "new_hot_character" which will make a character that always as a minimum has traits to make them attractive? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> cybrxkhan said: - When you say there's a database of scripted character templates, do you mean there's a unique file or folder that is focused purely on scripting new character creation templates, or this is more just a standard scripted effect? Click to expand...
<!-- artifact:quote:end -->
Exactly! There is a line in the effect where you would do template = new_hot_character and that will then be the base for them Its a unique database folder, common/scripted_character_templates, where the entries made in files there have a key and then all the various values you want and can use it in the effect like I mentioned above by doing template = key_of_entry.

## Reply 56 — participant_038 · 2020-06-09 · post-26644478

<!-- artifact:quote:start -->
> However, in CK2, these scripted triggers had to be stored inside a specific folder in /common, separate from the events (and other script) that they referenced. Click to expand...
<!-- artifact:quote:end -->
Good to see This was very annoying when I wanted to edit some portrait triggers for personal use, since editing common changed checksum (whereas portrait triggers did not), thus needing a big copy operation.

## Reply 57 — participant_027 · 2020-06-09 · post-26644559

<!-- artifact:quote:start -->
> blackninja9939 said: Exactly! There is a line in the effect where you would do template = new_hot_character and that will then be the base for them Its a unique database folder, common/scripted_character_templates, where the entries made in files there have a key and then all the various values you want and can use it in the effect like I mentioned above by doing template = key_of_entry. Click to expand...
<!-- artifact:quote:end -->
Oh wow this is really, really handy, as I make quite a bit of use of create_character in CK2 currently, and while the current system works it can be clunky if you're doing more complex things with it as you probably well know. Thanks for the clarification!

## Reply 58 — participant_039 · 2020-06-09 · post-26644571

<!-- artifact:quote:start -->
> Wokeg said: View attachment 586785 Click to expand...
<!-- artifact:quote:end -->
Nice

## Reply 59 — participant_040 · 2020-06-10 · post-26644732

boring

## Reply 60 — participant_041 · 2020-06-10 · post-26644790

I noticed in the code there's character facial expressions. As a modder, can we import static-images as portraits? I need to add anime waifus. Preferably, I'll have a static-image for each expression and I can code it to the use the appropriate one based on the situation. If it doesn't support static-images, would I need 3D software? If so, what is recommended?

## Reply 61 — participant_042 · 2020-06-10 · post-26644969

Can you clarify if Mean Time To Happen is reduced to a small number of events, supported but not used in vanilla, or completely removed?

## Reply 62 — participant_043 · 2020-06-10 · post-26645014

Are succession laws scriptable?

## Reply 63 — participant_044 · 2020-06-10 · post-26645241

>O< !!! AAaaaah! I want ALL OF THIS in Stellaris! These two functions alone... ...fulfil most of my scripting wishlist and do it better than the clunky array setup I would have settled on! Now I want to make mods for two Paradox games simultanously... Ehehe... I'm in danger.

## Reply 64 — participant_024 · 2020-06-10 · post-26645545

<!-- artifact:quote:start -->
> SchwarzKatze said: Can you clarify if Mean Time To Happen is reduced to a small number of events, supported but not used in vanilla, or completely removed? Click to expand...
<!-- artifact:quote:end -->
Completely removed, it is gone entirely in Imperator too and I don't see it ever making a come back in any future games as on a Jomini level the event class and manager does not handle mean time to happen, it is just objectively worse than on actions in pretty much every way: Bad on performance Not reliable to fire Cannot weight relative to other events easily Overall harder to maintain and control

## Reply 65 — participant_045 · 2020-06-10 · post-26645668

<!-- artifact:quote:start -->
> Atalvyr said: Helpful for modders I guess, but not much for the rest of us who hunger for CK3 info. Click to expand...
<!-- artifact:quote:end -->
Oh my, scriptable on_actions, my wet dream come true This is not only helpful for modders, it's also helpful for anybody else who doesn't mod but likes using mods. If you ever play with mods, this DD is indirectly important to you as well

## Reply 66 — participant_046 · 2020-06-10 · post-26647427

<!-- artifact:quote:start -->
> blackninja9939 said: Completely removed, it is gone entirely in Imperator too and I don't see it ever making a come back in any future games as on a Jomini level the event class and manager does not handle mean time to happen, it is just objectively worse than on actions in pretty much every way: Bad on performance Not reliable to fire Cannot weight relative to other events easily Overall harder to maintain and control Click to expand...
<!-- artifact:quote:end -->
But this doesn't mean that we will be seeing all events on the 2nd of the month, right? Just that on the second an event fires and selects all the other events that need to happen to our poor, hapless character this month.

## Reply 67 — participant_035 · 2020-06-10 · post-26647657

<!-- artifact:quote:start -->
> Rockphed said: But this doesn't mean that we will be seeing all events on the 2nd of the month, right? Just that on the second an event fires and selects all the other events that need to happen to our poor, hapless character this month. Click to expand...
<!-- artifact:quote:end -->
In the custom civil war on action example, it looks like you can provide a custom range for the events to fire in, 6 to 12 months in this case (or I'm mistaken and it'll trigger once in 6 months and once again in 12, but the former seems more useful and likely to me)

## Reply 68 — participant_024 · 2020-06-10 · post-26647686

<!-- artifact:quote:start -->
> Rockphed said: But this doesn't mean that we will be seeing all events on the 2nd of the month, right? Just that on the second an event fires and selects all the other events that need to happen to our poor, hapless character this month. Click to expand...
<!-- artifact:quote:end -->
Not really, the events can be delayed to run at a later date in a random range instead of on the same date. And of course this is only for various pulse events, reactive on actions and being part of other people's event chains will be at entirely different date ranges still.

## Reply 69 — participant_047 · 2020-06-11 · post-26650375

Will you guys release your in-house syntax highlighting to the general public?

## Reply 70 — participant_048 · 2020-06-12 · post-26652084

One thing that occurred to me looking at the shouty-man example: will there be a way to set up those lists ordered by numbers of some connection a character has? For instance, could you make an ordered list of rulers in your realm by the number of direct vassals they have, or a list of people sorted by how many friends they have, or a list of Muslim rulers sorted by number of wives? I've got very little experience modding, but I can see all sorts of uses for those in events.

## Reply 71 — participant_049 · 2020-06-12 · post-26652242

Will there be modding dev diaries before release? I'm curious what other functionalities/features you guys decided to carry over from Imperator (which really had very good modding capabilities)..

## Reply 72 — participant_050 · 2020-06-12 · post-26652874

Code: has_culture = culture:french has_faith = faith:ashari Nani? Why the extra faith:/culture: ?

## Reply 73 — participant_030 · 2020-06-12 · post-26652893

That does look redundant. Unless stuff other than culture can go into has_culture?

## Reply 74 — participant_042 · 2020-06-13 · post-26654549

Probably culture groups and religion groups

## Reply 75 — participant_051 · 2020-06-14 · post-26658266

<!-- artifact:quote:start -->
> Aerkhanite said: Code: has_culture = culture:french has_faith = faith:ashari Nani? Why the extra faith:/culture: ? Click to expand...
<!-- artifact:quote:end -->
I would hazard a guess it's because custom faiths can have custom names, and as such you could have a faith called "french" - that is, if custom faith names are identified as such, and not as, say, "customcatholicfaith1".

## Reply 76 — participant_052 · 2020-06-14 · post-26659265

Thank you, this is the most interesting dev diary yet. Moddability is one of the reasons CK2 is so popular. I cannot wait to re-experience ATE and ASOIF mods in CK3.

## Reply 77 — participant_053 · 2020-06-15 · post-26660118

Throughout Medieval History Cavalry played a paramount role in warfare. Seeing footman sprites in a game about Medieval times is very sad. So, Paradox , please can you make cavalry sprites instead of these. It is all about immersion and such. It was so disappointing to see "infantry" as your army representation on the game map that i started drinking again(been sober for the past three months )(jk). A mounted warrior is so symbolic to that period that you guys really must implement it. From the steppes of Mongolia to the arid Moroccan flatland. From Denmark to Italia a warrior on a HORSE was dominating the battlefields of that period. So WHY ON EARTH FOOTMAN SPRITES?? When you think of that period you imagine Norman proto knights with a spear and a tear shield, or Teutons with their intimidating helmets (i am Russian, so read Sergei Eisenstein: Aleksandr Nevsky). English knights with lions on red or French with lilies on blue. Mounted Mongols with their steppe horses, bringing a rain of arrows on their foes, Arabs on their graceful horses. BUT NOT FOOTMEN. I am opening a campaign against footman sprites. Lord Jesus help me in my endeavors.

## Reply 78 — participant_054 · 2020-06-15 · post-26660170

this is not actual scripting, these are data structures and we can set values... you should provide a .NET api, there are many things I am unhappy with in ck2 I wish I could just fix myself. Give us a .NET api and let us fix the game ourselves this code is terrible, let us use a proper language, any normal programming language, python whatever, anything but this!

## Reply 79 — participant_024 · 2020-06-15 · post-26660292

<!-- artifact:quote:start -->
> pcuser1584789 said: this is not actual scripting, these are data structures and we can set values... you should provide a .NET api, there are many things I am unhappy with in ck2 I wish I could just fix myself. Give us a .NET api and let us fix the game ourselves this code is terrible, let us use a proper language, any normal programming language, python whatever, anything but this! Click to expand...
<!-- artifact:quote:end -->
> these are data structures and we can set values I mean, that sums up the core of like most of all programming languages... Our scripting language is even turing complete... A .NET, python, lua or any other language API is very unlikely for the simple fact we don't internally use that. The amount of time it would take to re-expose everything via another language is just not a time investment we can ever really justify, along with the up front time cost that also then becomes another thing to have to maintain and we'd also then need to take the overhead of those languages into account when working on performance. And I'd highly doubt it will fix the things you likely want to script anyway, its not going to un-hardcode all the things that are already hardcoded which is the impression I get from you pointing out short comings of the scripting in CK2. Our script language is by no means perfect, but its plain english and very easy for non programmers to get to grips with to work to make things, as well as easy for us on the programming side to add new triggers and effects etc.

## Reply 80 — participant_041 · 2020-06-15 · post-26662422

<!-- artifact:quote:start -->
> pcuser1584789 said: this code is terrible, let us use a proper language, any normal programming language, python whatever, anything but this! Click to expand...
<!-- artifact:quote:end -->
One of the advantages to Paradox's code is its simplicity. I'm not a programmer, yet even I was able to mod heavily with CKII. In about 1-2 days of self-learning, I was creating custom events, new traits, and a new religion. I can't imagine how long it would have taken me otherwise. I get what you're saying though that if you're an experienced programmer, it might seem frustrating, but as a non-programmer, it helped me out a lot.

## Reply 81 — participant_035 · 2020-06-15 · post-26662444

<!-- artifact:quote:start -->
> RelVleDy said: I get what you're saying though that if you're an experienced programmer, it might seem frustrating, but as a non-programmer, it helped me out a lot. Click to expand...
<!-- artifact:quote:end -->
As an experienced programmer, CK2's scripting language is perfectly serviceable. The new tools previewed here plus other general features of the latest Clausewitz and Jomini will make it even better

## Reply 82 — participant_049 · 2020-06-16 · post-26663899

<!-- artifact:quote:start -->
> pcuser1584789 said: this is not actual scripting, these are data structures and we can set values... you should provide a .NET api, there are many things I am unhappy with in ck2 I wish I could just fix myself. Give us a .NET api and let us fix the game ourselves this code is terrible, let us use a proper language, any normal programming language, python whatever, anything but this! Click to expand...
<!-- artifact:quote:end -->
Yeah I don't think this is a good idea to be honest. This code is simplified enough for any gamer to learn how to mod. Using other programming languages will make it more difficult and no one will want to learn C++ or python just to be able to mod CK3.

## Reply 83 — participant_055 · 2020-06-16 · post-26666170

<!-- artifact:quote:start -->
> nCaveman said: Thing is modders are extremely important to many aspects of the CK community. Those groups need to know if they will be able to transition from one game to the next. Click to expand...
<!-- artifact:quote:end -->
Not just the modders, but the people who love playing those mods will also want to know if the mods (especially the total conversion mods) will make an appearance in CK3. The easier the game is to mod, not only will it be more likely that widely loved mods will make an appearance, but the sooner those mods will get translated.

## Reply 84 — participant_056 · 2020-06-22 · post-26681835

good post!

## Reply 85 — participant_057 · 2020-06-23 · post-26684471

As much as I love the customisable religions, and as interesting as the stress mechanic seems, I think the improvements to the scripting language might in the long term be the greatest addition to the game; I do like me some modding after all.

## Reply 86 — participant_020 · 2020-06-23 · post-26684478

<!-- artifact:quote:start -->
> DaJay42 said: As much as I love the customisable religions, and as interesting as the stress mechanic seems, I think the improvements to the scripting language might in the long term be the greatest addition to the game; I do like me some modding after all. Click to expand...
<!-- artifact:quote:end -->
Customisable religions in itself opens great opportunities for modders, as changing religions mid-gameplay was a bit of a chore if you didn't stick to just what the base game offered

## Reply 87 — participant_058 · 2020-06-26 · post-26693174

@blackninja9939 I don't remember if it's ever been asked, mostly because I haven't paid too much attention to the scripting part of CK(3), but is it theoretically possible to script new inheritance laws? And if not - if they're hard-coded - would it be possible to open up hard-coded inheritance laws just enough so as to modify how they...divide the estates, for example? I'm thinking specifically about Gavelkind.

## Reply 88 — participant_059 · 2020-09-05 · post-26873217

Thanks for the in-depth description. I have a question and I feel it might be a place to ask it. The Wiki says AI characters will use Decisions and Character Interactions based on the attributes. Energy determines how often the character will consider a Decision. Does it mean that if my character is ambitious (+75 energy) I'll get more events triggered? And if he is lazy (-50 energy) I'll have fewer opportunities to choose some answers from a list? If yes, how much does it influence the event occurrence?

