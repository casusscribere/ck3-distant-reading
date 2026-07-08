---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1320994/"
forum_thread_id: 1320994
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 12
title: "CK3 Dev Diary #12 - The Stewardship Lifestyle"
dd_date: 2020-02-04
author_handle: Voffvoffhunden
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2365
inline_image_count: 26
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1320994'
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
    location: raw_lines_~28_to_153
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_155_to_157
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_441_to_443
    action: preserved_and_flagged
    counts:
      Like: 3
      (unlabeled — rendered as base64 data URI): 2
      Love: 1
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_451_to_521
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_522_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #12 - The Stewardship Lifestyle

<!-- artifact:thread_metadata:start -->
- Thread starter [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)
- Start date [Feb 4, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-12-the-stewardship-lifestyle.1320994/)
<!-- artifact:thread_metadata:end -->

Hello everyone!  

Welcome to another dev diary about another wonderful Lifestyle and its associated Perks!  


This week I'm speaking to all you budding entrepreneurs and fiduciary financiers. No, this is not about another long-requested game that ends with the number 3, but the Stewardship Lifestyle!  

Stewardship covers all things gold, and all things relating to the development and management of your realm. The three focuses you can choose between are:  


![Stewardship focuses.PNG](https://forumcontent.paradoxplaza.com/public/530468/Stewardship focuses.PNG "Stewardship focuses.PNG")


[Wealth Focus - Monthly Income: +10%]  
[Domain Focus - Stewardship: +3]  
[Duty Focus - Stewardship: +1, Courtier and Guest opinion: +20]  


**Wealth -** grants a flat bonus to income, for when you need that slight gold-making edge.  

**Domain -** increases your Stewardship, with the various internal bonuses that grants.  

**Duty -** gives a small increase to Stewardship, and a large increase to Courtier and Guest opinions. It can be very helpful when it comes to keeping those closest to you loyal.  

Keep in mind that all values are subject to change as development continues!  

The goal of the associated perk trees are to offer new ways of emphasising these areas - your income, your development, and internal people management (the “HR branch”).  


![Stewardship Lifestyle Traits.png](https://forumcontent.paradoxplaza.com/public/530461/Stewardship Lifestyle Traits.png "Stewardship Lifestyle Traits.png")



**Avaricious**  

Avaricious is the course of gold, naturally enough, and it provides a number of new potential sources of income.  

![golden obligations.PNG](https://forumcontent.paradoxplaza.com/public/530452/golden obligations.PNG "golden obligations.PNG")


[Golden Obligations - You can Demand Payment for Hooks]  

Golden Obligations lets you demand money in exchange for Hooks, rather than the usual demand of enforcing your will in some matter. Considering a Dynasty Head gains Hooks on all Dynasty Members, I am personally very fond of levying the “family tax” when I want to build something ostentatious.  

If your Hooks don’t provide enough gold, you can dig a little deeper for it:  


![It is my domain.PNG](https://forumcontent.paradoxplaza.com/public/530454/It is my domain.PNG "It is my domain.PNG")


[It is MY Domain - Can use the Extort Subjects Decision]  

Extort Subjects lets you demand money from your vassals, holdings, courtiers, etc., although while the money might seem free in the short term, there are usually tradeoffs that need to be made, depending on exactly how you’re extorting it…  

When using the Decision, you'll be offered a specific opportunity - targeting a specific Powerful Vassal, for example - and get to make a decision about how hard you want to lean on them. Sometimes you only need a little extra gold, after all.  

Lastly, if you don’t feel good about taking money while offering little in exchange, you can sell “titles” piecemeal instead.  


![At any cost.PNG](https://forumcontent.paradoxplaza.com/public/530444/At any cost.PNG "At any cost.PNG")


[At Any Cost - You can use the Sell Titles Decision]  

Note that the Sell Titles decision does not involve selling your Landed Titles, but small meaningless knighthoods and honoraries instead. The cost is typically Prestige, or the dilution of the concept of nobility at all. How much you make depends on the gullibility of your subjects, or to what degree they find ways of turning the situation to their advantage or not...  

So with these perks, you'll have a lot of options when you need that extra pile of gold to pay for something.  

There are also more passive sources of income as well, for the feinschmecker who prefers to have their existing wealth work for them.  


![Heregeld.PNG](https://forumcontent.paradoxplaza.com/public/530456/Heregeld.PNG "Heregeld.PNG")


[Heregeld - Vassal Tax Contribution: +5%]  

![Detailed Ledgers.PNG](https://forumcontent.paradoxplaza.com/public/530458/Detailed Ledgers.PNG "Detailed Ledgers.PNG")


[Detailed Ledgers - Republican Ruler Opinion: +20, Republican Tax Contribution: +10%]  


And what’s this? The powerful getting richer by keeping their realm at war? What kind of silly fantasy world is it we’ve invented for this game?  


![War profiteer.PNG](https://forumcontent.paradoxplaza.com/public/530463/War profiteer.PNG "War profiteer.PNG")


[War Profiteer - Monthly Income while at War: +25%]  


Speaking of keeping your realm at war, money can buy you a lot of things, but only Dread can buy you an eager and willing army.  


![Fearful Troops.JPG](https://forumcontent.paradoxplaza.com/public/530445/Fearful Troops.JPG "Fearful Troops.JPG")


[Fearful Troops - Men-at-Arms Maintenance per Dread: -0.5%]  

Oh, wait! I guess that gold can also buy you an eager and willing army. We’re gonna talk about Mercenaries in a future dev diary at some point.  

If, after all that, you’re still not getting enough money, you can have the **Avaricious** trait. It’ll keep you going until you suffocate under the weight of your wealth, by providing you with a small boost to Stewardship, and a sound, direct boost to your monthly gold income.  


**Architect**  

But maybe it’s not all about dying with the biggest pile of money? Maybe it’s about leaving an imprint on the world? That might not be as crazy as it sounds. But what would that ever be?  

The biggest buildings, of course! Let’s see what the Architect tree has on offer.  

To start with, there’s a few perks to improve your ability to build things, naturally enough:  


![Cutting Cornerstones.PNG](https://forumcontent.paradoxplaza.com/public/530447/Cutting Cornerstones.PNG "Cutting Cornerstones.PNG")


[Cutting Cornerstones - Building Construction Gold Cost: -10%, Building Construction Piety Cost: -10%, Building Construction Prestige Cost: -10%, Holding Construction Gold Cost: -10%, Holding Construction Piety Cost: -10%, Holding Construction Prestige Cost: -10%]  

![Professional Workforce.PNG](https://forumcontent.paradoxplaza.com/public/530457/Professional Workforce.PNG "Professional Workforce.PNG")


[Professional Workforce - Building Construction Time: -30%, Holding Construction Time: -30%]  

This way you can build your realm up fast, and on the cheap, no matter what kind of constructions you’re looking for.  

You can also find improvements to the growth rate of Development in your capital:  


![Centralization NEW.JPG](https://forumcontent.paradoxplaza.com/public/530443/Centralization NEW.JPG "Centralization NEW.JPG")


[Centralization - Development Growth in Realm Capital: +0.2/month]  

I’m getting wistful here. Once you’ve been a game developer for a while, any kind of “Development Growth” bonus is something you dream of every day.  

Now, if you enjoy building, but your pesky Holding Limit is holding you back… Well, there’s a Perk to help you out!  


![Divided Attention.PNG](https://forumcontent.paradoxplaza.com/public/530451/Divided Attention.PNG "Divided Attention.PNG")


[Divided Attention - Domain Limit: +2]  

It’ll leave you with EVEN MORE LOCATIONS TO BUILD IN!  

If you have this many titles, though, you might end up with a lot of uppity peasants under your control, and they might even get dissatisfied. Unbelievable, I know (considering everything you do for them, such as organise their money into neat stacks), but far more likely than you think. But don’t worry! Popularity can, in fact, be bought:  


![Popular Figurehead.PNG](https://forumcontent.paradoxplaza.com/public/530467/Popular Figurehead.PNG "Popular Figurehead.PNG")


[Popular Figurehead - Popular Opinion: +50]  

Hopefully that will be enough to keep the peasants in line...  

If the threats against you are external, rather than internal, there are organizational tools to help you deal with those, too. Never give in to those who want to take away what you’ve BUILT WITH YOUR OWN TWO hundred thousand peasant HANDS!  


![Defensive Measures.PNG](https://forumcontent.paradoxplaza.com/public/530449/Defensive Measures.PNG "Defensive Measures.PNG")


[Defensive Measures - Fort Level: +1, Garrison Size: +20%]  

![Organised muster rolls.PNG](https://forumcontent.paradoxplaza.com/public/530459/Organised muster rolls.PNG "Organised muster rolls.PNG")


[Organized Muster Rolls - Levy Reinforcement Rate: +100%]  


What’s that you say? This dev diary has become too much about building things, and not enough about extracting wealth from things? Fine. Here, have a perk to help your Steward with that.  


![Tax Man.PNG](https://forumcontent.paradoxplaza.com/public/530462/Tax Man.PNG "Tax Man.PNG")


[Tax Man - Collect Taxes effectiveness: +25%]  


All this adds up to **Architect**, a trait that is going to keep your realm constructing around the clock. Not only does it grant you a Stewardship bonus, but it further reduces the Building Construction time! Castles and towers will soon be sprouting across your realm like toadstools after the rain.  



**Administrator**  

Now, I wouldn’t begrudge the more nobility-and-obligation-minded among you if you have started to think that Stewardship doesn’t offer you anything. Making money is precisely why you have a Steward to assign work to, after all. But don’t be so quick to judge! No matter who you are, you are going to have annoying vassals (and possibly lieges) to deal with. And boy do we have a tree for you.  

![Likable.PNG](https://forumcontent.paradoxplaza.com/public/530465/Likable.PNG "Likable.PNG")


[Likable - Direct Vassal Opinion: +10, Liege Opinion: +20]  

![Positions of Power.PNG](https://forumcontent.paradoxplaza.com/public/530466/Positions of Power.PNG "Positions of Power.PNG")


[Positions of Power - Councillor Opinion: +20]  

![Toe the Line.JPG](https://forumcontent.paradoxplaza.com/public/530446/Toe the Line.JPG "Toe the Line.JPG")

  
[Toe the Line - Your Vassals are less likely to join Independence Factions]  

These passive bonuses are going to be a godsend when it comes to keeping your realm together.  

If you want something more active, you can improve your Chancellor’s efforts to foster good relations with your vassals:  


![Chains of Loyalty.PNG](https://forumcontent.paradoxplaza.com/public/530448/Chains of Loyalty.PNG "Chains of Loyalty.PNG")


[Chains of Loyalty - Domestic Affairs efficiency: +25%]  

Sometimes, being viewed positively isn’t quite enough, and you have to employ harsh measures that may or may not be perceived as “unjust”, “vicious”, or “tyrannical”. Wouldn’t it be great if people didn’t get so hung up in the details, but focused more on the gifts you sent them afterwards?  


![Soon Forgiven.PNG](https://forumcontent.paradoxplaza.com/public/530464/Soon Forgiven.PNG "Soon Forgiven.PNG")


[Soon Forgiven - Monthly Tyranny: -0.05]  

But what’s the point of having all these loyal vassals if they don’t do anything for you? Well, loyal vassals do a lot for you, actually. But what if they did a little *extra*?  


![Large Levies.PNG](https://forumcontent.paradoxplaza.com/public/530453/Large Levies.PNG "Large Levies.PNG")


[Large Levies - Vassal Levy contribution: +10%]  

And those who are offered the highest respect and esteem should also contribute the most, should they not?  


![Honored to Serve.PNG](https://forumcontent.paradoxplaza.com/public/530450/Honored to Serve.PNG "Honored to Serve.PNG")


[Honored to Serve - Happy Powerful Vassal Tax contribution: +25%, Happy Powerful Vassal Levy contribution: +25%]  

A “Happy Powerful Vassal” refers to a Powerful Vassal who sits on the Council. You will have a really hard time making them actually happy, trust me. The ungrateful curs.  

So what if you don’t have a bunch of vassals? Maybe you’re not the top of the feudal heap, even though you clearly should be?  


![Meritocracy.PNG](https://forumcontent.paradoxplaza.com/public/530455/Meritocracy.PNG "Meritocracy.PNG")


[Meritocracy - You can use Claim Throne against your Liege]  

A Scheme called “Claim Throne” can obviously only ever be risky, but you can employ it against your Liege to get a claim on the realm. It’s a lot easier to get put into power by a Claimant Faction than by generations of unpredictable inheritance, after all.  

The Scheme itself is a Hostile Scheme that relies on Learning and Intrigue, and uses agents. The most powerful agents will be your Liege’s Council Members. You’re going to need a lot of powerful support to convincingly stake your claim, after all. Even though you are obviously the rightful ruler.  


Lastly, at the end of the path waits the **Administrator** trait. It’s a slight mix of both worlds, improving your vassal’s opinions of you, while also slightly reducing build costs.  

That’s all the new stuff for this week! I hope you’re all already drawing financial charts and editing your family history to make your claim sound somewhat legitimate. The Stewardship Lifestyle provides many paths to gold, stability and prosperity.  



**Notes on modding**  

Before I go, however, I want to highlight some parts of the moddability of this system. There were a series of questions following last week’s dev diary, and I should elaborate on those a little.  

The structure and setup of the different perk trees is scriptable, which means that one can easily add things, move things around, set different requirements for each Perk, etc. And as someone asked, it’s also possible to make all Perks in a lifestyle form a single big tree, instead of three separate ones, and it *is* possible to have multiple "entry points" and "end points" for a single tree.  

When it comes to what a modder will be able to make a Perk do… well, pretty much anything. Giving character modifiers, running specific effects, being used as a trigger for other things... If you can think of it, there's probably a way of making a perk do it. You can also make entirely new Lifestyles, if you have a good idea for one!  

I can think of half a dozen different uses for this system to a modder, and it wouldn’t surprise me if they quickly find ways of using it that haven’t even occurred to us. So while you’re patiently and excitedly waiting to play the game, I’m equally excited to see what the inspired people of our modding community are going to get up to!  


Next time we'll be looking at the Learning Lifestyle, and some associated things. We won't be going into detail about Religion just yet, but the Lifestyle still has a lot of cool stuff to it that I can't wait to share.  

Until then!

 

#### Attachments

- [![Golden aplomb.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/530460/Golden aplomb.PNG)](https://forum.paradoxplaza.com/forum/attachments/golden-aplomb-png.543105/)
  
  Golden aplomb.PNG
  114,7 KB

 · Views: 1.442

<!-- artifact:reactions:start -->
- 3 Like
- 2 (unlabeled — rendered as base64 data URI)
- 1 Love
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)**
Role: Rouge Game Dev - Former CK3 Content Designer
Badges: 74
Messages: 261
Reaction score: 1,286

*[Full game-badge icon list of 3 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
