---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1731866/"
forum_thread_id: 1731866
content_type: reply_thread
parent_dd_file: dd_165_2025-03-17_tributaries-confederations.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 165
title: "Dev Diary #165 - Tributaries & Confederations"
dd_date: 2025-03-18
expansion: Khans of the Steppe
patch: Patch 1.16
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 14
reply_count: 273
participant_count: 157
reply_date_first: 2025-03-18
reply_date_last: 2025-04-30
body_word_count: 17741
inline_image_count: 0
quoted_span_count: 131
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Dev Diary #165 - Tributaries & Confederations

*273 replies from 157 participants across 14 pages*

## Reply 1 — participant_001 · 2025-03-18 · post-30238958

All looks good but one thing to mention, the Khitans should be called Great Liao by 1178. Their government was of the Chinese Bureaucratic style and had many Chinese features. They got ran out by the Jurchen Jin but still kept their Chinese style of governance while ruling over different groups in Central Asia. Their rulers had the title of Emperor and/or “Gurkhan” which means universal ruler. In 1178 start date they should not nomadic but have Administrative government.

## Reply 2 — participant_002 · 2025-03-18 · post-30238960

<!-- artifact:quote:start -->
> lachek said: Hello there! Welcome back to the first official dev diary for our Core Expansion this year, Khans of the Steppe. For those who did not see it, we first talked about the DLC back last month with Dev Diary #162 - Steppe by Steppe, so I recommend reading that first. Today we will discuss Tributaries, Confederations, and Raid Intents. All three topics were mentioned in the previous Dev Diary, but we will discuss them at length in this one, so let’s settle in like a migrating nomad and get started. Follow-up from Previous Dev Diary​The team has gone through an intense iteration period based on both feedback collected internally and the comments received from our previous Dev Diary. Many changes have been thus made, and we are sure we are not done with it yet. However, here's a small list of some of the most significant tweaks done based on your feedback: A new, "base" Tributary type has been made available for non-Nomads. Concerns about the Nomadic economy have been addressed by adding a monthly income for nomads based on their Herd size (symbolizing the trade of meat, hides, etc.) A game rule has been added to include Nomadic governments in the Sahel, Arabia, the horn of Africa, Sami and Karelia regions Tweaked the borders of the Steppe and characters who should be nomadic in all bookmarks (more than I can list here, screenshots will be shared in following Diaries) We've added a Culture and Faith specific to your Nomadic Capital, different than your own Adventurers can now become Nomads if they move into a Herder holding We have expanded what we originally scoped for razing We've extended and altered the effects of some Seasons We have made it possible to grow your herd if you hold lands outside of the Steppe, giving those counties Fertility if held by a nomad Tributaries​One of the new features we’re introducing with Khans of the Steppe, and the free update that goes along with it, are Tributaries. Vast nomadic realms like the Cumans, Khitans, and Khazars were not kept together by a tiered system of formal vassalage and pledges of fealty, nor were they delineated by culture or religion. Instead, the harsh realpolitik of the steppe applied - whoever could muster the greatest capacity for destruction on their neighbors proved themselves worthy of tribute, in exchange for the privilege of not being trampled underhoof. Modeling this type of subject relationship properly was the impetus for the Tributary feature. Let's back up a bit and discuss some fundamentals first though, because tributaries aren't just a nomad thing. While Tributaries are similar to vassals in some respects, they represent a whole new type of unequal diplomatic relationship in the game. As a result, many game elements that formerly referred to "vassals" now refer to "subjects" instead. Subjects can be either vassals or tributaries, and these sub-types adhere to different rules. As with vassal contracts, there can be different types of tributary contracts with varying degrees of obligations. In most cases, these terms can be renegotiated. Tributaries can be seen as a more independent subject type compared to vassals. While in most cases they share the map color and realm name with their suzerain, they can act and be interacted with independently, even when it comes to warfare. Most tributary types can also be created through peaceful means, by a sovereign ruler pledging tribute to a nomadic realm in exchange for a guarantee to not be attacked by them, or through a nomadic ruler demanding tribute from a neighboring realm. Agreements of tribute are (usually) perpetuated across generations, but may change in nature over time or be more easily broken when the contract changes hands. View attachment 1267235 [Marzoban Tokku and his weak backbone stands little chance against the persuasive might of the Cumanian horde] View attachment 1267236 [If some scary nomadic realm is on your border and you'd like to remain as independent as possible, you can proactively choose to pay them tribute to avoid outright conquest] View attachment 1267237 [Existing vassals can be released as tributaries, and in some cases you can even vassalize an existing tributary] Nomadic Tributaries are what you will encounter most frequently in Khans of the Steppe. These consist of nomadic realms (or spineless herders) who have pledged tribute to a stronger nomadic ruler on their border. They will pay a part of their herd in tribute on a regular basis, and some of the prestige they gain will also be conferred upon their suzerain. In exchange for tribute, they enjoy a great deal of independence from their suzerain and will not be outright attacked or raided by them. They can even have tributaries of their own! Settled Tributaries are non-nomadic realms (such as feudal princes, tribes, or clans) who have yielded to a bordering nomadic ruler. Like their nomadic tributary counterparts, they will pay tribute on a regular basis, but instead of herd they will provide gold and levies. Both these types of tributary contracts are inherited across generations, but they also have quite a bit of leeway in simply ceasing payments (if they are ready to face the consequences of insulting their suzerain, that is). This is most likely to happen if a nomadic suzerain prove themselves weak in some way (and therefore unworthy of tribute, by the laws of the steppe), like losing a war or suffering a chaotic Kurultai succession. Once tributaries opt to stop sending gifts to their suzerain the suzerain can choose to attack them to recover control, or let them go try to make their own destiny without their protection. To try to keep this from happening, nomadic suzerains can either be lenient with their contract conditions, or leverage their Dread to demand Obedience of their tributaries. View attachment 1267238 [Your subject view will display if any of your tributaries are likely to stop paying you and why. Obedience plays a strong role in keeping your subjects in line, but even disobedient ones will be reluctant to stop paying off much stronger suzerains. More factors will be added before launch, such as losing a war or having chaotic Kurultai successions.] A third type of subjugated tributary has also been added, which has no direct relation to nomads. This is a tributary type obliged to pay a lot of gold and a small amount of prestige to their suzerain in exchange for their suzerain's protection from outside invasion. If attacked, a subjugated tributary can call their suzerain in to defend them, and if they refuse their tributary obligations are annulled. Any non-nomadic realm can create this type of tributary through the Bring Under Tribute casus belli, enabling the extortion of neighboring protectorates through sheer military might. This contract does not get inherited by the suzerain's heir upon their death, but also cannot be voluntarily broken. If the tributary wishes to break free of their obligations prior to their suzerain's death, they will have to fight them for independence. View attachment 1267239 [Even feudal realms can subjugate neighboring kingdoms to make them pay tribute, if their Crown Authority is high enough] It's important to note that it's possible to modify the terms of a tributary contract, just like a vassal contract. For example, nomads can negotiate for protection by their suzerains in exchange for higher tribute payments. If you and your tributary are Blood Brothers, you can even negotiate a guarantee that they will follow you on all military adventures, offensive as well as defensive. View attachment 1267240 [Even the tributary can try to renegotiate the terms, but without a good relationship with (or a hook on) your suzerain this might be met with limited success] Another aspect of tributaries of nomadic realms is that they can provide new Men-at-Arms types to their suzerain. In keeping with the flexible and heterogenous nature of steppe warfare, nomad rulers are able to recruit Men-at-Arms from both tributaries and vassals as if they were their own. Since the Men-at-Arms are recruited from other realms, rather than an additional cost of herd (to represent the development of more advanced mounted units) this costs a premium in gold to entice the foreigners to join up with the Khan's formidable horde. View attachment 1267241 [If you don’t have any subjects with access to some of the basic Men-at-Arms types, you get a little hint suggesting who might give you access to them…] Visually, tributary realms will typically adopt the map color and name of their suzerain to clarify the relationship between them. Modders might be interested to know that this behavior can be changed in script depending on the subject contract: you can make tributary types that do not inherit the suzerain's color or name, or just one of them, as well! View attachment 1267243 [In 867, the Khazars dominate the Western Steppe while the Kirghiz control the Eastern parts. The Karluks and Ohguz are powerful nomadic realms in the central steppe region and have a lot of opportunity to compete for the smaller nomadic and tribal realms towards the northern parts.] View attachment 1267246 [In 1066 the western and central steppe regions are dominated by the Cumans in the south, with a considerable tributary network maintaining their control of the center and maintaining their power against the Karluks and Khitans. The Pechenegs have migrated west and act as a buffer zone between the steppe and the Byzantine Empire - will they manage to become their own nomadic powerhouse, or fall to either of their titanic neighbors?] View attachment 1267247 [In 1178, the Cumans remain the most powerful nomadic realm on the steppe, but for how long? The Khitans are migrating south into East Asia, leaving their old lands to the fractured Mongols to thrive.] Since tributaries inherit all of the functionality of the vassal contract system, with a few extensions, they are very flexible and capable of modeling a great deal of unequal relationships between realms and rulers. There's a fair chance you will see more tributary types and dynamics added to the game in the future, and the system is fully available to modders to play with as well! But how would you deal with these massive, aggressive nomadic realms as a smaller nomad who just wants to live a laid-back, peaceful nomadic lifestyle? One avenue to that is what we'll discuss next. Confederations​Brothers and sisters, do you ever tire of lusting after power? When you jump into a game as a meek little Count, do you wish friends and neighbors would stand together with you against the masters of the world? Do you want something new to do as a tribal? Say no more, my brothers and sisters - but the sacred words, the oath of confederation! In short, Confederations are a new way for nomads and tribals to feel safe while initially building their power, playing tall, etc. It’s also a bit of an extra challenge for those looking to easily gobble up areas of the map that lack a mighty King or Emperor. View attachment 1267248 [12th c. Estonia mightn’t have looked quite like this, but hopefully this captures some of its spirit] The inspiration for Confederations came from a visit to beautiful Tallinn, Estonia (which I very highly recommend), a fascinating conversation with a very learned scholar in medieval Baltic history, and a visit to the Great Guild Hall Museum. Therein, an exhibit asked the question — “Why did Estonia not become a Kingdom?” It’s an interesting question, with at least a few answers. In a sense, the Estonian tribes did actually have kings, but these were temporary war-leaders or spiritual figures, and they did not serve to unite all the tribes together into one lasting polity. They are mentioned, as stubborn figures of resistance, in the Christian chronicles of conquest. This kind of defensive decentralization seemed new for CK3; I immediately wanted to represent it in our game. And, of course, there are the steppe confederations of history — the Khamag Mongol, the Kimek-Kipchaks, the Mogyërs, and so on — to consider and draw from as well. I’m also a Canadian btw, and Confederation has been a force of history around the Great Lakes for quite a while. Let’s go through the confederating process, and discuss. View attachment 1267249 [The Decision that lays the path to Confederation] The first step is a Decision that enables you to offer Confederation to other rulers. Its warnings are to be taken seriously — you will likely have to leave your Confederation if you want to increase your station in the world (through means like title creation, migration, Dominance) or enrich yourself by raiding/attacking your fellow weaklings. View attachment 1267250 [The requirements for starting a Confederation; you have to be something of a small fish] Who can make a Confederation? Well, you have to be standing on your own, and you can’t be standing very tall. These same restrictions apply to all prospective Confederates. View attachment 1267251 [Additional Confederation triggers. Most of the time, you’ll need a big, scary common foe] Confederations in Crusader Kings III will be fleeting, ephemeral things, and focused largely on deterring the depredations of powerful neighbors. Thus, they will almost always be created in response to major powers being at their borders. It’s been really cool to watch Conquerors and great kings arise and, as they do, Confederations spring up all along their underbellies like nests of rats or colonies of fire ants. There is now a third, sometimes-viable alternative to “submit or die.” The possible faith hostility trigger also works really nicely along the borderlands between pagan tribals and reformed faiths: it means the former can often be seen making the Confederation defensive arrangement to resist the brutal tide of history. View attachment 1267252 [You’re ready for Confederation… you just need a buddy to join you] Given Confederations are available across the map, to both nomads and tribals, related content is laced with conditional loc and effects to keep things from feeling too inappropriate. That said, this isn’t a content-heavy feature; development on Confederations instead focused on making it an effective new mechanic. View attachment 1267253 [The interaction used to create a Confederation, and also to add new members] The character interaction Offer Confederation (unlocked by the Call for Confederation decision or by Confederation membership) is how this brothers-in-arms, last stand-style shit comes to pass. Notice that, because migration removes members from the Confederation, there are incentives to stay put for a bit longer (a positive County Fertility modifier and an immediate County Fertility boost). AI should also be more reluctant to migrate than usual, at least for a few years. View attachment 1267254 [Weights are pretty comprehensive and pretty make-or-break] Your level of investment in your confederation can make a big difference in its strength: herd, prestige and hooks can be sacrificed to make valid members more willing to join. View attachment 1267255 [Well isn’t that nice - he accepts!] View attachment 1267256 [Note the Confederation icon and breakdown] Confederations aren’t a title. Their closest equivalent is an alliance or truce, thus they live in the Diplomacy space of the Character view. Here, you can see all members of the Confederation. The Kimek Confederation is a culture-based name, which happens when both the first members are of the same culture. When they aren’t, the Confederation will be named after the founder’s de jure duchy (ex. the Semey Confederation, the Kargassia Confederation). View attachment 1267257 [A handful of Kimeks have joined the Confederation (squint, it’s on the left)] On the map, Confederations will look similar to the new Tributaries: their individual realm names are replaced by the overall Confederation and their map colors are blended towards the main Confederation color (which is based on the founder’s capital). You may notice that the members remain rather unevenly-sized. That’s because only independent top rulers are members of the Confederation, and their vassals (if they have any) are not. View attachment 1267258 [The Confederation is attacked!] When a Confederation member is attacked is when the organization really comes into its own. All members are automatically added as Defenders. This can result in a pretty potent nest of bees that the aggressor has just poked. Accordingly, the combined strength of a Confederation is shown when opening the Declare War screen on one of its members, and AI should be appropriately hesitant to attack strong Confederations. Note that this applies only to members’ defensive wars. They cannot call on the Confederation when they themselves declare offensive wars. View attachment 1267259 [The Decision for when a Confederate decides it’s time to go…] While AI will usually give the Confederation at least a few years of their time, players are quite free to strike off on their own whenever. Albeit… for a higher Prestige cost during the first couple years. The AI weighting for this Decision is heavily dependent on circumstances. Chief among these is the presence of big nearby threats that necessitate confederation. The result is that, where confederations are needed, they should prove much more lasting and resilient. And when they are no longer needed, they should often quickly disband. View attachment 1267260 [BROTRAYAL] And there it is, Confederations! I hope this run-through has cleared up the feature. And remember — the CK player who stands alone, dies alone. Call up a friend right now and ask if they’d FUCKING DIE for you. Post results in the comments. Raid Intents​We discussed raid intents in the previous dev diary, with a small WIP screenshot. It’s time to expand on what we said then. First of all, we should talk about loot. As you all know, we’ve had loot in the game for quite a while. Gold you can take from a settlement as you raid them as a tribal ruler or a pagan, which you then bring back home to turn into gold and prestige. We haven’t changed the core mechanic of loot, but we have disconnected it slightly from purely being gold, now that you have more ways of using it. With Raid Intents, we now have ways of turning that loot into other things, to symbolize your aims as you are raiding foreign lands. View attachment 1267261 Here is the new raid intent screen (for nomads), after a small art pass and after we added some proper names. Now, let’s look at the default raid intent for nomadic rulers, Pillage. View attachment 1267262 [Note that none of the numbers are final, so they might change before the release] It’s a fairly straightforward calculation. If you bring home 100 loot, you will get 100 gold and 150 herd out of it when you return to your borders. Most of the other raid intents have some kind of separate side effects in addition to their base calculation, so let’s look at some of them. View attachment 1267263 Nomads were known for raiding far and wide, with the Hungarian raiders, for example, bringing home loot from all across Europe. With the Adventure raid intent, it will take a bit longer to raid each settlement, but you can carry a significantly larger amount of loot with you, and you will take no hostile county attrition. It should be noted that within the steppe, nomad raiders will not take any hostile county attrition, regardless of raid intent, but they will regularly take attrition outside of it. View attachment 1267264 Plunder symbolizes that you aren’t necessarily just taking anything but trying to find the most valuable things to take. It will take significantly longer to raid every single settlement. Still, the loot conversion as you get home is considerably better, and you have a chance to learn innovations of a culture as you raid a settlement if they know about something you do not (though the chances are quite low). View attachment 1267265 For those less interested in the loot itself but rather other side effects, you might want to take the capture raid intent to significantly increase the chance of capturing someone as you raid a settlement. It’s great if you are looking to ransom someone. View attachment 1267266 And last but not least, you have the opportunity to destroy. It’s an opportunity for nomads to increase their prestige (as they don’t get any prestige from other raid intents) and their dread (which is more important for nomads). It also destroys buildings and development in settlements they raid. Now, one thing to mention is that we don’t only have raid intents for nomads but for other raiders as well. Regular raiders also have access to the Terrorize raid intent, so feel free to bring destruction to your enemies no matter which flavor of uncivilized you are. They also have access to Pillage, but in a slightly different form: View attachment 1267267 Like current functionality, you simply change your loot to gold and prestige. And for Vikings, they have access to a slightly modified version of the Adventure intent. View attachment 1267268 If you want to raid your way down to Constantinople and then home again, feel free to take this to bring all that loot back home. Now for the other side, you can destroy the raiders as they enter your lands, but we have also made one small adjustment so you can protect yourself a bit against any incoming threat. View attachment 1267269 We have increased the hostile raid time reduction in the building, so you have more time to respond to incoming threats. It now also reduces the chances of special raid intents. In other words, it reduces the improvements from the Capture raid intent, minimizes the chance of Terrorize ruining your lands, and for Plunder to find any innovation. Next Week​That’s it for this week. Next week, we plan to revisit migrations and the nomadic government, so we hope to see you again then. Go forth and conquer, my blood brothers. Click to expand...
<!-- artifact:quote:end -->
Greatest Dev Team on earth! Thank you for supplying great content. Just one question, compared to administrative, how expansive will nomadics feel and be? What are settlment issues? Thanks!

## Reply 3 — participant_003 · 2025-03-18 · post-30238965

<!-- artifact:quote:start -->
> lachek said: A new, "base" Tributary type has been made available for non-Nomads. A game rule has been added to include Nomadic governments in the Sahel, Arabia, the horn of Africa, Sami and Karelia regions Click to expand...
<!-- artifact:quote:end -->
Those two alone warrant my unconditional love for you guys!

## Reply 4 — participant_004 · 2025-03-18 · post-30238973

nice, sorry for the off topic question, but when is the Q&A going to be relesed?

## Reply 5 — participant_005 · 2025-03-18 · post-30238977

Thanks for the run down! The systems look interesting, especially for modders to make use of. Thank you also for allowing non-steppe nomads access to the nomad govt. Will there be any substantial differences with how, for instance, the nomad stuff works in Arabia or the Sami lands compared to the steppes? For instance how would the climate system work?

## Reply 6 — participant_006 · 2025-03-18 · post-30238981

Turkic tribes still wear Mongol clothing............ Also in the 1066 start the Karluks should be renamed to Karakhanids.

## Reply 7 — participant_007 · 2025-03-18 · post-30238985

Kudos to taking up the ideas of players as well. It looks great. So technically you could form an Italian Catholic Horde with an Adventurer. Cool.

## Reply 8 — participant_008 · 2025-03-18 · post-30238986

Will we get "baqt" tribute paid by Nubians to Egypt?

## Reply 9 — participant_009 · 2025-03-18 · post-30238991

Looks awesome, I look forward to seeing confederations rise and fall, and for raiders such as the Hungarians to actually attempt far flung raids after settling in the Pannonian basin. Is there some kind of mechanic for confederations to federate into a more tight-knit realm? If memory serves me right, the Cumans were actually in a federation with the Kipchaks, which historically tightened into more of a proper realm.

## Reply 10 — participant_010 · 2025-03-18 · post-30238992

all very intresting addtions. also any non nomdas that start with tribitaries? the Byzantines for example?

## Reply 11 — participant_011 · 2025-03-18 · post-30238995

Sounds good, although the Tributary system should be available for Iberia too. A great part of the reasons why Granada survived for 250 years the rest of Al-Andalus is because they paid tributes to Castille. In 1066, at least Sevilla, Granada, Toledo and Zaragoza paid tributes to them.

## Reply 12 — participant_002 · 2025-03-18 · post-30238996

