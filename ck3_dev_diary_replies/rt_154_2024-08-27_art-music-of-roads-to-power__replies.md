---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1700890/"
forum_thread_id: 1700890
content_type: reply_thread
parent_dd_file: dd_154_2024-08-26_art-music-of-roads-to-power.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 154
title: "Dev Diary #154 - Art & Music of Roads to Power"
dd_date: 2024-08-27
expansion: Roads to Power
patch: Patch 1.13
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 7
reply_count: 130
participant_count: 108
reply_date_first: 2024-08-27
reply_date_last: 2024-09-06
body_word_count: 11637
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

# Reply thread — Dev Diary #154 - Art & Music of Roads to Power

*130 replies from 108 participants across 7 pages*

## Reply 1 — participant_001 · 2024-08-27 · post-29849134

<!-- artifact:quote:start -->
> X_FloW said: No armor for women? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> vyshan said: Some questions: 1.) Will the greek temple building be used for just greek culture, the Byzantine culture group, or for any orthodox? 2.) There are early and late clothing styles, what determines the changing of it from one style to another? 3.) Will this feature apply to other cultures, thinking of say the Norse and them adopting clothing of the rest of europe. 4.) Do wanders get anything unique for clothing? 5.) what is next week's dev diary? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> AHumpierRogue said: Great DD! Lovely art. For the eras, is the idea that Era 1 is Tribal+Early Medieval and Era 2 is High + Late medieval? I'd like for there to eventually be a bespoke Late Medieval era added eventually too, though of course that's a ton of asset work added. Could share assets with Project Caeser perhaps (Only joking... unless!?!?!?!?). Either way, really lovely stuff. I especially like the women's clothing, looking very snazzy and embraces the silly hats that are at the core to the human experience. The armor is also nice. When it says there's two armors, is that per era or just 1 per era? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> bfunk86 said: The music player addition is huge. Will we be able to import songs (like from CK2 maybe?) and play them? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Fall of Stars said: One question - I have a lot of modded music, is there anything you can share about how the music player will interact with music mods? Will it be possible to make custom "sets" for mods like we see for the DLC in the screenshot and enable/disable them, or include titles for mod songs in localization? Click to expand...
<!-- artifact:quote:end -->
This post is reserved by the Community Team for collecting developer responses within the thread. There are female versions of those two armors, but they do look the same as the male ones (adjusted to fit the female proportions). I'll answer the ones I know the answer to 2.) This is based on character age and current year (young people will be earlier adopters of the new style) which gives a gradual transition over 50 ish years. A proper mechanic would be cool but would require so many assets! 3.) It was implemented for Western Europe with Tours and Tournaments, and the ambition is to keep adding it for more cultures, including Norse (like you suggest perhaps by having them switch to Western Europe styles at some point). 4.) Currently, no. The focus for clothing was very much to flesh out the Byzantine culture. The early era is based on the time period from before game start (around 650) to around 1000 AD (so in game terms it is just the "tribal" era). The "late" era is primarily based on sources from 1000 to around 1200 (so early and high medieval). I would love to add a separate Palaiologan set for the late Medieval era Byzantium, as well as a full European one of course. Who knows what might happen in the future! We added one new armor per era, but there are already a number of Byzantine armors in the game, so we do get a pretty nice variety. The contents of the music player is moddable. For those who're already modding music into the game, there's just a few more steps you have to do in order to have the songs show in the music player. To add the Music tracks we wish to put into the Music Player into categories. To do this they must be implemented with the following files structure: Code: game └ music ├ music_categories │ └ music_categories.txt └ music.txt The music.txt files contain information on the tracks themselves, and in order to have them localized they all must have a name = loc_key field. Example: Code: mx_raid = { music = "event:/DLC/FP1/MUSIC/cuetracks/mx_raid" name = fp1_soundtrack_01_the_raid pause_factor = 35 } The music_category.txt files will then contain information on the categories and tracks contained within: Code: category = { id = "mx_category_10" name = "fp2_cue_soundtrack" tracks = { "mx_IberiaWar" "mx_Struggle_ending_compromise" "mx_Struggle_ending_conciliation" "mx_Struggle_ending_hostility" "mx_Struggle_Opening" } } It is important to note that the id field in these categories must be unique. Finally to get the art in, they'll be put into, using the above category as an example: Code: game └ gfx └ interface └ illustrations └ music_player └ fp2_cue_soundtrack.dds Of course all the audio banks and all that must also be added into it.

## Reply 2 — participant_002 · 2024-08-27 · post-29849154

I think this will be the best DLS of all time for CK3, thanks to the developers for their work! I have a few small questions.: 1) Will there be any unique names of cultures when hybridizing with Greek, such as the Outremer culture in Jerusalem? (I would like to arrange a role-playing game for the French settlers, after the 4th Crusade, who would assimilate with the Greeks, they could be called Latins) 2) In the last developer's diary, you wrote that the Albanian culture will appear, but will there be any unique solutions for this culture? 3) Will there be any other new cultures in the Byzantine region?

## Reply 3 — participant_003 · 2024-08-27 · post-29849160

Will Roman polytheism get reworks? I don't want worshipping Greek deities. It would be glorious if we could worshipping Mars or Sol Invictus

## Reply 4 — participant_004 · 2024-08-27 · post-29849163

Thank you for my next collection of amazing Wallpapers!

## Reply 5 — participant_005 · 2024-08-27 · post-29849168

I would really love for the CK2 soundtracks to also show up in the music player.

## Reply 6 — participant_006 · 2024-08-27 · post-29849169

i have a question will Hold Triumph be only avalible for Byzantines or we will get a similar thing for everyone else? i didnt read the previous dev diary so im not relly familary with it

## Reply 7 — participant_007 · 2024-08-27 · post-29849181

No armor for women? Also is there a chance the soundtrack might release before the DLC, like it did with Legacy of Persia?

## Reply 8 — participant_008 · 2024-08-27 · post-29849182

Gorgeous art, and as they say, give my compliments to the chef! Seriously, the artists here do amazing work. It often is taken for granted, but it helps setting the stage, fine work indeed. Especially looking forward to the music, and the music player (and not just a simplistic one!) is the cherry on top! A few questions remain: How long do you intend to tease us about coronations and not introducing it as a grand activity? You mentioned Restoration of Rome; tell us more! It's almost a crime to talk about the new music, music player, and not have at least something for the ear. It's hard to listen to the new music in the video DD, as the voice talks over it. This is the third time in a row now, that you're not telling us at the end about next week's DD. Tell us, what will next week's DD be about? Looking forward to the entire expansion, most anticipated release after Tours and Tournaments!

## Reply 9 — participant_009 · 2024-08-27 · post-29849183

will you be able to get struck by a lightning if you travel in a storm?

## Reply 10 — participant_010 · 2024-08-27 · post-29849185

I know its not about this dev diary but will Munis al Muzaffar (the greek eunuch in 867) be a playable adventurer? He was very influential in the Abbasid Caliphate. He became a sort of kingmaker. He had an achievement in ck2. He is now a courtier for one the greek dukes. Also will the 4th crusade form the Latin Empire and splinter the rest of the Byzantines (Nikea/Trebizond/Epirus)? Will the sucessor states be admin?

## Reply 11 — participant_011 · 2024-08-27 · post-29849186

Love the brilliant arts! but, hey, you promised you'll talk about Hasan i Sabbah some weeks ago! If you couldn't fit it in next diaries, what about describing it NOW?

## Reply 12 — participant_001 · 2024-08-27 · post-29849189

<!-- artifact:quote:start -->
> Angrum877 said: Thank you for my next collection of amazing Wallpapers! Click to expand...
<!-- artifact:quote:end -->
On that note: The images shown in the DD are scaled down to fit the forum page, but you can see the original full-size version by right-clicking an image and opening it in a new tab.

## Reply 13 — participant_012 · 2024-08-27 · post-29849190

Can you tell how many unique buildings were added?

## Reply 14 — participant_013 · 2024-08-27 · post-29849192

Hi, I have two quick questions: 1. Will we have an option to fight/support npcs with conqueror traits as landless players. I'd love to have an option to sometimes go with the flow and get myself a kingdom from supporting powerfull warlord (especially, if he's busy fighting my old imperium, which I got bored of) 2. After new dlc will iranian resurgance decision (or other decisions already in the game) let me change into administrative goverment? I'm currently busy researching and planning my playthroughs with new dlc and I'd love to know all the ways to play administrative content.

## Reply 15 — participant_014 · 2024-08-27 · post-29849196

Give the artist responsible a raise! This is excellent! Also finally a music player, thank you!

## Reply 16 — participant_015 · 2024-08-27 · post-29849198

<!-- artifact:quote:start -->
> Sofyan Rghiwi said: I would really love for the CK2 soundtracks to also show up in the music player. Click to expand...
<!-- artifact:quote:end -->
Exactly, would be great. HoI4 team did this so it shouldn't be much of a problem.

## Reply 17 — participant_016 · 2024-08-27 · post-29849199

Did you change the word for Knights? and what is the new word for it? ^_^ Edit: Can we also get access to that "Miro board" with all that imagery all in one place? pretty please?

## Reply 18 — participant_017 · 2024-08-27 · post-29849200

Great Art, costumes and music!! Would like to ask for this characters to be in the 867 game start as landless. Beowulf Siegfried Fafnir Even if they were just a reference to the real legends. Thank you all for the good work.

## Reply 19 — participant_018 · 2024-08-27 · post-29849201

The art is all beautiful, I can't wait to jump in.

## Reply 20 — participant_019 · 2024-08-27 · post-29849202

All of this looks gorgeous, and it's always lovely to see what you've been able to do with the sources available. I'm sure it'll look even better in game. I can't comment sensibly on the particulars, unlike gameplay-devoted diaries, but please don't take that as a sign of less interest!

