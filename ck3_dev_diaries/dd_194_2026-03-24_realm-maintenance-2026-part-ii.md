---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1911816/"
forum_thread_id: 1911816
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 194
title: "Dev Diary 194: Realm Maintenance 2026 (Part II)"
dd_date: 2026-03-24
author_handle: Arakrates
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3851
inline_image_count: 41
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1911816'
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
    location: raw_lines_~28_to_140
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_523_to_527
    action: preserved_and_flagged
    counts:
      Like: 108
      Love: 63
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_535_to_636
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_637_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary 194: Realm Maintenance 2026 (Part II)

<!-- artifact:thread_metadata:start -->
- Thread starter [Arakrates](https://forum.paradoxplaza.com/forum/members/arakrates.1605676/)
- Start date [Mar 24, 2026](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-194-realm-maintenance-2026-part-ii.1911816/)
<!-- artifact:thread_metadata:end -->

Hi everyone! Welcome to the second part of the Realm Maintenance Dev-Diary. Last week, we unveiled a whole host of features that we’ve been working on together [@Agamidae](https://forum.paradoxplaza.com/forum/members/1226207/). We are super excited to see your positive reaction to all of the things we’ve unveiled so far, and can’t wait for you to get your hands on it soon.  

We deeply believe that our community is our lifeblood, that is why we are constantly trying to find ways of giving back to the community and lift up talented creators through our different programs such as the Creator Packs or this update. Working with Agami has been super fun, and we are hopeful about continuing doing things like this in the future.  
*After all, we still have a ton of other stuff he wanted to work on that were at least equally as exciting as the things we showed off last week, so I think we almost have to at this point! ![:D](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Big Grin    :D")*  

On top of the more than 1,500 individual bug-fixes, tweaks, and changes we’ve done to the game with this update, we want to also highlight a couple of more projects we’ve been working on to improve existing features in different ways.  

Also, before we start, we won’t be talking more about the Accolade rework, since we believe we went into enough detail in a previous dev diary. If you’re interested to read more about it, please [check it out here!](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-192-spring-cleaning.1902372/) We have however been incorporating some of your feedback that we’ve received since revealing the rework, so thank you for that!  
Alright, to kick it off, I want to introduce [@PDX-Windy](https://forum.paradoxplaza.com/forum/members/1516457/), one of our producers on CK3, who will be showcasing one of his babies that he has been working hard on, and I believe you will all greatly appreciate it.  

---


Story Tracker  

Hello everyone, I am Windy and I’ve been producing Crusader Kings 3 for five years now. Thanks to Black Forge Jam I have an opportunity to actually contribute to the game beyond my capacity as a producer, and whatever random script things I do every now and then (to anyone who enjoys the fishing decision for adventurers in Roads to Power, that was me!).  

This year, for the game jam, I wanted to show how cool story cycle content actually is. We have quite a lot of story cycles in the game actually, some of them just drive AI behavior but a lot of it is fun gameplay. The studio agreed, it is something I think everyone has wanted at one point, it’s a shame they are so hidden away. To achieve this I got a star-studded team to help me develop the “Story Tracker”.  

I was joined by our Game Director [@rageair](https://forum.paradoxplaza.com/forum/members/375731/), 2 (TWO!) whole coders, a game designer, a lot of help from the UI artists, and even our studio manager helped out!  

Planning  

First thing is first, how do you go from nothing to something? Well, here my experience as a producer came in handy hehe…  
First up, what do we even want to show? What questions do we need to answer? What questions do WE have as CK3 players?? After an initial brainstorming session I set out to make some mockups and prototypes on paper and by kitbashing our UIs together to show *something*.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1473765/image_01.png "image_01.png")


*[Version 0.1 of the story tracker]*  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1473766/image_02.png "image_02.png")


*[Version 0.2 of the story tracker]*  

It ended up being very bad and very ugly, but it was a first step towards *something*. Now we could actually start quantifying what is useful, what is not, how we should display different things… All story cycles are very different, they have different things to keep track of, different characters, etc. etc.  

What even is there to keep track of? Well, to know that we need to list all our story cycles, and what suits us better than a nice spreadsheet…  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1473767/image_03.png "image_03.png")


*[Spreadsheet going through every story cycle in the game, what they do, how we should visualize it, whether it's something we want to visualize, and if we’ve implemented it.]*  

Now that we had an idea of what we needed to show, we ended up with a modular system (thanks [@rageair](https://forum.paradoxplaza.com/forum/members/375731/)!) and UI elements to be able to build on all these different game mechanics found in the story cycles.  


Implementation  
The very talented code team set to work to expose these things in the UI, and from Game Design’s side it was time to implement a maximum version of a story cycle for debugging. One that would make full use of all the planned elements so that we could layout it properly and see what we needed to do in order to display all the information we wanted to show in a neat and structured way.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1473768/image_04.png "image_04.png")


*[The very first version of the story tracker in game!! v0.3]*  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1473769/image_05.png "image_05.png")


*[Final paper mockup v0.4, now the interface design is in place!]*  

For each story cycle I designed mockups with elements that are needed for implementation  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1473770/image_06.png "image_06.png")


*[Did you know having a dog or cat or horse or rock is a story cycle? Of course it's the one we modelled first]*  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1473771/image_07.png "image_07.png")


*[Here’s the full board with all the designs (and the pain of implementing it all)]*  

For each element, code wrote GUI script that I could play around with, moving elements around, making sure everything is aligned, using the same amount of vertical and horizontal space…  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1473772/image_08.png "image_08.png")


*[Adding elements to the pet dog story…]*  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1473773/image_09.png "image_09.png")


*[Having stories be considered “personal situations” helped a lot with visibility, initially they were meant to go in the decisions panel (can you believe it!)]*  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1473774/image_10.png "image_10.png")


