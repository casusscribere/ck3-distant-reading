---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1625227/"
forum_thread_id: 1625227
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 146
title: "Dev Diary #146 - It Started With a Cough..."
dd_date: 2024-02-27
author_handle: blackninja9939
expansion: Legends of the Dead
patch: Patch 1.12
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2628
inline_image_count: 34
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1625227'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2876.jpg?1709038801
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_436_to_440
    action: preserved_and_flagged
    counts:
      Like: 107
      Love: 75
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_448_to_505
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_506_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2876.jpg?1709038801)
<!-- artifact:thread_banner:end -->

# Dev Diary #146 - It Started With a Cough...

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [Feb 27, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-146-it-started-with-a-cough.1625227/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to the 146th Dev Diary for Crusader Kings III! I’m Matthew, the Code Owner on *Legends of the Dead*. From the highly anticipated Epidemics feature to the Black Death itself—and what happens after your land is ravaged and your family taken to the grave—today we’re going to be covering all things Death!  

As stated in [the Vision Dev Diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-144-legends-and-lesions.1624034/), we’ve wanted to include Epidemics for a long time now—doing them bigger and better than CK2 ever did.  
Plagues should be an impactful part of the game, ranging from a mild illness in a localized area to the sweeping spread of diseases across continents. Not only should they cause death in their wake, but those who survive should have their trust in your rulership tested.  

Every barony with a holding is susceptible to an outbreak of disease, and many factors can influence the chance of an outbreak:  


- The development of the county
- Terrain of the province
- Number of buildings
- Specific buildings such as trade posts and markets
- Cultural era
- If there is a nearby epidemic already
- Game rules

When an outbreak occurs, it will be one of three intensities: Minor, Major, and Apocalyptic.  
The intensity impacts how much the disease can spread, how likely it is to spread to an uninfected province, and how long an infection in a province lasts.  

![image-01.png](https://forumcontent.paradoxplaza.com/public/1076728/image-01.png "image-01.png")



Each disease will leave the infected with a specific associated trait, and any character located in an infected province is at risk of getting sick.  

All outbreaks will get a dynamic name. Some will be named after the culture of the area, while others will claim the name of the region’s ruler…since if they were truly a legitimate ruler, the Gods would not punish them with such disease, right?  

Every ongoing epidemic can be seen on the map too, both as an effect in normal map modes or in its own dedicated map mode.  

![image-02.png](https://forumcontent.paradoxplaza.com/public/1076729/image-02.png "image-02.png")



![image-03.gif](https://forumcontent.paradoxplaza.com/public/1076730/image-03.gif "image-03.gif")



If you zoom in closer then we hide the epidemic pulsing blood and instead show the desolate gray land now haunted by death…  

![image-04.png](https://forumcontent.paradoxplaza.com/public/1076731/image-04.png "image-04.png")



When there is an epidemic nearby or in your realm, you will be notified by the new HUD widget, which if you open (or switch to the map mode manually) will show you more info about ongoing epidemics.  

![image-05.png](https://forumcontent.paradoxplaza.com/public/1076732/image-05.png "image-05.png")



If you click an epidemic on the map, or from the list, then you’ll be able to see an overview of the epidemic for every province in your domain it has infected, as well as the vassals in your realm and other independent rulers.  

This also shows you which provinces are at risk of being infected by the epidemic and what the chance of it spreading is.  

![image-06.png](https://forumcontent.paradoxplaza.com/public/1076733/image-06.png "image-06.png")



The chance of spreading to a neighboring province, as well as across two sea provinces, is influenced by many factors, such as how developed the provinces are, their buildings, cultural traditions, if they have immunity from prior infection, and more!  

Speaking of province infection, you can see here that every province tracks how infected it is as a percentage. Different infection thresholds will cause different modifiers to be applied to the province and its holder.  

![image-07.png](https://forumcontent.paradoxplaza.com/public/1076734/image-07.png "image-07.png")


![image-08.png](https://forumcontent.paradoxplaza.com/public/1076735/image-08.png "image-08.png")



The maximum infection rate is reduced by Plague Resistance, which can be increased through various means.  
You can preemptively increase it by constructing buildings that raise it, such as the new Hospices building chain or the Burial Site duchy building.  

![image-09.png](https://forumcontent.paradoxplaza.com/public/1076736/image-09.png "image-09.png")



You can also increase it by having your Court Physician work to Control Plagues using the new Court Position Tasks, or by taking the decisions to isolate in your capital or close the gates.  

![image-10.png](https://forumcontent.paradoxplaza.com/public/1076737/image-10.png "image-10.png")



*Legends of the Dead* also features three new illnesses that can take the form of Plagues. Measles, the Bloody Flux (Dysentery), and Holy Fire (Ergotism).  
As mentioned before, Measles is especially deadly to children, lowering their health even more than everyone else’s. This uses two new modifiers we’ve added for child and elderly health respectively, most diseases are more deadly to the elderly by default.  

![image-11.png](https://forumcontent.paradoxplaza.com/public/1076738/image-11.png "image-11.png")



Of course it wouldn’t be one of my dev diaries if I didn’t also point out that all of these things are very moddable: you can create custom epidemics, change how they spread, outbreak, infect characters, even how their blood splatter looks on the map!  

Both Plagues and Legends come with a handful of game rules for controlling how they play, as well as specific rules for the Black Death.  

![image-12.png](https://forumcontent.paradoxplaza.com/public/1076739/image-12.png "image-12.png")



Speaking of which, the Black Death holds a special place amongst the rest of the pantheon of epidemics, and as such, has some extra bells and whistles to go along with it.  


---

### The Black Death​

Hello all, [@PDS_Noodle](https://forum.paradoxplaza.com/forum/members/1394234/) here to ask the old question: “ʟᴏʀᴅ, ᴡʜᴀᴛ ᴄᴀɴ ᴛʜᴇ ʜᴀʀᴠᴇsᴛ ʜᴏᴘᴇ ꜰᴏʀ, ɪꜰ ɴᴏᴛ ꜰᴏʀ ᴛʜᴇ ᴄᴀʀᴇ ᴏꜰ ᴛʜᴇ ʀᴇᴀᴘᴇʀ ᴍᴀɴ?”  

![image-13.png](https://forumcontent.paradoxplaza.com/public/1076740/image-13.png "image-13.png")



No history of the medieval world is complete without reference to the Black Death.  

Killing up to half of Europe’s population over the course of seven years, the Bubonic Plague that swept across Europe, North Africa, and the Middle East in the 14th century altered the very fabric of society. Everyone - man, woman, adult, child, noble, pauper - found themselves at the mercy of the merciless pestilence. From the outset of development, we knew the Black Death had to be done proper justice.  

This naturally involves a bit of a balancing act. On one hand, the Black Death should behave within the confines of the mechanics we’ve built, so that reaction to it is natural and swift. Presenting you, the player, with an unfamiliar new set of ways to deal with this unique event would be complicating matters for no real gain. After all, the plague itself is simply the scariest amongst a whole host of potential pandemics that could occur. On the other hand… It's the Black Death. Anyone should feel the fear of God and be reaching for their rosaries when they see that seeping dark mass wend its way on to their screen.  

![image-14.png](https://forumcontent.paradoxplaza.com/public/1076741/image-14.png "image-14.png")



As such, the tack we took involved a deeper look at how the plague rolled out across the land. Like any good movie monster, half the fear is in the anticipation of the reveal rather than the monster itself, after all. It’s one thing to be dealing with the plague, but consider instead the stormy horizon: first come the missives of death and devastation, then the bedraggled and petrified refugees staggering to your borders, and then all of a sudden your armpit begins to swell…  

*That* is the frame of mind we want the player to be in when the plague erupts. When the scythe starts swinging there’s not a whole lot anyone can do, but the precious moments before that wicked blade reaps its harvest are the ones worth investigating.  

![image-15.png](https://forumcontent.paradoxplaza.com/public/1076742/image-15.png "image-15.png")



To move on from setting such an overly-elaborate scene, then, the actual mechanics of the Black Death follow the pattern laid out by other very large epidemics in-game. The notable difference is that - unless you’re incredibly unlucky (or have a truly massive empire, in which case I allow you no sympathy) and happen to have it take hold within your own realm - you’ll be getting fair warning of the coming storm.  

As the panic mounts, you’ll be able to at very least begin to make provisions for protecting your realm, aided or hindered by a set of unique Black Death events that will give you opportunities to stock up some counties beforehand. These vary from calming panicking crowds right through to instructing your physician to dissect infected bodies to try and glean some meager information.  

I won’t spoil those events any further here, but between them and the advanced warning a player can get, the Black Death becomes less strictly about waiting for the inevitable and more about a race against time. You will have to utilize all your options to the fullest to even withstand it, let alone escape relatively unscathed.  

As with any Apocalyptic-level disease, the damage wrought by the plague can be mighty. More developed areas of your realm will suffer harder in comparison, and the sickness can wipe out entire branches of families. The issue with the Black Death in that case is its violent effects. Its modifiers are brutal, and its cocktail of lethality and infectiousness makes for the single greatest consistent threat to a realm in the entire game.  

This is already getting rather lengthy, so I’ll leave it there. Hopefully you all have as much fun battling the Black Death as I did making it!  


---

### Funerals​

Of course, with Plague comes Death, and with that comes a time to mourn your lost friends and family:  

And with all this desolation there also comes the opportunity to remember the dead. With *Legends of the Dead*, we're introducing a new type of Activity: Funerals.  

![image-16.png](https://forumcontent.paradoxplaza.com/public/1076743/image-16.png "image-16.png")


*[Image: Decision to host a Funeral]*  

You can hold a Funeral for any deceased member of your family in the past 5 years, and a new specific intent "Mourn" is available as default, allowing you to lose some stress after going through the process of grief.  

![image-17.png](https://forumcontent.paradoxplaza.com/public/1076744/image-17.png "image-17.png")


*[Image: Funeral planning]*  

The Activity Planner will suggest the best place in your realm to host a Funeral, prioritizing baronies with a temple, and high level temples within that; if you choose one of them you will get extra Piety as a reward.  

![image-18.png](https://forumcontent.paradoxplaza.com/public/1076745/image-18.png "image-18.png")


*[Image: Selecting a place for your Funeral]*  

The different levels of the "Ceremonials" Activity Option also offer better final rewards for a higher gold cost, focused on Piety, Legitimacy and Stress loss.  

The first phase of the Funeral is the Wake, the wait until the Burial, and it features all guests reminiscing about the life of the deceased, their memories together and their more characteristic traits. They may also interact with each other and even in these distressed times there will be someone waiting patiently just to get a hook… or increase the funeral numbers.  

![image-19.png](https://forumcontent.paradoxplaza.com/public/1076746/image-19.png "image-19.png")



The "Burial" phase has different descriptions and general flavor depending on your faith's tenets, and will reflect your religious traditions, not always being a burial per se.  

All throughout the celebration, Active Pulse Actions (or APAs) will also inform you of what the other guests are doing meanwhile, bringing the activity to life (pun not intended).  

![image-20.png](https://forumcontent.paradoxplaza.com/public/1076747/image-20.png "image-20.png")



Funerals mainly reward your Piety and Legitimacy, as a moment to reflect on both the brevity of life and the legacy that we leave behind.  


---

### Disease Decals & How to Prevent Them​

![image-21.png](https://forumcontent.paradoxplaza.com/public/1076748/image-21.png "image-21.png")



As part of this Core Expansion, we’ve also decided to implement more ways of showing the declining health of your ruler & their kin. Now, most of you might know the plague was already grotesquely displayed in the game prior to *Legends of the Dead* - and hopefully you’ll be excited to welcome two new diseases to the visual roster: Smallpox and Measles.  


![image-22.png](https://forumcontent.paradoxplaza.com/public/1076749/image-22.png "image-22.png")


*[Image: Now might be a good time to remind the good player that this box can be un-ticked in the settings]*  

![image-23.png](https://forumcontent.paradoxplaza.com/public/1076750/image-23.png "image-23.png")



And while we’ll mostly leave it up to you to figure out what to do with those diseases, as far as prevention and treatment is concerned, I think it’s safe to say you’ll definitely want to employ a court-physician. Fortunately, us from the character art team have been hard at work making that option as lucrative as possible - by adding some new sick physician clothes (along with a bunch of other new garments as well of course).  


---

### Achievements​

And last but not least we have the new achievements! As always, they are listed in order of difficulty.  


Very Easy  

![image-24.jpg](https://forumcontent.paradoxplaza.com/public/1076751/image-24.jpg "image-24.jpg")


**Legendary!** - *Complete a Legend*  

![image-25.jpg](https://forumcontent.paradoxplaza.com/public/1076752/image-25.jpg "image-25.jpg")


**You'll Never Take Me Alive!** - *Travel to a safe holding while your Capital is infected by a Epidemic*  


Easy  

![image-26.jpg](https://forumcontent.paradoxplaza.com/public/1076753/image-26.jpg "image-26.jpg")


**Pay Respects** - *Host a Funeral for your Legend Protagonist*  

![image-27.jpg](https://forumcontent.paradoxplaza.com/public/1076754/image-27.jpg "image-27.jpg")


**Neverending Story** - *Complete your ancestor's Legend after their death*  


Medium  

![image-28.jpg](https://forumcontent.paradoxplaza.com/public/1076755/image-28.jpg "image-28.jpg")


**Divine Right** - *Reach the maximum level of Legitimacy*  

![image-29.jpg](https://forumcontent.paradoxplaza.com/public/1076756/image-29.jpg "image-29.jpg")


**Canonized** - *Manage to make your Legend Protagonist a Saint*  

![image-30.jpg](https://forumcontent.paradoxplaza.com/public/1076757/image-30.jpg "image-30.jpg")


**Upward Mobility** - *Successfully claim your Liege's title while having a higher Legitimacy Level than them*  

![image-31.jpg](https://forumcontent.paradoxplaza.com/public/1076758/image-31.jpg "image-31.jpg")


**Local Legend** - *As a Count, complete a Mythical Legend*  


Hard  

![image-32.jpg](https://forumcontent.paradoxplaza.com/public/1076759/image-32.jpg "image-32.jpg")


**Not Today** - *Contract, and recover from, the Bubonic Plague*  

![image-33.jpg](https://forumcontent.paradoxplaza.com/public/1076760/image-33.jpg "image-33.jpg")


**The Pharaoh Islands** - *As a Scottish character, complete a Legend claiming your descent from Ancient Egypt*  


Very Hard  

![image-34.jpg](https://forumcontent.paradoxplaza.com/public/1076761/image-34.jpg "image-34.jpg")


**Can't Touch This** - *Have an infected Barony at the maximum Epidemic Resistance*  

---


Thank you all for reading! We hope you’re as excited as we are for the release of *Legends of the Dead* next Monday to kick off Chapter 3!

<!-- artifact:reactions:start -->
- 107 Like
- 75 Love
- 7 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)**
Role: Former Senior Programmer - Crusader Kings 3
Badges: 99
Reaction score: 8,575
<!-- artifact:op_signature:end -->
