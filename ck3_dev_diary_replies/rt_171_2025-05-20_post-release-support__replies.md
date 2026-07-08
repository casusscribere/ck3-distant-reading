---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1755412/"
forum_thread_id: 1755412
content_type: reply_thread
parent_dd_file: dd_171_2025-05-20_post-release-support.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 171
title: "Dev Diary #171 - Post-Release Support"
dd_date: 2025-05-20
expansion: Khans of the Steppe
patch: Patch 1.16
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 9
reply_count: 175
participant_count: 103
reply_date_first: 2025-05-20
reply_date_last: 2025-06-19
body_word_count: 15738
inline_image_count: 0
quoted_span_count: 110
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Dev Diary #171 - Post-Release Support

*175 replies from 103 participants across 9 pages*

## Reply 1 — participant_001 · 2025-05-20 · post-30379387

I’m excited to try the new difficulty settings even if they are untested! Short of an AI overhaul, I believe this is what the game sorely needs to provide a more fulfilling and immersive experience to seasoned players.

## Reply 2 — participant_002 · 2025-05-20 · post-30379396

<!-- artifact:quote:start -->
> CatilinamSum said: I’m excited to try the new difficulty settings even if they are untested! Short of an AI overhaul, I believe this is what the game sorely needs to provide a more fulfilling and immersive experience to seasoned players. Click to expand...
<!-- artifact:quote:end -->
We have a variety of changes that weren't shown in the DD image for these difficulties, but I do want to temper expectations: This is not a silver bullet for the difficulty complaints players are posting, and we don't consider it a long-term solution to that problem. We'll need to iterate and refine this over time, and we're still looking for ways to increase the fundamental challenge of the game without leaning on AI "cheats" like these.

## Reply 3 — participant_003 · 2025-05-20 · post-30379398

<!-- artifact:quote:start -->
> While I’m just one part of the broader Community Team for Crusader Kings, I’m ultimately responsible for nearly every piece of public-facing communication we publish as a studio: dev diaries, feature breakdowns, chapter premiere videos, social media posts, etc. Click to expand...
<!-- artifact:quote:end -->
*(no text body — reaction-only or media-only post)*

## Reply 4 — participant_004 · 2025-05-20 · post-30379403

Could you show us more of the effects affected by hard/very hard modes ?

## Reply 5 — participant_005 · 2025-05-20 · post-30379407

Why do I feel ashamed after reading this diary...

## Reply 6 — participant_006 · 2025-05-20 · post-30379415

Could you incorporate a rule or setting that hides event outcomes? It would be a good way to incorporate difficulty (of course, it would be experimental, and some events would have to be rewritten to be clearer).

## Reply 7 — participant_007 · 2025-05-20 · post-30379418

One thing that would help a lot with difficulty: making alliances more difficult to procure. Right now, any difficult war can be mitigated by marrying a child to the HRE and calling them in. Any strong AI realm can be countered by setting up a bunch of alliances. The CK2 approach where marriage instead granted NAP's would still give them a diplomatic purpose, make diplomacy more interesting and make the game more 'difficult'. In general, difficulty can make a game more interesting. Any story without setbacks is a boring one and right now foreign diplomacy is basically non-existent compared to other paradox games when it comes to player considerations. Solving this would help elevate the game so much. (Also, in a recent game I was losing herd - herd growth was negative. Was that a bug? It was both a white zud and my local fertility was at 0 - it really made for an interesting game, forcing migrations)

## Reply 8 — participant_008 · 2025-05-20 · post-30379420

<!-- artifact:quote:start -->
> We’re not planning on implementing this. Put simply, the system wasn’t designed with this in mind and is instead built around discrete reductions. Too much of the game goes off the rails when it tries to deduct what doesn’t exist, and herd decay ultimately impacts AI rulers far more than it impacts players (compounding balance/difficulty concerns). With the PRS stage for Khans of the Steppe coming to an end, we don’t have the time or resources available to rework a core aspect of the DLC to this degred. Click to expand...
<!-- artifact:quote:end -->
Proof that you should make development public earlier to get proper feedback from broader community. This would get called out %100 if the community knew about it.

## Reply 9 — participant_002 · 2025-05-20 · post-30379426

<!-- artifact:quote:start -->
> IngvarBS said: Could you show us more of the effects affected by hard/very hard modes ? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Added Hard / Very Hard Difficulty game rule options The philosophy behind these changes is to try and compensate for what the AI can't or shouldn’t be able to do as efficiently as a player. For example: the AI doesn’t change Vassal Contracts very often, intentionally use Abductions to win wars/gain loads of money, use Marriages to pull realms into losing wars en masse, or mass construct economic buildings before hiring MaA, to name a few. We’ve tried to keep most of these changes as invisible as possible, instead of showing ‘Very Hard’ as a modifier in various tooltips (although it happens in some places out of necessity). Added the Hard difficulty which boosts AIs and changes some systemic behavior for players, aimed at providing a more challenging yet still balanced experience While AI realms are buffed, generally the game should progress similarly to the Normal game Changes for the AI: Buying and maintaining MaA is significantly easier Stress management is improved Constructing buildings and holdings is somewhat easier (not too much, or the player would be able to abuse it for their own gain!) Levies reinforce faster Improving opinion is faster Tyranny gain is reduced Mercenary use is cheaper Factions are slightly more lenient Revoking titles and retracting vassals is easier Activity costs are reduced Court Position management is significantly cheaper Agents are slightly more willing to join schemes vs. players Recruiting guests is significantly cheaper Amenities are significantly cheaper CB prestige costs are cheaper, especially vs. players Changes for the Player: Regular Mercenaries are more expensive Factions are somewhat less lenient (depending on vassal opinion) Revoking titles and retracting vassals is harder More vassals are inclined to join tyranny wars started by players, primarily guided by opinion Much less likely to randomly become a Conqueror Heavier penalties to arranging marriages based on number of existing alliances, lesser bonuses from desires alliance, etc. The player should be able to have one significant alliance, and one minor alliance. Gaining alliances at war will be almost impossible. Marrying with the intent of getting highly skilled courtiers or wanderers to join your court is now much harder, especially if your candidate is not your close family member. This should make it much harder to, for example, gain a great general or several fantastic knights the day before you go to war. Agents are slightly less willing to join schemes Tyranny gain from unfair Vassal Contract changes is significantly increased (see changes to Vassal Contract scoring in the balance section to see why this change is significant!) More resources are needed to reinforce armies for Adventurers & Nomads Gold gain from ransoming is lowered Religious heads are now less inclined to grant players gold Added the Very Hard Difficulty which significantly boosts AIs, changes systemic behavior, and applies some penalties to players, aimed at providing a much more challenging experience AI realms are going to be significantly more strong and stable, making the game progress differently Changes for the AI: Everything from hard, but the bonuses are greater AI Rulers gain extra advantage when leading their own armies Changes for the Player: Everything from hard, but the penalties are greater Hostile Scheme success chance starts at a much lower level Knight efficiency is reduced Click to expand...
<!-- artifact:quote:end -->
Sure. Might as well put it all on the table; here's the difficulty option section from the upcoming changelog.

## Reply 10 — participant_009 · 2025-05-20 · post-30379427

Making the game harder isn’t the issue. Making the game engaging is. The issue isn’t that the AI needs buffs, the issue is the AI doesn’t do anything meaningful in the first place. It’s very discouraging to see the solution appears to be “hard mode” after all the extensive discussions that are had outlining the problem on this forum. All this accomplishes is making a game with little in the way of emergent storytelling harder (read: more micro-intensive) without making it any more interesting. The problem isn’t that the game is easy. The problem is all the characters are cardboard cutouts who don’t have any agency - they are acted upon, they do not act. Between the Conquerer system and now these “hard mode” buffs it really comes off as you not understanding the core issue with the game. It’s not that it’s easy - it’s that it’s boring. All you accomplish by making it “harder” in this way is make it more micro-intense in addition to being boring.

## Reply 11 — participant_001 · 2025-05-20 · post-30379430

<!-- artifact:quote:start -->
> karasis65 said: Proof that you should make development public earlier to get proper feedback from broader community. This would get called out %100 if the community knew about it. Click to expand...
<!-- artifact:quote:end -->
At this point, I think their best solution is to implement large losses of Herd through discrete events, representing disasters and diseases. More of these % Herd die-offs would help to address the tendency of large Nomadic empires to snowball out of control.

## Reply 12 — participant_010 · 2025-05-20 · post-30379431

<!-- artifact:quote:start -->
> We’re not planning on implementing this. Put simply, the system wasn’t designed with this in mind and is instead built around discrete reductions. Too much of the game goes off the rails when it tries to deduct what doesn’t exist Click to expand...
<!-- artifact:quote:end -->
Sorry I really don't get this. How about ZERO herd growth during stuff like zud, maybe 1% herd deduction per month if your total herd is over the supply limit of your domain? This way smaller AI rulers wouldn't be impacted. Surely there are some solutions other than a mere % buff to fertility decline. All it does is make it so the player has +100 herd growth rather than +130. Or else a way to lose yurt upgrdes. I mean some kind of stakes. You could lock this behind hard mode now too. Anyway, thanks for the diary!

## Reply 13 — participant_011 · 2025-05-20 · post-30379435

<!-- artifact:quote:start -->
> PDX-Trinexx said: View attachment 1302678 [Highly experimental! Mostly untested! Probably imbalanced! Try it out later this week and tell us what you think.] Click to expand...
<!-- artifact:quote:end -->
Finally, something! "will make the game less balanced" are_you_sure_about_that.mp4 No herd decay is very sad though. The only thing that will really impact is saving up 75k herd for absolute dominance, which is already kinda tedious in vanilla, so does it really matter?

## Reply 14 — participant_007 · 2025-05-20 · post-30379436

Perhaps you could also remove the limitation of capping the amount of AI plots targeting the player. I cannot remember the last time I was assassinated - would be interesting if that occurred more often.

## Reply 15 — participant_012 · 2025-05-20 · post-30379438

Would you mind sharing how this new difficulty affects Kingdom and Empire tier realms? If both lieges and vassals get buffed, I am curious as to whether self-destruction via factions with more powerful members becomes the main issue for AI realms.

## Reply 16 — participant_013 · 2025-05-20 · post-30379439