*[Personal story for the Song of El-Cid (and his Bel-Air cat, apparently)]*  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1473775/image_11.png "image_11.png")


*[New UI element for titles, so you can keep track of that damn white [strike]whale[/strike] stag]*  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1473776/image_12.png "image_12.png")


*[Iteration makes things better]*  

We had Monday to Friday to complete this, and with good prep work and laying the foundation early we managed to have the feature complete by Wednesday, allowing us to bugfix and polish until the end of the week. Highly recommended!!  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1473777/image_13.png "image_13.png")


*[Some of the stories visible in the game…]*  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1473778/image_14.png "image_14.png")


*[Rare pet stories!]*  

Anyway that’s the long and short of it – it looks like we have a lot of new content but actually we are just showing off what we’ve made throughout the years.  

Now we can make new, cooler stories that use this interface to its full potential! Stay tuned for those!  

---

Super cool stuff, indeed we can’t wait to see how we can further use this new interface to deliver you all great and exciting content!  

Even our Game Director, Oltner, has been working on a pet project for this update. Up next, he will tell you a bit more about what happens when you grow old, both in real life and now the game!  

---

Elder Traits  

There are two problems with growing old in CK3 that I’ve wanted to change for a long time; there are very few complications of aging, and the ones that exist are immediately debilitating. For example, one day your character is a spry, capable warrior - and the next day, they’re infirm and basically good for nothing but waiting for death to claim them. Also, that’s basically the only consequence - infirmity - which represents both the deterioration of mind and body at once. Not very fun, and feels unfair from a challenge perspective.  

Since some time, we’ve had the tool to make this situation into something better - tiered traits. There’s now a selection of elderly traits, all medievally-flavored versions of real-life afflictions, that start out very mild but grow in severity over time. This includes the previously mentioned Infirm trait, which is now also tiered. Worth noting is that I didn’t want a repeat of the ‘Harm Events’ feature (which threw random events at the player which they couldn’t do anything about), so a crucial element of Elder Traits is offering methods for players to mitigate both: 1. Getting the traits in the first place, and 2. How fast they progress.  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1473779/image_15.png "image_15.png")



Your lifestyle has a large impact on whether you get Elder Traits - but there’s also a genetic component, and a certain degree of luck involved. Generally doing what you most often already do, like keeping your character healthy and free of stress, will reduce the chances of getting the traits. Note that the game concept will not list all factors, only the most major ones. Some of the more ‘niche’ playstyles and lifestyles are more socially-oriented, and thus counter mind-related afflictions: so now you have new reasons to pursue the diplomat/seducer trees!  