## Reply 21 — participant_020 · 2024-08-27 · post-29849203

I really love seeing the changes the Byzantine Empire is getting through their style of clothes and the artwork meant for them. Really fantastic! But with the mention of the Copts, I wonder if this means they'll get introduced through this expansion. Will it mean that other cultures will get introduced/reworked? Anyhow, keep it up with some glorious content. Τῷ πατάξαντι βασιλεῖς μεγάλους άλληλούϊα

## Reply 22 — participant_021 · 2024-08-27 · post-29849208

Did I misremember or was there mention that the different camp purposes would mean new sets of clothes for adventurers were included?

## Reply 23 — participant_008 · 2024-08-27 · post-29849210

Oh, and before I forget it, I'd like to say how much I appreciate that in the throne room, the emperor sits alone up there, while the empress has heir own chair below to the side. It's a nice touch.

## Reply 24 — participant_022 · 2024-08-27 · post-29849214

Can we see the different styles of Estate for western and MENA?

## Reply 25 — participant_023 · 2024-08-27 · post-29849215

Really interesting DD! Could you tell us more about the "Restoration of Rome" decision and then, will new Legends be introduced?

## Reply 26 — participant_024 · 2024-08-27 · post-29849221

This is always the part of the Dev Diaries that never disappoints. The Art Department is always solid

## Reply 27 — participant_004 · 2024-08-27 · post-29849224

Now that I have read the thing: I very much like the sandstorm effect, that looks very good! I'm also very excited to hear the orthodox chants! One question about the culture-dependent designs: What is MENA? I don't know that abbreviation. Best thing I've come up with is Middle-East-North-African. And the first idea of the estate was very funny, I just imagined someone spamming every building slot in his estate full of barracks, starcraft style

## Reply 28 — participant_025 · 2024-08-27 · post-29849228

What would happen if a non-Christian emperor ruled Byzantium? Would the throne room change, by removing the christian imagery?

## Reply 29 — participant_022 · 2024-08-27 · post-29849234

Some questions: 1.) Will the greek temple building be used for just greek culture, the Byzantine culture group, or for any orthodox? 2.) There are early and late clothing styles, what determines the changing of it from one style to another? 3.) Will this feature apply to other cultures, thinking of say the Norse and them adopting clothing of the rest of europe. 4.) Do wanders get anything unique for clothing? 5.) what is next week's dev diary?

## Reply 30 — participant_026 · 2024-08-27 · post-29849236

<!-- artifact:quote:start -->
> Almozor370 said: Will Roman polytheism get reworks? I don't want worshipping Greek deities. It would be glorious if we could worshipping Mars or Sol Invictus Click to expand...
<!-- artifact:quote:end -->
With the amount of fornication in this game the existence of priestesses of Vesta (Vestal Virgins) is impossible. They would be executed on a regular basis.

## Reply 31 — participant_022 · 2024-08-27 · post-29849242

<!-- artifact:quote:start -->
> Angrum877 said: Now that I have read the thing: I very much like the sandstorm effect, that looks very good! I'm also very excited to hear the orthodox chants! One question about the culture-dependent designs: What is MENA? I don't know that abbreviation. Best thing I've come up with is Middle-East-North-African. And the first idea of the estate was very funny, I just imagined someone spamming every building slot in his estate full of barracks, starcraft style Click to expand...
<!-- artifact:quote:end -->
MENA means Middle East and North Africa. Though in the code it is far broader then that, and also includes India and a good chunk of the steppe too IIRC.

## Reply 32 — participant_005 · 2024-08-27 · post-29849247

I hope one day the Tours and Tournaments screen would have a similar style to that of Admin Estates and Adventurer Campsites.

## Reply 33 — participant_027 · 2024-08-27 · post-29849267

For the event pictures, wouldn't more religion neutral picture for the throne room picture without Chi Rho be good for alternative religious gameplays with the byzantines/romans?

## Reply 34 — participant_028 · 2024-08-27 · post-29849271

Amazing as always. The art and graphics teams have truly outdone themselves in bringing the era to life. I assume however that given this dev diary's place in the pipeline, with three weeks of diaries left before the release, we've reached the end of your showcase for paid content, and the next two weeks will be spent showing us free content such as the scheming rework and changes to existing decisions? That is if the final week before release is dedicated solely to patch notes as is tradition at this point, of course.

## Reply 35 — participant_029 · 2024-08-27 · post-29849276

Any chance we can get a little peak into dlcs music piece without voiceover from the dev diary video?

## Reply 36 — participant_030 · 2024-08-27 · post-29849279

Would there be another culture besides Greek that would have Greek fashion or architecture, or would it be limited to that culture and those descended from it? In this sense, would Türkmân be considered as descended from Greek (as a historical hybrid between it and Oghuz)?

## Reply 37 — participant_031 · 2024-08-27 · post-29849286

Huh, we usually get art dev diaries closer to the release of the DLC! Only three more Dev Diaries to go!

## Reply 38 — participant_032 · 2024-08-27 · post-29849289

Is Constantinople unique in any mechanical way, beside graphical? It was the beating heart of Byzantine Empire. It would be a shame if I could just conquer the city, but the Empire continues on as if nothing major happened.

## Reply 39 — participant_007 · 2024-08-27 · post-29849290

<!-- artifact:quote:start -->
> vyshan said: MENA means Middle East and North Africa. Though in the code it is far broader then that, and also includes India and a good chunk of the steppe too IIRC. Click to expand...
<!-- artifact:quote:end -->
India has its own GFX category

## Reply 40 — participant_033 · 2024-08-27 · post-29849293

The music player addition is huge. Will we be able to import songs (like from CK2 maybe?) and play them?

## Reply 41 — participant_034 · 2024-08-27 · post-29849294

I love the Tyrian Purple cloth the map is placed on top of.

## Reply 42 — participant_035 · 2024-08-27 · post-29849296

We keep seeing the 4th crusade event but can I ask when we'll get a dev diary discussing it?

## Reply 43 — participant_036 · 2024-08-27 · post-29849300

Always fascinating to watch the creative process when it comes to deciding how the art is going to come to be. I only have 2 things to when it comes to this diary. Firstly, when it comes to the colors of the alerts, that's a good change. A quick glance and you have a better idea of how quickly you need to get to them. My only complaint and suggestion is that Red and Green might not be the best choices of colors. I can't speak for others, but for me, in the image shared of it, I see 2 colors, not 3. You see, I'm read green colorblind and while I can see them, they also tend to blend together for me if they are certain shades. The blue ones, those stand out just fine. The other issue I wanted to bring up. Previously, you guys brought in a neat little feature to add a tag to the events to show what it's from. Only, in all the images of events you've shared from Roads to Power, none of them use this tag. It's bad enough that modders don't use it to let us tell which events are from their mods, but it's something else when you guys don't use it to tell us what DLC an event is from.

## Reply 44 — participant_037 · 2024-08-27 · post-29849304

Huge kudos to the artists,they did a spectacular job.

## Reply 45 — participant_038 · 2024-08-27 · post-29849307

No indian ans african themes for estates and camps Dissapointing

## Reply 46 — participant_039 · 2024-08-27 · post-29849315

<!-- artifact:quote:start -->
> lucas.ribeiro.rodrigues said: View attachment 1179586 Click to expand...
<!-- artifact:quote:end -->
Will we learn more about Fourth Crusade mechanics in a future dev diary?

## Reply 47 — participant_040 · 2024-08-27 · post-29849319

Wow, that looks (and probably also sounds) incredible!

## Reply 48 — participant_022 · 2024-08-27 · post-29849329

Will the Icons in the throne room be removed if their is a second Iconoclastic revival?

## Reply 49 — participant_041 · 2024-08-27 · post-29849343

Everything looks spectacular; I love it so much! I agree that having CK2 imported music in the player would be a huge addition. You could always limit it to those who have the game and its DLC already bought on Steam if that's a problem

## Reply 50 — participant_042 · 2024-08-27 · post-29849349

This expansion looks great. Will there be any content for the other Byzantine heritage cultures? I'm particularly thinking of Georgia and Armenia.

## Reply 51 — participant_043 · 2024-08-27 · post-29849353

Wow, beautiful art!

## Reply 52 — participant_044 · 2024-08-27 · post-29849364

Hi, amazing work! I would like to know if the culture in the Balkans has also been revised for the dlc. I'm interested if the Aromanians are now oresent on the map instead of formable by hybridization since the Eastern Latins were around the game period and much more numerous than today.

## Reply 53 — participant_045 · 2024-08-27 · post-29849365

All the new arts and assets are very beautiful, and thank you for adding the music player as well. Will we see some of the CKII songs come back like Vicky III and HoI IV brought back some the past titles soundtracks?

## Reply 54 — participant_046 · 2024-08-27 · post-29849376

Does greek, orthodox temple holdings also get new 2D holding pictures or only just the castles and the cities? Can you show them also, please? There weren't showed in the DD

## Reply 55 — participant_047 · 2024-08-27 · post-29849380

Will you rework the Orthodoxy system so there is more than one patriarch?

## Reply 56 — participant_048 · 2024-08-27 · post-29849384

Hey Paradox, a couple things. First off, your babies are freaking CREEPY! Can we get an animation where a/the wetnurse carries the baby until a certain age? Obviously in a way that places the focus on the baby. You could even easily use that animation for a bunch of events around parenthood and early childhood. But seriously, your babies are CREEPY. Major Grey Alien or Changeling vibes. Second, is there any chance that the inability to choose river or water tiles for travel will be fixed at some point? It messes a whole bunch of things up. From a gameplay standpoint, if I want to sail the entire way I feel like that should be an option. From a modding standpoint, it means that modders have a much harder time adding river events. Which is odd, since rivers matters more than seas for most people until further along in history. Finally, holy crap I love the weather effects! How much are these spread out through old events? Do you have plans for more in the future, because that would be awesome! Things like volcanos, tornados, hurricanes, etc. Was the addition of these effects an afterthought or just tacked on for fun, or was it part of a system that you've wanted to do for a while?

