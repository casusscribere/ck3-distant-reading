---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1541141/"
forum_thread_id: 1541141
content_type: reply_thread
parent_dd_file: dd_107_2022-09-08_development-diary-107-1-7-0-bastion-upda.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 107
title: "Development Diary #107: 1.7.0 \"Bastion\" Update Notes"
dd_date: 2022-09-08
expansion: Friends and Foes
patch: Patch 1.7 (Bastion)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 7
reply_count: 134
participant_count: 92
reply_date_first: 2022-09-08
reply_date_last: 2022-09-17
body_word_count: 5754
inline_image_count: 0
quoted_span_count: 82
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Development Diary #107: 1.7.0 "Bastion" Update Notes

*134 replies from 92 participants across 7 pages*

## Reply 1 — participant_001 · 2022-09-08 · post-28460855

- The bypass_requirements console cheat was removed for Laws, because it messed up succession logic. Changed the cheat a bit so it will not cheat you out of your succession. Does this mean it is now working again for Laws because that was removed in the previous update and we mod makers who use this cheat to test our mods been asking for it to be enabled again so hopefully this works again now ?? If not please bring it back so we can test our mods again more quickly

## Reply 2 — participant_002 · 2022-09-08 · post-28460862

<!-- artifact:quote:start -->
> sidestep said: - You now only need 1 Holy Site to create or recreate a Head of Faith title Click to expand...
<!-- artifact:quote:end -->
Any specific reason for that change? I feel like that never was a problem and it seems very easy now.

## Reply 3 — participant_003 · 2022-09-08 · post-28460864

<!-- artifact:quote:start -->
> sidestep said: - Fixed combat evaluation incorrectly used on sea zones, leading to many naval invasions being impossible. Click to expand...
<!-- artifact:quote:end -->
Thanks for this. I was enjoying the dev diary a lot before I even opened the spoiler tag What was going on here exactly?

## Reply 4 — participant_004 · 2022-09-08 · post-28460869

<!-- artifact:quote:start -->
> johnty5 said: What was going on here exactly? Click to expand...
<!-- artifact:quote:end -->
if you want an even better bug: the counter system for men at arms is reversed, so units are countered by the unit types they are supposed to counter

## Reply 5 — participant_005 · 2022-09-08 · post-28460872

Update looks great, love the ai changes, but I swear guys you will never fix this bug with patronymics? https://forum.paradoxplaza.com/foru...working-well-sometimes.1466265/#post-28312717 It's been exactly 2 years and 10+ threads created, can you please fix it already. It's like my personal crusade at this point to bring attention of the devs to this bug.

## Reply 6 — participant_006 · 2022-09-08 · post-28460882

Still no fix to the saga in stone achivement? I don't wanna cheese this achievement.

## Reply 7 — participant_007 · 2022-09-08 · post-28460890

I love you Zack

## Reply 8 — participant_008 · 2022-09-08 · post-28460896

How many game mods will be updated when the game is updated? Or do you have no such plan?

## Reply 9 — participant_009 · 2022-09-08 · post-28460901

Are dissolution factions fixed now? Doesn't look like from the patch notes.

## Reply 10 — participant_010 · 2022-09-08 · post-28460903

Wow, those fixes look nice. I am looking forward to play the new patch and see what the Event Pack will bring.

## Reply 11 — participant_011 · 2022-09-08 · post-28460917

<!-- artifact:quote:start -->
> 阵亡者不杀 said: How many game mods will be updated when the game is updated? Or do you have no such plan? Click to expand...
<!-- artifact:quote:end -->
That's not really their responsibility, is it? Mods are updated by modders

## Reply 12 — participant_012 · 2022-09-08 · post-28460918

<!-- artifact:quote:start -->
> sidestep said: Heya everyone! This is your friendly neighborhood Tech Lead Zack. Someone made the rather unwise decision to allow me to write this dev diary for the "Bastion" update ( I think everyone else was sick ) and I intend to milk it as much as I can. "Bastion" goes live later today with Friends & Foes and I'm so happy to finally be able to share it with you. I'm the Tech Lead "in charge" of Friends & Foes which means that I work with the team to determine what tech ( see: code ) we can actually add to the update, that it works as it should and that we at the end of the day have a functioning build to deliver to you ( among other things, I also sit in a lot of meetings where I usually have a lot of wise and important things to say ). This is the first Event Pack that we have done for CK3 so me and the team have been treading a lot of new ground, which has been very exciting, and I also think that it's the best one so far! View attachment 874422 View attachment 874424 "Fun" tidbits from the development of F&F: We collected a bunch of name suggestions for the update and voted but I forgot which one we decided on and just picked "Bastion" because that was my favorite. It was probably the winner anyway, right? The '&' in Friends & Foes caused technical issues in one specific backend system due to it being a special character, so it had to be redone...but I wasn't here then so Joel had to do it for me instead ( funny ). We had a technical issue that only happened when saving saves with an even number of characters, it worked with an odd number. I thought it was funny, QA did not. Then when I realized I had to fix it I didn't find it funny anymore but then QA suddenly thought it was funny, so I guess it evened out. We had a merge that got screwed up so bad that it broke our changelog generation, therefore I had to manually find a lot of entries ( needle, haystack, fun ). Doing the merge itself was also a lot of fun, I'll be releasing a book about it titled "Zack and the Merge That Never Ended" and I'm forcing the design team ( who no doubt made fun of me during the ordeal ) to write it for me, good luck. We added a new jungle event image that had so many hidden monkeys that we kept finding new ones throughout the dev cycle, we probably haven't found them all yet. The gallows art is very well done, but also weirdly "upbeat" according to the design team. Proper gallows-humour right there. Jokes and tidbits aside; it has been super fun working on Friends & Foes, I could absolutely not have done it without the rest of the team and I hope you all enjoy it. Below you can find what you were actually looking for in this thread. Thanks for reading and playing, and remember: an enemy is just another potential lover that is slightly harder to woo! Click to expand...
<!-- artifact:quote:end -->
Ok, these fun tidbits are hilarious and I for one hope we can see more of these in the future! Oh the joys of game development! Patch notes look awesome and can not wait for the next 15 minutes to pass.

## Reply 13 — participant_001 · 2022-09-08 · post-28460919

<!-- artifact:quote:start -->
> 阵亡者不杀 said: How many game mods will be updated when the game is updated? Or do you have no such plan? Click to expand...
<!-- artifact:quote:end -->
That is up to each mod maker themselves, I am going to be updating all my mods in the coming hours.

## Reply 14 — participant_008 · 2022-09-08 · post-28460922

<!-- artifact:quote:start -->
> Keizer Harm said: That's not really their responsibility, isn't it? Mods are updated by modders Click to expand...
<!-- artifact:quote:end -->
Some games will release a new version to the more popular mod production team before the version update to ensure that the mod can be updated synchronously. It seems that there is no similar plan for Crusader Kings 3?

## Reply 15 — participant_013 · 2022-09-08 · post-28460929

<!-- artifact:quote:start -->
> sidestep said: Reworked Populist Factions in order to improve their functionality, especially in regards to how they interact with player vassals: Vassals directly affected by a Populist Revolt now get a letter from the revolt leader, asking the vassal how they will respond to their demand. The vassal may: Join the war and help their liege Convert to the faction's culture and/or faith and join the war on the side of the rebels Stay out of the war and do nothing (though still risk losing land if the liege loses the war) AI vassals are most likely to join the war on the side of their liege, but can in rare cases pick either of the other two options Click to expand...
<!-- artifact:quote:end -->
Honestly, I'd love to see a version of this extended to regular wars. If a vassal stands to have their land conquered by a foreign ruler, let them offer to join the war in defense or even let them offer to join the attacker in exchange for only being vassalised. If the war would only result in their vassalisation, still let them pick a side to support.

