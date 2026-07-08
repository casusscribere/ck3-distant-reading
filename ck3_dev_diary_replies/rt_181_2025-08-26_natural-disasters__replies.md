---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1856829/"
forum_thread_id: 1856829
content_type: reply_thread
parent_dd_file: dd_181_2025-08-25_natural-disasters.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 181
title: "Dev Diary #181 - Natural Disasters"
dd_date: 2025-08-26
expansion: All Under Heaven
patch: null
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 7
reply_count: 137
participant_count: 93
reply_date_first: 2025-08-26
reply_date_last: 2025-09-03
body_word_count: 7380
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

# Reply thread — Dev Diary #181 - Natural Disasters

*137 replies from 93 participants across 7 pages*

## Reply 1 — participant_001 · 2025-08-26 · post-30702058

Can disasters be visually visible on the map like "devastation" in Victoria 3? or at least like plagues?

## Reply 2 — participant_002 · 2025-08-26 · post-30702060

New clan coat of arms shape? I wonder why.

## Reply 3 — participant_003 · 2025-08-26 · post-30702062

These events read like an action trilogy - they have no right to go this crazy hard!

## Reply 4 — participant_004 · 2025-08-26 · post-30702064

<!-- artifact:quote:start -->
> X_FloW said: Can disasters be visually visible on the map like "devastation" in Victoria 3? or at least like plagues? Click to expand...
<!-- artifact:quote:end -->
They're visible on the map via both UI elements - map pins, borders - and terrain shaders if you zoom in close enough. The shaders are currently WIP so I can't show you screenshots yet, but you'll be able to see them, yes!

## Reply 5 — participant_005 · 2025-08-26 · post-30702068

Will famines be natural disasters?

## Reply 6 — participant_006 · 2025-08-26 · post-30702069

Neat. Natural Disasters remind me of plagues, down to the warning events and the option to pay for a better recovery. If you never do the recovery project, does the situation stay there forever? Can Natural Disasters appear in every region?

## Reply 7 — participant_007 · 2025-08-26 · post-30702072

<!-- artifact:quote:start -->
> lachek said: They're visible on the map via both UI elements - map pins, borders - and terrain shaders if you zoom in close enough. The shaders are currently WIP so I can't show you screenshots yet, but you'll be able to see them, yes! Click to expand...
<!-- artifact:quote:end -->
How many different kinds of disasters are there? Such are their forest fires?

## Reply 8 — participant_008 · 2025-08-26 · post-30702073

Looks really interesting! Are there types of natural disasters other than floods and earthquakes, such as typhoons? Also, do events such as outbreaks of disease occur directly in provinces that have been affected by natural disasters?

## Reply 9 — participant_009 · 2025-08-26 · post-30702079

Can we see full list of disasters?

## Reply 10 — participant_010 · 2025-08-26 · post-30702082

The image of a pagoda and other buildings in that architectural style seems immersion breaking for natural disasters outside of China, Korea or Japan.

## Reply 11 — participant_011 · 2025-08-26 · post-30702091

<!-- artifact:quote:start -->
> lachek said: Click to expand...
<!-- artifact:quote:end -->
>the modifier is called "Flood Fertility" >doesn't affect Fertility

## Reply 12 — participant_009 · 2025-08-26 · post-30702092

Will the disasters have "magnitude" parameter?

## Reply 13 — participant_012 · 2025-08-26 · post-30702097

Great illustration, and I'm particularly happy that you even mentioned the lesser known Rhine flood(s). One time, when it was really bad, people reported that you could take a boat over the city wall, a picture before my inner eye that stuck with me for all the years since I read about it. It really seems you guys are doing your homework very thoroughly! Really looking forward to this feature here, great read.

## Reply 14 — participant_004 · 2025-08-26 · post-30702101

<!-- artifact:quote:start -->
> apollo1989vieten said: Will famines be natural disasters? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> sandwich8 said: Neat. Natural Disasters remind me of plagues, down to the warning events and the option to pay for a better recovery. If you never do the recovery project, does the situation stay there forever? Can Natural Disasters appear in every region? Click to expand...
<!-- artifact:quote:end -->
Two natural disasters will be represented with the release of All Under Heaven, earthquakes and floods. The system is obviously extensible / moddable, but each disaster type require a fair bit of work to implement and balance, so we've focused on the primary ones that changed the course of history in our era (volcanic eruptions excluded; these were very rare but extremely impactful, and as such are very hard to balance for fun gameplay). Famines obviously did have a considerable effect on medieval balance of power, but if I'm going to allow myself to be nit-picky for a moment, famines are more of a side effect of natural disasters than a natural disaster in its own right. We're not getting quite as granular as Victoria 3's harvest conditions with this feature. The situation will remain until the Great Project is completed, but the negative modifiers will eventually time out unless removed by the Great Project. As the owner of the Great Project only you can elect to start it, but any vassal of your realm can contribute to it, so it's unlikely to stick around forever (unless you explicitly choose to never complete it).

## Reply 15 — participant_004 · 2025-08-26 · post-30702105

<!-- artifact:quote:start -->
> rasuuru said: Will the disasters have "magnitude" parameter? Click to expand...
<!-- artifact:quote:end -->
Yes, there is a severity value for every disaster which will affect how badly it affects the counties in its region and influence the cost of certain contributions.

## Reply 16 — participant_013 · 2025-08-26 · post-30702107

I've been looking forwards to natural disasters in CK3 for literal YEARS, as evidenced by this nearly 4000-words-long essay I wrote in 2023. I truly can't wait for this.

## Reply 17 — participant_014 · 2025-08-26 · post-30702108

So only flood and eathquake ? No typhoon/cyclone, tsunami, volcanic eruption, drought , etc.... ?

## Reply 18 — participant_015 · 2025-08-26 · post-30702114

<!-- artifact:quote:start -->
> lachek said: However - quite naturally - the larger the realm, the larger the risk one part of it will be struck by disaster at any given time. Click to expand...
<!-- artifact:quote:end -->
More challenges to larger realms are always welcome! One point I would make though - rulers should be able to use more than just hooks to mobilise the realm behind the recovery efforts, and should instead have something more like the range of options available to get people to join schemes. E.g. it would make sense that a very prestigious or influential ruler would be able to use their accumulated political capital - represented by prestige and influence - to coordinate the response. (I would also suggest things like friendship and dread would be relevant here too - if Vlad the Impaler shows up asking for me to contribute to the earthquake recovery, I think I am going to contribute to the earthquake recovery). EDIT: Also, do vassals gain prestige/legitimacy/piety bonuses for their contributions to the recovery fund? It seems like a good opportunity for ambitious vassals with money to spare to enhance their status within the realm - or indeed generous and charitable vassals to enhance the welfare of their fellow men.

## Reply 19 — participant_016 · 2025-08-26 · post-30702115

Allo allo allo what's all this then:

## Reply 20 — participant_017 · 2025-08-26 · post-30702120

Oooh, do I notice new flag shapes and dynasty coa frames?

## Reply 21 — participant_018 · 2025-08-26 · post-30702123

Im really hyped for natural disasters. But i would appreciate some game rules : • Harsher modifiers and effects. • Increased frequency of natural disasters (Rare, common, frequent and apocalyptic). • No warning phase. Also could you give us a list of what kinds of disasters the game will have for AUH, and if others are considered? Thank you and good work.

## Reply 22 — participant_004 · 2025-08-26 · post-30702129

<!-- artifact:quote:start -->
> SMiki Lorebringer said: >the modifier is called "Flood Fertility" >doesn't affect Fertility Click to expand...
<!-- artifact:quote:end -->
Fixed! Thank you!

## Reply 23 — participant_019 · 2025-08-26 · post-30702131

