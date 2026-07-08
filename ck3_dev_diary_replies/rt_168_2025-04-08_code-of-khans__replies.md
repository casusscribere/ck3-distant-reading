---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1734805/"
forum_thread_id: 1734805
content_type: reply_thread
parent_dd_file: dd_168_2025-04-08_code-of-khans.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 168
title: "Dev Diary #168 - Code of Khans"
dd_date: 2025-04-08
expansion: Khans of the Steppe
patch: Patch 1.16
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 4
reply_count: 75
participant_count: 50
reply_date_first: 2025-04-08
reply_date_last: 2025-04-22
body_word_count: 4238
inline_image_count: 0
quoted_span_count: 43
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Dev Diary #168 - Code of Khans

*75 replies from 50 participants across 4 pages*

## Reply 1 — participant_001 · 2025-04-08 · post-30279914

slightly off-topic. I am mongolian. I've been playing ck3 since the release even before Royal Court. I've been waiting for this since northern lords. Though, there are few things bothers me as a mongolian and history buff. 1) Borjigin family line In the game currently, all the brothers and mother of Bodanchar Munkhag is borjigin which is wrong and when he becomes a bastard founder he becomes "Munkhagid". like Munkhag means a fool. House Munkhagid sounds like house "Foolish". His mother Alan Gua had 2 sons from her late husband, and had 3 sons after her husband passed away - that's why Bodanchar is named Bodanchar -- it comes from a word бутач meaning bastard. He finds the house Borjigin. His brothers find different houses. Specifically, Bukha Khatagi founded house Khatagan, Bukhatu Salji founded house Salji'ud. 2) Potential story lines Bodanchar didn't go along with his brothers he was expelled to fend for himself alone at some point. I advise reading or finding a translation for a passage called "Боданчар Богд", It is story reimagining his life. in the game he could start as an adventurer, become a lord. When that happens he will found the Borjigin line. Also if you find the house borjigin, and play until 1100s, there could be an event where your son can born with a blood clot in his hands which can be an omen and status boost making him more likely to become a Khan. And only that Character can become "Chinghis Khan". All other houses could become "Gur Khan", title Jamukha took. Also I advise reading a passage called "Жамухын Өчил" where Jamukha is captured and Genghis khan wants to pardon him but Jamukha asks to be executed. The Temujin and Jamukha event story line could be most heartbreaking storyline if done right. From friends to best friends to enemies. Also in later start dates it would be cool to start with Temujin having house feud with powerful clans, Tatars, Mergids, and etc. 3) Mechanics Tribe feuds. There should be system where wheh each tribe raids another tribe and kills a house member and feud starting, fading away or worsening. system should count how many people they lost, mechanics to start or end one. and bride stealing. Events where enemy soldiers could be recruited after a battle won. Also when china comes in the game ther should be mechanic for chinese dynasties to pay tribes to protect from raiders or attack other tribe. 4) Nittpicking Alan Gua sounds bit innappriorate for me personally. How about Алунгоо, Alungoo or Alun Gua. Al, "Ал" means "female genetalia" in mongolian and not in a polite manner. Also her dead husbands line go way up about ten or more generations until Borte Chono and Gua Maral. I mean byzantine empire title go way up until Augustus why not do the same for Mongolians. Further more Alungoo's late husband's brother had 4 sons who founded the oirats. So it would be cool family tree to connect the houses. Also one last thing, mongolian faces don't really look mongolian they look weird. Idk if its me but please look into it. 5) I'm very excited for this chapter. and I am most grateful to you guys for being awesome developers. Thank you, and good luck.

## Reply 2 — participant_002 · 2025-04-08 · post-30279927

Thanks a lot for supporting modding! Modding community for ck is great and deserves all support and praise!

## Reply 3 — participant_003 · 2025-04-08 · post-30279928

This looks cool, thank you as always for a look behind the curtain! Some questions, including a repeat from last time: Is there / will there be a way to designate some titles as coming after a name rather than before it - e.g. the title Khan? Will herders ever be selected from existing characters during a migration, or are they always generated fresh? Will struggles be brought into situation code at some point, for simplicity / portability? Are any struggles planned in Chapter IV? Is it possible (in code) for any character to have multiple different domiciles. To ask a different way, whilst all current domiciles are tied to title & government type, is it possible to tie them to something else (as well)?

## Reply 4 — participant_004 · 2025-04-08 · post-30279932

I'm not sure to understand how the Situations works. For example, when you add another region to the Steppe, do you use start_situation (with type = eastern/central/eastern_steppe) ? Or is there another effect to add subregions to an already started situation? Great DD btw

## Reply 5 — participant_005 · 2025-04-08 · post-30279937

On the subject of modding, what I'd really like to see added is a global multiplier of the sum the percentages that increase the different values like prestige/piety/levy size. So instead of having another percentage just like all others, It will be one that affects the total. Modifier stacking is a huge reason why many regard this game as very easy, and since Devs seem hesitant to make some of the requested changes, I'd really appreciate if they'd give modders some way to decrease the percentage of resources that veterans can easily accumulate.

## Reply 6 — participant_006 · 2025-04-08 · post-30279940

Is de jure less important for nomads? As they are designed to migrate a lot, it would be kind of strange if a vassal moves his camp accross the river and suddenly starts to hate me.

