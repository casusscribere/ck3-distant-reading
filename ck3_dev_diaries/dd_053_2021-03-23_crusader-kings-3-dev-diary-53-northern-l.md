---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1463785/"
forum_thread_id: 1463785
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 53
title: "Crusader Kings 3 Dev Diary #53 - Northern Lords Content Rundown"
dd_date: 2021-03-23
author_handle: Wokeg
expansion: Northern Lords
patch: Patch 1.3 (Corvus)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 4452
inline_image_count: 27
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1463785'
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
    location: raw_lines_~28_to_149
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_148
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1586.jpg?1616509101
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_151_to_153
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_499_to_503
    action: preserved_and_flagged
    counts:
      Like: 134
      Love: 37
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_511_to_619
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_620_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1586.jpg?1616509101)
<!-- artifact:thread_banner:end -->

# Crusader Kings 3 Dev Diary #53 - Northern Lords Content Rundown

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Mar 23, 2021](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-53-northern-lords-content-rundown.1463785/)
<!-- artifact:thread_metadata:end -->

### Crusader Kings 3 Dev Diary #53 - Northern Lords Content Rundown​

Welcome comrades, to a very odd diary for me to be writing!  

Today, we’re going to be taking a look at what new scripted content we’ve added for CK3: the Northern Lords, and, since it’s been out and playable for a week, I thought it’d be fun to go a little bit into some of the design rationales we had and my personal perspective on some of the feedback so far.  

### Writing for the Vikings​

Tackling the Norse was always going to be an interesting affair, since, mechanically, they’re pretty well covered for many things already, though most especially warfare and raiding.  

Accordingly, this meant that, for this flavour pack, we needed to try and dive more into the daily lives of rural Scandinavians. Other than raiding and reaving across the waterways of the world, what did they get up to? What were their folk beliefs? How did they raise their children? What might you find happening on a lazy summer afternoon at a remote Nordic court?  

In short, how could we make tribal North Germanics come alive in ways other than running an efficient kleptocracy?  

Initially, we had intended to keep the focus tightly wrapped to rural Scandinavia, but the more reading and research that was done, the more it became apparent that we were going to have to tackle the Scandinavian colonies and adventurer realms elsewhere. Just as long as we kept everything mostly historically plausible, staying within feasibility as much as we could.  

With some exce-*cough*Mann*cough*-ptions.  

### Raid-Trade Events​

When leading raiding expeditions, rulers with the longboats innovation may occasionally get events allowing them to stop and trade with the locals. This gives them some loot, and a ceasefire with their target (or their target’s liege) if accepted.  

