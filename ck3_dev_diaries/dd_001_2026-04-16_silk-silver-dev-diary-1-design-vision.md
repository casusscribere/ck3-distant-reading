---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1917178/"
forum_thread_id: 1917178
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 1
title: "\"Silk & Silver\" Dev Diary #1 - Design Vision"
dd_date: 2026-04-16
author_handle: Snow Crystal
expansion: Silk & Silver
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 4721
inline_image_count: 25
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1917178'
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
    location: raw_lines_~28_to_120
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_122_to_123
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_396_to_401
    action: preserved_and_flagged
    counts:
      Love: 223
      Like: 125
      (unlabeled — rendered as base64 data URI): 4
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_409_to_510
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_511_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# "Silk & Silver" Dev Diary #1 - Design Vision

<!-- artifact:thread_metadata:start -->
- Thread starter [Snow Crystal](https://forum.paradoxplaza.com/forum/members/snow-crystal.1280952/)
- Start date [Apr 16, 2026](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-1-design-vision.1917178/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-1-design-vision.1917178/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-1-design-vision.1917178/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-1-design-vision.1917178/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22945](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-195-salve-in-domino.1914929/ "Dev Diary 195: Salve in Domino") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-1-tenets-spiritual-fulfillment.1919114/ "&quot;By God Alone&quot; Dev Diary #1 - Tenets &amp; Spiritual Fulfillment")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-1-design-vision.1917178/?prdxDevPosts=1)

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_banners/4/4442.jpg?1776772678)

# "Silk & Silver" Dev Diary #1 - Design Vision

- Thread starter [Snow Crystal](https://forum.paradoxplaza.com/forum/members/snow-crystal.1280952/)
- Start date [Apr 16, 2026](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-1-design-vision.1917178/)

Hello there,  

Today I have the honor of telling you a little bit about what is coming in this year’s major expansion, *Silk & Silver*. I talked a little bit about it in the announcement video, but this is the moment to put it all out here in a bit more detail for your enjoyment. Strap in, because we have a whole lot of different things to go through!  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1485426/image_01.png "image_01.png")


Unlike this beautiful illustration we got from one of our artists, there will be a number of unfinished things pictured in this thread, as the expansion is still in the middle of its development. Keep that in mind as you read through the dev diary.  


The Vision of Silk & Silver  

In the High Middle Ages, Flanders imported high-quality wool from England and transformed it into fine clothing sought after across Europe. Silk came from the Far East through the Silk Roads. You saw the rise of numerous republics and free cities, signaling the emergence of a new class. The burghers, the merchants, not people who had the right background or dynastic blood, but the ones who knew how to make money and use it well.  

For Silk & Silver, we wanted to really showcase the period's growth, as it was, in many ways, a very transformative time in history. Small villages and hamlets would become flourishing cities, and already notable cities would grow into historical metropolises. From the 11th to the 14th centuries, Paris grew from 20,000 to 30,000 people to over 200,000, and we want this to be something one could experience in the game in some capacity.  

So what were our goals going into this expansion?  


- Rework the economy of the entire game
- Make trade, merchants, and republics an integral part of the economic simulation of the game
- Distinguish between different cities and areas of the map, e.g., Paris is not the same as any other French city
- Make the map visualize the growth and change of the world over time
These are the main pillars of this DLC and the accompanying patch:  


- Merchants
- Republics
- Trade
- Economy Rework

