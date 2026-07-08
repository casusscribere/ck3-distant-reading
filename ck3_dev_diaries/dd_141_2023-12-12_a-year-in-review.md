---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1616623/"
forum_thread_id: 1616623
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 141
title: "Dev Diary #141 – A Year in Review"
dd_date: 2023-12-12
author_handle: rageair
expansion: Legacy of Persia
patch: Patch 1.11
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2345
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1616623'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2764.jpg?1702383672
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_285_to_288
    action: preserved_and_flagged
    counts:
      Like: 120
      Love: 81
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_296_to_383
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_384_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2764.jpg?1702383672)
<!-- artifact:thread_banner:end -->

# Dev Diary #141 – A Year in Review

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Dec 12, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-141-a-year-in-review.1616623/)
<!-- artifact:thread_metadata:end -->

Greetings!  

For those of you who do not know - I am Rageair, the Game Director of Crusader Kings III, and as we’re coming up to the end of 2023 it's time to look at this year in review - and take a quick glance toward the year to come! I will share our reflections, learnings, and opinions on the content we’ve made this year, and - while this diary will not be a roadmap/floor plan per se - I’ll make sure to share as much as I can about 2024.  


---

### **2023 in Review**​

So, what have we done in 2023? Quite a few things, it turns out!  


#### ​

#### **The Community Choice Poll**​

We started out the year by having a Community Choice Poll for the theme of the upcoming Event Pack, where among the three themes (Wards & Wardens, Love & Lust, and Villains & Vagabonds) the winning theme was Wards & Wardens, which gained 41.5% of the over 10,000 votes.  

While it was fantastic to see all the engagement, we won't be doing another poll for this year's event pack - mainly because we want something that will improve and expand upon existing content as well as content we're introducing next year, and we already have the perfect event pack for that in mind!  

We will instead continue reading your discussions, thoughts, and suggestions and focus on making content for areas that you would like to see expanded - it’s a more indirect way, but remember that you still have plenty of opportunity to affect what we do by simply discussing themes, ideas, or mechanics as you do normally.  

That said, it’s not impossible that we’ll have another poll in the future, especially if there’s demand for it!  


#### ​

#### **Tours & Tournaments**​

The highlight of the year was definitely Tours & Tournaments, our second Major Expansion. It made strides to connect the characters to the map, with travel, activities, and much more - and it’s obvious that the efforts were appreciated! While the expansion and its update leaned more towards roleplaying with its centerpiece Grand Activities, it also contained plenty of systems that enhanced the game overall, such as travel, regencies, MaA Stationing, etc. This combination made it a quintessential CK3 expansion that appealed to most (if not all) of you in the community, and we’ll definitely take a lot of learnings from the things we did right when looking into what to do for the future. All in all, we consider T&T a huge success!  

Of all the features we developed, travel is the one that we didn’t necessarily expect to be as fun as it turned out to actually be - we knew that it would be good, and fill a void that has existed since the early days of CK, but it turned into a very versatile system that we’re very likely to keep developing and progressively weave into as many other systems that we can. Travel also provides a great and versatile foundation for all sorts of features that may or may not appear in future updates…  

The expansion itself took a lot of time and effort to develop, over 10,000 days of work from various disciplines. During, and especially towards the end of the project, we started doing parallel development in order to up our cadence of releases, something which we’re successfully carrying with us into 2024. For those of you who might not be familiar with the concept, it means that we worked on several different expansions & updates with smaller teams-in-teams, all at the same time. During 2023 we have been working on roughly three different things at once, and at certain points as many as five! With the learnings we’ve gained from T&T, we’re keeping up the momentum as we want you to have a steady stream of content to look forward to - and we always want to make sure that we can make one Major Expansion per year!  


#### ​

#### **Legacy of Persia**​

