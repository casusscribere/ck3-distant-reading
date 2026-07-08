---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1697815/"
forum_thread_id: 1697815
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 151
title: "Dev Diary #151 - Landless Adventurers (Part I)"
dd_date: 2024-08-02
author_handle: Wokeg
expansion: Roads to Power
patch: Patch 1.13
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 9065
inline_image_count: 72
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1697815'
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
    location: raw_lines_~28_to_152
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_151
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3198.jpg?1722845739
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_154_to_156
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_924_to_928
    action: preserved_and_flagged
    counts:
      Love: 173
      Like: 103
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_936_to_1048
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_1049_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3198.jpg?1722845739)
<!-- artifact:thread_banner:end -->

# Dev Diary #151 - Landless Adventurers (Part I)

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Aug 2, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-151-landless-adventurers-part-i.1697815/)
<!-- artifact:thread_metadata:end -->

*Note: You can also listen to today's Dev Diary [here on our YouTube channel!](https://youtu.be/UDl-F0OYOP8)*  

---

Welcome comrades! Wokeg here: I hope everyone enjoyed their window into how the other half lives with the Administrative Government Dev Diaries, because today we’re gonna be going back down into the mud with our favourite homeless wanderers — Landless Adventurers.  

As usual, everything shown here today is a work in progress. Values are likely to be changed, features are final but details are not, all that good stuff. In particular, some of the adventurer contract rewards are currently a *smidge* high right now, so we’ll be taking those down a bit (specifically gold and prestige) pending further playtesting before release.  

Like the Administrative Government Dev Diaries, this will be a two-part dev diary. In part 1, we’ll go over the basic design and core gameplay loop, and then in the next diary, we’ll go into more detail about the individual nuts and bolts that make up this system.  

