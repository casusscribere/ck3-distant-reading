---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1458798/"
forum_thread_id: 1458798
content_type: reply_thread
parent_dd_file: dd_049_2021-02-23_crusader-kings-3-dev-diary-49-a-cold-emb.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 49
title: "Crusader Kings 3 Dev Diary #49 - A Cold Embrace"
dd_date: 2021-02-23
expansion: Northern Lords
patch: Patch 1.3 (Corvus)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 12
reply_count: 235
participant_count: 141
reply_date_first: 2021-02-23
reply_date_last: 2021-03-02
body_word_count: 12610
inline_image_count: 0
quoted_span_count: 124
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Crusader Kings 3 Dev Diary #49 - A Cold Embrace

*235 replies from 141 participants across 12 pages*

## Reply 1 — participant_001 · 2021-02-23 · post-27315718

Greetings everyone! Don’t stand out there in the cold. Come on in and warm yourself by the fire! Have you made yourself comfortable? Excellent. Before we get to it, first things first. I know that all of you are eagerly awaiting more news regarding upcoming DLC content, but we’re not ready to start talking about those quite yet. Don’t fret, you will not have to wait that long. They say that patience is a virtue, but knowing better, I’ll leave this right here. For the next few weeks and the coming dev diaries we’ll talk a bit about what we have in store for the next major update, 1.3. In usual fashion, you can expect 1.3 to land alongside the upcoming DLC. Without further ado, let’s get to it shall we? Winter is Coming Winter is being introduced to CK3, making the already unforgiving world of the Middle Ages a much harsher place! As winter approaches, the map will gradually get covered in snow, clearly showing the extent of the freezing cold. The system itself is fairly flexible and allows for a great degree of control, as we can set which provinces should experience winter, and which shouldn’t. Winter won’t be limited to just the northernmost parts of the map, so expect snow to appear in places such as the Persian Mountains, or on the heights of the Tibetan plateau. { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" } With the introduction of winter comes new gameplay considerations. It wouldn’t be any point in adding this cool system if it didn’t do anything interesting. Winter comes in three different variants; mild, normal, and harsh. Mild and normal winters will be fairly common throughout central Europe and parts of southern Europe, while harsh winters are rarer but can still occur. If you find yourself lost in the frozen landscape of places such as Sápmi, Mongolia, or Himalaya, expect harsh winters to be the norm and plan accordingly! We wanted to make sure that it’s easy to see what level of winter is present in any given barony at a glance. The amount of snow increases with higher levels. Mild winters should generally be fairly easy to spot, with patches of green still clearly visible. In contrast, harsh winters mostly cover an entire province with snow. Certain areas might even have clouds with steady snowfall appearing for that extra level of detail! Depending on the severity of winter, your armies will start to lose supply over time. Harsh winter means you’ll lose more supply each month, making it a risky business to go above the supply limit for an extended period during the winter season. Harsh winters will also have armies suffer more fatal casualties during battles. Winter will also have an effect on your Men-at-Arms. Most noticeably, cavalry units will perform worse in normal and harsh winters. Heavy cavalry, in particular, will suffer some hefty penalties. I would advise against the use of heavy cavalry if you know you’ll be fighting battles in mountainous terrain during the winter season. On the other hand, some Men-at-Arms will get (sometimes quite significant) bonuses while fighting in winter. One such unit is the Tibetan culture unit, Mountaineers. Accustomed to the cold and the snow in the mountains, they can utilize it to their advantage in the form of a damage bonus whenever they participate in battles when winter is present. The system for setting winter bonuses (or penalties if you will) on Men-at-Arms works just like setting terrain bonuses, making it very friendly for any modders out there. While winter and snow might look and play nice, it wouldn’t be complete without a fitting soundscape. I’ll hand over to our sound designer Gustav to talk a bit about what he did to bring winter to life! A Sound Plan Winter for a Swede is like butter on toast, we love it! (brr… please be spring soon!) There are two areas where we have updated audio on the map. Holdings: Audio gets reflected with real-time updates to holdings. When winter spreads over your lands; or any lands for that matter, folks now go inside their homes, birds have migrated to more southern regions, and the animals are now in their stables or inside by the hearths, cozy! The way we achieve this is to link the shader that covers the region with snow and Ice to a real-time float parameter, that then talks to our Audio Middleware Engine Fmod. Awesome, but what does it actually do? It attenuates sound layers, controls effects such as equalizers and reverb, and reshapes the original sound that was there during summertime, and morphs it into wintertime. VFX: We also have snow storms appearing, for both mild and harsh winters. If you hear the sounds, be wary, your troops will most likely suffer some penalties in these areas. Tread carefully! The snowstorms are spawned on the map with the particle system, which allows us to be able to spatialize the sound effects ( position them in a 3D location X-Y-Z ) as the mild snowstorm morphs into the harsh storm, so do the sound effects. I’ll leave you with this; a snippet of what goes on under the hood inside Fmod during winter. Obligatory Map Update Anyone who has followed the history of CK2 or the DDs for CK3 will know that I do enjoy my maps, and I’ll try to get in smaller map updates or improvements whenever I can. Since release, we’ve identified a few general areas that we think can be improved upon. Some of these will be updated in 1.3. First up, Ireland. The baronies in Ireland were a bit too large, making the emerald island have a significantly less holding density than its neighbors, England and Scotland. The western half of Ireland in particular suffered from a few quite large baronies. To solve this issue, we’ve added a number of new baronies, along with a couple of new counties, that should improve the overall experience of playing in Ireland. While Italy hasn't suffered from larger baronies in the same vein as Ireland, the area didn’t quite feel up to par with many other regions within Europe. Especially in terms of overall holding count. Italy generally had a bit too few holdings per county, so we’ve added new baronies in various places throughout the peninsula, from the slopes of the Alps all the way down to Reggio Calabria. The southern half in particular got some much needed attention. In the new setup, you’ll find significantly less counties with only two baronies. To mention a few examples, you’ll find that the county of Veneto has Malamacco as a new barony, Agnone can be found in the county of Lanciano, and Lecce is now an actual holding in the county with the same name. Overall, this should make Italy more representative of its historical impact and more fun to play in. That’ll be it for today! I do have a few more map improvements in store for you, but those will have to wait. Until next time!

## Reply 2 — participant_002 · 2021-02-23 · post-27315727

That's so nice to see. Thank you for bringing back some variation to the map! Maybe this will halt the expansion into Sapmi by the Scandinavian kings. Finger's crossed.

## Reply 3 — participant_003 · 2021-02-23 · post-27315737

"Now is the winter of our discontent Made glorious summer by this sun of York". This looks awesome!

## Reply 4 — participant_004 · 2021-02-23 · post-27315738

DEAR GOD, THIS IS EXCITING! Looking forward to the DLC soon. Extremely happy that this is free content and not even part of the upcoming expansions. Makes the entire wait more than worth it!

## Reply 5 — participant_005 · 2021-02-23 · post-27315742

I knew winter would come! Excellent!

## Reply 6 — participant_001 · 2021-02-23 · post-27315749

Videos doesn't appear to work properly. We'll get those sorted in a moment!

## Reply 7 — participant_006 · 2021-02-23 · post-27315752

New Irish provinces? Who'd have guessed?

## Reply 8 — participant_007 · 2021-02-23 · post-27315757

Its nice, but I find such temporary attrition effects to be rather minor in games like CK2 or EU4. They only last a few months which is rather short and changing your plans because you get a harsh winter instead of a normal one is usually not worth it, if you even notice it.

## Reply 9 — participant_002 · 2021-02-23 · post-27315758

<!-- artifact:quote:start -->
> riadach said: New Irish provinces? Who'd have guessed? Click to expand...
<!-- artifact:quote:end -->
Satisfied?

## Reply 10 — participant_008 · 2021-02-23 · post-27315760

Good news for the Game of Thrones mod!

## Reply 11 — participant_009 · 2021-02-23 · post-27315761

AGOT references intensifies...

## Reply 12 — participant_010 · 2021-02-23 · post-27315763

Wow that looks great Im sure this DD will get much better responses than the last one 1) Will winter only effect the combat, or are other systems, for example economics tied into this? 2) Will there be a way to predict the severity of the coming winter? Will it be necessary to make preparations for the winter like it was common back than? 3) How will performance be impacted? I guess you wont use the HoI3 system but still... 4) Any chance for new map modes? I really miss one where all existing and potential historic buildings are marked...

## Reply 13 — participant_011 · 2021-02-23 · post-27315765

Ireland was a bit too skinny.

## Reply 14 — participant_012 · 2021-02-23 · post-27315768

Great Job. But the videos do not work for me. Any suggestions.

## Reply 15 — participant_006 · 2021-02-23 · post-27315770

<!-- artifact:quote:start -->
> Voy said: Satisfied? Click to expand...
<!-- artifact:quote:end -->
Never!

## Reply 16 — participant_013 · 2021-02-23 · post-27315771

Where are the people who downvoted me when I said that we would have a DD this week? Very cool changes btw. Looking for the next DDs before the DLC announce at the Paradox Insider!

## Reply 17 — participant_014 · 2021-02-23 · post-27315773

<!-- artifact:quote:start -->
> halbort said: Great Job. But the videos do not work for me. Any suggestions. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Servancour said: Videos doesn't appear to work properly. We'll get those sorted in a moment! Click to expand...
<!-- artifact:quote:end -->
*(no text body — reaction-only or media-only post)*

## Reply 18 — participant_015 · 2021-02-23 · post-27315774

<!-- artifact:quote:start -->
> Servancour said: While Italy hasn't suffered from larger baronies in the same vein as Ireland, the area didn’t quite feel up to par with many other regions within Europe. Especially in terms of overall holding count. Italy generally had a bit too few holdings per county, so we’ve added new baronies in various places throughout the peninsula, from the slopes of the Alps all the way down to Reggio Calabria. The southern half in particular got some much needed attention. In the new setup, you’ll find significantly less counties with only two baronies. To mention a few examples, you’ll find that the county of Veneto has Malamacco as a new barony, Agnone can be found in the county of Lanciano, and Lecce is now an actual holding in the county with the same name. Overall, this should make Italy more representative of its historical impact and more fun to play in. Click to expand...
<!-- artifact:quote:end -->
So, how exactly are you planning to replicate the independent Italian city-states? If the individual city-states aren't available as counties, they can't be represented at any point in the game's timespan as independent policies, since independent baronies can't exist in CK3.

## Reply 19 — participant_016 · 2021-02-23 · post-27315776

<!-- artifact:quote:start -->
> halbort said: Great Job. But the videos do not work for me. Any suggestions. Click to expand...
<!-- artifact:quote:end -->
There are some minor technical difficulties there. Apologies, we are working to get those fixed! //Gustav

## Reply 20 — participant_008 · 2021-02-23 · post-27315778

"Fire" hints last week. "Ice" this week. Next DLC is a Game of Thrones total conversion Flavour Pack confirmed.

## Reply 21 — participant_017 · 2021-02-23 · post-27315779

More map improvements? Yes! Hope for Sampi nerf and Novgorod up.

## Reply 22 — participant_018 · 2021-02-23 · post-27315780

I think winter will contribute to making different parts of the map actually feel different. If there could also be a similar system for the monsoon in the south, it could highlight the differences in climate even more. Also, a more detailed map is always welcome.

## Reply 23 — participant_007 · 2021-02-23 · post-27315781

Will winter have an effect on river crossings, i.e. rivers freezing in harsh winter and allow crossings everywhere?

## Reply 24 — participant_019 · 2021-02-23 · post-27315782

Are the winters somewhat randomised? As in some years you might experience a mild year in a certain location, while in other years the same location could experience a normal or harsh winter? That would be quite interesting.

## Reply 25 — participant_006 · 2021-02-23 · post-27315785

I count two extra Irish counties, Ennis and Uí Mhaine. (Although I would suggest renaming Ennis to Thomond, and Thomond to Limerick). What's the barony count increases by?

## Reply 26 — participant_004 · 2021-02-23 · post-27315788

<!-- artifact:quote:start -->
> johnty5 said: "Fire" hints last week. "Ice" this week. Next DLC is a Game of Thrones total conversion Flavour Pack confirmed, Click to expand...
<!-- artifact:quote:end -->
Hell yeah! But really though, someone should tell Paradox to make a CK-like game from ASOIAF. Make it their Total War Warhammer.

## Reply 27 — participant_020 · 2021-02-23 · post-27315792

I love everything related to climate and attrition, thanks !

## Reply 28 — participant_021 · 2021-02-23 · post-27315795

With CK3's map style of both political and physical maps we can finally see the winter.

## Reply 29 — participant_001 · 2021-02-23 · post-27315797

<!-- artifact:quote:start -->
> Almas said: 1) Will winter only effect the combat, or are other systems, for example economics tied into this? 2) Will there be a way to predict the severity of the coming winter? Will it be necessary to make preparations for the winter like it was common back than? 3) How will performance be impacted? I guess you wont use the HoI3 system but still... 4) Any chance for new map modes? I really miss one where all existing and potential historic buildings are marked... Click to expand...
<!-- artifact:quote:end -->
1. It'll mostly affect combat for now. 2. Not per se. You'll learn what to expect in any given area as you play, but the actual severity is slightly random and will vary from year to year. 3. Testing so far shows only a small performance impact, but we are actively looking at it to make sure it doesn't go out of hand. 4. I do have a few map modes that I would like to have added at some point, but I can't say when we'll get about to adding any of those.

## Reply 30 — participant_007 · 2021-02-23 · post-27315801

Also, will modders be able to create their own "winters" (both having new graphics and deciding when and where said effect happens even apart from seasons)?

## Reply 31 — participant_022 · 2021-02-23 · post-27315802

Will this upcoming DLC be an actual full expansion or more of a flavor pack?

## Reply 32 — participant_023 · 2021-02-23 · post-27315805

<!-- artifact:quote:start -->
> Servancour said: Winter will also have an effect on your Men-at-Arms. Most noticeably, cavalry units will perform worse in normal and harsh winters. Heavy cavalry, in particular, will suffer some hefty penalties. I would advise against the use of heavy cavalry if you know you’ll be fighting battles in mountainous terrain during the winter season. On the other hand, some Men-at-Arms will get (sometimes quite significant) bonuses while fighting in winter. One such unit is the Tibetan culture unit, Mountaineers. Accustomed to the cold and the snow in the mountains, they can utilize it to their advantage in the form of a damage bonus whenever they participate in battles when winter is present. Click to expand...
<!-- artifact:quote:end -->
Not the DD I wanted but the DD I got Big fan of winter having an effect on combat/MAA! Looks very pretty too.

## Reply 33 — participant_024 · 2021-02-23 · post-27315807

Will we be seeing roads or urban sprawl on the map anytime soon?

## Reply 34 — participant_025 · 2021-02-23 · post-27315810

Happy to hear about this; and the pretty CK3 map will be much improved with the seasonal change! What I want to know for modders; could the winter setup handle a map spreading over both hemispheres? Lands south of the equator should have winters at the opposite time from the northern parts. So if besides harsh winter you could define a province as harsh_winter_opposite_hemisphere and it would properly get snow in June rather than January, I would be very happy

## Reply 35 — participant_026 · 2021-02-23 · post-27315817

First dev diary and they are already overdelivering by adding not only winter on the map that also affects individual MAA differently, but also specific sounds and updates to the map. I don't do this usually, but I TOLD YOU SO. The CK dev diaries have always been rarer than the others, but also much meatier.

## Reply 36 — participant_027 · 2021-02-23 · post-27315823

THIS is GREAT! Winter would be awesome! There will be any other weather conditions in future like rain for example? There will be seasons? Like hot summers, fall with colorful trees and so on? Please confirm if I understood that correctly - these two, map changes and winter mechanics will be free with 1.3 update? Or it's the first DLC/flavour pack content?

## Reply 37 — participant_028 · 2021-02-23 · post-27315826

How moddable are the winters? Specifically, can you set so different areas have winter at different times? Useful for simulating the south hemisphere.

## Reply 38 — participant_029 · 2021-02-23 · post-27315828

<!-- artifact:quote:start -->
> Niall9 said: Are the winters somewhat randomised? As in some years you might experience a mild year in a certain location, while in other years the same location could experience a normal or harsh winter? That would be quite interesting. Click to expand...
<!-- artifact:quote:end -->
that's what CKII had