<!-- artifact:quote:start -->
> PDX-Trinexx said: That said, our community has made it clear that we’re not meeting our objective, and doing something is better than doing nothing. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PDX-Trinexx said: We’ve also heard quite a few people asking for a passive herd decay mechanic. To go ahead and rip the bandaid off: We’re not planning on implementing this. Put simply, the system wasn’t designed with this in mind and is instead built around discrete reductions. Too much of the game goes off the rails when it tries to deduct what doesn’t exist, and herd decay ultimately impacts AI rulers far more than it impacts players (compounding balance/difficulty concerns). With the PRS stage for Khans of the Steppe coming to an end, we don’t have the time or resources available to rework a core aspect of the DLC to this degree. Additional adjustments to this system are still possible in Realm Maintenance updates, but these are unlikely to fundamentally rework the system itself. Click to expand...
<!-- artifact:quote:end -->
Difficulties based on AI cheat is really the worst idea ever, I know it's really popular because it's the easiest way to do it. Already posted it elsewhere, but here some ideas to increase dificulty without AI cheats : - increase odds for death/injuries, don't let almost all events with a good/safe option. The main issue is that currently all bad events have a safe option. Sometime you have to accept your fate - reduce powercreep features almost only used by player, or teach the AI to use it properly - Limit alliances from mariage : It's way to easy to have strong alliance with mariage. Mariage needs a rework. The AI should seek for strong alliance mariage instead of almost totaly based on prestige gain - Set threshold for opinion ( exemple : a rival can't go above 0 opinion ) It has always trigger me that you can have rivals with 100 opinion of you. Currently we can't mod the max opinion, it's a flat global value. Opinion max (or min) should not be the same for everyone, but should be conditioned on diferent factors (traits/relation/culture/etc...) The main problem with the herd mechanic, is that it's designed as gold as it should be designed as levies Here my solution to the problem : Each county shoud be able to substaint a max amount of herd (depending on fertility/season/etc...) meaning if you have only 1 county you could only have that maximum herd. Herd comming from your vassal/tributary are taken as % of they own herd (coming from their max county possibility) you still need to grow your herd to the maximum of the county can handle with the fertility (max is the equilibirum in fertility) currently everything is calculted arround the herd gain, while it should be calculated on the current/max herd (like levies)

## Reply 17 — participant_002 · 2025-05-20 · post-30379440

<!-- artifact:quote:start -->
> Athius said: Perhaps you could also remove the limitation of capping the amount of AI plots targeting the player. I cannot remember the last time I was assassinated - would be interesting if that occurred more often. Click to expand...
<!-- artifact:quote:end -->
I believe that's set as a define and not something we can selectively edit based on game rules, buuuut I can see about bullying someone into changing that. Maybe. No promises.

## Reply 18 — participant_014 · 2025-05-20 · post-30379441

I was wondering how would they get feedback about crashes when the crash reporter always crashes, thankfully they went ahead and collect data from other sources instead of going "we have got no report of crashes from the crash reporter so there's no problem".

## Reply 19 — participant_015 · 2025-05-20 · post-30379447

I really don't understand the approach to difficulty in this game. On the one hand, the standing philosophy has been to not want one-off solutions and instead work with emerging - assumedly systemic - difficulty. but then whenever new content comes out, there never is any systemic difficulty present. Landless and Nomads basically have no stakes (landless moreso of course as they literally have no stakes that could lead to loss barring your entire line simply dying). And, as a consequence, we get non-systemic difficulty as bandaids. This was true for the random death events, it's effectively true for great conquerors and it's true for this rule as well. Can we just admit that a focus on systemic difficulty isn't happening?

## Reply 20 — participant_011 · 2025-05-20 · post-30379450

<!-- artifact:quote:start -->
> PDX-Trinexx said: We have a variety of changes that weren't shown in the DD image for these difficulties, but I do want to temper expectations: This is not a silver bullet for the difficulty complaints players are posting, and we don't consider it a long-term solution to that problem. We'll need to iterate and refine this over time, and we're still looking for ways to increase the fundamental challenge of the game without leaning on AI "cheats" like these. Click to expand...
<!-- artifact:quote:end -->
Im pretty sure you saw me posting this a lot of times already, but messing with building and MAA scores could yeild a lot of results without fundamentally changing the AI. Right now AI fails to even build military buildings, and in the miraculous situations where it has some they have no impact at all on how they choose MAAs. and also AI should really stop trying to hire every MAA type in the game and focus on one or two "core" types, countering works against the first case and unless you are planning to revamp it soon-ish it would be better to just make AI build more monolithic armies.

## Reply 21 — participant_016 · 2025-05-20 · post-30379451

I think the difficulty can be solved simply with some sort of aggressive expansion or infamy mechanic.

## Reply 22 — participant_017 · 2025-05-20 · post-30379452

<!-- artifact:quote:start -->
> ourg said: Difficulties based on AI cheat is really the worst idea ever, I know it's really popular because it's the easiest way to do it. Already posted it elsewhere, but here some ideas to increase dificulties without AI cheats : - increase odds for death/injuries, don't let almost all events with a good/safe option. The main issue is that currently all bad events have a safe option. Sometime you have to accept your fate - reduce powercreep features almost only used by player, or teach the AI to use it properly - Limit alliances from mariage : It's way to easy to have strong alliance with mariage. Mariage needs a rework. The AI should seek for strong alliance mariage instead of almost totaly based on prestige gain - Set threshold for opinion ( exemple : a rival can't go above 0 opinion ) It has always trigger me that you can have rivals with 100 opinion of you. Currently we can't mod the max opinion, it's a flat global value. Opinion max (or min) should not be the same for everyone, but should be conditioned on diferent factors (traits/relation/culture/etc...) The main problem with the herd mechanic, is that it's designed as gold as it should be designed as levies Here my solution to the problem : Each county shoud be able to substaint a max amount of herd (depending on fertility/season/etc...) meaning if you have only 1 county you could only have that maximum herd. Herd comming from your vassal/tributary are taken as % of they own herd (coming from their max county possibility) you still need to grow your herd to the maximum of the county can handle with the fertility (max is the equilibirum in fertility) currently everything is calculted arround the herd gain, while it should be calculated on the current/max herd (like levies) Click to expand...
<!-- artifact:quote:end -->
every time i play with more options to randomly die i dont enjoy my experience in this game tho, so while its true that more death = harder game, it also is just so unfun to me that it makes me not want to play with those options at all.

## Reply 23 — participant_018 · 2025-05-20 · post-30379454

<!-- artifact:quote:start -->
> PDX-Trinexx said: We have a variety of changes that weren't shown in the DD image for these difficulties, but I do want to temper expectations: This is not a silver bullet for the difficulty complaints players are posting, and we don't consider it a long-term solution to that problem. We'll need to iterate and refine this over time, and we're still looking for ways to increase the fundamental challenge of the game without leaning on AI "cheats" like these. Click to expand...
<!-- artifact:quote:end -->
Trinexx, Master of Expectation Management.

## Reply 24 — participant_019 · 2025-05-20 · post-30379456

This looks very promising. I am looking forward to it.

## Reply 25 — participant_007 · 2025-05-20 · post-30379469

<!-- artifact:quote:start -->
> One Proud Bavarian said: I really don't understand the approach to difficulty in this game. On the one hand, the standing philosophy has been to not want one-off solutions and instead work with emerging - assumedly systemic - difficulty. but then whenever new content comes out, there never is any systemic difficulty present. Landless and Nomads basically have no stakes, landless moreso of course as they literally have no stakes that could lead to loss barring your entire line simply dying). And, as a consequence, we get non-systemic difficulty as bandaids. This was true for the random death events, it's effectively true for great conquerors and it's true for this rule as well. Can we just admit that a focus on sytemic difficulty isn't happening? Click to expand...
<!-- artifact:quote:end -->
I think there are a number of deeper problems affecting this: 1. All modifiers and systems scale linearly, and most systems affect gold and opinion. This means that each new system that is introduced allows us to 'solve' opinion and gold problems, and the more systems are added the easier it becomes. Systems that harm opinion / gold income can be mitigated. ("Yes I killed your brother, but my court is fancy and look at my Yurt upgrades - you now love me non-the-less) This can be solved by having things scale on a logistic graph. (Aka, diminishing returns the higher you go) - but this may be an engine issue. Its such a large rewrite that its probably more for CK4 2. Many systems are designed to be 'solved' and can be ignored once this is done. The ease of solving them becomes easier the more systems are added, as per point 1. What do I mean? - Negative opinion? Take the actions to increase it, its now no longer an issue. - Court fancyness too low? Move the sliders. Its now solved. - Lack of gold? After 40 years of estate/domain upgrades its now solved. - Low legitimacy? Trigger a few activities. Issue resolved. I understand how you arrive here from a game design perspective, but things would be much more interesting if they would linger and be things you'd have to deal with for the course of the live of that character. It gives the characters personality (emphasizing the role-play of ck3, which I think is its strength) 3. The game is not interested in international diplomacy. The fact that a bug where the AI did not use many CB's existed for so long points to this. It used to be very rare for the AI to declare war on you. Its extremely easy to secure alliances by marriages. Thus solving any thread. The AI also does not respond to rising powers. Confederations were added in the last expansion, but not for feudal realms, which I do not understand.

## Reply 26 — participant_020 · 2025-05-20 · post-30379470

Any spoiler for you-know-what? It's just hard to wait until next Tuesday.

## Reply 27 — participant_009 · 2025-05-20 · post-30379484

<!-- artifact:quote:start -->
> 47pik said: Making the game harder isn’t the issue. Making the game engaging is. The issue isn’t that the AI needs buffs, the issue is the AI doesn’t do anything meaningful in the first place. It’s very discouraging to see the solution appears to be “hard mode” after all the extensive discussions that are had outlining the problem on this forum. All this accomplishes is making a game with little in the way of emergent storytelling harder (read: more micro-intensive) without making it any more interesting. The problem isn’t that the game is easy. The problem is all the characters are cardboard cutouts who don’t have any agency - they are acted upon, they do not act. Between the Conquerer system and now these “hard mode” buffs it really comes off as you not understanding the core issue with the game. It’s not that it’s easy - it’s that it’s boring. All you accomplish by making it “harder” in this way is make it more micro-intense in addition to being boring. Click to expand...
<!-- artifact:quote:end -->
To follow up on this, let me give an example in Victoria 3. I’m playing Mexico, and the USA wants to seize California from me, and since they are stronger I really don’t want war with them. I get the backing of a European power so that if they do attack I’ll have backup, and so things settle into a stable tension. But after several years I get a little too aggressive in expanding influence in Central America, and suddenly the US is joining El Salvador to defend them from me. Because I’m not being attacked, my defensive pact with France won’t hold. Oh, and the USA will demand California as war reparations if they win. In this moment, I have been outplayed by the USA. They had a plan, they waited for the right time, and they responded to my mistake. It’s clear why and how we ended up here. I understand my enemy. I understand what they want, and how they intend to get it. I know who they are. What I can’t understand is why CK3, a game entirely about characters, never gives me anything that feels like this. I never feel like I’m witnessing one of their plans come together. I never even feel like they’re planning. They just…exist. How is it that countries in Vic 3 are able to have more character than the actual characters with extensive personality traits, skills, and relationships in CK3? Why do have to play Vic 3 tiptoeing around Great Britain making sure not to do anything they could make them my enemy, but I don’t have to think twice about seducing the wife of the leader of the HRE in CK3, or killing off my brothers kids?

## Reply 28 — participant_021 · 2025-05-20 · post-30379489

<!-- artifact:quote:start -->
> 47pik said: Between the Conquerer system and now these “hard mode” buffs it really comes off as you not understanding the core issue with the game. It’s not that it’s easy - it’s that it’s boring. All you accomplish by making it “harder” in this way is make it more micro-intense in addition to being boring. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> ourg said: - increase odds for death/injuries, don't let almost all events with a good/safe option. The main issue is that currently all bad events have a safe option. Sometime you shoudl ahve to accept tour fate Click to expand...
<!-- artifact:quote:end -->
I agree but at the same this is literally what big chuncks of the community have directly asked. It is also not a solustion that the designers seem best pleased with based on this wording: "As we’ve said in the past, we want difficulty and challenge to be something that arise organically from how our mechanics interact, and think that giving flat buffs to the AI or penalties to the player for arbitrary reasons isn’t an ideal solution." I think this sounds good in theory but would suck in game we already had the updated that introduced more random death and it was so hated they basically patched it out. DIseases are also the least popular feature according to the community and are very consistently talked about as annoying and not fun. For my money though this is the thing keeping someone alive for a long time is too easy currently but I think that is more of a question of subtle balance than large scale changes.

## Reply 29 — participant_022 · 2025-05-20 · post-30379490

Here are some potential buffs for hard/very hard AI: - Small court grandeur bonus - Slightly improved results from councilor tasks and their efficiency - Slightly increased chance to fabricate claim on entire duchy instead of a county - Slight discount on man at arms recruitment but dont give them a maintenance or power bonus there - Remove the gamerule for AI ship embarkment cost and make that part of the difficulty since you just did that anyway - Increase the amount of murder plots from or against claimants - Find a way to make admin realms less hilariously easy, maybe feudal/tribal vassals under an admin realm should be far more hostile. - Remove the huge penalty to count AI's chances of declearing war, I don't even know why this exists in the game files

## Reply 30 — participant_023 · 2025-05-20 · post-30379493

I will continue on the slight momentum regarding AI. The fact that being able to automate our army is quite nice, but it still suffers from a few issues. I think more options to choose whether the army can take boats or not would be good because I've too often seen my army take a boat to land a few counties away, thus draining our treasury for nothing since they could cross by land without any problems, especially when enemy territories were already occupied. Next, being able to choose if we prefer an offensive or defensive army would be good because I've lost wars when enemies took my capital while my army was besieging a castle a few counties away and wasn't prioritizing saving my domain. And the last point, in case of multiple wars, being able to focus the AI on one war at a time could also be beneficial. Because when you have a war against a land neighbor and another declares war but is on an island, it's annoying to have the army take a castle from one, then take a boat to go to the islands to take a castle, and come back to the continent to resume the fight with the first one. The treasury doesn't really like that.

## Reply 31 — participant_024 · 2025-05-20 · post-30379502

<!-- artifact:quote:start -->
> 47pik said: Making the game harder isn’t the issue. Making the game engaging is. The issue isn’t that the AI needs buffs, the issue is the AI doesn’t do anything meaningful in the first place. It’s very discouraging to see the solution appears to be “hard mode” after all the extensive discussions that are had outlining the problem on this forum. All this accomplishes is making a game with little in the way of emergent storytelling harder (read: more micro-intensive) without making it any more interesting. The problem isn’t that the game is easy. The problem is all the characters are cardboard cutouts who don’t have any agency - they are acted upon, they do not act. Between the Conquerer system and now these “hard mode” buffs it really comes off as you not understanding the core issue with the game. It’s not that it’s easy - it’s that it’s boring. All you accomplish by making it “harder” in this way is make it more micro-intense in addition to being boring. Click to expand...
<!-- artifact:quote:end -->
i think these are separate conversations, the game could use more engagement but also more difficulty having to use more than one brain cell to play this game is always welcome, no anymore do you have to just shut off your brain and dominate the world after snowballing to godhood in a few decades

## Reply 32 — participant_025 · 2025-05-20 · post-30379504

<!-- artifact:quote:start -->
> PDX-Trinexx said: Heavier penalties to arranging marriages based on number of existing alliances Click to expand...
<!-- artifact:quote:end -->
Im worried about this part. It's already quite annoying when Im for example an Emperor and have to marry my children to low nobility because of this "number of alliances" penalty. I usually can't roleplay a policy of marrying my children only to royal families or other imperial families beouse of alliance penalty. The best solution to this problem would be if marriages worked like in Ck2. They should give no effect on their own other than unlocking a diplomatic action to sign non agression pact and alliance. This way a penalty could be applied not to marrying but to turning marriage ties into alliances. For me it's a big problem because it severely breaks immersion when I as a prestigious ruler have to basically marry morganatically because of existing alliances penalty.

## Reply 33 — participant_026 · 2025-05-20 · post-30379508

I beg of you to remove the feudalization block from tribes of the north, it is neither fun nor historical, and it has inconsistent implementation since nomads can still feudalize through other decisions while tribals cannot.

## Reply 34 — participant_027 · 2025-05-20 · post-30379511

I'm going to copy and paste what I posted few minutes ago in a different thread because it seems we're discussing these things here The announced hard/very hard settings don't tackle what makes the game easy and some of the changes don't affect competent players at all: 1) AI vassals are much more likely to raise up in tyranny wars 2) Player has a harder time retracting vassals 3) Player has a harder time revoking titles 4) Factions 1 and 3 - don't change much of anything for competent players, vast majority of the time I revoke a title I want a rebellion to get rid of vassals or fix border gore. Only possible scenario that would make it harder is for players that are not that competent and use cbs that give them vassals instead of land. They might want the land or get rid of vassals from wrong culture/faith then again, a competent player won't have them in the first place using a different cb. So in short it tackles a situation that it's not a problem of the target audience for very hard. 2 - it's more an annoy OCD people that anything else, it doesnt make the game harder to not have clean borders internally. Duke A has 3 counties that he shouldn't have? Game won't be harder, it will annoy me at the most. 4 - factions won't be a problem for competent players ever, opinion modifiers and temporary opinion from activities are far too easy to get and on top of that AI it's weak and can be crushed even if they fire. worst part of a civil war is go vassal by vassal in jail revoking their titles not crush them. Things that can be good: 1) Penalties for knights (I hope this is an effectiveness cap and not something silly like your knights have -400% effectiveness) 2) AI pays less for activities 3) AI has easier time revoking/retracting Things that are core part of "the game it's too easy" that are not tackled: 1) AI build poorly and not frequent enough - which causes an income gap compared to players as the game goes by. not enough money and they can't recruit enough MaA to be a threat. 2) Drain gold events make AI poor - they're a terrible design and should not exist but as it's at the very least they shouldn't fire to AI. 3) Buffs from MaA stationing - no cap/nerf here? so my 2k heavy cav still gonna murder 50k armies? 4) AI struggle super hard to have claims - have you seen 1066 HRE declaring war on France for 1 county? They do it almost every run, makes any sense to you? So idk, a duchy conquest cb for neighboors or something that allows them to declare wars would be nice. 5) overall balances that should be applied to the game independently of difficulty? like seafarer nerf? buildings balance or just remove all the crap ones? landless, admin, steppe balances? because you can add all very hard settings but if something it's beyond broken hard/very hard mode it's a waste of development time and worth only to flex. I conquered the world in very hard mode! I played Temujin or I started as a landless character then swore fealty to Byzantines. Yeah boy, very hard indeed my imaginary cat friend can do that.

## Reply 35 — participant_028 · 2025-05-20 · post-30379522

<!-- artifact:quote:start -->
> PDX-Trinexx said: AI realms are going to be significantly more strong and stable, making the game progress differently Click to expand...
<!-- artifact:quote:end -->
Does this mean that AI tends to blob more on "very hard" difficulty ? Bigger and stronger AI realms ? (but less AI realms as a result?) Any examples in observer mode showing the difference ?

## Reply 36 — participant_026 · 2025-05-20 · post-30379525

Remedying the lack of herd decay Increase the success chance of stealing herd from characters over their herd limit Plague events that kill off herd when not already low (so above 20% of limit) Random migrations taking away your herd and leaving for better pastures if you have low legitimacy and you are either experiencing a plague, over your herd limit or low on fertility Urge the AI to spend their herd when close to limit or when low on fertility Reduce gold gained from herd when above herd limit

## Reply 37 — participant_029 · 2025-05-20 · post-30379526

Way of kings mod(unfortunetly currently dead) has hard, very hardy, even more difficulty options, interesting coincidence

## Reply 38 — participant_030 · 2025-05-20 · post-30379528

<!-- artifact:quote:start -->
> PDX-Trinexx said: I believe that's set as a define and not something we can selectively edit based on game rules, buuuut I can see about bullying someone into changing that. Maybe. No promises. Click to expand...
<!-- artifact:quote:end -->
Yes, please do it. Some players would really enjoy this game rule. Losing is fun if this situation is accompanied by a good story that is generated organically. Being able to be killed by the AI (BTW, this has never happened to me) would be incredibly fun and would generate a desire for revenge and to continue the campaign. Precisely, the lack of difficulty (or rather depth) is what makes it boring to roleplay a CK3 campaign, which is a shame because the game is great and has a lot of potential.

## Reply 39 — participant_031 · 2025-05-20 · post-30379531

My biggest thing with AI is their aggression. I’d like them to be more aggressive with both their conquests and their schemes. If they think they can beat me in war they should try and if they think they can’t they should try and murder me.

## Reply 40 — participant_032 · 2025-05-20 · post-30379532

<!-- artifact:quote:start -->
> Athius said: One thing that would help a lot with difficulty: making alliances more difficult to procure. Right now, any difficult war can be mitigated by marrying a child to the HRE and calling them in. Any strong AI realm can be countered by setting up a bunch of alliances. The CK2 approach where marriage instead granted NAP's would still give them a diplomatic purpose, make diplomacy more interesting and make the game more 'difficult'. Click to expand...
<!-- artifact:quote:end -->
Should also help in making marrying children/dynasty members off less annoying – less chance of getting a stupid ally calling you in for every random war with a count they decide to have. Edit: removed redundancy. I really should stop commenting on these on my phone...

## Reply 41 — participant_033 · 2025-05-20 · post-30379549

sorry if this wrong. but would it be easy to make land be expesive to maintain like military building having up keeping and control beeing like eu5 where it gets lower and lower the fruther away from captital? forcing to have vassals and the like?

## Reply 42 — participant_034 · 2025-05-20 · post-30379558