## Reply 7 — participant_007 · 2025-04-08 · post-30279942

<!-- artifact:quote:start -->
> zhabavon said: Also her dead husbands line go way up about ten or more generations until Borte Chono and Gua Maral. I mean byzantine empire title go way up until Augustus why not do the same for Mongolians. Click to expand...
<!-- artifact:quote:end -->
Not sure that's comparable since Augustus and the other Emperors are actual historical people while Alun Gua herself is a mythological figure let alone any alleged ancestry. A more comparable situation would be them having the Rome history go back to Romulus and Remus who are mythological/legendary figures.

## Reply 8 — participant_008 · 2025-04-08 · post-30279945

<!-- artifact:quote:start -->
> PDX-Trinexx said: Situations We have implemented a new general system for supporting dynamic region-based gameplay, which we call the Situation system. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PDX-Trinexx said: Graphical Features - Bundled with the Situation system we also have some additional graphical features. Simple ones include the ability to define the map-color of specific sub-regions or participant groups. But more notably we have also added Map Province Effects - a way to apply an effect on the map based on the current Situation phase of a sub-region. These effects can be applied with a specific effect type and intensity (0.0 - 1.0), we bundle some effects out of the box in Khans of the Steppe: Drought, Summer, Snow - but mods could add more of course! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PDX-Trinexx said: View attachment 1278324 Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PDX-Trinexx said: Combat​For the combat-loving modders out there, we have added some commonly requested on-actions you can use to apply effects when combat starts, or when an army joins a combat. View attachment 1278334 Click to expand...
<!-- artifact:quote:end -->
This is good! Can Hundred Years' War be implemented with this? Please, add proper math expressions to scripting language. Something like Perl: if = { limit = { @(a + b * scope:char.age + sqrt(3)]) < 10 } # ... } # or if = { limit = { [[a + b * scope:char.age + sqrt(3)]] < 10 } # ... } # or if = { limit = { @@[a + b * scope:char.age + sqrt(3)] < 10 } # ... } Perl: scope:actor = { add_prestige = @(abs(scope:recipient.age - this.age) + log(this.age)) # or add_prestige = @{ abs(scope:recipient.age - this.age) + log(this.age) } } You have const expressions @[x + 1] but it is not the same. I wanted this for a long time!

## Reply 9 — participant_009 · 2025-04-08 · post-30279953

Are there fixes coming to how warscore from war goal is shown? Right now it's always shown from attackers perspective (as of, you as a defender get +10% from wargoal, but UI shows -10%) in some wars (or maybe all of them? Im not defending that often).

## Reply 10 — participant_010 · 2025-04-08 · post-30279976

I see the livestock, will they react on the different climates as well? Will a big Drought eventually see them lying dead on the map?

## Reply 11 — participant_011 · 2025-04-08 · post-30279979

Ok, were Situations mentioned before? Because that's the first time I heard of them and they sounds reall nice, this is actuall what I thought Struggles will be before it was revealed to be a heavily scripted thing and not procedually generated one. Nice to see this finally be realised. And offtopic from the theme, but not the topic, I gotta say that addition of masking in Coat of Arms Editor turns out to be a thing that's missing there, I realised it was a missing thing when I tried to edit slightly the flag of Slavia and by just selecting one element of that flag, it broke. In addition to that, I find it quite weird that we dont get to chose how banners with out COA looks like, as in the item for the court. Quite weird to see a banner you invision as continuous banner, but in the Court it is not only bordered, but also take only a small portion of the banner.

## Reply 12 — participant_012 · 2025-04-08 · post-30279993

Will we get the story circle of Temujin?

## Reply 13 — participant_013 · 2025-04-08 · post-30280003

<!-- artifact:quote:start -->
> With more hand-on experience with this system some previous technical decisions proved to be error-prone and hard to work with. So we decided to change how domiciles are connected to playable landless rulers. Domiciles are now owned not by a person, but by a special landless title. Click to expand...
<!-- artifact:quote:end -->
The important question is, how compatible the old 1.15 saves will be? I have a few playthroughs paused the day before the Mongols spawn specifically so that the *new* Genghis Khan and his (proper) nomadic horde would be spawned in by the event.

## Reply 14 — participant_014 · 2025-04-08 · post-30280014

