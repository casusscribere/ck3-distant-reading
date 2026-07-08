---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1623007/"
forum_thread_id: 1623007
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 143
title: "Dev Diary #143 - The Next Chapter"
dd_date: 2024-02-02
author_handle: rageair
expansion: Legends of the Dead
patch: Patch 1.12
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1038
inline_image_count: 2
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1623007'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2837.jpg?1707240666
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_222_to_227
    action: preserved_and_flagged
    counts:
      Love: 292
      Like: 109
      (unlabeled — rendered as base64 data URI): 3
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_235_to_351
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_352_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2837.jpg?1707240666)
<!-- artifact:thread_banner:end -->

# Dev Diary #143 - The Next Chapter

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Feb 2, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-143-the-next-chapter.1623007/)
<!-- artifact:thread_metadata:end -->

Greetings!  

I’m [@rageair](https://forum.paradoxplaza.com/forum/members/375731/), the Game Director for Crusader Kings III, and today I’m excited to present to you Chapter III - in this Dev Diary we’ll briefly go over the themes of each of the expansions that will make up the full package and take sneak a peek at their features!  

Chapter III is definitely our most ambitious chapter yet, with a Core Expansion, Major Expansion, and an Event Pack (as well as an instant chapter unlock!) New ways of playing the game, and big, sweeping systems is the name of the game this year. Let's have a look, shall we!  

---


#### **Core Expansion -** ***Legends of the Dead***​

*Legends of the Dead* is all about the map - specifically that which spreads throughout it! Core Expansions will, as mentioned in previous Dev Diaries, focus on broad systemic changes to the core gameplay loop, or high-impact systems that affect large parts of the game world. As this is our first Core Expansion, we wanted systems that were big and all-encompassing, affecting all rulers on the map in one way or another! With that said, here’s a high-level list of what you will see in the Expansion and its accompanying update:  

Legends  
Tales of your or your ancestors' epic deeds will travel across the map, spreading news of your glory across borders into foreign realms. Embellished tales of heroism or piety were a massive and common part of medieval life, and here we’re allowing you to write your own saga - quite literally! As your legend spreads, a book will be updated with your story - and events you get along the way may allow you to… alter certain aspects to suit you better, after all perhaps it was a dragon that your grandfather slew rather than a bear! The more your legend spreads across the map, and the more rulers that propagate it, the more famed it will become.  

Plagues  
Plagues are the second thing that spreads across the map, but unlike legends they are destructive and nefarious - with a promise to shake up the game! Deadly diseases can sweep across your lands, spawned by either random chance or the activity of armies, and they will destroy development and kill characters with a vengeance. All plagues are different, with varying effects - such as consumption ending the lives of elders with haste, measles shortening the lives of children, and Holy Fire (aka the Dancing Plague) making rulers… move erratically. Of course, there will be ways to combat and recover your lands from these terrible maladies!  

![image1.png](https://forumcontent.paradoxplaza.com/public/1069350/image1.png "image1.png")


*[Image - One of the ways plagues are visualized]*  

The Black Death  
A looming threat that appears towards the later eras - there is no escape from the Black Death, no matter how much you prepare, the end is nigh!  

Legitimacy  
This is a new measurement of your right to rule and affects a whole host of other systems from factions, vassalization, and even title creation. Of course, this new value will heavily tie into both Legends and Plagues, but also a myriad of other systems. A legitimate ruler will have a much easier time running a realm… but some very tempting actions, such as unrightful title revocation, will decrease legitimacy - making it a precarious balancing act!  


#### **Major Expansion -** ***Roads to Power***​

Climbing your way up from Count to Emperor is a challenge - but to claw your way up the treacherous political ladder of the Byzantine bureaucracy or claiming a new realm as a destitute Adventurer are more challenging yet! This Major Expansion introduces two brand new ways of playing the game, one focused on the Administrative governance of Eastern Rome, and the other on traveling the map in search of fame and fortune. These features have been oft-requested since the early days of Crusader Kings, and we thought it high time to do them - we're pulling out all the stops!  

Imperial Administration  
Take the reins of a powerful Noble Family within Byzantium and lobby for powerful governorships. Use your influence to improve your standing, improve your estate, and ultimately convince the other families that you should rule as emperor!  

Adventurers  
Set out across the world as a historical adventurer, one of your own making, or keep playing your beloved character after being unfortunately deposed from your lands! Travel to distant realms, take on contracts, gather friends, wealth, and fame - do mercenary work, or settle in new lands.  

Everything Byzantium  
I’m not exaggerating when I say that this expansion will be dripping with Byzantine flavor. From imperial fashion to new buildings, historical flavor, beautiful mosaics, and much more - the game will immerse you in the setting with a passion.  

![image2.jpg](https://forumcontent.paradoxplaza.com/public/1069351/image2.jpg "image2.jpg")


*[Image - Everyone likes grapes]*  


#### **Event Pack -** ***Wandering Nobles***​

Travel is a mechanic that really connects your characters to the map, and in this Event Pack we want to flesh the mechanic out with even more reasons to travel, and things that can happen on the road - new sights to see, new paths to take, and new stories to weave together into an immersive narrative!  

Is it about the journey, or the destination? Your characters can decide for themselves as they engage with a new Traveler Lifestyle!  

#### ​

#### **Instant Unlock -** ***Couture of the Capets***​

The French were a fancy lot, and with this Instant Unlock you can admire their splendor during the high medieval period. As always we’ve put a lot of effort into research to make sure that the clothes are not only glorious, but as historical as we can make them!  

---

That’s it for now! Next week we’ll begin posting Dev Diaries for Legends of the Dead, so keep your eyes out! Also, a reminder that Chapter III is available right now, and if you purchase it now you will immediately get access to the *Couture of the Capets* (as well as the expansions as soon as they are released, of course!)  

We’re very excited to show off the work we’ve done, this really is the biggest chapter we’ve ever done! Until next time!

<!-- artifact:reactions:start -->
- 292 Love
- 109 Like
- 7 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
