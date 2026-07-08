---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1492792/"
forum_thread_id: 1492792
content_type: reply_thread
parent_dd_file: dd_075_2021-09-28_crusader-kings-3-dev-diary-75-in-the-eve.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 75
title: "Crusader Kings 3 Dev Diary #75 - In the Event of Court Events"
dd_date: 2021-09-28
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 7
reply_count: 123
participant_count: 82
reply_date_first: 2021-09-28
reply_date_last: 2021-10-06
body_word_count: 7776
inline_image_count: 0
quoted_span_count: 86
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Crusader Kings 3 Dev Diary #75 - In the Event of Court Events

*123 replies from 82 participants across 7 pages*

## Reply 1 — participant_001 · 2021-09-28 · post-27817364

Alright, now if JaLot would kindly put down the knife and release the hostage, we can all move on with our day.

## Reply 2 — participant_002 · 2021-09-28 · post-27817380

Awesome look into the new events! No new poses though? It'd be awesome to see more, as well as new and more elaborate animations for characters in court scenes. Maybe some walking around or talking?

## Reply 3 — participant_003 · 2021-09-28 · post-27817385

Nice, I welcome the chance to look at 3D character models more often. But the semi-bird's view is a bit weird, wouldn't mind a more conventional perspective.

## Reply 4 — participant_004 · 2021-09-28 · post-27817392

questions that only make sense in CK3: is that a problem of perspective or is that archbishop really a dwarf?

## Reply 5 — participant_005 · 2021-09-28 · post-27817393

"… and their optional nature. Unlike yearly events, court events are opt-in, meaning that you don’t have to take them if you don’t want to, in which case their default (neutral-ish) option will be selected after a long-ish time-out period." I immediately thought of two things. What about 1) A game option/decision to let your regent (or any other designated title) handle these matters if you don't? That way, their personality/skills/opinion plays into what decision is made. 2) What about asking specific characters for their thoughts on the matter? Again, the default could be the regent, where it's high-lighted to you what they'd do and it's your decision to take their suggestion or not.

## Reply 6 — participant_006 · 2021-09-28 · post-27817394

<!-- artifact:quote:start -->
> Wokeg said: Welcome comrades! In today’s (not at all late shutup SHUTUP) dev diary, we’ll be going over the new court-type event; many of you will likely have seen them a bit already in a few preceding dev diaries, but for the rest, allow me to formally introduce court-type events: View attachment 760580 This new event type is seen exclusively within the court view, where they replace standard character-type events. We added these because one of the major design limitations with character-type events is that they’re uhh… they’re small. Really, really, really small, and having comparatively little space to work with means they impose a lot of restrictions on their use. Those of you who mod, or have dabbled at modding, will likely know what I’m talking about: generally, a character event can only fit about three paragraphs of copy and 3-4 options before it starts to look a little naff. Less if there are characters or titles involved with very long names, or if you have to do a lot of paragraphing. There are good reasons for them to be this small - they get in the way less when popping up, it encourages concise delivery of information, and it frames the portrait characters in each event nicely. For the court scene, these considerations are (generally) moot, so we wanted to play around with a more liberal event format. We don’t need to worry about framing characters in the traditional sense since we show them in the scene, the player always opts into a court-type event and thus can’t have one pop-up unexpectedly, and though information (and options) still need to be reasonably concise, it’s nice to have a little room to flex the meaning of “concise” somewhat. View attachment 760581 From a player’s perspective, you’ll mostly interact with court-type events through the not-at-all-confusingly-named court events pool. Similar to random yearlies, court events reflect the life of your court just existing, with all the petty drama and courtly intrigue you’d expect from a medieval monarch’s household. They primarily involve characters consistently within your court (rather than far-flung vassals or guests), and often tie into court grandeur and your different levels of amenities. View attachment 760582 Other than their tone, size, and occasional number of options, the biggest differences that players will notice are their usage of different camera shots instead of backgrounds and portraits… View attachment 760583 View attachment 760584 View attachment 760585 … and their optional nature. Unlike yearly events, court events are opt-in, meaning that you don’t have to take them if you don’t want to, in which case their default (neutral-ish) option will be selected after a long-ish time-out period. To open a court event, you simply click on a button that’ll appear floating over one of your court’s relevant characters. Whenever you’ve got court events you could be checking, you’ll be notified via the Royal Court button in the right-hand panel. View attachment 760586 From a scripting perspective, court-type events share a fair amount of DNA with character-type events, but differ mostly in the form of their court_scene block. Usually, I’d go on to explain everything in a bit more depth inside the dev diary itself, but since court-type events can be tricksy to script till you get the hang of ‘em, we’ve included an example court-type event inside one of the event files that breaks down their make-up: View attachment 760587 ^^ Hopefully, this should be a solid annotated example, but just in case, here’s a few pre-emptive clarifications: 1) Every court-type event must have a button character, even if that character is just your character, so that must always be set up. 2) The group parameter defines which spot in the scene that character stands in. These groups themselves are scriptable (with a bit of work) elsewhere, so you can arrange characters inside the court however you like. The groups shown in the example actually contain multiple different preset positions within the court scene, one of which is selected randomly for each event when it tries to fire. 3) For animations, we can access all the standard ones, plus a slew of new animations created specifically for the court scene. Finally, just for fun, let’s have some more court events: View attachment 760588 View attachment 760589 View attachment 760590 Oh, right, yes, I titled the dev diary “and friend” too, didn’t I? Welp, the new court-type isn’t the only event type we’re adding with this expansion (just the most exciting). We also have the new duel event type! Duels were added as part of our first flavour pack, but I’m sure you’ve all noticed that the space for ‘em is pretty limited, and the animations don’t work so well for this context. Welp, we’ve revamped both of those with this new type, giving duels a face-lift: View attachment 760591 … Naturally, the weapon held by either character does correspond to their signature weapon type, or whatever weapon artefact they have equipped (if they’ve got one). And that’s all from me, folks. As ever, I’ll be around in the comments for an hour or so to answer questions, but otherwise, see y’all next diary! Click to expand...
<!-- artifact:quote:end -->
Niiice! But big question I have is, when will you talk about the patch notes? I am also very interested in seeing if GHWs are fixed, AI is more potent and many more things.

## Reply 7 — participant_007 · 2021-09-28 · post-27817396

"There are good reasons for them to be this small - they get in the way less when popping up" Proceeds to show tiny bishop.

## Reply 8 — participant_008 · 2021-09-28 · post-27817397

The weapons in the duels look great! Also thanks for showing the script for the court events! I'm always one who likes to see how things look scriptwise!

## Reply 9 — participant_009 · 2021-09-28 · post-27817399

<!-- artifact:quote:start -->
> Axis89 said: Niiice! But big question I have is, when will you talk about the patch notes? I am also very interested in seeing if GHWs are fixed, AI is more potent and many more things. Click to expand...
<!-- artifact:quote:end -->
99% of the time they do near release.

## Reply 10 — participant_010 · 2021-09-28 · post-27817403

Ooh, how amazing! I love the flavour this will bring! I simply must ask though, shall the court events vary based upon region? It feels like there are some events that are very oriented to Europe but can pop up anywhere in the current game.

## Reply 11 — participant_011 · 2021-09-28 · post-27817405

<!-- artifact:quote:start -->
> Wokeg said: Alright, now if JaLot would kindly put down the knife and release the hostage, we can all move on with our day. Click to expand...
<!-- artifact:quote:end -->
and the release date is still unclear?

## Reply 12 — participant_012 · 2021-09-28 · post-27817408

<!-- artifact:quote:start -->
> Wokeg said: Alright, now if JaLot would kindly put down the knife and release the hostage, we can all move on with our day. Click to expand...
<!-- artifact:quote:end -->
Glitterhoof has been released to his family relatively stab wound free.

## Reply 13 — participant_013 · 2021-09-28 · post-27817409

"I titled the dev diary “and friend” too" What was the original title?

## Reply 14 — participant_014 · 2021-09-28 · post-27817412

<!-- artifact:quote:start -->
> UberEpicZach said: The weapons in the duels look great! Also thanks for showing the script for the court events! I'm always one who likes to see how things look scriptwise! Click to expand...
<!-- artifact:quote:end -->
Would be better with proper armor. XD

## Reply 15 — participant_015 · 2021-09-28 · post-27817413

any info on release date? please? PLEASE?

## Reply 16 — participant_016 · 2021-09-28 · post-27817414

<!-- artifact:quote:start -->
> Wokeg said: From a player’s perspective, you’ll mostly interact with court-type events through the not-at-all-confusingly-named court events pool. Similar to random yearlies, court events reflect the life of your court just existing, with all the petty drama and courtly intrigue you’d expect from a medieval monarch’s household. They primarily involve characters consistently within your court (rather than far-flung vassals or guests), and often tie into court grandeur and your different levels of amenities. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Wokeg said: Oh, right, yes, I titled the dev diary “and friend” too, didn’t I? Welp, the new court-type isn’t the only event type we’re adding with this expansion (just the most exciting). We also have the new duel event type! Duels were added as part of our first flavour pack, but I’m sure you’ve all noticed that the space for ‘em is pretty limited, and the animations don’t work so well for this context. Welp, we’ve revamped both of those with this new type, giving duels a face-lift: … Naturally, the weapon held by either character does correspond to their signature weapon type, or whatever weapon artefact they have equipped (if they’ve got one). And that’s all from me, folks. As ever, I’ll be around in the comments for an hour or so to answer questions, but otherwise, see y’all next diary! Click to expand...
<!-- artifact:quote:end -->
Courtiers are typically the characters I care about the least, and vassals are typically the characters I care about the most. Game mechanics basically demand this - courtiers are powerless and irrelevant, and vassals are a constant threat. Will this expansion give me more reason to care about courtiers, or will this just be even more events about characters that don't matter to me? A new event interface is not what duels needed. The problem with duels is that we can't duel anyone important to us, we can only duel distant adulterous counts who we've never interacted with. Adding a new UI on top of that half-baked system is just lipstick on a pig.