![image_02.png](https://forumcontent.paradoxplaza.com/public/1485427/image_02.png "image_02.png")



![basics of trade.png](https://forumcontent.paradoxplaza.com/public/1485428/basics of trade.png "basics of trade.png")


Before we look at anything else, we will start by taking a look at trade. As an entirely new feature that connects everything else in the expansion, it’s good to get everyone on the same page with what it is and what it isn’t, before we move on to the other features.  

Trade is a new feature that allows merchants and republics to move trade goods around the world to meet demand in different markets. At its core, it is about finding areas that produce a trade good and supplying it to areas that need it. It will primarily be done by mercantile governments (merchants & republics), but landed rulers may be able to move goods within their lands to a lesser extent.  

Every duchy in the world counts as its own separate market, and every province will have a new set of buildings (this will be discussed later) that will produce or require trade goods for its market, meaning we have just over 900 separate markets in the world of CK3 come Silk & Silver. For trade goods produced within a market, they will be available for local consumption before they are available for purchase by foreign traders.  

As for trade goods, they are special goods created in provinces across the whole world. You will build farms, mines, or workshops that will create, grow, or mine different types of trade goods that can, in turn, be used or repurposed in other buildings. Every county now has a new type of slot focused on crafting/making these trade goods, which we call the “resource district” (more about districts later).  

I won’t give you a full list of all our new trade goods right now, but you can see a selection below (we have just short of 50 trade goods in total).  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1485429/image_03.png "image_03.png")


These trade goods will then, in turn, be consumed by new “building needs”. A need is effectively an optional modifier on a building that will only be active if it is regularly supplied with the trade good (or goods) it needs. For example, a fishing hut may produce more fish if it is regularly supplied with salt, and a port may produce more taxes if it is supplied with wood for its ships. For landed rulers, this means trade goods will be necessary to make the most of their lands, whereas for mercantile rulers, it means an opportunity to profit from bringing goods over.  


![establishing a trade route.png](https://forumcontent.paradoxplaza.com/public/1485430/establishing a trade route.png "establishing a trade route.png")


When establishing a trade route, you have a fair number of limitations that decide what you can do with a trade route:  


- Number of trade goods on the route
- Number of markets on the route
- Length of the route
- How many goods can be moved on the route in total
- How competitive the route is
As a newly minted merchant setting up your first trade route, you are fairly limited in both scope and potential for what you can do with your trade route. You will find some key goods you can work with in your vicinity, and then trade relatively close by (think up to a couple of markets away at most).  

At first, it will be a small trickle of gold that comes in regularly as you are still finding your footing, before your trade company and family become better known for your mercantile endeavors. As you continue trading a specific trade good, your family will slowly become better at handling it and will gain some boons for that trade route, as well as gain experience with that good in general (improving the sell price for that good and other small boons).  

As your company and family continue to grow their power and prestige, they will slowly be able to dominate the trade of specific trade goods and specific areas, gaining monopolies and squeezing out the competition.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1485431/image_04.png "image_04.png")



![mercantile governments.png](https://forumcontent.paradoxplaza.com/public/1485432/mercantile governments.png "mercantile governments.png")


In the expansion, we have two new playable government forms, the republics and the merchants. The two of them share some similarities, as both are based on the trade system in some ways, but they also have distinct differences. To make it simple, the merchants are landless, whereas the republic and its patricians are focused on the competition for a landed title (the republic city).  

They both focus on building their family-owned company and share a domicile. For the domicile this time around, it is a big focus of ours to make it really feel like you are settled in a city and part of it, rather than creating your own little villa area like the administrative government types do. It is a key component in the progression of the mercantile governments, as they can improve their trade capabilities with many of their domicile buildings.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1485433/image_05.png "image_05.png")



![life of a merchant.png](https://forumcontent.paradoxplaza.com/public/1485434/life of a merchant.png "life of a merchant.png")


The new merchant government form is inspired by the many important mercantile families that existed throughout the medieval world, and these were not necessarily tied to a specific piece of land or state. Think of the Jewish families in Cairo that traded goods far and wide, or the trade guilds of southern India.  
While as a merchant, you do not own land, unlike your republic peers, you are still situated in and around a city. You are a landless character with a domicile in your home city and the local ruler as your patron. It will be possible to change the location of your domicile, but it is not supposed to be a regular occurrence, as it is going to be the heart of your little budding trade empire. All trade routes you establish as a merchant will use the domicile location as their starting point.  

One thing to mention is that merchants are essential for the new trade system to work. In many ways, they are the roots of the new system that connects everything in the world. They are the main caretakers and providers who fulfill needs across all markets. In other words, they are important enough for landed rulers to engage with at times to ensure that their provinces are actually getting the goods they need, and they give merchants some power in relation to their landed patrons.  
Merchants have a gameplay loop focused on making gold, which can be turned into prestige. Prestige, in turn, will open up opportunities for improving how much gold you can make. As merchants, similar to their landless adventure peers, aren’t blue-blooded, they have a bit of a harder time making prestige than regular landed rulers, and they need it to be taken seriously if they are to engage with the nobility for trade deals and the like.  

In their day-to-day, the merchants have a couple of things to focus on. They have new “trade opportunity” contracts they can engage with, which will allow them to oversee their trade routes, temporarily improve their trade capability, and gain luxury artifacts to add to their domicile.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1485435/image_06.png "image_06.png")


The merchant starts off as a small-time trader in their local area, and as they improve their trade capabilities, they will have the opportunity to increase their Company Size, a set of laws that reflect how well-known your trade company is worldwide. You go from being an unknown to becoming a prominent merchant family, something akin to the famous banking families of Italy and the HRE of the late Middle Ages and early Renaissance.  

In addition, the merchant companies offer several purposes to choose from, so you can decide which kind of interactions you excel at and what kind of focus you want. You can be a creditor, a war profiteer, or perhaps a caravaneer who has an easier time engaging in longer trade routes. These exist for the company as a whole, but also as a trait for merchant characters to improve over time, if they so wish.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1485436/image_07.png "image_07.png")