## Reply 57 — participant_049 · 2024-08-27 · post-29849389

Great DD! Lovely art. For the eras, is the idea that Era 1 is Tribal+Early Medieval and Era 2 is High + Late medieval? I'd like for there to eventually be a bespoke Late Medieval era added eventually too, though of course that's a ton of asset work added. Could share assets with Project Caeser perhaps (Only joking... unless!?!?!?!?). Either way, really lovely stuff. I especially like the women's clothing, looking very snazzy and embraces the silly hats that are at the core to the human experience. The armor is also nice. When it says there's two armors, is that per era or just 1 per era? Bit of a shame to see India missing out on the GFX, but maybe that's a sign for future India DLC? I think that, of the regions on the map currently India is pretty high up there with regions that deserve an actual bespoke expansion alla Byzantium to flesh them out instead of "just" flavor packs. So maybe that DLC could update their GFX. Though not necessarily soon.

## Reply 58 — participant_050 · 2024-08-27 · post-29849392

<!-- artifact:quote:start -->
> lucas.ribeiro.rodrigues said: View attachment 1179537 Click to expand...
<!-- artifact:quote:end -->
Isn't it a bit silly and incongruous to represent a fairly accurate modern map on a floor mosaic like this? I believe there are some reconstructions at least of contemporary world maps that could have been used instead.

## Reply 59 — participant_051 · 2024-08-27 · post-29849394

Hello, Mother.

## Reply 60 — participant_052 · 2024-08-27 · post-29849397

Did I miss it or has the map graphic for Constantinople not been shown off? I think there was one screenshot a few DD's ago that had it obscured by an emblem.

## Reply 61 — participant_053 · 2024-08-27 · post-29849420

Looks really good!

## Reply 62 — participant_039 · 2024-08-27 · post-29849427

<!-- artifact:quote:start -->
> lucas.ribeiro.rodrigues said: View attachment 1179586 Click to expand...
<!-- artifact:quote:end -->
Due to the upcoming adventurer mechanics and the ability to switch to wayward dynasty members, will the player have the opportunity to play as an Alexios IV Angelos analogue and trigger the Fourth Crusade themselves? Or is the Alexios IV Angelos analogue always a random claimant? Also, is Venice always a sponsor of the Fourth Crusade? Or can it be any maritime republic? Will a Fourth Crusade still trigger even if Byzantium or another power conquers Venice and the other maritime republics in advance?

## Reply 63 — participant_054 · 2024-08-27 · post-29849434

Man, that is some beautiful art. I wish muslims and christians in Iberian had more of this. More art like this to at least differetiate one of the other. I'd LOVE to see more character backgrounds for them, not only the muslim ones for all of them.

## Reply 64 — participant_035 · 2024-08-27 · post-29849440

<!-- artifact:quote:start -->
> ScribeofNekoti said: Hey Paradox, a couple things. First off, your babies are freaking CREEPY! Can we get an animation where a/the wetnurse carries the baby until a certain age? Obviously in a way that places the focus on the baby. You could even easily use that animation for a bunch of events around parenthood and early childhood. But seriously, your babies are CREEPY. Major Grey Alien or Changeling vibes. Second, is there any chance that the inability to choose river or water tiles for travel will be fixed at some point? It messes a whole bunch of things up. From a gameplay standpoint, if I want to sail the entire way I feel like that should be an option. From a modding standpoint, it means that modders have a much harder time adding river events. Which is odd, since rivers matters more than seas for most people until further along in history. Finally, holy crap I love the weather effects! How much are these spread out through old events? Do you have plans for more in the future, because that would be awesome! Things like volcanos, tornados, hurricanes, etc. Was the addition of these effects an afterthought or just tacked on for fun, or was it part of a system that you've wanted to do for a while? Click to expand...
<!-- artifact:quote:end -->
The just stand there...... Menacingly

## Reply 65 — participant_055 · 2024-08-27 · post-29849441

<!-- artifact:quote:start -->
> X_FloW said: No armor for women? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> vyshan said: Some questions: 1.) Will the greek temple building be used for just greek culture, the Byzantine culture group, or for any orthodox? 2.) There are early and late clothing styles, what determines the changing of it from one style to another? 3.) Will this feature apply to other cultures, thinking of say the Norse and them adopting clothing of the rest of europe. 4.) Do wanders get anything unique for clothing? 5.) what is next week's dev diary? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> AHumpierRogue said: Great DD! Lovely art. For the eras, is the idea that Era 1 is Tribal+Early Medieval and Era 2 is High + Late medieval? I'd like for there to eventually be a bespoke Late Medieval era added eventually too, though of course that's a ton of asset work added. Could share assets with Project Caeser perhaps (Only joking... unless!?!?!?!?). Either way, really lovely stuff. I especially like the women's clothing, looking very snazzy and embraces the silly hats that are at the core to the human experience. The armor is also nice. When it says there's two armors, is that per era or just 1 per era? Click to expand...
<!-- artifact:quote:end -->
There are female versions of those two armors, but they do look the same as the male ones (adjusted to fit the female proportions). I'll answer the ones I know the answer to 2.) This is based on character age and current year (young people will be earlier adopters of the new style) which gives a gradual transition over 50 ish years. A proper mechanic would be cool but would require so many assets! 3.) It was implemented for Western Europe with Tours and Tournaments, and the ambition is to keep adding it for more cultures, including Norse (like you suggest perhaps by having them switch to Western Europe styles at some point). 4.) Currently, no. The focus for clothing was very much to flesh out the Byzantine culture. The early era is based on the time period from before game start (around 650) to around 1000 AD (so in game terms it is just the "tribal" era). The "late" era is primarily based on sources from 1000 to around 1200 (so early and high medieval). I would love to add a separate Palaiologan set for the late Medieval era Byzantium, as well as a full European one of course. Who knows what might happen in the future! We added one new armor per era, but there are already a number of Byzantine armors in the game, so we do get a pretty nice variety.

## Reply 66 — participant_056 · 2024-08-27 · post-29849445

Really pleased with the UI improvements. Not intended as a criticism but I think one of reasons events are complained about in CK3 isn't the writing of the event but presentation: in CK2 you had unique and distinctive art and now you often have characters against a background. So adding more varied backgrounds, more animations, and also colour variations will make me want to engage with the events more!

## Reply 67 — participant_057 · 2024-08-27 · post-29849448

All this new art looks amazing and really well made, love it. One of my personal favorite things is the new unique 2D art for the holding of Constantinople itself, looks great! I hope we'll get more of these for other unique holdings aswell (like Rome, Paris, Baghdad, etc.). Also, will there be any unique content/art for the holding of Rome itself?

## Reply 68 — participant_058 · 2024-08-27 · post-29849451

This is all really impressive and it's gonna be hard to wait another month! Thanks for all this transparency and hard work. One question - I have a lot of modded music, is there anything you can share about how the music player will interact with music mods? Will it be possible to make custom "sets" for mods like we see for the DLC in the screenshot and enable/disable them, or include titles for mod songs in localization?

## Reply 69 — participant_007 · 2024-08-27 · post-29849455

<!-- artifact:quote:start -->
> Niall9 said: Really pleased with the UI improvements. Not intended as a criticism but I think one of reasons events are complained about in CK3 isn't the writing of the event but presentation: in CK2 you had unique and distinctive art and now you often have characters against a background. So adding more varied backgrounds, more animations, and also colour variations will make me want to engage with the events more! Click to expand...
<!-- artifact:quote:end -->
Another complaint for events is repetitive events, a lot of people have no problems with frequency (I myself would want as many as possible as long as they're varied), it's seeing the same event over and over.

## Reply 70 — participant_059 · 2024-08-27 · post-29849474

Credit to the artist for the artwork and costumes, they all look great.

## Reply 71 — participant_060 · 2024-08-27 · post-29849477

Regarding "Miscellaneous Improvements": 1) Will we see finally Coptic culture (Remenkemi would be a proper name)? 2) Due the new start date, will we finally see deleted the out of place split between Galician and Portuguese in the Iberian P.?

## Reply 72 — participant_048 · 2024-08-27 · post-29849484

Will the Parthenon in Athens make an appearance? Your temple of Theotokos seems similar as a model.

## Reply 73 — participant_061 · 2024-08-27 · post-29849488

<!-- artifact:quote:start -->
> bfunk86 said: The music player addition is huge. Will we be able to import songs (like from CK2 maybe?) and play them? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Fall of Stars said: One question - I have a lot of modded music, is there anything you can share about how the music player will interact with music mods? Will it be possible to make custom "sets" for mods like we see for the DLC in the screenshot and enable/disable them, or include titles for mod songs in localization? Click to expand...
<!-- artifact:quote:end -->
The contents of the music player is moddable. For those who're already modding music into the game, there's just a few more steps you have to do in order to have the songs show in the music player. To add the Music tracks we wish to put into the Music Player into categories. To do this they must be implemented with the following files structure: Code: game └ music ├ music_categories │ └ music_categories.txt └ music.txt The music.txt files contain information on the tracks themselves, and in order to have them localized they all must have a name = loc_key field. Example: Code: mx_raid = { music = "event:/DLC/FP1/MUSIC/cuetracks/mx_raid" name = fp1_soundtrack_01_the_raid pause_factor = 35 } The music_category.txt files will then contain information on the categories and tracks contained within: Code: category = { id = "mx_category_10" name = "fp2_cue_soundtrack" tracks = { "mx_IberiaWar" "mx_Struggle_ending_compromise" "mx_Struggle_ending_conciliation" "mx_Struggle_ending_hostility" "mx_Struggle_Opening" } } It is important to note that the id field in these categories must be unique. Finally to get the art in, they'll be put into, using the above category as an example: Code: game └ gfx └ interface └ illustrations └ music_player └ fp2_cue_soundtrack.dds Of course all the audio banks and all that must also be added into it.