## Reply 17 — participant_017 · 2021-09-28 · post-27817415

Tiny nitpick but can the characters in the duel event be wearing armor seems weird seeing a man dressed in full fancy court clothes about to wack someone with a hammer

## Reply 18 — participant_018 · 2021-09-28 · post-27817421

Perhaps I missed it in the code… but does the context of the event tie to actual character behavior? If a court event says a particular character is present at every banquet… is that true? Is there a connection? For example was the character present at the last two banquets?

## Reply 19 — participant_019 · 2021-09-28 · post-27817428

It seems that the Christian Iberians are using the Byzantine Court Architecture. Could it be changed so that Iberian cultures (and maybe North Italians too, Sicilian is just a different thing) use the Western Court Architecture? There was a very strong influence of French art in Spain during CK3 time period, they too employed the Romanesque and Gothic styles, and sometimes also French craftsmen. The Court here just looks too Byzantine to me in comparison to the experience I have visiting Medieval Castles and Royal Palaces in Spain.

## Reply 20 — participant_020 · 2021-09-28 · post-27817431

<!-- artifact:quote:start -->
> King Anund said: It seems that the Christian Iberians are using the Byzantine Court Architecture. Could it be changed so that Iberian cultures (and maybe North Italians too, Sicilian is just a different thing) use the Western Court Architecture? There was a very strong influence of French art in Spain during CK3 time period, they too employed the Romanesque and Gothic styles, and sometimes also French craftsmen. The Court here just looks too Byzantine to me in comparison to the experience I have visiting Medieval Castles and Royal Palaces in Spain. Click to expand...
<!-- artifact:quote:end -->
Mediterranean actually. It would be either that or the default Euro court I defer to you though concerning the art style

## Reply 21 — participant_001 · 2021-09-28 · post-27817434

<!-- artifact:quote:start -->
> Sword of Glass said: Awesome look into the new events! No new poses though? It'd be awesome to see more, as well as new and more elaborate animations for characters in court scenes. Maybe some walking around or talking? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> anbeck said: Nice, I welcome the chance to look at 3D character models more often. But the semi-bird's view is a bit weird, wouldn't mind a more conventional perspective. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Lucododosor said: questions that only make sense in CK3: is that a problem of perspective or is that archbishop really a dwarf? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Jaevelklein said: "… and their optional nature. Unlike yearly events, court events are opt-in, meaning that you don’t have to take them if you don’t want to, in which case their default (neutral-ish) option will be selected after a long-ish time-out period." I immediately thought of two things. What about 1) A game option/decision to let your regent (or any other designated title) handle these matters if you don't? That way, their personality/skills/opinion plays into what decision is made. 2) What about asking specific characters for their thoughts on the matter? Again, the default could be the regent, where it's high-lighted to you what they'd do and it's your decision to take their suggestion or not. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Axis89 said: Niiice! But big question I have is, when will you talk about the patch notes? I am also very interested in seeing if GHWs are fixed, AI is more potent and many more things. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> UberEpicZach said: The weapons in the duels look great! Also thanks for showing the script for the court events! I'm always one who likes to see how things look scriptwise! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> InfinitySmiles said: Ooh, how amazing! I love the flavour this will bring! I simply must ask though, shall the court events vary based upon region? It feels like there are some events that are very oriented to Europe but can pop up anywhere in the current game. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> JaLot said: Glitterhoof has been released to his family relatively stab wound free. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> aantia said: "I titled the dev diary “and friend” too" What was the original title? Click to expand...
<!-- artifact:quote:end -->
We *do* have new poses, but I'm afraid I've been a bit selfish and not shown them off here. ^^' I suspect Art might prefer to be the ones to show of their gorgeous new animations. This is fair: perspective are all still somewhat WIP, and I expect we'll adjust at least a few a bit in future after player feedback. Naturally we're trying to get them as good as we can before release, though. He is, indeed, a dwarf. 1) I'm afraid that'd be pretty far out of scope to add, though live the spirit. 2) That actually does happen in the petition events last week's diary covered, but it'd be a prohibitive amount of extra time to add it to all of these events. I don't set the diary schedule, but traditionally I believe we do those in the last diary before release. Unsure what issues exactly you're having with GHWs, but I did fix a bunch of their broken targeting systems a while back. ^^ Thanks! Some do, some are more universal. We'd definitely like to vary up our regional content more and more in future. _Phew_, ok, that was a concern. _Shhhhhhhhhhhhhh, you didn't see anything, no one forbade me to use the *original* title shhhhhhhhhh_.

## Reply 22 — participant_021 · 2021-09-28 · post-27817439

what happens to the court when during a raid or a siege or even when someone else conquers the holding containing the court?

## Reply 23 — participant_022 · 2021-09-28 · post-27817442

Makes me wonder if there's the posibility of an Erfurt Latrine Desaster like event.

## Reply 24 — participant_019 · 2021-09-28 · post-27817443

<!-- artifact:quote:start -->
> Koyraboro said: Mediterranean actually. It would be either that or the default Euro court I defer to you though concerning the art style Click to expand...
<!-- artifact:quote:end -->
Yes. IMO the default European court looks more fitting to Christian Spanish Architecture. Is quite obvious that the Mediterranean has been conceived with Byzantium in mind.

## Reply 25 — participant_023 · 2021-09-28 · post-27817447

Isn't that silly how they discuss some pagan books and can "pretend they saw nothing" in the middle of small room surrounded by dozen of people looking in their direction and probably hearing what they are talking about? That kind of event text really needs some work because it looks ridiculous when it mentions only 2-3 people in the event while everyone else is right here! At least put the event characters in the actual corner --- Also, adding weapons to duels is a nice touch, but why are they fighting in their dresses, crowns and capes?? They should also automatically switch to combat clothes

## Reply 26 — participant_002 · 2021-09-28 · post-27817451

<!-- artifact:quote:start -->
> Wokeg said: We *do* have new poses, but I'm afraid I've been a bit selfish and not shown them off here. ^^' I suspect Art might prefer to be the ones to show of their gorgeous new animations. Click to expand...
<!-- artifact:quote:end -->
HELL YES! New poses and animations for the Court are what I'm most looking for in this expansion in all honesty- just seeing all our characters interact with each other in different ways livens up the imagination so much.

## Reply 27 — participant_024 · 2021-09-28 · post-27817455

I'm not... sure about these 3D scenes. I like the event pictures with 3d characters, but this I'm not sure. I really hope lightning, camera position, etc could be improved.

## Reply 28 — participant_025 · 2021-09-28 · post-27817456

Out of curiosity, just exactly what part of the DD took the whole of 3 1/2 hours?

## Reply 29 — participant_026 · 2021-09-28 · post-27817463

What's Glitterhoof doing there. Sneaky little horse.

## Reply 30 — participant_027 · 2021-09-28 · post-27817467

The court events look pretty good judging from the screenshots. I am curious how they will feel compared to the other types of events. Regarding the duels: I have played a fair bit of CK3 since the duel system was introduced, and so far I have seen one (1) actual duel take place, which I lost because my character wasn't a good fighter. A lot of "duels" in events are still just regular prowess-checks, and there aren't that many opportunities to duel people given by the mechanics unless your character is wrathful or irritable. I hope that there will be more opportunities for duels to happen in 1.5, because then I might actually get to appreciate the new UI a bit more.

## Reply 31 — participant_018 · 2021-09-28 · post-27817476

Is there any connection to a player not holding court contributing to faction growth?

## Reply 32 — participant_016 · 2021-09-28 · post-27817482

<!-- artifact:quote:start -->
> Vityviktor said: I'm not... sure about these 3D scenes. I like the event pictures with 3d characters, but this I'm not sure. I really hope lightning, camera position, etc could be improved. Click to expand...
<!-- artifact:quote:end -->
Agree, the lighting and poses make it look like just a pile of 3D models pasted together onto a backround, not a coherent scene. I know CK3 isn't the sort of game that's going to have cutting-edge graphics, and that's perfectly fine, but they've landed in a sort of uncanny valley that is really unpleasant to look at. Hopefully these are just WIP and things will look a little more natural when everything's finished.

## Reply 33 — participant_018 · 2021-09-28 · post-27817485

Looking at the dwarf Archbishop, he doesn’t look like a dwarf. Any plans to adjust scaling of body and clothing somewhat to adjust proportions and make them look more realistic or as if clothing is a bit oversized?

## Reply 34 — participant_028 · 2021-09-28 · post-27817490

<!-- artifact:quote:start -->
> anbeck said: Nice, I welcome the chance to look at 3D character models more often. But the semi-bird's view is a bit weird, wouldn't mind a more conventional perspective. Click to expand...
<!-- artifact:quote:end -->
Yeah I was gonna say that, it looks to me like CCTV footage. I'd prefer something a bit more cinematic.

## Reply 35 — participant_029 · 2021-09-28 · post-27817491

It would be awesome if normal events were "optional" with notifications just like these. That way the player could select them when they want and it won't prevent them from focusing on something else. And conversely it would make something more to check when they are bored because there is not war currently.

## Reply 36 — participant_030 · 2021-09-28 · post-27817497

As a modder I'm loving the potential of the new event type... but... I see one major problem that will limit its useability significantly: since the "court scene" appears to be limited to Kings and above, and Dukes and down don't have their own physical HQ kind of place, I'm afraid it will be hard to incorporate these kinds of events in content aimed at all title tiers ._. Hopefully with future updates we might see everyone eventually get access to their own court/manor/rented-closet-at-a-cheap-inn. It's such a fun feature with so much potential that it would be a shame to limit it to the 1% of playable characters

## Reply 37 — participant_031 · 2021-09-28 · post-27817499

Are the new duel events part of the DLC, or are they included free in the update?

