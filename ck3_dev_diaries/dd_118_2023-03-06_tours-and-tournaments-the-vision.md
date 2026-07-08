---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1572201/"
forum_thread_id: 1572201
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 118
title: "CK3: Tours and Tournaments - The Vision"
dd_date: 2023-03-06
author_handle: rageair
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1168
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1572201'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2222.jpg?1678115634
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_214_to_219
    action: preserved_and_flagged
    counts:
      Like: 269
      (unlabeled — rendered as base64 data URI): 6
      Love: 141
      Haha: 7
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_227_to_324
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_325_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2222.jpg?1678115634)
<!-- artifact:thread_banner:end -->

# CK3: Tours and Tournaments - The Vision

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Mar 6, 2023](https://forum.paradoxplaza.com/forum/developer-diary/ck3-tours-and-tournaments-the-vision.1572201/)
<!-- artifact:thread_metadata:end -->

Greetings!  

*Come one, come all! The grand tournament awaits your attendance - your steeds have been readied and your entourage assembled for the journey ahead! It’s time to show the world your graciousness as host and worth in the arena… but to get there, we’re better off routing our journey around the treacherous mountain passes of Stipon, as I hear they’ve been crawling with highwaymen since your, ahem, dalliance with Duke Andronikos’ wife during his son's wedding. Then there’s the matter of your unruly vassals: perhaps it’s time for a royal tour?*  

The life of a ruler was always active - there were many things to attend to, and most courts at the time were itinerant, roaming from place to place constantly. *Tours and Tournaments* aims to give rulers plenty of things to do, especially during times of peace, by introducing new systems of Travel and Grand Activities!  

As mentioned in the [Floorplan Dev Diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-109-floor-plan-for-the-future.1546534/), we want to reinforce the connection between *character* and *map* - after all, the game is played on a beautiful medieval map, and no longer will the only time your ruler leaves the safety of their capital be when you’re at war. There’s an entire world out there to explore, filled with both great opportunities and adventurous obstacles.  

By assembling an entourage, selecting options for your travel, and hiring a caravan master, you are ready to set out on the road and travel to activities across the world. The Travel system is an integral part of activities, with both the host and guests traveling to reach them - creating a stronger feeling of *place* as you see your route being plotted and your character moving directly on the map.  


![3.png](https://forumcontent.paradoxplaza.com/public/941418/3.png "3.png")


[Image: The Duke of Bohemia setting out on a Tour]  

So what are these activities you can travel to, you ask? There’s plenty - firstly we’ve updated and revamped Feasts, Hunts, and Pilgrimages completely - the bread-and-butter of activities. There’s now a reason to hunt in a specific forest within your domain, as a ferocious wolf or legendary stag might have been spotted there - or a reason to hold a feast in a holding with leisure palaces, as you might need to impress a particularly unruly vassal. Pilgrimages will now be epic journeys, potentially taking years if you’re going far - making it necessary for a regent to rule in your stead. All activities have dedicated interfaces with easily-accessible information and beautiful art to set the scene.  

Of course, there are Grand activities that are even more impactful - each of them different in their own magnificent way! They have Options and Intents which affect rewards and what type of content you might encounter. Our aim is to make each activity have a clear purpose and be interesting in its own right, therefore we chose to make Grand Tournaments, Grand Tours, and Grand Weddings - three vastly different activities with vastly different executions and purposes!

![2.png](https://forumcontent.paradoxplaza.com/public/941419/2.png "2.png")


[Image: Example of Activity Types, initial step]  

Grand Tournaments are where you go to test your mettle: spectacles to be announced far and wide, with rewards ranging from precious trinkets to fabulous prizes! Grand Tournaments aren’t only for martially-inclined characters - while there are contests such as melees and jousts, there are also more cerebral ones such as recitals or erudite board games. You can join your knights in slippery wrestling, eagle-eyed archery, dangerous horse racing, and vicious team melees - all clad in gleaming armor brandishing your coat of arms for the masses to see! Participating and winning in these contests will see your characters and knights grow in skill and receive prizes; living the life of a frequent tournament-goer is a valid path to take. Exploring the tournament Locale and choosing the right Intents might help you out in other ways as well, be it finding friends or dispatching rivals. If you’re in need of renown, hosting tournaments yourself will grow your standing significantly, as rulers from foreign realms come flocking to the fateful grounds, eager to compete!  


![4.png](https://forumcontent.paradoxplaza.com/public/941420/4.png "4.png")


[Image: Snapshot of part of the Tournament UI. Tournaments, unlike other Grand Activities, have an extra special interface - more on that in the Tournaments Dev Diary]  

Grand Tours see you assemble your entire court and set out to visit vassals in your realm - an activity commonly undertaken by medieval rulers. This is a way to assert your overlordship, while also enjoying the hospitality your vassals have to offer. There are various paths to take: Intimidation, Majesty, or Taxation, all affecting the rewards and opinions of your vassals. At its core, Tours are a tool for realm stability - and something a newly-ascended ruler should undertake quite early to avoid factions and revolts. You also get to choose between ways of approaching your vassals individually; you might want to tour the grounds, observe a cultural festival, or simply have a private dinner hosted for you.  

Grand Weddings allow you to marry above your station… if you’re willing to pay the cost! They also provide ample opportunity for diplomatic shenanigans, such as impressing neighboring rulers into becoming vassals, forming hard-to-get alliances, or creating favorable matches for your children. Of course, these spectacles come with everything you’d expect out of a medieval ceremony - revelries, drama, and even a bedding ritual at the end. Or you can invite a group of mercenaries to color the halls crimson with the blood of the other House, should you desire it.  


![1.png](https://forumcontent.paradoxplaza.com/public/941421/1.png "1.png")


[Image: Planning a Grand Wedding]  

As some of you managed to cleverly figure out, there’s also a brand-new regency system where we’ve made sure that it’s both interesting to *have* and to *be* a regent. Loyal regents help you by dutifully fulfilling their Mandates, and being the regent of your liege gives you opportunities to (with varying degrees of bloodshed) seize the throne for yourself, should you be doing a “good” job.  

There’s also a myriad of other changes which we’ll go into in future dev diaries - smaller systemic updates to buildings, knights, vassal opinions, and so on - all to support a more interesting and living map, where your choices matter more.  

So take to the road, ruler - great opportunities await!  

Tours and Tournaments will be released in late spring, and until the release we will have weekly Dev Diaries.  

Don’t forget to wishlist:  
[Wishlist on Steam](https://pdxint.at/3ZM3AjJ)  
[Microsoft Store](https://pdxint.at/41NnwnU)  

[Watch the trailer here!](https://youtu.be/YUpC4IdfXuE)  


[https://www.youtube.com/embed/YUpC4IdfXuE?wmode=opaque](https://www.youtube.com/embed/YUpC4IdfXuE?wmode=opaque)

<!-- artifact:reactions:start -->
- 269 Like
- 232 (unlabeled — rendered as base64 data URI)
- 141 Love
- 20 (unlabeled — rendered as base64 data URI)
- 7 Haha
- 6 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 35 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