![001.PNG](https://forumcontent.paradoxplaza.com/public/683917/001.PNG "001.PNG")



We added this because we were quite keen on showing that, for all that they raided extensively, the Norse were just as often traders as looters. That said, keen-eyed observers will note that much weaker holdings are *always* raided, with only holdings that are a significant challenge for the raiding army potentially getting the softer option.  

The Norse may have traded almost as often as they raided, but either choice was fundamentally motivated by practicality, not ethics.  

#### Retrospective​

These were scripted early and intended to be something of a minor feature, just adding a little extra depth and flavour to Norse raiding. I really didn’t anticipate how much both QA and the public would enjoy getting more complex raiding options, though, and if I could go back and expand on any one feature, man, this’d be it.  

### Scandinavian Adventurer System​

One thing that the Swedish AI really, really loves to do in the base title is collect holiday homes. Ireland, France, Spain, Sardinia, Stoke-on-Trent… if it’s vaguely near a coast, Sweden wants a piece of that action. Preferably just a small piece. For the collection.  

We wanted to improve on that by giving a more guided experience for Scandinavian expansion during the Viking Age, something aesthetically pleasing that models historical paths of expansion.  

Thus: the Scandinavian Adventurer system.  

![002.PNG](https://forumcontent.paradoxplaza.com/public/683918/002.PNG "002.PNG")



As lords in Scandinavia lose their last holding, they’re added to a pile of other such rulers, from which we select someone every X years. Then, looking down a list of major areas of Norse colonial interest (two lists, technically: one for the west, one for the east), we check to see how the Norse are doing. If we find somewhere in the lists where the Norse presence is either gone or else negligible, we grab one of our landless Scandinavian warlords and send them off to conquer anew.  

The intent here was to make something that meant you couldn’t simply push the Norse out of a certain area and assume they’d stay out, whilst not ending up with tiny Norwegian, Swedish, and Danish exclaves scattered across the world. Instead, we get lots of minor/moderate Scandinavian adventurers, raiding and attacking opportunistically in their areas of interest, and generally harrying people as small bandit lordships till the Viking Age passes and things begin to calm down.  

Fun fact: the Apocalyptic Scandinavian Adventurers game rule setting was initially just for testing purposes. I left it in for a bit of fun, but QA kept coming back after playtesting and telling us how it wasn’t truly apocalyptic enough, and how they expected more, and worse, etc., etc. So uhhh, that’s how we got to have several perfectly sane settings and one that leads to mass border-gore and terrifying Viking emigres marauding across Europe.  

The Scandinavian Adventurers system also includes various other minor mixed mechanics; there’s the attached decision for rulers to go native (though they’ll still count as vikings for the purposes of the system, at least till they die), special exceptions to ensure famous vikings get booted up the list if they lose their last county unexpectedly (looking at you, Haesteinn, you terrifying old man), and an auto-grabber that checks for Rollo & Ubbe after a certain period and, if they’re not tied down, throws them out in the world to go a-conquering.  

Last but not least, the weighting system for selecting adventurers also prioritises player relations, meaning that, if you’re playing within Scandinavia and throw a rival out of their lands entirely, you may not have quite seen the last of ‘em...  

#### Retrospective​

If I could pick any one thing to change about this? The name. Having two separate, but related, adventurer systems was not the smartest idea. Not so bad from a player’s perspective, as all the adventurers just blend together, but having to specify *which* type of adventurer you mean when designing is just a little annoying ![:p](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Stick Out Tongue    :p").  

It could also do with a little more variety in attack date, and perhaps feed notifications for visibility. Maybe someday.  

### Yearly Events​

The Northern Lords includes a little over 40 mixed yearly events, reflecting a broad cocktail of Scandinavian living: rural mythologising, child-rearing, the impact of raids and slave-taking, and aspects of performative Norse honour like nithings and shieldmaidens. We’ve got holmgangs and hofs, whales and warriors, conversions and curses, all trying to approach different core and esoteric aspects of Nordic life.  

![003.PNG](https://forumcontent.paradoxplaza.com/public/683919/003.PNG "003.PNG")



Part of the reason for focusing on small-scale rural living was to try and promote a feeling of being a down-to-earth lordling at the edge of the world, dealing with concerns both petty and practical. Sure, you need to go out raiding and bring back loot for your capital, but you’ve also got to deal with tensions between your elite warrior class and the freeholder farmers that work the land whilst you’re gone, or the monsters that the smallfolk tell themselves stalk the forests at night...  

![004.PNG](https://forumcontent.paradoxplaza.com/public/683920/004.PNG "004.PNG")



Into this, we added a mix of historically-inspired events (like an explorer fresh from the depths of the Atlantic), relatable life events (I know I can empathise with struggling to stay awake at a meeting that’s running too long), and some experimental events (like the nithing pole whodunnit).  


![005.PNG](https://forumcontent.paradoxplaza.com/public/683921/005.PNG "005.PNG")


### Jomsvikings​

As an unreformed holy order that’s uniquely much easier to found than usual (and which happens automagically even if no characters gets around to such), the Jomsvikings offer some interesting benefits to both their founder (including an event army) and to Norse pagans as a whole.  

To balance that, we wanted the Jomsvikings to be, basically, bastards.  

![006.PNG](https://forumcontent.paradoxplaza.com/public/683922/006.PNG "006.PNG")



They’re religious fundamentalists and they’re unhappy that no one is quite as serious as them about the old ways: everyone’s either in a rush to reform, which is heresy, or a rush to convert away, which is apostasy.  

They take it on themselves to roam the Baltic and other areas, rewarding the pious and stealing from literally everyone else, and will continue making a nuisance of themselves against all comers until Jomsberg itself is burnt to the ground.  

![007.PNG](https://forumcontent.paradoxplaza.com/public/683923/007.PNG "007.PNG")



### Shieldmaidens​

Returning in triumph from CK2, for CK3, we knew we wanted to have shieldmaidens be somewhat fewer in number (CK2 tended to inflate them) but also be more impactful as a result. Thus, CK3’s shieldmaidens can save you from various types of assassination, grow deadlier the more battles they’re in via the acquisition of special modifiers, and are more likely to turn up in general events than their CK2 counterparts.  

![008.PNG](https://forumcontent.paradoxplaza.com/public/683925/008.PNG "008.PNG")



This is balanced by the modifier progression event’s cooldown being set per host, not per shieldmaiden. If you *do* acquire lots of shieldmaidens, they’ll level markedly slower than one or two truly legendary ones, allowing the player to choose between widespread shieldmaidenry and a few names that echo through the ages.  

Needless to say, we’re also quite happy to be bringing gender-neutral shieldmaidenry to CK for the first time with the alternate version, the shieldswain, accessible for female-dominated Norse pagans.  

![009.PNG](https://forumcontent.paradoxplaza.com/public/683927/009.PNG "009.PNG")



### Decisions​

#### Secure the High Kingdom of the North Sea​

What needs to be said for forming an empire in the North Sea? In its day, this was tried numerous times, and though each successive polity tended to be incredibly powerful, they never outlasted the short lives of their rulers.  

By living long enough to complete the process of formally tying the kingdoms together within a single lifetime, you can do what Canute the Great could not, and make the binding permanent.  

Our portrayal of the High Kingdom is thus very much alternate history, but it’s still somewhat plausible alternate history, and thus we tried to keep the requirements and outcomes somewhat feasible whilst still letting them vary according to exactly *who* is taking the decision.  

![010.PNG](https://forumcontent.paradoxplaza.com/public/683928/010.PNG "010.PNG")



Unreformed tribals get an easy conversion to feudalism and a modifier that not only helps them live long enough to use it, it makes it so that you lose minimal power transitioning out of tribal.  

Reformed pagans get a modifier that makes it markedly easier to convert other reformed faiths, letting them propagate their faith around the realm with impunity.  

Everyone else gets a strong hook on every powerful vassal with a positive opinion of them which is, understandably, both profitable and stabilising.  

Needless to say, no matter which path you go, you get a cool nickname.  

#### Found the Capital of the Rus’​

In the 9th century, the rise of the Rus’ is just beginning, and though a glorious future is certainly on the way, exactly *what* future is up for grabs.  

We wanted to put the player in the driving seat for this by letting them choose where the heart of the Rus’ truly lays, setting the de jure capital for Russia by their actions in much the same way Helgi the Seer would do after Rurik’s death.  

In addition to setting Russia’s de jure capital, this decision also gives a hefty development boost and a marked long-term increase to local taxes and levies, making it a decision that you can form a strong core realm around.  

#### Retrospective​

… That said, we could *probably* make the instant development-gain into a growth-over-time instead. Development gain is a really great, tangible reward, and the actual effect should stay at roughly the same level, but it certainly does produce some weird parallels with other major development hubs if you rush it in the 9th century.  

#### Elevate the Kingdom of Mann & the Isles​

Oh boi, have I seen some mixed opinions on this’un! Elevating Mann gives you so many bonuses scattered all over the place, most of them extremely good, and it’s easily one of the more powerful decisions in the title (which, given it has to catch the Isle of Mann up as a major world player, it sorta has to be). Your whole dynasty gets to raid for a hundred years despite it making you feudal (something we otherwise heavily restrict), you get a large pirate army with many free Men-at-Arms, you get lots of renown, and the Isle of Mann is made into an absolute powerhouse of a county.  

![011.PNG](https://forumcontent.paradoxplaza.com/public/683929/011.PNG "011.PNG")



Remember when I said at the start of the diary that we generally wanted to stay historically plausible? Well, that’s very true, and everywhere else we’ve tried to stick quite hard to, at the least, a valid interpretation of historical evidence.  

Elevating Mann is the one major exception we allowed (and a *big* shout out to everyone who’s already found the other, more-hidden major exception and are readying their corrective posts right now, but *shhhhhh*, let people find it by themselves). It’s dumb, it’s fun, it’s for bringing out your inner pirate-monarch and stealing the wealth of the world away.  

![012.PNG](https://forumcontent.paradoxplaza.com/public/683930/012.PNG "012.PNG")



#### Retrospective​

… It probably could use a gold-looted requirement, though.  

### Religious Changes​

#### Blots​

Blots are an interesting conundrum, and one we took quite a few risks with this DLC.  

In CK2, they were heavily modelled after the account of Adam of Bremen, an 11th century German bishop and chronicler who specialised in, amongst other things, Scandinavian accounts. They’re fun, but they also require a lot of micro to get the most out of them, and paint a very human sacrifice-happy view of Norse paganism that Adam of Bremen certainly agreed with, but which has somewhat more mixed archaeological evidence.  

For CK3, then, we wanted to reduce the inherent micro involved in prisoner selection & acquisition, and give the option to throw a grand blot *without* needing to ensure at least an optimal number of prisoners. Our version is, instead, based on Adam of Bremen, reports from the sagas, contemporary archaeology, and some input from relevant medievalists.  

![013.PNG](https://forumcontent.paradoxplaza.com/public/683931/013.PNG "013.PNG")



Thus, rather than raising money and eliminating prisoners, throwing a colossal feast costs money but brings the realm together by doling out popular and vassal opinion.  

The player is also always assumed to have enough thralls and petty prisoners to hand to be able to put on a decent human sacrifice if they want to, but can still throw a helluva party even just using animals. Instead, we make a larger deal about selecting a particularly noteworthy sacrifice to take centre-stage, and keep this as optional throughout.  

![014.PNG](https://forumcontent.paradoxplaza.com/public/683932/014.PNG "014.PNG")



Per several accounts, even rulers not of the faith can hold great blots to please their blot-faith vassals and lands, though they must be careful not to upset their co-faithists. Particularly if they plan to indulge the blot’s most vicious customs.  

![015.PNG](https://forumcontent.paradoxplaza.com/public/683933/015.PNG "015.PNG")



One small bit of flavour I quite like about blots is that they’re responsive to dietary needs: different syncretisms and religions will filter out sacred or unclean animals so that they’re no longer served, and those who prefer their food more *intelligent* likewise have slightly different sacrifice loc.  

#### Select Personal God​

An extension of vanilla’s Bhakti tenet, selecting a personal god lets characters choose a patron deity whose worship guides their life and attracts relevant specialists to their side.  

I’ve got to say, of these, my all-time favourite has to be selecting Ullr. I know Odin is generally better and more versatile, and Thor has the catchier theme tune, but extra winter movement speed from leading an army that devoutly worships the god of skis tickles me so much.  

![016.PNG](https://forumcontent.paradoxplaza.com/public/683934/016.PNG "016.PNG")



#### Retrospective​

Originally, this was going to be a much more diverse selection of gods, divided according to local cults from around Scandinavia. Unfortunately, during the research phase of production, we turned up a paucity of sources on the specifics of Norse pagan worship. Since the choice was to go with almost entirely what’s presented in the Eddas or to scale back the feature a bit, we chose to try to cleave to reliable history, and scale back the feature.  

A little part of this original functionality still survives in the form of Tyr and Ullr being mutually exclusive for Danes and non-Danes respectively, a division which is moderately supported by current studies in place name archaeology.  

#### Holy Sites​

One of our largest changes in 1.3 is shifting the Norse pagan holy sites around, removing the two from Denmark and Holland and shifting them instead to York and Kiev.  

![017.PNG](https://forumcontent.paradoxplaza.com/public/683935/017.PNG "017.PNG")



This was partly for balance (Norse paganism has some of the strongest holy sites in the game clustered in an easily defensible area), partly to make it a bit more challenging to reform Norse paganism, and partly because these holy sites have been the same since 2013 and not really revisited since the Old Gods launched.  

Holland’s claim in particular was extremely dubious compared to York, which, as the focal point for a lot of events around the death of Ragnar Lothbrok (who, whether he was historical or not, forms the background legend for much of Scandinavia’s major nobility) and centre of Scandinavian colonialism in the British Isles, really needed a priority bump.  

For the Danish holy site being moved to Russia, we more or less had a straight choice between Novgorod and Kiev. Since part of the rationale was to make it a bit harder to reform the faith, though Novgorod was arguably a more important site, we went with Kiev. Denmark’s claim to having a holy site to begin with is arguable (certainly significantly more than Holland), but not the strongest, especially not compared to Uppsala or, to a lesser extent, Trondheim.  

#### Virtues​

… has anyone else noticed that, since we added One-Eyed as a virtue to Norse paganism, suddenly everyone’s ruler designed characters are all missing an eye? I think we may well have inadvertently drastically reduced the number of eyes in CK3 overall. It’s hilarious.  

Including Poet and One Eyed as virtues for Norse paganism is technically part of the free patch, but I think it’s one of my favourite little aspects of flavour in 1.3, and especially the randomised poetry system was scripted very partially so that Norse paganism could regain its signature unique virtue.  

![018.PNG](https://forumcontent.paradoxplaza.com/public/683936/018.PNG "018.PNG")



### Dynasty Legacies​

As part of the Northern Lords, we’ve added two new dynasty legacies: Adventure, for those who like to wander the world, and Pillage, for those who wish to see it *burn*.  

![019.PNG](https://forumcontent.paradoxplaza.com/public/683937/019.PNG "019.PNG")



Early in the design process, we were initially only going to have one new dynasty legacy, but the perks it ended up with were pretty wildly variable (imagine Wanderlust and Gift-Givers on the same track as Making a Killing and No Quarter).  

![020.PNG](https://forumcontent.paradoxplaza.com/public/683938/020.PNG "020.PNG")



We pretty quickly decided that, since we were trying to expand on non-raiding areas of play, we should break the dynasty perks into two separate tracks, so that players could choose one without strictly needing to have both, and so build the Norse legacy that most fits their roleplay.  

### Regional Innovations & Cultural Mechanics​

#### Varangian Adventurers​

These are, perhaps, my favourite part of the flavour pack! Varangian Adventures allow independent Norse rulers to pick up sticks and, along with a small army of followers, move their entire realm to another part of the world, abandoning their old holdings for pastures new.  

![021.PNG](https://forumcontent.paradoxplaza.com/public/683939/021.PNG "021.PNG")



This has been something that I, personally, have wanted to do in Crusader Kings for years, but previous methods have always required you to manually lose your old holdings and it’s honestly just a bit of a chore. Being able to do it automatically whilst gaining an event army, and so build my own version of Haesteinn or Rurik, is so much fun.  

It’s also been an absolute delight to see pictures of other people’s adventurer empires, with Norsemen ending up anywhere from Ceylon to the Sahara, and we love seeing players get into the spirit of wandering the world.  

#### All-Things​

Since the Norse tend to swim in prestige but can struggle feudalising, All-Things are intended to allow you to equalise these two somewhat. By losing much of your excess prestige, you can transition up and down the realm authority rungs much easier, making for a smoother process if you want to change laws in a hurry.  

A couple of our yearlies are also tied to the possession of this innovation, either yourself, or by your counties.  

#### Retrospective​

I quite like the dynamic with All-Things, effectively loosening some of feudalisation’s harsh requirements, but feel they could perhaps have done with a few more events to make such a notable feature of the innovation.  

#### Revamping the Raising of Runestones​

Now, I’ve seen a *lot* of confusion about runestones out there, so let me clear something up: runestones were (and, in a marginally-improved form, still are) accessible in the base title, fulfilling a very similar role to their CK2 incarnation.  

What we’ve done for the Northern Lords, since we happened to be in the neighbourhood of runestones and wanted to give them a little more attention whilst we could, was expand and improve on that original design. For this flavour pack, we made them more responsive to specific scenarios and events that happen in your character’s life, both in terms of triggering and by providing custom flavour for individual runestones related to their contents.  

![022.PNG](https://forumcontent.paradoxplaza.com/public/683940/022.PNG "022.PNG")



This lets you make runestones work for your more specific needs, shoring up weak counties and boosting strong ones with selectable, flavourful bonuses.  

We uhhh, we may have gone a bit overboard with some of the flavour loc variants though, honestly. I’m not totally convinced that anyone is ever likely to raise a runestone commemorating a Norse Chakravarti or a Norse Greatest of Khans, but hey, if you do, you can bet it’ll be commemorated on their runestone.  

![023.PNG](https://forumcontent.paradoxplaza.com/public/683941/023.PNG "023.PNG")



Unless you do both, I suppose. Only so much space ~~in the modifier description~~ on the rock.  

#### Trials-by-Combat​

TbCs! These took the absolute *longest* time to set up. Not because of the actual interaction, but because we first had to script and localise the single combat system to get a decent implementation. If I recall correctly, localisation for duelling alone wound up at somewhere around 28k words, including dozens of variant ways to die or be injured.  

Our intent with Trials-by-Combat was to present something that worked orthogonally to the usual prison system without replacing it. Serious matters should, predominantly, continue to work via the use of imprisonment or factions, but where these two avenues are unavailable, aggrieved parties can agree on a settlement then settle their dispute in a fair fight.  

This makes them a little tricky to grok at first, but slots them neatly into an unused gameplay groove once you do. I’ve seen more than a few high-prowess players financing entire civil works programs via TbC cash settlements and, really, who doesn’t like beating someone in a fight so hard they start compulsively telling the truth?  

![024.PNG](https://forumcontent.paradoxplaza.com/public/683942/024.PNG "024.PNG")



#### Men-at-Arms​

The Northern Lords introduced four new MaA types: Bondi, Vigmen, Varangian Veterans, and Jomsviking Pirates. We wanted each of these to be situationally useful, generally a bit more specialist than the standard MaA types, and almost universally better winter fighters.  

Bondi are the freeholding smallfolk of the land, the people who make up most of the attendees at the Thing-meets, and are represented as a cheaper (but also somewhat worse) alternative to pikemen.  

![025.png](https://forumcontent.paradoxplaza.com/public/683943/025.png "025.png")



Vigmen are professional warriors by trade, but not the most experienced or best equipped. Relying on massed short-range archery and firm shield walls, they’re at their best when fighting massed light infantry.  

![026.png](https://forumcontent.paradoxplaza.com/public/683944/026.png "026.png")



Varangian Veterans represent the adventurers, wanderers, and, in later centuries, alumni of the Varangian Guard that permeate Scandinavia. They’re individualistic, they’re deadly, and they charge a frankly exorbitant sum for their services.  

![027.png](https://forumcontent.paradoxplaza.com/public/683945/027.png "027.png")



Finally, Jomsviking Pirates are a special MaA type, only given out through events and decisions (usually those involving the Jomsvikings). As skirmishers, they’re fairly easily countered, and they lack a terrain speciality like most other MaA types, but they make up for this by having good all-round states *including* both pursuit and screening. A force of anarchy on the battlefield, the Jomsvikings come into their own when substituting for a lack of light horse, either harrying the enemy as they flee or covering their comrades as they escape.  

With these MaA types, we wanted to cover some (though not all) of the Viking deficiencies in the earlier centuries of the title, whilst still leaving them open to being out-teched by better MaA in the mid to late game.  

### That’s All Folks!​

![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)") We hope this has been an interesting dev diary for you, even after release, and don’t forget to drop a screenshot of your Varangian Adventure kingdom in the thread!

<!-- artifact:reactions:start -->
- 134 Like
- 37 Love
- 24 (unlabeled — rendered as base64 data URI)
- 9 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)**
Role: Former CK3 Experienced Game Designer
Badges: 65
Messages: 528
Reaction score: 15,169

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
