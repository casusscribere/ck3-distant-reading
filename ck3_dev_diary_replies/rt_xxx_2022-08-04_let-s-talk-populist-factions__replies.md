---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1537785/"
forum_thread_id: 1537785
content_type: reply_thread
parent_dd_file: dd_xxx_2022-08-04_let-s-talk-populist-factions.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "Let's Talk: Populist Factions"
dd_date: 2022-08-04
expansion: Friends and Foes
patch: Patch 1.7 (Bastion)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 4
reply_count: 64
participant_count: 42
reply_date_first: 2022-08-04
reply_date_last: 2023-04-30
body_word_count: 5820
inline_image_count: 0
quoted_span_count: 39
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Let's Talk: Populist Factions

*64 replies from 42 participants across 4 pages*

## Reply 1 — participant_001 · 2022-08-04 · post-28406853

Salutations! We’ll be starting up our regular Dev Diaries in the next few weeks or so, but until then, I wanted to take the opportunity to give you a brief look into some changes I’ve been working on. Specifically, I wanted to talk a bit about Populist Factions. Populist Factions have remained largely unchanged since release. We’ve done the occasional bug fixing and whatnot, but have yet to do something more substantial. They are, frankly, just as problematic now as they were at release. Populist factions have a number of problems that make them boring or frustrating to play against. These include (but are not necessarily limited to): Significant issues in regards to vassal gameplay. It’s not particularly fun to have a large part of your realm (and possibly your domain) suddenly go independent with next to no warning. They are little more than a glorified peasant revolt that offers no real challenge for a top liege who has a decent amount of men-at-arms or knights at their disposal. You don’t really have a lot of tools to manage a Populist Faction, or the popular opinion of the counties joining one. The last point was somewhat made better with the cultural rework in Royal Court, and the introduction of cultural acceptance. The rework gave you a new tool to influence and reduce the overall impact of popular opinion. I’d like to explore popular opinion further in the future, but for now, let’s focus on resolving the other two issues. In an effort to improve Populist Factions, I’ve been working on a smaller update to alleviate the issues mentioned above. Do note that some of the changes are a bit experimental in nature. Which is why I’d like to get your input and thoughts on how you think these might pan out. I approached the faction with the following goals in mind: Solve the issue regarding the lack of player agency when playing as a vassal Differentiate them from Peasant Factions Increase difficulty to make them more interesting and challenging Let’s start with the most outstanding issue, that of vassal gameplay. The main issue stems from the fact that the faction may only target the top liege. This prevents you as a vassal to have any influence in the outcome, and you don’t receive any real information as to what happens with the faction. Having a liege simply accept a Populist Faction's demand is a large source of frustration, as you can lose a big part of your realm without being able to do anything about it (and you are not even told why it happened). Simply switching the perspective to the vassal won’t cut it. We don’t want the reverse situation, where the vassal makes the decision without allowing the liege to have any say in the matter. So how do we solve it? I wanted to keep the functionality of the faction targeting the top liege. A popular uprising should go independent if they are successful. But vassals should be able to get involved. So I figured I’d try something new here, but stay away from any complicated solutions. When a Populist Faction goes to war, any direct vassal is now invited to participate in the faction war if they want to. The vassal has the option to join and help the liege, join the rebels, or stay out of it. Yes, that means that vassals and liege now fight side by side against a popular revolt. It’s limited to direct vassals only though, in order to keep the amount of vassals that may join on a reasonable level. We do, however, extend the functionality to any player sub-vassals, so that you always have the option of joining the war and protecting your lands (this is the problem we are attempting to solve here after all). { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" } The war overview for a populist revolt. Note the vassals who have joined on each side.​ With vassals being able to join, an AI liege will never accept the faction demand if an affected vassal is a player. Cause if they do, that would just take us back to square one. This guarantees that, as a vassal, you can react and help your liege against a populist revolt which includes counties within your own realm. You’ll still have the option of joining a liege’s war even if you are unaffected, you just won’t get a direct invitation to the war. The letter event a vassal receives when a populist faction send their demands.​ Now that vassals are allowed to join, we need to give a populist uprising additional military prowess. Otherwise they would be trivial to fight against. The difficulty has been ramped up in multiple ways. The most significant change here is that their armies will no longer only have levies. They’ll generate some base men-at-arms depending on the terrain type they spawn in. Hills will give them archers, mountains will give them spearmen, and so on. This should ensure that they get an appropriate troop composition. As before, the amount of levies and men-at-arms depends on the holdings of the counties participating in the revolt. Stronger holdings provide more troops. Additionally, armies will get some siege weapons that depend on the innovations the culture has unlocked. If the culture has gained access to trebuchets, that’s what they will spawn with. This will ensure that populists are able to stay relevant in the mid to late game, without having to besiege a holding for years before making any sort of progress. The troops of a populist revolt.​ Populist revolts used to only spawn with the leader as an available commander. Step one was to make the leader a bit better. By increasing their martial skill, and giving them some better traits (you are not going to be a popular leader for nothing after all), they’ll be slightly more threatening. Step two was to provide them with multiple commanders. A revolt should generally start with enough commanders to assign one to each spawned army. These commanders tend to be fairly skilled as well, significantly increasing their advantage in battles. The advantage of the leader of a revolt.​ That about sums it up, at least for the major changes. I hope that Populist Factions will be significantly more interesting than before. Let me know what you think!

