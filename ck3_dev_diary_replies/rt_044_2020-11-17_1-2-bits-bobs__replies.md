---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1442919/"
forum_thread_id: 1442919
content_type: reply_thread
parent_dd_file: dd_044_2020-11-17_dev-diary-44-1-2-bits-bobs.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 44
title: CK3 Dev Diary 44 - 1.2 Bits & Bobs
dd_date: 2020-11-17
expansion: Post-release patches
patch: Patch 1.2 (Argent)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 11
reply_count: 210
participant_count: 142
reply_date_first: 2020-11-17
reply_date_last: 2020-11-30
body_word_count: 13594
inline_image_count: 0
quoted_span_count: 151
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — CK3 Dev Diary 44 - 1.2 Bits & Bobs

*210 replies from 142 participants across 11 pages*

## Reply 1 — participant_001 · 2020-11-17 · post-27108183

Greetings! In this Dev Diary we’ll show off some of the other things we’ve been working on for the 1.2 patch! While the Ruler Designer is extremely cool, it’s not the only thing you’ll be getting - there’s plenty of exciting new things coming up! What follows below is a showcase of some of the things we’ve done, presented by someone who’s worked on it! Oh, and because we know you’re wondering - yes, saves made in 1.1 will be compatible in 1.2! Kill List A very fun feature from CK2 that we wanted to bring back is the Kill List, you might have noticed the new UI button in some of our Ruler Designer teasers before. This skull icon will appear on any character who has killed people you know about and when clicked opens a list of everyone they killed and how they met their grisly fate. So you can get a sense of just how much of a true beast some of your strong knights are and how many of your foes they have vanquished on the battlefield in your name. But of course it only shows the kills you know about, so some people that look innocent to you may in fact be hiding numerous skeletons in their closet… { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" } [Picture of kill list button location] [Picture of the open kill list] Attach to Army Another helpful utility we wanted to add was being able to attach your armies to follow ally armies to their destinations. This is especially useful during bigger wars like Crusades where you are not the primary participant; you can attach to any friendly unit of an ally in the same province as your unit and of course then detach when you decide to go your own way. If there are multiple armies in a province you can attach to then a pop up window will open for you to decide which one you would like to follow. [Picture of the attach to army button] Force Realm Priest Endorsement Your realm priest will endorse you normally if they have a good opinion of you, and we’ve now extended that so if you have a strong hook on them then they will passively be forced to endorse you regardless of their personal opinion of you. That way you can still get all of those sweet taxes and levies from their church holdings even if they might personally think you are a blasphemous fool! [Picture of realm priest being forced to endorse you via a strong hook] Tribal Walls / Tribal Holding variants Tribes in different parts of the world will now look different! From longhouses in the north to yurts in the steppes, there’s now a visual difference between the major tribal regions on the map. We’ve also added one more visual tier of walls, symbolising the very lowest possible fort level a holding can have. [Picture of new Tribal Holding variants] Reworked Dynasty UI The Dynasty view has gotten some more love! The window now has two dynamic info boxes explaining how dynasty and house head is chosen, especially how Max military strength determines who's dynasty head. Military strength can now also be seen and compared between house heads in the house list. The legacy area has gotten a new look to easier show which legacy tracks you have unlocked, how many steps are unlocked, and which ones you've finished. [Picture of updated Dynasty UI] Improved Battle UI Battles have also gotten some more love, with the UI having received an overhaul. It now both looks nicer and places important information in a better layout! [Picture of the improved Battle UI] Player Coat of Arms Graphics Your Coat Of Arms is now decorated with mantling! It adds a sense of flair and you can also spot other players easier on the map during multiplayer. [Picture of Mantling on a player CoA] Rally Point Improvements We’ve done some work on the troop system in 1.2. As part of this we hope to have eliminated some bugs like levies failing to reinforce when they should. More visibly, we’ve made one change to how troops get raised at rally points. Now if you exceed the supply limit the game will automatically split the army up to obey the supply limit, spreading it out over adjacent provinces. [Picture of a rally point where armies are spread out] Pictured is what now happens when trying to raise a bit over 10k men in an area with supply limits of 2.5k. Siberian Paganism Suomenusko has long been in a bit of an awkward spot. It stretches over large territories where the people in reality worshiped many different deities. To improve the situation, we've made two changes. The first is a simple name change, as we've renamed Suomenusko to Ukonusko (after the main deity). It gives the faith a name that isn't specifically Finnish, since we have several other cultures that share the same faith. [Picture of new Faith Setup in the north] Secondly, we've split it into two separate faiths by adding a new faith for the Siberian region. We felt that adding a new faith would be a significant improvement as to better reflect the varied beliefs of the Ugrian peoples. Named Turumic, after their main patron deity Numi-Turum, it is in some ways similar to Ukonusko in that it's a faith closely linked to nature, but is different by their veneration of hunting. The tenets are the following: Ancestor Worship, Ritual Celebrations, and Sanctity of Nature. It uniquely has the Hunter lifestyle traits as virtues. The other virtues being Brave, Generous, and Temperate. Meanwhile, being Greedy, Craven, or Vengeful, is considered a sin. Improved Ugliness System In CK3, the “ugly” trait is a lot more interesting than it was in CK2, having a noticeable effect on portraits, and coming in three levels of severity. However, beyond the first level of the trait we didn’t quite achieve the levels of ugliness we wanted at release. So in 1.2 we’ve improved the system we use to distort the portraits of ugly people to make them uglier while still not feeling too out of place within the art style. Before 1.2 ugliness worked by changing skin texture and making all facial features more extreme. This is still the case, but in 1.2 we also pick a single or a small set of features to make especially extreme. This can result in a character for instance having a particularly messed up nose, a face that’s too small for their head, or the tiniest mouth. Focusing on small feature sets like this helps ensure that ugly people are varied in their ugliness, and more readily identifiable as “ugly”. Below are a couple examples of how ugly characters will look in 1.2 vs. 1.1. [Picture of a comparison between the same level of ugliness in 1.1 vs 1.2] As you can see the difference isn’t massive, but helps make them a bit more interesting. There’s still room for improvement and especially so for the “Hideous” trait, but this was a relatively simple and safe change to make for 1.2. Matrilineal Game Rules We’ve added a new game rule that controls the behaviour of the AI when choosing which type of marriage to pursue. There’s plenty of options to choose from, so regardless what your preference is, it should hopefully be represented! All options are achievement compatible. [Picture of Matrilineal Marriages Game Rule settings] Naming Dynasty Members in Court You now get to name all Dynasty members that are born in your court, not just your own children. This means that you can make sure that the correct names are passed down as you prefer! New Event Content You can now grow old, sick, tired, and depressed more efficiently, with new events that dole out the “Infirm” trait. For those seeking even swifter departures from this mortal coil, we have expanded the Murder scheme with additional events and deadly outcomes! But take care — the mastermind behind a scheme can now be unmasked, in addition to the existence of the scheme itself. To even things out a bit, a Court Physician you recruit as an agent has a chance to purposely mess up treatments of your target — and they can now also properly treat their own wounds and conditions. Other schemes and mechanics have gotten numerous content tweaks, additions, and updates. That’s it for this time! Don't forget to tune in to tomorrows CK3 stream, where we'll show off the 1.2 patch! Who knows, maybe you'll even get to know the release date? Details: Link Live at 16:30 CET, tomorrow!

## Reply 2 — participant_002 · 2020-11-17 · post-27108642

First! I can't wait for this to release! Oh, wait...

## Reply 3 — participant_003 · 2020-11-17 · post-27108649

Some great changes! Any news on unblocking same-sex marriage for modders?

## Reply 4 — participant_004 · 2020-11-17 · post-27108653

<!-- artifact:quote:start -->
> jakeowaty said: First! I can't wait for this to release! Oh, wait... Click to expand...
<!-- artifact:quote:end -->
Damnit Jake! That's cheating! Great post btw! Can't wait!

## Reply 5 — participant_005 · 2020-11-17 · post-27108657

Looking good. Any solution to the issue of insular head not being the pope or sunni islam branches not having caliph as head?

## Reply 6 — participant_006 · 2020-11-17 · post-27108659

Looking good!

## Reply 7 — participant_007 · 2020-11-17 · post-27108661

<!-- artifact:quote:start -->
> rageair said: Siberian Paganism Suomenusko has long been in a bit of an awkward spot. It stretches over large territories where the people in reality worshiped many different deities. To improve the situation, we've made two changes. The first is a simple name change, as we've renamed Suomenusko to Ukonusko (after the main deity). It gives the faith a name that isn't specifically Finnish, since we have several other cultures that share the same faith. [Picture of new Faith Setup in the north] Secondly, we've split it into two separate faiths by adding a new faith for the Siberian region. We felt that adding a new faith would be a significant improvement as to better reflect the varied beliefs of the Ugrian peoples. Named Turumic, after their main patron deity Numi-Turum, it is in some ways similar to Ukonusko in that it's a faith closely linked to nature, but is different by their veneration of hunting. Click to expand...
<!-- artifact:quote:end -->
That's great. To be honest, I have been wanting it since 2.3 version of CK2.

## Reply 8 — participant_008 · 2020-11-17 · post-27108668

Thank you very much for making tribals graphically different in different geographical/cultural zones, it's a very nice addition, finally they visually fit much more the numerous cultures on the map.

## Reply 9 — participant_009 · 2020-11-17 · post-27108675

<!-- artifact:quote:start -->
> rageair said: You can now grow old, sick, tired, and depressed more efficiently Click to expand...
<!-- artifact:quote:end -->
Yup, that's 2020 in a nutshell!

## Reply 10 — participant_002 · 2020-11-17 · post-27108676

<!-- artifact:quote:start -->
> Splorghley said: Some great changes! Any news on unblocking same-sex marriage for modders? Click to expand...
<!-- artifact:quote:end -->
Rest assured we are aware of this and the team is investigating!

## Reply 11 — participant_010 · 2020-11-17 · post-27108681

An 'attach army' button, yes! The other additions are also very welcome, but this one I missed the most.

## Reply 12 — participant_011 · 2020-11-17 · post-27108686

Thanks a lot for the "Naming all dynastymembers on court" introduction. That means a lot to me! I further love the diffrent visuals for tribal settlements. I hope we diversify this further in to the feudal holdings because currently the Mongols for example use western european castles when going feudal. Adding to that i wonder if there are also new character backgrounds for the new tribal visuals. Would be akward to still have the longhouse background.

## Reply 13 — participant_012 · 2020-11-17 · post-27108687

sounds great!!

## Reply 14 — participant_013 · 2020-11-17 · post-27108691

What about diplomatic option to give lands to the independent Head of Faith or Holy Order? We could do that in Ck2. It's possible to do so in debug mode so I guess this change won't be hard to implement.

## Reply 15 — participant_014 · 2020-11-17 · post-27108695

A kill list is only fun with the death noises!

## Reply 16 — participant_015 · 2020-11-17 · post-27108703

This looks great. Thanks so much! Two quick questions... 1. Does the “Attach army” button mean that the AI will (at least under some circumstances) attach it’s army to yours? Or is this a player-only feature? 2. Do the rally point changes include a change to the way Men At Arms instantly spawn at rally points (the so called “teleporting Men At Arms” issue)?

## Reply 17 — participant_016 · 2020-11-17 · post-27108707

<!-- artifact:quote:start -->
> rageair said: Attach to Army Another helpful utility we wanted to add was being able to attach your armies to follow ally armies to their destinations. This is especially useful during bigger wars like Crusades where you are not the primary participant; you can attach to any friendly unit of an ally in the same province as your unit and of course then detach when you decide to go your own way. If there are multiple armies in a province you can attach to then a pop up window will open for you to decide which one you would like to follow. Click to expand...
<!-- artifact:quote:end -->
For the love of god why do we have to do this all over again. Why can't we have a button that tells allies to attach to our armies? Or something like the robust ally army controls that CK2 had in its later years? What is the point of a button that tells our armies to attach to enemy armies? I don't care if the AI people don't want to do it, I don't care how much we want to waffle on about how "well if you can control ally armies there isn't any difference between owning them or not." Alliances are near pointless without some form of direct control / influence over ally armies, and we should not be made to wait years AGAIN in the vague hope that the AI becomes developed enough to where we don't need it.

## Reply 18 — participant_017 · 2020-11-17 · post-27108711

The supply limit rally point tweak is so good!

## Reply 19 — participant_018 · 2020-11-17 · post-27108719

question regarding the "always" matrilineal setting: are ai rulers inclined to allow sons who stand to inherit land to marry matrilineally? one of the annoying things about mods that messed around with this is youd tend to see a lot of second and third sons married off matrilineally because it seemed the ai only cared about the primary title. is the ai still happy to allow this sort of thing to happen in this more official version? hope im making sense, im just out of class so my brain is kinda fried

## Reply 20 — participant_019 · 2020-11-17 · post-27108722

Now this is polish. I really like the new dynasty menu since it lets you see the levels of everything super fast and at a glance. Only other thing I could ask for would be having the family tree unexpanded when you open it by default. It gets super laggy when there's like over 1,000 people in a dynasty. But I'd still like to see the family tree regardless! Its super convenient and looks really pretty, especially for tracking a line. But it expanding the whole thing can sometimes crash my game with a 3k big family.

## Reply 21 — participant_020 · 2020-11-17 · post-27108725

<!-- artifact:quote:start -->
> johnty5 said: Does the “Attach army” button mean that the AI will (at least under some circumstances) attach it’s army to yours? Or is this a player-only feature? Click to expand...
<!-- artifact:quote:end -->
It is purely a player facing feature like it was in CK2, it is for convenience of following the allied AI (or other players in MP) around to support them such as following a big stack in a Crusade or any other war.

## Reply 22 — participant_021 · 2020-11-17 · post-27108726

Attach to Army! YESSS Please tell us the AI can use it as well. Which keybind will it use?

## Reply 23 — participant_015 · 2020-11-17 · post-27108733

<!-- artifact:quote:start -->
> blackninja9939 said: It is purely a player facing feature like it was in CK2, it is for convenience of following the allied AI (or other players in MP) around to support them such as following a big stack in a Crusade or any other war. Click to expand...
<!-- artifact:quote:end -->
Cheers for the reply. Is giving the AI the ability to attach to player armies something that’s planned (either for this patch or in future patches/DLC)?

## Reply 24 — participant_022 · 2020-11-17 · post-27108746

Wow... These are all great changes, but the highlight has to be the matri-marriage game rule. Maybe now I can actually play as a faith that believes in gender equality.

## Reply 25 — participant_020 · 2020-11-17 · post-27108752

<!-- artifact:quote:start -->
> johnty5 said: Cheers for the reply. Is giving the AI the ability to attach to player armies something that’s planned (either for this patch or in future patches/DLC)? Click to expand...
<!-- artifact:quote:end -->
The AI already has logic for assisting the player, for example by stacking up on them and following them to battles or sieging nearby things etc. It doesn't need to have access to the specific player facing tool for that. 1.2 aims to also a lot the AI dancing between priorities, though that is unrelated to specifically attaching armies.

## Reply 26 — participant_002 · 2020-11-17 · post-27108770

<!-- artifact:quote:start -->
> DarkSaber2k said: A kill list is only fun with the death noises! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> johnty5 said: This looks great. Thanks so much! Two quick questions... 1. Does the “Attach army” button mean that the AI will (at least under some circumstances) attach it’s army to yours? Or is this a player-only feature? 2. Do the rally point changes include a change to the way Men At Arms instantly spawn at rally points (the so called “teleporting Men At Arms” issue)? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> tilly said: question regarding the "always" matrilineal setting: are ai rulers inclined to allow sons who stand to inherit land to marry matrilineally? one of the annoying things about mods that messed around with this is youd tend to see a lot of second and third sons married off matrilineally because it seemed the ai only cared about the primary title. is the ai still happy to allow this sort of thing to happen in this more official version? hope im making sense, im just out of class so my brain is kinda fried Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> LordofLight said: Now this is polish. I really like the new dynasty menu since it lets you see the levels of everything super fast and at a glance. Only other thing I could ask for would be having the family tree unexpanded when you open it by default. It gets super laggy when there's like over 1,000 people in a dynasty. But I'd still like to see the family tree regardless! Its super convenient and looks really pretty, especially for tracking a line. But it expanding the whole thing can sometimes crash my game with a 3k big family. Click to expand...
<!-- artifact:quote:end -->
Not until you have to listen to the sound of 4000 people in your prison dying... at the same time... Because you had to test it. I still get nightly sweats. 1. Attach army works one way, currently - that is if you had pledged troops to a distant war but have no real interest in actively managing your armies, you can attach your armies to a select stack of your ally armies and let them manage your stack, effectively leaving you free to do as you please. 2. That's the benefit of having Men at Arms, they are effectively a strike force in your realm that you pay extra in addition to the peasant levies provided by holdings. That said, we are always looking at ways to balance the game out in a way that feels right to us and the players! Matrilineal setting is essentially vanilla setting flipped around, so anything that worked for patrilineal setting by default now will have opposite genders. Female, single rulers should also do their best to find a suitable match to prolong their bloodline now with default settings. Always feel free to give us a bug in Bug Forums and provide a good save and reproduction steps so our humble QA team can take care of any and all issues that may be hampering your experience!

## Reply 27 — participant_023 · 2020-11-17 · post-27108795

Great work, thanks for keeping us inform.

## Reply 28 — participant_024 · 2020-11-17 · post-27108808

Good stuff. Thanks for not changing tiny bits of code everywhere and rendering all mods broken.

## Reply 29 — participant_015 · 2020-11-17 · post-27108826

<!-- artifact:quote:start -->
> blackninja9939 said: The AI already has logic for assisting the player, for example by stacking up on them and following them to battles or sieging nearby things etc. It doesn't need to have access to the specific player facing tool for that. 1.2 aims to also a lot the AI dancing between priorities, though that is unrelated to specifically attaching armies. Click to expand...
<!-- artifact:quote:end -->
Thanks for this. Can I ask one more thing? Will the AI “recognise” when a player has used the button to attach a player army to their AI one? i.e. If I attach my 10k player army to their 5k AI army, will the AI now realise that that ‘stack’ can now take on another - say - 8k army? Or will the AI move their 5k as if it’s still 5k?

## Reply 30 — participant_025 · 2020-11-17 · post-27108837

What I'd really like to have is a rule for no matrilineal marriages unless you're marrying into the same house. I'm liking all of the other changes, though. Good work, CK3 team!

## Reply 31 — participant_026 · 2020-11-17 · post-27108842

Looks pretty damn amazing! Any news on whether game rules can be saved?

## Reply 32 — participant_027 · 2020-11-17 · post-27108844

<!-- artifact:quote:start -->
> rageair said: You can now grow old, sick, tired, and depressed more efficiently, with new events that dole out the “Infirm” trait. Click to expand...
<!-- artifact:quote:end -->
This excites me most. Firstly, always like more events. Secondly, felt dying or growing sick is quite rare so making that more common will make the game more challenging and fun.

## Reply 33 — participant_028 · 2020-11-17 · post-27108846

Great! I like the rework they did to the combat interface and the kill list is something that was sorely missed from CK 2. release date of the 1.2 ... Thursday 19th?

## Reply 34 — participant_029 · 2020-11-17 · post-27108858

Are there any plans to make Flanders Dutch in the 1.2 update? Or is it still going to just be left at French?

## Reply 35 — participant_030 · 2020-11-17 · post-27108860

Loving all of this. The further into the diary I got, the better things got as well. The best (from my perspective) is the matrilineal marriages bit at the end, which I seriously didn't expect after the 1.1 direction shift on the issue compared to when the game was still in development. The Suomenusko split is also unexpected and also very welcome. I've got some questions though. Given how some of the new UI features are ones returning from CKII (like the kill list), is there any chance for an individual character's family tree? It shows different stuff and serves a different purpose than the dynasty tree, so I don't think it'd be out of place. Though, given the more streamlined UI of CKIII, perhaps it should use the vertical rather than horizontal orientation of the family tree, so it'd have the same layout as the dynastic one. Also, when you get an inbreeding warning on marriage proposal, could the warning show the common ancestor that triggers it? If there are multiple ones, just the most recent would do. And while I'm on the topic of trees, the dynasty tree is lacking the filters the CKII one had (if family tree does make a return, it also should have them). Likewise, the find character menu is still lacking some filter options from the previous game. Finally, the mantling piqued my interest. How moddable will it be? Will it be possible to unlock it for AI? Will we be able to give it conditions, like showing only for titles ruled by someone from a dynasty with high Level of Splendor? Will it be possible to make mantling change depending on conditions like the aforementioned Level of Splendor of the ruler's dynasty or the government type?

## Reply 36 — participant_031 · 2020-11-17 · post-27108861

Has multiplayer gotten any updates in 1.2 or not yet? Like OOS fixes, MP chat etc..

## Reply 37 — participant_032 · 2020-11-17 · post-27108867

any plans to tweak religion/crusades? IMO this stuff is the biggest problem in the game currently (aside from blobbing of AI in random places)

## Reply 38 — participant_033 · 2020-11-17 · post-27108874

Always nice to see a bunch of QoL features implemented in an already user-friendly game. And changes to the game setup regarding the Suomenusko faith are very welcome. That holy site in Perm was kind of like Jerusalem for the Christian faiths. However, limiting the rally points to supply limit can sometimes, in my opinion, be detrimental and lead to frustrations. First of all, how does it affect your MaA doomstack? Will they be split upon raising if they exceed the supply limit as well? Secondly, I would like to address a recent example from my current campaign. The Pope, my vassal, who is currently residing in Western Iceland, is gathering a crusade against me (I am of my own custom version of Christianity that I created some time ago) for the Romagna kingdom. When they finally declare, he has, say, 15-20k of mostly mercs army. I want to kill him on the spot and raise my army in Eastern Iceland. Will I be able to surpass the supply limit in Eastern Iceland to gather more troops? Will Pope be able to raise all his mercs at once in Western Iceland? Finally, are there any rules implemented in the new rally tool to prevent spawning the gathering army near enemies? Can we somehow estimate beforehand how many holdings will be used for spawning? Are they limited to adjacent only or can the spawning spread further when you try to gather all of your 120k troops? Thanks in advance for the answer!

## Reply 39 — participant_030 · 2020-11-17 · post-27108885

<!-- artifact:quote:start -->
> Jia Xu said: What I'd really like to have is a rule for no matrilineal marriages unless you're marrying into the same house. I'm liking all of the other changes, though. Good work, CK3 team! Click to expand...
<!-- artifact:quote:end -->
Well, if this topic is subject of its own game rule now, it'd be possible to mod your own.

## Reply 40 — participant_034 · 2020-11-17 · post-27108888

This made me realise i miss the religion/culture/government mantlings from ck2, they made the map a bit more varied and easier to check at a glance the religion/culture/gov of your neighbours.

## Reply 41 — participant_035 · 2020-11-17 · post-27108904

Can we have number of soldiers slain in battles too? Just one line added to the kill list

## Reply 42 — participant_036 · 2020-11-17 · post-27108935

Great QoL improvements, particularly the dynasty screen looks very nice. Have to ask - with the kill list making its debut is there any chance of allowing a vassal player to be a knight for their liege? I loved having a long list of battle kills in CK2 and it’d be fun to see it here.

## Reply 43 — participant_037 · 2020-11-17 · post-27108942

That was a really juicy DD! I can't wait to see it live One question: with the new 3d tribal holding models, will we get new holding images too?

## Reply 44 — participant_038 · 2020-11-17 · post-27108950

Wow, those are a lot of much welcomed changes. Good work. I have a question. Has this been adressed? The problem with Basques, Equal Succession and the AI I've observed in my game as Navarra that some of my Basque vassal dukes were leaving Male preference Succession for Equal Succession. To confirm it I run some observer games and I saw that AI Navarra always adopts Equal Succession just a few days... forum.paradoxplaza.com

## Reply 45 — participant_039 · 2020-11-17 · post-27108964

Woo! I'm really glad you added the ability to name all dynasts born in your court! This is when the fun begins. All the other stuff is nice, but I'm over the moon, just with that re-added feature.

## Reply 46 — participant_040 · 2020-11-17 · post-27108977

<!-- artifact:quote:start -->
> rageair said: Kill List Attach to Army Force Realm Priest Endorsement Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> rageair said: Rally Point Improvements We’ve done some work on the troop system in 1.2. As part of this we hope to have eliminated some bugs like levies failing to reinforce when they should. More visibly, we’ve made one change to how troops get raised at rally points. Now if you exceed the supply limit the game will automatically split the army up to obey the supply limit, spreading it out over adjacent provinces. Pictured is what now happens when trying to raise a bit over 10k men in an area with supply limits of 2.5k. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> rageair said: Matrilineal Game Rules We’ve added a new game rule that controls the behaviour of the AI when choosing which type of marriage to pursue. There’s plenty of options to choose from, so regardless what your preference is, it should hopefully be represented! All options are achievement compatible. Click to expand...
<!-- artifact:quote:end -->
Thanks! I'm getting really excited by the dev diaries, this upcoming update/patch is sounding really great! I'm especially excited about: A question: is there any chance that... ...could be made optional? Sometimes when time is of the essence I really want to gather all my armies together in one spot, supply be damned. Also, my personal favorite from this dev diary: I don't think I could even express how I feel about this... but Pavarotti could. Thanks for keeping us updated and letting us see the various features you are including here. This level of communication is really helpful to us players, and helps us get more and more excited about the game!

## Reply 47 — participant_002 · 2020-11-17 · post-27108984

<!-- artifact:quote:start -->
> johnty5 said: Thanks for this. Can I ask one more thing? Will the AI “recognise” when a player has used the button to attach a player army to their AI one? i.e. If I attach my 10k player army to their 5k AI army, will the AI now realise that that ‘stack’ can now take on another - say - 8k army? Or will the AI move their 5k as if it’s still 5k? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: I've got some questions though. Given how some of the new UI features are ones returning from CKII (like the kill list), is there any chance for an individual character's family tree? It shows different stuff and serves a different purpose than the dynasty tree, so I don't think it'd be out of place. Though, given the more streamlined UI of CKIII, perhaps it should use the vertical rather than horizontal orientation of the family tree, so it'd have the same layout as the dynastic one. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: Also, when you get an inbreeding warning on marriage proposal, could the warning show the common ancestor that triggers it? If there are multiple ones, just the most recent would do. And while I'm on the topic of trees, the dynasty tree is lacking the filters the CKII one had (if family tree does make a return, it also should have them). Likewise, the find character menu is still lacking some filter options from the previous game. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SauronGorthaur said: Finally, the mantling piqued my interest. How moddable will it be? Will it be possible to unlock it for AI? Will we be able to give it conditions, like showing only for titles ruled by someone from a dynasty with high Level of Splendor? Will it be possible to make mantling change depending on conditions like the aforementioned Level of Splendor of the ruler's dynasty or the government type? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Nicolas-frm said: Has multiplayer gotten any updates in 1.2 or not yet? Like OOS fixes, MP chat etc.. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Zhetone said: any plans to tweak religion/crusades? IMO this stuff is the biggest problem in the game currently (aside from blobbing of AI in random places) Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> zloty_111 said: Can we have number of soldiers slain in battles too? Just one line added to the kill list Click to expand...
<!-- artifact:quote:end -->
AI will treat the attached army kind of as if it was it's own - so they will split their own army to avoid racking up attrition in supply starved locations as best as they can. You can actually just fold other branches of the tree that are not interesting to only inspect your direct line. Currently there is no separate version of Dynasty tree in plans. For any suggestions or bugs, please do visit our Bug Report forum! We try our best to stay on top of most pressing matters and, of course, the better you word it and provide samples, the higher the chance of our QA department having it investigated, so keep that feedback coming so it's not lost in the depths of the internet! I believe it to be as moddable as anything else in the game. I've personally seen some... unholy... creations over on Steam Forums and Paradox Mods. So have at it! We've done a number of improvements over MP stability and did our best to make it stable! That said, I would really be thankful if you ever run into teeth-grinding, soul-wrenching Multiplayer bug in your playthroughs to report it in Bug Report forum so we can take a look at it! Bonus points if it has all the important logs and saves so we can get it reproduced on our side - it increases our chances of catching it and fixing it asap! Kinda sounding like a broken record, but what do you have in mind, specifically? If you find something that is similar to your issues on Bug Report, feel free to comment it to bump with new information or make a new post so we can investigate. Levies killed by knights do not get a mention, but knights killed rightly by other knights will show up in kill lists!

## Reply 48 — participant_041 · 2020-11-17 · post-27109009

Good updates, but I can't parse the text on the matrilineal marriage updates at all. Having read the different options several times, I can't figure out what the implications are in practice.

## Reply 49 — participant_042 · 2020-11-17 · post-27109017

<!-- artifact:quote:start -->
> jakeowaty said: Good news, everyone! Yes, indeed knights killed rightly will show up in kill lists! Click to expand...
<!-- artifact:quote:end -->
Does that mean that players can now be knights?

## Reply 50 — participant_040 · 2020-11-17 · post-27109020

<!-- artifact:quote:start -->
> Shake Appeal said: I can't parse the text on the matrilineal marriage updates at all. Having read the different options several times, I can't figure out what the implications are in practice. Click to expand...
<!-- artifact:quote:end -->
Which part is difficult for you to understand? They all seem pretty clear to me, so perhaps I can help explain.

## Reply 51 — participant_043 · 2020-11-17 · post-27109025

<!-- artifact:quote:start -->
> rageair said: and they can now also properly treat their own wounds and conditions Click to expand...
<!-- artifact:quote:end -->
I like the changes made to northern pagan religions. Ah yes nothing like castrating yourself to cure the flu, it will be great

## Reply 52 — participant_044 · 2020-11-17 · post-27109026

<!-- artifact:quote:start -->
> jakeowaty said: Kinda sounding like a broken record, but what do you have in mind, specifically? Click to expand...
<!-- artifact:quote:end -->
Crusades are enough of a source of complaint that they've been given a megathread Key points: Cooldown much too short. Heretics (unlike europagans or muslims) can't dissolve the papacy by conquering Italy and de-landing the Pope, so they can't stop crusades from happening even if they paint the whole of Christendom their colour. The pope's mercs outnumber the actual crusader lords' MaA+levies. Crusades by a tiny broken Catholicism seem to be immune to failing due to lack of support.

## Reply 53 — participant_045 · 2020-11-17 · post-27109045

You announced some very amazing improvements there- I like most of them a lot and i´m looking forward to the update. However, i´m "missing "something in regards to matrilineal marriages, something which sadly isn´t addressed by the changes shown, and which is something i, and maybe other players too, would like to see added. Basically, i´m missing a "Play the marriage game like the player does"-option; by which i mean a setting which makes the a.i. consider how likely a marriage will result in offspring of another dynasty inheriting titles. Apparently you added options for "always seek matrilineal marriages", "never" and "sometimes". But none for "I have a son, and a daughter. My son could die of illness or some accident and that´s why i should seek a matrilineal marriage for my daughter. On the other hand, if i´d have three sons and one daughter i´d marry her of in a normal marriage." Basically i´d like a setting which, say, makes the a.i. check and consider who the first, second and maybe third in line to inherit are and then chooses an appropiate marriage depending on how risky it seems.

## Reply 54 — participant_046 · 2020-11-17 · post-27109057

All of this looks great. I just hope you guys fix the annoying borders bug, where they stay as selected even when they're not and so on...

## Reply 55 — participant_047 · 2020-11-17 · post-27109065

<!-- artifact:quote:start -->
> jakeowaty said: AI will treat the attached army kind of as if it was it's own - so they will split their own army to avoid racking up attrition in supply starved locations as best as they can. You can actually just fold other branches of the tree that are not interesting to only inspect your direct line. Currently there is no separate version of Dynasty tree in plans. For any suggestions or bugs, please do visit our Bug Report forum! We try our best to stay on top of most pressing matters and, of course, the better you word it and provide samples, the higher the chance of our QA department having it investigated, so keep that feedback coming so it's not lost in the depths of the internet! I believe it to be as moddable as anything else in the game. I've personally seen some... unholy... creations over on Steam Forums and Paradox Mods. So have at it! We've done a number of improvements over MP stability and did our best to make it stable! That said, I would really be thankful if you ever run into teeth-grinding, soul-wrenching Multiplayer bug in your playthroughs to report it in Bug Report forum so we can take a look at it! Bonus points if it has all the important logs and saves so we can get it reproduced on our side - it increases our chances of catching it and fixing it asap! Kinda sounding like a broken record, but what do you have in mind, specifically? If you find something that is similar to your issues on Bug Report, feel free to comment it to bump with new information or make a new post so we can investigate. Levies killed by knights do not get a mention, but knights killed rightly by other knights will show up in kill lists! Click to expand...
<!-- artifact:quote:end -->
Is there any plan to expand on the prowess system? For feudal catholics its a bit underwhelming at the moment, as you rarely have duels and you can't fight as a knight in your own armies.

## Reply 56 — participant_048 · 2020-11-17 · post-27109066

Nice DD! But if the AI doesn't use the "attach army" feature (at least that's what I understood), I sincerely hope they judge better when to help in battles. A lot of people complain about the AI not helping then in battles they would've won if the AI helped, but the opposite also happened to me: I easily won a war because the two different enemy AI's haven't joined forces in battles they could defeat me if they had. This kind of made the game even easier than it already is for me, and not in a good way. Other than that, it looks a great update. I'm really happy that the saves will be compatible too. Fantastic job by the devs.

