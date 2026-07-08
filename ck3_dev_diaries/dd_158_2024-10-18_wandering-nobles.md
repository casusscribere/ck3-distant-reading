---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1710648/"
forum_thread_id: 1710648
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 158
title: "Dev Diary #158 - Wandering Nobles"
dd_date: 2024-10-18
author_handle: Snow Crystal
expansion: Wandering Nobles
patch: Patch 1.14
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1154
inline_image_count: 10
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1710648'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3339.jpg?1729248316
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_235_to_239
    action: preserved_and_flagged
    counts:
      Like: 88
      Love: 33
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_247_to_357
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_358_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3339.jpg?1729248316)
<!-- artifact:thread_banner:end -->

# Dev Diary #158 - Wandering Nobles

<!-- artifact:thread_metadata:start -->
- Thread starter [Snow Crystal](https://forum.paradoxplaza.com/forum/members/snow-crystal.1280952/)
- Start date [Oct 18, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-158-wandering-nobles.1710648/)
<!-- artifact:thread_metadata:end -->

Hello there!  

It’s been a while since I wrote one of these, so I figured I could give a short presentation of myself. I’m [@Snow Crystal](https://forum.paradoxplaza.com/forum/members/1280952/) , one of the two Design Leads on CK3, and I have been around at Paradox on different projects since CK2’s Holy Fury (my first DLC). It’s my pleasure to present our last entry in Chapter 3, namely, the Wandering Nobles DLC.  

## Vision​

As we set out to create this piece of content, our primary goal was to see if we could spend more time with the traveling system from Tours & Tournament. It was a system that was generally well-liked internally and externally, and we knew we would most likely be used a fair bit by adventurers (though exactly how that game loop would turn out was unclear at the time). We wanted to continue experimenting with it and see if we could add more content to it in different ways.  

Since I have seen some confusion about this, one thing to clarify is that the Wandering Nobles is not a Landless Adventurer DLC. It was made primarily for landed gameplay, and though much of it is also available to landless characters, they are not the pack's focus. In other words, this DLC will not have unique landless features, new contracts, or anything locked to the adventurer playstyle.  

Even though I will not go into detail about events, a plethora of new events are spread throughout the different features that will be detailed here, as well as a slew of new travel events. In this event pack, we tied them all into things the player will choose to engage with, see activities, lifestyle, and travel, rather than having them appear seemingly at random.  

## Lifestyle​


Besides the traveling focus, what you can find in the pack is our first new lifestyle since the game's release. This avenue of content has remained almost untouched since the game was first released, except for adventurer-specific perks in Roads to Power, which we wanted to try and experiment with. It is set up like all other lifestyles in the game, with 27 perks split across 3 lifestyle trees, 3 focuses, 3 traits, and landless perk variants where needed.  

One essential philosophy of the new lifestyle tree is that we wanted it to be a tree where you had to engage with it rather than having it simply engage with you. In other words, there are fewer passive bonuses, and most bonuses are gained by engaging in travel or activities. In that sense, we tried to go for impactful effects and bonuses from the perks, but at an opportunity and gold cost. We will talk at length about the lifestyle trees and perks next week, but I wanted to give you a small look at what it looks like.  

![image 01.png](https://forumcontent.paradoxplaza.com/public/1195085/image 01.png "image 01.png")


![image 02.png](https://forumcontent.paradoxplaza.com/public/1195086/image 02.png "image 02.png")



## Activities​

In the DLC, we have included three activities, each associated with (and unlocked by) one of the new lifestyle trees. They are intended to be about the size of the University Visit we introduced in Wards & Wardens, giving landed rulers more opportunities to travel through your realm or abroad. Two of the new activities are set in your realm, whereas one takes you outside your borders.  

When we created these new activities, one of our philosophies was that we wanted them to be deeply tied to each of the lifestyle trees, synergizing in different ways and playing into the strengths of the lifestyle tree. That way, investing in the lifestyle tree opens up an activity that lets you continue to build down that route.  

The first activity we will examine is Inspection, where you can choose to travel to a specific part of your realm to ensure that it is well-run. You will be able to decide what parts of realm management you would like to focus on, and if you travel to a border county, you might even get vassalization acceptance from neighboring rulers or claims on their lands.  

![image 03.png](https://forumcontent.paradoxplaza.com/public/1195087/image 03.png "image 03.png")



Our second activity, the Monument Expedition, involves traveling to a distant city to see its sights. This allows you to visit specific places with Points of Interest, which you’d previously have to drop by as you pilgrimage elsewhere.  

![image 04.png](https://forumcontent.paradoxplaza.com/public/1195088/image 04.png "image 04.png")



The final activity, the Hike, is one where you can temporarily leave behind the stress of court life and seek the calm of nature. Shy characters, you poor souls who would desperately try to lose stress through feasts, I see you.  

![image 05.png](https://forumcontent.paradoxplaza.com/public/1195089/image 05.png "image 05.png")



## Battle Points of Interest​

As a travel-focused pack, we wanted to include something new for the players to see as they traveled around the map. One I had wanted to include for a while was points of interest focused on battles. These new points of interest will come in two forms: dynamically created ones as particular battles happen on the map and historical ones set up from the start of the game.  

For the historical ones, we have some that can be seen in all our bookmarks and others that can only be seen in later bookmarks, like two related to the fight over England in 1066.  

![image 06.png](https://forumcontent.paradoxplaza.com/public/1195090/image 06.png "image 06.png")



## A Toast for Your Travels​

One minor addition to this patch is a new building and court position, primarily for Catholics but accessible by anyone with a new cultural tradition. The building can only be built in Catholic churches by default, but in any city for those who choose to get the cultural tradition. It is intentionally made to have a fair number of county-wide bonuses rather than holding specific ones and opening the new Court Brewmaster Court Position for whoever is in charge of the county.  

![image 07.png](https://forumcontent.paradoxplaza.com/public/1195091/image 07.png "image 07.png")


![image 08.png](https://forumcontent.paradoxplaza.com/public/1195093/image 08.png "image 08.png")



## Until Next Time​

That was all for this week. I hope you enjoyed this first look at Wandering Nobles. We will look in-depth at the activities and lifestyle perks next week. Until then, I figured I’d show some of the new art we have in the DLC to tide you over.  

![image 09.png](https://forumcontent.paradoxplaza.com/public/1195097/image 09.png "image 09.png")



![image 10.png](https://forumcontent.paradoxplaza.com/public/1195098/image 10.png "image 10.png")

<!-- artifact:reactions:start -->
- 88 Like
- 33 Love
- 9 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Snow Crystal](https://forum.paradoxplaza.com/forum/members/snow-crystal.1280952/)**
Role: Game Designer - Crusader Kings 3
Badges: 63
Reaction score: 12,089

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