## Reply 74 — participant_062 · 2024-08-27 · post-29849495

The Mausoleum at Halicarnassus is noticeably absent from that showcase of special buildings.

## Reply 75 — participant_063 · 2024-08-27 · post-29849499

<!-- artifact:quote:start -->
> Angrum877 said: Now that I have read the thing: I very much like the sandstorm effect, that looks very good! I'm also very excited to hear the orthodox chants! One question about the culture-dependent designs: What is MENA? I don't know that abbreviation. Best thing I've come up with is Middle-East-North-African. And the first idea of the estate was very funny, I just imagined someone spamming every building slot in his estate full of barracks, starcraft style Click to expand...
<!-- artifact:quote:end -->
You are correct, MENA is an acronym exactly for those regions since North Africa is much closer to the history and culture of the middle east rather than Sub-Saharan Africa.

## Reply 76 — participant_064 · 2024-08-27 · post-29849505

Wow we VN now lol

## Reply 77 — participant_065 · 2024-08-27 · post-29849517

Reading this DD while visiting Istanbul and sitting in front of the Hagia Sophie is 10/10

## Reply 78 — participant_066 · 2024-08-27 · post-29849519

Honestly the new art for the DLC looks truly decadent, well suited to Eastern Romans. I’m perhaps being cheeky but I noticed that on the new table design there was a map of the new start date. Would we be able to get a closer view of it.

## Reply 79 — participant_067 · 2024-08-27 · post-29849522

The Court Amenity invalidated toast notification is just.... /chef kiss.

## Reply 80 — participant_068 · 2024-08-27 · post-29849527

Will religious discussions be represented, for example Christological, so characteristic of Byzantine history?

## Reply 81 — participant_056 · 2024-08-27 · post-29849543