<!-- artifact:quote:start -->
> zhabavon said: slightly off-topic. I am mongolian. I've been playing ck3 since the release even before Royal Court. I've been waiting for this since northern lords. Though, there are few things bothers me as a mongolian and history buff. 1) Borjigin family line In the game currently, all the brothers and mother of Bodanchar Munkhag is borjigin which is wrong and when he becomes a bastard founder he becomes "Munkhagid". like Munkhag means a fool. House Munkhagid sounds like house "Foolish". His mother Alan Gua had 2 sons from her late husband, and had 3 sons after her husband passed away - that's why Bodanchar is named Bodanchar -- it comes from a word бутач meaning bastard. He finds the house Borjigin. His brothers find different houses. Specifically, Bukha Khatagi founded house Khatagan, Bukhatu Salji founded house Salji'ud. 2) Potential story lines Bodanchar didn't go along with his brothers he was expelled to fend for himself alone at some point. I advise reading or finding a translation for a passage called "Боданчар Богд", It is story reimagining his life. in the game he could start as an adventurer, become a lord. When that happens he will found the Borjigin line. Also if you find the house borjigin, and play until 1100s, there could be an event where your son can born with a blood clot in his hands which can be an omen and status boost making him more likely to become a Khan. And only that Character can become "Chinghis Khan". All other houses could become "Gur Khan", title Jamukha took. Also I advise reading a passage called "Жамухын Өчил" where Jamukha is captured and Genghis khan wants to pardon him but Jamukha asks to be executed. The Temujin and Jamukha event story line could be most heartbreaking storyline if done right. From friends to best friends to enemies. Also in later start dates it would be cool to start with Temujin having house feud with powerful clans, Tatars, Mergids, and etc. 3) Mechanics Tribe feuds. There should be system where wheh each tribe raids another tribe and kills a house member and feud starting, fading away or worsening. system should count how many people they lost, mechanics to start or end one. and bride stealing. Events where enemy soldiers could be recruited after a battle won. Also when china comes in the game ther should be mechanic for chinese dynasties to pay tribes to protect from raiders or attack other tribe. 4) Nittpicking Alan Gua sounds bit innappriorate for me personally. How about Алунгоо, Alungoo or Alun Gua. Al, "Ал" means "female genetalia" in mongolian and not in a polite manner. Also her dead husbands line go way up about ten or more generations until Borte Chono and Gua Maral. I mean byzantine empire title go way up until Augustus why not do the same for Mongolians. Further more Alungoo's late husband's brother had 4 sons who founded the oirats. So it would be cool family tree to connect the houses. Also one last thing, mongolian faces don't really look mongolian they look weird. Idk if its me but please look into it. 5) I'm very excited for this chapter. and I am most grateful to you guys for being awesome developers. Thank you, and good luck. Click to expand...
<!-- artifact:quote:end -->
Since there is still no mention of allowing nomads to settle in your realms, will it even be possible to do it as a mod? I'm thinking something along the lines of settle adventurer can perhaps be done, but can that nomad then be kept as a nomad vassal after being settled in your realm? I am curious what does a Mongolian history buff thinks on Turkic groups not getting anything in this dlc especially considering Mongol army was primarily composed of various Turkic tribes.

## Reply 15 — participant_015 · 2025-04-08 · post-30280020

Hello, thank you. I have a concern regarding the 'situations' — aren't you afraid of creating confusion by having them coexist with the 'struggles'? I read that you don’t plan to modify them, but this will create a redundant layer, two mechanisms serving roughly the same purpose. Are you planning to leave it like that?

## Reply 16 — participant_016 · 2025-04-08 · post-30280027

Re: The Skeleton Update...Does that mean we will finally get houppelandes for when we get to the 14th and 15 Centuries?

## Reply 17 — participant_003 · 2025-04-08 · post-30280031

<!-- artifact:quote:start -->
> NGC224 said: The important question is, how compatible the old 1.15 saves will be? I have a few playthroughs paused the day before the Mongols spawn specifically so that the *new* Genghis Khan and his (proper) nomadic horde would be spawned in by the event. Click to expand...
<!-- artifact:quote:end -->
I'd always assume incompatibility at worst and "play at your own risk" at best between major patches, such as those accompanying DLC, especially those with new mechanics. The same was true for all prior ones.

## Reply 18 — participant_017 · 2025-04-08 · post-30280035

These are great news! I have a few questions: Are there character modifiers or province modifiers that can modify Herc Conversion, Gold from Herd and Herd Gain from County? These would be very useful to balance different governments that use herds. Just to be sure, you NEED a domicile to use/interact with herds, but you don't necessarily need to be landed, correct? Will unlanded characters with herds benefit from fertility on the province where their domicile is? Will mods need to change how domiciles work? For example, mods that add domiciles to feudals or theocracies will need to add titular titles just to hold these, or should it work naturally?

## Reply 19 — participant_018 · 2025-04-08 · post-30280047

Can a character belong to multiple situations? This new system is very interesting, and I would like to see if it's possible to combine, for example, a climate situation with a regional social situation. Also, can the raiding intent limit the targets that can be raided? For example, a "pirate" intent could only raid coastal counties, while a "religious" intent could only target rulers of an enemy religion, etc.

## Reply 20 — participant_019 · 2025-04-08 · post-30280054

I don't think this has been answered in previous dev diaries, can you tell us how cultures will work for nomads? They don't have promote culture task. Will their culture "spread" like with CK2 nomads, or in a different way?

## Reply 21 — participant_020 · 2025-04-08 · post-30280055

<!-- artifact:quote:start -->
> Trovador said: Will mods need to change how domiciles work? For example, mods that add domiciles to feudals or theocracies will need to add titular titles just to hold these, or should it work naturally? Click to expand...
<!-- artifact:quote:end -->
Correct. Effects that create/destroy domiciles directly are removed, instead you use an effect to create a landless title with a government type that has a domicile associated with it

## Reply 22 — participant_020 · 2025-04-08 · post-30280056

<!-- artifact:quote:start -->
> Asterios_III said: Can a character belong to multiple situations? Click to expand...
<!-- artifact:quote:end -->
Yes, they can

## Reply 23 — participant_020 · 2025-04-08 · post-30280062