And I am not here to tell you how to spend your mercantile wealth, be that investing it into domicile artifacts, controlling the markets, bending the local rulers to your will, or investing it in the land you live in and becoming a republic. Say, speaking of republics…  


![city of marbles.png](https://forumcontent.paradoxplaza.com/public/1485437/city of marbles.png "city of marbles.png")


The republics of Silk & Silver are inspired by their namesakes from the Middle Ages, but unlike Crusader Kings 2, we are not limiting ourselves only to the maritime republics of Genoa, Venice, Amalfi, and Pisa. We are going for the whole spectrum, from the many republics of Italy to the free cities of the Holy Roman Empire to the Hanseatic League in the Baltic Sea. The goal is to serve you no matter where you are: in Florence, Venice, or even in the Commune of Rome.  

The people of the republic are all focused on holding the city in which they are settled, and they have regular elections to determine just that. We have the doges and podestas who hold temporary leadership titles, and the patricians who vie for power and authority beneath them.  

Whereas merchants are fulfilling needs across all markets, republics tend to create a small nucleus of trade focused around their capital, which stretches outwards. And as the republic grows stronger, this trade power becomes larger and larger. In addition, since republican rulers also have land, they can create synergies between what they want to trade and what is happening in the republic at any given time.  

For the republics, we have added a new system we call “assembly”, which is a law-focused voting mechanic. Basically, it allows anyone in the republic to propose laws for a vote, and then gives every member of the assembly time to vote. And this includes laws on who is even allowed to vote in the assembly in the first place, be that all the patricians, patricians and city vassals, or perhaps just your council.  

For us, the goal was to simulate a real-life situation in which many of these republics originally started as quite communal and often ended up as signorias, effectively ruled by a single lord. So you will see the republics start out with many laws that favor all the patricians, but you will have opportunities to limit your opponents over time.  

Unlike their landless peers, the people of the republic have access to trade leagues and trade posts. Trade posts will be small districts that can be built in other people’s lands, where you can effectively impact your ability to trade in that province, and you can nudge things you are interested in. They are inspired by the factories and the kontors of the late Middle Ages, basically.  

Trade leagues, on the other hand, are effectively confederations of republics that come together to form a stronger trade group and protect one another. Think the Hanseatic League or the Swiss Confederation. They protect one another and improve the trade capabilities of all league members. Think of the Hanseatic cities coming together to form a strong trade bloc that can effectively bully all of Scandinavia into submission.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1485438/image_08.png "image_08.png")