## Reply 2 — participant_002 · 2022-08-04 · post-28406893

This is an excellent way to fix the number one problem with CK3. Very excited about the update!

## Reply 3 — participant_003 · 2022-08-04 · post-28406900

I am more interested in join the rebel instead of the liege. I really like to see if we can incite them into a war and take advantage in it

## Reply 4 — participant_004 · 2022-08-04 · post-28406905

oh cool. this looks like something everyone can live with.

## Reply 5 — participant_005 · 2022-08-04 · post-28406921

I'm sure there are plenty of devils left in the details, but this looks perfect!

## Reply 6 — participant_001 · 2022-08-04 · post-28406945

<!-- artifact:quote:start -->
> void0x00 said: I am more interested in join the rebel instead of the liege. I really like to see if we can incite them into a war and take advantage in it Click to expand...
<!-- artifact:quote:end -->
You won't be able to start a populist faction yourself, if that's what you mean. They are still very much driven by counties having low popular opinion. The option to convert and join the rebels is similar to that of the top-liege. You will switch to the culture and faith of the faction, only, you'll then join in on their side of the war. If successful, you'll either be part of the new realm, or go independent if your rank is too high to be vassalized by the revolt leader. While the option is a bit more restrictive for the AI, it's much easier for a player, should they want to go that route. You are free to join if you share the same faith, or at least 20% of your realm is of their faith already.

## Reply 7 — participant_002 · 2022-08-04 · post-28406965

After thinking about it a bit more, I do have some questions: -> If I already am of the culture and faith of the populist faction and decide to join them, will the populist counties of my realm stay in my realm if the revolt wins? I would hope so. -> If I am already fighting a revolt against my liege when the faction fires, do I need to join the populist war on the side of my liege in order to keep my land? How does that work? -> What happens if a revolting county is conquered by an external realm while the populist war is going on? I think I recall there being some issues with that as well, but I am not sure right now.

## Reply 8 — participant_006 · 2022-08-04 · post-28406967

<!-- artifact:quote:start -->
> void0x00 said: I am more interested in join the rebel instead of the liege. I really like to see if we can incite them into a war and take advantage in it Click to expand...
<!-- artifact:quote:end -->
Sounds like you can - you get an option to join either the rebels or the liege.

## Reply 9 — participant_001 · 2022-08-04 · post-28406977

<!-- artifact:quote:start -->
> fodazd said: -> If I already am of the culture and faith of the populist faction and decide to join them, will the populist counties of my realm stay in my realm if the revolt wins? I would hope so. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> fodazd said: -> If I am already fighting a revolt against my liege when the faction fires, do I need to join the populist war on the side of my liege in order to keep my land? How does that work? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> fodazd said: -> What happens if a revolting county is conquered by an external realm while the populist war is going on? I think I recall there being some issues with that as well, but I am not sure right now. Click to expand...
<!-- artifact:quote:end -->
Yes. If you join the revolt and win, you get to keep your realm just as it was before joining. Due to how wars work in general, the option to join either side will be disabled if you are already at with with any of the participants. You'll still get the letter event shown in my original post though, to give you a proper notification that the war is still happening. If you are able to conclude your other war, you can still opt into the war with the "Offer to Join War" interaction on your liege. Sadly, for technical reasons, that won't work for the rebels. If you can't join them in the initial event, you won't be able to join them later either. I'm actually not entirely sure. I haven't tested this specifically, but I think the county would leave the faction and belong to its new ruler. I'll see if I can verify that though.

## Reply 10 — participant_004 · 2022-08-04 · post-28406989

<!-- artifact:quote:start -->
> fodazd said: If I am already fighting a revolt against my liege when the faction fires, do I need to join the populist war on the side of my liege in order to keep my land? How does that work? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> fodazd said: -> What happens if a revolting county is conquered by an external realm while the populist war is going on? I think I recall there being some issues with that as well, but I am not sure right now? Click to expand...
<!-- artifact:quote:end -->
wouldn't everyone just be hostile to each other? at the moment the county's lost and i don't think that should change.

## Reply 11 — participant_007 · 2022-08-04 · post-28407009

Sounds to me that you rightly nailed down the problem. Congrats!

## Reply 12 — participant_004 · 2022-08-04 · post-28407029

<!-- artifact:quote:start -->
> Servancour said: Yes. If you join the revolt and win, you get to keep your realm just as it was before joining. Due to how wars work in general, the option to join either side will be disabled if you are already at with with any of the participants. You'll still get the letter event shown in my original post though, to give you a proper notification that the war is still happening. If you are able to conclude your other war, you can still opt into the war with the "Offer to Join War" interaction on your liege. Sadly, for technical reasons, that won't work for the rebels. If you can't join them in the initial event, you won't be able to join them later either. I'm actually not entirely sure. I haven't tested this specifically, but I think the county would leave the faction and belong to its new ruler. I'll see if I can verify that though. Click to expand...
<!-- artifact:quote:end -->
i think part of the fun of factions is when a rebel's vassal rebels against them. i wouldn't want that to change.

## Reply 13 — participant_008 · 2022-08-04 · post-28407045

I don't think making the revolts stronger will make things more interesting, I'm still just going to raise my army next to theirs and walk into them.