<!-- artifact:quote:start -->
> rasuuru said: Please, add proper math expressions to scripting language. Click to expand...
<!-- artifact:quote:end -->
No, too much effort for such a complex feature. Maybe some other new PDS game will do that eventually, not CK3. I doubt there'll be a champion to do that in their free time

## Reply 24 — participant_021 · 2025-04-08 · post-30280068

Governments can be sticky now ? What does that entail ?

## Reply 25 — participant_022 · 2025-04-08 · post-30280073

Devs: explaining some (probably not very) complicated math Me, a genius modder: And thank god for the combat effects, oh my heavens, that's so amazing.

## Reply 26 — participant_023 · 2025-04-08 · post-30280101

Can we see the code that transforms horde riders into MaA and whether or not a similar system could be implemented into levies?

## Reply 27 — participant_024 · 2025-04-08 · post-30280122

I still don't get those Fertility modifiers. Why don't you show the Equilibrium in the tooltip? And I also do not get the difference between Struggles and Situations, mechanically speaking. A cursory read tells me they're functionally the same and the former could be adapted into the latter. What am I missing?

## Reply 28 — participant_025 · 2025-04-08 · post-30280131

So I am correct, that a tributary, can only be of a level below you? Just like a duke-level steppe ruler can only have county-level tributaries?

## Reply 29 — participant_026 · 2025-04-08 · post-30280132

<!-- artifact:quote:start -->
> rasuuru said: Please, add proper math expressions to scripting language. Something like Perl: if = { limit = { @(a + b * scope:char.age + sqrt(3)]) < 10 } # ... } # or if = { limit = { [[a + b * scope:char.age + sqrt(3)]] < 10 } # ... } # or if = { limit = { @@[a + b * scope:char.age + sqrt(3)] < 10 } # ... } Perl: scope:actor = { add_prestige = @(abs(scope:recipient.age - this.age) + log(this.age)) # or add_prestige = @{ abs(scope:recipient.age - this.age) + log(this.age) } } You have const expressions @[x + 1] but it is not the same. Click to expand...
<!-- artifact:quote:end -->
Math inlined in script like this is indeed very limited in what it can do, but we use scripted math for this purpose all the time. If you're not aware, you can define a scripted calculated value in script_values and perform all these operations in sequence, even switch what algorithm or steps you use depending on scripted logic. Obedience, for example, is a fully scripted value in KotS, and while it may look like simple additive modifiers in most cases it's not limited to just that. Note that instead of log you have to use exp and invert.

## Reply 30 — participant_027 · 2025-04-08 · post-30280149

Good dev diary. Thanks for the breakdown of the new game system.

## Reply 31 — participant_020 · 2025-04-08 · post-30280153

<!-- artifact:quote:start -->
> Veldmaarschalk said: So I am correct, that a tributary, can only be of a level below you? Just like a duke-level steppe ruler can only have county-level tributaries? Click to expand...
<!-- artifact:quote:end -->
No, there's no such limitation on tributaries, as well as the length of tributaries chain can be very long

## Reply 32 — participant_020 · 2025-04-08 · post-30280191

<!-- artifact:quote:start -->
> Alratan said: This looks cool, thank you as always for a look behind the curtain! Some questions, including a repeat from last time: Will struggles be brought into situation code at some point, for simplicity / portability? Are any struggles planned in Chapter IV? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Inspecta said: Ok, were Situations mentioned before? Because that's the first time I heard of them and they sounds reall nice, this is actuall what I thought Struggles will be before it was revealed to be a heavily scripted thing and not procedually generated one. Nice to see this finally be realised. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Beauarien said: Hello, thank you. I have a concern regarding the 'situations' — aren't you afraid of creating confusion by having them coexist with the 'struggles'? I read that you don’t plan to modify them, but this will create a redundant layer, two mechanisms serving roughly the same purpose. Are you planning to leave it like that? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> FleetingRain said: And I also do not get the difference between Struggles and Situations, mechanically speaking. A cursory read tells me they're functionally the same and the former could be adapted into the latter. What am I missing? Click to expand...
<!-- artifact:quote:end -->
Existing struggles will remain in the game as is, along with code support and modding features for it. There's enough differences between the systems to make transition of old content too risky and error-prone for very little benefit. All new content will be in the form of situations. Think of it as evolution of old struggles system into a better situations system. Sometimes the only way to get an insight about how to make a good generic system - it to make lots of various use cases for it. Old struggles were only 2 examples with very specially tailored features. It was hard to scale it up and expand in the way designers need it now for Chapter 3. That's the reason for a fresh start

## Reply 33 — participant_003 · 2025-04-08 · post-30280213

<!-- artifact:quote:start -->
> Alien-47 said: Existing struggles will remain in the game as is, along with code support and modding features for it. There's enough differences between the systems to make transition of old content too risky and error-prone for very little benefit. All new content will be in the form of situations. Think of it as evolution of old struggles system into a better situations system. Sometimes the only way to get an insight about how to make a good generic system - it to make lots of various use cases for it. Old struggles were only 2 examples with very specially tailored features. It was hard to scale it up and expand in the way designers need it now for Chapter 3. That's the reason for a fresh start Click to expand...
<!-- artifact:quote:end -->
That's very good to know, and it makes perfect sense - thanks! As a follow-up, are there any Situations planned in Chapter 4 which have a Struggle-like ending - i.e. not just the permanently active seasons system? Also, copying my other questions for any other devs to answer if they just skim the thread. Is there / will there be a way to designate some titles as coming after a name rather than before it - e.g. the title Khan? Will herders ever be selected from existing characters during a migration, or are they always generated fresh? Will struggles be brought into situation code at some point, for simplicity / portability? Are any struggles planned in Chapter IV? Is it possible (in code) for any character to have multiple different domiciles. To ask a different way, whilst all current domiciles are tied to title & government type, is it possible to tie them to something else (as well)?