![economy province reworks.png](https://forumcontent.paradoxplaza.com/public/1485440/economy province reworks.png "economy province reworks.png")


This part of the dev diary will most likely be the most immediately visible thing for anyone who opens the game after we release this DLC and its accompanying patch. All of the changes discussed in this section of the dev diary will be coming free with the patch, as they are essential for the rebalancing of the game’s economy.  


Districts & Buildings  
Before anything else, we should discuss buildings and districts. I have already mentioned districts a couple of times throughout the dev diary, so it is time for a clarification. We often found it weird that, as a ruler, you would build *a brewery* or *a windmill*. It always felt a bit underwhelming, and with few building slots, it was hard to dig deeper into the system, as there wasn’t a lot of room to add anything.  

As part of our rework, we have removed every single regular building in the game (note, we have mostly kept all the special buildings that existed, but they will all see tweaks to their effects). Instead of having building slots, we will now have district slots instead, with districts in them. A district is effectively a thematic folder for buildings, where you will build a district (which will have some effects by itself), and then you will be able to build buildings within the district afterward. Instead of building an e.g., a smithy, you will be able to build a district for artisans that you can then fill with different buildings like a smithy.  

The goal is that a district is an investment, whereas the buildings are more easily switched and cheaper to replace if need be, and they will be flavorful and thematic. So you will see districts focused on the military, markets, urban life, or even on keeping the city small so it can remain an effective rural location. Speaking of size…  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1485441/image_09.png "image_09.png")


Development Changes  
Development was always meant to symbolize both how wealthy an area is and how many people live there. It could lead to some weird results, where one would be conflated with the other, and vice versa. So, for Silk & Silver, we are splitting development into two: “Settlement Size” and “Prosperity”.  

Prosperity is a measure of how rich and prosperous a county is, and it will affect how likely traders are to drop by (as they will make more money there), as well as multiplying the amount of tax obtained from the county.  

Settlement Size is a measure of how many people live in the city in the barony (a county capital will differ from other holdings, for example). We will use a 1-10 scale to track size in a somewhat abstract way. Size will directly affect how many district slots are available in the province, so you will, for example, see a whole lot more districts in Constantinople than you would in, e.g., the capital of Sweden. But in turn, we have added new rural districts that will benefit from smaller sizes, while counties with larger settlements face challenges to both county control and popular opinion within the county.  

Control Changes  
County control will no longer always max out at 100, as it used to before. We will now have a new baseline system, where different things will add to the baseline control you can have, to showcase that different counties and districts work differently.  

Your capital will always have relatively high control, as this is where you are situated and live, but your other titles will need a bit of… encouragement to actually pay taxes and the like. You will be able to gain control from stationing Men-at-Arms, building castles and fortifications in the area, from different eras, and most likely, some more districts will give bonuses to control as well.  

Since this system works a bit like, e.g., Court Grandeur, you can gain effects that temporarily increase it beyond the baseline. For example, let us say your current baseline is 40; that is now the number control will always trickle towards. Then you can gain effects that could bump up your current control to 60 or 80, but it would then trickle down towards 40 again, as that is only a temporary boon to the area.  

The goal is that it will take a bit more investment to ensure that a county is worthwhile conquering, and that holding more land in itself is not useful if the people who live there aren’t *incentivized* to give you any taxes.  

Popular Opinion changes  
For Popular Opinion, we are using the same baseline changes we have for control, but instead, it is now a bar from -100 to 100. Similarly to control, it means you can now gain a temporary popular opinion that will bump the current opinion up or down, but it will trickle back towards what the popular opinion is at any given time.  

Unlike before, there will now also be positive effects from having a positive level of popular support. Higher levels of popular opinion will have a direct effect on control in an area, which means that you will, in turn, gain more from the county as a whole.  

Below is an early mock-up of how we plan to make the county view going forward.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1485442/image_10.png "image_10.png")


Economy  
All of the things mentioned above will, of course, have a large impact on the economy. In addition to these sweeping changes, we will also take a look at every single part of the game where we interact with the economy in the game. Meaning that we will go over all the costs and all gold gains in the game.  

The goal is to significantly slow the snowballing economy in the game and make the player and AI economies more in line, so it is not as easy to overpower all your neighbors. As part of this rebalancing effort, we are exploring splitting modifiers. Instead of getting a general income bonus, you may gain “maritime income” bonuses instead. Instead of gaining a bonus to building speed in general, you would get a bonus to military district building speed instead, etc. Our goal is to minimize the places where we have been very liberal in handing out modifiers to players before, and to flavorize them into smaller boons instead.  