## Reply 16 — participant_014 · 2022-09-08 · post-28460934

- You as the liege no longer lose a piety level for choosing not to imprison the guilty party in secret reveal events This is the best part

## Reply 17 — participant_015 · 2022-09-08 · post-28460935

cool update, was really hoping for dynasty map mode, but maybe next time

## Reply 18 — participant_016 · 2022-09-08 · post-28460939

- Slightly loosened the requirements of pagan conversions for the AI so that less scattered pagan realms persist into the very late game I'm a little confused by this one. Are you saying that pagan realms will be less scattered, so late-game we will get pagan blobs instead of a random pagan duke somewhere? Or are you saying that the AI will leave paganism more willingly, so fewer pagans will persist because they have all converted?

## Reply 19 — participant_017 · 2022-09-08 · post-28460945

The AI and UX improvements look great. Also, I am somehow excited by the new events coming in the DLC, even if they are rather montypythonic. And they introduced much more new art and music than I expected! But damn, I hoped for a bugfix list at least twice that long... The court tutor is still not working and it is a simple script-only fix. The Canary Islands mess is left untouched. No fixes for any struggle-related bugs (this surprises me the most, TBH). The situation is not terrible at the moment, but we are moving towards Leviathan territory at steady peace. Still, there is a high chance that 1.7.0 would turn out to be the most stable CKIII version since...the last summer update a year ago? Well, util a new expansion destabilises it once again.

## Reply 20 — participant_011 · 2022-09-08 · post-28460946

<!-- artifact:quote:start -->
> 阵亡者不杀 said: Some games will release a new version to the more popular mod production team before the version update to ensure that the mod can be updated synchronously. It seems that there is no similar plan for Crusader Kings 3? Click to expand...
<!-- artifact:quote:end -->
That has been done for the Royal Court update. This update is much smaller so fewer mods will break, updating them will be less work.

## Reply 21 — participant_018 · 2022-09-08 · post-28460948

I'm quite happy to see a lot of improvement with the Mongols and also the reduction of likelihood for incest from IA controlled characters.

## Reply 22 — participant_019 · 2022-09-08 · post-28460950

Is 1.7.0 compatible with 1.6.1.2 saves?

## Reply 23 — participant_001 · 2022-09-08 · post-28460958

<!-- artifact:quote:start -->
> IsakMDMA said: Is 1.7.0 compatible with 1.6.1.2 saves? Click to expand...
<!-- artifact:quote:end -->
Some things might be but its always recommend to start a new game to make full use of all the updates.

## Reply 24 — participant_020 · 2022-09-08 · post-28460969

<!-- artifact:quote:start -->
> Ciccillo Rre said: Are dissolution factions fixed now? Doesn't look like from the patch notes. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> sidestep said: We had a merge that got screwed up so bad that it broke our changelog generation, therefore I had to manually find a lot of entries ( needle, haystack, fun ). Click to expand...
<!-- artifact:quote:end -->
Well, the text does say this: So, while the changelog is impressive, it is likely (that is, even more likely than usual) to be not full.

## Reply 25 — participant_021 · 2022-09-08 · post-28460976

<!-- artifact:quote:start -->
> 阵亡者不杀 said: How many game mods will be updated when the game is updated? Or do you have no such plan? Click to expand...
<!-- artifact:quote:end -->
Huh? You do know that mods are community managed? Or are you referring to something else? For the devs: Showcasing the importance of proper communications, this and the DD just before, has made me significantly likelier to actually buy F&F.

## Reply 26 — participant_022 · 2022-09-08 · post-28460984

Just checking if Dissolution factions not functioning properly got fixed? At the moment they aren't destroying the liege's top titles

## Reply 27 — participant_022 · 2022-09-08 · post-28460987

<!-- artifact:quote:start -->
> Viridianus said: Well, the text does say this: So, while the changelog is impressive, it is likely (that is, even more likely than usual) to be not full Click to expand...
<!-- artifact:quote:end -->
Ah fantastic actually, I thought a few things were missing

## Reply 28 — participant_023 · 2022-09-08 · post-28460992

... This is what happens when you let a programmer write stuff for the public. ;p

## Reply 29 — participant_024 · 2022-09-08 · post-28460994

I loved the tidbits. As a fellow programmer I'm always delighted in hearing about particularly weird bugs and the even number of charachters save file is absolutely hilarious. Especially because I wasn't the one who had to fix it. Please do share more of these.

## Reply 30 — participant_025 · 2022-09-08 · post-28461004

Thanks for the patch notes.

## Reply 31 — participant_026 · 2022-09-08 · post-28461005

<!-- artifact:quote:start -->
> Players are fickle on the best of days and dishonorable on the worst! No longer shall we depend on their assistance when we declare our righteous wars for [GetWarReason]! They may still interfere with our plans, so we will still be weary of enemy player alliances. Click to expand...
<!-- artifact:quote:end -->
So does this mean the AI ignores the military strength of its player allies when declaring wars?

## Reply 32 — participant_027 · 2022-09-08 · post-28461010

do we see ghosts ? i want events like Morgan from The Walking Dead does see.

## Reply 33 — participant_028 · 2022-09-08 · post-28461015

Good job, I don't know how effective these changes will be to ensure that AI realms are more stable and don't shatter into a million pieces 10 years into the game, but I am happy you recognized it as a problem.

## Reply 34 — participant_029 · 2022-09-08 · post-28461021

<!-- artifact:quote:start -->
> sidestep said: - Significantly lowered the chances of artifacts getting damaged during feasts Click to expand...
<!-- artifact:quote:end -->
[ _] Sidestep, how could you! [ x] These things happen. It wasn't my favorite event.

## Reply 35 — participant_030 · 2022-09-08 · post-28461034

<!-- artifact:quote:start -->
> junassa said: So does this mean the AI ignores the military strength of its player allies when declaring wars? Click to expand...
<!-- artifact:quote:end -->
I think it means that AI will ignore player alliance in offensive war. (You can leave them hanging) But it will still take it into consideration when you are allied to the target. So the AI doesn't trust player to support them in a war.

## Reply 36 — participant_031 · 2022-09-08 · post-28461035

The event pack should've been free and included in the update. Was raising the prices on existing DLCs really not enough?

## Reply 37 — participant_032 · 2022-09-08 · post-28461041

<!-- artifact:quote:start -->
> johnty5 said: Thanks for this. I was enjoying the dev diary a lot before I even opened the spoiler tag What was going on here exactly? Click to expand...
<!-- artifact:quote:end -->
Glad that you enjoyed it, haha. I don't quite remember what was going on there, I don't think I personally touched it. But needless to say something wrong was going on but it works now.

## Reply 38 — participant_032 · 2022-09-08 · post-28461044

<!-- artifact:quote:start -->
> Tilarium said: Ok, these fun tidbits are hilarious and I for one hope we can see more of these in the future! Oh the joys of game development! Patch notes look awesome and can not wait for the next 15 minutes to pass. Click to expand...
<!-- artifact:quote:end -->
There were more tidbits but not all of them are safe for...humanity? Haha.

## Reply 39 — participant_032 · 2022-09-08 · post-28461054