Let's take a look at the traits and their mitigations!  


Faltering Heart  
The most stress-linked Elder Trait is Faltering Heart, which progresses in severity the more stress breaks your character suffers. The trait itself increases stress gain and reduces stress loss, but for a careful player this is the easiest trait to avoid worsening. If you reach its rank 4, you will die.  

![image_16.png](https://forumcontent.paradoxplaza.com/public/1473780/image_16.png "image_16.png")


*[As this trait progresses with every mental break, its mitigation is simply to avoid stress.]*  


Fragile Bones  
Fragile Bones is unique in that it doesn’t convey any direct health penalties - it just makes everything surrounding health worse for your character. The trait lowers your life expectancy (which means aging will cause you to lose health slightly faster than usual), makes your frail mortal form easier to murder, and makes any wounds you suffer worse. Yes, that’s right! Whenever you would become Wounded, your Fragile Bones trait will instead cause you to become Severely Injured, or Brutally Mauled if the trait rank is high.  

![image_17.png](https://forumcontent.paradoxplaza.com/public/1473781/image_17.png "image_17.png")



Fragile Bones slowly increase its rank over time, but this is very slow unless you’re traveling or commanding armies.  

![image_18.png](https://forumcontent.paradoxplaza.com/public/1473782/image_18.png "image_18.png")



If you have Fragile Bones or Withering Heart with an advanced trait rank, your character will show a new animation in the character window:  

![image_19.png](https://forumcontent.paradoxplaza.com/public/1473783/image_19.png "image_19.png")



![image_20.gif](https://forumcontent.paradoxplaza.com/public/1473784/image_20.gif "image_20.gif")




Clouded Eyes  
The mildest Elder Trait is Clouded Eyes, which disperses the penalties of the Blind trait over several levels, with the final one replacing the trait with Blind outright.  

![image_21.png](https://forumcontent.paradoxplaza.com/public/1473785/image_21.png "image_21.png")



This trait progresses very randomly, with a vast majority of characters only ending up around level 1-2. It can be mitigated by avoiding areas with a lot of sun and glare.  

![image_22.png](https://forumcontent.paradoxplaza.com/public/1473786/image_22.png "image_22.png")



As an added detail, characters with this trait will actually have clouded eyes visible on their portrait.  

![image_23.png](https://forumcontent.paradoxplaza.com/public/1473787/image_23.png "image_23.png")




Withering Mind  
While Withering Mind does not give any penalties to health, it will - if left unchecked - decimate your skills. This is by far the most debilitating of the Elder Traits, yet also the one with the most possible mitigations. Keep yourself as healthy as you can by surrounding yourself with friends, lovers, wards, etc. Think twice before stacking all your typical health modifiers; sometimes it's better to die than to spend your life in purgatory.  

![image_24.png](https://forumcontent.paradoxplaza.com/public/1473790/image_24.png "image_24.png")



This trait is the reason we’ve added multiplicative skill modifiers in this Update - for each advancement on the track, you’ll lose 25% of your skills. No matter how high those skills are. You can have a learning skill of 5 or 50 - you’ll slowly slide down the slope of oblivion regardless…  

![image_25.png](https://forumcontent.paradoxplaza.com/public/1473791/image_25.png "image_25.png")



Some of the mitigations for Withering Mind are things that actually worsen the state of other Elder Traits. For instance, traveling is bad for those with Fragile Bones, but good for those with Withering Mind.  

![image_26.png](https://forumcontent.paradoxplaza.com/public/1473792/image_26.png "image_26.png")



Characters with a sufficiently high level of Withering Mind will have the ‘Delirium’ animation in the character view.  

![image_27.png](https://forumcontent.paradoxplaza.com/public/1473793/image_27.png "image_27.png")




Infirm  
The Infirm trait is now tiered, just like the other traits, and no longer reduces intrigue or learning - it now represents a general physical degradation of the body. As this trait is still one of the most impactful traits in the Elder Trait category, it’s now much more rare. It’s extremely unlikely that you’ll get infirm without already having gained one or more of the other Elder Traits first.  

![image_28.png](https://forumcontent.paradoxplaza.com/public/1473794/image_28.png "image_28.png")



Infirmity increases by a full level every time you contract an illness of any severity. Stay healthy, and stay far away from any epidemics.  

![image_29.png](https://forumcontent.paradoxplaza.com/public/1473795/image_29.png "image_29.png")




Content  
We’ve made some content to make the traits feel present, such as events while traveling, etc. This includes not only events which highlight the Elder Traits you’ve gained, but also events exhibiting the impact of your close family or loved ones having these nasty traits.  

Examples:  

![image_30.png](https://forumcontent.paradoxplaza.com/public/1473796/image_30.png "image_30.png")


![image_32.png](https://forumcontent.paradoxplaza.com/public/1473798/image_32.png "image_32.png")

![image_31.png](https://forumcontent.paradoxplaza.com/public/1473797/image_31.png "image_31.png")



Surround yourself with the right people to avoid the worst consequences.  

![image_33.png](https://forumcontent.paradoxplaza.com/public/1473799/image_33.png "image_33.png")


![image_34.png](https://forumcontent.paradoxplaza.com/public/1473800/image_34.png "image_34.png")


![image_35.png](https://forumcontent.paradoxplaza.com/public/1473801/image_35.png "image_35.png")



Some traits, like athletic, make little sense the more infirm you get.  

![image_36.png](https://forumcontent.paradoxplaza.com/public/1473803/image_36.png "image_36.png")




Game Rule  
If you prefer the ‘old’ way of representing Elder Traits with only the Infirm trait, we have added a game rule where you can customize that to your preference. The only option that disables Achievements is the one disabling aging consequences altogether.  

![image_37.png](https://forumcontent.paradoxplaza.com/public/1473804/image_37.png "image_37.png")




---

Now up next is Nomads and the work that has gone into rebalancing them. I will let Jason explain that in more detail. He’s really enthusiastic about this so please entertain him.  

---

Nomadic Adjustments: The Quest for Herders  

ALL LANDS UNDER THE SUN BELONG TO THE GREAT KHAN.  

With this truth established between us, I will tell you of the nomad adjustments that have set up camp in this fine update. The chief steppe issue we addressed was Herders. Specifically, the lack of them. After game start, Herders tend to mostly disappear from the world. This leaves the steppe barren of Fertility, and Nomads with few good targets for migration. It’s a recipe for stagnation.  

![image_38.png](https://forumcontent.paradoxplaza.com/public/1473805/image_38.png "image_38.png")


*[The pre-patch state of Herders. Not much to be seen here.]*  

So what measures did we take to welcome Herders back into the world?  

**First — a “culling” effect of very weak AI nomads.**  
If an AI nomad has no Herd, but a single barre n pasture or two, and no fame to their name… they are made a pathetic (but Fertility-generating) Herder. And they deserve it.  

**Secondly — Humiliation Casus Belli Realm-Breakup**  
The Humiliation Casus Belli will now not only demote nomads in Dominance level, but will break off their non-capital border counties as independent herders.  

**Thirdly — Tweaking of the Overrun Kingdom Casus Belli.**  
Because this CB moves nomads out of the steppe and leaves Herders in their wake, it being used *more* by king-tier khans (specifically, those who have little or no reason to believe they may become Gurkhan) creates fertile openings in the steppe, and contribute to the region being more dynamic.  

So the AI will indeed use the Overrun Casus Belli more often, *but* only against much more appropriate-feeling targets: either their neighbors or regions historically moved into by nomads (Persia, the Middle East, Asia Minor, Eastern Europe, Northeast Asia). Indeed, issues with the related targeting script have been fixed, and there should be no more random Cuman Frances appearing.  
Oh, also, the culture/faith replacement effect that happens when the victorious nomads move into their conquests is now somewhat more limited and less capable of making local cultures/faiths disappear.  

![image_39.png](https://forumcontent.paradoxplaza.com/public/1473806/image_39.png "image_39.png")


*[A nice, big blob of post-Overrun war herders!]*  


A New Overrun Duchy Casus Belli  
We cooked up a smaller version of the CB discussed above. This one is available to duke-tier nomads and targets only a duchy. It does *not* swap the local culture and faith with the invader’s culture and faith. Thus, it has a less disruptive impact on the game world, and can be used more frequently as part of the regular permeability between the world of the steppe and the soft settled peoples.  

As with the Overrun Kingdom Casus Belli , a nomad invader achieving victory with Overrun Duchy moves into the non-nomadic lands they targeted and assumes non-nomadic government. Their old territory goes to herders.  

In addition, this Casus Belli, unlike the Kingdom-level one, is potentially available to Confederation members. By using this CB successfully, they leave the ranks of their Confederation. So this is another vector for steppe dynamism: a decrease in the long-term stability of nomadic confederations.  

![image_40.png](https://forumcontent.paradoxplaza.com/public/1473807/image_40.png "image_40.png")



**So… Herders?**  
After testing, I’m happy to say that there are not only GREAT MIGHTY KHANS on the steppe after game start - there are herders too! The cycle of steppe life (and steppe-victim life) seems rather more vivaciously unpredictable. Praise Chinggis Khan.  

---

Thank you Jason!  

We hope that this and last week's showcase has left you excited for this update. Like I mentioned in the beginning, we have a whole slew of fixes on top of the work here that has been done.  

I want to raise a special thanks to everyone who participated in the Community Fix Day Event we launched a few weeks ago. In our eyes, it was a massive success and we were super happy about the participation we got from you, the community. We will be evaluating the event, and look into how we could incorporate this into perhaps a more regular format.  

For those interested in the changelog of all the things that were fixed, I am happy to announce that we will be revealing the preliminary changelog very soon as we go into Open Beta.  

Lastly, before ending this development Diary, there are two more additions I want to show off.  

We’ve had fantastic work from one of our programmers to finally separate each accessory type so that it has its own set of 16(!) color channels that you can modify for your character. What does this mean in plain language?  

It means that in the future, you will be able to finally color the clothes of your character ***without*** accidentally painting your horse.  

![image_41.png](https://forumcontent.paradoxplaza.com/public/1473808/image_41.png "image_41.png")



Now, I want to be clear that this has not yet gone through QA. While we are hopeful that it will make it into this update, we also want to be careful not to introduce any new issues, so please make sure to thoroughly try out this feature during the Open Beta.  

We’ve also done a pretty significant change to the domain limit so it is not as easily obtained by Stewardship anymore. [@Snow Crystal](https://forum.paradoxplaza.com/forum/members/1280952/) has been working on overhauling the system, so you now no longer get domain limit from stewardship. A small thanks to [@MummyMonk](https://forum.paradoxplaza.com/forum/members/1861895/) for the idea in the first place.  

In addition, we moved some of these lost domain limit bonuses into education traits instead, so you now get domain limit based on education trait:  


- Tier 1 → -1
- Tier 2 → 0
- Tier 3 → 1
- Tier 4 → 2
- Tier 5 → 3

We also reduced the amount of domain limit from the Architect tree to 1, and put it into one tree of each type:  


- Patriarch tree (trait)
- Theologian tree (trait)
- Torturer tree (fear tax)
- Overseer (absolute control)

We want to ensure that this update lives up to both our quality standards and your expectations. While we cannot share a release date just yet, we can say that you will not have to wait much longer, as we hope to share more updates soon.  

---

For those interested in joining the Open Beta and helping us ensure the release is the best it can be, please keep an eye out for more information very soon. We are planning to launch the branch on March 30th, assuming everything goes according to plan.  

We are extremely grateful for all your support during this time, and I hope you are just as excited as we are to play this update. The next time I make a post, it will be the final changelog and a go through of the mod support we’ve managed to get in as well for this update. Please look forward to it!  

Thank you, and see you soon!

<!-- artifact:reactions:start -->
- 108 Like
- 63 Love
- 5 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Arakrates](https://forum.paradoxplaza.com/forum/members/arakrates.1605676/)**
Role: Design Manager
Badges: 41
Messages: 167
Reaction score: 1,427

*[Full game-badge icon list of 41 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