<!-- artifact:quote:start -->
> X_FloW said: Another complaint for events is repetitive events, a lot of people have no problems with frequency (I myself would want as many as possible as long as they're varied), it's seeing the same event over and over. Click to expand...
<!-- artifact:quote:end -->
I think frequency and repetitiveness are related though. Because they are so frequent they get repeated more often. For me, it's less about frequency or repetitiveness, but impact. I don't mind if events became more frequent or less if they are more consequential. The most exciting ones are ones which can lead to an unexpected death that changes succession, or sparks a war.

## Reply 82 — participant_069 · 2024-08-27 · post-29849545

Oh my god, the toasts and character event icons look so good. The art is amazing. You guys always do such incredible work. I really love the rejected splash screen, too, probably even more than that awesome coronation—I'm glad it's being reused for something else. Unfortunately, I'm not going to be able to play this game for a while after it comes out, as I'm going to be too busy giddily listening to the golden lions banging their tails and roaring.

## Reply 83 — participant_070 · 2024-08-27 · post-29849560

<!-- artifact:quote:start -->
> NilsW said: There are female versions of those two armors, but they do look the same as the male ones (adjusted to fit the female proportions). I'll answer the ones I know the answer to 2.) This is based on character age and current year (young people will be earlier adopters of the new style) which gives a gradual transition over 50 ish years. A proper mechanic would be cool but would require so many assets! 3.) It was implemented for Western Europe with Tours and Tournaments, and the ambition is to keep adding it for more cultures, including Norse (like you suggest perhaps by having them switch to Western Europe styles at some point). 4.) Currently, no. The focus for clothing was very much to flesh out the Byzantine culture. The early era is based on the time period from before game start (around 650) to around 1000 AD (so in game terms it is just the "tribal" era). The "late" era is primarily based on sources from 1000 to around 1200 (so early and high medieval). I would love to add a separate Palaiologan set for the late Medieval era Byzantium, as well as a full European one of course. Who knows what might happen in the future! We added one new armor per era, but there are already a number of Byzantine armors in the game, so we do get a pretty nice variety. Click to expand...
<!-- artifact:quote:end -->
I have to ask if the Late era is 1000-1200, why the Palaiologian era Crown/Stemma? I see you guys used Timothy Dawsons book so you must know it’s inaccurate for that period? That same book also says the Circular Stemmas were not used in 1066 so I just have to wonder what the thought process was there? Is it to represent the Palaiologians due to their lack of an era? I can understand that with the hope they are separated whenever you guys get to a proper late era. Also a question in general to any dev since heraldry in general is being updated, will House Komnēnós no longer have those made Up Bells? I understand not wanting the Single and Double headed spam but those eagles specifically the Single headed Eagle are the symbols associated with the dynasty. The first hard proof we have of an imperial family period using a symbol is the Komnenoi patronizing buildings such as the Theotokos Kosmosoteria Bulit by Sebastokrator Isaac Komnenos in 1152 with Single headed eagles. Now undoubtedly this symbol did not have heraldry related origins during its use by the Komnenoi proper and was just the traditional imperial Sigil but it was adopted as such by the Grand Komnenoi and appears on their patronized buildings and imperial regalia in the 1200s whereas we see the Laskarids in Nicaea utilized the Fleur-de-lis in the same period. This is just a suggestion though of course if the Komnenian coat of arms was even thought about. And my continuous Grievances with the Stemma aside this is undoubtedly the biggest glow up and best depiction of Byzantium in any video game, period, to date, so major props to the whole team.

## Reply 84 — participant_071 · 2024-08-27 · post-29849574

Excellent Dev Diary, as usual. The new Byzantine clothing is amazing. Could we get a look at the culture map of the Byzantine Empire?

## Reply 85 — participant_072 · 2024-08-27 · post-29849605

<!-- artifact:quote:start -->
> tundragrass said: Did I miss it or has the map graphic for Constantinople not been shown off? I think there was one screenshot a few DD's ago that had it obscured by an emblem. Click to expand...
<!-- artifact:quote:end -->
You can see it in feature breakdown video

## Reply 86 — participant_073 · 2024-08-27 · post-29849621

No San Vitale special Building in Ravenna? Would be pretty fitting in my opinion. The Rest looks awesome, as always!

## Reply 87 — participant_074 · 2024-08-27 · post-29849645

The art is really beautiful for this, I don't envy having to choose between those 8 different loading screen ideas, the Hagia Sofia coronation was def in my top 3 and I think just about everyone will be happy with that decision. I also really liked 1 (the emperor on the ship) and 6 the religious debate too. The Estate and Camp art is just so pretty too though, definitely some of my favourite from CK3 too, and as someone who plays on a weak laptop that lags everytime I enter the royal court I'm definitely glad that the UI for this will be easy to access and look good. I can't wait to see what some of my favourite total conversion mods do with art for these. Lastly I'm not sure if you can answer this but I'm curious if there were any new religion icons made for this (either updated icons for old religions or new icons for new religions).

## Reply 88 — participant_075 · 2024-08-27 · post-29849698

I did see Shields for Landless how many shield types are there? Like Norse, Greek and etc.

## Reply 89 — participant_076 · 2024-08-27 · post-29849699

I assume with some references in this dev post and some of the previous ones we shall see more events following the Norman conquest of England such Hereward the Wake and Harrying of the North? The artwork and events look absolutely beautiful, looking forward to the DLC and the update. I am very much going to enjoy more coat of arms options in the game also having the music controller.

## Reply 90 — participant_032 · 2024-08-27 · post-29849703

<!-- artifact:quote:start -->
> Ugolinos said: View attachment 1180084Reading this DD while visiting Istanbul and sitting in front of the Hagia Sophie is 10/10 Click to expand...
<!-- artifact:quote:end -->
Awesome! I'm visiting Istanbul for the first time in November this year, so it's going to a fun exploration after playing this expansion.

## Reply 91 — participant_077 · 2024-08-27 · post-29849714

hope you gonna fix headgear_armor bugs that are here since T&T : The greathelm with torse and mantle has the wrong culture trigger the coat of arms crest is not even coded in the headgear_armor trigger script (and so never display) all EP2_western_war headgears armor use the wrong clothing era trigger, which leads to dates where none of era 2 and 3 helms trigger The iberian and germanic modifier factor 0 use an OR trigger while it should use an AND etc etc....

## Reply 92 — participant_078 · 2024-08-27 · post-29849720

I do rarely post here anymore but this does indeed look magnificent. Cant wait to try out the new update once it hits live.

## Reply 93 — participant_079 · 2024-08-27 · post-29849738

WOAW Really Thank you for all this great job !

## Reply 94 — participant_080 · 2024-08-27 · post-29849747

Did new army model for the Greeks as well? This art looks fabulous!

## Reply 95 — participant_081 · 2024-08-27 · post-29849767

HOLY SHIT FINALLY WE GOT MUSIC PLAYER

## Reply 96 — participant_082 · 2024-08-27 · post-29849768

Will you revisit the Legacy of Persia and Northern Lords with more map rooms? The special Byzantine one is just so beautiful. I wish there one in Iranian fashion as well.

## Reply 97 — participant_081 · 2024-08-27 · post-29849781

I love the new music player. Can we go back to the previous track, like in EU4 and Hoi4?Can it be added?

## Reply 98 — participant_083 · 2024-08-27 · post-29849784

Amazing work!

## Reply 99 — participant_084 · 2024-08-27 · post-29849803

Can you add the names of the characters and their titles/positions in event screens? For example in the Crimes of Passion event pop up at the end of the OP, the two women are unknown at face value unless you put your mouse over them. There is a mod for this called nameplates but it would be essential to add to the base game as a general QoL improvement.

## Reply 100 — participant_085 · 2024-08-27 · post-29849811

Please allow us to disable the map tables as a toggleable option.

## Reply 101 — participant_086 · 2024-08-27 · post-29849874

Mind. Blown. Thank you dev team for your wonderful work and the music player!

## Reply 102 — participant_087 · 2024-08-27 · post-29849929

those assets are fantastic but also inaccurate as shown here ( https://twitter.com/x/status/1828286804560056378 ) would it be possible to have more accurate clothing?

## Reply 103 — participant_088 · 2024-08-27 · post-29849968

Speaking of clothing, and I know I'm being a broken record... will Jewish characters *not* wear Byzantine Clothing with this update? because currently Ashkenazim all wear byzantine clothes and it's just a wholly inaccurate and frankly baffling design choice.

## Reply 104 — participant_089 · 2024-08-27 · post-29850061

Can landless travelers place bets at the track and experience Byzantine inspired events? I just hope that all regions don't feel sameish for travelers, otherwise what is there other than just finding more contracts and all feeling the same anywhere on the map?

## Reply 105 — participant_090 · 2024-08-27 · post-29850064

<!-- artifact:quote:start -->
> PDX-Trinexx said: This post is reserved by the Community Team for collecting developer responses within the thread. There are female versions of those two armors, but they do look the same as the male ones (adjusted to fit the female proportions). I'll answer the ones I know the answer to 2.) This is based on character age and current year (young people will be earlier adopters of the new style) which gives a gradual transition over 50 ish years. A proper mechanic would be cool but would require so many assets! 3.) It was implemented for Western Europe with Tours and Tournaments, and the ambition is to keep adding it for more cultures, including Norse (like you suggest perhaps by having them switch to Western Europe styles at some point). 4.) Currently, no. The focus for clothing was very much to flesh out the Byzantine culture. The early era is based on the time period from before game start (around 650) to around 1000 AD (so in game terms it is just the "tribal" era). The "late" era is primarily based on sources from 1000 to around 1200 (so early and high medieval). I would love to add a separate Palaiologan set for the late Medieval era Byzantium, as well as a full European one of course. Who knows what might happen in the future! We added one new armor per era, but there are already a number of Byzantine armors in the game, so we do get a pretty nice variety. Click to expand...
<!-- artifact:quote:end -->
3: When it comes to this stuff, the aesthetic part. would it be possible for you guys to include more options & roleplay for what our culture's aesthetic would be? the norse adopting a much more western european style (including hair etc) would make sense if they adopt christianity, but in this game theres a ton of alt history & what about hairstyles and such? it makes sense that cultures adapt & integrate somewhat, especially if the weather require it for such thing as clothing but what about hairstyles & beards etc? i made a suggestion a while back https://forum.paradoxplaza.com/foru...beard-cloak-headwear-like-barbershop.1519081/ for this, basically just seperate the aesthetic pillar into a few more choices such as hairstyles,beard & clothing(headgear seperate). So that our aesthetic from our unique hybrid & divergent cultures actually feel unique. what if the Asatru reforms & stay? should they lose their cultural heritage and stop having the hairstyles of their forefathers? What if the Rus/russians merge with steppe culture? What about Norman africa, perhaps the people there would keep norman aesthetics(clothes & hairdo) but wear turbans/scarves due to the climate/weather?

## Reply 106 — participant_091 · 2024-08-27 · post-29850113

<!-- artifact:quote:start -->
> Estate buildings have different visuals according to culture. For now, we have Western, Byzantine and MENA themes. Camp buildings are the same regardless of culture, except for the main tent, which has western, steppe, tribal and mena themes. Click to expand...
<!-- artifact:quote:end -->
Thanks for this nice looking DD My question is : Are we limited to those 3 estate / 4 camp variation themes, or it might change in the future both via update, or cosmetic DLC release? Also are those themes are moddable , so skilled members of our society can add missing ones from other cultures present in the game ( indian, and viking comes as obvious example ? Can we also ask for adding more emblems/patterns for western/central european coats of arms

## Reply 107 — participant_092 · 2024-08-27 · post-29850118

<!-- artifact:quote:start -->
> Blodhevn said: i made a suggestion a while back https://forum.paradoxplaza.com/foru...beard-cloak-headwear-like-barbershop.1519081/ for this, basically just seperate the aesthetic pillar into a few more choices such as hairstyles,beard & clothing(headgear seperate). So that our aesthetic from our unique hybrid & divergent cultures actually feel unique. what if the Asatru reforms & stay? should they lose their cultural heritage and stop having the hairstyles of their forefathers? What if the Rus/russians merge with steppe culture? What about Norman africa, perhaps the people there would keep norman aesthetics(clothes & hairdo) but wear turbans/scarves due to the climate/weather? Click to expand...
<!-- artifact:quote:end -->
I hear what you're saying, but the head wear hybridization par excellence happened outside the game's timeline!

## Reply 108 — participant_093 · 2024-08-28 · post-29850202

<!-- artifact:quote:start -->
> ZANE1066 said: those assets are fantastic but also inaccurate as shown here ( https://twitter.com/x/status/1828286804560056378 ) would it be possible to have more accurate clothing? Click to expand...
<!-- artifact:quote:end -->
Ah I see someone found my twitter thread. So yeah I was at Lowe's at 12 AM in the middle of night shift because I'm a grad student trying to pay rent, but I'm at home on my PC now so I can give a proper response (especially since I can actually see the references posted). My primary interest is in arms and armor (I just finished my MA in it and will receive it by the end of the week, and have one paper stuck in editing/peer review hell right now and like 10 more on textiles and armor and mosaics I'm about to submit as soon as I can find time), but I know a very wide range of Byzantine Material Culture because my interest is in reconstruction, specifically, so I have to delve into everything from house and city plans to forks and spoons to helmets to musical notation. But clothing and armor is the easiest to tackle here because it's the stuff I have memorized. So first thing's first: Byzantine Art is a MESS. Artists were trained and followed very specific traditions, and that included maintaining extreme conservatism in how they practiced art, or depicted certain things. These are a form of topos like we find in literature (e.g. Priscus using the format of Herodotus and Thucidydes to write his history). Sometimes this can get extreme: certain icons or illuminations of early church fathers (particularly authors, usually shown as scribes) are always depicted in 1st century Roman tunics, for example, despite the depiction being from the 14th century, or even the modern day. Let's start with the sources: Spoiler: Dev Post Sources Image So what we see here is probably only part of what's been consulted, but also kind of a critical failure to understand what they're looking at and its context. I see some material which is really good, which I can actually name because I know the people who did it. Dr. Timothy Dawson's By the Emperor's Hand is here, which is a really good book that you need to read to understand Byzantine court dress (Alongside Dr. Jennifer Ball's Byzantine Dress: Representations of Secular Dress and Dr. Faith Morgan's Dress and Personal Appearance in Late Antiquity). The reenactors (And vendors, I see quite a bit of MedievalDesign) you posted are all personal friends of mine, hell I'm surprised there's not a picture of me in there actually. But what you have is a collection of artefacts and art that spans from the 4th to the 15th century, what looks like one post-Byzantine liturgical garment (not a bad source, you just have to know how to use it). The reality is that a lot of the archaeology contradicts what we see in art, as Byzantine art is extremely stylized even in its best period (867-~1190), and gets worse after that (at least for representation of contemporary dress and military equipment). And on top of that, archaeologically most objects only are in use for about 25 to 75 years, depending, which I'll show more clearly below. But fashion trends change rapidly and we can see this in the primary source material that actually explains specifically what each court officer or bureaucrat was required to wear. We have very clear primary sources on this and there's already a difference between the late 9th century (the game's start) and the mid-10th century, when the Kletorologion and the De Ceremoniis were written. Spoiler: Tunicae Manicatae from the Dev Post Let's start with the Tunics, pictured here. So first thing's first: these were all found at sites such as Antinoupolis and Panopolis and mostly date from about 280 to 640 CE, in fact most of these have been Carbon-14 dated now by the University of Bonn so we have really precise ranges for some of these, which allows us to track the evolution of certain patterns and motifs. The motifs you've used here are called Dionysian (they often depict Bacchanalia, Dionysus, and his minions) and do in fact extend into the early Islamic period, we have some 7th-8th century examples. But they also die out in the Early Islamic period. However, there's a failure to understand the context of these tunics which has impacted the art, from the tunic in the bottom left of the first image and in the concept art from the third image (figure on the far left). This tunic is from the Metropolitan Museum of art and if you look closely at the neck here, you can see this tunic is a chopjob. This is a really common problem with these tunics, which were all found back in the good ol' days of grinding up mummies and eating them (i.e., these were mostly found and sold at auction between the 1880s-1920s). The problem is, tunics usually aren't in that great of shape when they're uncovered, let alone going through multiple looters' hands (this was in the very earliest days of archaeology becoming a thing) to an auction house in Memphis or Thebes or Cairo. Pieces of tunics were also harder to sell and didn't fetch as much money. So what did they do? They cut out the nice bits of tunics and burial shrouds and pillows and curtains and amalgamed together into "complete" pieces, which is what we see here, and why this one's neckline is so abnormal compared to the rest of the surviving tunics (although it probably does come from a tunic, just a later, different one). The same can be said for its lower hem and the cuffs. Notice how the style of decoration doesn't match? These were really nice pieces of probably a curtain or shroud that were put on the tunic to sell it for more. So this isn't a good example because it defies the methods in which these tunics are manufactured (as one giant cross-shaped piece on a 2+ meter warp-weighted loom which is then folded in half, each one requiring two people working non-stop for about a year and a half to make from the sheep to the finished product - such as the replica of the Lendbreen Tunic made for "Secrets of the Ice"). Spoiler: Met Museum Accession Number 12.185.3 Notice too that we never see large rondel silks being used for these forms of tunic: these, by the 6th century, are already being codified in the De Magistratibus of John Lydos. What this is called is a Paragaudes or Paragaudion, and the segmentae and orbiculi cannot clash with the use of large rondels on the ground that they are woven (not embroidered) into. This is important because the early codification of dress is already stating office-specific garments such as Stikharia being worn by members of the senate, while men with military office wore the Khlamys. And this is under Justinian, before the hyper-specificity of the Kletorologion or De Ceremoniis (or the 14th century author Pseudo-Kodinos). Spoiler: Behold my Microsoft Paint Skills We see very few of these with decorated grounds, the only real example I know of is the Diptych from Monza Cathedral either of Stilicho or Aetius (so either 398 or 432 CE). And that uses very small portraits characteristic of late Roman silks, before newer Central Asian patterns spread west. Rondel silks with facing beasts really only start coming in during the 6th century and mostly come in during the 8th. This is before the game's time period, but it's a big reason why we don't see them on Tunicae Manicatae. Spoiler: 3D Models from Dev Post So what's wrong with Era One here? Well he's using a 9th century silk (I'm not sure which, I see the Alfred and Bonno Museum one in your sources but it's not that one) with a Dionysian motif on the Clavi and in the Segmentae which would date to the 4th-6th centuries. He also uses a 7th century buckle (looks like maybe an E25 or an E26), with a 10th century (Magyar, so out of its cultural context) belt pouch (we never see belt-suspended pouches, only ever shoulder-suspended, at least this late). The shoes are based on 6th century Consular Diptychs and don't reflect contemporary examples from the game's start date of 867. The torc is 6th-7th century which I'll honestly give that a pass just because we don't have any (at least not any made of more than just bronze wire) from the middle Byzantine period, but torcs indicate really specific ranks (Spatharokandidatos and Protospatharios) so this man would have to be a Protospatharios to wear that torc, because it has garnets and is solid gold. That's a really high station - not even Harald Hardrada received that rank and he was serving in the Varangians in an era where it was being given out like candy by Michael IV and therefore losing its status and value. I can't tell you whether or not the leggings are wrong because I can't see if they're hosen or trousers. This one does get the general cut of the tunic right - the perikheiridai (stripes on the cuffs) should be set back from the edge of the sleeve mostly (the weave will fray if it's actually up against the rim of the cuff, which uses a tablet weave to selvedge it), but they are properly tight fitting and the pattern is largely correct. Spoiler: Byzantinische Gurtelschnallen und Gurtelbeschlage im RGZM Mainz I have to go to work in like 30-40 minutes so I have to unfortunately cut this post off here, but I will be back to respond to and expound on the rest of the dev post tomorrow night.

## Reply 109 — participant_094 · 2024-08-28 · post-29850253

Is there any struggle mechanic for the post fourth crusade successor and crusader states

## Reply 110 — participant_038 · 2024-08-28 · post-29850286

<!-- artifact:quote:start -->
> firespark 84 said: Is there any struggle mechanic for the post fourth crusade successor and crusader states Click to expand...
<!-- artifact:quote:end -->
No. We would know about it because it would be the flagship mechanic of the expansion.

## Reply 111 — participant_095 · 2024-08-28 · post-29850293

<!-- artifact:quote:start -->
> PDX-Trinexx said: -SNIP- Click to expand...
<!-- artifact:quote:end -->
Hats of to the whole CK3 team, you have outdone yourselves for this DLC/Update. Now since you're also looking and listening to the community i would like to ask you for one very small thing that has annyoed a lot of RP players and that's the "hidden dynasty prefixes problem". Basicly if you rename your dynasty then you lose the hidden prefix of "von" or "of" and you have to put it in your name. and then you're the only house in the world with the "Von Habsburg" instead of "Habsburg". It has been often posten in the suggestion tab and the solution "looked" simple. As the user "drefurion" suggested: "I would like to suggest the option, possibly with some sign like <de >, <of >, <d’> to be able to create these hidden prefix dynasty names in the dynasty edit interface." I know this isn't the suggestion tab but i just couldn't resists posting since i noticed you listened to the community a lot this time. Thank you in advance and just like everyone else, i'm looking forward for the update/DLC.

## Reply 112 — participant_089 · 2024-08-28 · post-29850396

<!-- artifact:quote:start -->
> firespark 84 said: Is there any struggle mechanic for the post fourth crusade successor and crusader states Click to expand...
<!-- artifact:quote:end -->
I'd kinda like to see more of a struggle mechanic with holy wars with player founded holy orders that could just be a traveler that can own land (If they can make that work somehow). You're not a king so other kings won't see you as their equal. But as the head of a holy order you can travel around and help anyone of the same faith in wars or conversions to the right religion (in peace or by force). As your order gains more influence other kings of the same faith might start to not like you so much and want you gone. It would be like a hybrid landed traveler, and you get manpower, supply and gold by gaining influence, the more land you have and the bigger the wars you win the more influence you get. But instead of gaining manpower per month, you get nobles will flock to your banner bringing their units with them. But maybe theres only so many spots for nobels so you can only keep a few of the most powerful ones. Nobles in your order after years of faithful service will want to be given land of their own. After all why conquer the heathens land if they won't be given to the good faithful of God. Maybe even have a contract system where you promise a plot of land for service. Like pay 1000g as a downpayment for a noble that has 10k troops and promise them Arabia for 10 years of service. If you succeed with in those 10 years you get back the 1000g they get their land, If you fail they keep the gold and you lose a lot of street cred. You can't fight against anyone of the same faith, but they can against you. If you can't fight other kings of the same faith how can you control them? They likely won't join in your wars if you're too powerful and might even try to take that power from you, but you can keep them under your thumb with the Fear of God. On the death of the Head Master the Holy Order will be passed to the next in command. But he will have to build his own reputation, gaining his own influence and if you haven't been good to the nobles under your command they will break off from the order grabbing what land they can. I don't know if any of this could work, but I just like throwing ideas out there.

## Reply 113 — participant_096 · 2024-08-28 · post-29850543

Do those horses have 5 legs?

## Reply 114 — participant_097 · 2024-08-28 · post-29850577

<!-- artifact:quote:start -->
> lucas.ribeiro.rodrigues said: Estate buildings have different visuals according to culture. For now, we have Western, Byzantine and MENA themes. (…) Besides variation of buildings by culture, we also wanted to reinforce the sense of place in the world of the domiciles by creating different backgrounds that change according to the position of the estate or the camp. Estate Background can be: Dry, Green, Jungle, Rough and Urban. While Camp Backgrounds can be: Dry, Green, Jungle, Rough, Snow and Snowy Mountains. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> SMiki Lorebringer said: Do the buildings available depend on the climate of the barony where the Estate is located and the religion of the holder? For example, let's say I form Scandinavia empire (with a climate famously unsuitable for vine cultivation) and make it administrative – do I get something more flavourful to build rather than a vineyard? Or, let's say I'm a Muslim Estate owner whose religion forbids drinking – I imagine something like a cannabis plantation for shisha could be used to replace the vineyard? If the buildings don't depend on the above and we get vineyards for everyone, is it moddable so that we can change that ourselves? And could you consider making regional and cultural/religious variations of the buildings later on if they don't exist in the release version? Click to expand...
<!-- artifact:quote:end -->
This potentially answers my question from the other thread: Given the visual styles listed, there won't be a Northern estate visual set for now, so no need for the vineyard replacement in areas where vine doesn't grow at this moment. How about devout Muslims and other abstinents however? Do they still have vineyards (perhaps with some maluses), a replacement building (cannabis plantation?) or simply are not able to build it or use it if they inherit it already built?

## Reply 115 — participant_093 · 2024-08-28 · post-29850789

So following up on my previous post, we're going to start off with figure 2 (second from the left) in Era 1: Spoiler: 3D Models from Dev Post So immediately we have several problems. We'll ignore the Pteryges and the debate over whether they existed for now, but at least they're linen (as stated in the Suda and De Ceremoniis). Let's start with the clothing and then move on to the armor. First of all, the shoes are based on a pair made by Timothy Dawson actually for one of his much later impressions. The word hypodemata is used in the primary sources for boots (specifically the Taktika of Leo VI, the Sylloge Taktikon of Romanos II, the Praecepta Militaria of Nikeforos Fokas, and the Taktika of Nikeforos Ouranos), but these texts are partially copying off of the older mid-7th century De Militari Scientia, which basically chopped up and rearranged the Strategikon of the early 7th century. Boots certainly existed and were in use (we have a nice 9th century pair from Panopolis and of course many forms from Moshchevaya Balka and other sites in the Caucasus/Transcaucasus/Dagestan), but the problem is we don't see infantry wearing boots in any Byzantine art until the 12th century. Instead we see low shoes like Figure 1 on the far left is attempting, but his shoes suffer from having a strap arrangement (and a bad interpretation of the strap arrangement at that). In fact we have multiple pairs of such low Tzanggia or Mouzakia (also called Kampagia or even Sandalia) shoes, mostly from the various tombs of Amorion (I have images of the unpublished ones as well, which I'm not supposed to share because it's Dr. Linscheid's intellectual property). There's also a pair from Cherson (also unpublished). All of these shoes lack strapping arrangements and closely match the low, black-colored "slippers" seen in the artwork. They're clearly derived from various 4th to 8th century "Coptic" patterns such as those in the Byzantine Museum at Athens. The most famous of these finds are the so-called "sad shoes" from Amorion (below), but the type is unisex - both the man, woman, and teenage daughter in tomb 103 at Amorion were found wearing the same shoe pattern. Spoiler: Amorion Grave 103 Shoes Of course, a high ranking officer would wear boots since they were probably fighting mounted. However, fold-over boots, barring the Republican and Principate-era Roman Perones of Senators and Emperors, would not be fold-over boots. Instead, they were usually decorated with leather tooling or even silk, like on the mentioned examples from Panopolis and Moshchevaya Balka. Some of the taller, knee-height boots even had laces to tie them to the braies or a belt like hosen. Spoiler: Panopolis Boots The next major problem is his tunic. First thing's first: there's just no evidence for 3/4 sleeves like that. Short sleeves are rare archaeologically (usually found on Children's Tunics like the Al-Lahun tunic or several Coptic tunics) and all Tunicae Manicatae had tight fitting cuffs, with buttoned cuffs (persikomanikia) coming in under Anastasius (but not found on most tunics of this type). By the late 6th century these were already considered old-fashioned with the adoption of shaped sleeves and waisted cuts from Sasanian fashion, although traditional Coptic tunics hang around very, very late, only phasing out completely in the 1000s, definitely before 1100. We have several late examples, the most famous of which is from the Katoen Natie collection which is 9th-10th century and a Woman's dress. But military tunics already were following modernized patterns with gores and gussets in the sides and the armpits, like west European fashion. A few 9th-10th century tunics like this are known from the Victoria and Albert Museum, all found in Egypt, and would be the norm for most Romans. Spoiler: Child's Tunic from the Victoria and Albert Museum, Probably 8th-12th Centuries Military tunics also are always in four colors when in armor: red, green, or blue, and certain units do have evidence for wearing white like the Schola Palatina or the Tagmata. While there isn't direct codification of this practice, there is a substantial amount of indirect evidence for this which is being published in the upcoming Limitanei volume by Dr. Robert Collins in a paper authored by Dr. Boris Alexander Burandt (when it will be published, I do not know; this is the same volume my paper is stuck in Peer Review & Editing hell with right now). Later Coptic tunics do start to see a break in the traditional dichotomous forms of late antiquity, which really begins with the change in shape and decoration of the neck in the late 5th century when buttoned necks are introduced, to more complex forms that emerge in the 8th-9th centuries, followed by a contraction to a very simple form in the 11th century that gradually transitions into the 13th century post-Coptic tunic patterns. This doesn't make sense without context, of course, and a few very nice patterns I can show below. Primarily, traditional floral and Dionysian motifs fade out in the 7th-8th centuries in exchange for much simpler patterns. When complex decoration appears, it's often in the form of biblical scense such as on the Katoen Natie Tunic. Spoiler: Incomplete woman's dress from the Katoen Natie Collection, 854-970 CE View attachment 1724841343423.jpeg Other tunics typically have heart, spade, or oversimplified floral motifs, such as these tunics from Katoen Natie and the Louvre. This first starts popping up in the 6th century, and some even have these patterns as a ground: Spoiler: Incomplete tunic from the Katoen Natie Collection, 761-989 CE Spoiler: Tunic from the Caucasus in the Katoen Natie Collection, Late 8th-Early 9th Centuries Spoiler: Various Tunics from the Louvre The example from the Caucasus in Katoen Natie above, as well as the last example from the Louvre above, represent the much more modern and typical patterns of decoration from the 9th-10th centuries. We can see these in a variety of the art pieces you posted above (particularly the Menologion, but also many others). Critically we can also see them in provincial art from Cappadocia, which as Dr. Jennifer Ball shows in her book, tells us a great deal about how quickly new fashions reached Constantinople, and how quickly it was adopted. Another thing we see in the Menologion is that hosen and trousers are always tight fitting. You'll always have a little bit of bagginess and folds at the joints (knee and ankle), but the bagginess of the trousers seen on figure 2 is more typical of poorly fitting reenactors' clothing than the actual historical reality. Then we get into the armor: There's a couple big issues with this here. The first is the helmet, which is an amalgam of a Baldenheim-type Spangenhelm (c. 500 to 640 CE, so well before this game's timeframe) and two helmets from the Caucasus housed in the RGZM which are actually amalgams (published in a paper by Dr. Christian Miks from 2009). In other words, the helmet is a historically inspired fantasy more suited for Mount and Blade: Bannerlord than Crusader Kings III. Of course, we also have the problem that there are no Byzantine Helmets datable to the period between about 640 and 1180 CE (with one possible exception that needs testing to prove it's not a fake). However, there are options from around the empire - Hungary, the Pontic (Ukraine, Krasnodar Krai, etc.), and the Caucasus. The helmet from Bezhta is the only type which might be evidenced in Byzantine art, but it also fades out of use right before this game's start in 867. The Prague/Stromovka/Gnezdovo family of "Ridge Helmets" however are almost certainly evolved from Late Roman forms, as evidenced by an intermediary seen in a fresco from Santa Maria Antiqua dated to its fourth phase of paintings from about 749-752 CE. We don't directly see these in Byzantine art, but the late 9th century Sacra Parallela may show something like them. They are very widespread, being found ranging from Prague to Mecklenberg-Vorpommern on the Baltic to Gnezdovo in Russia, and do have a few decorated variants (although we only have fragments of decorated ones, no complete examples). So while they are probably being manufactured in Prague, they're a fairly good choice for pretty much all of Europe in this period. Spoiler: Helmet from Bojna, late 9th to mid-10th century CE A more decorative example would be the helmet from Pecs, which belongs to the "Black Mound" family. Spoiler: Helmet from Pecs, Hungary, mid-late 9th century. The scale armor is another matter. We have scale armors from this period from Veliki Preslav, Pernik, and Pliska, so the choice to use the fantasy "Dragonscale" shape is weird. The armor itself is based off of Benjamen Franckaert's interpretation of the shape of late Roman scale armor, which is... one choice, albeit not the one I'd make. The "Varangian Bra" is a whole debate on its own (it probably was for some specific rank or office, but we don't know which - the strongest theory is that it was an evolution of the Centurion's harness for carrying awards in the Principate). Spoiler: Scale Armor from Pliska The sword is the sword from the Serce Limani shipwreck, which is probably a better choice for Era 2 (I'll discuss it in the next post). The best choice for Era 1 would really be the sword from Garabonc or Cherkassy, shown in the Homilies of Gregory of Nazianus and the Menologion of Basil II, and assuredly in use from its introduction from the Islamic World in about 750-800 until at least 1000 CE, before morphing into the Serce Limani Type which dates from 1030-1060 CE. Spoiler: Distribution of Garabonc-Type Swords, 9th-10th Centuries Spoiler: Judgement of Solomon, Homilies of Gregory of Nazianus (BNF Grec. 591), 878-883 CE I need to sleep, so I'll pick up with Figure 3 (the best one of these, really just needs the belt pouch and "seax" removed and the shoes fixed) and Figure 4 (literally complete fantasy worthy of Raffaele D'Amato's publications) later. BTW someone clarify for me exactly when the middle graphical era starts and ends? I think it's 1100 and 1300 but I'm not 100% sure.