<!-- artifact:quote:start -->
> ArthanM said: I think it means that AI will ignore player alliance in offensive war. (You can leave them hanging) But it will still take it into consideration when you are allied to the target. So the AI doesn't trust player to support them in a war. Click to expand...
<!-- artifact:quote:end -->
Yeah if I remember it correctly the AI will not count on a player joining them in an offensive war, because...let's be honest, we couldn't care less about their offensive wars usually. But they will count player allies of the defender because in the worst case scenario they will join in the defense and we wanted the AI to account for the worst case scenario instead of launching into an offensive war they cannot win by themselves.

## Reply 40 — participant_032 · 2022-09-08 · post-28461057

<!-- artifact:quote:start -->
> IsakMDMA said: Is 1.7.0 compatible with 1.6.1.2 saves? Click to expand...
<!-- artifact:quote:end -->
Yes, saves should be fully compatible. But make a backup first just in case ^^

## Reply 41 — participant_032 · 2022-09-08 · post-28461063

<!-- artifact:quote:start -->
> Alerias said: ... This is what happens when you let a programmer write stuff for the public. ;p Click to expand...
<!-- artifact:quote:end -->
Trust that I was not their first choice, haha.

## Reply 42 — participant_032 · 2022-09-08 · post-28461071

<!-- artifact:quote:start -->
> Rukawa said: do we see ghosts ? i want events like Morgan from The Walking Dead does see. Click to expand...
<!-- artifact:quote:end -->
We added the ability to animate dead characters in event windows...make of that what you will

## Reply 43 — participant_032 · 2022-09-08 · post-28461074

<!-- artifact:quote:start -->
> Wythric said: Good job, I don't know how effective these changes will be to ensure that AI realms are more stable and don't shatter into a million pieces 10 years into the game, but I am happy you recognized it as a problem. Click to expand...
<!-- artifact:quote:end -->
We saw good results in testing after these changes, so...hopefully you'll see them too

## Reply 44 — participant_033 · 2022-09-08 · post-28461075

Still haven't fixed the Iberian walls popping out everywhere.

## Reply 45 — participant_034 · 2022-09-08 · post-28461092

<!-- artifact:quote:start -->
> sidestep said: Yes, saves should be fully compatible. But make a backup first just in case ^^ Click to expand...
<!-- artifact:quote:end -->
Game crash when trying to load a save from previous version. But I've already decided not to play it for now. My issue is will the version 1.6.1.2 be uploaded to the list of available beta versions on steam so I can rollback? Cause it is currently not there.

## Reply 46 — participant_026 · 2022-09-08 · post-28461094

<!-- artifact:quote:start -->
> ArthanM said: I think it means that AI will ignore player alliance in offensive war. (You can leave them hanging) But it will still take it into consideration when you are allied to the target. So the AI doesn't trust player to support them in a war. Click to expand...
<!-- artifact:quote:end -->
That was pretty much the status quo before the patch though: the AI was designed to not "see" it's player allies' army once the war was declared, but they took player military strength into account when deciding to declare war.

## Reply 47 — participant_035 · 2022-09-08 · post-28461107

I really hoped you would fix the bug with the archduchy of austria and the bug with the truth is relative. Will this bugfix be next?

## Reply 48 — participant_026 · 2022-09-08 · post-28461111

<!-- artifact:quote:start -->
> sidestep said: Yeah if I remember it correctly the AI will not count on a player joining them in an offensive war, because...let's be honest, we couldn't care less about their offensive wars usually. But they will count player allies of the defender because in the worst case scenario they will join in the defense and we wanted the AI to account for the worst case scenario instead of launching into an offensive war they cannot win by themselves. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> junassa said: @PDXOxycoon Hi. thanks for bringing clarity to this issue. I think this is very problematic. 1. So far as I know, the AI takes the strength of its human allies into account when deciding to declare war 2. As you've stated, the AI doesn't take the strength of its human allies into account when actually prosecuting said war. While it's all well and good that PDX is working on a solution to this problem I think you've left the players in an intolerable position. In the interim my recommendation would be to change (1) so that the AI only sees its non human allies. Click to expand...
<!-- artifact:quote:end -->
I get this but IMO this doesn't really clear anything up. AI won't fight their own war So I'm called into an ally's offensive war to take a nearby county, our armies plus a third ally's are on par with the enemy and their ally. Pretty simple right? My army arrives to the scene and the enemy is sitting on the war target not doing... forum.paradoxplaza.com @PDXOxycoon already stated that the AI doesn't "see" the player's army after the war has been declared; what I'm asking is if the AI considers the players military strength in determining whether or not it should declare war in the first place

## Reply 49 — participant_036 · 2022-09-08 · post-28461116

- Satisfied community thirstiness for Bohemond Bruh i saw the reddit post. Funniest thing ever

## Reply 50 — participant_037 · 2022-09-08 · post-28461119

I'm getting a CTD when I attempt to load my 1.6.2 saves that are autosaves. Is this a known issue that will be resolved? Mac OS 12.5.1

## Reply 51 — participant_024 · 2022-09-08 · post-28461133

Can I run 1.7.0 if my CPU doesn't support AVX?

## Reply 52 — participant_038 · 2022-09-08 · post-28461171

<!-- artifact:quote:start -->
> Djaevlenselv said: Honestly, I'd love to see a version of this extended to regular wars. If a vassal stands to have their land conquered by a foreign ruler, let them offer to join the war in defense or even let them offer to join the attacker in exchange for only being vassalised. If the war would only result in their vassalisation, still let them pick a side to support. Click to expand...
<!-- artifact:quote:end -->
Should be dire consequences if your liege wins the war while you tried to help your opponent though.

## Reply 53 — participant_039 · 2022-09-08 · post-28461175

<!-- artifact:quote:start -->
> Spartakus said: Can I run 1.7.0 if my CPU doesn't support AVX? Click to expand...
<!-- artifact:quote:end -->
Should be able to yeah

## Reply 54 — participant_040 · 2022-09-08 · post-28461220

The issue of Chinese Localization. The "MAX_RECURSIVE_DEPTH" are still exist. Chinese language does not need articles, but these things are still displayed incorrectly in the game.

## Reply 55 — participant_005 · 2022-09-08 · post-28461243

<!-- artifact:quote:start -->
> https://imgur.com/Qu32r27
<!-- artifact:quote:end -->
So if you ended a feud and got a buff/debuff, if I understand it correctly you can't start a new feud? Event has a cooldown for duration of this buff?

## Reply 56 — participant_041 · 2022-09-08 · post-28461275

<!-- artifact:quote:start -->
> sidestep said: Yes, saves should be fully compatible. But make a backup first just in case ^^ Click to expand...
<!-- artifact:quote:end -->
I'm crashing whenever I try to load a save from 1.6.1.2. Made a bug report but I'm seeing some other people experience the same problem on Reddit as well.

## Reply 57 — participant_024 · 2022-09-08 · post-28461315

<!-- artifact:quote:start -->
> blackninja9939 said: Should be able to yeah Click to expand...
<!-- artifact:quote:end -->
Unfortunately I am not - and others apparently too. CPU Support Issue for Fate of Iberia Howdy all! We have seen a fair amount of reports from players not being able to play the game on PC since Fate of Iberia was released. We think we have identified the issue and are working on a fix. People who are affected are likely those with... forum.paradoxplaza.com

## Reply 58 — participant_042 · 2022-09-08 · post-28461326