So can the yellow river alter its course (as happened several times historically) or will it have a fixed course? I know it's a demanding mechanics but I feel like the yellow river ought to be an exception considering the magnitude and uniqueness of its floods

## Reply 24 — participant_004 · 2025-08-26 · post-30702134

<!-- artifact:quote:start -->
> pbw-410 said: More challenges to larger realms are always welcome! One point I would make though - rulers should be able to use more than just hooks to mobilise the realm behind the recovery efforts, and should instead have something more like the range of options available to get people to join schemes. E.g. it would make sense that a very prestigious or influential ruler would be able to use their accumulated political capital - represented by prestige and influence - to coordinate the response. (I would also suggest things like friendship and dread would be relevant here too - if Vlad the Impaler shows up asking for me to contribute to the earthquake recovery, I think I am going to contribute to the earthquake recovery). Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pbw-410 said: EDIT: Also, do vassals gain prestige/legitimacy/piety bonuses for their contributions to the recovery fund? It seems like a good opportunity for ambitious vassals with money to spare to enhance their status within the realm - or indeed generous and charitable vassals to enhance the welfare of their fellow men. Click to expand...
<!-- artifact:quote:end -->
More options for how to pressure your vassals are certainly plausible! I'll see what we can do here. Yes! Anyone contributing gets the reward for that contributions, including modifiers, Merit, prestige, etc depending on who they are and what currencies they use.

## Reply 25 — participant_004 · 2025-08-26 · post-30702140

<!-- artifact:quote:start -->
> Illicitline45 said: So can the yellow river alter its course (as happened several times historically) or will it have a fixed course? I know it's a demanding mechanics but I feel like the yellow river ought to be an exception considering the magnitude and uniqueness of its floods Click to expand...
<!-- artifact:quote:end -->
Sadly, our current map tech doesn't permit for runtime alterations of the map, it's all static data initialized when the game loads. So redirecting rivers will unfortunately not be possible until the next generation of Paradox GSGs (maybe).

## Reply 26 — participant_020 · 2025-08-26 · post-30702153

With how extensive this disaster system is, would it also have stuff that can also be implemented to plagues such as relief projects for plagues?

## Reply 27 — participant_021 · 2025-08-26 · post-30702164

<!-- artifact:quote:start -->
> JonZone said: View attachment 1354328View attachment 1354329View attachment 1354330 These events read like an action trilogy - they have no right to go this crazy hard! Click to expand...
<!-- artifact:quote:end -->
"Photos of Caliph al Majid after the great disasters of 1087 (Colorized)"

## Reply 28 — participant_011 · 2025-08-26 · post-30702165

<!-- artifact:quote:start -->
> lachek said: View attachment 1354337 Fixed! Thank you! Click to expand...
<!-- artifact:quote:end -->
THE GAME IS SAVED. Mandate of Paradox swings towards the Stable era.

## Reply 29 — participant_022 · 2025-08-26 · post-30702169

<!-- artifact:quote:start -->
> lachek said: Two natural disasters will be represented with the release of All Under Heaven, earthquakes and floods. The system is obviously extensible / moddable, but each disaster type require a fair bit of work to implement and balance, so we've focused on the primary ones that changed the course of history in our era (volcanic eruptions excluded; these were very rare but extremely impactful, and as such are very hard to balance for fun gameplay). Famines obviously did have a considerable effect on medieval balance of power, but if I'm going to allow myself to be nit-picky for a moment, famines are more of a side effect of natural disasters than a natural disaster in its own right. We're not getting quite as granular as Victoria 3's harvest conditions with this feature. The situation will remain until the Great Project is completed, but the negative modifiers will eventually time out unless removed by the Great Project. As the owner of the Great Project only you can elect to start it, but any vassal of your realm can contribute to it, so it's unlikely to stick around forever (unless you explicitly choose to never complete it). Click to expand...
<!-- artifact:quote:end -->
What happens if the ‘owner’ of a great project dies? Does the heir inherit the great project? What happens if the land in progress for a great project is lost/gained in a war? Is it partially completed?

## Reply 30 — participant_023 · 2025-08-26 · post-30702175

I think that other countries in the region, namely Korea and Japan (...and maybe Vietnam, but I'm not too sure), should also get the extra Legitimacy loss treatment since they also believed in the concept of the mandate of heaven

## Reply 31 — participant_024 · 2025-08-26 · post-30702176

What's the synergy with plagues? Surely the black death is considered a natural disaster, it is both natural and a disaster? The current experience of plagues is less than it should be, whereas the disaster system would lead to a much better experience other than simply agreeing to a soft/desperate approach or witchcraft.

## Reply 32 — participant_021 · 2025-08-26 · post-30702177

Also, I really like how flooding is not just a negative thing, and that it boosts land fertility and such, that's a nice touch! I have just one question, in the same regard that your forts can be impacted can anything else be impacted? Such as ports? or anything else? Such an overall cool addition to the game! Can't wait to try it out

## Reply 33 — participant_025 · 2025-08-26 · post-30702179

I'm not a fan of how Disasters end up giving the player permanent positive modifiers in exchange for some temporary negative ones. Can't help but see that players will be eagerly awaiting natural disasters to strike their realms since its long term benefits far more outweighs its negative short term debuffs.

## Reply 34 — participant_026 · 2025-08-26 · post-30702181

Suggestion: Major fires are another natural disaster that occurs relatively frequently during these times. They continue to occur even today.

## Reply 35 — participant_027 · 2025-08-26 · post-30702185

Ok, ok. I dig. I hope we'll see some variety in disasters. And that little camel/caravan icon is interesting! Are we seeing the beginnings of the Silk Road, which will hopefully be expanded in the next Chapter? But what happens if I am just a small, independent ruler (a count or duke) and get hit by a flood or earthquake? I might not have rich vassals and a high income - would that basically mean the end of my rule? Or can the little guys still recover? Or can perhaps some temporary option for raiding be given in compensation? (I don't have the money but someone else has...) And what if my camp of landless vagrants is in the area as it is being hit, will I be involved in the disaster?

## Reply 36 — participant_028 · 2025-08-26 · post-30702194

<!-- artifact:quote:start -->
> lachek said: The situation will remain until the Great Project is completed, but the negative modifiers will eventually time out unless removed by the Great Project. As the owner of the Great Project only you can elect to start it, but any vassal of your realm can contribute to it, so it's unlikely to stick around forever (unless you explicitly choose to never complete it). Click to expand...
<!-- artifact:quote:end -->
I'm a little worried - won't this create orphan situations for recovery from a decades-old disasters that are no longer causing negative effects? I imagine poorer corners of the map sitting around with situations for great projects that no one would fund.

## Reply 37 — participant_004 · 2025-08-26 · post-30702201

<!-- artifact:quote:start -->
> Stardance said: What happens if the ‘owner’ of a great project dies? Does the heir inherit the great project? What happens if the land in progress for a great project is lost/gained in a war? Is it partially completed? Click to expand...
<!-- artifact:quote:end -->
Ownership of a project is delegated via the Situation's participant groups, which is based on the counties associated with the situation in a given realm. So if you lose all affected counties to another ruler, you will lose the Great Project while they will gain one. If they only take over one county, they will gain one of the counties (and your project will have a lower cost to the remaining contributions since there's now less land to restore). Etc. It's all contingent on whoever controls the affected counties.

## Reply 38 — participant_004 · 2025-08-26 · post-30702204

<!-- artifact:quote:start -->
> Videogames said: I'm a little worried - won't this create orphan situations for recovery from a decades-old disasters that are no longer causing negative effects? I imagine poorer corners of the map sitting around with situations for great projects that no one would fund. Click to expand...
<!-- artifact:quote:end -->
This hasn't played out in testing yet, but if we find this to be an issue we can run something that'd clean now-irrelevant situations up.