<!-- artifact:quote:start -->
> PDX-Trinexx said: Hello everyone! I’m Jacob, the Community Manager with Paradox Studio Black. My role within the studio is to strengthen communication between us and you, the players, to ensure that we understand what you want from the game and that you understand what our intentions are for the future. While I’m just one part of the broader Community Team for Crusader Kings, I’m ultimately responsible for nearly every piece of public-facing communication we publish as a studio: dev diaries, feature breakdowns, chapter premiere videos, social media posts, etc. I’m also responsible for the reverse; every piece of feedback that ends up on a designer’s desk goes through me at some point in the process. Today, I’m going to talk about the release of Khans of the Steppe and the feedback we’ve received from players, as well as how we’re addressing it. After that I’ll give a brief overview of how our development cycles work, what the hell Post-Release Support even is, and then cap it off with a quick look at what our next steps are as a studio. I am a map gamer, so fair warning: There will be a good amount of graphs and charts in this dev diary. State of Launch​As you may or may not be aware, Khans of the Steppe and the 1.16 “Chamfron” Update were released on April 28th, and the initial response was fairly positive both from a technical perspective and a player sentiment one. However, we quickly noticed a spike in crash reports and commentary from players confirming this. Setting our lovely QA team to work, we quickly identified two major contributors to instability in 1.16 and pushed hotfixes to tackle both of them. These fixes have led to a significant reduction in crash rates, but we’re still seeing elevated levels, so we’re still working to identify and resolve the causes of these crashes. View attachment 1302669 [Crash rate analytics since the release of Khans of the Steppe. The 1.16.0.2 hotfix (circled in red) made a big difference, but there’s still work to be done.] While there was an immediate spike in negative reviews due to stability issues, the response at large to Khans of the Steppe was quite positive right out of the gate. When you spend months working on a specific project, it’s always an immense relief to see that it went well and players were having fun with the new content, so everyone at the studio was elated at the response! Then the review score started dropping. View attachment 1302670 [Steam reviews for Khans of the Steppe. You can see the ratio of positive to negative reviews shrinking over time; In the “biz”, this is considered a Bad Thing. While the amount of people who leave reviews are a sliver of a fraction of the greater playerbase, this is still a valuable source of information for us.] With all of our releases, we do a series of internal reports on the state of things at predefined intervals. There’s a Day 0 report, Day 1, Day 7, etc. While the Day 0 and Day 1 reports were initially positive, by the end of the week it became clear that there were outstanding problems that took some time to reach a breaking point for players. So, what were those problems? In order to figure that out, we have to do some basic analysis of the reviews themselves. To begin, I took every negative review on Steam and put them into a spreadsheet where they’re arranged, translated (we try to assess feedback from as many languages as we possibly can), and categorized based on what their main complaint is. (This isn’t the only way we analyze feedback, but reviews are fairly easy to explain so they make ideal content for demonstrating the point in this dev diary.) Once everything has been neatly categorized (a task I find immensely soothing, for the record), I can generate a quick chart showing which complaints are dominating the conversation. The main cause of stability complaints in the reviews were already addressed or being investigated, so we can skip that category and take a look at the next one in the list: Balancing. View attachment 1302671 [Outside of stability issues, balancing concerns make up the majority of complaints about Khans of the Steppe.] With my chart prepared, I can go to the design team and our Game Director to tell them “Players think the balancing is wonky, and here’s data to prove it.” From there, we can actually go through feedback to identify specific pain points and begin to address them in our first post-release support update (more on what that specific term means later). If you’re only interested in what’s next for Khans of the Steppe, then I’ll summarize here and save you some time: We know that players have concerns with the DLC and we’re working to address as many of these concerns as we can within the time we have allotted for post-release support before anything else is pushed off to Realm Maintenance. If you want to know more about how our communication pipeline from player to developer works, and how we act on what we hear from you, then read on! I intend to ramble for a bit longer. Player Feedback​In order to properly explain how we turn comments on the internet into changelog entries, I first need to talk about how we collect and parse feedback from all of our supported platforms. Pre-Release Feedback​Our handling of player feedback for Khans of the Steppe started quite a while back, before the announcement of Chapter 4 in fact. Our preview dev diary back in February was published so far ahead of the normal schedule specifically so that we could gather information about player desires and expectations regarding a Nomad-focused DLC. The feedback we received from that DD is directly responsible for a variety of changes that made it into the release version of Khans of the Steppe, such as expanding the new Nomadic government type to certain non-steppe regions. Additionally, we run a persistent closed beta program of roughly 100 people from our community. This includes members of various high-profile mod teams, historians, members of the community with a history of sending detailed and actionable feedback, and a small pile of content creators. The point of this program is to get direct player feedback on upcoming content as early into the development process of an update as we can (For Khans of the Steppe, this began roughly a year ago). As development progresses, more of the design is solidified and becomes more difficult to change in response to feedback, so this program is considered vital to us. Once the development version has progressed far enough that we’re able to announce it publicly, we begin a fresh dev diary cycle. These serve to inform the playerbase of what we’re working on while giving us a chance to get broader opinions and suggestions about the upcoming content. Our companion videos that are released on our YouTube channel are also helpful here, since viewer retention stats can inform us which sections within a given dev diary are of particular interest to viewers. View attachment 1302672 [Retention graph for Dev Diary 166; the bump at the 11 minute mark shows that viewers were particularly interested in the “Blessings of the Blue Sky” segment] Finally, in the last month or so before releasing Khans of the Steppe, we ran a separate preview group to get a final round of feedback. This is essentially a time-limited version of our persistent beta, and has a similar selection criteria for participation. During this stage, we essentially throw the flood gates open and pull in as many people as we think we can manage while maintaining some semblance of operational security. Mod team representation increases dramatically during this stage in order to give them a head start on compatibility patching their mods, and any content creator too slow to outrun our Influencer Relations Manager is also pulled into this time-limited program. Before you ask: Yes, that youtuber you’re thinking of is in this program. Yes, that one is too. Yes, them as well. View attachment 1302673 [A snippet from the aforementioned preview group. Yes, we run this through Discord.] The goal here is to make sure that the content we’re working on matches the expectations of our players as closely as possible ahead of release; the persistent beta program allows us to do this in broader strokes while the DLC is still taking shape, and the preview program allows us to catch more issues that would have slipped through the net (as well as giving us a head start on our first post-release support update). Post-Release Feedback​That’s all well and good, but what do we do about feedback after something is released? After a major release, gathering immediate feedback from players is crucial to ensure that any critical issues that made it through testing phases are swiftly handled, and that our post-release support cycle is focused on addressing player pain points with the new content. We actively collect this feedback from a wide variety of places; our own forums, Facebook, Steam, YouTube, Twitter, Reddit, Discord, QQ Guild, Bilibili, Tieba, among others. Essentially, if it’s posted on a publicly visible platform, odds are that we’re going to see it one way or another. View attachment 1302674 [The pc-feedback channel on our official Discord server is one of several “primary” feedback channels we use. Voting systems make it easier to tell at a glance which posts are more important to the community there. Sadly, Reddit votes aren’t as useful for this purpose.] To facilitate the collection of this amount of information, we have a set of Community Ambassadors (or “CAs”) who act as additional support for the bridge between our players and the development team. One of the main responsibilities of our CAs revolves around collecting player sentiment and feedback, monitoring discussions, and identifying pressing issues that players report post-release. You’ve said it? They’ve probably read it. They help cast the net as far as possible to ensure no significant feedback slips through. After a major release drops, they immediately begin scouring for reactions then compile them into a detailed Day 1 post-release report for the studio. View attachment 1302675 [A snippet from the Day 1 report for Khans of the Steppe. These initial reports are crucial for identifying standout issues that need to be handled as soon as possible] They condense hundreds of discussion threads, suggestions, and reports into a more digestible format to quickly identify what the community finds most pressing. As you can see above, crashing was the most prevalent issue highlighted in the Day 1 report, while balance issues weren’t widely reported until after the Day 1 report period. Feedback gathered this way is used to determine what the priorities of the development team should be during the post-release cycle, which finally brings us to the namesake of this dev diary… Post-Release Support​Our studio is structured into various internal teams, with each one focusing on specific updates or expansions. We have a team for Khans of the Steppe, All Under Heaven, Coronations, and others we can’t discuss quite yet. Post-Release Support (PRS) is the final stage of development for a Major Update before the team assigned to that update is dissolved and its members moved to other teams within the studio. The main objective of the PRS stage is to address any outstanding issue that may have slipped through the pre-development cycle. This includes fixing bugs, tweaking gameplay balances, and implementing various improvements or alterations to systems based on player feedback. The goal is to essentially “finalize” the DLC, but this doesn’t mean we cease work on the DLC outright. Any further updates or fixes that aren’t able to be implemented during the PRS stage go towards Realm Maintenance to be integrated into future updates rather than having their own dedicated release. During a PRS stage, we step up our Quality Assurance (QA) efforts by bringing in additional specialists to assist with PRS. These specialists work closely with the development team to review bug reports and ensure that as many reported issues as possible are investigated, identified, and assigned to a member of the development team to be addressed. If you’re reporting bugs on our official forums during a PRS stage, these are the people replying to and tagging your posts. View attachment 1302676 [As an aside, the tags are there to signal to other members of the team that a post has been looked at; this reduces the chances of us wasting time by going over threads that are already being handled.] Another important aspect of the PRS stage is taking care of issues that were “locked out” of the initial release for one reason or another. Two of the main reasons this could happen are feature freeze and loc freeze. During feature freeze, no new mechanics can be added to a DLC; anything that needs to be tacked on after feature freeze must target a future update. Similarly, a loc freeze means that no new player-facing text can be added, as localization into all of our supported languages takes a significant amount of time; any content that requires new or updated text after localization freeze must be scheduled for a future update. While these freezes mean that our response to feedback can sometimes be delayed, they ultimately help ensure that updates actually release when they’re intended to. In most cases, the aforementioned future update will be one of the “point releases” during PRS. Each PRS stage typically has time allocated for two or three of these updates, with the expectation that we’ll need them to tackle issues that cropped up after feature/loc freeze or issues reported by the community. Additionally, we allocate time for hotfixes as necessary to allow emergency updates. View attachment 1302677 [It’s a bit messy to look at, but you can see here how certain commits by the development team are sent to different branches depending on their contents. We have a lot of internal development branches.] Post-Release Support is an essential part of the development cycle in that it allows us to address player feedback as it’s submitted to us, but also to set the stage for future development by giving us a stronger idea of what players expect and want from the game. Next Steps​So, what has the feedback we’ve gotten since Khans of the Steppe been about, and what do players want from the game? Mainly, that the balancing is wonky and that our more dedicated players want the game to be harder. We’ve released Update 1.16.1 and 1.16.2 already to tackle the former, and I’ve been working directly with our Game Director to implement something to help us address the latter; this will take the form of Hard and Very Hard difficulty modes releasing alongside Update 1.16.2.1 sometime later this week. View attachment 1302678 [Highly experimental! Mostly untested! Probably imbalanced! Try it out later this week and tell us what you think.] As we’ve said in the past, we want difficulty and challenge to be something that arise organically from how our mechanics interact, and think that giving flat buffs to the AI or penalties to the player for arbitrary reasons isn’t an ideal solution. That said, our community has made it clear that we’re not meeting our objective, and doing something is better than doing nothing. So while we intend to continue pursuing our goal of emergent challenge in the long term, we’re introducing these new difficulties for players who want the game to be harder right now. View attachment 1302679 [A small collection of some of the bonuses AI characters will receive in Hard/Very Hard difficulties.] We’ve also heard quite a few people asking for a passive herd decay mechanic. To go ahead and rip the bandaid off: We’re not planning on implementing this. Put simply, the system wasn’t designed with this in mind and is instead built around discrete reductions. Too much of the game goes off the rails when it tries to deduct what doesn’t exist, and herd decay ultimately impacts AI rulers far more than it impacts players (compounding balance/difficulty concerns). With the PRS stage for Khans of the Steppe coming to an end, we don’t have the time or resources available to rework a core aspect of the DLC to this degree. Additional adjustments to this system are still possible in Realm Maintenance updates, but these are unlikely to fundamentally rework the system itself. Aside from that, we’ve heard we still have bugs to squash! AI asking you for paizas should be significantly reduced in the next update, the steppe region map mode should be properly colored in again, etc etc etc. We’ll have a full changelog of what’s been fixed releasing alongside the update itself later this week. After that, we’ll have a period of relative stability where mod authors can update their mods and players can finish a longer campaign without worrying about another update dropping and causing them grief. We’ll still be working on bugs and other issues that get reported (or already have been), but they’ll be packaged up alongside the release of our next piece of Chapter IV. While this is far from a comprehensive overview of development cycles, post-release support, or even feedback loops, I hope this gives you a stronger understanding of how these systems work at a glance. I’m always happy to talk at length about damn near anything involving Studio Black (as anyone subjected to one of my rants on our Discord can attest), so if you have any specifics you’d like to know more about then feel free to drop a comment and I’ll answer them as best I can! That’s all we have for this week, but be sure to come back next Tuesday; we’ll be talking about the design vision for a small piece of content we’re working on called All Under Heaven. Click to expand...
<!-- artifact:quote:end -->
Whether it can increase the influence of weather on nomadic regime, in ancient East Asia, when nomadic regime showed strong aggression and aggressiveness, it was often that grasslands suffered serious disasters, and nomadic tribes would choose bloody looting of agricultural countries, while in the absence of serious meteorological disasters, nomadic tribes with little pressure to survive tended to prefer bloodless trade activities.Of course, I don't know whether nomadic tribes in Europe and Central Asia are like this. The reason why I put forward this opinion is because I feel that the weather system in the game is too weak for nomadic tribes

## Reply 43 — participant_035 · 2025-05-20 · post-30379575

That massive wall of text and long words about quality control. And yet not a single mention of pillaging system. So all of your testers(bot paid and beta)played nomads, and were like "Yeah, this is ok". Not a single one of them said something to the effect of "I don't think clicking every single holding manually, then keeping it, and clicking it again years after, is a good idea".

## Reply 44 — participant_036 · 2025-05-20 · post-30379603

While I agree that mechanical bonuses to the AI isn't an ideal solution for difficulty, having the option for it is still much better than not having the option. As someone who would like CK3 to be more challenging, I really appreciate the addition of harder difficulties.

## Reply 45 — participant_037 · 2025-05-20 · post-30379604

That was an interesting read! Can you share what you know, do other PDS teams / titles have similar process and staffing? Are there PDS-level standards of QA, and metrics to check whether these standards are upheld? An unrelated question: why does playerless simulation play so seemingly little role in QA? It looks like in Grand Strategy (where thorough regression testing can not possibly cover all bases) it would be worth it to run a thousand simulation and look at the share of games where certain facts happened (e.g. HRE formed), so that if some of the percentage is wonky (HRE forms only in 0.8% of runs; HRE forms in 99.7% or runs) you would know where to dig.

## Reply 46 — participant_038 · 2025-05-20 · post-30379606

Couple suggestions for new difficulty levels: Teach AI to detect situations when the player or other AI tries to matri-/patrilenally marry their kids to second, third, ..., nth heirs and then kill older heirs. AI should either reject such marriages or keep an eye on older children's safety. For example, this will make "A.E.I.O.U. and Me" achievement really hard to unlock. This ability should depend on AI's own, spouse's and council's intrigue skills and past experience. Teach AI to trick players into such marriages. I don't play normal games much after new schemes were released, mostly as overpowered character, but if murder events such as getting carpet or poisoned gold still exist (I saw a character having "Not feeling well" modifier yesterday) then they should be disguised as normal gift events, for example, a carpet given by Persian ruler can be absolutely harmless. Changing faith should involve pilgrimages to new faith's holy sites before converting, raising questions. Imagine your Archbishop sending a letter to Pope with suspicions about your weird behavior.

## Reply 47 — participant_027 · 2025-05-20 · post-30379611

<!-- artifact:quote:start -->
> Willy Waggler said: That massive wall of text and long words about quality control. And yet not a single mention of pillaging system. So all of your testers(bot paid and beta)played nomads, and were like "Yeah, this is ok". Not a single one of them said something to the effect of "I don't think clicking every single holding manually, then keeping it, and clicking it again years after, is a good idea". Click to expand...
<!-- artifact:quote:end -->
They probably done that so if a player lose their domain to nomads it doesnt get grazed right away

## Reply 48 — participant_039 · 2025-05-20 · post-30379615

It's encouraging to see that difficulty concerns are being taken seriously with the new hard mode...but I do still think there are changes that can be made that would increase difficulty (mostly by hindering rapid player expansion) without needing to either introduce arbitrary AI bonuses or re-configure entire systems from the ground up. Eg: - marriages only grant non-aggression pacts, not alliances; defensive alliances must be negotiated, and offensive alliances require hooks or quid-pro-quos. - escalating opinion maluses with lieges and peer vassals accompanying a character's rise in status (maybe 'up-jumped count/duke/adventurer', 'jealousy', or something like that, which would be even more severe for ambitious/paranoid AIs, and possibly mitigated by the 'Administrator' trait). - Relevant vassals can be called as allies in defensive wars. - Pending a re-configuring of the MAA system or an update that enables the AI to station them effectively, allowing building bonuses to apply universally to AI MAA. - Local lower-level office holders and unlanded imperial councilors/court position holders at the emperor's court/noble family heads are automatically placed in the line of succession for administrative governorships. - making dread impact players by causing stress whenever you make your character act against someone they are afraid of. - More nerfing of strategies that only players use, such as eugenic marriages, bringing in talented knights/courtiers through matrilineal marriages to existing courtiers, etc.

## Reply 49 — participant_002 · 2025-05-20 · post-30379645

<!-- artifact:quote:start -->
> tribnia said: Any spoiler for you-know-what? It's just hard to wait until next Tuesday. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> yurcick said: An unrelated question: why does playerless simulation play so seemingly little role in QA? It looks like in Grand Strategy (where thorough regression testing can not possibly cover all bases) it would be worth it to run a thousand simulation and look at the share of games where certain facts happened (e.g. HRE formed), so that if some of the percentage is wonky (HRE forms only in 0.8% of runs; HRE forms in 99.7% or runs) you would know where to dig. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> pbw-410 said: It's encouraging to see that difficulty concerns are being taken seriously with the new hard mode...but I do still think there are changes that can be made that would increase difficulty (mostly by hindering rapid player expansion) without needing to either introduce arbitrary AI bonuses or re-configure entire systems from the ground up. Eg: - marriages only grant non-aggression pacts, not alliances; defensive alliances must be negotiated, and offensive alliances require hooks or quid-pro-quos. - escalating opinion maluses with lieges and peer vassals accompanying a character's rise in status (maybe 'up-jumped count/duke/adventurer', 'jealousy', or something like that, which would be even more severe for ambitious/paranoid AIs, and possibly mitigated by the 'Administrator' trait). - Relevant vassals can be called as allies in defensive wars. - Pending a re-configuring of the MAA system or an update that enables the AI to station them effectively, allowing building bonuses to apply universally to AI MAA. - Local lower-level office holders and unlanded imperial councilors/court position holders at the emperor's court/noble family heads are automatically placed in the line of succession for administrative governorships. - making dread impact players by causing stress whenever you make your character act against someone they are afraid of. - More nerfing of strategies that only players use, such as eugenic marriages, bringing in talented knights/courtiers through matrilineal marriages to existing courtiers, etc. Click to expand...
<!-- artifact:quote:end -->
We'll give a brief overview of the major features and mechanics, but won't give any crunchy/detailed information on said mechanics until their own dedicated dev diaries. We do exactly that! We run overnight simulations on a regular basis during development and graph the data from them to help us approximate the likelihood of certain outcomes. Broadly speaking, those are the kind of changes that are out of scope for a PRS update like the one being discussed here. Only reason we were able to justify what we've done outside of the normal development cycle is because it's a self-contained gamerule and has minimal odds of messing things up in Unforeseen Ways. Regardless, it'll be a while before our QA team forgives me for my role in this going out during PRS.

## Reply 50 — participant_040 · 2025-05-20 · post-30379651

<!-- artifact:quote:start -->
> PDX-Trinexx said: I believe that's set as a define and not something we can selectively edit based on game rules, buuuut I can see about bullying someone into changing that. Maybe. No promises. Click to expand...
<!-- artifact:quote:end -->
I will take it!

## Reply 51 — participant_010 · 2025-05-20 · post-30379660

<!-- artifact:quote:start -->
> qiukeshan said: Whether it can increase the influence of weather on nomadic regime, in ancient East Asia, when nomadic regime showed strong aggression and aggressiveness, it was often that grasslands suffered serious disasters, and nomadic tribes would choose bloody looting of agricultural countries, while in the absence of serious meteorological disasters, nomadic tribes with little pressure to survive tended to prefer bloodless trade activities.Of course, I don't know whether nomadic tribes in Europe and Central Asia are like this. The reason why I put forward this opinion is because I feel that the weather system in the game is too weak for nomadic tribes Click to expand...
<!-- artifact:quote:end -->
We could get something like this with dynastic cycles in all under heaven tbh. Because as far as I know the nomads situation also had to do with the ruling chinese dynasty. If the chinese dynasty is a native one and strong empire it in turn created a strong nomadic ruler to the north through expanded trade and gifts. If the chinese dynasty weakens and cannot provide trade or gifts the nomadic empire also weakens economically. When this happens the nomads descend from manchuria and become the ruling chinese dynasty through conquest. Because the dynasty is of nomadic origin it continues to fight and dissolve the remaining nomads. After some generations the chinese rise up and remove the nomadic-origin dynasty. The native empire again becomes strong and establishes diplomatic relations with the nomads creating a stable nomadic empire. Until the dynasty weakens... Idk how exactly accurate it is historically but it's a theory that the 2500 year chinese history has this cycle of interaction with the nomads. Theres a book on it called The Perilous Frontier. Just sounded pretty similar to the dynastic cycle mechanic they talked about in the chapter 4 reveal

## Reply 52 — participant_039 · 2025-05-20 · post-30379674

<!-- artifact:quote:start -->
> PDX-Trinexx said: We'll give a brief overview of the major features and mechanics, but won't give any crunchy/detailed information on said mechanics until their own dedicated dev diaries. We do exactly that! We run overnight simulations on a regular basis during development and graph the data from them to help us approximate the likelihood of certain outcomes. Broadly speaking, those are the kind of changes that are out of scope for a PRS update like the one being discussed here. Only reason we were able to justify what we've done outside of the normal development cycle is because it's a self-contained gamerule and has minimal odds of messing things up in Unforeseen Ways. Regardless, it'll be a while before our QA team forgives me for my role in this going out during PRS. Click to expand...
<!-- artifact:quote:end -->
Cool, thanks for the feedback!

## Reply 53 — participant_041 · 2025-05-20 · post-30379682

I was really expecting to get information on the turks and magyars. It even appears on the chart! Decisions and flavour not working or fitting properly, lack of general content, taltoism not being a steppe religion... Any thoughts or plans? Thanks!

## Reply 54 — participant_042 · 2025-05-20 · post-30379683

It seems like a good process, thanks for sharing the details of it. Could you clarify whether Realm Maintenance is a permanent team or an occasional development period? There seems to be some confusion about that and I would like to be able to point people to a statement clarifying that.

## Reply 55 — participant_028 · 2025-05-20 · post-30379689

Also wondering whether an equivalent of 'obfusckate' mod could be integrated as an optional game rule (and/or part of higher difficulty levels). A lot of us don't want to play without it and have to wait for the mod to update before being able to play on a new version of the game properly...

## Reply 56 — participant_038 · 2025-05-20 · post-30379724

And other suggestion. Instead of "Hard" and "Very Hard" levels make two rule categories (after you reorganize the rule window of course): "Roleplay" section with rules like: Hide (or Show) event results. Options: Yes | No Hide (or Show) character info. Options: All | Unknown | None Hide (or Show) portraits of unknown characters. Options: Yes | No (EDIT) Or better than above: Portrait type of unknown characters. Options: Normal (Full 3D) | Painting (Using legends shader) | No portrait Remove Medieval matching app (all marriages only using portraits, by visiting or blindly, depending on culture or faith). Options: Yes | No Hide (or Show) factions (should not affect Spy mechanic). Options: All | Small (or Big) | None Hide (or Show) faction members (should not affect Spy mechanic). Options: All | With High (or Low) Intrigue | None etc. "AI Buff/Player Debuff" section with rules which simply change numbers.

## Reply 57 — participant_002 · 2025-05-20 · post-30379744