Good patch but still no fix for battles not correctly giving prestige/fame when there is multiple armies involved in one side. That's a bug that's existed since royal court was released.

## Reply 59 — participant_043 · 2022-09-08 · post-28461369

- AI characters are now much less likely to convert to Adamitism, only truly irrational characters will consider it. just did a playthrough and conquered africa. Starting character was adamist. ended up being able to vassalize everyone like crazy because i could marry off my 20 or so kids that went through "enhanced training". I needed to take a shower after that for sure.

## Reply 60 — participant_044 · 2022-09-08 · post-28461381

<!-- artifact:quote:start -->
> sidestep said: We had a technical issue that only happened when saving saves with an even number of characters, it worked with an odd number. I thought it was funny, QA did not. Then when I realized I had to fix it I didn't find it funny anymore but then QA suddenly thought it was funny, so I guess it evened out. Click to expand...
<!-- artifact:quote:end -->
I have got to ask... how the hell did that even happen???

## Reply 61 — participant_045 · 2022-09-08 · post-28461410

Imma buy this just cuz i like Tech Lead Zac. Yall should put Zac in charge of making dev diaries from now on for profit

## Reply 62 — participant_046 · 2022-09-08 · post-28461416

Hello! When microsoft store version will be avaivable? i can't actually find it.

## Reply 63 — participant_047 · 2022-09-08 · post-28461434

<!-- artifact:quote:start -->
> sidestep said: We had a merge that got screwed up so bad that it broke our changelog generation, therefore I had to manually find a lot of entries ( needle, haystack, fun ). Doing the merge itself was also a lot of fun, I'll be releasing a book about it titled "Zack and the Merge That Never Ended" and I'm forcing the design team ( who no doubt made fun of me during the ordeal ) to write it for me, good luck. Click to expand...
<!-- artifact:quote:end -->
What version control are you using?

## Reply 64 — participant_048 · 2022-09-08 · post-28461461

I'd have kept the banishing the bishop to confiscate his gold "exploit" but added serious consequences for doing it. HUGE opinion hit with the pope (to the point of almost automatic excommunication unless you're already on very good terms with him) + smaller opinion hit (doubled if character is zealous, 0 if cynical) with all other characters of the same religion if tyrannical. If a just banishment (I.E. he tried to murder someone), no opinion hit happens, but the Pope is less willing to give you gold for a long time because you already took gold from the church and shouldn't be asking him too. Sometimes you just have a very serious financial emergency and your priest has a few thousand gold sitting around and won't even upgrade his own church for some reason. I don't see anything wrong with confiscating the gold because I imagine something similar has happened at some point in history. Just add more negative geopolitical consequences for doing it.

## Reply 65 — participant_049 · 2022-09-08 · post-28461477

<!-- artifact:quote:start -->
> 阵亡者不杀 said: How many game mods will be updated when the game is updated? Or do you have no such plan? Click to expand...
<!-- artifact:quote:end -->
that's a question for the modders

## Reply 66 — participant_017 · 2022-09-08 · post-28461482

<!-- artifact:quote:start -->
> Toybasher said: I'd have kept the banishing the bishop to confiscate his gold "exploit" but added serious consequences for doing it. HUGE opinion hit with the pope (to the point of almost automatic excommunication unless you're already on very good terms with him) + smaller opinion hit (doubled if character is zealous, 0 if cynical) with all other characters of the same religion if tyrannical. If a just banishment (I.E. he tried to murder someone), no opinion hit happens, but the Pope is less willing to give you gold for a long time because you already took gold from the church and shouldn't be asking him too. Sometimes you just have a very serious financial emergency and your priest has a few thousand gold sitting around and won't even upgrade his own church for some reason. I don't see anything wrong with confiscating the gold because I imagine something similar has happened at some point in history. Just add more negative geopolitical consequences for doing it. Click to expand...
<!-- artifact:quote:end -->
It will be cool if (probably as a part of a more religion-centred DLC) the church coffers (inherited with getting "the job" of realm priest or pope or neoasaturiasalian calif) were separated from the private treasure of the person holding the title.

## Reply 67 — participant_050 · 2022-09-08 · post-28461484

<!-- artifact:quote:start -->
> - Players are fickle on the best of days and dishonorable on the worst! No longer shall we depend on their assistance when we declare our righteous wars for [GetWarReason]! They may still interfere with our plans, so we will still be weary of enemy player alliances. Click to expand...
<!-- artifact:quote:end -->
This seems like it could be a big improvement. I always avoided marriages outside my realm because I would get multiple calls to war every year from my allies, which always distracted me from my own expansion.

## Reply 68 — participant_049 · 2022-09-08 · post-28461488

<!-- artifact:quote:start -->
> 阵亡者不杀 said: Some games will release a new version to the more popular mod production team before the version update to ensure that the mod can be updated synchronously. It seems that there is no similar plan for Crusader Kings 3? Click to expand...
<!-- artifact:quote:end -->
CK3 doesn't really have mods that are massive enough in terms of playerbase, as far as i'm aware

## Reply 69 — participant_051 · 2022-09-08 · post-28461493

<!-- artifact:quote:start -->
> Toybasher said: I'd have kept the banishing the bishop to confiscate his gold "exploit" but added serious consequences for doing it. HUGE opinion hit with the pope (to the point of almost automatic excommunication unless you're already on very good terms with him) + smaller opinion hit (doubled if character is zealous, 0 if cynical) with all other characters of the same religion if tyrannical. [...] Click to expand...
<!-- artifact:quote:end -->
Had the same thought when I read the changelog. Should have made it an option with consequences unless there is a really good reason not to have any. In some cases it might even be justified if the bishops are corrupt... to give it "back to the people", but in reality you are just as corrupt and have the option to sack it for yourself. xD

## Reply 70 — participant_052 · 2022-09-08 · post-28461508

Very exciting changes! (Not to mention the entertaining write up ) A little disappointed to still see Iberian walls everywhere. They look fantastic but only around Iberian castles. Hope to see an official fix to that next time.

## Reply 71 — participant_053 · 2022-09-08 · post-28461516

Does this patch include the changes to AI that were recently reported in a DD? EDIT: It does. Just found the note.

## Reply 72 — participant_054 · 2022-09-08 · post-28461530

<!-- artifact:quote:start -->
> sidestep said: Crossroads with Inn Click to expand...
<!-- artifact:quote:end -->
I went down to the crossroads, fell down on my knees

## Reply 73 — participant_055 · 2022-09-08 · post-28461542

<!-- artifact:quote:start -->
> Adamus Petius Jusus said: Any specific reason for that change? I feel like that never was a problem and it seems very easy now. Click to expand...
<!-- artifact:quote:end -->
That's highly dependent on who you are playing as. Its also only really easy for already established religions. Not to mention most of the religions in the gam require you to paint the map in order to hold 3 holy site, or the alternative is to cheese the game to take single counties in various spots around the map....also crappy

## Reply 74 — participant_017 · 2022-09-08 · post-28461553

<!-- artifact:quote:start -->
> Medu Salem said: Sadly true. A lot of the mods (even some that were initially very popular) I subscribed to haven't been updated ever since RC or even longer, which held me back for quite a while now to start a serious play with RC. And I am growing weary of even subscribing to any newer mods because you never know if it just won't break a savegame soon with a minor patch already when the modder lost the interest to keep it up-to-date. And I am not even talking about the big conversation mods. But rather stuff with some of the QoL features that the basegame still lacks and which I find necessary to make the game more manageable and endurable for a longer run. I mean, some of them got ticked off the list by the vanilla game already, like the CoA designer, or now the memory system. But some others still remain. Click to expand...
<!-- artifact:quote:end -->
Is CK3 modding that harder? The game has an active player count similar to Stellaris and equal to roughly 50% of HoI4. Those are not bad numbers at all. What happened to that ambitious GoT mod and other similar projects?

