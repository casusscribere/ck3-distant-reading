---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1546534/"
forum_thread_id: 1546534
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 109
title: "Dev Diary #109 - Floor Plan for the Future"
dd_date: 2022-10-04
author_handle: rageair
expansion: Friends and Foes
patch: Patch 1.8 (Robe)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3460
inline_image_count: 2
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1546534'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2080.jpg?1664879363
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_254_to_258
    action: preserved_and_flagged
    counts:
      Like: 263
      Love: 113
      (unlabeled — rendered as base64 data URI): 9
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_266_to_378
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_379_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2080.jpg?1664879363)
<!-- artifact:thread_banner:end -->

# Dev Diary #109 - Floor Plan for the Future

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Oct 4, 2022](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-109-floor-plan-for-the-future.1546534/)
<!-- artifact:thread_metadata:end -->

Greetings!  

A long time in the making, this diary is dedicated to plans, and what we have in store for CK3. From more present matters to musings and thoughts ranging into the far future. Crusader Kings is a unique game series, and one that has been close to my heart for a long time - the focus on characters as the driving force, emergent narratives, and player freedom make it truly stand out.  

Ever since I took the reins of the project I’ve continued to follow the original vision, which some of you might remember from the very first Dev Diary: *Character Focus, Player Freedom and Progression, Player Stories,* and *Approachability*. As you can see, the points correspond fairly well with my initial sentiment, and I do not intend to deviate too far from these points - that said there are always things we can do better or differently within them, and I think that we could do even more to, for example, improve the cohesion of player stories or the sense of progression. I am a firm believer in that everything in the game should help you in making stories (while not necessarily being *explicitly* connected).  

Internally we’ve always worked with the premise “Live the life of a Medieval Ruler”, which means that we want the game to be uniquely true to how life was during the period. We want to attribute more than just ‘death, suffering, and war’ to the era we portray. Highlighting things that you might not see elsewhere, such as family, or the challenges of rulership, is important to us. Going forward this will remain a priority, though it is important to note that we do exaggerate and romanticize a lot - it *is* a game after all!  


#### thinking_ani.gif


#### This all leads me to the next point; what are we doing?​

As a project, we aspire to have a cadence of roughly four releases per year, not including post-release support in the form of patches or hotfixes. During this year we’ve released Royal Court, Fate of Iberia, Friends & Foes, and as mentioned previously we’re aiming to have a free update out before the year is over. We want to have a steady stream of new content, while also maintaining the game by acting on feedback. For next year, our ambition is to have somewhere around four updates (barring unforeseen circumstances).  

Going even further (long-term) we have the ambition to shorten our cycles, so we can get more content and updates out. The project is (by Paradox Development Studio standards) still young, and has a long future ahead of it. There’s so much to do, and so many ideas still to explore. Though as I mentioned this is an ambition and not a promise - it might be complicated to get everything in place, but rest assured that we’re always evaluating what we can do to achieve this.  

Of course, we’re also watching initiatives that other studios are driving, such as the Stellaris Custodian Initiative, with interest. While we’re not organized in a way where we could adopt a similar structure today, it’s something that’s worth investigating - again, this is a *long-term* thing, and it’s very possible that we would find another setup that works better for Crusader Kings.  

For next year we want to do something similar to Royal Edition again, an Expansion Pass with a bundle of intriguing content. One drawback of the Royal Edition was the fact that the main beat, the Major Expansion, came later in the cycle. For the next one, we want to either start off the cycle with the Major Expansion, or make it obvious what the theme is going to be from the start. This should make it much clearer what you’re actually getting in the package as a whole. We’re also exploring what formats and formulas of expansions could make up a future Expansion Pass, as the ‘1 Expansion, 2 Flavor Pack’ formula is not set in stone.  

In addition to this, we also aim to do experiments now and then. For this year, the experiment was Friends & Foes; a smaller content format that was born out of the minds of the team. We’re looking into a few different experiments for the future, which I can unfortunately not share right now. Though something we can share is that we’re looking into more community involvement.  

