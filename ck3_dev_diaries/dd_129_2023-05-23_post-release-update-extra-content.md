---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1586430/"
forum_thread_id: 1586430
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 129
title: "Dev Diary #129 – Post Release Update Extra Content"
dd_date: 2023-05-23
author_handle: Portable Grump
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2582
inline_image_count: 17
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1586430'
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
  - type: thread_banner
    location: raw_line_139
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2373.jpg?1684842025
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_337_to_342
    action: preserved_and_flagged
    counts:
      Love: 151
      Like: 107
      (unlabeled — rendered as base64 data URI): 3
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_350_to_462
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_463_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2373.jpg?1684842025)
<!-- artifact:thread_banner:end -->

# Dev Diary #129 – Post Release Update Extra Content

<!-- artifact:thread_metadata:start -->
- Thread starter [Portable Grump](https://forum.paradoxplaza.com/forum/members/portable-grump.1503097/)
- Start date [May 23, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-129-post-release-update-extra-content.1586430/)
<!-- artifact:thread_metadata:end -->

This Dev Diary will talk about some of the extra content coming with our next post-release update, 1.9.1! The update will of course also include a ton of fixes and tweaks, as we’ve been monitoring all the ways you’ve been playing with the big 1.9.0 update and the Tours and Tournaments DLC.  


### Points of Interest​

Hi everyone! I am Daan, also known as Joror, and I am a programmer on the CK3 team.  


### It is I, le Joror​

First off a little background info about me so we’re no longer strangers: I have worked at Paradox for over five years, and in a couple of different roles. First in our online department (DevOps) as a software engineer and Developer Relations specialist, then as a Clausewitz Engine programmer and tech lead, and finally I have been working in the CK3 team as a programmer!  
Before joining Paradox I also dabbled in making mods and modding tools for Paradox games - which has helped me a lot in understanding how the games work from the outside, before moving to the inside.  
I am Dutch, like cats, fancy beers, the occasional Goth party, game-jamming, and in general games of all varieties!  


### Resurrecting Darlings​

Making games is hard - it is a space where ideas are easy, but time is short, and success is measured by a graspable but fickle thing called ‘fun’.  
So when developing, we design, build, evaluate, and cut. Many ideas fall by the wayside during each of those steps, including some personal darlings. Often not because the ideas are bad, but because there is not enough time, or they would be too risky, or… one of many other reasons.  

Luckily, we also bake various ways into our process that give us space for personal agency and creativity! And one such way is PDT - Personal Development Time.  
This is dedicated time in our busy schedule where every developer can work on improving their skills in an area of their choice. And (after checking with leads) we can also work towards adding ‘darling’ features or ‘pet peeve’ fixes that can make it into the game.  

The “Points of Interest” travel system is such a feature! It’s also the reason why it is in a post-release update. Of course, it is not just a one person effort. Lovely icons and GUI elements were added by a crafty Artist, code was reviewed by discerning Programmers, the user experience checked for consistency and purpose by a UX Designer, its rewards evaluated for balance by a Game Designer, the end product tested by perceptive QA, while being supported by a whole range of other disciplines that make the work environment organized and smooth.  


### A Travel Carrot: Points of Interest​

While working on Tours and Tournaments, one of the main systems I was involved in was the Travel system. For a little dev-insight, this is what route planning looked like early on in the process:  

![image14.png](https://forumcontent.paradoxplaza.com/public/974682/image14.png "image14.png")


*A screenshot of an early state of development of travel route planning, with different colors and icons.*  

We added Danger as one of the main ‘friction’ mechanics of travel, where players get to make planning decisions and have reasons to change their route. But Danger is mostly a ‘Stick’ - a punishment if you will - and it would be nice to have a ‘Carrot’ as well - a positive reason to change your route!  

**Enter:** Points of Interest - a small system that rewards you for visiting interesting places.  
These points of interest will give a reward the first time you visit them during your lifetime. The same also applies to your entourage, so bringing people along will also help them improve.  


![image15.png](https://forumcontent.paradoxplaza.com/public/974683/image15.png "image15.png")


*An adjusted travel plan which travels through Pisa, a province that contains a Point of Interest.*  


### Types and Rewards​


These Points of Interest are not static locations - but grabbed from the living world of CK3.  

All Special Buildings (if they are built) give a Point of Interest based on their type, and give different rewards depending on the Special Building type:  

![image9.png](https://forumcontent.paradoxplaza.com/public/974684/image9.png "image9.png")


*Visiting the Pyramids is something to boast about.*  

Special building type rewards:  

- Walls and Forts: +100 Martial Lifestyle Experience
- A part of a multi-province defensive structure (Hadrian’s Wall, etc): +25 Martial Lifestyle Experience
- Universities & Places of Learning: +100 Lifestyle Experience in your currently selected Lifestyle
- Religious Sites & Buildings: +100 Learning Lifestyle Experience, and +100 Piety if they are of your Faith
- Palaces and Political Buildings: +100 Diplomacy Lifestyle Experience
- Ancient Wonders & Natural Wonders: +100 Stewardship Lifestyle Experience, and +150 Prestige
- Economic Buildings (mines, ports): +100 Stewardship Lifestyle Experience

Visiting Capitals of independent Kingdoms and Empires also gives Lifestyle experience, based on their Court Type (if you have the Royal Court DLC) or Diplomacy Lifestyle experience when they do not have a Court Type. Empire Capitals are more rare, and give +300 lifestyle experience points, where Kingdom rank Capitals give +100 points. The capital Points of Interest are updated monthly, so sometimes your information might be slightly out of date.  

![image3.png](https://forumcontent.paradoxplaza.com/public/974685/image3.png "image3.png")


*The Byzantine Empire has an Intrigue Court - and will give Intrigue Lifestyle Experience when visited*  

Giving out these Lifestyle rewards is very narratively fitting for expanding the horizons of your character, but also substitutes nicely for the normal Lifestyle events you are not getting while traveling.  

Some locations can also trigger a “Great City” sight-seeing event chain, which is actually hooking in a PDT project of another CK3 developer, TrinTragula!  

![image10.png](https://forumcontent.paradoxplaza.com/public/974686/image10.png "image10.png")



When you visit, you get a message and the Point of Interest is marked as visited. To seek similar rewards, you will have to visit different places in the future!  

![image12.png](https://forumcontent.paradoxplaza.com/public/974687/image12.png "image12.png")


*A point of interest has been visited, and the rewards given.*  

Once you have picked up the Traveler Trait, you also start getting a bit of experience towards the different tracks within that Trait. (Martial and Economic building Points of Interest give Seasoned track experience, where the rest give Wanderer track experience.)  

![image16.png](https://forumcontent.paradoxplaza.com/public/974688/image16.png "image16.png")


*Getting ‘Seasoned’ travel track experience.*  

To conclude, here is a snapshot of the Points of Interest that exist in 1066:  


![image11.png](https://forumcontent.paradoxplaza.com/public/974689/image11.png "image11.png")


*A zoomed out map showing Points of Interest in 1066*  

To note, this system is part of the Free Update - so no specific DLC required.  
**Happy sight-seeing in Update 1.9.1.0~!**  


---


### What’s the Harm?​

Welcome comrades, to the Wokeg section of the DD! I’m afraid I don’t have anything quite as meaty for you as Joror. Instead of lovely new player carrots, we’ll be talking about the oldest and wackiest of all sticks with which to whack the player: *death*.  

Something we’ve generally been a bit reluctant to do in CK3 is to just kill you. Luck plays a decent roll in the events you get and guiding your own luck is an element of many core mechanics, but we’ve been really reticent to have you just… die unexpectedly.  

This was a stylistic design choice. It doesn’t really feel great when a random event pops and just kills you mid-run with no set-up or warning — it can be impactful every now and then, especially if it happens at a narratively dramatic time, but it’s just such a quit moment for so many people, and in wanting to provide an experience that felt fair, we over-corrected somewhat and scrubbed a vital element of friction from much of the title.  

Whether you’re building your realm, planning marriage alliances, or carefully organizing your succession, these little shake-ups are needed to keep you course-correcting. They’re the firm, unexpected kick to the back of the knee that keeps you guessing and makes you react on the fly.  

Not just that, of course, because random death and dismemberment were absolutely staple features of the medieval world too: you might be struck down by a virulent camp disease whilst marching, you might fall from the window of a tall tower, you might die in a house fire, you might be thrown from your horse whilst riding, you might be playing too roughly with another child, you might be old and just fall down the stairs, the list goes on. Paupers, kings, and clergy alike all have to walk the danse macabre eventually, and not everyone gets to go from the traditional big three of honorable combat, succumbing to wasting disease, or expiring from the ravages of age. Sometimes you just die.  

The challenge we set ourselves, then, was adding in more ways for death to happen unpredictably *without* making for an irritatingly frustrating experience. Enter, the harm event.  

![image13.png](https://forumcontent.paradoxplaza.com/public/974691/image13.png "image13.png")



Harm events are out to do one of two things: if you’re unlucky, they want to kill you, and if you’re lucky, they want to render you incapable. There generally isn’t a direct gameplay benefit to surviving them, and there’s always a stress cost. Their odds are generally pretty harshly against you, though depending on the event, high skill levels might give you a much better chance of success, and some traits will let you trade stress for negating a specific harm event entirely.  

With these, there’s a whole variety of new ways to unexpectedly expire or be reduced to a bed-ridden shell! Fun stuff, y’love to see it. I did also say, though, that we were trying to avoid frustrating rocks-fall-PC-dies situations, and that’s still true. To avoid that, almost all harm events are partnered with a foreboding event — something that fires first and alerts you that hey, you are now eligible to… [spins tombola] … unexpectedly choke to death!  

Rather than spring immediate death/incapability on you out of the blue, we alert you that you are now at risk of it. It can now just happen, at any time. In fact, just *getting* a foreboding event gives you a 50% chance of getting the follow-up harm event within the next 4-8 years, though you’re also eligible to fire it forever after.  

For example, here’s a foreboding event:  

![image17.png](https://forumcontent.paradoxplaza.com/public/974694/image17.png "image17.png")



And its follow-up harm event:  

![image6.png](https://forumcontent.paradoxplaza.com/public/974695/image6.png "image6.png")



The goal is to warn you that a new type of random harm is on the table, so that the notion is playing around at the back of your mind. Maybe it’ll come to nothing, maybe you’ll forget about it, maybe you’ve got just a few short years left to live. Do you want to make rapid preparations for succession? What if it never happens at all? What if you just pushed to do things a little bit faster so the realm’ll be ready for your heir? What if it happens sooner than expected? Lots of little questions to ask yourself. Or, if you’re one of the coworkers testing or playing on internal builds since we added these, lots of questions to menacingly direct to me when I’m making tea, demanding to know when they can stop being worried about impending doom. WAD, I whisper back to them, WAD.  

There’s sixteen new harm-foreboding pairs for becoming incapable (well, fifteen pairs and one triplet: becoming incapable due to the march of time vs. your declining health sees your mind weaken, your body start to fade a little, then you risk becoming incapable), twelve new harm-foreboding pairs for dying unexpectedly, and six new events for dying/becoming incapable whilst on campaign.  

![image5.png](https://forumcontent.paradoxplaza.com/public/974696/image5.png "image5.png")



![image8.png](https://forumcontent.paradoxplaza.com/public/974697/image8.png "image8.png")



Those last six aren’t paired with a foreboding event. Like I said, almost all harm events are, and the exceptions to this are the ones that fire for army commanders. Warfare could kill you quickly and unexpectedly without you ever donning your armor, and history is replete with examples of even fairly hale and hearty warriors succumbing to sudden unexpected disease, poor luck, or taxing environmental conditions, from John Lackland to Richard the Lionheart to Frederick Barbarossa.  

Instead, opting to put yourself in charge of an army is your warning that you’re in a dangerous, taxing position, where poor luck might cost you dearly at any moment. High health will protect you from many of the potential ravages of campaigning (with the amount needed going up more the more you age), but the best way to stave off the risk of death outside of battle is to campaign in terrain you have the correct commander trait for.  

![image2.png](https://forumcontent.paradoxplaza.com/public/974698/image2.png "image2.png")



![image1.png](https://forumcontent.paradoxplaza.com/public/974699/image1.png "image1.png")



Maybe you’re not too big a fan of this change - perhaps you prefer a more predictable world, or you want to have the occasional sudden death but mostly skate on by just fine. For you, we have the Safe & Illusion of Safety settings for the new Random Harm game rule, so you don’t have to deal with this stuff if you don’t want to.  

Maybe, though, you’ve been waiting for something like this. Maybe you want more uncertainty in the world, or for life to be just that little bit more mean-spirited than most. For you, we’ve got the Tragic setting, making harm events much more likely generally. If you’d prefer that the tallest blade of grass be the first under the scythe, then we’ve also got the Spiteful setting, which specifically weights up the likelihood for harm events to target proportionally better or more interesting characters. And if you want both, welp, Tragically Spiteful, the single edgiest game rule we’ve added to date, has got you covered.  

As long as you’ve got harm events set to anything but Safe, they do run on a cooldown. Players can’t be subject to a harm event more than once every fifty years, and the AI not more than once every thirty per house. These cooldowns help to reduce frustration whilst keeping the threat present, and mean that even playing on Tragically Spiteful, you can still thrive and survive. Just, with the occasional setback.  

![image4.png](https://forumcontent.paradoxplaza.com/public/974701/image4.png "image4.png")



![image7.png](https://forumcontent.paradoxplaza.com/public/974702/image7.png "image7.png")



… and that’s it from me! Hope you like the harm events, I tried to cover a variety of types from historic references and common causes of death or severe injury either still present in the modern day or mitigated only in the last few centuries, and I’m very happy to be able to resurrect this particular darling for 1.9.1. Have fun with the update!

<!-- artifact:reactions:start -->
- 151 Love
- 107 Like
- 10 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Portable Grump](https://forum.paradoxplaza.com/forum/members/portable-grump.1503097/)**
Role: ♛ CK3 Community Team ♛
Badges: 18
Messages: 276
Reaction score: 1,620

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
