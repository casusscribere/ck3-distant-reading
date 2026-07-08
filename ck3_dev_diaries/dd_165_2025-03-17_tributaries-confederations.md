---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1731866/"
forum_thread_id: 1731866
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 165
title: "Dev Diary #165 - Tributaries & Confederations"
dd_date: 2025-03-17
author_handle: lachek
expansion: Khans of the Steppe
patch: Patch 1.16
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 4146
inline_image_count: 32
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1731866'
extraction_rationale: |
  XenForo forum page rendered server-side; WebFetch's native
  HTML-to-Markdown conversion preserves the OP body, image
  references, and paragraph structure cleanly. Boundary
  detection performed by deterministic regex against the saved
  fetch output.
detected_artifacts:
  - type: webfetch_metadata
    location: raw_lines_1_to_~27
    action: discarded_from_output
  - type: forum_chrome
    location: raw_lines_~28_to_146
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_145
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3635.jpg?1742204630
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_438_to_443
    action: preserved_and_flagged
    counts:
      Like: 145
      Love: 76
      (unlabeled — rendered as base64 data URI): 3
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_451_to_561
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_562_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

<!-- artifact:thread_banner:start -->
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3635.jpg?1742204630)
<!-- artifact:thread_banner:end -->

# Dev Diary #165 - Tributaries & Confederations

<!-- artifact:thread_metadata:start -->
- Thread starter [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)
- Start date [Mar 17, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-165-tributaries-confederations.1731866/)
<!-- artifact:thread_metadata:end -->

Hello there!  