<!-- artifact:quote:start -->
> JonZone said: View attachment 1302728 I will take it! Click to expand...
<!-- artifact:quote:end -->
The contract is sealed.

## Reply 58 — participant_043 · 2025-05-20 · post-30379777

Not being able to reduce herd size massively seems like an issue in core game design that wasn't pointed out by people early enough. It's a shame the mechanic won't be redesigned.

## Reply 59 — participant_044 · 2025-05-20 · post-30379783

Mostly agree with comments in this DD about what the game needs to be more difficult but i have to add what would made the game more engaging for me. Just repeating some suggestions from myself but again : • Hide information/resources from player about other AI or other players (Hide their gold, influence, herd, army numbers, relationships unless spied/schemed or having a relationship with them). • More historical invasions like for example : Knut (North Sea Empire) or others… • Micromanage wars day by day with mechanics like “traps” or “climate” during battles. • Adding complex mechanics like Banking (Something like from AGOT maybe) or trade if it is made in the future, so that players have bigger challenges in specific mechanics of the game. • Adding a slavery mechanic so that players get more punished with its unique mechanics, mainly if they are landless. • Adding traits or reworking existing ones that forces the player to focus in other mechanics of the game rather then just conquering everything and painting the map. But first some mechanics really needs to get more deep seriously. • Use the lack of knowledge or hability of the player against them, like for example : if you are landless and you don’t know the language of other culture or you don’t have something like a “translator” when you accept contracts of another part of the world, make the contract be in that different cultures language so that the player has to learn the language in real life or in the game, or hire a “translator” in game… • Tie gold/prestige/army/herd/influence and etc together and make it so losing one affects the other. Make it so losing your soldiers/army really hurts the player, not just hire or wait the numbers recover like nothing happened. For now i can think of only that. But i think the game is going to the right way. My honest opinion is that it is better when you use the players individual limit of information or hability against them then just buffing or nerfing the AI, tho i don’t dislike that, i think people adapt more easily to external challenges then internal ones specially through repetitive action it is only a matter of time until players find the weaknesses in “hard” or “very hard” mode. Anyway, good work.

## Reply 60 — participant_011 · 2025-05-20 · post-30379794

<!-- artifact:quote:start -->
> giorgosth128 said: sorry if this wrong. but would it be easy to make land be expesive to maintain like military building having up keeping and control beeing like eu5 where it gets lower and lower the fruther away from captital? forcing to have vassals and the like? Click to expand...
<!-- artifact:quote:end -->
Guess who will struggle more with those systems, the player or the AI?

## Reply 61 — participant_034 · 2025-05-20 · post-30379812

<!-- artifact:quote:start -->
> Zifircin said: We could get something like this with dynastic cycles in all under heaven tbh. Because as far as I know the nomads situation also had to do with the ruling chinese dynasty. If the chinese dynasty is a native one and strong empire it in turn created a strong nomadic ruler to the north through expanded trade and gifts. If the chinese dynasty weakens and cannot provide trade or gifts the nomadic empire also weakens economically. When this happens the nomads descend from manchuria and become the ruling chinese dynasty through conquest. Because the dynasty is of nomadic origin it continues to fight and dissolve the remaining nomads. After some generations the chinese rise up and remove the nomadic-origin dynasty. The native empire again becomes strong and establishes diplomatic relations with the nomads creating a stable nomadic empire. Until the dynasty weakens... Idk how exactly accurate it is historically but it's a theory that the 2500 year chinese history has this cycle of interaction with the nomads. Theres a book on it called The Perilous Frontier. Just sounded pretty similar to the dynastic cycle mechanic they talked about in the chapter 4 reveal Click to expand...
<!-- artifact:quote:end -->
There are right and wrong, as you said, the ancient Chinese dynasty was at its peak - weakened - nomadic invasion established a new dynasty - the ruling Chinese overthrew the nomadic dynasty - And so on and so forth But in fact, there was only one nomadic conquest of China in ancient China, that is, the Mongols, and the Manchus actually belonged to the fishing and hunting people. The Mongols and Manchus completely conquered China and ruled for about 400 years In the rest of the period, there was a brief era of confrontation between China and the nomadic north and south, and there was also an era when the nomadic occupied part of China's core territory. But in general, from the time of 220 BC, the first centralized Qin dynasty in China, Qin, Han, Sui, Tang, Ming, Yuan, These major dynasties were destroyed by the peasant uprising, ancient China was a typical agricultural civilization, a large number of people relied on the land to survive, when the land was annexed, the peasants lost their land or suffered from the Yellow River bursting, drought and flood and could not survive, the country's ruling class could not guarantee the survival of tens of millions of peasants, the peasants would gather and declare that the current dynasty had lost the Mandate of Heaven, and then a rebellion with millions to tens of millions of casualties broke out, and finally the victor would declare himself the new Chinese emperor, and the victor might be the former peasants, Or maybe it was a bureaucrat or a general of the former empire But regardless of the outcome, starting with the Qin Dynasty in 220 BC, only a few hundred years were due to the collapse of the dynasty caused by nomadic invasions, and the collapse of most of the rest of the Chinese dynasties was a great peasant revolt that broke out after the class contradictions could not be reconciled (the Ming Dynasty was replaced by the Qing Dynasty established by the Manchus, but in fact the Ming Dynasty was the capital attacked by the peasant army, and the subsequent peasant army failed to defeat the Manchu cavalry, so the Manchus established the Qing Dynasty, and the final victors this time were no longer peasants or bureaucratic generals of the old empire, but Manchus who fished and hunted )

## Reply 62 — participant_045 · 2025-05-20 · post-30379830

Really hope these stability / crash issues will be resolved soon. My Windows 11 pc often crashes multiple times in a couple hours, forcing me to shut it down with on / off button. Quite frustrating, especially since I am actively modding for the LOTR Realms in Exile mod, slowing down my progress.

## Reply 63 — participant_046 · 2025-05-20 · post-30379833

Am I the only one who do not want more stability but more ways how AI and player realms can crush?

## Reply 64 — participant_047 · 2025-05-20 · post-30379850

I appreciate the fact that we're getting more difficulty options, even if it is admittedly a small bandage to crunchier features that I'm hoping we can get down the road (aggressive expansion penalties, nerfing alliances to non-aggression pacts, councils actually mattering, more personality- and rank- driven plots against the player, etc). The bandage is a good first step, be we need the follow-up comprehensive treatment too!

## Reply 65 — participant_048 · 2025-05-20 · post-30379862

<!-- artifact:quote:start -->
> Andrzej2 said: Im worried about this part. It's already quite annoying when Im for example an Emperor and have to marry my children to low nobility because of this "number of alliances" penalty. I usually can't roleplay a policy of marrying my children only to royal families or other imperial families beouse of alliance penalty. The best solution to this problem would be if marriages worked like in Ck2. They should give no effect on their own other than unlocking a diplomatic action to sign non agression pact and alliance. This way a penalty could be applied not to marrying but to turning marriage ties into alliances. For me it's a big problem because it severely breaks immersion when I as a prestigious ruler have to basically marry morganatically because of existing alliances penalty. Click to expand...
<!-- artifact:quote:end -->
I like that. When I marry my kids off, I like to marry the girls off to at least the heirs to titles, doesn't always work out but I try. Boy's I try to marry off to landed females. Again, doesn't always work out. But I don't do this for alliances. I hate being dragged into other peoples' wars, and I don't like to go on conquering sprees either. Making marriages work like they did in CK2 would be perfect for a player like me...

## Reply 66 — participant_049 · 2025-05-20 · post-30379886

<!-- artifact:quote:start -->
> PDX-Trinexx said: Mainly, that the balancing is wonky and that our more dedicated players want the game to be harder. We’ve released Update 1.16.1 and 1.16.2 already to tackle the former, and I’ve been working directly with our Game Director to implement something to help us address the latter; this will take the form of Hard and Very Hard difficulty modes releasing alongside Update 1.16.2.1 sometime later this week. [Highly experimental! Mostly untested! Probably imbalanced! Try it out later this week and tell us what you think.] Click to expand...
<!-- artifact:quote:end -->
Thank you! Yes, 'ideally' the game would offer challenge organically but even Civ, the most prestigious strategy series out there, makes heavy use of difficulty options to give experienced players something to do. It is just unavoidable in strategy games until we manage to get 'real' AI in games, no matter how much a certain crowd on the forum will complain. If you are one of those feel free to give us examples of strategy games that doesn't use "artificial difficulty" for difficulty options, because I sure have never played one. (but it is obviously not an excuse to stop working on making the AI better).

## Reply 67 — participant_050 · 2025-05-20 · post-30379888

Thanks for this update and the continued efforst to find a fix for the crashes.

## Reply 68 — participant_009 · 2025-05-20 · post-30379912

<!-- artifact:quote:start -->
> fodazd said: While I agree that mechanical bonuses to the AI isn't an ideal solution for difficulty, having the option for it is still much better than not having the option. As someone who would like CK3 to be more challenging, I really appreciate the addition of harder difficulties. Click to expand...
<!-- artifact:quote:end -->
Disagree - more difficulty modes = more work balancing. This makes the core issue worse.

## Reply 69 — participant_051 · 2025-05-20 · post-30379913

Could we also have an option at the start during character creation to create our own culture and religion? That would be great. Thank you.

## Reply 70 — participant_052 · 2025-05-20 · post-30379920

Please consider dramatically limiting the diplo range for lower tier rulers. The fact that a nobody Count in southern France can ally a duke halfway across Europe in eastern Poland in the 800s massively messes with the balance. It immunizes the player from ever having any threats because of how the AI calculates whether or not they are willing to go to war with the player. I strongly feel that earlier in the game and especially at lower lord ranks we should only be able to marry/ally our very near neighbors. It forces the player to learn the people around him and care more about not making them angry. It would also be a way to increase the difficulty by not allowing the player to artificially boost his total levy numbers (and thus convincing other AI not to invade him) by leeching off of some lord half a world away. Being a one count minor should have more existential danger. Currently, it doesn't. The ability to summon thousands of men from all across Europe should be limited to only the highest lord tiers, especially in the 9th century.

## Reply 71 — participant_009 · 2025-05-20 · post-30379929

<!-- artifact:quote:start -->
> Kainser said: Thank you! Yes, 'ideally' the game would offer challenge organically but even Civ, the most prestigious strategy series out there, makes heavy use of difficulty options to give experienced players something to do. It is just unavoidable in strategy games until we manage to get 'real' AI in games, no matter how much a certain crowd on the forum will complain. If you are one of those feel free to give us examples of strategy games that doesn't use "artificial difficulty" for difficulty options, because I sure have never played one. (but it is obviously not an excuse to stop working on making the AI better). Click to expand...
<!-- artifact:quote:end -->
I would sincerely hope the bar is significantly higher than Civ, of all things

## Reply 72 — participant_053 · 2025-05-20 · post-30379953

My main problems with ck3 are 3: 1- Balance: I won't repeat myself; there are many comments on this forum and elsewhere explaining why this or that is overpowered or overnerfed. Everyone has a different opinion, and ultimately, it's impossible to tailor a build to each player. This can be fine-tuned with patches. Examples of things that are unbalanced in my opinion: Marriages, bonuses, penalties, maa,etc. 2-Replace mechanics with bonuses/maluses: I think the clearest example to talk about this is eu5. I'm sure there will be bonuses and penalties, but most of them are mechanics. You have artists, trade, economics, etc. And this is what ck3 doesn't have. I understand you want this game to be accessible, but you don't have laws that make us understand that our economy and kingdom evolve or degrade over time. There's no trade (yet), no food system, etc. I could be a bit of a hater, but you're showing me you can do it incredibly well. With Khans of the Steppe, you've managed to make me enjoy herding my flock after 1,000 hours of playing the game, give me an imperial objective (becoming a great khan), provide interesting repercussions and rivals, and include a basic fertility system that makes me make decisions, enjoy my game, analyze other things. This is a great strategy, we know you want this to be a more accessible game, that there are no pops, etc. but I think that making mechanics easy to understand and difficult to master can make the game much more attractive. 3- Lack of consistency and repercussions: I've said this in many posts and I'll keep saying it: there are dynamic moments that happen that have no response, which makes you disconnect from the game very quickly. Someone kills the pope, nothing happens, there will be no repercussions. The king is a murderer, he's excommunicated, he's killed his cousins, it doesn't matter, everything's fine, why should we get angry... Three of your five powerful vassals have the attitude of fanatics, it doesn't matter either, they will never pressure you to do this or that. And I could give many more examples. Observations: 1- It can be adjusted with different patches 2- Upcoming patches and dlc can improve the game incredibly in many other ways 3- This is where I see the most problems. We could obviously see improvements in the future, but I think the optimal solution is to simulate what EU5 seems likely to do and create temporary international situations. I realize that you can't trigger everything, and that there's a lot of debate about whether to follow the historical path or allow alternative games, but there are situations where both methods have to have repercussions. A) If someone attacks, kills, or kidnaps the leader of the religion, this must trigger a situation in which the rulers of that faith react in some way. B) If your ruler does their job very poorly and/or is a person who goes deeply against the values of that religion, the vassals must align themselves and a reaction must arise. I've mentioned this several times, but I think it would be very interesting to introduce a faction loyal to the crown. Let's take the example of Kingdom Come Deliverance 2. Let's imagine there's a king who doesn't know how to govern and doesn't care about anything. It's fine for the vassals to want to place another relative on the throne, but a resistance faction must also emerge that wants to keep the current king. C) Please add interregnums. I think coronations are perfect for something like this. Until a king is crowned or approved by the council, the tribe (each culture here has its own way of considering their ruler valid) has to create an interregnum situation, which can provide a lot of play and make the games more realistic. I think this would be the perfect time for the different neighboring rulers to support one side or the other. Thank you very much for everything. I hope my comments are interpreted as constructive criticism.

## Reply 73 — participant_054 · 2025-05-20 · post-30379963

Thanks for sharing the details of the process.

## Reply 74 — participant_055 · 2025-05-20 · post-30379981

<!-- artifact:quote:start -->
> PDX-Trinexx said: Sure. Might as well put it all on the table; here's the difficulty option section from the upcoming changelog. Click to expand...
<!-- artifact:quote:end -->
Could you also add making strong-alliance marriages harder to get on Very Hard? That's one of the reasons the game is so easy now: just marry the three most powerful families you can, and bingo - no one can touch you.

## Reply 75 — participant_056 · 2025-05-20 · post-30380021

I'm a little bit concerned over the size of the dev team and what percentage of the team works from home. I feel as though larger dev teams with a significant number of devs working from home is hurting collaboration over new features. For example, in Khans of the Steppe there was a raid intent that was supposed to give double herd gain, but it was coded to give 4x the herd gain instead on release, which made raiding for herd incredibly overpowered. It was eventually fixed in a post release patch but that still leaves the question how this was overlooked in the first place. I can totally see a dev working from home testing various values in the code, settling on a 2x value but forgetting to go back into the code to change it, and since he is working from home there is no one else to provide a second pair of eyes to catch the mistake. All of this is just speculation on my part, but I do persistently worry that this is a factor in harming the quality of new content and worsening blunders such as balancing in Khans of the Steppe or the marketing disaster that was Legends of the Dead.

## Reply 76 — participant_027 · 2025-05-20 · post-30380022

<!-- artifact:quote:start -->
> bretjemaine said: Could you also add making strong-alliance marriages harder to get on Very Hard? That's one of the reasons the game is so easy now: just marry the three most powerful families you can, and bingo - no one can touch you. Click to expand...
<!-- artifact:quote:end -->
from the post you quoted: Heavier penalties to arranging marriages based on number of existing alliances, lesser bonuses from desires alliance, etc. The player should be able to have one significant alliance, and one minor alliance. Gaining alliances at war will be almost impossible. Everything from hard, but the penalties are greater

## Reply 77 — participant_049 · 2025-05-20 · post-30380023

<!-- artifact:quote:start -->
> 47pik said: Disagree - more difficulty modes = more work balancing. This makes the core issue worse. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> 47pik said: I would sincerely hope the bar is significantly higher than Civ, of all things Click to expand...
<!-- artifact:quote:end -->
what is your opinion of Civilization, which last I checked had 8 difficulty levels? So which other strategy games doesn't have diffiulty levels with AI cheats? I'm all ears. All other paradox games certainly handles it that way. Playing on higher difficulties is considered completely normal in Stellaris yet people here consider them being added a slap in the face. Paradox gamers thinking they are too good for the single biggest strategy game in the world is pretty funny either way.

## Reply 78 — participant_011 · 2025-05-20 · post-30380051

<!-- artifact:quote:start -->
> bfunk86 said: Please consider dramatically limiting the diplo range for lower tier rulers. The fact that a nobody Count in southern France can ally a duke halfway across Europe in eastern Poland in the 800s massively messes with the balance. It immunizes the player from ever having any threats because of how the AI calculates whether or not they are willing to go to war with the player. Click to expand...
<!-- artifact:quote:end -->
that's more of a problem with alliances not taking distance into account at all tbh

## Reply 79 — participant_057 · 2025-05-20 · post-30380083

<!-- artifact:quote:start -->
> 47pik said: Making the game harder isn’t the issue. Making the game engaging is. The issue isn’t that the AI needs buffs, the issue is the AI doesn’t do anything meaningful in the first place. It’s very discouraging to see the solution appears to be “hard mode” after all the extensive discussions that are had outlining the problem on this forum. All this accomplishes is making a game with little in the way of emergent storytelling harder (read: more micro-intensive) without making it any more interesting. The problem isn’t that the game is easy. The problem is all the characters are cardboard cutouts who don’t have any agency - they are acted upon, they do not act. Between the Conquerer system and now these “hard mode” buffs it really comes off as you not understanding the core issue with the game. It’s not that it’s easy - it’s that it’s boring. All you accomplish by making it “harder” in this way is make it more micro-intense in addition to being boring. Click to expand...
<!-- artifact:quote:end -->
I completely agree with this message. In my opinion, the game is boring precisely because the AI doesn’t behave the way it should, and giving it cheats is a step—but in the wrong direction. Let me explain: If the AI has the Ruthless trait or is my nemesis, I expect it to plot against me and my family frequently—kidnappings, assassinations, etc. I want to feel threatened, not by a conqueror with 20k troops blessed by the heavens, but by an AI that conspires. Imagine an AI that forces you into a war against your will because it has a blackmail hook on you. Or a sadistic conqueror who, once they’ve taken one of your territories, destroys the buildings, forcing you to rebuild them after the war. A true nemesis, if they conquer my lands, should raze them, kill my relatives, and try to bring me to my knees. And if I lose, I’d be okay with that—because I lost to a capable opponent, not a divine entity blessed with cheats just because I set the difficulty to hard or very hard. The AI is static. Some examples? -In the administrative government (and not only there), it doesn't fight for the imperial throne. In fact, I often find myself ending up as emperor just because—for some unknown reason—the AI votes for me. It shouldn't vote for me unless it’s my ally or I’ve used a hook to force them. Another examples: -the AI always builds the building that increases development and influence (I don’t remember the name since I play in Italian), even if it doesn’t have an administrative government. -The AI doesn’t build based on its economic archetype. If it’s militaristic, then it should focus on fortifications and military buildings. -The AI rarely raids unless it’s Norse. For instance, the Practiced Pirates tradition is basically ignored by the AI. -Seasons don’t impact gameplay. Winter should reduce available resources, slow down movement, and increase troop maintenance costs. There should be a war exhaustion system similar to Europa Universalis IV. War SHOULD be heavy and costly in terms of money and realm stability. -The Mongol invasion should drastically reduce the development of conquered counties. They should raze buildings. -The Black Death? It’s a joke compared to other minor diseases. I’m more afraid of measles—which regularly wipes out my children—than of the plague, which hasn’t caused me any serious damage in-game. -There’s no cap on obtainable skill points. Look at the mod that reworks lifestyles—if your character doesn’t have the required skill level, they should only be able to progress up to a certain point in lifestyle trees and perks. I love this game, but lately I haven’t felt like playing because I get bored after 100 years. Veteran players are dropping the game because there’s no real roleplay from the AI and everything feels static—unless I intentionally put myself into difficult situations. In conclusion, I appreciate the effort, but in my opinion, you’re looking in the wrong direction. If you don’t address this critical issue, I think the game will die out before the economy system (which, by the way, also desperately needs improvement) or the republics are even released. P.S. English is not my native language and I play the game in Italian (thanks to a mod—thank you, Paradox...), so some of the terms or perk names might not be correct, but I hope the meaning is clear.