## Reply 39 — participant_030 · 2021-02-23 · post-27315829

<!-- artifact:quote:start -->
> Finear said: these two, map changes and winter mechanics will be free with 1.3 update? O Click to expand...
<!-- artifact:quote:end -->
From what I've understood from the diary this will be part of the free update.

## Reply 40 — participant_031 · 2021-02-23 · post-27315834

I am bit sceptical about the consequences of a harsh weather because the game is not really made up for it. In games like Hearts of Iron you can plan for a winter campaign but in CK3 where battles could last weeks there is simply no way to avoid winter warfare. It's the same problem that makes it impossible to conquer England as William the Conquerer by Christmas 1066. The time flows to fast in comparison to the battles and the movement.

## Reply 41 — participant_001 · 2021-02-23 · post-27315841

<!-- artifact:quote:start -->
> jpapple said: From what I've understood from the diary this will be part of the free update. Click to expand...
<!-- artifact:quote:end -->
Correct! This is all part of the free update.

## Reply 42 — participant_032 · 2021-02-23 · post-27315854

<!-- artifact:quote:start -->
> johnty5 said: "Fire" hints last week. "Ice" this week. Next DLC is a Game of Thrones total conversion Flavour Pack confirmed, Click to expand...
<!-- artifact:quote:end -->
plus, they showed Ireland with Leinster, which is almost like Lanister

## Reply 43 — participant_001 · 2021-02-23 · post-27315867

<!-- artifact:quote:start -->
> Heatth said: How moddable are the winters? Specifically, can you set so different areas have winter at different times? Useful for simulating the south hemisphere. Click to expand...
<!-- artifact:quote:end -->
It's not possible to have winter appear at two different times. Other than that, winter should be fairly moddable. You can set exactly which provinces have winter, and how likely they are to get the different severities of winter by setting a "bias" value on them. There are a number of default values set in defines that can be overriden by individual provinces as well.

## Reply 44 — participant_025 · 2021-02-23 · post-27315871

<!-- artifact:quote:start -->
> Servancour said: It's not possible to have winter appear at two different times. Other than that, winter should be fairly moddable. You can set exactly which provinces have winter, and how likely they are to get the different severities of winter by setting a "bias" value on them. There are a number of default values set in defines that can be overriden by individual provinces as well. Click to expand...
<!-- artifact:quote:end -->
Hmmm, the hemisphere thing is a shame. Of course the other moddability features are very appreciated Is winter mimicable though? Could we duplicate the system by cobbling together a province modifier that similarly alters the terrain, sound, etc., and then script it to appear in the right provinces?

## Reply 45 — participant_033 · 2021-02-23 · post-27315880

