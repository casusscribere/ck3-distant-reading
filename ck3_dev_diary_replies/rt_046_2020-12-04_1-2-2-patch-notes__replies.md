---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1446267/"
forum_thread_id: 1446267
content_type: reply_thread
parent_dd_file: dd_046_2020-12-04_dev-diary-46-1-2-2-patch-notes.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 46
title: "CK3 Dev Diary #46 - 1.2.2 Patch Notes"
dd_date: 2020-12-04
expansion: Post-release patches
patch: Patch 1.2 (Argent)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 4
reply_count: 69
participant_count: 50
reply_date_first: 2020-12-04
reply_date_last: 2020-12-14
body_word_count: 3356
inline_image_count: 0
quoted_span_count: 41
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — CK3 Dev Diary #46 - 1.2.2 Patch Notes

*69 replies from 50 participants across 4 pages*

## Reply 1 — participant_001 · 2020-12-04 · post-27147758

Greetings! Patch 1.2 ‘Argent’ has been out for a while now, and we hope you’re enjoying it! It’s so much fun to see what fascinating creations you all create in the Ruler Designer! To round off the year, we’re planning to release a small patch early next week. Originally we wanted to release it this week, but some more issues were found that we wanted to address - such is the nature of software development! The patch will address a number of bugs and issues, listed below: Spoiler: 1.2.2 Patch Notes - You can now hold the Control-key when raising armies to not have them be split based on supply when you raise them - Fixed the Ruler Designer crashing when using the arrow keys to move sliders on machines with limited RAM - Fixed some characters not having access to Cultural Names when naming children because their Religion didn’t have any Religious names defined - Fixed a crash that could happen when randomizing Dynasty Names for certain cultures in the Ruler Designer - Fixed the Legacies button being hidden beyond the screen if both Dynasty and House modifiers are present - Fixed the AI not always supporting the player correctly when handling massive armies - Fixed not being able to build certain buildings when playing the game in spanish, esto ahora está arreglado - Fixed siege sounds sometimes persisting after you close the siege window - Removed the deprecated Nudity game rule, nudity is now toggled on/off in the settings menu, accessible in the same place as you toggle displaying graphical diseases - The lifestyle/focus button is no longer visible on characters that cannot have a lifestyle set - Kicking a player that is still inside the Ruler Designer will no longer block a multiplayer game from starting - When you Ruler Design a character, you will no longer lose all non-De Jure vassals that ruler had - Fixed not always having access to all hairstyles when Ruler Designing a character that is 18 years old or younger - You now get less points from being extremely old when Ruler Designing a character - Fixed the list of Faiths exceeding its limits when playing the game in a non-english language - Criminal rulers no longer get a free pass on imprisoning without impunity - Diplomacy perk modifiers are now added and subtracted properly (Sound Foundations and Friendly Counsel) - Fixed losing Piety when imprisoning generic Criminals, now properly only applies when imprisoning your Head of Faith - Fixed an issue with floating or sinking infant characters in the main menu, exorcism successful - Fixed a memory leak in the GUI editor - Fixed a memory leak for character portraits. This could have a significant effect in the Ruler Designer, and a lesser one during normal play - Fixed achievements sometimes being shown as unavailable even though they were available That's all for now! Have a great winter!

## Reply 2 — participant_002 · 2020-12-04 · post-27147770

Don't suppose you have any idea when you're aiming to have dev diaries back? Hoping for first week of January but maybe thats just me being too optimistic for news of the first expansion! Hope you all have a great winter too though!

## Reply 3 — participant_003 · 2020-12-04 · post-27147787

I reported an easy to fix bug on the 1st of September, 90 minutes after the game was launched and I added the fixed code (took me 5 min) into the bug report. The response on the 2nd September was that "We are aware of the issue, it has already been added to our bug database." Why isn't it fixed? It is literally takes 5 minutes and I included the fixed code: CK III - Estonian culture doesn't have access to longships Short summary of your issue Estonian culture doesn't have access to longships Game Version 1.0.2 What OS are you playing on? Windows What platform are you using? Steam Do you have mods enabled? No Have you tried verifying your game... forum.paradoxplaza.com I studied Northern-European history in uni and that's the main region where I play with different cultures. It's hard to be immersed if there's an easy to fix bug that practically makes a culture unplayable as the core part of that culture is just missing.

