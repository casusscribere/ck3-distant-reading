---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1465030/"
forum_thread_id: 1465030
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 54
title: "Crusader Kings III Dev Diary #54 - A Sound Plan"
dd_date: 2021-03-30
author_handle: ParadoxGustav
expansion: Northern Lords
patch: Patch 1.3 (Corvus)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1145
inline_image_count: 6
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1465030'
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
    location: raw_lines_~28_to_148
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_147
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1590.jpg?1617107458
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_150_to_152
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_271_to_276
    action: preserved_and_flagged
    counts:
      Like: 86
      Love: 39
      (unlabeled — rendered as base64 data URI): 4
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_284_to_385
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_386_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1590.jpg?1617107458)
<!-- artifact:thread_banner:end -->

# Crusader Kings III Dev Diary #54 - A Sound Plan

<!-- artifact:thread_metadata:start -->
- Thread starter [ParadoxGustav](https://forum.paradoxplaza.com/forum/members/paradoxgustav.1338734/)
- Start date [Mar 30, 2021](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-iii-dev-diary-54-a-sound-plan.1465030/)
<!-- artifact:thread_metadata:end -->

 **A Sound Plan**  

Welcome to another Dev Diary from the Audio Department! Now that Northern Lords is out in the world, we can share some behind the scenes on what went on during development for the Flavourpack.  

We are going to talk about Field recording, The Sound design of the Event Images, some 1.3 patch updates, and of course, the music from Andreas Waldetoft.  

So if that is your cup of tea (or mead), then be our guest and follow along in this Dev Diary!  

**SFX**  
Field Recording:  
We decided early on in the production that we wanted genuine ambiences for the event backgrounds, which meant that source recordings were required.  
The recordings were conducted over a span of two days in a cold desolate “Vik” (Bay area) in the west coast called Onsala as it is currently known (Coming from “Odin's Sala” which translates to “The Halls of Odin” in Viking times) Which is my home area where I grew up.  

First of all, is preparation, what do you need for the recording session, and how light do you need to travel? (You don’t want to carry an entire audio studio on your back if you are tracking through forests and fields. Light is fast, and your back will thank you).  

I ended up using two handheld recorders, some lightweight stands, and an Ambisonic Microphone (a 4-way microphone array that captures audio in all directions, not unlike a VR camera, but for audio)  

That way I can position the location in post-production, and not worry if I did or didn’t capture something outside the audibility of a regular microphone.  

![image5.jpg](https://forumcontent.paradoxplaza.com/public/686637/image5.jpg "image5.jpg")


Picture 1: equipment test and packing day  

During the pandemic, there were minimal planes, cars, or any activity for that matter, which made it ideal for recording audio. it was just me, nature, and my recorders.  

![image7.jpg](https://forumcontent.paradoxplaza.com/public/686638/image7.jpg "image7.jpg")

Picture 2: Recording rig deployed on one location site.  

Placing yourself among Vikings wasn’t hard at all, and at times almost serene. Listening to the waves roll in on the shores is something quite special and I highly recommend it, if you can spare the time.  

[https://www.youtube.com/embed/ujSY0Z6C0b8?wmode=opaque](https://www.youtube.com/embed/ujSY0Z6C0b8?wmode=opaque)

Northern Lords Audio Field Recording Session  

**Event-images**  
After the field recording was concluded, the source material was processed and implemented to be the backgrounds for the event images that appear in the Northern Lords Pack.  
Each event image has a unique evolving loop that places you right in the center of the area. Whether it is out on the windy ocean, the stone pebbled shore, or in a pigsty prison!  
Videos of the different event images in the game during development:  

[https://www.youtube.com/embed/mQBXP6GmRGU?wmode=opaque](https://www.youtube.com/embed/mQBXP6GmRGU?wmode=opaque)

[https://www.youtube.com/embed/r92MJRfCkk8?wmode=opaque](https://www.youtube.com/embed/r92MJRfCkk8?wmode=opaque)

[https://www.youtube.com/embed/IP-Caqx9XkU?wmode=opaque](https://www.youtube.com/embed/IP-Caqx9XkU?wmode=opaque)

[https://www.youtube.com/embed/oNcUFMLiU4A?wmode=opaque](https://www.youtube.com/embed/oNcUFMLiU4A?wmode=opaque)

[https://www.youtube.com/embed/pz5r1wCfaqg?wmode=opaque](https://www.youtube.com/embed/pz5r1wCfaqg?wmode=opaque)


All of these are crafted in our sound design tools and then “performed” by Fmod.  
It can scatter the birds you hear, the insects that pass you by, or how windy the ocean is. All to make each event appearance as unique as possible, while still being in the same “space”.  


**Map Ambience**  
As part of the 1.3 update patch, winter now affects the map, and so does the audio, as shown in Dev Diary #49: A cold Embrace. Have a look at how the Winter sprawls with heavy snowstorms, and how the audible townspeople disappear from the outside and into the hearths and the warmth.  

We also updated the ambience system to a procedural system. That we call the  
Map Ambience System. (Highly technical terminology at play here)  

It is driven by the game camera, that scans the terrain of all visible provinces, determines what amount of a specific terrain type the camera can see at any point in time, and generates a percentage value that then gets translated into a Fmod parameter that is connected to the Master Ambience Event.  

All this fancy talk boils down to, rather than us having us placing hundreds of audio emitters on the map at strategic locations (we did, and let me tell you, that is labor-intensive!) The game tells the audio middleware (Fmod) what to play, when, where and how much.  

And now, over to Andreas, our Senior Music Composer!  


**MUSIC**  

Hi all, Andreas Waldetoft here,  

I’m glad to be talking about the music that we wrote for the Northern Lords  

In this Flavourpack, we recorded authentic old instruments from the time era, like the lovely Mungiga (translates to Mouth-Harp or Jaw-Harp) different kind of flutes, Swedish bagpipes, fiddles such as a Keyed Fiddle and Hardanger Fiddle, a Throat singer and not to forget a Viking Choir singing in Norse.  

Recording anything in a pandemic is not an easy feat, especially with varying amounts of lockdown, for example, Kalabalik, our medieval session musicians and skalds for hire, did a fantastic job recording themselves from a home setting. Below are some images of the instruments that made an appearance in the score:  


![image2.jpg](https://forumcontent.paradoxplaza.com/public/686628/image2.jpg "image2.jpg")


Picture 1: Mouth Harps  

![image6.jpg](https://forumcontent.paradoxplaza.com/public/686629/image6.jpg "image6.jpg")


Picture 2: Closeup Nyckelharpa  

![image4.jpg](https://forumcontent.paradoxplaza.com/public/686648/image4.jpg "image4.jpg")


Picture 3: Overview of some of the live instruments included in the soundtrack  

![image1.jpg](https://forumcontent.paradoxplaza.com/public/686632/image1.jpg "image1.jpg")


Picture 4: Studio Deepwods, Also known as my composing lair  

We are all so happy and grateful for the result and prove that music can be done anywhere, and what matters is that the soul of the music is there.  
What you as the player will hear are Three new mood tracks called Drakkar, Scandinavia, and The Feast and One new cue track called The Raid.  
The nifty thing with our music system is that both Scandinavia and The Raid have different versions that vary between themselves, so there will be variations that play intermittently during a game-session.  

I'll leave you all with this, The cue called The Raid. Enjoy!  


[https://www.youtube.com/embed/6Wb7JT7iVio?wmode=opaque](https://www.youtube.com/embed/6Wb7JT7iVio?wmode=opaque)



That is all from us in the Audio Department, until next time!

 

Last edited by a moderator: Mar 30, 2021

<!-- artifact:reactions:start -->
- 86 Like
- 39 Love
- 25 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [ParadoxGustav](https://forum.paradoxplaza.com/forum/members/paradoxgustav.1338734/)**
Role: Recruit
Badges: 59
Messages: 6
Reaction score: 219

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
