---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1922255/"
forum_thread_id: 1922255
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 2
title: "\"Silk & Silver\" Dev Diary #2 - Trade Vision"
dd_date: 2026-05-12
author_handle: chaddling
expansion: Silk & Silver
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2864
inline_image_count: 17
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1922255'
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
    location: raw_lines_321_to_326
    action: preserved_and_flagged
    counts:
      Love: 104
      Like: 97
      (unlabeled — rendered as base64 data URI): 1
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_334_to_444
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_445_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# "Silk & Silver" Dev Diary #2 - Trade Vision

<!-- artifact:thread_metadata:start -->
- Thread starter [chaddling](https://forum.paradoxplaza.com/forum/members/chaddling.1717140/)
- Start date [May 12, 2026](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-2-trade-vision.1922255/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-2-trade-vision.1922255/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-2-trade-vision.1922255/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-2-trade-vision.1922255/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22945](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-2-ecclesiastical-power-rites.1920599/ "&quot;By God Alone&quot; Dev Diary #2 - Ecclesiastical Power &amp; Rites") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-3-puppets-theocratic-play.1923707/ "&quot;By God Alone&quot; Dev Diary #3 - Puppets &amp; Theocratic Play")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-2-trade-vision.1922255/?prdxDevPosts=1)

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_banners/4/4497.jpg?1778577633)

# "Silk & Silver" Dev Diary #2 - Trade Vision