## Reply 80 — participant_011 · 2025-05-20 · post-30380105

<!-- artifact:quote:start -->
> Ikatosh said: -The AI doesn’t build based on its economic archetype. If it’s militaristic, then it should focus on fortifications and military buildings. Click to expand...
<!-- artifact:quote:end -->
The problem is that AI just generally doesnt build enough. Builder is the only archetype that really builds stuff (and even then, not enough imo) and it obviously specs into economy. The problem with that is, since other archetypes generally build less, most of buildings AI builds are economy and they just run out of space to put any military buildings down. Forts are fine due to insane weighting on them (x5 if capital with <3 free buildings slots, another x5 if there's < 3 free buildings slots, another x5 if there's < 2 free building slots).

## Reply 81 — participant_058 · 2025-05-20 · post-30380122

<!-- artifact:quote:start -->
> PDX-Trinexx said: That said, our community has made it clear that we’re not meeting our objective Click to expand...
<!-- artifact:quote:end -->
Probably because you are still trying to balance a single game mode, normal difficulty, around both new and experienced players - which you cannot do. A level of challenge that is satisfying for experienced players is probably going to be incredibly frustrating for new players. The game is going to need a "hard" mode, no matter how you want to go about it, because you can't properly balance the game effectively for both new and experienced players on a single difficulty. It why pretty much every game has different mode for players at different skill levels. Also, any chance of actually doing anything about modifier stacking, which was mentioned as an issue needing to be addressed all the way back in the floor plan almost three years ago(!), or is that never going to be fixed?

## Reply 82 — participant_059 · 2025-05-20 · post-30380178

As mod maker that has been maintaining over 50 mods and still making new ones since the game released i would love beta access so i dont have to spend 24 hours straight updating my mods on release day. been asking for beta testing position for the past years so far no luck. If only someone from the beta team would invite me in. Check my workshop https://steamcommunity.com/id/FunGaming44/myworkshopfiles/?appid=1158310 so you can see for yourselfs

## Reply 83 — participant_047 · 2025-05-20 · post-30380257

<!-- artifact:quote:start -->
> InsidiousMage said: Also, any chance of actually doing anything about modifier stacking, which was mentioned as an issue needing to be addressed all the way back in the floor plan almost three years ago(!), or is that never going to be fixed? Click to expand...
<!-- artifact:quote:end -->
This, this, this. We've been complaining about modifier stacking and snowballing for years, but each DLC we get more and more and it seems like we're continually moving further away from where we were told it was going. Modifiers are a problem because they're an easy, universal non-mechanical way for the game to do "something" to the player, but IMO that's led to an over-reliance on them instead of focusing on improving systems: diplomacy, character traits being impactful, vassal/faction management (I'm still amazed all these years in we don't have a basic "change realm law" faction functionality). The next realm maintenance pass absolutely needs to look at paring and consolidating modifiers, or at least introducing some form of cap on effectiveness/addition, otherwise I feel like each new expansion is just going to make the problem even more unweildly and unsolvable if modifiers are continued to use as a substitute for actual mechanics.

## Reply 84 — participant_060 · 2025-05-20 · post-30380276

Very excited for the new difficulties. I think for hard/very hard it should definitely lean on nerfing player cheese rather than giving AI cheats. After all it's not the AI going from count to emperor of mankind in a single lifetime. Honestly I think the biggest culprit is alliances. While the changes limiting the numbers are a start, I would also recommend limiting them to equal ranks. It's too powerful and cheesy to be able to make an alliance one tier above you and then wield them like a hammer to upjump yourself with little to no planning required. Still overall good progress!

## Reply 85 — participant_061 · 2025-05-20 · post-30380289

<!-- artifact:quote:start -->
> After that, we’ll have a period of relative stability where mod authors can update their mods and players can finish a longer campaign without worrying about another update dropping and causing them grief. Click to expand...
<!-- artifact:quote:end -->
This was a really interesting read, especially for someone on the team of a major mod. We also try to gather player feedback and have to balance with post-release changes & further polishing vs our own desire to work on new content. But also I'm in this picture, and I don't like it.

## Reply 86 — participant_048 · 2025-05-20 · post-30380311

<!-- artifact:quote:start -->
> FunGaming said: As mod maker that has been maintaining over 50 mods and still making new ones since the game released i would love beta access so i dont have to spend 24 hours straight updating my mods on release day. been asking for beta testing position for the past years so far no luck. If only someone from the beta team would invite me in. Check my workshop https://steamcommunity.com/id/FunGaming44/myworkshopfiles/?appid=1158310 so you can see for yourselfs Click to expand...
<!-- artifact:quote:end -->
Ideally all Modders should be given beta access. I've seen some Mods take almost two weeks to update after major updates. And, on occasion, when multiple update occur over the span of one month, they have been known to take over a month to completely update. Beta Access would make things easier for both Modders, and the players who use those Mods...

## Reply 87 — participant_062 · 2025-05-20 · post-30380312

<!-- artifact:quote:start -->
> PDX-Trinexx said: We have a variety of changes that weren't shown in the DD image for these difficulties, but I do want to temper expectations: This is not a silver bullet for the difficulty complaints players are posting, and we don't consider it a long-term solution to that problem. We'll need to iterate and refine this over time, and we're still looking for ways to increase the fundamental challenge of the game without leaning on AI "cheats" like these. Click to expand...
<!-- artifact:quote:end -->
Have you all considered integrating a system similar to ObfusCKate mod into the main game or into the game settings? Having the stats of different characters obscured depending on your realm knowledge and spycraft could add an immense amount of difficulty and immersion into the game. It also prevents players from wife shopping too much and makes running a eugenics breeding operation much more difficult.

## Reply 88 — participant_063 · 2025-05-20 · post-30380316

I want to push a cheeky question, since its a small yet relatively sizable minority of concern will you actually address the turkic content portion?

## Reply 89 — participant_059 · 2025-05-20 · post-30380319

In the upcoming update I hope the following things are also fixed that i been telling you guys for the past weeks now AI not starting legends eunuch court position you can still hire anyone no matter if they are a eunuch or not, you guys need to put back OR = { has_trait = eunuch_1 has_trait = beardless_eunuch } in the 00_court_positions.txt file as a requirement same file needs a fix for the lady in waiting why can we hire men for the position, put back in is_shown_character = { scope:employee = { is_imprisoned = no is_female = yes } }

## Reply 90 — participant_064 · 2025-05-20 · post-30380325