Persia is the first region we’ve expanded that is situated outside of Europe, which was an interesting and very fun challenge! At the start of the project, we sought out anyone at Paradox who was well-versed in Iranian history (it turns out there were quite a few individuals!) and started formulating plans for what content we would focus on making. Our goal was to make the content grounded and historical, while still enabling powerful player fantasies such as reviving Zoroastrianism. We knew that we wanted a central core system to connect flavor to, which is how the Iranian Intermezzo struggle came to be. Unlike the Iberian struggle, we wanted this one to have a much wider spread of plausible alt-history paths to pursue, as the history of the region could have gone in many different ways - and this is something that we’re sure you’re experiencing when you play. You never know who will be a powerful actor, which faith will dominate, etc.  

While the historical ending is the Concession timed ending, we’re very pleased with the other ways in which you can conclude the struggle - from the community-favorite Iranian Resurgence where the Persian cultural identity and ideals dominate (be it as Zoroastrian or not!) to essentially breaking the very thought of Persian independence and empowering the Caliph to create another Dar-al-Islam with the Renewed Caliphate ending. The Intermezzo really sets the scene for how the rest of the game will play with large and sweeping effects on the region and beyond. This quicker style of struggle is something we’ve noticed that you in the community seem to like, so it’s something we’ll definitely keep in mind!  


#### ​

#### **General Improvements**​

As some of you may remember, we have an ambition to continually update and change parts of the game to make them better over time - and in 2023 we managed to do a lot. While we did an absolute ton of stuff, such as adding a nickname system, rebalancing domain limits, changing how building slots are gained, added vassal stances, etc, etc, etc - we also got to some of the general areas that we outlined in the floorplan, so let's take an extra look at those!  


#### ​

#### **Clans**​

In Legacy of Persia we got around to making Clans unique; previously they worked almost identically to how the Feudal government worked in CK2 - heavily opinion based, with angry vassals paying you nothing and happy ones giving you a lot. Now the economy of clans is heavily inspired by the Iqta system, with Tax Collectors assigned to Tax Jurisdictions, taxing them based on various Tax Decrees. Managing a Clan realm well gives you very clear advantages, and with the addition of House Unity you can also draw significant benefits from good old-fashioned nepotism!  

House Unity, fundamentally a part of Clans, brings a chaotic and character-driven element to the stability of clans. If your family is Harmonious you will enjoy a period of peace and stability, while an Antagonistic family is driven to expand and compete. This makes Clans ebb and flow in power, with the potential to rise quickly, and fall as quickly - simulating how many of the areas dominated by Clans in-game behaved historically.  

With these changes we feel like Clans are truly distinct from their Feudal counterparts, and playing them is an entirely different type of challenge. Feudal realms are generally more stable, while Clan realms have a much higher maximum potential.  


#### ​

#### **Modifier Stacking**​

With the building slot rework followed Men-at-Arms Stationing, which aimed to curb the mono-unit type armies that dominated previously because buildings gave global bonuses to MaA types. This caused battles to be completely trivialized as long as the player started optimizing their buildings even a little bit - and this is obviously not fun. You want to be able to defeat the AI by putting in time and effort, you don’t want them to just roll over. With these changes the AI can now also field incredibly powerful units, and they will also tend to buy significantly more MaA overall than they used to - especially if they are Warmongers.  

For next year we will aim to continually improve the game. In fact, we’ve set up a massive sheet internally where we detail areas of the game that are in need of balancing or reworking. Exactly what we’ll be tackling is still up in the air, but know that we still aim to continually improve the game!  


---

### **What’s happening in 2024?**​

And now for the perhaps extra interesting bit of the Dev Diary - what have we got cooking for 2024? Also quite a bit, it turns out!  

### **A New Experiment**​

At the beginning of next year, we’ve got another small experiment lined up. While I cannot go into detail about what it is, I can say that it *has something to do with the game directly* and that involves *something we’ve never done before.* We are very excited about it, and we hope you will be too - the idea for it actually came directly from the community itself, during a PDXCon where the Crusader Kings III team got to interact with some of you!  