- Thread starter [chaddling](https://forum.paradoxplaza.com/forum/members/chaddling.1717140/)
- Start date [May 12, 2026](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-2-trade-vision.1922255/)

Greetings!  

I’ll be following up on the overall vision dev diary with a deeper dive into our design for the Trade System. We’re starting our feature-specific dev diaries with Trade because, as you’ll see, it is connected to nearly every other feature we’re developing for Silk & Silver. But before we get into it, remember that all screenshots are work-in-progress and we are in the middle of development. Everything is subject to change.  

Trade is a new layer that not only provides a new mechanic primarily used by Mercantile Governments, but more importantly, makes economic play more strategic for all characters and connects buildings on the map to actual gameplay. It’s where the other features in Silk & Silver meet and clash, where mercantile empires and trade leagues are born.  

When you start your first Trade Route in Silk & Silver, the economic engines of the medieval world will already be turning. Your job is to muscle your way in and carve out your niche.  

![image_01.gif](https://forumcontent.paradoxplaza.com/private/1496459/image_01.gif?t=1781010673&amp;sig=7536819e8c6b115ef80a2f21b1ef5e6d "image_01.gif")




![divider_01.png](https://forumcontent.paradoxplaza.com/private/1496460/divider_01.png?t=1781010673&amp;sig=5929f404855e20c1f1a499ee84aeb911 "divider_01.png")


Before we get into how Trade plays out moment-to-moment, let's lay out all the levers we will have at our disposal. The Trade system is built from a handful of core concepts: Markets, Goods, Categories, Routes, and Monopolies. Each has a clear function, but they interact constantly. We'll take each in turn.  

Trade Markets  

The world is filled with over 900 Trade Markets, one for each de jure duchy on the map. Each Market is located in the capital barony of its de jure duchy and serves all of its constituent holdings inside that duchy area. These are defined on game start and do not move.  

**![image_02.png](https://forumcontent.paradoxplaza.com/private/1496462/image_02.png?t=1781010673&amp;sig=d860c26342bdae54db7552b60f8c18b2 "image_02.png")**​


Trade Markets track the overall Trade Good Productions and Needs of their constituent holdings. They are the mercantile hub of the area. Holding the de jure duchy capital where the Market is located provides you with some bonuses like being able to hand out Monopolies (discussed below).  

Trade Goods  
At time of writing, there are over 40 types of Trade Goods scripted in the game. These are entirely defined by script, so yes, modders, you can go wild.  

**![image_03.jpg](https://forumcontent.paradoxplaza.com/private/1496463/image_03.jpg?t=1781010673&amp;sig=0e7c569a69537b975f22f18a58dc9584 "image_03.jpg")**​


Trade Goods are primarily produced in Resource Production Districts and their associated Buildings. We track Production via modifiers on provinces. The system is designed to be quite flexible to allow for content and other systems to affect production, buy/sell price, and other factors.  

Trade Categories  
When a building needs grain to feed its workers, it doesn't really care whether it gets grain, millet, or rice. What it really wants is *cereals*. Cue Trade Categories.  

Trade Categories group related goods together so the system can express needs at the right level of abstraction. Some categories are simple: Salt is a single-good category. Others, like Cereals or Meats, can be filled by any of several substitutable goods. This becomes important in two places: when buildings broadcast what they want, and when monopolies claim an entire slice of the market, but more on those below.  

**![image_04.jpg](https://forumcontent.paradoxplaza.com/private/1496464/image_04.jpg?t=1781010673&amp;sig=1d0e78a47c8056b0da07f541a885c504 "image_04.jpg")**​


Trade Routes  **Trade Stats**  


- **Max Routes** — how many routes you can run simultaneously.
- **Max Markets per Route** — how many stops a single route can string together.
- **Range** — how far from your home market a route can reach.
- **Capacity** — how much a single route can carry in terms of Trade Good quantity.
- **Competitiveness** — how aggressively the route claims its share when contested. (Big enough topic that we'll come back to it below.)

Most of these grow as you invest in the trader assigned to the Route, your Domicile buildings, and your route history. Specialization and commitment compound.  

Primary Goods & Trade Expertise  
Every Trade Route designates one of its goods as the route's Primary Good. This is the route's specialty, the thing it gets better at over time. Trading a Primary Good earns Trade Expertise in that good's category, and as a category levels up, the merchant gains stacking bonuses to how well they trade goods in that category.  

**![image_05.png](https://forumcontent.paradoxplaza.com/private/1496467/image_05.png?t=1781010673&amp;sig=ef4f5fc950c79ad82ad90c513a9ee58c "image_05.png")**​


A merchant who's mongered cheese for forty years isn't just a simple cheese trader. They're *the* Cheesemonger of Europe, and the system is built to reward exactly that kind of patience. Pick a good, stick with it, and let the years compound.  

**![image_06.png](https://forumcontent.paradoxplaza.com/private/1496469/image_06.png?t=1781010673&amp;sig=399849aa96f7357df351224081ac9fe0 "image_06.png")**​


Trade Expertise lives on the merchant's title rather than directly on the character, so progression survives succession. Your heir inherits the family's hard-won reputation and resumes the work.  

Acumen  
Acumen represents a Merchant's business savvy. It grows month by month based on the *profit* they actually pull in, not the volume they move or how many routes they run. At higher levels, Acumen unlocks personal bonuses that lift every Trade Route the Merchant owns. The intent is a subtle pressure to stay profitable and reward sharp deals.  

Traders  
The quotidian tasks of a Trade Route are managed by a Trader. Traders are characters you assign from your Associates or family members. A Trader's skills shape what their route is good at, affecting things like Competitiveness, for example. A well-rounded Merchant Company means you can maximize the effectiveness of all your Trade Routes  

Competitiveness  
When more than one merchant tries to sell salt in the same market, who wins? Cue Competitiveness. Each route's share of a market's trade is determined by its Competitiveness relative to the Competitiveness of other Trade Routes trading that same good.  

You don't get exclusivity without a Monopoly (discussed below). Instead, you get a slice proportional to your Competitiveness score. That makes Competitiveness the single most contested stat in the system. Investing in your Competitiveness is a key way to garner success as a Merchant and ensure that you are able to buy and sell up to your maximum potential.  

Monopolies  
A Monopoly is the ultimate version of Competitiveness. Where Competitiveness lets you compete for a share, a Monopoly locks the market down entirely. Other traders simply cannot move that category of goods through a market you have monopolized.  

Monopolies are granted by the holder of the market's capital, and they can be granted to a specific merchant, to a republic, or to an entire Trade League whose members all share the privilege. Two types exist:  


- **Normal** monopolies respect local needs and claim the entire surplus.
- **Exploitative** monopolies pull goods from local demand too, enriching the monopoly holder at the expense of the markets.

**![image_07.png](https://forumcontent.paradoxplaza.com/private/1496470/image_07.png?t=1781010673&amp;sig=3dd3b4832395162c88d3bc4755f10a35 "image_07.png")**​


Both of these types can be on a single Category, or extended over an entire Market, making it a complete market monopoly.  


![divider_02.png](https://forumcontent.paradoxplaza.com/private/1496471/divider_02.png?t=1781010673&amp;sig=4074e501143254cc8b7bc6f0ead124a2 "divider_02.png")


The Trade Loop Overview  
Trade connects Trade Markets and balances their surplus productions with needed goods. Once a month, every market in the world calculates what it produces and what its buildings need. Routes then look at those balances and propose trades: buy up some surplus from one market, sell it for a tidy profit (if you have a Mercantile government) in a market with a deficit. The system resolves all of these proposals, adjusts balances across all the markets, settles the profit accumulated, and marks which Buildings' Needs are fulfilled.  

Needs & Productions  
**Needs** come from buildings. Many buildings require certain trade good types or categories: grain, leather, iron, dyes, etc. That demand is rolled into its market's monthly Needs.  

**Production** comes from Resource Production Districts and their associated Buildings.  

**![image_08.png](https://forumcontent.paradoxplaza.com/private/1496472/image_08.png?t=1781010673&amp;sig=ca936352cbdfbdd804d7e70b22e6a573 "image_08.png")



![image_09.png](https://forumcontent.paradoxplaza.com/private/1496473/image_09.png?t=1781010673&amp;sig=944be86e68a6d4ba5a3c8c1e7b4b23c4 "image_09.png")**​


When Production exceeds Need, the market has a Surplus available to export. When Need exceeds Production, the market has a Deficit waiting to be filled. Buildings sit at the heart of the new economy and your decisions about which buildings to construct directly shape how markets behave and, consequently, what the trade landscape looks like from game to game.  

Trade for Landed Rulers  
If you're playing a settled ruler with land to manage, Trade is mostly something that happens *to* you. You don't profit from trade routes, and you can't really go toe-to-toe with merchants for market share. What you *can* do is run what we're currently calling Acquisition Routes (the name is still in flux): routes that exist purely to move goods into your lands so your buildings get what they need.  



These are incredibly limited, though, and you'll rely on Merchants to fulfill the vast majority of your Needs. They're the ones who'll actually fill your markets at scale. So you build relationships: invite merchants to your court, grant them concessions, contract them to fulfill a certain Need, etc. How you interact with them is entirely up to you, but remember that the carrot usually works better than the stick.  

Trade For Merchants & Republics  
If you're a Merchant or a Republic, Trade is your whole world. You run Profit Routes with the goal of buying low in surplus markets, selling high in deficit markets, and most importantly, profiting. You compete with market rivals, lobby for Monopolies, level up Trader skills, build Acumen, and stitch together a network of Markets that compounds over generations.  

**![image_10.png](https://forumcontent.paradoxplaza.com/private/1496474/image_10.png?t=1781010673&amp;sig=a2787680a5915c049bfe9d357d2f2fc3 "image_10.png")**​


Setting up a Trade Route  
Setting up a route is the central action of mercantile gameplay. You pick a chain of markets you want to connect, choose which goods you'll move, designate one as your Primary Good (the route's specialty, and the category for which you'll earn experience in), and assign a Trader to run it. The route then becomes a persistent thing in the world, visible on the map, generating gold (only for mercantile characters), aging, leveling, and over time perhaps even paving roads as it goes.  

**![image_11.png](https://forumcontent.paradoxplaza.com/private/1496475/image_11.png?t=1781010673&amp;sig=f93f1149ac2f4efcda00b00a89864ae7 "image_11.png")**​


Routes require a certain level of commitment. You can edit them, sure, but you can't shuffle them around entirely or replace a route so completely that it becomes the Route of Theseus. A route's defining characteristics matter.  

Monthly Recurring Trade  
Once a route is running, it's largely self-driving. Each month, every active route ticks: it buys from its source markets, sells in its destination markets, settles the books, and credits your treasury. You don't *need* to micromanage, though you very well can and should if you want to squeeze every last piece of gold out of the economy.  

**![image_12.png](https://forumcontent.paradoxplaza.com/private/1496476/image_12.png?t=1781010673&amp;sig=12544bc54fd2cfaa65b813341f07f320 "image_12.png")**​


Wars, plagues, building changes, and competitor pressure all shift the numbers month-to-month. A perspicacious merchant will notice when a profitable route starts slipping and intervene before it breaks; one who doesn't may simply wonder why their income is quietly eroding as the months pass by.  

Trade Posts  
Trade Posts are the long arm of a Republic. A Republic ruler can establish Trade Posts in county capitals across the world. Trade Posts host their own buildings (which benefit the Republic owner, not the local ruler) and let a Republic project economic power into territories it doesn't actually control. You'll hear more about these in a future dev diary.  

Roads  
Trade leaves marks on the map. Where routes run consistently between two Markets year after year, roads emerge: first as worn paths, then proper roads, climbing through tiers as the routes hold their course. Each tier moves armies a bit faster, makes travel a bit safer, and adds a variety of modifiers along the way. Stop trading, and the road decays. We'll dig into roads further in a future dev diary.  


![divider_03.png](https://forumcontent.paradoxplaza.com/private/1496477/divider_03.png?t=1781010673&amp;sig=eb2501d587d02689679e65403da6472e "divider_03.png")


One question we know we'll get is: *How will the AI handle all this?* This, along with economy balancing, is something we are seriously iterating on as we develop the expansion. Merchant and Republic AI characters create routes, pick goods, assign Traders, lobby for monopolies, and compete with you for market share. Currently, the new system feels populated: markets aren't empty until you show up to trade in them; they're already busy, and your job is to muscle in.  

We're still tuning, and will continue to do so until release. The AI doesn't yet do everything we want it to, and we'll keep iterating through the rest of the production cycle. But the foundation, i.e. AI characters being real participants in the economic world instead of background scenery, is in.  

Other areas we have a keen eye on are ensuring the AI has competitive strategies for determining building chains to construct and, on the flip side, that AI Merchants make smart trades without min/maxing like some players might.  


![divider_04.png](https://forumcontent.paradoxplaza.com/private/1496478/divider_04.png?t=1781010673&amp;sig=06a1f52660da033ac62ef5b8a531af55 "divider_04.png")


That's the vision. Trade in Silk & Silver is the layer where buildings, characters, geography, and politics all push against each other. It's a system that wants you to build empires of cheese, medicaments, salami, and silk; one that rewards specialization and patience; and one that makes the world feel populated with economic competitors and allies.  

We've left out some detail here on purpose. A more technical dev diary will follow closer to release where we'll dig into the mechanics, modifiers, script, etc. For now, we wanted to give you the shape of the system and a sense of how it'll feel to play. See you in the comments.

<!-- artifact:reactions:start -->
- 104 Love
- 97 Like
- 13 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [chaddling](https://forum.paradoxplaza.com/forum/members/chaddling.1717140/)**
Role: Game Designer
Badges: 57
Messages: 56
Reaction score: 2,122

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