![001.PNG](https://forumcontent.paradoxplaza.com/public/1161599/001.PNG "001.PNG")


*[Overview of a Landless Adventurer’s camp]*  

---

### Why Adventurers?​

Alright, let’s start off with a question that I’m sure a few of you have been asking yourselves: why did we pick *Landless Adventurers* ahead of, say, nomads? Well, we’ve already given the answer to this on the forums, but let’s cover it again quickly for the folks who don’t follow every little dev post.  

Initially, we envisioned the expansion as being both systems-heavy and a detailed look at the Byzantine Empire; both highly requested focal points for a DLC. That, naturally, became Administrative play. We were then casting around for something to round that out, since an entire expansion that’s *just* Administrative and *just* Byzantium wouldn’t have much else for the rest of the map, which is a point of feedback we’ve gotten when we’ve done regional flavour packs previously — let alone a highly regional expansion.  

The focus would still be too narrow even if other areas might become Administrative over the course of a campaign, so we needed to add something a bit more broadly applicable. Another heavily systems-based government type would be too large, as we’d end up doing two government types poorly rather than one government type well. We investigated a few possible alternative features to see if we could portray them without detracting from the challenge of adding a whole new way of playing Crusader Kings III.  

![002.PNG](https://forumcontent.paradoxplaza.com/public/1161600/002.PNG "002.PNG")


*[Your camp exists in a physical place on the map, much like Estates do for Administrative characters.]*  

Of those, Landless Adventurers turned out to be the ideal candidate. A lot of the underlying technical work they required could be done with fairly little extra cost at the same time as Administrative gameplay, and they didn’t need the broad extra mechanics and systems that other governments would require to really feel like an improvement.  

Prior to this, Adventurers had been penned in as something we could maybe do late in the game’s lifespan. If we did them simultaneously with Administrative play, however, then they offered something we thought we could do a good job with without hurting either mechanic.  

Them having their own following of requesters was, of course, a nice bonus.  

Nomads et al will doubtless get their own time to shine, but we want to wait until a point when they can truly be the stars of their own shows.  

---

### The Vision​

Alright, so what do we see adventurers as even being? Crusader Kings is a game about marriage, inheritance, and complex realm politics; none of which really apply to wandering characters with nary a vassal to call their own.  

Well, simply put, we think of them as the ultimate underdogs: outsiders with no land or prospects, but also no responsibilities or restrictions. A landed character (even the lowliest baron) has a host of functionaries and regular income from taxable subjects, but they also have pressures on their rule that they can’t escape; the rigours of ritual and silent formality soak up their time and energy.  

![003.PNG](https://forumcontent.paradoxplaza.com/public/1161601/003.PNG "003.PNG")


*[With Roads to Power, you’ll be able to create a custom Landless Adventurer via the Ruler Designer at the start of a campaign.]*  

An Adventurer lacks that surety and those benefits, but they also have no demands on their time save those they *choose* to accept. They’re able to amass power through hard work and skill rather than privilege and history, and if they so choose, translate that power into a dramatic entrance onto the landed stage.  

We wanted to reflect this philosophy with a play style focused on travel and roaming, encouraging you to experience the map in a different way by moving across and spectating it — occasionally stopping to influence this realm or that when you have to proverbially sing for your supper. We wanted your camp to feel more intimate than your court, to have its characters be a bit more memorable. Afterall, in a travelling Adventurer band, your followers *are* your resources, and you’ll see them literally every day.  

Naturally, a core part of this is servicing the fantasy of forming a strong, mobile mercenary army, but we also didn’t want players to be restricted to *just* this. For every Roger de Flor, there’s an Ibn Battuta or a Marco Polo, after all.  

![004.PNG](https://forumcontent.paradoxplaza.com/public/1161602/004.PNG "004.PNG")


*[Adventurer Camps can be given a specific purpose, affording various bonuses or downsides to better accommodate their goals]*  

Finally, we wanted being an Adventurer to be viable as a short, mid, *or* long-term playstyle. Perhaps not one you’d pass an entire campaign in, but a short stint of landlessness before shooting your shot at reclaiming your lands (or conquering new ones) should be viable with a bit of effort, as should staying a wanderer for multiple generations at a time.  

Landing yourself should be possible (especially if you’re willing to take the indignity of an impoverished, remote county somewhere), but not something you can do with a click of your fingers and no prep work. Those unwilling to accept getting in on the lowest conceivable rung of the feudal ladder should have to actually try to climb higher.  

Overall, the idea was to create a closer relationship to your location on the map and incentives to explore it, whilst letting you build resources faster than some landed rulers — with sufficient work and at the cost of not being able to do so passively.  

---

### Adventuring Core Loop​

When playing as a Landless Adventurer, the basic gameplay flow is to find yourself in a new location (either because you’ve moved your camp there, or because you just became an Adventurer and started there), and to look around for work you could undertake.  

“Work” here means contracts — these appear as scrolls on the map, each of which represents a different job. What a job might be is fairly varied, both tonally and mechanically, and we’ll go into those in more detail in juuuuust one moment.  

![005.PNG](https://forumcontent.paradoxplaza.com/public/1161603/005.PNG "005.PNG")


*[Contracts are visible as scrolls on the map surrounding your Camp, with a different icon on the scroll depending on the type of contract it represents. The tier of the contract can also be determined by the number of stars at the top of the scroll.]*  

Each contract has a minimum of a pass state and a fail state with rewards/penalties for either outcome; though many have various alternate successes and failures depending on whether you get an exceptional result or a below-grade one. Generally, we only show you the standard rewards packages here.  

If you complete a contract to your employer’s satisfaction, you’ll receive resources like gold, prestige, sometimes piety, and the new Adventurer-specific provisions.  

As with Administrative families, Adventurers have a domicile — unlike the grand estates of an Administrative realm, our humble wanderers only have a camp to call their own. The gold they earn can be spent on building upgrades here, generally instituting new organisations or customs rather than permanent structures. Martially-inclined Adventurers may also spend it on building and maintaining large armies.  

![006.PNG](https://forumcontent.paradoxplaza.com/public/1161604/006.PNG "006.PNG")


*[Camps, like Estates, can be upgraded over time.]*  

Prestige is needed to advance your fame, which both governs the tier of rulers who’ll offer you contracts (kings and emperors won’t hand them out to just anybody, and even dukes look askance at those without a modicum of fame) and unlocks increasingly more powerful versions of ways to become landed.  

Provisions are spent to allow you to travel with your camp across the map. While you can move on low — or even no — provisions, you’ll suffer increasingly dramatic consequences for doing so.  

When you exhaust the contracts you wish to take in a particular area, you can most easily find new ones by moving your camp a significant distance away, or to a new de jure kingdom that you haven’t visited recently. Then you take new contracts, earn new rewards, and repeat the process as you move around the map. You gather new followers from different lands, try to balance your provision income vs. expenditure, and decide which contracts you think you’re capable of taking and when.  

![007.PNG](https://forumcontent.paradoxplaza.com/public/1161605/007.PNG "007.PNG")


*[Your camp can be moved to new regions of the world, but doing so costs Provisions.]*  

We do expect some players to want to be adventurers for as little time as possible, and others to want to be them for centuries at a time. Off-ramps are provided at various stages for players who decide they want to leave the life of an Adventurer. It’s up to you if you’d be happy taking a back-water county somewhere in exchange for a huge sum of cash, building an army to try retaking your throne, or simply drift around the world making your mark in a half a dozen small ways.  

---

### What is a Contract?​

Fundamentally, contracts are a vehicle for different types of content you opt into in hopes of a reward you generally see in advance. Different jobs offer different rewards, and rulers of higher tier in turn offer higher tier contracts with all-around better rewards.  

The jobs themselves range from helping in wars, to assisting councillor tasks, to educating children, to collecting back-taxes. They’re an abstraction of the word of mouth, heralds, spies, and town criers that would’ve filled this role historically but which are a smidge tricky to represent with neat, concise visuals, which is why we’ve gone for this sort of faux-noticeboard aesthetic.  

If this looks familiar to you from the Administrative dev diaries, well, it should! Governor duties use the same basic system for a little extra spice in their districts, but it was added primarily as a core mechanic for Adventurers to connect back to the world.  

![008.PNG](https://forumcontent.paradoxplaza.com/public/1161606/008.PNG "008.PNG")


*[An example of a contract. This one requires you to ambush travellers on the road.]*  

One thing I should probably nip in the bud immediately is what contracts you, as a landed ruler, can offer an Adventurer: with the exception of mercenary contracts, all contracts are offered by AI only.  

We approached them this way because they’re *the* core gameplay loop for Landless Adventurers, which means Adventurers are expected to do a lot of contracts. That means that variety is key in order to slow the rate at which individual contracts grow stale, and if they were bilaterally playable, that substantially more than doubles the complexity of just about every conceivable contract. Ultimately this means we’d be able to make far, far fewer of them.  

Essentially, we’ve opted to prioritise the experience of playing as an Adventurer rather than the experience of simply interacting with them. I know not everyone will agree with that decision, but I wanted to be honest about the rationale and hope you can understand why we’ve gone this way.  

---

### Nuts’n’Bolts​

When contracts appear on the map, they have an icon indicating roughly what type of job they’re offering you, as well as slightly nicer paper depending on the tier of the employer.  

Opening one shows you not just the potential rewards and penalties, but also who the employer is, a little narrative breakdown of what they want, and a plain-speech breakdown of what the contract’s mechanics will be.  

![009.png](https://forumcontent.paradoxplaza.com/public/1161607/009.png "009.png")


*[When viewing a contract, you can see a variety of details about what the contract entails.]*  

One thing you’ll notice quickly is that different contracts offer different rewards. Some might give you mostly gold or primarily prestige, others mainly provisions for the road, or a mix thereof. Contracts that offer possible critical successes will generally offer substantial extra rewards (either new currencies or more of the main reward) for achieving them — though the employer’s greed may compel them to offer much more or much less than usual too.  

This is to help encourage you to shop around for different contracts in different areas. Maybe you land in a kingdom full of tightfisted gits handing out paltry sums for substantial work, and decide to move on rather than waste your time even if it means stretching your provisions a little tighter. Maybe a contract that you usually wouldn’t take or might not be very good at happens to be offering rewards simply too good to pass up from a specific employer.  

![010.PNG](https://forumcontent.paradoxplaza.com/public/1161608/010.PNG "010.PNG")


*[Failing a contract, predictably, has drawbacks and consequences.]*  

The parameters tied to them also tend to uhh… *vary*. Some require no travel, some require you to travel the length of the map, while others might involve a small tour of a character’s realm. Some are made up of small linked event chains, others have their own custom micro-decisions. The more common a contract is likely to be, the more we’ve tried to focus hard on slight replayability and variability, so that the same contract is mechanically and aesthetically a bit different each time, even if you’re performing it twice in quick succession.  

Finding them is easy and automatic: contracts are discovered when you either move a certain distance or move to a new de jure kingdom that you’ve not been to recently. Occasional new contracts will also appear in place over time, and when you’re travelling, notable contracts may spring up along the route to encourage you to make pit stops.  

Exactly which types of contracts you’re likely to find is controlled by your camp purpose — teased in an earlier image, but something we’ll be going into more detail on next week.  

The base contract mechanic is free for modders to implement regardless of DLC ownership, but the vanilla version of the game only features paid uses of the system.  

![011.PNG](https://forumcontent.paradoxplaza.com/public/1161609/011.PNG "011.PNG")


*[The contract mechanic is freely modifiable.]*  

---

### Example Contracts​

We’ve added a raft of situational contracts tied to what’s going on in the game, a few that come specifically from content you see as you play, and then an underlying core that are generally valid unless you’re really far out in the wild tribal areas (so that Adventurers won’t run out of ways to earn money or provisions just because no one is currently using a certain council task).  

That’s… a lot of words and not enough pictures. Let’s take a second and game out a few contracts together, just to give you a more visual idea of how they play.  

As a reminder, we’re still in the throes of balancing right now, so these numbers are *not* final. Gold especially is noticeably too high in some contracts and too low in others. Don’t panic, they’ll be normalised before release.  

So with that in mind, here’s a ruler designed Adventurer I’ve just made: not the most interesting character, but a solid generalist with average or above average stats for everything but prowess. She should be suitable for most anything that crosses our path. I’ve got two starting followers, whose speciality in diplomacy I picked (though I could’ve chosen to start utterly alone had I wanted to) to help me.  

Shirin here begins in Kashmir, but longs to explore far from home, and she’s going to take us through a few example contracts.  

![012.PNG](https://forumcontent.paradoxplaza.com/public/1161610/012.PNG "012.PNG")


*[Shirin’s stats are well-rounded, which will allow her to demonstrate several types of contracts for us.]*  

#### Scheme Contracts​

First, we’ll try our hand at a very simple scheme contract. Some of these have on-going events, some are very simplistic, but they’re generally a nice easy way to earn a little coin.  

![013.PNG](https://forumcontent.paradoxplaza.com/public/1161611/013.PNG "013.PNG")


*[Shirin’s first contract is one with a Stewardship focus. Once more for those at the back, the rewards shown here are not final and will likely be changed before the final release of Roads to Power.]*  

We’ll be going into the changes we’ve made to schemes in a future dev diary, I expect, but as you saw in our last dev diary we now have different types of agents, a more deterministic approach to progression, and we’ve tried to broaden how accessible they are to characters with lacking Intrigue.  

This is a Stewardship scheme, so after travelling to the contract’s location, we get to decide what type of agents we’ll be relying on.  

![014.PNG](https://forumcontent.paradoxplaza.com/public/1161612/014.PNG "014.PNG")


*[Upon beginning the contract, you’re given several options on how to approach your task.]*  

I’ve only got two followers at the moment, so I’m not actually too fussed about my choice and opt for a balanced approach.  

![015.PNG](https://forumcontent.paradoxplaza.com/public/1161613/015.PNG "015.PNG")


*[Our camp followers are obvious choices for agents in this contract. We’ll go into more detail about the new Scheme system in the future.]*  

Lalit and Pran between them aren’t actually half bad at engineering, but they’re not great and we can’t fill out the rest of the agent slots just yet anyway.  

We’ll give this a little bit for the bar to start creeping upwards. I don’t want to spend too long here, I want to get out and see the world, but I can tarry a short while.  

![016.PNG](https://forumcontent.paradoxplaza.com/public/1161614/016.PNG "016.PNG")


*[Our camp followers, fortunately, seem to be getting along just fine. As camps tend to have fewer characters in them than landed courts, interpersonal events like this can be far more impactful.]*  

Oh, well, nice to see those two getting along. We’ve actually added some events for agents relating to each other in this DLC (both getting on and arguing) as part of the free update, so this might help my contract scheme.  

![017.PNG](https://forumcontent.paradoxplaza.com/public/1161615/017.PNG "017.PNG")


*[Camp followers aren’t as numerous as courtiers can be, but there are various ways to obtain additional followers.]*  

A wandering Tengri asks to join our camp. I can use all the help I can get right now, so we take her on.  

![018.PNG](https://forumcontent.paradoxplaza.com/public/1161616/018.PNG "018.PNG")


*[The new follower’s skills make her a great addition to our agents for this contract.]  

Well, well, well,* that was a good move.  

![019.PNG](https://forumcontent.paradoxplaza.com/public/1161617/019.PNG "019.PNG")


*[Schemes can be executed at any point, even if they’re not fully prepared.]*  

Alright, once I’ve capped my success chance here, I execute the scheme. I could wait around for better odds but I want to go travelling, so I’m gonna risk it for a biscuit.  

![020.PNG](https://forumcontent.paradoxplaza.com/public/1161618/020.PNG "020.PNG")


*[Successful execution of a contract.]*  

A fat purse for Shirin! Not bad for relatively swift work (pending further balancing for fun vs. exploitability).  

So, that’s a scheme contract. A bit involved, some set-up, some risk vs. how much time you’re willing to plough into it, but simple enough in practice.  

#### Event-Based Contracts​

As soon as we get back to camp, there’s light trouble in the ranks.  

![021.PNG](https://forumcontent.paradoxplaza.com/public/1161619/021.PNG "021.PNG")


*[Two of our camp followers are having a dispute. We have the option to side with either one of them, or stay out of it entirely.]*  

This is beneath me. I’m not their nanny, so I let them figure it out amongst themselves and look for an event-based contract instead.  

![022.PNG](https://forumcontent.paradoxplaza.com/public/1161620/022.PNG "022.PNG")


*[Another Stewardship contract. This contract has the potential for an Exceptional Success, which here gives slightly less gold but many more provisions.]*  

Looks suitable, and our stewardship isn’t too bad, so let’s give this one a go.  

![023.PNG](https://forumcontent.paradoxplaza.com/public/1161621/023.PNG "023.PNG")


*[Most contracts will require your character to travel to a specific location in order to carry the contract out.]*  

Once again, we need to travel to the contract location for this job, but it’s not too far and the forests of Lahore are beautiful.  

![024.PNG](https://forumcontent.paradoxplaza.com/public/1161622/024.PNG "024.PNG")


*[Some contracts will present you with a variety of ways to resolve them.]*  

We’ve got various options here: I can try to solve the problem with my own raw stewardship, but that’s got a chance of failure and I’m not *that* good. Alternatively, I could leave Pran here for a few years on loan, using his diplomacy to keep things calm.  

Since I don’t have a quartermaster officer, I can’t test their aptitude to see if they could solve the problem for me, but, finally, I *can* pass automatically in exchange for eating a chunk of stress.  

Well, Pran was fighting with Changshou (the Khitan Tengri I picked up) so maybe some time away would do him good. I opt to loan him out.  

![025.PNG](https://forumcontent.paradoxplaza.com/public/1161623/025.PNG "025.PNG")


*[Camp followers can be used to complete contracts in many different ways.]*  

Event-based contracts vary quite a bit. This was a relatively simple one, with a variety of different issues and solutions along the same theme that could’ve been presented, but others involve more complex chains that must be navigated successfully & in short order for your coin.  

#### Travel Contracts​

Let’s try something that’s a bit more involved next. The only remaining contract I’ve got in this area is prowess-focused, which isn’t exactly my speciality, so I take my camp west through the mountains and into Transoxiana.  

Here, several travel contracts await me and I leaf through them looking for one I find interesting.  

![026.PNG](https://forumcontent.paradoxplaza.com/public/1161624/026.PNG "026.PNG")


*[An example of a Transport contract. These generally involve far more travel than other contract types.]*  

![027.PNG](https://forumcontent.paradoxplaza.com/public/1161625/027.PNG "027.PNG")


*[Most contracts involving travel give you a choice of whether to take your camp with you or double back for them afterwards.]*  

We’re not exactly mercenaries, but uhhhh, we can probably escort a baron. He wants to go west, further into Khorasan, which suits me just fine, so I’ll be taking my camp with me on the journey.  

![028.png](https://forumcontent.paradoxplaza.com/public/1161626/028.png "028.png")


[Travel as a Landless Adventurer is subject to the same travel safety mechanics that were introduced in Tours & Tournaments]  

Oh. Right. The Struggle for Persia is happening.  

Okay, not a deal breaker: we built up some gold, let’s stick by our word and hire some travel options to boost safety — even if it means we won’t make a profit on this venture.  

Along the way, travel danger events bedevil us, Lalit manages to lose some provisions and get beaten up in a tavern fight, and I caught typhus.  

![029.png](https://forumcontent.paradoxplaza.com/public/1161628/029.png "029.png")


*[Not every contract pays off in the end, either in gold or effort]*  

But, we make it, earning a fairly measly 44 gold for our trouble and my disease. I’ll not be taking work from Na’ib Resan again, I think, but serves me right for taking a job from a measly baron.  

Higher tier travel contracts, especially those in less fragmented areas, tend to offer longer journeys and better pay.  

#### Councillor Contracts​

After waiting a few months for my illness to recede, I decide to take to the road again. The on-going war between Khorasan and Makran could last another year or two, and their battling makes all the travel I might have to do for contracts much riskier than usual.  

Seeking safer lands, I move west into Tabaristan: to the south, Arabia is embroiled in the Azariqa Rebellion, and to the north is steppe and desert that’s likely to pose its own dangers. We’re not going back home, so the west road towards the Caucasus is the easiest path open to us.  

![030.PNG](https://forumcontent.paradoxplaza.com/public/1161629/030.PNG "030.PNG")


*[From our camp, we survey the available contracts in northern Persia.]*  

Aha, shortly after arriving, I see a contract put out by the AI using their marshal to Increase Control. That’s another type of contract to demonstrate, so let’s take a look.  

![031.PNG](https://forumcontent.paradoxplaza.com/public/1161630/031.PNG "031.PNG")


*[An AI ruler puts out a contract to assist him in performing his duties as marshal.]*  

Looks like the rewards are mostly the same for both successes and exceptional successes here, but if I really succeed then I also get to add his boss to my Roll of Patrons (more on that in about a section or so) — his boss is a duke, and I’m not famous enough for them to give me work yet otherwise, so I’ll absolutely shoot for that.  

![032.PNG](https://forumcontent.paradoxplaza.com/public/1161631/032.PNG "032.PNG")


*[Agreeing to help the Marshal, we can see that we only need to deal with one county to complete the contract.]*  

We won’t be moving our camp that far south (we’re trying to avoid trouble rather than embrace it) so we travel with just our trusted followers and leave our domicile safely in Tabaristan.  

![033.PNG](https://forumcontent.paradoxplaza.com/public/1161632/033.PNG "033.PNG")


*[A few more complicated contracts include their own custom widgets for tracking purposes.]*  

Here, we can choose to try and stir trouble against our employer — which we might be able to utilise or which might just suit our goals in this part of the world — but we’re gonna stay honest and do our job instead. All we’re after is coin, not problems.  

The peasants cave to our pressure, and our reward is delivered swiftly. Emir al-Qasim is fortunate that only the one county in his realm is particularly low in control, but so are we: if he had less of a handle on things, we might’ve needed to tour quite a few more peasant holdings in order to earn our keep, the risk of failure increasing as we go.  

#### Mercenary Contracts​

Lastly, we’re gonna skip ahead ten years: Shirin adventures through Persia, Anatolia, and up into the belly of Europe. After a while of taking backwater contracts, she branches out into mercenary work, spending time profitably fighting her way through a shattered Poland’s many wars and gradually building up a respectable 1500 men.  

![034.PNG](https://forumcontent.paradoxplaza.com/public/1161633/034.PNG "034.PNG")


*[Followers you loan out for contract work will eventually make their way home.]*  

Along the way, Pran returns. He’s the same as ever, but he could easily have returned with a new faith, culture, skills, or spouse. If he was unlucky, maybe he wouldn’t have returned at all.  

Mercenary contracts are a bit of a special case, since adventurers, in particular, need to be wary of getting stack-wiped: an army obliterated in a moment is much more of a concern when you don’t have a realm to easily reinforce them, so even if your troops are powerful, you need to be wary of casualties.  

![035.PNG](https://forumcontent.paradoxplaza.com/public/1161634/035.PNG "035.PNG")


[Mercenary contracts are an excellent opportunity for martial-focused Adventurers to earn some gold.]  

Jaromir here is having a very bad day, and looking for, around, say… 1500 soldiers of no fixed paymaster.  

I think I know someone who can help.  

![036.PNG](https://forumcontent.paradoxplaza.com/public/1161635/036.PNG "036.PNG")


*[Shirin lost an eye whilst poaching.]*  

The war is actually pretty typical of the type I’ve been fighting in this area: large, unified polities are bad for business, so I take the side of the smaller independents (provided I can beat their attackers) and help them stay that way.  

![038.PNG](https://forumcontent.paradoxplaza.com/public/1161636/038.PNG "038.PNG")


*[An adventuring army hastens to reach its employer before the war ends.]*  

Whoops, bit of a mad dash to reach the battlefield in time here: the enemy actually has a slight numbers advantage, but I’m willing to bet my men-at-arms and camp bonuses can more than swing the result.  

![039.PNG](https://forumcontent.paradoxplaza.com/public/1161637/039.PNG "039.PNG")


*[Elite mercenary troops face off against a numerically superior landed army.]*  

Battle is joined!  

![040.PNG](https://forumcontent.paradoxplaza.com/public/1161638/040.PNG "040.PNG")


*[The smaller, more elite adventurer force inflicts more casualties, but its losses won’t be sustainable in a longer conflict]*  

And just as quickly, over. The enemy can reconstitute his forces much better than we can, but we’ve maimed him and taken his chancellor as a prisoner, so… reconstitute that, landy.  

As our pay depends on our contribution, we ideally want to keep hitting them whilst they’re weak, but we won’t win unless we can keep our employer’s lands unoccupied.  

![041.PNG](https://forumcontent.paradoxplaza.com/public/1161639/041.PNG "041.PNG")


*[With the enemy’s capital occupied and the employer’s lands freed, our adventurer needs just one more good battle to earn her pay]*  

A swift countersiege alongside our employer flips the warscore immensely in our favour. One more battle should end this.  

![042.PNG](https://forumcontent.paradoxplaza.com/public/1161640/042.PNG "042.PNG")


*[Round 2 goes as poorly for the foe as Round 1]*  

As if the clear result of the battle wasn’t enough, we capture our foe in the aftermath. Well, we’ve won anyway, so I ransom him quickly — my employer doesn’t need to know and couldn’t really complain if he did.  

![043.PNG](https://forumcontent.paradoxplaza.com/public/1161641/043.PNG "043.PNG")


*[A grateful employer pays his mercenaries]]*  

Chieftain Jaromir, an honest man, pays us our due. It’s a modest reward from a modest ruler, but at least he didn’t give me typhus.  

Were he a grander ruler, perhaps I’d try to do a few contracts for him to earn his good graces, then see if he’d take me as a vassal. I’m far from home, and I can’t keep fighting forever…  

---

### And a Very Special Thanks to all my Patron Supporters​

Of course, once you’ve done a contract for someone, you’re a bit more known to them than just any random wanderer.  

Most successfully completed contracts allow you to add your employer to your Roll of Patrons — although some, especially basic or simple contracts, may require an exceptional success before you can add your employer as a patron.  

Patrons are, simply put, people you can try to mooch off of. By burning opinion with them, you can extract favours, obtain unnegotiated rewards, and even garner things as exotic as marriages or troops. The more you try to take, the more annoyed they’ll get with you, and the less you’ll be able to rely on them for work in future.  

Family and friends can be lobbied for the same favours even if you’ve done no work for them.  

Provided they like you, of course.  

![043.5.PNG](https://forumcontent.paradoxplaza.com/public/1161642/043.5.PNG "043.5.PNG")


*[Your list of Patrons can be accessed from the camp view.]*  

Your list of your patrons is housed in your camp view.  

As Adventurers don’t have a fixed abode (we assume they’re move some nights even when stationary within one barony, travelling on as one area’s foraging gets bad or the locals get rowdy), let alone the infrastructure of a domain behind them, there are fairly hard distance restrictions on where you can ask patrons for favours from.  

You can see those in the interface here, as we divide the list up so that you can easily check who you can blag from now and who you need to pay a visit to mooch off of. The distance requirement stops you requesting support and favours from a string of people half a world away and encourages you to form local connections.  

---

### A Life of Crime​

Of course, not every jobbing Adventurer is a roving scholar out to teach the children of the world or engage exclusively in honourable mercenary work. Some of them, shockingly, have been known to lie, cheat, swindle, steal, kidnap, and kill.  

Enter the criminal contract.  

![044.PNG](https://forumcontent.paradoxplaza.com/public/1161643/044.PNG "044.PNG")


*[Criminal contracts are visually distinct from other contracts on the map.]*  

These have different icons on the map, they’re slathered in red and mud to mark them apart visually, and will tend to offer greater rewards for even mediocre successes. Criminal contracts may be performed on behalf of the employer (say, kidnapping their rival) or even targeting the “employer” themselves (for instance, preying on the travellers of someone foolish enough to advertise weakened wilderness patrols in their domain).  

![045.PNG](https://forumcontent.paradoxplaza.com/public/1161644/045.PNG "045.PNG")


*[Ambushing travelers gives the chance to attack pool characters, travelling rulers, and even other adventurers]*  

The drawback is that criminal contracts are… crimes, y’know?  

Unless you’re performing a crime on behalf of the employer (e.g., murdering someone for them), you’ll lose opinion with them rather than gain it and won’t add them to your Roll of Patrons. Depending on the exact crime you do, you may even lose prestige for succeeding due to your lowered reputation.  

A violated employer will also receive a criminal opinion of you, making them able to imprison you should they ever get the chance to try, and much more likely to try to evict you from their realm — an interaction we’ll be covering more next week.  

![046.PNG](https://forumcontent.paradoxplaza.com/public/1161645/046.PNG "046.PNG")


*[Criminal contracts generally pay very well for the amount of work that needs doing]*  

The real short-term consequence to undertaking criminal contracts is the Gallowsbait trait, which measures how much the world at large considers you to be an upstart, petty thug.  

Though there are some niche benefits to levelling up its various tracks, overall, this negative fame trait gradually makes the rest of the world hate you more and more as you successfully complete more crimes (with less successful criminals receiving lower amounts of trait xp for being less infamous).  

![047.PNG](https://forumcontent.paradoxplaza.com/public/1161646/047.PNG "047.PNG")


*[Gallowsbait has many different tracks, each reflecting a different category of crime that a Landless Adventurer might commit]*  

When a landed noble — or even a fancy courtier or a baron’s guest — commits a murder, it’s an exciting scandal for the history books. When an Adventurer loots a caravan in the woods, they’re just a petty bandit upstart deserving no more attention than it takes to tie the noose around their neck.  

Of course, some non-criminal contracts will also offer the chance to conduct yourself unlawfully, particularly if you generally fancy yourself something of a bandit.  

#### But I’ve Changed!​

Many a petty bandit, lying swindler, and deadly marauder have managed to make the jump to respectable landed ruler through the centuries, and they’ve generally got one thing in common: they know how to use their new gains to cover up their old crimes.  

Should you tire of the world’s disdain, either as an adventurer or a newly-minted lordling, you’ll probably want to lose those general opinion debuffs, and with the Wipe Slate decision, the world can be convinced to forget… for a price, of course  


![048.PNG](https://forumcontent.paradoxplaza.com/public/1161647/048.PNG "048.PNG")


*[Even the most foul of criminals can be forgiven if they have the coin to buy goodwill]*  

---

### Travel & Provisions​

Given that we expect you to move from county to county searching for work, what’s to stop you, say… moving from Brittany to Tibet in one long trip?  

Well, you can try it, I guess — if you’ve got enough Provisions, and assuming that travel danger doesn’t cost you any more on the way.  

![049.png](https://forumcontent.paradoxplaza.com/public/1161648/049.png "049.png")


*[Moving your camp costs Provisions. As you might expect, the Provision cost increases with distance.]*  

Since you don’t have any land of your own, you don’t have a steady source of income or way of obtaining food. When you’re camping out in a province, this isn’t too big of a deal: your followers can forage, do odd-jobs, or at least avoid calorie-intensive activities, so your provisions count won’t go *down.*  

We did experiment with the idea of a ticking reduction a bit during development, but found that it became too easy to get stuck in death spirals where not playing efficiently at all times would cause you to starve to death even in very silly scenarios (e.g., you can’t find enough food in high dev farmland in the middle of summer and die of starvation in a berry field). The intended flow is that if you’re stopped, you can tread water to give you a shot at refilling your provisions — if you stand a chance at completing any of the contracts in the area, that is.  

When you’re on the road, though, you have far less time for subsistence living and have to use whatever supplies you have in reserve: Provisions represent the sum total of your travelling rations, whatever water you’re carrying if it wouldn’t be easily obtainable otherwise, and even odds and ends like spare fabrics and tools for repairing your tents.  

![050.PNG](https://forumcontent.paradoxplaza.com/public/1161649/050.PNG "050.PNG")


*[Provisions use an apple as an icon.]*  

As an Adventurer’s camp moves from one barony to another, they expend provisions with every province they travel. The cost is determined by the terrain, plus the men-at-arms the adventurer has — every men-at-arms regiment now has a provision cost shown for adventurers.  

Light infantry tend to be cheap to feed, though their numbers may add up over time, whilst elephantry are positively hellish consumers of provisions, and elaborate heavy cavalry come with not only their beasts but their support personnel who need clothing and feeding too. Large armies will want to make pit stops to re-supply, whereas smaller camps of followers can often afford to go further on less.  

![051.PNG](https://forumcontent.paradoxplaza.com/public/1161653/051.PNG "051.PNG")


*[Moving even moderately sized mercenary armies is expensive, requiring you to build your camp to match your play style.]*  

Your maximum number of provisions is an increasable cap determined by the buildings in your camp. When you start to fall below a certain number, you’ll begin suffering privation events. These involve your followers losing faith, some leaving you or losing substantial amounts of opinion; eventually both you and your followers will risk lost health, permanent negative traits, and even death.  

![052.PNG](https://forumcontent.paradoxplaza.com/public/1161654/052.PNG "052.PNG")


*[There are seven different buildings for camps, as well as the central pavilion building.]*  

The closer you are to zero provisions, the worse the privation events you can receive. Never travel without provisions if you can help it.  

![053.PNG](https://forumcontent.paradoxplaza.com/public/1161655/053.PNG "053.PNG")


*[Travelling without provisions will frequently kill or permanently hurt you, as well as substantially reducing your armies.]*  

Otherwise, adventurers can travel to any barony on the map. The only limit is the size of your men-at-arms and the number of provisions you’ve stocked. Unless you’ve been exiled from a certain realm, of course — more on that next DD.  

The easiest way to gain provisions is from contracts, but they can also be obtained via hunt activities, a dedicated decision for foraging, events, and the new Visit Settlement decision (which: more on that last one next week, too).  

![054.PNG](https://forumcontent.paradoxplaza.com/public/1161656/054.PNG "054.PNG")


*[Even without hunting in a lord’s forests, adventurers can find ways to live off of the land.]*  

Of course, not every time an Adventurer travels requires them to take their whole camp with them, so they don’t *always* expend provisions when they move – only if their domicile is being moved around the map. You’re explicitly told when you’ll be spending provisions and how many you expect to expend.  

Good examples of travel that won’t generally cost provisions are things like turning up to a feast or tournament, or going on a pilgrimage. Contracts that involve travel generally give you the option of whether or not to bring your camp with you when you do, so if you’re touring some lord’s realm to collect taxes, you don’t need to pay as you go unless you choose to.  

We opted to add a new resource rather than just use the army supply map mode for this largely so that the whole military system doesn’t have to be tied to the balance of how adventurers play and vice versa, doubly so since not everyone is going to own the DLC.  

Narratively, you can think of it this way: an army on the move from a landed realm can forage much more aggressively — and with a lot less regard for local laws or consequences — than even a travelling mercenary company, which has nowhere to flee to other than its own camp.  

---

### Camps​

Like Administrative families, Adventurers have a domicile: unlike Administratives (who have majestic, sprawling estates), Adventurers have only a humble camp to call their own.  

![055.PNG](https://forumcontent.paradoxplaza.com/public/1161657/055.PNG "055.PNG")


*[A tribal camp in the snow with a mysterious guest.]*  

These camps have fewer building slots available than estates, but provide a partial refund of their construction costs on destruction (including if an Adventurer becomes landed). This gives you a bit more freedom to try different configurations of buildings and upgrades, changing them out over time and retooling your camp according to its current purpose or adapting to the changing world.  

![056.PNG](https://forumcontent.paradoxplaza.com/public/1161658/056.PNG "056.PNG")


*[Many camp buildings have upgrades that unlock unique camp officers.]*  

Also like estates, camp buildings have many internal upgrades, though these do not branch and can be applied in any combination. Some of these upgrades are locked to your camp purpose, meaning that adventurers don’t have access to all the same upgrades at the same time.  

Specialising in this way or that should pay dividends as upgrades, both internal and not, have various powerful benefits, and many of them unlock new types of officers (the adventuring equivalent of a court position).  

![057.PNG](https://forumcontent.paradoxplaza.com/public/1161659/057.PNG "057.PNG")


*[Some camp buildings are less savoury than others.]*  

In addition to your Roll of Patrons (which we discussed earlier), we have the Camp Temperament.  

This is a simple measure of how many of your followers (the adventurer equivalent of courtiers) actually like you: if the majority like you, you get bonuses, if the majority dislike you, you get penalties, and if there’s no majority, you get nothing.  

![058.PNG](https://forumcontent.paradoxplaza.com/public/1161660/058.PNG "058.PNG")


*[Your followers at camp make their opinions known via modifiers.]*  

The bonuses and penalties scale according to your prestige level, so less notable adventurers have a bit more slack to ignore this, whilst more famous ones must manage their camp more carefully.  

Of course, you can ask any follower you dislike to to leave your camp, but their friends and family (who are likely travelling with you too) will likely take offence and may leave too.  

Removing followers is certainly doable, but something you likely want to take a gentle approach to rather than exiling anyone who disagrees at the drop of a hat — you’re not a feudal ruler and people won’t treat you like one.  

![059.PNG](https://forumcontent.paradoxplaza.com/public/1161661/059.PNG "059.PNG")


*[A happy camp schemes better and fights better.]*  

![060.PNG](https://forumcontent.paradoxplaza.com/public/1161662/060.PNG "060.PNG")


*[An unhappy camp schemes slower and fights poorly.]*  

Happy followers pay dividends in events, whilst unhappy followers may, if left long enough, resort to… drastic measures.  

---

### Key Differences from Landed Play​

We’ll round out now by going over a few remaining key differences between Adventurers and non-adventurers, with further nitty-gritty to follow in the next dev diary.  


### The Fresh​

Probably the largest obvious change in pure content would be the lifestyle trees, which have been completely redone for any effects that wouldn’t be immediately useful to adventuring characters.  

This includes new modifiers…  


![061.PNG](https://forumcontent.paradoxplaza.com/public/1161663/061.PNG "061.PNG")


![062.PNG](https://forumcontent.paradoxplaza.com/public/1161664/062.PNG "062.PNG")


… new effects…  


![063.PNG](https://forumcontent.paradoxplaza.com/public/1161665/063.PNG "063.PNG")


![065.PNG](https://forumcontent.paradoxplaza.com/public/1161667/065.PNG "065.PNG")

![064.PNG](https://forumcontent.paradoxplaza.com/public/1161666/064.PNG "064.PNG")



… and modified content.  


![066.PNG](https://forumcontent.paradoxplaza.com/public/1161668/066.PNG "066.PNG")


![067.PNG](https://forumcontent.paradoxplaza.com/public/1161669/067.PNG "067.PNG")


![068.PNG](https://forumcontent.paradoxplaza.com/public/1161670/068.PNG "068.PNG")



The lifestyle trees remain largely the same for ordinary landed characters. Mechanically, the perks are the same and only the functionality is flipped, so becoming an Adventurer with a full tree or two of perks starts you out with many useful things already unlocked, whilst an Adventurer becoming landed carries over their experience into their new life.  

### The Familiar​

#### Renames​

As an adventurer, you’ll notice a few things renamed for immersion. The most obvious are that your courtiers will be generally referred to as followers instead, and your court positions as your camp officers (we’ll be going into those in a lot more detail in the next dev diary).  

Functionally, they’re still the same things working in the same way, but aesthetics are important too.  

#### Activities​

On this front, you’ll be unsurprised to hear that Adventurers cannot host grand activities of any kind, nor can they host proper feasts. They *can* hunt, though if they don’t have permission from the local ruler (generally obtained via the Roll of Patrons) then it constitutes poaching (with the appropriate Gallowsbait awarded). Hunting awards provisions regardless. Pilgrimages and university visits (for owners of Wards & Wardens) are accessible as normal.  

There are, however, no restrictions on inviting adventurers to things, so they can turn up as guests anywhere they’re invited to. Some of the new Adventurer lifestyle perk variants allow you to request feasts, and even tournaments, from other characters for you to attend.  

Replacing the grandiose, luxurious affair of even the humblest noble’s feast, Adventurers instead receive the new camp revelry micro-activity, having fun and getting drunk under the stars. Here they can relieve stress and gain opinion with their followers, which is important for managing your camp temperament.  

![069.PNG](https://forumcontent.paradoxplaza.com/public/1161671/069.PNG "069.PNG")


*[Adventurers have access to a new micro-activity to replace lordly feasts.]*  

#### Miscellaneous​

A small but noticeable facet of adventuring is that they cannot demand conversion of their followers unless they’ve built a specific camp building upgrade, the portable shrine. Adventurers lack the compelling force to be able to effect such drastic life changes with simply a demand: followers can be expelled, but they won’t abandon their faith unless you’re at least somewhat invested in yours.  

![070.PNG](https://forumcontent.paradoxplaza.com/public/1161672/070.PNG "070.PNG")


*[Without a portable shrine, adventurers cannot attempt to convert their followers.]*  

Less noticeable but no less important was the work done by the two designers to update old content for both adventurers and administrative characters. I was uhhhh, lucky enough to be performing vital… other… duties when this job was handed out, and they tore through nearly 900 events, over 200 decisions, and more than 160 character interactions to update their mechanics and loc to work for landless play.  

I wish good luck and good mental health to whichever poor bastards get stuck doing the same for our total conversion mods. Godspeed.  

---

### The Future​

As we talked about towards the start of this dev diary, Adventurers don’t really experience succession politics in the same way that even the smallest realm does. There are no laws binding them save their own will, and comparatively little to be divided or fought over anyway — even a successful mercenary company is just one or two bad wars away from complete ruin.  

Instead of access to electives, partition, or complex single heir preferences, camps are locked to a single succession type: the title will be inherited by your oldest child (or next closest relative), provided they are your follower. Characters not considered part of the camp cannot inherit it, meaning it will never be inherited by any character with a title of their own (though prisoners and wards are valid).  

If no relative is available, the follower with the highest prowess inherits instead, and the camp passes from your dynasty.  

Though they are locked to this succession, Adventurers do still receive some benefits for their independence, gaining access to two powerful tools of succession: they may freely designate their valid heir, and they may adopt any successor willing to agree as a child of their own.  

Children adopted in this fashion join the character’s dynasty, but immediately spin off their own new house to mark their unorthodox lineage.  

![071.PNG](https://forumcontent.paradoxplaza.com/public/1161673/071.PNG "071.PNG")


*[Succession in a camp is informal at best, allowing them to adopt freely from amongst willing characters.]*  

---

### The Forgotten​

As they have no lands to use their council tasks on, and because many of the benefits would be simply pointless for them, Adventurers do not have councils or councillors. Core benefits/mechanics of a council (like a spouse’s stat buffs or your spymaster catching schemes) are instead taken in by your Second-in-Command, a camp officer available to all.  

Additionally, unless you have some leverage over them or a truly fantastic reputation, rulers generally won’t marry their children into a smelly band of wanderers, no matter how noble some of that band may once have been. You cannot even ask them unless they are on your Roll of Patrons.  

Of course, you can work your way up the prestige levels, do a contract for a king, and see if you can squeeze a marriage to yourself or your child out of them, but… that’s a lot of work to put in, especially if they marry your intended spouse off in the meanwhilst, versus swallowing your pride and simply wedding a peasant.  

Likewise, Adventurers cannot use the Invite to Camp interaction on anyone but close relations and player heirs. Your camp may pick up many people on the road, but you cannot offer the stable life at court that a landed ruler or Administrative family can.  

![072.PNG](https://forumcontent.paradoxplaza.com/public/1161674/072.PNG "072.PNG")


[By design, Landless Adventurers must find or earn their characters manually — they cannot simply lure them in with the promise of a bed at court.]  

Finally — and as I’m sure should be obvious from everything else I’ve said — Adventurers do not use legitimacy mechanics.  

---

### End of Part 1​

Alright, that’s the core flow, key differences, and what you can expect to experience as the bread and butter of adventurer play. I’ll be back next week with more details on specifics, so stay tuned!  

As ever, I’ll be around in the thread for the next couple of hours to answer questions, duck accusations, graciously and humbly accept compliments, steal ideas, etc., etc.

<!-- artifact:reactions:start -->
- 173 Love
- 103 Like
- 15 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)**
Role: Former CK3 Experienced Game Designer
Badges: 102
Messages: 528
Reaction score: 15,169

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