## Reply 4 — participant_004 · 2020-12-04 · post-27147795

Thanks for the fixes! I did notice the one with the Siege sounds, and was very confused. Glad it's fixed! Saves me a reload when it happens.

## Reply 5 — participant_005 · 2020-12-04 · post-27147810

<!-- artifact:quote:start -->
> es333 said: I reported an easy to fix bug on the 1st of September, 90 minutes after the game was launched and I added the fixed code (took me 5 min) into the bug report. The response on the 2nd September was that "We are aware of the issue, it has already been added to our bug database." Why isn't it fixed? It is literally takes 5 minutes and I included the fixed code: CK III - Estonian culture doesn't have access to longships Short summary of your issue Estonian culture doesn't have access to longships Game Version 1.0.2 What OS are you playing on? Windows What platform are you using? Steam Do you have mods enabled? No Have you tried verifying your game... forum.paradoxplaza.com I studied Northern-European history in uni and that's the main region where I play with different cultures. It's hard to be immersed if there's an easy to fix bug that practically makes a culture unplayable as the core part of that culture is just missing. Click to expand...
<!-- artifact:quote:end -->
That it is not a bug, this is a history issue and there are many areas where it could be improved. 1.2 was for the ruler designer and to fix game issues, history will be always second to gameplay. Maybe 1.3 or 1.4 you will get it.

## Reply 6 — participant_006 · 2020-12-04 · post-27147811

<!-- artifact:quote:start -->
> es333 said: The response on the 2nd September was that "We are aware of the issue, it has already been added to our bug database." Why isn't it fixed? It is literally takes 5 minutes and I included the fixed code: Click to expand...
<!-- artifact:quote:end -->
Because once you start fixing the small/easy/low priority issues you're opening the floodgates to a never ending waterfall. There is this analogy for life that involves a jar, rocks, marbles and sand that can also apply to bug fixing/project time boxing. First you do the critical and high priority issues (rocks), then the medium ones (marbles) and then the low ones (sand), if you start by doing the low priority issues first you'll keep going cause there will always be another, and another, and another.

## Reply 7 — participant_003 · 2020-12-04 · post-27147838

<!-- artifact:quote:start -->
> daniloy said: That it is not a bug, this is a history issue and there are many areas where it could be improved. 1.2 was for the ruler designer and to fix game issues, history will be always second to gameplay. Maybe 1.3 or 1.4 you will get it. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Hello es333! We are aware of the issue, it has already been added to our bug database. Thank you for your report! Click to expand...
<!-- artifact:quote:end -->
What? If you open up the CK code then you see that it is a bug, an area has mistakenly been placed into a wrong geographical region. From my bug report thread:

## Reply 8 — participant_007 · 2020-12-04 · post-27147845

<!-- artifact:quote:start -->
> Akazury said: Because once you start fixing the small/easy/low priority issues you're opening the floodgates to a never ending waterfall. There is this analogy for life that involves a jar, rocks, marbles and sand that can also apply to bug fixing/project time boxing. First you do the critical and high priority issues (rocks), then the medium ones (marbles) and then the low ones (sand), if you start by doing the low priority issues first you'll keep going cause there will always be another, and another, and another. Click to expand...
<!-- artifact:quote:end -->
In CK2 most that issues were fixed by modders, but for now we have no major mods released yet I think, It is important case

## Reply 9 — participant_003 · 2020-12-04 · post-27147846

<!-- artifact:quote:start -->
> Akazury said: Because once you start fixing the small/easy/low priority issues you're opening the floodgates to a never ending waterfall. There is this analogy for life that involves a jar, rocks, marbles and sand that can also apply to bug fixing/project time boxing. First you do the critical and high priority issues (rocks), then the medium ones (marbles) and then the low ones (sand), if you start by doing the low priority issues first you'll keep going cause there will always be another, and another, and another. Click to expand...
<!-- artifact:quote:end -->
Interesting viewpoint. As I know how to code on an acceptable level then I would fix different small bugs voluntarily from my free time as it's actually interesting. I think there are others in the community who share my mindset. The thing is that several small bugs are so obvious and easy to fix that you do not even have to be very familiar with CK to fix them.

## Reply 10 — participant_008 · 2020-12-04 · post-27147847