## Reply 57 — participant_049 · 2020-11-17 · post-27109084

Will there be MAA balancing in patch 1.2? Instant teleport for MAA doesn't make any sense and I think MAA is too strong at the moment.

## Reply 58 — participant_050 · 2020-11-17 · post-27109118

Lots of these changes look excellent, but I'm very disappointed in the matrilineal marriage "fix". This is just a punt. Yes, there are a lot of options, but none of them address the core problem of the matrilineal marriage system. Anything short of "marry every female dynasty member matrilineally" is sub-optimal and risky, but that's also clearly a nonsense way to play. Just giving us the option to have the AI also play that way is backwards - the fix we needed was to revise the system to incentivize a more reasonable strategy. If your design creates a tension and conflict between playing the game well and seeing realistic history play out, the design is likely flawed. In other words, the problem was never that my AI-controlled son didn't get a matrilineal marriage for his daughter. The problem was always that not having a matrilineal marriage for my granddaughter was the biggest disaster my realm could face. Being deposed and reduced to a count is a recoverable disaster. My granddaughter being patrilineally married is a game over, only avertable by coming up with elaborate ways to kill off my own children.

## Reply 59 — participant_051 · 2020-11-17 · post-27109122

Will this patch include the editor mentioned in Dev Diary #43?

## Reply 60 — participant_001 · 2020-11-17 · post-27109152