## Reply 38 — participant_032 · 2021-09-28 · post-27817507

Duel changes look great. A couple thoughts: 1. agree with those saying they should be in armor, not Royal garb. 2. I would love to see these type of events happening on the battlefield if you are leading your own troops! Duels are rare, so won’t see this new feature often, but having this pop up on occasion in war would make war more interesting and allow us to see this cool mechanic more often. If not for this patch, sure, can’t rush it, but definitely put it on a wish list for later.

## Reply 39 — participant_033 · 2021-09-28 · post-27817519

Is the game always paused when you are in court view? Also, are there loading times or any performance hit going from map view to court view?

## Reply 40 — participant_034 · 2021-09-28 · post-27817521

I really hope the duel screen could show a health bar or something else, thus making it a mini-game, I mean, like Pokemon.

## Reply 41 — participant_004 · 2021-09-28 · post-27817527

<!-- artifact:quote:start -->
> Wokeg said: Similar to random yearlies, court events reflect the life of your court just existing, with all the petty drama and courtly intrigue you’d expect from a medieval monarch’s household. They primarily involve characters consistently within your court (rather than far-flung vassals or guests), and often tie into court grandeur and your different levels of amenities. Click to expand...
<!-- artifact:quote:end -->
So how often do you interact with your vassals in court events? Based on the images released it looks like very rarely, which is disappointing. I would much prefer deeper interactions with in-game characters I should care about, vassals, rather than people who are not terribly important, all things considered. I find it hard to care about random courtiers when you don't really interact with them regularly anyway, which is a real problem with the game right. Its hard to form connections with characters when you don't interact with them or if they don't "matter" to the player, however you want to define that. I would much rather the game improve liege/vassal relationships rather than try and make you care about random courtiers or guests. Also, are there going to be game rulers involving the court mechanics? Will you be able to turn certain mechanics on and off? Could you, for example, keep artifacts while turning off the ability to hold court?

## Reply 42 — participant_001 · 2021-09-28 · post-27817537

<!-- artifact:quote:start -->
> Dadoverde said: Would be better with proper armor. XD Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> KermitxTheFrog said: Tiny nitpick but can the characters in the duel event be wearing armor seems weird seeing a man dressed in full fancy court clothes about to wack someone with a hammer Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Miroku20X6 said: 1. agree with those saying they should be in armor, not Royal garb. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> james24eagle said: Perhaps I missed it in the code… but does the context of the event tie to actual character behavior? If a court event says a particular character is present at every banquet… is that true? Is there a connection? For example was the character present at the last two banquets? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> King Anund said: It seems that the Christian Iberians are using the Byzantine Court Architecture. Could it be changed so that Iberian cultures (and maybe North Italians too, Sicilian is just a different thing) use the Western Court Architecture? There was a very strong influence of French art in Spain during CK3 time period, they too employed the Romanesque and Gothic styles, and sometimes also French craftsmen. The Court here just looks too Byzantine to me in comparison to the experience I have visiting Medieval Castles and Royal Palaces in Spain. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> IWST said: Makes me wonder if there's the posibility of an Erfurt Latrine Desaster like event. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Vityviktor said: I'm not... sure about these 3D scenes. I like the event pictures with 3d characters, but this I'm not sure. I really hope lightning, camera position, etc could be improved. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Admiral Boysen said: Out of curiosity, just exactly what part of the DD took the whole of 3 1/2 hours? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> EmeraldThanatos said: What's Glitterhoof doing there. Sneaky little horse. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> fodazd said: The court events look pretty good judging from the screenshots. I am curious how they will feel compared to the other types of events. Regarding the duels: I have played a fair bit of CK3 since the duel system was introduced, and so far I have seen one (1) actual duel take place, which I lost because my character wasn't a good fighter. A lot of "duels" in events are still just regular prowess-checks, and there aren't that many opportunities to duel people given by the mechanics unless your character is wrathful or irritable. I hope that there will be more opportunities for duels to happen in 1.5, because then I might actually get to appreciate the new UI a bit more. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> james24eagle said: Is there any connection to a player not holding court contributing to faction growth? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> james24eagle said: Looking at the dwarf Archbishop, he doesn’t look like a dwarf. Any plans to adjust scaling of body and clothing somewhat to adjust proportions and make them look more realistic or as if clothing is a bit oversized? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> ajokitty said: Are the new duel events part of the DLC, or are they included free in the update? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Miroku20X6 said: Duel changes look great. A couple thoughts: 2. I would love to see these type of events happening on the battlefield if you are leading your own troops! Duels are rare, so won’t see this new feature often, but having this pop up on occasion in war would make war more interesting and allow us to see this cool mechanic more often. If not for this patch, sure, can’t rush it, but definitely put it on a wish list for later. Click to expand...
<!-- artifact:quote:end -->
Valid; it's on my list of polish things to sort for the duel system (still haven't added cheating!), but not something I've gotten around to yet, I'm afraid. Depends on the event: generally, when writing events, we try to pick appropriate characters through the trigger block but don't set things up to ensure the copy is definitely 100% accurate, only that it seems accurate at a glance/with a bit of casual digging. Sadly, if we were to track such things, it'd likely merc both save game size and a bit of performance. Interesting; we might have defaulted a little bit too much to later medieval Iberian architecture, which (at least, IME) tends to have more of a flourish. I'll raise this internally! Funnily enough, there is a follow-up event to this one if you ignore the problem and get unlucky... Lighting, positioning, et al are all WIP. We'll continue adjusting, tweaking, and improving such as we go, but sadly one of the issues with dev diary screenshots is that they mean we're showing unfinished or unpolished work, so it'll rarely look quite as good as the final thing. I'm afraid that it was insinuated that if I went into details on that, I wouldn't be writing much script any time soon. Rest assured that the parties responsible are have been dealt with. Permanently. That's uhh... a supervisory horse. Doing. Supervising things. Yeah. ^^' Aggh, yeah, we do need to go through and do more updating of older content for this. Certainly some duels we're happy to keep as prowess checks (essentially anything that doesn't need a full fight), but some could really use the new system. A handful of the new court events do, FWIW, and there's a bit of cultural tradition stuff related to duelling. :thinking_face: Not as far as I'm aware. ^^' Not my department, I'm afraid. Not that I know of, though. It's just the UI! The duel system came in with the first flavour pack. The UI is, however, free, as was the system. I've gone into this a little elsewhere, but essentially it's a deliberate design decision not to have overt battlefield events pop up like this, since they get in the way of army movement and, especially in MP, they'd be an active nuisance.

## Reply 43 — participant_021 · 2021-09-28 · post-27817542

<!-- artifact:quote:start -->
> Miroku20X6 said: Duel changes look great. A couple thoughts: 1. agree with those saying they should be in armor, not Royal garb. 2. I would love to see these type of events happening on the battlefield if you are leading your own troops! Duels are rare, so won’t see this new feature often, but having this pop up on occasion in war would make war more interesting and allow us to see this cool mechanic more often. If not for this patch, sure, can’t rush it, but definitely put it on a wish list for later. Click to expand...
<!-- artifact:quote:end -->
I've seen Norse characters fight naked and become naked during a fight so I don't see why wearing an armour would be any different

## Reply 44 — participant_001 · 2021-09-28 · post-27817548

<!-- artifact:quote:start -->
> tribnia said: I really hope the duel screen could show a health bar or something else, thus making it a mini-game, I mean, like Pokemon. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> InsidiousMage said: So how often do you interact with your vassals in court events? Based on the images released it looks like very rarely, which is disappointing. I would much prefer deeper interactions with in-game characters I should care about, vassals, rather than people who are not terribly important, all things considered. I find it hard to care about random courtiers when you don't really interact with them regularly anyway, which is a real problem with the game right. Its hard to form connections with characters when you don't interact with them or if they don't "matter" to the player, however you want to define that. I would much rather the game improve liege/vassal relationships rather than try and make you care about random courtiers or guests. Also, are there going to be game rulers involving the court mechanics? Will you be able to turn certain mechanics on and off? Could you, for example, keep artifacts while turning off the ability to hold court? Click to expand...
<!-- artifact:quote:end -->
^^' Yeah, eventually I'd like to see a more graphical solution for how we represent current status in duels. No plans for that for this release as far as I'm aware, I'm afraid. Generally, court events are more focused on the people who are actually physically present in your court. Vassals aren't ruled out, but they tend to be included more if you'd see them mooching around the palace from time to time; councillors, powerful vassals, that type of thing. I will say that us not providing content for interacting with courtiers or your family might worsen not feeling connected to them. Artefacts are entirely too integral to be turned on or off via game rule, I'm afraid, and we've not plans make hold court optional via game rule. I don't believe we have any game rules for court mechanics at the moment.

## Reply 45 — participant_016 · 2021-09-28 · post-27817557

<!-- artifact:quote:start -->
> Wokeg said: I will say that us not providing content for interacting with courtiers or your family might worsen not feeling connected to them. Click to expand...
<!-- artifact:quote:end -->
Courtiers and family already show up a lot in events. Lack of content isn't the reason we don't feel connected to them, the reason is that that content is not impactful. It doesn't matter if I pick the option that offends my courtier, because nothing will ever come of that - the world will march on just the same as it would if I had appeased him. Perhaps if courtiers grew into friends and rivals (other than by sitting forgotten in your dungeon for a few decades), or had some more connection to other game systems, it'd be different. As an example, suppose an event gives me a strong hook on a lowborn courtier. What can I realistically use that for? It feels like the answer is very often "nothing" - even if I have the maximum amount of leverage over this character, there is nothing I can accomplish with it. It doesn't matter how often that character shows up in an event, it's going to be really difficult for me to care about them, because they don't matter to the game world.

## Reply 46 — participant_027 · 2021-09-28 · post-27817569