<!-- artifact:quote:start -->
> es333 said: I reported an easy to fix bug on the 1st of September, 90 minutes after the game was launched and I added the fixed code (took me 5 min) into the bug report. The response on the 2nd September was that "We are aware of the issue, it has already been added to our bug database." Why isn't it fixed? It is literally takes 5 minutes and I included the fixed code: CK III - Estonian culture doesn't have access to longships Short summary of your issue Estonian culture doesn't have access to longships Game Version 1.0.2 What OS are you playing on? Windows What platform are you using? Steam Do you have mods enabled? No Have you tried verifying your game... forum.paradoxplaza.com I studied Northern-European history in uni and that's the main region where I play with different cultures. It's hard to be immersed if there's an easy to fix bug that practically makes a culture unplayable as the core part of that culture is just missing. Click to expand...
<!-- artifact:quote:end -->
Something being quick to fix does not justify its inclusion in a hotfix, as hotfixes require a high impact vs. risk ratio. We're likely to fix it in 1.3, but not a hotfix.

## Reply 11 — participant_003 · 2020-12-04 · post-27147858

<!-- artifact:quote:start -->
> Meneth said: Something being quick to fix does not justify its inclusion in a hotfix, as hotfixes require a high impact vs. risk ratio. We're likely to fix it in 1.3, but not a hotfix. Click to expand...
<!-- artifact:quote:end -->
I completely forgot that point, you're correct, that is a completely valid (and preferable) logic. I'm sorry for being too harsh.

## Reply 12 — participant_008 · 2020-12-04 · post-27147861

<!-- artifact:quote:start -->
> es333 said: I completely forgot that point, you're correct, that is a completely valid (and preferable) logic. I'm sorry for being too harsh. Click to expand...
<!-- artifact:quote:end -->
<3

## Reply 13 — participant_009 · 2020-12-04 · post-27147867

That all sounds really good!

## Reply 14 — participant_010 · 2020-12-04 · post-27147872

<!-- artifact:quote:start -->
> rageair said: - Fixed a memory leak in the GUI editor Click to expand...
<!-- artifact:quote:end -->
I am really glad that this has been fixed.

## Reply 15 — participant_011 · 2020-12-04 · post-27147923

Kinda wish it was hold control to raise split, rather than the other way around, but hopefully it'll just get completely reworked in the next full patch anyway. The raise split behavior seems very rarely desirable, and I'll forget to hold control some significant portion of the time.

## Reply 16 — participant_012 · 2020-12-04 · post-27148066

So no fix for the hook manufacture=perceived murder. Sad!

## Reply 17 — participant_013 · 2020-12-04 · post-27148184

<!-- artifact:quote:start -->
> Subcomandante said: So no fix for the hook manufacture=perceived murder. Sad! Click to expand...
<!-- artifact:quote:end -->
Does not sound like something a hotfix would be used to fix.

## Reply 18 — participant_014 · 2020-12-04 · post-27148253

<!-- artifact:quote:start -->
> rageair said: Criminal rulers no longer get a free pass on imprisoning without impunity Click to expand...
<!-- artifact:quote:end -->
I thought it was a feature to work with Empire of Sin's release.

## Reply 19 — participant_015 · 2020-12-04 · post-27148303

1.2 savegames compatible with the hotfix? I recall you guys said that 1.1.3 games would be playable in 1.2 but they actually weren't so...

## Reply 20 — participant_016 · 2020-12-04 · post-27148374

<!-- artifact:quote:start -->
> rageair said: - Fixed a memory leak in the GUI editor - Fixed a memory leak for character portraits. This could have a significant effect in the Ruler Designer, and a lesser one during normal play Click to expand...
<!-- artifact:quote:end -->
<3

## Reply 21 — participant_017 · 2020-12-04 · post-27148388

<!-- artifact:quote:start -->
> Subcomandante said: So no fix for the hook manufacture=perceived murder. Sad! Click to expand...
<!-- artifact:quote:end -->
Was that bug reported and acknowledged yet?

## Reply 22 — participant_018 · 2020-12-04 · post-27148433