#### But what are we doing? What’s the next Expansion about?​

As I’ve mentioned before, it’s too early to reveal the theme. However, the next Expansion is leaning towards the *roleplaying* side of the game. Without revealing too much we’re focusing in large parts on reinforcing the connection between *map and character*. The theme is not one that has been the subject of an expansion in previous iterations of CK - to make things extra clear; we’re not doing trade, imperial/byzantine mechanics, nomads, or similar *this time.*  

That said, I know that many of you are also hungry for more systemic expansions, and that’s understandable! Of course, the next Expansion isn’t devoid of systemic changes or mechanics just because it’s leaning heavily towards roleplaying. CK, like all GSGs, *requires* systemic content to remain true to what they are. There will be plenty of systems, both as part of the Expansion and the free update that comes along with it. For Flavor Packs we’re also going to aim to have systemic content as part of the formula - Fate of Iberia proved that a combination of flavor (events, clothes, illustrations, etc.) and a central systemic feature (the struggle) served to elevate the experience as a whole.  

As of now, we have a team of designers that is unlike anything we’ve had before - it’s not only a large team, but they’re also highly skilled and competent. This, in part, is why we’ve chosen to do an Expansion focusing on the roleplaying side of things, and it’s also the reason why we had the capacity to do the Friends & Foes experiment.  

My aspiration is to shift focus towards more systems-heavy expansions after the next one, and we’re gearing up the team to be able to do just that. I’m of the opinion that there must be balance, and as we’ll have had two roleplay-focused expansions in a row, by then it’ll be time for the scales to shift towards the systemic side. We’ve expanded our team of programmers significantly, so the future looks bright for those of you that crave new and exciting systemic content…  

#### Looking toward the future, what will we be doing over the coming years?​

Now, there are a lot of areas that I want to explore in the future! Please note that anything I write or list here is not in any way chronological, and they’re not explicit promises. Great ideas come along at any moment, from any direction, and we want to stay flexible with our plans.  

The current formats of Major Expansions, Flavor Packs, and Event Packs I believe let us cover every style of content we want to do, and we intend to keep these formats (while maybe tweaking the formulas a little bit here and there!).  

**Flavor Themes**  
Starting off with Flavor Packs; the regional focus is great and allows us to deep-dive into the history of a particular area - but as fun as it is to hit the books on a specific region, it’s possible that we’ll *also* be looking into non-regional Flavor Pack variants. Anything can be possible as long as there’s a central system where flavor can be woven in. That said, at least the next Flavor pack is likely to remain regional in nature.  

A long-term goal is to revitalize and create diverse and varied gameplay throughout the map. Something we want to do is to explore regions outside of Europe, as both of our Flavor Packs so far have been within the region. We want to show how much fascinating history and intriguing gameplay can be found around the world. Examples with a lot of surprisingly deep history include regions such as Tibet, Persia, the Caucasus, and North Africa, to name only a few.  

Of course, in due time we also want to explore regions within Europe that are very popular for players, some examples including Britain, France, and the West/East Slavic lands. It’s likely that we’ll alternate a bit, especially if someone on the team is extra passionate about a theme. Also one final thing; a lot of you are asking for a Byzantine Flavor Pack, but I know for a fact that the scope of a Flavor Pack wouldn’t sate your ravenous hunger for East Roman content… when we eventually get to them, it’d *more than likely* be as the part of a Major Expansion!  

As for non-regional, there are some ideas floating around; further exploring governments such as the Tribal Government, or building flavorful systems around for example Epidemics (which is a system that would, foundationally, be free if/when we make it), etc. A benefit that this format would have is that we’d be able to make systems that don’t fit the larger theme of a Major Expansion, but that we still feel would be great for the game.  

Just to reiterate; don’t take anything I say here as a statement that we’re doing one of these themes *right now!*  

**Ambitions for Expansions**  
There are already years worth of ideas for what we could do for Expansions. I’ll go through a handful of the areas I’d like to explore in the future, focusing on some of the topics commonly seen around the community. Note that these are not necessarily standalone Expansion themes, some might be combined, others divided. While there are some themes that I think are more important than others, **there’s really no saying what we’ll look at first or in what order.**  