## Reply 14 — participant_009 · 2022-08-04 · post-28407049

this seems like an excellent change. the ability to side with the rebels especially is a really nice touch i worry having the leaders spawn in with a selection of baller traits is going to flood the world with really powerful dudes, though. the ai is still pretty rancid with realm management and they tend to deal with a lot of revolts. every revolt they put down where they dont immediately execute the leader is going to result in another one of these god-men hanging around, and i dont think having them just auto-execute the leader is a good idea either, certain traits would just make that an out of character action and result in an accumulation of stress. this isnt a HUGE problem, but it gives the player another big advantage over the ai, since the player is generally better at gathering up talented dudes in their court and putting them to good use. strikes me as a potential balance issue

## Reply 15 — participant_010 · 2022-08-04 · post-28407115

<!-- artifact:quote:start -->
> Slow Bathroom said: I don't think making the revolts stronger will make things more interesting, I'm still just going to raise my army next to theirs and walk into them. Click to expand...
<!-- artifact:quote:end -->
I mean, making wars in general more interesting will only come from a revamp of the entire feature, not from changes to how revolts work. I think this is a good solution to the currently often underwhelming or frustrating populist revolts, but yeah the game needs to handle wars differently. Chasing shouldn't be the focus, we need something more simular to situations or how wars work in V3.

## Reply 16 — participant_011 · 2022-08-04 · post-28407131

In HRE are populist factions almost every year, additionaly emperor is facing many another factions and rebelions... He Is usually out of troops and all HRE is fragmented and weak... In my opinion populist factions should have be less frequently and their strength much weaker. My biggest problem in my actual game as king of Bohemia are polish populist factions, where exhausted emperor is giving independence to rebel counties instantly.... Popular factions occured almost every year...If I understand clearly, with this patch I will be every year in war with my polish counties? Its unplayable!!!!

## Reply 17 — participant_004 · 2022-08-04 · post-28407132

<!-- artifact:quote:start -->
> ahoj said: with this patch I will be every year in war with my polish counties? Click to expand...
<!-- artifact:quote:end -->
or the emperor

## Reply 18 — participant_012 · 2022-08-04 · post-28407139

So I've seen popular revolts involving vassals before. And to win you just need to clear out the rebel armies. If you join on the side of the revolt will the liege be forced to siege things down?

## Reply 19 — participant_011 · 2022-08-04 · post-28407147

<!-- artifact:quote:start -->
> prismaticmarcus said: or the emperor Click to expand...
<!-- artifact:quote:end -->
Okey, Emperor and who else? Me as his direct vasal (king), or my direct vasal duke or count? I dont understant this change. If the chance to join war will have only direct liege, in will be duke...and me as king will have no control over my realm as nowadays!!! I hate populist factions, really HATE!! It ruins all my game

## Reply 20 — participant_013 · 2022-08-04 · post-28407164

The populist's faction ultimatum stands out as the only one that reduces the whole level of fame instead of fixed prestige cost. I wonder if (very much needed!) improvements might trash some of the AIs rulers fame a bit too much. Maybe reducing the whole level of fame could be a dissolutions faction feature instead?

## Reply 21 — participant_001 · 2022-08-04 · post-28407175

<!-- artifact:quote:start -->
> tilly said: i worry having the leaders spawn in with a selection of baller traits is going to flood the world with really powerful dudes, though. the ai is still pretty rancid with realm management and they tend to deal with a lot of revolts. every revolt they put down where they dont immediately execute the leader is going to result in another one of these god-men hanging around, and i dont think having them just auto-execute the leader is a good idea either, certain traits would just make that an out of character action and result in an accumulation of stress. this isnt a HUGE problem, but it gives the player another big advantage over the ai, since the player is generally better at gathering up talented dudes in their court and putting them to good use. strikes me as a potential balance issue Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> ahoj said: Okey, Emperor and who else? Me as his direct vasal (king), or my direct vasal duke or count? Click to expand...
<!-- artifact:quote:end -->
A fair concern. I haven't seen this become a problem just by observing the AI, but it's true that the player is able to more efficiently recruit these characters to their court if they want to. Do note that they are not intended to be overpowered, just have a bit higher martial than your average character. If needed, we'll adjust their skills accordingly. When it comes to the AI, only direct vassals can join (in your case, that would be the direct vassals of the emperor). But as a player, you can always join to try and defend your realm, even as a sub-vassal.

## Reply 22 — participant_011 · 2022-08-04 · post-28407212

<!-- artifact:quote:start -->
> Servancour said: A fair concern. I haven't seen this become a problem just by observing the AI, but it's true that the player is able to more efficiently recruit these characters to their court if they want to. Do note that they are not intended to be overpowered, just have a bit higher martial than your average character. If needed, we'll adjust their skills accordingly. When it comes to the AI, only direct vassals can join (in your case, that would be the direct vassals of the emperor). But as a player, you can always join to try and defend your realm, even as a sub-vassal. Click to expand...
<!-- artifact:quote:end -->
Thank you for answer. It sounds good and it should solve my biggest problem But still Im afraid of how often these wars against populist factions will occured. I dont want to fighting every year May be there should be option to turn them off in game settings. I like to play in stable enviroment where great powers arent fragmented and weak. AI never maintain stable and powerful Russia, France, HRE there is lot of revolts and independent wars and rulers are ussualy defeated and weak But Im looking forward to this change Small step for mankind, but huge for me