<!-- artifact:quote:start -->
> Wokeg said: ^^' Aggh, yeah, we do need to go through and do more updating of older content for this. Certainly some duels we're happy to keep as prowess checks (essentially anything that doesn't need a full fight), but some could really use the new system. A handful of the new court events do, FWIW, and there's a bit of cultural tradition stuff related to duelling. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Wokeg said: I've gone into this a little elsewhere, but essentially it's a deliberate design decision not to have overt battlefield events pop up like this, since they get in the way of army movement and, especially in MP, they'd be an active nuisance. Click to expand...
<!-- artifact:quote:end -->
I am glad to hear that there is additional duel-content coming. I understand this logic when it comes to multiplayer, because the game doesn't pause on events there, but I still think that this decision is a huge missed opportunity for single player.

## Reply 47 — participant_023 · 2021-09-28 · post-27817580

<!-- artifact:quote:start -->
> Tiax said: Courtiers and family already show up a lot in events. Lack of content isn't the reason we don't feel connected to them, the reason is that that content is not impactful. It doesn't matter if I pick the option that offends my courtier, because nothing will ever come of that - the world will march on just the same as it would if I had appeased him. Perhaps if courtiers grew into friends and rivals (other than by sitting forgotten in your dungeon for a few decades), or had some more connection to other game systems, it'd be different. Click to expand...
<!-- artifact:quote:end -->
Even if they would become rivals, you can just always send them away from your court, so "courtier opinion doesn't matter" doubles down here

## Reply 48 — participant_035 · 2021-09-28 · post-27817590

<!-- artifact:quote:start -->
> EmeraldThanatos said: What's Glitterhoof doing there. Sneaky little horse. Click to expand...
<!-- artifact:quote:end -->
And absconded with the imperial crown too!

## Reply 49 — participant_036 · 2021-09-28 · post-27817601

Why is there no option to let poor Rashid eat all the comfit he wants in peace?

## Reply 50 — participant_017 · 2021-09-28 · post-27817602

I think it would be cool if one of the outcomes of an assassination attempt was dueling one of the higher prowess agents in the plot. For instance if you got the bodyguard of the ruler in on the plot he tries to ambush the king and the king yanks a ceremonial sword off a wall and starts a duel lose the duel and the king gets assassinated. It would just be a nice way to integrate the cool dueling system into the game more

## Reply 51 — participant_037 · 2021-09-28 · post-27817607

I see a Western European jester in an Islamic court. I suppose this confirms it then that we're gonna see jesters everywhere wearing the same clothing.

## Reply 52 — participant_038 · 2021-09-28 · post-27817629

Is it possible to have floating icons when court events are available too? Currently, we have three notification types, events that pause the game and pop-up on the screen, interactable notifications on top that we can choose to deal with or not, and temporary notifications on the bottom right (that I mostly ignore). Having a fourth small icon to keep an eye on would be annoying and I would miss so many court events compared to having a floating icon on the top of the screen. Also, will the 'hold court' decision be a decision (i.e. I can click to tell the game to notify me when I can use it) or only done via the court button?

## Reply 53 — participant_004 · 2021-09-28 · post-27817636

<!-- artifact:quote:start -->
> Wokeg said: Generally, court events are more focused on the people who are actually physically present in your court. Vassals aren't ruled out, but they tend to be included more if you'd see them mooching around the palace from time to time; councillors, powerful vassals, that type of thing. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Wokeg said: I will say that us not providing content for interacting with courtiers or your family might worsen not feeling connected to them. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Wokeg said: Artefacts are entirely too integral to be turned on or off via game rule, I'm afraid, and we've not plans make hold court optional via game rule. I don't believe we have any game rules for court mechanics at the moment. Click to expand...
<!-- artifact:quote:end -->
That's nice to know. On the one hand, sure, you can't care about someone if you don't interact with them. But, on the other hand, the game seems to be moving in the direction of more interactions with more characters, rather than more interactions but with a smaller number of characters. If I only interact with a character once or twice I'm not sure how I'm supposed to develop a relationship with them, which is what generally happens in the game right now. I'll get a notice that courtier X is attempting to murder courtier Y and I don't care because I've never seen either one of them before and I'm not sure that having to potentially mediate a dispute between them before they start trying to murder each would really make me care about them. All of the talk about why haven't people played the game recently got me to do a Kushitism game and I'm currently the Emperor of Abyssinia, I've got a dozen or so vassals and the one thing I would really like is more interaction with them right now, not my courtiers. I never interact with my courtiers because I've got enough vassals that anything I need done can be done by my vassals. Again, maybe this will change once I actually play with the DLC, but I'm not sure how I'm going to care about a random courtier that I only interact with once or twice in the context of holding court versus the ability to deepen my connection with my vassals while holding court because I'm already interacting with them regularly anyway. That's disappointing. I'm really looking forward to culture rework, I'm interesting about artifacts but, and maybe playing with it will change my mind, I'm not terribly interested in the court mechanics right now. I would hate to have to turn off the entire DLC if I end up not liking the court mechanics since the rest looks interesting. Hopefully I'll be wrong and the court mechanics are really fun to interact with but I do hope the devs consider some games rules for the court mechanics in case people don't like them or just want to play the occasional game without them.

## Reply 54 — participant_004 · 2021-09-28 · post-27817650

<!-- artifact:quote:start -->
> Voy said: I see a Western European jester in an Islamic court. I suppose this confirms it then that we're gonna see jesters everywhere wearing the same clothing. Click to expand...
<!-- artifact:quote:end -->
I think someone just discovered some potential new content for upcoming flavor packs!

## Reply 55 — participant_039 · 2021-09-28 · post-27817658

It looks good I'm content enough with the look of the royal court for now. I hope in the future, with future flavour packs, you'll change up the court rooms so they don't all look so similar. Like, I can definitely see variation in carpets, wall decor, construction material, etc. That's great! But I can also see that all throne rooms, from Moorish Spain to the Byzantines to India to Scandinavia are exactly the same size, with the throne in the same place and position, etc. That works well for a DLC with a focus on gameplay features like this, but I hope in future flavour packs this is one of the things you can add to make a region feel more unique - by adding more unique throne room variation. I'm thinking tribes with wooden huts, mongols in tents, etc. This leaves the question, what about the Norse, who have already had a flavour pack?

## Reply 56 — participant_037 · 2021-09-28 · post-27817666

<!-- artifact:quote:start -->
> InsidiousMage said: I think someone just discovered some potential new content for upcoming flavor packs! Click to expand...
<!-- artifact:quote:end -->
I wouldn't personally applaud this. It would be better if future jester inspired courtiers were introduced in flavour packs than having to look at a Western replica (anachronistic until the late medieval ages no less) until they do add specific flavor several years down the line. Limit them to Western Europe, is what I'd say.

## Reply 57 — participant_040 · 2021-09-28 · post-27817681

The new court events, they are a nice addition.

## Reply 58 — participant_016 · 2021-09-28 · post-27817683

<!-- artifact:quote:start -->
> tsr-aph said: Is it possible to have floating icons when court events are available too? Currently, we have three notification types, events that pause the game and pop-up on the screen, interactable notifications on top that we can choose to deal with or not, and temporary notifications on the bottom right (that I mostly ignore). Having a fourth small icon to keep an eye on would be annoying and I would miss so many court events compared to having a floating icon on the top of the screen. Also, will the 'hold court' decision be a decision (i.e. I can click to tell the game to notify me when I can use it) or only done via the court button? Click to expand...
<!-- artifact:quote:end -->
Honestly I'm just happy they didn't decide to throw it into this useless black hole:

## Reply 59 — participant_041 · 2021-09-28 · post-27817704

Just imagine, Im asking my lord for some dutchies to keep my wife happy thank *BONK* im dead because he hits me with a hammer. And im now my 2 year old son and now stripped of my titles and land. Can I with no land get allies as i grow to try to retake what's mine?

## Reply 60 — participant_042 · 2021-09-28 · post-27817723

I feel like these forced court interactions instead of regular events will break the pace

## Reply 61 — participant_043 · 2021-09-28 · post-27817776

Has the problem where characters turn into skinny skeletons while wearing fighting trousers been fixed?

## Reply 62 — participant_044 · 2021-09-28 · post-27817794

So couldn't help but notice that the aesthetic for the Denmark and England courts, as well as the Asturian and Byzantine courts look different. Does this imply there are now more court visuals? So Denmark doesn't use western courts but instead maybe northern courts? And same for Asturias not using the byzantine/Mediterranean one?

## Reply 63 — participant_037 · 2021-09-28 · post-27817795

Why would King Svend of Denmark say "Since Sigrid joined my court..." when she's his daughter? I feel like this particular event needs some character flags because this is silly.

## Reply 64 — participant_037 · 2021-09-28 · post-27817801

Also, can we talk about the event texts on display in this devdiary ? Thesaurus come through.

## Reply 65 — participant_016 · 2021-09-28 · post-27817803

<!-- artifact:quote:start -->
> Voy said: Why would King Svend of Denmark say "Since Sigrid joined my court..." when she's his daughter? I feel like this particular event needs some character flags because this is silly. Click to expand...
<!-- artifact:quote:end -->
The man appears to have tucked his cape into his pants, he's clearly not the sharpest axe in the armory, if you know what I mean.

## Reply 66 — participant_045 · 2021-09-28 · post-27817810

<!-- artifact:quote:start -->
> Unknown Sage said: So couldn't help but notice that the aesthetic for the Denmark and England courts, as well as the Asturian and Byzantine courts look different. Does this imply there are now more court visuals? So Denmark doesn't use western courts but instead maybe northern courts? And same for Asturias not using the byzantine/Mediterranean one? Click to expand...
<!-- artifact:quote:end -->
That would be lovely!

## Reply 67 — participant_046 · 2021-09-28 · post-27817814

Is it me, or look the legs rather short of the characters?

## Reply 68 — participant_016 · 2021-09-28 · post-27817826

<!-- artifact:quote:start -->
> Wokeg said: View attachment 760583 Click to expand...
<!-- artifact:quote:end -->
Is Patriarch Prokopios standing next to the player in this scene because the event text mentions him by name, despite the fact that it's in the context of merely imagining what his reaction would be? If the system is that all the characters mentioned in the text will be present in the scene, you should probably write the text so that it implies they should be present.

## Reply 69 — participant_047 · 2021-09-28 · post-27817895

This is a welcome addition, "fluffy" events have a more important role in CK than the rest of PDX series. Having them in a pool of "optional" events potentially solves one of the problems that these kind of events have in PDX games - they are nice to read during peacetime, but can be an annoyance and distraction in war. Imperator has something resembling this, but with no royal court attached (but damn I'd love to see a Roman Senate in that game eh eh). What I'm intrigued about is that this court event pool basically opens a new way for event mods. If modders want to add events about courtlife, celebrations, audiences, life under siege, etc., they could go absolutely wild with them and never worry about "overdoing" them, since these events won't end up cluttering the map and pausing the game every 5 days.

## Reply 70 — participant_048 · 2021-09-28 · post-27817916

Yeeei my suggestion about weapons in duel event screens became true

## Reply 71 — participant_049 · 2021-09-28 · post-27817935

<!-- artifact:quote:start -->
> LukeCreed13 said: This is a welcome addition, "fluffy" events have a more important role in CK than the rest of PDX series. Having them in a pool of "optional" events potentially solves one of the problems that these kind of events have in PDX games - they are nice to read during peacetime, but can be an annoyance and distraction in war. Click to expand...
<!-- artifact:quote:end -->
Came here to say this. I know many people are still upset about the lack of options for event notifications, but I'm interested to see this system in action. Huge potential to smooth out some of the tonal clashes that happen due to the stochastic nature of events (e.g., I don't care about carp ponds when I'm laying siege to Baghdad). I think it's a great idea to separate events into "urgent" ones that players deal with immediately and less urgent ones that, if neglected over a long time, might simmer into discontent. Other than that, I don't get some of the negative reactions to this dev diary. I am a player who cares about some courtiers like individual knights. CK3 did a good job of cutting down on "useless" courtiers with their wandering system, and I'm happy to have more ways to interact with them. Do we need more vassal interactions? Yes, but I thought those were covered in separate court mechanics in another dev diary. Maybe I am missing something,

## Reply 72 — participant_050 · 2021-09-28 · post-27818007

When the DLC will be released ?

## Reply 73 — participant_051 · 2021-09-28 · post-27818026

<!-- artifact:quote:start -->
> Wokeg said: … and their optional nature. Unlike yearly events, court events are opt-in, meaning that you don’t have to take them if you don’t want to, in which case their default (neutral-ish) option will be selected after a long-ish time-out period. To open a court event, you simply click on a button that’ll appear floating over one of your court’s relevant characters. Whenever you’ve got court events you could be checking, you’ll be notified via the Royal Court button in the right-hand panel. Click to expand...
<!-- artifact:quote:end -->
Can mods bypass this? I.e. can modders trigger court-type events by normal means, like decisions etc., and have them pop up immediately?

## Reply 74 — participant_052 · 2021-09-28 · post-27818037

<!-- artifact:quote:start -->
> Wokeg said: I've gone into this a little elsewhere, but essentially it's a deliberate design decision not to have overt battlefield events pop up like this, since they get in the way of army movement and, especially in MP, they'd be an active nuisance. Click to expand...
<!-- artifact:quote:end -->
Would it be possible to make the events so they wouldn’t happen in multiplayer? Discarding interesting times for stuff to happen, just because it won’t work for a one type of game mode is rather unfortunate. Please, don’t let multiplayer limit the single player experience.

## Reply 75 — participant_053 · 2021-09-28 · post-27818054

Since there are duels, a knightly tournament is also needed ))