## Reply 116 — participant_098 · 2024-08-28 · post-29850793

Will the new CoA figures be dlc exclusive? It would be great to put St. George on some historical CoAs.

## Reply 117 — participant_099 · 2024-08-28 · post-29851465

I love the art style choice for the estates. It reminds me of the village view Kingdom Come: Deliverance's "From the Ashes" DLC, and I loved that.

## Reply 118 — participant_093 · 2024-08-29 · post-29852126

Okay so picking back up again, we move on to figure 3 (left guy in Era 2), which is honestly the best of the male models here (the women are actually really good barring some minor errors which I'll discuss later). Basically the big problem with figure 3 is his sleeves are over-long, and should have decorated cuffs. By the Komnenian period (I'm assuming Era 2 is Komnenian based on the 1178 start date) Persikomanikia and Epimanikia (buttoned cuffs) had become unfashionable, although they were still in use by the devalued, older court ranks until the end of the reign of Manuel I. Instead we have a return to the tight-fitting sleeves of late Roman fashion, which this captures, but they should be much better fitted (ending at the wrist, and again with decorated cuffs). The presence of a "seax" also makes no sense here. We have plenty of evidence for kitchen/utility/hunting knives, sure, but these weren't worn as some sort of accessory by the court. It was the kind of thing you might tie to a belt out in the field if you were a civilian or a soldier, but wasn't an element of fashion and definitely wasn't a military sidearm (that's what the sword was). Again, the Belt Pouch isn't representative of Byzantine dress either, these Magyar (or Bulgar) belt pouches come from a different cultural context. We do see bags in Byzantine art, but they are leather slung satchels (as in the Roman tradition, e.g. the old bag of the Commaccio II shipwreck from the 2nd century CE) or reliquary bags (like the silk bags from the Collegiate Church of Beromunster in Switzerland, which are Byzantine exports from the 9th century). And of course, as I said before, the shoes need to be changed. Spoiler: 3D Models from Dev Post Figure 4 is where things get... out of hand. It's an awfully 14th century piece for an 1178 start, although I can name what everything here is from. Let's break it down: We'll start at the head, with the helmet clearly taken from the 13th century phase of the mosaics of Basilica di San Marco in Venice. There are still questions about where and when the Kettle Helmet was invented: a lot of Byzantine manuscripts (and a few enamel depictions) are cited as evidence for its origin, but I'm not convinced. A flared brim is known on some early helmets, like the late 6th to mid-7th century helmet from Groningen, or the late 7th to mid-8th century helmet from Yarm. We do also see "brims" in art throughout Classical and Late Antiquity - there are "brims" on the Intercisa-type and Iatrus-Krivina-type helmets in the Basilica di Santa Maria Maggiore (whose mosaic cycle is from ~431 CE). Classicizing art (which includes Santa Maria Maggiore, which shows Hellenistic Tube-and-Yoke armors and Phrygian helmets) seems to attach this feature to harken back to Hellenistic helmets with Brims, which mostly died out around the 1st Century BCE-1st Century CE. I suspect learned Byzantine illuminators and mosaicists may have somewhat been keeping that tradition alive. Of course, a few of said illuminations are actually 13th-14th century illuminations in an 11th century manuscript, a fact which was missed by certain scholars (like D'Amato... but also more reputable ones). Kettle helmets come in archaeologically right after the Komnenian period, in fact our earliest datable find is Byzantine. It's from the Saranda Kolones fortress in Paphos, destroyed by Crusaders in 1222, where a nearly completely intact Kettle helmet was found (see below). Spoiler: Helmet from Saranda Kolones Fortress, 1222 CE A better choice, however, would be the helmet from Branicevo, which belongs to the Pseudo-Phrygian family of helmets. These two helmets were found in a Byzantine House from the destruction layer of 1182 (probably, or possibly 1198). A similar helmet is also known from Pernik. While the original publication labelled them (and Pernik's publication labelled it) Latin, these three helmets are all probably Byzantine manufactured. Why? Because of the features of their construction - the method of attaching the loops for the maille aventail is a Caucasus style, known from at least the the 6th century CE. The Pernik Helmet has a Turban-Type nasal, also a Caucasus or Anatolian feature. Furthermore, these helmets are first evidenced in Byzantine art from Cappadocia, appearing possibly as early as 913-920 but definitely by the 960s, and spreading to South Italy, South France, and North Spain between 990 and 1030 CE. They don't seem to have become dominant until later though, in the late 11th-12th centuries, and they last until the 1220s in West Europe, and possibly as late as the 1260s in Armenia. Spoiler: Helmets from Branicevo, 1182-1198 CE Spoiler: Pernik Helmet, 1183-1186 CE There's nothing to say about the torso armor other than that it's a fantasy. Lamellar and Scale armors are still in use in the 12th century, we have large scales from Kliso which look a lot like the ones seen not only in Byzantine and Seljuq art but also in a few South Italian and German artworks. There's also the lamellar from the Great Palace in Constantinople itself, and of course the earliest find of hidden lacing lamellar is from the Byzantine layer of Ras from 1146 CE in Serbia. This is all to say nothing of maille, which was considered the best armor available. Al-Mutanabbi and Anna Komnene describe how John Tzimiskes and Alexios Komnenos' maille were impenetrable to cavalry lances, and some of the finest maille we have in the world is from Mihailovo in Bulgaria and believed to be of Roman manufacture, dated from the 10th-11th centuries and made of silvered brass in tiny, 3mm and 4mm internal diameter links. Roman maille even has pseudo-pteryges, which makes it stand out from contemporary European mailles, and it's the earliest evidence for the tailoring of maille (except maybe the shirt from Kazazovo or the Saint Vaclav maille). Spoiler: Silvered Maille Armor from Mihailovo, 10th-11th centuries CE Spoiler: Great Palace Lamellar, 12th-13th centuries CE Spoiler: Star Ras Lamellar, 1146 CE The sword also needs to be replaced. The Serce Limani sword you used in Figure 2 would be a better choice, to say nothing of the Byzantine swords from Pernik (from the same date as the helmet) or in the Rousse Regional Museum (same type as Pernik, Oakeshott-Xa with a Byzantine Sleeved crossguard). I know it's based off the Joshua Fresco from Hosios Loukas, but that sword is probably a late form of Galovo-type sword like the one in the Vatevi Collection (published formally by Errikos Maniotis), with slightly exaggerated shape to make room for the decoration. Spoiler: Sword from the Vatevi Collection, Late 11th-12th Centuries Spoiler: Sword with Sleeved Crossguard from Pernik, 1183-1186 CE Of course, the dagger needs to go, we do see daggers come in much later in the 1300s, but they're West European imports, mostly Quillon daggers. The same can be said for the belt, which uses 13th century Latin fittings. While we do have a lack of strap ends, we do have buckles from the 12th century and 13th centuries, including a Silvered Women's buckle from Thessaloniki, and Type-G4 and Type-G5 buckles from various sites ranging from Sicily to the Balkans. Art seems to indicate that the elaborate, Magyar/Bulgar derived studs had fallen out of use in this period anyways. Latin fittings are picked up eventually, but only after the Sack of Constantinople in 1204 and the establishment of a Venetian precious metal-working industry in the Aegean. Spoiler: Middle Byzantine Buckle Typology Spoiler: Silvered Bronze Women's Buckle from Thessaloniki, 13th Century As before, the boots need to be replaced with a different form. The Gamlebyn-DD style is a form directly derived from steppe fashion in use in West Europe and probably in use in Byzantium, as it closely matches what we see on some Ivory and Steatite icons from the 12th century. This form dates from the late 12th to late 13th centuries CE. Spoiler: Replica of the Gamlebyn-DD Boots by Dr. Marquita Volken Spoiler: Icon of Theodore Stratelates with a Taller form of Moshchevaja Balka or Gambelyn-DD boots, 11th Century I have to go run errands but there is a lot more to say about the silk patterns used, the decoration of the cuffs, and more.