<!-- artifact:quote:start -->
> lachek said: Hello there! Welcome back to the first official dev diary for our Core Expansion this year, Khans of the Steppe. For those who did not see it, we first talked about the DLC back last month with Dev Diary #162 - Steppe by Steppe, so I recommend reading that first. Today we will discuss Tributaries, Confederations, and Raid Intents. All three topics were mentioned in the previous Dev Diary, but we will discuss them at length in this one, so let’s settle in like a migrating nomad and get started. Follow-up from Previous Dev Diary​The team has gone through an intense iteration period based on both feedback collected internally and the comments received from our previous Dev Diary. Many changes have been thus made, and we are sure we are not done with it yet. However, here's a small list of some of the most significant tweaks done based on your feedback: A new, "base" Tributary type has been made available for non-Nomads. Concerns about the Nomadic economy have been addressed by adding a monthly income for nomads based on their Herd size (symbolizing the trade of meat, hides, etc.) A game rule has been added to include Nomadic governments in the Sahel, Arabia, the horn of Africa, Sami and Karelia regions Tweaked the borders of the Steppe and characters who should be nomadic in all bookmarks (more than I can list here, screenshots will be shared in following Diaries) We've added a Culture and Faith specific to your Nomadic Capital, different than your own Adventurers can now become Nomads if they move into a Herder holding We have expanded what we originally scoped for razing We've extended and altered the effects of some Seasons We have made it possible to grow your herd if you hold lands outside of the Steppe, giving those counties Fertility if held by a nomad Tributaries​One of the new features we’re introducing with Khans of the Steppe, and the free update that goes along with it, are Tributaries. Vast nomadic realms like the Cumans, Khitans, and Khazars were not kept together by a tiered system of formal vassalage and pledges of fealty, nor were they delineated by culture or religion. Instead, the harsh realpolitik of the steppe applied - whoever could muster the greatest capacity for destruction on their neighbors proved themselves worthy of tribute, in exchange for the privilege of not being trampled underhoof. Modeling this type of subject relationship properly was the impetus for the Tributary feature. Let's back up a bit and discuss some fundamentals first though, because tributaries aren't just a nomad thing. While Tributaries are similar to vassals in some respects, they represent a whole new type of unequal diplomatic relationship in the game. As a result, many game elements that formerly referred to "vassals" now refer to "subjects" instead. Subjects can be either vassals or tributaries, and these sub-types adhere to different rules. As with vassal contracts, there can be different types of tributary contracts with varying degrees of obligations. In most cases, these terms can be renegotiated. Tributaries can be seen as a more independent subject type compared to vassals. While in most cases they share the map color and realm name with their suzerain, they can act and be interacted with independently, even when it comes to warfare. Most tributary types can also be created through peaceful means, by a sovereign ruler pledging tribute to a nomadic realm in exchange for a guarantee to not be attacked by them, or through a nomadic ruler demanding tribute from a neighboring realm. Agreements of tribute are (usually) perpetuated across generations, but may change in nature over time or be more easily broken when the contract changes hands. View attachment 1267235 [Marzoban Tokku and his weak backbone stands little chance against the persuasive might of the Cumanian horde] View attachment 1267236 [If some scary nomadic realm is on your border and you'd like to remain as independent as possible, you can proactively choose to pay them tribute to avoid outright conquest] View attachment 1267237 [Existing vassals can be released as tributaries, and in some cases you can even vassalize an existing tributary] Nomadic Tributaries are what you will encounter most frequently in Khans of the Steppe. These consist of nomadic realms (or spineless herders) who have pledged tribute to a stronger nomadic ruler on their border. They will pay a part of their herd in tribute on a regular basis, and some of the prestige they gain will also be conferred upon their suzerain. In exchange for tribute, they enjoy a great deal of independence from their suzerain and will not be outright attacked or raided by them. They can even have tributaries of their own! Settled Tributaries are non-nomadic realms (such as feudal princes, tribes, or clans) who have yielded to a bordering nomadic ruler. Like their nomadic tributary counterparts, they will pay tribute on a regular basis, but instead of herd they will provide gold and levies. Both these types of tributary contracts are inherited across generations, but they also have quite a bit of leeway in simply ceasing payments (if they are ready to face the consequences of insulting their suzerain, that is). This is most likely to happen if a nomadic suzerain prove themselves weak in some way (and therefore unworthy of tribute, by the laws of the steppe), like losing a war or suffering a chaotic Kurultai succession. Once tributaries opt to stop sending gifts to their suzerain the suzerain can choose to attack them to recover control, or let them go try to make their own destiny without their protection. To try to keep this from happening, nomadic suzerains can either be lenient with their contract conditions, or leverage their Dread to demand Obedience of their tributaries. View attachment 1267238 [Your subject view will display if any of your tributaries are likely to stop paying you and why. Obedience plays a strong role in keeping your subjects in line, but even disobedient ones will be reluctant to stop paying off much stronger suzerains. More factors will be added before launch, such as losing a war or having chaotic Kurultai successions.] A third type of subjugated tributary has also been added, which has no direct relation to nomads. This is a tributary type obliged to pay a lot of gold and a small amount of prestige to their suzerain in exchange for their suzerain's protection from outside invasion. If attacked, a subjugated tributary can call their suzerain in to defend them, and if they refuse their tributary obligations are annulled. Any non-nomadic realm can create this type of tributary through the Bring Under Tribute casus belli, enabling the extortion of neighboring protectorates through sheer military might. This contract does not get inherited by the suzerain's heir upon their death, but also cannot be voluntarily broken. If the tributary wishes to break free of their obligations prior to their suzerain's death, they will have to fight them for independence. View attachment 1267239 [Even feudal realms can subjugate neighboring kingdoms to make them pay tribute, if their Crown Authority is high enough] It's important to note that it's possible to modify the terms of a tributary contract, just like a vassal contract. For example, nomads can negotiate for protection by their suzerains in exchange for higher tribute payments. If you and your tributary are Blood Brothers, you can even negotiate a guarantee that they will follow you on all military adventures, offensive as well as defensive. View attachment 1267240 [Even the tributary can try to renegotiate the terms, but without a good relationship with (or a hook on) your suzerain this might be met with limited success] Another aspect of tributaries of nomadic realms is that they can provide new Men-at-Arms types to their suzerain. In keeping with the flexible and heterogenous nature of steppe warfare, nomad rulers are able to recruit Men-at-Arms from both tributaries and vassals as if they were their own. Since the Men-at-Arms are recruited from other realms, rather than an additional cost of herd (to represent the development of more advanced mounted units) this costs a premium in gold to entice the foreigners to join up with the Khan's formidable horde. View attachment 1267241 [If you don’t have any subjects with access to some of the basic Men-at-Arms types, you get a little hint suggesting who might give you access to them…] Visually, tributary realms will typically adopt the map color and name of their suzerain to clarify the relationship between them. Modders might be interested to know that this behavior can be changed in script depending on the subject contract: you can make tributary types that do not inherit the suzerain's color or name, or just one of them, as well! View attachment 1267243 [In 867, the Khazars dominate the Western Steppe while the Kirghiz control the Eastern parts. The Karluks and Ohguz are powerful nomadic realms in the central steppe region and have a lot of opportunity to compete for the smaller nomadic and tribal realms towards the northern parts.] View attachment 1267246 [In 1066 the western and central steppe regions are dominated by the Cumans in the south, with a considerable tributary network maintaining their control of the center and maintaining their power against the Karluks and Khitans. The Pechenegs have migrated west and act as a buffer zone between the steppe and the Byzantine Empire - will they manage to become their own nomadic powerhouse, or fall to either of their titanic neighbors?] View attachment 1267247 [In 1178, the Cumans remain the most powerful nomadic realm on the steppe, but for how long? The Khitans are migrating south into East Asia, leaving their old lands to the fractured Mongols to thrive.] Since tributaries inherit all of the functionality of the vassal contract system, with a few extensions, they are very flexible and capable of modeling a great deal of unequal relationships between realms and rulers. There's a fair chance you will see more tributary types and dynamics added to the game in the future, and the system is fully available to modders to play with as well! But how would you deal with these massive, aggressive nomadic realms as a smaller nomad who just wants to live a laid-back, peaceful nomadic lifestyle? One avenue to that is what we'll discuss next. Confederations​Brothers and sisters, do you ever tire of lusting after power? When you jump into a game as a meek little Count, do you wish friends and neighbors would stand together with you against the masters of the world? Do you want something new to do as a tribal? Say no more, my brothers and sisters - but the sacred words, the oath of confederation! In short, Confederations are a new way for nomads and tribals to feel safe while initially building their power, playing tall, etc. It’s also a bit of an extra challenge for those looking to easily gobble up areas of the map that lack a mighty King or Emperor. View attachment 1267248 [12th c. Estonia mightn’t have looked quite like this, but hopefully this captures some of its spirit] The inspiration for Confederations came from a visit to beautiful Tallinn, Estonia (which I very highly recommend), a fascinating conversation with a very learned scholar in medieval Baltic history, and a visit to the Great Guild Hall Museum. Therein, an exhibit asked the question — “Why did Estonia not become a Kingdom?” It’s an interesting question, with at least a few answers. In a sense, the Estonian tribes did actually have kings, but these were temporary war-leaders or spiritual figures, and they did not serve to unite all the tribes together into one lasting polity. They are mentioned, as stubborn figures of resistance, in the Christian chronicles of conquest. This kind of defensive decentralization seemed new for CK3; I immediately wanted to represent it in our game. And, of course, there are the steppe confederations of history — the Khamag Mongol, the Kimek-Kipchaks, the Mogyërs, and so on — to consider and draw from as well. I’m also a Canadian btw, and Confederation has been a force of history around the Great Lakes for quite a while. Let’s go through the confederating process, and discuss. View attachment 1267249 [The Decision that lays the path to Confederation] The first step is a Decision that enables you to offer Confederation to other rulers. Its warnings are to be taken seriously — you will likely have to leave your Confederation if you want to increase your station in the world (through means like title creation, migration, Dominance) or enrich yourself by raiding/attacking your fellow weaklings. View attachment 1267250 [The requirements for starting a Confederation; you have to be something of a small fish] Who can make a Confederation? Well, you have to be standing on your own, and you can’t be standing very tall. These same restrictions apply to all prospective Confederates. View attachment 1267251 [Additional Confederation triggers. Most of the time, you’ll need a big, scary common foe] Confederations in Crusader Kings III will be fleeting, ephemeral things, and focused largely on deterring the depredations of powerful neighbors. Thus, they will almost always be created in response to major powers being at their borders. It’s been really cool to watch Conquerors and great kings arise and, as they do, Confederations spring up all along their underbellies like nests of rats or colonies of fire ants. There is now a third, sometimes-viable alternative to “submit or die.” The possible faith hostility trigger also works really nicely along the borderlands between pagan tribals and reformed faiths: it means the former can often be seen making the Confederation defensive arrangement to resist the brutal tide of history. View attachment 1267252 [You’re ready for Confederation… you just need a buddy to join you] Given Confederations are available across the map, to both nomads and tribals, related content is laced with conditional loc and effects to keep things from feeling too inappropriate. That said, this isn’t a content-heavy feature; development on Confederations instead focused on making it an effective new mechanic. View attachment 1267253 [The interaction used to create a Confederation, and also to add new members] The character interaction Offer Confederation (unlocked by the Call for Confederation decision or by Confederation membership) is how this brothers-in-arms, last stand-style shit comes to pass. Notice that, because migration removes members from the Confederation, there are incentives to stay put for a bit longer (a positive County Fertility modifier and an immediate County Fertility boost). AI should also be more reluctant to migrate than usual, at least for a few years. View attachment 1267254 [Weights are pretty comprehensive and pretty make-or-break] Your level of investment in your confederation can make a big difference in its strength: herd, prestige and hooks can be sacrificed to make valid members more willing to join. View attachment 1267255 [Well isn’t that nice - he accepts!] View attachment 1267256 [Note the Confederation icon and breakdown] Confederations aren’t a title. Their closest equivalent is an alliance or truce, thus they live in the Diplomacy space of the Character view. Here, you can see all members of the Confederation. The Kimek Confederation is a culture-based name, which happens when both the first members are of the same culture. When they aren’t, the Confederation will be named after the founder’s de jure duchy (ex. the Semey Confederation, the Kargassia Confederation). View attachment 1267257 [A handful of Kimeks have joined the Confederation (squint, it’s on the left)] On the map, Confederations will look similar to the new Tributaries: their individual realm names are replaced by the overall Confederation and their map colors are blended towards the main Confederation color (which is based on the founder’s capital). You may notice that the members remain rather unevenly-sized. That’s because only independent top rulers are members of the Confederation, and their vassals (if they have any) are not. View attachment 1267258 [The Confederation is attacked!] When a Confederation member is attacked is when the organization really comes into its own. All members are automatically added as Defenders. This can result in a pretty potent nest of bees that the aggressor has just poked. Accordingly, the combined strength of a Confederation is shown when opening the Declare War screen on one of its members, and AI should be appropriately hesitant to attack strong Confederations. Note that this applies only to members’ defensive wars. They cannot call on the Confederation when they themselves declare offensive wars. View attachment 1267259 [The Decision for when a Confederate decides it’s time to go…] While AI will usually give the Confederation at least a few years of their time, players are quite free to strike off on their own whenever. Albeit… for a higher Prestige cost during the first couple years. The AI weighting for this Decision is heavily dependent on circumstances. Chief among these is the presence of big nearby threats that necessitate confederation. The result is that, where confederations are needed, they should prove much more lasting and resilient. And when they are no longer needed, they should often quickly disband. View attachment 1267260 [BROTRAYAL] And there it is, Confederations! I hope this run-through has cleared up the feature. And remember — the CK player who stands alone, dies alone. Call up a friend right now and ask if they’d FUCKING DIE for you. Post results in the comments. Raid Intents​We discussed raid intents in the previous dev diary, with a small WIP screenshot. It’s time to expand on what we said then. First of all, we should talk about loot. As you all know, we’ve had loot in the game for quite a while. Gold you can take from a settlement as you raid them as a tribal ruler or a pagan, which you then bring back home to turn into gold and prestige. We haven’t changed the core mechanic of loot, but we have disconnected it slightly from purely being gold, now that you have more ways of using it. With Raid Intents, we now have ways of turning that loot into other things, to symbolize your aims as you are raiding foreign lands. View attachment 1267261 Here is the new raid intent screen (for nomads), after a small art pass and after we added some proper names. Now, let’s look at the default raid intent for nomadic rulers, Pillage. View attachment 1267262 [Note that none of the numbers are final, so they might change before the release] It’s a fairly straightforward calculation. If you bring home 100 loot, you will get 100 gold and 150 herd out of it when you return to your borders. Most of the other raid intents have some kind of separate side effects in addition to their base calculation, so let’s look at some of them. View attachment 1267263 Nomads were known for raiding far and wide, with the Hungarian raiders, for example, bringing home loot from all across Europe. With the Adventure raid intent, it will take a bit longer to raid each settlement, but you can carry a significantly larger amount of loot with you, and you will take no hostile county attrition. It should be noted that within the steppe, nomad raiders will not take any hostile county attrition, regardless of raid intent, but they will regularly take attrition outside of it. View attachment 1267264 Plunder symbolizes that you aren’t necessarily just taking anything but trying to find the most valuable things to take. It will take significantly longer to raid every single settlement. Still, the loot conversion as you get home is considerably better, and you have a chance to learn innovations of a culture as you raid a settlement if they know about something you do not (though the chances are quite low). View attachment 1267265 For those less interested in the loot itself but rather other side effects, you might want to take the capture raid intent to significantly increase the chance of capturing someone as you raid a settlement. It’s great if you are looking to ransom someone. View attachment 1267266 And last but not least, you have the opportunity to destroy. It’s an opportunity for nomads to increase their prestige (as they don’t get any prestige from other raid intents) and their dread (which is more important for nomads). It also destroys buildings and development in settlements they raid. Now, one thing to mention is that we don’t only have raid intents for nomads but for other raiders as well. Regular raiders also have access to the Terrorize raid intent, so feel free to bring destruction to your enemies no matter which flavor of uncivilized you are. They also have access to Pillage, but in a slightly different form: View attachment 1267267 Like current functionality, you simply change your loot to gold and prestige. And for Vikings, they have access to a slightly modified version of the Adventure intent. View attachment 1267268 If you want to raid your way down to Constantinople and then home again, feel free to take this to bring all that loot back home. Now for the other side, you can destroy the raiders as they enter your lands, but we have also made one small adjustment so you can protect yourself a bit against any incoming threat. View attachment 1267269 We have increased the hostile raid time reduction in the building, so you have more time to respond to incoming threats. It now also reduces the chances of special raid intents. In other words, it reduces the improvements from the Capture raid intent, minimizes the chance of Terrorize ruining your lands, and for Plunder to find any innovation. Upgrading the building will improve the effect and block raid intent special effects from happening outright. In other words, something to keep in mind if you experience a lot of raids in your lands. Next Week​That’s it for this week. Next week, we plan to revisit migrations and the nomadic government, so we hope to see you again then. Go forth and conquer, my blood brothers. Click to expand...
<!-- artifact:quote:end -->
Nice! Will confederations have any influence over laws, rulers, or anything political? Or is it purely a defensive alliance?

## Reply 13 — participant_012 · 2025-03-18 · post-30238997

Qara Khitai probably should not be a steppe nomad. Although it indeed had some nomadic elements, it had a sedentary capital at Balasagun, and a proper administrative system inherited from Great Liao. Maybe it can be better portrayed as a feudal empire with nomadic vassals.

## Reply 14 — participant_013 · 2025-03-18 · post-30238999

i dont like how the tributaries look like a realm under rebellion

## Reply 15 — participant_014 · 2025-03-18 · post-30239001

<!-- artifact:quote:start -->
> lachek said: A game rule has been added to include Nomadic governments in the Sahel, Arabia, the horn of Africa, Sami and Karelia regions Click to expand...
<!-- artifact:quote:end -->
With this and the arctic pack, we are essentially fulfilling my power fantasy of becoming Plupp, Khan of Khans, and destroyer of worlds.

## Reply 16 — participant_015 · 2025-03-18 · post-30239008

Doesn't seem to be anything to distinguish tribal tributaries from feudal ones which is disappointing. Could they be made ephemeral like the nomad tributaries and be broken without automatically resorting to war? I like confederations, but I think these systems are a lot more common than you've depicted and aren't entirely defensive. The almoravids originally were a berber confederation, likewise many of the slavic polities in Eastern Europe which would eventually become kingdoms. In a previous reply, your colleague mentioned that there could be a decision to turn a confederation into a kingdom of some description. Does that still hold?

## Reply 17 — participant_002 · 2025-03-18 · post-30239015

<!-- artifact:quote:start -->
> JonZone said: View attachment 1267673 With this and the arctic pack, we are essentially fulfilling my power fantasy of becoming Plupp, Khan of Khans, and destroyer of worlds. Click to expand...
<!-- artifact:quote:end -->
You've just inspired my first playthrough when the dlc releases, Huzzah!.

## Reply 18 — participant_016 · 2025-03-18 · post-30239019

<!-- artifact:quote:start -->
> cybrxkhan said: Thanks for the run down! The systems look interesting, especially for modders to make use of. Thank you also for allowing non-steppe nomads access to the nomad govt. Will there be any substantial differences with how, for instance, the nomad stuff works in Arabia or the Sami lands compared to the steppes? For instance how would the climate system work? Click to expand...
<!-- artifact:quote:end -->
No special Seasons have been made for these regions. As they are not part of the core pack, we do not have the time to add bespoke content for them. They work like the game rules to make extra Administrative realms in Egypt, the Arabian Empire, Ghana, etc.

## Reply 19 — participant_017 · 2025-03-18 · post-30239024

Imo, tributaries should be the main mean for a tribal government to expand and control a realm, as it much better reflection of how tribes actually functioned.

## Reply 20 — participant_018 · 2025-03-18 · post-30239028

Love what I’m seeing here! Is there a plan for extending the confederation mechanic to feudal rulers as well? Things like the Lombard League aren’t really well represented in the game as is, and it still is very easy to just snowball as a large landed ruler.

## Reply 21 — participant_019 · 2025-03-18 · post-30239029

Huh. So if the Plunder raid intent can steal innovations, does that mean tribal cultures can move past tribal era but still remain tribal? That and confederations, it might be possible for "late game" tribal governments to actually thrive. Also it would be interesting if there was an option for a confederation to formalize into a single realm and create a federation version of the de jure kingdom title. With consent of the members, of course.

## Reply 22 — participant_020 · 2025-03-18 · post-30239030

Sweet plug for Estonia. Thanks! Speaking of... could we maybe update the DNA for Estonians? I've never seen an Estonian look as asiatic as they do in this game. I know I'm not the only one who feels that way. I've seen others bring it up on the forum before.

## Reply 23 — participant_021 · 2025-03-18 · post-30239033

Question: You mention that "Even feudal realms can subjugate neighboring kingdoms to make them pay tribute, if their Crown Authority is high enough" but shouldn't it be a default thing not if you have high authority. Looking at a number of the various realms, like the HRE they had in the early days of the Ottonians when it was founded lots of vassals, Hungary, Bohemia, Poland but only Bohemia would be incorporated into the empire. Likewise with England and Scotland, England tried a number of times to enforce basically a tributary status on Scotland. So how would this be reflected?

## Reply 24 — participant_022 · 2025-03-18 · post-30239043

Hoping independent factions may want to be tributary now. Definitely will it be more moderate.

## Reply 25 — participant_023 · 2025-03-18 · post-30239050

Can confederations of kingdom rank titles become active when a conquerer or Great Khan is in their border? So basicly can we see Oghuz and Cuman confederation if Mongols are on their doorsteps?

## Reply 26 — participant_024 · 2025-03-18 · post-30239053

Finally a restored Carolingian Empire can expand its' borders via tributaries (as historically, it did have) instead of outright conquest! Clean border enjoyers everywhere can rejoice, all four (maybe more!) of us!

## Reply 27 — participant_025 · 2025-03-18 · post-30239059

You seem to have left out that the Chigils were independent in 1066. Could this be because they get absorbed easily?

## Reply 28 — participant_026 · 2025-03-18 · post-30239063

What is the reason for non nomadic raiders to have not access to the other raid intents? Personally I think they should have at least the capture intent too, but honestly the coolest would be of course having access to all. Many they could be locked behind cultural traditions that tribals can also gain by reforming their culture?

## Reply 29 — participant_027 · 2025-03-18 · post-30239064

Bohemia in 867 should start as a tributary to Eastern Frankia Frankia during Charlemagne failed to subjugate the region but got a peace tribute out of it that has been paid ever since (in fact st. Wenceslaus might've been murdered by his brother's men due to continuing to pay the tribute, it's a part of Czech history where wars were waged constantly over it in 10th century) Moravia was in same-ish situation but unsure about the 867 startdate The Avars should probably be made tributaries of Bulgaria and not full vassals, Krum did wage war with them but Bulgarian control extended mostly to Transylvania and Syrmium, not full authority over Pest and border with Nitra (Svatopluk's marriage with Bulgarian princess is just a theory too... on the topic of Svatopluk, can someone give him proper traits? for one of the figures who got the "the Great" nickname and who got adressed as "my son" by the pope as "king of Slavs" while territorially expanding to rival East Frankia in size, having random stats and traits feels very underwhelming)

## Reply 30 — participant_028 · 2025-03-18 · post-30239070

<!-- artifact:quote:start -->
> lachek said: For those less interested in the loot itself but rather other side effects, you might want to take the capture raid intent to significantly increase the chance of capturing someone as you raid a settlement. It’s great if you are looking to ransom someone. View attachment 1267266 Click to expand...
<!-- artifact:quote:end -->
I am going to raise a red-flag here. This will *not* to be fun, from a 'how does it feel to be raided' perspective or from an player-AI balance perspective. In general balance terms, if the AI takes this intent with any regularity, it will cripple the AI compared to players across the world. The military power of tribal and feudal realms is tied to the buildings. The advantage of the raiders is that they already have a MAA-advantage to complete their raids, and thus destroy buildings that might- in aggregate over generations- give the settled folk the ability to resist. As presented, this is a double-win mechanic to cripple landed AI to the advantage of the nomadic AI. In much the same way that the Adventurers started bankrupting already poor landed nobles and preventing them from upgrading their economies, actively destroying the economies that are being built is worse. This makes it also a weakness for the player-AI balance, because the more the players prioritize their own defense, their AI vassals / neighbors will become weaker. Ease of expansion is already a common issue. Making it easier will not help, nor will making it easier to stabilize and have a more stable frontier vassal by having fewer military buildings. And that's if you are inclined to spend money like that, because this raiding intent also creates a perverse incentive for a player in a liege role to *not* defend the realm against raiders. Vassal instaiblity is driven by relative military strength, regardless of whether you measure that in size or quality. The best way to mitigate troublesome vassals if for their military buildings to be replaced with econ buildings. You cannot do that as a liege absent seizing the county. You could, however, have raiders do it for you. A liege's cheap-and-easy strategy for vassal management should not be 'deliberately don't protect them.' It will also not be fun for players anywhere near tribal realms, as the players who want to protect against building destruction- which is to say, anyone in reach of any tribal or especially Viking threat- will have to treat each raiding force like a 'we can destroy months / years of income if you don't respond' threat. It won't matter of the risk is low, both in terms of event probability or AI chance to take the intent. Players go out of their way to avoid low risks all the time. What will matter is that the only counter-play to this is to go out and be hyper-aggressive in subjugating the potential raiders so they can't destroy your personal domain investments. If confederations are meant to allow a basis for smaller powers to be too tough to be worth conquering, don't give player powers a reason to be hyper-aggressive against the raiders who can form them. Gold doesn't matter. Hostages are annoying, but a 'liberate kinsmen' casus belli can make for interesting scenarios. (Add more of that, please.) CK2 steppe raiders were annoying enough, but they were just that- annoying. If you make every tribal in the game who can sail or march to your capital a 'we might destroy your expensive investment that takes decades for a return on investment' threat, then players are going to prioritize conquering every tribal in range. Please don't.