## Reply 76 — participant_054 · 2021-09-29 · post-27818231

<!-- artifact:quote:start -->
> Kvelen said: Since there are duels, a knightly tournament is also needed )) Click to expand...
<!-- artifact:quote:end -->
If they do bring back Tournaments, hopefully they are a bit more interesting and eventful now, not just an injury giveaway from Oprah like we had in vanilla CK2.

## Reply 77 — participant_021 · 2021-09-29 · post-27818277

<!-- artifact:quote:start -->
> Kvelen said: Since there are duels, a knightly tournament is also needed )) Click to expand...
<!-- artifact:quote:end -->
How about Mortal Kombat type duels in the following DLC?

## Reply 78 — participant_055 · 2021-09-29 · post-27818299

At this point every dev diary is a bit exasperating. A year in and only the one little flavor pack. Apparently we were spoiled with the fast paced ck2 dlc release schedule.... I hope the pace picks up a bit after this finally comes out.

## Reply 79 — participant_056 · 2021-09-29 · post-27818331

All this talk of Glitterhoof has got me wondering: Will there be any space in the court screen for our beloved pets? I seem to recall having a dog or cat periodically during my games, and even without appointing Glitterhoof to a council position, who doesn't enjoy the presence of a large tame reptile or hilariously drunken moose?

## Reply 80 — participant_057 · 2021-09-29 · post-27818375

Could there be meetups and exchanges of usual information when you hold feasts or go carousing? Maybe each lifestyle would give you an option to meet with people in different ways.

## Reply 81 — participant_058 · 2021-09-29 · post-27818381

I don't want you to rush, but how soon is Royal Court coming out?

## Reply 82 — participant_059 · 2021-09-29 · post-27818467

Seems like this will open up a lot of possibilities for modding if nothing else. Good!

## Reply 83 — participant_060 · 2021-09-29 · post-27818519

Overall, I'm liking what I'm seeing. As others have said, this offers a lot of potential for modders. It also gives us some stuff to do during peace when it can be dull. Graphics in the court scenes definitely needs some work - mainly lighting, clipping (or clothing moving in weird ways like that cape that appears tucked in), and camera positioning, but overall it's not bad. Some more variation in how the courts look would be appreciated so they don't all look the same in the same region - I'd rather not have every game where I play in Europe show the exact same court no matter who I play as. Maybe artifacts will help by having differences in wall hangings and displays and such, but I'd like to see some changes to layout of the room itself. Regarding duels in the middle of battles, I have always been opposed to the current design choice to not allow them. I liked having those in CK2 and miss them in CK3. Sure, in MP it might be a problem, but I'm sure you can decide on a way to handle that problem other than just remove these entirely. Maybe that's just removing them in MP but leaving them for SP or maybe something else. Either way, they are a nice addition that is sorely missing in CK3 right now. I'd love seeing some animals in the court scenes at some point. I remember a DD quite awhile ago mentioned crocodiles going on a rampage IIRC and would love to see that appear perhaps as a very rare easter egg type event where they appear in court so those of us who saw that old DD/dev post can get a laugh out of it. Even without something like that, just having certain animals that would potentially have been present in a court would add to the already great display. Maybe something like a caged bird (parrot, etc.), a dog by the ruler's throne, a peacock even. Having it be whatever pet you might have gotten in the game would be nice too, but it doesn't even have to be an actual pet but just the regular animals often seen in courts back then. I'd love to see Glitterhoof make an appearance... maybe an event where your courtier brings his horse through the court because he got lost on the way to the stables and you see the horse standing there. It would also be nice to see the "court" that is displayed adjust based on events. Labyrinthine Halls suggests that the event is in the halls and not in the court itself. Would it be that difficult to change the display to make it appear that you're in a hallway instead of the court itself? You could accomplish that with just a camera position that puts the camera closer to the wall so that you only see a small part of the floor and just the wall and the two people standing there. It would still be technically in the court, so no new graphics work needed. It would just need a different camera position. It might be a "cheat" way of doing it, but it would work pretty well. Otherwise, the event text should be changed to not suggest you're in a hallway while showing you in the court.

## Reply 84 — participant_044 · 2021-09-29 · post-27818757

<!-- artifact:quote:start -->
> NimbleShadow said: Admit it, the bird's-eye view camera angle is because you didn't make ceilings and chandeliers. Click to expand...
<!-- artifact:quote:end -->
Actually though if you look at the first image in dev diary 72. There is a clearly visible ceiling. Not quite a chandelier though, but it does have a nice-ish lamp

## Reply 85 — participant_061 · 2021-09-29 · post-27818842

Guh, I'm losing my mind waiting for this! The game feels so empty, knowing what's coming!

## Reply 86 — participant_062 · 2021-09-29 · post-27818956

The new weapon models are getting me hyped! Some questions though... 1: Will there be gunpowder artifacts? Considering how bombards are an innovation, I'd like to see if we could have all kinds of pre-1453 gunpowder weapons, from arquebus to flintlocks! 2: Will it be possible for soldiers in the court room to equip said weapons in their own pose if gunpowder's added? 3: Battlefield combat when?

## Reply 87 — participant_063 · 2021-09-29 · post-27819048