## Reply 23 — participant_007 · 2022-08-04 · post-28407299

<!-- artifact:quote:start -->
> Servancour said: A fair concern. I haven't seen this become a problem just by observing the AI, but it's true that the player is able to more efficiently recruit these characters to their court if they want to. Do note that they are not intended to be overpowered, just have a bit higher martial than your average character. If needed, we'll adjust their skills accordingly. Click to expand...
<!-- artifact:quote:end -->
One thing you can do is to make them "disappear" once they are not army commanders or are at peace. There was something similar to this effect - I don't know if it is still true as I modded it pretty fast some sub versions ago - where there were plenty of characters generated by some event being Geniuses and Lunatic at the same time.

## Reply 24 — participant_014 · 2022-08-04 · post-28407314

I'm a bit afraid populist factions might be too strong if they get MAAs and better commanders, especially if you managed to conquer large swathes of land (e.g. a kingdom), where they would be a threat already if they managed to join their armies. But that also makes expansion more interesting and might slow down blobbing in general if they become a force that you can't just ignore. I guess it will depend on balancing how it turns out. A few more ways to influence popular opinion would be nice, in my experience cultural acceptance plays only a minor role (and is extremely slow to change). Like visit county, hold speech, invest in county (for minuscule gameplay bonuses, yet gives popular opinion - like giving a gift to a vassal).

## Reply 25 — participant_015 · 2022-08-04 · post-28407342

I would like to see a bit more influence possibilities from the side of the liege. For example, the liege could promise hooks or money etc. to nobles to have them take their side. The Royal Court could be used here, too.

## Reply 26 — participant_016 · 2022-08-04 · post-28407637

I am *extremely* happy to see populist revolts getting a closer look. This is definitely one of the biggest issues in the game, and it's great to see it getting tackled. A+ work. I do however have some concerns: First, I don't see any mention of populist revolt resolutions - what happens when a populist faction wins a war? This has been completely broken for a very long time - it doesn't work at all. https://forum.paradoxplaza.com/foru...ot-resolving-correctly.1517227/#post-28171624 The last set of patch notes included a line that suggested this was fixed, but in fact nothing seems to have changed, and it is just as broken as its always been. I'm not even clear whether these exists a clear vision for what is *supposed* to happen at the end of a populist revolt. Is it documented anywhere what the intended behavior is? Second, I'm concerned that there seems to be a lot of "we do X differently if the player is involved" here. Obviously there is some upside to this approach - it allows you to make targeted fixes for things that are particularly painful for a player. But there's a danger here too. How do you keep faction strength balanced for the cases where player subvassals join and also balanced for the cases where an AI-only realm is deciding whether to just surrender to the revolt? Certainly the gameplay experience for a player-involved revolt is most pressing, but the balance of AI-only revolts is also very problematic currently. It's so bad that we have to have special grace periods at the start of the game - and then the AI often falls to revolts as soon as they expire anyway! My worry is that once a special carve-out for the player is made, that will be an excuse to sweep the larger balance issues under the rug. Third, the letter that you get as a vassal show in one of the screenshots seems to suggest that you have the option to join the rebels. But players are currently prohibited from joining populist factions (while AI vassals are allowed to). Does this represent a change in the general policy, or are you only allowed to join when you get the letter? In either case, I think this is playing with fire, at least until my first concern above is addressed. Currently, AI vassals who join successful populist revolts *lose their territory to the populist leader anyway*. Is it a good idea to give the player the option to do this as well, without clearly spelling out what they are signing up for?

## Reply 27 — participant_017 · 2022-08-04 · post-28407743