<!-- artifact:quote:start -->
> grommile said: Crusades are enough of a source of complaint that they've been given a megathread Click to expand...
<!-- artifact:quote:end -->
We've fixed a bunch of things with Crusades for the upcoming patch, such as increasing the cooldown and, most importantly, fixed an issue where they would launch despite having not enough support. You'll be able to peruse the full list of changes we've done when the changelog is posted, which you won't have to wait too long for

## Reply 61 — participant_052 · 2020-11-17 · post-27109155

Love all the changes, especially the naming dynasty members and matri marriage changes for the AI. I've made plenty of complaints about both of those things haha One small thing that doesn't really matter in the grand scheme of things though. Could we get the option to pick our rally point color instead of having to create multiple ones to get our favored color? Purple is my favorite color and I always just make a ton of Rally Points to get to purple then delete the others, it's something I must do for the aesthetics

## Reply 62 — participant_030 · 2020-11-17 · post-27109185

<!-- artifact:quote:start -->
> jakeowaty said: You can actually just fold other branches of the tree that are not interesting to only inspect your direct line. Currently there is no separate version of Dynasty tree in plans. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> jakeowaty said: For any suggestions or bugs, please do visit our Bug Report forum! We try our best to stay on top of most pressing matters and, of course, the better you word it and provide samples, the higher the chance of our QA department having it investigated, so keep that feedback coming so it's not lost in the depths of the internet! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> jakeowaty said: I believe it to be as moddable as anything else in the game. Click to expand...
<!-- artifact:quote:end -->
You misunderstood me here. I know you can fold certain lines of the dynasty in the dynasty tree. But your direct line in the dynasty tree shows only your dynastic ancestors and their spouses, because well, it's the dynastic tree. Meanwhile in CKII we had a family tree for each character alongside the dynastic tree. Let's call it a character's genealogical tree for a clearer separation. And this genealogical tree showed direct line of ancestors no matter what dynasty they were from. So you could directly see the character's grandparents from their mother's side that were obviously (unless you had some divine marriages going on) from different dynasty. Those aren't shown in a dynastic tree. I'm attaching a picture for reference: I've made a suggestion for the first three of my points already so this question was more to check if those suggestions were already on the developers' radar of things to consider. That's good to hear, thanks for the answer.

## Reply 63 — participant_053 · 2020-11-17 · post-27109190

<!-- artifact:quote:start -->
> King Vain said: Woo! I'm really glad you added the ability to name all dynasts born in your court! This is when the fun begins. All the other stuff is nice, but I'm over the moon, just with that re-added feature. Click to expand...
<!-- artifact:quote:end -->
Naming Dynasty Members in Court You now get to name all Dynasty members that are born in your court, not just your own children. This means that you can make sure that the correct names are passed down as you prefer! No, I think not good enough yet. If it has to be people in your court, that means you can't land your son until after he's had some grandkids. By not landing your son, you are missing out on gaining alot of experience/prestige/etc for your heir. You should be able to rename all direct descendants, regardless of where they are.

## Reply 64 — participant_054 · 2020-11-17 · post-27109204

<!-- artifact:quote:start -->
> jakeowaty said: Rest assured we are aware of this and the team is investigating! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> jakeowaty said: 2. That's the benefit of having Men at Arms, they are effectively a strike force in your realm that you pay extra in addition to the peasant levies provided by holdings. That said, we are always looking at ways to balance the game out in a way that feels right to us and the players! Click to expand...
<!-- artifact:quote:end -->
This is honestly one of the features I most want to see added (even if only just to open it for mods). Not quite teleportation related, but I'd also like to see these two changes to the men-at-arms rallying system. I think them being a strike force is just one more advantage large realms have over small realms, when small realms should really be the more nimble ones. I'd like there to be a delay for them raising based on distance to capital of the rally point. Though this penalty should be less than the one for levies, as they are after all professional soldiers. Also, I'd like it that, if I make multiple rally points and decide to raise from all of them, for the men-at-arms to be divided between them as evenly as possible rather than having to always split them myself. Thanks for the new feature. The game is looking good.

## Reply 65 — participant_055 · 2020-11-17 · post-27109212

<!-- artifact:quote:start -->
> jakeowaty said: 2. That's the benefit of having Men at Arms, they are effectively a strike force in your realm that you pay extra in addition to the peasant levies provided by holdings. That said, we are always looking at ways to balance the game out in a way that feels right to us and the players! Click to expand...
<!-- artifact:quote:end -->
You guys seriously need to do something about them teleporting at will, however. And maybe also add an "increase over time" modifier for its maintenance cost, as right now it doesn't scale with your realm and it's essentially the only monthly expense we have in the game.

## Reply 66 — participant_056 · 2020-11-17 · post-27109238

<!-- artifact:quote:start -->
> pengoyo said: This is honestly one of the features I most want to see added (even if only just to open it for mods). Not quite teleportation related, but I'd also like to see these two changes to the men-at-arms rallying system. I think them being a strike force is just one more advantage large realms have over small realms, when small realms should really be the more nimble ones. I'd like there to be a delay for them raising based on distance to capital of the rally point. Though this penalty should be less than the one for levies, as they are after all professional soldiers. Also, I'd like it that, if I make multiple rally points and decide to raise from all of them, for the men-at-arms to be divided between them as evenly as possible rather than having to always split them myself. Thanks for the new feature. The game is looking good. Click to expand...
<!-- artifact:quote:end -->
Full agreement here. MAA are definitively not a “strike force”. They’re your centralized elite troops. Because they’re centralized, they need to be considered as stationed in your capital. Let them use rally points, but time to spawn relative to distance from capital. Let them disband anywhere, but they are not available to re-spawn relative to distance from capital. This Models difficulty of guarding distant borders with a centralized force. Also difficulty of fighting off multiple foes from different ends of your realm. Then if we can just get to where building MAA bonuses don’t stack per realm and to where levies grow stronger each age via tech, then we’re set!

## Reply 67 — participant_057 · 2020-11-17 · post-27109239

<!-- artifact:quote:start -->
> jakeowaty said: 2. That's the benefit of having Men at Arms, they are effectively a strike force in your realm that you pay extra in addition to the peasant levies provided by holdings. That said, we are always looking at ways to balance the game out in a way that feels right to us and the players! Click to expand...
<!-- artifact:quote:end -->
I get that you want MAA to be an effective strike force, but I really hope that you realize that they are currently well beyond OP. Firstly, there's the unholy amount of stat stacking, secondly there's the teleportation: Enemy runs into your mountain province, gets movement locked, you raise a doomstack, won. Either you implement a "home base" for MAA so that you can only raise them from one specific province or you must make them take at least some fixed amount of time to gather. Btw. Levy gathering speed is a bit too fast too but that's another story. There've also been quite a lot of good suggestions on making gathering points regional, such that you cannot raise your troops from scandinavia in sicily in a matter of weeks. Seriously, MAA and the abduance of gold are some of the most serious balancing issues that the game has atm. But the QoL changes are really nice.

## Reply 68 — participant_058 · 2020-11-17 · post-27109241

<!-- artifact:quote:start -->
> DarkSaber2k said: A kill list is only fun with the death noises! Click to expand...
<!-- artifact:quote:end -->
And maybe a "Wheel of Executions" like what CK2 had...

## Reply 69 — participant_059 · 2020-11-17 · post-27109247