## Reply 119 — participant_100 · 2024-08-29 · post-29852351

This look good, but I think the chariot animations are little wonky. They kinda look like they're on one of those coin-operated kiddie rides they have outside of supermarkets and pharmacies.

## Reply 120 — participant_101 · 2024-08-29 · post-29852881

I'm a bit surprised/disappointed that the Greek pagan religions didn't get any artistic representation with this one. At least a Holy Site background and 3D Hellenic temple model. Considering the Restoration of Rome got a special artwork, I was kinda expecting a pagan alternatove history play to also be included somehow

## Reply 121 — participant_102 · 2024-08-29 · post-29852939

<!-- artifact:quote:start -->
> lucas.ribeiro.rodrigues said: The non-descript isometric buildings ended up paling in comparison to the charming illustrations we had come up with. Click to expand...
<!-- artifact:quote:end -->
I dunno, I kinda like the isometric buildings. They really bring out the "cozy late 90s game" vibe.

## Reply 122 — participant_103 · 2024-08-29 · post-29853572

<!-- artifact:quote:start -->
> NilsW said: There are female versions of those two armors, but they do look the same as the male ones (adjusted to fit the female proportions). Click to expand...
<!-- artifact:quote:end -->
Speaking of female proportions, can you add the Reichskrone (official crown of the Holy Roman Empire) as a possible garment for women please? Ingame a woman can form the holy roman empire and they can rule it, and they can equip the crown, but for some reason they cant have Reichskrone visually on the avatar. The option doesn't exist in the barbershop. OT: Art looks stunning and I love the addition of a music player.