## Reply 34 — participant_020 · 2025-04-08 · post-30280226

<!-- artifact:quote:start -->
> Alratan said: Is it possible (in code) for any character to have multiple different domiciles. To ask a different way, whilst all current domiciles are tied to title & government type, is it possible to tie them to something else (as well)? Click to expand...
<!-- artifact:quote:end -->
Yes and no. In order to keep existing script and content working, game's code and UI still treats only one domicile as active and current one - that one is used in links and triggers. On the other hand there's a new link from title to a domicile - so you can iterate over ruler's domain and try to do things on multiple domiciles that way. It was one of the potential benefits of the rework - not being limited by 1 domicile per person in theory. But as of now for release of Khans of the Steppe there's no promises and official support for multiple domiciles

## Reply 35 — participant_028 · 2025-04-08 · post-30280234

<!-- artifact:quote:start -->
> Alien-47 said: Existing struggles will remain in the game as is, along with code support and modding features for it. There's enough differences between the systems to make transition of old content too risky and error-prone for very little benefit. All new content will be in the form of situations. Think of it as evolution of old struggles system into a better situations system. Sometimes the only way to get an insight about how to make a good generic system - it to make lots of various use cases for it. Old struggles were only 2 examples with very specially tailored features. It was hard to scale it up and expand in the way designers need it now for Chapter 3. That's the reason for a fresh start Click to expand...
<!-- artifact:quote:end -->
Does this mean that new struggles going forward would use the situation system or that there are no planned new struggles going forward?

## Reply 36 — participant_020 · 2025-04-08 · post-30280245

<!-- artifact:quote:start -->
> IIXBatmanXII said: Does this mean that new struggles going forward would use the situation system or that there are no planned new struggles going forward? Click to expand...
<!-- artifact:quote:end -->
I think there's a conflation of 2 separate things. There's code and script mechanics called old struggles and new situations that helps drive game content. There will be no new game content that uses old struggles code and script. There's game content about people having political struggles in various parts of the world. I don't know what kind of content about politics and people will be made in the future, whatever that content is going to be, it'll be based on the new situations system.

## Reply 37 — participant_029 · 2025-04-08 · post-30280257

It was shown in the earlier dev diaries that the Steppe could be "expanded" to cover other regions through a decision. I suspect that that decision uses this new start_situation effect, with the dynamic sub_region creation depending on which region you chose for the decision. When this is taken, will that new "Steppe" region appear in the same Great Steppe UI window shown before (possibly adding a scroll bar or something if a lot of regions are present), or will each new region get its own separate UI window?

## Reply 38 — participant_028 · 2025-04-08 · post-30280299

<!-- artifact:quote:start -->
> Alien-47 said: I think there's a conflation of 2 separate things. There's code and script mechanics called old struggles and new situations that helps drive game content. There will be no new game content that uses old struggles code and script. There's game content about people having political struggles in various parts of the world. I don't know what kind of content about politics and people will be made in the future, whatever that content is going to be, it'll be based on the new situations system. Click to expand...
<!-- artifact:quote:end -->
I think that answers my question. Basically all “struggles” going forward will be coded as situations, though the old ones for Iberia and Persia remain as they were originally coded.

## Reply 39 — participant_023 · 2025-04-08 · post-30280306

Perhaps for those of us who are truly mad, allow in code vassal held tributaries and tributary loops. It may break things yes, but it may also prove useful. Perhaps have a separate check where if a tributary loop does happen, remove map effects.

## Reply 40 — participant_030 · 2025-04-08 · post-30280311

<!-- artifact:quote:start -->
> PDX-Trinexx said: County Fertility Decline is changed according to this function: [County Fertility Decline Equation and Graph] [Defines for affecting how County Fertility Change behaves] Click to expand...
<!-- artifact:quote:end -->
Well, since you have used trigonometric function (which is periodic), if COUNTY_FERTILITY_DECLINE_FACTOR is greater than 1, maybe there will be something strange to happen?

## Reply 41 — participant_031 · 2025-04-08 · post-30280353

The combat changes look great, could they be used to make a commander trait that gives like - friendly casualties + screen +% chance to skip pursuit to model guerilla warfare? Also this reminds me, since Yurts are domiciles are they immune to siege and raiding?

## Reply 42 — participant_020 · 2025-04-08 · post-30280369

<!-- artifact:quote:start -->
> Slime99 said: Perhaps for those of us who are truly mad, allow in code vassal held tributaries and tributary loops. It may break things yes, but it may also prove useful. Perhaps have a separate check where if a tributary loop does happen, remove map effects. Click to expand...
<!-- artifact:quote:end -->
It will simply crash the game, so no. We tried. Unintentionally.

## Reply 43 — participant_022 · 2025-04-08 · post-30280392

