---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1391886/"
forum_thread_id: 1391886
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 27
title: "CKIII Dev Diary #27 - Cultures & Cultural Innovations"
dd_date: 2020-05-19
author_handle: Wokeg
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1673
inline_image_count: 13
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1391886'
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
    location: raw_lines_~28_to_143
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_142
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1383.jpg?1589891475
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_145_to_147
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_288_to_293
    action: preserved_and_flagged
    counts:
      Like: 165
      Love: 72
      (unlabeled — rendered as base64 data URI): 10
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_301_to_408
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_409_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1383.jpg?1589891475)
<!-- artifact:thread_banner:end -->

# CKIII Dev Diary #27 - Cultures & Cultural Innovations

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [May 19, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ckiii-dev-diary-27-cultures-cultural-innovations.1391886/)
<!-- artifact:thread_metadata:end -->

Greetings, dear friends, and welcome to the cultural dev diary! Today, we’re going to be going over some familiar mechanics from CK2, and, relatedly, our decidedly less familiar all-new tech system!  

**Cultures & Culture Groups**  
The basic structure of the cultural system will be fairly recognisable to many of you. Every county and character on the map has a culture, representing (usually) the majority demographic for that county or the preferred customs of that character. Most cultures are based around a language, but some focus more on dialect or specific bodies of tradition, and a few are even primarily just regional.  

Every culture, in turn, belongs to a culture group. These are gatherings of several cultures that, whilst distinct from one another, are nevertheless closely related. Most often this is down to a shared root culture, but in a few cases cultures have entered the same group merely by cohabiting for a long period of time.  

Characters who come from completely different cultures like each other less, with characters who come from different cultures within the same group taking a reduced penalty. Like CK2, this only matters within your realm, so you won’t get grumpy at your neighbour for being different unless you’re occasionally required to talk to the lad.  

Cultural preferences carry over to the peasantry: if the lord who directly holds a particular county doesn’t share that county’s culture, then that county will take a hit to popular opinion (with the hit being smaller if they’re at least part of the same culture group).  

Of course, as this is only the direct holder of a county, having a good friend who understands the local customs in charge of all these strange foreign peasants can be an excellent way to stave off peasant revolts...  

**But what about...**  
… Melting pots and culture splits? Still got ‘em! We’ve even got some fancy new scripted effects to make it easier than ever to add your own.  

Culture conversion is also more easily accessible: per the council task dev diary, this is now a council task, performed by your steward. You can attempt to culture convert any county in your sub-realm, though without an excellent steward or certain types of faith, it’ll likely take a while. People seldom change their culture quickly or willingly.  

**Show us the good stuff!**  
Ahhhhhh, you want to see some maps? See how granular we’re getting with our cultural setup this time around? Well, maps I’ve got! How many new cultures can you pick out?  