## Reply 39 — participant_029 · 2025-08-26 · post-30702207

Okay. I really have to see how it turns out gameplay-wise. There should be a high chance of plagues if a disaster relief is botched or not handled well as it was offen a thing that went hand in hand. It is a pity that volcanic eruptions are not available, even if there were only a few well recorded ones in medieval times. If warfare or naval mechanics get overhauled droughts, typhoons, storms and wet spells/ harsh monsoons should also be some kind of disaster.

## Reply 40 — participant_030 · 2025-08-26 · post-30702213

Are there cultural linked ui's pictures to be made ? The chinese one looks very good but it is a little out of place for ,let's say Egypt

## Reply 41 — participant_004 · 2025-08-26 · post-30702221

<!-- artifact:quote:start -->
> SmallieM said: But what happens if I am just a small, independent ruler (a count or duke) and get hit by a flood or earthquake? I might not have rich vassals and a high income - would that basically mean the end of my rule? Or can the little guys still recover? Or can perhaps some temporary option for raiding be given in compensation? (I don't have the money but someone else has...) Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SmallieM said: And what if my camp of landless vagrants is in the area as it is being hit, will I be involved in the disaster? Click to expand...
<!-- artifact:quote:end -->
Smaller rulers will have less capital but also less land to restore, so costs will naturally be lower. But yes, it'll be more challenging for counts whose entire realm is affected by an earthquake than for the Huangdi who can draw on taxes from 90% of their realm to restore the 10% affected, of course. We are still playtesting and balancing here, and we have a few possible solutions in our back pocket if this turns out to be an issue. Not directly "involved in the disaster" as such - only ruler characters are considered "involved" in the situation. But landless characters traveling through the region will face greater dangers and could possibly die if they're in the wrong place at the wrong time.

## Reply 42 — participant_031 · 2025-08-26 · post-30702227

<!-- artifact:quote:start -->
> lachek said: Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> lachek said: Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> lachek said: Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> lachek said: Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> lachek said: Land Drainage, for example, will tie up much of your army for 10 years but give you a permanent +10 Direct Vassal Opinion boost as soon as you fund it. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> lachek said: esettling refugees requires you to give up some land until the project is complete - resulting in a reduced domain limit for characters of most cultures - but yields twice the Legitimacy and a Levy Reinforcement boost. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> lachek said: …only in exchange for a Strong Hook, but that will do. At least he will suffer a -75% Levy Reinforcement rate for a while, so in the event he rises up against me… Click to expand...
<!-- artifact:quote:end -->
Regency? I sure hope paradox will add at least one more interaction to it and it wont be the same as it currently is - the ruler (obv stronger side) and the regent pressing the same button on CD and ruler "asking" regent to leave. -50 legitimacy is rather low. -50% Garrison size sounds scary, but garrison size really doesnt do anything, armies are usually large enough to clear the minimum and as of now having more than that might as well not do anything (0.01 siege progress per day per 200 soldiers above garrison) -0.25 is half a senechal. That's low. How permanent are we speaking? Permanent-permanent? If so - that's insane, no. There's no way this is worth it, im sorry. 1. levies are not important at all unless you made some major, MAJOR balance changes, this does nothing 2. There're only those 3 options? That's... very limiting.

## Reply 43 — participant_018 · 2025-08-26 · post-30702232

<!-- artifact:quote:start -->
> lachek said: Smaller rulers will have less capital but also less land to restore, so costs will naturally be lower. But yes, it'll be more challenging for counts whose entire realm is affected by an earthquake than for the Huangdi who can draw on taxes from 90% of their realm to restore the 10% affected, of course. We are still playtesting and balancing here, and we have a few possible solutions in our back pocket if this turns out to be an issue. Not directly "involved in the disaster" as such - only ruler characters are considered "involved" in the situation. But landless characters traveling through the region will face greater dangers and could possibly die if they're in the wrong place at the wrong time. Click to expand...
<!-- artifact:quote:end -->
Will the landless characters companions also be in danger of dying? I saw a comment talking about disasters causing plagues, will that happen?

## Reply 44 — participant_032 · 2025-08-26 · post-30702246

<!-- artifact:quote:start -->
> lachek said: (volcanic eruptions excluded; these were very rare but extremely impactful, and as such are very hard to balance for fun gameplay). Click to expand...
<!-- artifact:quote:end -->
Perfectly sound reasoning, but I can't wait until modders add them, especially now that Krakatoa is on the map

## Reply 45 — participant_033 · 2025-08-26 · post-30702251

<!-- artifact:quote:start -->
> lachek said: Two natural disasters will be represented with the release of All Under Heaven, earthquakes and floods. The system is obviously extensible / moddable, but each disaster type require a fair bit of work to implement and balance, so we've focused on the primary ones that changed the course of history in our era (volcanic eruptions excluded; these were very rare but extremely impactful, and as such are very hard to balance for fun gameplay). Click to expand...
<!-- artifact:quote:end -->
Will there be drought and locusts in the future? Though not always killing people, it would lead to severe famine.

## Reply 46 — participant_034 · 2025-08-26 · post-30702256

<!-- artifact:quote:start -->
> To some degree this also depends on the terrain in your realm and what part of the world you're playing in. Regions that historically suffered earthquakes or floods during this era have a higher probability of being afflicted by one. When a region is afflicted, it is more likely to be centered in terrain suitable for that disaster. Mountainous regions will be more prone to suffer earthquakes, and provinces far from major rivers won't get flooded. Click to expand...
<!-- artifact:quote:end -->
Will there be an option to join a neighboring Disaster Situation if it hasn't affected you? For roleplay purposes, I think it could be neat to offer assistance to a neighboring lord, bridging the Rhine, so to speak, for opinion/piety/cultural acceptance bonuses, depending on how much you offer. Meanwhile, the Papacy/Head of Faith sending some of that charity money towards actual acts of charity could be a good way to add to its efforts as a historical institution Secondly, with only Floods and Earthquakes in the scope, will there be a kind of map mode to show the risks of Disasters, ala Danger in EU5, or will they generally mostly just depend on terrain types with odds of occurrence?

## Reply 47 — participant_033 · 2025-08-26 · post-30702266

<!-- artifact:quote:start -->
> biny496 said: I think that other countries in the region, namely Korea and Japan (...and maybe Vietnam, but I'm not too sure), should also get the extra Legitimacy loss treatment since they also believed in the concept of the mandate of heaven Click to expand...
<!-- artifact:quote:end -->
I doubt if the concept worked in Japan, as a country located on seismic belt, their legitimacy would drop pretty quickly.

## Reply 48 — participant_035 · 2025-08-26 · post-30702282

Is it possible to call on neighbouring/friendly countries, which are not necessarily involved in the situation, to contribute to the effort out of friendship, kindness or prestige?

## Reply 49 — participant_036 · 2025-08-26 · post-30702288

As if the endless diarrhea epidemic wasn't enough...

## Reply 50 — participant_033 · 2025-08-26 · post-30702289

Will the natural disaster cause disease? There's a old Chinese saying said, "After a major disaster comes a epidemic". After a disaster the infrasture is destroyed, and harder to get prepared for plague.

## Reply 51 — participant_004 · 2025-08-26 · post-30702291

<!-- artifact:quote:start -->
> Benismann said: How permanent are we speaking? Permanent-permanent? If so - that's insane, no. Click to expand...
<!-- artifact:quote:end -->
Any permanent modifiers are applied to the character, such as this one. So in this case you do get a Direct Vassal +10 opinion for the lifetime of your character for resolving this disaster, yes. Disasters are very rare and can be very difficult to resolve, so you're not going to be stacking this. As for the rest of your balance concerns, I will bring it back to the team and we'll consider it during the final balancing pass! Thank you!

## Reply 52 — participant_037 · 2025-08-26 · post-30702297

WIll you add an option that makes natural disasters extremely common (apocalypse)? Also will there be forest fires for countries like Sweden?

## Reply 53 — participant_038 · 2025-08-26 · post-30702300

Will plagues and disease be updated to use the Situation system and Great Projects as part of the recovery effort? This looks like a fun way to interact with unforseen events and giving the players short term goals. Plagues can be a bit boring since the recovery effort depends on wether you have the money at the time of the event whereas this can lead you to change your current strategy/focus.

## Reply 54 — participant_012 · 2025-08-26 · post-30702317

One question popped right up for me: what's up next week? Will we talk about Great Projects, which will use the same system we have seen today?

## Reply 55 — participant_039 · 2025-08-26 · post-30702335

Will there be game rules for disaster frequency and severity? Something similar to plagues? I'd love to see some apocalyptic scenarios here.

## Reply 56 — participant_040 · 2025-08-26 · post-30702342

<!-- artifact:quote:start -->
> lachek said: Resettling refugees requires you to give up some land until the project is complete - resulting in a reduced domain limit for characters of most cultures - but yields twice the Legitimacy and a Levy Reinforcement boost. Click to expand...
<!-- artifact:quote:end -->
Any chance of options to use them for construction time or tax benefits instead? Because you could amputate all my limbs and I'd still have enough appendages to count all the situations in which I'd give up a holding of domain limit for levy reinforcement

## Reply 57 — participant_041 · 2025-08-26 · post-30702351

Now that you are speaking about Egypt and the Nile. Please, please tell me u will finally add Coptic/Native Egyptian culture (and language ofc). Please. Specially as the first start date is just a few decades after the Bashmuriam Revolts

## Reply 58 — participant_042 · 2025-08-26 · post-30702353

2 questions: If a disaster happens and affects counties in both your realm and a neighboring realm, what happens if you conquer a devastated county from that neighboring realm? Will recovery costs automatically change to account for the new county? Will that county automatically gain any recovery modifiers that were already given to your own counties? One of my concerns might be what "rewards" you get while/after doing the recovery efforts. You can see screenshots here, on Reddit, etc., about people getting loads of piety/prestige/gold maybe one or two characters in, or 100 dev counties not even 100 years in, and I curious how this will play into that. Obviously the effects of the disasters shown in the DD show that they can be devastating. But if the rewards you get from recovery efforts makeup for, or even overpower, those penalties, I feel it might just lead to players getting even stronger than before. Generally from testing, do characters, especially players, end up in a better/stronger position than they were before the disaster, or will these disasters truly actually devastate realms?

## Reply 59 — participant_011 · 2025-08-26 · post-30702355

<!-- artifact:quote:start -->
> lachek said: Not directly "involved in the disaster" as such - only ruler characters are considered "involved" in the situation. But landless characters traveling through the region will face greater dangers and could possibly die if they're in the wrong place at the wrong time. Click to expand...
<!-- artifact:quote:end -->
IMHO if their Camp is located in the disaster area, the Adventurers should be incentivized to move it during the Warning phase. If they don't move their Camp out of danger, the disaster should end up killing a random number of their Followers and potentially downgrading some buildings in the Camp.

## Reply 60 — participant_043 · 2025-08-26 · post-30702356

I must say I am a bit worried about these positive modifiers being permanent. I would much prefer if they were just slowly ticking down for like a long period of like 20 years or something. Otherwise there will become disater optimization plays that pepole hunt for things like this.

## Reply 61 — participant_027 · 2025-08-26 · post-30702371

<!-- artifact:quote:start -->
> lachek said: Smaller rulers will have less capital but also less land to restore, so costs will naturally be lower. But yes, it'll be more challenging for counts whose entire realm is affected by an earthquake than for the Huangdi who can draw on taxes from 90% of their realm to restore the 10% affected, of course. We are still playtesting and balancing here, and we have a few possible solutions in our back pocket if this turns out to be an issue. Click to expand...
<!-- artifact:quote:end -->
Might make sense that for smaller lords, who simply don't have the capacity to act, the malus would be lower. Can't blame someone if there is nothing they can do about it... The opposite making sense as well: ''who can draw on taxes'' as you said, would be expected to do so. But I imagine an independent duke with his territories ravaged by disaster won't be independent very long. Might confederations or alliances play a role here? I imagine such collaboration extends beyond the strictly military.

## Reply 62 — participant_044 · 2025-08-26 · post-30702373

Between this and border wars I'm noticing a common theme: make large realms less stable and OP.

## Reply 63 — participant_011 · 2025-08-26 · post-30702375

<!-- artifact:quote:start -->
> lachek said: Click to expand...
<!-- artifact:quote:end -->
Could this modifier allow faster cultural&religious conversion, to reflect that it's easier to convert a depopulated area than a densely inhabited one?

## Reply 64 — participant_045 · 2025-08-26 · post-30702382

<!-- artifact:quote:start -->
> lachek said: Any permanent modifiers are applied to the character, such as this one. So in this case you do get a Direct Vassal +10 opinion for the lifetime of your character for resolving this disaster, yes. Disasters are very rare and can be very difficult to resolve, so you're not going to be stacking this. Click to expand...
<!-- artifact:quote:end -->
Will there be a game rule for a frequency and location of disasters, so even locations that weren't flooded but are on the river can still flood? Can I make it truly apocalyptic? If I can suggest - I'd rather the modifier "permanent" for the duration of the situation and then timed for the next 10/20 years once the situation completes. This will still result in a very long time of reward, while not being lifetime long. *** Also one final question - are the disasters part of a DLC or the patch accompanying the DLC? As in do I need to buy it to be able to be hit by an earthquake or is it free for everyone to enjoy?

## Reply 65 — participant_035 · 2025-08-26 · post-30702383

Do you plan to rework the Black Death to integrate it into this system of “natural” disaster Situations? Because the Black Death seems to have been a significant event since the release of Legend of the Dead. With a system like this to recover from the Black Death, the event could become interesting.

## Reply 66 — participant_046 · 2025-08-26 · post-30702386

Wonder how the chinese fanbase will react to natural disasters given how little they liked them in eu4. Will egypt start with anything to counter nile flooding? Will your steward be the regent when you deal with a disaster?

## Reply 67 — participant_047 · 2025-08-26 · post-30702390

How unexpected and pleasant! However, I am worried about one thing - will the frequency of events be revised? Since the release of the game, many wonderful additions have been released, each of which has contributed to the gameplay in one way or another. And to be honest, lately I have begun to notice that the flow of events has become too large. This became especially noticeable after the release of the Legend of Death and Wandering Nobles DLC. I am afraid that the new disaster system will only make this worse.

## Reply 68 — participant_004 · 2025-08-26 · post-30702398

<!-- artifact:quote:start -->
> tanner918 said: If a disaster happens and affects counties in both your realm and a neighboring realm, what happens if you conquer a devastated county from that neighboring realm? Will recovery costs automatically change to account for the new county? Will that county automatically gain any recovery modifiers that were already given to your own counties? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> tanner918 said: One of my concerns might be what "rewards" you get while/after doing the recovery efforts. You can see screenshots here, on Reddit, etc., about people getting loads of piety/prestige/gold maybe one or two characters in, or 100 dev counties not even 100 years in, and I curious how this will play into that. Obviously the effects of the disasters shown in the DD show that they can be devastating. But if the rewards you get from recovery efforts makeup for, or even overpower, those penalties, I feel it might just lead to players getting even stronger than before. Generally from testing, do characters, especially players, end up in a better/stronger position than they were before the disaster, or will these disasters truly actually devastate realms? Click to expand...
<!-- artifact:quote:end -->
I covered this a bit here already; the short answer is yes, recovery costs will update and modifiers already gained will be retained. It's highly contingent. If the severity is high, impacts a large part of your realm, and the ruler is unprepared and with little ability to influence their vassals, it can be devastating. If the severity is low, you still have plenty of resources to draw upon, and you have the tools available to make for a quick recovery, it can be a net positive for your rule.

## Reply 69 — participant_048 · 2025-08-26 · post-30702415

Say the Rhine floods impacting my realm on the east bank, but Im also in a war for the west bank. If I win the war, will the recovery project grow in conjunction with the increased amount of affected counties? Similarly, if I had no counties in an affected area during the disaster but conquer it during the recovery phase, will I inherit the recovery project (and the investments of the previous ruler)?

## Reply 70 — participant_049 · 2025-08-26 · post-30702421

Have you considered something like a "historic" game rule, that ensures certain disasters (like the Aleppo earthquake you mentioned) will happen in the right area at roughly the right time? Might be nice to have some more predictable calamities to prepare for, similar to the Black Death or Mongol invasion. Maybe even some unique flavour text when those historic events do happen.

## Reply 71 — participant_050 · 2025-08-26 · post-30702447

So we will get the 2nd Marcellusflood now? Personally I prefer the low german name. Grote Mandrenke, great drowning of men. Very cool

## Reply 72 — participant_051 · 2025-08-26 · post-30702459

Hopefully some culture and faith stuff could provide other opportunities in the recovery and handling of the floods for example: Ritual hospitality: makes providing aid for the victims cheaper Communal Lands and Communal possessions: perhaps allows you to levy aid from the communities Monasticism: Monasteries were well organized and sometimes decently wealthy areas. It could be cool to reach out to the monasteries for aid. Finally some terrain traditions like Polders or Agrarian could lead to the counties of the culture being able to snap back quicker?

## Reply 73 — participant_052 · 2025-08-26 · post-30702496

Would heavy rains and blizzards count as a disaster? Or just drought?

## Reply 74 — participant_053 · 2025-08-26 · post-30702498

To me this feature bears resemblance to plagues. Not that this is a negative thing, but these two mechanics do seem quite similar. Perhaps with the difference that the follow-up phase of a disaster is much more essential than the actual event what is the case for plagues. On another note, are there any other disasters apart from flooding and earthquakes that we'll see in the game? Things like drought or blizzards would be quite appropriate too for southern and northern regions respectively, I assume.

## Reply 75 — participant_050 · 2025-08-26 · post-30702499

Speaking of the 2nd Marcellus flood. Will there be scripted predicatable desasters in the game, are they semi scripted or complete random? Semi scripted in a way that there needs to be one catastrophic flood in the North Sea at least once

## Reply 76 — participant_052 · 2025-08-26 · post-30702500

@lachek What do you think about counties affected by disasters having a modifier that raises religious conversion efficiency?

## Reply 77 — participant_054 · 2025-08-26 · post-30702502

Please, add more ways to prevent both natural disasters and plagues as it was historically (like it was with Poland and The Black Death for instance), not to mention it would be great for the players to not suffer from RNG more than it's necessary and not want to "keep themselves safe" irl

## Reply 78 — participant_055 · 2025-08-26 · post-30702520

I hope it will give really big negative modifiers and not so strong positive modifiers when we achieve the project. Actually it seem to be an other tool for snowballing the game. Maybe the rewards shouldn't stay during the lifetime of the character, but for something like 100 years (I am thinking for modded content) Natural Disasters are free content or the dlc will be needed? (To me it look good for free content) It would be interesting to see epidemies rise after a disaster

## Reply 79 — participant_056 · 2025-08-26 · post-30702526

I like what I read. As a suggestion, I think this system could be expanded in the future. Examples: 1. The large construction system could be used in the future to build large cathedrals/mosques or other cultural and/or religious buildings. 2. The situation system could be implemented for diseases or even the emergence of heresies.

## Reply 80 — participant_057 · 2025-08-26 · post-30702528

Do natural disasters affect raised armies? The Fifth and Seventh Crusades failed because of the flooding of the Nile.

## Reply 81 — participant_005 · 2025-08-26 · post-30702529

Low Nile flood level, low rainfall, blights, and other things caused famine, not just natural disasters and pandemics.

## Reply 82 — participant_058 · 2025-08-26 · post-30702561

Is the Disaster mechanic locked behind the DLC, or is it available for everybody with the free patch?

## Reply 83 — participant_059 · 2025-08-26 · post-30702574

While I like everything I see, I wish the CK3 dev team wasn't so hesitant to be mean to players. The game needs more random, punishing problems that are largely outside our control. It feels contrary to the concept of "Disasters" that these events are so easy to turn in the player's favor. It's already frustrating that Plagues have zero effect on armies when there ought to be brutal attrition for players and AI alike. I understand that some of the community may not agree, but could these settings at least be included as Game Rules?

## Reply 84 — participant_060 · 2025-08-26 · post-30702579

Funnily enough I feel like something like this should have been how the plague system operated instead of with the generic event system (that once again just turns everything into a clickfest because I'm not going to be bothered reading the same events 500 times). Event spam and modifier spam are the current mechanical scourges of the game for me. I hope that disaster management errs more towards the new screens and management aspects and not towards events, which I am so tired of.

## Reply 85 — participant_046 · 2025-08-26 · post-30702586

<!-- artifact:quote:start -->
> Seleukos.I.Nikator said: To me this feature bears resemblance to plagues. Not that this is a negative thing, but these two mechanics do seem quite similar. Perhaps with the difference that the follow-up phase of a disaster is much more essential than the actual event what is the case for plagues. On another note, are there any other disasters apart from flooding and earthquakes that we'll see in the game? Things like drought or blizzards would be quite appropriate too for southern and northern regions respectively, I assume. Click to expand...
<!-- artifact:quote:end -->
Its interesting that plagues had innate dev recovery, whilst disasters need great projects

## Reply 86 — participant_061 · 2025-08-26 · post-30702605

Wide gameplay with natural disasters is going to be "interesting". What's the length of time between natural disasters?

## Reply 87 — participant_062 · 2025-08-26 · post-30702612

Great work with the illustration. For natural disasters, what about volcanoes in places like Italy and Iceland?

## Reply 88 — participant_061 · 2025-08-26 · post-30702637

<!-- artifact:quote:start -->
> MagisterKiras said: As if the endless diarrhea epidemic wasn't enough... Click to expand...
<!-- artifact:quote:end -->
The brown wave left no survivors. (1:00)

## Reply 89 — participant_063 · 2025-08-26 · post-30702655

-Paradox: *introduces a new feature* -Fanbase: That's amazing, but how about expanding it tenfold? Seriously though, I really like this. And hopefully we get to see more disasters along the way. Fires, tsunamis, storms. And if I were to allow myself some more ambitious thoughts, we could have bandits, heretics and peasant revolts represented this way. You coordinate with your vassals to finance guard posts, large countryside patrols and help to those who are affected. Instead of being a one-time hit, it could be an ongoing situation, only resolved if you dedicate enough time and funds to it.

## Reply 90 — participant_064 · 2025-08-26 · post-30702656

It's cool that this is coming but it really makes me want pop mechanics. Disasters and plagues could have so much more teeth to them if we had those.

## Reply 91 — participant_065 · 2025-08-26 · post-30702703

Just think, but will it be possible to build the Aswan Dam to permanently stop the Nile from flooding?

## Reply 92 — participant_027 · 2025-08-26 · post-30702710

<!-- artifact:quote:start -->
> Beefalaxx said: It's cool that this is coming but it really makes me want pop mechanics. Disasters and plagues could have so much more teeth to them if we had those. Click to expand...
<!-- artifact:quote:end -->
I have advocated for a toned down version of a pop mechanic. I'd love to see a full pop system integrated as well but I doubt they'll go that far.

## Reply 93 — participant_016 · 2025-08-26 · post-30702711

If we do eventually get production mechanics (and food), I imagine this could be used to represent famine. We already have fertility mechanics anyway, even if they are limited in scope.

## Reply 94 — participant_066 · 2025-08-26 · post-30702735

<!-- artifact:quote:start -->
> Riiizzz said: Also, I really like how flooding is not just a negative thing, and that it boosts land fertility and such Click to expand...
<!-- artifact:quote:end -->
The Nile is a soft and gentle mother. The Yellow River ... is the og Asian tiger mom.

## Reply 95 — participant_067 · 2025-08-26 · post-30702884

1. Was there a refresh on the design of Coat of Arms? The Fatimid banner stands out a bit more than it does now. 2. If the Silk Road is going to be a situation, then you should just leave it out of All Under Heaven and put it into the Trade-focused dlc I presume is coming next year. A situation will be a terrible way to represent the Silk Road. 3. I foresee Natural Disasters being nerfed five days from release just like Plagues, Harm events, and Feuds were.

## Reply 96 — participant_068 · 2025-08-26 · post-30702911

Wow, I really like the new clan coat of arms design!

## Reply 97 — participant_011 · 2025-08-26 · post-30702913

<!-- artifact:quote:start -->
> DiabloDeVille said: Its interesting that plagues had innate dev recovery, whilst disasters need great projects Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> FondMemberofSociety said: The Nile is a soft and gentle mother. The Yellow River ... is the og Asian tiger mom. Click to expand...
<!-- artifact:quote:end -->
Makes sense, I guess? A plague kills off a bunch of people but to recover from it once it's over they just need to procreate more often. Rebuilding cities flattened by earthquakes requires more effort.

## Reply 98 — participant_069 · 2025-08-26 · post-30702985

Hey i know it's not the topic of the DD but can we please have a look at how the "Change Empires Oficial Faith" Decision is balanced ? It is going to be specially important since we are going to be seeing Burocratic governmet mechanichs more. I understand it should be harder to do than just in a feudal relm as bureocratic relms kinda have this pseudoconstitution along with them, but as of right know changing them is prohibitly expensive for no reason in my sight. A sugestion i have its make it scale with how many of either your vassals or your powerfull vassals have the same religion as you, this would actualy make you go through all the trouble of dealing with the problem of conversions, giving up hooks, money and unrest/resistaince instead of just having to accrue pure influence. I think it's problematic as is because the game treats only your character in the entire world having said faith and everyone in your relm following the faith you want to change it to as the same thing ! same costs and difficulties wich is ridiculous. The only ways of getting that one decision to be cheaper right now as far as i know is the theology tree perk which discounts almost nothing if i am going to be honest, and that Absolutelly awefull Estate building, it's bad because you can only acess it mid to late game.... in which case what is even the point lmaooooo ??? that building is porly designed as fuck, it should honestly be removed or the modifiers be made available from the get go. Anyways thats it, thank you. Ps. it's a specially spit on the face when a populist faction changes the byzantine empire religion for example... like what you mean i have to grind just to change religion and the ai can do it FOR FREE ????? WHAT?

## Reply 99 — participant_070 · 2025-08-26 · post-30703015

<!-- artifact:quote:start -->
> SMiki Lorebringer said: Makes sense, I guess? A plague kills off a bunch of people but to recover from it once it's over they just need to procreate more often. Rebuilding cities flattened by earthquakes requires more effort. Click to expand...
<!-- artifact:quote:end -->
*(no text body — reaction-only or media-only post)*

## Reply 100 — participant_071 · 2025-08-26 · post-30703021

Please, say that isolation will be reworked. When a pregnant woman in isolation gives birth, the child doesn’t get “isolation.” That’s ridiculous. If the isolation mechanic is going to be so important in these events, then it’s necessary.

## Reply 101 — participant_052 · 2025-08-26 · post-30703154

Disaster affected areas could spawn missions for adventurers. Helping out could be a good way to gain prestige. Landed rulers donating money could also be a good way to get a renown bonus as renown is a bit hard to gain.

## Reply 102 — participant_072 · 2025-08-26 · post-30703197

This is great! I would love to see the plagues from Legends of the Dead folded into this system, giving us a more active way to recover Can these disasters happen anywhere on the map or are they limited to certain areas (i.e. The Rhine, Nile River, Yellow River)

## Reply 103 — participant_014 · 2025-08-26 · post-30703225

<!-- artifact:quote:start -->
> sreckom92 said: Seriously though, I really like this. And hopefully we get to see more disasters along the way. Fires, tsunamis, storms. Click to expand...
<!-- artifact:quote:end -->
The chance go get them is close to zero Paradox has proven that they rarely go back to ancient dlc features : - Legends are still terribles - We are still waiting for interactions with adventurers when playing landed - They claimed herd mechanic is not perfect due to lack of time, but they said it will stay The reason is simple, working on old content brings in very little money I would like them to have a custody team working only on old content and fixing bugs more seriously, but it's not in paradox plans

## Reply 104 — participant_073 · 2025-08-26 · post-30703448

Something I really hope someone does is make a mod to add Volcanoes to this system, since it won't be in the base game version.

## Reply 105 — participant_074 · 2025-08-26 · post-30703461

<!-- artifact:quote:start -->
> "Historical Frisian settlements were built on artificial terpen up to 15 metres (49 ft) high to be safe from floods in periods of rising sea levels." Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> "third terp-building period dates from AD 700 (Old Frisian times). This ended with the coming of the dike somewhere around 1200." Click to expand...
<!-- artifact:quote:end -->
Are River Floods the only type of flood, or are storm tides from the sea also possible? Especially around the North Sea storm tides could be more widespread and deadly than river floods, and North Sea Storm tides account to some of the most devastating floods in recorded history. They should affect modern day Denmark, northwest Germany, the Netherlands, Belgium and England. Other mentioned the St Marcellus's Flood, there was also the St Lucia's flood, the All Saints Flood and the St Elisabeth Flood within the time frame of the game just as some examples of some truly devestating North Sea storm tides. The St Lucia's flood had major political ramifications as well, securing the dominance of the county of Holland over Frisia On top of that I think Frisian and Dutch culture should get access to the technology of Terps from game start and have the unlockable technology of dikes. These should help mitigate the effects of flood disasters to some extent (from Wikipedia on terps)

## Reply 106 — participant_075 · 2025-08-26 · post-30703464

the gold cost seem insane like always income from building really is never enough

## Reply 107 — participant_076 · 2025-08-27 · post-30703509

I don't hate the idea, but it's another system that will fall prey to CK3's terrible money balance. In the early game you won't have enough money to interact with these projects at all and will just have to eat the negatives, which isn't particularly fun, and in the later game youll have infinite money and just ace them every time, turning it into another free benefit simulator. I know people don't want an economic rework (for some reason) but I think it's by far the biggest system holding the game back right now. The entire game suffers from this situation where there's an incredibly harsh divide between the early game lack of money, where you literally can't afford anything, to then hitting some arbitrary point of having infinite money for the rest of the game you cant spend even if you try. Anyway, at least for this system, I think there should be relief options that trade something like country control and levies instead of gold for the relief options. It's not perfect but I think having some method to interact with this system without gold is essential to not being completely terrible. It's not like unpaid labour was uncommon during this time period.

## Reply 108 — participant_073 · 2025-08-27 · post-30703517

Uhhh, where did you get the impression people don't want an economic rework? I feel like a lot of people here do want an economic rework.

## Reply 109 — participant_077 · 2025-08-27 · post-30703652

"I DID LEAVE THE WATER RUNNING!"

## Reply 110 — participant_078 · 2025-08-27 · post-30703719

<!-- artifact:quote:start -->
> ourg said: So only flood and eathquake ? No typhoon/cyclone, tsunami, volcanic eruption, drought , etc.... ? Click to expand...
<!-- artifact:quote:end -->
Scope creep kills ambitious games. If Paradox Interactive wants to focus on the core Natural Disaster mechanics and the two natural disasters most relevant to Chinese history, I hope they circle back to those core mechanics in future expansions. Droughts especially—tsunamis and tropical storms are very regional disasters, but droughts are problems everywhere! (Albeit not problems with interesting solutions.) Volcano eruptions are crazy rare, though. At a glance, I only see one historically-significent eruption that took place in the time period covered by CK3. There are probably more, since most areas with lots of vulcanism are poorly-covered by medieval historians, but by the same token...most areas with lots of vulcanism are poorly-covered by medieval historians. I feel it's also worth noting that volcanic eruptions, in addition to being rare, are kinda weaksauce as far as natural disasters go. RIP if your village is on that mountain, but even the worst volcanic eruptions have death tolls in the low tens of thousands. (Except the 1815 Mount Tambora eruption, which probably killed something like 70-100k people without counting the effect on global climate, but that's a world-shaking anomaly, not a typical volcanic disaster.) For all the grip volcanoes have on the human psyche, they're just not important. Unless you live on a volcano.

## Reply 111 — participant_046 · 2025-08-27 · post-30703732

<!-- artifact:quote:start -->
> GreatWyrmGold said: Scope creep kills ambitious games. If Paradox Interactive wants to focus on the core Natural Disaster mechanics and the two natural disasters most relevant to Chinese history, I hope they circle back to those core mechanics in future expansions. Droughts especially—tsunamis and tropical storms are very regional disasters, but droughts are problems everywhere! (Albeit not problems with interesting solutions.) Volcano eruptions are crazy rare, though. At a glance, I only see one historically-significent eruption that took place in the time period covered by CK3. There are probably more, since most areas with lots of vulcanism are poorly-covered by medieval historians, but by the same token...most areas with lots of vulcanism are poorly-covered by medieval historians. I feel it's also worth noting that volcanic eruptions, in addition to being rare, are kinda weaksauce as far as natural disasters go. RIP if your village is on that mountain, but even the worst volcanic eruptions have death tolls in the low tens of thousands. (Except the 1815 Mount Tambora eruption, which probably killed something like 70-100k people without counting the effect on global climate, but that's a world-shaking anomaly, not a typical volcanic disaster.) For all the grip volcanoes have on the human psyche, they're just not important. Unless you live on a volcano. Click to expand...
<!-- artifact:quote:end -->
Its not scope creep, its that if theyre adding natural disasters, they should add most of them. It'd be weird to claim youre adding weather to the game, but only adding rain not sunny days

## Reply 112 — participant_028 · 2025-08-27 · post-30703748

<!-- artifact:quote:start -->
> DiabloDeVille said: Its not scope creep, its that if theyre adding natural disasters, they should add most of them. It'd be weird to claim youre adding weather to the game, but only adding rain not sunny days Click to expand...
<!-- artifact:quote:end -->
Just imagine if they picked a more niche disaster. Nothing but mudslides all across the map from the Canary Islands to Bali. Your court was wiped out in a mudslide? Oh, most of mine was too!

## Reply 113 — participant_045 · 2025-08-27 · post-30703906

<!-- artifact:quote:start -->
> DiabloDeVille said: It'd be weird to claim youre adding weather to the game, but only adding rain not sunny days Click to expand...
<!-- artifact:quote:end -->
Cough cough Fertility only in Nomad Lands. cough cough

## Reply 114 — participant_027 · 2025-08-27 · post-30703966

<!-- artifact:quote:start -->
> TheBusStop said: Are River Floods the only type of flood, or are storm tides from the sea also possible? Especially around the North Sea storm tides could be more widespread and deadly than river floods, and North Sea Storm tides account to some of the most devastating floods in recorded history. They should affect modern day Denmark, northwest Germany, the Netherlands, Belgium and England. Other mentioned the St Marcellus's Flood, there was also the St Lucia's flood, the All Saints Flood and the St Elisabeth Flood within the time frame of the game just as some examples of some truly devestating North Sea storm tides. The St Lucia's flood had major political ramifications as well, securing the dominance of the county of Holland over Frisia On top of that I think Frisian and Dutch culture should get access to the technology of Terps from game start and have the unlockable technology of dikes. These should help mitigate the effects of flood disasters to some extent (from Wikipedia on terps) Click to expand...
<!-- artifact:quote:end -->
Oooh yes, sir. I hope that region gets some love in the near future. The landscape changed dramatically and the relationship the Dutch have with the sea is currently underrepresented. Your suggestion of terps and dikes makes perfect sense to me. And the fact that the northern region doesn't start with the Frisian culture by default irritates me beyond measure...

## Reply 115 — participant_079 · 2025-08-27 · post-30704221

Culture and disasters? With all the environmental cultural traits, and you really really are specialized at making the taigas and winters as nice and comforting as imaginable.. certainly the cold shouldn't come as a surprise? Besides the taiga is kinda covered in sprawling metropolises. Might even have olive trees & vineyards growing in the 2 oaks deep permafrost -ok that might need fixing. Just consider modern day: one thumb of snow in the new philippines (txas) vs a manheight or two of snow in norse lands. Or for that matter a few years or drought in say persia: laughs in farsi and draws another mountain crystal goblet of water from the qanats before returing to philosophy.

## Reply 116 — participant_080 · 2025-08-27 · post-30704305

I think a good idea for a adventurer's contract would be disaster relief. It would most likely be stewardship based.

## Reply 117 — participant_002 · 2025-08-27 · post-30704328

<!-- artifact:quote:start -->
> Enuvrack said: I think a good idea for a adventurer's contract would be disaster relief. It would most likely be stewardship based. Click to expand...
<!-- artifact:quote:end -->
That's great idea!

## Reply 118 — participant_081 · 2025-08-27 · post-30704341

Will all Natural Disasters follow this format? I can understand there being warning signs for floods, or famines, or even , at a bit more of a stretch, great fires and storms. But quakes? I've experienced earthquakes, and let me tell you it would have been greatly appreciated if there'd been a handy popup situation letting me know that it was about to happen.

## Reply 119 — participant_082 · 2025-08-27 · post-30704471

Can anyone convince me that this doesnt seem much different or any less impactful than plagues? Fundementally it looks to be the exact same thing

## Reply 120 — participant_083 · 2025-08-27 · post-30704474

<!-- artifact:quote:start -->
> Takisha said: Please, say that isolation will be reworked. When a pregnant woman in isolation gives birth, the child doesn’t get “isolation.” That’s ridiculous. If the isolation mechanic is going to be so important in these events, then it’s necessary. Click to expand...
<!-- artifact:quote:end -->
what we're getting: even more event spam, basically plagues 2.0 what we need: bug fixes, localisation fixes, interconnect DLC mechanics, more fixes you're implying they need to fix broken old stuff ... thats not how this dev team roles

## Reply 121 — participant_033 · 2025-08-27 · post-30704498

Will natural disasters really DESTROY buildings? Especially those in Domicile? And perhaps banks and enclaves in the future? As they are often more fragile than castles, can not be sieged, and destroying updates may stop AI from stacking updates.

## Reply 122 — participant_014 · 2025-08-27 · post-30704697

<!-- artifact:quote:start -->
> Takisha said: Please, say that isolation will be reworked. When a pregnant woman in isolation gives birth, the child doesn’t get “isolation.” That’s ridiculous. If the isolation mechanic is going to be so important in these events, then it’s necessary. Click to expand...
<!-- artifact:quote:end -->
Thx I was not aware of this bug. I've added it to my plague fix mod Took me 2 mins to fix.

## Reply 123 — participant_084 · 2025-08-27 · post-30704804

I'm not sure I like the warning phase. It's sure nice gameplay-wise to get some time to prepare, but natural disasters are supposed to be somewhat unpredictable. It would be more interesting if, say, the warning event doesn't always triggers the disaster. "The Nile river might flood" rather than "The Nile river will flood" Not a fan of the duration of the disaster itself. I see the phase lasts over SEVEN months here; most floods don't last that long, only truly apocalyptic, once-in-a-millenium would. I humbly suggest that the phase lasts a couple days, a month at most, with several events firing quickly, possibly up to 1 every day (to let you feel the weight of the disaster, and not having it feel just like a notif "earthquake just happened, time to help those filthy peasants"). Not too much events though; we all know too much events kills the event, and CK3 already has a big event spam problem. This ended up sounding much more negative than I'd wanted, so let me congratulate the dev team for this; overall it's (nearly) what the plagues should have been, and I really love everything around the recovery in concept. I hold my definitive judgment until I see it in gameplay, but this sounds very cool despite my complaining above.

## Reply 124 — participant_085 · 2025-08-27 · post-30705147

<!-- artifact:quote:start -->
> lachek said: View attachment 1353632 Click to expand...
<!-- artifact:quote:end -->
Two minor things I noticed in this event text: it's should be its (the possessive form rather than a contraction of 'it is'), and to me 'erected' also seems like an odd word choice for a body of water as it suggests it rises up over the land. 'Formed'/'created'/'left' seem like more natural words to me in that context. The disaster system looks great and I like the approach focusing more on player reaction than just random setbacks. While the system might still be pretty rough for players with small territories which are completely within the disaster area, realistically if there were a small independent state in the direct path of the Yellow River flood it would have probably been game over...

## Reply 125 — participant_078 · 2025-08-27 · post-30705244

<!-- artifact:quote:start -->
> DiabloDeVille said: Its not scope creep, its that if theyre adding natural disasters, they should add most of them. It'd be weird to claim youre adding weather to the game, but only adding rain not sunny days Click to expand...
<!-- artifact:quote:end -->
Absurd analogy. A sunny day is just a day without rain; the two concepts are obviously inherently linked. Adding rainy days is meaningless if there aren't sunny days to contrast them. Different natural disasters are...different disasters. Earthquakes and droughts have nothing in common except "bad thing that happens to a big area".

## Reply 126 — participant_046 · 2025-08-27 · post-30705397

<!-- artifact:quote:start -->
> GreatWyrmGold said: Absurd analogy. A sunny day is just a day without rain; the two concepts are obviously inherently linked. Adding rainy days is meaningless if there aren't sunny days to contrast them. Different natural disasters are...different disasters. Earthquakes and droughts have nothing in common except "bad thing that happens to a big area". Click to expand...
<!-- artifact:quote:end -->
An overcast day is a day without rain, sun, hail, or snow. Earthquakes are alot worse for cities than droughts are, as you can import during a drought, but need to rebuild during an earthquake

## Reply 127 — participant_005 · 2025-08-27 · post-30705474

<!-- artifact:quote:start -->
> DiabloDeVille said: An overcast day is a day without rain, sun, hail, or snow. Earthquakes are alot worse for cities than droughts are, as you can import during a drought, but need to rebuild during an earthquake Click to expand...
<!-- artifact:quote:end -->
Droughts can be less severe on people damage now a days, but it was much more a problem back in medieval times. Droughts can mean famine, and the nobles don't waste resources making sure that the peasants were fed. Cities typically got their grain from local sources, so droughts did impact cities a great deal. Earthquakes can cause infrastructure damage depending on how severe the earthquake is and will most likely cause a more immediate impact, but the famines caused by droughts should not be understated. A low flood Nile could be just as damaging as a high flood Nile.

## Reply 128 — participant_079 · 2025-08-27 · post-30705520

<!-- artifact:quote:start -->
> tribnia said: Will natural disasters really DESTROY buildings? Especially those in Domicile? And perhaps banks and enclaves in the future? As they are often more fragile than castles, can not be sieged, and destroying updates may stop AI from stacking updates. Click to expand...
<!-- artifact:quote:end -->
Maybe even holdings, Antioch was supposedly leveled by a earthquake, Or a falling star, go figure.

## Reply 129 — participant_086 · 2025-08-28 · post-30705687

Interesting that Typhoons arn't one the natural disasters in game. I thought Kamikazi would be relevant considering ya know, two of them knocked out the mongol fleet in this games time frame. I don't think floods will really make sense as a replacment either. Some kind if intense storm natural disaster with localization to Typhoon for east Asia could have been useful for the white ship incident too. Maybe i'm over thinking this. There aren't even navies in this game still.

## Reply 130 — participant_087 · 2025-08-28 · post-30706171

How will disasters interact with diseases and legends? + Will there be changes to the price and support of legends? Because now there is an illogical situation where a poor but capable count can do the greatest trick on a hunt, but due to the small amount of money, this case will not spread by itself simply because it is COOL. + The game needs improvements directly related to characters, roleplaying and AI behavior. Please look at this idea - https://forum.paradoxplaza.com/foru...ction-of-future-content.1788817/post-30492314

## Reply 131 — participant_088 · 2025-08-28 · post-30706298

I think draught should maybe be another one depending on region. And maybe rare 1 per campaign volcano in indonesia?

## Reply 132 — participant_089 · 2025-08-29 · post-30708461

Are disasters going to open up opportunities for urban redesign and land redistribution, like real life disasters did?

## Reply 133 — participant_090 · 2025-08-29 · post-30708569

<!-- artifact:quote:start -->
> Asaipuol said: Not a fan of the duration of the disaster itself. I see the phase lasts over SEVEN months here; most floods don't last that long, only truly apocalyptic, once-in-a-millenium would. Click to expand...
<!-- artifact:quote:end -->
Most feats, hunts and weddings didn't last for many weeks or even months either. But ingame they do. I wouldn't worry about it.

## Reply 134 — participant_033 · 2025-08-29 · post-30708857

<!-- artifact:quote:start -->
> karl2025 said: Are disasters going to open up opportunities for urban redesign and land redistribution, like real life disasters did? Click to expand...
<!-- artifact:quote:end -->
Oh that Great Fire of Rome event in CK2...

## Reply 135 — participant_091 · 2025-08-31 · post-30712407

Do the disasters carry special names (like e.g. historic floods named after saints) and is some chronology of them kept? It is something that I miss for plagues...they happen, ravage thorugh the lands and then...POOF...they are over and gone from the game without you being able to see their full extend and vanish without a trace. Don't get me wrong, no need to book-keep every small disease outbreak or maybe a local forest fire (provided we get that disaster type on day), but really big impact ones would be nice. Or if you don't want to create a separate system: Maybe characters somehow affected by a disaster could get a memory entry? That system is undeused IMO anyway; still waiting for none minor wound and becoming disbabled getting added as memories.

## Reply 136 — participant_092 · 2025-09-03 · post-30717967

Not related to Natural Disasters per se, but will some of the existing big construction projects, like say Legendary Buildings or Universities also be made into Great Projects? Can you as a vassal contribute to your liege lord's extravagant palace?

## Reply 137 — participant_093 · 2025-09-03 · post-30718962

<!-- artifact:quote:start -->
> M0ridin said: Not related to Natural Disasters per se, but will some of the existing big construction projects, like say Legendary Buildings or Universities also be made into Great Projects? Can you as a vassal contribute to your liege lord's extravagant palace? Click to expand...
<!-- artifact:quote:end -->
I *feel like* the special temples currently in Burma might be changed with AUH? because the giant temple complex currently in the county of Pagan is kinda what they described for the Mandala Gov, but yeah I think that would really separate special unique buildings from normal ones, which I would like.