<!-- artifact:quote:start -->
> Wokeg said: Welcome comrades! In today’s (not at all late shutup SHUTUP) dev diary, we’ll be going over the new court-type event; many of you will likely have seen them a bit already in a few preceding dev diaries, but for the rest, allow me to formally introduce court-type events: View attachment 760580 This new event type is seen exclusively within the court view, where they replace standard character-type events. We added these because one of the major design limitations with character-type events is that they’re uhh… they’re small. Really, really, really small, and having comparatively little space to work with means they impose a lot of restrictions on their use. Those of you who mod, or have dabbled at modding, will likely know what I’m talking about: generally, a character event can only fit about three paragraphs of copy and 3-4 options before it starts to look a little naff. Less if there are characters or titles involved with very long names, or if you have to do a lot of paragraphing. There are good reasons for them to be this small - they get in the way less when popping up, it encourages concise delivery of information, and it frames the portrait characters in each event nicely. For the court scene, these considerations are (generally) moot, so we wanted to play around with a more liberal event format. We don’t need to worry about framing characters in the traditional sense since we show them in the scene, the player always opts into a court-type event and thus can’t have one pop-up unexpectedly, and though information (and options) still need to be reasonably concise, it’s nice to have a little room to flex the meaning of “concise” somewhat. View attachment 760581 From a player’s perspective, you’ll mostly interact with court-type events through the not-at-all-confusingly-named court events pool. Similar to random yearlies, court events reflect the life of your court just existing, with all the petty drama and courtly intrigue you’d expect from a medieval monarch’s household. They primarily involve characters consistently within your court (rather than far-flung vassals or guests), and often tie into court grandeur and your different levels of amenities. View attachment 760582 Other than their tone, size, and occasional number of options, the biggest differences that players will notice are their usage of different camera shots instead of backgrounds and portraits… View attachment 760583 View attachment 760584 View attachment 760585 … and their optional nature. Unlike yearly events, court events are opt-in, meaning that you don’t have to take them if you don’t want to, in which case their default (neutral-ish) option will be selected after a long-ish time-out period. To open a court event, you simply click on a button that’ll appear floating over one of your court’s relevant characters. Whenever you’ve got court events you could be checking, you’ll be notified via the Royal Court button in the right-hand panel. View attachment 760586 From a scripting perspective, court-type events share a fair amount of DNA with character-type events, but differ mostly in the form of their court_scene block. Usually, I’d go on to explain everything in a bit more depth inside the dev diary itself, but since court-type events can be tricksy to script till you get the hang of ‘em, we’ve included an example court-type event inside one of the event files that breaks down their make-up: View attachment 760587 ^^ Hopefully, this should be a solid annotated example, but just in case, here’s a few pre-emptive clarifications: 1) Every court-type event must have a button character, even if that character is just your character, so that must always be set up. 2) The group parameter defines which spot in the scene that character stands in. These groups themselves are scriptable (with a bit of work) elsewhere, so you can arrange characters inside the court however you like. The groups shown in the example actually contain multiple different preset positions within the court scene, one of which is selected randomly for each event when it tries to fire. 3) For animations, we can access all the standard ones, plus a slew of new animations created specifically for the court scene. Finally, just for fun, let’s have some more court events: View attachment 760588 View attachment 760589 View attachment 760590 Oh, right, yes, I titled the dev diary “and friend” too, didn’t I? Welp, the new court-type isn’t the only event type we’re adding with this expansion (just the most exciting). We also have the new duel event type! Duels were added as part of our first flavour pack, but I’m sure you’ve all noticed that the space for ‘em is pretty limited, and the animations don’t work so well for this context. Welp, we’ve revamped both of those with this new type, giving duels a face-lift: View attachment 760591 … Naturally, the weapon held by either character does correspond to their signature weapon type, or whatever weapon artefact they have equipped (if they’ve got one). And that’s all from me, folks. As ever, I’ll be around in the comments for an hour or so to answer questions, but otherwise, see y’all next diary! Click to expand...
<!-- artifact:quote:end -->
I wonder,will there be like a mistress systm ? like common ladies with looks traits and stuff that you can do this or that,and the fact that you get adulturer rank or somethinf if you have a lover,which is kinda wrong since kings had sometimes hunderds of lovers,and the fact you get a massive debuff because of it is a but dumb and extremly unhistorical

## Reply 88 — participant_064 · 2021-09-29 · post-27819547

New patch when?

## Reply 89 — participant_065 · 2021-09-29 · post-27819682

<!-- artifact:quote:start -->
> Wokeg said: Welcome comrades! In today’s (not at all late shutup SHUTUP) dev diary, we’ll be going over the new court-type event; many of you will likely have seen them a bit already in a few preceding dev diaries, but for the rest, allow me to formally introduce court-type events: View attachment 760580 This new event type is seen exclusively within the court view, where they replace standard character-type events. We added these because one of the major design limitations with character-type events is that they’re uhh… they’re small. Really, really, really small, and having comparatively little space to work with means they impose a lot of restrictions on their use. Those of you who mod, or have dabbled at modding, will likely know what I’m talking about: generally, a character event can only fit about three paragraphs of copy and 3-4 options before it starts to look a little naff. Less if there are characters or titles involved with very long names, or if you have to do a lot of paragraphing. There are good reasons for them to be this small - they get in the way less when popping up, it encourages concise delivery of information, and it frames the portrait characters in each event nicely. For the court scene, these considerations are (generally) moot, so we wanted to play around with a more liberal event format. We don’t need to worry about framing characters in the traditional sense since we show them in the scene, the player always opts into a court-type event and thus can’t have one pop-up unexpectedly, and though information (and options) still need to be reasonably concise, it’s nice to have a little room to flex the meaning of “concise” somewhat. View attachment 760581 Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Wokeg said: View attachment 760588 View attachment 760589 Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Wokeg said: View attachment 760591 Click to expand...
<!-- artifact:quote:end -->
The new system in events is nice. But this camera angle is not pleasant at all. It's as if the characters appear in 2D from this camera perspective and are glued in there. When you look at some characters, it doesn't look dwarf in terms of posture, but you said dwarf. For example, why is the priest here so short? The perspective needs to be looked at again and adjusted. For example, in these two photos, there is a black bar line right behind the main characters when viewed from the perspective. It does not look like a shade. If there is a shadow, the shadows of the other characters are reflected to the other side. That's why this perspective is so wrong from every angle. Finally, I will talk about the new event style, the duel mode. A good direction has been taken here. But why do duelists look like they just got out of bed? I know they're going to duel by swinging swords? Or pillow fight? Why didn't they wear their armor? These also definitely need to be addressed.

## Reply 90 — participant_021 · 2021-09-29 · post-27819712

<!-- artifact:quote:start -->
> johnnybgood89 said: New patch when? Click to expand...
<!-- artifact:quote:end -->
I've heard a day is added each time someone asks this

## Reply 91 — participant_066 · 2021-09-29 · post-27819857

These are all very well, but when on earth could we get the new dlc?

## Reply 92 — participant_067 · 2021-09-29 · post-27819938

<!-- artifact:quote:start -->
> Wokeg said: View attachment 760585 Click to expand...
<!-- artifact:quote:end -->
Very minor but thought I'd point out: the word for a person who walks by is 'passers-by' not 'by-passers'. I know the verb is 'bypass' and in some instances its also a noun, but English? I guess?

## Reply 93 — participant_068 · 2021-09-30 · post-27820366

It is useless to ask the release date of the patch and dlc. All the same, they do not speak and will not say, I think that no one should consider themselves deceived, otherwise they will promise, they will say in the end they will not have time and the accusations will begin that everyone was deceived and did not live up to expectations. Personally, I have not played since summer because knowing what will be in the update the game will become more interesting and until that moment, there is no point in starting new or continuing old save games. Every week convulsively wait for the diary in the hope of hearing something about the exit, and they tell 3 diaries about the events! We'll see everything when we start playing!

## Reply 94 — participant_069 · 2021-09-30 · post-27820536

Argh, every one of these dev diaries make me want Royal Court to come out sooner!

## Reply 95 — participant_016 · 2021-09-30 · post-27820589

<!-- artifact:quote:start -->
> MrButtermancer said: Taking these SAME character models and dropping them in awkward poses in what's obviously a room inside a video game is three steps backwards and striking your head on a low doorframe. It looks so grossly artificial. What works as a pose in front of a painted scene does NOT look natural from multiple angles in what's supposed to be a believable breathing room. An idle animation which looks fine from the front will look bizarre and alien once dropped into a cube with textures painted on each side. Click to expand...
<!-- artifact:quote:end -->
Strongly agree with this. The "surprised" pose, which already looks a little stilted in the event view, looks ABYSSMAL in the court scenes. Totally unnatural and out of place. The "folded hands" pose, which looks okay in the event window, looks horrifying from the side. I'm sure some of these can be cleaned up a bit...but they need more than a little bit of cleanup. I really think Paradox bit off more than it can chew on this.

## Reply 96 — participant_070 · 2021-09-30 · post-27820800

when? when? when?

## Reply 97 — participant_020 · 2021-09-30 · post-27821004

<!-- artifact:quote:start -->
> Wokeg said: View attachment 760591 … Naturally, the weapon held by either character does correspond to their signature weapon type, or whatever weapon artefact they have equipped (if they’ve got one).[...] Click to expand...
<!-- artifact:quote:end -->
These weapons all look nice but...any chance we are getting shields? Pretty important to duelling I'm sure you agree

## Reply 98 — participant_071 · 2021-09-30 · post-27821052

It has that 2000 era RPG look.Dated and not very natural looking.

## Reply 99 — participant_018 · 2021-09-30 · post-27821226

Thank you Wokeg and Devs for answering questions that were asked.

## Reply 100 — participant_072 · 2021-09-30 · post-27821234

I struggle to see how everyone is so hyped for this? £24 to add some random events that dont even make sense in your play through? Am I missing something?

## Reply 101 — participant_021 · 2021-09-30 · post-27821299

<!-- artifact:quote:start -->
> Staffy50 said: I struggle to see how everyone is so hyped for this? £24 to add some random events that dont even make sense in your play through? Am I missing something? Click to expand...
<!-- artifact:quote:end -->
I'm more hyped for cultural divergence and hybrid cultures that the DLC brings

## Reply 102 — participant_072 · 2021-09-30 · post-27821305

<!-- artifact:quote:start -->
> NimbleShadow said: "play it like The Sims" Click to expand...
<!-- artifact:quote:end -->
Oh god did they actually say that? That explains alot... Next expansion confirmed - Throne variety DLC pack, £7.99.

## Reply 103 — participant_020 · 2021-09-30 · post-27821323

<!-- artifact:quote:start -->
> Staffy50 said: Oh god did they actually say that? That explains alot... Next expansion confirmed - Throne variety DLC pack, £7.99. Click to expand...
<!-- artifact:quote:end -->
You say it as a joke but pretty sure subsequent flavour packs will add new artifacts and other stuff to build upon RC