## Reply 31 — participant_029 · 2025-03-18 · post-30239071

<!-- artifact:quote:start -->
> lachek said: Call up a friend right now and ask if they’d FUCKING DIE for you. Post results in the comments. Click to expand...
<!-- artifact:quote:end -->
I called up my friend, and asked him. He would die to see defensive pacts to be added for feudal government type

## Reply 32 — participant_005 · 2025-03-18 · post-30239081

<!-- artifact:quote:start -->
> hattusa said: No special Seasons have been made for these regions. As they are not part of the core pack, we do not have the time to add bespoke content for them. They work like the game rules to make extra Administrative realms in Egypt, the Arabian Empire, Ghana, etc. Click to expand...
<!-- artifact:quote:end -->
Thank you for the clarification! So if I understand correctly: Seasons are, script-wise, a general feature that are optional for nomad regions Steppe's seasons are unique to the nomad steppe region, and are part of the nomad DLC Non-steppe nomads, if enabled, will not get any season-related content by default, so nomad features in their regions (such as herds, fertility, etc.) will not be affected by seasons.

## Reply 33 — participant_030 · 2025-03-18 · post-30239083

How often can you change raid intent?

## Reply 34 — participant_031 · 2025-03-18 · post-30239085

This looks really great! I'm happy to see a lot of the changes, and even some things like the game rule to allow nomads in Arabia could be really fun even if it's not the 'intended' gameplay. If you're considering adding more subject types in the future, my one worry would be about UI clutter. Instead of right-clinking and having the option of "demand tributary" or "demand vassal" as individual options, I'd consider grouping them as "demand subjugation." Then when you're determining the tributary contract, you have the option to cycle through different tabs for tributary, vassal, etc. This would also give the flexibility to switch between contract types, so a tribal tributary could become a feudal vassal over time.

## Reply 35 — participant_021 · 2025-03-18 · post-30239091

Question: While republics are still not yet playable. The way that Confederations are described sounds pretty great for reflecting the Lombard League. I wonder if in 1178 the northern Italian republics will be in a confederation. Even if they aren't yet playable, this could help balance things out for the emperor and other vassals.

## Reply 36 — participant_032 · 2025-03-18 · post-30239092

<!-- artifact:quote:start -->
> lachek said: Follow-up from Previous Dev Diary A game rule has been added to include Nomadic governments in the Sahel, Arabia, the horn of Africa, Sami and Karelia regions Click to expand...
<!-- artifact:quote:end -->
Thanks for this implementation! Even if these governments aren't exactly modeled to the specifics for those regions, I think it's a good basis that could be used to allow for differentiation That being said, with the Extra Administrative Rules, we're going to be getting a large number of "Extra Government Options," and I probably can see more of them in the future with All Under Heaven. As I enjoy the Rules (and make use of them extensively in some of my mods), this has me wondering if a new sort of rule display might be better for grouping a lot of these more "simple" choices, rather than when we end up with some 20-30 different government rules in the future. This might be a bit too far out of scope for this kind of UI modding, especially since the rules section is already so easy to use, but I think the Rules could use some kind of Singular "Extra Administrative Realms" and "Extra Nomadic Realms" header that pulls out a small pop up window with a scroll-able list and a series of check boxes. Again, this is not necessary, but it could be useful for grouping similar kinds of laws that have the same purpose and numbers, with variants for choosing between different areas of the world, between the player/AI (like Realm Stability), etc Edit: I realize the Carolingians and Player rules are not the same kind of rules, this was just an example image; they can be seperated out because they're unique, but other options like Perisa and Ghaznavids should be in there.

## Reply 37 — participant_033 · 2025-03-18 · post-30239094

Very satisfied with this DD! Good work!!!! Just two things to ask : A trait to roleplay as Herders as landless A trait opposite to Conquerors that makes you unable to declare war, lose prestige, gold, piety, legitimacy or any other debuffs to punish weak or cowardly rulers or players that make too much mistakes without considering consequences. Ps: This one could be obviously removed if you started winning battles or got to a higher level or legitimacy, or another… just to stop blobs and make players do other things beyond conquering stuff all the time, could also be a game rule.

## Reply 38 — participant_034 · 2025-03-18 · post-30239096

A couple questions/concerns: It seems that making the color and name of a tributary may make it difficult to discern both how much of your territory is tributaries relative to actual vassals and difficult to for other players to discern what parts of your realm are potentially more vulnerable to falling away since they are mere tributaries. Is this information not important to the player due to the way tributaries function? Would it perhaps make more sense to stripe the territory color or something so that it becomes clearer? If I understand correctly, Vikings have not received the capture raid intent. If so, this is very disappointing. Much of the gold gain from raiding is probably made from ransoming prisoners and I am often targeting specific territories in the hopes of capturing the women with good congenital traits who live there to serve as concubines. Not to mention the drive for women and slaves that historians seem to believe fueled the Viking raids.

## Reply 39 — participant_016 · 2025-03-18 · post-30239102