Thanks for improving a major bug with the Spanish localization. Only today did my roommate and I realize the Intrigue tab’s conspiracies are supposed to show actual numbers/stats, as they simply don’t show up in Spanish. So I’m glad to see that locale fixes aren’t outside the scope of hotfix releases. Aside, I wish there was a good way to contribute to the localizations. I’ve been fixing the yaml files myself as I play but there doesn’t seem to be any good handoff from technical volunteer to developer. Edit: I see that CK3 has a way to override built-in localization rules without touching the game files (https://ck3.paradoxwikis.com/index.php?title=Modding). I have a few dozen changes made to the game's Spanish locale files. I'm going to move my changes to the mentioned "replace" folder. It's a good enough middle ground. Edit2: Is there another folder I can put my "replace" folder that will still allow achievements?

## Reply 23 — participant_019 · 2020-12-04 · post-27148439

Very nice improvements! Especially with Ruler Designer performance

## Reply 24 — participant_020 · 2020-12-04 · post-27148484

<!-- artifact:quote:start -->
> rageair said: esto ahora está arreglado Click to expand...
<!-- artifact:quote:end -->
buenisimo, gracias

## Reply 25 — participant_021 · 2020-12-04 · post-27148569

Nice work! Does the intimidation perk bug difficult to fix? I think the 'Forever Infamous' perk bugged the Dread monthly changes. { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" } I reported the bug and the dev already acknowledged it. I hope this will be fixed next hotfix, even though I don't see it on the notes above. I hope it's one of the 'more issues' that you guys wanted to address.

## Reply 26 — participant_022 · 2020-12-04 · post-27148574

<!-- artifact:quote:start -->
> rageair said: - You now get less points from being extremely old when Ruler Designing a character Click to expand...
<!-- artifact:quote:end -->
*(no text body — reaction-only or media-only post)*

## Reply 27 — participant_023 · 2020-12-04 · post-27148679

Thank you PDX the game is perfect now! You can’t believe how happy I was you fixed the border highlight issue, and how happy I am you’re going to fix the siege sound issue

## Reply 28 — participant_024 · 2020-12-04 · post-27148740

<!-- artifact:quote:start -->
> rageair said: Fixed the AI not always supporting the player correctly when handling massive armies Click to expand...
<!-- artifact:quote:end -->
Finally! Im glad

## Reply 29 — participant_025 · 2020-12-04 · post-27148771

some mods that only change aesthetics (i have a potato computer, so some performance mods are very helpful) stuff are not achievement-compatible. Are you planning on changing that on a future update?

## Reply 30 — participant_026 · 2020-12-04 · post-27148812

Will you developers add the "Parsig" culture from CK2's HIP mod?

## Reply 31 — participant_027 · 2020-12-04 · post-27148826

Thank you for the fixes!!

## Reply 32 — participant_028 · 2020-12-05 · post-27149167

Really glad to see the first line of the patch notes and really appreciate your work!

## Reply 33 — participant_029 · 2020-12-05 · post-27149264

Great work, keep it up! I just have one question, have you considered a spouse designer?

## Reply 34 — participant_030 · 2020-12-05 · post-27150025

- You can now hold the Control-key when raising armies to not have them be split based on supply when you raise them May you consider adding another key combo where it would raise the MAA in the target county (and do not add more levies to it), and the levies in the surrounding counties? I personally love the new function when raising levies to mass siege when my MAAs are already up and killing things, so I don't have to manually split a death stack into multiple siege stacks.

## Reply 35 — participant_031 · 2020-12-05 · post-27150433

<!-- artifact:quote:start -->
> rageair said: - You can now hold the Control-key when raising armies to not have them be split based on supply when you raise them Click to expand...
<!-- artifact:quote:end -->
Greetings. Please make an option to raise armys like it was before. It now takes forever to raise 30-40 armys on point! I dont play the game anymore after the last patch because of this change.

## Reply 36 — participant_032 · 2020-12-06 · post-27150493

<!-- artifact:quote:start -->
> Gutser CKIII said: Greetings. Please make an option to raise armys like it was before. It now takes forever to raise 30-40 armys on point! I dont play the game anymore after the last patch because of this change. Click to expand...
<!-- artifact:quote:end -->
That's... literally what you are quoting. Holding control will make it function as it did before the 1.2 patch

## Reply 37 — participant_033 · 2020-12-06 · post-27150532

Would recommend having at some point the ability when creating a custom religion (or a modded one) a line that defines what faith's naming conventions to use. Example being when in custom religion designer, an option to choose which faith's naming conventions to have available to it, either of the same religious group (or maybe ones its syncretic with as well) could be placed in the section with a simple button under the "Description" of the faith for "Religious names" where they are enabled/disabled similar to how tenants work (if its of the same religious group its automatically selectable, if its syncretic it is enabled as well). This could simplify and allow for religious names to be more easily chosen from and add a bit to the benefit of the custom religion mechanic that shouldn't be too difficult to add.

## Reply 38 — participant_031 · 2020-12-06 · post-27150553

<!-- artifact:quote:start -->
> pevergreen said: That's... literally what you are quoting. Holding control will make it function as it did before the 1.2 patch Click to expand...
<!-- artifact:quote:end -->
Patch can´t come soon enough. I want to play Option on/off would be better anyway.

## Reply 39 — participant_034 · 2020-12-06 · post-27150675

<!-- artifact:quote:start -->
> Gutser CKIII said: Patch can´t come soon enough. I want to play Option on/off would be better anyway. Click to expand...
<!-- artifact:quote:end -->
There are legitimate reasons to use both options in the same playthrough. A checkbox in the rally point interface itself might be slightly more convenient than modifier-click, but in the end it's all much of a muchness.

## Reply 40 — participant_035 · 2020-12-06 · post-27150765

<!-- artifact:quote:start -->
> Tiax said: Kinda wish it was hold control to raise split, rather than the other way around, but hopefully it'll just get completely reworked in the next full patch anyway. The raise split behavior seems very rarely desirable, and I'll forget to hold control some significant portion of the time. Click to expand...
<!-- artifact:quote:end -->
Agreed, but I'm not going to complain. I wasn't expecting any changes to avoid the splitting armies feature (considering it is meant to be a feature) anytime even remotely soon. I'm very happy that they listened to all of us who were not happy with that feature. Holding CTRL may be a bit of a pain, but at least it's there as an option now, which is much more than I expected.

## Reply 41 — participant_036 · 2020-12-06 · post-27151084

The Prison "Fix" should never have been broken in the first place. How much of an edge case is it to imprison your religious figure? Come on, now. It was an attempt to reign in imprisonment, and it was flawed like the Raise All fiasco. Can we get some real test involved? The Raise All would've been caught in 2 seconds as a design fail. Same with imprisonment Piety costs... assuming it is like you say, a "bug", and not marketing speak for overzealous attempts to control unwanted user interactions.

## Reply 42 — participant_017 · 2020-12-06 · post-27151172

<!-- artifact:quote:start -->
> prenda claw said: The Prison "Fix" should never have been broken in the first place. How much of an edge case is it to imprison your religious figure? Come on, now. It was an attempt to reign in imprisonment, and it was flawed like the Raise All fiasco. Can we get some real test involved? The Raise All would've been caught in 2 seconds as a design fail. Same with imprisonment Piety costs... assuming it is like you say, a "bug", and not marketing speak for overzealous attempts to control unwanted user interactions. Click to expand...
<!-- artifact:quote:end -->
About the prison bug: agreed. So do Paradox. Which is presumably why they are releasing a hotfix for it. My guess is that they were trying to work on something else, deleted a { or } or changed some check somewhere, and ended up with that Piety bug. That's not necessarily something you'll easily catch on testing.

## Reply 43 — participant_036 · 2020-12-06 · post-27151259

If you're working in that part of the code for imprisonment, shouldn't you test it? They say in the notes they were working on imprisonment and wanted to change player behaviors. It's literally every interaction related to imprisonment. So this Piety loss is a "bug"? Sure, maybe. I mean, when they sold us this Raise All thing as a "feature", I take all of these marketing-speak patch notes with a hefty dose of salt.

## Reply 44 — participant_017 · 2020-12-06 · post-27151271

<!-- artifact:quote:start -->
> prenda claw said: If you're working in that part of the code for imprisonment, shouldn't you test it? They say in the notes they were working on imprisonment and wanted to change player behaviors. It's literally every interaction related to imprisonment. So this Piety loss is a "bug"? Sure, maybe. I mean, when they sold us this Raise All thing as a "feature", I take all of these marketing-speak patch notes with a hefty dose of salt. Click to expand...
<!-- artifact:quote:end -->
Heh, I've never seen people marketing their products with bugs.

## Reply 45 — participant_031 · 2020-12-06 · post-27151397

<!-- artifact:quote:start -->
> Riamus said: Agreed, but I'm not going to complain. Click to expand...
<!-- artifact:quote:end -->
I´m not complaining. I simply don´t play they game until it´s fixed. From my point of view it is a game braking bug. I cannot create focused armys anymore and this is a main activity in this game. I declare wars in waves, 1 wave 3-6 wars. Therefore I create 1 main army, 30 little armys etc., raising man at arms just to eliminate peasant revolts and enemy border armys. It is a mess to do it with the new patch, unplayable. Edit: I put some research in it. So this BUG is well known from Paradox - Do they want to drive people away from the game? It seems so. Because the game is unplayable with big armys for month now. ... O.k., I complain.

## Reply 46 — participant_035 · 2020-12-06 · post-27151428

I wasn't suggesting you or anyone was complaining. I was saying only that I'm not because this is more than I expected anyhow.

## Reply 47 — participant_031 · 2020-12-06 · post-27151446

Okay sorry. This raising armys problem makes me little bit angry.

## Reply 48 — participant_037 · 2020-12-06 · post-27151447

Nice patch , and diplomacy tree playable again. And seems like we need wait for 1.3 now But pdx need do open beta test before realese games. 3 month already we are waiting for fixing key futures

## Reply 49 — participant_018 · 2020-12-06 · post-27151570

<!-- artifact:quote:start -->
> prenda claw said: The Prison "Fix" should never have been broken in the first place. How much of an edge case is it to imprison your religious figure? Come on, now. It was an attempt to reign in imprisonment, and it was flawed like the Raise All fiasco. Can we get some real test involved? The Raise All would've been caught in 2 seconds as a design fail. Same with imprisonment Piety costs... assuming it is like you say, a "bug", and not marketing speak for overzealous attempts to control unwanted user interactions. Click to expand...
<!-- artifact:quote:end -->
You're suggesting malice or ulterior motives because a bug was too elementary for your tastes, but it's not a helpful nor realistic way to imagine software, a complex constantly-changing system where the most seemingly harmless change can ricochet into a seemingly unrelated regression. Frankly, Paradox makes it look too easy to build a simulation like EU/CK that is a compelling experience and not just a dumpster fire.

## Reply 50 — participant_038 · 2020-12-07 · post-27153040

The beginning of next week is a very vague period. Is there more accurate information?

## Reply 51 — participant_017 · 2020-12-07 · post-27153046

<!-- artifact:quote:start -->
> Turgaud said: The beginning of next week is a very vague period. Is there more accurate information? Click to expand...
<!-- artifact:quote:end -->
Monday, Tuesday, or Wednesday.

## Reply 52 — participant_039 · 2020-12-07 · post-27153111

<!-- artifact:quote:start -->
> rageair said: - When you Ruler Design a character, you will no longer lose all non-De Jure vassals that ruler had Click to expand...
<!-- artifact:quote:end -->
Hi, I think I saw a related bug last weekend. I ruler designed a character who had a non-De Jure liege and was unable to modify my feudal contract. Will this issue be covered by this fix?

## Reply 53 — participant_040 · 2020-12-07 · post-27153127

@rageair Could you please fix bastards automatically being given royal titles? (Prince, Princess, etc.) I don't remember this ever being an issue in CK II.

## Reply 54 — participant_041 · 2020-12-07 · post-27153320

I couldn't cancel a temple holding from being constructed after I started its construction... Is this intended, or a bug?

## Reply 55 — participant_017 · 2020-12-07 · post-27153328

<!-- artifact:quote:start -->
> Talos the Cat said: I couldn't cancel a temple holding from being constructed after I started its construction... Is this intended, or a bug? Click to expand...
<!-- artifact:quote:end -->
Was it in your own county, or was someone else holding the county? As of the latest update we can no longer cancel buildings and upgrades in vassal-held counties.

## Reply 56 — participant_042 · 2020-12-07 · post-27153346

Um, could you let us revert to 1.2? So we could compare if there were any changes to gui files?

## Reply 57 — participant_043 · 2020-12-07 · post-27153488

<!-- artifact:quote:start -->
> rageair said: - Criminal rulers no longer get a free pass on imprisoning without impunity Click to expand...
<!-- artifact:quote:end -->
The triple negative in that confuses me. Punity is the ability to be punished. Impunity means you lack the ability to be punished. "Without impunity" would mean that you can be punished (again). So saying that criminal rulers no longer get a free pass on that means they used to be able to be punished for imprisoning people but now they can't? Am I reading that correctly?

## Reply 58 — participant_020 · 2020-12-07 · post-27153506

<!-- artifact:quote:start -->
> o76923 said: The triple negative in that confuses me. Punity is the ability to be punished. Impunity means you lack the ability to be punished. "Without impunity" would mean that you can be punished (again). So saying that criminal rulers no longer get a free pass on that means they used to be able to be punished for imprisoning people but now they can't? Am I reading that correctly? Click to expand...
<!-- artifact:quote:end -->
i read it like: rulers who are known criminals used to have the ability to imprison other people without any consequence, but now that is no longer the case

## Reply 59 — participant_044 · 2020-12-07 · post-27153555

<!-- artifact:quote:start -->
> Fac0810 said: i read it like: rulers who are known criminals used to have the ability to imprison other people without any consequence, but now that is no longer the case Click to expand...
<!-- artifact:quote:end -->
Yeah... That sentence was just a little bit more twisty than what I'm used to reading. The explanations make sense...

## Reply 60 — participant_045 · 2020-12-07 · post-27153891

Thanks for all the hard work, Paradox team. Looking forward to content (and eventual fixes) to come!

## Reply 61 — participant_046 · 2020-12-07 · post-27154000

<!-- artifact:quote:start -->
> rageair said: - You can now hold the Control-key when raising armies to not have them be split based on supply when you raise them Click to expand...
<!-- artifact:quote:end -->
Remarkable, such mistakes would not reverse generally.

## Reply 62 — participant_047 · 2020-12-07 · post-27154224

<!-- artifact:quote:start -->
> rageair said: - Diplomacy perk modifiers are now added and subtracted properly (Sound Foundations and Friendly Counsel) Click to expand...
<!-- artifact:quote:end -->
I have a game where my character has both of these perks unlocked and so I stopped playing for a while waiting for this patch to fix it. However, now I have updated my game and the additional skills are still not being applied. I have 4 friends and 16 living children. I tried restarting the game again but that didn't help. Does anyone have any other tricks I could try to fix this?

## Reply 63 — participant_048 · 2020-12-07 · post-27154336

<!-- artifact:quote:start -->
> rageair said: - You can now hold the Control-key when raising armies to not have them be split based on supply when you raise them Click to expand...
<!-- artifact:quote:end -->
THANK YOU SO MUCH!!!

## Reply 64 — participant_033 · 2020-12-08 · post-27154718

<!-- artifact:quote:start -->
> prenda claw said: If you're working in that part of the code for imprisonment, shouldn't you test it? They say in the notes they were working on imprisonment and wanted to change player behaviors. It's literally every interaction related to imprisonment. So this Piety loss is a "bug"? Sure, maybe. I mean, when they sold us this Raise All thing as a "feature", I take all of these marketing-speak patch notes with a hefty dose of salt. Click to expand...
<!-- artifact:quote:end -->
They shouldn't be imposing by trying to "change player behavior" AT ALL. Pretty sure that runs contrary to how Pdox has marketed PDS titles to us since... like the beginning. Paradox has always had a good rep of trying to balance fun/challenge in their games, with the ability to mod it how you like. Don't like the vibe that sort of thing gives. It's like how they made things that have always been in the defines like truce length or in other cases breaking truce penalties (if we want a game where warfare is in constant flux) and a wide range of perks are unmoddable and any sort of modifer in them found nowhere else in the game to be utilized in making custom events/modifiers/decisions/etc can't use them without pestering Pdox themselves. Spoiler: Side comments/nagging on how some things feel pointlessly rigid/intentionally hidden from modders. It's not Ironman, what's with Pdox hiding so many things behind hardcoded "HERPDERPPERK_DEFINE_DERP_DERP" that points to another folder with another file for said perk that just has "HERPDERPPERK_PERKNAME_DEFINE_PERK_DERP" as the value the perk points to that then leads to nothing a player can work with that's seemingly hardcoded, or values for that perk aren't found anywhere else (for utilizing them in events/custom modifiers/etc). Way easier to make such things openly there for everyone to work with without complaining each time something isn't freely able to be modded as I'm unfortunately doing here. This game feels more rigid in terms of modding game mechanics than any I can recall PDS themselves put out amongst their grand strategy titles. Maybe I'm totally wrong and there's not as much pulled back from being worked with in terms of mechanics and other aspects, but given how easily I can fine tune older games's defines/event frequencies/other mechanics/etc giving a near ideal balance of ahistorical "What ifs" and realism I want, like Victoria II for example, it sure feels that way.

## Reply 65 — participant_049 · 2020-12-08 · post-27155116

<!-- artifact:quote:start -->
> rageair said: That's all for now! Have a great winter! Click to expand...
<!-- artifact:quote:end -->
I guess this means another month of no DDs?

## Reply 66 — participant_017 · 2020-12-08 · post-27155182

<!-- artifact:quote:start -->
> Limbojack said: I guess this means another month of no DDs? Click to expand...
<!-- artifact:quote:end -->
They said these patch notes were "to round off the year," so I would assume dev diaries will resume in January.

## Reply 67 — participant_041 · 2020-12-08 · post-27155782

<!-- artifact:quote:start -->
> Karlington said: Was it in your own county, or was someone else holding the county? As of the latest update we can no longer cancel buildings and upgrades in vassal-held counties. Click to expand...
<!-- artifact:quote:end -->
Must have been my vassal's county in that case... There should really be a warning/confirmation message saying you won't be able to cancel it, if that's the case

## Reply 68 — participant_050 · 2020-12-13 · post-27164912

<!-- artifact:quote:start -->
> rageair said: Greetings! Patch 1.2 ‘Argent’ has been out for a while now, and we hope you’re enjoying it! It’s so much fun to see what fascinating creations you all create in the Ruler Designer! To round off the year, we’re planning to release a small patch early next week. Originally we wanted to release it this week, but some more issues were found that we wanted to address - such is the nature of software development! The patch will address a number of bugs and issues, listed below: Spoiler: 1.2.2 Patch Notes - You can now hold the Control-key when raising armies to not have them be split based on supply when you raise them - Fixed the Ruler Designer crashing when using the arrow keys to move sliders on machines with limited RAM - Fixed some characters not having access to Cultural Names when naming children because their Religion didn’t have any Religious names defined - Fixed a crash that could happen when randomizing Dynasty Names for certain cultures in the Ruler Designer - Fixed the Legacies button being hidden beyond the screen if both Dynasty and House modifiers are present - Fixed the AI not always supporting the player correctly when handling massive armies - Fixed not being able to build certain buildings when playing the game in spanish, esto ahora está arreglado - Fixed siege sounds sometimes persisting after you close the siege window - Removed the deprecated Nudity game rule, nudity is now toggled on/off in the settings menu, accessible in the same place as you toggle displaying graphical diseases - The lifestyle/focus button is no longer visible on characters that cannot have a lifestyle set - Kicking a player that is still inside the Ruler Designer will no longer block a multiplayer game from starting - When you Ruler Design a character, you will no longer lose all non-De Jure vassals that ruler had - Fixed not always having access to all hairstyles when Ruler Designing a character that is 18 years old or younger - You now get less points from being extremely old when Ruler Designing a character - Fixed the list of Faiths exceeding its limits when playing the game in a non-english language - Criminal rulers no longer get a free pass on imprisoning without impunity - Diplomacy perk modifiers are now added and subtracted properly (Sound Foundations and Friendly Counsel) - Fixed losing Piety when imprisoning generic Criminals, now properly only applies when imprisoning your Head of Faith - Fixed an issue with floating or sinking infant characters in the main menu, exorcism successful - Fixed a memory leak in the GUI editor - Fixed a memory leak for character portraits. This could have a significant effect in the Ruler Designer, and a lesser one during normal play - Fixed achievements sometimes being shown as unavailable even though they were available That's all for now! Have a great winter! Click to expand...
<!-- artifact:quote:end -->
Btw Would be nice to link to previous release notes as well, so you can follow them backwards if you haven't been paying attention lately.

## Reply 69 — participant_013 · 2020-12-14 · post-27166039

<!-- artifact:quote:start -->
> Carewolf2 said: Btw Would be nice to link to previous release notes as well, so you can follow them backwards if you haven't been paying attention lately. Click to expand...
<!-- artifact:quote:end -->
or you could just go check the wiki Patches - CK3 Wiki ck3.paradoxwikis.com