## Reply 104 — participant_073 · 2021-09-30 · post-27821496

<!-- artifact:quote:start -->
> Wokeg said: Valid; it's on my list of polish things to sort for the duel system (still haven't added cheating!), but not something I've gotten around to yet, I'm afraid. Depends on the event: generally, when writing events, we try to pick appropriate characters through the trigger block but don't set things up to ensure the copy is definitely 100% accurate, only that it seems accurate at a glance/with a bit of casual digging. Sadly, if we were to track such things, it'd likely merc both save game size and a bit of performance. Interesting; we might have defaulted a little bit too much to later medieval Iberian architecture, which (at least, IME) tends to have more of a flourish. I'll raise this internally! Funnily enough, there is a follow-up event to this one if you ignore the problem and get unlucky... Lighting, positioning, et al are all WIP. We'll continue adjusting, tweaking, and improving such as we go, but sadly one of the issues with dev diary screenshots is that they mean we're showing unfinished or unpolished work, so it'll rarely look quite as good as the final thing. I'm afraid that it was insinuated that if I went into details on that, I wouldn't be writing much script any time soon. Rest assured that the parties responsible are have been dealt with. Permanently. That's uhh... a supervisory horse. Doing. Supervising things. Yeah. ^^' Aggh, yeah, we do need to go through and do more updating of older content for this. Certainly some duels we're happy to keep as prowess checks (essentially anything that doesn't need a full fight), but some could really use the new system. A handful of the new court events do, FWIW, and there's a bit of cultural tradition stuff related to duelling. :thinking_face: Not as far as I'm aware. ^^' Not my department, I'm afraid. Not that I know of, though. It's just the UI! The duel system came in with the first flavour pack. The UI is, however, free, as was the system. I've gone into this a little elsewhere, but essentially it's a deliberate design decision not to have overt battlefield events pop up like this, since they get in the way of army movement and, especially in MP, they'd be an active nuisance. Click to expand...
<!-- artifact:quote:end -->
What about SP only battlefield duels? They are pause popups anyhow.

## Reply 105 — participant_069 · 2021-09-30 · post-27822108

<!-- artifact:quote:start -->
> Staffy50 said: Oh god did they actually say that? That explains alot... Next expansion confirmed - Throne variety DLC pack, £7.99. Click to expand...
<!-- artifact:quote:end -->
I'm looking forward to My First Barony Stuff.

## Reply 106 — participant_068 · 2021-09-30 · post-27822481

<!-- artifact:quote:start -->
> MrButtermancer said: I've gotta say, the more I see of it, the more I'm certain I absolutely despise the court view. In the base game events and character screens, the character models look great in front of oil paintings which lend the game a classy reserved aesthetic. There's just enough abstraction I feel like there's a scene behind which I'm filling in mentally, but enough going on that it's quite pleasant to look at. It's delicately artful and genuinely lovely to look at. Taking these SAME character models and dropping them in awkward poses in what's obviously a room inside a video game is three steps backwards and striking your head on a low doorframe. It looks grossly artificial. What works as a pose in front of a painted scene does NOT look natural from multiple angles in what's supposed to be a believable breathing room. An idle animation which looks fine from the front will look bizarre and alien once dropped into a cube with textures painted on each side. You're at the point where you would have to have fully motion-captured people walking around, talking, eating, and using furniture. Furniture covered in uniquely 3D modeled food, silverware, rumpled tablecloths, dribbling candlewax... I don't think that kind of resources will be (or should be) committed to this. And while yes, this is "in development," what I've seen has utterly failed to convince me any of these rooms are going to look even passably organic once they're done. It's been brought out of the abstracted paintings far enough your instinct is to expect more than empty breathing cycle-animating idle statutes of people, and perfectly-spaced cookie-cutter chairs at right angles on clean flat floors -- but not developed far enough to indulge realism. what's here is jarring. There is no signal to my brain this could possibly be anything but a video game -- a completely different feeling than the oil backdrops which are strangely lovely and evocative. It's being steered into uncanny valley territory. What's worse, I'm sure it's eating up a huge amount of development time. This is a significant investment in labor which will ultimately make the game look worse. I can't believe this is a landmine this studio is stepping on, either. Throughout the development diaries, a resounding value of CK3 has seemed to be accomplishing more with less. More efficient code. Less cluttered mechanics and UI. The current system for event graphics is exactly in line with getting a huge amount out of relatively little. I'd have expected a few sets of oil paintings of courtrooms of various cultures from different angles, maybe with assignations to have the character models standing around in them (basically just a scaled up version of the sort of thing we see on the title screen). This could functionally accomplish the exact same role as the full 3D being developed for the courtroom, except you could fill the room with the delightful color and clutter and *character* of the events which has become an essential and defining part of the game's aesthetic. This 3D courtroom view is a travesty. It's off-key. A sour note. A weird chord which is bothersome in an otherwise harmonious progression. It just doesn't fit. And while I'm sure there are going to be people so emotionally invested in CK3 being among their favorite games they'll convince themselves it's alright (or even good depending on their qualifications as emotional acrobats) -- aesthetically, this is wrong. When I look at the title screen, or any event, I get a little dopamine buzz because it's just lovely to look at. These courtroom views have me sucking air through my teeth. The new portrayal in full 3D is more expensive, louder, and weaker by every metric those qualities can be measured. Paintings with superimposed animated character models would do so much more with less. It would require less from a PC's hardware and fit better with the rest of the game's aesthetic. They would look more organic, and be classier. I don't see the current trajectory having a graceful outcome. It's a horrible thing to consider at this stage -- but what's going on here on the graphical side is bad and should be reconsidered. Click to expand...
<!-- artifact:quote:end -->
Personally, I'm afraid that all these transitions to the courtyard window will make the game stupid even more ... Suffice it to cite the example of the crusade, it quite often happens that when all the participants withdraw their armies, the game turns into a slideshow. It only saves when the crusade ends, and there was even such that the preservation broke because of this, since personally I always play only in the iron man!

## Reply 107 — participant_016 · 2021-09-30 · post-27822491

<!-- artifact:quote:start -->
> Ckopcepeo said: Personally, I'm afraid that all these transitions to the courtyard window will make the game stupid even more ... Suffice it to cite the example of the crusade, it quite often happens that when all the participants withdraw their armies, the game turns into a slideshow. It only saves when the crusade ends, and there was even such that the preservation broke because of this, since personally I always play only in the iron man! Click to expand...
<!-- artifact:quote:end -->
I *really* hope the transition to the court scene is smooth and nearly instant, like bringing up an event window. It doesn't take much lag at all to make a UI feel frustrating to interact with. CK3 did a great job making the game start experience feel nearly seamless (at least compared to the eon it took in CK2), so hopefully they're still cognizant of the danger of load times.

## Reply 108 — participant_074 · 2021-09-30 · post-27822507

<!-- artifact:quote:start -->
> MrButtermancer said: What's worse, I'm sure it's eating up a huge amount of development time. Click to expand...
<!-- artifact:quote:end -->
I sure hope I am proved wrong, but I tend to agree with @MrButtermancer on this one, especially with the opportunity cost of developing this over something else. The court view seems like a distraction that doesn’t interest me all that much and that could break the flow / cohesion of the game. Again, I sure hope I am wrong. I just want the best for CK3 (and all of Paradox’s games, for the matter).

## Reply 109 — participant_054 · 2021-10-01 · post-27822593

<!-- artifact:quote:start -->
> Tiax said: Strongly agree with this. The "surprised" pose, which already looks a little stilted in the event view, looks ABYSSMAL in the court scenes. Totally unnatural and out of place. View attachment 761200 The "folded hands" pose, which looks okay in the event window, looks horrifying from the side. View attachment 761204 View attachment 761213 I'm sure some of these can be cleaned up a bit...but they need more than a little bit of cleanup. I really think Paradox bit off more than it can chew on this. Click to expand...
<!-- artifact:quote:end -->
While I agree this is an issue, I hope the Royal Court isn't delayed because of simple clipping errors like this which honestly most modern games have to some extent. Graphics don't affect gameplay, and their focus really should move to the gameplay part of CK3 pronto.

## Reply 110 — participant_075 · 2021-10-01 · post-27823258

<!-- artifact:quote:start -->
> Staffy50 said: Oh god did they actually say that? That explains alot... Next expansion confirmed - Throne variety DLC pack, £7.99. Click to expand...
<!-- artifact:quote:end -->
Surely the company that charged money for a Barber Shop and the ability to rename your kingdom would never do something like that...

## Reply 111 — participant_076 · 2021-10-02 · post-27824538

<!-- artifact:quote:start -->
> MrButtermancer said: I'd have expected a few sets of oil paintings of courtrooms of various cultures from different angles, maybe with assignations to have the character models standing around in them (basically just a scaled up version of the sort of thing we see on the title screen). This could functionally accomplish the exact same role as the full 3D being developed for the courtroom, except you could fill the room with the delightful color and clutter and *character* of the events which has become an essential and defining part of the game's aesthetic. Click to expand...
<!-- artifact:quote:end -->
I agree. CK is never going to be perfectly realistic, but so long as it allows the player to suspend disbelief and rely a little on his or her imagination, that's not so much of an issue. It can even be an asset! Many of CK's best emergent narratives come from a mix of aptly-timed RNG and generous imagination. The more difficult it becomes to suspend disbelief / the less space that's left for our imaginations to fill in the gaps, the more apparent the thinness of the simulation. I honestly don't understand why they've chosen to go down this needlessly difficult route. Maybe they're trying to build 3D experience for further projects? (VtMB2?) But A$42.95 seems pretty steep for a training project. I would much prefer that the work that went into all this careful 3D modelling went instead into writing events, or better differentiating governments / cultures / religions.

## Reply 112 — participant_077 · 2021-10-02 · post-27825284