The goal and hope are that, with more interesting levers to pull, we can do more interesting things with less, and in turn affect the snowball effect across the game with plenty of tweaks all over.  

As a fun little side note, here’s a picture from one of our whiteboard sessions, trying to make a good visual map of what affects what. I am sorry for our terrible handwriting. But not sorry enough not to share the picture. Note that these are, of course, not the only things interacting with these different values, but it is rather about how these specific values interact with each other.  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1485443/image_11.png "image_11.png")



![italian flavor.png](https://forumcontent.paradoxplaza.com/public/1485444/italian flavor.png "italian flavor.png")


While it is not the main focus of the DLC, we also want to take the opportunity to add some flavor to the Italian region. It is home to many historical republics and at the heart of the mercantile transformation I described earlier in the diary.  

Guelphs & Ghibellines  
The Guelphs & Ghibellines conflict was a conflict between the Kaiser and his supporters on one side, and the Pope and his supporters on the other. It is related to the investiture crisis, but it also spun into a bit of a local conflict in Italy on its own about how much power the Kaiser should have over the area. This latter bit is what we are focused on for Silk & Silver.  

We are representing the conflict through one (kinda two) new situations situated around Northern Italy. At the 1066 start date, it hasn’t properly started yet, so you have a prelude situation that will slowly grow into the proper one, whereas in 1178, it is already in full swing.  

I am not going to go too deep into how it works just yet, so here’s a picture for now.  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1485445/image_12.png "image_12.png")


Miscellaneous Italian Flavor  
Just so they are mentioned, we are also looking into some other pieces of content for Italy in this DLC.  


- A new Carnival activity
- Redrawing the Italian map (welcome back, Amalfi)
- Looking into Italian cultures cultural traditions, and historical setup

A work-in-progress picture for the carnival.  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1485446/image_13.png "image_13.png")


Now, I want to be clear that Italy is one of the things we are looking at in the DLC, but unlike All Under Heaven, which focused solely on fleshing out regional flavor and mechanics, it is not a main focus here.  

This update will be focused quite a bit on mechanics, on trade, and in doing so will also touch Italy, but this is not for Italy what All Under Heaven was for East Asia, and it is also not what Roads to Power was for Byzantium (where the main government mechanics were all centered on one empire).  


![what we're not doing.png](https://forumcontent.paradoxplaza.com/public/1485447/what we're not doing.png "what we're not doing.png")


Since this will be a topic both asked about and discussed, if we do not bring it up ourselves, I will rip off this band-aid sooner rather than later. There will be no naval warfare or naval battles in this DLC. We know this is a topic people care about and relate to the republics strongly, but between a whole lot of balancing and a whole lot of new systems that we are adding to the game, we chose not to spend time and energy on trying to pack in another large feature that we would not be able to give it enough love and time to do well.  

To put it lightly, even the most minimal of minimum viable product implementations of naval warfare would blow our schedule out of water, and there are a lot of other changes in the expansion that carry a fair amount of risk, which we want to make sure can do as well as possible.  

There will be trading across the water, but we will not engage in naval warfare.  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1485448/image_14.png "image_14.png")



![conclusion.png](https://forumcontent.paradoxplaza.com/public/1485449/conclusion.png "conclusion.png")


Thank you for taking the time to read everything. I know we have covered a fair amount of topics, and not necessarily in great detail. Moving forward, we will alternate dev diaries for By God Alone and Silk & Silver, so you’ll hear more from us in the Silk & Silver team in a couple of weeks.  

We hope you are as excited about this expansion as we are about bringing it to life. Please leave comments and questions below, and I will do my best to answer them. Though I want to stress that we won’t go into detail on everything quite yet, even in the responses, as there’s still a lot of work left to do.  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1485451/image_15.png "image_15.png")

<!-- artifact:reactions:start -->
- 223 Love
- 125 Like
- 12 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Snow Crystal](https://forum.paradoxplaza.com/forum/members/snow-crystal.1280952/)**
Role: Game Designer - Crusader Kings 3
Badges: 63
Reaction score: 12,090

*[Full game-badge icon list of 41 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