Are there more script effects for combat than the ones shown? Are there any effects that, for example, kill men or increase the damage multipliers of armies in the middle of a fight? I have tried to mod such a thing in myself using the battle events in a janky way, and, if I remember correctly, the only way I had to really affect armies was to give the army owners' character modifiers, but couldn't actually apply character modifiers to already engaged army owners (or they worked unreliably or something). If there is an effect to remove soldiers or use modifiers that affect combat while already in combat, it would be really cool.

## Reply 44 — participant_028 · 2025-04-08 · post-30280420

<!-- artifact:quote:start -->
> DONGHAIZHIDABIE said: Will we get the story circle of Temujin? Click to expand...
<!-- artifact:quote:end -->
I believe the last Khans of the Steppy livestream teased his story with his wife having been kidnapped, etc., though they didn’t want to show it because otherwise everyone already knows the event cycle before the release.

## Reply 45 — participant_032 · 2025-04-08 · post-30280439

Well this confirms Iberian Struggle will remain an obsolete and annoying system for the rest of the development cycle. Being my favorite region this makes me sad.

## Reply 46 — participant_028 · 2025-04-08 · post-30280440

<!-- artifact:quote:start -->
> Inspecta said: Ok, were Situations mentioned before? Because that's the first time I heard of them and they sounds reall nice, this is actuall what I thought Struggles will be before it was revealed to be a heavily scripted thing and not procedually generated one. Nice to see this finally be realised. Click to expand...
<!-- artifact:quote:end -->
The situations were sorta revealed last dev diary or the one before in screenshots but not addressed. In the comments we got the answer to what they were since the screenshots said, for instance, “becomes part of the Great Steppe Situation”.

## Reply 47 — participant_023 · 2025-04-08 · post-30280466

<!-- artifact:quote:start -->
> Alien-47 said: It will simply crash the game, so no. We tried. Unintentionally. Click to expand...
<!-- artifact:quote:end -->
Aww. What about vassal held tributaries? With the caveat that the tributaries are independent.

## Reply 48 — participant_033 · 2025-04-08 · post-30280472

I've asked this on the previous Dev diary but I'm going to ask it again today, but please add the pastoralist tradition to the Pulaar culture, it's the basis of Fulani culture and history.

## Reply 49 — participant_015 · 2025-04-08 · post-30280560

<!-- artifact:quote:start -->
> Alien-47 said: Existing struggles will remain in the game as is, along with code support and modding features for it. There's enough differences between the systems to make transition of old content too risky and error-prone for very little benefit. All new content will be in the form of situations. Think of it as evolution of old struggles system into a better situations system. Sometimes the only way to get an insight about how to make a good generic system - it to make lots of various use cases for it. Old struggles were only 2 examples with very specially tailored features. It was hard to scale it up and expand in the way designers need it now for Chapter 3. That's the reason for a fresh start Click to expand...
<!-- artifact:quote:end -->
Thank you for your response regarding the company's policy on the matter. If I may, try to put yourself in the shoes of a player three or four years from now, who will be playing the game with all the DLCs and will have to understand that in this game, the mechanics for Spain and Persia are handled completely differently from the rest of the game, even to create completely identical situations... I think that will come across as a messy experience.

## Reply 50 — participant_034 · 2025-04-08 · post-30280616

By on action effects that apply to combat, would this mean you can set your armies to use "tactics" such as delaying an enemy army so it won't reinforce another army you want to destroy? Or having an army "commit" to a battle to the end to force a decisive victory on the field, etc. On a side note, will we see in the future the ability for armies to shelter within castles?

## Reply 51 — participant_035 · 2025-04-08 · post-30280665

What on earth were you thinking with the formulas for fertility? Someone on the team got really excited about the high school math he remembered and nobody else wanted to deal with him? It could be so much simpler with equivalent effect.

## Reply 52 — participant_036 · 2025-04-08 · post-30280683

<!-- artifact:quote:start -->
> luanmameili said: Well, since you have used trigonometric function (which is periodic), if COUNTY_FERTILITY_DECLINE_FACTOR is greater than 1, maybe there will be something strange to happen? View attachment 1278498 Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> IoannesBarbarus said: What on earth were you thinking with the formulas for fertility? Someone on the team got really excited about the high school math he remembered and nobody else wanted to deal with him? It could be so much simpler with equivalent effect. Click to expand...
<!-- artifact:quote:end -->
Strange things indeed, thanks to a small but significant typo. The formula should be COUNTY_FERTILITY_DECLINE_FACTOR * Sin ( PI * CurrentFertility / 200 ), not multiply the argument of sine function. Alas while we were busy restraining the person who suggested to model County Fertility using a modified Lennard-Jones potential another one snuck in and implemented this

## Reply 53 — participant_037 · 2025-04-08 · post-30280730

<!-- artifact:quote:start -->
> klanker said: Strange things indeed, thanks to a small but significant typo. The formula should be COUNTY_FERTILITY_DECLINE_FACTOR * Sin ( PI * CurrentFertility / 200 ), not multiply the argument of sine function. Alas while we were busy restraining the person who suggested to model County Fertility using a modified Lennard-Jones potential another one snuck in and implemented this Click to expand...
<!-- artifact:quote:end -->
Would it computationally not be much easier to use the derivative of the discrete logistics function? dfertility/dt = fertility_growth_rate * fertility * (1 - fertility / fertility_equilibrium). This combines the equation for the consumption and growth, reducing the necessary calculation. It work for fertility that is both above and below the equilibrium. Although I suppose merged the two sources may defeat the point. Additionally I had hoped to use this mechanics to simulate a population_number per country and figured the logistics function was the easiest way to model population growth. Alternatively, would it be possible to create a define for these functions?