## Reply 123 — participant_100 · 2024-08-30 · post-29853999

<!-- artifact:quote:start -->
> Domon0310 said: I'm a bit surprised/disappointed that the Greek pagan religions didn't get any artistic representation with this one. At least a Holy Site background and 3D Hellenic temple model. Considering the Restoration of Rome got a special artwork, I was kinda expecting a pagan alternatove history play to also be included somehow Click to expand...
<!-- artifact:quote:end -->
IMO that's kind of unlikely. One of the devs said that the Hellenic restoration content that they put in in CK II was kind of a mistake and they probably won't do something like that again.

## Reply 124 — participant_104 · 2024-08-30 · post-29854121

<!-- artifact:quote:start -->
> BrotherJonathan said: IMO that's kind of unlikely. One of the devs said that the Hellenic restoration content that they put in in CK II was kind of a mistake and they probably won't do something like that again. Click to expand...
<!-- artifact:quote:end -->
It can also be easily added in by mods. So not necessarily as big of a deal imo.

## Reply 125 — participant_105 · 2024-08-30 · post-29854443

I've got a somewhat nitpicky question about the third picture of the adventurer camp. I think it's called picture-18, it's this one: https://forumcontent.paradoxplaza.com/public/1170408/image-18.jpg It seems to me the mace should logically be upside down. The heavier head should rest on the ground, not against a weaker and more precious wooden dresser. Conversely, it would be more practical to pick the mace up if the handle were upwards, and not awkwardly on the ground. Thoughts? P.S. all this is really beautiful, great work!!

## Reply 126 — participant_103 · 2024-08-30 · post-29854488

<!-- artifact:quote:start -->
> misopogon said: I've got a somewhat nitpicky question about the third picture of the adventurer camp. I think it's called picture-18, it's this one: https://forumcontent.paradoxplaza.com/public/1170408/image-18.jpg It seems to me the mace should logically be upside down. The heavier head should rest on the ground, not against a weaker and more precious wooden dresser. Conversely, it would be more practical to pick the mace up if the handle were upwards, and not awkwardly on the ground. Thoughts? P.S. all this is really beautiful, great work!! Click to expand...
<!-- artifact:quote:end -->
While it can be considered nitpicky, I agree that the position of the mace makes no sense. The much heavier end should be resting against the ground..

## Reply 127 — participant_093 · 2024-08-30 · post-29855744

If you want to get nitpicky, that particular shape is a late 15th century Shestopyor from after the end of this game, alongside 13th century "Gothic" style furniture and a "Viking" era shield... (among many other issues)...

## Reply 128 — participant_106 · 2024-08-31 · post-29857029

As an amateur mosaicist, I find your mosaic designs fascinating and beautiful. I want to try and do one in smalti now.

## Reply 129 — participant_107 · 2024-09-02 · post-29858719

Awesome work — very exciting to see the quality of the artwork! By the way, will "Entry of the Gladiators" be available for when you reinstate the gladiatorial games?

## Reply 130 — participant_108 · 2024-09-06 · post-29868173

The incredible dedication for authenticity is beyond admirable. Even though I won't have time to play this expansion for a while, I will order it immediately when available at full price as you deserve nothing less