Seems good change to me. But I always found the military aspect of big popular revolts a much more cursed: their stacks spawning spread out all over the country can't be countered by raising your armies near them, because your armies have to assemble, theirs don't (also you can't influence how many and which troops spawn per place). So I always get an incredibly confusing hunt after a dozen rebel stacks, which is for me one of the most annoying things in the game right now.

## Reply 28 — participant_018 · 2022-08-04 · post-28407892

Great, finally to adress some lower tier play as vasal.

## Reply 29 — participant_019 · 2022-08-04 · post-28407980

Can't wait to capture the leader and commanders then recruit them!

## Reply 30 — participant_003 · 2022-08-05 · post-28408208

<!-- artifact:quote:start -->
> Servancour said: You won't be able to start a populist faction yourself, if that's what you mean. They are still very much driven by counties having low popular opinion. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Servancour said: You are free to join if you share the same faith, or at least 20% of your realm is of their faith already. Click to expand...
<!-- artifact:quote:end -->
what I think of is intentionly lower the culture acceptance and popular opinion and wait them to start the faction. can player join the faction or have anyway to sponsor them? or can only join them after the war start? as now only NPC can join populist faction. is it limited to vassals? if foreign rulers can help them get independent?

## Reply 31 — participant_020 · 2022-08-05 · post-28408440

<!-- artifact:quote:start -->
> void0x00 said: can player join the faction or have anyway to sponsor them? or can only join them after the war start? as now only NPC can join populist faction. Click to expand...
<!-- artifact:quote:end -->
That would be awsome if as a foreign ruler, you sponsor the revolt with money to create chaos in the realm. And of course if the other ruler learns about it, he becomes your rival or try to kill you

## Reply 32 — participant_021 · 2022-08-05 · post-28408571

The main problem (to my gameplay experience) remains: These are revolts originated and lead by NOBODIES. This game is about inter-character relations. Having rebellions spawn (and they spawn often) led by constant nobodies is frankly tedious. Can't the leaders of the rebellion be picked from among your most discontent "that-culture" vassals? Historically, such "cultural" rebellions offered the crown to a prominent noble of their culture. They didn't crown the peasant lowborn leading the revolt. It's bad history and it's not good gameplay. Sometimes the rebels offered the crown to a foreign king, but a rival of their enemy who could be made into a powerful ally, even if that would create problems later. I'm thinking about the Catalan Civil War, where the rebels against King John offered the crown to a Portuguese prince and afterwards to Good King René (after Peter of Portugal died in campaign). I'm also a bit bummed that there's no complexity as to what these rebels want, in terms of government. If you get Italian rebels as a foreign king, I'd like to know if these are nobles yearning for a native king, or communes revolting and trying to set up a republican League or federation of communes of some sort. All in all, changes to these rebellions are welcome, but I hope this really is just step 1.

## Reply 33 — participant_005 · 2022-08-05 · post-28408588

<!-- artifact:quote:start -->
> Cèsar de Quart said: Can't the leaders of the rebellion be picked from among your most discontent "that-culture" vassals? Click to expand...
<!-- artifact:quote:end -->
No. Because if a county's immediate holder has the county culture as their personal culture, it doesn't get populist revolts – but the vassal themselves can start an independence faction.

## Reply 34 — participant_021 · 2022-08-05 · post-28408604

<!-- artifact:quote:start -->
> grommile said: No. Because if a county's immediate holder has the county culture as their personal culture, it doesn't get populist revolts – but the vassal themselves can start an independence faction. Click to expand...
<!-- artifact:quote:end -->
Okay, but then the rebels should be given options once the rebellion is successful. a) Offer the crown to some lord who joined the rebellion b) Offer the crown to a powerful lord of the same culture c) Establish a republic or theocracy, depending on culture tenets. c) Create a new realm with a nobody as king, but this nobody will be a pariah and the new state should not really last. Historically, this is not what happened. I say this becouse I'm tired of seeing off-color kingdoms led by populist rebels with no pedigree when there's a perfectly old that-culture family nearby who also is independent.

## Reply 35 — participant_022 · 2022-08-05 · post-28408612

Thanks for the update.

## Reply 36 — participant_023 · 2022-08-05 · post-28408626

<!-- artifact:quote:start -->
> tonifr said: That would be awsome if as a foreign ruler, you sponsor the revolt with money to create chaos in the realm. And of course if the other ruler learns about it, he becomes your rival or try to kill you Click to expand...
<!-- artifact:quote:end -->
At least the first part is already easily possible: Just gift the revolt leader gold via the " Make gift" character interaction - the AI is pretty straight forward in using such funds for mercenaries, when in a war (provided you gift enough to cover the costs and they deem extra forces necessary to win)

## Reply 37 — participant_024 · 2022-08-05 · post-28408676

<!-- artifact:quote:start -->
> Herennius said: At least the first part is already easily possible: Just gift the revolt leader gold via the " Make gift" character interaction - the AI is pretty straight forward in using such funds for mercenaries, when in a war (provided you gift enough to cover the costs and they deem extra forces necessary to win) Click to expand...
<!-- artifact:quote:end -->
We currently have the "contract assistance" interaction in the iberian struggle, where you can join a war in exchange for money if you contribute enough. We should also have same kind of interaction where you gift money to rebels in exchange for a hook or something similar... Maybe some characters accept these, while some personalities might only accept gifts with no strings attached.

## Reply 38 — participant_001 · 2022-08-05 · post-28408681

<!-- artifact:quote:start -->
> Tiax said: First, I don't see any mention of populist revolt resolutions - what happens when a populist faction wins a war? This has been completely broken for a very long time - it doesn't work at all. https://forum.paradoxplaza.com/foru...ot-resolving-correctly.1517227/#post-28171624 Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Cèsar de Quart said: Okay, but then the rebels should be given options once the rebellion is successful. a) Offer the crown to some lord who joined the rebellion b) Offer the crown to a powerful lord of the same culture c) Establish a republic or theocracy, depending on culture tenets. c) Create a new realm with a nobody as king, but this nobody will be a pariah and the new state should not really last. Historically, this is not what happened. Click to expand...
<!-- artifact:quote:end -->
I had a look at the issues mentioned in the bug report. While I can't promise to get in fixes for all of them, at least some of these are issues that should be fixed already (such as faction members not going independent if they can't be vassalized). I've been exploring the possibility to do something similar to your suggestions actually, but I decided against doing too many changes at once. Factions tend to be fairly complicated and require extensive testing to make sure they behave the way they should. So for now, the populist leader will still become the ruler of the new realm.

## Reply 39 — participant_024 · 2022-08-05 · post-28408781

Do you have any estimates when could we see these changes implemented?

## Reply 40 — participant_001 · 2022-08-05 · post-28408801