<!-- artifact:quote:start -->
> cybrxkhan said: Thank you for the clarification! So if I understand correctly: Seasons are, script-wise, a general feature that are optional for nomad regions Steppe's seasons are unique to the nomad steppe region, and are part of the nomad DLC Non-steppe nomads, if enabled, will not get any season-related content by default, so nomad features in their regions (such as herds, fertility, etc.) will not be affected by seasons. Click to expand...
<!-- artifact:quote:end -->
Apologies for being unclear. The optional nomadic regions (everything that's not the Great Steppe) will have the generic seasons we've prepared for the steppe that make sense for each, and the content associated with those. For example, the Sahel only has the Drought, Abundant Grazing and Everlasting Summer seasons, as the Zud seasons (blizzard, frozen grass, layers of snow, etc) would make no sense. We will go more over the different Season effects in the next DD.

## Reply 40 — participant_035 · 2025-03-18 · post-30239104

How will sedentary empires be able to break apart confederations? Or seek to claim one ally amongst the nomadic tribes to fight off against other nomadic tribes? The divide and conquer, as well as making allies with nomads tribes to fight other nomad tribes is historically a key policy for the Byzantines and the Chinese empires. External powers should be able to weaken coalitions and confederations by making certain tribes tributaries.

## Reply 41 — participant_036 · 2025-03-18 · post-30239110

The new armor looks sick!

## Reply 42 — participant_037 · 2025-03-18 · post-30239115

Could vassals make a confederation against entrenched regency?

## Reply 43 — participant_033 · 2025-03-18 · post-30239119

<!-- artifact:quote:start -->
> hattusa said: No special Seasons have been made for these regions. As they are not part of the core pack, we do not have the time to add bespoke content for them. They work like the game rules to make extra Administrative realms in Egypt, the Arabian Empire, Ghana, etc. Click to expand...
<!-- artifact:quote:end -->
But please revisit those regions in the future when the team will have time to work those things

## Reply 44 — participant_038 · 2025-03-18 · post-30239124

Why isn't Alania nomadic government if you don't mind me asking? as the Alanian tribes weren't this settled group but constantly moved around and were treated as such by the Georgian Chronicles.

## Reply 45 — participant_039 · 2025-03-18 · post-30239133

It would be nice if a settlement being reduced to zero development by plague would have a chance to converted to Herders as long as it was distant from centers of development on the map. There would need to be balance thrown in, but part of nomadic expansions as far as I am aware came from expanding into depopulated areas. This of course being in addition to all the other historical reasons mentioned. Also, I wonder if the "prevents special raiding intents" mechanic will be slapped onto some more Landmarks like walls or the legend buildings. I am also wondering how this DLC will integrate Legends of the Dead rather than ignoring it.

## Reply 46 — participant_040 · 2025-03-18 · post-30239139

Is there a chance that a variant of confederation mechanic will be available for Feudal rulers? Having coalitions against expanding neighbors is one of my greatest wishes for CK3 - it would really enliven the diplomatic gameplay and give the player both some challenge (if they are the conqueror) or fun gameplay (if they are one of the smaller powers that would be gobbled up, but are now able to resist)

## Reply 47 — participant_041 · 2025-03-18 · post-30239140

Should confederations be able to centralize over time? I.e a crown authority level, where you, at say level 3, can gather the confederates together to discuss an offensive war? With various laws such as strong majority, veto right etc? Once at level 4 centralization, they can agree to transform into a custom kingdom or commonwealth.

## Reply 48 — participant_038 · 2025-03-18 · post-30239145

also will confederations mean that Ireland will start in one? in 867

## Reply 49 — participant_009 · 2025-03-18 · post-30239152

<!-- artifact:quote:start -->
> We've added a Culture and Faith specific to your Nomadic Capital, different than your own Click to expand...
<!-- artifact:quote:end -->
This makes me curious, how would culture converting a nomadic realm function? Cause, obviously, the entire realm shouldn't become a different culture just because the ruler changes culture, which you've remedied, but at the same time, it's not as if it makes sense to have you convert every county individually since they're just a representation of the grazing area used by your realm, not of any specific permanent settlement which could change culture. Do you set your steward to the promote councillor task in your capital and the realm gradually changes culture, in proportion to his progress? So if you start with a cuman realm, and your ruler turns kipchak, you'd promote culture this way and gradually see your realm turn more kipchak, which would be proportionally maintained during migrations?

## Reply 50 — participant_042 · 2025-03-18 · post-30239153

So I am wondering why the Khitans are blue instead of their normal green. Is that a new title for them?

## Reply 51 — participant_016 · 2025-03-18 · post-30239162

<!-- artifact:quote:start -->
> IIXBatmanXII said: If I understand correctly, Vikings have not received the capture raid intent. If so, this is very disappointing. Much of the gold gain from raiding is probably made from ransoming prisoners and I am often targeting specific territories in the hopes of capturing the women with good congenital traits who live there to serve as concubines. Not to mention the drive for women and slaves that historians seem to believe fueled the Viking raids. Click to expand...
<!-- artifact:quote:end -->
This is a very fair point. We will add it to Norse tribals.

## Reply 52 — participant_043 · 2025-03-18 · post-30239166

<!-- artifact:quote:start -->
> KAMCITY13 said: All looks good but one thing to mention, the Khitans should be called Great Liao by 1178. Their government was of the Chinese Bureaucratic style and had many Chinese features. They got ran out by the Jurchen Jin but still kept their Chinese style of governance while ruling over different groups in Central Asia. Their rulers had the title of Emperor and/or “Gurkhan” which means universal ruler. In 1178 start date they should not nomadic but have Administrative government. Click to expand...
<!-- artifact:quote:end -->
Thanks for your feedback! The name has already been changed to "Kara Khitai" on the current development branch actually (these screenshots are a few days old), reflecting the new dynastic identity of the refugees of Great Liao after the Jurchen Jin drove them south in 1125. Regarding their government type, I agree that some administrative/nomadic fusion would be most appropriate, but the admin government type from Roads to Power isn't a great fit for them currently. With the China-specific additions coming later in All Under Heaven we might be able to create a better representation for them for this bookmark, but note that high Dominance nomadic gameplay is already quite different from low Dominance. For example, the Kara Khitai won't be migrating with the seasons even though nominally "nomadic". We'll talk more about this in upcoming dev diaries! Gurkhan is a reserved game term in Khans of the Steppe, so to avoid confusion, the ruler of Kara Khitai has the Khagan title at game start - he could certainly claim the Gurkhan title during the game though!

## Reply 53 — participant_044 · 2025-03-18 · post-30239167

Super glad to see that now nomads can get herd from land outside the steppe. I expect that this will of course be generally lower levels than within the steppe proper but still, it's nice. If I may suggest, I think that if a nomad captures a non-steppe country certain buildings like farms or any sort of "agricultural" building should have its income cut by like 90% if held by a nomad government. Obviously if I am trampling the fields and farmlands for my herd, they should not also be getting me gold. Unsure how I feel about the Khitans. Naming debates aside(Khitans, Khara Khitai, Western Liao etc.) I feel like maybe we should just have to wait until All Under Heaven for them to be complete but ideally they would be a settled government with nomad tributaries. In fact honestly maybe a variant government where you can have a herd and "celestial Empire" government at the same time may be necessary then, or some system where non-nomads can make use of herd levies if they have tributaries/vassals from the steppe. Would be useful for 1066 Liao and for Yuan(and I assume the Ilkhanate? I know they had quite a few mongol and turkic tribes operating throughout Persia who still functioned as tribes apart from the persians).

## Reply 54 — participant_045 · 2025-03-18 · post-30239168

So if I understood it correctly regular raiders have pillage (basic raiding) and terrorize, while Vikings on top of that have Adventure, right? Kinda sucks, that not everything, but I'll take what I can. *** Also what's the functional difference between Vassal and Tributary? From what I've seen they look more or the same. For Confederations and Alliances there are some limiters like "you cannot gain new titles" and "they only work in defence, but not in offence".

## Reply 55 — participant_046 · 2025-03-18 · post-30239171

<!-- artifact:quote:start -->
> Conguitosnucleares said: Sounds good, although the Tributary system should be available for Iberia too. A great part of the reasons why Granada survived for 250 years the rest of Al-Andalus is because they paid tributes to Castille. In 1066, at least Sevilla, Granada, Toledo and Zaragoza paid tributes to them. Click to expand...
<!-- artifact:quote:end -->
Maybe they didn’t make tributes general to all govs because it isn’t as fun, but may ability to create tributes could be tied to a cultural tenant to keep different parts of the map feeling distinct.

## Reply 56 — participant_021 · 2025-03-18 · post-30239179

Can Tributaries become Vassals?

## Reply 57 — participant_047 · 2025-03-18 · post-30239182

"We have expanded what we originally scoped for razing" Sounds interesting, what was the original scope for razing?

## Reply 58 — participant_048 · 2025-03-18 · post-30239185

So question with the optional locations for nomads? How nomads feel in smaller locations to the steppes? Somalia for example?

## Reply 59 — participant_043 · 2025-03-18 · post-30239187

<!-- artifact:quote:start -->
> YonosTheManlyManner said: Greatest Dev Team on earth! Thank you for supplying great content. Just one question, compared to administrative, how expansive will nomadics feel and be? What are settlment issues? Thanks! Click to expand...
<!-- artifact:quote:end -->
In my experience with the game, nomadic realms can expand quite a bit and very far compared to other types of realms, to a large extent due to tributaries, the relative ease of capturing land from herders and other, weaker nomads, and the ability to easily relocate your realm. However, it's also easy to lose land for the same reasons. As a result, nomads care less about generational titles than they do herd, land fertility, and relationships. Settlement issues are connected to migration and will be covered in a later dev diary!

## Reply 60 — participant_015 · 2025-03-18 · post-30239190

I also think you should employ the hostages mechanic into the tributary mechanic as well. Very often they were the basis for sustaining such tributary agreements and ensuring the lesser party wouldn't go back on their word.

## Reply 61 — participant_049 · 2025-03-18 · post-30239213

It would be interesting to add the option of strong arming tributaries into becoming vassals through soft power

## Reply 62 — participant_043 · 2025-03-18 · post-30239237

<!-- artifact:quote:start -->
> giorgosth128 said: all very intresting addtions. also any non nomdas that start with tribitaries? the Byzantines for example? Click to expand...
<!-- artifact:quote:end -->
We're looking to add a few Byzantine tributary realms as well as some Slavic tribes paying tribute to East Frankia, at least. If you have other suggestions let us know!

## Reply 63 — participant_050 · 2025-03-18 · post-30239241

<!-- artifact:quote:start -->
> Conguitosnucleares said: Sounds good, although the Tributary system should be available for Iberia too. A great part of the reasons why Granada survived for 250 years the rest of Al-Andalus is because they paid tributes to Castille. In 1066, at least Sevilla, Granada, Toledo and Zaragoza paid tributes to them. Click to expand...
<!-- artifact:quote:end -->
It will be available for clan and feudal goverments too as stated at the start of the dev diary.

## Reply 64 — participant_005 · 2025-03-18 · post-30239243

<!-- artifact:quote:start -->
> hattusa said: Apologies for being unclear. The optional nomadic regions (everything that's not the Great Steppe) will have the generic seasons we've prepared for the steppe that make sense for each, and the content associated with those. For example, the Sahel only has the Drought, Abundant Grazing and Everlasting Summer seasons, as the Zud seasons (blizzard, frozen grass, layers of snow, etc) would make no sense. We will go more over the different Season effects in the next DD. Click to expand...
<!-- artifact:quote:end -->
That makes more sense! Thank you for the further clarifications!

## Reply 65 — participant_051 · 2025-03-18 · post-30239244

The main thing I'm thinking of is a system where a given member of a Confederation can end up turning it into a Kingdom title, if they have the highest dominance or prestige. Perhaps it would be contingent on an event chain triggered by winning a battle, or a Confederation lasting for much longer than it had initially intended to have been.

## Reply 66 — participant_052 · 2025-03-18 · post-30239247

Will Mongol or Turkic will get new army unit models? Just curious

## Reply 67 — participant_043 · 2025-03-18 · post-30239251

<!-- artifact:quote:start -->
> riadach said: Doesn't seem to be anything to distinguish tribal tributaries from feudal ones which is disappointing. Could they be made ephemeral like the nomad tributaries and be broken without automatically resorting to war? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> riadach said: In a previous reply, your colleague mentioned that there could be a decision to turn a confederation into a kingdom of some description. Does that still hold? Click to expand...
<!-- artifact:quote:end -->
Unlike nomadic tributaries, they will be automatically dissolved when the current suzerain dies. They also have a different set of obligations, as well as the requirement for the suzerain to defend them on demand. Those all make a pretty big difference in play! We're still looking into it! Fingers crossed!

## Reply 68 — participant_022 · 2025-03-18 · post-30239255

<!-- artifact:quote:start -->
> lachek said: We're looking to add a few Byzantine tributary realms as well as some Slavic tribes paying tribute to East Frankia, at least. If you have other suggestions let us know! Click to expand...
<!-- artifact:quote:end -->
Local mirs of Dardistan (Bruzha and Baltistan) should be tributaries of Kashmir, if they must be the subjects of Kashmir.

## Reply 69 — participant_015 · 2025-03-18 · post-30239266

<!-- artifact:quote:start -->
> lachek said: Unlike nomadic tributaries, they will be automatically dissolved when the current suzerain dies. They also have a different set of obligations, as well as the requirement for the suzerain to defend them on demand. Those all make a pretty big difference in play! Click to expand...
<!-- artifact:quote:end -->
I understand, but it doesn't differentiate them from Feudal. A lot of the mechanics for Tribals regretfully seems to be just feudal without some bells and whistles. I think tributaries (instead of vassals) and fleshed out confederacies would be a nice way of making playing as tribals a unique experience.

## Reply 70 — participant_043 · 2025-03-18 · post-30239274

<!-- artifact:quote:start -->
> vyshan said: Question: You mention that "Even feudal realms can subjugate neighboring kingdoms to make them pay tribute, if their Crown Authority is high enough" but shouldn't it be a default thing not if you have high authority. Looking at a number of the various realms, like the HRE they had in the early days of the Ottonians when it was founded lots of vassals, Hungary, Bohemia, Poland but only Bohemia would be incorporated into the empire. Likewise with England and Scotland, England tried a number of times to enforce basically a tributary status on Scotland. So how would this be reflected? Click to expand...
<!-- artifact:quote:end -->
It's a bit of a game balance thing: we don't want small or only loosely held together realms to start dominating their neighbors for tribute. Crown / Tribal Authority seemed like a pretty good approximation for the thing you'd need in order to qualify as a suzerain and it plays well. But the system is quite flexible, if you have some other suggestions for what the qualifications could be that feels more fitting and immersive, let us know!

## Reply 71 — participant_053 · 2025-03-18 · post-30239278

On a unrelated topic would it be possible to add some more customer titles to the game? i.e. if I have the vassal with the march special contract can there title be Marquess?

## Reply 72 — participant_054 · 2025-03-18 · post-30239283

Could you please tell me if there will be some changes in Seljuks? Now they feel really weak compared to byzantines. In most games they fail their invasion and than implode.

## Reply 73 — participant_055 · 2025-03-18 · post-30239289

Is it possible to destroy holdings during terror raids? And if not why?

## Reply 74 — participant_056 · 2025-03-18 · post-30239293

<!-- artifact:quote:start -->
> hattusa said: They work like the game rules to make extra Administrative realms in Egypt, the Arabian Empire, Ghana, etc. Click to expand...
<!-- artifact:quote:end -->
Can I ask a stupid question? Do you have to turn on the game rule to make extra Administrative and Nomad realms before the start of the game or is it on by default?

## Reply 75 — participant_057 · 2025-03-18 · post-30239299

I think this is the first dev diary I've ever read from Paradox that includes swear words. To be clear I'm not upset by this, I find it amusing.

## Reply 76 — participant_058 · 2025-03-18 · post-30239303

I know you must be focused on the steppe but the confederation system is perfect for the Italian League. Since in the 1178 start date the various Italian States are already independent could you please open the confederation to them, maybe through culture. It would be really fun Barbarossing across Italy.

## Reply 77 — participant_043 · 2025-03-18 · post-30239305

<!-- artifact:quote:start -->
> Corvids said: You seem to have left out that the Chigils were independent in 1066. Could this be because they get absorbed easily? Click to expand...
<!-- artifact:quote:end -->
The Chigils are represented as tributaries of the Karluks in 1066. They're still technically independent! They're just part of the larger "Karluk realm" visually.

## Reply 78 — participant_022 · 2025-03-18 · post-30239315

I feel that tribal lands of a different culture should become tributaries on succession. So large empires may not blob through the tribes in 867 bookmark.

## Reply 79 — participant_044 · 2025-03-18 · post-30239316

<!-- artifact:quote:start -->
> RoDMaster said: I know you must be focused on the steppe but the confederation system is perfect for the Italian League. Since in the 1178 start date the various Italian States are already independent could you please open the confederation to them, maybe through culture. It would be really fun Barbarossing across Italy. Click to expand...
<!-- artifact:quote:end -->
IIRC confederations are tribal only; maybe in the future Leagues can be a thing of their own for feudal realms. With particular focus for Italy?

## Reply 80 — participant_059 · 2025-03-18 · post-30239317

so like. assuming you become powerful enough to do overland raids on every holding in europe and the middle east without opposition (i do not expect players will have much trouble with this), how many innovations are you likely to come away with per run? have you tested? edit: asking bc my gut here instantly tells me this is WAY too strong and doesnt really make a lot of sense. itd surely be better to have it give innovation PROGRESS rather than just straight unlocking stuff instantly

## Reply 81 — participant_060 · 2025-03-18 · post-30239319

What's the justification for restricting Confederations to Tribal and Nomadic only? Correct me if I'm wrong but wasn't this very common for smaller independent feudal realms as well e.g. Italian cities, Irish alliances, German leagues etc?

## Reply 82 — participant_030 · 2025-03-18 · post-30239320

Does this mean that adventurers can opt to go east and become nomads and then begin to raid? (Or go to the other areas that allow to become nomadic).

## Reply 83 — participant_030 · 2025-03-18 · post-30239324

<!-- artifact:quote:start -->
> Extradaemon said: What's the justification for restricting Confederations to Tribal and Nomadic only? Correct me if I'm wrong but wasn't this very common for smaller independent feudal realms as well e.g. Italian cities, Irish alliances, German leagues etc? Click to expand...
<!-- artifact:quote:end -->
Maybe this is for Chapter 5 and they might have a different name (league?) to differentiate.

## Reply 84 — participant_061 · 2025-03-18 · post-30239331

<!-- artifact:quote:start -->
> 0th Law said: The main thing I'm thinking of is a system where a given member of a Confederation can end up turning it into a Kingdom title, if they have the highest dominance or prestige. Perhaps it would be contingent on an event chain triggered by winning a battle, or a Confederation lasting for much longer than it had initially intended to have been. Click to expand...
<!-- artifact:quote:end -->
Are there any plans to have IMO I'd love if: Confederations gave cultural acceptance when its members are of different cultures. Confederations gave opportunities for opinion buffs and maluses depending on your conduct in the confederation. There was an activity to raise issues / discuss matter with other confederacy members and one of those matters could be the formation of a Kingdom and who should rule it.

## Reply 85 — participant_043 · 2025-03-18 · post-30239343

<!-- artifact:quote:start -->
> riadach said: I understand, but it doesn't differentiate them from Feudal. A lot of the mechanics for Tribals regretfully seems to be just feudal without some bells and whistles. I think tributaries (instead of vassals) and fleshed out confederacies would be a nice way of making playing as tribals a unique experience. Click to expand...
<!-- artifact:quote:end -->
Ah, I'm sorry, I misread you! You're right, tribal and feudal tributaries work the same at the moment (though Tribals can get access to them easier). I'll have a think and see if we can make them more distinct in future updates, thanks for the feedback!

## Reply 86 — participant_043 · 2025-03-18 · post-30239363

<!-- artifact:quote:start -->
> DeanTheDull said: I am going to raise a red-flag here. This will *not* to be fun, from a 'how does it feel to be raided' perspective or from an player-AI balance perspective. In general balance terms, if the AI takes this intent with any regularity, it will cripple the AI compared to players across the world. The military power of tribal and feudal realms is tied to the buildings. The advantage of the raiders is that they already have a MAA-advantage to complete their raids, and thus destroy buildings that might- in aggregate over generations- give the settled folk the ability to resist. As prsented, this is a double-win mechanic to cripple landed AI to the advantage of the nomadic AI. In much the same way that the Adventurers started bankrupting already poor landed nobles and preventing them from upgrading their economies, actively destroying the economies that are being built is worse. This makes it also a weakness for the player-AI balance, because the more the players prioritize their own defense, their AI vassals / neighbors will become weaker. Ease of expansion is already a common issue. Making it easier will not help, nor will making it easier to stabilize and have a more stable frontier vassal by having fewer military buildings. And that's if you are inclined to spend money like that, because this raiding intent also creates a perverse incentive for a player in a liege role to *not* defend the realm against raiders. Vassal instaiblity is driven by relative military strength, regardless of whether you measure that in size or quality. The best way to mitigate troublesome vassals if for their military buildings to be replaced with econ buildings. You cannot do that as a liege absent seizing the conty. You could, however, have raiders do it for yous. A liege's cheap-and-easy strategy for vassal management should not be 'deliberately don't protect them.' It will also not be fun for players anywhere near tribal realms, as the players who want to protect against building destruction- which is to say, anyone in reach of any tribal or especially viking threat- will have to treat each raiding force like a 'we can destroy months / years of income if you don't respond' threat. It won't matter of the risk is low, both in terms of event probability or AI chance to take the intent. Players go out of their way to avoid low risks all the time. What will matter is that the only counter-play to this is to go out and be hyper-aggressive in subjugating the potential raiders so they can't destroy your personal domain investments. If confederations are meant to allow a basis for smaller powers to be too tough to be worth conquering, don't give player powers a reason to be hyper-aggressive against the raiders who can form them. Gold doesn't matter. Hostages are annoying, but a 'liberate kinsmen' casus belli can make for interesting scenarios. (Add more of that, please.) CK2 steppe raiders were annoying enough, but they were just that- annoying. If you make every tribal in the game who can sail or march to your capital a 'we might destroy your expensive investment that takes decades for a return on investment' threat, then players are going to prioritize conquering every tribal in range. Please don't. Click to expand...
<!-- artifact:quote:end -->
That's a good point and we really appreciate feedback like this!! While the AI is already less likely to select the Raze raid intent, we will also make it possible for non-nomad rulers to Purchase Truce with nomad realms to prevent raiding for a limited time. Weaker settled realms might just cave and become tributaries, but stronger ones should be more inclined to buy the nomads off on a semi-regular basis to prevent their investments from damage. What we don't want to do is not make it possible for nomads to burn everything in their path to the ground. The long-term benefit of having your settled opponents weakened by neighboring nomads while you're immune due to paying them off is, however, quite historically appropriate and a decent strategy (at least in the short-term). There's already a lot of game balance changes that will result from Khans of the Steppe due to the very different game dynamics introduced by e.g. herd, land fertility, and seasons, and the game will of course be rebalanced around all of this + the new raid intents.

## Reply 87 — participant_062 · 2025-03-18 · post-30239367

Will we have any throat singing music added?

## Reply 88 — participant_063 · 2025-03-18 · post-30239368

Can you add another category called "confederate members" to some activities that allow you to invite foreign rulers? I wanna jive with the bros without having to pity invite the rest of the neighbours.

## Reply 89 — participant_021 · 2025-03-18 · post-30239370

<!-- artifact:quote:start -->
> lachek said: It's a bit of a game balance thing: we don't want small or only loosely held together realms to start dominating their neighbors for tribute. Crown / Tribal Authority seemed like a pretty good approximation for the thing you'd need in order to qualify as a suzerain and it plays well. But the system is quite flexible, if you have some other suggestions for what the qualifications could be that feels more fitting and immersive, let us know! Click to expand...
<!-- artifact:quote:end -->
My thought is that high crown authority doesn't really fit how the Emperors of the HRE tried to bring other parts of europe under their sway particularly under the ottonian and salians. And also England under various kings tried to reduce Scotland and Wales to tributary status, this would work well IMO for reflecting how Æthelstan of England dealt with Scotland. Maybe tie it into the amount of counties you own, so that way smaller kingdoms like say Wales can't make England a tributary. Maybe tie it into grandur of your court? Empires should IMO always be able to do so, that is kind of what empires are about, especially within the christian context. Though if say Wales was able to defeat their much large foe England when they are smaller and and weaker and force them to pay them tribute for a while, does sound like fun drama story. Maybe it is fine for all? Also related to this how do tributaries work with Adminstrative realms? The Byzantines should not be conquering areas outside of core areas but instead be making them tributaries.

## Reply 90 — participant_043 · 2025-03-18 · post-30239384

<!-- artifact:quote:start -->
> CaptainBritish said: Will we have any throat singing music added? Click to expand...
<!-- artifact:quote:end -->
What kind of expansion would it be if we didn't?

## Reply 91 — participant_064 · 2025-03-18 · post-30239385

Confederations need some mechanics when it comes to centralising and becoming actual tags. It didn't happen often but they should be able to become far more cohesive and become unified, albeit decentralised tags. Maybe it could be done via a decision if all the members are extremely friendly and the confederation has been around for a while. Some examples of this happening historically would be the Magyars, Kipchaks, Xiongnu (debated) and the Haudenosaunee. These federations should act much more like unified tags and if they're nomadic they should also have restrictions on migration. Individual members should still be able to migrate short distances independently (so long as they're still beside their fellow members), but larger migrations would be done as a group. They should form quite rarely (even being hard for the player to form them) and should still be able to break apart, but more in the same way that normal realms break apart.

## Reply 92 — participant_060 · 2025-03-18 · post-30239393

<!-- artifact:quote:start -->
> lachek said: Ah, I'm sorry, I misread you! You're right, tribal and feudal tributaries work the same at the moment (though Tribals can get access to them easier). I'll have a think and see if we can make them more distinct in future updates, thanks for the feedback! Click to expand...
<!-- artifact:quote:end -->
Very much off-topic, but the best idea for a future Tribal update I've seen was to tie them directly into the Cultural Head mechanic. Where your authority as a tribal leader is explicitly based on how much of your own culture you have control of (Since tribals as a catch-all term for pre or non-feudal states derived their power and authority from their ability to unite and protect a group of people with shared cultural, ethnic, and sometimes linguistic ties). If a vassal or neighbour took the title of culture head off you (from for example spreading culture or seizing land), they would automatically usurp the title from you. Would make sense for example that a "King of the Yoruba" would be the culture head of the culture, with other independent or vassal leaders being chiefs, and any vassals culture heads of a different culture retaining their title as "Petty King", since it was common for tribal kings to rule other kings as vassals or tributaries (e.g. Zulu and Xhosa).

## Reply 93 — participant_065 · 2025-03-18 · post-30239412

If possible, could you make Tributary type 3 available to all Admin rulers and make them prioritize this over reckless expansion, especially outside their de jure lands? Would be a great way to balance the current Byzantine blobbing. Also, I think there should be some way that type 3 tributary relationships don’t end with the suzerain’s death - they’re just easier to escape. Maybe a decision whereby the new ruler of each realm can choose to leave - and if both agree to maintain the same status, the relationship continues. Have y’all seen Confederacy behavior working for the Tribal Irish in 867? Protection against the Viking scourge…

## Reply 94 — participant_066 · 2025-03-18 · post-30239417

Can we ditch "the" on the map? I think "Cumans" and "Kirghiz" look better than having "the" in every country in the steppes.

## Reply 95 — participant_067 · 2025-03-18 · post-30239419

it would be fun to make an Open-Invite for Confederation Feast lol it is always easier to convince people when you give them plenty of food and project soft power I love parallel and diverse forms of state-relations like the Tributaries are being done. The more well-structured government and diplomatic relations the better! Will love to see confederations, hostages, marriages, oaths, tributaries, trade rights, defense pacts, vassals, allies, and migrations interacting!

## Reply 96 — participant_068 · 2025-03-18 · post-30239425

Feudals can have tributaries too. What can i say other than "based"? Throwing DD out early was a great success i see, at least for the players.

## Reply 97 — participant_069 · 2025-03-18 · post-30239428

Little by little, it's getting there.

## Reply 98 — participant_070 · 2025-03-18 · post-30239436

<!-- artifact:quote:start -->
> lachek said: Kurultai Click to expand...
<!-- artifact:quote:end -->
Can we expect things for Norse, althing for Iceland, or tribal assemblies in general?

## Reply 99 — participant_071 · 2025-03-18 · post-30239456

Will there be a way to turn a confederation in a more formal realm? I think it would make thematic sense for a confederation be able to turn into a kingdom but initially limited to election succession. This would seem a pretty natural progression.

## Reply 100 — participant_068 · 2025-03-18 · post-30239471

<!-- artifact:quote:start -->
> rasuuru said: Can we expect things for Norse, althing for Iceland, or tribal assemblies in general? Click to expand...
<!-- artifact:quote:end -->
I wouldn't hope for that. This is not "general tribal expansion", this is "this particular region expansion"

## Reply 101 — participant_035 · 2025-03-18 · post-30239472

Will we be able to entice or convince tributaries to switch suzerain via diplomacy? Can a non-nomadic power entice nomadic tribes to change recognition of suzerainty from a nomadic ruler to a sedentary ruler?

## Reply 102 — participant_072 · 2025-03-18 · post-30239477

Will Switzerland be updated to take advantage of the confederation mechanic?

## Reply 103 — participant_031 · 2025-03-18 · post-30239481

<!-- artifact:quote:start -->
> lachek said: That's a good point and we really appreciate feedback like this!! While the AI is already less likely to select the Raze raid intent, we will also make it possible for non-nomad rulers to Purchase Truce with nomad realms to prevent raiding for a limited time. Weaker settled realms might just cave and become tributaries, but stronger ones should be more inclined to buy the nomads off on a semi-regular basis to prevent their investments from damage. What we don't want to do is not make it possible for nomads to burn everything in their path to the ground. The long-term benefit of having your settled opponents weakened by neighboring nomads while you're immune due to paying them off is, however, quite historically appropriate and a decent strategy (at least in the short-term). There's already a lot of game balance changes that will result from Khans of the Steppe due to the very different game dynamics introduced by e.g. herd, land fertility, and seasons, and the game will of course be rebalanced around all of this + the new raid intents. Click to expand...
<!-- artifact:quote:end -->
Maybe the answer is to only allow razing in narrower circumstances: Against someone who has broken a truce/alliance Against someone who refused to be subjugated Against a rival That would help by making razing a retaliatory gesture that's only used for spite, and gives players+AI a defense against it. Eg the Mongols didn't raze enemies for the sake of razing territory, they did it to act as an example so that other cities would give in preemptively. Then the second layer of balance: is it better to raze a dozen Central Asian cities for 1 building each, or to burn every building in Baghdad to the ground...

## Reply 104 — participant_070 · 2025-03-18 · post-30239489

<!-- artifact:quote:start -->
> lachek said: Note that this applies only to members’ defensive wars. They cannot call on the Confederation when they themselves declare offensive wars. Click to expand...
<!-- artifact:quote:end -->
Can confederation members gather and decide to attack someone as one? Will Mogyër Confederation be special exception?

## Reply 105 — participant_073 · 2025-03-18 · post-30239494

It's a shame we can't have confederations for feudal and kings at least. They could be a funny counter against big rising empires. And make the game harder for the player in the late game, as would have more problems to streamroll the AI kingdoms once he has got strong enough (which use to happen in all games) As confederations only create when a big enemy is threating in your borders, I don't think it would affect the gameplay in most scenarios. Only when a big, menacing empire is created.

## Reply 106 — participant_074 · 2025-03-18 · post-30239519

Thanks for all, and please give the option to recruit men-at-arms from vassals to non nomads too. That layballow it to happen like it did historically notably in India with persians or Turks invaders, with the mamluks and other parts of the world where it was not only limited to nomads (even Rome did it)

## Reply 107 — participant_075 · 2025-03-18 · post-30239527

<!-- artifact:quote:start -->
> DeanTheDull said: CK2 steppe raiders were annoying enough, but they were just that- annoying. Click to expand...
<!-- artifact:quote:end -->
While the event had a cooldown per county or holding, as a nomadic raider you could destroy two buildings guaranteed for loot and absolutely annihilate neighbours' attempts to build up their holdings in CK2. This was in addition to raiding in general destroying buildings randomly. How often the AI picks the option, rather than sparing I do not know, not my thing unless I was really poor. I was going to conquer those holdings myself eventually so why kill them? Also less developed holdings had far less gold to loot.

## Reply 108 — participant_052 · 2025-03-18 · post-30239535

Can I have some questions? Will you add Handcannon MaA? Almost everyone know that Mongol brought gunpowder to Europe and Middle-East in 1280

## Reply 109 — participant_076 · 2025-03-18 · post-30239543

Love these new systems, although, I'm a bit disappointed we won't be able to form Confederations out of Feudal governments. While Confederations might be uniquely designed for Tribal and Nomadic cultures and governments, I would still love the opportunity to form the Old Swiss Confederation like it did due to a mutual defensive pact and desire to work together, instead of the current decision.

## Reply 110 — participant_077 · 2025-03-18 · post-30239549

Will more cultures/religions be able to raid? Right now a lot of characters who historically did raid cannot, mostly across the mediterranean (which are not tribals or nomads or pagans).

## Reply 111 — participant_078 · 2025-03-18 · post-30239550

<!-- artifact:quote:start -->
> lachek said: We're looking to add a few Byzantine tributary realms as well as some Slavic tribes paying tribute to East Frankia, at least. If you have other suggestions let us know! Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> The Treaty of Falaise was a forced written agreement made in December 1174 between the captive William I, King of Scots, and Henry II, King of England. The Treaty's provisions affected the Scottish king, nobles, and clergy; their heirs; judicial proceedings, and transferred the castles of Roxburgh, Berwick, Jedburgh, Edinburgh, and Stirling over to English soldiers; in short, where previously the king of Scots was supreme, now England was the ultimate authority in Scotland. During the next 15 years, William was forced to observe Henry's overlordship, such as needing to obtain permission from the English crown before putting down local uprisings. The humiliation for William caused domestic trouble for him in Scotland, and Henry's authority extended as far as picking William's bride. The treaty was annulled in 1189 when King Richard I, Henry's successor, was distracted by his interest in joining the Third Crusade, and William's offer of 10,000 marks sterling. More pre-disposed to William than his father, Richard drew up a new charter on 5 December 1189, known as the Quitclaim of Canterbury, that nullified the Treaty of Falaise in its entirety.​ Click to expand...
<!-- artifact:quote:end -->
A big one I'd recommend is in the 1178 date; England should be the overlord of Scotland under the Treaty of Falaise: It's one of the one's I had represented in my Kingdom of Heaven mod in the past and adds an entirely new dynamic to the British Isles.

## Reply 112 — participant_079 · 2025-03-18 · post-30239562

Hello. The tributary and confederation mechanics look particularly interesting. Tributary contracts will be largely modable since they are based on vassal contracts, but what about confederations? Is it considered a scripted diplomatic relationship between multiple leaders? Will it be easy to modify the effects of a confederation (such as allowing other members to be called to war in an offensive war?) Would it be possible to create new types of confederation?

## Reply 113 — participant_080 · 2025-03-18 · post-30239563

Will the East Slavic vassals of the Khazars in 867 be finally demoted into tributaries? This would more accurately represent the pre-Rus' political landscape and would allow a strong ruler to more easily overthrow their dominance as happened historically. Likewise, will the Sami and "Bjarmians" be turned into herders instead of nomads? We don't exactly know what the herder government type will represent yet, but the name suggests it would be more representative of the socioeconomic order in the far North of Europe.

## Reply 114 — participant_081 · 2025-03-18 · post-30239570

The new content looks interesting. Good dev diary.

## Reply 115 — participant_082 · 2025-03-18 · post-30239580

<!-- artifact:quote:start -->
> lachek said: We're looking to add a few Byzantine tributary realms as well as some Slavic tribes paying tribute to East Frankia, at least. If you have other suggestions let us know! Click to expand...
<!-- artifact:quote:end -->
Great Moravia was basically until Svatopluk took power. Probably all neighbouring Slavic tribes should be East Frankish tributaries but have less knowledge on those Also, did soy consider to add something like confederations for other governments? Yes it would not be that much historical, but I believe game needs such mechanism. AI is extremely passive in facing players snowballing now imho.

## Reply 116 — participant_068 · 2025-03-18 · post-30239582

<!-- artifact:quote:start -->
> Arcvalons said: Will more cultures/religions be able to raid? Right now a lot of characters who historically did raid cannot, mostly across the mediterranean (which are not tribals or nomads or pagans). Click to expand...
<!-- artifact:quote:end -->
Ghazi status lets clans raid since the last update. I wonder if they will extend that to, idk, march contract too? Or some other one, so feudals have that option too.

## Reply 117 — participant_083 · 2025-03-18 · post-30239583

Just to make sure - there are no ranks limitations to tributaries? So for example a Duke can make a King (or even an Emperor) a tributary? Also, I guess that answer for that question will be no, but I will ask it anyway: can adventurers have tributaries?

## Reply 118 — participant_084 · 2025-03-18 · post-30239591

Could you please consider including the Anatolian plateau as a region suitable for nomads via an optional gamerule as well? Much of the post-Manzikert collapse of the ERE cannot be simulated properly, if there are no Turkic nomads who press onto the plateau in search for grazing grounds.

## Reply 119 — participant_085 · 2025-03-18 · post-30239597

<!-- artifact:quote:start -->
> I_have_no_ideas_for_name said: Will the East Slavic vassals of the Khazars in 867 be finally demoted into tributaries? This would more accurately represent the pre-Rus' political landscape and would allow a strong ruler to more easily overthrow their dominance as happened historically. Likewise, will the Sami and "Bjarmians" be turned into herders instead of nomads? We don't exactly know what the herder government type will represent yet, but the name suggests it would be more representative of the socioeconomic order in the far North of Europe. Click to expand...
<!-- artifact:quote:end -->
The herder government is a placeholder.

## Reply 120 — participant_070 · 2025-03-18 · post-30239599

<!-- artifact:quote:start -->
> Benismann said: I wouldn't hope for that. This is not "general tribal expansion", this is "this particular region expansion" Click to expand...
<!-- artifact:quote:end -->
I guess "Kurultai succession" mentioned in the DD is nothing but another elective succession where the voters are subjects with largest herds, and there is no new activity type during which new suzerain is elected or different matters are discussed.

## Reply 121 — participant_008 · 2025-03-18 · post-30239605

What is it? Chinease coin?

## Reply 122 — participant_086 · 2025-03-18 · post-30239624

Love the tributary But I won't lie though that I laugh pretty hard because now tributary subject will have more worth than vassal because at least you can make them join all your war. Not to mention tributary probably contribute more the your realm than vassal too, more gold and less on the useless thing that called levy.

## Reply 123 — participant_087 · 2025-03-18 · post-30239639

<!-- artifact:quote:start -->
> Ksiendzu said: What is it? Chinease coin? View attachment 1267804 Click to expand...
<!-- artifact:quote:end -->
Looks like a paiza to me. It's probably the icon for levels of dominance.

## Reply 124 — participant_088 · 2025-03-18 · post-30239647

<!-- artifact:quote:start -->
> lachek said: That's a good point and we really appreciate feedback like this!! While the AI is already less likely to select the Raze raid intent, we will also make it possible for non-nomad rulers to Purchase Truce with nomad realms to prevent raiding for a limited time. Weaker settled realms might just cave and become tributaries, but stronger ones should be more inclined to buy the nomads off on a semi-regular basis to prevent their investments from damage. What we don't want to do is not make it possible for nomads to burn everything in their path to the ground. The long-term benefit of having your settled opponents weakened by neighboring nomads while you're immune due to paying them off is, however, quite historically appropriate and a decent strategy (at least in the short-term). There's already a lot of game balance changes that will result from Khans of the Steppe due to the very different game dynamics introduced by e.g. herd, land fertility, and seasons, and the game will of course be rebalanced around all of this + the new raid intents. Click to expand...
<!-- artifact:quote:end -->
Failing to protect your vassals lands from raiding should be considered a breach of the Feudal contract, and either weaken the contract obligations and/or cause serious negative opinion modifiers, possibly even Tyranny (with all vassals) if it happens repeatedly. The Liege should really be penalized for not protecting his vassals from raiders.

## Reply 125 — participant_001 · 2025-03-18 · post-30239649

<!-- artifact:quote:start -->
> lachek said: Thanks for your feedback! The name has already been changed to "Kara Khitai" on the current development branch actually (these screenshots are a few days old), reflecting the new dynastic identity of the refugees of Great Liao after the Jurchen Jin drove them south in 1125. Regarding their government type, I agree that some administrative/nomadic fusion would be most appropriate, but the admin government type from Roads to Power isn't a great fit for them currently. With the China-specific additions coming later in All Under Heaven we might be able to create a better representation for them for this bookmark, but note that high Dominance nomadic gameplay is already quite different from low Dominance. For example, the Kara Khitai won't be migrating with the seasons even though nominally "nomadic". We'll talk more about this in upcoming dev diaries! Gurkhan is a reserved game term in Khans of the Steppe, so to avoid confusion, the ruler of Kara Khitai has the Khagan title at game start - he could certainly claim the Gurkhan title during the game though! Click to expand...
<!-- artifact:quote:end -->
Thank you for the response and clarifications! A good book to read up on the Qara Khitai is called: “The Empire of the Qara Khitai in Eurasian History Between China and the Islamic World” ​

## Reply 126 — participant_089 · 2025-03-18 · post-30239653

Any chance of making titles like Khan come after the name of characters, rather than before? Perhaps defined in culture?

## Reply 127 — participant_006 · 2025-03-18 · post-30239657

A Turkic-Karluk still having Mongol style hair.The devs could give them the long dreadlocks which exist since Legacy of Persia.

## Reply 128 — participant_090 · 2025-03-18 · post-30239659

I really like Tributaries and Confederation I always like to see variance to the diplomacy. Raid Intent seems pretty cool, a good way to make raiding feel a little more deliberate. Not exactly sure why only the Nomads are capable of having the idea "raid for prisoners", though. Seeing the UI for Raid Intents really makes wish we could have "Seige Intents" during a regular war as well. Ohviously it would be great to be able to say my main focus is on hostages, and often much rather take supply for my army on the march from a seige than just the gold. Or if I'm especially mad, maybe I turn a blind eye while my levees burn down the capital...

## Reply 129 — participant_091 · 2025-03-18 · post-30239663

Why can't everyone be allowed to confederate?

## Reply 130 — participant_092 · 2025-03-18 · post-30239666

<!-- artifact:quote:start -->
> lachek said: A game rule has been added to include Nomadic governments in the Sahel, Arabia, the horn of Africa, Sami and Karelia regions Click to expand...
<!-- artifact:quote:end -->
So the Sami will turn reindeers into soldiers ​

## Reply 131 — participant_093 · 2025-03-18 · post-30239672

<!-- artifact:quote:start -->
> Sami and Karelia Click to expand...
<!-- artifact:quote:end -->
This is anachronistic and the inclusion of Karelia is kind of bizarre. Saami wouldn't start reindeer herding until the 15th century at the earliest, and Medieval Karelians had nothing do with reindeer herding at all. Not to mention that reindeer herding of Saami, Finns and Karelians of today is much more comparable to pastoralism in more sedentary societies than to the nomadic pastoralism on the steppe. Sure people move around after their herd, but there are no horde riders or might dynamics among different Saami polities.

## Reply 132 — participant_093 · 2025-03-18 · post-30239692

I suggest giving certain vassals such as frontier themes a counter-raid intet, in which you reduce the levy size, levy reinforcement, fertility and supply limit in the holding. You would get prestige, a reduced amount of gold and when appropriate influence or legitimacy. You would also have extra pursuit while raiding, thus inflicting more fatal casualties on retreating enemies. You could only counter-raid in close by counties to your realm, say at most 1 land county away. For maritime themes the range could be 2 sea provinces.

## Reply 133 — participant_094 · 2025-03-18 · post-30239694

I really like that you are making a feudal version of tributaries. It's great to see some new options of exerting influence over the neighboring nations without necessarily having to conquer them. I also like the sound of confederations. It sounds like it might actually make conquering the tribal rulers a bit more of a challenge this way. However, I wish there was a little bit more to it. It would be great to see some of the confederations eventually forming a more unified entity. Though it would probably be weird for the result to always be just another realm with one of the rulers standing on top with the others as their vassals, it would need to be more fleshed out. Either way, it would be nice to have more options of expanding through diplomacy alone.

## Reply 134 — participant_093 · 2025-03-18 · post-30239698

Give Cumania the Kimek treatment and turn it into a confederacy, the Cumans never had a great khan ruling over all of them at once.

## Reply 135 — participant_095 · 2025-03-18 · post-30239709

Shouldnt give the adventure pillage prestige for completing it when you are a nomad too? As the name says its an adventure, you are probably going to far lands and have stories to tell

## Reply 136 — participant_093 · 2025-03-18 · post-30239720

May I request the culture and religion setup for all start dates from the steppe. I would like to give some feedback on that.

## Reply 137 — participant_093 · 2025-03-18 · post-30239723

<!-- artifact:quote:start -->
> Earendil Ardamire said: Why isn't Alania nomadic government if you don't mind me asking? as the Alanian tribes weren't this settled group but constantly moved around and were treated as such by the Georgian Chronicles. Click to expand...
<!-- artifact:quote:end -->
The Alans can hardly be characterized as steppe herders as primarily they were sedentary farmers and pastoralists living in the hills and mountains. Not to mention that they built a lot of castles and churches.

## Reply 138 — participant_096 · 2025-03-18 · post-30239742

How do you take tributaries from your tributaries/can your tributaries defend their tributaries against you while remaining tributaries? Do Confederations stop tribal conversion? Does this solve the persistent problem of West/East Africa converting entirely to Christianity or Islam? Will there be a Confederation "screen" in the Realm section or somewhere else where we can see who is in the confederation, how long they've been in, how likely they are to leave, etc.?

## Reply 139 — participant_093 · 2025-03-18 · post-30239772

Perhaps tribal and nomadic rulers should have access to a very limited amount of vassals. Dukes could have 3, kings 5 and emperors 8. This may sound extremely harsh, but it is to underline the fact that these societies don't work well with feudal style vassalage and make tributaries more attractive. You could greatly raise the cap with tribal authority of course.

## Reply 140 — participant_097 · 2025-03-18 · post-30239776

<!-- artifact:quote:start -->
> lachek said: We're looking to add a few Byzantine tributary realms as well as some Slavic tribes paying tribute to East Frankia, at least. If you have other suggestions let us know! Click to expand...
<!-- artifact:quote:end -->
You could check Iberia a bit, as it was quite common for christians to have muslim tributaries and the other way too

## Reply 141 — participant_098 · 2025-03-18 · post-30239781

Would you be able to make someone of the same tier or even higher tier your tributary ?

## Reply 142 — participant_099 · 2025-03-18 · post-30239794

Administrative realms should probably prioritize forming tributes than outright conquering to counteract their blobbing and to display how historically they didn't really prefer outright conquest. Also please add a generic version of confederations for fuedals and clans, counts and weaker dukes should form leagues to defend against larger scarier antagonistic realms. Think an Islamic league in the Levant joining forces to defend against byzantine expansion, a catholic defensive league in the holy land to defend against saladin, an Italian defense league to defend against the hre or foreign powers expanding into Italy. Maybe they could be heavily restricted to being religious or culturally based coalitions instead of general ones.

## Reply 143 — participant_100 · 2025-03-18 · post-30239797

<!-- artifact:quote:start -->
> lachek said: Thanks for your feedback! The name has already been changed to "Kara Khitai" on the current development branch actually (these screenshots are a few days old), reflecting the new dynastic identity of the refugees of Great Liao after the Jurchen Jin drove them south in 1125. Regarding their government type, I agree that some administrative/nomadic fusion would be most appropriate, but the admin government type from Roads to Power isn't a great fit for them currently. With the China-specific additions coming later in All Under Heaven we might be able to create a better representation for them for this bookmark, but note that high Dominance nomadic gameplay is already quite different from low Dominance. For example, the Kara Khitai won't be migrating with the seasons even though nominally "nomadic". We'll talk more about this in upcoming dev diaries! Gurkhan is a reserved game term in Khans of the Steppe, so to avoid confusion, the ruler of Kara Khitai has the Khagan title at game start - he could certainly claim the Gurkhan title during the game though! Click to expand...
<!-- artifact:quote:end -->
This has probably been adjusted as well then, but in the case it hasn't, have the Khitans also been adjusted to be referred to as Great Liao in the 1066 start date?

## Reply 144 — participant_101 · 2025-03-18 · post-30239804

Please, make the confederation available to feudal and clan. Make my Najdi clan confederation dream a reality

## Reply 145 — participant_102 · 2025-03-18 · post-30239811

Are there any downsides to non nomadic tributaries beyond them breaking the tribute once your character dies? To me, at least, it looks like they're probably going to give a lot more valuable resources (ie everything besides levies, especially gold) than normal feudal and clan vassals do, and I sort of doubt that they'll be that difficult to retain through generations if you can keep making people around you your tributaries through war. Given all of that is correct, then what's there to discourage players from focusing on gathering a ton of tributaries and keeping them under their thumb via war after each of their rulers dies? I really like the look of tributaries so far, as well the roleplay value, but I'm concerned about non nomadic tributaries being such a better option (income wise) compared to normal vassals that it's not worth focusing on anything else 90% of the time.

## Reply 146 — participant_103 · 2025-03-18 · post-30239823

Playing as Normans collecting innovations like Pokemon is now the best strat.

## Reply 147 — participant_104 · 2025-03-18 · post-30239838

<!-- artifact:quote:start -->
> tribnia said: I feel that tribal lands of a different culture should become tributaries on succession. So large empires may not blob through the tribes in 867 bookmark. Click to expand...
<!-- artifact:quote:end -->
Honestly, hardlocking feudal realm to only be able turn tribal into tributaries, then offer them to "feudalize" their realm by paying that development to vassalize them would be a pretty great idea to slow down blobbing rathen than outright handicapping those who want to blob. (since if you don't have money to feudalize this people, they will be independent cause non-nomad tributary system will make them independent). I honestly think this is a great compromise

## Reply 148 — participant_105 · 2025-03-18 · post-30239840

Just for clarification, will my vassals be able to attack my tributaries ?

## Reply 149 — participant_063 · 2025-03-18 · post-30239850

I think giving confederations for republics makes the most sense out of all missing them. Imagine the city-state alliances in Italy. The Lombard League etc

## Reply 150 — participant_085 · 2025-03-18 · post-30239856

Will same title level rulers being able to tributary each other. Aethelstan was able to bring Alba and Strathclyde into tributary relationship. They attempted to rebel, but Anglo Saxon tributary relationship of the two wasn't dissolved until Aethelstan's death

## Reply 151 — participant_106 · 2025-03-18 · post-30239857

Can counties with the Swiss Culture create a Confederation even if technically Feudal?

## Reply 152 — participant_107 · 2025-03-18 · post-30239864

<!-- artifact:quote:start -->
> lachek said: Unlike nomadic tributaries, they will be automatically dissolved when the current suzerain dies. They also have a different set of obligations, as well as the requirement for the suzerain to defend them on demand. Those all make a pretty big difference in play! We're still looking into it! Fingers crossed! Click to expand...
<!-- artifact:quote:end -->
If it did happen, could it be possible for the de jure duchies to be defined by the members of the confederation, rather than just keeping the default duchies (in effect, making new duchies)?

## Reply 153 — participant_108 · 2025-03-18 · post-30239872

Hi. As always, it was a very informative dev diary. I have a couple of questions considering what was written. To become a nomad, should an adventurer be of nomadic culture or can any adventurer adopt a nomadic government? (Haestain the Nomad) Ok, so I see how the subjugation of settled rulers by nomadic ones works. Will it be possible the other way around, i.e. settled rulers subjugating the nomads, like the relations between Black Klobuks and Rus' were in the 10th century? If they do how will it be reflected mechanically, will nomads be your tributaries or vassals? What characteristics will tributaries share with other subjects like vassals? Could I form a new title if titles that needed to form is held not by my vassals but by my tributaries? Also, I have a suggestion to decrease the vassal limit for Tribal rulers so they would be encouraged to use tributaries more.

## Reply 154 — participant_095 · 2025-03-18 · post-30239877

what will happen to a tributary if the leader dies and gets fragmented in various realms?

## Reply 155 — participant_093 · 2025-03-18 · post-30239890

Can you be a tributary of multiple suzerains?

## Reply 156 — participant_080 · 2025-03-18 · post-30239903

<!-- artifact:quote:start -->
> apollo1989vieten said: The herder government is a placeholder. Click to expand...
<!-- artifact:quote:end -->
No it's not? Unless I misunderstood you, the first DD for the update mentions that the unplayable herder government will be a core part of the new nomadism mechanics.

## Reply 157 — participant_108 · 2025-03-18 · post-30239905

<!-- artifact:quote:start -->
> Slime99 said: Can you be a tributary of multiple suzerains? Click to expand...
<!-- artifact:quote:end -->
My guess is no as it clearly uses the same system as vassalage.

## Reply 158 — participant_085 · 2025-03-18 · post-30239907

<!-- artifact:quote:start -->
> I_have_no_ideas_for_name said: No it's not? Unless I misunderstood you, the first DD for the update mentions that the unplayable herder government will be a core part of the new nomadism mechanics. Click to expand...
<!-- artifact:quote:end -->
Every single county has to have some government type. Herders move in when nomads move out and are unplayable.

## Reply 159 — participant_093 · 2025-03-18 · post-30239911

<!-- artifact:quote:start -->
> Sky _Talez said: My guess is no as it clearly uses the same system as vassalage. Click to expand...
<!-- artifact:quote:end -->
I wonder if it would even be plausible. I mean, can a member of a confederation be a tributary? I think the two use similar systems.

## Reply 160 — participant_090 · 2025-03-18 · post-30239916

Something confederations might be useful for is that it could basically disable Conquest CB against members of your own culture (except maybe in rare cases like a rivalry). This could also come with a drastic reduction of demense for tribals. Maybe even when your culture is united under a single confederation you lead, you can then make the choice to become a King through religious reformation. That way, if you want to unite the tribes of your people, you have to play the diplomatic game some, and save the wars of expansion for outsiders. I just am always thinking of ways tribal can be different, and could more reflect the idea that you are playing a people and families and less so a government.

## Reply 161 — participant_109 · 2025-03-18 · post-30239928

With Tributaries is it possible for them to become vassals? Admittedly I recall some stuff in antiquity of Tributaries joining their overlord willingly so was curious if it was possible to make Tributaries and peacefully or "peacefully" work them into your Empire or Kingdom.

## Reply 162 — participant_080 · 2025-03-18 · post-30239935

<!-- artifact:quote:start -->
> apollo1989vieten said: Every single county has to have some government type. Herders move in when nomads move out and are unplayable. Click to expand...
<!-- artifact:quote:end -->
Well yeah, but the "Herders" also, seemingly, represent decentralized nomadic tribes who live in small settlements peacefully grazing their lands as opposed to the "Nomad" governments which have centralized authority and participate in trade and warfare. The former is more representative of the traditional Sami lifestyle, so wouldn't it make sense to make them into herders?

## Reply 163 — participant_108 · 2025-03-18 · post-30239944

<!-- artifact:quote:start -->
> Slime99 said: I wonder if it would even be plausible. I mean, can a member of a confederation be a tributary? I think the two use similar systems. Click to expand...
<!-- artifact:quote:end -->
I believe that it is two different systems. Confederation is using a diplomacy system and tributaries are using a system that was used only for vassals before, that's why both vassals and tributaries are called subjects now. Besides they explicitly said in the dev diary that to form or become part of the confederation you need to not be a tributary. So tough luck.

## Reply 164 — participant_093 · 2025-03-18 · post-30239947

<!-- artifact:quote:start -->
> I_have_no_ideas_for_name said: Well yeah, but the "Herders" also, seemingly, represent decentralized nomadic tribes who live in small settlements peacefully grazing their lands as opposed to the "Nomad" governments which have centralized authority and participate in trade and warfare. The former is more representative of the traditional Sami lifestyle, so wouldn't it make sense to make them into herders? Click to expand...
<!-- artifact:quote:end -->
Saami were not reindeer herders at this time.

## Reply 165 — participant_086 · 2025-03-18 · post-30239957

<!-- artifact:quote:start -->
> Forgetfulman said: Are there any downsides to non nomadic tributaries beyond them breaking the tribute once your character dies? To me, at least, it looks like they're probably going to give a lot more valuable resources (ie everything besides levies, especially gold) than normal feudal and clan vassals do, and I sort of doubt that they'll be that difficult to retain through generations if you can keep making people around you your tributaries through war. Given all of that is correct, then what's there to discourage players from focusing on gathering a ton of tributaries and keeping them under their thumb via war after each of their rulers dies? I really like the look of tributaries so far, as well the roleplay value, but I'm concerned about non nomadic tributaries being such a better option (income wise) compared to normal vassals that it's not worth focusing on anything else 90% of the time. Click to expand...
<!-- artifact:quote:end -->
While I already raise some concern about this and it's probably not historical in Europe but when All Under Heaven release, this play style will be rather appropriate to SEA. The downside of large amount of tributaries will probably be that when it rains it pour aka cascading tributaries declare independence war when you lose enough wars/battles. Might not be that much of a problem for veteran player but it's a risk nonetheless, a major one too.

## Reply 166 — participant_070 · 2025-03-18 · post-30239959

<!-- artifact:quote:start -->
> Vasiklios said: Would you be able to make someone of the same tier or even higher tier your tributary ? Click to expand...
<!-- artifact:quote:end -->
Yeah, can count Hasteinn make king Charles his tributary?

## Reply 167 — participant_110 · 2025-03-18 · post-30239984

Will tributaries count towards your vassal limit? (In which case I suppose it'd become "subject limit") It'd be odd considering you're not actually governing them.

## Reply 168 — participant_111 · 2025-03-18 · post-30240074

It's a pity that the Caucasus, especially its northern part, has not been developed again. And judging by everything, it is unlikely to be developed now. There have been additions about Persia, Byzantium, and now about the nomads. That is, literally about all the regions around the Caucasus. And judging by the screenshots, the number of provinces hasn't changed, and no new states have been added. And there's really no hope for such an option

## Reply 169 — participant_085 · 2025-03-18 · post-30240114

<!-- artifact:quote:start -->
> I_have_no_ideas_for_name said: Well yeah, but the "Herders" also, seemingly, represent decentralized nomadic tribes who live in small settlements peacefully grazing their lands as opposed to the "Nomad" governments which have centralized authority and participate in trade and warfare. The former is more representative of the traditional Sami lifestyle, so wouldn't it make sense to make them into herders? Click to expand...
<!-- artifact:quote:end -->
But that would also make them unplayable. Having them as optional nomads is better.

## Reply 170 — participant_028 · 2025-03-18 · post-30240180

<!-- artifact:quote:start -->
> lachek said: That's a good point and we really appreciate feedback like this!! While the AI is already less likely to select the Raze raid intent, we will also make it possible for non-nomad rulers to Purchase Truce with nomad realms to prevent raiding for a limited time. Weaker settled realms might just cave and become tributaries, but stronger ones should be more inclined to buy the nomads off on a semi-regular basis to prevent their investments from damage. What we don't want to do is not make it possible for nomads to burn everything in their path to the ground. The long-term benefit of having your settled opponents weakened by neighboring nomads while you're immune due to paying them off is, however, quite historically appropriate and a decent strategy (at least in the short-term). There's already a lot of game balance changes that will result from Khans of the Steppe due to the very different game dynamics introduced by e.g. herd, land fertility, and seasons, and the game will of course be rebalanced around all of this + the new raid intents. Click to expand...
<!-- artifact:quote:end -->
Thank you for acknowledging my concern. I appreciate it, and recognize you and the team's concern from the other direction. I recognize what you intent is, and acknowledge it is both legitimate and something that players will want to do. If I might raise some measure that might mitigate my concern, while leaving it inline with what I believe your intent is? (Disregard as you please, of course.) (Soft) Limits on Terror-Raiding 1 - Message Criteria: Have distinct UI pop ups for if your realm or your domain is being raided Reason: Players with larger realms might not want to be bothered defending larger realms, but make it a priority alert to know if their own domain is in trouble 2 - Purchase Truce cost-balancing: Raid-truces might scale off of the raider's base income, not the landed rulers (larger) income Reason: Current truce purchases are scaled by the proposers income. In 867 in particular, this contributes to poor rulers remaining too poor to invest in econ buildings, especially since more gold costs will likely arise. Smaller gold costs for nomads will help with the higher likelihood* of more nomad truces being necessary. *Particularly since the raider you purchased a truce from may migrate, or have vassals who are not covered by the truce, or there are so many raiders who can range you. This is particularly true with the Norse. 3 - Clearly signal Terrorize raiders with distinct graphics / sounds / etc. Reason: If Terror-raiders are easily identifiable at a glance (such as fire / pillage effect, and a screams-of-terror effect if zoomed in), it will help distinguish them from other, less concerning raiders. Ideally this might also be visible at sea, such as some storm-cloud effect around terror-vikings. 4 - Gate Terror-raiding behind traits, perks, or relationships Reason: Rather than a weighted chance systems (that presumably would favor, but not limit, certain traits), have terror-raiding gated to specific character aspects that can be recognized by inspecting characters. Say that a character requires certain traits (sinful / violent traits like Wrathful, Sadistic, Greedy, etc.), going a bit down certain lifestyles (Overseer, Torturer, and Avaricious), or a particular character relationship (rivalry, house feud). In the last case, perhaps a special AI planning so that rivals will pursue it only against certain hated enemies, but will try to raze as much of that character's domain, and family domain, as possible. 5 - Ensure hostages (generally) prevent terror raiding (by prioritizing capture-raiding) If possible, taking hostages from raider-realms should have them prioritize capture-raiding in future raids on you, so that they try to capture (free) any hostages and take your own family hostage. Aside from being a way to prevent the worst raids, it opens up a space for family feuds, especially if paired with a rescue casus belli below. Victim-focused measures to deal with raiding 1 - Provide a small legitimacy for defeating raiders, and vassal benefits for countering terror-raiders in particular. Reason: This gives players a an incentive to hunt-down the raiders going after vassals, and mitigates gold/income losses for the AI who do the same. In the current model the main reward for countering raiders is the gold recovered. Legitimacy could substitute. Gaining vassal hooks / favor for defending their lands / recovering their family could help. 2 - Increase acceptance for Head of Faith gold requests / charity acts for terror raid victims to rebuild Reason: This could leverage religion / culture systems to help mitigate raider costs. For the appropriate faiths, an ability to get a lump sum of money after a raid could help restart reconstruction. *This would likely need a script so that the AI would not only ask for the gold, but actually use the gold for construction, unlike the current AI which often won't spend gifted gold on buildings due to income concerns. 3 - Provide a chance to take-back prisoners taken by raiders you defeat in the field Reason: This could provide an interesting way to get characters out of raider-jail and play internal realm politics. Currently, prisoners from raid teleport to the dungeons of the raider. If a short-term tag were added, then perhaps taking out the army that captured them could reverse the capture, transferring them to the victor instead. This could provide interesting choices, such as options to release a vassal's family member for leverage, free people for relations, kill them for reasons, or just rescue family members you landed in the realm. 4 - Provide raid-victims a window for a rescue-pursuit cassus belli Reason: A rescue cassus belli is a way to have wars to mitigate the raids, without conquering them. Cassus belli that don't require / directly allow conquest should be encouraged over those that occupy more of the map. Additionally, this could cover a gap with the 'there's no way to take back your wife who was made concubine of a raider,' which annoying. Having a window of opportunity- say you can launch a pursuit / rescue casus belli until the nomads return home and demobilize- would incentive immediate responses, but not require you to literally catch the raiding army before it returns home like chasing the raiding army itself might. 5 - Provide a 'Punishment Expedition' casus belli to target / force no-raid truces on top-level lieges (and weaken their dominance) Reason: A bit historical, in that the Chinese had various campaigns to mitigate potential nomadic threats. This could be a role players want to play, by using this casus belli after a raid to force a raid truce and cripple the target's ability to exert dominance.

## Reply 171 — participant_102 · 2025-03-18 · post-30240183

<!-- artifact:quote:start -->
> Nevars said: While I already raise some concern about this and it's probably not historical in Europe but when All Under Heaven release, this play style will be rather appropriate to SEA. The downside of large amount of tributaries will probably be that when it rains it pour aka cascading tributaries declare independence war when you lose enough wars/battles. Might not be that much of a problem for veteran player but it's a risk nonetheless, a major one too. Click to expand...
<!-- artifact:quote:end -->
Id honestly hope that, since there's already being multiple types of tributaries, that there'd be a special version for SEA and Indonesia that would make that type of playstyle viable in those regions or for those cultures, and the generic type of tributary that any culture/ government type can have would be it's own thing. My own ideas (obviously very close to what's already here lol, it's just small changes) for it would be that the general tributaries that you could have as the king of France or something would mostly be kept in line by your military strength and performance in wars and battles, provides a good bit less gold than a vassal and no levies, but also provides prestige, doesn't contribute to the vassal limit that we have now, and of course isn't kept as a subject between generations, maybe also there could be a tributary limit for only those generic tributaries. That way they're still worth it to get and serves a purpose, but it's more worth it to first get the most amount of vassals that you can before getting tributaries. And maybe you could get a year long truce with each tributary you lose whenever succession happens, but, admittedly, that could be an annoyance after a certain point and probably not the greatest idea of the bunch.

## Reply 172 — participant_112 · 2025-03-18 · post-30240191

Adventurers can become nomads but can nomads become adventurers? Or are they stuck in that government type until succession like admin rulers - who have to give up their court, wealth, and artifacts (unless they start the arduous process of sending them to favorite child) ?

## Reply 173 — participant_104 · 2025-03-18 · post-30240217

<!-- artifact:quote:start -->
> Nevars said: While I already raise some concern about this and it's probably not historical in Europe but when All Under Heaven release, this play style will be rather appropriate to SEA. The downside of large amount of tributaries will probably be that when it rains it pour aka cascading tributaries declare independence war when you lose enough wars/battles. Might not be that much of a problem for veteran player but it's a risk nonetheless, a major one too. Click to expand...
<!-- artifact:quote:end -->
Pretty sure they said SEA will get Mandala/unique government, so I think they will intergate this there with this government. Though the size of the expansion does worry me about how fleshed out this government will be.

## Reply 174 — participant_113 · 2025-03-18 · post-30240245

<!-- artifact:quote:start -->
> Koppel235 said: View attachment 1267814 A Turkic-Karluk still having Mongol style hair.The devs could give them the long dreadlocks which exist since Legacy of Persia. Click to expand...
<!-- artifact:quote:end -->
Turks/Turkics did not only use Seljuk style dreadlocks, these types of strange partly shaven hair styles and braids were also always popular among Turks too. There is even a thing called “Turk head” in European heraldry with a hair style like this. You can google it

## Reply 175 — participant_114 · 2025-03-18 · post-30240254

can we please get a client state type of tributary for admin realms? with more flexibility and directives to specialize them as needed. less about extracting wealth from the land and more about providing a buffer state against other large empires.

## Reply 176 — participant_113 · 2025-03-18 · post-30240255

1. As another user also mentioned; literally in every single 1066 game nothing ever happens in Anatolia. Seljuks attack Byzantine Empire for Greater Armenia region, sometimes they win sometimes they lose, they take Greater Armenia region and in few years they are getting attacked by someone or they get in a civilwar and collapse in few decades. That is happening because AI have no reason to invade inner anatolia. It would be nice if you guys try to change something here, like making some more nomadic Turkmen adventurer tribes living in Seljuk realm who wants to invade new territories for to make them grazing lands or making some of the Seljuks vassals nomads in search for grazing lands (which was the actual case in the history) And for that to work out, central anatolia also should be made a fertile grazing land too 2. A wide ranging cultural and ethnicity pack for different regions and cultures of Eurasian steppe. Like Manchu and Cumans were not wearing same stuff and their DNAs were also pretty different from each other. I trust ck3 staff on this and I think I am already seeing some variation in phenotypes. That’s pretty cool.

## Reply 177 — participant_015 · 2025-03-18 · post-30240283

I would also like if consideration could be given to confederations based on dynasty and ancestry. The Eoghanacht of Munster were such a confederation, likewise the Uí Néill, (the Rurikids too?). The head of the dynasty would thus be head of the confederation. Similarly the head of a confederation based on culture should be lead by the cultural ahead. Perhaps if the first two members of a federation are of the same dynasty that the confederation would share the dynasty name. There's great potential for this mechanic but I do think it needs padding out a little.

## Reply 178 — participant_115 · 2025-03-18 · post-30240302

<!-- artifact:quote:start -->
> lachek said: We're looking to add a few Byzantine tributary realms as well as some Slavic tribes paying tribute to East Frankia, at least. If you have other suggestions let us know! Click to expand...
<!-- artifact:quote:end -->
Maybe for Abbasids in some form, although maybe on the VERY low end of the tribute scale (like Aghlabids). And maybe for Tulunids around Hejaz and the Libyan Coast?

## Reply 179 — participant_063 · 2025-03-18 · post-30240306

<!-- artifact:quote:start -->
> riadach said: I would also like if consideration could be given to confederations based on dynasty and ancestry. The Eoghanacht of Munster were such a confederation, likewise the Uí Néill, (the Rurikids too?). The head of the dynasty would thus be head of the confederation. Similarly the head of a confederation based on culture should be lead by the cultural ahead. Perhaps if the first two members of a federation are of the same dynasty that the confederation would share the dynasty name. There's great potential for this mechanic but I do think it needs padding out a little. Click to expand...
<!-- artifact:quote:end -->
There can also be a case for confederate partition succession laws.

## Reply 180 — participant_116 · 2025-03-18 · post-30240313

Since current Dev Diary is about Confederations, Cumans Should be a confederation with Kipchaks. as at least one other people (ngl didn't read after page 1) has mentioned NOTE: Below are a lot of things that would've been links but I can't post them due to a warning of "Spams", some are wikipedia, rest comes from Prosopography of the Byantine World (pbw2016) Speaking of Cumans and since the upcoming DLC is about Nomads, There should be Cuman-Kipchaks in both Georgia and Byzantine Empire and by the 1178 start date, some of those in Georgia should already be "de-Kipchakized" but possibly not the ones in BE. Wikipedia on Georgian Kipchaks is Kipchaks in Georgia is named Kipchaks_in_Georgia A couple of Cuman pronoia holders from 1181 as examples of Byzantine Cumans, in the narrative section you can find more pronoia holders. Baltzanares Komanopoulos, name tells it all. Pbw person 143148 Masout Armenopoulos, his name suggests he has Armenian ancestry as well. PBW person 143437 Cumans should also have lighter skin and hair colors. Wikipedia Cumans Appearance (again, can't post link) Since DLC is about nomads and I've already mentioned Cumans settling in BE, let us not forget that Pechenegs have also been settled in BE in huge numbers, in their hundreds of thousands, possibly and in fact, in 1066 start Pechenegs (ones settled south of Danube). Kegen(or perhaps named Tegenes, called Ioannes Kegen after baptism, who successfuly fought of Uzes on several occasions got the backing of 2 tribes when Tyrach wanted to murder him due to his success to Byzantine Empire with 2 tribes backing him, against 11 backing Tyrach, after being defeated, went to BE with 20.000 supporters. After several eventful years, Tyrach flees to BE with his entire nation, which at one point said to number 800.000. They both die in 1050, during the Pecheneg revolt: some Pechenegs rebel because Emperor wants to resettle them, Tyrach joins the rebel Pechenegs and is defeated and presumably dies, Kegen is sent to the Pechenegs as an emissary and murdered by them, Pechenegs are rather successful and defeat Byzantines time after time until a plague hits them and they make peace, possibly one granting them great autonomy so they can(ones settled in BE) also be made tributaries in 1066. Wikipedia articles on Ioannes Kegen and Tyrach (which are rather lackluster) are Ioannes_Kegen Tyrach Wikipedia article on Pecheneg revolt (which doesn't mention the plague, can't find the source I read it atm) Pecheneg_revolt Although Tyrach has no known family beside his father Bilter, or at least I couldn't find them, Kegen has known family which can be added for 1066 start as Tyrach and his father Bilter PBW person 108496 PBW person 106844 Kegen, his father Baltzar and his two sons Goulinos and Baltzar PBW person 107514 PBW person 106734 PBW person 107201 PBW person 106733 There are also other known Pechenegs of Byzantine Empire close to 1066 start date, for example Anna Komnene mentions two Pecheneg chieftains who rule Bitzina/Vicina in 1083 and these two allow Pechenegs who remain north of the Danube and were pressed by Uzes to cross south, and the new coming Pechenegs later ravage Byzantine land. PBW person 156755 PBW person 156756 Traulos, a former "Manichean"(Paulician) who was a servant of Alexios Komnenos is apparently also a part of this ravaging and his second wife was the daughter of a Pecheneg chieftain, perhaps a daughter of one of the two above. PBW person 161179 Edit: Also, Magyar Migration should be adjusted, it is NOT the result of Magyars defeating Bulgars but instead Magyars being defeated by Bulgars and their Pecheneg allies, and Pechenegs migrating to Magyar territory, pushing them. Pecheneg themselves were pushed westwardby Oghuz, who were allied with Khazars and defeated Pechenegs, so in reality it should be Pecheneg migration first, Magyar migration second.

## Reply 181 — participant_117 · 2025-03-18 · post-30240315

Maybe when in a Confederation Dominance could be replaced by some kind of "Confederation Centralization" track shared by all members, which could be changed on cooldown by either the strongest member or someone with a hook on them upon doing great deeds like leading the Confederation to win a war or the like, which could then lead to the creation of a united Kingdom or Empire at the highest levels.

## Reply 182 — participant_118 · 2025-03-18 · post-30240319

Maybe you can add the ability to increase development to the "Capture" intent (as in the event that is already in the game). After all, in addition to the capture of “important” hostages, it would be logical that slaves were also captured.

## Reply 183 — participant_119 · 2025-03-18 · post-30240329

With Tributaries perhaps there can be a bit of flavor added to the 1066 bookmark for Spain? Parias, the tribute the muslim taifas gave to the christian kingdoms were a large factor in inter-faith conflict on who recieves this money. When Ferdinand the Great died in 1065 his children all inherited Parias from the taifas in Badajoz, Toledo, and Zaragoza.

## Reply 184 — participant_034 · 2025-03-18 · post-30240352

<!-- artifact:quote:start -->
> Liberal3000 said: Maybe you can add the ability to increase development to the "Capture" intent (as in the event that is already in the game). After all, in addition to the capture of “important” hostages, it would be logical that slaves were also captured. Click to expand...
<!-- artifact:quote:end -->
I’m thinking and hoping what they’ll do for Norse tribal is exchange the nomad only portion for development. Probably development wasn’t included because it was a nomad only intent and development is tied to the country and not the nomadic state.

## Reply 185 — participant_034 · 2025-03-18 · post-30240377

<!-- artifact:quote:start -->
> hattusa said: This is a very fair point. We will add it to Norse tribals. Click to expand...
<!-- artifact:quote:end -->
Thanks! If you don’t mind a follow up, is it inclined to be reduced gold & prestige as the other tribal intents posted, or will it be gold & a small boost to development akin to the current “bounteous plunder”/“skilled slaves” event? It seems the later might be more appropriate to represent that the goal for a viking historically was more to capture thralls as opposed to targets for ransom.

## Reply 186 — participant_120 · 2025-03-18 · post-30240405

May be a bit out of place... But since the devs are taking their time to make some changes and improvements to Tribal whilst implementing Nomads, it is a good opportunity to finally add that much requested unique court room for tribal Norse kings and emperors.

## Reply 187 — participant_121 · 2025-03-18 · post-30240419

The change raid intent is such a good idea. Hope the implementation is good also!! There are sometimes when neighbours wrong me and I honestly don´t feel like the current game mechanics always allow you to really get revenge. The ´terrorize´ option could really add some nice gameplay and RP elements. Very very cool!!

## Reply 188 — participant_122 · 2025-03-19 · post-30240457

What are the title tier requirements for tributaries? Does a tributary have to be a lower title than their suzerain or can they be equal. (King paying tribute to a King, for example) Can they even be a higher tier?

## Reply 189 — participant_123 · 2025-03-19 · post-30240460

<!-- artifact:quote:start -->
> and you have a chance to learn innovations of a culture as you raid a settlement if they know about something you do not (though the chances are quite low). Click to expand...
<!-- artifact:quote:end -->
I was just thinking, a less rare but small boost to innovation progress in that tech might be nicer that suddenly learning an innovation on a very small chance. Not sure how others would feel about that though.

## Reply 190 — participant_124 · 2025-03-19 · post-30240499

<!-- artifact:quote:start -->
> Conguitosnucleares said: Sounds good, although the Tributary system should be available for Iberia too. A great part of the reasons why Granada survived for 250 years the rest of Al-Andalus is because they paid tributes to Castille. In 1066, at least Sevilla, Granada, Toledo and Zaragoza paid tributes to them. Click to expand...
<!-- artifact:quote:end -->
This man is right haha. This is a great time to touch up the Taifas properly.

## Reply 191 — participant_093 · 2025-03-19 · post-30240560

I propose a new kind of tributary, the nominal vassal. This tributary provides zero taxes, but may call their liege to a defensive war, after which the vassal will be revassalized if there are no further defensive wars. If the liege refuses, the vassal gains full independence. The liege may also join wars of the nominal vassal to the same result. The vassal may also be revassalized using the offer vassalization interaction with an increased acceptance. The liege may visit the vassal capital while traveling and doing so grants an event where the vassal can be revassalized. Nominal vassals may also be invited to activities, and doing so also revassalizes them. Nominal vassals may also assert independence, which causes an opinion hit to the nominal liege and grants you legitimacy. This requires high legitimacy and costs prestige to do, but grants a big chunk of legitimacy. Doing so grants the nominal liege a casus belli to revassalize the nominal vassal for 5 years and no truce. Refusing to join a coronation also triggers independence and so does refusing revassalization. Nominal vassals form upon exclave independence, but vassals may also slip away upon succession if they are outside of liege de jure, the authority law is at it's lowest level possible, the vassal has high legitimacy/governor efficiency and the new liege has low legitimacy. The vassal will get an event where they may choose to become a nominal vassal if they desire independence. Doing so causes no penalties to their liege, but means they lose the perks of being a vassal. Remaining a part of the realm will grant the vassal a slight opinion modifier for their liege and some prestige and legitimacy/influence when appropriate. AI should heavily weigh internal claims and their relation to the realm. Administrative vassals should be very reluctant to becoming nominal vassals as they lose their administrative government type if it is no longer valid. Essentially the independence faction weighing but slightly tweaked. There are contract levels to nominal vassals in regards to tributary war support, forced, optional and none. The first one calls the nominal liege to all defensive wars, the second has it as an option and the third makes it no longer possible. Changing the obligation level costs prestige and requires high legitimacy when going further away from the liege, but costs legitimacy when going closer. The nominal liege doesn't need to approve of these changes and cannot change the contract. As for historical nominal vassals, I think the biggest example is Venice and the Byzantine Empire. This would have no tributary war support. Sardinia would also fall under this and have optional war support. It could also apply to Kievan Rus in 1066, but doing so would mean that the optional war support should not result in automatic vassalization. The automatic vassalization would thus be restricted to forced war support, and this would also apply to activities and other interactions that would result in vassalization short of offering it.

## Reply 192 — participant_090 · 2025-03-19 · post-30240634

<!-- artifact:quote:start -->
> X_FloW said: i dont like how the tributaries look like a realm under rebellion Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Pigposting said: Huh. So if the Plunder raid intent can steal innovations, does that mean tribal cultures can move past tribal era but still remain tribal? That and confederations, it might be possible for "late game" tribal governments to actually thrive. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DeanTheDull said: I am going to raise a red-flag here. This will *not* to be fun, from a 'how does it feel to be raided' perspective or from an player-AI balance perspective. - snip - Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> AHumpierRogue said: If I may suggest, I think that if a nomad captures a non-steppe country certain buildings like farms or any sort of "agricultural" building should have its income cut by like 90% if held by a nomad government. Obviously if I am trampling the fields and farmlands for my herd, they should not also be getting me gold. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Slime99 said: Perhaps tribal and nomadic rulers should have access to a very limited amount of vassals. Dukes could have 3, kings 5 and emperors 8. This may sound extremely harsh, but it is to underline the fact that these societies don't work well with feudal style vassalage and make tributaries more attractive. You could greatly raise the cap with tribal authority of course. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Forgetfulman said: Given all of that is correct, then what's there to discourage players from focusing on gathering a ton of tributaries and keeping them under their thumb via war after each of their rulers dies? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> rboetto said: Will tributaries count towards your vassal limit? (In which case I suppose it'd become "subject limit") It'd be odd considering you're not actually governing them. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> DeanTheDull said: Thank you for acknowledging my concern. Click to expand...
<!-- artifact:quote:end -->
Maybe dotted lines for internal border could look better. Makes me wonder if it is possible for small amount of tech progress could be gained from battles with armies using techs you don't have. Just personally want to say, I do like the idea of things actually getting worse and destroyed, because that happened a lot in history and it is pretty hard for things to regress in the current systems in the game. The only regression is large countries breaking apart, but economically not so much changes when that happens. I haven't seen yet, but i hope we have a way to raze our holdings (over time, not instant destroy, like unbuilding basically) to make places good for the herd. I think now that we are getting other kinds of diplomacy, vassal limit could across the board be turned down. I wish that the big thing about vassals was they are basically automatic allies and that you can call them to defensive wars. It makes no sense some random Viking comes and takes half of France because my Vassals just let themselves get conquered. I think that it should. I represents your diplomatic infrastructure either way. These are all great ideas, even if in principle as I said above I like that raiding can be a threat to infrastructure.

## Reply 193 — participant_110 · 2025-03-19 · post-30240645

This is unrelated to the dev diary, but will we still be able to play in the old map? Asking because I want to know if I want to rush Lingua Franca right now.

## Reply 194 — participant_125 · 2025-03-19 · post-30240661

All the follow up stuff is very exciting. This is shaping up well. I hope that some time in the future the confederation mechanic might become useful for some kind of high king mechanic. I'd love to see the Irish and welsh have their own little ways of forming a defensive block.

## Reply 195 — participant_068 · 2025-03-19 · post-30240684

<!-- artifact:quote:start -->
> I_have_no_ideas_for_name said: No it's not? Unless I misunderstood you, the first DD for the update mentions that the unplayable herder government will be a core part of the new nomadism mechanics. Click to expand...
<!-- artifact:quote:end -->
Yes they are. In a sense that the devs had to make them because the game really, really dislikes when counties have no holders. They're essentially just a no mans land, except with a character attached. Do you really want sapmi to have no army and be just a conquest-fodder? Do you? Same with 3.5 people who asked for welsh herders.

## Reply 196 — participant_126 · 2025-03-19 · post-30240730

Will vassals be able to attack/raid neighbors that are tributaries of their liege? If so, it kind of defeats the purpose of becoming a tributary in the first place.

## Reply 197 — participant_127 · 2025-03-19 · post-30240755

<!-- artifact:quote:start -->
> lachek said: Thanks for your feedback! The name has already been changed to "Kara Khitai" on the current development branch actually (these screenshots are a few days old), reflecting the new dynastic identity of the refugees of Great Liao after the Jurchen Jin drove them south in 1125. Regarding their government type, I agree that some administrative/nomadic fusion would be most appropriate, but the admin government type from Roads to Power isn't a great fit for them currently. With the China-specific additions coming later in All Under Heaven we might be able to create a better representation for them for this bookmark, but note that high Dominance nomadic gameplay is already quite different from low Dominance. For example, the Kara Khitai won't be migrating with the seasons even though nominally "nomadic". We'll talk more about this in upcoming dev diaries! Gurkhan is a reserved game term in Khans of the Steppe, so to avoid confusion, the ruler of Kara Khitai has the Khagan title at game start - he could certainly claim the Gurkhan title during the game though! Click to expand...
<!-- artifact:quote:end -->
Any chance of getting Khitan split into Mongolic Khitans and Sinicized Khitans? Right now the Khitans we have speak Mongolic but half of their name bank is Chinese. It feels weird, like Egyptian.

## Reply 198 — participant_128 · 2025-03-19 · post-30240768

can nomad still burn holding to create more grazing land

## Reply 199 — participant_015 · 2025-03-19 · post-30240813

<!-- artifact:quote:start -->
> klopkr said: All the follow up stuff is very exciting. This is shaping up well. I hope that some time in the future the confederation mechanic might become useful for some kind of high king mechanic. I'd love to see the Irish and welsh have their own little ways of forming a defensive block. Click to expand...
<!-- artifact:quote:end -->
I imagine in the 867 startdate, Ivor the Boneless is going to push a lot of Irish tribes into a confederation anyway. But there should be confederations and tributary relationships there already. Airgialla should be in a tributary relationship with Aed Findliath as its suzerain. One could change Aed from Duke of Meath to Duke of Ulster(more accurately 'The North' or 'In Tuaiscert' or 'In Fochla') in confederation with Flann Sinna as Petty King of Meath. Similarly the Eoghanacht provinces of Munster should also be in a confederation, with Ormond as the leading member. A Dal gCais dynasty member should read be in Ennis and remain aloof from this arrangement.

## Reply 200 — participant_129 · 2025-03-19 · post-30240873

I read it but I didn't find anything interesting to be honest. Total apathy for the first time since launch.

## Reply 201 — participant_130 · 2025-03-19 · post-30240876

I still think Tributaries should work with Vikings as well...

## Reply 202 — participant_131 · 2025-03-19 · post-30240879

<!-- artifact:quote:start -->
> IIXBatmanXII said: A couple questions/concerns: It seems that making the color and name of a tributary may make it difficult to discern both how much of your territory is tributaries relative to actual vassals and difficult to for other players to discern what parts of your realm are potentially more vulnerable to falling away since they are mere tributaries. Is this information not important to the player due to the way tributaries function? Would it perhaps make more sense to stripe the territory color or something so that it becomes clearer? If I understand correctly, Vikings have not received the capture raid intent. If so, this is very disappointing. Much of the gold gain from raiding is probably made from ransoming prisoners and I am often targeting specific territories in the hopes of capturing the women with good congenital traits who live there to serve as concubines. Not to mention the drive for women and slaves that historians seem to believe fueled the Viking raids. Click to expand...
<!-- artifact:quote:end -->
It`s not a warcrime if warcrimes have not been invented yet XD

## Reply 203 — participant_132 · 2025-03-19 · post-30240887

I'm surprised there hasn't been any looting for artifacts.

## Reply 204 — participant_133 · 2025-03-19 · post-30241044

Why not apply confederation to Crusader Countries?

## Reply 205 — participant_134 · 2025-03-19 · post-30241055

It'd be nice if feudal realms could also form confederations under certain conditions, like the historic Swiss Confederation in 1241. Maybe lock it behind some innovation? It might make sense to tie that with some tradition granting pike men-at-arms (Pike Square), which the Swiss also currently can't get, even though they famously had them historically.

## Reply 206 — participant_068 · 2025-03-19 · post-30241098

<!-- artifact:quote:start -->
> tokinoha said: Why not apply confederation to Crusader Countries? Click to expand...
<!-- artifact:quote:end -->
Because it's not "countries", it's one kingdom. I dont think you would be able to confederate with your own vassals

## Reply 207 — participant_085 · 2025-03-19 · post-30241123

<!-- artifact:quote:start -->
> Benismann said: Because it's not "countries", it's one kingdom. I dont think you would be able to confederate with your own vassals Click to expand...
<!-- artifact:quote:end -->
It’s not so in 1178. Not all the crusader states are controlled by the kingdom of Jerusalem.

## Reply 208 — participant_135 · 2025-03-19 · post-30241157

I look at the maps in these dev diaries and see the vast majority of the steppe being ruled by Turkic tribes - which will receive no flavor. It is super weird.

## Reply 209 — participant_136 · 2025-03-19 · post-30241216

<!-- artifact:quote:start -->
> lachek said: It's a bit of a game balance thing: we don't want small or only loosely held together realms to start dominating their neighbors for tribute. Crown / Tribal Authority seemed like a pretty good approximation for the thing you'd need in order to qualify as a suzerain and it plays well. But the system is quite flexible, if you have some other suggestions for what the qualifications could be that feels more fitting and immersive, let us know! Click to expand...
<!-- artifact:quote:end -->
As I see it, the fact that tributaries of non-nomadic realms automatically expire on ruler death should be enough to keep things from getting out of hand, but, if you think there needs to be further limitations, then perhaps, rather than low crown authority outright forbidding tributaries, it could instead allow the tributaries to voluntarily end the relationship whenever they feel it to be no longer beneficial.

## Reply 210 — participant_087 · 2025-03-19 · post-30241330

<!-- artifact:quote:start -->
> Callid said: It'd be nice if feudal realms could also form confederations under certain conditions, like the historic Swiss Confederation in 1241. Maybe lock it behind some innovation? It might make sense to tie that with some tradition granting pike men-at-arms (Pike Square), which the Swiss also currently can't get, even though they famously had them historically. Click to expand...
<!-- artifact:quote:end -->
Wouldn't the Swiss Confederation members be considered republics rather than feudal? I bet there will be a league mechanic for republics whenever the eventual dlc comes out that makes them playable.

## Reply 211 — participant_137 · 2025-03-19 · post-30241379

Considering that there is now some fertility outside of the steep, a settled ruler should be able to give land to a nomad or allow them to graze in their territory and in exchange they become either allies or a subject, making them join wars on the side of their "liege", like the cummans with hungry.

## Reply 212 — participant_134 · 2025-03-19 · post-30241381

<!-- artifact:quote:start -->
> Videogames said: Wouldn't the Swiss Confederation members be considered republics rather than feudal? I bet there will be a league mechanic for republics whenever the eventual dlc comes out that makes them playable. Click to expand...
<!-- artifact:quote:end -->
It was both, IIRC, and even abbeys and the like. Hence the idea of tying it to a (cultural? regional?) innovation.

## Reply 213 — participant_138 · 2025-03-19 · post-30241784

Regarding the Plunder raid intent, do we get to capture all innovations? Like Cultural and Regional ones such as Longboats and Wootz Steel? Can we also get advanced innovations beyond our culture's era since tribals (and I assume Nomads would as well) are barred from advancing era

## Reply 214 — participant_093 · 2025-03-19 · post-30241812

Here's some historical confederations: Pecheneg-Bashkir confederation in 867 I think a cool mechanic would be a raid casus belli that depletes the fertility of the target area. Another cool mechanic to follow up this is spawning adventurers who take a part of the herd to wander elsewhere in search of new land without spawning in herders. This way the Pecheneg migration to the west could be simulated like thus: The Khazars and Oghuz Yabgu begin a war against the Pechenegs around 892. If they win, the Pecheneg fertility will plummet, and two migratory bands will spawn. One of them will attack the Magyars, and the other will go settle among the Khazars. If the Magyars lose the war against the Pecheneg migratory band, they will attack the Bulgarians for Pannonia. The Pechenegs will take over Yedisan. If the Magyars win, there will be no migration to the west. The Khazar Pechenegs request land on the Dnieper, and will become Khazar tributaries in doing so. The Khazar vassal there will be angered by this, and the area will flip to Pecheneg. If the Khazars refuse, the Pechenegs will declare a war on them. This is the territory the Pechenegs will demand. Here's the areas of the Kimek confederation in 867. This simply shows the cultures, the areas should be split up a lot, those being Kipchak, Kimek and Laktan. I think some sort of cascading effect happening around the 1030s where Kipchaks migrate en masse into the Pontic Steppe would be appreciated, and I hope it happens dynamically anyways. Here's the Cuman-Kipchaks in 1066. The Kimeks should remain in the Irtysh region as it has only been about 30 years since they lost the primacy in the confederation. Cumans can form as a hybrid between Kipchaks and Oghuz. Perhaps there should be a Qangli culture on the Syr darya too to represent a more urbanized Kipchak population there. The Qangli would become very important in the next century after all. Here's 1178 The Kimeks were apparently absorbed (or maybe were the ancestors of) the Qangli as Qangli are mention to neighbor the Naimans on the Irtysh. There doesn't seem to be that many references to the Kimeks from the 12th century anyways that aren't obviously discussing an earlier time period. The areas outlined in green are under the Khwarezmians and the county outlined by magenta is under the Kara Khitai. Perhaps more counties should be added to accommodate the Qangli here, but alas. All of these confederations make me wish for some laws that enable leaders and offensive war declaration too. It would be neat to not only have confederations as a defensive pact but also and offensive one. I think migratory bands should remain part of the confederation if they settle close enough to the old one, or they should rejoin that confederation if possible with high acceptance.

## Reply 215 — participant_093 · 2025-03-19 · post-30241837

This post has a lot of my sources: https://forum.paradoxplaza.com/forum/threads/steppe-culture-changes-no-county-setup-changes.1728474/

## Reply 216 — participant_093 · 2025-03-19 · post-30241891

<!-- artifact:quote:start -->
> The active formation of a common culture for all variants is in no way a reason to deny the fact that the northernmost of them, the forest-steppe variant, is noticeably different from the others. Perhaps I. I. Lyapushkin is right, explaining this primarily by anthropological differences: most people who lived in forest-steppe settlements and buried their dead in the burial grounds located next to them were dolichocranic. Their anthropological, and therefore ethnic, proximity to the Alans of the Ciscaucasia determined the similarity of the culture of this variant with the Alan culture. The Alans who came to the Don basin from the foothills settled on lands that were close to them in physical and geographical features: the high chalk spurs of the right bank of the rivers served them for the construction of fortified settlements, spacious and flat, often with a slightly sloping surface, dry areas were used for the placement of settlements and burial grounds. The Alans brought with them an economic way of life (sedentary, agricultural), certain skills in house-building, weapons, ceramics and many other things, and most importantly, the ability to make them, i.e. handicraft production: ceramics, blacksmithing, jewelry. There are several hypotheses about the reasons for the penetration of the Alans into the Don basin. The first is that the Alans retreated to the Don forest-steppe under pressure from the Khazars in the 7th century (Lyapushkin, 1958), the second is that they left the Ciscaucasia regions devastated by Arab troops in the middle of the 8th century (Pletneva, 1967, p. 91), and the third is that the Alans were forcibly resettled in the second half of the 8th century by the Khazar government to the northern outskirts of the Khaganate, since at that time they were in vassal dependence on the rulers of Khazaria (Gadlo, 1979, p. 193; Mikheev, 1985, p. 97). The Alans occupied vast lands of the Don forest-steppe (see Fig. 4). In this territory, at the end of the 1960s, 75 monuments were known: hillforts, settlements, burial grounds (Pletneva, 1967, pp. 191-194, Fig. 5). At present, their number has doubled (Afanasyev, 1987, pp. 168-184). The list published by G.E. Afanasyev in 1987 indicates 277 numbers, which means that the number of monuments has increased not twofold, but more than threefold. But it should be taken into account that the author slightly changed the numbering system. Afanasyev gave separate numbers to all the objects that, according to Pletneva, constituted single "nests" and therefore received one common number. Thus, the 1967 list grew by 28 monuments. In addition, newly discovered monuments, which were included in both previously allocated and new "nests", also received their numbers. Such an accounting of monuments, adopted by the compilers of the Codes, is certainly more legitimate. It should be noted that on Oskol, where the teacher of the Volokonovskaya school A.G. Nikolaenko conducted extremely energetic explorations for many seasons, the number of monuments has actually tripled compared to 1967. Click to expand...
<!-- artifact:quote:end -->
Change the county setup to allow for the forest-steppe variant of Saltovo-Mayaki culture. The people here were Alans who survived up until the Mongol era around Kharkiv. А.З. Винников, С.А. Плетнёва. «На северных рубежах Хазарского каганата. Маяцкое поселение» :: Глава I. Салтово-маяцкая культура и ее лесостепной вариант — северная окраина хазарского каганата А.З. Винников, С.А. Плетнёва. «На северных рубежах Хазарского каганата. Маяцкое поселение» :: Глава I. Салтово-маяцкая культура и ее лесостепной вариант — северная окраина хазарского каганата hagahan-lib.ru http://archtat.ru/content/uploads/2023/10/AVUR-5-tom-18.09.2023-kopiya.pdf

## Reply 217 — participant_093 · 2025-03-19 · post-30241906

The Khazar capital Itil should be located here. It would later become Saqsin, a trade hub consisting of various small emirates. Saqsin was predominantly Muslim Oghuz. ДВАДЦАТЬ ЛЕТ ИССЛЕДОВАНИЙ САМОСДЕЛЬСКОГО ГОРОДИЩА: РЕЗУЛЬТАТЫ, ПРОБЛЕМЫ, ИНТЕРПРЕТАЦИЯ Исполнилось 20 лет с момента начала раскопок на Самосдельском городище в дельте Волги. В статье подводятся итоги работы Самосдельской экспедиции на памятнике, который ассоциируется с остатками средневекового торгового города Саксина, до сих пор известного только по отдельным упоминаниям в... cyberleninka.ru НАХОДИЛСЯ ЛИ САКСИН В СОСТАВЕ ДЕШТ-И-КЫПЧАК? Статья посвящена истории Нижнего Поволжья в Х-XVII в. Население Нижнего Поволжья (Сакси-на) было полиэтничным. Его можно разделить на местное и иноземное. К местным жителям относились огузы и потомки хазар, к иноземному населению - волжские булгары и аланские колонисты. Саксин не являлся частью... cyberleninka.ru

## Reply 218 — participant_139 · 2025-03-19 · post-30242286

Do I understand correctly that the nomads will not have cities? If so, then this is a bit silly, the nomads always had cities, these cities served as control centers and trading points, the khans mostly sat in cities, the only thing is that the nomad cities were more often destroyed by other nomads. You can add cities, at least historical one, or allow them to be founded, as feudal lords can.

## Reply 219 — participant_125 · 2025-03-19 · post-30242385

<!-- artifact:quote:start -->
> riadach said: I imagine in the 867 startdate, Ivor the Boneless is going to push a lot of Irish tribes into a confederation anyway. But there should be confederations and tributary relationships there already. Airgialla should be in a tributary relationship with Aed Findliath as its suzerain. One could change Aed from Duke of Meath to Duke of Ulster(more accurately 'The North' or 'In Tuaiscert' or 'In Fochla') in confederation with Flann Sinna as Petty King of Meath. Similarly the Eoghanacht provinces of Munster should also be in a confederation, with Ormond as the leading member. A Dal gCais dynasty member should read be in Ennis and remain aloof from this arrangement. Click to expand...
<!-- artifact:quote:end -->
Yes! But feudal Ireland should retain confederations too I think. And that's where I think a special high kingship mechanic could come into play.

## Reply 220 — participant_140 · 2025-03-20 · post-30242496

<!-- artifact:quote:start -->
> We have made it possible to grow your herd if you hold lands outside of the Steppe, giving those counties Fertility if held by a nomad Click to expand...
<!-- artifact:quote:end -->
THANK YOU!!!

## Reply 221 — participant_141 · 2025-03-20 · post-30242596

It'd be S-tier if ya'll could add a game rule to automatically start the player realm as Nomadic regardless of location just like with Administrative. I really wanna roleplay as a certain blue-faced hobo in Scotland fighting for independence from English rule...

## Reply 222 — participant_108 · 2025-03-20 · post-30242668

<!-- artifact:quote:start -->
> SupremeFeline said: It'd be S-tier if ya'll could add a game rule to automatically start the player realm as Nomadic regardless of location just like with Administrative. I really wanna roleplay as a certain blue-faced hobo in Scotland fighting for independence from English rule... Click to expand...
<!-- artifact:quote:end -->
Why should you be nomadic to roleplay as him?

## Reply 223 — participant_141 · 2025-03-20 · post-30242672

<!-- artifact:quote:start -->
> Sky _Talez said: Why should you be nomadic to roleplay as him? Click to expand...
<!-- artifact:quote:end -->
Nomads just sound better than adventurers. I never really liked them. Maybe it's closer to Robert the Bruce while he was in exile? Whatever I just wanna play nomadic Scots don't question my logic.

## Reply 224 — participant_141 · 2025-03-20 · post-30242676

You know, if they're going to keep adding new government types like Celestial and whatever the heck Japan will be (Shogunate?) in the Asia expansion, at that point might as well add a "start as realm type" option at custom ruler/realm selection at game start and include feudal/clan/tribal, at least so if a "start as realm type" game rule is active in multiplayer it doesn't affect those who don't want it. Like, say I wanted to start as Celestial HRE (Mandate of Actual Heaven moment, Even Holier Roman Empire jumpscare) and my friends wanted to be Clan Byzantium, Administrative Norway, and Nomadic France (this is sounding more cursed by the moment but that's what's so beautiful about it). First I need friends. But I play 4X games so that's difficult...

## Reply 225 — participant_015 · 2025-03-20 · post-30242743

<!-- artifact:quote:start -->
> klopkr said: Yes! But feudal Ireland should retain confederations too I think. And that's where I think a special high kingship mechanic could come into play. Click to expand...
<!-- artifact:quote:end -->
I'm not sure. By the 11th century, the administrative powers of the Irish kings had grown and they were lords of their own provinces not merely primus inter pares. Outside of their own provinces, it's more difficult. In the late 11th century, after the death of Diarmait Mac Maíl na mBó and the rise of Tairelbach Ua Briain, Leinster was dominated by Munster but still managed to return to full independence in the 12th. Perhaps tributary relationships would suffice to represent the High Kingship. My issue at the moment is that Paradox is designing confederations as a peaceful coalescence of threatened polities looking for mutual defence. Campaigns for a united High Kingship in the 11th and 12th century couldn't be further from this. They were wars for dominance. (Although oddly, there is an argument for this in the mid-13th century).

## Reply 226 — participant_015 · 2025-03-20 · post-30242748

<!-- artifact:quote:start -->
> Sky _Talez said: Why should you be nomadic to roleplay as him? Click to expand...
<!-- artifact:quote:end -->
I assume for funsies.

## Reply 227 — participant_142 · 2025-03-20 · post-30242934

It took me a moment to understand why "target's boldness" gave +50 reason to accept. I get it, it works, it kind of makes sense, but I think it would be cool if tooltips like that could change depending on the value so when the boldness acceptance value is positive it says "Target's cowardice"

## Reply 228 — participant_093 · 2025-03-20 · post-30242980

I think dissolution and independence factions should heavily weigh in liege weakness like tributaries. It was often moments of defeat that led to the downfall of a realm. Finding a way to implement dynamic collapse of a title through conquest in the style of the 4th crusade would also be nice, perhaps if the liege loses their entire personal domain vassals may choose to become independent unless crown authority is high enough to allow for revocation.

## Reply 229 — participant_143 · 2025-03-20 · post-30243050

Confederations being tribal/nomadic makes sense, but damn it would be cool to make the actual swiss confederacy, instead of it just being a regular kingdom title creation. If confederations would be allowed for feudal vassals of the HRE, it would be cool if you could only form switzerland if you have the whole thing in a confederation.

## Reply 230 — participant_093 · 2025-03-20 · post-30243067

I propose that the terrorize raid intent also plummets fertility.

## Reply 231 — participant_093 · 2025-03-20 · post-30243076

I think it would be cool for there to be an actual counterraid mechanic where you can raid border counties of the realm raiding you while the raid is still active. You would not get much loot, but you would destroy the local levy size and supply limit.

## Reply 232 — participant_144 · 2025-03-20 · post-30243077

I think the game needs 2 new systems: A New Tribal Identification System and a Semi-Nomadic State 1. Tribal identification Mechanics It is proposed to introduce an additional tribal identification mechanic. A tribe is essentially a group of people with common ancestors. Nomadic states were formed from various tribal alliances, where all members of a tribe were considered part of a single lineage. Since the game focuses on dynasties, creating genealogical trees for tens of thousands of people would be impractical, especially with the constant emergence of new NPCs. Instead, a unique mechanic or trait system could be introduced to instantly determine a character’s tribal affiliation—whether they belong to a specific dynasty or are an independent NPC. This is important because, in nomadic societies, tribal affiliation played a decisive role in a person's status and future. Depending on their tribal background, individuals could be treated better or worse. Even today, tribal ties remain central to the politics of many nations, especially among Arab, Kurdish, and some Turkic communities. In essence, Arab clans are also societies of people with shared ancestry. 2. Semi-Nomadic States Most Turkic and Mongol states cannot be classified as fully nomadic or fully sedentary. Rulers and administrations governed from cities, while a significant part of the army, consisting of their own tribe, maintained a nomadic lifestyle. Examples: Seljuks, Hulaguids, Emperors of China from the line of Genghis Khan, Ilkhanids, Safavids, Ottomans, Qajars... — a large portion of their armies remained nomadic, while governance followed a feudal structure.

## Reply 233 — participant_093 · 2025-03-20 · post-30243082

<!-- artifact:quote:start -->
> keriefie said: Confederations being tribal/nomadic makes sense, but damn it would be cool to make the actual swiss confederacy, instead of it just being a regular kingdom title creation. If confederations would be allowed for feudal vassals of the HRE, it would be cool if you could only form switzerland if you have the whole thing in a confederation. Click to expand...
<!-- artifact:quote:end -->
Can vassals form confederations? Not to mention do they or should they need to? The liege is supposed to take care of them. This was obviously not always true so maybe vassal confederations could only form if internal wars are allowed.

## Reply 234 — participant_093 · 2025-03-20 · post-30243112

On a serious note I think a good counterplay to raiders will be vassals capable of raiding themselves. Maybe these vassals should also have a CB to subdue close by raiders into a truce with the liege.

## Reply 235 — participant_093 · 2025-03-20 · post-30243115

If war declaration is not sanctioned, vassals should be unable to raid rulers with an alliance or a truce with their top liege.

## Reply 236 — participant_016 · 2025-03-20 · post-30243129

<!-- artifact:quote:start -->
> SupremeFeline said: It'd be S-tier if ya'll could add a game rule to automatically start the player realm as Nomadic regardless of location just like with Administrative. I really wanna roleplay as a certain blue-faced hobo in Scotland fighting for independence from English rule... Click to expand...
<!-- artifact:quote:end -->
Sadly this is not possible. To make the Nomadic Government work you need a "Nomadic Area" with Fertility and Seasons, and we cannot currently create those on the fly. You can, however, become a landless Robert the Bruce, move to a Herder county, take the decision to become a Nomad and strive to become Genghis Khan, thus leading the Nomadic Scots to glory, which should be your main goal.

## Reply 237 — participant_093 · 2025-03-20 · post-30243133

<!-- artifact:quote:start -->
> hattusa said: Sadly this is not possible. To make the Nomadic Government work you need a "Nomadic Area" with Fertility and Seasons, and we cannot currently create those on the fly. You can, however, become a landless Robert the Bruce, move to a Herder county, take the decision to become a Nomad and strive to become Genghis Khan, thus leading the Nomadic Scots to glory, which should be your main goal. Click to expand...
<!-- artifact:quote:end -->
To be fair the DD mentioned that nomads build up fertility in the counties they own.

## Reply 238 — participant_145 · 2025-03-20 · post-30243250

Recruiting MAA from tributary sounds not particularly convenient... I think if players could order vassals of different cultures to specifically train certain MAAs( in some costs), then let players recruit them, it might be a better idea?

## Reply 239 — participant_146 · 2025-03-20 · post-30243320

<!-- artifact:quote:start -->
> Slime99 said: I think it would be cool for there to be an actual counterraid mechanic where you can raid border counties of the realm raiding you while the raid is still active. You would not get much loot, but you would destroy the local levy size and supply limit. Click to expand...
<!-- artifact:quote:end -->
Since raiders are considered hostile to you for a few months (6?) after they leave your land, can't you siege one of their counties (assuming that aren't too far away and you can siege the holding in less than 6 months)? With some luck you might even capture the raider

## Reply 240 — participant_087 · 2025-03-20 · post-30243337

<!-- artifact:quote:start -->
> hattusa said: You can, however, become a landless Robert the Bruce, move to a Herder county, take the decision to become a Nomad and strive to become Genghis Khan, thus leading the Nomadic Scots to glory, which should be your main goal. Click to expand...
<!-- artifact:quote:end -->
Can there be a cultural requirement to do this? Not just anyone has the skills to follow a nomadic way of life, and I think it makes for good storytelling if someone from Western Europe has to adapt to new cultural ways before being able to pull off such a transition.

## Reply 241 — participant_068 · 2025-03-20 · post-30243405

<!-- artifact:quote:start -->
> LeSingeAffame said: Since raiders are considered hostile to you for a few months (6?) after they leave your land, can't you siege one of their counties (assuming that aren't too far away and you can siege the holding in less than 6 months)? With some luck you might even capture the raider Click to expand...
<!-- artifact:quote:end -->
No. You can't siege "hostile" realms.

## Reply 242 — participant_093 · 2025-03-20 · post-30243572

<!-- artifact:quote:start -->
> LeSingeAffame said: Since raiders are considered hostile to you for a few months (6?) after they leave your land, can't you siege one of their counties (assuming that aren't too far away and you can siege the holding in less than 6 months)? With some luck you might even capture the raider Click to expand...
<!-- artifact:quote:end -->
I think you can start raiding if it's available to you, but you can't raid if you otherwise can't. So rulers who don't have it as an option cannot counter-raid. But enabling that is what I was thinking of exactly.

## Reply 243 — participant_093 · 2025-03-20 · post-30243583

<!-- artifact:quote:start -->
> Videogames said: Can there be a cultural requirement to do this? Not just anyone has the skills to follow a nomadic way of life, and I think it makes for good storytelling if someone from Western Europe has to adapt to new cultural ways before being able to pull off such a transition. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> We've added a Culture and Faith specific to your Nomadic Capital, different than your own Click to expand...
<!-- artifact:quote:end -->
Perhaps this means that the local culture and faith will be used when becoming a nomad through a herder county, and I think it would be immersive if that did happen.

## Reply 244 — participant_085 · 2025-03-20 · post-30243590

<!-- artifact:quote:start -->
> Slime99 said: I think you can start raiding if it's available to you, but you can't raid if you otherwise can't. So rulers who don't have it as an option cannot counter-raid. But enabling that is what I was thinking of exactly. Click to expand...
<!-- artifact:quote:end -->
There should be some allowance for counter measures while raiders are still hostile. Let me avenge the Viking raiding Wessex without actively declaring war. I think that you cannot counter raid until the hostility time goes away.

## Reply 245 — participant_108 · 2025-03-20 · post-30243829

<!-- artifact:quote:start -->
> SupremeFeline said: Nomads just sound better than adventurers. I never really liked them. Maybe it's closer to Robert the Bruce while he was in exile? Whatever I just wanna play nomadic Scots don't question my logic. Click to expand...
<!-- artifact:quote:end -->
We don't kinkshame here.

## Reply 246 — participant_093 · 2025-03-20 · post-30243890

I propose that there be laws for confederations. Nothing too crazy. I hope at least. Offensive wars: No joining Joining enabled Joining forced War declaration: No restriction Confederate allies can't be targeted Complete approval (requires offensive war joining to be enabled or forced) Majority approval (requires offensive war joining to be enabled or forced) Leader approval (requires a leader and offensive war joining to be enabled or forced) Leader: None Elected Member seniority Hereditary Confederate migration: Confederate leaves upon migration Confederate may remain if settles close to the confederation Voting type: Complete approval Majority approval Leader approval (requires a leader) Confederation cohesion: Basic leaving penalties Increased leaving penalties, confederates gain extra prestige per month Severe leaving penalties, confederates gain even more prestige per month Each of these laws requires a big chunk of prestige to pass. Each voter not only takes into account their opinion of the proposer but also their opinion on the proposal. Confederates will be very hesitant in declaring a leader, increasing the confederation cohesion and changing the voting type to be more restricted. The laws will influence the willingness to stay within a confederation or joining it, but confederation cohesion will make the confederation stabler due to the harsher penalties but also the enticing prestige gain. If the confederation has a leader, severe leaving penalties, offensive war calling is either enabled or forced and war declaration requires approval, then the confederation can unite into a single realm. This requires a lot of dominance on the steppe or prestige and a high legitimacy level otherwise. Voting type is also taken into account. Vassals who don't want to become a part of the new realm will immediately leave the confederation. The new title will be either an appropriate uncreated de jure title or a titular one.

## Reply 247 — participant_044 · 2025-03-20 · post-30244416

<!-- artifact:quote:start -->
> Slime99 said: Here's some historical confederations: Pecheneg-Bashkir confederation in 867 View attachment 1268327 I think a cool mechanic would be a raid casus belli that depletes the fertility of the target area. Another cool mechanic to follow up this is spawning adventurers who take a part of the herd to wander elsewhere in search of new land without spawning in herders. This way the Pecheneg migration to the west could be simulated like thus: The Khazars and Oghuz Yabgu begin a war against the Pechenegs around 892. If they win, the Pecheneg fertility will plummet, and two migratory bands will spawn. One of them will attack the Magyars, and the other will go settle among the Khazars. If the Magyars lose the war against the Pecheneg migratory band, they will attack the Bulgarians for Pannonia. The Pechenegs will take over Yedisan. If the Magyars win, there will be no migration to the west. The Khazar Pechenegs request land on the Dnieper, and will become Khazar tributaries in doing so. The Khazar vassal there will be angered by this, and the area will flip to Pecheneg. If the Khazars refuse, the Pechenegs will declare a war on them. This is the territory the Pechenegs will demand. View attachment 1268331 Here's the areas of the Kimek confederation in 867. This simply shows the cultures, the areas should be split up a lot, those being Kipchak, Kimek and Laktan. I think some sort of cascading effect happening around the 1030s where Kipchaks migrate en masse into the Pontic Steppe would be appreciated, and I hope it happens dynamically anyways. View attachment 1268340 Here's the Cuman-Kipchaks in 1066. View attachment 1268346 The Kimeks should remain in the Irtysh region as it has only been about 30 years since they lost the primacy in the confederation. Cumans can form as a hybrid between Kipchaks and Oghuz. Perhaps there should be a Qangli culture on the Syr darya too to represent a more urbanized Kipchak population there. The Qangli would become very important in the next century after all. Here's 1178 View attachment 1268348 The Kimeks were apparently absorbed (or maybe were the ancestors of) the Qangli as Qangli are mention to neighbor the Naimans on the Irtysh. There doesn't seem to be that many references to the Kimeks from the 12th century anyways that aren't obviously discussing an earlier time period. The areas outlined in green are under the Khwarezmians and the county outlined by magenta is under the Kara Khitai. Perhaps more counties should be added to accommodate the Qangli here, but alas. All of these confederations make me wish for some laws that enable leaders and offensive war declaration too. It would be neat to not only have confederations as a defensive pact but also and offensive one. I think migratory bands should remain part of the confederation if they settle close enough to the old one, or they should rejoin that confederation if possible with high acceptance. Click to expand...
<!-- artifact:quote:end -->
I feel like the confederation mechanic we see is clearly not designed to represent confederations like this. Confederations are supposed to be for realms of tribals and nomads that are like, the size of a kingdom at most. Maybe a bit bigger. Not these massive confederations you have here; whether that is a failing of the system I leave up to you.

## Reply 248 — participant_093 · 2025-03-20 · post-30244443

<!-- artifact:quote:start -->
> AHumpierRogue said: I feel like the confederation mechanic we see is clearly not designed to represent confederations like this. Confederations are supposed to be for realms of tribals and nomads that are like, the size of a kingdom at most. Maybe a bit bigger. Not these massive confederations you have here; whether that is a failing of the system I leave up to you. Click to expand...
<!-- artifact:quote:end -->
They don't necessarily have to be existing confederations that cover the entire area, rather these should be the territories where those temporary confederations may form in. The confederation mechanic does actually reflect the nature of the steppe quite well, although the ability to hold them together for longer and using them for offensive wars as well would be nice and reflect things such as the Cuman-Rus' wars around the early 12th century which saw various Cuman tribes uniting to attack Rus' together.

## Reply 249 — participant_125 · 2025-03-20 · post-30244473

<!-- artifact:quote:start -->
> Slime99 said: On a serious note I think a good counterplay to raiders will be vassals capable of raiding themselves. Maybe these vassals should also have a CB to subdue close by raiders into a truce with the liege. Click to expand...
<!-- artifact:quote:end -->
I like what you're putting down. Maybe all vassals should have "Defend the realm" Cb to attack a neighbouring realm. If they win they force the realm into a few year truce with their liege.

## Reply 250 — participant_147 · 2025-03-21 · post-30244568

<!-- artifact:quote:start -->
> lachek said: We have increased the hostile raid time reduction in the building, so you have more time to respond to incoming threats. It now also reduces the chances of special raid intents. In other words, it reduces the improvements from the Capture raid intent, minimizes the chance of Terrorize ruining your lands, and for Plunder to find any innovation. Click to expand...
<!-- artifact:quote:end -->
How is this done? Is it part of the building's text file, or is it a trigger akin to the one enabling university visits? I ask because the latter is, in my opinion, more annoying for mods, so I'd much prefer it to be the former.

## Reply 251 — participant_148 · 2025-03-21 · post-30244661

<!-- artifact:quote:start -->
> lachek said: We have made it possible to grow your herd if you hold lands outside of the Steppe, giving those counties Fertility if held by a nomad Click to expand...
<!-- artifact:quote:end -->
This sounds odd, I'm sorry. What is the mechanic for growing a herd as a nomadic in sedentary lands? There will be sedentary holdings in those lands, or will they need to be cleared? Will such a county possess sedentary holdings(and farm fields), yet also 'have' sufficient open fields of pasture to sustain large herds of large and small stock? Or is it assumed the herds are in corrals and therefore subject to being maintained with hay in shelters and such?

## Reply 252 — participant_149 · 2025-03-21 · post-30244945

a minor Change I’d like is for a exception for the name system of nomad realm be added so Kara Khitai is still Kara Khitai

## Reply 253 — participant_093 · 2025-03-21 · post-30245149

I hope the CB to make tributaries is enabled on tributaries of other realms so you can essentially steal tributaries. Also can tributaries have tributaries of their own?

## Reply 254 — participant_093 · 2025-03-21 · post-30245151

<!-- artifact:quote:start -->
> Lazarenko said: This sounds odd, I'm sorry. What is the mechanic for growing a herd as a nomadic in sedentary lands? There will be sedentary holdings in those lands, or will they need to be cleared? Will such a county possess sedentary holdings(and farm fields), yet also 'have' sufficient open fields of pasture to sustain large herds of large and small stock? Or is it assumed the herds are in corrals and therefore subject to being maintained with hay in shelters and such? Click to expand...
<!-- artifact:quote:end -->
Since you can build holdings in steppe counties I doubt it will be much different from that. I think it will be harder in settled areas but still possible, and terrain should also play a big role.

## Reply 255 — participant_108 · 2025-03-21 · post-30245875

<!-- artifact:quote:start -->
> hattusa said: Sadly this is not possible. To make the Nomadic Government work you need a "Nomadic Area" with Fertility and Seasons, and we cannot currently create those on the fly. You can, however, become a landless Robert the Bruce, move to a Herder county, take the decision to become a Nomad and strive to become Genghis Khan, thus leading the Nomadic Scots to glory, which should be your main goal. Click to expand...
<!-- artifact:quote:end -->
Oh so you don't need a Horcelords tradition to become a nomad as an adventurer, Brodnici RP here I come! On a serious note. How will Horcelords tradition change in Khans of the Steppe.

## Reply 256 — participant_096 · 2025-03-21 · post-30245979

<!-- artifact:quote:start -->
> tokinoha said: Why not apply confederation to Crusader Countries? Click to expand...
<!-- artifact:quote:end -->
Yes the "King" of Jerusalem or whichever target of the crusade (excluding the 4th) should be a crusader state localisation of the capital duchy of the relevant kingdom. This king is then the head of a confederation of the other crusader duchies so we can have more of the historical infighting that broke up crusader states Also the dissolution faction should replace their liege's title with a confederation instead of straight independence

## Reply 257 — participant_068 · 2025-03-21 · post-30245984

<!-- artifact:quote:start -->
> Sky _Talez said: On a serious note. How will Horcelords tradition change in Khans of the Steppe. Click to expand...
<!-- artifact:quote:end -->
Im pretty sure they said somewhere that they may remove it? Since they ported most of the features to the government itself and tradition itself made all the steppe cultures feel very same-y. I however can't point you to the quote because i dont remember it that much, you may find it either in DD 162 or somewhere in the replies to it maybe?

## Reply 258 — participant_150 · 2025-03-21 · post-30246391

<!-- artifact:quote:start -->
> hattusa said: This is a very fair point. We will add it to Norse tribals. Click to expand...
<!-- artifact:quote:end -->
Please add the Capture intent to all tribals. Those concubine slots for my many, many landed sons ain't gonna fill themselves (not with good congenital traits, anyway!)

## Reply 259 — participant_093 · 2025-03-22 · post-30246667

I think most lands of Novgorod in Bjarmaland should be tributaries in 1178.

## Reply 260 — participant_151 · 2025-03-22 · post-30246883

Doubt that I will get this answered so long after the dev diary, but: 1. Are confederations its own entire system, allowing custom confederation-like relationships to be setup in the script (in the same sense how government types or laws are their own systems, allowing mods to create their own custom government types or laws)? 2. Since tributaries now seem to allow you to have subjects that are the same rank as you, and since it was mentioned in the dev diary that custom tributary types can be setup, will this system allow you to have subjects that are of higher rank than you? 3. Also, do either of these systems (confederations or tributaries) allow for titular or landless titles with no land to be in one of these relationships, like the Papal States being a tributary even when it holds no land, or potentially even landless governments, given that Noble Families can already be vassals in Admin realms?

## Reply 261 — participant_152 · 2025-03-22 · post-30247626

The Kyrgyz not the "Kirghiz". Kirghiz is the russification of the word Kyrgyz(kıərgız). Its very sensitive for kyrgyz people. Please don't use colonial word kirghiz.

## Reply 262 — participant_153 · 2025-03-23 · post-30248305

Now that you mentioned tributaries, I'm going to ask this. I know the Dev Dairy for All Under Heaven is gonna be on May. I've read that under a mandala government, tributaries can have multiple overlords.

## Reply 263 — participant_141 · 2025-03-23 · post-30248423

<!-- artifact:quote:start -->
> hattusa said: Sadly this is not possible. To make the Nomadic Government work you need a "Nomadic Area" with Fertility and Seasons, and we cannot currently create those on the fly. You can, however, become a landless Robert the Bruce, move to a Herder county, take the decision to become a Nomad and strive to become Genghis Khan, thus leading the Nomadic Scots to glory, which should be your main goal. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> We have made it possible to grow your herd if you hold lands outside of the Steppe, giving those counties Fertility if held by a nomad Click to expand...
<!-- artifact:quote:end -->
Is it not in the cards to eventually make this a universal system? What about adding a stat to counties to host fertility? This could also work as part of an economy expansion, as fertility and seasons did not only affect nomads but also serfs and thus the entirety of a nation's economy. This feels like the start of a long-overdo economic rework. Could modders feasibly add fertility to every region? Another important side note: Restricting nomadic government to a specific area seems rough, as nomads moved all over (far past the steppes, Siberia, and Slavia). Consider the Huns who settled in central Europe after wandering all the way from Mongolia to like... everywhere else. Also, there are players who will not want to stop being nomadic. Feudal kind of sucks. If I start as a tribal nation I stay tribal for the entire conquest phase of the game, up until I've conquered my empire (sometimes two or three) and decide to settle down. Consider this honest feedback and a suggestion: Please find a way to add nomadic compatibility for the whole world. Not just for the sake of "start as nomadic anywhere" but rather for the sake of nomadic gameplay as a whole. There are nomadic players who will want to go to far and exotic places, as is the nomad spirit. By restricting nomadic gameplay to these regions, it really breaks that fantasy. It feels like a cage when you just want to ride horses and be free. Edit: After re-reading the dev diary, what about this? Does this not make it possible to start as a nomad anywhere?

## Reply 264 — participant_086 · 2025-03-23 · post-30248438

<!-- artifact:quote:start -->
> SupremeFeline said: Is it not in the cards to eventually make this a universal system? What about adding a stat to counties to host fertility? This could also work as part of an economy expansion, as fertility and seasons did not only affect nomads but also serfs and thus the entirety of a nation's economy. This feels like the start of a long-overdo economic rework. Could modders feasibly add fertility to every region? Click to expand...
<!-- artifact:quote:end -->
You are thinking the land fertility they are talking about is the fertility for agriculture. I think it's quite clear that they means land fertility for ranching which I think is not the same thing.

## Reply 265 — participant_085 · 2025-03-23 · post-30248446

<!-- artifact:quote:start -->
> Nevars said: You are thinking the land fertility they are talking about is the fertility for agriculture. I think it's quite clear that they means land fertility for ranching which I think is not the same thing. Click to expand...
<!-- artifact:quote:end -->
If the land can build pastures, maybe it can have a fertility level for the nomads. Fertility might be the wrong term for describing the condition of the steppe. When we think of fertility of the land, we think of its capacity to grow grains and other plants for human consumption. Grazing capacity is more correct for what the game fertility seems to trying to quantify.

## Reply 266 — participant_068 · 2025-03-23 · post-30248453

<!-- artifact:quote:start -->
> SupremeFeline said: Is it not in the cards to eventually make this a universal system? What about adding a stat to counties to host fertility? This could also work as part of an economy expansion, as fertility and seasons did not only affect nomads but also serfs and thus the entirety of a nation's economy. This feels like the start of a long-overdo economic rework. Could modders feasibly add fertility to every region? Another important side note: Restricting nomadic government to a specific area seems rough, as nomads moved all over (far past the steppes, Siberia, and Slavia). Consider the Huns who settled in central Europe after wandering all the way from Mongolia to like... everywhere else. Also, there are players who will not want to stop being nomadic. Feudal kind of sucks. If I start as a tribal nation I stay tribal for the entire conquest phase of the game, up until I've conquered my empire (sometimes two or three) and decide to settle down. Consider this honest feedback and a suggestion: Please find a way to add nomadic compatibility for the whole world. Not just for the sake of "start as nomadic anywhere" but rather for the sake of nomadic gameplay as a whole. There are nomadic players who will want to go to far and exotic places, as is the nomad spirit. By restricting nomadic gameplay to these regions, it really breaks that fantasy. It feels like a cage when you just want to ride horses and be free. Edit: After re-reading the dev diary, what about this? Does this not make it possible to start as a nomad anywhere? Click to expand...
<!-- artifact:quote:end -->
You are reading too much into how things are called. Yes, fertility, it gets depleted to generate herd for u and it only does that. Does that help any other government type at all? No. And you probably dont want it to deplete passively either. If it doesnt deplete passively and doesnt provide the herd you just ripped everything that makes this mechanic THIS particular mechanic and by that point you might as well use struggle for it. Or legitimacy. Or whatever other random thing, because you completely changed how the mechanic works. Also yes, the huns, except they're like way out of the game's timeframe and also they SETTLED in central europe. And you can SETTLE wherever you want.

## Reply 267 — participant_068 · 2025-03-23 · post-30248458

<!-- artifact:quote:start -->
> Nevars said: You are thinking the land fertility they are talking about is the fertility for agriculture. I think it's quite clear that they means land fertility for ranching which I think is not the same thing. Click to expand...
<!-- artifact:quote:end -->
Yea paradox calling it "fertility" is a massive blunder coz now there's a bunch of people who think a mechanic that makes your herd grow but also depletes over time is something you can just smack onto any other government type and expect to work just because it's called "fertility" and not "the value that represents how much herd you can extract from this particular place at this particular time"

## Reply 268 — participant_154 · 2025-03-23 · post-30248534

<!-- artifact:quote:start -->
> Benismann said: Yea paradox calling it "fertility" is a massive blunder coz now there's a bunch of people who think a mechanic that makes your herd grow but also depletes over time is something you can just smack onto any other government type and expect to work just because it's called "fertility" and not "the value that represents how much herd you can extract from this particular place at this particular time" Click to expand...
<!-- artifact:quote:end -->
Indeed, I think the suggestion made in response to the previous dev diary that ‘fertility’ should be renamed ‘pasturage’ was a good one which would avoid the confused expectations around this concept.

## Reply 269 — participant_141 · 2025-03-23 · post-30249373

<!-- artifact:quote:start -->
> Benismann said: You are reading too much into how things are called. Yes, fertility, it gets depleted to generate herd for u and it only does that. Does that help any other government type at all? No. And you probably dont want it to deplete passively either. If it doesnt deplete passively and doesnt provide the herd you just ripped everything that makes this mechanic THIS particular mechanic and by that point you might as well use struggle for it. Or legitimacy. Or whatever other random thing, because you completely changed how the mechanic works. Also yes, the huns, except they're like way out of the game's timeframe and also they SETTLED in central europe. And you can SETTLE wherever you want. Click to expand...
<!-- artifact:quote:end -->
Okay, I'll give you that, but still, what about the comment for fertility growing in the lands outside the Steppe when held by nomads? Does that not make it possible to start as a nomad anywhere? I fail to see the problem. Also, the huns still MIGRATED all the way there, and they were nomadic along the way. The migration was about 70 years, all before they officially settled and started the Hunnic Empire.

## Reply 270 — participant_155 · 2025-04-04 · post-30272012

“While in ‘most cases’ they share the map color and realm name with their suzerain, they can act and be interacted with independently, even when it comes to warfare.” What do you mean by “in most cases” exactly? Does it have any significance if a tributary does not share the map color and realm name?

## Reply 271 — participant_156 · 2025-04-29 · post-30315237

So on the current build confederation are not "fleeting an ephemeral". I have multiple confederations of nomads that have been around for 60-70 years at this point. It's not clear how one is supposed to counter this. You cant migrate into their area. Not sure if rebellions cause the confederation to come to their aid.

## Reply 272 — participant_157 · 2025-04-30 · post-30315636

<!-- artifact:quote:start -->
> Madwwwizard said: So on the current build confederation are not "fleeting an ephemeral". I have multiple confederations of nomads that have been around for 60-70 years at this point. It's not clear how one is supposed to counter this. You cant migrate into their area. Not sure if rebellions cause the confederation to come to their aid. Click to expand...
<!-- artifact:quote:end -->
Maybe the big threat for the defence against which they were created is still around? Then it would make sense for them to last that long

## Reply 273 — participant_156 · 2025-04-30 · post-30315757

<!-- artifact:quote:start -->
> MirrorMonkey2 said: Maybe the big threat for the defence against which they were created is still around? Then it would make sense for them to last that long Click to expand...
<!-- artifact:quote:end -->
Im about 6 more hours in an they kinda fell apart. It seems like they will default to for confederations in the presence of big enemies until they reach the third tier of dominance, at which point they leave. In my case, I don't was spamming the steal herd scheme with high intrigue rulers. Once they died and I switched to not doing that, their herds grew large enough that they went they were able to adopt it.