## Reply 54 — participant_038 · 2025-04-08 · post-30280741

<!-- artifact:quote:start -->
> PDX-Trinexx said: Confederations​Confederations are a group of smaller independent rulers coming together, acting as allies in defense against greater threats. Creating one is simple using the “create_confederation” effect. View attachment 1278309 Confederations invalidate on a daily tick if they have fewer than two members, so after a confederation has been created another member must be added using “add_confederation_member” View attachment 1278310 Members of the confederation will skew their map color towards the color of the confederation creator based on the define “CONFEDERATION_REALM_COLOR_FACTOR”. Click to expand...
<!-- artifact:quote:end -->
Confederations all seem to follow the exact same parameters... is there no way to mod it so that we could represent things like trade leagues as confederations?

## Reply 55 — participant_039 · 2025-04-08 · post-30280836

<!-- artifact:quote:start -->
> PDX-Trinexx said: View attachment 1278306 -25 + 106 - 67 is 14, not 13 Click to expand...
<!-- artifact:quote:end -->
*(no text body — reaction-only or media-only post)*

## Reply 56 — participant_040 · 2025-04-08 · post-30280857

Are domiciles being deactivated automatically hardcoded because I would like to use the domicile changes for counties of great importance like Constantinople and Bagdhad to get around the duchy/special building limits.

## Reply 57 — participant_029 · 2025-04-09 · post-30281045

Participant groups seem to be a generalized form of the Involved/Interloper/etc. system from struggles. But the dev diary doesn't mention things like involved cultures/faiths. Out of curiosity, is it possible to save variables/lists in a specific situation scope in order to recreate the involved system from struggles, just more dynamic?

## Reply 58 — participant_041 · 2025-04-09 · post-30281055

<!-- artifact:quote:start -->
> tanner918 said: Participant groups seem to be a generalized form of the Involved/Interloper/etc. system from struggles. But the dev diary doesn't mention things like involved cultures/faiths. Out of curiosity, is it possible to save variables/lists in a specific situation scope in order to recreate the involved system from struggles, just more dynamic? Click to expand...
<!-- artifact:quote:end -->
I wonder if there's a way to make it fully custom like a situation where the only involved characters are dwarfs, or christians... great schism situation when?

## Reply 59 — participant_042 · 2025-04-09 · post-30281065

Will the situations for the seasons of the nomads of the Sahel, Arabia, and (hopefully) Sahara be able to receive snow? Because if so that's a problem, since last time I checked there wasn't much snow in the Sahara and Arabian deserts.

## Reply 60 — participant_043 · 2025-04-09 · post-30281084

I have almost no idea what's going on here, but it looks impressive.

## Reply 61 — participant_044 · 2025-04-09 · post-30281111

Ah it wouldn't be a CK3 DLC without old hardcoding leading to reinventing the wheel again.

## Reply 62 — participant_003 · 2025-04-09 · post-30281415

<!-- artifact:quote:start -->
> Cameron122 said: Are domiciles being deactivated automatically hardcoded because I would like to use the domicile changes for counties of great importance like Constantinople and Bagdhad to get around the duchy/special building limits. Click to expand...
<!-- artifact:quote:end -->
Presumably you could move around a special title whenever Constantinople changes hands?

## Reply 63 — participant_041 · 2025-04-09 · post-30281768

<!-- artifact:quote:start -->
> BeaverNation57 said: Will the situations for the seasons of the nomads of the Sahel, Arabia, and (hopefully) Sahara be able to receive snow? Because if so that's a problem, since last time I checked there wasn't much snow in the Sahara and Arabian deserts. Click to expand...
<!-- artifact:quote:end -->
They stated earlier that extra nomad regions will only get seasons that make sense. White zud won't happen in Sahara.

## Reply 64 — participant_045 · 2025-04-09 · post-30282570

<!-- artifact:quote:start -->
> PDX-Trinexx said: Domiciles​It is our second expansion that uses domiciles, and it introduces a new domicile type - nomadic camp. With more hand-on experience with this system some previous technical decisions proved to be error-prone and hard to work with. So we decided to change how domiciles are connected to playable landless rulers. Domiciles are now owned not by a person, but by a special landless title. Adventurers always have their camp title, landless noble families have noble family title, and nomads have a nomadic camp title. This solves several problems at once - domicile inheritance is now completely controlled by inheritance of special titles. No more cases when code has to decide for a ruler which of the 2 domiciles they should keep - their own or the one they inherited from someone else. Title can have no holder for some time, and when it gets a new holder at some point, domicile is returned back into the game - no risk of accidentally destroying a rich and build-up domicile due to an unfortunate succession. Nothing changes in script or UI - there’s still a direct connection between a ruler and active domicile they have. When a ruler holds several special titles with domiciles, only one of those domiciles will be active - the one that matches the ruler's government type. This shouldn’t normally happen in the base game though. Click to expand...
<!-- artifact:quote:end -->
Domiciles being tied to a title is what I expected when I heard about the mechanic initially, and I was pleasantly surprised that it didn't work that way. Instead, the mechanic was open to all sorts of potential expansions, both from code and modding perspective, like mutliple people in one noble family having estates. Or courtiers having estates. Or italians capturing a byzantine family estate after a war. Or buying and selling estates/camps freely like artifacts. It is all potentially possible - with the current code. Alas, all good things must come to an end. "Owner of XYZ Estate" "adventurer" placeholder titles, here we come.