## Reply 75 — participant_049 · 2022-09-08 · post-28461564

<!-- artifact:quote:start -->
> Prpht said: Is CK3 modding that harder? The game has an active player count similar to Stellaris and equal to roughly 50% of HoI4. Those are not bad numbers at all. What happened to that ambitious GoT mod and other similar projects? Click to expand...
<!-- artifact:quote:end -->
well, that's still underway as of a few days ago. you've got to expect that it will take time

## Reply 76 — participant_048 · 2022-09-08 · post-28461567

<!-- artifact:quote:start -->
> sidestep said: Yeah if I remember it correctly the AI will not count on a player joining them in an offensive war, because...let's be honest, we couldn't care less about their offensive wars usually. But they will count player allies of the defender because in the worst case scenario they will join in the defense and we wanted the AI to account for the worst case scenario instead of launching into an offensive war they cannot win by themselves. Click to expand...
<!-- artifact:quote:end -->
I'd like if this could be fleshed out a bit. I.E.: The AI still taking the player's alliance into account. However, before declaring a war, if the alliance is reason why they feel they have enough force to start the war, and the player is the ally, they will try to wait until the player doesn't seem "busy". For instance, if the player is already in a war, a large malus to the "Alliance force multiplier" because the player ally clearly has stuff on their plate (an even higher malus if it's a defensive or civil war) and they can't expect the player to come to their aid when the player is already at war with someone else. Also, it's been a while, but in Stellaris I think alliances or even mutual rivals of the target declaring a war can start a vote. I remember having something like that happen when a random empire contacted me with a vote for declaring a war on one of my rivals. Alliances in CK3 should do something similar where you can ask for support before you actually start the war. Currently the AI would declare war because the alliance thinks they will be able to win, then they rush to the player (who might be in a defensive war of their own) to beg for help for something they started. If it's an offensive war Call To Arms, they should send a "I want to declare war on X and I need your assistance" letter. If the player accepts, great. If the player declines, don't start the war. (and apply a diplomatic penalty of some sort. There could even be a "not right now, but soon" option which makes the AI wait about 6 months (if the CB isn't one that will soon expire) before contacting the player again. (at this point the player can only accept or decline outright.) Sometimes I want to join but I'm already in a war, but my only option is to accept right away or fully decline. If they'd wait a bit for me to finish up I'd gladly join but they instead declare a war they can't win while I got my hands full. Also, one last thing. Can we get the option to nag the AI for compensation (Gold, etc.) like they do to the player when you don't do enough war-score? The AI can do it to us but I've had allies who do jack squat and I'd like to have a middleman solution between letting them get off scot free and tyrannical executions. Heck, if the AI doesn't want to join a war, you can't even send the war invite to them, but when they want you to join a war, you must accept or lose an entire level of fame usually.

## Reply 77 — participant_049 · 2022-09-08 · post-28461569

<!-- artifact:quote:start -->
> The Russian Empire said: I went down to the crossroads, fell down on my knees Click to expand...
<!-- artifact:quote:end -->
the crossroads are within, man! within!

## Reply 78 — participant_056 · 2022-09-08 · post-28461587

Are Muslim HoF still bugged where they are always in your diplo range therefore making it harder to take the "Appoint a Righteous Caliph" decision?

## Reply 79 — participant_057 · 2022-09-08 · post-28461594

<!-- artifact:quote:start -->
> Djaevlenselv said: Honestly, I'd love to see a version of this extended to regular wars. If a vassal stands to have their land conquered by a foreign ruler, let them offer to join the war in defense or even let them offer to join the attacker in exchange for only being vassalised. If the war would only result in their vassalisation, still let them pick a side to support. Click to expand...
<!-- artifact:quote:end -->
The perfect opportunity to share one of my favourite mods: Vassals to Arms.

## Reply 80 — participant_058 · 2022-09-08 · post-28461728

<!-- artifact:quote:start -->
> Ciccillo Rre said: Are dissolution factions fixed now? Doesn't look like from the patch notes. Click to expand...
<!-- artifact:quote:end -->
I just made the test by dissoluting Byzantine empire through a dissolution faction war and enforce demands. It seems to be fixed despite not being mentioned in the patch notes.

## Reply 81 — participant_059 · 2022-09-08 · post-28461776

I like the relationship icons. Can't tell you how many times I was surprised to discover someone that died was a rival or friend.

## Reply 82 — participant_060 · 2022-09-08 · post-28461804

> Harold Godwinson will no longer get alliances within the first 5 years of the game, to let the battle for England play out first That seems like a penalty that will mean Harold can't win, if William and Harald are still capable of gaining and bringing allies into the war, but Harold isn't.

## Reply 83 — participant_061 · 2022-09-08 · post-28461822

Most excited for the vassalization changes in the free update. Looking forward to getting the dlc after work.

## Reply 84 — participant_062 · 2022-09-08 · post-28461837

Love these changes. But is it gonna take 2 weeks to fix compatibility every time now?

## Reply 85 — participant_059 · 2022-09-08 · post-28461856

It would be okay if there was a very slight chance that they did assume the player would join/not join - unless there already is an in-built chance for the ai to miscalculate army strength.

## Reply 86 — participant_005 · 2022-09-08 · post-28461897

<!-- artifact:quote:start -->
> https://imgur.com/z6HcxCw
<!-- artifact:quote:end -->
I have never seen 2 AI empires being formed in 1 game. There is some bordergore in Bavaria region, but overall map looks pretty decent for a 867 start. Paradox actually did it and fixed the AI.

## Reply 87 — participant_063 · 2022-09-08 · post-28461902

<!-- artifact:quote:start -->
> Adamus Petius Jusus said: Any specific reason for that change? I feel like that never was a problem and it seems very easy now Click to expand...
<!-- artifact:quote:end -->
There are some faiths (Catholicism being the big one) who’s whole sites are very far apart from each other Ive also always thought the requirement of needing two holy sites never made much sense to begin with.

## Reply 88 — participant_064 · 2022-09-08 · post-28461947

<!-- artifact:quote:start -->
> - You can no longer seize the gold from realm priests through banishment, and any gold that former realm priests hold will be transferred to the new realm priest if possible Click to expand...
<!-- artifact:quote:end -->
What? I can't rob the church from its money? Outrageous!

## Reply 89 — participant_065 · 2022-09-08 · post-28461958

What is MaA? I really hate acronyms.

## Reply 90 — participant_049 · 2022-09-08 · post-28461973

<!-- artifact:quote:start -->
> Pugman said: What is MaA? I really hate acronyms. Click to expand...
<!-- artifact:quote:end -->
men at arms

## Reply 91 — participant_057 · 2022-09-08 · post-28461994

<!-- artifact:quote:start -->
> Pugman said: What is MaA? I really hate acronyms. Click to expand...
<!-- artifact:quote:end -->
Men-at-arms

## Reply 92 — participant_066 · 2022-09-08 · post-28462030

These are all wonderful! Unfortunate that we still can't get rid of hostile holy orders in cities run by republican vassals tho

## Reply 93 — participant_067 · 2022-09-08 · post-28462034

<!-- artifact:quote:start -->
> Djaevlenselv said: Honestly, I'd love to see a version of this extended to regular wars. If a vassal stands to have their land conquered by a foreign ruler, let them offer to join the war in defense or even let them offer to join the attacker in exchange for only being vassalised. If the war would only result in their vassalisation, still let them pick a side to support. Click to expand...
<!-- artifact:quote:end -->
God I hope so, this always made War in Ck2 ASOIAF actually fun

## Reply 94 — participant_068 · 2022-09-08 · post-28462101

<!-- artifact:quote:start -->
> Djaevlenselv said: Honestly, I'd love to see a version of this extended to regular wars. If a vassal stands to have their land conquered by a foreign ruler, let them offer to join the war in defense or even let them offer to join the attacker in exchange for only being vassalised. If the war would only result in their vassalisation, still let them pick a side to support. Click to expand...
<!-- artifact:quote:end -->
While I agree that this would be fun and add additional depth to conflict, is there a historical precedent for this sort of behavior? In a feudal-like system, would there be a a social stigma attached to breaking one’s contract? I could also see cultures and governments that rely more heavily on personal/familial connections to be especially punishing in that regard.

## Reply 95 — participant_067 · 2022-09-08 · post-28462216

<!-- artifact:quote:start -->
> ck3enjoyer said: https://imgur.com/z6HcxCw I have never seen 2 AI empires being formed in 1 game. There is some bordergore in Bavaria region, but overall map looks pretty decent for a 867 start. Paradox actually did it and fixed the AI. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> https://imgur.com/z6HcxCw
<!-- artifact:quote:end -->
God i hope this is a pattern and not a one off. it may sound stupid but I've actually dropped a bunch of Norse>Norman>English runs beacuse France falls apart even with me putting strong capets on the throne, Aquitaine is always lost and never regained and only once did the Ai form england for me to want to later conquer (and I had to push this heavily to happen).

## Reply 96 — participant_069 · 2022-09-08 · post-28462254

Glad to see another update but it has broken my ironman save (437 years in game). Unfortunately I can't even share crash report Fortunately it works on 1.6.1.2 and save is not corrupted (ironman is still active).

## Reply 97 — participant_003 · 2022-09-08 · post-28462274

<!-- artifact:quote:start -->
> The Shacks said: God i hope this is a pattern and not a one off. it may sound stupid but I've actually dropped a bunch of Norse>Norman>English runs beacuse France falls apart even with me putting strong capets on the throne, Aquitaine is always lost and never regained and only once did the Ai form england for me to want to later conquer (and I had to push this heavily to happen). Click to expand...
<!-- artifact:quote:end -->
Incredibly stable France in my first (observer) 1066 run. French monarch consolidated domain quickly and France remained intact. Lost Aquitaine once, but diplomatically reintegrated within a decade. France was so stable that, last time I looked, the entirity of Aquitaine's duchies were a few years away from drifting into France. Never seen anything like it before this patch.

## Reply 98 — participant_070 · 2022-09-08 · post-28462328

<!-- artifact:quote:start -->
> Zen0ren said: Game crash when trying to load a save from previous version. But I've already decided not to play it for now. My issue is will the version 1.6.1.2 be uploaded to the list of available beta versions on steam so I can rollback? Cause it is currently not there. Click to expand...
<!-- artifact:quote:end -->
I'm also crashing when trying to play a save from 1.6.1.2. It's really annoying because I gave up on that save when I was so close to getting a number of the Christian Spanish/Iberian achievements (I had already ended the Iberian Struggle via force) when an update was pushed through which made Mozarabism consider itself Astray, which almost made me collapse due to the problems that caused. I put that save on ice waiting for an update to fix the issue but now it looks like it's lost. Does anyone know if this can be fixed?

## Reply 99 — participant_071 · 2022-09-08 · post-28462336

Observed a 867 start and the AI seems to get pretty stable with kingdom-tier realms after the first 100 years. From 950 onwards there were minimal changes to the overall layot of my map, never seen that before. Some things I've noticed (observed a game until 1200~). - The Karlings managed to hold Lotharingia, East Francia, Italy and Burgundy under the same ruler for almost 50 years, but no empire was formed. Francia was formed right after that and seems stable as far as 1200~ - In general, feudalization seems to happen VERY fast now. At around 1100 there were just a dozen of Tribal counties in the Niger Delta, around Mongolia, and in Sami. Everyone else was a Clan or Feudal by then. - Iberia seems to be the most unstable place in the map. Even the steppe region quickly formed kingdoms and changed only slightly after 1000. - Development seems to be faster too. India by 1100 was a massive powerhouse with multiple kingdoms with 25k+ troops. - The Abbasids seem bizarrely stable. The same with the Bizantine Empire. After France formed those three were constantly fighting for the highest amount of troops and the caliphs had INSANE monthly piety, one was gaining like 50 per month. - Almost every ruler seems to be holding their maximum amount of domains as the Dev Diary suggested they would. - Reformed Faiths seems to be bleeding out to nearby unreformed rulers much faster than before. Before 1000 every Norse ruler was either Catholic or Waldensian. By 1100 Russia was entirely Orthodox and Kuzar. By 1200 there were only half a dozen pagan kings in the Altay Region. Even Mongolia converted to Manicheism and Taoism. Apostolics seems to be resisting for longer, by 1200 they pretty much control Armenia in its entirety. - Army numbers and gold accumulated is WAAAY higher it seems. By 1100 Abassids had 100k troops, Francia and Byzantium had 50k, and many other kingdoms had more than 15k. Reconquering kingdoms from siblings seems to be happening much more frequently for the AI. Africa split multiple times during sucession and at every generation it was reunited, the same with Persia, Khorasan, and the Samanids. Well, this is what I've seem for now. It looks more stable overall, but I can't say how that will influence a playthrough. I THINK it may become harder than how it was after the first 100 years or so, which is fine, because that was when the game just became so easy you would be able to correct every mistake you did without hassle.

## Reply 100 — participant_072 · 2022-09-08 · post-28462529

<!-- artifact:quote:start -->
> Luka031 said: - Satisfied community thirstiness for Bohemond Bruh i saw the reddit post. Funniest thing ever Click to expand...
<!-- artifact:quote:end -->
I was wondering what this was about. Do you have a link to the thread/comment?

## Reply 101 — participant_036 · 2022-09-08 · post-28462557

<!-- artifact:quote:start -->
> Gnostiko said: I was wondering what this was about. Do you have a link to the thread/comment? Click to expand...
<!-- artifact:quote:end -->
https://www.reddit.com/r/CrusaderKings/comments/x79guj

## Reply 102 — participant_073 · 2022-09-09 · post-28462668

The decision to form the archduchy of Austria isn't fix ! It has been since Royal court that this one's bugged, and the ticket in the bug forum closed.

## Reply 103 — participant_074 · 2022-09-09 · post-28462687

<!-- artifact:quote:start -->
> Chip Block said: if you want an even better bug: the counter system for men at arms is reversed, so units are countered by the unit types they are supposed to counter Click to expand...
<!-- artifact:quote:end -->
Amazed no one has followed up on this, are you saying that was introduced in this patch or resolved by it? Or neither

## Reply 104 — participant_075 · 2022-09-09 · post-28462770

<!-- artifact:quote:start -->
> sidestep said: Convert to the faction's culture and/or faith and join the war on the side of the rebels Click to expand...
<!-- artifact:quote:end -->
"I was always a Zoroastrian Persian, whatever gave you the idea I was some Arab from the Caliphate?"

## Reply 105 — participant_076 · 2022-09-09 · post-28462838

great update but now EPE is broken so no ck3 for a few weeks

## Reply 106 — participant_077 · 2022-09-09 · post-28463031

Excited for the improvements to the AI.

## Reply 107 — participant_078 · 2022-09-09 · post-28463182

Great stuff. One question: Will previous Events be reworked to work within the new memory system? thanks. Looking forward to playing

## Reply 108 — participant_079 · 2022-09-09 · post-28463575

<!-- artifact:quote:start -->
> Chip Block said: if you want an even better bug: the counter system for men at arms is reversed, so units are countered by the unit types they are supposed to counter Click to expand...
<!-- artifact:quote:end -->
I’m testing it now, it does not seem to be the case. Do you have a link to the original bug report and a way to reproduce this issue?

## Reply 109 — participant_004 · 2022-09-09 · post-28463892

<!-- artifact:quote:start -->
> Ilya Belkin said: I’m testing it now, it does not seem to be the case. Do you have a link to the original bug report and a way to reproduce this issue? Click to expand...
<!-- artifact:quote:end -->
i read it the other day, it's to do with efficiency CK III - Counter Efficiency appears to increase how badly your MAA is countered, not the enemy's Short summary of your issue Counter Efficiency appears to increase how badly your MAA is countered, not the enemy's Game Version 1.5.1 What OS are you playing on? Mac What platform are you using? Steam What DLC do you have... forum.paradoxplaza.com

## Reply 110 — participant_079 · 2022-09-09 · post-28464095

<!-- artifact:quote:start -->
> Chip Block said: i read it the other day, it's to do with efficiency Click to expand...
<!-- artifact:quote:end -->
Thank you, this is less impactful but still a very painful bug, strange it got so little upvote. Need to check for myself and see if any of the mods fixing it well. How about boosting the thread up?

## Reply 111 — participant_071 · 2022-09-09 · post-28464153

<!-- artifact:quote:start -->
> irohma86 said: Observed a 867 start and the AI seems to get pretty stable with kingdom-tier realms after the first 100 years. From 950 onwards there were minimal changes to the overall layot of my map, never seen that before. Some things I've noticed (observed a game until 1200~). ... Click to expand...
<!-- artifact:quote:end -->
I've seen my game up to the final day and here are my observations. - Kingdoms are even more stable late game. The amount of troops and gold accumulated by the AI seems to help keeping kingdoms from falling apart. After 1000s the only dissolutions I've noticed (outside Mongols) were for the Kingdom of Leon at some point around 1250~ and for one nation around the Indus River around 1300~ No other kingdom broke down, and their original formations from the 950~ were only truly disrupted by the Mongol Invasion. A new empire was formed which I've never seen before too, the Volga-Ural empire. - The Mongols are still somewhat weak, although they grew much more than in most previous games I've seen. In my playthrough, however, the Abbasids were so stable and powerful that the Mongols fought thrice against them and lost every time. They also struggled for about 20 years to conquer Transoxiana, as they had around 40k troops and the maturidi muslims from that kingdom had 50k+. In the end they've conquered half of Persia and as far as Ruthenia before breaking down. The Abbasids had 200k troops at some point during the invasion, no one in the map could challenge them. - The Abbasids, in fact, became truly powerful and never ever got close to dissolve. In previous saves I've noticed them lasting for a few centuries, but not enduring until the end date and finishing up with 250k troops and with a territory that spanned from Anatolia to the Indus River and also conquering the Horn region in Africa. The caliphs constantly got 50+ piety per month because of insane stacking of modifiers. One of the last calips was earning 110 monthly piety. Never seen such absurd amount even when I was playing Learning-focused dynasties myself. - Genghis Khan spawned as a Kuzar (or switched faith so fast I didn't even noticed). Those warmongering followers of judaims could not sustain their broken empire for long though. The Golden Horde immediately dissolved after their first ruler died. The Ilkhanate existed for about 3 years before dissolving as well. The Chagatai lasted longer but always weak and fending of invaders, dissolving after about 30 years or so. Mongolia lasted until the end, but with not even half of their De Jure territory. - When muslims finally consolidated a kingdom in Iberia they immediately conquered all of it. Their 60-size kingdom had twice the troop count and 50% more gold generated than that of Francia's empire with 200+ counties. That not counting mercenaries (which they contracted about 50k of them at one point). In general, it seems the changes not only brought stable kingdoms to play, but the changes for vassalization are benefiting muslims and making them much more stable and powerful than before. Starting from 867 the development growth is also much faster, by 1066 the major cities were already nearing 60 development and by 1300 Persia and Mesopotamia were almost entirely at 50+ development, with major hubs close to 100. Even the steppe had 20+ development in most counties. I've enjoyed the faster spread of organized religion, it finally feels more historical seeing the norse becoming christians, but I'm afraid the Tengrism is getting owned by Kuzarism in a fashion that makes the steppe a bit weird and is affecting the mongol horde late ingame.

## Reply 112 — participant_043 · 2022-09-09 · post-28464429

Interesting the biggest change I have been seeing is the Byzantine empire is routinely dissolving itself into multiple kingdoms if starting in the 800s. Since the byzantines are no more the Abbasids are free to well abbhorde.

## Reply 113 — participant_080 · 2022-09-09 · post-28464476

<!-- artifact:quote:start -->
> irohma86 said: I've seen my game up to the final day and here are my observations.... .... I've enjoyed the faster spread of organized religion, it finally feels more historical seeing the norse becoming christians, but I'm afraid the Tengrism is getting owned by Kuzarism in a fashion that makes the steppe a bit weird and is affecting the mongol horde late ingame. Click to expand...
<!-- artifact:quote:end -->
Thank you for sharing your test in these two posts, they were very informative. Some of my favourite game starts in ck2 were late bookmarks in the Escandinavia region playing unreformed pagans faiths threatened with extinction and make an attempt to resurge against the onslaught of christiniaty all around. Now, we don't get such bookmarks in ck3, but 1066 could now be fun in that way too.

## Reply 114 — participant_081 · 2022-09-09 · post-28464507

in this patch of before correct when mistaken no changes to raiding (more realistic AI behaviour and better defence options, realism), economy, buy/sell land, infrastructure, castle defence customisation &more clarity of transferring buildings from tribal to feudal?

## Reply 115 — participant_082 · 2022-09-09 · post-28464969

<!-- artifact:quote:start -->
> Prpht said: Is CK3 modding that harder? The game has an active player count similar to Stellaris and equal to roughly 50% of HoI4. Those are not bad numbers at all. What happened to that ambitious GoT mod and other similar projects? Click to expand...
<!-- artifact:quote:end -->
Modcon 2 Is happening soon

## Reply 116 — participant_083 · 2022-09-09 · post-28465015

1) When Are u going to add a modifier for women age marriages? It's really quick to do and it would improve a lot the game. There are a lot of dead houses because of useless marriages with over 50 years women. 2) there is a simple mod to manage knights and define with a check if heirs, councilors, husband can be knights. Please copy paste it and save our micromanaging time. 3) please make friendship and rivalry great (again ). Nice icons but what's the point if my friends declare war on me and nemesis brothers accept alliances ?

## Reply 117 — participant_084 · 2022-09-10 · post-28465205

<!-- artifact:quote:start -->
> kmh42 said: Still no fix to the saga in stone achivement? I don't wanna cheese this achievement. Click to expand...
<!-- artifact:quote:end -->
You can get it without cheese. I got it with the Sigurdr dynasty just playing normally. It took from 867 to 1205.

## Reply 118 — participant_085 · 2022-09-10 · post-28465372

<!-- artifact:quote:start -->
> BenjiAD1290 said: You can get it without cheese. I got it with the Sigurdr dynasty just playing normally. It took from 866 to 1205. Click to expand...
<!-- artifact:quote:end -->
you say you didnt cheese it, and yet you started a year earlier than everyone else!

## Reply 119 — participant_086 · 2022-09-10 · post-28466179

<!-- artifact:quote:start -->
> among other things, I also sit in a lot of meetings where I usually have a lot of wise and important things to say Click to expand...
<!-- artifact:quote:end -->
I sympathize with you.

## Reply 120 — participant_087 · 2022-09-10 · post-28466267

I really loved the DLC. I had to abandon my Denmark campaign but no worries, I'll come back to it later on. Fate of Iberia got really better with this DLC!!

## Reply 121 — participant_088 · 2022-09-10 · post-28467046

<!-- artifact:quote:start -->
> sidestep said: Reworked Populist Factions in order to improve their functionality, especially in regards to how they interact with player vassals: Vassals directly affected by a Populist Revolt now get a letter from the revolt leader, asking the vassal how they will respond to their demand. The vassal may: Join the war and help their liege Convert to the faction's culture and/or faith and join the war on the side of the rebels Stay out of the war and do nothing (though still risk losing land if the liege loses the war) AI vassals are most likely to join the war on the side of their liege, but can in rare cases pick either of the other two options Made it so that AI lieges will never accept the faction demand if a player vassal is targeted by the faction (this will finally allow player vassals to intervene and help protect their own realm) Greatly increased the military strength of Populist Factions, to compensate for the fact that vassals can join the war: Populist armies now spawn a few basic Men-at-Arms in addition to levies Populist armies spawn Siege Weapons depending on their culture's innovations, allowing them to better scale into the late game Populist factions now generate a few commanders to lead their troops The populist leader will now get some extra gold upon victory, to ensure that they can afford creating titles and Men-at-Arms Reduced the rate at which factions gain discontent for being over the military power threshold. In practice, this will give rulers a longer time to react before factions press their ultimatum (especially when the faction is only slightly stronger than their target) A successful Populist Faction will no longer usurp or create an existing title if they don't control at least 50% of its De Jure (this is to prevent titles from being usurped too easily) Increased the restrictions for a successful Populist Faction to create custom kingdoms and duchies. They will primarily attempt to create a title without a holder or usurp an existing title Rulers participating in a Populist Faction will now become independent if they have too high a rank to be vassalized by the populist leader, instead of remaining a vassal to their old liege The leader of a successful Populist Faction should no longer steal counties from rulers joining the revolt Click to expand...
<!-- artifact:quote:end -->
I feel like every new set of patch notes promises to fix Populist Factions, and they never do. Here I switched to the AI Byzantines (things are not going well for them), and waited for their populist faction to send demands. Of particular interest is Doux Dragos of Macva, a member of the faction. What happens to him when we give into their demands? All of his lands are given to a randomly generated character! His Duchy title is *disolved*! How is it that we have seen *multiple successive patch notes* promise to fix this issue, and it is still so obviously present? Does no one check? Are the patch notes merely aspirational? What is going on?

## Reply 122 — participant_089 · 2022-09-11 · post-28467756

- The Petition event “Personal Matter” should no longer fire in a way that has you accusing yourself of infidelity This still happens because your spouse is still a valid target and will bring you with her to the event. In order to fix it you need to do a "Not = { spouse_of = root } on all triggers.

## Reply 123 — participant_090 · 2022-09-11 · post-28468366

<!-- artifact:quote:start -->
> Voy said: - The Petition event “Personal Matter” should no longer fire in a way that has you accusing yourself of infidelity This still happens because your spouse is still a valid target and will bring you with her to the event. In order to fix it you need to do a "Not = { spouse_of = root } on all triggers. Click to expand...
<!-- artifact:quote:end -->
Yes. If your Spouse wants to confront you over any improprieties you may have committed, she'd be far more likely to do it privately. Like CK2 had the option for you to privately talk to someone about how they were eating too much...

## Reply 124 — participant_091 · 2022-09-11 · post-28468654

Another W update with a pretty good dlc! idk guys five bucks for over 100 events that interconnect with eachother isn't that bad especially when the content isn't needed to play! it is literally just events! I find the hate the dlc is getting to be astronomically overblown and thank the devs for writing over 100 events to provide more flavour and content alongside this massive and expansive update. This game is gonna go far with its current dlc policy - here is to hoping for another season pass and more great content! keep it up!

## Reply 125 — participant_004 · 2022-09-12 · post-28470109

whats the new update

## Reply 126 — participant_017 · 2022-09-12 · post-28470338

Hotfix for CPU problems.

## Reply 127 — participant_032 · 2022-09-15 · post-28477292

<!-- artifact:quote:start -->
> Voodoo Lilium said: I have got to ask... how the hell did that even happen??? Click to expand...
<!-- artifact:quote:end -->
I can't really go into detail, but rest assured that it was due to a quite arcane piece of code that we rarely use and rarely change that had a little "boo-boo" in it. We were all very confused until we figured it out.

## Reply 128 — participant_032 · 2022-09-15 · post-28477298

<!-- artifact:quote:start -->
> meii said: Imma buy this just cuz i like Tech Lead Zac. Yall should put Zac in charge of making dev diaries from now on for profit Click to expand...
<!-- artifact:quote:end -->
Haha, thank you ^^ I'll bring this up in our leads team...for profit!

## Reply 129 — participant_032 · 2022-09-15 · post-28477301

<!-- artifact:quote:start -->
> Diamonds said: What version control are you using? Click to expand...
<!-- artifact:quote:end -->
we use Git, which is very powerful but, as they say, with great power comes great responsibility ( and potential for screwing up )

## Reply 130 — participant_004 · 2022-09-15 · post-28477303

<!-- artifact:quote:start -->
> sidestep said: we use Git, which is very powerful but, as they say, with great power comes great responsibility ( and potential for screwing up ) Click to expand...
<!-- artifact:quote:end -->
plz fix the coat of arms duplicate bug

## Reply 131 — participant_032 · 2022-09-15 · post-28477308

<!-- artifact:quote:start -->
> Draakbeest said: I sympathize with you. Click to expand...
<!-- artifact:quote:end -->
Thank you, but I have only myself to blame really...mostly.

## Reply 132 — participant_032 · 2022-09-15 · post-28477310

<!-- artifact:quote:start -->
> Chip Block said: plz fix the coat of arms duplicate bug Click to expand...
<!-- artifact:quote:end -->
This is part of the new 1.7.1 update that just went out

## Reply 133 — participant_004 · 2022-09-15 · post-28477318

<!-- artifact:quote:start -->
> sidestep said: This is part of the new 1.7.1 update that just went out Click to expand...
<!-- artifact:quote:end -->
oh i missed this! thank you

## Reply 134 — participant_092 · 2022-09-17 · post-28482225

<!-- artifact:quote:start -->
> Adamus Petius Jusus said: Any specific reason for that change? I feel like that never was a problem and it seems very easy now. Click to expand...
<!-- artifact:quote:end -->
for those of us who don't like to take over the world it lets us use a feature..