Videos finally work. Good stuff. Tbh to me this seems more like a texture to the gameplay rather than a serious element. So more just to help make the game feel alive. Nice to see it finally arrive (considering we've seen snow in pre-release footage. I'm still hoping to see some urban and sprawl and maybe roads too but I guess that might be a bit further away in the future

## Reply 46 — participant_007 · 2021-02-23 · post-27315884

<!-- artifact:quote:start -->
> Servancour said: It's not possible to have winter appear at two different times. Other than that, winter should be fairly moddable. You can set exactly which provinces have winter, and how likely they are to get the different severities of winter by setting a "bias" value on them. There are a number of default values set in defines that can be overriden by individual provinces as well. Click to expand...
<!-- artifact:quote:end -->
Hm, a bit of a bummer. Would be nice if in the future the system could be opened up to allow modders to create their own region wide effects, complete with graphics and hook into game functions, like winters to simulate something like volcano erruptions, etc.

## Reply 47 — participant_034 · 2021-02-23 · post-27315885

Italy needed new baronies badly, especially in Sicily, so this is quite welcome. Ireland is nice too of course It seems to me the Winter addition may not say a whole lot about what the DLC is, unless it really is a Viking DLC, since it would make sense to add Winter in an update if you're going to work on Scandinavia.

## Reply 48 — participant_028 · 2021-02-23 · post-27315899

<!-- artifact:quote:start -->
> Servancour said: It's not possible to have winter appear at two different times. Other than that, winter should be fairly moddable. You can set exactly which provinces have winter, and how likely they are to get the different severities of winter by setting a "bias" value on them. There are a number of default values set in defines that can be overriden by individual provinces as well. Click to expand...
<!-- artifact:quote:end -->
That is very disappointing. Many mods expand the map or create a complete new one that encompasses more than one hemisphere, so it is a shame the winter is still limited to just one of them.

## Reply 49 — participant_035 · 2021-02-23 · post-27315901

How flexible? Is it possible to add crazy summer which would burn almost everything in the county?

## Reply 50 — participant_036 · 2021-02-23 · post-27315904

That is what in my Opinion a DD should look like. Now I can sit down and wait happy for the upcoming news and dlc. Thank you.

## Reply 51 — participant_037 · 2021-02-23 · post-27315911

Very interesting and informative. Thanks.

## Reply 52 — participant_008 · 2021-02-23 · post-27315916

Is this a new Alert icon? (From picture 4)

## Reply 53 — participant_034 · 2021-02-23 · post-27315918

<!-- artifact:quote:start -->
> johnty5 said: View attachment 685272 Is this a new Alert icon? (From picture 4) Click to expand...
<!-- artifact:quote:end -->
seems familiar to me, though I am not sure I remember how/why. election notice?

## Reply 54 — participant_038 · 2021-02-23 · post-27315928

Would (harsh) winter in coastal provinces prevent armies from (dis)embarking? It would probably make sense for armies e.g. in the Baltic not to be able to send massive invasion forces via sea, a lot of the ports would be mostly frozen. This would also create a strong motivation to try to get warm water ports for larger empires in that region.

## Reply 55 — participant_039 · 2021-02-23 · post-27315931

Sounds great. Not sure it’ll have big gameplay implications currently unless maybe you’re playing in an area of the world with very long winters, but honestly I’d be happy with it even without gameplay effects. It just looks nice and adds some dynamism to the map. I hope weather and other map effects keep being added!

## Reply 56 — participant_040 · 2021-02-23 · post-27315937

The word 'embrace' is in this DD title which is clearly signalling the long awaited (by me) CK/VtM crossover we (me) have all been waiting for.

## Reply 57 — participant_041 · 2021-02-23 · post-27315941

Heh, at first I thought the title was a comment on the community's overall reaction to last week's DD

## Reply 58 — participant_042 · 2021-02-23 · post-27315943

I like the new winter effect, thanks.

## Reply 59 — participant_043 · 2021-02-23 · post-27315954

<!-- artifact:quote:start -->
> Heatth said: That is very disappointing. Many mods expand the map or create a complete new one that encompasses more than one hemisphere, so it is a shame the winter is still limited to just one of them. Click to expand...
<!-- artifact:quote:end -->
Well maybe the settings for Winter on the South hemisphere would actually be warmer temperatures, while Summer colder? Not a modder myself but I'm almost sure you'd be able to tweak that. Awesome update CK3 team! Always wanted snow on the map, and the sound and battle consequences are brilliant! - Are there new events related to Winter and Cold? - Could we expect to see extremely hot summers and even drought events?

## Reply 60 — participant_008 · 2021-02-23 · post-27315959

Feels like the winter mechanic would interact well with a nomadic government type. Any plans for that?

## Reply 61 — participant_044 · 2021-02-23 · post-27315966

Videos should be all good and ready for you all!

## Reply 62 — participant_045 · 2021-02-23 · post-27315970

Good stuff! (The title had me half-expecting the subject matter to relate to funerals, since Death's embrace is traditionally cold.)

## Reply 63 — participant_046 · 2021-02-23 · post-27315990

Prediction: the DLC will be the Wars of the Roses. They had to implement winters of discontent to accurately model the conflict.

## Reply 64 — participant_008 · 2021-02-23 · post-27315998

CK3 Multiplayer Battle Royale mod/map: With supply-sapping, county-income-killing winter closing in on all sides, who will be the last ruler standing?

## Reply 65 — participant_047 · 2021-02-23 · post-27316002

While the added "depth" to attrition with winter is nice, I don't feel like it really adds much to war. One of the best strategies is already to split your army into 2-3 so that the ai is baited into attacking a "small" army and then just piling on. Time also moves REALLY fast in CK especially in wars.

## Reply 66 — participant_048 · 2021-02-23 · post-27316006

<!-- artifact:quote:start -->
> Servancour said: Greetings everyone! Don’t stand out there in the cold. Come on in and warm yourself by the fire! Have you made yourself comfortable? Excellent. Before we get to it, first things first. I know that all of you are eagerly awaiting more news regarding upcoming DLC content, but we’re not ready to start talking about those quite yet. Don’t fret, you will not have to wait that long. They say that patience is a virtue, but knowing better, I’ll leave this right here. For the next few weeks and the coming dev diaries we’ll talk a bit about what we have in store for the next major update, 1.3. In usual fashion, you can expect 1.3 to land alongside the upcoming DLC. Without further ado, let’s get to it shall we? Winter is Coming Winter is being introduced to CK3, making the already unforgiving world of the Middle Ages a much harsher place! As winter approaches, the map will gradually get covered in snow, clearly showing the extent of the freezing cold. The system itself is fairly flexible and allows for a great degree of control, as we can set which provinces should experience winter, and which shouldn’t. Winter won’t be limited to just the northernmost parts of the map, so expect snow to appear in places such as the Persian Mountains, or on the heights of the Tibetan plateau. View attachment 685202 With the introduction of winter comes new gameplay considerations. It wouldn’t be any point in adding this cool system if it didn’t do anything interesting. Winter comes in three different variants; mild, normal, and harsh. Mild and normal winters will be fairly common throughout central Europe and parts of southern Europe, while harsh winters are rarer but can still occur. If you find yourself lost in the frozen landscape of places such as Sápmi, Mongolia, or Himalaya, expect harsh winters to be the norm and plan accordingly! We wanted to make sure that it’s easy to see what level of winter is present in any given barony at a glance. The amount of snow increases with higher levels. Mild winters should generally be fairly easy to spot, with patches of green still clearly visible. In contrast, harsh winters mostly cover an entire province with snow. Certain areas might even have clouds with steady snowfall appearing for that extra level of detail! Depending on the severity of winter, your armies will start to lose supply over time. Harsh winter means you’ll lose more supply each month, making it a risky business to go above the supply limit for an extended period during the winter season. Harsh winters will also have armies suffer more fatal casualties during battles. Winter will also have an effect on your Men-at-Arms. Most noticeably, cavalry units will perform worse in normal and harsh winters. Heavy cavalry, in particular, will suffer some hefty penalties. I would advise against the use of heavy cavalry if you know you’ll be fighting battles in mountainous terrain during the winter season. On the other hand, some Men-at-Arms will get (sometimes quite significant) bonuses while fighting in winter. One such unit is the Tibetan culture unit, Mountaineers. Accustomed to the cold and the snow in the mountains, they can utilize it to their advantage in the form of a damage bonus whenever they participate in battles when winter is present. View attachment 685219 The system for setting winter bonuses (or penalties if you will) on Men-at-Arms works just like setting terrain bonuses, making it very friendly for any modders out there. While winter and snow might look and play nice, it wouldn’t be complete without a fitting soundscape. I’ll hand over to our sound designer Gustav to talk a bit about what he did to bring winter to life! A Sound Plan Winter for a Swede is like butter on toast, we love it! (brr… please be spring soon!) There are two areas where we have updated audio on the map. Holdings: Audio gets reflected with real-time updates to holdings. When winter spreads over your lands; or any lands for that matter, folks now go inside their homes, birds have migrated to more southern regions, and the animals are now in their stables or inside by the hearths, cozy! The way we achieve this is to link the shader that covers the region with snow and Ice to a real-time float parameter, that then talks to our Audio Middleware Engine Fmod. Awesome, but what does it actually do? It attenuates sound layers, controls effects such as equalizers and reverb, and reshapes the original sound that was there during summertime, and morphs it into wintertime. VFX: We also have snow storms appearing, for both mild and harsh winters. If you hear the sounds, be wary, your troops will most likely suffer some penalties in these areas. Tread carefully! The snowstorms are spawned on the map with the particle system, which allows us to be able to spatialize the sound effects ( position them in a 3D location X-Y-Z ) as the mild snowstorm morphs into the harsh storm, so do the sound effects. I’ll leave you with this; a snippet of what goes on under the hood inside Fmod during winter. Obligatory Map Update Anyone who has followed the history of CK2 or the DDs for CK3 will know that I do enjoy my maps, and I’ll try to get in smaller map updates or improvements whenever I can. Since release, we’ve identified a few general areas that we think can be improved upon. Some of these will be updated in 1.3. First up, Ireland. The baronies in Ireland were a bit too large, making the emerald island have a significantly less holding density than its neighbors, England and Scotland. The western half of Ireland in particular suffered from a few quite large baronies. To solve this issue, we’ve added a number of new baronies, along with a couple of new counties, that should improve the overall experience of playing in Ireland. View attachment 685220 While Italy hasn't suffered from larger baronies in the same vein as Ireland, the area didn’t quite feel up to par with many other regions within Europe. Especially in terms of overall holding count. Italy generally had a bit too few holdings per county, so we’ve added new baronies in various places throughout the peninsula, from the slopes of the Alps all the way down to Reggio Calabria. The southern half in particular got some much needed attention. In the new setup, you’ll find significantly less counties with only two baronies. To mention a few examples, you’ll find that the county of Veneto has Malamacco as a new barony, Agnone can be found in the county of Lanciano, and Lecce is now an actual holding in the county with the same name. Overall, this should make Italy more representative of its historical impact and more fun to play in. View attachment 685221 View attachment 685222 That’ll be it for today! I do have a few more map improvements in store for you, but those will have to wait. Until next time! Click to expand...
<!-- artifact:quote:end -->
Thank you very much for upgrading Italian Map! XD

## Reply 67 — participant_049 · 2021-02-23 · post-27316010

Winter weather looks and sounds great! The map will surely feel even more alive now. Loving these map improvements in Ireland and Italy as well. I was wondering though if you are referring to this Malamocco or if Malamacco is the correct name of another/older settlement in the region?

## Reply 68 — participant_050 · 2021-02-23 · post-27316011

<!-- artifact:quote:start -->
> Servancour said: Obligatory Map Update Anyone who has followed the history of CK2 or the DDs for CK3 will know that I do enjoy my maps, and I’ll try to get in smaller map updates or improvements whenever I can. Since release, we’ve identified a few general areas that we think can be improved upon. Some of these will be updated in 1.3. First up, Ireland. The baronies in Ireland were a bit too large, making the emerald island have a significantly less holding density than its neighbors, England and Scotland. The western half of Ireland in particular suffered from a few quite large baronies. To solve this issue, we’ve added a number of new baronies, along with a couple of new counties, that should improve the overall experience of playing in Ireland. While Italy hasn't suffered from larger baronies in the same vein as Ireland, the area didn’t quite feel up to par with many other regions within Europe. Especially in terms of overall holding count. Italy generally had a bit too few holdings per county, so we’ve added new baronies in various places throughout the peninsula, from the slopes of the Alps all the way down to Reggio Calabria. The southern half in particular got some much needed attention. In the new setup, you’ll find significantly less counties with only two baronies. To mention a few examples, you’ll find that the county of Veneto has Malamacco as a new barony, Agnone can be found in the county of Lanciano, and Lecce is now an actual holding in the county with the same name. Overall, this should make Italy more representative of its historical impact and more fun to play in. Click to expand...
<!-- artifact:quote:end -->
I do not want to seem to critical as I welcome any fixes. But there are some obligatory things to mention which I think should still be fixed: Ireland: 1. The Shannon Estuary is still not navigable. It is represented as a river while there is a clear distinction. Shannon Estuary - Wikipedia en.wikipedia.org 2. Some places are still in the wrong location, Limerick being the primary one, which should be located at the end of the estuary where the Shannon river meets it. Alpine Region: I commend the changes to Italy, but do feel that Switzerland still lacks a great deal of detail, being mostly covered in a mountain range, where baronies and counties ought to be located. SImilarly the Aosta valley points north-south, while it ought to be East-West and open up into Savoy instead.

## Reply 69 — participant_051 · 2021-02-23 · post-27316013

Hmm... Winter... that's weather. What else is weather? Typhoons! And the most relevant typhoons of the medieval period... are the two that derailed Kublai Khan's invasion of Japan in 1274 and 1281! FLEETS AND EAST ASIA EXPANSION CONFIRMED!

## Reply 70 — participant_052 · 2021-02-23 · post-27316014

Very Nice. Maybe some more optional weather effects to really show bad bad the weather is like harsh winter will show a visual blizzard in the province?

## Reply 71 — participant_020 · 2021-02-23 · post-27316037

Will this update destroy old campaign savefiles?

## Reply 72 — participant_053 · 2021-02-23 · post-27316038

Very nice feature for sure. I like how it's going to be interacting with the combat system. And the map changers are certainly welcome. I haven't played in Italy yet, but I'll probably give it a try after 1.3 drops.

## Reply 73 — participant_054 · 2021-02-23 · post-27316051

Sounds cool I already dread my casualtie numbers seasons will inflict upon my men. I do expect that other seasons will be included too? Super hot summers in some areas and monsoons in SE Asia? This also gives perfect operations to add Additional weather anomalies like dust rain (especially blood rain for some biblical turmoil, which would give reason to add more catastrophes) Keep up the work but try to not leave us hanging for too long

## Reply 74 — participant_055 · 2021-02-23 · post-27316059

Are there any historically harsh winters that are represented in the game or is it purely randomized? Could a winter’s harshness be determined by an event?

## Reply 75 — participant_056 · 2021-02-23 · post-27316061

<!-- artifact:quote:start -->
> Ixal said: Will winter have an effect on river crossings, i.e. rivers freezing in harsh winter and allow crossings everywhere? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Niall9 said: Are the winters somewhat randomised? As in some years you might experience a mild year in a certain location, while in other years the same location could experience a normal or harsh winter? That would be quite interesting. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Ares Enyalios said: I am bit sceptical about the consequences of a harsh weather because the game is not really made up for it. In games like Hearts of Iron you can plan for a winter campaign but in CK3 where battles could last weeks there is simply no way to avoid winter warfare. It's the same problem that makes it impossible to conquer England as William the Conquerer by Christmas 1066. The time flows to fast in comparison to the battles and the movement. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> IntoTheStars said: Sounds great. Not sure it’ll have big gameplay implications currently unless maybe you’re playing in an area of the world with very long winters, but honestly I’d be happy with it even without gameplay effects. It just looks nice and adds some dynamism to the map. I hope weather and other map effects keep being added! Click to expand...
<!-- artifact:quote:end -->
No, it's a really cool idea though. The tricky part is time dilation, the fact that time in CK passes quite fast compared to real life. Absolutely, though this heavily depends on where you are. If you're in southern continental Europe, you can pretty much expect mild winters. If you're close to the polar circle you can expect harsh to be the norm. If you're somewhere in-between, it can vary - but we've been quite diligent in assuring that nothing feels extremely out of place. There are several regions where Harsh winter can't appear, for example. Most of the significant effects take hold at the start of a combat rather than continually change during it, specifically because of the time dilation CK uses. It should be good enough to plan an engagement to occur during a specific point of winter, rather than having to plan for winter to occur during it. It feels quite good in practice, even if it is a trade-off. Mild winters have quite a nominal impact, by design. We want Normal and especially Harsh winters to 'pop', with quite tangible effects. For example, if you're in the steppe fending off light cavalry, picking a fight in harsh winter might actually be very beneficial for you. There's a tactical layer to it, and it's generally very good to defend in harsh winter should you be attacked.

## Reply 76 — participant_029 · 2021-02-23 · post-27316079

<!-- artifact:quote:start -->
> Kazanov said: Will this update destroy old campaign savefiles? Click to expand...
<!-- artifact:quote:end -->
probably, due to the map changing, but you can revert via steam

## Reply 77 — participant_002 · 2021-02-23 · post-27316083

Will winter become an economic factor as well? Say as an amplifier to the region type. I feel like CK3 needs some way to deter the AI from conquering worthless provinces by actually making some provinces virtually worthless to non-tribals.

## Reply 78 — participant_057 · 2021-02-23 · post-27316089

<!-- artifact:quote:start -->
> TheSeraphim said: While the added "depth" to attrition with winter is nice, I don't feel like it really adds much to war. One of the best strategies is already to split your army into 2-3 so that the ai is baited into attacking a "small" army and then just piling on. Time also moves REALLY fast in CK especially in wars. Click to expand...
<!-- artifact:quote:end -->
Unless the attrition is really significant and they introduce a system where a stopped army suffers much less from it - thus inducing pauses in warfare due to seasons - the net effect on gameplay will be negligible. As for time moving really fast, well, if significant army management is required during winter, there is always the option to det it to speed 1 or 2. Overall, I think it is a nice dev diary. Lets see if the army AI takes into its calculations the actual value of attrition while planning its moves, in case Paradox makes it too bland and if one needs to mod it to more extreme levels to change the gameplay.

## Reply 79 — participant_058 · 2021-02-23 · post-27316118

So will the AI be smart enough to withdraw troops from winter areas? Ha ha, just kidding. Nice looking system for the player though.

## Reply 80 — participant_045 · 2021-02-23 · post-27316122

<!-- artifact:quote:start -->
> Kazanov said: Will this update destroy old campaign savefiles? Click to expand...
<!-- artifact:quote:end -->
There are map changes, so yes, you are likely to have problems if you load your 1.2 save in 1.3. (Probably not as weird as the time in EU4 where Portuguese Brazil gained provinces in Russia if you loaded an old save on a new map, but still problems.)

## Reply 81 — participant_059 · 2021-02-23 · post-27316166

I hope the ai can handle this and don't only cheat supplies for the winter time. Maybe they are smart enough to avoid wars in winter or love to attack in winter, if they play as nations like Rus, vikings, etc.

## Reply 82 — participant_060 · 2021-02-23 · post-27316183

<!-- artifact:quote:start -->
> Servancour said: The system for setting winter bonuses (or penalties if you will) on Men-at-Arms works just like setting terrain bonuses, making it very friendly for any modders out there. Click to expand...
<!-- artifact:quote:end -->
Hi, sorry if this a dumb question but I'm not yet acquainted with modifiers in CK3: Would it be possible to apply the climate modifiers outside the scope of a particular man-at-arms type, applying the bonus to all units of a specific culture for example?

## Reply 83 — participant_031 · 2021-02-23 · post-27316200

<!-- artifact:quote:start -->
> rageair said: Most of the significant effects take hold at the start of a combat rather than continually change during it, specifically because of the time dilation CK uses. It should be good enough to plan an engagement to occur during a specific point of winter, rather than having to plan for winter to occur during it. It feels quite good in practice, even if it is a trade-off. Click to expand...
<!-- artifact:quote:end -->
Thanks for the reply. That i am sceptical how it should work in the end, doesn't mean that i have no cofidence at all that you guys will get it working. Having the same weather during the entire battle is clearly a good solution but this doesn't let the player avoid fighting in situations where attrition is just horrible. 90 % of the wars are not over within 1 year ingame time. The battles take often weeks and sieges at least months. That means that i can't avoid winter attrition. I guess you will in the end implent it in a way where the attrition is not that high as intended in the beginning. I am especially worried about the AI. In Imperator Rome there was a development phase where the AI absolutly got starved by attrition. Definitly talk to your collegues about their experiences. Really consequencal would be a solution where large warfare is almost impossible during winter and only smal warbands of a 100 man engage in the fights. If the AI could handle this, this would make smal scale battles actually fun, but i am not sure if this would be fun from a gameplay experience.

## Reply 84 — participant_061 · 2021-02-23 · post-27316223

Thank you for the informative Dev diary that actually does give us some information about what is coming up for the game! Very excited to see what else you guys have planned over the next few weeks!!

## Reply 85 — participant_062 · 2021-02-23 · post-27316236

<!-- artifact:quote:start -->
> Ixal said: Will winter have an effect on river crossings, i.e. rivers freezing in harsh winter and allow crossings everywhere? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Ares Enyalios said: I am bit sceptical about the consequences of a harsh weather because the game is not really made up for it. In games like Hearts of Iron you can plan for a winter campaign but in CK3 where battles could last weeks there is simply no way to avoid winter warfare. It's the same problem that makes it impossible to conquer England as William the Conquerer by Christmas 1066. The time flows to fast in comparison to the battles and the movement. Click to expand...
<!-- artifact:quote:end -->
Two additional questions answered by the dev team: No freezing rivers but it would be very interesting Winter matters when a battle starts. So you can try to avoid it by making sure you start battles before winter arrives or gets worse.

## Reply 86 — participant_062 · 2021-02-23 · post-27316270

Recap of current Q/A asked by the community & answered by our dev team: ▲ Will winter only affect Combat, or are other systems tied to it, like Economy? ► It'll mostly affect combat for now. ▲ Will there be a way to predict the severity of the coming winter? Will it be necessary to make preparations for the winter like it was common back then? ► Not per se. You'll learn what to expect in any given area as you play, but the actual severity is slightly random and will vary from year to year. ▲ How will performance be impacted? ► Testing so far shows only a small performance impact, but we are actively looking at it to make sure it doesn't go out of hand. ▲ Any chance for new map modes? I really miss one where all existing and potential historic buildings are marked... ► I do have a few map modes that I would like to have added at some point, but I can't say when we'll get about to adding any of those. ▲ Is Update 1.3 free? ► Indeed, this content is part of the free update. ▲ How moddable are the winters? Specifically, can you set so different areas have winter at different times? Useful for simulating the south hemisphere. ► It's not possible to have winter appear at two different times. Other than that, winter should be fairly moddable. You can set exactly which provinces have winter, and how likely they are to get the different severities of winter by setting a "bias" value on them. There are a number of default values set in defines that can be overriden by individual provinces as well. ▲ Are the winters somewhat randomised? ► Absolutely, though this heavily depends on where you are. If you're in southern continental Europe, you can pretty much expect mild winters. If you're close to the polar circle you can expect harsh to be the norm. If you're somewhere in-between, it can vary - but we've been quite diligent in assuring that nothing feels extremely out of place. There are several regions where Harsh winter can't appear, for example. ▲ In CK3, battles could last for weeks. I don't see any way to avoid winter warfare...? ► Most of the significant effects take hold at the start of a combat rather than continually change during it, specifically because of the time dilation CK uses. It should be good enough to plan an engagement to occur during a specific point of winter, rather than having to plan for winter to occur during it. It feels quite good in practice, even if it is a trade-off. ► Mild winters have quite a nominal impact, by design. We want Normal and especially Harsh winters to 'pop', with quite tangible effects. For example, if you're in the steppe fending off light cavalry, picking a fight in harsh winter might actually be very beneficial for you. There's a tactical layer to it, and it's generally very good to defend in harsh winter should you be attacked. ► Winter matters when a battle starts. So you can try to avoid it by making sure you start battles before winter arrives or gets worse.

## Reply 87 — participant_063 · 2021-02-23 · post-27316278

good dev diary

## Reply 88 — participant_036 · 2021-02-23 · post-27316279

Will the Update include maybe a solving in terms of the Multiplayer drop out problem? Most times after some time my mates drop out during the game.

## Reply 89 — participant_064 · 2021-02-23 · post-27316296

<!-- artifact:quote:start -->
> Servancour said: Veneto has Malamacco as a new barony Click to expand...
<!-- artifact:quote:end -->
Unless I'm missing on some local history, the name should be Malamocco, with an O. Please do correct me if I'm wrong

## Reply 90 — participant_065 · 2021-02-23 · post-27316302

Winter is coming. Alright, I won't be too critical. This is a great change, and time passing will be easier to see, which is always cool. I hope that each year in the game will have different amounts of winter in different places. For instance Denmark didn't always have snow - and sometimes it had a lot etc. I will, however, look very much forward to deeper political mechanics that can add some interesting mechanics. Or perhaps a much more interesting siege system which probably could work well with the Winter system. Still, this is a decent start for updating CK3.

## Reply 91 — participant_066 · 2021-02-23 · post-27316305

This sounds neat, but I'm very concerned that it will just be something that both players and AI (if the AI is even aware that winter exists) treat as a basically unavoidable source of extra attrition. With the rate that armies move and the time battles last, it has never felt reasonable to have a spring and summer campaign and then retreat for the harvest and winter. Especially in many areas of the map where harsh winters would be expected, as the provinces are so large it takes a month or more just to walk between them! It's hard for me to imagine what my play pattern would have to look like to meaningfully take advantage of winter coming and going.

## Reply 92 — participant_065 · 2021-02-23 · post-27316309

<!-- artifact:quote:start -->
> Servancour said: 1. It'll mostly affect combat for now. 2. Not per se. You'll learn what to expect in any given area as you play, but the actual severity is slightly random and will vary from year to year. 3. Testing so far shows only a small performance impact, but we are actively looking at it to make sure it doesn't go out of hand. 4. I do have a few map modes that I would like to have added at some point, but I can't say when we'll get about to adding any of those. Click to expand...
<!-- artifact:quote:end -->
So, it will mostly be a visual change and not change much other than battles in those areas? Well, to be fair, the game can't really accommodate any other things as there's no political system to change and the economy is so basic that it never would be able to incorporate winter. That said, map updates are always nice and I hope you'll tie it into some deeper game play at some point. Edit: I'm also happy to see Paradox engaging with community in this thread.

## Reply 93 — participant_067 · 2021-02-23 · post-27316358

Will different winter types be addable with mods? Similarly, will other weather effects be moddable?

## Reply 94 — participant_068 · 2021-02-23 · post-27316397

Nice to hear new news about upcoming updates. Above all the focus on winter, hopefully they also address the impacts on the economy during winters. And also if you could inform us if the next DLC is the flavor package or the expansion, although from the information obtained in these months I deduce that it will be a flavor package. Anyway, thanks for keeping us informed!

## Reply 95 — participant_069 · 2021-02-23 · post-27316407

Gameplay-wise this sounds like something players will just ignore while Genghis Khan's stupid AI dies in Tibet. But visually it seems nice.

## Reply 96 — participant_070 · 2021-02-23 · post-27316424

This is awesome for the GOT mod !

## Reply 97 — participant_071 · 2021-02-23 · post-27316425

<!-- artifact:quote:start -->
> Servancour said: Greetings everyone! Don’t stand out there in the cold. Come on in and warm yourself by the fire! Have you made yourself comfortable? Excellent. Before we get to it, first things first. I know that all of you are eagerly awaiting more news regarding upcoming DLC content, but we’re not ready to start talking about those quite yet. Don’t fret, you will not have to wait that long. They say that patience is a virtue, but knowing better, I’ll leave this right here. For the next few weeks and the coming dev diaries we’ll talk a bit about what we have in store for the next major update, 1.3. In usual fashion, you can expect 1.3 to land alongside the upcoming DLC. Without further ado, let’s get to it shall we? Winter is Coming Winter is being introduced to CK3, making the already unforgiving world of the Middle Ages a much harsher place! As winter approaches, the map will gradually get covered in snow, clearly showing the extent of the freezing cold. The system itself is fairly flexible and allows for a great degree of control, as we can set which provinces should experience winter, and which shouldn’t. Winter won’t be limited to just the northernmost parts of the map, so expect snow to appear in places such as the Persian Mountains, or on the heights of the Tibetan plateau. View attachment 685202 With the introduction of winter comes new gameplay considerations. It wouldn’t be any point in adding this cool system if it didn’t do anything interesting. Winter comes in three different variants; mild, normal, and harsh. Mild and normal winters will be fairly common throughout central Europe and parts of southern Europe, while harsh winters are rarer but can still occur. If you find yourself lost in the frozen landscape of places such as Sápmi, Mongolia, or Himalaya, expect harsh winters to be the norm and plan accordingly! We wanted to make sure that it’s easy to see what level of winter is present in any given barony at a glance. The amount of snow increases with higher levels. Mild winters should generally be fairly easy to spot, with patches of green still clearly visible. In contrast, harsh winters mostly cover an entire province with snow. Certain areas might even have clouds with steady snowfall appearing for that extra level of detail! Depending on the severity of winter, your armies will start to lose supply over time. Harsh winter means you’ll lose more supply each month, making it a risky business to go above the supply limit for an extended period during the winter season. Harsh winters will also have armies suffer more fatal casualties during battles. Winter will also have an effect on your Men-at-Arms. Most noticeably, cavalry units will perform worse in normal and harsh winters. Heavy cavalry, in particular, will suffer some hefty penalties. I would advise against the use of heavy cavalry if you know you’ll be fighting battles in mountainous terrain during the winter season. On the other hand, some Men-at-Arms will get (sometimes quite significant) bonuses while fighting in winter. One such unit is the Tibetan culture unit, Mountaineers. Accustomed to the cold and the snow in the mountains, they can utilize it to their advantage in the form of a damage bonus whenever they participate in battles when winter is present. View attachment 685219 The system for setting winter bonuses (or penalties if you will) on Men-at-Arms works just like setting terrain bonuses, making it very friendly for any modders out there. While winter and snow might look and play nice, it wouldn’t be complete without a fitting soundscape. I’ll hand over to our sound designer Gustav to talk a bit about what he did to bring winter to life! A Sound Plan Winter for a Swede is like butter on toast, we love it! (brr… please be spring soon!) There are two areas where we have updated audio on the map. Holdings: Audio gets reflected with real-time updates to holdings. When winter spreads over your lands; or any lands for that matter, folks now go inside their homes, birds have migrated to more southern regions, and the animals are now in their stables or inside by the hearths, cozy! The way we achieve this is to link the shader that covers the region with snow and Ice to a real-time float parameter, that then talks to our Audio Middleware Engine Fmod. Awesome, but what does it actually do? It attenuates sound layers, controls effects such as equalizers and reverb, and reshapes the original sound that was there during summertime, and morphs it into wintertime. VFX: We also have snow storms appearing, for both mild and harsh winters. If you hear the sounds, be wary, your troops will most likely suffer some penalties in these areas. Tread carefully! The snowstorms are spawned on the map with the particle system, which allows us to be able to spatialize the sound effects ( position them in a 3D location X-Y-Z ) as the mild snowstorm morphs into the harsh storm, so do the sound effects. I’ll leave you with this; a snippet of what goes on under the hood inside Fmod during winter. Obligatory Map Update Anyone who has followed the history of CK2 or the DDs for CK3 will know that I do enjoy my maps, and I’ll try to get in smaller map updates or improvements whenever I can. Since release, we’ve identified a few general areas that we think can be improved upon. Some of these will be updated in 1.3. First up, Ireland. The baronies in Ireland were a bit too large, making the emerald island have a significantly less holding density than its neighbors, England and Scotland. The western half of Ireland in particular suffered from a few quite large baronies. To solve this issue, we’ve added a number of new baronies, along with a couple of new counties, that should improve the overall experience of playing in Ireland. View attachment 685220 While Italy hasn't suffered from larger baronies in the same vein as Ireland, the area didn’t quite feel up to par with many other regions within Europe. Especially in terms of overall holding count. Italy generally had a bit too few holdings per county, so we’ve added new baronies in various places throughout the peninsula, from the slopes of the Alps all the way down to Reggio Calabria. The southern half in particular got some much needed attention. In the new setup, you’ll find significantly less counties with only two baronies. To mention a few examples, you’ll find that the county of Veneto has Malamacco as a new barony, Agnone can be found in the county of Lanciano, and Lecce is now an actual holding in the county with the same name. Overall, this should make Italy more representative of its historical impact and more fun to play in. View attachment 685221 View attachment 685222 That’ll be it for today! I do have a few more map improvements in store for you, but those will have to wait. Until next time! Click to expand...
<!-- artifact:quote:end -->
What!? a CK3 Dev Diary? Nice!

## Reply 98 — participant_001 · 2021-02-23 · post-27316426

<!-- artifact:quote:start -->
> Kazanov said: Will this update destroy old campaign savefiles? Click to expand...
<!-- artifact:quote:end -->
And just to make sure this gets addressed. Generally speaking, you should be able to continue with your save, and the game should be fine. There might be some oddities though, since we are updating the map in a few areas. Previous versions are usually made available in Steam, and we recommend you to continue playing on the 1.2.2 branch if you have a campaign that you really want to finish and don't want to risk running into any potential issues.

## Reply 99 — participant_072 · 2021-02-23 · post-27316437

No offence, but we all know Patience is a virtue and laziness is a sin.

## Reply 100 — participant_073 · 2021-02-23 · post-27316439

>heavy cavalry now nerfed by seasons I mean, okay, not like there was much reason to use them much before this anyways I guess.

## Reply 101 — participant_020 · 2021-02-23 · post-27316449

<!-- artifact:quote:start -->
> Servancour said: And just to make sure this gets addressed. Generally speaking, you should be able to continue with your save, and the game should be fine. There might be some oddities though, since we are updating the map in a few areas. Previous versions are usually made available in Steam, and we recommend you to continue playing on the 1.2.2 branch if you have a campaign that you really want to finish and don't want to risk running into any potential issues. Click to expand...
<!-- artifact:quote:end -->
Well, ill have to wait or see how game-breaking are these oddities, i cant wait to see what else the team has prepared for the next update

## Reply 102 — participant_074 · 2021-02-23 · post-27316475

<!-- artifact:quote:start -->
> Servancour said: 1. It'll mostly affect combat for now. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PDX-Nicou said: Recap of current Q/A asked by the community & answered by our dev team: ▲ Will winter only affect Combat, or are other systems tied to it, like Economy? ► It'll mostly affect combat for now. Click to expand...
<!-- artifact:quote:end -->
Well, I notice that "mostly" caveat - can you explain what effects it has outside of combat? (Or is it just supply you are referring to with that?)

## Reply 103 — participant_075 · 2021-02-23 · post-27316493

This is exciting! Got me really interested in the theme of the DLC

## Reply 104 — participant_076 · 2021-02-23 · post-27316506

Looks great! I wonder if we could get some kind of mechanics to simulate seasonal monsoons or rainstorms as well in certain parts of the world.

## Reply 105 — participant_077 · 2021-02-23 · post-27316516

This is cool to hear, and even cooler to see that the mechanic is going to have a real impact to both gameplay and aesthetics. I remember winter being a thing in CK2 (unless it was actually a part of a mod, I have played so much modded CK2 I can hardly remember what is from a mod and what is not) but it was ultimately just a minor attrition debuff on provinces that was barely noticeable or impactful unless you were REALLY min maxing.

## Reply 106 — participant_078 · 2021-02-23 · post-27316548

<!-- artifact:quote:start -->
> De_Dominator69 said: This is cool to hear, and even cooler to see that the mechanic is going to have a real impact to both gameplay and aesthetics. I remember winter being a thing in CK2 (unless it was actually a part of a mod, I have played so much modded CK2 I can hardly remember what is from a mod and what is not) but it was ultimately just a minor attrition debuff on provinces that was barely noticeable or impactful unless you were REALLY min maxing. Click to expand...
<!-- artifact:quote:end -->
It isn't a part of a mod, it's in vanilla CK2. It has mild, normal and harsh winters that affect supply limit and max attrition in counties. You're right about it not being overly noticeable in CK2 though. The only time I care about winter in the game is if I'm playing in an area that has long winters, I want a commander with the winter solider trait which can be pretty powerful. I wonder if they're going to add a commander trait associated with winter weather for the 1.3 update?

## Reply 107 — participant_002 · 2021-02-23 · post-27316562

<!-- artifact:quote:start -->
> Karlington said: Well, I notice that "mostly" caveat - can you explain what effects it has outside of combat? (Or is it just supply you are referring to with that?) Click to expand...
<!-- artifact:quote:end -->
I guess visually would be a point.

## Reply 108 — participant_079 · 2021-02-23 · post-27316606

<!-- artifact:quote:start -->
> Ixal said: Will winter have an effect on river crossings, i.e. rivers freezing in harsh winter and allow crossings everywhere? Click to expand...
<!-- artifact:quote:end -->
I think this is an good point. Barbarians crossing the frozen Rhine in 406 AD, bypassing the well-fortified bridges and forts, ultimately caused the collapse of Rome. Northern rivers freezing up, disabling Vikings from sailing through (was a feature in CK2) but also allowing armies to slowly cross them anywhere would be a nice feature.

## Reply 109 — participant_080 · 2021-02-23 · post-27316607

<!-- artifact:quote:start -->
> Karlington said: Well, I notice that "mostly" caveat - can you explain what effects it has outside of combat? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Karlington said: (Or is it just supply you are referring to with that?) Click to expand...
<!-- artifact:quote:end -->
I am too curious. I would guess a movement penalty too, they like those.

## Reply 110 — participant_081 · 2021-02-23 · post-27316617

Will there be ways to hook game events into this? For instance, trigger a specific event if area x is experiencing an uncharacteristically harsh winter?

## Reply 111 — participant_082 · 2021-02-23 · post-27316618

<!-- artifact:quote:start -->
> Ixal said: Will winter have an effect on river crossings, i.e. rivers freezing in harsh winter and allow crossings everywhere? Click to expand...
<!-- artifact:quote:end -->
This was during the reign of Henry VIII, so it's outside of CK3's timespan, but there was a winter where the Thames froze solid. King Henry, who usually took the State Barge to go to London for the Opening of Parliament, and to go in Procession there instead...

## Reply 112 — participant_083 · 2021-02-23 · post-27316622

<!-- artifact:quote:start -->
> Servancour said: Malamacco Click to expand...
<!-- artifact:quote:end -->
I don't want to be pedantic, but the place is named Malamocco (Małamoco, in Venitian) not Malamacco

## Reply 113 — participant_084 · 2021-02-23 · post-27316692

Very nice! It is nice to see some new content

## Reply 114 — participant_085 · 2021-02-23 · post-27316697

Glad to see the bridge across the major river in Mantua got added. Though wish the Venetian strait crossing I'd also suggested would've also gotten added. Otherwise, happy to see the other changes coming to CK3 and look forward to next week's diary.

## Reply 115 — participant_086 · 2021-02-23 · post-27316759

<!-- artifact:quote:start -->
> rageair said: No, it's a really cool idea though. The tricky part is time dilation, the fact that time in CK passes quite fast compared to real life. Absolutely, though this heavily depends on where you are. If you're in southern continental Europe, you can pretty much expect mild winters. If you're close to the polar circle you can expect harsh to be the norm. If you're somewhere in-between, it can vary - but we've been quite diligent in assuring that nothing feels extremely out of place. There are several regions where Harsh winter can't appear, for example. Most of the significant effects take hold at the start of a combat rather than continually change during it, specifically because of the time dilation CK uses. It should be good enough to plan an engagement to occur during a specific point of winter, rather than having to plan for winter to occur during it. It feels quite good in practice, even if it is a trade-off. Mild winters have quite a nominal impact, by design. We want Normal and especially Harsh winters to 'pop', with quite tangible effects. For example, if you're in the steppe fending off light cavalry, picking a fight in harsh winter might actually be very beneficial for you. There's a tactical layer to it, and it's generally very good to defend in harsh winter should you be attacked. Click to expand...
<!-- artifact:quote:end -->
I wouldn't mind if the time dilation was decreased in ck3, so that the same English army could potentially fight Stamford Bridge and Hastings within 3 weeks of each other. It would make playing on speed 2 or 3 more fun. You tend to get into the steamroll phase after 4 generations anyhow.

## Reply 116 — participant_087 · 2021-02-23 · post-27316769

<!-- artifact:quote:start -->
> Servancour said: And just to make sure this gets addressed. Generally speaking, you should be able to continue with your save, and the game should be fine. There might be some oddities though, since we are updating the map in a few areas. Previous versions are usually made available in Steam, and we recommend you to continue playing on the 1.2.2 branch if you have a campaign that you really want to finish and don't want to risk running into any potential issues. Click to expand...
<!-- artifact:quote:end -->
Will Ironman/ Achievements be broken?

## Reply 117 — participant_088 · 2021-02-23 · post-27316796

<!-- artifact:quote:start -->
> Servancour said: It's not possible to have winter appear at two different times. Other than that, winter should be fairly moddable. You can set exactly which provinces have winter, and how likely they are to get the different severities of winter by setting a "bias" value on them. There are a number of default values set in defines that can be overriden by individual provinces as well. Click to expand...
<!-- artifact:quote:end -->
That sounds fairly limited. Do different severities of winter have different lengths? Can we add new levels of winter severity besides the initial three? I'm still hoping for a workaround by defining duplicate winters timed appropriately for the southern hemisphere, but this kind of functionality seems handy for the base game too. What kinds of things are in the "number of default values"?

## Reply 118 — participant_089 · 2021-02-23 · post-27316817

The extra baronies in Ireland sound interesting - I'll be able to tweak my setup a bit, and possibly squeeze another new county in.

## Reply 119 — participant_090 · 2021-02-23 · post-27316841

I mean winter sounds good but the ai can't handle supplies now. Won't their enormous stacks just get obliterated?

## Reply 120 — participant_024 · 2021-02-23 · post-27316845

<!-- artifact:quote:start -->
> Servancour said: With the introduction of winter comes new gameplay considerations. It wouldn’t be any point in adding this cool system if it didn’t do anything interesting. Click to expand...
<!-- artifact:quote:end -->
Have you considered adding a small health debuff to characters located in winter areas?

## Reply 121 — participant_001 · 2021-02-23 · post-27316864

<!-- artifact:quote:start -->
> Karlington said: Well, I notice that "mostly" caveat - can you explain what effects it has outside of combat? (Or is it just supply you are referring to with that?) Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Blackwhitecavias said: Will Ironman/ Achievements be broken? Click to expand...
<!-- artifact:quote:end -->
Let's clarify that a bit. Winter won't have an impact on gameplay outside of warfare. Winter mainly affect battles, by giving bonuses or penalties to MaAs, and increases the overall fatal casualties on both sides. Armies also loses supply over time (a modifier that increases with each winter severity, and is added on top of the normal penalty for being over the supply limit), along with a couple of other additions, such as an increased movement speed during winter if your commander has a corresponding commander trait. As far as I know, ironman games should continue to run fine with the new version. Again though, if you have a save you are very invested in, I recommend you to continue with the 1.2.2 branch to avoid any potential issues.

## Reply 122 — participant_091 · 2021-02-23 · post-27316884

Can you give us an estimate of when the expansion associated with 1.3 will happen? Just so I can get the pennies ready in time...

## Reply 123 — participant_027 · 2021-02-23 · post-27316895

I'm pretty sure that they'll announce DLC release date on Paradox Insider event

## Reply 124 — participant_092 · 2021-02-23 · post-27316923

haven't looked into it in a while? are teleporting troops/MaA and lovers still a thing?

## Reply 125 — participant_089 · 2021-02-23 · post-27316956

@Servancour With your Irish map update it would be great if you could also finally split Strathclyde off from Galloway, rather than using the same duchy to represent both entities. They were totally separate, and represented different culture groups. It's like using the same title to represent Normandy and Brittany, which would - quite rightly - look absurd. I just find it very irritating because it's a very simple thing to fix - Galloway should be de jure Galloway and Carrick, and the rest can be Strathclyde. Both should exist in 867, and only Galloway should exist in 1066. Strathclyde collapsed in 1054. It should look something like this: Galloway should be ruled by the Cumbric kings of Galwyddel in 867 and the Gaelic lords of Galloway in 1066. Strathclyde should be ruled by the Cumbric kings of Alt Clut in 867 and not exist in 1066. Both should exist as de jure duchies however. This really isn't much work to do, but would make Scotland much better. Looking forward to the patch and DLC.

## Reply 126 — participant_093 · 2021-02-23 · post-27316990

Hi Devs. Excited to see more stuff being added to Ireland! Being from the North of Ireland, Carrickfergus castle is our most famous castle , but in-game the barony in Ulster for it is a city. Is this addressed in this update? Perhaps you could add another barony or maybe get an event to convert the city to a castle?

## Reply 127 — participant_094 · 2021-02-23 · post-27317003

MAY I HAVE YOU ATTENTION PLEASE? Please, get Iberian winters right this time. They didn't get them right in CK3, they didn't get them right in EU4, they didn't get them right in Hoi4, they didn't get them right in Imperator: Rome... They NEVER get them right. It's really not that hard, look at the image below, that is what it should be, please don't make it a weird stripe of land in the North Coast, the Coastal provinces NEVER get too cold. I highlighted in red what should be mild winters (Comparable to Ireland, Southern England, Western France, Northern Italy etc...), and in black what could potentially be normal winters depending on how the rest of Europe is portrayed. Further bellow is the corresponding Baronies or Counties, depending on how the the game calculates weather. (red: mild, dark red: potentially normal) Thank you for listening, looking forward to see CK3 as the first game in history to not mess this up.​ On a side note, since you are also tweaking the map as you go, could you please consider tweaking Southern Galicia one of these days? The borders with Badajoz are, simply put, wrong. The barony of Leiria was only conquered in 1135, the barony of Obidos in 1147, the one in Tomar in 1159, the one in Beira in 1165 and the one in Castelo Branco in 1174. All in different times, and yet all almost a century after 1066. These 5 baronies (2 counties) should belong to Badajoz and not Galicia in 1066. On the other hand, to balance this I would also add a couple literally of baronies in Portucale and Coimbra, it has a remarkably low county and barony density, among the lowest on all of Iberia (just compare it to North Galicia, it's like not even half as dense), it also has the lowest development by far (8, all other Catholic kingdoms have at least 11 and the Muslims have 14) this is all very odd considering this was one of the most densely populated parts of Iberia (and by the 15th century it had by far the highest density in the peninsula higher than the French average even) not to mention it was the only county powerfull enough to successfully rebel and rise to Kingdom status. Not asking for much, just 4 baronies and 1 historically accurate county that did exist during the game's timeframe (and you can keep development as it is).

## Reply 128 — participant_095 · 2021-02-23 · post-27317061

Will the AI use the seasons in determining when to start a new war/raise a rebellion? As much as I'd enjoy watching them raise troops in October to die out over the winter, it would be a bit dissappointing if my allies' only contribution to my war was employing my undertakers.

## Reply 129 — participant_096 · 2021-02-23 · post-27317094

Thanks for the update, happy to see you guys back. Besides the warfare in winter, I would humbly suggest some more ideas for the winter theme. For me, Ck3 is a fabulous RPG game. So, adding some winter event might make the characters more alive and a more well-rounded experience for players. Let me give some example : 1. Spouse or children sending hot meal/drink to you, slightly increase your health. 2. Due to the winter, framers/vassals in your realm are suffered in low profit, as a good liege you might generously give out your money. 3. Brave Vikinger's mature children can do a winter survival challenge (Just like the hunt), possibly increase their powers or prestige? In addition, Fighting in winter will decrease the popular opinion in your realm, buildings like crop field will decrease half of their income. A new set of winter clothing? It is merely the small number of ideas that I can imagine, and I am sure CK3's devs can create a much better storyline and events in the upcoming days, not only in terms of warfare. Hope to see you guys again!!

## Reply 130 — participant_025 · 2021-02-23 · post-27317110

<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: MAY I HAVE YOU ATTENTION PLEASE? Please, get Iberian winters right this time. They didn't get them right in CK3, they didn't get them right in EU4, they didn't get them right in Hoi4, they didn't get them right in Imperator: Rome... They NEVER get them right. It's really not that hard, look at the image below, that is what it should be, please don't make it a weird stripe of land in the North Coast, the Coastal provinces NEVER get too cold. I highlighted in red what should be mild winters (Comparable to Ireland, Southern England, Western France, Northern Italy etc...), and in black what could potentially be normal winters depending on how the rest of Europe is portrayed. Further bellow is the corresponding Baronies or Counties, depending on how the the game calculates weather. (red: mild, dark red: potentially normal) View attachment 685368 Thank you for listening, looking forward to see CK3 as the first game in history to not mess this up.​ On a side note, since you are also tweaking the map as you go, could you please consider tweaking Southern Galicia one of these days? The borders with Badajoz are, simply put, wrong. The barony of Leiria was only conquered in 1135, the barony of Obidos in 1147, the one in Tomar in 1159, the one in Beira in 1165 and the one in Castelo Branco in 1174. All in different times, and yet all almost a century after 1066. These 5 baronies (2 counties) should belong to Badajoz and not Galicia in 1066. On the other hand, to balance this I would also add a couple literally of baronies in Portucale and Coimbra, it has a remarkably low county and barony density, among the lowest on all of Iberia (just compare it to North Galicia, it's like not even half as dense), it also has the lowest development by far (8, all other Catholic kingdoms have at least 11 and the Muslims have 14) this is all very odd considering this was one of the most densely populated parts of Iberia (and by the 15th century it had by far the highest density in the peninsula higher than the French average even) not to mention it was the only county powerfull enough to successfully rebel and rise to Kingdom status. Not asking for much, just 4 baronies and 1 historically accurate county that did exist during the game's timeframe (and you can keep development as it is). View attachment 685379 Click to expand...
<!-- artifact:quote:end -->
I for one like your suggestion, but have you made it into a thread yet? You should; it will allow better discussion on the subject, and it won't go lost in the comment section of an unrelated dev diary

## Reply 131 — participant_094 · 2021-02-23 · post-27317114

<!-- artifact:quote:start -->
> Keizer Harm said: I for one like your suggestion, but have you made it into a thread yet? You should; it will allow better discussion on the subject, and it won't go lost in the comment section of an unrelated dev diary Click to expand...
<!-- artifact:quote:end -->
I was thinking I should wait untill i see if they actually get the winters right. It would be embarrassing if i made this thread and they turned out to have got them right in the first place.

## Reply 132 — participant_074 · 2021-02-23 · post-27317129

<!-- artifact:quote:start -->
> Bandua_of_Gallaecia said: I was thinking I should wait untill i see if they actually get the winters right. It would be embarrassing if i made this thread and they turned out to have got them right in the first place. Click to expand...
<!-- artifact:quote:end -->
It makes more sense to do it now IMO. Easier to get things right from the beginning than to have to go back and change them later. No need for embarrassment.

## Reply 133 — participant_094 · 2021-02-23 · post-27317138

<!-- artifact:quote:start -->
> Karlington said: It makes more sense to do it now IMO. Easier to get things right from the beginning than to have to go back and change them later. No need for embarrassment. Click to expand...
<!-- artifact:quote:end -->
Good point

## Reply 134 — participant_097 · 2021-02-23 · post-27317176

<!-- artifact:quote:start -->
> Servancour said: Greetings everyone! Don’t stand out there in the cold. Come on in and warm yourself by the fire! Have you made yourself comfortable? Excellent. Before we get to it, first things first. I know that all of you are eagerly awaiting more news regarding upcoming DLC content, but we’re not ready to start talking about those quite yet. Don’t fret, you will not have to wait that long. They say that patience is a virtue, but knowing better, I’ll leave this right here. For the next few weeks and the coming dev diaries we’ll talk a bit about what we have in store for the next major update, 1.3. In usual fashion, you can expect 1.3 to land alongside the upcoming DLC. Without further ado, let’s get to it shall we? Winter is Coming Winter is being introduced to CK3, making the already unforgiving world of the Middle Ages a much harsher place! As winter approaches, the map will gradually get covered in snow, clearly showing the extent of the freezing cold. The system itself is fairly flexible and allows for a great degree of control, as we can set which provinces should experience winter, and which shouldn’t. Winter won’t be limited to just the northernmost parts of the map, so expect snow to appear in places such as the Persian Mountains, or on the heights of the Tibetan plateau. View attachment 685202 With the introduction of winter comes new gameplay considerations. It wouldn’t be any point in adding this cool system if it didn’t do anything interesting. Winter comes in three different variants; mild, normal, and harsh. Mild and normal winters will be fairly common throughout central Europe and parts of southern Europe, while harsh winters are rarer but can still occur. If you find yourself lost in the frozen landscape of places such as Sápmi, Mongolia, or Himalaya, expect harsh winters to be the norm and plan accordingly! We wanted to make sure that it’s easy to see what level of winter is present in any given barony at a glance. The amount of snow increases with higher levels. Mild winters should generally be fairly easy to spot, with patches of green still clearly visible. In contrast, harsh winters mostly cover an entire province with snow. Certain areas might even have clouds with steady snowfall appearing for that extra level of detail! Depending on the severity of winter, your armies will start to lose supply over time. Harsh winter means you’ll lose more supply each month, making it a risky business to go above the supply limit for an extended period during the winter season. Harsh winters will also have armies suffer more fatal casualties during battles. Winter will also have an effect on your Men-at-Arms. Most noticeably, cavalry units will perform worse in normal and harsh winters. Heavy cavalry, in particular, will suffer some hefty penalties. I would advise against the use of heavy cavalry if you know you’ll be fighting battles in mountainous terrain during the winter season. On the other hand, some Men-at-Arms will get (sometimes quite significant) bonuses while fighting in winter. One such unit is the Tibetan culture unit, Mountaineers. Accustomed to the cold and the snow in the mountains, they can utilize it to their advantage in the form of a damage bonus whenever they participate in battles when winter is present. View attachment 685219 The system for setting winter bonuses (or penalties if you will) on Men-at-Arms works just like setting terrain bonuses, making it very friendly for any modders out there. While winter and snow might look and play nice, it wouldn’t be complete without a fitting soundscape. I’ll hand over to our sound designer Gustav to talk a bit about what he did to bring winter to life! A Sound Plan Winter for a Swede is like butter on toast, we love it! (brr… please be spring soon!) There are two areas where we have updated audio on the map. Holdings: Audio gets reflected with real-time updates to holdings. When winter spreads over your lands; or any lands for that matter, folks now go inside their homes, birds have migrated to more southern regions, and the animals are now in their stables or inside by the hearths, cozy! The way we achieve this is to link the shader that covers the region with snow and Ice to a real-time float parameter, that then talks to our Audio Middleware Engine Fmod. Awesome, but what does it actually do? It attenuates sound layers, controls effects such as equalizers and reverb, and reshapes the original sound that was there during summertime, and morphs it into wintertime. VFX: We also have snow storms appearing, for both mild and harsh winters. If you hear the sounds, be wary, your troops will most likely suffer some penalties in these areas. Tread carefully! The snowstorms are spawned on the map with the particle system, which allows us to be able to spatialize the sound effects ( position them in a 3D location X-Y-Z ) as the mild snowstorm morphs into the harsh storm, so do the sound effects. I’ll leave you with this; a snippet of what goes on under the hood inside Fmod during winter. Obligatory Map Update Anyone who has followed the history of CK2 or the DDs for CK3 will know that I do enjoy my maps, and I’ll try to get in smaller map updates or improvements whenever I can. Since release, we’ve identified a few general areas that we think can be improved upon. Some of these will be updated in 1.3. First up, Ireland. The baronies in Ireland were a bit too large, making the emerald island have a significantly less holding density than its neighbors, England and Scotland. The western half of Ireland in particular suffered from a few quite large baronies. To solve this issue, we’ve added a number of new baronies, along with a couple of new counties, that should improve the overall experience of playing in Ireland. View attachment 685220 While Italy hasn't suffered from larger baronies in the same vein as Ireland, the area didn’t quite feel up to par with many other regions within Europe. Especially in terms of overall holding count. Italy generally had a bit too few holdings per county, so we’ve added new baronies in various places throughout the peninsula, from the slopes of the Alps all the way down to Reggio Calabria. The southern half in particular got some much needed attention. In the new setup, you’ll find significantly less counties with only two baronies. To mention a few examples, you’ll find that the county of Veneto has Malamacco as a new barony, Agnone can be found in the county of Lanciano, and Lecce is now an actual holding in the county with the same name. Overall, this should make Italy more representative of its historical impact and more fun to play in. View attachment 685221 View attachment 685222 That’ll be it for today! I do have a few more map improvements in store for you, but those will have to wait. Until next time! Click to expand...
<!-- artifact:quote:end -->
Awesome I suggested weather effects like this a little while back I'm super exited to see it in game.

## Reply 135 — participant_098 · 2021-02-23 · post-27317202

Very happy to see seasons return! Didn't realize how much your brain needs those tiny changes in the background to prevent all the years from blending into each other as your character progresses until they were gone. The fact that they will have actual gameplay effects as well is a much welcome bonus

## Reply 136 — participant_099 · 2021-02-23 · post-27317296

<!-- artifact:quote:start -->
> Servancour said: Let's clarify that a bit. Winter won't have an impact on gameplay outside of warfare Click to expand...
<!-- artifact:quote:end -->
Well that is a shame. Would have been nice to see some frostbite on characters, amputations and increased chance to get cold related diseases when campaigning in cold provinces.

## Reply 137 — participant_082 · 2021-02-23 · post-27317391

<!-- artifact:quote:start -->
> DahndI said: Well that is a shame. Would have been nice to see some frostbite on characters, amputations and increased chance to get cold related diseases when campaigning in cold provinces. Click to expand...
<!-- artifact:quote:end -->
If one's at Peace in Winter, then the ones most likely to get Frostbite would be the serfs and peasants. Not the nobility who live in castles. Now I get that castles can be drafty, and they certainly aren't weatherized. But the people who lived there lived in far more comfortable circumstances than the common folk...

## Reply 138 — participant_100 · 2021-02-23 · post-27317426

Brace yourselves!

## Reply 139 — participant_091 · 2021-02-23 · post-27317428

<!-- artifact:quote:start -->
> vandevere said: If one's at Peace in Winter, then the ones most likely to get Frostbite would be the serfs and peasants. Not the nobility who live in castles. Now I get that castles can be drafty, and they certainly aren't weatherized. But the people who lived there lived in far more comfortable circumstances than the common folk... Click to expand...
<!-- artifact:quote:end -->
And could afford to have a fire in the main hall at all times...

## Reply 140 — participant_082 · 2021-02-23 · post-27317436

<!-- artifact:quote:start -->
> DreadLindwyrm said: And could afford to have a fire in the main hall at all times... Click to expand...
<!-- artifact:quote:end -->
Precisely! And since the lowest we can play are Counts, it's perfectly reasonable for us to not have to worry about things like frostbite when we are not at war...

## Reply 141 — participant_101 · 2021-02-23 · post-27317438

<!-- artifact:quote:start -->
> Servancour said: [...]Winter is Coming[...] Click to expand...
<!-- artifact:quote:end -->
IMO: The Good: - visual representation of winter on the map - improved soundscape - local province / barony overhaul The Bad: - winter having a significant impact on the supply situation of your armies: Historically there were specific campaign seasons, which usually excluded winter. Since this isn't modeled in the game, as a player you have no choice but to either suffer increased causalities during winter or to engage in even more tedious micromanagement of your armies. Warfare is already the worst system of CK3, all you are doing with this addition is to make it more annoying for human players.

## Reply 142 — participant_102 · 2021-02-23 · post-27317442

<!-- artifact:quote:start -->
> Servancour said: Let's clarify that a bit. Winter won't have an impact on gameplay outside of warfare. Winter mainly affect battles, by giving bonuses or penalties to MaAs, and increases the overall fatal casualties on both sides. Armies also loses supply over time (a modifier that increases with each winter severity, and is added on top of the normal penalty for being over the supply limit), along with a couple of other additions, such as an increased movement speed during winter if your commander has a corresponding commander trait. As far as I know, ironman games should continue to run fine with the new version. Again though, if you have a save you are very invested in, I recommend you to continue with the 1.2.2 branch to avoid any potential issues. Click to expand...
<!-- artifact:quote:end -->
Are the Winter effects moddable?

## Reply 143 — participant_002 · 2021-02-23 · post-27317443

<!-- artifact:quote:start -->
> KomodoWaran said: IMO: The Good: - visual representation of winter on the map - improved soundscape - local province / barony overhaul The Bad: - winter having a significant impact on the supply situation of your armies: Historically there were specific campaign seasons, which usually excluded winter. Since this isn't modeled in the game, as a player you have no choice but to either suffer increased causalities during winter or to engage in even more tedious micromanagement of your armies. Warfare is already the worst system of CK3, all you are doing with this addition is to make it more annoying for human players. Click to expand...
<!-- artifact:quote:end -->
If anything is to be lamented it's the poor AI who'll get frostbitten first thing in winter.

## Reply 144 — participant_066 · 2021-02-23 · post-27317474

<!-- artifact:quote:start -->
> Voy said: If anything is to be lamented it's the poor AI who'll get frostbitten first thing in winter. Click to expand...
<!-- artifact:quote:end -->
I wonder if the effect of this update will be that you should always invade Russia in the winter because the AI will do a worse job of avoiding attrition than the human.

## Reply 145 — participant_002 · 2021-02-24 · post-27317519

<!-- artifact:quote:start -->
> Tiax said: I wonder if the effect of this update will be that you should always invade Russia in the winter because the AI will do a worse job of avoiding attrition than the human. Click to expand...
<!-- artifact:quote:end -->
I'd bet that's the more effective tactic unless being in defensive territory brings with it a certain advantage in terms of supplies still to avoid the problem. One must also consider the allies.

## Reply 146 — participant_045 · 2021-02-24 · post-27317532

<!-- artifact:quote:start -->
> Tiax said: I wonder if the effect of this update will be that you should always invade Russia in the winter because the AI will do a worse job of avoiding attrition than the human. Click to expand...
<!-- artifact:quote:end -->
Put it this way, there's a reason EU4's attrition cap was lowered to 5% and extra attrition cap from winter was removed entirely

## Reply 147 — participant_103 · 2021-02-24 · post-27317547

<!-- artifact:quote:start -->
> Servancour said: ...along with a couple of other additions, such as an increased movement speed during winter if your commander has a corresponding commander trait. Click to expand...
<!-- artifact:quote:end -->
Is there a default penalty to movement speed in winter? Because it doesn't make sense to be able to move faster in winter compared to summer, even with a special trait. It does make sense to move faster in winter with a special trait compared to those who lack the trait, but only if everyone moves slower in winter by default.

## Reply 148 — participant_104 · 2021-02-24 · post-27317650

<!-- artifact:quote:start -->
> Slow Bathroom said: Gameplay-wise this sounds like something players will just ignore while Genghis Khan's stupid AI dies in Tibet. But visually it seems nice. Click to expand...
<!-- artifact:quote:end -->
Pretty much this. If you give the AI the option of stabbing themselves in the face with a rusty axe or ruling the world.... They will always choose the former. I'd never played a CK game before a friend suggested it and I've been having a lot of fun, but the completely brain dead AI makes the game pretty boring pretty quickly (so I end up restarting a lot, and messing around, which is fun but....) and adding winter seems like it's only going to make it worse. I'm just envisioning the AI declaring war in the dead of winter and not a single troop makes it to the enemy capitol. Are there any plans to make the AI.... not smart necessarily, but at least not face-palmingly stupid?

## Reply 149 — participant_082 · 2021-02-24 · post-27317657

<!-- artifact:quote:start -->
> StarkeBlade said: Pretty much this. If you give the AI the option of stabbing themselves in the face with a rusty axe or ruling the world.... They will always choose the former. I'd never played a CK game before a friend suggested it and I'm having a lot of fun, but the completely brain dead AI takes some of the fun out of it and adding winter seems like it's only going to make it worse. I'm just envisioning the AI declaring war in the dead of winter and not a single troop makes it to the enemy capitol. Are there any plans to make the AI.... not smart necessarily, but at least not face-palmingly stupid? Click to expand...
<!-- artifact:quote:end -->
Maybe the devs could use real history to program AI war behavior. Declare War in the Spring, and try to get it done by Fall. Either that, or make it possible to declare temporary truces during the Winter Months...

## Reply 150 — participant_091 · 2021-02-24 · post-27317659

<!-- artifact:quote:start -->
> LeonOfOddecca said: Is there a default penalty to movement speed in winter? Because it doesn't make sense to be able to move faster in winter compared to summer, even with a special trait. It does make sense to move faster in winter with a special trait compared to those who lack the trait, but only if everyone moves slower in winter by default. Click to expand...
<!-- artifact:quote:end -->
Skis and sleds compared to walking? I can move heavy objects better on a properly frozen surface than I can on a soft, slightly damp, summer dirt road.

## Reply 151 — participant_105 · 2021-02-24 · post-27317671

What I find funny is that I was already taking account for winter during my game-play sessions. So between the Months of December & February I would avoid starting any wars or starting any new constructions.

## Reply 152 — participant_094 · 2021-02-24 · post-27317675

<!-- artifact:quote:start -->
> LeonOfOddecca said: Because it doesn't make sense to be able to move faster in winter compared to summer, Click to expand...
<!-- artifact:quote:end -->
It makes sense in the Middle-East.

## Reply 153 — participant_104 · 2021-02-24 · post-27317684

<!-- artifact:quote:start -->
> vandevere said: Maybe the devs could use real history to program AI war behavior. Declare War in the Spring, and try to get it done by Fall. Either that, or make it possible to declare temporary truces during the Winter Months... Click to expand...
<!-- artifact:quote:end -->
That would be cool, except half the time the AI ends up in multi year wars even though it only has enough gold to support it's army for 18 months. Temporary truces might solve that though, either that or... encouraging the AI to finish wars quickly and not get into ones that are going to last years unless it has the resources to do so.

## Reply 154 — participant_106 · 2021-02-24 · post-27317712

<!-- artifact:quote:start -->
> Ares Enyalios said: I am bit sceptical about the consequences of a harsh weather because the game is not really made up for it. In games like Hearts of Iron you can plan for a winter campaign but in CK3 where battles could last weeks there is simply no way to avoid winter warfare. It's the same problem that makes it impossible to conquer England as William the Conquerer by Christmas 1066. The time flows to fast in comparison to the battles and the movement. Click to expand...
<!-- artifact:quote:end -->
I think the weather effect will make things slightly more interesting but probably won't really have a very significant impact on much of anything in terms of planning or execution. Personally, I wish that warfare was less drawn out in general so things like winter, the harvest, feudal obligations, etc could be introduced as part of your planning process when going to war.

## Reply 155 — participant_107 · 2021-02-24 · post-27317723

Cool. Yet, since you mention MAA... are there going to be MAA added for the two, IIRC, cultures that lack them: Assyrian and Alan? Alan, in particular, could reasonably use the all-Iranian Ayyar. (And change the Dravidian MAA to something... different while you're at it?)

## Reply 156 — participant_010 · 2021-02-24 · post-27317761

My biggest hope for 1.3 is, that they will remove the automatic alliance from a marriage and make it a nonagression pact at best. That way i wouldnt hesitate anymore to marry my dynasty members to kings and other landed people to increase my renown. I just dont want alliances most of the time to and be called to other wars or call them to mine. I want to achieve stuff myself And that way the HRE would not invade ireland with their whole army anymore because some counts daughter got a good marriage.

## Reply 157 — participant_108 · 2021-02-24 · post-27317845

Connacht with their capital in the right place! Looks like it'll be a great update.

## Reply 158 — participant_109 · 2021-02-24 · post-27317886

Looks wonderful for a first real patch. Can't wait to see the bug fixes.

## Reply 159 — participant_110 · 2021-02-24 · post-27317905

The A.I. can't catch a break

## Reply 160 — participant_111 · 2021-02-24 · post-27318096

This is pretty, I look forward to it. I think you guys did a great job at making the map look good, and this looks like it will only improve on that. Incidentally, I wouldn't mind a map mode that's just... terrain, with county/kingdom names depending on zoom level, and maybe the "selected land" border, and nothing else, not even political borders. Just to admire the landscape. The gameplay changes, to be completely honest, sound like they will mostly be as inconsequential as they were in CKII. At least, I know I barely interacted with the weather mechanic due to a mix of: More micro than I cared to bother with (or had time for, in the case of multiplayer) Not a huge impact if you ignored it, and perhaps brought a bit more troops than you otherwise would have needed (exception: invading defensive pagans) Time dilation makes warfare pacing not conducive to planning around yearly events, AKA "Welp, I got distracted watching a battle and it's December already, guess I lose a bunch of troops now" Of course the mechanics are a bit different this time around, and there's the MaA bonuses, so I'm interested to at least check it out with an open mind, in any case. EDIT: Also sounds pretty! Good job, Gustav, and thanks for the videos!

## Reply 161 — participant_112 · 2021-02-24 · post-27318103

I'm on the fence with this. Graphically pretty, and will add some immersion but concerned the AI will flounder. Surely, the programmers should be trying to add inventive solutions to aid the AI, not the other way round. They should take some advice from the EUIV camp. Winter attrition killed the AI.

## Reply 162 — participant_074 · 2021-02-24 · post-27318116

<!-- artifact:quote:start -->
> pdstanbridge said: Winter attrition killed the AI. Click to expand...
<!-- artifact:quote:end -->
The newest song from The Buggles.

## Reply 163 — participant_113 · 2021-02-24 · post-27318139

Would modders be able to use this same kind of framework to add other seasonal effects such as the monsoons? What about a more experimental kind of set up with universally very small MTTHs to simulate natural disasters like heat waves, flooding, hurricanes or large dust storms?

## Reply 164 — participant_114 · 2021-02-24 · post-27318146

<!-- artifact:quote:start -->
> Servancour said: Winter won't have an impact on gameplay outside of warfare Click to expand...
<!-- artifact:quote:end -->
sad! very sad. i think CK3 need futures from ROMe . where provinces have a food capacity and with winter food will be generated 50% less if you down below zero you harm from penalty development Like a -XX% per month so that it can go into the negative otherwise winter is just graphic and stress for AI cuz it cant handle supples

## Reply 165 — participant_019 · 2021-02-24 · post-27318187

I think it would be neat if as well as damage buffs/debuffs that you also got buffs or debuffs based for speed based on your culture. I think it would be make for much more interesting winter battles if you had two nations fighting who could handle different levels of mobility during the snow.

## Reply 166 — participant_115 · 2021-02-24 · post-27318249

With wars spanning years and the AI not really altering their plans because of winter. Whilst this is a nice feature I dont see how it will alter many aspects of how you will wage war. Nice roleplay addition though. If there were trade goods like fur etc. then I could see how this could play a part i.e. making sure your troops had relevant equipment for fighting in colder climes etc.

## Reply 167 — participant_116 · 2021-02-24 · post-27318358

<!-- artifact:quote:start -->
> Servancour said: you’ll find that the county of Veneto has Malamacco as a new barony Click to expand...
<!-- artifact:quote:end -->
I guess you mean Malamocco! (Great DD btw)

## Reply 168 — participant_117 · 2021-02-24 · post-27318495

Nice! I really missed the dynamic seasons in Ck3. It's awesome that you bring them back so soon!

## Reply 169 — participant_118 · 2021-02-24 · post-27318503

I'm wondering how this will change war. Sometimes movement of armies can take half a year. I'm really excited for this and was just thinking how interesting this could be gameplay wise, but now that it's a thing... I'm just currious how it will all work!

## Reply 170 — participant_119 · 2021-02-24 · post-27318518

I really love it! Great work! My personal opinion: I wish thr battle modifiers were harsher. Worde attrition overall, better bonus to for example Tibetan mountainers etc. But thats just me. Anyway, great work cant wait!

## Reply 171 — participant_120 · 2021-02-24 · post-27318554

<!-- artifact:quote:start -->
> Pied-Noir said: @Servancour With your Irish map update it would be great if you could also finally split Strathclyde off from Galloway, rather than using the same duchy to represent both entities. They were totally separate, and represented different culture groups. It's like using the same title to represent Normandy and Brittany, which would - quite rightly - look absurd. I just find it very irritating because it's a very simple thing to fix - Galloway should be de jure Galloway and Carrick, and the rest can be Strathclyde. Both should exist in 867, and only Galloway should exist in 1066. Strathclyde collapsed in 1054. It should look something like this: View attachment 685372 Galloway should be ruled by the Cumbric kings of Galwyddel in 867 and the Gaelic lords of Galloway in 1066. Strathclyde should be ruled by the Cumbric kings of Alt Clut in 867 and not exist in 1066. Both should exist as de jure duchies however. This really isn't much work to do, but would make Scotland much better. Looking forward to the patch and DLC. Click to expand...
<!-- artifact:quote:end -->
I really enjoyed the Dev Diary, lots to look forward to it seems!! Further to these point above, one very small thing in Scotland really bugs me and that is the fact that the Barony of Arran isn't located on Arran on the map, tiny detail but extremely annoying

## Reply 172 — participant_002 · 2021-02-24 · post-27318559

<!-- artifact:quote:start -->
> the_atm said: I'm wondering how this will change war. Sometimes movement of armies can take half a year. I'm really excited for this and was just thinking how interesting this could be gameplay wise, but now that it's a thing... I'm just currious how it will all work! Click to expand...
<!-- artifact:quote:end -->
I'd be prepared for some AI dancing around harsh winter regions, just in case.

## Reply 173 — participant_089 · 2021-02-24 · post-27318570

<!-- artifact:quote:start -->
> mwa11ace said: I really enjoyed the Dev Diary, lots to look forward to it seems!! Further to these point above, one very small thing in Scotland really bugs me and that is the fact that the Barony of Arran isn't located on Arran on the map, tiny detail but extremely annoying Click to expand...
<!-- artifact:quote:end -->
If we're getting into non-existent medieval baronies: Mar, in Angus (Scotland) and Cornouailles, in Cornouaille (Brittany) are not actual places. They're just baronies which have been given the name of a county. I'm not sure about Mar, but Cornouaille could be replaced with Carhaix (known as Karaez in Breton). This is an actual medieval town in the same barony as Cornouailles currently is. Currently it's like having a barony called 'Yorkshire' - it's obviously a place, but it isn't an actual settlement.

## Reply 174 — participant_120 · 2021-02-24 · post-27318591

<!-- artifact:quote:start -->
> Pied-Noir said: If we're getting into non-existent medieval baronies: Mar, in Angus (Scotland) and Cornouailles, in Cornouaille (Brittany) are not actual places. They're just baronies which have been given the name of a county. I'm not sure about Mar, but Cornouaille could be replaced with Carhaix (known as Karaez in Breton). This is an actual medieval town in the same barony as Cornouailles currently is. Currently it's like having a barony called 'Yorkshire' - it's obviously a place, but it isn't an actual settlement. Click to expand...
<!-- artifact:quote:end -->
I agree however if we are going to have non-existent medieval Baronies named after islands at least put it on the island its named after

## Reply 175 — participant_121 · 2021-02-24 · post-27318796

Oh no, supply management again Would we have game rule when we can set only mild winters or set harsh winters to super rare? Thanks for the map update especially Italy. <3

## Reply 176 — participant_121 · 2021-02-24 · post-27318806

<!-- artifact:quote:start -->
> Scanz said: sad! very sad. i think CK3 need futures from ROMe . where provinces have a food capacity and with winter food will be generated 50% less if you down below zero you harm from penalty development Like a -XX% per month so that it can go into the negative otherwise winter is just graphic and stress for AI cuz it cant handle supples Click to expand...
<!-- artifact:quote:end -->
They said this game isnt about the war only, but mostly it is. If you don't do wars, it becomes boring. I hope they will focus the game more on economy, culture, more rpg elements, more events, buildings, court etc...

## Reply 177 — participant_119 · 2021-02-24 · post-27318813

<!-- artifact:quote:start -->
> johnnybgood89 said: Oh no, supply management again Would we have game rule when we can set only mild winters or set harsh winters to super rare? Thanks for the map update especially Italy. <3 Click to expand...
<!-- artifact:quote:end -->
Hmm maybe an option is good as you want less and I want more. Maybe a mild, normal and harsh modifier rule at game setup?

## Reply 178 — participant_121 · 2021-02-24 · post-27318823

<!-- artifact:quote:start -->
> Axis89 said: Hmm maybe an option is good as you want less and I want more. Maybe a mild, normal and harsh modifier rule at game setup? Click to expand...
<!-- artifact:quote:end -->
Sounds good.

## Reply 179 — participant_082 · 2021-02-24 · post-27318925

<!-- artifact:quote:start -->
> StarkeBlade said: That would be cool, except half the time the AI ends up in multi year wars even though it only has enough gold to support it's army for 18 months. Temporary truces might solve that though, either that or... encouraging the AI to finish wars quickly and not get into ones that are going to last years unless it has the resources to do so. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> johnnybgood89 said: They said this game isnt about the war only, but mostly it is. If you don't do wars, it becomes boring. I hope they will focus the game more on economy, culture, more rpg elements, more events, buildings, court etc... Click to expand...
<!-- artifact:quote:end -->
I don't really go to war all that often, and I'm not bored...

## Reply 180 — participant_091 · 2021-02-24 · post-27318956

<!-- artifact:quote:start -->
> vandevere said: I don't really go to war all that often, and I'm not bored... Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> johnnybgood89 said: They said this game isnt about the war only, but mostly it is. If you don't do wars, it becomes boring. I hope they will focus the game more on economy, culture, more rpg elements, more events, buildings, court etc... Click to expand...
<!-- artifact:quote:end -->
My Islamic Hispania game has hit a consolidation phase, and it's not boring. It *is* suffering from pre-emptively handling revolts, and trying to build up the (now stabilised) core domain, but boring it is not. I'm also adjusting my vassal structure everytime someone does something stupid, so that's got some interest in it, and I've still got a *big* religious adjustment to do after my last large war. More RPG elements and more events doesn't necessarily help, because you learn what to do with them, and they essentially become less interesting. More building isn't interesting at all, because it's not actually that interactive in most cases - you click on the province, build the thing, and that's it. Maybe you click on the next province over and also build the thing.

## Reply 181 — participant_019 · 2021-02-24 · post-27318979

<!-- artifact:quote:start -->
> DreadLindwyrm said: More RPG elements and more events doesn't necessarily help, because you learn what to do with them, and they essentially become less interesting. More building isn't interesting at all, because it's not actually that interactive in most cases - you click on the province, build the thing, and that's it. Maybe you click on the next province over and also build the thing. Click to expand...
<!-- artifact:quote:end -->
I do feel they have managed to work around the issues with the RPG elements using stress which encourages you to roleplay more than just going for best outcome. That said, I think the stress system could be even stricter than it is now.

## Reply 182 — participant_122 · 2021-02-24 · post-27319116

<!-- artifact:quote:start -->
> Niall9 said: I do feel they have managed to work around the issues with the RPG elements using stress which encourages you to roleplay more than just going for best outcome. That said, I think the stress system could be even stricter than it is now. Click to expand...
<!-- artifact:quote:end -->
If def. needs to be better. You can simply game the stress system out, by not hunting/feasting/etc until you need to lower stress. The stress system is kinda dumb imo, but I guess they couldn't think of anything better.

## Reply 183 — participant_123 · 2021-02-24 · post-27319162

*(no text body — reaction-only or media-only post)*

## Reply 184 — participant_124 · 2021-02-24 · post-27319226

Scrubbed some of the last 24 hours clean. I'm not asking too much here: Be polite Don't insult anyone

## Reply 185 — participant_080 · 2021-02-24 · post-27319306

<!-- artifact:quote:start -->
> Adam363 said: If def. needs to be better. You can simply game the stress system out, by not hunting/feasting/etc until you need to lower stress. The stress system is kinda dumb imo, but I guess they couldn't think of anything better. Click to expand...
<!-- artifact:quote:end -->
This is assuming that you are not lazy (for hunting) or shy (for feasting). This also means that you are losing out on the other benefits of those activities.

## Reply 186 — participant_091 · 2021-02-24 · post-27319326

<!-- artifact:quote:start -->
> Adam363 said: If def. needs to be better. You can simply game the stress system out, by not hunting/feasting/etc until you need to lower stress. The stress system is kinda dumb imo, but I guess they couldn't think of anything better. Click to expand...
<!-- artifact:quote:end -->
Your point assumes you don't have any stress multipliers that cause you to go from "minimal" stress to being overloaded with stress *really* quickly - and that you don't get hit with mutliple stress events in quick succession. It assumes that you don't have your stress result in something like "change religion, go whoring (and catch diseases), or gain an entire extra level of stress" and not recover enough stress from the available recovery methods. It's *far* better than them not having anything in place like in CK2.

## Reply 187 — participant_122 · 2021-02-24 · post-27319353

<!-- artifact:quote:start -->
> DreadLindwyrm said: Your point assumes you don't have any stress multipliers that cause you to go from "minimal" stress to being overloaded with stress *really* quickly - and that you don't get hit with mutliple stress events in quick succession. It assumes that you don't have your stress result in something like "change religion, go whoring (and catch diseases), or gain an entire extra level of stress" and not recover enough stress from the available recovery methods. It's *far* better than them not having anything in place like in CK2. Click to expand...
<!-- artifact:quote:end -->
It doesn't matter. At all. I've played hundreds of hours of CK3 and my level of concern about stress over that period of time was 0. It doesn't matter and its easy to mitigate.

## Reply 188 — participant_091 · 2021-02-24 · post-27319369

<!-- artifact:quote:start -->
> Adam363 said: It doesn't matter. At all. I've played hundreds of hours of CK3 and my level of concern about stress over that period of time was 0. It doesn't matter and its easy to mitigate. Click to expand...
<!-- artifact:quote:end -->
I've also played hundreds of hours, and it has, sometimes, been a major factor. It's killed characters I've been playing, and it's forced me into having choices between three bad options. Mitigation is possible, but not *always* easy.

## Reply 189 — participant_122 · 2021-02-24 · post-27319372

<!-- artifact:quote:start -->
> DreadLindwyrm said: I've also played hundreds of hours, and it has, sometimes, been a major factor. It's killed characters I've been playing, and it's forced me into having choices between three bad options. Mitigation is possible, but not *always* easy. Click to expand...
<!-- artifact:quote:end -->
How can you say its not easy? Its literally the easiest thing to do. And most of the time, if you know what your doing, the game provides you with tons of ways to reduce stress outside of hunting/feasting. There is the athletics, riding, journaling, etc etc. You are exaggerating the magnitude of stress, and its OBVIOUS to anyone who has put substantial time into the game. We both know, it doesn't matter and its easy to mitigate.

## Reply 190 — participant_082 · 2021-02-24 · post-27319397

I've had Rulers start their reigns, literally Day One of their reign with 92 Stress. How the hell do you mitigate that before the Game throws you a curveball that overwhelms you? Feasts and Hunts don't mitigate that quickly enough to help much. Especially if the Game decides to throw you a curveball...

## Reply 191 — participant_091 · 2021-02-24 · post-27319445

<!-- artifact:quote:start -->
> Adam363 said: How can you say its not easy? Its literally the easiest thing to do. And most of the time, if you know what your doing, the game provides you with tons of ways to reduce stress outside of hunting/feasting. There is the athletics, riding, journaling, etc etc. You are exaggerating the magnitude of stress, and its OBVIOUS to anyone who has put substantial time into the game. We both know, it doesn't matter and its easy to mitigate. Click to expand...
<!-- artifact:quote:end -->
Shy characters who essentially get *nothing* from feasts. Lazy characters who essentially get *nothing* from hunting. Characters who are not rich enough to pay for the hunts and feasts because they *have* to spend that money elsewhere (say in defensive wars). Getting large stress gains whilst feasts and hunting are on cool down. Especially where this is due to dynastic relatives, friends, and lovers (sometimes all the same person) dying. I had one sequence of deaths (including other relatives dying of stress) cause me to gain 3 levels of stress in a few months. Athletics, riding, journalling, and confidants are locked behind RNG. They're not guaranteed to come up at all for any given character. You can equally get heavy drinking or whoring - both of which are risky to your life and health. As a result, these can't really be put under "if you know what you're doing", since you aren't guaranteed to have *any* of them even after stress has hit a couple of times. They're also on a cool down, so if you get hit with enough stress over a short enough period, these don't help either. *And* the amount you lose from them isn't always sufficient to bring you back to a safe number. I've had my three choices on stress being "convert to a religion hostile to *everyone* in the region", "gain a stress relieving trait that causes me to be wounded if I use it, with that level of wounding increasing if I'm already wounded", or "gain another 60 stress". You can also outright die, murder your heir, or be forced to abdicate. You can gain some really bad traits.

## Reply 192 — participant_125 · 2021-02-24 · post-27319479

I was contemplating buying the Royal Edition, but I thought "hey, what is the chance that the first expansion will bring improvement to northernmost Europe of all places? What are the chances that one of those flavour packs will cover Sapmi and/or Finland?" Figuring those chances would be slim, I decided to go for the standard edition instead. Obviously it's still unclear what the expansion and the flavour packs will be about, but seeing this makes me a tad worried I made the "wrong" choice (my wallet doesn't blame me though). There's also another thing I keep bringing up when it comes to speculation; is there any cross-game thematicism when it comes to development at Paradox? It's pretty likely HoI4 will get some Winter War flavour, but will we be seeing more snow beyond that ?

## Reply 193 — participant_085 · 2021-02-24 · post-27319509

<!-- artifact:quote:start -->
> StarkeBlade said: That would be cool, except half the time the AI ends up in multi year wars even though it only has enough gold to support it's army for 18 months. Temporary truces might solve that though, either that or... encouraging the AI to finish wars quickly and not get into ones that are going to last years unless it has the resources to do so. Click to expand...
<!-- artifact:quote:end -->
Personally I think holding war goals and battles should be worth more warscore. That would do a lot to shorten wars and make small border skirmishes not turn into total war. Now doing so would also have the bonus of helping the AI avoid fighting in the winter.

## Reply 194 — participant_002 · 2021-02-24 · post-27319807

<!-- artifact:quote:start -->
> Krey_Lollipop said: I was contemplating buying the Royal Edition, but I thought "hey, what is the chance that the first expansion will bring improvement to northernmost Europe of all places? What are the chances that one of those flavour packs will cover Sapmi and/or Finland?" Figuring those chances would be slim, I decided to go for the standard edition instead. Obviously it's still unclear what the expansion and the flavour packs will be about, but seeing this makes me a tad worried I made the "wrong" choice (my wallet doesn't blame me though). There's also another thing I keep bringing up when it comes to speculation; is there any cross-game thematicism when it comes to development at Paradox? It's pretty likely HoI4 will get some Winter War flavour, but will we be seeing more snow beyond that ? Click to expand...
<!-- artifact:quote:end -->
I feel like you would have saved money by just buying the royal edition, it's a tidy lil discount on the DLC. We all know that the completionist force within each and every one of us is too strong to oppose in the end. I share your enthusiasm for the Sapmi, especially after seeing the expanded area they have been given in CK3, but I also do not know if there would be enough content to be created to justify an entire "flavor pack" for only them. Let's be honest, the region is basically worthless even if you're a semi-nomadic reindeer hustling kindred group and any resemblance of power and martial influence over the neighbours would have been a straight-up fantasy in the making, especially since they weren't terribly dynastic or many. Regardless, it would have been nice to have them be some sort of trade incentive in furs and so would have a more passive influence on its neighbours. EDIT: Suddenly I'm very inspired to make a mod for the Sapmi...

## Reply 195 — participant_103 · 2021-02-24 · post-27319908

<!-- artifact:quote:start -->
> DreadLindwyrm said: Skis and sleds compared to walking? I can move heavy objects better on a properly frozen surface than I can on a soft, slightly damp, summer dirt road. Click to expand...
<!-- artifact:quote:end -->
So you're imagining an entire army moving through several provinces on skis and sleds? I wasn't suggesting that nothing can move faster in winter than in summer. I was taking it for granted that we're talking about an army full of men, horses, wagons, etc.

## Reply 196 — participant_091 · 2021-02-25 · post-27320029

<!-- artifact:quote:start -->
> LeonOfOddecca said: So you're imagining an entire army moving through several provinces on skis and sleds? I wasn't suggesting that nothing can move faster in winter than in summer. I was taking it for granted that we're talking about an army full of men, horses, wagons, etc. Click to expand...
<!-- artifact:quote:end -->
And the wagons are the main thing slowing you down. Putting them on sleds (even temporarily strapping runners to them( and going over frozen terrain can be faster (sometimes *much* faster) than on soft summer ground.

## Reply 197 — participant_086 · 2021-02-25 · post-27320062

<!-- artifact:quote:start -->
> Adam363 said: It doesn't matter. At all. I've played hundreds of hours of CK3 and my level of concern about stress over that period of time was 0. It doesn't matter and its easy to mitigate. Click to expand...
<!-- artifact:quote:end -->
Most of the time it was like this.. until I got a shy character.

## Reply 198 — participant_111 · 2021-02-25 · post-27320358

<!-- artifact:quote:start -->
> Jarolleon said: Most of the time it was like this.. until I got a shy character. Click to expand...
<!-- artifact:quote:end -->
Yep shy is rough. Wait til you get a shy and paranoid character, it's brutal. I really like that a large part of the traits' values are actually tied to what event options they incentivize you to pick. There is way more of a push to act like your character actually would than there was in CKII.

## Reply 199 — participant_126 · 2021-02-25 · post-27320906

Wasn’t that already in ckII ?? (Im talking about winter)

## Reply 200 — participant_103 · 2021-02-25 · post-27321061

<!-- artifact:quote:start -->
> DreadLindwyrm said: And the wagons are the main thing slowing you down. Putting them on sleds (even temporarily strapping runners to them( and going over frozen terrain can be faster (sometimes *much* faster) than on soft summer ground. Click to expand...
<!-- artifact:quote:end -->
Do you know of any instance in history which confirms this?

## Reply 201 — participant_045 · 2021-02-25 · post-27321131

<!-- artifact:quote:start -->
> Voy said: We all know that the completionist force within each and every one of us is too strong to oppose in the end. Click to expand...
<!-- artifact:quote:end -->
i still haven't bought Mare Nostrum

## Reply 202 — participant_125 · 2021-02-25 · post-27321133

<!-- artifact:quote:start -->
> Voy said: I feel like you would have saved money by just buying the royal edition, it's a tidy lil discount on the DLC. We all know that the completionist force within each and every one of us is too strong to oppose in the end. I share your enthusiasm for the Sapmi, especially after seeing the expanded area they have been given in CK3, but I also do not know if there would be enough content to be created to justify an entire "flavor pack" for only them. Let's be honest, the region is basically worthless even if you're a semi-nomadic reindeer hustling kindred group and any resemblance of power and martial influence over the neighbours would have been a straight-up fantasy in the making, especially since they weren't terribly dynastic or many. Regardless, it would have been nice to have them be some sort of trade incentive in furs and so would have a more passive influence on its neighbours. EDIT: Suddenly I'm very inspired to make a mod for the Sapmi... Click to expand...
<!-- artifact:quote:end -->
No kidding, the completionist force is crazy. That said, I haven't really gotten into CK yet, really the main reasons I own CK3 at all is a) said force, b) customization and c) being able to play in Sapmi/Finland without any trickery (Finland is pretty limited in HoI4, especially the good half). So unless one of the DLCs covers the north I'm not exactly dying to get it. Better then to wait for a sale. I also just remembered one of my first and only CK2 games. Played as THE local Sami ruler (I only think there was one, local to me that is). Started off as a vassal and a year later my character died without an heir. I might have been unlucky, but CK3 sure improves the playability in the region. I especially love the long and narrow mountain passes which really give the area a distinct look. What I can say about a flavor pack is that it could be bundled with say the vikings. They're popular and having fancy vikings but vanilla neighbours/subjects (or vice-versa) would probably ruin the immersion for some. There could also be some fun alt-history potentials here, like how there are sources claiming some Sami participated in the settlement of Iceland. I don't know how that works in CK3 at the moment, but considering what Iceland looks like on the CK3 map I don't expect it to be much to brag about. But even under the assumption that Sapmi/Finland would be bundled with some of their more popular neighbours, I found it to be too much of a bet still. Vikings do seem like likely candidates for DLC, but there are so many other possibilites and I didn't wanna risk paying 25€ extra for some fancy Italians or whatever. Fun if you're playing as them, but I haven't gotten there yet.

## Reply 203 — participant_086 · 2021-02-25 · post-27321487

<!-- artifact:quote:start -->
> DaviBones said: Yep shy is rough. Wait til you get a shy and paranoid character, it's brutal. I really like that a large part of the traits' values are actually tied to what event options they incentivize you to pick. There is way more of a push to act like your character actually would than there was in CKII. Click to expand...
<!-- artifact:quote:end -->
Meanwhile the stats you get from them are rather superfluous once you capture the House of Wisdom & University of Pataliputra and get some lifestyle traits.

## Reply 204 — participant_127 · 2021-02-25 · post-27321687

Question to the developers: Since you add winter to the game here is a big question: Around the very late 13th century and the beginning of the 14th century (somewhat ~1275 until about ~1875) we entered something called the Little Ice Age. The biggest effect to the period of the middle ages was when warm summers stopped being dependable in Northern Europe starting 1300, as well as winters being longer and colder in average. That lead to much less agriculture output. Is this something you planning to simulate with the new winter game mechanics by having average colder and longer winters starting around the year 1300? This definably would add to historical realism. It also would make the late game a little bit more challenging since it is by far too easy as of right now.

## Reply 205 — participant_128 · 2021-02-25 · post-27321775

Certain types of cavalry, notably steppe nomad, do very well in harsh winters. The Mongols moved faster in winter than in summer.

## Reply 206 — participant_129 · 2021-02-25 · post-27321923

Mountaineers? In MY HOI4 CK3?

## Reply 207 — participant_130 · 2021-02-25 · post-27322395

Very nice, didn't expect this at all. Would love to see similar features implemented for monsoons in India, maybe the Harmattan in West Africa. Hey, maybe a whole climate map mode where you can see the regional variations and special buildings are available for appropriate cultures in their borders. Special monsoon wind trading posts in India and the Horn of Africa, spring fairgrounds buildings in Europe that give a boost to income, prestige, and/or province satisfaction that depends on how harsh the prior winter was. Seasonal fertility/harvest festivals for pagan cultures, Christians/Muslims can ban them as heresy or syncretize the festivals for greater province satisfaction and decreased risk of rebellion but also decreased conversion time, maybe with the chance of spawning dynamic syncretic folk religions that are harder to convert to the true faith without more brutality? Which reminds me, I'd love more features relating to the peasantry and common tribals, making them feel dynamic and alive. Of course the dynasties are the draw of the game, but they need to have subjects! But I could go all day, excited for this, looks very neat.

## Reply 208 — participant_091 · 2021-02-26 · post-27322574

<!-- artifact:quote:start -->
> LeonOfOddecca said: Do you know of any instance in history which confirms this? Click to expand...
<!-- artifact:quote:end -->
I can't specifically quote anything that would show a military use, but then I'm not a student of warfare in the far and frozen north, and couldn't point to a specific organised army fighting in winter that would have benefited from it. I have however had to move heavy loads over frozen ground myself, and it was easier than in the summer with damp, soft ground where the wheels sink and get bogged down.

## Reply 209 — participant_131 · 2021-02-26 · post-27322578

They didn't call summer "campaigning season" for nothing

## Reply 210 — participant_132 · 2021-02-26 · post-27322742

I was actually just about to suggest they add this. I heartily approve; should make long campaigns a bit more strategic, since you'd now have to find winter quarters for your army before it gets too cold.

## Reply 211 — participant_133 · 2021-02-26 · post-27323472

Is anyone else not getting the Dev Diaries displaying on the forum home screen? Normally they appear on the front page but I had to come directly to the CKIII forum page to find it.

## Reply 212 — participant_134 · 2021-02-27 · post-27325893

I feel like a few flavor events related to winter could possibly be cool

## Reply 213 — participant_135 · 2021-02-27 · post-27326157

<!-- artifact:quote:start -->
> LeonOfOddecca said: Do you know of any instance in history which confirms this? Click to expand...
<!-- artifact:quote:end -->
I don't know about summer ground being an issue and winter would certainly bog down wagons unless the ground is very hard. Maybe they were using skis on the wagons back then, but I don't really know. One thing, however, is that spring time is often the worst time for moving heavy wagons because of the rain causing a lot of mud. There's a good reason why the Romans were so into building roads. It gave them the ability to move their troops very quickly (comparatively) from place to place without the issues caused by muddy dirt paths, not to mention having a wider path than you'd generally have or no path at all. For heavy wagons-- Spring = Really bad time due to sinking into mud, except during drought years Summer = Generally a good time unless you live in an area that is very wet in the summer and then it may be similar to Spring Fall = Generally a good time Winter = Not a good time unless they used skis (not sure if they did) or if the snow is not deep or is frozen over well enough not to break through and sink and there is the benefit of crossing frozen water (rivers, lakes, etc.) more easily in the winter Of course, some armies used heavy wagons less often (I don't think Mongols used them too much) and so the seasonal effects would be less for them. Light cavalry can often move fairly easily through muddy and snowy land as long as they don't sink too badly compared to other troops. Light infantry can often move more easily as long as the snow isn't too deep and can more easily move around the worst muddy areas to avoid being slowed down than the supply carts. Heavy infantry and cavalry are going to usually be in a similar situation as heavy wagons. This is just in general and may not always be true and may not affect certain cultures as much due to how they waged war. But I believe much of European warfare used the heavy wagon supply lines that would cause problems whenever you have bad road conditions.

## Reply 214 — participant_045 · 2021-02-27 · post-27326179

<!-- artifact:quote:start -->
> Riamus said: Fall = Generally a good time Click to expand...
<!-- artifact:quote:end -->
Depends strongly on the local climate and geology. Famously, western Russia, Belarus, and Ukraine have mud season twice a year – first from the spring thaw, and then from autumn rainfall.

## Reply 215 — participant_136 · 2021-02-27 · post-27326514

The rate of improvement on this game is almost... glacial *rimshot*

## Reply 216 — participant_135 · 2021-02-28 · post-27327449

<!-- artifact:quote:start -->
> grommile said: Depends strongly on the local climate and geology. Famously, western Russia, Belarus, and Ukraine have mud season twice a year – first from the spring thaw, and then from autumn rainfall. Click to expand...
<!-- artifact:quote:end -->
Good point. Fall can certainly be a wet season in certain parts of CK's map and it's may also be true that some areas don't normally experience wet springs. So to clarify Spring and Fall... These are either going to be good times or bad times depending on whether or not the season is wet or dry.

## Reply 217 — participant_137 · 2021-02-28 · post-27327932

I think it would be rather good to have some rivers become non-navigable in harsh winter, keeping the vikings to the coast for a short while.

## Reply 218 — participant_138 · 2021-03-01 · post-27329624

<!-- artifact:quote:start -->
> Servancour said: Greetings everyone! Don’t stand out there in the cold. Come on in and warm yourself by the fire! Have you made yourself comfortable? Excellent. Before we get to it, first things first. I know that all of you are eagerly awaiting more news regarding upcoming DLC content, but we’re not ready to start talking about those quite yet. Don’t fret, you will not have to wait that long. They say that patience is a virtue, but knowing better, I’ll leave this right here. For the next few weeks and the coming dev diaries we’ll talk a bit about what we have in store for the next major update, 1.3. In usual fashion, you can expect 1.3 to land alongside the upcoming DLC. Without further ado, let’s get to it shall we? Winter is Coming Winter is being introduced to CK3, making the already unforgiving world of the Middle Ages a much harsher place! As winter approaches, the map will gradually get covered in snow, clearly showing the extent of the freezing cold. The system itself is fairly flexible and allows for a great degree of control, as we can set which provinces should experience winter, and which shouldn’t. Winter won’t be limited to just the northernmost parts of the map, so expect snow to appear in places such as the Persian Mountains, or on the heights of the Tibetan plateau. View attachment 685202 With the introduction of winter comes new gameplay considerations. It wouldn’t be any point in adding this cool system if it didn’t do anything interesting. Winter comes in three different variants; mild, normal, and harsh. Mild and normal winters will be fairly common throughout central Europe and parts of southern Europe, while harsh winters are rarer but can still occur. If you find yourself lost in the frozen landscape of places such as Sápmi, Mongolia, or Himalaya, expect harsh winters to be the norm and plan accordingly! We wanted to make sure that it’s easy to see what level of winter is present in any given barony at a glance. The amount of snow increases with higher levels. Mild winters should generally be fairly easy to spot, with patches of green still clearly visible. In contrast, harsh winters mostly cover an entire province with snow. Certain areas might even have clouds with steady snowfall appearing for that extra level of detail! Depending on the severity of winter, your armies will start to lose supply over time. Harsh winter means you’ll lose more supply each month, making it a risky business to go above the supply limit for an extended period during the winter season. Harsh winters will also have armies suffer more fatal casualties during battles. Winter will also have an effect on your Men-at-Arms. Most noticeably, cavalry units will perform worse in normal and harsh winters. Heavy cavalry, in particular, will suffer some hefty penalties. I would advise against the use of heavy cavalry if you know you’ll be fighting battles in mountainous terrain during the winter season. On the other hand, some Men-at-Arms will get (sometimes quite significant) bonuses while fighting in winter. One such unit is the Tibetan culture unit, Mountaineers. Accustomed to the cold and the snow in the mountains, they can utilize it to their advantage in the form of a damage bonus whenever they participate in battles when winter is present. View attachment 685219 The system for setting winter bonuses (or penalties if you will) on Men-at-Arms works just like setting terrain bonuses, making it very friendly for any modders out there. While winter and snow might look and play nice, it wouldn’t be complete without a fitting soundscape. I’ll hand over to our sound designer Gustav to talk a bit about what he did to bring winter to life! A Sound Plan Winter for a Swede is like butter on toast, we love it! (brr… please be spring soon!) There are two areas where we have updated audio on the map. Holdings: Audio gets reflected with real-time updates to holdings. When winter spreads over your lands; or any lands for that matter, folks now go inside their homes, birds have migrated to more southern regions, and the animals are now in their stables or inside by the hearths, cozy! The way we achieve this is to link the shader that covers the region with snow and Ice to a real-time float parameter, that then talks to our Audio Middleware Engine Fmod. Awesome, but what does it actually do? It attenuates sound layers, controls effects such as equalizers and reverb, and reshapes the original sound that was there during summertime, and morphs it into wintertime. VFX: We also have snow storms appearing, for both mild and harsh winters. If you hear the sounds, be wary, your troops will most likely suffer some penalties in these areas. Tread carefully! The snowstorms are spawned on the map with the particle system, which allows us to be able to spatialize the sound effects ( position them in a 3D location X-Y-Z ) as the mild snowstorm morphs into the harsh storm, so do the sound effects. I’ll leave you with this; a snippet of what goes on under the hood inside Fmod during winter. Obligatory Map Update Anyone who has followed the history of CK2 or the DDs for CK3 will know that I do enjoy my maps, and I’ll try to get in smaller map updates or improvements whenever I can. Since release, we’ve identified a few general areas that we think can be improved upon. Some of these will be updated in 1.3. First up, Ireland. The baronies in Ireland were a bit too large, making the emerald island have a significantly less holding density than its neighbors, England and Scotland. The western half of Ireland in particular suffered from a few quite large baronies. To solve this issue, we’ve added a number of new baronies, along with a couple of new counties, that should improve the overall experience of playing in Ireland. View attachment 685220 While Italy hasn't suffered from larger baronies in the same vein as Ireland, the area didn’t quite feel up to par with many other regions within Europe. Especially in terms of overall holding count. Italy generally had a bit too few holdings per county, so we’ve added new baronies in various places throughout the peninsula, from the slopes of the Alps all the way down to Reggio Calabria. The southern half in particular got some much needed attention. In the new setup, you’ll find significantly less counties with only two baronies. To mention a few examples, you’ll find that the county of Veneto has Malamacco as a new barony, Agnone can be found in the county of Lanciano, and Lecce is now an actual holding in the county with the same name. Overall, this should make Italy more representative of its historical impact and more fun to play in. View attachment 685221 View attachment 685222 That’ll be it for today! I do have a few more map improvements in store for you, but those will have to wait. Until next time! Click to expand...
<!-- artifact:quote:end -->
Thank you for the dev diary that we have been asking for! Love the extra dynamism that is being added to the map and map changes are always fun to see. Ireland did feel a tad empty, so I am happy it got some more meat to it

## Reply 219 — participant_138 · 2021-03-01 · post-27329632

<!-- artifact:quote:start -->
> Servancour said: It's not possible to have winter appear at two different times. Other than that, winter should be fairly moddable. You can set exactly which provinces have winter, and how likely they are to get the different severities of winter by setting a "bias" value on them. There are a number of default values set in defines that can be overriden by individual provinces as well. Click to expand...
<!-- artifact:quote:end -->
Wouldn’t you be able to create a seperate effect for a southern hemisphere winter? I mean in theory, as I realise there is no Southern hemisphere yet

## Reply 220 — participant_008 · 2021-03-01 · post-27330132

So. Who's excited for tomorrow's dev diary?

## Reply 221 — participant_081 · 2021-03-01 · post-27330288

<!-- artifact:quote:start -->
> johnty5 said: So. Who's excited for tomorrow's dev diary? Click to expand...
<!-- artifact:quote:end -->
Very much so.

## Reply 222 — participant_139 · 2021-03-02 · post-27331835

<!-- artifact:quote:start -->
> johnty5 said: So. Who's excited for tomorrow's dev diary? Click to expand...
<!-- artifact:quote:end -->
There's any confirmation we'll have weekly DD from now on?

## Reply 223 — participant_074 · 2021-03-02 · post-27331922

<!-- artifact:quote:start -->
> sbcmola said: There's any confirmation we'll have weekly DD from now on? Click to expand...
<!-- artifact:quote:end -->
Yes. Several people desire it which means their energy is bending the universe to their will, and my cousin's boyfriend's sister read it in her tea leaves this morning, so I'd say it's pretty much a slam dunk! (No, though they did say "For the next few weeks and the coming dev diaries we’ll talk a bit about what we have in store for the next major update," which is close enough to engender hope. )

## Reply 224 — participant_062 · 2021-03-02 · post-27332044

<!-- artifact:quote:start -->
> sbcmola said: There's any confirmation we'll have weekly DD from now on? Click to expand...
<!-- artifact:quote:end -->
Dev Diary confirmed!

## Reply 225 — participant_008 · 2021-03-02 · post-27332081

<!-- artifact:quote:start -->
> sbcmola said: There's any confirmation we'll have weekly DD from now on? Click to expand...
<!-- artifact:quote:end -->
It's been pretty strongly implied since January that once they start, they'll be weekly. The fact that we've had two in two weeks since the first one backs that up too.

## Reply 226 — participant_074 · 2021-03-02 · post-27332148

<!-- artifact:quote:start -->
> PDX-Nicou said: Dev Diary confirmed! Click to expand...
<!-- artifact:quote:end -->
Is this confirmed for today, @PDX-Nicou, or on a weekly basis? All of the above? Something else?

## Reply 227 — participant_140 · 2021-03-02 · post-27332326

<!-- artifact:quote:start -->
> Karlington said: Is this confirmed for today, @PDX-Nicou, or on a weekly basis? All of the above? Something else? Click to expand...
<!-- artifact:quote:end -->
Yes

## Reply 228 — participant_014 · 2021-03-02 · post-27332388

There will be a developer diary at 14:30 CET, so stay tuned

## Reply 229 — participant_009 · 2021-03-02 · post-27332392

<!-- artifact:quote:start -->
> PDXOxycoon said: There will be a developer diary at 14:30 CET, so stay tuned Click to expand...
<!-- artifact:quote:end -->
Thank you very much. I'm waiting

## Reply 230 — participant_140 · 2021-03-02 · post-27332402

<!-- artifact:quote:start -->
> PDXOxycoon said: There will be a developer diary at 14:30 CET, so stay tuned Click to expand...
<!-- artifact:quote:end -->
This is the kind of communication that we like, so we can stay calm and patiently wait for it, without refreshing the forum every few seconds. The fact that I will do it anyway don't affect my argument

## Reply 231 — participant_082 · 2021-03-02 · post-27332409

<!-- artifact:quote:start -->
> PDXOxycoon said: There will be a developer diary at 14:30 CET, so stay tuned Click to expand...
<!-- artifact:quote:end -->
Around 10-10:30 AM EST...

## Reply 232 — participant_062 · 2021-03-02 · post-27332412

Weekly Dev Diaries confirmed o7

## Reply 233 — participant_141 · 2021-03-02 · post-27332437

<!-- artifact:quote:start -->
> PDX-Nicou said: Weekly Dev Diaries confirmed o7 Click to expand...
<!-- artifact:quote:end -->
Elite: Dangerous reference confirmed. Expect Medieval Spaceships DLC, confirmed.

## Reply 234 — participant_127 · 2021-03-02 · post-27332446

Magnificent peace, glorious war (Pax Magnifica, Bellum Gloriosum!)? Is that the hint about the content of the DLC?

## Reply 235 — participant_062 · 2021-03-02 · post-27332517

<!-- artifact:quote:start -->
> Amaiur of Navarre said: Elite: Dangerous reference confirmed. Expect Medieval Spaceships DLC, confirmed. Click to expand...
<!-- artifact:quote:end -->
Hutton Castle is selling free royal crowns for your king/queen, it's far far far from your holdings though... Let's jump to Dev Diary #50: Poetry To My Ears