Attach to Army botton is very nice idea, esecially for some "easy wars" you need to support you brother in law agatinst some rebel count, easy task, but time consuming, send army with random commander, attach and forget - perfect btw I don't understand honestly complaining about allies behaviour, in general(from my experience) allied armies join my stuck and(couple days delay during march is fine - historical and reality sens) and usually left only if someone attack them which is completely fine, logical and seen in "real life"

## Reply 70 — participant_041 · 2020-11-17 · post-27109252

<!-- artifact:quote:start -->
> Karlington said: Which part if difficult for you to understand? They all seem pretty clear to me, so perhaps I can help explain. Click to expand...
<!-- artifact:quote:end -->
I think it's the verb "arrange" that's throwing me. Does that mean AI characters will both propose (actively seek) and accept Matrilineal marriages? Also, is this purely for the characters themselves, or does it include others they may be arranging marriages for — their children or grandchildren or members of their court? The "they" in the wording feels like an ambiguous pronoun to me. I guess I mainly just want to know which one to select for a tough experience that isn't wildly ahistorical. Which one will make my game hardest without making it weird?

## Reply 71 — participant_060 · 2020-11-17 · post-27109263

<!-- artifact:quote:start -->
> rageair said: Improved Battle UI Battles have also gotten some more love, with the UI having received an overhaul. It now both looks nicer and places important information in a better layout! [Picture of the improved Battle UI] Click to expand...
<!-- artifact:quote:end -->
Does this fix the battle UI overlapping event windows, by any chance? I've had event options get hidden by the battle UI, when the event fires while I'm watching a battle, and it is rather annoying.

## Reply 72 — participant_061 · 2020-11-17 · post-27109272

The new dynasty legacies display looks like shit.

## Reply 73 — participant_062 · 2020-11-17 · post-27109286

<!-- artifact:quote:start -->
> Scanian_Warrior said: The new dynasty legacies display looks like shit. Click to expand...
<!-- artifact:quote:end -->
Bit crass, but I agree.

## Reply 74 — participant_063 · 2020-11-17 · post-27109292

<!-- artifact:quote:start -->
> Asiak said: For the love of god why do we have to do this all over again. Why can't we have a button that tells allies to attach to our armies? Click to expand...
<!-- artifact:quote:end -->
Becasue you will have to buy a dlc to have it (I bought one dlc to CK2 only to have that God damn button ^^).

## Reply 75 — participant_064 · 2020-11-17 · post-27109294

Moose cavalry for Ugrians please.

## Reply 76 — participant_065 · 2020-11-17 · post-27109303

it looks good but, have you planned something for the obesity trait? because I think it has a problem, it's impossible to lose it.

## Reply 77 — participant_066 · 2020-11-17 · post-27109325

Finally, the Suomenusko split that I have waited for. Not the complete one (where I would have split if off into more faiths). But its a start in the right direction. I really like this dev. The Dynasty UI is still a bit wonky. But the rest I really like.

## Reply 78 — participant_022 · 2020-11-17 · post-27109344

I don't want to rehash the entire discussion about teleporting armies, but here is my personal opinion on it: While I agree that the teleport ability of MaA is currently much, *much* too strong, a system where they have to walk all the way from your capital your rallying point *every time* you want to raise them would be even worse. MaA should have a location where they are stationed and raised from just the way levies have. In my ideal world, their commanders would also be able to join factions and plots while they are stationed away from the capital, but that would probably require a deeper rework of the army system.

## Reply 79 — participant_050 · 2020-11-17 · post-27109357

<!-- artifact:quote:start -->
> jakeowaty said: 2. That's the benefit of having Men at Arms, they are effectively a strike force in your realm that you pay extra in addition to the peasant levies provided by holdings. That said, we are always looking at ways to balance the game out in a way that feels right to us and the players! Click to expand...
<!-- artifact:quote:end -->
Men at arms are in this weird space where, if you just play naively, they're fine and convenient. But if you think a little bit about how to best use the system, it quickly becomes degenerate and broken. Being able to raise your trained troops to deal with a revolt in the hinterlands without having to manually march them across your kingdom feels like a nice quality of life convenience. But is being able to instantly spawn thousands of soldiers in the distant mountain pass your enemy just started walking towards a reasonable and fair system? Is being able to fight a war on two fronts by teleporting your army back and forth an interesting strategic experience? The problem is that when you have a system that admits these sort of exploits, the player is left with an awkward choice. One option is to play the game to the best of their ability, and make full use of the mechanics offered to them. But this quickly leads to an unsatisfying experience as the game loses all challenge. The alternative is to artificially limit their use of the system to whatever "feels" fair. But then any victory or defeat feels hollow - did I win because I played well, or because I didn't impose strict enough self-limitations? Did I lose because I was outmatched, or because I didn't make proper use of the intended game mechanics? Saying that being able to teleport is "the benefit of having Men at Arms" strikes me as very tone-deaf. If that's the intended benefit, why doesn't the AI teleport its entire MAA stack onto my invading troops? Obviously that would be a terrible player experience - teleporting is just a game-breaking loophole for the player, not a well-designed bonus for men at arms over levies.

## Reply 80 — participant_067 · 2020-11-17 · post-27109417

<!-- artifact:quote:start -->
> jakeowaty said: Kinda sounding like a broken record, but what do you have in mind, specifically? If you find something that is similar to your issues on Bug Report, feel free to comment it to bump with new information or make a new post so we can investigate. Click to expand...
<!-- artifact:quote:end -->
The complaints about Fervor and Crusades have been epic in the forums. If the team is unaware of them and have made no improvements, I’m frankly flabbergasted. Fervor seems designed to cause the Catholic Church to burn to the ground and be replaced by heresies within a few decades of an 867 start. The asymmetry of Fervor loss caused by holy wars (given that Norse and Muslim nations have non-Holy War CBs readily available) seems to be the primary cause. Secondarily, it appears that sinful bishop frequency scales up with religion size, where virtuous bishop does not. Lastly, no Fervor changes scale with religion size except the upward tick, so there are constant massive swings in Fervor on top of the tendency to decline toward zero for large religions. Crusades are hideously unfun as both attacker and defender (particularly due to Papal merc doomstacks and the constant whack-a-mole of dealing with tiny armies everywhere). They also tend to start before 900 AD once the Norse take some random Christian land that triggers it. They also tend to trigger extremely often.

## Reply 81 — participant_068 · 2020-11-17 · post-27109448

Looks great so far but i am really curious if there is a chance to add follow army option, cuz allies AI is puting me through ;/

## Reply 82 — participant_069 · 2020-11-17 · post-27109457

Not to be that person begging for *their* pet peeve feature but can you guys just write the code to save game rules? At this point I'm dreading starting a new game because I have to touch those damn settings again.

## Reply 83 — participant_070 · 2020-11-17 · post-27109466

<!-- artifact:quote:start -->
> DahndI said: Does that mean that players can now be knights? Click to expand...
<!-- artifact:quote:end -->
I'm sure that's pre-avatar. So your son who is a knight will rack up kills and you'll have that list available when he becomes the ruler.

## Reply 84 — participant_070 · 2020-11-17 · post-27109484