Welcome back to the first official dev diary for our Core Expansion this year, *Khans of the Steppe*. For those who did not see it, we first talked about the DLC back last month with [Dev Diary #162 - Steppe by Steppe](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-162-steppe-by-steppe.1728107/), so I recommend reading that first.  

Today we will discuss Tributaries, Confederations, and Raid Intents. All three topics were mentioned in the previous Dev Diary, but we will discuss them at length in this one, so let’s settle in like a migrating nomad and get started.  

### Follow-up from Previous Dev Diary​

The team has gone through an intense iteration period based on both feedback collected internally and the comments received from our previous Dev Diary. Many changes have been thus made, and we are sure we are not done with it yet. However, here's a small list of some of the most significant tweaks done based on your feedback:  


- A new, "base" Tributary type has been made available for non-Nomads.
- Concerns about the Nomadic economy have been addressed by adding a monthly income for nomads based on their Herd size (symbolizing the trade of meat, hides, etc.)
- A game rule has been added to include Nomadic governments in the Sahel, Arabia, the horn of Africa, Sami and Karelia regions
- Tweaked the borders of the Steppe and characters who should be nomadic in all bookmarks (more than I can list here, screenshots will be shared in following Diaries)
- We've added a Culture and Faith specific to your Nomadic Capital, different than your own
- Adventurers can now become Nomads if they move into a Herder holding
- We have expanded what we originally scoped for razing
- We've extended and altered the effects of some Seasons
- We have made it possible to grow your herd if you hold lands outside of the Steppe, giving those counties Fertility if held by a nomad

### Tributaries​

One of the new features we’re introducing with *Khans of the Steppe*, and the free update that goes along with it, are Tributaries. Vast nomadic realms like the Cumans, Khitans, and Khazars were not kept together by a tiered system of formal vassalage and pledges of fealty, nor were they delineated by culture or religion. Instead, the harsh realpolitik of the steppe applied - whoever could muster the greatest capacity for destruction on their neighbors proved themselves worthy of tribute, in exchange for the privilege of not being trampled underhoof. Modeling this type of subject relationship properly was the impetus for the Tributary feature.  

Let's back up a bit and discuss some fundamentals first though, because tributaries aren't just a nomad thing. While Tributaries are similar to vassals in some respects, they represent a whole new type of unequal diplomatic relationship in the game. As a result, many game elements that formerly referred to "vassals" now refer to "subjects" instead. Subjects can be either vassals or tributaries, and these sub-types adhere to different rules. As with vassal contracts, there can be different types of tributary contracts with varying degrees of obligations. In most cases, these terms can be renegotiated.  

Tributaries can be seen as a more independent subject type compared to vassals. While in most cases they share the map color and realm name with their suzerain, they can act and be interacted with independently, even when it comes to warfare. Most tributary types can also be created through peaceful means, by a sovereign ruler pledging tribute to a nomadic realm in exchange for a guarantee to not be attacked by them, or through a nomadic ruler demanding tribute from a neighboring realm. Agreements of tribute are (usually) perpetuated across generations, but may change in nature over time or be more easily broken when the contract changes hands.  

![image-01.png](https://forumcontent.paradoxplaza.com/public/1259952/image-01.png "image-01.png")


*[Marzoban Tokku and his weak backbone stands little chance against the persuasive might of the Cumanian horde]*  

![image-02.png](https://forumcontent.paradoxplaza.com/public/1259953/image-02.png "image-02.png")


*[If some scary nomadic realm is on your border and you'd like to remain as independent as possible, you can proactively choose to pay them tribute to avoid outright conquest]*  

![image-03.png](https://forumcontent.paradoxplaza.com/public/1259954/image-03.png "image-03.png")


*[Existing vassals can be released as tributaries, and in some cases you can even vassalize an existing tributary]*  

Nomadic Tributaries are what you will encounter most frequently in *Khans of the Steppe*. These consist of nomadic realms (or spineless herders) who have pledged tribute to a stronger nomadic ruler on their border. They will pay a part of their herd in tribute on a regular basis, and some of the prestige they gain will also be conferred upon their suzerain. In exchange for tribute, they enjoy a great deal of independence from their suzerain and will not be outright attacked or raided by them. They can even have tributaries of their own!  

Settled Tributaries are non-nomadic realms (such as feudal princes, tribes, or clans) who have yielded to a bordering nomadic ruler. Like their nomadic tributary counterparts, they will pay tribute on a regular basis, but instead of herd they will provide gold and levies.  

Both these types of tributary contracts are inherited across generations, but they also have quite a bit of leeway in simply ceasing payments (if they are ready to face the consequences of insulting their suzerain, that is). This is most likely to happen if a nomadic suzerain prove themselves weak in some way (and therefore unworthy of tribute, by the laws of the steppe), like losing a war or suffering a chaotic Kurultai succession. Once tributaries opt to stop sending gifts to their suzerain the suzerain can choose to attack them to recover control, or let them go try to make their own destiny without their protection. To try to keep this from happening, nomadic suzerains can either be lenient with their contract conditions, or leverage their Dread to demand Obedience of their tributaries.  

![image-04.png](https://forumcontent.paradoxplaza.com/public/1259955/image-04.png "image-04.png")


*[Your subject view will display if any of your tributaries are likely to stop paying you and why. Obedience plays a strong role in keeping your subjects in line, but even disobedient ones will be reluctant to stop paying off much stronger suzerains. More factors will be added before launch, such as losing a war or having chaotic Kurultai successions.]*  

A third type of subjugated tributary has also been added, which has no direct relation to nomads. This is a tributary type obliged to pay a lot of gold and a small amount of prestige to their suzerain in exchange for their suzerain's protection from outside invasion. If attacked, a subjugated tributary can call their suzerain in to defend them, and if they refuse their tributary obligations are annulled. Any non-nomadic realm can create this type of tributary through the Bring Under Tribute casus belli, enabling the extortion of neighboring protectorates through sheer military might.  

This contract does not get inherited by the suzerain's heir upon their death, but also cannot be voluntarily broken. If the tributary wishes to break free of their obligations prior to their suzerain's death, they will have to fight them for independence.  

![image-05.png](https://forumcontent.paradoxplaza.com/public/1259956/image-05.png "image-05.png")


*[Even feudal realms can subjugate neighboring kingdoms to make them pay tribute, if their Crown Authority is high enough]*  

It's important to note that it's possible to modify the terms of a tributary contract, just like a vassal contract. For example, nomads can negotiate for protection by their suzerains in exchange for higher tribute payments. If you and your tributary are Blood Brothers, you can even negotiate a guarantee that they will follow you on all military adventures, offensive as well as defensive.  

![image-06.png](https://forumcontent.paradoxplaza.com/public/1259957/image-06.png "image-06.png")


*[Even the tributary can try to renegotiate the terms, but without a good relationship with (or a hook on) your suzerain this might be met with limited success]*  

Another aspect of tributaries of nomadic realms is that they can provide new Men-at-Arms types to their suzerain. In keeping with the flexible and heterogenous nature of steppe warfare, nomad rulers are able to recruit Men-at-Arms from both tributaries and vassals as if they were their own. Since the Men-at-Arms are recruited from other realms, rather than an additional cost of herd (to represent the development of more advanced mounted units) this costs a premium in gold to entice the foreigners to join up with the Khan's formidable horde.  

![image-07.png](https://forumcontent.paradoxplaza.com/public/1259958/image-07.png "image-07.png")


*[If you don’t have any subjects with access to some of the basic Men-at-Arms types, you get a little hint suggesting who might give you access to them…]*  

Visually, tributary realms will typically adopt the map color and name of their suzerain to clarify the relationship between them. Modders might be interested to know that this behavior can be changed in script depending on the subject contract: you can make tributary types that do not inherit the suzerain's color or name, or just one of them, as well!  

![image-08.png](https://forumcontent.paradoxplaza.com/public/1259960/image-08.png "image-08.png")


*[In 867, the Khazars dominate the Western Steppe while the Kirghiz control the Eastern parts. The Karluks and Ohguz are powerful nomadic realms in the central steppe region and have a lot of opportunity to compete for the smaller nomadic and tribal realms towards the northern parts.]*  

![image-09.png](https://forumcontent.paradoxplaza.com/public/1259963/image-09.png "image-09.png")


*[In 1066 the western and central steppe regions are dominated by the Cumans in the south, with a considerable tributary network maintaining their control of the center and maintaining their power against the Karluks and Khitans. The Pechenegs have migrated west and act as a buffer zone between the steppe and the Byzantine Empire - will they manage to become their own nomadic powerhouse, or fall to either of their titanic neighbors?]*  

![image-10.png](https://forumcontent.paradoxplaza.com/public/1259964/image-10.png "image-10.png")


*[In 1178, the Cumans remain the most powerful nomadic realm on the steppe, but for how long? The Khitans are migrating south into East Asia, leaving their old lands to the fractured Mongols to thrive.]*  

Since tributaries inherit all of the functionality of the vassal contract system, with a few extensions, they are very flexible and capable of modeling a great deal of unequal relationships between realms and rulers. There's a fair chance you will see more tributary types and dynamics added to the game in the future, and the system is fully available to modders to play with as well!  

But how would you deal with these massive, aggressive nomadic realms as a smaller nomad who just wants to live a laid-back, peaceful nomadic lifestyle? One avenue to that is what we'll discuss next.  


### Confederations​

Brothers and sisters, do you ever tire of lusting after power? When you jump into a game as a meek little Count, do you wish friends and neighbors would stand together with you against the masters of the world? Do you want something new to do as a tribal? Say no more, my brothers and sisters - but the sacred words, the oath of confederation!  

In short, Confederations are a new way for nomads and tribals to feel safe while initially building their power, playing tall, etc. It’s also a bit of an extra challenge for those looking to easily gobble up areas of the map that lack a mighty King or Emperor.  

![image-12.png](https://forumcontent.paradoxplaza.com/public/1259965/image-12.png "image-12.png")


*[12th c. Estonia mightn’t have looked quite like this, but hopefully this captures some of its spirit]*  

The inspiration for Confederations came from a visit to beautiful Tallinn, Estonia (which I very highly recommend), a fascinating conversation with a very learned scholar in medieval Baltic history, and a visit to the Great Guild Hall Museum. Therein, an exhibit asked the question — “Why did Estonia not become a Kingdom?”  

It’s an interesting question, with at least a few answers. In a sense, the Estonian tribes did actually have kings, but these were temporary war-leaders or spiritual figures, and they did not serve to unite all the tribes together into one lasting polity. They are mentioned, as stubborn figures of resistance, in the Christian chronicles of conquest. This kind of defensive decentralization seemed new for CK3; I immediately wanted to represent it in our game. And, of course, there are the steppe confederations of history — the Khamag Mongol, the Kimek-Kipchaks, the Mogyërs, and so on — to consider and draw from as well. I’m also a Canadian btw, and Confederation has been a force of history around the Great Lakes for quite a while.  

Let’s go through the confederating process, and discuss.  

![image-13.png](https://forumcontent.paradoxplaza.com/public/1259966/image-13.png "image-13.png")


*[The Decision that lays the path to Confederation]*  

The first step is a Decision that enables you to offer Confederation to other rulers. Its warnings are to be taken seriously — you will likely have to leave your Confederation if you want to increase your station in the world (through means like title creation, migration, Dominance) or enrich yourself by raiding/attacking your fellow weaklings.  

![image-14.png](https://forumcontent.paradoxplaza.com/public/1259967/image-14.png "image-14.png")


*[The requirements for starting a Confederation; you have to be something of a small fish]*  

Who can make a Confederation? Well, you have to be standing on your own, and you can’t be standing very tall. These same restrictions apply to all prospective Confederates.  

![image-15.png](https://forumcontent.paradoxplaza.com/public/1259968/image-15.png "image-15.png")


*[Additional Confederation triggers. Most of the time, you’ll need a big, scary common foe]*  

Confederations in Crusader Kings III will be fleeting, ephemeral things, and focused largely on deterring the depredations of powerful neighbors. Thus, they will almost always be created in response to major powers being at their borders. It’s been really cool to watch Conquerors and great kings arise and, as they do, Confederations spring up all along their underbellies like nests of rats or colonies of fire ants. There is now a third, sometimes-viable alternative to “submit or die.”  

The possible faith hostility trigger also works really nicely along the borderlands between pagan tribals and reformed faiths: it means the former can often be seen making the Confederation defensive arrangement to resist the brutal tide of history.  

![image-16.png](https://forumcontent.paradoxplaza.com/public/1259969/image-16.png "image-16.png")


*[You’re ready for Confederation… you just need a buddy to join you]*  

Given Confederations are available across the map, to both nomads and tribals, related content is laced with conditional loc and effects to keep things from feeling too inappropriate. That said, this isn’t a content-heavy feature; development on Confederations instead focused on making it an effective new mechanic.  

![image-17.png](https://forumcontent.paradoxplaza.com/public/1259970/image-17.png "image-17.png")


*[The interaction used to create a Confederation, and also to add new members]*  

The character interaction Offer Confederation (unlocked by the Call for Confederation decision or by Confederation membership) is how this brothers-in-arms, last stand-style shit comes to pass. Notice that, because migration removes members from the Confederation, there are incentives to stay put for a bit longer (a positive County Fertility modifier and an immediate County Fertility boost). AI should also be more reluctant to migrate than usual, at least for a few years.  

![image-18.png](https://forumcontent.paradoxplaza.com/public/1259971/image-18.png "image-18.png")


*[Weights are pretty comprehensive and pretty make-or-break]*  

Your level of investment in your confederation can make a big difference in its strength: herd, prestige and hooks can be sacrificed to make valid members more willing to join.  

![image-19.png](https://forumcontent.paradoxplaza.com/public/1259972/image-19.png "image-19.png")


*[Well isn’t that nice - he accepts!]*  

![image-20.png](https://forumcontent.paradoxplaza.com/public/1259973/image-20.png "image-20.png")


*[Note the Confederation icon and breakdown]*  

Confederations aren’t a title. Their closest equivalent is an alliance or truce, thus they live in the Diplomacy space of the Character view. Here, you can see all members of the Confederation.  

The Kimek Confederation is a culture-based name, which happens when both the first members are of the same culture. When they aren’t, the Confederation will be named after the founder’s de jure duchy (ex. the Semey Confederation, the Kargassia Confederation).  

![image-21.png](https://forumcontent.paradoxplaza.com/public/1259974/image-21.png "image-21.png")


*[A handful of Kimeks have joined the Confederation (squint, it’s on the left)]*  

On the map, Confederations will look similar to the new Tributaries: their individual realm names are replaced by the overall Confederation and their map colors are blended towards the main Confederation color (which is based on the founder’s capital).  

You may notice that the members remain rather unevenly-sized. That’s because only independent top rulers are members of the Confederation, and their vassals (if they have any) are not.  

![image-22.png](https://forumcontent.paradoxplaza.com/public/1259975/image-22.png "image-22.png")


*[The Confederation is attacked!]*  

When a Confederation member is attacked is when the organization really comes into its own. All members are automatically added as Defenders. This can result in a pretty potent nest of bees that the aggressor has just poked. Accordingly, the combined strength of a Confederation is shown when opening the Declare War screen on one of its members, and AI should be appropriately hesitant to attack strong Confederations.  

Note that this applies only to members’ defensive wars. They cannot call on the Confederation when they themselves declare offensive wars.  

![image-23.png](https://forumcontent.paradoxplaza.com/public/1259976/image-23.png "image-23.png")


*[The Decision for when a Confederate decides it’s time to go…]*  

While AI will usually give the Confederation at least a few years of their time, players are quite free to strike off on their own whenever. Albeit… for a higher Prestige cost during the first couple years.  

The AI weighting for this Decision is heavily dependent on circumstances. Chief among these is the presence of big nearby threats that necessitate confederation. The result is that, where confederations are needed, they should prove much more lasting and resilient. And when they are no longer needed, they should often quickly disband.  

![image-24.png](https://forumcontent.paradoxplaza.com/public/1259977/image-24.png "image-24.png")


*[BROTRAYAL]*  

And there it is, Confederations! I hope this run-through has cleared up the feature. And remember — the CK player who stands alone, dies alone. Call up a friend right now and ask if they’d FUCKING DIE for you. Post results in the comments.  

### Raid Intents​

We discussed raid intents in the previous dev diary, with a small WIP screenshot. It’s time to expand on what we said then.  

First of all, we should talk about loot. As you all know, we’ve had loot in the game for quite a while. Gold you can take from a settlement as you raid them as a tribal ruler or a pagan, which you then bring back home to turn into gold and prestige. We haven’t changed the core mechanic of loot, but we have disconnected it slightly from purely being gold, now that you have more ways of using it. With Raid Intents, we now have ways of turning that loot into other things, to symbolize your aims as you are raiding foreign lands.  

![image-25.png](https://forumcontent.paradoxplaza.com/public/1259978/image-25.png "image-25.png")



Here is the new raid intent screen (for nomads), after a small art pass and after we added some proper names. Now, let’s look at the default raid intent for nomadic rulers, Pillage.  

![image-26.png](https://forumcontent.paradoxplaza.com/public/1259979/image-26.png "image-26.png")


*[Note that none of the numbers are final, so they might change before the release]*  

It’s a fairly straightforward calculation. If you bring home 100 loot, you will get 100 gold and 150 herd out of it when you return to your borders.  

Most of the other raid intents have some kind of separate side effects in addition to their base calculation, so let’s look at some of them.  

![image-27.png](https://forumcontent.paradoxplaza.com/public/1259980/image-27.png "image-27.png")



Nomads were known for raiding far and wide, with the Hungarian raiders, for example, bringing home loot from all across Europe. With the Adventure raid intent, it will take a bit longer to raid each settlement, but you can carry a significantly larger amount of loot with you, and you will take no hostile county attrition.  

It should be noted that within the steppe, nomad raiders will not take any hostile county attrition, regardless of raid intent, but they will regularly take attrition outside of it.  

![image-28.png](https://forumcontent.paradoxplaza.com/public/1259981/image-28.png "image-28.png")



Plunder symbolizes that you aren’t necessarily just taking anything but trying to find the most valuable things to take. It will take significantly longer to raid every single settlement. Still, the loot conversion as you get home is considerably better, and you have a chance to learn innovations of a culture as you raid a settlement if they know about something you do not (though the chances are quite low).  

![image-29.png](https://forumcontent.paradoxplaza.com/public/1259982/image-29.png "image-29.png")



For those less interested in the loot itself but rather other side effects, you might want to take the capture raid intent to significantly increase the chance of capturing someone as you raid a settlement. It’s great if you are looking to ransom someone.  

![image-30.png](https://forumcontent.paradoxplaza.com/public/1259983/image-30.png "image-30.png")



And last but not least, you have the opportunity to destroy. It’s an opportunity for nomads to increase their prestige (as they don’t get any prestige from other raid intents) and their dread (which is more important for nomads). It also destroys buildings and development in settlements they raid.  

Now, one thing to mention is that we don’t only have raid intents for nomads but for other raiders as well. Regular raiders also have access to the Terrorize raid intent, so feel free to bring destruction to your enemies no matter which flavor of uncivilized you are. They also have access to Pillage, but in a slightly different form:  

![image-31.png](https://forumcontent.paradoxplaza.com/public/1259984/image-31.png "image-31.png")



Like current functionality, you simply change your loot to gold and prestige. And for Vikings, they have access to a slightly modified version of the Adventure intent.  

![image-32.png](https://forumcontent.paradoxplaza.com/public/1259985/image-32.png "image-32.png")



If you want to raid your way down to Constantinople and then home again, feel free to take this to bring all that loot back home.  

Now for the other side, you can destroy the raiders as they enter your lands, but we have also made one small adjustment so you can protect yourself a bit against any incoming threat.  

![image-33.png](https://forumcontent.paradoxplaza.com/public/1259986/image-33.png "image-33.png")



We have increased the hostile raid time reduction in the building, so you have more time to respond to incoming threats. It now also reduces the chances of special raid intents. In other words, it reduces the improvements from the Capture raid intent, minimizes the chance of Terrorize ruining your lands, and for Plunder to find any innovation.  

Upgrading the building will improve the effect and block raid intent special effects from happening outright. In other words, something to keep in mind if you experience a lot of raids in your lands.  

### Next Week​

That’s it for this week. Next week, we plan to revisit migrations and the nomadic government, so we hope to see you again then. Go forth and conquer, my blood brothers.

<!-- artifact:reactions:start -->
- 145 Like
- 76 Love
- 7 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)**
Role: Design & UX Manager/Lead, Crusader Kings III
Badges: 37
Messages: 814
Reaction score: 49,611

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