<!-- artifact:quote:start -->
> Splorghley said: I agree. CK is never going to be perfectly realistic, but so long as it allows the player to suspend disbelief and rely a little on his or her imagination, that's not so much of an issue. It can even be an asset! Many of CK's best emergent narratives come from a mix of aptly-timed RNG and generous imagination. The more difficult it becomes to suspend disbelief / the less space that's left for our imaginations to fill in the gaps, the more apparent the thinness of the simulation. I honestly don't understand why they've chosen to go down this needlessly difficult route. Maybe they're trying to build 3D experience for further projects? (VtMB2?) But A$42.95 seems pretty steep for a training project. I would much prefer that the work that went into all this careful 3D modelling went instead into writing events, or better differentiating governments / cultures / religions. Click to expand...
<!-- artifact:quote:end -->
Good news... Your $42 is going on all of those things.

## Reply 113 — participant_078 · 2021-10-03 · post-27826105

uncanny valley I've been in denial for weeks, but this dev diary + Mr. Buttermancer's post made me accept it. And the rooms too! I was hoping for that haunting grandeur of the intro throne rooms: Instead we get this doll cabinet: I literally refused to buy Civ 6 because it felt too "doll-house-y". I agree with Buttermancer. They can go ALL IN at this point or stick to the oil style. (fwiw i'm a hopeless romantic who votes all-in: textures, clutter, movement and unnecessary palm fanning)

## Reply 114 — participant_072 · 2021-10-03 · post-27826456

<!-- artifact:quote:start -->
> Castle Adrian said: uncanny valley I've been in denial for weeks, but this dev diary + Mr. Buttermancer's post made me accept it. And the rooms too! I was hoping for that haunting grandeur of the intro throne rooms: Instead we get this doll cabinet: I literally refused to buy Civ 6 because it felt too "doll-house-y". I agree with Buttermancer. They can go ALL IN at this point or stick to the oil style. (fwiw i'm a hopeless romantic who votes all-in: textures, clutter, movement and unnecessary palm fanning) Click to expand...
<!-- artifact:quote:end -->
You mean you dont like mobile free to play games graphical style???

## Reply 115 — participant_016 · 2021-10-03 · post-27826907

<!-- artifact:quote:start -->
> Staffy50 said: You mean you dont like mobile free to play games graphical style??? Click to expand...
<!-- artifact:quote:end -->
It also reminds me of the pre-rendered 3D scenes from the intro movies of games in 1998.

## Reply 116 — participant_037 · 2021-10-03 · post-27827089

<!-- artifact:quote:start -->
> Tiax said: It also reminds me of the pre-rendered 3D scenes from the intro movies of games in 1998. Click to expand...
<!-- artifact:quote:end -->
Just missing the T-poses.

## Reply 117 — participant_079 · 2021-10-04 · post-27828606

Wow the difference in enthusiasm and care between EU4 dlc's and CK3 is stunning. Great job

## Reply 118 — participant_080 · 2021-10-04 · post-27828790

The more I see of the 3d court the more I dislike it. The graphics are terrible Im sad to say. For all the time we will spend in the court view I dont think this has been cost effective at all. Im hoping that someone just mods the new events into the event windows we are familiar with to cut out these throne rooms. Or at least make them part of the DLC so I don't have to buy it.

## Reply 119 — participant_078 · 2021-10-06 · post-27830902

<!-- artifact:quote:start -->
> Staffy50 said: I struggle to see how everyone is so hyped for this? £24 to add some random events that dont even make sense in your play through? Am I missing something? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Overhead pull-out third-person (god view) in SIMCITY 3000 Unlimited. Many strategy video games, drawing on earlier ludic strategy models like chess and GO, have the player operate as an all-seeing force on the world; hence the term 'god’s-eye view.' The SIMCITY strategy design illustrates the god’s-eye view by allowing the player to see everything that exists in the game world at any given time. (Image from: Maxis (EA). SIMCITY 3000 Unlimited. Redwood City, CA: Maxis (EA), 2000.) Click to expand...
<!-- artifact:quote:end -->
I don't think Royal Court is gonna perfect (and that's okay!). But I'm very excited because I think it's the start of something. It combines two very different POV's in one game. Most of the games I've played...... city builders, CK3, EU4, Civ5..... are all like this: https://www.researchgate.net/figure/5-Overhead-pull-out-third-person-god-view-in-SIMCITY-3000-Unlimited-Many-strategy_fig5_35486642 I love these games for what they are. Don't get me wrong. But there's always those moments... staring down at my creations.... where I think: if only I could play INSIDE of that... how lucky those pedestrians are! Always the architect; never the resident. What does Royal Court bring? I know I know. At the moment it's like a glorified cosmetic pack. Like, do we really need a 3D room to receive a couple messages? Not necessarily. But down the road? "Interior" perspectives offer possibilities that a God View doesn't. You could explore rooms, search for mysterious objects in libraries/armories (home and abroad), choose who to talk to, arrange dinner guests to honor or humiliate them, set standards of dress and protocol (affecting budgets and cultural opinions), gain access (or lose access) to rooms and spaces where plots and swaying and seduction can occur , and... though it may not be your top priority... DECORATE... in ways that honor certain cultures/values so as to signal your beliefs and stances as a ruler And I'm not the only one thinking this way. Check out this dude's Tavern mods: Steam Community :: Error steamcommunity.com a bit redundant, but here's an older wish-list of mine: https://forum.paradoxplaza.com/foru...-courtly-fashion.1489882/page-4#post-27778390

## Reply 120 — participant_004 · 2021-10-06 · post-27830913

<!-- artifact:quote:start -->
> Castle Adrian said: You could explore rooms, search for mysterious objects in libraries/armories (home and abroad), choose who to talk to, arrange dinner guests to honor or humiliate them, set standards of dress and protocol (affecting budgets and cultural opinions), gain access (or lose access) to rooms and spaces where plots and swaying and seduction can occur , and... though it may not be your top priority... DECORATE... in ways that honor certain cultures/values so as to signal your beliefs and stances as a ruler. Click to expand...
<!-- artifact:quote:end -->
This might be possible in CK4 but the devs have stated that they are trying to make Royal Court playable on the lower end of recommended specs for the game and add more visuals to the game is going to limit who can by the DLC because CK3 isn't a graphics intense game so there are people who can play CK3 fine right now but adding too many graphical elements to the game and they won't be able to play so now you are limiting your potential sales. Also, this is just way too much of a deviation of the standard gameplay that the game has established that I can't see the devs going in this direction.

## Reply 121 — participant_078 · 2021-10-06 · post-27831130

<!-- artifact:quote:start -->
> InsidiousMage said: This might be possible in CK4 but the devs have stated that they are trying to make Royal Court playable on the lower end of recommended specs for the game and add more visuals to the game is going to limit who can by the DLC because CK3 isn't a graphics intense game so there are people who can play CK3 fine right now but adding too many graphical elements to the game and they won't be able to play so now you are limiting your potential sales. Click to expand...
<!-- artifact:quote:end -->
explore rooms: The graphics limits are understandable. But I don't mean walking around and zooming in and picking things up (maybe CK4, lol). I mean simply looking at a room from multiple camera angles. And the dev's are already providing this, just for one room (for now). Adding a few more rooms shouldn't kill the graphics... you leave one room and then the game loads the next. search for mysterious objects in libraries/armories (home and abroad): My description's kinda misleading. You won't be examining nooks and crannies like Luigi's Mansion. I mean your character could request access to a library/study of a foreign ruler. They could "Take out books" or possibly "Search for documents". Such items could help them with lifestyle experience, discovering secrets, uncovering secret societies, or even fabricating claims. The longer you search, the more likely you are to be discovered. Again, the graphics don't have to be complicated. One could "Open Books". By the way... if you think I'm crazy, look what this modder has already done: Steam Workshop::The King's Bork (Discontinued) steamcommunity.com With books and libraries and KEYS to SHELVES and DRAWERS, one could make something quite elaborate. Have you ever read The Name of the Rose? Me neither. But there was an entire course on it at my college (which I conveniently skipped). Murder mystery. Medieval. LIBRARY! choose who to talk to: What's wrong with this? The game's AWFULLY control-ly about who we talk to, and when ......doesn't sound healthy arrange dinner guests to honor or humiliate them new way to juggle the feelings of your petty, mean-girl dukes and duchesses. simple. visual. fun! set standards of dress and protocol (affecting budgets and cultural opinions) Come on! This is so simple and so fun who wouldn't want it? Based on what styles/dress/decorations you allow... you can choose which cultures to promote/tolerate/persecute in court. With the cultural changes coming up, this would give depth and integrate seamlessly. gain access (or lose access) to rooms and spaces where plots and swaying and seduction can occur As I said about libraries, there's lots of possibilities when ACCESS vs NO ENTRY come into play. It could add depth to schemes and seduction. Instead of just working your way into someone's percentage-heart-circle....... you could work your way into various rooms and alone times. As in life, going deeper into a person's home is metaphorically going deeper into a person's heart. And in each room, the conversations, events and options increase. Meanwhile, the more time you spend in the wrong chambers or with the wrong people, the more suspicious others will become. Beware the gossip! ---------------------------------------------- I'm not saying the devs need to do these things NOW. I'm just saying: a) theoretically possible b) not graphics-intensive c) can be worked into the flow of the game

## Reply 122 — participant_081 · 2021-10-06 · post-27831317

This looks like ugly Sim game... Ck2 is still superior.

## Reply 123 — participant_082 · 2021-10-06 · post-27831656

I'm very exited for this feature! But I feel like it's very sad that you won't have these small-scale personal events as a count/duke or as a tribal leader. These feel like they would fit pretty neatly in a lowly and small court with a more personal feel. I really think it should be reconsidered wether or not you want to keep players in the early game from having these events. Maybe these could be disabled for AI but enabled for players of all ranks and gouvernment types...