<!-- artifact:quote:start -->
> Mööpelitintti said: Do you have any estimates when could we see these changes implemented? Click to expand...
<!-- artifact:quote:end -->
If all goes well, they'll be included with the next major update. Though I can't say when that will be.

## Reply 41 — participant_025 · 2022-08-05 · post-28408868

I welcome any changes that make the game more challenging. In its current state, it is very easy. The only thing that seems to stop the player from achieving something, is their willingness to do it.

## Reply 42 — participant_016 · 2022-08-05 · post-28409057

<!-- artifact:quote:start -->
> Servancour said: I had a look at the issues mentioned in the bug report. While I can't promise to get in fixes for all of them, at least some of these are issues that should be fixed already (such as faction members not going independent if they can't be vassalized). Click to expand...
<!-- artifact:quote:end -->
The patch notes for 1.6 promised to fix this, but I'm not convinced that it actually did: CK3 Dev Diary #99: It is time to decide the Fate of Iberia Buenos días Crusaders! The time has finally come to decide the Fate of Iberia. Everything went according to plan since the last diary (phew!), so today we are really excited to release our new Flavor Pack. In today’s Dev Diary, I’ll be... forum.paradoxplaza.com Maybe there is some particular corner case that is actually fixed, but it doesn't seem like faction members are properly made independent in many cases.

## Reply 43 — participant_026 · 2022-08-06 · post-28409662

Personally, I think all defensive wars should be like this anyway, with any vassals in the claimed area given the call to arms.

## Reply 44 — participant_027 · 2022-08-06 · post-28409758

<!-- artifact:quote:start -->
> Ezumiyr said: I mean, making wars in general more interesting will only come from a revamp of the entire feature, not from changes to how revolts work. I think this is a good solution to the currently often underwhelming or frustrating populist revolts, but yeah the game needs to handle wars differently. Chasing shouldn't be the focus, we need something more simular to situations or how wars work in V3. Click to expand...
<!-- artifact:quote:end -->
Chasing is exactly how wars should work if there is an imbalance. Vying for a good position before giving battle, and then winning by siege.

## Reply 45 — participant_021 · 2022-08-06 · post-28410289

<!-- artifact:quote:start -->
> Servancour said: I had a look at the issues mentioned in the bug report. While I can't promise to get in fixes for all of them, at least some of these are issues that should be fixed already (such as faction members not going independent if they can't be vassalized). I've been exploring the possibility to do something similar to your suggestions actually, but I decided against doing too many changes at once. Factions tend to be fairly complicated and require extensive testing to make sure they behave the way they should. So for now, the populist leader will still become the ruler of the new realm. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Tiax said: I am *extremely* happy to see populist revolts getting a closer look. This is definitely one of the biggest issues in the game, and it's great to see it getting tackled. A+ work. I do however have some concerns: First, I don't see any mention of populist revolt resolutions - what happens when a populist faction wins a war? This has been completely broken for a very long time - it doesn't work at all. https://forum.paradoxplaza.com/foru...ot-resolving-correctly.1517227/#post-28171624 The last set of patch notes included a line that suggested this was fixed, but in fact nothing seems to have changed, and it is just as broken as its always been. I'm not even clear whether these exists a clear vision for what is *supposed* to happen at the end of a populist revolt. Is it documented anywhere what the intended behavior is? Second, I'm concerned that there seems to be a lot of "we do X differently if the player is involved" here. Obviously there is some upside to this approach - it allows you to make targeted fixes for things that are particularly painful for a player. But there's a danger here too. How do you keep faction strength balanced for the cases where player subvassals join and also balanced for the cases where an AI-only realm is deciding whether to just surrender to the revolt? Certainly the gameplay experience for a player-involved revolt is most pressing, but the balance of AI-only revolts is also very problematic currently. It's so bad that we have to have special grace periods at the start of the game - and then the AI often falls to revolts as soon as they expire anyway! My worry is that once a special carve-out for the player is made, that will be an excuse to sweep the larger balance issues under the rug. Third, the letter that you get as a vassal show in one of the screenshots seems to suggest that you have the option to join the rebels. But players are currently prohibited from joining populist factions (while AI vassals are allowed to). Does this represent a change in the general policy, or are you only allowed to join when you get the letter? In either case, I think this is playing with fire, at least until my first concern above is addressed. Currently, AI vassals who join successful populist revolts *lose their territory to the populist leader anyway*. Is it a good idea to give the player the option to do this as well, without clearly spelling out what they are signing up for? Click to expand...
<!-- artifact:quote:end -->
Thanks for the answer! This is a good exploration of the problems these revolts lead to.

## Reply 46 — participant_028 · 2022-08-07 · post-28410745

It‘s great to hear basic things which have never been touched since launch being reviewed and made better! I‘d love to see more like this in many different aspects of the game! Keep up the good work

## Reply 47 — participant_029 · 2022-08-09 · post-28412935

PRAISE THE LORD! I am elated. Since release day, I have had so many games ruined due to the silly mechanics of populist factions. I cannot wait to play with these changes.

## Reply 48 — participant_030 · 2022-08-09 · post-28412982

This feels like a not dev-diary dev diary. I like it a lot... like a dev actually reaching out and sharing their thoughts and asking for feedback. I feel like it's what a dev diary should be...