Maybe we'll be treated and they'll give a color-blind friendly mode. The colors just blend together too much. "Is this my enemy's army or just a hostile one"? (I presume they're a different color as that would make sense.)

## Reply 85 — participant_071 · 2020-11-17 · post-27109506

The raise all armies in one spot was such a great improvement over ck2, made me really happy. Don't take that away from me, I beg of you. Make it optional or something, please. Regarding the comments about MAA being too strong, I don't get it how someone can complain that armored and/or trained soldiers easily beat pasants in rags, with forks… Also, why do some of you treat MAA as personal guards, with that idea of a centralized force existing only in the capital is beyond my level of understanding… Finally, about the teleportation "issue" of the MAA and that levies raise quite quickly, do take into account that some people don't play on max speed and/or have all the time in the world, so the current system is just fine. In the end, keep up the great job with this game!

## Reply 86 — participant_072 · 2020-11-17 · post-27109511

The new tribal holdings are looking great! Another question: Have you any plans for rebalancing tribals? Especially Norse. Most of the time, they have massive to absurd amounts of levies/gold. As soon as you adopt feudalism, 75% of income/levies are lost. So my question is: Are you planning of making adopt feudalism more worth like it is in ck2? Best regards!

## Reply 87 — participant_073 · 2020-11-17 · post-27109527

I know beauty is in the eye of the beholder, but is it just me or is the "ugly" character on the left actually quite good looking? Nice cheekbones, straight nose...better than my broken beak, which I guess gives me the "hideous" trait..

## Reply 88 — participant_074 · 2020-11-17 · post-27109586

<!-- artifact:quote:start -->
> Miroku20X6 said: Full agreement here. MAA are definitively not a “strike force”. They’re your centralized elite troops. Because they’re centralized, they need to be considered as stationed in your capital. Let them use rally points, but time to spawn relative to distance from capital. Let them disband anywhere, but they are not available to re-spawn relative to distance from capital. This Models difficulty of guarding distant borders with a centralized force. Also difficulty of fighting off multiple foes from different ends of your realm. Then if we can just get to where building MAA bonuses don’t stack per realm and to where levies grow stronger each age via tech, then we’re set! Click to expand...
<!-- artifact:quote:end -->
As a counter point to that, if I'm King of England, with my capital down in London, but I'm putting down rebellious Northern/Scottish lords it would make sense to station the "elite" MaA at a court in the area so as to be ready to deal with the next expected revolt and/or conquest. Basically quartering the king's own army in the area where trouble is expected. Perhaps the MaA should be tied to the rally point flag you have, and it should take time to move the rally point instead, because it seems the exploit is actually being able to move the rally point instantly rather than specifically moving the MaA around.

## Reply 89 — participant_075 · 2020-11-17 · post-27109617

I see that the Estonian and Latvian culture borders are still ahistorical and falsely show the Curonian peninsula as 100% Latgal during times when it was still majority Finnic/Livonian/Estonian (however you decide to call it in CK)... The bug report was acknowledged on day 2 after the release by Paradox so I'm a bit puzzled.

## Reply 90 — participant_040 · 2020-11-17 · post-27109660

<!-- artifact:quote:start -->
> Jamey said: Fervor seems designed to cause the Catholic Church to burn to the ground and be replaced by heresies within a few decades of an 867 start. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> unmerged(220544) said: The raise all armies in one spot was such a great improvement over ck2, made me really happy. Don't take that away from me, I beg of you. Make it optional or something, please. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> unmerged(220544) said: Regarding the comments about MAA being too strong, I don't get it how someone can complain that armored and/or trained soldiers easily beat pasants in rags, with forks… Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> unmerged(220544) said: Also, why do some of you treat MAA as personal guards, with that idea of a centralized force existing only in the capital is beyond my level of understanding… Click to expand...
<!-- artifact:quote:end -->
This virtually never happens. You are correct in general terms about the issues, but let's not exaggerate valid concerns and risk having them not taken seriously. Agreed. Nobody thinks MAA shouldn't be stronger than levies, but some of us think they are too strong. For example, witness this: Crossbowmen with Strength/Durability of 319/78. For reference, War Elephants have 250/50. Now I don't think that a single Crossbowman should hit about ~25% harder than a War Elephant no matter what buildings the owner has. The Durability becomes even more absurd. The Crossbowmen can take over 50% more punishment than a War Elephant. Imagine that you deliver enough punishment to kill a frickin' elephant to a Crossbowman, and he's still standing. That's just too unrealistic to swallow. What some people have said is that MAAs shouldn't be able to teleport across the map, and should use the same time mechanic for being called up as levies do, using the capital as a starting point since that's presumably where the majority of MAAs would be stationed when not on duty. MAAs also have no "return time" like levies do when you dismiss them while you're at war, so you can literally call your MAA up and have them fight a battle in Spain, then dismiss them and have them fight a battle in India the day after the first battle ends. That movement might be just a bit too fast.

## Reply 91 — participant_076 · 2020-11-17 · post-27109670

Thanks for the update. It will be great if you can add a "Dynasties" map-mode. It will be really useful to see the spread of one's dynasty, and not just one's house.

## Reply 92 — participant_077 · 2020-11-17 · post-27109674

Still no notifications added, that is crazy. Want to know what’s going on in the world!

## Reply 93 — participant_078 · 2020-11-17 · post-27109680

<!-- artifact:quote:start -->
> rageair said: Naming Dynasty Members in Court You now get to name all Dynasty members that are born in your court, not just your own children. This means that you can make sure that the correct names are passed down as you prefer! Click to expand...
<!-- artifact:quote:end -->
at last! we will be notified when dynasty members are born! (at least the ones in court.) now, could you please also make message settings a little more generous? i need to know when that cousin leaves my court for the greener pastures of Too Far to Interact With, or who got a new rival, or that this handsome duke got married when i wasn't looking! not knowing things really bothers me.

## Reply 94 — participant_079 · 2020-11-17 · post-27109695

I think the whole rally point system limits the thinking on armies. And I do think the game desperately needs some more strategic depth to its wars. Therefore I will shamelessly promote my solution which you can find in the suggestions under the title “Replace the rally point system with army system”. In any regards, seems like a great update coming up!

## Reply 95 — participant_080 · 2020-11-17 · post-27109790

<!-- artifact:quote:start -->
> Karlington said: MAAs also have no "return time" like levies do when you dismiss them while you're at war, so you can literally call your MAA up and have them fight a battle in Spain, then dismiss them and have them fight a battle in India the day after the first battle ends. That movement might be just a bit too fast. Click to expand...
<!-- artifact:quote:end -->
While I agree I felt for completeness I had to point out some caveats in your example. To disband you would have to control the area from which they are leaving. To disband there cannot be hostile armies 'nearby' (I have not figure out how close that is) which includes fleeing armies. To have them then go to India you need to own (not just control) the barony in which they are appearing. Typically these things are easy to handle. It does make them better on the defense. Once you start pushing into enemy territory it makes it take longer for them to return to the 'front'.

## Reply 96 — participant_081 · 2020-11-17 · post-27109800

<!-- artifact:quote:start -->
> es333 said: I see that the Estonian and Latvian culture borders are still ahistorical and falsely show the Curonian peninsula as 100% Latgal during times when it was still majority Finnic/Livonian/Estonian (however you decide to call it in CK)... Click to expand...
<!-- artifact:quote:end -->
In this regard, I am much more worried about the absence of the Balts in central Russia at that time (approximately in the Moscow region (let me remind you that the names of most of the largest rivers in Moscow are of Baltic origin (Jauza, Sietun', Nieglimna, as well as most likely Moscow (Moskva) itself))). And if in CK2 I made allowances for the imperfection of the map as a whole, in CK3 it looks as strange as possible given the very presence of Golyad' tribe (aka eastern Galindians) in the game (as Mozhaysk). Spoiler: Big map

## Reply 97 — participant_082 · 2020-11-17 · post-27109802

<!-- artifact:quote:start -->
> rageair said: Naming Dynasty Members in Court You now get to name all Dynasty members that are born in your court, not just your own children. This means that you can make sure that the correct names are passed down as you prefer! Click to expand...
<!-- artifact:quote:end -->
THANK YOU! At last I can have a good historical game with cool historical names.

## Reply 98 — participant_071 · 2020-11-17 · post-27109833

<!-- artifact:quote:start -->
> Keizer Harm said: The supply limit rally point tweak is so good! Click to expand...
<!-- artifact:quote:end -->
Why? Why is it so good?! They all gather in one point that I can split, if I want, however I desire. All in one point instead of a bunch, just to merge them in one big blob a bit later on. But when I run low of supplies, I don't have a button so that the army splits and auto go to neighboring provinces in order to resuply according to the supply limit of the province. No, I have to check the provincial supply limit and split the army in tiny bits and manually send each little one to a province. Soooo… why is this change so good?

## Reply 99 — participant_083 · 2020-11-17 · post-27109862

Release it at once.

## Reply 100 — participant_050 · 2020-11-17 · post-27109881

<!-- artifact:quote:start -->
> unmerged(220544) said: But when I run low of supplies, I don't have a button so that the army splits and auto go to neighboring provinces in order to resuply according to the supply limit of the province. No, I have to check the provincial supply limit and split the army in tiny bits and manually send each little one to a province. Click to expand...
<!-- artifact:quote:end -->
Yeah, the pain of resupplying could really use some UI work. For better or worse, wars in CK3 are won by doomstacks. Your best strategy is almost always to put all your troops in one small area so that you can be at maximum strength for an eventual battle. The supply system means that you need to keep your forces spread out into a handful of adjacent baronies, and move each one independently. There's little additional strategic depth - you're still ultimately going to combine them into one big army when it's time to fight. It just means that all troop maneuvering takes about ten times as many clicks as it otherwise would. Instead of just moving my doomstack from one province to the next, I have to carefully move each component army one at a time, making sure I don't accidentally walk several of them into the same barony at once. And once the battle's over, I have to re-divide my army to stay under supply limits. If the AI already knows how to do this effectively, it'd be very nice to have a button that does it for us. Although at some point I think we should ask whether the system is giving us any real benefits. If we're still just doing one big doomstack battle, but with 10x the clicks, what's the point of the supply system? It's not actually incentivizing me to divide my army into multiple smaller forces that pursue different objectives. It's just making me divide my army into multiple smaller forces that all do the same thing.

## Reply 101 — participant_067 · 2020-11-17 · post-27109885

<!-- artifact:quote:start -->
> Karlington said: This virtually never happens. You are correct in general terms about the issues, but let's not exaggerate valid concerns and risk having them not taken seriously. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Tiax said: If we're still just doing one big doomstack battle, but with 10x the clicks, what's the point of the supply system? It's not actually incentivizing me to divide my army into multiple smaller forces that pursue different objectives. It's just making me divide my army into multiple smaller forces that all do the same thing. Click to expand...
<!-- artifact:quote:end -->
It happened in all three games I played, and a lot of people in the forums have voiced similar complaints. From my point of view, it’s hard to see that as something that virtually never happens. To be blunt, the Fervor mechanic’s impact on the Catholic Church is the primary reason I’ve stopped playing CK3. I‘m checking out the DDs to evaluate if I’m going to try playing 1.2 or not, and the fact the Fervor is not mentioned makes me feel like the CK3 team, like you, doesn’t see Fervor as a major problem. That’s disappointing, because when Fervor goes bad, it goes really bad. This perfectly describes the problem with the current supply mechanics.

## Reply 102 — participant_084 · 2020-11-18 · post-27110067

Really hoped to see an improvement for the Knights system and the way we choose them. Anyway, nice update!

## Reply 103 — participant_085 · 2020-11-18 · post-27110135

<!-- artifact:quote:start -->
> TrojanRabbit said: I know beauty is in the eye of the beholder, but is it just me or is the "ugly" character on the left actually quite good looking? Nice cheekbones, straight nose...better than my broken beak, which I guess gives me the "hideous" trait.. Click to expand...
<!-- artifact:quote:end -->
It looks like his "ugly" trait is being expressed as his eyes being a bit too close together and his face just being really narrow.

## Reply 104 — participant_086 · 2020-11-18 · post-27110159

<!-- artifact:quote:start -->
> rageair said: Kill List Click to expand...
<!-- artifact:quote:end -->
Please add a Love List: all the people your character has f*cked.

## Reply 105 — participant_087 · 2020-11-18 · post-27110168

<!-- artifact:quote:start -->
> jakeowaty said: 2. That's the benefit of having Men at Arms, they are effectively a strike force in your realm that you pay extra in addition to the peasant levies provided by holdings. That said, we are always looking at ways to balance the game out in a way that feels right to us and the players! Click to expand...
<!-- artifact:quote:end -->
For proper balance I think that MAA should still take at least some degree of time to muster. However, it should be much faster than levies. Next level would be if the last place they were disbanded was also taken into account when determining how quickly they are once again ready for action in a different location.

## Reply 106 — participant_088 · 2020-11-18 · post-27110175

Could you please make the dangerous faction alert appear when they are strong enough to increase discontent rather than when they are days away from sending their demands?

## Reply 107 — participant_089 · 2020-11-18 · post-27110179

<!-- artifact:quote:start -->
> Krik_iddqd said: about the absence of the Balts in central Russia at that time Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Tiax said: The supply system means that you need to keep your forces spread out into a handful of adjacent baronies, and move each one independently Click to expand...
<!-- artifact:quote:end -->
This patch is glorious! I would say that the map is a bit too old though. It is quite possible that they were assimilated by 867 (not to mention 1066). Sounds barely undertakeable. Also, is supply really counted per barony not per county? If yes, this single tweak could make you split your armies more (because most counties have several baronies), and the strategy of "doomstack split into smaller parts but still doomstack" you described becomes almost impossible.

## Reply 108 — participant_090 · 2020-11-18 · post-27110199

<!-- artifact:quote:start -->
> jakeowaty said: First! I can't wait for this to release! Oh, wait... Click to expand...
<!-- artifact:quote:end -->
Nice great additions to the game ty!

## Reply 109 — participant_091 · 2020-11-18 · post-27110293

<!-- artifact:quote:start -->
> rageair said: Matrilineal Game Rules We’ve added a new game rule that controls the behaviour of the AI when choosing which type of marriage to pursue. There’s plenty of options to choose from, so regardless what your preference is, it should hopefully be represented! All options are achievement compatible. [Picture of Matrilineal Marriages Game Rule settings] Click to expand...
<!-- artifact:quote:end -->
So players will still be able to do them (if not outside their court, then inside it)? Why not add a rule banning them completely like in CK2? Historically matrilineal marriages were not a thing. EDIT: What's with the downvotes? Please do show evidence if I'm wrong, but AFAIK matrilineal marriages as they are in the game simply did not exist in the Middle Ages.

## Reply 110 — participant_081 · 2020-11-18 · post-27110322

<!-- artifact:quote:start -->
> Viridianus said: It is quite possible that they were assimilated by 867 (not to mention 1066). Click to expand...
<!-- artifact:quote:end -->
Regarding 1066, Golyad' should remain only in the Mozhaysk county (basin of the Protva river). Actually, the very first mention of them is dated only 1058th year and they really conquered only in the middle of the 12th century. This region as a whole was not particularly colonized until the 15th century, since it was difficult to access - far from large navigable rivers and completely covered with forests. There, in general, the whole region needs to be redone, the Vyatichi, for example, remained independent for a very long time and by the beginning of the 12th century were still pagans. As for the Balts in the 867th year, their range should be even wider, occupying the entire territory with Moskva, Tver, Mozhaysk, Odoyev, Novosil and maybe Ryazan and Tula. By 1066, all this had already been assimilated by Vyatiches (except Mozhaysk, of course).

## Reply 111 — participant_040 · 2020-11-18 · post-27110325

<!-- artifact:quote:start -->
> Jamey said: It happened in all three games I played, and a lot of people in the forums have voiced similar complaints. From my point of view, it’s hard to see that as something that virtually never happens. Click to expand...
<!-- artifact:quote:end -->
Within a few decades? Don't think I've ever seen that in my games. Haven't really seen people complaining about it happening with a few decades here on the forum either.

## Reply 112 — participant_092 · 2020-11-18 · post-27110334

<!-- artifact:quote:start -->
> Kydir said: Moose cavalry for Ugrians please. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Tschobo said: Finally, the Suomenusko split that I have waited for. Not the complete one (where I would have split if off into more faiths). But its a start in the right direction. I really like this dev. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> es333 said: I see that the Estonian and Latvian culture borders are still ahistorical and falsely show the Curonian peninsula as 100% Latgal during times when it was still majority Finnic/Livonian/Estonian (however you decide to call it in CK)... The bug report was acknowledged on day 2 after the release by Paradox so I'm a bit puzzled. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Viridianus said: I would say that the map is a bit too old though. It is quite possible that they were assimilated by 867 (not to mention 1066).Sounds barely undertakeable. Also, is supply really counted per barony not per county? If yes, this single tweak could make you split your armies more (because most counties have several baronies), and the strategy of "doomstack split into smaller parts but still doomstack" you described becomes almost impossible. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Krik_iddqd said: Regarding 1066, Golyad' should remain only in the Mozhaysk county (basin of the Protva river). Actually, the very first mention of them is dated only 1058th year and they really conquered only in the middle of the 12th century. This region as a whole was not particularly colonized until the 15th century, since it was difficult to access - far from large navigable rivers and completely covered with forests. There, in general, the whole region needs to be redone, the Vyatichi, for example, remained independent for a very long time and by the beginning of the 12th century were still pagans. As for the Balts in the 867th year, their range should be even wider, occupying the entire territory with Moskva, Tver, Mozhaysk, Odoyev, Novosil and maybe Ryazan and Tula. By 1066, all this had already been assimilated by Vyatiches (except Mozhaysk, of course). Click to expand...
<!-- artifact:quote:end -->
There's been no real evidence that the Mansi rode moose into battle, so as cool as it would be to have moose cavalry Men-at-Arms, it wouldn't be historically accurate to include them in the game. It's a good step forward, but ideally Suomenusko needs to be fragmented even further. Having Volga Finns use Finnish god names and Sami religious titles doesn't feel right at all, especially since the native Mari religion is still extant to this day and pretty well attested. At the very least, two more religions are needed (for the Sami and Volga-Finns respectively, although ideally the latter should be split between distinct Mordvin and Mari faiths), while more could be made to achieve better historical and gameplay accuracy (most notably the distinction between Mari and Mordvin religions, and less importantly but still preferably unique religions for Estonians, Livonians, Udmurts, Komi, and *just maybe* Bjarmians, depending on how the game can handle a single faith having different deity names depending on certain conditions). I'd imagine that they're holding on to updating Livonia in favour of completely overhauling the current set-up of Old Livonia. After all, pretty much none of the historically attested counties and principalities in Latvia and Estonia are playable, and instead we have fictional place-holder states that don't match any of the old Baltic states. It's like lumping the Irish petty kingdoms into two or three large duchies and calling it a day. The Eastern Galindians are attested as an independent tribe in sources as far as 1147, and probably didn't assimilate into the Russian society until 1400s-1500s. There were still people who identified as Golyads in the 1800s, if "Peoples of the USSR" is to be believed. As a result, it would be perfectly accurate to include the Eastern Galindians in the game. Of course, the main problem would be how to represent them, since we have no written records of their language. Would they need to be represented by having Lithuanian or Prussian culture? I dunno, I find it dubious that the Golyad' would assimilate that fast into the old East Slavic society, especially since Kievan Rus' didn't even manage to achieve the creation of an united Rus' identity while it still existed. Furthermore, wouldn't those areas that you listed be inhabited by Uralic tribes in 867?

## Reply 113 — participant_093 · 2020-11-18 · post-27110347

Please, Make West Africa have more Farmlands and Floodplains. Especially Places like Benin and Oyo/Ife

## Reply 114 — participant_074 · 2020-11-18 · post-27110362

<!-- artifact:quote:start -->
> Jamey said: It happened in all three games I played, and a lot of people in the forums have voiced similar complaints. From my point of view, it’s hard to see that as something that virtually never happens. To be blunt, the Fervor mechanic’s impact on the Catholic Church is the primary reason I’ve stopped playing CK3. I‘m checking out the DDs to evaluate if I’m going to try playing 1.2 or not, and the fact the Fervor is not mentioned makes me feel like the CK3 team, like you, doesn’t see Fervor as a major problem. That’s disappointing, because when Fervor goes bad, it goes really bad. Click to expand...
<!-- artifact:quote:end -->
I've seen Catholicism crumble *once*, and it took a couple of hundred years, with me carving off slices of their land (as an Insular Christian) at every plausible opportunity. So something is happening differently in your games to mine. Perhaps you're seeing the top liege in one of the empires or bigger kingdoms convert, at which point it's logical that they'll start converting their courtiers, vassals, and land. But at that point aside from the initial outbreak (possibly), it's not exactly a fervour issue any more.

## Reply 115 — participant_094 · 2020-11-18 · post-27110393

Everything looks great, except for one thing. The legacy section of the Dynasty window just looks out of place. The multi-block bar to show how many are unlocked of a given tree doesn't resemble anything else in the game that I can think of. It makes it look strange and out of place in the game. I'd recommend choosing a graphical style that better fits in with the rest of the UI styling. I understand having multiple blocks to indicate what the level is as a single bar might be hard to distinguish exactly where you're at, but there should be a better option than this one... something that looks like it belongs in this game's UI. I'd also ask that you make it possible to disable the automatic splitting of armies based on supply. If I have an enemy charging my gates and I raise my army and instead of having the full army at one location, they are spread around in smaller groups, this could quite easily cost me the war if I can't get them joined up quickly enough in the right terrain location. It's a nice idea, but generally speaking, you really aren't going to have so much trouble with supply that raising everyone in one location is going to be a problem unless you let them camp out there, which isn't very likely.

## Reply 116 — participant_095 · 2020-11-18 · post-27110398

<!-- artifact:quote:start -->
> rageair said: Improved Ugliness System [...] As you can see the difference isn’t massive, but helps make them a bit more interesting. There’s still room for improvement and especially so for the “Hideous” trait, but this was a relatively simple and safe change to make for 1.2. Click to expand...
<!-- artifact:quote:end -->
Still not ugly enough!!!

## Reply 117 — participant_035 · 2020-11-18 · post-27110453

<!-- artifact:quote:start -->
> jakeowaty said: Levies killed by knights do not get a mention, but knights killed rightly by other knights will show up in kill lists! Click to expand...
<!-- artifact:quote:end -->
Understandable, but I'm sad we won't get to see total number thousands and thousands levies smashed to pieces by our champions. Thank you for your answer

## Reply 118 — participant_096 · 2020-11-18 · post-27110518

Thank you for adding the character editor and attach armies function!

## Reply 119 — participant_097 · 2020-11-18 · post-27110553

And the next devdiary's title is going to be: "Blobs to Bits" How we are going to nerf snowballing empires. I am eagerly awaiting this.

## Reply 120 — participant_098 · 2020-11-18 · post-27110664

The army attachment is the one I missed most - it's actually the main reason why I didn't play the game anymore. Thanks for adding it - can't wait the patch

## Reply 121 — participant_099 · 2020-11-18 · post-27110682

NERF ARMIES PLS. and attrition when on boats

## Reply 122 — participant_100 · 2020-11-18 · post-27110720

Great stuff, though the Ruler Designer is a welcome feature, will Coat of Arms designer be added in the future? And the ability to change subject's CoA, sometimes the game can randomly generate ugly ones.

## Reply 123 — participant_101 · 2020-11-18 · post-27110789

So, kill list is back. But now we need tools to populate it. We need an option to lead armies and participate in battles!

## Reply 124 — participant_062 · 2020-11-18 · post-27110812

<!-- artifact:quote:start -->
> ZlNT said: So, kill list is back. But now we need tools to populate it. We need an option to lead armies and participate in battles! Click to expand...
<!-- artifact:quote:end -->
But we can... Just lead your troops as a commander. You can die in battle, the logical conclusion is that you can kill in battle too.

## Reply 125 — participant_102 · 2020-11-18 · post-27110827

Great news! So I can finaly play as a Hashimid in Mecca and Medina. All I need now is a Coat of Arms designer so I can have this nice pure green flag. xD

## Reply 126 — participant_103 · 2020-11-18 · post-27110832

What about fix for the paradox account regarding multiplayer???

## Reply 127 — participant_104 · 2020-11-18 · post-27110911

<!-- artifact:quote:start -->
> Aquamancer said: It's a good step forward, but ideally Suomenusko needs to be fragmented even further. Having Volga Finns use Finnish god names and Sami religious titles doesn't feel right at all, especially since the native Mari religion is still extant to this day and pretty well attested. At the very least, two more religions are needed (for the Sami and Volga-Finns respectively, although ideally the latter should be split between distinct Mordvin and Mari faiths), while more could be made to achieve better historical and gameplay accuracy (most notably the distinction between Mari and Mordvin religions, and less importantly but still preferably unique religions for Estonians, Livonians, Udmurts, Komi, and *just maybe* Bjarmians, depending on how the game can handle a single faith having different deity names depending on certain conditions). Click to expand...
<!-- artifact:quote:end -->
While I like some variety in pagan faiths and was a bit disappointed that most of them were basically just the same as CK2, one faith religions. BUT, I also think having unique faith for almost every Finnic culture is overkill. Maybe a third one could be added but beyond that it's too much in my opinion.

## Reply 128 — participant_081 · 2020-11-18 · post-27110923

<!-- artifact:quote:start -->
> Aquamancer said: Would they need to be represented by having Lithuanian or Prussian culture? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Aquamancer said: I dunno, I find it dubious that the Golyad' would assimilate that fast into the old East Slavic society, especially since Kievan Rus' didn't even manage to achieve the creation of an united Rus' identity while it still existed. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Aquamancer said: Furthermore, wouldn't those areas that you listed be inhabited by Uralic tribes in 867? Click to expand...
<!-- artifact:quote:end -->
Of course as a separate Dnieper-Oka culture within the Baltic family. It's just a couple of lines of code. A names can be taken in Prussian (it is possible, as an option, to fantasize a little more, but this should be done by a person who is well versed in the history of the Balto-Slavic languages). Regarding the Slavic colonization, and in particular the Russian colonization of northeastern Rus', several things must be understood. First - the population of these territories is very sparse. The Russians, when they colonized Zalesye and more distant lands, did not meet any resistance from the local population. The local population either left for other places (a lot of space, enough for everyone), or remained to live side by side without any problems and simply fast dissolved in a new, multi-arriving population. Second - colonization took place mostly not centrally and often independently of statehood. Yes, the ruling elite of Russia founded new cities, but this applies mainly to a later time, the same Zalesye was colonized mainly by the independent Vyatiches and Kriviches. Colonization and assimilation in general proceeded very quickly - if by the 7th century a Slavs inhabited only the outskirts of Kursk and Novgorod (even territories of modern Belarus was not really settled), then by the the 13th century the border already reaches almost the Kama region. Huge territories in a very short time. Specifically, in these territories, Baltic archeology and toponymy dominate more. The Baltic settlements themselves go far beyond these territories. Spoiler: Baltic settlements blue - archeological data, red - toponymy data

## Reply 129 — participant_105 · 2020-11-18 · post-27110979

So any updates on multiplayer????

## Reply 130 — participant_040 · 2020-11-18 · post-27110996

<!-- artifact:quote:start -->
> Voy said: But we can... Just lead your troops as a commander. You can die in battle, the logical conclusion is that you can kill in battle too. Click to expand...
<!-- artifact:quote:end -->
That may seem logical, but if you read the events files this is not the case. As commander you can get injured or die, but you don't participate in the actual battle yourself (other than the bonus to advantage rolls and bonuses from any commander traits). Players are specifically excluded from fighting like knights.

## Reply 131 — participant_022 · 2020-11-18 · post-27111215

My personal opinion: Commanders should have the option to fight as a knight. I agree that players should be able to participate in battles, not just by commanding the army, but by actually dealing and taking damage with prowess like a knight would.

## Reply 132 — participant_063 · 2020-11-18 · post-27111217

<!-- artifact:quote:start -->
> suburbanknight said: Great stuff, though the Ruler Designer is a welcome feature, will Coat of Arms designer be added in the future? And the ability to change subject's CoA, sometimes the game can randomly generate ugly ones. Click to expand...
<!-- artifact:quote:end -->
Check what coat of arms you'll get if you create a cadet branch as a member of the dynasty Anjou with capital in the county Anjou

## Reply 133 — participant_106 · 2020-11-18 · post-27111359

Given that the kill list is supposed to show how many people a person has killed, will it also show the number of anonymous troops they kill as knights on the battlefield?

## Reply 134 — participant_080 · 2020-11-18 · post-27111639

<!-- artifact:quote:start -->
> Fryslan0109 said: Given that the kill list is supposed to show how many people a person has killed, will it also show the number of anonymous troops they kill as knights on the battlefield? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> zloty_111 said: Can we have number of soldiers slain in battles too? Just one line added to the kill list Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> jakeowaty said: Levies killed by knights do not get a mention, but knights killed rightly by other knights will show up in kill lists! Click to expand...
<!-- artifact:quote:end -->
Already asked and answered

## Reply 135 — participant_107 · 2020-11-18 · post-27111656

<!-- artifact:quote:start -->
> Voy said: But we can... Just lead your troops as a commander. You can die in battle, the logical conclusion is that you can kill in battle too. Click to expand...
<!-- artifact:quote:end -->
You would assume that, yes. Unfortunately, it only goes one way at the moment. Honestly that's my biggest disappointment in the game at the moment. I just want my character to be able to go fight, and have battle events for them.

## Reply 136 — participant_108 · 2020-11-18 · post-27111699

<!-- artifact:quote:start -->
> rageair said: Matrilineal Game Rules We’ve added a new game rule that controls the behaviour of the AI when choosing which type of marriage to pursue. There’s plenty of options to choose from, so regardless what your preference is, it should hopefully be represented! All options are achievement compatible. View attachment 653501 [Picture of Matrilineal Marriages Game Rule settings] Click to expand...
<!-- artifact:quote:end -->
Fucking finally! I don't know why this wasn't in at the start! I'm not criticizing. This is just me being very very relieved at this being added in so I don't have to mod the game with Ironman breaking mods anymore.

## Reply 137 — participant_071 · 2020-11-18 · post-27111703

<!-- artifact:quote:start -->
> rageair said: More visibly, we’ve made one change to how troops get raised at rally points. Now if you exceed the supply limit the game will automatically split the army up to obey the supply limit, spreading it out over adjacent provinces. Click to expand...
<!-- artifact:quote:end -->
Already voiced my thoughts why I consider this a downgrade. Anyway, do we get a supply map mode?

## Reply 138 — participant_071 · 2020-11-18 · post-27111737

<!-- artifact:quote:start -->
> rageair said: Don't forget to tune in to tomorrows CK3 stream, where we'll show off the 1.2 patch! Click to expand...
<!-- artifact:quote:end -->
I did watch it. I saw Matt's army sitting in one province, enemy army (2x size) in the adjacent province. Enemy army instead of straight attacking over land, it embarks and disembarks on top of Matt's army, failing miserably.

## Reply 139 — participant_109 · 2020-11-18 · post-27111770

<!-- artifact:quote:start -->
> suburbanknight said: Great stuff, though the Ruler Designer is a welcome feature, will Coat of Arms designer be added in the future? And the ability to change subject's CoA, sometimes the game can randomly generate ugly ones. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Jamey said: The complaints about Fervor and Crusades have been epic in the forums. If the team is unaware of them and have made no improvements, I’m frankly flabbergasted. Click to expand...
<!-- artifact:quote:end -->
We don't have any concrete data or timeline for a Coat of Arms designer, but it is definitely something on our list of things we want - Matt We've fixed a bunch of things with Crusades for the upcoming patch, such as increasing the cooldown and, most importantly, fixed an issue where they would launch despite having not enough support. You'll be able to peruse the full list of changes we've done when the changelog is posted, which you won't have to wait too long for - Rageair

## Reply 140 — participant_074 · 2020-11-18 · post-27111937

<!-- artifact:quote:start -->
> PDX-Nicou said: We don't have any concrete data or timeline for a Coat of Arms designer, but it is definitely something on our list of things we want - Matt Click to expand...
<!-- artifact:quote:end -->
Things I'd like to see - 1) being able to redesign hideous cadet arms that my relatives have, or ones where it's almost impossible to tell the difference between two cadet branches (I was playing in India with a custom hindu religion, and must have had a dozen that differed only in the bottom left corner - but were all similar coloured emblems on a similar coloured background. 2) If the main line of the dynasty goes extinct, an ability for the new dynasty head to reclaim the name and arms of the founding dynasty. 3) An ability, when creating a cadet branch to choose the secondary/tertiary/quarterenary arms, either based on provinces or main titles, or to take maternal/paternal arms as the non-primary quarter. 4) An ability to ditch a quartered shield for a simple non-quartered one if I'm equivalent rank to the dynasty head as a cadet branch head. 5) Quartered territorial arms for more situations, including arbitrary unions (So if I'm England-Castille I can put the dragon or the leopards quartered with the tower of Castille; if I'm France-Jerusalem I can quarter the lillies with the cross). 6) I'd also like to be able to have alternate versions of some of the territorial arms, especially for Empires and Kingdoms that are non-historic, but are based on geography (so an alternate Britain in case the white with a red dragon is inappropriate 7) More options to display either the dynastic arms or the territorial arms, and for more cultures and religions. 8) A nice simple interface, and one that can guide the user to make something pleasant, rather than "mauve on purple and burgundy" 9) Integration with the ruler designer, so you can design your new CoA alongside the new character (even though I'm unlikely to use the ruler designer, it might as well be included for completeness sake).

## Reply 141 — participant_073 · 2020-11-18 · post-27111951

<!-- artifact:quote:start -->
> TheHundredDollarHeadache said: It looks like his "ugly" trait is being expressed as his eyes being a bit too close together and his face just being really narrow. Click to expand...
<!-- artifact:quote:end -->
So if the character acquires the obese trait & his face becomes less narrow, should he then lose the "ugly" trait?

## Reply 142 — participant_110 · 2020-11-18 · post-27112231

With new game rules, could the game remember rule settings from last time so every new game you dont have to do all the rules again?

## Reply 143 — participant_085 · 2020-11-19 · post-27112477

<!-- artifact:quote:start -->
> TrojanRabbit said: So if the character acquires the obese trait & his face becomes less narrow, should he then lose the "ugly" trait? Click to expand...
<!-- artifact:quote:end -->
I doubt that would fix his eye socket placement.

## Reply 144 — participant_111 · 2020-11-19 · post-27112518

Sounds great! Are you planning to add the fix of the transparent / missing coats of arms?

## Reply 145 — participant_040 · 2020-11-19 · post-27112567

<!-- artifact:quote:start -->
> TrojanRabbit said: So if the character acquires the obese trait & his face becomes less narrow, should he then lose the "ugly" trait? Click to expand...
<!-- artifact:quote:end -->
It'd still be a narrow face, just a fat narrow face. Fat gain and fat loss affects the appearance of the face almost as much as the appearance of the body.

## Reply 146 — participant_063 · 2020-11-19 · post-27112598

So: was the date of release announced? Somebody knows?

## Reply 147 — participant_075 · 2020-11-19 · post-27112650

<!-- artifact:quote:start -->
> Aquamancer said: I'd imagine that they're holding on to updating Livonia in favour of completely overhauling the current set-up of Old Livonia. After all, pretty much none of the historically attested counties and principalities in Latvia and Estonia are playable, and instead we have fictional place-holder states that don't match any of the old Baltic states. It's like lumping the Irish petty kingdoms into two or three large duchies and calling it a day. Click to expand...
<!-- artifact:quote:end -->
Yes I agree, it seems that the Finnic kingdoms of Estonia and Finland + the Baltics are quite barebones. Estonia isn't a Baltic in CK3 as it doesn't have any Baltic cultures inside its borders in that time frame nor in the future.

## Reply 148 — participant_112 · 2020-11-19 · post-27112678

A little underwhelmed so far. Maybe I'll change my tune after the changelog comes out.

## Reply 149 — participant_113 · 2020-11-19 · post-27112682

Could you concentrate on making female characters look better instead of making the already ugly character uglier? Right now, after a couple of generations. 90% of female characters look awful. Thanks.

## Reply 150 — participant_114 · 2020-11-19 · post-27112688

<!-- artifact:quote:start -->
> Slimane said: Could you concentrate on making female characters look better instead of making the already ugly character uglier? Right now, after a couple of generations. 90% of female characters look awful. Thanks. Click to expand...
<!-- artifact:quote:end -->
True, and the crazy thing is that they looked so good in 1.0. What happened? I honestly think 1.0 was all around better.

## Reply 151 — participant_073 · 2020-11-19 · post-27112718

<!-- artifact:quote:start -->
> Karlington said: It'd still be a narrow face, just a fat narrow face. Fat gain and fat loss affects the appearance of the face almost as much as the appearance of the body. Click to expand...
<!-- artifact:quote:end -->
I like big, fat, narrow butts & I can not lie

## Reply 152 — participant_115 · 2020-11-19 · post-27112781

<!-- artifact:quote:start -->
> Slimane said: Could you concentrate on making female characters look better instead of making the already ugly character uglier? Right now, after a couple of generations. 90% of female characters look awful. Thanks. Click to expand...
<!-- artifact:quote:end -->
Stop marrying ugly women? The women in my dynasty are hot.

## Reply 153 — participant_116 · 2020-11-19 · post-27112925

<!-- artifact:quote:start -->
> rageair said: To even things out a bit, a Court Physician you recruit as an agent has a chance to purposely mess up treatments of your target Click to expand...
<!-- artifact:quote:end -->
That was the thing I really missed. Now you need to consider who to hire not only basing on character stats (similar to spymaster). Other changes are great too ^^

## Reply 154 — participant_117 · 2020-11-19 · post-27113205

This is probably the best and most complete game ever released by Paradox! Good job guys, hope this is indicative of the future and huge props.

## Reply 155 — participant_118 · 2020-11-19 · post-27113548

<!-- artifact:quote:start -->
> rageair said: Attach to Army Click to expand...
<!-- artifact:quote:end -->
Yeeeeeeeeeeah boy! At last, I can play this game!

## Reply 156 — participant_119 · 2020-11-19 · post-27113741

An update where I like every single change? Praise Christ. Keep slaying guys.

## Reply 157 — participant_120 · 2020-11-19 · post-27114065

Will there be a quick way to see a character in their dynasty tree? I use this constantly in CKII and it's very frustrating to always have to start from the head of the dynasty and go manually looking for the character I was already checking in the first place.

## Reply 158 — participant_121 · 2020-11-19 · post-27114076

<!-- artifact:quote:start -->
> PLrc said: So: was the date of release announced? Somebody knows? Click to expand...
<!-- artifact:quote:end -->
24th of november, it was one of the first things revealed during the ck3 stream

## Reply 159 — participant_122 · 2020-11-19 · post-27114540

<!-- artifact:quote:start -->
> Gunthah said: Will there be a quick way to see a character in their dynasty tree? I use this constantly in CKII and it's very frustrating to always have to start from the head of the dynasty and go manually looking for the character I was already checking in the first place. Click to expand...
<!-- artifact:quote:end -->
Same here! It's especially annoying if you're searching for a random nobody from some obscure house that is so far removed from the dynasty head that you don't even know where to start looking.

## Reply 160 — participant_074 · 2020-11-19 · post-27114557

Having watched the youtube clip from the stream, something that struck me that would be nice to eventually have : Access to the custom religions system in the character builder.

## Reply 161 — participant_123 · 2020-11-19 · post-27114820

thank for your hard work

## Reply 162 — participant_124 · 2020-11-20 · post-27115202

I missed the stream and can't find it on twitch or YouTube, anyone have a link? Was the release date announced?

## Reply 163 — participant_040 · 2020-11-20 · post-27115236

<!-- artifact:quote:start -->
> xenger said: I missed the stream and can't find it on twitch or YouTube, anyone have a link? Was the release date announced? Click to expand...
<!-- artifact:quote:end -->
Unfortunately I have no idea where/if you can find the stream, but the release date has been confirmed to be November 24.

## Reply 164 — participant_125 · 2020-11-20 · post-27115419

<!-- artifact:quote:start -->
> xenger said: I missed the stream and can't find it on twitch or YouTube, anyone have a link? Was the release date announced? Click to expand...
<!-- artifact:quote:end -->
You can watch the stream here. CK3 content starts at 3 hours in - the release date is announced at about 3:03:15.

## Reply 165 — participant_126 · 2020-11-20 · post-27115608

<!-- artifact:quote:start -->
> rageair said: Naming Dynasty Members in Court You now get to name all Dynasty members that are born in your court, not just your own children. This means that you can make sure that the correct names are passed down as you prefer! Click to expand...
<!-- artifact:quote:end -->
Any chance a dev can expound upon the reasoning for not letting us rename anybody in the game?

## Reply 166 — participant_017 · 2020-11-20 · post-27115758

<!-- artifact:quote:start -->
> x4077 said: Any chance a dev can expound upon the reasoning for not letting us rename anybody in the game? Click to expand...
<!-- artifact:quote:end -->
Anybody? You could rename your enemy king Poopy McPoopFace. Or everyone in your family's dynasty. Most of the actions are limited by whether a ruler could meaningfully carry them out.

## Reply 167 — participant_083 · 2020-11-20 · post-27116004

Sucks that we need to wait till 24.11 (according to official twitter) rather than receiving an update before the weekend, when adults CAN ACTUALLY play the game.

## Reply 168 — participant_062 · 2020-11-20 · post-27116041

<!-- artifact:quote:start -->
> PanzerMonster said: Sucks that we need to wait till 24.11 (according to official twitter) rather than receiving an update before the weekend, when adults CAN ACTUALLY play the game. Click to expand...
<!-- artifact:quote:end -->
How very adult of you to throw a temper tantrum because of it. It's better they're given time to hotfix their mistakes before the next weekend "when adults CAN ACTUALLY play the game", otherwise you'd be pissed about that too.

## Reply 169 — participant_020 · 2020-11-20 · post-27116044

<!-- artifact:quote:start -->
> PanzerMonster said: Sucks that we need to wait till 24.11 (according to official twitter) rather than receiving an update before the weekend, when adults CAN ACTUALLY play the game. Click to expand...
<!-- artifact:quote:end -->
Would you prefer it on a Friday where if any critical issue happens all of the development team are going home and enjoying their weekend so any issues have to wait for the next week before being looked? Cause I guarantee you would not prefer it that way

## Reply 170 — participant_083 · 2020-11-20 · post-27116049

<!-- artifact:quote:start -->
> blackninja9939 said: Would you prefer it on a Friday where if any critical issue happens all of the development team are going home and enjoying their weekend so any issues have to wait for the next week before being looked? Cause I guarantee you would not prefer it that way Click to expand...
<!-- artifact:quote:end -->
Well, I figured its 2 working days before 24.11, meaning that most likely latest build is already in the master branch. If you are saying that you still are fixing bugs, then fine, I agree with you.

## Reply 171 — participant_020 · 2020-11-20 · post-27116054

<!-- artifact:quote:start -->
> PanzerMonster said: Well, I figured its 2 working days before 24.11, meaning that most likely latest build is already in the master branch. If you are saying that you still are fixing bugs, then fine, I agree with you. Click to expand...
<!-- artifact:quote:end -->
The build is mostly finalized yes, but that doesn't magically prevent the possibility of critical issues appearing when it is released to thousands of people playing on a much wider array of hardware than we can feasibly test on. There is always a risk with any patch to any piece of non-trivial software. So it is still better to release and give us working days after to fix anything in a worst case scenario. I'm sure you can handle waiting a few days until the weekend before playing the update if you can't play it in the evenings after work.

## Reply 172 — participant_083 · 2020-11-20 · post-27116101

<!-- artifact:quote:start -->
> blackninja9939 said: The build is mostly finalized yes, but that doesn't magically prevent the possibility of critical issues appearing when it is released to thousands of people playing on a much wider array of hardware than we can feasibly test on. There is always a risk with any patch to any piece of non-trivial software. So it is still better to release and give us working days after to fix anything in a worst case scenario. I'm sure you can handle waiting a few days until the weekend before playing the update if you can't play it in the evenings after work. Click to expand...
<!-- artifact:quote:end -->
Thanks for the clarification. We will wait, no worries. It's just frustrating that there's nothing to play at the moment. Baldur's gate 3 is a EA mess, Mount and Blade 2 is a EA mess as well, new Warhammer 2 DLC wont be released till 3.12. Had my hopes for CA3. I guess I will read a book then.

## Reply 173 — participant_058 · 2020-11-20 · post-27116389

<!-- artifact:quote:start -->
> blackninja9939 said: Would you prefer it on a Friday where if any critical issue happens all of the development team are going home and enjoying their weekend so any issues have to wait for the next week before being looked? Cause I guarantee you would not prefer it that way Click to expand...
<!-- artifact:quote:end -->
I understand. Sorry that not everyone does. Sometimes Devs just can't win for losin'...

## Reply 174 — participant_127 · 2020-11-20 · post-27116524

<!-- artifact:quote:start -->
> blackninja9939 said: The AI already has logic for assisting the player, for example by stacking up on them and following them to battles or sieging nearby things etc. It doesn't need to have access to the specific player facing tool for that. 1.2 aims to also a lot the AI dancing between priorities, though that is unrelated to specifically attaching armies. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DreadLindwyrm said: Perhaps the MaA should be tied to the rally point flag you have, and it should take time to move the rally point instead, because it seems the exploit is actually being able to move the rally point instantly rather than specifically moving the MaA around. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> unmerged(220544) said: Why? Why is it so good?! They all gather in one point that I can split, if I want, however I desire. All in one point instead of a bunch, just to merge them in one big blob a bit later on. But when I run low of supplies, I don't have a button so that the army splits and auto go to neighboring provinces in order to resuply according to the supply limit of the province. No, I have to check the provincial supply limit and split the army in tiny bits and manually send each little one to a province. Soooo… why is this change so good? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Slimane said: Could you concentrate on making female characters look better instead of making the already ugly character uglier? Right now, after a couple of generations. 90% of female characters look awful. Thanks. Click to expand...
<!-- artifact:quote:end -->
I find this response somewhat unconvincing and unsatisfying. Attaching armies is only a "player facing tool" if you talk about the literal button to do so, otherwise it is made that only by your decision to not let the AI use it. I appreciate all the work you put into the tactical AI, and I am sure the impact will be felt. But there is still value in clearly communicating to the player "the AI has decided to attach their army to yours for the moment". Because despite possible improvements, it is still an open question what the AI will do next otherwise. I find that often my allies are not as reliable as they seem, and I do not want to monitor their intended movements day to day to make sure they align with what I consider favourable engagements. Most people agree that demanding the AI should attach their armies is excessive and defeats the point of having autonomous allies, but it would be much better if AIs could decide themselves to attach their armies so this reliability is surfaced to the player. This is the correct answer. I hope the devs consider changes along these lines. You're right. Having a general "split army to match supply limits" would be a great button to have. And so would a "consolidate with neighboring armies". Anything that helps avoiding the tedious micromanagement around large armies and supply would be appreciated. No, female characters look fine. I am glad that Paradox is not following the male gaze oriented MMO type character design school for female characters. It apparently has reached the point where people cannot tell what real women look like anymore.

## Reply 175 — participant_128 · 2020-11-20 · post-27116774

<!-- artifact:quote:start -->
> blackninja9939 said: The build is mostly finalized yes, but that doesn't magically prevent the possibility of critical issues appearing when it is released to thousands of people playing on a much wider array of hardware than we can feasibly test on. There is always a risk with any patch to any piece of non-trivial software. So it is still better to release and give us working days after to fix anything in a worst case scenario. I'm sure you can handle waiting a few days until the weekend before playing the update if you can't play it in the evenings after work. Click to expand...
<!-- artifact:quote:end -->
Have your employees draw straws. Short straw gets chained to the basement over the weekend to fix any bugs that popup. Who do I see about my consultant fee?

## Reply 176 — participant_050 · 2020-11-20 · post-27116902

<!-- artifact:quote:start -->
> Keizer Harm said: Anybody? You could rename your enemy king Poopy McPoopFace. Or everyone in your family's dynasty. Most of the actions are limited by whether a ruler could meaningfully carry them out. Click to expand...
<!-- artifact:quote:end -->
If I issue a royal decree that William the Conqueror is to be referred to exclusively as William the Poopyfaced in my presence, then that's his new name as far as I'm concerned!

## Reply 177 — participant_118 · 2020-11-20 · post-27116944

<!-- artifact:quote:start -->
> Leoreth said: No, female characters look fine. I am glad that Paradox is not following the male gaze oriented MMO type character design school for female characters. It apparently has reached the point where people cannot tell what real women look like anymore. Click to expand...
<!-- artifact:quote:end -->
If you want to see "real women" just go outside your home. Games must provide some pleasure for our eyes and help us to escape reality.

## Reply 178 — participant_129 · 2020-11-20 · post-27117061

<!-- artifact:quote:start -->
> blackninja9939 said: It is purely a player facing feature like it was in CK2, it is for convenience of following the allied AI (or other players in MP) around to support them such as following a big stack in a Crusade or any other war. Click to expand...
<!-- artifact:quote:end -->
please tell me AI is willing to convert to reformed faiths after some time passes :/

## Reply 179 — participant_032 · 2020-11-20 · post-27117081

<!-- artifact:quote:start -->
> makaramus said: please tell me AI is willing to convert to reformed faiths after some time passes :/ Click to expand...
<!-- artifact:quote:end -->
no

## Reply 180 — participant_129 · 2020-11-20 · post-27117224

<!-- artifact:quote:start -->
> Zhetone said: no Click to expand...
<!-- artifact:quote:end -->
*Insert darth vader "No"*

## Reply 181 — participant_074 · 2020-11-20 · post-27117242

<!-- artifact:quote:start -->
> PanzerMonster said: Sucks that we need to wait till 24.11 (according to official twitter) rather than receiving an update before the weekend, when adults CAN ACTUALLY play the game. Click to expand...
<!-- artifact:quote:end -->
There was a big patch launch on one of the other titles some years ago that took place just before the weekend, and it effectively made the game unplayable - some people were getting hard crashes, others were getting all sorts of errors, still others couldn't even launch; and the fan base were (rightfully) up in arms about it, and there being no-one in the office to fix it. At the worst if such an incident happens with an early-week or mid-week patch it can be rolled back, and the game restored to pre-patch condition. It's much better that they release at a point when it can be easily monitored and rolled back rather than risk that again.

## Reply 182 — participant_130 · 2020-11-20 · post-27117549

<!-- artifact:quote:start -->
> Jayavarman said: Please add a Love List: all the people your character has f*cked. Click to expand...
<!-- artifact:quote:end -->
Arguably, this is much more important. Reminiscing over our dead enemies is all good. But forgetting our living enemies of our own making is very bad.

## Reply 183 — participant_131 · 2020-11-20 · post-27117635

The kill list doesn't specify how they were killed?

## Reply 184 — participant_126 · 2020-11-21 · post-27117984

<!-- artifact:quote:start -->
> Keizer Harm said: Anybody? You could rename your enemy king Poopy McPoopFace. Or everyone in your family's dynasty. Most of the actions are limited by whether a ruler could meaningfully carry them out. Click to expand...
<!-- artifact:quote:end -->
So what? Why do you care what I name the people in my game? It doesn't change the balance of the game other than to make dealing with information easier for the player. Hell, half of the Eastern religion names I end up shortening so that they fit on the UI. In regards to actions being limited to whether a ruler could meaningfully carry them out I only have one word in reply - immortality.

## Reply 185 — participant_044 · 2020-11-21 · post-27117992

<!-- artifact:quote:start -->
> Col. W. T. Philmore said: Games must provide some pleasure for our eyes and help us to escape reality. Click to expand...
<!-- artifact:quote:end -->
There are whole genres of games catering to people who want to look at pretty ladies. There is no reason for CK3 to go out of its way to cater to that particular market demand.

## Reply 186 — participant_017 · 2020-11-21 · post-27118178

<!-- artifact:quote:start -->
> x4077 said: In regards to actions being limited to whether a ruler could meaningfully carry them out I only have one word in reply - immortality. Click to expand...
<!-- artifact:quote:end -->
That's CK2.

## Reply 187 — participant_118 · 2020-11-21 · post-27118217

<!-- artifact:quote:start -->
> grommile said: There are whole genres of games catering to people who want to look at pretty ladies. There is no reason for CK3 to go out of its way to cater to that particular market demand. Click to expand...
<!-- artifact:quote:end -->
In any case it is better to show something beautiful, instead of something ugly. It is not market demand, it is a sense of beauty demand. Except if it is a horror or thriller genre, and you need specific atmosphere.

## Reply 188 — participant_132 · 2020-11-21 · post-27118323

I know it's not the top of your work priority list, but please use a serif font for the russian translation. The sans-serif one is really immersion breaking. The modders have fixed it in-game, but your promo materialsuffers greatly because a modern typeface clashes with the medieval theme of the game. The patch looks great btw!

## Reply 189 — participant_074 · 2020-11-21 · post-27118758

<!-- artifact:quote:start -->
> x4077 said: So what? Why do you care what I name the people in my game? It doesn't change the balance of the game other than to make dealing with information easier for the player. Hell, half of the Eastern religion names I end up shortening so that they fit on the UI. In regards to actions being limited to whether a ruler could meaningfully carry them out I only have one word in reply - immortality. Click to expand...
<!-- artifact:quote:end -->
Because being able to rename "anyone" includes people being able to rename (at a minimum) other players' heirs and wives in MP. Obviously being able to rename someone's wife as "I've had your wife", or naming your heir "Target" would be problematic.

## Reply 190 — participant_133 · 2020-11-21 · post-27118828

Pretty dang excited for the Turumic religion, I've been holding off on a Siberian playthrough until it got one of its own.

## Reply 191 — participant_126 · 2020-11-21 · post-27119143

<!-- artifact:quote:start -->
> DreadLindwyrm said: Because being able to rename "anyone" includes people being able to rename (at a minimum) other players' heirs and wives in MP. Obviously being able to rename someone's wife as "I've had your wife", or naming your heir "Target" would be problematic. Click to expand...
<!-- artifact:quote:end -->
Multiplayer is what, 5% of the use cases for this game? I'd rather not remove a useful feature for 95% of the use cases for the sake of 5%. Additionally, knowing whether the game is MP or SP is probably something the devs at PDX can differentiate, and therefore could easily change the behavior of rename all to a more restricted rename when in MP mode. Also, if all else fails, make rename all conditional on a game rule. Poof, no longer a problem for all those people that are worried about Mayor McCheese showing up in their game.

## Reply 192 — participant_074 · 2020-11-21 · post-27119167

<!-- artifact:quote:start -->
> x4077 said: Multiplayer is what, 5% of the use cases for this game? I'd rather not remove a useful feature for 95% of the use cases for the sake of 5%. Additionally, knowing whether the game is MP or SP is probably something the devs at PDX can differentiate, and therefore could easily change the behavior of rename all to a more restricted rename when in MP mode. Also, if all else fails, make rename all conditional on a game rule. Poof, no longer a problem for all those people that are worried about Mayor McCheese showing up in their game. Click to expand...
<!-- artifact:quote:end -->
I don't know what the proportion is off of the top of my head. But it's something that needs to be taken into account - plus it's not a case of *removing* it - it's a case of limiting it to more sensible levels, and only characters that you plausibly have control over. If the function has different functionality in SP and MP, it's an extra level of testing and complexity that isn't necessarily warranted.

## Reply 193 — participant_126 · 2020-11-21 · post-27119235

<!-- artifact:quote:start -->
> DreadLindwyrm said: I don't know what the proportion is off of the top of my head. But it's something that needs to be taken into account - plus it's not a case of *removing* it - it's a case of limiting it to more sensible levels, and only characters that you plausibly have control over. If the function has different functionality in SP and MP, it's an extra level of testing and complexity that isn't necessarily warranted. Click to expand...
<!-- artifact:quote:end -->
The fact that they are checking whether a person is eligible to be renamed or not at all is an extra level of testing and complexity that isn't warranted IMO. If you are playing MP with a person that is an asshole and is renaming your family to obscene names, quit. Trolls are going to troll, if they can't annoy you via rename they'll find some other way to annoy you.

## Reply 194 — participant_134 · 2020-11-21 · post-27119393

Given the changes going on for paganism in Siberia, I'm personally wondering if some of the more insane crime/general doctrine situations for religions will be getting a look at? Some of them make literally no sense. Slavic Paganism still mystifies me to this day.

## Reply 195 — participant_135 · 2020-11-22 · post-27119541

Kill list? Attach to ally army? Matrilinial game rules? Proof that the CK dev team is in tune with their community more than most other games I can think of Only thing I miss is the ledger... sometimes I just wanna see what the biggest religion/culture/realm in the world is!

## Reply 196 — participant_040 · 2020-11-22 · post-27119881

<!-- artifact:quote:start -->
> DreadLindwyrm said: Because being able to rename "anyone" includes people being able to rename (at a minimum) other players' heirs and wives in MP. Obviously being able to rename someone's wife as "I've had your wife", or naming your heir "Target" would be problematic. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> x4077 said: Multiplayer is what, 5% of the use cases for this game? I'd rather not remove a useful feature for 95% of the use cases for the sake of 5%. Additionally, knowing whether the game is MP or SP is probably something the devs at PDX can differentiate, and therefore could easily change the behavior of rename all to a more restricted rename when in MP mode. Also, if all else fails, make rename all conditional on a game rule. Poof, no longer a problem for all those people that are worried about Mayor McCheese showing up in their game. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DreadLindwyrm said: I don't know what the proportion is off of the top of my head. But it's something that needs to be taken into account - plus it's not a case of *removing* it - it's a case of limiting it to more sensible levels, and only characters that you plausibly have control over. If the function has different functionality in SP and MP, it's an extra level of testing and complexity that isn't necessarily warranted. Click to expand...
<!-- artifact:quote:end -->
We already have three game rules which restrict certain features in multiplayer (Assassinations, Invasions, and 3rd Party Claims), of which two have three options and one has two options. All three have actual game-technical effects, unlike names. I think it's safe to say that Paradox is more than capable of implementing this and that it's unlikely to consume too many resources once it's been implemented. However, that is ultimately something only they can determine, so for us to speculate whether it's plausible or not is a waste of time. All we can do is recommend, request, and then Paradox can tell us if it's feasible or not from a development-perspective.

## Reply 197 — participant_136 · 2020-11-23 · post-27121328

<!-- artifact:quote:start -->
> PLrc said: Becasue you will have to buy a dlc to have it (I bought one dlc to CK2 only to have that God damn button ^^). Click to expand...
<!-- artifact:quote:end -->
Well let's hope it's at least in the first DLC since for some silly reason I already pre ordered it! All these people who say allies screwing up isn't a problem for them. What are they smoking and where can I get some?

## Reply 198 — participant_063 · 2020-11-23 · post-27121342

<!-- artifact:quote:start -->
> Meg2345 said: Well let's hope it's at least in the first DLC since for some silly reason I already pre ordered it! All these people who say allies screwing up isn't a problem for them. What are they smoking and where can I get some. Click to expand...
<!-- artifact:quote:end -->
Well, I must admit the authors tried to improve the AI behaviour in this area with regard to the CK2. AI tries to stick with you and to help you, but despite it, AI happens to bug. And I'm always afraid if the AI will come at time and if it won't bug... I would feel safier if I had this button. Happily I rather havn't yet lost a war becasue of lack of it, maybe because I avoid wars, especially the big ones. Maybe thats why I don't have bad oppinion about AI on this matter... still I'd like to have the button

## Reply 199 — participant_137 · 2020-11-23 · post-27121513

Educational traits are finally done in corresponding colors?

## Reply 200 — participant_138 · 2020-11-23 · post-27122013

I hope we get to see patch notes today.... who's with me?

## Reply 201 — participant_109 · 2020-11-23 · post-27122020

<!-- artifact:quote:start -->
> repent said: I hope we get to see patch notes today.... who's with me? Click to expand...
<!-- artifact:quote:end -->
I'm the one shattering dreams <3 Patch Notes are expected for tomorrow, earlier than our usual Dev Diary timing (before 2:30pm CET); No set time yet.

## Reply 202 — participant_138 · 2020-11-23 · post-27122045

<!-- artifact:quote:start -->
> PDX-Nicou said: I'm the one shattering dreams <3 Patch Notes are expected for tomorrow, earlier than our usual Dev Diary timing (before 2:30pm CET); No set time yet. Click to expand...
<!-- artifact:quote:end -->
Thanks for the info.

## Reply 203 — participant_040 · 2020-11-23 · post-27122496

<!-- artifact:quote:start -->
> PDX-Nicou said: I'm the one shattering dreams <3 Patch Notes are expected for tomorrow, earlier than our usual Dev Diary timing (before 2:30pm CET); No set time yet. Click to expand...
<!-- artifact:quote:end -->
But we are the music makers, and we are the dreamers of dreams.

## Reply 204 — participant_139 · 2020-11-23 · post-27123064

<!-- artifact:quote:start -->
> PDX-Nicou said: I'm the one shattering dreams <3 Patch Notes are expected for tomorrow, earlier than our usual Dev Diary timing (before 2:30pm CET); No set time yet. Click to expand...
<!-- artifact:quote:end -->
Have you managed to get rule sets to save yet?

## Reply 205 — participant_140 · 2020-11-23 · post-27123180

<!-- artifact:quote:start -->
> repent said: I hope we get to see patch notes today.... who's with me? Click to expand...
<!-- artifact:quote:end -->
I been refreshing every so often to see but no luck yet.

## Reply 206 — participant_080 · 2020-11-23 · post-27123273

<!-- artifact:quote:start -->
> Untold said: I been refreshing every so often to see but no luck yet. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PDX-Nicou said: I'm the one shattering dreams <3 Patch Notes are expected for tomorrow, earlier than our usual Dev Diary timing (before 2:30pm CET); No set time yet. Click to expand...
<!-- artifact:quote:end -->
I guess you didn't see the message directly after Repent's message responding to them. So I will quote it here

## Reply 207 — participant_105 · 2020-11-25 · post-27127800

Oh I really hoped the patch notes would have something about multiplayer, apparently not.

## Reply 208 — participant_141 · 2020-11-25 · post-27127984

<!-- artifact:quote:start -->
> rageair said: You can now grow old, sick, tired, and depressed more efficiently Click to expand...
<!-- artifact:quote:end -->
We're still talking about the game, right? Excellent

## Reply 209 — participant_040 · 2020-11-25 · post-27128161

<!-- artifact:quote:start -->
> Zernos said: We're still talking about the game, right? Excellent Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Shakespeare said: All the world’s a [game], And all the men and women merely players; They have their exits and their entrances; And one man in his time plays many parts Click to expand...
<!-- artifact:quote:end -->
Well, as Shakespeare once wrote:

## Reply 210 — participant_142 · 2020-11-30 · post-27138503

I presume the han chinese are still appearing as nomadic tribal? or will it get the closer representation of india/tibet tribal?