You will be able to get your hands on this experiment very early next year, before the release of the new chapter! Speaking of:  

### **Chapter III**​

We will indeed be having another Chapter next year! Similar to this year the chapter will include four items, including one Major Expansion. One difference from Chapter II is that we have swapped out the Flavor Pack in favor of a larger type of expansion that we call a Core Expansion - I will clear up what this means in just a bit! Other than that, there will be an instant unlock to start Chapter III off, and an event pack to close the package.  

So what is the difference between a Major Expansion and a Core Expansion? The new Core Expansion format refers to the core gameplay loop: it focuses on adding, changing, or updating mechanics that are applicable for most rulers and/or high-impact systems that affect large parts of the game world, unlike Flavor Packs which are strictly regional in nature. Major Expansions are ‘wider’, and will either apply sweeping updates to the world, give you new ways of playing the game (such as new playstyles), or both!  

This means that Core Expansions are scoped in between Flavor Packs and Major Expansions. They are bigger and more impactful than Flavor Packs, but smaller with fewer sweeping changes than Major Expansions. Seeing how we want to shift towards more high-impact content that appeals to a majority of the community, we decided to up our pace and make a Core Expansion instead of a Flavor pack next year.  

That said, I want to emphasize how excited we are for next year, and though I *really* want to tell you what we’re working on I must limit myself to obscure hints and extremely non-telling images for now…  

#### **Instant Unlock**​

The instant unlock will be similar to Elegance of the Empire, the one we had for Chapter II. This time we’re also aiming to make clothes that embody the very essence of royalty. Inspired by the couture of the French, they will be gilded and lavish - and as with all assets we make - they are real, well-researched, and historical! Here’s a little peek of a crown:  

![image-01.png](https://forumcontent.paradoxplaza.com/public/1051644/image-01.png "image-01.png")


The gilded angel is a personal highlight.  

#### **Core Expansion**​

The Core Expansion will, among other features, introduce something that has been frequently requested by you in the community. Without saying too much, it will definitely make the game more challenging - and we’ve spent a lot of time making sure that it’s as dynamic and immersive as possible, while also presenting you with new ways to strategize. We’re also going to introduce a feature dripping with medieval flavor, a system that can be used by clever players to really make their mark on the world. All in all, this expansion will lean more towards the *systemic* side of the game.  

![image-02.gif](https://forumcontent.paradoxplaza.com/public/1051645/image-02.gif "image-02.gif")



#### **Major Expansion**​

As with the Core Expansion, the Major Expansion will focus on several things that have been requested by you in the community for *ages* - some of what we’re choosing to do has been asked for since the early days of Crusader Kings as a game series. One of the feature sets comes up very frequently when we see you discuss what you’d like to see in expansions - and another is brought up now-and-again as a powerful player fantasy. No matter what, we promise that this expansion will provide several new and fresh perspectives, and should please you regardless of which style of expansion you prefer, systemic or roleplay-focused. We can barely wait until you get your hands on this one, and personally, I can say that it’s one of the expansions I’ve been wanting to make since my early days working on CK2 - its time will soon come!  

![image-03.gif](https://forumcontent.paradoxplaza.com/public/1051646/image-03.gif "image-03.gif")



#### **Event Pack**​

As mentioned above, this time there will be no poll about the theme. Instead, we’ve been seeing an overwhelming amount of discussions about a certain well-liked feature for *months*. We’ve chosen to expand that feature with more things to do and experience, and this time we’ll be focusing on *highly visible* content!  

![image-04.gif](https://forumcontent.paradoxplaza.com/public/1051647/image-04.gif "image-04.gif")



---

That’s it for this year! We’ll be back in early 2024 with more updates, but until then we wish you all a fantastic winter holiday season, and a *God Jul*!

<!-- artifact:reactions:start -->
- 120 Like
- 81 Love
- 13 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 25 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
