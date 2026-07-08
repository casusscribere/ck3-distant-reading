---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1571227/"
forum_thread_id: 1571227
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 117
title: "Dev Diary #117 - Shave and a Map Mode"
dd_date: 2023-02-28
author_handle: PDX Jens
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1198
inline_image_count: 8
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1571227'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2214.jpg?1677584349
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_245_to_250
    action: preserved_and_flagged
    counts:
      Like: 151
      Love: 59
      (unlabeled — rendered as base64 data URI): 10
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_258_to_368
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_369_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2214.jpg?1677584349)
<!-- artifact:thread_banner:end -->

# Dev Diary #117 - Shave and a Map Mode

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX Jens](https://forum.paradoxplaza.com/forum/members/pdx-jens.1725938/)
- Start date [Feb 28, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-117-shave-and-a-map-mode.1571227/)
<!-- artifact:thread_metadata:end -->

Hello everyone!  

My name is Jens and this is my first appearance on this forum. I’ve got the opportunity to share some details with you on my probation project for CK3, which is making it all the way into the upcoming release (because that’s where I pushed my changes, lol)!  

I’m happy at least [one of you](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-116-agrarian-research-techniques.1569914/page-21#post-28791283) caught on to the subtle hint in the previous DD. I was like “Wokeg, did you use my new thing to set up the screenshots?” Well yes, because all of a sudden most assets and characters have become way more accessible. So what is it I’m talking about? At this point, most of you have probably guessed it - but yes, we have upgraded our old friend the Barbershop.  

I’ve scrambled through the webs looking for feedback and wishes of what you would like and expect from such a tool. Heck, no mediocre fix would do: I want only the best for you! I distilled the info down, looking for the essence of how you’d want to use the tool, set up the tasks, prioritized them, and spent the last few weeks going through them all. Well, I’ll spare you the fluff. Let’s get into some details.  

First off, we have expanded the Barbershop into two tabs. The first is focused on changing the appearance of your character. Additionally, I’ve added a fuzzy search box next to the drop downs, in case you already know the name of what you’re looking for.  

![barbershop1.png](https://forumcontent.paradoxplaza.com/public/939132/barbershop1.png "barbershop1.png")


*[Image: Barbershop, tab for changing appearance]*  


In the second tab, we’ve added drag and drop support for the portraits, so you may click, drag and place them wherever you want. You can also rotate them 360 degrees and we’ve also got 4 different zoom levels for you to play around with. Every character has their own dropdown of poses and animations and we’ve also added a wide variety of backgrounds. The only limit now is your own imagination.  

![barbershop2.png](https://forumcontent.paradoxplaza.com/public/939133/barbershop2.png "barbershop2.png")


*[Image: Barbershop, tab for placing characters in the scene]*  


One of the big reasons we play is to create stories and make memories. I took a deep dive into the forum history and found out some of you want to use the Barbershop to relive past events between characters, dress up a serious ruler in a funny outfit or take family photos. To support this I’ve added presets. The “Custom” preset lets you import characters simply by pinning them. Another preset I really wanted in (based on a comment) was an easy way to view your entire Council, so for that end I present to you:  

![barbershop3.png](https://forumcontent.paradoxplaza.com/public/939134/barbershop3.png "barbershop3.png")


*[Image: Barbershop, easily view your council]*  


Also, note the council preset supports modding if that’s your thing.  

![barbershop-script.png](https://forumcontent.paradoxplaza.com/public/939135/barbershop-script.png "barbershop-script.png")


*[Image: Barbershop script]*  


With only a few polish tasks left, people have already begun discovering this tool in-house and started trolling and meme-ing each other. I hope you guys will enjoy the new Barbershop as much as we do. Let me know if you have any last minute requests and I will see what I can do. Now [@rageair](https://forum.paradoxplaza.com/forum/members/375731/) also has something in store for you.  




---  

Greetings! In addition to the above we also want to show some additions to our collection of Map Modes - namely the introduction of the Control and Economy map modes! These two new tools are very useful in managing your realm… and planning your conquests.  

![map-modes.png](https://forumcontent.paradoxplaza.com/public/939136/map-modes.png "map-modes.png")


*[Image - New Map Mode Buttons]*  


The Control map mode is very straightforward, showing you exactly what you’d expect. It spans from a dark purple (denoting very low control) to a light yellow (showing just a slight lack of control), and a bright white shows where there’s Absolute Control.  

![control-map.png](https://forumcontent.paradoxplaza.com/public/939140/control-map.png "control-map.png")


*[Image: Control Map mode Example]*  


The Economy map mode is a little bit less straightforward - but we aspired to make it as useful as possible. The nebulous concept of ‘economy’ is a bit harder to represent, but we decided to include what most of us thought were key factors in making informed decisions.  

![econ-map-france.png](https://forumcontent.paradoxplaza.com/public/939143/econ-map-france.png "econ-map-france.png")


*[Image: Economy Map mode Example, Southern France]*  


Similar to the Development Map mode, the color spans from dark purple to bright yellow; bright yellow indicates an area is quite rich. The area colors are based on Counties, including income from Cities, Bishoprics, and so on - for an overall approximation of the County’s use to the player (of course, Counties with more Castles might be better in the eyes of some, but we had to make a call and thought that this was the most useful overall). This coloring is relative to the state of the world, meaning that the most brilliant yellow County is the richest one in the world at that moment. This map mode doesn’t care about the current Control Level of the County, which makes it useful for planning conquest targets.  

![econ-map-india.png](https://forumcontent.paradoxplaza.com/public/939144/econ-map-india.png "econ-map-india.png")


*[Image: Economy map mode, showing India]*  


Something else that you no-doubt notice is that Special Buildings are shown on this map mode! They’ve been hidden away for much too long, and we decided that this was an excellent time to reveal them… and maybe add a handful of new ones. Getting Special Buildings in your domain was always a fun goal for the player to achieve, and now it’s not only possible to see where they are - but also whether you can use them, if they are already built, what they provide, and so on!  

As an added bonus, we’ve added an absolute ton of new mines strewn around the map, and we’ve also revised the system for founding Universities - now it’s no longer a decision, but rather the institutions are constructed as normal special buildings (and in many more places than before!), with the same rewards on offer.  

This means that there are many, many more great capital locations strewn across the world, and it’s now easier than ever to find them!  

---  

That’s it for this time! But stay tuned… our spymaster sends word that what’s next for Crusader Kings III will soon be announced! Make sure to mark Monday next week, March 6th, in your calendars and visit [this link](https://pdxint.at/pdxannounce2023)!  

[https://www.youtube.com/embed/HCbJZqnuNYg?wmode=opaque](https://www.youtube.com/embed/HCbJZqnuNYg?wmode=opaque)

<!-- artifact:reactions:start -->
- 151 Like
- 59 Love
- 19 (unlabeled — rendered as base64 data URI)
- 12 (unlabeled — rendered as base64 data URI)
- 10 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX Jens](https://forum.paradoxplaza.com/forum/members/pdx-jens.1725938/)**
Role: Recruit
Badges: 72
Messages: 8
Reaction score: 508

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