<!-- artifact:quote:start -->
> ourg said: Difficulties based on AI cheat is really the worst idea ever, I know it's really popular because it's the easiest way to do it. Already posted it elsewhere, but here some ideas to increase dificulty without AI cheats : - increase odds for death/injuries, don't let almost all events with a good/safe option. The main issue is that currently all bad events have a safe option. Sometime you have to accept your fate - reduce powercreep features almost only used by player, or teach the AI to use it properly - Limit alliances from mariage : It's way to easy to have strong alliance with mariage. Mariage needs a rework. The AI should seek for strong alliance mariage instead of almost totaly based on prestige gain - Set threshold for opinion ( exemple : a rival can't go above 0 opinion ) It has always trigger me that you can have rivals with 100 opinion of you. Currently we can't mod the max opinion, it's a flat global value. Opinion max (or min) should not be the same for everyone, but should be conditioned on diferent factors (traits/relation/culture/etc...) The main problem with the herd mechanic, is that it's designed as gold as it should be designed as levies Here my solution to the problem : Each county shoud be able to substaint a max amount of herd (depending on fertility/season/etc...) meaning if you have only 1 county you could only have that maximum herd. Herd comming from your vassal/tributary are taken as % of they own herd (coming from their max county possibility) you still need to grow your herd to the maximum of the county can handle with the fertility (max is the equilibirum in fertility) currently everything is calculted arround the herd gain, while it should be calculated on the current/max herd (like levies) Click to expand...
<!-- artifact:quote:end -->
also need to reduce diplomatic radius.

## Reply 91 — participant_038 · 2025-05-20 · post-30380328

<!-- artifact:quote:start -->
> Juboboman said: I would also recommend limiting them to equal ranks. It's too powerful and cheesy to be able to make an alliance one tier above you Click to expand...
<!-- artifact:quote:end -->
Unless a ruler of the rank above is your liege. Isn't it normal for powerful duke to expect a marriage of his child and king's child? Unless you are powerful enough for a ruler of the rank above to consider you a powerful ally. Probably there were even cases of counts marrying king's children.

## Reply 92 — participant_065 · 2025-05-20 · post-30380346

>wake up >no Herd Decay >day ruined Hard Mode might be an interesting bandaid for the game, at least. Thank you for being open to suggestions. ...but I still have a question about Herd Decay: did you think about it during development but dropped it due to how the game would go "off the rails", or did you not even think of it at first and only now realized you can't change course without dedicating massive resources to solve the related issues?

## Reply 93 — participant_026 · 2025-05-20 · post-30380353

I think strong ambitious AI should consider leaving a confederation more often if they're not the confederation founder.

## Reply 94 — participant_066 · 2025-05-20 · post-30380356

<!-- artifact:quote:start -->
> Metz said: I think the difficulty can be solved simply with some sort of aggressive expansion or infamy mechanic. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> InsidiousMage said: Probably because you are still trying to balance a single game mode, normal difficulty, around both new and experienced players - which you cannot do. A level of challenge that is satisfying for experienced players is probably going to be incredibly frustrating for new players. The game is going to need a "hard" mode, no matter how you want to go about it, because you can't properly balance the game effectively for both new and experienced players on a single difficulty. It why pretty much every game has different mode for players at different skill levels. Also, any chance of actually doing anything about modifier stacking, which was mentioned as an issue needing to be addressed all the way back in the floor plan almost three years ago(!), or is that never going to be fixed? Click to expand...
<!-- artifact:quote:end -->
Thank goodness you put your foot down on the herd decay mechanic. Now maybe the armchair devs will move onto something else. Because everyone loved defensive pacts in CK2. Nothing like the Pope and the Abbasids joining together in their hatred of Ireland. The way I see it, giving the AI a bunch of mathematical bonuses can be seen as a direct counter to modifier stacking. It's not perfect by any means, nor will it address all issues, but if one major problem is that the player is better at the AI at stacking various modifiers which give them bigger numbers, then making sure the AI has bigger numbers by default at least keeps them more competitive. I say "more competitive" because, really, the AI never going to be able to plan and strategize and squeeze the game mechanics like the player can. I don't think there's a good solution here that satisfies everyone. But I can appreciate the attempt, at least, and I think it will have an overall positive impact for those who actually bother to change their difficulty to hard/very hard.

## Reply 95 — participant_011 · 2025-05-20 · post-30380370

<!-- artifact:quote:start -->
> Magil said: Thank goodness you put your foot down on the herd decay mechanic. Now maybe the armchair devs will move onto something else. Click to expand...
<!-- artifact:quote:end -->
"Armchair devs"? Idk about others, i modded it as soon as i heard the idea and i and didnt see any major issues arise from that. Granted, i can only playtest it so much as one person, but there're plenty of AIs in the steppe and they weren't dead by any means...

## Reply 96 — participant_038 · 2025-05-20 · post-30380373

<!-- artifact:quote:start -->
> rasuuru said: Teach AI to detect situations when the player or other AI tries to matri-/patrilenally marry their kids to second, third, ..., nth heirs and then kill older heirs. Click to expand...
<!-- artifact:quote:end -->
Just now I saw Louis 'The Younger's daughter Ermengarde being in patrilineal marriage and doing nothing to prevent another dynasty inheriting her duchy of Provence. She already has two kids of another dynasty and is pregnant with a third child. Apparently, Louis thought that her little brother will live long enough to make more Karlings but he died from measles at age 4. Louis himself died from measles three months later.

## Reply 97 — participant_067 · 2025-05-20 · post-30380398

<!-- artifact:quote:start -->
> PDX-Trinexx said: After a major release, gathering immediate feedback from players is crucial to ensure that any critical issues that made it through testing phases are swiftly handled, and that our post-release support cycle is focused on addressing player pain points with the new content. We actively collect this feedback from a wide variety of places; our own forums, Facebook, Steam, YouTube, Twitter, Reddit, Discord, QQ Guild, Bilibili, Tieba, among others. Essentially, if it’s posted on a publicly visible platform, odds are that we’re going to see it one way or another. Click to expand...
<!-- artifact:quote:end -->
At some point- maybe before the next Coronations DLC- would you consider a dev diary that 'walks through' how a feedback gets incorporated into the game? And possible includes you providing recommendations to the readers on how to make (format and frame) a good/actionable feedback that can lead to a fix from a (hypothetical) ungood/unactionable feedback that can't really be acted upon? Part of this is inviting you to encourage common format style, so that your team can receive the feedback style better for capture / organization, and explaining *why* the feedback style is good. For example- Issue: [Description] being less good than Issue: [Description] ...because [Description] is easier to copy, paste, and organize in a compilation if it doesn't include the line header (and thus effort to remove "Issue:" from every iteration). The other part is tracing how a good example is able to work through the system, particularly in why the reasons it is good- clear, discrete, reasonable in scope, potential mitigation identified- helps it goes through. On one hand, I imagine it'd be interesting for the community to see how the sausage is made, so to speak. Take a good news story of someone's success story, and walk it through the process. On the other hand, you could help the community help you by helping provide better-structured feedback. Totally useless, I'm sure. On the meta-mutant third hand, it'd give you all an excuse dev diary anywhere you want to farm that sweet, sweet engagement without bugging the coders too much. Cheers, and enjoyed the post.

## Reply 98 — participant_067 · 2025-05-20 · post-30380434

<!-- artifact:quote:start -->
> PDX-Trinexx said: I believe that's set as a define and not something we can selectively edit based on game rules, buuuut I can see about bullying someone into changing that. Maybe. No promises. Click to expand...
<!-- artifact:quote:end -->
For a longer term suggestion / recommendation for future consideration- what about having higher-threat (intrigue + wealth) schemers 'co-opt' / takeover hostile schemes someone else is pursuing? One of the reasons that the current cap on AI scheming against the player creates is that the AI that *does* start the scheme is too low, and so they are both slow and unlikely to succeed, 'occupying' the slot of who could act. Rather than simply expanding the number of plots the player, making the current plot-holder 'give up' their slot would be another option. Say run some sort of comparison of 'how long would it take / how effective would it be' comparison between the two parties, and give AI with substantial advantages in intrigue / accomplices the slot. This could even be signaled to the player in a way to build tension. Since the early release, the 'someone is trying to murder you' events (here is a rug) just let you know there is someone out to get you, letting the player prepare otherwise. A 'some nebulous threat has been displaced' event could do something similar- either implying that a plot has stopped, or that it's been replaced by something more dangerous. Kind of like the ominous foreshadowing events in the harm system, which may or may not lead to anything. Except here, it implies either the threat is gone... or getting worse.

## Reply 99 — participant_068 · 2025-05-20 · post-30380492

@PDX-Trinexx , bummed to hear about no change to the Herd mechanic but thank you for being up front. I would hope that, even if the dev team doesn't have the resources to change it now, they realize why we're unhappy with it and keep it in mind when designing future mechanics. For me at least, the Herd mechanic and theme don't match well enough. It feels like a mana bar with a Herd label on it. I understand needing to deviate from a faithful simulation a little bit to find the fun, but... for Paradox games, a faithful simulation is a huge part of the fun and appeal.

## Reply 100 — participant_069 · 2025-05-20 · post-30380503

To increase the difficulty, you could also hide information from players like obfusCKate - Hidden Information mod. This would make the game more challenging without giving bonuses to the AI or penalties to the player, while also increasing realism

## Reply 101 — participant_067 · 2025-05-20 · post-30380515

<!-- artifact:quote:start -->
> Devorious said: To increase the difficulty, you could also hide information from players like obfusCKate - Hidden Information mod. This would make the game more challenging without giving bonuses to the AI or penalties to the player, while also increasing realism Click to expand...
<!-- artifact:quote:end -->
PDX actually responded to a poster about that on Reddit. The crux was that the mod metrics they use don't show it being played much / enough. I think there's an argument to be made that this can be undercut by mod compatibility issues- obfusCKate is often outdated and not compatible with some other popular mods, and does some not-fun things. At the very least, I imagine that aspects of obfusCKate could be relativley easily adopted- things like the skill letters instead of skill numbers, hiding eugenics traits until adulthood, and using probability language instead of exact statistics.

## Reply 102 — participant_070 · 2025-05-20 · post-30380525

In my opinion, the stacking of positive opinion modifiers is the biggest balance concern outside of MAA being dramatically OP. Right now, as the King of Burgundy, literally every single subject and courtier of mine has an opinion on me of 100, the exact same as my Soulmate best friend wife of 40 years. It means nobody ever takes any hostile action whatsoever, and everything becomes a ball of undifferentiated slop. There needs to be an across the board slashing of all positive opinion modifiers, and certain negative ones need to be dramatically worsened, like tyranny, murdering high profile figures, murdering or harming family and friends. Like, why does my nemesis have a positive opinion of me? Give him a -1000 opinion malus. Let dishonourable characters completely ignore opinion when evaluating their course of action. Just let people hate you and fuck with you! There needs to be a lower opinion cap if nothing else, which gets raised by special relations. Say, default is +25, a basic relation like marriage or being a courtier is +50, a special relation like a friend or lover is +75, and a unique relation like soulmate is +100. People should not love you like your devoted wife of decades because you throw great parties sometimes. It's so frustrating watching the game just kneecap any and all difficulty that exists for seemingly no reason. And I know it's for no reason, because I use mods and made edits myself to do something similar to what I asked for above (minus the relation cap) and the game is so much more enjoyable.

## Reply 103 — participant_038 · 2025-05-20 · post-30380564

<!-- artifact:quote:start -->
> ParagonExile said: In my opinion, the stacking of positive opinion modifiers is the biggest balance concern outside of MAA being dramatically OP. Right now, as the King of Burgundy, literally every single subject and courtier of mine has an opinion on me of 100, the exact same as my Soulmate best friend wife of 40 years. It means nobody ever takes any hostile action whatsoever, and everything becomes a ball of undifferentiated slop. There needs to be an across the board slashing of all positive opinion modifiers, and certain negative ones need to be dramatically worsened, like tyranny, murdering high profile figures, murdering or harming family and friends. Like, why does my nemesis have a positive opinion of me? Give him a -1000 opinion malus. Let dishonourable characters completely ignore opinion when evaluating their course of action. Just let people hate you and fuck with you! There needs to be a lower opinion cap if nothing else, which gets raised by special relations. Say, default is +25, a basic relation like marriage or being a courtier is +50, a special relation like a friend or lover is +75, and a unique relation like soulmate is +100. People should not love you like your devoted wife of decades because you throw great parties sometimes. It's so frustrating watching the game just kneecap any and all difficulty that exists for seemingly no reason. And I know it's for no reason, because I use mods and made edits myself to do something similar to what I asked for above (minus the relation cap) and the game is so much more enjoyable. Click to expand...
<!-- artifact:quote:end -->
It was always weird to see how you can execute character's entire family and still have +100 opinion. For unlawful execution of loved ones there should be -1000 opinion and -1000000 for massacre so that we can't make it positive with gifts and lands. Just characters should not have such huge modifiers for lawful executions though. And removing someone's rival should make them happy.

## Reply 104 — participant_035 · 2025-05-20 · post-30380574

<!-- artifact:quote:start -->
> Devorious said: To increase the difficulty, you could also hide information from players Click to expand...
<!-- artifact:quote:end -->
Same line of thought in regards to raze clicking. Instead of making functional ai or making engaging mechanics, just make player click more, or do research on internet more, or dig game files more. Great.

## Reply 105 — participant_065 · 2025-05-20 · post-30380625

I'm going to shoot my shot and say how I hate that diplomatic range does not impact conveyed info. An Irish count should not be able to know what some courtier in Pagan's Stewardship is. There really should be a "fog of war" that prevents you from knowing what's going on far away. At the very least, their numeric values (Opinion, stats etc) should use Obfusckate's letter-tiers for faraway characters.

## Reply 106 — participant_038 · 2025-05-20 · post-30380655

<!-- artifact:quote:start -->
> FleetingRain said: Obfusckate's letter-tiers for faraway characters Click to expand...
<!-- artifact:quote:end -->
These letters still give you information about skills. I'd rather have them hidden completely. The same with traits and even portraits.

## Reply 107 — participant_071 · 2025-05-20 · post-30380693

Strongly agree with other posters that the Hard/Very Hard stuff should take more into account what players in need of challenge abuse, and that some buffs/nerfs are unnecessary annoyances that don't really add to challenge because they address . Simply adding in a harsh diplomatic range and a stationed penalty would have done probably more than all of these combined by cutting down on strats where the player can effectively trivialize most problems through untouchable firepower and accessing suitable breeding partners from a solid third of the map even as the middling Count of Buck Nowhere. And please, reconsider ObfusCKate - of course a Mod that deals in difficulty will have lower numbers; only a fraction of the players that 'graduate', so to speak, move on to it when there's so many alternatives such as different runs, total conversions that also cater to most other players, or simple annoyance that one must seek challenge elsewhere because the Devs apparently struggle with providing it. Simply porting it over as 'true hard mode' would be harder than the modes outlined in the comments, but also more flavorful and force the game to engage with more game systems, which has always been stated as an objective.

## Reply 108 — participant_072 · 2025-05-20 · post-30380700

<!-- artifact:quote:start -->
> PDX-Trinexx said: Only reason we were able to justify what we've done outside of the normal development cycle is because it's a self-contained gamerule and has minimal odds of messing things up in Unforeseen Ways. Regardless, it'll be a while before our QA team forgives me for my role in this going out during PPRS. Click to expand...
<!-- artifact:quote:end -->
What's your opinion of those suggestions?

## Reply 109 — participant_039 · 2025-05-20 · post-30380757

A compromise between the current game and full obfuscate could be hidden stats, but just for wanderers and (unimportant) foreign courtiers - the king of England will probably have a good sense of the personality and skills of the king of France and his heir, but not of a random lowborn wandering about in Ukraine that he has never met before. (This would also limit the player's advantage of being able to google search talented underlings/marriage options)

## Reply 110 — participant_073 · 2025-05-20 · post-30380842

<!-- artifact:quote:start -->
> One Proud Bavarian said: [...] On the one hand, the standing philosophy has been to not want one-off solutions and instead work with emerging - assumedly systemic - difficulty. but then whenever new content comes out, there never is any systemic difficulty present. [...] Can we just admit that a focus on systemic difficulty isn't happening? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Andrzej2 said: It's already quite annoying when Im for example an Emperor and have to marry my children to low nobility because of this "number of alliances" penalty. I usually can't roleplay a policy of marrying my children only to royal families or other imperial families beouse of alliance penalty. The best solution to this problem would be if marriages worked like in Ck2. They should give no effect on their own other than unlocking a diplomatic action to sign non agression pact and alliance. This way a penalty could be applied not to marrying but to turning marriage ties into alliances. For me it's a big problem because it severely breaks immersion when I as a prestigious ruler have to basically marry morganatically because of existing alliances penalty. Click to expand...
<!-- artifact:quote:end -->
glad to see that this feedback has been heard and that it's recognized that this upcoming change may help but does not address the core issues. something that keeps coming to mind as i read comments on the "difficulty issue" lately is the perk system (and the legacy system). they add too many bonuses the player can optimize towards his goals that the AI can't. if you wanted to design something specifically to empower the player over AI, you could hardly do better. and even worse, they break my immersion. i've thought they were wrong for CK since they were announced, and none of my 1k hours in CK3 have changed that judgment. removing them from the game entirely would improve it. i'm here for the kind of historical simulation gameplay that EU5 is focusing on and I hate that it's like the company has decided that Crusader Kings will leave that side to EU and instead focus on being an RPG and Sims game. I would just switch to EU, except that I much prefer CK's time period and relative lack of game design assuming "progress" through history. well said & seconded. it seems like "as high a % of players as possible should get to feel a power fantasy because otherwise we think they'll quit" which is inherently opposed to trying to create systemic difficulty. also, many people are talking about alliances - i think modifier and stat stacking is way more impactful than alliances. the one part of the harder difficulties i don't like is the marriage acceptance - i agree with this reply:

## Reply 111 — participant_074 · 2025-05-20 · post-30380928

<!-- artifact:quote:start -->
> PDX-Trinexx said: We have a variety of changes that weren't shown in the DD image for these difficulties, but I do want to temper expectations: This is not a silver bullet for the difficulty complaints players are posting, and we don't consider it a long-term solution to that problem. We'll need to iterate and refine this over time, and we're still looking for ways to increase the fundamental challenge of the game without leaning on AI "cheats" like these. Click to expand...
<!-- artifact:quote:end -->
Having a hard and very hard difficulty levels would be terrific, for me this is sth far more exciting to look for than an extended map or new OP governments. Would be great if it could be done by making AI more competent (no just buffed, but buffed as well), AI rulers trying to build a coalition/alliance against the human player and removing all the advances for a human player, like not being affected by the AI ruler dread.

## Reply 112 — participant_013 · 2025-05-20 · post-30380957

About herd, I hope they will at least get rid of the infinite respawn of levies herd

## Reply 113 — participant_075 · 2025-05-20 · post-30380961

You've talked a lot about the herd decay, and I don't feel the need to discuss that whole thing again, however something I have seen people discussing that I don't think has been brought up is Yurt balancing issues. Is there any intention at tweaking any of those numbers?

## Reply 114 — participant_076 · 2025-05-21 · post-30381105

<!-- artifact:quote:start -->
> PDX-Trinexx said: We have a variety of changes that weren't shown in the DD image for these difficulties, but I do want to temper expectations: This is not a silver bullet for the difficulty complaints players are posting, and we don't consider it a long-term solution to that problem. We'll need to iterate and refine this over time, and we're still looking for ways to increase the fundamental challenge of the game without leaning on AI "cheats" like these. Click to expand...
<!-- artifact:quote:end -->
I'm pleased that will be an option: actually, even upon release and not being familiar with the new mechanics I still found Ck3 too easy. That being said, what are the ways that AI needs to be tougher? Personally the thing which I would enjoy most is a competently aggressive AI. A very vicious mode where you can expect to be attacked, revoked, assassinated at every corner. Basically where I can feel the AI is as ruthless as I am, since for the most part, at the moment they are mainly chumps waiting to be exploited for My New Empire™.

## Reply 115 — participant_077 · 2025-05-21 · post-30381109

Not every day I see myself in a developer diary. This is why you write bug reports kids. you too can be on a post in the internet

## Reply 116 — participant_078 · 2025-05-21 · post-30381115

<!-- artifact:quote:start -->
> Athius said: Perhaps you could also remove the limitation of capping the amount of AI plots targeting the player. I cannot remember the last time I was assassinated - would be interesting if that occurred more often. Click to expand...
<!-- artifact:quote:end -->
Please do this for the hard/very hard mode. There are mods that do this and I always have them turned on.

## Reply 117 — participant_079 · 2025-05-21 · post-30381117

<!-- artifact:quote:start -->
> 47pik said: Making the game harder isn’t the issue. Making the game engaging is. The issue isn’t that the AI needs buffs, the issue is the AI doesn’t do anything meaningful in the first place. It’s very discouraging to see the solution appears to be “hard mode” after all the extensive discussions that are had outlining the problem on this forum. All this accomplishes is making a game with little in the way of emergent storytelling harder (read: more micro-intensive) without making it any more interesting. The problem isn’t that the game is easy. The problem is all the characters are cardboard cutouts who don’t have any agency - they are acted upon, they do not act. Between the Conquerer system and now these “hard mode” buffs it really comes off as you not understanding the core issue with the game. It’s not that it’s easy - it’s that it’s boring. All you accomplish by making it “harder” in this way is make it more micro-intense in addition to being boring. Click to expand...
<!-- artifact:quote:end -->
I agree with this... adding a "hard mode" so that you need to adjust difficulty depending on what faction you wish to play should be a non-starter. The point is that all "normal" difficulty settings should be roughly equal in difficulty to play regardless what style you select. People who GENERALLY found the game too easy or hard will adjust this slider. This is not a fix. If playing the Khans is far too easy to get ahead and dominate, there should be adjustments that make the Khans equally difficult to play as other factions in the same relative difficulty level. I can't really speak to how easy or hard the Khans are... as (due to the significant difference in playing style) I haven't figured out how to effectively play them yet. My comments are purely targeting the idea of adding things to the difficulty level to have players adjust them to balance. Feels like a cop out.

## Reply 118 — participant_080 · 2025-05-21 · post-30381210

My favorite part of my Nomad DLC is the part where the Devs threw their hands up in the air, gave up and just let Herds stay as mana since the main mechanics of nomads are literally broken from the conceptual level. Every Chapter needs a LotD I guess.

## Reply 119 — participant_081 · 2025-05-21 · post-30381232

<!-- artifact:quote:start -->
> PDX-Trinexx said: Mainly, that the balancing is wonky and that our more dedicated players want the game to be harder. We’ve released Update 1.16.1 and 1.16.2 already to tackle the former, and I’ve been working directly with our Game Director to implement something to help us address the latter; this will take the form of Hard and Very Hard difficulty modes releasing alongside Update 1.16.2.1 sometime later this week. View attachment 1302678 [Highly experimental! Mostly untested! Probably imbalanced! Try it out later this week and tell us what you think.] As we’ve said in the past, we want difficulty and challenge to be something that arise organically from how our mechanics interact, and think that giving flat buffs to the AI or penalties to the player for arbitrary reasons isn’t an ideal solution. That said, our community has made it clear that we’re not meeting our objective, and doing something is better than doing nothing. So while we intend to continue pursuing our goal of emergent challenge in the long term, we’re introducing these new difficulties for players who want the game to be harder right now. View attachment 1302679 [A small collection of some of the bonuses AI characters will receive in Hard/Very Hard difficulties.] We’ve also heard quite a few people asking for a passive herd decay mechanic. To go ahead and rip the bandaid off: We’re not planning on implementing this. Put simply, the system wasn’t designed with this in mind and is instead built around discrete reductions. Too much of the game goes off the rails when it tries to deduct what doesn’t exist, and herd decay ultimately impacts AI rulers far more than it impacts players (compounding balance/difficulty concerns). With the PRS stage for Khans of the Steppe coming to an end, we don’t have the time or resources available to rework a core aspect of the DLC to this degree. Additional adjustments to this system are still possible in Realm Maintenance updates, but these are unlikely to fundamentally rework the system itself. Click to expand...
<!-- artifact:quote:end -->
Praise to the Endless Sky, praise to Trinex I personally don't care who gets upset with the new difficulty, normal and easy are still completely playable and these revocation changes mean we can turn down domain limit without crippling the AI Seconding all the ObfusCKate, diplo range cap, and opinion cap suggestions, the lack of these is the biggest reason you never learn the names of your fellow vassals/realm peers in the vast majority of games

## Reply 120 — participant_075 · 2025-05-21 · post-30381260

<!-- artifact:quote:start -->
> TheSeraphim said: My favorite part of my Nomad DLC is the part where the Devs threw their hands up in the air, gave up and just let Herds stay as mana since the main mechanics of nomads are literally broken from the conceptual level. Every Chapter needs a LotD I guess. Click to expand...
<!-- artifact:quote:end -->
I personally disagree, I feel It's not broken from a fundamental level, what makes you think that?

## Reply 121 — participant_080 · 2025-05-21 · post-30381286

<!-- artifact:quote:start -->
> lo24681 said: I personally disagree, I feel It's not broken from a fundamental level, what makes you think that? Click to expand...
<!-- artifact:quote:end -->
Nomads were supposed to revolve around seasons and herds, with you migrating to greener pastures when needed. But neither can be punishing since the ai is too dumb to not get itself into constant death-spirals. If you design a mechanic that the ai is unable to use & thus need to defang then it is broken, end of story. The same goes for the current MaA & building design.

## Reply 122 — participant_075 · 2025-05-21 · post-30381296

<!-- artifact:quote:start -->
> TheSeraphim said: Nomads were supposed to revolve around seasons and herds, with you migrating to greener pastures when needed. But neither can be punishing since the ai is too dumb to not get itself into constant death-spirals. If you design a mechanic that the ai is unable to use it is broken, end of story. The same goes for the current MaA & building design. Click to expand...
<!-- artifact:quote:end -->
so less fundamentally broken, more not balanced well at all, which I will agree with. If there is gonna be no herd decay for whatever reason, then have the harsh seasons maybe do more events that drain a percentage of the herd? IDK, maybe that will work.

## Reply 123 — participant_081 · 2025-05-21 · post-30381298

<!-- artifact:quote:start -->
> hytth said: I'm a little bit concerned over the size of the dev team and what percentage of the team works from home. Click to expand...
<!-- artifact:quote:end -->
trying to make the work culture at a company you don't work for worse is foul behaviour and speaks to a deep, troubling level of entitlement. I also want the game to be better but this is an antisocial way to go about it

## Reply 124 — participant_075 · 2025-05-21 · post-30381300

<!-- artifact:quote:start -->
> Bisonmask said: trying to make the work culture at a company you don't work for worse is foul behaviour and speaks to a deep, troubling level of entitlement. I also want the game to be better but this is an antisocial way to go about it Click to expand...
<!-- artifact:quote:end -->
I will say I believe it was said somewhere that they are ending WFM some point this summer? regardless I am not sure that is an issue with anything going on.

## Reply 125 — participant_082 · 2025-05-21 · post-30381325

Why werent the constant crashes caught earlier in development of the patches? Or vassal contracts resetting?

## Reply 126 — participant_083 · 2025-05-21 · post-30381537

Damn this Jacob guy sounds well-versed in player expectations and game difficulty. I hope Trinexx can learn one or two things from this man. This was such a pleasant DD to read. People are already making good suggestions and points so I'll just wish you people good luck and fortune to do what needs to be done! Thanks for always lending an ear to us.

## Reply 127 — participant_082 · 2025-05-21 · post-30381574

<!-- artifact:quote:start -->
> Bisonmask said: trying to make the work culture at a company you don't work for worse is foul behaviour and speaks to a deep, troubling level of entitlement. I also want the game to be better but this is an antisocial way to go about it Click to expand...
<!-- artifact:quote:end -->
Having people work in the office isnt worsening the work culture, if it boosts productivity, itll be greatly appreciated by all

## Reply 128 — participant_084 · 2025-05-21 · post-30381583

Thank you for this!! Great solution, who wants higher difficulty could use it and who doesn’t will play as usual. Don’t understand negative reactions tbh. Tho I still believe some challenge should be incorporated on its own in mechanics itself. For example as landless I feel more secure than as feudal - I don’t need to pay upkeep and I cannot be touched. There are mechanical changes required which would be very nice to see. Still this is step in good direction.

## Reply 129 — participant_085 · 2025-05-21 · post-30381589

<!-- artifact:quote:start -->
> PDX-Trinexx said: We’ve also heard quite a few people asking for a passive herd decay mechanic. To go ahead and rip the bandaid off: We’re not planning on implementing this. Put simply, the system wasn’t designed with this in mind and is instead built around discrete reductions. Too much of the game goes off the rails when it tries to deduct what doesn’t exist, and herd decay ultimately impacts AI rulers far more than it impacts players (compounding balance/difficulty concerns). Click to expand...
<!-- artifact:quote:end -->
I'm very happy you wrote this DD and are being open about how you collect and act upon feedback and how your internal planning works. Truth be told, I really wish you had done this much sooner, but better late than never. Please make sure to continue communicating or at least hinting at your future plans and priorities early and often and explaining the reasoning behind your decisions going forwards! Even if there's something that bugs us that can't be fixed, knowing why it can't be fixed really helps. I'm personally not hyped about the addition of a Hard Mode (I agree with you that it's not the best way of adding difficulty), but I can't really argue with your logic - it's the fastest and most-often requested way of doing it, and doing something is better than nothing, as long as you also work on more engaging ways of adding difficulty for the future of course. I am very sad to hear this. I think this problem - that there is no herd decay mechanic, and your herd continues to grow even under plagues and harsh weather - is a very fundamental design flaw that isn't just a problem with this DLC, but is reflected in many mechanics in the game as a whole: For a while now I've advocated adding upkeep costs to buildings to stop incomes from snowballing, and I assume that this couldn't be added for the very same reason herd decay couldn't - that the system is just not designed with this in mind and would impact AI too negatively. In the same vein, another thing I wish the game had but don't expect to see anytime soon was a cost for maintaining Dynasty Legacies (with the possibility of families that fall from grace to lose their own Legacies). As it stands I find that the game economy and general balancing inevitably goes completely off-rails very quickly, 200 years into a run is enough to see your income grow ridiculously huge and accumulate a massive stack of gold you'll have no use for. The game's mechanics generally lack the realistic trade-off that accumulating stocks of resources also incurs the costs of maintaining them, and for this reason you can endlessly accumulate several bonuses from buildings and legacies and other things that stack up massively. I really think the entire game economy needs a very fundamental rework, designed with the principle that most gains should have some trade-off and stocks of resources should generally incur some proportional maintenance cost, with the possibility of losing things you can no longer maintain. I understand that you can't really focus on redoing Khans of the Steppe and deeply changing the AI just to add a herd decay mechanic at this moment, but I do hope you have plans for reworking the game economy as a whole and how the AI interacts with it when you work on the eventual Republic and Trade Route DLC's and can take this criticism into consideration if you do, and I do hope you find the time to add herd decay (alongside other forms of decay and upkeep in general) in the future.

## Reply 130 — participant_086 · 2025-05-21 · post-30381725

<!-- artifact:quote:start -->
> yokyoka said: Damn this Jacob guy sounds well-versed in player expectations and game difficulty. I hope Trinexx can learn one or two things from this man. This was such a pleasant DD to read. People are already making good suggestions and points so I'll just wish you people good luck and fortune to do what needs to be done! Thanks for always lending an ear to us. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Hello everyone! I’m Jacob, the Community Manager with Paradox Studio Black. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PDX-Trinexx​Community Manager​ Click to expand...
<!-- artifact:quote:end -->
Are you teasing us? Hoping Jacob can learn one or two things from himself? I cannot swear to it, but I’m pretty sure Jacob and PDX-Trinexx are one and the same. Maybe someone else can confirm or deny.

## Reply 131 — participant_087 · 2025-05-21 · post-30381826

That is one nice Dev Diary. It is always fun to "peek behind the curtain", so to speak. I do have few questions - you mentioned that you folks get an allocated time for Post Release Support where " main team" works on the updates, before it gets passed to Realm Maintenance Team. How long is that period usually (cause I believe it's flexible based on the workflow)? Does it have some minimum time it always needs to allocate like for example 2 weeks? What was the longest PRS period and for which update? Does the move from "regular releases" to "chapter releases" hurt the possible time "main team" can dedicate for Post Release Support?

## Reply 132 — participant_088 · 2025-05-21 · post-30381828

Now that there's going to be an actual hard mode, will you remove the faux-hard-mode that's attached to Hellenic Rome?

## Reply 133 — participant_083 · 2025-05-21 · post-30381871

<!-- artifact:quote:start -->
> Flockingbird said: Are you teasing us? Hoping Jacob can learn one or two things from himself? I cannot swear to it, but I’m pretty sure Jacob and PDX-Trinexx are one and the same. Maybe someone else can confirm or deny. Click to expand...
<!-- artifact:quote:end -->
I don't think that's possible. As it can be read in this DD, Jacob is a passionate, kind bosnian who cares a lot about the player concerns regarding balance, difficulty and game's direction. A hard working honest man who's trying his best. Trinexx on the other hand... Evil manifest. Telling people to go play another game because they beat it. We are losing more and more complainers each day. You think they quit complaining? Of course not. That's Trinexx "taking care" of them. Just because Trinexx posted Jacob's dev diary doesn't mean they are the same person.

## Reply 134 — participant_071 · 2025-05-21 · post-30381902

<!-- artifact:quote:start -->
> lnodiv said: Now that there's going to be an actual hard mode, will you remove the faux-hard-mode that's attached to Hellenic Rome? Click to expand...
<!-- artifact:quote:end -->
It was made optional in Roads to Power, so there's that.

## Reply 135 — participant_089 · 2025-05-21 · post-30381923

I'm adding my voice to beg you to do everything you can to eventually remove these difficulty modes. The game is quite balanced as long as you stay small, once you have that critical mass, you'll roll on everything. An AI cheat will just make that critical point a "bit" longer to reach, not fix it. I share your wish of an organic difficulty rather than that, and i fully support you on this point.

## Reply 136 — participant_038 · 2025-05-21 · post-30381942

<!-- artifact:quote:start -->
> Diskianterezh said: eventually remove these difficulty modes. Click to expand...
<!-- artifact:quote:end -->
If you mean making difficulty modular where instead of choosing between [Easy, Normal, Hard] everyone can precisely adjust settings to match their playstyle then I agree.

## Reply 137 — participant_013 · 2025-05-21 · post-30381991

<!-- artifact:quote:start -->
> TheSeraphim said: Nomads were supposed to revolve around seasons and herds, with you migrating to greener pastures when needed. But neither can be punishing since the ai is too dumb to not get itself into constant death-spirals. If you design a mechanic that the ai is unable to use & thus need to defang then it is broken, end of story. The same goes for the current MaA & building design. Click to expand...
<!-- artifact:quote:end -->
And you can add that migration is pointless while it should be the core of the gameplay. Maybe apart at the very beginning when playing a count single county. When playing nomad I don't even look at season like that it has almost no impact. The main problem of herd is the core design of the mecanic, they built and designed it like gold. Herd should be a value available at max per county, and you get a percentage of the actual herd value of vasssals/tributaries, not a percentage of their gain, like levies. And we can't even mod it because it's hardcoded. I'm still wondering who was the testers invited to approve the mecanic, because it was clearly not good. I'm worried how Paradox is handling dlc in the game, it seems like they're just adding layers of new things while old things need desperately a rework, without going back to the old average or even mediocre DLC mechanics (hi legends). They should inspire from CA and total warhammer 3 dlc, adding new stuff and a major rework of old stuff (even past dlc features)

## Reply 138 — participant_040 · 2025-05-21 · post-30382126

<!-- artifact:quote:start -->
> hytth said: All of this is just speculation on my part, but I do persistently worry that this is a factor in harming the quality of new content and worsening blunders such as balancing in Khans of the Steppe or the marketing disaster that was Legends of the Dead. Click to expand...
<!-- artifact:quote:end -->
Please don't speculate on things like this. I am a programmer - I made the raid intent system - I am mostly in the office. We have a great office. Some people have different commutes. People work differently well in different settings. Sometimes I personally feel like working from home gives me great focus without distractions. Designers play around with concepts and values. Miscommunication or overtuning happens in the office just as much as at home. It doesn't have anything to do with if we're in the office or out of it. If anything - making the work positions less attractive to people that easily can just hop companies to someone offering them better benefits - is something that most companies suffer from. Replacing a senior position that has worked on the game for over eight years... takes over eight years.

## Reply 139 — participant_090 · 2025-05-21 · post-30382200

I had two severe crashes trying to start the game today, both freezing out my PC entirely while loading the game, the first one even breaking the Paradox launcher generally, for CKIII and EUIV.

## Reply 140 — participant_011 · 2025-05-21 · post-30382207

<!-- artifact:quote:start -->
> Flockingbird said: Are you teasing us? Hoping Jacob can learn one or two things from himself? I cannot swear to it, but I’m pretty sure Jacob and PDX-Trinexx are one and the same. Maybe someone else can confirm or deny. Click to expand...
<!-- artifact:quote:end -->
Jacob to Trinexx conversation (dunno which one is which)

## Reply 141 — participant_011 · 2025-05-21 · post-30382209

<!-- artifact:quote:start -->
> ourg said: The main problem of herd is the core design of the mecanic, they built and designed it like gold. Herd should be a value available at max per county, and you get a percentage of the actual herd value of vasssals/tributaries, not a percentage of their gain, like levies. And we can't even mod it because it's hardcoded. Click to expand...
<!-- artifact:quote:end -->
Im pretty sure you can mod it to be almost like levies. It would require a lot of jank though

## Reply 142 — participant_030 · 2025-05-21 · post-30382210

<!-- artifact:quote:start -->
> ArynI said: Thank you for this!! Great solution, who wants higher difficulty could use it and who doesn’t will play as usual. Don’t understand negative reactions tbh. Click to expand...
<!-- artifact:quote:end -->
Surely many of those negative reactions are not due to the new difficulty options but due to the fact that the devs cannot implement the much needed passive herd decay mechanic because it was not even considered in the design phase.

## Reply 143 — participant_013 · 2025-05-21 · post-30382220

<!-- artifact:quote:start -->
> Benismann said: Im pretty sure you can mod it to be almost like levies. It would require a lot of jank though Click to expand...
<!-- artifact:quote:end -->
We can't mod the calculation with fertility, it's hardcoded. We can adjust value it's all we can do. I mean yes we can adjust/nerf. But we can't rework le herd systme by itself

## Reply 144 — participant_011 · 2025-05-21 · post-30382325

<!-- artifact:quote:start -->
> ourg said: We can't mod the calculation with fertility, it's hardcoded. We can adjust value it's all we can do. I mean yes we can adjust/nerf. But we can't rework le herd systme by itself Click to expand...
<!-- artifact:quote:end -->
You can turn the numbers to 0 and manually calculate whatever you want based on fertility, i dont think fertility equilibrium algorithms are that important to change or even keep if you want herd to be more like levies. It's just that.... where will you get the herd from in the first place?

## Reply 145 — participant_091 · 2025-05-21 · post-30382422

Generally, It was usually the doomstacks that made the game more challenging. Think of CK2—things like the Sunset Invasion, the Chinese Invasions from Jade Dragon made the game more challenging. It was simple but effective (though many people probably dislike it).

## Reply 146 — participant_013 · 2025-05-21 · post-30382433

<!-- artifact:quote:start -->
> Benismann said: You can turn the numbers to 0 and manually calculate whatever you want based on fertility, i dont think fertility equilibrium algorithms are that important to change or even keep if you want herd to be more like levies. It's just that.... where will you get the herd from in the first place? Click to expand...
<!-- artifact:quote:end -->
yes you can do that, but it would be weird and the fertility equilibirum which is the base of the mecanic will be totally ignored. We can access to the value that define the equilibirum. So yes we can replace them by "levies", but it will be levie that's all and fertility will be totally ignored.

## Reply 147 — participant_092 · 2025-05-21 · post-30382435

<!-- artifact:quote:start -->
> PDX-Trinexx said: We have a variety of changes that weren't shown in the DD image for these difficulties, but I do want to temper expectations: This is not a silver bullet for the difficulty complaints players are posting, and we don't consider it a long-term solution to that problem. We'll need to iterate and refine this over time, and we're still looking for ways to increase the fundamental challenge of the game without leaning on AI "cheats" like these. Click to expand...
<!-- artifact:quote:end -->
I believe that more emergent difficulty would arise if there was more mechanical depth in the interactions between lieges and vassals. Maybe this can be addressed in Realm Maintenance or alongside the development towards Coronations. Edit: having alliances work like in CK2, where a marriage created a non-aggression-pact and not an immediate alliance, would also probably make the game more difficult organically.

## Reply 148 — participant_013 · 2025-05-21 · post-30382550

<!-- artifact:quote:start -->
> Benismann said: You can turn the numbers to 0 and manually calculate whatever you want based on fertility, i dont think fertility equilibrium algorithms are that important to change or even keep if you want herd to be more like levies. It's just that.... where will you get the herd from in the first place? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> ourg said: yes you can do that, but it would be weird and the fertility equilibirum which is the base of the mecanic will be totally ignored. We can access to the value that define the equilibirum. So yes we can replace them by "levies", but it will be levie that's all and fertility will be totally ignored. Click to expand...
<!-- artifact:quote:end -->
I've tested and we can't even set the actual gain herd to 0 because the game refuse to set the HERD_GAIN_FROM_COUNTY_MULTIPLIER to 0 So we are obliged to keep the actual herd gain

## Reply 149 — participant_040 · 2025-05-21 · post-30382589

<!-- artifact:quote:start -->
> ourg said: I've tested and we can't even set the actual gain herd to 0 because the game refuse to set the HERD_GAIN_FROM_COUNTY_MULTIPLIER to 0 So we are obliged to keep the actual herd gain Click to expand...
<!-- artifact:quote:end -->
Oh yeah, that's fair man. Sometimes we programmers just kind of forget the possibility of modders wanting "unexpected behaviour". I will fully admit that the lack of modding mindset is something we sometimes have to get better at. Unfortunately this is one of those things that will probably have to wait until a future hotfix to actually get in the game - because the next upcoming hotfix is the last we're doing for a little while - to not keep breaking savegames / mods and just keep it stable. I promise I will fix this validation though. I have it in front of me - and it's just as you say - it checks for the value to be "Greater than 0 - or something has broken". For your modding needs it should probably be "Greater or equal to 0". You might be able to set it to like 0.00001 or something like that for now for experiments?

## Reply 150 — participant_013 · 2025-05-21 · post-30382780

<!-- artifact:quote:start -->
> JonZone said: You might be able to set it to like 0.00001 or something like that for now for experiments? Click to expand...
<!-- artifact:quote:end -->
it seems to accept not less than 0.01, still good but not perfect if we want to get something without this gain I've tried 0.0000000001 at first but the engine wasn't happy and load the base one

## Reply 151 — participant_040 · 2025-05-21 · post-30382833

<!-- artifact:quote:start -->
> ourg said: it seems to accept not less than 0.01, still good but not perfect if we want to get something without this gain I've tried 0.0000000001 at first but the engine wasn't happy and load the base one Click to expand...
<!-- artifact:quote:end -->
Agh okay. Have you tried 0.001? I'd expect that to work - but yes - if it fails validation it will set it to 1 I think. I have pushed the fix - but unfortunately I had to do it as part of my current tasks which is not until All Under Heaven. So it's in the pipeline, but unfortunately it's not going to roll out to your client for quite a bit.

## Reply 152 — participant_013 · 2025-05-21 · post-30382893

<!-- artifact:quote:start -->
> JonZone said: Agh okay. Have you tried 0.001? I'd expect that to work - but yes - if it fails validation it will set it to 1 I think. Click to expand...
<!-- artifact:quote:end -->
yes it works with 0.001. Looks enought for testing. but thx for the change in the future

## Reply 153 — participant_002 · 2025-05-21 · post-30382902

<!-- artifact:quote:start -->
> JonZone said: Agh okay. Have you tried 0.001? I'd expect that to work - but yes - if it fails validation it will set it to 1 I think. I have pushed the fix - but unfortunately I had to do it as part of my current tasks which is not until All Under Heaven. So it's in the pipeline, but unfortunately it's not going to roll out to your client for quite a bit. Click to expand...
<!-- artifact:quote:end -->
Just push it to the live branch on Steam right at 5PM on Friday. See how long you can survive before @Arakrates finds you.

## Reply 154 — participant_040 · 2025-05-21 · post-30382941

<!-- artifact:quote:start -->
> PDX-Trinexx said: Just push it to the live branch on Steam right at 5PM on Friday. See how long you can survive before @Arakrates finds you. Click to expand...
<!-- artifact:quote:end -->
I was given permission by Trinexx, I swear!

## Reply 155 — participant_093 · 2025-05-21 · post-30383765

So this means officially that you'll not add any Turkic content at all to the dlc most related to Turkic peoples. Great! Balancing which was a problem long before this dlc at %10.2 gets addressed but Turkic content at %7.4 does not when we may probably never get any other dlcs as related to Turkic peoples as this one. Performance also at % 7.4 doesn't get addressed either which is even more concerning considering there is an upcoming dlc that is going to add a huge chunk of the world to the map.

## Reply 156 — participant_038 · 2025-05-21 · post-30383847

<!-- artifact:quote:start -->
> Pups' Socks said: So this means officially that you'll not add any Turkic content at all to the dlc most related to Turkic peoples. Great! Balancing which was a problem long before this dlc at %10.2 gets addressed but Turkic content at %7.4 does not when we may probably never get any other dlcs as related to Turkic peoples as this one. Performance also at % 7.4 doesn't get addressed either which is even more concerning considering there is an upcoming dlc that is going to add a huge chunk of the world to the map. Click to expand...
<!-- artifact:quote:end -->
Just like how Mongols and Byzantines came with big changes and mechanics, Turkic people can get their "own" DLC too. This group is too big, developers wouldn't ignore them.

## Reply 157 — participant_094 · 2025-05-21 · post-30384030

Fascinating and reassuring glimpse behind the curtain, thank you! Admit i'm someone who buys the expansion to support the devs, but waits until a few patches have dropped before starting a proper playthrough.

## Reply 158 — participant_095 · 2025-05-22 · post-30385660

I appreciate this type of communication and directly addressing difficulty, but so far, the major expansions have been powercreep without accompanying downsides that properly balance them out. Admin government quickly turns into Space Marine MAA spam due to increased MAA sizes and borrowing governor troops. The drawback is meant to be intense internal political struggles against the noble families within your realm, who go after governorships so they can increase Influence gain and support their candidates for the throne. But the AI struggles to get off the ground and maintain consistent control of governorships within a single family, so none of the families gain enough influence to contest the imperial succession. The lack of independence factions, in conjunction with MAA spam, makes blobbing trivial. Nomad government gives you tons of special horde rider levies with improved stats, your own version of the estate with powerful bonuses, the ability to simply ask other rulers to become tributaries, and other benefits. This is meant to be counterbalanced by the need to maintain your herd size, at the mercy of fertility and seasons, requiring careful planning and frequent migrations. But it's impossible to have negative herd growth, making seasons and fertility irrelevant. Rather than a cycle of prosperity followed by desperate survival, it's as if you are being constantly pulled upward, with armies ballooning due to herd size, then becoming supermen due to yurt upgrades. Other DLCs (Legends, Royal Court, etc) have similar executions; further advantages with trivial or non-existent costs to maintain them, coalescing with other modifiers into a big snowball effect. Trying to rectify this by stacking extra buffs on the AI or similar measures might help, but is ultimately not feasible because each new expansion will bring another bevy of advantages for the player. By the time the final DLC for CK3 releases, you would likely have to give insane buffs to the AI to compensate. For the China expansion, I hope that we finally see a government type that strikes that fun, enjoyable balance, where you have to overcome some idiosyncratic challenges and are rewarded by experiencing the government types strengths. Allow for more setbacks and temporary failure; CK3 is designed to let playthroughs recover from the loss of characters and titles, so we actually have more leeway for challenge than other PDX titles.

## Reply 159 — participant_011 · 2025-05-22 · post-30386191

<!-- artifact:quote:start -->
> Vatonage said: But the AI struggles to get off the ground and maintain consistent control of governorships within a single family, Click to expand...
<!-- artifact:quote:end -->
And btw unlanded house heads have no AI as far as i know and just throw some schemes around sometimes through some other scripts i would guess.

## Reply 160 — participant_096 · 2025-05-22 · post-30386346

What about limit on how many AI can declare war on the player when he is weak? I remember that it was mentioned somewhere that it's capped, can it also be unlocked or increased somehow?

## Reply 161 — participant_016 · 2025-05-22 · post-30387290

What if you added a game rule to hide AI traits if your relations with them are low, plus taking into account diplomatic range. If relations sour the traits would still be present but you wouldn’t know of any new traits until you improve the relations again. This would be to simulate that you need to send an emissary elsewhere to learn about your regional neighbors. It would help prevent a lot of gamey random marriages done to improve stats.

## Reply 162 — participant_038 · 2025-05-22 · post-30387327

Any plans for special achievements for hard modes? Or achievements with different tiers and progress?

## Reply 163 — participant_097 · 2025-05-23 · post-30388175

<!-- artifact:quote:start -->
> PDX-Trinexx said: Hello everyone! I’m Jacob, the Community Manager with Paradox Studio Black. My role within the studio is to strengthen communication between us and you, the players, to ensure that we understand what you want from the game and that you understand what our intentions are for the future. While I’m just one part of the broader Community Team for Crusader Kings, I’m ultimately responsible for nearly every piece of public-facing communication we publish as a studio: dev diaries, feature breakdowns, chapter premiere videos, social media posts, etc. I’m also responsible for the reverse; every piece of feedback that ends up on a designer’s desk goes through me at some point in the process. Today, I’m going to talk about the release of Khans of the Steppe and the feedback we’ve received from players, as well as how we’re addressing it. After that I’ll give a brief overview of how our development cycles work, what the hell Post-Release Support even is, and then cap it off with a quick look at what our next steps are as a studio. I am a map gamer, so fair warning: There will be a good amount of graphs and charts in this dev diary. State of Launch​As you may or may not be aware, Khans of the Steppe and the 1.16 “Chamfron” Update were released on April 28th, and the initial response was fairly positive both from a technical perspective and a player sentiment one. However, we quickly noticed a spike in crash reports and commentary from players confirming this. Setting our lovely QA team to work, we quickly identified two major contributors to instability in 1.16 and pushed hotfixes to tackle both of them. These fixes have led to a significant reduction in crash rates, but we’re still seeing elevated levels, so we’re still working to identify and resolve the causes of these crashes. View attachment 1302669 [Crash rate analytics since the release of Khans of the Steppe. The 1.16.0.2 hotfix (circled in red) made a big difference, but there’s still work to be done.] While there was an immediate spike in negative reviews due to stability issues, the response at large to Khans of the Steppe was quite positive right out of the gate. When you spend months working on a specific project, it’s always an immense relief to see that it went well and players were having fun with the new content, so everyone at the studio was elated at the response! Then the review score started dropping. View attachment 1302670 [Steam reviews for Khans of the Steppe. You can see the ratio of positive to negative reviews shrinking over time; In the “biz”, this is considered a Bad Thing. While the amount of people who leave reviews are a sliver of a fraction of the greater playerbase, this is still a valuable source of information for us.] With all of our releases, we do a series of internal reports on the state of things at predefined intervals. There’s a Day 0 report, Day 1, Day 7, etc. While the Day 0 and Day 1 reports were initially positive, by the end of the week it became clear that there were outstanding problems that took some time to reach a breaking point for players. So, what were those problems? In order to figure that out, we have to do some basic analysis of the reviews themselves. To begin, I took every negative review on Steam and put them into a spreadsheet where they’re arranged, translated (we try to assess feedback from as many languages as we possibly can), and categorized based on what their main complaint is. (This isn’t the only way we analyze feedback, but reviews are fairly easy to explain so they make ideal content for demonstrating the point in this dev diary.) Once everything has been neatly categorized (a task I find immensely soothing, for the record), I can generate a quick chart showing which complaints are dominating the conversation. The main cause of stability complaints in the reviews were already addressed or being investigated, so we can skip that category and take a look at the next one in the list: Balancing. View attachment 1302671 [Outside of stability issues, balancing concerns make up the majority of complaints about Khans of the Steppe.] With my chart prepared, I can go to the design team and our Game Director to tell them “Players think the balancing is wonky, and here’s data to prove it.” From there, we can actually go through feedback to identify specific pain points and begin to address them in our first post-release support update (more on what that specific term means later). If you’re only interested in what’s next for Khans of the Steppe, then I’ll summarize here and save you some time: We know that players have concerns with the DLC and we’re working to address as many of these concerns as we can within the time we have allotted for post-release support before anything else is pushed off to Realm Maintenance. If you want to know more about how our communication pipeline from player to developer works, and how we act on what we hear from you, then read on! I intend to ramble for a bit longer. Player Feedback​In order to properly explain how we turn comments on the internet into changelog entries, I first need to talk about how we collect and parse feedback from all of our supported platforms. Pre-Release Feedback​Our handling of player feedback for Khans of the Steppe started quite a while back, before the announcement of Chapter 4 in fact. Our preview dev diary back in February was published so far ahead of the normal schedule specifically so that we could gather information about player desires and expectations regarding a Nomad-focused DLC. The feedback we received from that DD is directly responsible for a variety of changes that made it into the release version of Khans of the Steppe, such as expanding the new Nomadic government type to certain non-steppe regions. Additionally, we run a persistent closed beta program of roughly 100 people from our community. This includes members of various high-profile mod teams, historians, members of the community with a history of sending detailed and actionable feedback, and a small pile of content creators. The point of this program is to get direct player feedback on upcoming content as early into the development process of an update as we can (For Khans of the Steppe, this began roughly a year ago). As development progresses, more of the design is solidified and becomes more difficult to change in response to feedback, so this program is considered vital to us. Once the development version has progressed far enough that we’re able to announce it publicly, we begin a fresh dev diary cycle. These serve to inform the playerbase of what we’re working on while giving us a chance to get broader opinions and suggestions about the upcoming content. Our companion videos that are released on our YouTube channel are also helpful here, since viewer retention stats can inform us which sections within a given dev diary are of particular interest to viewers. View attachment 1302672 [Retention graph for Dev Diary 166; the bump at the 11 minute mark shows that viewers were particularly interested in the “Blessings of the Blue Sky” segment] Finally, in the last month or so before releasing Khans of the Steppe, we ran a separate preview group to get a final round of feedback. This is essentially a time-limited version of our persistent beta, and has a similar selection criteria for participation. During this stage, we essentially throw the flood gates open and pull in as many people as we think we can manage while maintaining some semblance of operational security. Mod team representation increases dramatically during this stage in order to give them a head start on compatibility patching their mods, and any content creator too slow to outrun our Influencer Relations Manager is also pulled into this time-limited program. Before you ask: Yes, that youtuber you’re thinking of is in this program. Yes, that one is too. Yes, them as well. View attachment 1302673 [A snippet from the aforementioned preview group. Yes, we run this through Discord.] The goal here is to make sure that the content we’re working on matches the expectations of our players as closely as possible ahead of release; the persistent beta program allows us to do this in broader strokes while the DLC is still taking shape, and the preview program allows us to catch more issues that would have slipped through the net (as well as giving us a head start on our first post-release support update). Post-Release Feedback​That’s all well and good, but what do we do about feedback after something is released? After a major release, gathering immediate feedback from players is crucial to ensure that any critical issues that made it through testing phases are swiftly handled, and that our post-release support cycle is focused on addressing player pain points with the new content. We actively collect this feedback from a wide variety of places; our own forums, Facebook, Steam, YouTube, Twitter, Reddit, Discord, QQ Guild, Bilibili, Tieba, among others. Essentially, if it’s posted on a publicly visible platform, odds are that we’re going to see it one way or another. View attachment 1302674 [The pc-feedback channel on our official Discord server is one of several “primary” feedback channels we use. Voting systems make it easier to tell at a glance which posts are more important to the community there. Sadly, Reddit votes aren’t as useful for this purpose.] To facilitate the collection of this amount of information, we have a set of Community Ambassadors (or “CAs”) who act as additional support for the bridge between our players and the development team. One of the main responsibilities of our CAs revolves around collecting player sentiment and feedback, monitoring discussions, and identifying pressing issues that players report post-release. You’ve said it? They’ve probably read it. They help cast the net as far as possible to ensure no significant feedback slips through. After a major release drops, they immediately begin scouring for reactions then compile them into a detailed Day 1 post-release report for the studio. View attachment 1302675 [A snippet from the Day 1 report for Khans of the Steppe. These initial reports are crucial for identifying standout issues that need to be handled as soon as possible] They condense hundreds of discussion threads, suggestions, and reports into a more digestible format to quickly identify what the community finds most pressing. As you can see above, crashing was the most prevalent issue highlighted in the Day 1 report, while balance issues weren’t widely reported until after the Day 1 report period. Feedback gathered this way is used to determine what the priorities of the development team should be during the post-release cycle, which finally brings us to the namesake of this dev diary… Post-Release Support​Our studio is structured into various internal teams, with each one focusing on specific updates or expansions. We have a team for Khans of the Steppe, All Under Heaven, Coronations, and others we can’t discuss quite yet. Post-Release Support (PRS) is the final stage of development for a Major Update before the team assigned to that update is dissolved and its members moved to other teams within the studio. The main objective of the PRS stage is to address any outstanding issue that may have slipped through the pre-development cycle. This includes fixing bugs, tweaking gameplay balances, and implementing various improvements or alterations to systems based on player feedback. The goal is to essentially “finalize” the DLC, but this doesn’t mean we cease work on the DLC outright. Any further updates or fixes that aren’t able to be implemented during the PRS stage go towards Realm Maintenance to be integrated into future updates rather than having their own dedicated release. During a PRS stage, we step up our Quality Assurance (QA) efforts by bringing in additional specialists to assist with PRS. These specialists work closely with the development team to review bug reports and ensure that as many reported issues as possible are investigated, identified, and assigned to a member of the development team to be addressed. If you’re reporting bugs on our official forums during a PRS stage, these are the people replying to and tagging your posts. View attachment 1302676 [As an aside, the tags are there to signal to other members of the team that a post has been looked at; this reduces the chances of us wasting time by going over threads that are already being handled.] Another important aspect of the PRS stage is taking care of issues that were “locked out” of the initial release for one reason or another. Two of the main reasons this could happen are feature freeze and loc freeze. During feature freeze, no new mechanics can be added to a DLC; anything that needs to be tacked on after feature freeze must target a future update. Similarly, a loc freeze means that no new player-facing text can be added, as localization into all of our supported languages takes a significant amount of time; any content that requires new or updated text after localization freeze must be scheduled for a future update. While these freezes mean that our response to feedback can sometimes be delayed, they ultimately help ensure that updates actually release when they’re intended to. In most cases, the aforementioned future update will be one of the “point releases” during PRS. Each PRS stage typically has time allocated for two or three of these updates, with the expectation that we’ll need them to tackle issues that cropped up after feature/loc freeze or issues reported by the community. Additionally, we allocate time for hotfixes as necessary to allow emergency updates. View attachment 1302677 [It’s a bit messy to look at, but you can see here how certain commits by the development team are sent to different branches depending on their contents. We have a lot of internal development branches.] Post-Release Support is an essential part of the development cycle in that it allows us to address player feedback as it’s submitted to us, but also to set the stage for future development by giving us a stronger idea of what players expect and want from the game. Next Steps​So, what has the feedback we’ve gotten since Khans of the Steppe been about, and what do players want from the game? Mainly, that the balancing is wonky and that our more dedicated players want the game to be harder. We’ve released Update 1.16.1 and 1.16.2 already to tackle the former, and I’ve been working directly with our Game Director to implement something to help us address the latter; this will take the form of Hard and Very Hard difficulty modes releasing alongside Update 1.16.2.1 sometime later this week. View attachment 1302678 [Highly experimental! Mostly untested! Probably imbalanced! Try it out later this week and tell us what you think.] As we’ve said in the past, we want difficulty and challenge to be something that arise organically from how our mechanics interact, and think that giving flat buffs to the AI or penalties to the player for arbitrary reasons isn’t an ideal solution. That said, our community has made it clear that we’re not meeting our objective, and doing something is better than doing nothing. So while we intend to continue pursuing our goal of emergent challenge in the long term, we’re introducing these new difficulties for players who want the game to be harder right now. View attachment 1302679 [A small collection of some of the bonuses AI characters will receive in Hard/Very Hard difficulties.] We’ve also heard quite a few people asking for a passive herd decay mechanic. To go ahead and rip the bandaid off: We’re not planning on implementing this. Put simply, the system wasn’t designed with this in mind and is instead built around discrete reductions. Too much of the game goes off the rails when it tries to deduct what doesn’t exist, and herd decay ultimately impacts AI rulers far more than it impacts players (compounding balance/difficulty concerns). With the PRS stage for Khans of the Steppe coming to an end, we don’t have the time or resources available to rework a core aspect of the DLC to this degree. Additional adjustments to this system are still possible in Realm Maintenance updates, but these are unlikely to fundamentally rework the system itself. Aside from that, we’ve heard we still have bugs to squash! AI asking you for paizas should be significantly reduced in the next update, the steppe region map mode should be properly colored in again, etc etc etc. We’ll have a full changelog of what’s been fixed releasing alongside the update itself later this week. After that, we’ll have a period of relative stability where mod authors can update their mods and players can finish a longer campaign without worrying about another update dropping and causing them grief. We’ll still be working on bugs and other issues that get reported (or already have been), but they’ll be packaged up alongside the release of our next piece of Chapter IV. While this is far from a comprehensive overview of development cycles, post-release support, or even feedback loops, I hope this gives you a stronger understanding of how these systems work at a glance. I’m always happy to talk at length about damn near anything involving Studio Black (as anyone subjected to one of my rants on our Discord can attest), so if you have any specifics you’d like to know more about then feel free to drop a comment and I’ll answer them as best I can! That’s all we have for this week, but be sure to come back next Tuesday; we’ll be talking about the design vision for a small piece of content we’re working on called All Under Heaven. Click to expand...
<!-- artifact:quote:end -->
What about multiplayer OOS fixes. I only really play multiplayer with my wife, son and brother. Umm, CK3 has always been less than ideal for stability with OOS, but this release makes it pretty much unplayable, especially if you have someone doing adventuring. Please fix this.

## Reply 164 — participant_098 · 2025-05-23 · post-30388732

The new difficulty options are going to make a lot of people very happy.

## Reply 165 — participant_099 · 2025-05-23 · post-30389029

Only reasonable way for game to get harder is for AI to "git gud" at playing the game. Mechanics don't have to change fundamentally, AI just needs to use them properly. It would also solve the other pressing issue of the game, micromanagement creep, as it would allow players to delegate stuff like routine family member guardianships and marriages.

## Reply 166 — participant_100 · 2025-05-23 · post-30389658

Could you please fix the 'none of estate' bug for previous saves, the new update has broken estates https://www.reddit.com/r/crusaderkings3/comments/1kg9qor/none_of_estate Estate goes blank on succession Information I have verifed my game files (Steam only) Yes I have disabled all mods Yes I am running the latest game update Yes Required Summary Estate goes blank on succession Description I am having trouble with my Estate disappearing on... forum.paradoxplaza.com Its mentioned a few times and nothings been sorted

## Reply 167 — participant_101 · 2025-05-26 · post-30396200

The CTDs are excessive. I've lost a hell of a lot of good game starts. Will the fix allow any of these starts to be rescued? Or should we just delete them?

## Reply 168 — participant_011 · 2025-05-26 · post-30396241

<!-- artifact:quote:start -->
> PeterCorless said: They actually have it, but it is tuned up so high that you hardly ever get hug-boxed. And by the time they try to organize against you, you're too big to stop. Click to expand...
<!-- artifact:quote:end -->
Wdym "they actually have it"? Where?

## Reply 169 — participant_101 · 2025-05-26 · post-30396332

<!-- artifact:quote:start -->
> Benismann said: Wdym "they actually have it"? Where? Click to expand...
<!-- artifact:quote:end -->
Oh Jesus! It was CK2. I forgot they didn't carry that forward.

## Reply 170 — participant_011 · 2025-05-26 · post-30396346

<!-- artifact:quote:start -->
> PeterCorless said: Oh Jesus! It was CK2. I forgot they didn't carry that forward. Click to expand...
<!-- artifact:quote:end -->
And it was in every other paradox game ever... Except hoi4 i guess, but even that has world tensions and major powers throwing guarantees left right and center.

## Reply 171 — participant_088 · 2025-05-27 · post-30400439

<!-- artifact:quote:start -->
> Evil Crusader said: It was made optional in Roads to Power, so there's that. Click to expand...
<!-- artifact:quote:end -->
Isn't Roads to Power the DLC that added the BS hard mode in the first place? I'm not seeing anything about it being made optional if you want Hellenic Rome.

## Reply 172 — participant_071 · 2025-05-27 · post-30400588

<!-- artifact:quote:start -->
> lnodiv said: Isn't Roads to Power the DLC that added the BS hard mode in the first place? I'm not seeing anything about it being made optional if you want Hellenic Rome. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Added a new option where you can choose to adopt Hellenism without activating "hard mode" - Giving you the possibility to go full role play mode if you want to. The option for hard mode remains available. Click to expand...
<!-- artifact:quote:end -->
Haven't been able to track down when it was introduced. 1.15.0 did make 'hard mode' optional, but I really forgot it was released later than RtP:

## Reply 173 — participant_098 · 2025-05-27 · post-30400601

<!-- artifact:quote:start -->
> lnodiv said: Isn't Roads to Power the DLC that added the BS hard mode in the first place? I'm not seeing anything about it being made optional if you want Hellenic Rome. Click to expand...
<!-- artifact:quote:end -->
What you seem to be referring to is a different thing. That is a special, unique "hard mode" that gets triggered if a player restores the Roman Empire (specifically a pagan Roman Empire AFAIK).

## Reply 174 — participant_102 · 2025-06-02 · post-30413921

Is it possible for Temujin to get conqueror earlier in his life? I almost always get it in his 40s, rarely late 30s, and sometimes never. The conqueror trait just seems random for him and it would be great to get it earlier if not just for roleplay purposes and not waste tens of hours trying to achieve greatest of khans with him.

## Reply 175 — participant_103 · 2025-06-19 · post-30495175

We can expect a new patch 1.16.2.4/1.16.3. in the near future (fixing current bugs) or the current bugs will be fixed in the upcoming DLC?