![WIPdeck.png](https://forumcontent.paradoxplaza.com/public/873012/WIPdeck.png "WIPdeck.png")



**Trade & Merchant Republics** is something I hear a lot about - and it’s something that I really want to get to in time. However, I found the CK2 implementation in *The Republic* to be incredibly lackluster; in a game with thousands of interesting starts, it added only a handful more, and it didn’t actually have that much to do with trade. For CK3 my vision would be different - medieval rulers didn’t *trade*, per se, and noble rulers didn’t regularly barter resources with each other, so while that’s not a thing I’d want, there are a lot of interactions that could be added around trade and the *people who did the trading*. A system for CK3 would be character-driven, and there’s definitely an opportunity for new playstyles that aren’t as limited as the ones in CK2…  

**Imperial Mechanics**, especially in relation to the Byzantine Empire, is another common topic. Empires are generally not very exciting, essentially having the same mechanics as a king does. I believe that there’s an opportunity not only for *emperors*, but *to be part of an empire.* In many cases, such as in Byzantium, the Abbasids, or even the HRE, being a part of the empire should be as interesting as ruling it. There are many ways of going about this, but ideally, I’d want to get a lot of differences in there - no two empires were ever really the same, after all.  

**Laws** were another system that was lackluster at best in CK2. While they allowed a degree of customization and mechanical impact, the implementation was static and fairly uninspired. Conceptually laws were a huge part of being a ruler and being part of a realm, and while we do have vassal contracts (which I’d like to revise at some point, too) there’s room for more. For CK3, a law system would be deeply driven by characters, rather than confined to a static setup. Dynamism and evolution would be two keywords for the vision here.  

**Religion** in CK3 took a great step up from previous iterations, but there’s always more we can do. There are a plethora of ideas floating around, and as religion was such a common part of everyone’s lives by this point in history, it’s hardly surprising. It’s hard to nail down exactly what I’d like to do here as there’s just so much, but CK3 is uniquely suited to simulate all the drama that happened between everyone involved within the sphere of faith, be they Pope, Grandmaster, or simply an influential ruler. There’s also a lot of potential around crusades, and all the happenings before, during, and after them. I’d also really like to get faith to play a larger part in the everyday lives of rulers, as it’s much too easy to ignore as it stands.  

**Nomads** are just one part of the whole; the Steppe. This region is unique, and we’ve never done it real justice. In CK2 every ruler on the Steppe was a Genghis-in-the-making, with little focus beyond war. In reality, the Steppe was like an ocean - and the nomads were the only ones who had mastered it. I’d like to make the Steppe as a region stand out with mechanics of its own, and I’d like a large part of nomadic life to be about moving, focusing on the dynamism of the place and the people within.  

The **Late Game** is another area that I’m very interested in expanding, as the game currently plays very similar across the entire timeline. Sure, there are some differences, primarily in how easy it is to rule, and how much you’re able to claim in wars, but the differences could be more fundamental. This is one of those topics where there are a million things we could do, but an ambition I have is that the game should stay interesting for longer than is currently the average play session (around 200 years or so). Looking at Eras and their effects on the game is one venue, so is taking a look at holdings, economy, and other fundamental components of the game.  

I think it’s quite obvious that I eventually want to **Expand the Map**, to include the rest of the Old World. If we’d do it all at once or in segments is still up in the air, but regardless of what approach we take, it’s imperative that the area feels different to play in from the western half. While it’s obvious that the area would require a lot of unique art, I’d also want it to work differently from a mechanical standpoint - governments, faiths, etc. It’s an ambitious goal, but one I wish to tackle eventually.  

![Floorplan.png](https://forumcontent.paradoxplaza.com/public/873011/Floorplan.png "Floorplan.png")


*An incredibly rough floor plan for the future.*  

**General Areas**  
Of course, there are also areas of the game that I want to revisit, rework, rebalance, or expand in general - it’s not all about expansions or flavor, existing systems, and core loops must be revisited now and then to keep the game in a good state. Of course, this would be done in free updates, either free-standing or as part of a bigger release. Here are some of the things that I’d like to get to within a reasonable timeline, some more important than others. **This is not an exhaustive list.  

Alliances** are too binary as they stand, while it’s true that it’s easy to understand how they work, it also results in a lot of unwanted busywork when you have to fight in wars you’ve no interest in (or you have to take a big prestige hit…) - at the same time, it’s much too easy to get a lot of allies that, at a moments notice, are ready to drop everything in order to help in your wars. I’d like to see a pact-based system where you have to negotiate more, without making it annoying to find and get the alliances you need. You should, for example, never be fooled into a marriage hoping to get an offensive alliance, where it turns out you simply can’t. Exactly how/what we’d do is still in the works, but it’s high up on my list.  

**Clans** do not feel unique enough, while they have some mechanics that simulate the sphere’s tendency for spectacular rises & falls, there’s more we can do to show the differences from Feudal. I’d like to explore what made Clan realms so different historically and draw upon that for a more flavorful set of differing mechanics. I definitely also want to make the *Clan*, as in the group of people, matter more in the government bearing its namesake.  

**Warfare** is not and never will be a *primary* focus for CK3, that said it’s not as character-driven as it could be, outside of commander advantage and the occasional great knight. There’s also a real problem with delivering content (usually in the form of events) during times of war, as the player more often than not gets interrupted by something appearing in the middle of the screen while maneuvering units. I’d eventually like for us to be able to deliver content in a way that doesn’t interrupt warfare, and use that system to highlight characters and heroic acts (Battle of Agincourt, anyone?). I’d also like to rework the major annoyances of warfare, such as supply.  

**Modifier Stacking** is becoming an issue in some places, especially for Men-at-Arms modifiers (primarily from buildings) and Building Cost Reduction modifiers. While some issues can be solved by tweaking numbers (we’ve for example reduced prestige sources in the past) others require a redesign/revisit of the underlying problem. For example, I’d like to take a long, hard look at MaA modifiers, seeing as the player can very easily destroy AI armies with little work. I’d like to not only rebalance the sources of MaA boons but potentially also create new options for fun management.  

**AI** is an enigmatic beast, with aspects that are incredibly diverse. One of them is warfare AI, where Crusades stand out as an area in need of improvement - on one hand, historical crusades were incredibly disorganized, but on the other, we don’t want the player to feel like they’re hopeless endeavors. No matter what we decide to do, we’ll have to strike a balance - if the AI played perfectly optimally, crusades would steamroll everything, and I don’t want that. There are of course other aspects of the AI where I want to see improvements, such as the marriage AI, but we’ve at least made some good strides with the [economical AI](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-104-ai-ai-ai.1539411/)over the last few updates, so that’s not a priority. We eventually want personalities to shine through every aspect of the AI, and we have some plans for that, which will likely come in steps.  

**Community & History**  
As I touched upon earlier, we’d like to invite you in the community to take part in some of the things we’re doing in the not-too-distant future - my guess would be within Q1 of next year (though still TBD). Without spoiling too much it’d have something to do with the content we’ll be making…  

While not directly related to the game, an (at least if you ask me) incredibly cool initiative that we’ll be driving is to have more collaborations with historical media - this goes hand-in-hand with what I mentioned early on in this diary, regarding us wanting to show how medieval life actually was! This means that you’ll be seeing even more podcasts, videos, etc., about themes close to the game. Who knows, we might even get historians or professors to be guests or consult for our upcoming content.  

For those of you playing on console there will be a post later this week, answering some of the questions you have.  

That’s it for now! I invite you all to discuss what you see here - share your thoughts about the themes, ideas for what you’d like to see, suggestions on how things could be done, and so on!

<!-- artifact:reactions:start -->
- 263 Like
- 113 Love
- 47 (unlabeled — rendered as base64 data URI)
- 19 (unlabeled — rendered as base64 data URI)
- 9 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