## Reply 49 — participant_031 · 2022-08-09 · post-28413179

<!-- artifact:quote:start -->
> Kenlin said: Personally, I think all defensive wars should be like this anyway, with any vassals in the claimed area given the call to arms. Click to expand...
<!-- artifact:quote:end -->
At least if the war would result in getting landless by it, the vassal should always join his/her liege. It is the natural thing to do.

## Reply 50 — participant_032 · 2022-08-09 · post-28413257

I'm really happy to finally see that the liege cannot just give away my character's land to the rebels without my character having no say at all in the matter. Thanks for the update, it is really needed

## Reply 51 — participant_033 · 2022-08-09 · post-28413275

<!-- artifact:quote:start -->
> johnty5 said: It’d be interesting if revolts always started at the single county-level - declaring war on the count of that county. If they beat the count, they could then expand and declare war on the Duke, then kingdom, then empire. As a ruler further up the food chain, you’d have to keep an eye on small peasant revolts happening to your counts - as they would have the potential to escalate/spread and eventually start causing you real problems. There’d be choices to be made about whether to help out a problematic vassal with their revolts - choosing between letting it rumble on and weakening them vs risking it expanding and biting you in the arse later. If a peasant revolt beat one of your vassals, maybe they’d issue demands (guarantee liege of their culture, guarantee no attempts at culture conversion or some such) that you could accept in order to stop the revolt from spreading at the expense of other vassal opinion/dread/whatever. Click to expand...
<!-- artifact:quote:end -->
Definitely not in the scope of what's being asked, but leaving this here. Wrote it earlier in the year and think it'd be an interesting direction for revolts to go in.

## Reply 52 — participant_034 · 2022-08-09 · post-28413370

<!-- artifact:quote:start -->
> Servancour said: If all goes well, they'll be included with the next major update. Though I can't say when that will be. Click to expand...
<!-- artifact:quote:end -->
That will be a great addition to the update. Can you tell us wherether the next Major update will be for a flavour pack or for an expansion?

## Reply 53 — participant_030 · 2022-08-09 · post-28413722

<!-- artifact:quote:start -->
> Kenlin said: Personally, I think all defensive wars should be like this anyway, with any vassals in the claimed area given the call to arms. Click to expand...
<!-- artifact:quote:end -->
I fully agree. It would give defenders a boost to their troop numbers and make wars harder for the attacker, which along with defender advantage stats I think is duly neccesary. The only potential issue I see is if you, as a player liege, let powerful vassals' armies die on purpose first so that their influence in factions is reduced. But that type of thinking actually seems par for the course for the middle ages... I actually have a wish for CK3 that vassals don't give troops to their liege, but instead act more like allies that you call to war.

## Reply 54 — participant_035 · 2022-08-10 · post-28414804

I think that overall it could bring many good improvements to Populist Factions. Only thing that bothers me is balance - these factions should be challanging and a real threat but not a pain in the ass (or mayby they should...? ). I think that balancing this (and explaining this balance mayby in some DD) will be important case here. But as I mentioned on start - overall very good improvements!

## Reply 55 — participant_036 · 2022-08-11 · post-28416030

improvements are good but I honestly think peasant rebellions need an entire overhaul. They aren't dangerous for the most part which is fine because that's historically accurate but they need to have stronger economic costs. Under the current system you just lose a bit of control in a province, that's hardly sounds like the economic cost of having to slaughter thousands of your own workers. If CK3 worked under a Pop system than like the rebellion failing should get like 20% of peasant Pops in the area killed or something, at least that would feel like I actually get punished for letting a peasant rebellion happen. The way things are now there isn't a serious downside to being hated because peasant rebels don't stand a chance and can't cause any real damage to the realm. But I kinda think I feel this way about war in general in CK3, its just not as devastating as it should be.

## Reply 56 — participant_037 · 2022-08-11 · post-28416193

<!-- artifact:quote:start -->
> Servancour said: Sadly, for technical reasons, that won't work for the rebels. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> tilly said: i worry having the leaders spawn in with a selection of baller traits is going to flood the world with really powerful dudes, though. Click to expand...
<!-- artifact:quote:end -->
Technical reasons in terms of unreasonable high effort or "just" out-of-scope for the upcoming patch, because it needs more changes than just script? Just a suggestion: what about highly increased injury/death risk for these popular leaders/commanders? (and reduced capture chance for commanders) That way they are less likely to stay in anyone's realm. Since capturing the leader is a quick-route to enforcing demands, maybe they should be a less powerful commander than the other ones. Because they'd be the most likely one to be able to recruit with the suggested change in mind. (justification: they are the charismatic leader that gets people to rise up, not the martial genius that makes sure they succeed.)

## Reply 57 — participant_037 · 2022-08-11 · post-28416195

