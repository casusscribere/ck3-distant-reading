---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1410656/"
forum_thread_id: 1410656
content_type: reply_thread
parent_dd_file: dd_037_2020-08-11_dev-diary-37-making-mods.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 37
title: "CK3 Dev Diary #37 - Making Mods"
dd_date: 2020-08-11
expansion: Base game
patch: Crusader Kings III
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 11
reply_count: 200
participant_count: 100
reply_date_first: 2020-08-11
reply_date_last: 2020-10-20
body_word_count: 14084
inline_image_count: 0
quoted_span_count: 153
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — CK3 Dev Diary #37 - Making Mods

*200 replies from 100 participants across 11 pages*

## Reply 1 — participant_001 · 2020-08-11 · post-26791842

It's here wohoo! Reserving my seat so I can ask questions hehe. Didn't know you were a modder Matthew! You da bomb! How moddable is the mouse-over entries on a character? Are relationships still hard-coded? Can it be exposed as an entry like "set_relationship_with_player" so we can do our own relationship calculation if we want to (please :>)? How moddable is the text? Is it possible to create an entire new GUI window using the scripts? For example a new dynasty tree viewer. Okay possible with workaround. I assume that the character portrait is a GUI element and can be pasted anywhere just like other elements (buttons, texts)? is family related stuff included in the dynasty folder? do you have a portrait viewer or editor in game? can we add another base model or will it be restricted to only one?

## Reply 2 — participant_002 · 2020-08-11 · post-26791845

Oh yes. I was looking forward to this the most. Mods like Elder Kings are what made me find CK2 to begin with. I cant wait to see what mods and how they'll be like in CK3

## Reply 3 — participant_003 · 2020-08-11 · post-26791846

Good work

## Reply 4 — participant_004 · 2020-08-11 · post-26791852

Well, even though I understood less than 5% of that, I still find myself more excited for the game than I did before reading it. Odd.

## Reply 5 — participant_005 · 2020-08-11 · post-26791859

Thanks for this! This all looks very promising for the modding community.

## Reply 6 — participant_006 · 2020-08-11 · post-26791862

<!-- artifact:quote:start -->
> There are still some hard coded links with the interactions, specifically when it’s an interaction that’s needed to be used by the AI in a non-trivial manner. These interactions are all marked clearly, though, and if you attempt to remove them then the game will give you a warning when loading that it really needs this interaction so put it back please. This behaviour in fact applies to almost all hard coded database objects, not just those which are interactions. Click to expand...
<!-- artifact:quote:end -->
I will take a guess and say that marriage is still (mostly) hardcoded?

## Reply 7 — participant_007 · 2020-08-11 · post-26791873

Is there gonna be a dev diary about holy wars? Wouldn't it make more sense to explore the mechanics of the game first before diving into stuff like performance and modding?

## Reply 8 — participant_008 · 2020-08-11 · post-26791877

<!-- artifact:quote:start -->
> LeSingeAffame said: I will take a guess and say that marriage is still (mostly) hardcoded? Click to expand...
<!-- artifact:quote:end -->
Not really, it is one of the ones that if you remove the game will yell at you for but it is mostly decided in script who can marry who, the various extra effects of the interaction, who the AI can and prefers to marry etc.

## Reply 9 — participant_006 · 2020-08-11 · post-26791880

<!-- artifact:quote:start -->
> blackninja9939 said: Not really, it is one of the ones that if you remove the game will yell at you for but it is mostly decided in script who can marry who, the various extra effects of the interaction, who the AI can and prefers to marry etc. Click to expand...
<!-- artifact:quote:end -->
Oh, that's really nice!

## Reply 10 — participant_002 · 2020-08-11 · post-26791881

That's great to hear for fantasy mods really. Like when you don't want certain monster races to marry non monster races or the like. You know instead of having a jank script that auto divorces. So it's really awesome to see that being more flexible.

## Reply 11 — participant_009 · 2020-08-11 · post-26791891

This isn't directly linked to the content of either this dev diary or #30, but it's a question about modding, so... Perhaps my favorite mod for Crusader Kings 2 is the Game of Thrones mod, which (among other features) has dragons. As many of you on the forum likely know, the mod tracks dragons like characters—just like Chancellor Glitterhoof, Spymaster Mittens, and Sir Bearington. All of these nonhuman characters were possible with 2D portraits because you can just draw an animal or dragon and stick that in the project folder. However, CK3's portraits are human-shaped character models, and while there are many ways to alter proportions, facial structure, texture, etc, there's no indication that you can simply replace that model with another one (not that modeling and rigging a dragon model is a trivial task in the first place!) How do you see mods with nonhuman characters as a central feature, whether they be rulers' accessories (as with the GoT mod) or rulers in their own right (as with the Faerun mod and Pope Glitterhoof) faring in Crusader Kings 3?

## Reply 12 — participant_010 · 2020-08-11 · post-26791902

yay, that override system for modularising files is excellent, will allow so much more compatability between mods!

## Reply 13 — participant_011 · 2020-08-11 · post-26791913

Will there be an on_action that triggers at the start of pregnancy instead of when the trait shows up, or any way of altering the 'unborn' segment? I tried to make a mod to make more fertile and tall etc characters have more twins in CK2, but couldn't find a method that worked.

## Reply 14 — participant_012 · 2020-08-11 · post-26791914

i hope that this means that fantasy mods have more options to work with (specifically for mods with races)

## Reply 15 — participant_013 · 2020-08-11 · post-26791918

What about mods changing localisation files (like improved localisations for other languages)? Will they affect checksum? EDIT: Also, will the localisation files include things like character or dynasty names (like Imperator)?

## Reply 16 — participant_014 · 2020-08-11 · post-26791925

As a modder too, I really liked this DD! Thank you Howewer, I'd like to ask two questions: 1. About title localisations, the game'll handle it in the landed_title folder, just like in CK2 or in a similar way, like in EU4? 2. How can the game handle special characters, like č, š, ž ? CK2 had some limitation with that.

## Reply 17 — participant_015 · 2020-08-11 · post-26791933

<!-- artifact:quote:start -->
> blackninja9939 said: Combining Mods Combining multiple mods together has always been a bit tricky but I wanted to try and make some gains with compatibility so that it doesn’t require as many manual patches. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> blackninja9939 said: ai_accept_negotiation = yes/no # If the interaction is declined negotiations will start. We don't show "won't accept", etc. because there is still a possibility that the interaction will be accepted via negotiation event chain Click to expand...
<!-- artifact:quote:end -->
That's really great! What does that mean exactly? Are negotiation event chains something special? And of course the obvious two questions: Can barons be made playable (though buggy) via modding? Can other government types (theocracies for example) be made playable?

## Reply 18 — participant_016 · 2020-08-11 · post-26791937

Will you return to listing mod names in the filenames? Remember, people may have dozens of mods, so looking up Charlemagnes_Happy_Booze_Adventures.mod is a lot quicker than looking through forty mods that are ugc-with-a-number to find a specific mod. And, of course, if you need the numbers you can always combine them with ugc_123456789_Charlemagnes_Happy_Booze_Adventures.mod.

## Reply 19 — participant_017 · 2020-08-11 · post-26791949

Modders are going to have a field day, thanks for this week development dairy.

## Reply 20 — participant_018 · 2020-08-11 · post-26791950