![001.png](https://forumcontent.paradoxplaza.com/public/566852/001.png "001.png")



![002.png](https://forumcontent.paradoxplaza.com/public/566853/002.png "002.png")



![003.png](https://forumcontent.paradoxplaza.com/public/566854/003.png "003.png")



![004.png](https://forumcontent.paradoxplaza.com/public/566855/004.png "004.png")



**Cultural & Technology**  
In CK3, cultures mean a lot more than just a few points of opinion here and there. Cultures are now an integral part of our reworked system for technology, with eras, explicit innovations, and mechanics for tussling over the cultural heart of your people.  

**Innovations**  
Innovations are the very heart of CK3’s technological system. Each one represents a thorough proliferation of an idea, a legal practice, or a specific technology, taken to heart by any given culture, or still weird and foreign no matter its advantages. As the game progresses, cultures will slowly become more and more accustomed to the various innovations, until each innovation is thoroughly embraced and ubiquitous amongst the people of that culture. At that point, an innovation is considered “unlocked”, and its unique benefits are accessible to characters and counties of the unlocking culture.  

![005.png](https://forumcontent.paradoxplaza.com/public/566856/005.png "005.png")



Benefits for each innovation vary tremendously between them. Some unlock new and better forms of succession law, some give bonuses to growth or income, some allow access to specific Men-at-Arms, or even grant entirely new CBs. We have innovations for everything from battlements to bombards, from coinage to cranes, and wootz steel to wierdijks!  

Innovations broadly fall into one of three categories: military, civic, and special (a.k.a, "Cultural and Regional"), each grouped together in the interface.  

Military and civic innovations typically cover what you might expect (martial and non-martial matters, respectively). All cultures can, eventually, acquire all military and civic innovations.  

Special innovations behave a bit differently. A few are unlocked via special decisions and can only be acquired by taking those decisions, whilst some are cultural, requiring you to belong to a specific culture or culture group, but most are regional innovations.  

![006.png](https://forumcontent.paradoxplaza.com/public/566858/006.png "006.png")



Regional innovations require you to either have at least a certain number of counties within a specific area to unlock, or else to have a certain percentage of your culture’s total counties within that area. They represent concepts and technologies that were specific to certain areas historically, rather than spreading across large areas of the globe, but which could very easily have been developed by any culture moving into that area.  

Needless to say, innovations, the bonuses they provide, and the mechanics they unlock are all fully scriptable and can be modded with ease.  

**But how do I *unlock* an innovation?**  
All innovations have a small chance to progress towards being unlocked per month, affected by a few factors, with the most telling one being average development of the sum counties a culture holds. A culture that spreads recklessly will have naturally slower growth than one that exists in concentrated pockets of high development.  

The major ways generation progress towards unlocking innovations are setting fascinations and exposure. Each of these affect only a single innovation at a time, though both happen simultaneously.  

Exposure is a natural process, occurring when your culture has counties that border another culture with a specific innovation. The more you have in common (culture group, religion, and so on) with that other culture, and the more of its counties your culture borders, the faster you’ll unlock that innovation.  

![007.png](https://forumcontent.paradoxplaza.com/public/566859/007.png "007.png")



Fascination, by contrast, is an entirely character-driven process, reflecting the drive of powerful leaders to introduce new concepts and technologies (be they original or imported) to their people. Where exposure is selected randomly from suitable innovations, fascination is deliberately selected by a specific character.  

Who gets to pick? Why, the cultural head.  

![008.png](https://forumcontent.paradoxplaza.com/public/566860/008.png "008.png")



Any culture with at least one landed ruler somewhere has a cultural head, who then has complete control over which fascination is selected from available innovations. The cultural head *always* shares the culture they are the head of, and is the character with the most counties of that culture within their sub-realm in the world.  

As you can imagine, the size of the culture makes a difference in how easy it is to become (and stay) cultural head: there are many more Andalusian counties than there are, say, Cornish ones.  

An important factor in unlocking innovations via fascination is the learning skill of the cultural head. An unlearned cultural head doesn’t do much to bring new ideas and technologies to their people, but an erudite scholar knows who to invite to court, how to phrase ideas in a way the peasants will accept, and how to get the nobility to see the benefit of embracing a foreign concept!  

**Eras**  
You might be thinking that this sounds a little bit disorganised. What stops me, say, unlocking bombards in the 900s and blowing my enemies away with oversized canons for the next five hundred years?  

The answer to that is eras.  

![009.png](https://forumcontent.paradoxplaza.com/public/566862/009.png "009.png")



In CK3, all innovations are organised into one of four eras, before being categorised into military, civic, or special. In order to begin unlocking innovations from an era, you need to have actually *reached* that era.  

If an innovation belongs to the Tribal Era, no problem. All cultures start with the tribal era reached, and many primarily-feudal cultures will start with most (if not all) of its innovations unlocked, especially in 1066.  

For the eras beyond that (the Early Medieval, High Medieval, and Late Medieval), you need to meet two criteria. The date must be at least an appropriate minimum year (e.g., the high medieval period cannot start before 1050 AD), and you must have at least 50% of the preceding era’s innovations unlocked. Further, if your cultural head is tribal, you will be unable to progress to the next era until you obtain a non-tribal cultural head. Cultures that have just left the Tribal Era will unlock innovations faster for a time, allowing them to catch up a little as medieval social and legal structures begin sweeping their lands.  

Eras therefore let us gate technologies and features in stages, so that cultures which thrived in later centuries can still use their special bonuses, units, and features, but don’t get them too anachronistically.  

Aaaand that about wraps it up for cultures and technology! I’ll be around the thread to answer questions for the next couple of hours, but otherwise, we’ll see you next week!

 

#### Attachments

- [![001.png](https://forumcontent.paradoxplaza.com/thumbnail/public/566848/001.png)](https://forum.paradoxplaza.com/forum/attachments/001-png.579489/)
  
  001.png
  1,1 MB

 · Views: 0

- [![002.png](https://forumcontent.paradoxplaza.com/thumbnail/public/566849/002.png)](https://forum.paradoxplaza.com/forum/attachments/002-png.579490/)
  
  002.png
  1,1 MB

 · Views: 0

- [![003.png](https://forumcontent.paradoxplaza.com/thumbnail/public/566850/003.png)](https://forum.paradoxplaza.com/forum/attachments/003-png.579491/)
  
  003.png
  1,1 MB

 · Views: 0

- [![004.png](https://forumcontent.paradoxplaza.com/thumbnail/public/566851/004.png)](https://forum.paradoxplaza.com/forum/attachments/004-png.579492/)
  
  004.png
  1,2 MB

 · Views: 0

<!-- artifact:reactions:start -->
- 165 Like
- 72 Love
- 34 (unlabeled — rendered as base64 data URI)
- 10 (unlabeled — rendered as base64 data URI)
- 10 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)**
Role: Former CK3 Experienced Game Designer
Badges: 49
Messages: 528
Reaction score: 15,169

*[Full game-badge icon list of 49 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