<!-- artifact:quote:start -->
> Nawjak said: A few more ways to influence popular opinion would be nice, in my experience cultural acceptance plays only a minor role (and is extremely slow to change). Like visit county, hold speech, invest in county (for minuscule gameplay bonuses, yet gives popular opinion - like giving a gift to a vassal). Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Mööpelitintti said: We currently have the "contract assistance" interaction in the iberian struggle, where you can join a war in exchange for money if you contribute enough. We should also have same kind of interaction where you gift money to rebels in exchange for a hook or something similar... Maybe some characters accept these, while some personalities might only accept gifts with no strings attached. Click to expand...
<!-- artifact:quote:end -->
Yes. That is thoroughly needed. Popular opinion is largely unchangeable. Especially for larger areas you just took over. It will take many years to get cultural acceptance and faith conversion done to not have everyone hate you and there is no way around that. I like the "invest in county" option a lot. Use money to stabilize your realm. Show the populace that things will be improving in the long run. The bonus could be like +5-20% development growth in addition to the popular opinion bonus for 10 years (with a significant cost that scales harder than linear). It really shouldn't be cheap, because that would allow players to use that as a default solution every time a populist faction rises up. Yes, or a general "offer war support" that could be done in secret. I.e. not joining a dissolution war, but funding it, because you'd still profit off of it. (Or funding a foreign dissolution war). A mechanic like that could either directly be money for mercenaries or significant buff to levy reinforcement rate + levy size. (or both) With potentially three categories ("token support" (minor cost, minor opinion boost), "war support"(significant cost, strong opinion boost) and a level of obscene support (obnoxiously high cost, very strong opinion boost)). The more support you give the more likely you will be found out and the opposing side gets a significant malus scaled to your support.

## Reply 58 — participant_032 · 2022-08-11 · post-28416293

I agree that jacqueries should be more costly, but also if they're going to be that, the popular opinion and the entire nobles-commoners relations should be worked from just a statistic to a playable mechanic that lets to actually avoid the jacquerie by making reasonable concessions to the commoners without just "losing" to the peasants "ultimatum".

## Reply 59 — participant_038 · 2022-08-11 · post-28416680

<!-- artifact:quote:start -->
> The last point was somewhat made better with the cultural rework in Royal Court, and the introduction of cultural acceptance. The rework gave you a new tool to influence and reduce the overall impact of popular opinion. I’d like to explore popular opinion further in the future, but for now, let’s focus on resolving the other two issues. Click to expand...
<!-- artifact:quote:end -->
First I want to say that I'm very happy with making the populist factions more of a real threat. However, I really think you should update popular opinion before you do this update. The extra challenge is good, but people are going to get frustrated when they have no way of preventing a populist faction. Look at tyranny, independence, or claim throne factions. They can be extremely deadly, but you can influence your vassals with several different ways to make them drop out of the faction; feasts, pilgrimages for religious opinion, improve relations, jailing, and gaining dread. If we are going to add this new threat then their needs to be more you can do to prevent it. If you're just a vassal then I understand not being able to influence it, but as top liege you really should have options. Whatever system you could come up for this would also give the players something new to manage in their realm, which will give players more to do in the mid-late game.

## Reply 60 — participant_039 · 2022-08-12 · post-28418539

It would be nice if there were ways of dealing with (as the top liege) and participating with (as a vassal) a populist faction outside the very binary choice of war/not war. For instance, choosing to support/promote a faction with diplomacy, cash or intrigue would open up so much more player choice. Buttons to advance/retard a faction's trigger level using your diplomacy/intrigue skill and funnel funds into the army size would be a simple mechanism to allow much more advanced gameplay.

## Reply 61 — participant_040 · 2022-08-13 · post-28418916

Hi I really like these changes But I have a question: Can you make it that your culture or religious rebels in country you declare war to are not hostile to you? For example catholic rebels are hostile to you, crusader, during crusade, which is really weird. At the very least made it for religious rebels and holy wars

## Reply 62 — participant_041 · 2022-08-31 · post-28446956

It isn't just Populist Factions that need a rework. It is all factions. Please make them be more similar to factions in CK+. Please. They suck now, they are fundamentally broken and unfun, they're terrible. They need to be reworked so that they pursue goals that may or may not align with the player's goals, a bit like IG's in V3. I cannot think of anything the game needs more.

## Reply 63 — participant_006 · 2023-04-30 · post-28907005

For populist revolts, their troop numbers depend on the number of counties in the faction, and how bad their opinion is. A worse popular opinion will mean more angry peasants with pitchforks. It is possible that your war with the king lasted long enough to drive up the offensive war opinion penalty, which made things worse. It definitely doesn't have to be game over. You could try white peacing with the king (or swiftly defeating him) so you have one war to focus on with more levies. Usual things with trying to get allies involved and cutting off small armies, mercenaries, trying to take out the revolt leader. Sounds like it won't be easy, and it may be impossible or unlikely. It is worth remembering that a setback doesn't have to be a game over. If you lose the war and they go independent, you now have the new direction for your campaign. Perhaps your current (or next) Emperor/Empress can gradually take these upstart peasants down, making sure to convert them to Odin. Maybe this will convince the Emperor to convert to Christianity. Either way, if you can avoid having the majority of your realm hate you it will help your stability next time. Although it doesn't seem like it initially, sometimes something like this can be good, because it makes your campaign more interesting and memorable. Either way, good luck

## Reply 64 — participant_042 · 2023-04-30 · post-28907934

<!-- artifact:quote:start -->
> Slow Bathroom said: I don't think making the revolts stronger will make things more interesting, I'm still just going to raise my army next to theirs and walk into them. Click to expand...
<!-- artifact:quote:end -->
a way to counter this would be to make the rally points take even longer to assemble the troops the further away from the capital you are raising them in.