## Reply 65 — participant_034 · 2025-04-10 · post-30283207

Can you allow Muslim Administration governments to use their dynasty name for their empires? When turning on administrative for the Abbasids and Fatimids, they show up as Arabian Empire and Egypt in game.

## Reply 66 — participant_009 · 2025-04-10 · post-30283364

<!-- artifact:quote:start -->
> Von Lauenburg said: like mutliple people in one noble family having estates. Or courtiers having estates. Or italians capturing a byzantine family estate after a war. Or buying and selling estates/camps freely like artifacts. It is all potentially possible - with the current code. Click to expand...
<!-- artifact:quote:end -->
Considering you would have to jank it in anyways, it's still possible, so what's the problem?

## Reply 67 — participant_045 · 2025-04-10 · post-30283376

<!-- artifact:quote:start -->
> Benismann said: Considering you would have to jank it in anyways, it's still possible, so what's the problem? Click to expand...
<!-- artifact:quote:end -->
It's not very janky when you can do this with one direct effect (setting domicile ownership), bypassing succession. It will be become very janky once you have to deal with the succession mess every time.

## Reply 68 — participant_046 · 2025-04-10 · post-30283562

Regarding the Asian expansion, I believe that groundbreaking optimization cannot currently be achieved. As the regions increase, the rise in computational load is inevitable. Therefore, I hope that a setting allowing specific regions to be turned on or off before starting the game can be provided, similar to the 'Smaller World Map' Mod.

## Reply 69 — participant_047 · 2025-04-10 · post-30283653

<!-- artifact:quote:start -->
> Kabiliam said: Regarding the Asian expansion, I believe that groundbreaking optimization cannot currently be achieved. Click to expand...
<!-- artifact:quote:end -->
You may well be correct. On what do you base this belief?

## Reply 70 — participant_009 · 2025-04-10 · post-30283829

<!-- artifact:quote:start -->
> Kabiliam said: Regarding the Asian expansion, I believe that groundbreaking optimization cannot currently be achieved. As the regions increase, the rise in computational load is inevitable. Therefore, I hope that a setting allowing specific regions to be turned on or off before starting the game can be provided, similar to the 'Smaller World Map' Mod. Click to expand...
<!-- artifact:quote:end -->
Then i believe you know nothing about the game and your first remark is void, because you can't change map after game launch at all

## Reply 71 — participant_048 · 2025-04-11 · post-30285043

<!-- artifact:quote:start -->
> Kabiliam said: Regarding the Asian expansion, I believe that groundbreaking optimization cannot currently be achieved. As the regions increase, the rise in computational load is inevitable. Therefore, I hope that a setting allowing specific regions to be turned on or off before starting the game can be provided, similar to the 'Smaller World Map' Mod. Click to expand...
<!-- artifact:quote:end -->
This would be a major capitulation and IMO should never, ever be considered by PDX. They should try to get performance right and should never treat some regions of the world as "optional". Gameplay systems and balance should be designed around the whole world existing, both for current stuff(like the Steppe) and later developments like Trade(as they said in the Q&A, having the east means we can have full trade routes and goods).

## Reply 72 — participant_023 · 2025-04-12 · post-30287452

Although confederation leaders won't be a thing in the base game, from my understanding they were implemented at one point. Maybe it could be left in as an unused mechanic for modding purposes only.

## Reply 73 — participant_006 · 2025-04-13 · post-30288609

The domicile part is kind of confusing. So is it now possible to make noble families and adventurers county-level? May be nice for modders working on duchy-level republics and theocracies.

## Reply 74 — participant_049 · 2025-04-21 · post-30300521

<!-- artifact:quote:start -->
> Von Lauenburg said: Domiciles being tied to a title is what I expected when I heard about the mechanic initially, and I was pleasantly surprised that it didn't work that way. Instead, the mechanic was open to all sorts of potential expansions, both from code and modding perspective, like mutliple people in one noble family having estates. Or courtiers having estates. Or italians capturing a byzantine family estate after a war. Or buying and selling estates/camps freely like artifacts. It is all potentially possible - with the current code. Alas, all good things must come to an end. "Owner of XYZ Estate" "adventurer" placeholder titles, here we come. Click to expand...
<!-- artifact:quote:end -->
Can't all your examples also be done with a title too? I'm not familiar with that part of modding. One noble family - multiple "estate" titles, create an estate title and give it to courtier (need a vassal like relationship to the title maybe here) Italians capturing the estate title along with a city. Buying /selling titles. Bonus is now one person may have multiple domicile titles, alas only one active for now.

## Reply 75 — participant_050 · 2025-04-22 · post-30303339

about the change with liege/suzerain/overlord So if we use any trigger with liege, we should have to all rewrite them by the overlord counterpart if we want to trigger on nomad and no nomad ? I am right ?