Would it be possible to mod out auto-accepting when Hooks are used where applicable and instead fire a "X is asking for Y demanding a Hook. You can refuse this if you really want to, but if you don't have a good enough reason you'll suffer a harsh penalty." version of the normal interaction (e.g. a marriage request)? The lack of such an option has been a rather big annoyance for me ever since we got Favours in CK2, seeing as circumstances could have changed a lot by the time a Favour is called in (e.g. the other party could have been caught murdering your heir, sleeping with your wife, and/or forcing your daughter to become his concubine) and some requests might be unpalatable enough to rather take a Trucebreaker-size penalty (particularly if you're roleplaying a dishonest character that would go back on their word), so if it is possible to mod it in in CK3 that'd be a pretty big plus as far as I'm concerned...

## Reply 21 — participant_019 · 2020-08-11 · post-26791957

<!-- artifact:quote:start -->
> Lordy's said: Can barons be made playable (though buggy) via modding? Can other government types (theocracies for example) be made playable? Click to expand...
<!-- artifact:quote:end -->
I feel like this is for modders to figure out.

## Reply 22 — participant_020 · 2020-08-11 · post-26791971

How will map modding work? One of my biggest gripes with Imperator Rome modding was that the map, country, and history setup was all in a single massive setup file.

## Reply 23 — participant_008 · 2020-08-11 · post-26791988

<!-- artifact:quote:start -->
> DaStormDragon said: Will there be an on_action that triggers at the start of pregnancy instead of when the trait shows up, or any way of altering the 'unborn' segment? I tried to make a mod to make more fertile and tall etc characters have more twins in CK2, but couldn't find a method that worked. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Vityviktor said: What about mods changing localisation files (like improved localisations for other languages)? Will they affect checksum? EDIT: Also, will the localisation files include things like character or dynasty names (like Imperator)? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Sylas said: As a modder too, I really liked this DD! Thank you Howewer, I'd like to ask two questions: 1. About title localisations, the game'll handle it in the landed_title folder, just like in CK2 or in a similar way, like in EU4? 2. How can the game handle special characters, like č, š, ž ? CK2 had some limitation with that. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Tirenedon said: How will map modding work? One of my biggest gripes with Imperator Rome modding was that the map, country, and history setup was all in a single massive setup file. Click to expand...
<!-- artifact:quote:end -->
There is not one for the start of pregnancy I don't think, we have one for the mother and father when the pregnancy is revealed which adds the trait. We do have effects to modify the unborn character though such as setting if they are a known bastard, changing the assumed father, and setting the number of children. Localization and gui still effects the checksum yes as both need to be checked otherwise using the new more powerful gui and localization system mods could cause cheating and out of sync issues. 1. Not sure what you mean with that question to be honest 2. We should be able display those just fine We have a similar split of files like CK2 did with various map, province and history folders containing the files to change. Not a handful of massive csv files like Imperator has.

## Reply 24 — participant_014 · 2020-08-11 · post-26792009

<!-- artifact:quote:start -->
> blackninja9939 said: 1. Not sure what you mean with that question to be honest Click to expand...
<!-- artifact:quote:end -->
Oh, sorry for my english I'm referring to the landed_titlles.txt file, where you can mess with titles and culture specific localisations in CK2. It's works the same for CK3 too, or there is some separated file for the localisations?

## Reply 25 — participant_021 · 2020-08-11 · post-26792017

<!-- artifact:quote:start -->
> OOOOefpkwèfkweèf said: Is there gonna be a dev diary about holy wars? Wouldn't it make more sense to explore the mechanics of the game first before diving into stuff like performance and modding? Click to expand...
<!-- artifact:quote:end -->
The biggest part of our playerbase plays mods and never touch the basegame, thats why PDX focuses on the modding community so much. How many people play mods? Well, most achievements i have have been obtained by the 1% of the community so its a big number. The mechanics will be shown in time, we need the modders to understand the game so they can deliver good mods at launch

## Reply 26 — participant_022 · 2020-08-11 · post-26792022

I had hopes the DD would feature character model modding. Will there be possibilities to add/change textures, meshes and morphs (assuming morphs are used)? And the format/tools used.

## Reply 27 — participant_023 · 2020-08-11 · post-26792024

Looks like an awesome framework, as well as an awesome game! Can we mod holding types? Eg add a 4th type in addition to city, castle, temple?

## Reply 28 — participant_011 · 2020-08-11 · post-26792026

<!-- artifact:quote:start -->
> We do have effects to modify the unborn character though such as setting if they are a known bastard, changing the assumed father, and setting the number of children. Click to expand...
<!-- artifact:quote:end -->
Great! The last one sounds perfect.

## Reply 29 — participant_007 · 2020-08-11 · post-26792029

<!-- artifact:quote:start -->
> Kazanov said: The biggest part of our playerbase plays mods and never touch the basegame, thats why PDX focuses on the modding community so much. How many people play mods? Well, most achievements i have have been obtained by the 1% of the community so its a big number. The mechanics will be shown in time, we need the modders to understand the game so they can deliver good mods at launch Click to expand...
<!-- artifact:quote:end -->
Well it's not like the game is already released so even if they released the dev diary about modding a bit later it wouldn't really affect the development of mods much. Supposedly some mod makers got the game? I'm not sure about the validity of that but even if that's the case, they would have already probably gotten the gist of this. Also, i'm pretty certain that not everyone knows about modding, that's why the writer for this dev diary said it had a 'niche' appeal, a dev diary about mechanics would be much much more appealing for casual players which constitutes about 90% of Ck2 players.

## Reply 30 — participant_024 · 2020-08-11 · post-26792032

<!-- artifact:quote:start -->
> blackninja9939 said: 1. Not sure what you mean with that question to be honest Click to expand...
<!-- artifact:quote:end -->
Code: k_england_welsh:0 "Lloegyr" Or Code: k_england = { ... welsh="Lloegyr" ... d_essex ={ ... } ... }

## Reply 31 — participant_025 · 2020-08-11 · post-26792035

I don't know much about coding or modding, so please correct me if I'm wrong, but: does the "trait_level=1" bit mean that traits are now able to have different levels of intensity? As in, two characters have the Deceitful trait, but one is more deceitful than the other, for instance?

## Reply 32 — participant_011 · 2020-08-11 · post-26792042

<!-- artifact:quote:start -->
> Vivs said: I don't know much about coding or modding, so please correct me if I'm wrong, but: does the "trait_level=1" bit mean that traits are now able to have different levels of intensity? As in, two characters have the Deceitful trait, but one is more deceitful than the other, for instance? Click to expand...
<!-- artifact:quote:end -->
The devs said genetic traits had levels and could reinforce or dilute.

## Reply 33 — participant_007 · 2020-08-11 · post-26792044

<!-- artifact:quote:start -->
> Vivs said: I don't know much about coding or modding, so please correct me if I'm wrong, but: does the "trait_level=1" bit mean that traits are now able to have different levels of intensity? As in, two characters have the Deceitful trait, but one is more deceitful than the other, for instance? Click to expand...
<!-- artifact:quote:end -->
Probably something like scarred -> Grievously scarred -> Horrifically Scarred

## Reply 34 — participant_007 · 2020-08-11 · post-26792049

<!-- artifact:quote:start -->
> DaStormDragon said: The devs said genetic traits had levels and could reinforce or dilute. Click to expand...
<!-- artifact:quote:end -->
I'm pretty certain deceitful isn't a genetic trait. I think that by 'reinforce' and 'dilute' they meant inheritance of genetic traits. Like, you can reinforce the attractive trait in your family by marrying more attractive people, therefore making attractive more common in your dynasty. Something along those lines.

## Reply 35 — participant_026 · 2020-08-11 · post-26792050

<!-- artifact:quote:start -->
> Kazanov said: The biggest part of our playerbase plays mods and never touch the basegame, thats why PDX focuses on the modding community so much. How many people play mods? Well, most achievements i have have been obtained by the 1% of the community so its a big number. Click to expand...
<!-- artifact:quote:end -->
This is wrong. A minority uses mods and a minority play ironman. Most people don't do either.

## Reply 36 — participant_027 · 2020-08-11 · post-26792057

One of my favorite features in Imperator was the GUI array/list feature you added later. Is that also supported in CK3 or not yet?

## Reply 37 — participant_007 · 2020-08-11 · post-26792062

<!-- artifact:quote:start -->
> Nc-Rm said: One of my favorite features in Imperator was the GUI array/list feature you added later. Is that also supported in CK3 or not yet? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> blackninja9939 said: At its core our scripting language in Imperator and Crusader Kings III is based on an in-house grand strategy library called Jomini, which acts as a more GSG focused layer used on top of our Clausewitz engine. When Imperator released I posted a lot of information about the things that come directly from Jomini and which are shared between both games, so I would recommend checking out my Grand Jomini Modding Information Manuscript thread if you are an interested modder. Click to expand...
<!-- artifact:quote:end -->
Probably yes.

## Reply 38 — participant_028 · 2020-08-11 · post-26792078

Sees modable folder named "Deathreasons" *Quietly laughs inside brain*

## Reply 39 — participant_029 · 2020-08-11 · post-26792080

<!-- artifact:quote:start -->
> blackninja9939 said: View attachment 607492 [a custom alert] Click to expand...
<!-- artifact:quote:end -->
Well…if only I could have custom alerts also in IR, EU, HOI and Stellaris…

## Reply 40 — participant_027 · 2020-08-11 · post-26792085

<!-- artifact:quote:start -->
> Sindai said: This is wrong. A minority uses mods and a minority play ironman. Most people don't do either. Click to expand...
<!-- artifact:quote:end -->
This is not true for every game. HOI4 for example, a big portion of playerbase actually use mods. It depends on the game. The more moddable the game is, the more people use mods.

## Reply 41 — participant_030 · 2020-08-11 · post-26792092

Are the dimensions of individual flags and dynasticCOAs 128x128 again? Just want to know if I can recycle all my custom flags and COAs from CK2.

## Reply 42 — participant_025 · 2020-08-11 · post-26792098

<!-- artifact:quote:start -->
> DaStormDragon said: The devs said genetic traits had levels and could reinforce or dilute. Click to expand...
<!-- artifact:quote:end -->
Yes, but in the DD the trait in question was Lunatic (which is not genetic), and the "trait_level" thing seemed to be a universal descriptor, not limited to just genetic traits. That's why I imagined it may open the possibility of having "levels of intensity" for personality traits.

## Reply 43 — participant_031 · 2020-08-11 · post-26792123

Has the character id system been changed? Currently in CK2 it seems you can't use namespaces in events or characters (not in eu4) like in EU4. So every character has an id in certain ranges. I know you reworked events entirely, but what about this?

## Reply 44 — participant_032 · 2020-08-11 · post-26792133

I was wondering, this greater moddability that the Jomini layer allows. Does that also help on your end for developing new features in DLC? I can imagine it helps a lot of things like the GUI are as open to changes as they seem to me if you want to introduce new features that go a bit deeper then skins for units etc.

## Reply 45 — participant_001 · 2020-08-11 · post-26792154

Will there be a detailed guide on the new system (specifically for CK3) and a detailed guide on 3D portrait modding? The IR wiki didn't have this section.

## Reply 46 — participant_033 · 2020-08-11 · post-26792155

How moddable are succession laws? In that screenshot of the game directory there is only a folder for elective...

## Reply 47 — participant_002 · 2020-08-11 · post-26792163

<!-- artifact:quote:start -->
> Kazanov said: The biggest part of our playerbase plays mods Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Sindai said: This is wrong. A minority uses mods and a minority play ironman. Most people don't do either. Click to expand...
<!-- artifact:quote:end -->
Source? I'd like to know where these numbers are coming from unless they are purely guesses. I can only see steam achievements support the "minority play ironman" bit since only 16.2% of the playerbase has an achievement for marrying. Which is practically impossible not to do when playing CK2. I can see someone making a vague connection between ironman mode and playing with mods, but even I only played ironman once. Mods or not. Granted that's a sample size of literally just me.

## Reply 48 — participant_034 · 2020-08-11 · post-26792190

What is the resolution of the map files used in CK3?

## Reply 49 — participant_035 · 2020-08-11 · post-26792207

Do we still have to adhere to that stupid checksum for achievements? esp considering HIP is far superior to base ck2 but you cant get achievements from it

## Reply 50 — participant_021 · 2020-08-11 · post-26792213

<!-- artifact:quote:start -->
> LordofLight said: Source? I'd like to know where these numbers are coming from unless they are purely guesses. I can only see steam achievements support the "minority play ironman" bit since only 16.2% of the playerbase has an achievement for marrying. Which is practically impossible not to do when playing CK2. I can see someone making a vague connection between ironman mode and playing with mods, but even I only played ironman once. Mods or not. Granted that's a sample size of literally just me. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> As I talked about in the Mods and Mod Telemetry dev diary, we consider mods and modders to be a great thing for CK2. Mods increase the longevity of the game by letting people tweak it to their liking, to explore alternate scenarios, and alternate realities. At the time of writing, just under half (48%) of all players who played yesterday were using at least one mod, up from 42% when I wrote the Mods and Mod Telemetry dev diary. Click to expand...
<!-- artifact:quote:end -->
CK2 Dev Diary #58: Modding and a bit of optimization Good afternoon, all. I’m Magne “Meneth” Skjæran, the programmer on CK2. In the past I’ve written dev diaries about modding, optimization, and quality of life improvements, as well as last week’s dev diary talking about the life of a bug, and the... forum.paradoxplaza.com CK2 Dev Diary #49: Mods and mod telemetry Good evening, everyone. I’m Magne “Meneth” Skjæran, one of the programmers on CK2. In the past I’ve written dev diaries about modding, optimization, and quality of life improvements, and I'm writing this somewhat belated (due to technical issues)... forum.paradoxplaza.com So, if 48-42% of players use mods, and -+10% are Ironman players, almost 40%+- of players play vanilla. And Sindai said that a minority uses mods, which is not correct. At least me, if im not playing Ironman i just dont play vanilla, there is no point of playing that version of the game with so many awesome mods out there.

## Reply 51 — participant_036 · 2020-08-11 · post-26792225

<!-- artifact:quote:start -->
> Sute]{h said: What is the resolution of the map files used in CK3? Click to expand...
<!-- artifact:quote:end -->
the map files are 8192x4096 according to this bit in the developer answers thread ▲ What is the resolution of the map files? (asking for modding purposes) ► 8192x4096

## Reply 52 — participant_037 · 2020-08-11 · post-26792227

Read through the linked Jomini document and just want to give all praise to you and your fellows that have made that happen. It's an amazing achievement and I can only imagine how good it must feel to use internally and to share with the community.

## Reply 53 — participant_038 · 2020-08-11 · post-26792255

Still can't wait for 3D Khajiit models.

## Reply 54 — participant_039 · 2020-08-11 · post-26792290

This is great. I had a lot of joy modding CK2 and I'm really glad to see that modding CK3 will be even more flexible. Looking forward to working on it! I have gone through the linked Jomini page and it looks very nice. I have the following questions: Will there be a documentation of all the available conditions, commands, scopes etc. on release? Is there any plan to make an official tool like the Validator for CK2 to check for scripting errors in mod code? Will there be color-coded language available for Notepad++ or any IDE? These tools will be really helpful in making the process of modding efficient.

## Reply 55 — participant_040 · 2020-08-11 · post-26792304

I see that there's a dna_data directory in the database. Will that let us mod the character meshes and textures? If so to what extent? Could we mod in playable Orks and Elves? What about horses and bears?

## Reply 56 — participant_009 · 2020-08-11 · post-26792305

<!-- artifact:quote:start -->
> Sindai said: This is wrong. A minority uses mods and a minority play ironman. Most people don't do either. Click to expand...
<!-- artifact:quote:end -->
Possibly true, but most big games these days report at least basic information about how the game is being played to the devs so they have an accurate understanding of what their players do. This post from Ask a Game Dev gives a decent overview of how they gather and use telemetric data; their Telemetry Data tag gives more in-depth information. But TL;DR, I would trust Paradox's business decisions word on anything related to player behavior more than a random poster on the Paradox forums, even if Paradox didn't disclose the exact percentages.

## Reply 57 — participant_041 · 2020-08-11 · post-26792310

What about modding character models, either introducing new variables for existing models (pointy ears, etc.) or adding new models of nonhumans altogether?

## Reply 58 — participant_042 · 2020-08-11 · post-26792315

I'm not a modder, but I still have a question. Let's say a modder makes a fantasy mod with other races. They may want to have a trait to express each race's special stats (such as an Elf trait that gives an intelligence bonus (aka learning) or a Dwarf trait that gives a "strength" bonus such as martial skill, personal combat skill, or prowess, or a combination of those). Obviously you would not want the game to randomly stick an Elf trait onto the child of two Dwarves or vice versa. Is a modder able to limit certain traits so they cannot randomly be acquired and must be passed down? In addition, is it possible to prevent two such traits from being on the same computer generated character later (whenever the game decides to add more wandering courtiers, for example)? And can you prevent the player from being able to use the dynasty skill tree to choose those traits and place them on their characters themselves (no adding all racial traits on one dynasty or character)? And can you make it so the trait always passes on? If these aren't possible, I'm sure modders have other ways to do this -- just adjusting stats directly without the use of a trait, but I think being able to have that kind of trait would be valuable.

## Reply 59 — participant_039 · 2020-08-11 · post-26792322

<!-- artifact:quote:start -->
> Riamus said: I'm not a modder, but I still have a question. Let's say a modder makes a fantasy mod with other races. They may want to have a trait to express each race's special stats (such as an Elf trait that gives an intelligence bonus (aka learning) or a Dwarf trait that gives a "strength" bonus such as martial skill, personal combat skill, or prowess, or a combination of those). Obviously you would not want the game to randomly stick an Elf trait onto the child of two Dwarves or vice versa. Is a modder able to limit certain traits so they cannot randomly be acquired and must be passed down? In addition, is it possible to prevent two such traits from being on the same computer generated character later (whenever the game decides to add more wandering courtiers, for example)? And can you prevent the player from being able to use the dynasty skill tree to choose those traits and place them on their characters themselves (no adding all racial traits on one dynasty or character)? And can you make it so the trait always passes on? If these aren't possible, I'm sure modders have other ways to do this -- just adjusting stats directly without the use of a trait, but I think being able to have that kind of trait would be valuable. Click to expand...
<!-- artifact:quote:end -->
All of this is already doable in CK2 so I'm pretty sure it will be doable in CK3 as well.

## Reply 60 — participant_043 · 2020-08-11 · post-26792348

Making it easier to mod just one small element of a file instead of having to replace the entire one is huge and should help with compatibility. In fact I'd say it's one of the biggest changes to modding if not the whole game over CK2. Of the folders listed in the screenshot, I'm particularly interested in what ethnicities, flavorization, genes, and story cycles might do.

## Reply 61 — participant_008 · 2020-08-11 · post-26792383

<!-- artifact:quote:start -->
> Nc-Rm said: One of my favorite features in Imperator was the GUI array/list feature you added later. Is that also supported in CK3 or not yet? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Pbhuh said: Has the character id system been changed? Currently in CK2 it seems you can't use namespaces in events or characters (not in eu4) like in EU4. So every character has an id in certain ranges. I know you reworked events entirely, but what about this? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Arcvalons said: How moddable are succession laws? In that screenshot of the game directory there is only a folder for elective... Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> philanthropic19 said: This is great. I had a lot of joy modding CK2 and I'm really glad to see that modding CK3 will be even more flexible. Looking forward to working on it! I have gone through the linked Jomini page and it looks very nice. I have the following questions: Will there be a documentation of all the available conditions, commands, scopes etc. on release? Is there any plan to make an official tool like the Validator for CK2 to check for scripting errors in mod code? Will there be color-coded language available for Notepad++ or any IDE? These tools will be really helpful in making the process of modding efficient. Click to expand...
<!-- artifact:quote:end -->
Yep, I probably could've made an example GUI using that as we share that functionality with Imperator. Any things added to a variable list on a scope can be retrieved in the gui via Scope.GetList( 'name' ) and then worked with. Historical Character IDs can be any string now. You can mod in new ones but they will need to pick a specific rule to use which does have a hardcoded number, you can make your own partition law with extra requirements or fancy names but you cannot make a new type of succession as that is in code. 1. There is a script_docs console command which outputs all triggers, effects, scope types, event target links, modifiers, and on actions to log files. 2. In theory the game is the validator, the game aims to catch and log any errors already as we want our in house Content Designers to get those same errors, we've put a lot of work in to make sure CK3 is a lot better at logging various types of errors so I doubt an external tool like the Validator will be something we work on. If the community does then anything we fail to error on I'd love to see posts about so we can try to catch them as well. 3. I don't know on that, I know some people in house have stuff and there are various community tools as well. So I'm sure something will come out from some source eventually!

## Reply 62 — participant_008 · 2020-08-11 · post-26792416

<!-- artifact:quote:start -->
> cybrxkhan said: Making it easier to mod just one small element of a file instead of having to replace the entire one is huge and should help with compatibility. In fact I'd say it's one of the biggest changes to modding if not the whole game over CK2. Of the folders listed in the screenshot, I'm particularly interested in what ethnicities, flavorization, genes, and story cycles might do. Click to expand...
<!-- artifact:quote:end -->
Ethnicites are the range of how various portrait genes are distributed, for example the usual skin tone range or facial features more or less promiment in different parts of the world. Flavorization is how we name titles and characters, for example based on culture and government whether someone is a Count or an Earl or if a title should be a County or Earldom. Story cycles are a sort of event container that can hold variables and run updates intermittently. For example, when owning a cat is a story cycle which when setup will store various variables for the cat age, eye color, gender, and fur and add some modifiers. Then in various intermissions it will do things like every 365 days increase the age counter, prompt you to name it if you have not already, trigger some random events, or have the cat die of old age. It then has a cleanup effect to remove the various modifiers and things it may have applied. It can also handle what to do if the owner of the story dies, for the cat one it then attempts to pass the pet on to a family member or friend etc.

## Reply 63 — participant_044 · 2020-08-11 · post-26792431

<!-- artifact:quote:start -->
> blackninja9939 said: You can mod in new ones but they will need to pick a specific rule to use which does have a hardcoded number, you can make your own partition law with extra requirements or fancy names but you cannot make a new type of succession as that is in code. Click to expand...
<!-- artifact:quote:end -->
View attachment 607501 WHY YES, I am very sure I want to "Do the Murdering" Follow up question about this though: What sort of requirements can you mod into a succession customised in this way? Can you influence who's eligible for succession and who's allowed to vote (in the case of an elective succession)? And what succession rules are currently hardcoded in?

## Reply 64 — participant_045 · 2020-08-11 · post-26792437

I agree that being able to change specific elements in a file without needing to overwrite everything else as well is a huge improvement. I also hope that it will eventually be possible to do the same thing with defines. Only having to change what you actually want to change can do a lot to make sure different mods can coexist peacefully.

## Reply 65 — participant_046 · 2020-08-11 · post-26792459

<!-- artifact:quote:start -->
> Kazanov said: CK2 Dev Diary #58: Modding and a bit of optimization Good afternoon, all. I’m Magne “Meneth” Skjæran, the programmer on CK2. In the past I’ve written dev diaries about modding, optimization, and quality of life improvements, as well as last week’s dev diary talking about the life of a bug, and the... forum.paradoxplaza.com CK2 Dev Diary #49: Mods and mod telemetry Good evening, everyone. I’m Magne “Meneth” Skjæran, one of the programmers on CK2. In the past I’ve written dev diaries about modding, optimization, and quality of life improvements, and I'm writing this somewhat belated (due to technical issues)... forum.paradoxplaza.com So, if 48-42% of players use mods, and -+10% are Ironman players, almost 40%+- of players play vanilla. And Sindai said that a minority uses mods, which is not correct. At least me, if im not playing Ironman i just dont play vanilla, there is no point of playing that version of the game with so many awesome mods out there. Click to expand...
<!-- artifact:quote:end -->
I hate to tell you this, but *tecnhically* 48% is still a minority. It's just a very *large* minority. And with the range given for mod users being so wide, "non-ironman, non-mod using" players still might be a larger minority at any given point than mod using players. (42% + 10 % = 52%, leaving 48% who use neither). In fact taking your numbers, 42-48% play mods, 10% use ironman and no mods, leaving 42-48% to play without mods or ironman. You could argue that either group is a plurality of course, but the point about either group being larger at a given point still stands - and they're not effectively the same range. It's further complicated by not all mods changing the checksum, and preventing ironman for achievements. On that note @blackninja9939 - can we get an indication of what can be changed in the database without affecting checksum and achievements? It'd be nice to have *all* the cosmetic stuff be independent of achievements, so we can customise the look without affecting gameplay and our shiny trophies of self-worth.

## Reply 66 — participant_047 · 2020-08-11 · post-26792513

I hope that map is moddable because it is fairly bad compared to f.e HIP. Ck2 sequal should have a far better map than what we got..

## Reply 67 — participant_001 · 2020-08-11 · post-26792535

Hi Matthew another question, hopefully this one is good enough: Can you mod animation? Can we add new animations ourselves? How complicated is it?

## Reply 68 — participant_048 · 2020-08-11 · post-26792555

<!-- artifact:quote:start -->
> Maxamaicus said: yay, that override system for modularising files is excellent, will allow so much more compatability between mods! Click to expand...
<!-- artifact:quote:end -->
Yeah, it's certainly the way to go as far as modability goes, although I suspect initial load times will increase as the number of overrides increase, as you'll first load the "normal" files, then each override in sequence. Regardless, it certainly makes more sense then having to modify and overwrite an entire file.

## Reply 69 — participant_046 · 2020-08-11 · post-26792570

<!-- artifact:quote:start -->
> gamerk2 said: Yeah, it's certainly the way to go as far as modability goes, although I suspect initial load times will increase as the number of overrides increase, as you'll first load the "normal" files, then each override in sequence. Regardless, it certainly makes more sense then having to modify and overwrite an entire file. Click to expand...
<!-- artifact:quote:end -->
On the other hand, each override will (hopefully) be far smaller, and can maybe be collated together into a single override file.

## Reply 70 — participant_043 · 2020-08-11 · post-26792584

<!-- artifact:quote:start -->
> blackninja9939 said: Ethnicites are the range of how various portrait genes are distributed, for example the usual skin tone range or facial features more or less promiment in different parts of the world. Flavorization is how we name titles and characters, for example based on culture and government whether someone is a Count or an Earl or if a title should be a County or Earldom. Story cycles are a sort of event container that can hold variables and run updates intermittently. For example, when owning a cat is a story cycle which when setup will store various variables for the cat age, eye color, gender, and fur and add some modifiers. Then in various intermissions it will do things like every 365 days increase the age counter, prompt you to name it if you have not already, trigger some random events, or have the cat die of old age. It then has a cleanup effect to remove the various modifiers and things it may have applied. It can also handle what to do if the owner of the story dies, for the cat one it then attempts to pass the pet on to a family member or friend etc. Click to expand...
<!-- artifact:quote:end -->
Thank you for the explanation. That all sounds great. The flavorization seems to fix one of the issues with CK2 where culture based title localizations were put in the landed_titles file, making it virtually impossible to mod localizations without causing compatibility issues with mods that edited the map or de jure setup in some way. As for story cycles, so if I understand it correctly it is not so much the actual events per se, but more a "mini database" or the "brain" connecting various aspects of an event chain to make it easier to keep track of and change things instead of doing some weird long-winded roundabout methods like we would in CK2's event chains. Passing the event chain onto someone else if the person the event chain revolves around dies, is really great as well, as while it's certainly doable in CK2, this seems to make the process so much simpler and painless.

## Reply 71 — participant_049 · 2020-08-11 · post-26792802

There are possible to mod character 3D models or replace it with Stellaris-like animations?

## Reply 72 — participant_050 · 2020-08-11 · post-26792816

Does replace_path (or something similar) work this time around?

## Reply 73 — participant_031 · 2020-08-11 · post-26792848

Could you also tell us more about Map Modding and Setup Modding? For example, I assume adding in new Baronies is relatively easy. But what if someone wants to change the coastline, how does the giant overlay change this? Would a modder have to create a new overlay picture? And how is the setup changing in CK3? In Ck2 when you wanna assign counties to duchies we use the landed_titles setup, will this change to be more similar to for example to eu4 with areas, regions files or will it be similar to the landed_titles in ck2? And what about baronies and changing de jure setup? In ck2 we could move counties and duchies to other dejure parts of the world through history, but can we also move baronies in CK3 with this tool? I can already come up with a few places where baronies were seperated to form a new county

## Reply 74 — participant_051 · 2020-08-11 · post-26792859

<!-- artifact:quote:start -->
> Sylas said: 2. How can the game handle special characters, like č, š, ž ? CK2 had some limitation with that. Click to expand...
<!-- artifact:quote:end -->
Sorry if this has been resolved in the meantime, but we have already seen screenshots in which a Bohemian province of Plzeň is with ň, which is among the characters which are the least common among character sets, so I suppose all similar characters should be supported. Not just for modding but in general.

## Reply 75 — participant_052 · 2020-08-11 · post-26792867

Can we poke at the DNA system directly from script? I.e. would something like this be possible: (Actual syntax probably differing ofc.) Code: lying_pinocchio_effect = { # maybe these would take an additional parameter # for selecting dominant / recessive if = { limit = { get_dna_value = { what = nose_length value < 19 } } change_dna_value = { what = nose_length value = 1 } } else = { set_dna_value = { what = nose_length value = 20 } } }

## Reply 76 — participant_053 · 2020-08-11 · post-26792882

Thanks for diary. Has a question about the calendar. How much is it moddable? Can i change names of [days] into [hours], change number of months? in other words, for example make 30 days into 24 hours, and 12 months into 365 days. So every year would x24 times slower. If yes, then it could be possible to make calendar like in hoi4, so all modders could make deep role play game of some interesting historical period. Just curious, thanks for any answer.

## Reply 77 — participant_054 · 2020-08-11 · post-26792944

how moddable are character models? will it be possible to replace the character models with something entirely different or are they required to be humanoid?

## Reply 78 — participant_055 · 2020-08-11 · post-26792945

I, for one, would love to see some History files! Although a confirmation along the lines of, "We didn't bother showing them because they're basically the same as in CK2" would satisfy me. [And having a dev respond to this with EXACTLY that response would thrill me.]

## Reply 79 — participant_056 · 2020-08-11 · post-26792988

I have no idea what most of this is, but I like it. Seems strange to me that the fix for that one issue is being pushed back to the 1.1 release if it's already done, though. Is that a "We don't have time to implement this because we're in hardcore crunch time" thing, or is it just a game dev thing?

## Reply 80 — participant_057 · 2020-08-11 · post-26792992

I started and stopped so many mods for CK2 because there were just certain constraints and knowledge gaps that made it impossible for me to actually finish my own mod. This seems extremely good for the modding community. I hope to one day release my own mod for CK3.

## Reply 81 — participant_001 · 2020-08-11 · post-26793016

<!-- artifact:quote:start -->
> Lord Cuddlesworth said: I have no idea what most of this is, but I like it. Seems strange to me that the fix for that one issue is being pushed back to the 1.1 release if it's already done, though. Is that a "We don't have time to implement this because we're in hardcore crunch time" thing, or is it just a game dev thing? Click to expand...
<!-- artifact:quote:end -->
They have a version 1.0 that have been frozen a long time ago so that they can distribute it out to make Steam and other distribution platforms happy. All changes occured after that will have to be through a patch.

## Reply 82 — participant_058 · 2020-08-11 · post-26793173

<!-- artifact:quote:start -->
> Admiral Boysen said: Code: k_england_welsh:0 "Lloegyr" Or Code: k_england = { ... welsh="Lloegyr" ... d_essex ={ ... } ... } Click to expand...
<!-- artifact:quote:end -->
This one seems to have got lost and I'm curious as to the answer. Are cultural landed title name changes handled like CK2, like EU4 or in some other way? To extend that question, how about titles themselves? e.g. CK2's "city_empire_of_basque;...;", "tribal_duke_female_bohemian;...;" system or something more like EU4's system?

## Reply 83 — participant_059 · 2020-08-11 · post-26793358

<!-- artifact:quote:start -->
> Kazanov said: The biggest part of our playerbase plays mods and never touch the basegame, thats why PDX focuses on the modding community so much. How many people play mods? Well, most achievements i have have been obtained by the 1% of the community so its a big number. The mechanics will be shown in time, we need the modders to understand the game so they can deliver good mods at launch Click to expand...
<!-- artifact:quote:end -->
Because few people play Ironman, not because many play with mods.

## Reply 84 — participant_060 · 2020-08-11 · post-26793363

<!-- artifact:quote:start -->
> Kazanov said: The biggest part of our playerbase plays mods and never touch the basegame, thats why PDX focuses on the modding community so much. How many people play mods? Well, most achievements i have have been obtained by the 1% of the community so its a big number. The mechanics will be shown in time, we need the modders to understand the game so they can deliver good mods at launch Click to expand...
<!-- artifact:quote:end -->
That is... very much not true. For any game, the subset of people who play mods is minimal compared to the total player base.

## Reply 85 — participant_052 · 2020-08-12 · post-26793421

<!-- artifact:quote:start -->
> wilcoxchar said: That is... very much not true. For any game, the subset of people who play mods is minimal compared to the total player base. Click to expand...
<!-- artifact:quote:end -->
Going by Paradox's own data, mod user account for about 40%-50% of the CK2 player base. As you'd've known, had you bothered to read the last two pages of discussion. But here, I'll link it again: CK2 Dev Diary #49: Mods and mod telemetry Good evening, everyone. I’m Magne “Meneth” Skjæran, one of the programmers on CK2. In the past I’ve written dev diaries about modding, optimization, and quality of life improvements, and I'm writing this somewhat belated (due to technical issues)... forum.paradoxplaza.com CK2 Dev Diary #58: Modding and a bit of optimization Good afternoon, all. I’m Magne “Meneth” Skjæran, the programmer on CK2. In the past I’ve written dev diaries about modding, optimization, and quality of life improvements, as well as last week’s dev diary talking about the life of a bug, and the... forum.paradoxplaza.com

## Reply 86 — participant_061 · 2020-08-12 · post-26793474

<!-- artifact:quote:start -->
> blackninja9939 said: Localization and gui still effects the checksum yes as both need to be checked otherwise using the new more powerful gui and localization system mods could cause cheating and out of sync issues. Click to expand...
<!-- artifact:quote:end -->
I can see how that would be a concern for multiplayer, but on the other hand I am annoyed how in Stellaris for example something like a ship name list mod makes my game ineligible for gaining achievements. Any chance the game might calculate two checksums? One for the purpose of playing multiplayer and another for the purpose of achievement eligibility that will ignore anything that doesn't actually affect game mechanics?

## Reply 87 — participant_060 · 2020-08-12 · post-26793588

<!-- artifact:quote:start -->
> DaJay42 said: Going by Paradox's own data, mod user account for about 40%-50% of the CK2 player base. As you'd've known, had you bothered to read the last two pages of discussion. But here, I'll link it again: CK2 Dev Diary #49: Mods and mod telemetry Good evening, everyone. I’m Magne “Meneth” Skjæran, one of the programmers on CK2. In the past I’ve written dev diaries about modding, optimization, and quality of life improvements, and I'm writing this somewhat belated (due to technical issues)... forum.paradoxplaza.com CK2 Dev Diary #58: Modding and a bit of optimization Good afternoon, all. I’m Magne “Meneth” Skjæran, the programmer on CK2. In the past I’ve written dev diaries about modding, optimization, and quality of life improvements, as well as last week’s dev diary talking about the life of a bug, and the... forum.paradoxplaza.com Click to expand...
<!-- artifact:quote:end -->
So that's data for... one day... three years ago... on a game that has been out now for eight years and would not have the statistics for all the player base considering it came out at a time when it was available for purchase through platforms that wouldn't be submitting those statistics. Really there isn't any info about how the data is collected so no information on what parts of the player base is being left out of the submitted data, so the given number is not very indicative of anything tbh. It really is great that Paradox supports the modding community to the extent that it does, but people really need to understand that, just as the number of people who are on the forum and vocal on here are a small minority of the total player base, the modders and people who use any mods that are more than a minor tweak are also a small minority of the player base. The reality is that for every game out there, most people are going to be playing vanilla and vanilla only.

## Reply 88 — participant_062 · 2020-08-12 · post-26793608

Enchanced modability is always good.

## Reply 89 — participant_063 · 2020-08-12 · post-26793700

<!-- artifact:quote:start -->
> wilcoxchar said: That is... very much not true. For any game, the subset of people who play mods is minimal compared to the total player base. Click to expand...
<!-- artifact:quote:end -->
I haven't played the basegame for like 6 or 7 years and I know of others who did the same thing. I've only been playing mods or rather overhaul mods all this time.

## Reply 90 — participant_030 · 2020-08-12 · post-26793747

<!-- artifact:quote:start -->
> The Unknown Guy said: the map files are 8192x4096 according to this bit in the developer answers thread ▲ What is the resolution of the map files? (asking for modding purposes) ► 8192x4096 Click to expand...
<!-- artifact:quote:end -->
That's a curious resolution. The maps we've seen so far haven't been as wide as all that. If you fit the images we've seen into a 2:1 image you would be left with a gap on the side(s). A very curious gap indeed. Overlay a world map and squeeze it to fit CK3 proportions and who knows what you might be able to broadly infer about the future direction of game development. EDIT: By the way, using Lake Baikal as reference I wouldn't be surprised if Japan were included in the top right corner. I'm onto you, Paradox All I can say is Tennoheika Banzai! EDIT2: I stitched together a *tentative* *speculative* map extension. My method was first to create a 2:1 file in GIMP (2,000x1,000 for ease). Secondly I grabbed a map screenshot, square-cropped it to the edges of the actual map, with some give at the edges just in case, and resized it using the height (1,000) as benchmark. After that I further traced along the eastern "torn edges" of the map and cut out the table there. I then cut out a piece of East Asia from a world map I had on hand and scaled and rotated it to match the in-game coastline of Burma, paying special attention to that indentation that leads into the rest of SE Asia. I then traced Lake Baikal as it appears in-game on a separate layer and put it at the top so I could use it as a reference. Then I used the Unified Transform Tool to push and pull the corners of the overlay image so that Lake Baikal on the overlay would be aligned with the in-game map, while keeping it (somewhat) aligned with the southern coastline of Burma. Needless to say the alignments are not exact: the Burma-India coastline ended up being off, and the lake is also stretched. I also made an effort to insert Japan within the boundaries for the only reason that otherwise I always ended up with a cheeky Kyushu and cutoff Honshu at the edges, but this made no difference to the Burma-Baikal alignment. A small limitation to this method apart from the problems already mentioned is that the border of in-game Eastern Tibet intrudes into the overlay of China too much. A huge limitation to this method is, obviously, the screenshot is (seemingly) distorted to begin with, the map being narrower at the top. If the apparent perspective of the map is distorted then the proper location of Lake Baikal should be slightly further to the east, affecting the proper placement and distortion of the overlay. NEVERTHELESS Paradox is pretty creative with coastlines and projections, so while there are obvious drawbacks to this method, it makes little difference because as we know from their treatment of the Mediterranean, for instance, they are perfectly free to twist and turn the map as they see fit, provided only it looks and feels right. Hopefully this *total speculation* is instructive on just how feasible it is, given what we know about the map resolution and how it looks in screenshots, to include East Asia on the map, even as far as Glorious Nippon.

## Reply 91 — participant_064 · 2020-08-12 · post-26793780

<!-- artifact:quote:start -->
> wolfgag said: That's a curious resolution. The maps we've seen so far haven't been as wide as all that. If you fit the images we've seen into a 2:1 image you would be left with a gap on the side(s). A very curious gap indeed. Overlay a world map and squeeze it to fit CK3 proportions and who knows what you might be able to broadly infer about the future direction of game development. Click to expand...
<!-- artifact:quote:end -->
Considering how much CK3 has clearly been built with a long term roadmap in mind... this makes a lot of sense.

## Reply 92 — participant_001 · 2020-08-12 · post-26793788

<!-- artifact:quote:start -->
> wilcoxchar said: So that's data for... one day... three years ago... on a game that has been out now for eight years and would not have the statistics for all the player base considering it came out at a time when it was available for purchase through platforms that wouldn't be submitting those statistics. Really there isn't any info about how the data is collected so no information on what parts of the player base is being left out of the submitted data, so the given number is not very indicative of anything tbh. It really is great that Paradox supports the modding community to the extent that it does, but people really need to understand that, just as the number of people who are on the forum and vocal on here are a small minority of the total player base, the modders and people who use any mods that are more than a minor tweak are also a small minority of the player base. The reality is that for every game out there, most people are going to be playing vanilla and vanilla only. Click to expand...
<!-- artifact:quote:end -->
Bruh you can't just refute the legitimacy of one data point and proceed to give no data to back up your claim. That's cheating man. "The reality is" just doesn't cut it here. Give us more data! And I highly doubt games like The Sim, Skyrim, GTA, City Skylines et cetera have less players playing with mods than the base game... Especially Skyrim and GTA.

## Reply 93 — participant_042 · 2020-08-12 · post-26793810

<!-- artifact:quote:start -->
> wilcoxchar said: So that's data for... one day... three years ago... on a game that has been out now for eight years and would not have the statistics for all the player base considering it came out at a time when it was available for purchase through platforms that wouldn't be submitting those statistics. Really there isn't any info about how the data is collected so no information on what parts of the player base is being left out of the submitted data, so the given number is not very indicative of anything tbh. It really is great that Paradox supports the modding community to the extent that it does, but people really need to understand that, just as the number of people who are on the forum and vocal on here are a small minority of the total player base, the modders and people who use any mods that are more than a minor tweak are also a small minority of the player base. The reality is that for every game out there, most people are going to be playing vanilla and vanilla only. Click to expand...
<!-- artifact:quote:end -->
I don't claim to know what the actual stats are and it could be either way, but you are disagreeing with the data and making an assumption of your own. Just because other games may have few people using mods, there are going to be others where most people use mods. It just depends on the game and how easy it is to get good quality mods for it. The modding community for CK2 is pretty impressive and I expect CK3 modding will grow even bigger as it sounds like the game has made modding much easier (maybe not in terms of technical ease, but at least in terms of time and effort). I can easily see a bare minimum of 1/3 of players using mods and it's likely much more than that. I personally don't use mods in games very often, mostly due to lost achievements (I'd love to use the realistic water mod for Skyrim, but it's not worth losing achievements to me just for nicer water), but I've played CK2 with a couple overhaul mods just because they are interesting in how they change the game. I still mostly play it vanilla, but the mods are definitely fun and interesting and worth playing around with. Perhaps you'll get a different number based on who uses mods exclusively and who uses them occasionally, but even if you break it down that way, I still expect over 1/3 exclusively using mods (or almost exclusively). If you have information to show that the mod users are much lower number than is believed here, please feel free to show the data. But you can't just make assumptions and expect people to agree with you, especially when there's evidence to the contrary.

## Reply 94 — participant_065 · 2020-08-12 · post-26793815

My question is how easy is it to turn characters from 3D to 2D? I'm not the greatest with programs like Blender, and for my modding purposes 2D Characters would be easier for me to work with. Is it even doable to turn the regular Characters into 2D?

## Reply 95 — participant_066 · 2020-08-12 · post-26793821

How user-friendly is editing character models/portraits, or is that hard-coded?

## Reply 96 — participant_042 · 2020-08-12 · post-26793824

<!-- artifact:quote:start -->
> RelVleDy said: How user-friendly is editing character models/portraits, or is that hard-coded? Click to expand...
<!-- artifact:quote:end -->
Depends how you want to mod them. They aren't hard-coded and can be modded. If you're just wanting to change the DNA so you can make a character look differently, that sounds like it will be pretty easy to do. If you want to make a non-human character, that will be possible, but far more challenging from my understanding.

## Reply 97 — participant_067 · 2020-08-12 · post-26793885

<!-- artifact:quote:start -->
> Kazanov said: CK2 Dev Diary #58: Modding and a bit of optimization Good afternoon, all. I’m Magne “Meneth” Skjæran, the programmer on CK2. In the past I’ve written dev diaries about modding, optimization, and quality of life improvements, as well as last week’s dev diary talking about the life of a bug, and the... forum.paradoxplaza.com CK2 Dev Diary #49: Mods and mod telemetry Good evening, everyone. I’m Magne “Meneth” Skjæran, one of the programmers on CK2. In the past I’ve written dev diaries about modding, optimization, and quality of life improvements, and I'm writing this somewhat belated (due to technical issues)... forum.paradoxplaza.com So, if 48-42% of players use mods, and -+10% are Ironman players, almost 40%+- of players play vanilla. And Sindai said that a minority uses mods, which is not correct. At least me, if im not playing Ironman i just dont play vanilla, there is no point of playing that version of the game with so many awesome mods out there. Click to expand...
<!-- artifact:quote:end -->
Personally I only mod games that I feel I have exhausted (like rimworld, and still i have only found like two or three mods that are actually good, but my standards for a good mod might not be ... normal). In CK2 that never happened. I assume CK3 will remain unmodded as well.

## Reply 98 — participant_068 · 2020-08-12 · post-26793918

How come there isn't a "minor_titles" folder?

## Reply 99 — participant_069 · 2020-08-12 · post-26794138

<!-- artifact:quote:start -->
> ShadyGuy_SuspiciousGoal said: It's here wohoo! Reserving my seat so I can ask questions hehe. Didn't know you were a modder Matthew! You da bomb! How moddable is the mouse-over entries on a character? Are relationships still hard-coded? Can it be exposed as an entry like "set_relationship_with_player" so we can do our own relationship calculation if we want to (please :>)? How moddable is the text? Is it possible to create an entire new GUI window using the scripts? For example a new dynasty tree viewer. Okay possible with workaround. I assume that the character portrait is a GUI element and can be pasted anywhere just like other elements (buttons, texts)? is family related stuff included in the dynasty folder? do you have a portrait viewer or editor in game? can we add another base model or will it be restricted to only one? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> GreatWyrmGold said: This isn't directly linked to the content of either this dev diary or #30, but it's a question about modding, so... Perhaps my favorite mod for Crusader Kings 2 is the Game of Thrones mod, which (among other features) has dragons. As many of you on the forum likely know, the mod tracks dragons like characters—just like Chancellor Glitterhoof, Spymaster Mittens, and Sir Bearington. All of these nonhuman characters were possible with 2D portraits because you can just draw an animal or dragon and stick that in the project folder. However, CK3's portraits are human-shaped character models, and while there are many ways to alter proportions, facial structure, texture, etc, there's no indication that you can simply replace that model with another one (not that modeling and rigging a dragon model is a trivial task in the first place!) How do you see mods with nonhuman characters as a central feature, whether they be rulers' accessories (as with the GoT mod) or rulers in their own right (as with the Faerun mod and Pope Glitterhoof) faring in Crusader Kings 3? Click to expand...
<!-- artifact:quote:end -->
Just as an added detail, Matthew is/was the lead dev for the CK2 AGoT mod, although I believe that it's currently feature complete and only bug fixes are really being worked on. Personally speaking, I'm sure that stuff like this has occurred to him and others, and that they'll have accounted for it. Reading between the lines a bit, the fact that things are explicitly so moddable, with very little being hardcoded, would seem to imply that if needed or desired, modders could probably choose to ditch the 3D models and animations altogether.

## Reply 100 — participant_008 · 2020-08-12 · post-26794471

<!-- artifact:quote:start -->
> Mayonez_kun said: Thanks for diary. Has a question about the calendar. How much is it moddable? Can i change names of [days] into [hours], change number of months? in other words, for example make 30 days into 24 hours, and 12 months into 365 days. So every year would x24 times slower. If yes, then it could be possible to make calendar like in hoi4, so all modders could make deep role play game of some interesting historical period. Just curious, thanks for any answer. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Lord Cuddlesworth said: I have no idea what most of this is, but I like it. Seems strange to me that the fix for that one issue is being pushed back to the 1.1 release if it's already done, though. Is that a "We don't have time to implement this because we're in hardcore crunch time" thing, or is it just a game dev thing? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Fabuloscriptor said: This one seems to have got lost and I'm curious as to the answer. Are cultural landed title name changes handled like CK2, like EU4 or in some other way? To extend that question, how about titles themselves? e.g. CK2's "city_empire_of_basque;...;", "tribal_duke_female_bohemian;...;" system or something more like EU4's system? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Dragatus said: I can see how that would be a concern for multiplayer, but on the other hand I am annoyed how in Stellaris for example something like a ship name list mod makes my game ineligible for gaining achievements. Any chance the game might calculate two checksums? One for the purpose of playing multiplayer and another for the purpose of achievement eligibility that will ignore anything that doesn't actually affect game mechanics? Click to expand...
<!-- artifact:quote:end -->
You can relocalise them but other than that they are hardcoded, changing the time scale would need more support on the game end to do and I'd argue its a fairly niche modding need. As @ShadyGuy_SuspiciousGoal said, the 1.0 version is frozen from any changes unless they are of the severest impact and very critical as we do not want to risk introducing other issues into the build that could be worse than the one we fix. So for something low impact and that does not effect the vanilla game like this issue it is not considered a worthwhile risk to take. I answered in response to someone else, its handled by our "flavorization" system which deals with both the names of titles and the styling of character names as Count or Earl etc. It is something I have thought of, splitting into a hard and soft checksum but I've not had time to do this as its not really a high priority compared to features, bugs or performance work. It is one of the things on my list of things to investigate during our personal development time but that list of things to look at is pretty massive so no promises.

## Reply 101 — participant_070 · 2020-08-12 · post-26794495

Is there a reason why you're avoiding answering any questions about modding character models?

## Reply 102 — participant_008 · 2020-08-12 · post-26794518

<!-- artifact:quote:start -->
> TheProf said: Is there a reason why you're avoiding answering any questions about modding character models? Click to expand...
<!-- artifact:quote:end -->
Mainly cause I don't know the system too much in depth and our artists are busy so we covered other things in the dev diary. I know it is possible to mod the models, we use the same basic system as Imperator and they have multiple fantasy mods so I know its definitely feasible to do a variety of stuff there. But I do not know enough of the syntax or files needed to change to do much of those things.

## Reply 103 — participant_071 · 2020-08-12 · post-26794573

2 questions: - How much of this is already on the CK3 wiki? Will it all be there too on release or will I have to wait until smarter people than me have figured out how stuff works? - Do you happen to know how education traits are assigned in CK3? I've been toying with making a CK2 education trait overhaul to introduce some hybrid educations but I never quite figured out how to get it working nicely.

## Reply 104 — participant_072 · 2020-08-12 · post-26794859

So, anything done to combat the issue with savefile bloating by mid-late game?

## Reply 105 — participant_022 · 2020-08-12 · post-26794879

<!-- artifact:quote:start -->
> TheProf said: Is there a reason why you're avoiding answering any questions about modding character models? Click to expand...
<!-- artifact:quote:end -->
After digging around i have found some information, but it is not directly related to CK3... Paradox seem to use Maya for 3d modelling. There is an extractor form game files to Maya, people have used this to create unit models. There seems to be some issues at times, and the extractor is a Maya product so Paradox does not provide support for it. https://forum.paradoxplaza.com/forum/forums/clausewitz-maya-exporter-modding-tool.935/ Someone has created an extractor for blender, but there seems to be some differences between Maya and blenders coordinate systems that create "wonkyness". While the tool has been used to create unit models in HOI4 and ship models in Stellaris, it might not work for larger 3d models as the ck3 character models.

## Reply 106 — participant_073 · 2020-08-12 · post-26795378

Is there any way to dynamically create events? edit: It seems that it's possible according to the Jomini Modding Information article! It seems very tedious to implement a seq2seq algorithm though.

## Reply 107 — participant_074 · 2020-08-13 · post-26795835

I'm very glad to hear that the sound and music will be moddable but if CK3 uses FMOD like Imperator does will an easy method be provided to edit the bank files? I find FMOD to be annoyingly inaccessible.

## Reply 108 — participant_048 · 2020-08-13 · post-26795966

<!-- artifact:quote:start -->
> DreadLindwyrm said: On the other hand, each override will (hopefully) be far smaller, and can maybe be collated together into a single override file. Click to expand...
<!-- artifact:quote:end -->
Depends on implementation; the easiest way is to load the main files, then load each override in order. You could combine them into one file at the start of loading (which also works as a good validation method), but that also takes time (at least the first time you do it). either way, initial load times will be slightly longer.

## Reply 109 — participant_075 · 2020-08-13 · post-26795999

Hey! First of all, very interesting dev diary even if my question isn't related precicely to it. Indeed, I noticed in the screenshots of the game that the flag of my region, Brittany, is not accurate. The true coat of arms of Brittany at this time is the one in ck2, with plain hermine on the shield. The blue and yellow squares added in ck3 are from the dreux family, that added it when they arrived to power in the 12th century, way after the start of ck3. This is a small issue of course and I understand if it is not worth fixing it but as a breton it was important to me. Thank you and good work!!

## Reply 110 — participant_046 · 2020-08-13 · post-26796056

<!-- artifact:quote:start -->
> SaMajesté said: Hey! First of all, very interesting dev diary even if my question isn't related precicely to it. Indeed, I noticed in the screenshots of the game that the flag of my region, Brittany, is not accurate. The true coat of arms of Brittany at this time is the one in ck2, with plain hermine on the shield. The blue and yellow squares added in ck3 are from the dreux family, that added it when they arrived to power in the 12th century, way after the start of ck3. This is a small issue of course and I understand if it is not worth fixing it but as a breton it was important to me. Thank you and good work!! Click to expand...
<!-- artifact:quote:end -->
I've heard suggestions that the ermine field of Brittany is actually derived from the canton carried by Pierre I, with it being a difference to the Dreux arms, and that it's unrelated to anything the Bretons had used before. It also has legendary adoptions from mid-late game period, with it being suggested that it was adopted when one of the Dukes saw an ermine turn and attack a fox. Either way, the Dreux + ermine canton coat of arms is inappropriate.

## Reply 111 — participant_076 · 2020-08-13 · post-26796278

<!-- artifact:quote:start -->
> TheProf said: Is there a reason why you're avoiding answering any questions about modding character models? Click to expand...
<!-- artifact:quote:end -->
Hey, I've done a bit of everything 3D wise in Imperator and it seems like CK3 will be using a similar system (just expanded with full bodies instead of busts). If you have any specific questions about the 3D side of things I'd be happy to answer. I only worked on limited map models. However I did a lot of unit models, but the main area I worked on was in the 3D portraits, creating custom blendshapes for things like elf ears or orc faces, to new outfits that are tied to specific gameplay situations (such as for a king, making a separate outfit if he's leading an army, things like that)

## Reply 112 — participant_077 · 2020-08-13 · post-26796587

yo can we get just, like, a single screenshot of literally any character history file, just so i know what that looks like now? i dont know how to use a computer and i can barely read under most circumstances, but i did spend a lot of time modding the history files in ck2 since its relatively easy. if im modding anything its probably going to be that if i gotta learn how to actually code now thats gonna suck for me, a man who doesnt know math, but i guess thems the breaks

## Reply 113 — participant_078 · 2020-08-13 · post-26796671

I hope it would be possible for mod to hide some information from the player: how easy it would be for a plot to succeed, for example. CK2 did not have an option

## Reply 114 — participant_075 · 2020-08-13 · post-26796787

<!-- artifact:quote:start -->
> DreadLindwyrm said: I've heard suggestions that the ermine field of Brittany is actually derived from the canton carried by Pierre I, with it being a difference to the Dreux arms, and that it's unrelated to anything the Bretons had used before. It also has legendary adoptions from mid-late game period, with it being suggested that it was adopted when one of the Dukes saw an ermine turn and attack a fox. Either way, the Dreux + ermine canton coat of arms is inappropriate. Click to expand...
<!-- artifact:quote:end -->
I agree That either way it is unaccurate but i would prefer plain ermine because it represents Brittany itself when the one in ck3 represents not really the duchy, but more the Dreux family itself.

## Reply 115 — participant_079 · 2020-08-13 · post-26796945

Thanks for the Dev diary! Do custom elective voting rules support variable voting strength, similar to Imperial Elective in CK2?

## Reply 116 — participant_046 · 2020-08-13 · post-26797296

<!-- artifact:quote:start -->
> SaMajesté said: I agree That either way it is unaccurate but i would prefer plain ermine because it represents Brittany itself when the one in ck3 represents not really the duchy, but more the Dreux family itself. Click to expand...
<!-- artifact:quote:end -->
What would you think to the "black cross" flag for Brittany? (Either at Duchy or Kingdom level)

## Reply 117 — participant_080 · 2020-08-13 · post-26797391

Ohhh I hope I'm not too late, but I have two questions: 1. Is it possible for a mod to add an option to adopt any character? Like, as long as that character and the pope agree to this, and as long as you are childless, you may adopt a courtier. 2. Is it possible to add another variant of "Gavelkind", where you could open a new window in which to decide which heir gets what titles?

## Reply 118 — participant_042 · 2020-08-13 · post-26798264

<!-- artifact:quote:start -->
> wickermoon said: Ohhh I hope I'm not too late, but I have two questions: 1. Is it possible for a mod to add an option to adopt any character? Like, as long as that character and the pope agree to this, and as long as you are childless, you may adopt a courtier. 2. Is it possible to add another variant of "Gavelkind", where you could open a new window in which to decide which heir gets what titles? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> blackninja9939 said: You can mod in new ones but they will need to pick a specific rule to use which does have a hardcoded number, you can make your own partition law with extra requirements or fancy names but you cannot make a new type of succession as that is in code. Click to expand...
<!-- artifact:quote:end -->
Not sure about #1, but probably not. For #2, see:

## Reply 119 — participant_081 · 2020-08-14 · post-26799632

<!-- artifact:quote:start -->
> GreatWyrmGold said: This isn't directly linked to the content of either this dev diary or #30, but it's a question about modding, so... Perhaps my favorite mod for Crusader Kings 2 is the Game of Thrones mod, which (among other features) has dragons. As many of you on the forum likely know, the mod tracks dragons like characters—just like Chancellor Glitterhoof, Spymaster Mittens, and Sir Bearington. All of these nonhuman characters were possible with 2D portraits because you can just draw an animal or dragon and stick that in the project folder. However, CK3's portraits are human-shaped character models, and while there are many ways to alter proportions, facial structure, texture, etc, there's no indication that you can simply replace that model with another one (not that modeling and rigging a dragon model is a trivial task in the first place!) How do you see mods with nonhuman characters as a central feature, whether they be rulers' accessories (as with the GoT mod) or rulers in their own right (as with the Faerun mod and Pope Glitterhoof) faring in Crusader Kings 3? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> mteir said: I had hopes the DD would feature character model modding. Will there be possibilities to add/change textures, meshes and morphs (assuming morphs are used)? And the format/tools used. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Zeek40 said: I see that there's a dna_data directory in the database. Will that let us mod the character meshes and textures? If so to what extent? Could we mod in playable Orks and Elves? What about horses and bears? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Ixalmaris said: What about modding character models, either introducing new variables for existing models (pointy ears, etc.) or adding new models of nonhumans altogether? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> ShadyGuy_SuspiciousGoal said: Hi Matthew another question, hopefully this one is good enough: Can you mod animation? Can we add new animations ourselves? How complicated is it? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> kenken244 said: how moddable are character models? will it be possible to replace the character models with something entirely different or are they required to be humanoid? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> RelVleDy said: How user-friendly is editing character models/portraits, or is that hard-coded? Click to expand...
<!-- artifact:quote:end -->
So a lot of questions about 3D character modding (understandably!). I'll try to explain a little bit more about it here. The good news is that most aspects of the portraits should be moddable. The easiest to change are things related to genes and ethnicities. Quite a lot can be done without editing any meshes or textures at all. Adding a new ethnicity is actually very simple. The same goes for historical and custom characters. You can use the portrait editor available from the console to design a DNA, add it to dna_data script files and then just add a reference to it in the history entry for that character. Making everyone look like monstrous caricatures is also very easy by just ramping up the values for extremes in the ethnicity script files. Now for more ambitious modding projects, like adding new races and species. I know there is a tool to import .mesh files from the game (by ross-g somewhere on these forums). So what you would need to do to create elves or orcs or any other humanoid is to import the male and female head models and rigs into Maya and do whatever changes to them by adding blend shapes and then export it using our Maya exporter tool that we have released publicly. If you make bigger changes you're likely going to have to edit the rig as well. And this is where things become tricky. While it should be perfectly possible to change the rig the game uses predefined portrait types for male, female, boy and girl. It isn't really built around the concept of several different species. But it might still be possible with some creative modding. I could imagine implementing dragons for example as an "attachment". Essentially a dragon suit (It would not have to match human proportions or anything). It may or may not be possible to give it it's own rig and animations, I'd have to look into that to be sure. But a static dragon should at least be doable as an attachment. Smaller things, like adding new clothing and headgear (for humans), is much more straight forward and is essentially following the procedure outlined above. All textures are very easy to edit. And it's easy to add new ones as well. They're all in .dds format which is possible to edit in Photoshop with the free plugin from NVIDIA. The same goes for the color palettes we use. So adding outlandish skin colors and hair colors for example is again very easy.

## Reply 120 — participant_052 · 2020-08-14 · post-26799866

Is it possible to add custom "Currencies"? I imagine fantasy overhauls or any other mod with magic will want to add an Mana system (not EU mana, actual magical Mana), and similar things for other kinds of mods. In CK2, most mods had to misappropriate piety or introduce some placeholder-offmap to use its grace mechanic, which are rather hacky workarounds. By comparison, Stellaris has a rather extensible (even if problematic compatibility-wise) resource system, will there be anything like that?

## Reply 121 — participant_001 · 2020-08-14 · post-26800007

<!-- artifact:quote:start -->
> NilsW said: So a lot of questions about 3D character modding (understandably!). I'll try to explain a little bit more about it here. The good news is that most aspects of the portraits should be moddable. The easiest to change are things related to genes and ethnicities. Quite a lot can be done without editing any meshes or textures at all. Adding a new ethnicity is actually very simple. The same goes for historical and custom characters. You can use the portrait editor available from the console to design a DNA, add it to dna_data script files and then just add a reference to it in the history entry for that character. Making everyone look like monstrous caricatures is also very easy by just ramping up the values for extremes in the ethnicity script files. Now for more ambitious modding projects, like adding new races and species. I know there is a tool to import .mesh files from the game (by ross-g somewhere on these forums). So what you would need to do to create elves or orcs or any other humanoid is to import the male and female head models and rigs into Maya and do whatever changes to them by adding blend shapes and then export it using our Maya exporter tool that we have released publicly. If you make bigger changes you're likely going to have to edit the rig as well. And this is where things become tricky. While it should be perfectly possible to change the rig the game uses predefined portrait types for male, female, boy and girl. It isn't really built around the concept of several different species. But it might still be possible with some creative modding. I could imagine implementing dragons for example as an "attachment". Essentially a dragon suit (It would not have to match human proportions or anything). It may or may not be possible to give it it's own rig and animations, I'd have to look into that to be sure. But a static dragon should at least be doable as an attachment. Smaller things, like adding new clothing and headgear (for humans), is much more straight forward and is essentially following the procedure outlined above. All textures are very easy to edit. And it's easy to add new ones as well. They're all in .dds format which is possible to edit in Photoshop with the free plugin from NVIDIA. The same goes for the color palettes we use. So adding outlandish skin colors and hair colors for example is again very easy. Click to expand...
<!-- artifact:quote:end -->
Sweet sweet info NilsW! Thank you for the answer. So are you saying that new attachments won't have their own animation?

## Reply 122 — participant_041 · 2020-08-14 · post-26800117

A shame that switching out models for fantasy ones is not fully supported. Although wait a moment, does that mean no glitterhoof? You would need a different model for that.

## Reply 123 — participant_082 · 2020-08-14 · post-26800118

<!-- artifact:quote:start -->
> DaJay42 said: Is it possible to add custom "Currencies"? I imagine fantasy overhauls or any other mod with magic will want to add an Mana system (not EU mana, actual magical Mana), and similar things for other kinds of mods. In CK2, most mods had to misappropriate piety or introduce some placeholder-offmap to use its grace mechanic, which are rather hacky workarounds. By comparison, Stellaris has a rather extensible (even if problematic compatibility-wise) resource system, will there be anything like that? Click to expand...
<!-- artifact:quote:end -->
I think that the real problem you're getting at is displaying the currency in the interface, otherwise it's just a numeric variable. Given that @blackninja9939 added a button to the interface, I am hopeful.

## Reply 124 — participant_081 · 2020-08-14 · post-26800130

<!-- artifact:quote:start -->
> ShadyGuy_SuspiciousGoal said: Sweet sweet info NilsW! Thank you for the answer. So are you saying that new attachments won't have their own animation? Click to expand...
<!-- artifact:quote:end -->
I'm saying it might be possible but TBH I'm not completely sure so I can't make any guarantees. We haven't tried to use the system in that way.

## Reply 125 — participant_052 · 2020-08-14 · post-26800666

<!-- artifact:quote:start -->
> Keizer Harm said: I think that the real problem you're getting at is displaying the currency in the interface, otherwise it's just a numeric variable. Given that @blackninja9939 added a button to the interface, I am hopeful. Click to expand...
<!-- artifact:quote:end -->
Well, that is one part. Another is, for example, modifiers. Emulating something like a trait, artifact or building that gives e.g. "+x monthly <currency> gain" was not exactly easy or efficient to do.

## Reply 126 — participant_082 · 2020-08-14 · post-26800699

<!-- artifact:quote:start -->
> DaJay42 said: Well, that is one part. Another is, for example, modifiers. Emulating something like a trait, artifact or building that gives e.g. "+x monthly <currency> gain" was not exactly easy or efficient to do. Click to expand...
<!-- artifact:quote:end -->
Good point; didn't consider modifiers.

## Reply 127 — participant_008 · 2020-08-14 · post-26800947

<!-- artifact:quote:start -->
> DaJay42 said: Is it possible to add custom "Currencies"? I imagine fantasy overhauls or any other mod with magic will want to add an Mana system (not EU mana, actual magical Mana), and similar things for other kinds of mods. In CK2, most mods had to misappropriate piety or introduce some placeholder-offmap to use its grace mechanic, which are rather hacky workarounds. By comparison, Stellaris has a rather extensible (even if problematic compatibility-wise) resource system, will there be anything like that? Click to expand...
<!-- artifact:quote:end -->
You can store it as a numeric variable on the characters then just grab that number out in the interface somewhere, so that should be entirely fine to do.

## Reply 128 — participant_058 · 2020-08-15 · post-26801594

<!-- artifact:quote:start -->
> blackninja9939 said: I answered in response to someone else, its handled by our "flavorization" system which deals with both the names of titles and the styling of character names as Count or Earl etc. Click to expand...
<!-- artifact:quote:end -->
Can you elaborate at all on what that system looks like? We'll know soon enough, but is it a localisation-based csv system like CK2 or a common file-based system like EU4?

## Reply 129 — participant_001 · 2020-08-15 · post-26801608

And talk about localization keys, how organized are they this time ?

## Reply 130 — participant_083 · 2020-08-15 · post-26801744

<!-- artifact:quote:start -->
> NilsW said: But it might still be possible with some creative modding. I could imagine implementing dragons for example as an "attachment". Essentially a dragon suit (It would not have to match human proportions or anything). It may or may not be possible to give it it's own rig and animations, I'd have to look into that to be sure. Click to expand...
<!-- artifact:quote:end -->
Oh man, we are going to get so many crazy mods. I guarantee some of the first "outfit mods" will be for Shrek, and Thomas the Tank Engine. That's good news for fantasy races. But honestly it sounds like we might not even need new models for some of the humanoids. For Orcs, all you need to do is just create a trait with green skin and ugly faces, for Elves depending on how pointy ears can get with DNA, you can just make a pointy ear trait. For more alien races like Lizardmen, I'm sure a talented modder can pull off a convincing edit.

## Reply 131 — participant_084 · 2020-08-15 · post-26801812

<!-- artifact:quote:start -->
> gamemaster said: Oh man, we are going to get so many crazy mods. I guarantee some of the first "outfit mods" will be for Shrek, and Thomas the Tank Engine. That's good news for fantasy races. But honestly it sounds like we might not even need new models for some of the humanoids. For Orcs, all you need to do is just create a trait with green skin and ugly faces, for Elves depending on how pointy ears can get with DNA, you can just make a pointy ear trait. For more alien races like Lizardmen, I'm sure a talented modder can pull off a convincing edit. Click to expand...
<!-- artifact:quote:end -->
You wouldn't even need to do traits, all you would need to do is create an ethnicity and set the value ranges for all the options.

## Reply 132 — participant_008 · 2020-08-15 · post-26801981

<!-- artifact:quote:start -->
> Fabuloscriptor said: Can you elaborate at all on what that system looks like? We'll know soon enough, but is it a localisation-based csv system like CK2 or a common file-based system like EU4? Click to expand...
<!-- artifact:quote:end -->
It is a folder in common though I don't know how EU4 does it/ For us its key with a priority and various options such as checking culture, faith, government, independence, council position, and more which will pick whatever conditions are met of the highest priority and use that one.

## Reply 133 — participant_085 · 2020-08-15 · post-26802569

Is the ethnicity skin tone handled in straight line (dark-light spectrum) or can you add new ones that blend with them? Like normal black, white, and mixed humans, who can also breed with blue or green humans to produce offspring with new shades? Would it work so that we can have ALL the vanilla skin colors AND a number of custom ones able to freely exchange genes in-game?

## Reply 134 — participant_058 · 2020-08-15 · post-26803181

<!-- artifact:quote:start -->
> blackninja9939 said: It is a folder in common though I don't know how EU4 does it/ For us its key with a priority and various options such as checking culture, faith, government, independence, council position, and more which will pick whatever conditions are met of the highest priority and use that one. Click to expand...
<!-- artifact:quote:end -->
You can do culture and religion specific localisation? You spoil me!

## Reply 135 — participant_001 · 2020-08-15 · post-26803335

<!-- artifact:quote:start -->
> Fabuloscriptor said: You can do culture and religion specific localisation? You spoil me! Click to expand...
<!-- artifact:quote:end -->
Hm, I think he's referring to the "GetHerHim" type of commands, unless that's what you're referring to too. Details here

## Reply 136 — participant_057 · 2020-08-16 · post-26803770

Hey just a question about Religious Heads, is it possible to have a constantly changing title holder based on which character holds the most land or overall troops? So basically the most powerful ruler is granted the title of the religious head, kinda like how cultural head works? Hopefully this makes sense. Edit: also thanks if you end up answering this, I see you've been answering a lot of questions.

## Reply 137 — participant_081 · 2020-08-17 · post-26806867

<!-- artifact:quote:start -->
> SMiki Lorebringer said: Is the ethnicity skin tone handled in straight line (dark-light spectrum) or can you add new ones that blend with them? Like normal black, white, and mixed humans, who can also breed with blue or green humans to produce offspring with new shades? Would it work so that we can have ALL the vanilla skin colors AND a number of custom ones able to freely exchange genes in-game? Click to expand...
<!-- artifact:quote:end -->
So the skin color palette that we use is a square image with gradients from light to dark on the y axis and from reddish to yellowish on the x axis. Skin color is simply defined as a coordinate on this palette. Children that are born will get a skin color that is picked somewhere along the line between the parents' coordinates. So you could definitely add more colors to the palette but you would have to put some thought into which colors are next to each other. If you would have all the colors of the rainbow in the palette, for example, a child between a red skinned person and a blue skinned person might get green skin

## Reply 138 — participant_086 · 2020-08-17 · post-26806872

How simple will it be to mod the contrast and brightness up a few notches? Say, to look like the screenshots in this thread. I'm not too worried about it being perfect... I just find the grey 'veil' over everything strains my eyes. I'm most interested in increasing the contrast of the text to the background.

## Reply 139 — participant_087 · 2020-08-17 · post-26806927

<!-- artifact:quote:start -->
> NilsW said: So you could definitely add more colors to the palette but you would have to put some thought into which colors are next to each other. If you would have all the colors of the rainbow in the palette, for example, a child between a red skinned person and a blue skinned person might get green skin View attachment 610263 Click to expand...
<!-- artifact:quote:end -->
Green, or purple? You gotta draw the line somewhere. To heck with purple people! Unless they're suffocating. Then... help 'em.

## Reply 140 — participant_088 · 2020-08-17 · post-26807275

Hi, I'm currently working on a mod focusing on the British Isles for CKII and I was wondering how easy it would be to port a map to CKIII? Would it require a lot of work and an entirely new set of images? [ MOD ] Britain - Barons, Hundreds, Wards and Wapentakes "Britain - Barons, Hundreds, Wards and Wapentakes" is a mod for CK2 focusing on the British Isles. In this mod you can play as a smaller tier feudal lord as the map is made up of smaller divisions of land, using the historical system of... forum.paradoxplaza.com Also, I had planned to rework the holdings to fit more of a manorial system (Since the map is split into a tonne of baronies it wouldn't make sense for each one to have a castle) Do you have any idea how moddable the holdings would be? Could we perhaps create entirely new holding types?

## Reply 141 — participant_076 · 2020-08-17 · post-26807536

<!-- artifact:quote:start -->
> Karlington said: Green, or purple? You gotta draw the line somewhere. To heck with purple people! Unless they're suffocating. Then... help 'em. Click to expand...
<!-- artifact:quote:end -->
IS that a Mitch Hedberg quote? I applaud your good taste sir

## Reply 142 — participant_085 · 2020-08-17 · post-26807547

<!-- artifact:quote:start -->
> NilsW said: So the skin color palette that we use is a square image with gradients from light to dark on the y axis and from reddish to yellowish on the x axis. View attachment 610259 Skin color is simply defined as a coordinate on this palette. Children that are born will get a skin color that is picked somewhere along the line between the parents' coordinates. So you could definitely add more colors to the palette but you would have to put some thought into which colors are next to each other. If you would have all the colors of the rainbow in the palette, for example, a child between a red skinned person and a blue skinned person might get green skin View attachment 610263 Click to expand...
<!-- artifact:quote:end -->
Can it be changed to a rectangle or must it be a square?

## Reply 143 — participant_042 · 2020-08-17 · post-26807573

<!-- artifact:quote:start -->
> SMiki Lorebringer said: Can it be changed to a rectangle or must it be a square? Click to expand...
<!-- artifact:quote:end -->
He showed a rectangle, so that should be fine. The square just gives you more chance to blend along 2 axes equally rather than mostly just one axis. If you were to make the normal skin tones on a rectangle, you'd lose out on a lot of the possibilities. Of course, if you're just using fake skin tones or you only want specific ones, a rectangle may work better for you. I think the bigger question is... can you use more than one palette? For a fantasy mod, for example, you might want orcs to have a brownish set of skin tones, trolls to have a blue to green range of skin tones, elves to have a normal "pinkish" to blue or purple skin tones, etc. I suppose you could put these on the same palette and since the child will be somewhere between the skin tones of the parents, you could just have each race set in the right part and go from there. But it might be easier to work with and adjust the skin tones if you could do so with multiple palettes.

## Reply 144 — participant_087 · 2020-08-17 · post-26807716

<!-- artifact:quote:start -->
> rewinged said: IS that a Mitch Hedberg quote? I applaud your good taste sir Click to expand...
<!-- artifact:quote:end -->
It is indeed, my good man! Thank you! I was hoping someone would recognize it for what it was.

## Reply 145 — participant_022 · 2020-08-17 · post-26807928

<!-- artifact:quote:start -->
> Riamus said: He showed a rectangle, so that should be fine. The square just gives you more chance to blend along 2 axes equally rather than mostly just one axis. If you were to make the normal skin tones on a rectangle, you'd lose out on a lot of the possibilities. Of course, if you're just using fake skin tones or you only want specific ones, a rectangle may work better for you. I think the bigger question is... can you use more than one palette? For a fantasy mod, for example, you might want orcs to have a brownish set of skin tones, trolls to have a blue to green range of skin tones, elves to have a normal "pinkish" to blue or purple skin tones, etc. I suppose you could put these on the same palette and since the child will be somewhere between the skin tones of the parents, you could just have each race set in the right part and go from there. But it might be easier to work with and adjust the skin tones if you could do so with multiple palettes. Click to expand...
<!-- artifact:quote:end -->
Even if you can't have multiple pallets (because the DNA system can only use one?) you could hijack the 125 shades of black and white by flipping the main axis of the gradient to add some colours. Would need to rework every race DNA color in game to ocupy a new area on the gradient map, and if a greenish and a pinkie has a child it would be human color. Someone more creative might try to jam in more color dimensions.

## Reply 146 — participant_046 · 2020-08-17 · post-26807954

<!-- artifact:quote:start -->
> mteir said: Even if you can't have multiple pallets (because the DNA system can only use one?) you could hijack the 125 shades of black and white by flipping the main axis of the gradient to add some colours. Would need to rework every race DNA color in game to ocupy a new area on the gradient map, and if a greenish and a pinkie has a child it would be human color. Someone more creative might try to jam in more color dimensions. View attachment 610349 Click to expand...
<!-- artifact:quote:end -->
Potentially a 3D colour space?

## Reply 147 — participant_022 · 2020-08-17 · post-26808504

<!-- artifact:quote:start -->
> DreadLindwyrm said: Potentially a 3D colour space? Click to expand...
<!-- artifact:quote:end -->
Likely not full 3D color space. More, how to flatten the 3D color space to 128x128 2D and have the DNA system still produce offspring with sensible colors (choose any two points as parents and every point on a straight line between those two points should make sense as a child). Another possible option is decals if they are available, assigning race as a trait and the trait applies a decal over the character skin, slightly similar as how ck2 handles fantasy races modded in.

## Reply 148 — participant_089 · 2020-08-18 · post-26808765

In modding CK2, if you wanted to 'unlock' certain events or chains of events, it was generally necessary to edit all of the events to change the conditions checked in their triggers. For example, if you wanted to enable Seduction events and decisions for a character that doesn't have the Seduction focus, you'd have to search through the script and decision files for instances of "has_focus = focus_seduction" and make many changes. Has there been any restructuring in how such prerequisites are implemented in CK3 that could streamline that and allow accomplishing the same with fewer elements edited? For the above example as an illustration, if the game applied a character flag on choosing a focus, and the vanilla events checked for the presence of that flag instead of the presence of the focus, then the modder would have the freedom to add that flag in other ways to enable the Seduction content. I'm thinking specifically of what would be involved in modding in new lifestyles, focuses, and perk trees. One might wish to add content like this, but re-use events from pre-existing ones rather than needing to create entirely new sets of events.

## Reply 149 — participant_066 · 2020-08-18 · post-26808834

<!-- artifact:quote:start -->
> NilsW said: I'm saying it might be possible but TBH I'm not completely sure so I can't make any guarantees. We haven't tried to use the system in that way. Click to expand...
<!-- artifact:quote:end -->
Would implementing static character models be significantly easier then, such as swapping out assets for still-images of dragons via Google search? Perhaps the modder can create multiple dragon traits with each trait devoted to a unique static image that substitutes out the in-game model for the image. I'd have to play around with where the best place to store each image would be though.

## Reply 150 — participant_052 · 2020-08-18 · post-26810308

<!-- artifact:quote:start -->
> blackninja9939 said: We do have effects to modify the unborn character though such as setting if they are a known bastard, changing the assumed father, and setting the number of children. Click to expand...
<!-- artifact:quote:end -->
Is the gender of the child still determined at birth? If not, can we get/set the gender of an unborn child? Otherwise, can we do so before the birth is announced to the player? I imagine certain total conversion mods might find this very useful.

## Reply 151 — participant_090 · 2020-08-20 · post-26815074

Why won't the Dev's answer whether baronies will be able to be modded in? If we can't remove the restriction to play baronies as they are, we'll just have to bump the titles down by one so baronies are just counties with only the capital barony attatched, making the base baron level title obsolete, or possibly having it as a sort of off-world title for knights in your realm.

## Reply 152 — participant_009 · 2020-08-20 · post-26815994

<!-- artifact:quote:start -->
> Lord Cuddlesworth said: I have no idea what most of this is, but I like it. Seems strange to me that the fix for that one issue is being pushed back to the 1.1 release if it's already done, though. Is that a "We don't have time to implement this because we're in hardcore crunch time" thing, or is it just a game dev thing? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> NilsW said: So the skin color palette that we use is a square image with gradients from light to dark on the y axis and from reddish to yellowish on the x axis. View attachment 610259 Skin color is simply defined as a coordinate on this palette. Children that are born will get a skin color that is picked somewhere along the line between the parents' coordinates. So you could definitely add more colors to the palette but you would have to put some thought into which colors are next to each other. If you would have all the colors of the rainbow in the palette, for example, a child between a red skinned person and a blue skinned person might get green skin View attachment 610263 Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Astephos said: Why won't the Dev's answer whether baronies will be able to be modded in? If we can't remove the restriction to play baronies as they are, we'll just have to bump the titles down by one so baronies are just counties with only the capital barony attatched, making the base baron level title obsolete, or possibly having it as a sort of off-world title for knights in your realm. Click to expand...
<!-- artifact:quote:end -->
I realize I'm answering a week-old question (which already has multiple simple, if solid, answers, including one from a Paradox programmer), but there are good reasons (certification requirements, mostly) for a fix made late in development to be put into an early patch and not in version 1.0, and if nothing else I want to link to a guy who knows what he's talking about. Also, I am of the opinion that more details are always better, as long as they're presented clearly. To summarize: Games need to go through a process called certification before they can be released on any platform. The exact process varies a lot by platform, but it's invariably a significant expense, so you don't want to go through it twice. This means that A. you don't submit games for certification before you're confident they'll pass, and B. you don't change games after submitting them for certification except to fix bugs that will make the game fail certification. Patches also need to be certified, but the process is much easier (and cheaper) than certifying a whole game. If you find a non-cert-breaking bug after the game has been submitted for certification, you fix it in the first patch, because that's cheaper and easier. Then, if everything goes according to plan, you release the patch on day 1 so nobody ever notices the broken aspects of 1.0. A clever artist should be able to find a better way to arrange the colors, of course. My first point of reference is the paint.net color wheel thingy: Spoiler Here, a red/blue hybrid child would be magenta-ish. It should go without saying that having technicolor people and ordinary skin tones on the same palette would be...tricky. My intuition says that they can't be modded like that, because the levels of title which are playable (and hence are fully engaged in the world around them) is presumably central to how the code is structured. (And, moreover, that such a hypothetical mod would probably cause serious performance issues, because there are squillions of baron-level nobles.) But I can't think of any way to reply to this kind of question well from Paradox's perspective, especially if providing more than a simple "No" requires understanding technical issues that the people running these threads don't understand (which they probably do, because again, this is presumably central to how the code is structured). TL;DR: It's a surprisingly complicated issue, but the overall answer is probably no.

## Reply 153 — participant_087 · 2020-08-20 · post-26816250

<!-- artifact:quote:start -->
> GreatWyrmGold said: I realize I'm answering a week-old question (which already has multiple simple, if solid, answers, including one from a Paradox programmer), but there are good reasons (certification requirements, mostly) for a fix made late in development to be put into an early patch and not in version 1.0, and if nothing else I want to link to a guy who knows what he's talking about. Also, I am of the opinion that more details are always better, as long as they're presented clearly. To summarize: Games need to go through a process called certification before they can be released on any platform. The exact process varies a lot by platform, but it's invariably a significant expense, so you don't want to go through it twice. This means that A. you don't submit games for certification before you're confident they'll pass, and B. you don't change games after submitting them for certification except to fix bugs that will make the game fail certification. Patches also need to be certified, but the process is much easier (and cheaper) than certifying a whole game. If you find a non-cert-breaking bug after the game has been submitted for certification, you fix it in the first patch, because that's cheaper and easier. Then, if everything goes according to plan, you release the patch on day 1 so nobody ever notices the broken aspects of 1.0. Click to expand...
<!-- artifact:quote:end -->
I may be wrong here, because this is not my area of expertise, but I thought the certification requirements were only for consoles? I.e. you have to get certified by Nintendo for Nintendo, by Microsoft for Xbox, and so on?

## Reply 154 — participant_046 · 2020-08-20 · post-26816280

<!-- artifact:quote:start -->
> Astephos said: Why won't the Dev's answer whether baronies will be able to be modded in? If we can't remove the restriction to play baronies as they are, we'll just have to bump the titles down by one so baronies are just counties with only the capital barony attatched, making the base baron level title obsolete, or possibly having it as a sort of off-world title for knights in your realm. Click to expand...
<!-- artifact:quote:end -->
You can almost certainly mod it in so that "counts" run what would otherwise be baronies, and everyone moves down one - the problem comes that unless you do something about it, your four "playable" tiers now run out at what would normally be king tier. This may or may not be solvable by adding more tiers - or the number of tiers may be fixed. There is a problem as well that since barons have severely abbreviated courts, you've now taken the number of potential comital courts and multiplies it by 5 or so - increasing the number of characters that will be around. Then not all baronies are feudal holdings. "Single holding counties" are often relatively poor, and without the tax income from the barons it would be quite hard to get any momentum going. It also brings back the problem from CK2 of "control X kingdom entirely" becoming a chore once again as you have to hunt down far, far more title holders in the process.

## Reply 155 — participant_009 · 2020-08-20 · post-26816895

<!-- artifact:quote:start -->
> Karlington said: I may be wrong here, because this is not my area of expertise, but I thought the certification requirements were only for consoles? I.e. you have to get certified by Nintendo for Nintendo, by Microsoft for Xbox, and so on? Click to expand...
<!-- artifact:quote:end -->
I'm pretty sure, though not 100%, that Steam also has some certification requirements. Not as stringent as the consoles', of course, but still extant. Maybe we should look for someone with firsthand knowledge instead of guessing at each other.

## Reply 156 — participant_087 · 2020-08-20 · post-26816912

<!-- artifact:quote:start -->
> GreatWyrmGold said: I'm pretty sure, though not 100%, that Steam also has some certification requirements. Not as stringent as the consoles', of course, but still extant. Maybe we should look for someone with firsthand knowledge instead of guessing at each other. Click to expand...
<!-- artifact:quote:end -->
I think you might be right. I looked and I found, well, Steam themselves.

## Reply 157 — participant_009 · 2020-08-20 · post-26816949

<!-- artifact:quote:start -->
> Karlington said: I think you might be right. I looked and I found, well, Steam themselves. Click to expand...
<!-- artifact:quote:end -->
Oh. Right. Steam would need to put their requirements somewhere public, because everyone's making Steam games.

## Reply 158 — participant_087 · 2020-08-20 · post-26816953

<!-- artifact:quote:start -->
> GreatWyrmGold said: Oh. Right. Steam would need to put their requirements somewhere public, because everyone's making Steam games. Click to expand...
<!-- artifact:quote:end -->
Yup! Every guy and gal who knows a little code is hoping to become the Angry Birds of Steam.

## Reply 159 — participant_052 · 2020-08-21 · post-26817210

<!-- artifact:quote:start -->
> Karlington said: I think you might be right. I looked and I found, well, Steam themselves. Click to expand...
<!-- artifact:quote:end -->
Huh, those must be new, considering people have managed to put "games" on steam that didn't even contain an executable.

## Reply 160 — participant_087 · 2020-08-21 · post-26817269

<!-- artifact:quote:start -->
> DaJay42 said: Huh, those must be new, considering people have managed to put "games" on steam that didn't even contain an executable. Click to expand...
<!-- artifact:quote:end -->
That might very well be why, then.

## Reply 161 — participant_091 · 2020-08-21 · post-26818195

<!-- artifact:quote:start -->
> blackninja9939 said: Alerts, Issues and Notifications As I mentioned in Dev Diary 16, all of the new interface utilities we have for explaining the game are moddable. Which means you can add, remove, and modify any of these things through script instead of them being hard coded like in CK2. Click to expand...
<!-- artifact:quote:end -->
A bit late question, but what sort of triggers there are for these notifications and are there any effects that can be added to them? I.e. can I make a notification "army x has arrived to province y" that autopauses the game when it triggers or something similar? And how extensive and customisable (via in-game settings) the alert and notification system in the base game itself is?

## Reply 162 — participant_092 · 2020-08-21 · post-26819231

<!-- artifact:quote:start -->
> NilsW said: Children that are born will get a skin color that is picked somewhere along the line between the parents' coordinates. Click to expand...
<!-- artifact:quote:end -->
Could we get an overview on CoA modding? I would assume it's basically like Imperator, but considering the way the CoAs look, the emblems, at least, are very clearly not the same. I'm particularly interested in how color channels work, since they were used pretty creatively in Imperator. Doesn't that mean that the population of the game will trend strongly away from extremes? Why not just use the gene system? You only need like eight, and that covers hair and eye coloration too.

## Reply 163 — participant_046 · 2020-08-21 · post-26819255

<!-- artifact:quote:start -->
> Cruxador said: Could we get an overview on CoA modding? I would assume it's basically like Imperator, but considering the way the CoAs look, the emblems, at least, are very clearly not the same. I'm particularly interested in how color channels work, since they were used pretty creatively in Imperator. Doesn't that mean that the population of the game will trend strongly away from extremes? Why not just use the gene system? You only need like eight, and that covers hair and eye coloration too. Click to expand...
<!-- artifact:quote:end -->
Only if you get a lot of mixing between the extremes. If black people tend to marry black people, and white people tend to marry white people you'll *generally* preserve your extreme pools of skin tone. Plus newly spawned characters will tend to have their default cultural skin tone, and so will act as an anchor to preserve tones. It is however reasonably accurate that a mixing pot will tend towards the centre of the skin tones in that pot over time, so a population of scandinavians and Mali should over time come to a "tanned" tone rather than black or white. Eight tones is insufficient when there's the possibility of doing it cleanly and dynamically, and there are certainly more than 8 tones for hair colour, just in the celtic/roman/saxon/frankish/scandinavian pool that is "native british". I could probably find you 8 different tones of blonde and 8 different tones of brown if I looked. Add to that that "European black hair" and "African black hair" aren't quite the same, even taking that generalisation, and there's a lot of colours out there.

## Reply 164 — participant_009 · 2020-08-21 · post-26819333

<!-- artifact:quote:start -->
> Cruxador said: Doesn't that mean that the population of the game will trend strongly away from extremes? Why not just use the gene system? You only need like eight, and that covers hair and eye coloration too. Click to expand...
<!-- artifact:quote:end -->
Aside from what DreadLindwyrm said, using a handful of presets would make modding a lot clumsier, and for that matter would make interracial kids less...workable. Also, these aren't clusters of individually-drawn portraits, these are specific colors applied to the texture. Giving everyone of a given race the exact same skin color would look eerie. After all, not all white people are equally white, especially when you take e.g. lifestyle into account.

## Reply 165 — participant_046 · 2020-08-21 · post-26819418

<!-- artifact:quote:start -->
> GreatWyrmGold said: Aside from what DreadLindwyrm said, using a handful of presets would make modding a lot clumsier, and for that matter would make interracial kids less...workable. Also, these aren't clusters of individually-drawn portraits, these are specific colors applied to the texture. Giving everyone of a given race the exact same skin color would look eerie. After all, not all white people are equally white, especially when you take e.g. lifestyle into account. Click to expand...
<!-- artifact:quote:end -->
I'm certainly reasonably dark for a "white Northern European", but then I've got dark brown hair and blue eyes, so I'm a bit of a mutt. If I ever actually tan though, I can look almost middle eastern at first glance (although I don't get as dark as a middle eastern who has *also* tanned). A couple of friends of mine are almost as white as milk, and just don't ever seem to tan - they just burn. They're a lot redder in colouration even when not exposed to sunlight because their blood vessels show up more than mine. I tend to a sort of "light wooden" colour if that's an apt comparison, rather than their white/pink look.

## Reply 166 — participant_092 · 2020-08-21 · post-26819556

<!-- artifact:quote:start -->
> DreadLindwyrm said: Only if you get a lot of mixing between the extremes. If black people tend to marry black people, and white people tend to marry white people you'll *generally* preserve your extreme pools of skin tone. Plus newly spawned characters will tend to have their default cultural skin tone, and so will act as an anchor to preserve tones. It is however reasonably accurate that a mixing pot will tend towards the centre of the skin tones in that pot over time, so a population of scandinavians and Mali should over time come to a "tanned" tone rather than black or white. Eight tones is insufficient when there's the possibility of doing it cleanly and dynamically, and there are certainly more than 8 tones for hair colour, just in the celtic/roman/saxon/frankish/scandinavian pool that is "native british". I could probably find you 8 different tones of blonde and 8 different tones of brown if I looked. Add to that that "European black hair" and "African black hair" aren't quite the same, even taking that generalisation, and there's a lot of colours out there. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> GreatWyrmGold said: Aside from what DreadLindwyrm said, using a handful of presets would make modding a lot clumsier, and for that matter would make interracial kids less...workable. Also, these aren't clusters of individually-drawn portraits, these are specific colors applied to the texture. Giving everyone of a given race the exact same skin color would look eerie. After all, not all white people are equally white, especially when you take e.g. lifestyle into account. Click to expand...
<!-- artifact:quote:end -->
Eight genes, not eight tones. Eight genes have 256 combinations. Honestly, 5 would probably be enough but might as well use a full byte. Lifestyle isn't determined at birth. I also don't think it's reflected in skin color in the game currently; I would think the devs would mention if it was. It would certainly be nice though, one of the things that annoyed me in CK2 was how some races had implied lifestyles, with aztecs being super craggy and farmerous and norse looking very indoor-oriented. As for modding, I don't entirely agree. I think being able to define color influences of new genes (e.g., this set of alleles correlates to increased green in the skin) would be easier than having to change the skin tones available to humans (removing the darker colors probably, considering how most fantasy settings are) or rotating the image and redefining everything (theoretically a clever solution, but tedious to implement, and diagonal is less intuitive).

## Reply 167 — participant_084 · 2020-08-22 · post-26819953

<!-- artifact:quote:start -->
> Cruxador said: I also don't think it's reflected in skin color in the game currently; Click to expand...
<!-- artifact:quote:end -->
It actually is sort of in, if you have for instance the Drunkard Trait, you characters skin on the face will become flushed red. If they are ill, they will become sickly pale and gaunt looking.

## Reply 168 — participant_009 · 2020-08-22 · post-26821435

<!-- artifact:quote:start -->
> Cruxador said: Eight genes, not eight tones. Eight genes have 256 combinations. Honestly, 5 would probably be enough but might as well use a full byte. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Lifestyle isn't determined at birth. I also don't think it's reflected in skin color in the game currently... Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> As for modding, I don't entirely agree. I think being able to define color influences of new genes (e.g., this set of alleles correlates to increased green in the skin) would be easier than having to change the skin tones available to humans (removing the darker colors probably, considering how most fantasy settings are) or rotating the image and redefining everything (theoretically a clever solution, but tedious to implement, and diagonal is less intuitive). Click to expand...
<!-- artifact:quote:end -->
Alright, how does this system work? You have eight genes that can be present or absent; how are they inherited? Wouldn't you still run the risk of homogeneity due to everyone who has/lacks a given skin tone happening to die without issue, no miscegenation required? How does this solve the racial homogeneity problem you're so concerned about? They have all the tools in place for that kind of stuff. IIRC, skin tone isn't solely determined by genetics, and about half a dev diary was spent showing how lifestyles modify the model and texture of a character. Now that I realize the genes are supposed to be miscible, yeah. But as indicated above, that introduces a bunch of new problems. In the end, I don't see it providing much meaningful benefit compared to the added complexity...outside this specific type of mod, where it could absolutely make things easier.

## Reply 169 — participant_093 · 2020-08-23 · post-26823109

<!-- artifact:quote:start -->
> blackninja9939 said: Hello everyone and welcome to the 37th CK3 Dev Diary! I’m Matthew, one of the Programmers on the CK3 team, and today I am going to talk to you about the modding in Crusader Kings III! Mods are something very important to the team and something especially close to my heart. I got started at Paradox as a Content Designer due to my modding work on Crusader Kings II, so being able to make sure the sequel has lots of modding opportunities and trying to give back to the community that aided me in getting into this industry is something I am very passionate about, and I know others on the team had similar starts in modding as well. ... Click to expand...
<!-- artifact:quote:end -->
Will there be a way to have Achievements work on most mods?

## Reply 170 — participant_052 · 2020-08-23 · post-26823224

<!-- artifact:quote:start -->
> Prometheus_1 said: Will there be a way to have Achievements work on most mods? Click to expand...
<!-- artifact:quote:end -->
Given that this is a paradox game, I doubt we'll get achievements with anything but the most basic cosmetic mods.

## Reply 171 — participant_087 · 2020-08-23 · post-26823230

<!-- artifact:quote:start -->
> Prometheus_1 said: Will there be a way to have Achievements work on most mods? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DaJay42 said: Given that this is a paradox game, I doubt we'll get achievements with anything but the most basic cosmetic mods. Click to expand...
<!-- artifact:quote:end -->
Agreed. In CK2 the hard limit was changing the checksum IIRC. If your mod did not change the checksum it wouldn't affect achievements, but if it did it would disable them. That's not to say you couldn't have mods that were basically cheats, just that they couldn't have game-technical effects. For example, there are CK2 mods out there that enable you to see characters' exact Health and Fertility, secret lovers, secret bastard status and real father, etc while still allowing for achievements.

## Reply 172 — participant_060 · 2020-08-23 · post-26823239

<!-- artifact:quote:start -->
> Prometheus_1 said: Will there be a way to have Achievements work on most mods? Click to expand...
<!-- artifact:quote:end -->
No, because otherwise there would be no point to achievements. The reason they don't allow achievements with nearly all mods is to stop people from modding the game so the achievement conditions are already met.

## Reply 173 — participant_092 · 2020-08-23 · post-26823371

<!-- artifact:quote:start -->
> Alenarae118 said: It actually is sort of in, if you have for instance the Drunkard Trait, you characters skin on the face will become flushed red. If they are ill, they will become sickly pale and gaunt looking. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> GreatWyrmGold said: Alright, how does this system work? You have eight genes that can be present or absent; how are they inherited? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Wouldn't you still run the risk of homogeneity due to everyone who has/lacks a given skin tone happening to die without issue, no miscegenation required? How does this solve the racial homogeneity problem you're so concerned about? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> They have all the tools in place for that kind of stuff. IIRC, skin tone isn't solely determined by genetics, and about half a dev diary was spent showing how lifestyles modify the model and texture of a character. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> wilcoxchar said: No, because otherwise there would be no point to achievements. The reason they don't allow achievements with nearly all mods is to stop people from modding the game so the achievement conditions are already met. Click to expand...
<!-- artifact:quote:end -->
Does that use the skin tone system or overlays/shaders? Good news either way, I suppose. I was mostly thinking of habitual exposure to the elements, as alluded to in my example, but health stuff should also be considered relevant, I reckon. According to the gene system already in the game. I don't think a single gene dying out in a game is a bit concern, they would be seeded to some extent from random characters, but if races develop dynamically and in some cases bits of genetic diversity die out, that's only an improvement in the "simulation" aspect. It would be cool if new genes are added later in the game (as in, in-game time) from random appearances or from outside sources (such as the mongols) but that's getting into a much deeper genetic simulation which... Honestly is totally possible from what the devs have already shared about how it works, so it would be cool even if not very related to the game's core focus. The pose I responded to (from a Paradox employee) said it isn't determined by genetics at all, but is an average value. Did you miss that? Or if you're referring to real life, then yes. I know. That stuff is layered on top of the "natural" tendency though. Rather than to prevent intentional cheating, I think it's more just to keep things fair in general, and only give them when the situation is equal. After all, if you don't care about them being meaningless you can always just add or remove achievements from your account with an external program anyway. Cheating for achievements is inherently a dumb thing to do.

## Reply 174 — participant_009 · 2020-08-23 · post-26823453

<!-- artifact:quote:start -->
> Cruxador said: According to the gene system already in the game. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> I don't think a single gene dying out in a game is a bit concern, they would be seeded to some extent from random characters, but if races develop dynamically and in some cases bits of genetic diversity die out, that's only an improvement in the "simulation" aspect. It would be cool if new genes are added later in the game (as in, in-game time) from random appearances or from outside sources (such as the mongols) but that's getting into a much deeper genetic simulation which... Honestly is totally possible from what the devs have already shared about how it works, so it would be cool even if not very related to the game's core focus. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Cruxador said: Doesn't that mean that the population of the game will trend strongly away from extremes? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> The pose I responded to (from a Paradox employee) said it isn't determined by genetics at all, but is an average value. Did you miss that? Click to expand...
<!-- artifact:quote:end -->
Do you mean the genetic traits? Which are incredibly clunky and unwieldy for this kind of task? So, first question, how the hell do you know how the game would progress under different skin-tone genetic models? Second, why is a quantized gene dying out due to genetic drift so much less less likely than homogeneity from all the interbreeding between races that basically never happens outside player control? Also, why is having genetic diversity die out "an improvement to the simulation aspect," but: a problem that needs to be changed? The only difference is how precise the two systems can be in how they render skin tones, and your system comes out worse in that regard. NOTHING in this game is determined by genetics. It's determined by computer code. I'm just using "genetics" to refer to anything that's inherited in a way meant to simulate actual genetics, because why would someone get into a snit about having different genetic traits represented differently in-game?

## Reply 175 — participant_094 · 2020-08-23 · post-26823473

<!-- artifact:quote:start -->
> Cruxador said: The pose I responded to (from a Paradox employee) said it isn't determined by genetics at all, but is an average value. Did you miss that? Click to expand...
<!-- artifact:quote:end -->
A random value between the two values, not the average value.

## Reply 176 — participant_085 · 2020-08-24 · post-26825090

Eh, I'd agree that skin tone being a result of mix of different genes with specific RGB value would be more modder-friendly than one image where you have to squeeze the already existing colors to fit the new ones in.

## Reply 177 — participant_009 · 2020-08-24 · post-26825548

<!-- artifact:quote:start -->
> SMiki Lorebringer said: Eh, I'd agree that skin tone being a result of mix of different genes with specific RGB value would be more modder-friendly than one image where you have to squeeze the already existing colors to fit the new ones in. Click to expand...
<!-- artifact:quote:end -->
That wasn't the problem you originally brought it up to solve. You didn't even think to mention it until some idiot misunderstood what you meant by eight genes and questioned how fantasy mods would work with only eight skin tones.

## Reply 178 — participant_094 · 2020-08-24 · post-26825570

With the way the skin tones are set up, it would be rather tricky to introduce new fantasy skintones without unintended behavior (such as, let's say a character with green skin has a child with another character with dark skin, the child would be very pale skinned, because the pale tones were between the green and the dark tones). I have no idea if it would be at all possible, but if the child's skin tone was not generated as a point on the tone map, but instead would temporarily generate a gradient between the values of the skin tones of the parents, and the child's skin tone would picked along that gradient - then you could have any number of skin tones that would mix more or less nicely. But, that would work fundamentally different from how the game is set up to handle skin tones, so I have no idea how feasible that would be.

## Reply 179 — participant_046 · 2020-08-24 · post-26825791

<!-- artifact:quote:start -->
> GreatWyrmGold said: That wasn't the problem you originally brought it up to solve. You didn't even think to mention it until some idiot misunderstood what you meant by eight genes and questioned how fantasy mods would work with only eight skin tones. Click to expand...
<!-- artifact:quote:end -->
There's no call for that. Misreading posts happens.

## Reply 180 — participant_095 · 2020-08-24 · post-26826608

One of the folders is called "lease_contracts" has anything relating to lease contracts been shown before?. im kinda interested in what this might entail. (leasing land for instance)

## Reply 181 — participant_096 · 2020-08-24 · post-26826741

Is there a mod creation tool with the launcher? Something that creates the necessary folders automatically and then I can just put in the edited files inside that folder?

## Reply 182 — participant_085 · 2020-08-24 · post-26826841

<!-- artifact:quote:start -->
> GreatWyrmGold said: That wasn't the problem you originally brought it up to solve. You didn't even think to mention it until some idiot misunderstood what you meant by eight genes and questioned how fantasy mods would work with only eight skin tones. Click to expand...
<!-- artifact:quote:end -->
I wasn't the person who brought the 8 genes thing. I only noted that different swathes of color mixing with one another would make it simpler for the modders to add new tones. It's not the end of the world though. The current one might work -- squeeze it a bit, add red to the left and green to blue to the right, with a bit of dark violet at lower right corner. It might give disappointing results in cases like unhealthy violet and fiery bright red giving birth to a mundane swarthy human, but I don't think such accuracy will be needed in most mods.

## Reply 183 — participant_009 · 2020-08-24 · post-26826858

<!-- artifact:quote:start -->
> DreadLindwyrm said: There's no call for that. Misreading posts happens. Click to expand...
<!-- artifact:quote:end -->
Yes there is. The idiot was me.

## Reply 184 — participant_097 · 2020-08-25 · post-26829478

It occurs to me that if 3D models can be inserted, then this could be used to make a total conversion for the Girl Genius world. A Europa full of mad scientists in eternal struggle with each other, truly special troops (carnivorous ducks and steam-powered dire teddy bears and so on), and the random events would be REALLY weird. The Spark runs in families, and there is a truly stupendous amount of backstabbing going on. If I remember right, one of the taglines was 'Mad science rules the world, but not very well'.

## Reply 185 — participant_009 · 2020-08-25 · post-26829636

<!-- artifact:quote:start -->
> Sesostris said: It occurs to me that if 3D models can be inserted, then this could be used to make a total conversion for the Girl Genius world. A Europa full of mad scientists in eternal struggle with each other, truly special troops (carnivorous ducks and steam-powered dire teddy bears and so on), and the random events would be REALLY weird. The Spark runs in families, and there is a truly stupendous amount of backstabbing going on. If I remember right, one of the taglines was 'Mad science rules the world, but not very well'. Click to expand...
<!-- artifact:quote:end -->
That would be cool, but it would take effort on the scale of the A Song of Ice and Fire mod to pull off decently. So either we need to get some serious fandom cross-pollination going on, or we need to wait for the hit HBO series that butchers the themes of the story in favor of blood and tits before crashing and burning from all the scuttled groundwork.

## Reply 186 — participant_098 · 2020-08-31 · post-26847217

I've heard mixed reports from Reddit, but will mods be allowed on the Gamepass version of CK3? Im assuming so as most of the mods go in the My Documents folder anyways but was just curious. Thanks for all you do!

## Reply 187 — participant_068 · 2020-09-01 · post-26851688

<!-- artifact:quote:start -->
> blackninja9939 said: You can relocalise them but other than that they are hardcoded, changing the time scale would need more support on the game end to do and I'd argue its a fairly niche modding need. As @ShadyGuy_SuspiciousGoal said, the 1.0 version is frozen from any changes unless they are of the severest impact and very critical as we do not want to risk introducing other issues into the build that could be worse than the one we fix. So for something low impact and that does not effect the vanilla game like this issue it is not considered a worthwhile risk to take. I answered in response to someone else, its handled by our "flavorization" system which deals with both the names of titles and the styling of character names as Count or Earl etc. It is something I have thought of, splitting into a hard and soft checksum but I've not had time to do this as its not really a high priority compared to features, bugs or performance work. It is one of the things on my list of things to investigate during our personal development time but that list of things to look at is pretty massive so no promises. Click to expand...
<!-- artifact:quote:end -->
Hi Blackninja - sorry to resurrect a post that's a few weeks old, but regarding the flavorization system... I would like to leverage this to port over my mod "Rank & File" from CK2 to CK3. However, there are some gaps with the new system that is preventing me from doing so. 1. It doesn't appear to be possible to use custom conditions in the flavorization titles. 2. We can't use custom scopes in flavorization titles - the only ones available (ruler_child and queen_mother) are hardcoded :/. Is there a chance we could see that functionality restored in the near future? I'd love to be able to port over my mod, and I don't think I'll be able to enjoy CK3 without it.

## Reply 188 — participant_008 · 2020-09-02 · post-26855416

<!-- artifact:quote:start -->
> Azarias59 said: Hi Blackninja - sorry to resurrect a post that's a few weeks old, but regarding the flavorization system... I would like to leverage this to port over my mod "Rank & File" from CK2 to CK3. However, there are some gaps with the new system that is preventing me from doing so. 1. It doesn't appear to be possible to use custom conditions in the flavorization titles. 2. We can't use custom scopes in flavorization titles - the only ones available (ruler_child and queen_mother) are hardcoded :/. Is there a chance we could see that functionality restored in the near future? I'd love to be able to port over my mod, and I don't think I'll be able to enjoy CK3 without it. Click to expand...
<!-- artifact:quote:end -->
Correct, for performance reasons the things we check are limited to specific checks instead of going through the entire trigger system as that overhead is too high. Sorry that your mod is now harder to implement for these flavour names like that, is there a subset of triggers that you specifically need to check as it may be possible for us to add them as other specific check options? I'm sure you'll be able to find some fun and enjoyment in the rest of the game though.

## Reply 189 — participant_068 · 2020-09-02 · post-26855796

<!-- artifact:quote:start -->
> blackninja9939 said: Correct, for performance reasons the things we check are limited to specific checks instead of going through the entire trigger system as that overhead is too high. Sorry that your mod is now harder to implement for these flavour names like that, is there a subset of triggers that you specifically need to check as it may be possible for us to add them as other specific check options? I'm sure you'll be able to find some fun and enjoyment in the rest of the game though. Click to expand...
<!-- artifact:quote:end -->
Hi blackninja - I appreciate the prompt response . A "has_character_flag" condition would be good, since I can hand those out via events. If that's done, I think I could solve the other half of my issues by using custom localization to emulate the "of <realm>" part of the title. I did a similar thing in CK2. I wrote a bit about my struggles with the new system in this post here: https://forum.paradoxplaza.com/foru...the-minor-title-system.1414940/#post-26854847 I think other modders will have similar challenges, specifically the AGOT team with their "Ser" title.

## Reply 190 — participant_008 · 2020-09-02 · post-26856362

<!-- artifact:quote:start -->
> Azarias59 said: Hi blackninja - I appreciate the prompt response . A "has_character_flag" condition would be good, since I can hand those out via events. If that's done, I think I could solve the other half of my issues by using custom localization to emulate the "of <realm>" part of the title. I did a similar thing in CK2. I wrote a bit about my struggles with the new system in this post here: https://forum.paradoxplaza.com/foru...the-minor-title-system.1414940/#post-26854847 I think other modders will have similar challenges, specifically the AGOT team with their "Ser" title. Click to expand...
<!-- artifact:quote:end -->
I'll look at adding a flag entry for a future patch.

## Reply 191 — participant_091 · 2020-09-02 · post-26856435

@blackninja9939 apologies for pinging you, but would it be possible to add "autopause = yes/no" (defaulting to "no") command/parameter/whatever to both "messages" and "important_actions" so that I and others who like various notifications to autopause could at least mod that in?

## Reply 192 — participant_068 · 2020-09-02 · post-26856540

<!-- artifact:quote:start -->
> blackninja9939 said: I'll look at adding a flag entry for a future patch. Click to expand...
<!-- artifact:quote:end -->
Thanks, glad to hear that. Also, if there was some way that we could have titles persist after death? In CK2 I used the "set_special_character_title" function for this - don't know if that could make a return.

## Reply 193 — participant_099 · 2020-09-04 · post-26865156

Really stupid question and I feel bad for asking, but I couldn't find an answer anywhere else and I've only recently started playing with the files. Where are the definitions given for kingdom CoAs? I want to change the coat of arms for Sicily but I cannot for the life of me find where and what to change. Nevermind, worked it out.

## Reply 194 — participant_039 · 2020-09-08 · post-26886824

<!-- artifact:quote:start -->
> blackninja9939 said: Currently we do not support creating your own new windows GUIs (though it is on my never ending to do list), but the easy work around there is just to make them as children of the main HUD window, which is always shown, and then you can have anything. Click to expand...
<!-- artifact:quote:end -->
Does anyone know how to do this? How to make new windows by making them children of the main HUD window? And in general how to work with the GUI. Will appreciate if anyone here can help me out.

## Reply 195 — participant_027 · 2020-09-10 · post-26895597

@blackninja9939 I have a complicated question. Is there a way to make army icons visible on the paper map (zoom level 20 or so)? I found this in map_icon_layer_templates.gui, but I couldn't change it to make it viewable when zoom level is equal or above 20. Is it hardcoded? Code: type container_allied_unit_icon_item = container { name = "allied_unit_icon_item" datacontext = "[UnitItem.GetArmy]" visible = "[Not(Or(UnitItem.IsUnitItemEnemy, UnitItem.IsUnitItemHostile))]" container_unit_effect_icons = { position = { 38 25 } } button_group = { block "onclick" { onclick = "[UnitMapIcon.OnClickArmyGroup( Army.Self )]" } I'm asking because I'm trying to make an accessibility mod for blind players. I was told by this poster that this change could make the game easier to play with OCR https://www.reddit.com/r/paradoxplaza/comments/ip6v26/_/g4n2l4f Thank you in advance!

## Reply 196 — participant_100 · 2020-09-11 · post-26898764

<!-- artifact:quote:start -->
> Nicolas-frm said: @blackninja9939 I have a complicated question. Is there a way to make army icons visible on the paper map (zoom level 20 or so)? I found this in map_icon_layer_templates.gui, but I couldn't change it to make it viewable when zoom level is equal or above 20. Is it hardcoded? Code: type container_allied_unit_icon_item = container { name = "allied_unit_icon_item" datacontext = "[UnitItem.GetArmy]" visible = "[Not(Or(UnitItem.IsUnitItemEnemy, UnitItem.IsUnitItemHostile))]" container_unit_effect_icons = { position = { 38 25 } } button_group = { block "onclick" { onclick = "[UnitMapIcon.OnClickArmyGroup( Army.Self )]" } I'm asking because I'm trying to make an accessibility mod for blind players. I was told by this poster that this change could make the game easier to play with OCR https://www.reddit.com/r/paradoxplaza/comments/ip6v26/_/g4n2l4f Thank you in advance! Click to expand...
<!-- artifact:quote:end -->
Just for further context, @blackninja9939 and anyone else interested, I'm trying to play CK3 using my screen reading program, as detailed in this post among other places. At the moment it's a little more annoying than it could be, particularly dealing with the map and armies, though honestly any help at all in making some of the relatively small changes for improved blind accessibility I outline would be very much appreciated. The "tooltips to clipboard/screen reaDer," idea alone would solve ~95% of my issues. As further elucidated in the linked Reddit post, my problem with armies is that it's difficult to find them because of the pixel hunting using the map currently requires. My own units can be found in the outliner but visible enemies cannot. @Nicolas-frm suggested that he might be able to create a mod to pan to enemy units, which would help quite a bit. I just wanted to drop a note to explain myself a bit and hope for further help, as I'm very much enjoying the game thus far but it could be so much easier with a few small enhancements. As a stopgap measure I was trying to figure out if I could copy the tooltip(s) currently displayed to the debug log, but there doesn't appear to be a way to do this. The OCR and map/army issues are my two biggest right now, and are kind of interrelated. If we can solve one or both, I'll be very much happier.

## Reply 197 — participant_027 · 2020-09-11 · post-26899389

<!-- artifact:quote:start -->
> BlindGuyNW said: Just for further context, @blackninja9939 and anyone else interested, I'm trying to play CK3 using my screen reading program, as detailed in this post among other places. At the moment it's a little more annoying than it could be, particularly dealing with the map and armies, though honestly any help at all in making some of the relatively small changes for improved blind accessibility I outline would be very much appreciated. The "tooltips to clipboard/screen reaDer," idea alone would solve ~95% of my issues. As further elucidated in the linked Reddit post, my problem with armies is that it's difficult to find them because of the pixel hunting using the map currently requires. My own units can be found in the outliner but visible enemies cannot. @Nicolas-frm suggested that he might be able to create a mod to pan to enemy units, which would help quite a bit. I just wanted to drop a note to explain myself a bit and hope for further help, as I'm very much enjoying the game thus far but it could be so much easier with a few small enhancements. As a stopgap measure I was trying to figure out if I could copy the tooltip(s) currently displayed to the debug log, but there doesn't appear to be a way to do this. The OCR and map/army issues are my two biggest right now, and are kind of interrelated. If we can solve one or both, I'll be very much happier. Click to expand...
<!-- artifact:quote:end -->
So here is the mod: https://steamcommunity.com/sharedfiles/filedetails/?id=2225500765 This is more of a start. What this currently does is pan the camera to one of the enemy troops. For now it creates a list of armies that are fighting you and pan the camera to one of them randomly each time you click the button. If you have suggestions on how to make it work better please let me know. I could make a list of buttons for every army too. If it pans the camera and no tooltip appears, it means that the army is currently not in sight of player view (hidden by fog of war). I added the button under the decisions tab button. But the issue with shortcuts, is apparently mods aren't allowed to add them in for the players. You will have to add it yourself if you can in the game folder. The shortcut for such feature is called "pan_to_enemy". The shortcut folder for CK3 can be located in: C:\Program Files (x86)\Steam\steamapps\common\Crusader Kings III\game\gui The file is called "shortcuts.shortcuts". An example is to add a line: pan_to_enemy = "F10" F10 is currently unused in CK3 but you can replace it with any key you like. I will continue supporting this mod with other features. If this works well, I can add a similar mechanic for ally troops as well. I will just need your feedback on what changes may improve the experience for you. Thank you!

## Reply 198 — participant_068 · 2020-09-29 · post-26968623

<!-- artifact:quote:start -->
> blackninja9939 said: I'll look at adding a flag entry for a future patch. Click to expand...
<!-- artifact:quote:end -->
Hi @blackninja9939 - did this make it into the 1.1 patch? I didn't see it referenced in the patch notes, however, I didn't know if a minor change in this area would've been noted. If not, do you know when we should expect it to make it into the game?

## Reply 199 — participant_068 · 2020-10-15 · post-27019885

<!-- artifact:quote:start -->
> Azarias59 said: Hi @blackninja9939 - did this make it into the 1.1 patch? I didn't see it referenced in the patch notes, however, I didn't know if a minor change in this area would've been noted. If not, do you know when we should expect it to make it into the game? Click to expand...
<!-- artifact:quote:end -->
Hi @blackninja9939. It's been a few weeks, just thought I'd give this a bump to see if you saw the message.

## Reply 200 — participant_085 · 2020-10-20 · post-27032929

@blackninja9939 are there any plans on fixing the issue with the map crashing after exceeding 8192px height? 14k seems to work for width, but it's impossible to exceed 8k in height atm. Fixing the issue would greatly help with mods set in regions that are more vertical than horizontal, such as the Americas. [Map Modding] Increasing Map Dimensions Over 8192x4096? CONCLUSION EDIT: Exceeding the height dimension of the map by 8192 leads to graphical issues So the vanilla map dimensions are 8192x4096. From what I can tell, you need to change the dimensions of the heightmap.png, provinces.png, rivers.png... forum.paradoxplaza.com

