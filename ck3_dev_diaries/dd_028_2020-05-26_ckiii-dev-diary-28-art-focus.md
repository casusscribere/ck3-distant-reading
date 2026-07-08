---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1393627/"
forum_thread_id: 1393627
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 28
title: "CKIII Dev Diary #28 - Art Focus"
dd_date: 2020-05-26
author_handle: Carlberg
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2557
inline_image_count: 25
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1393627'
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
    location: raw_lines_~28_to_142
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_141
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1388.jpg?1590496755
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_144_to_146
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_387_to_391
    action: preserved_and_flagged
    counts:
      Love: 175
      Like: 142
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_399_to_509
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_510_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1388.jpg?1590496755)
<!-- artifact:thread_banner:end -->

# CKIII Dev Diary #28 - Art Focus

<!-- artifact:thread_metadata:start -->
- Thread starter [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)
- Start date [May 26, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ckiii-dev-diary-28-art-focus.1393627/)
<!-- artifact:thread_metadata:end -->

> **Hello my name is Joacim, Art Lead on Crusader Kings 3, I am positing here a developer diary written by Pontus, Art Director on Crusader Kings 3, currently on paternity leave. Our artists will reply to your questions in the comments!**
>
> Click to expand...


**Art Focus**  
Hey! Let’s talk about the art of Crusader Kings III!  

My name is Pontus, Art Director on CK3. I’ve written this dev diary together with the art team, and if you promise to tell everyone this is the best dev diary so far, there will be some sweet wallpapers at the end of it. Cool?  

Certainly, you’ve seen a lot of the art already, in various states of completion, with all our diaries and previews. Let’s start by talking about the way we’ve approached creating the graphics for the game!  

The starting point for the art direction is, as it should be, the game design. If you recall Dev Diary #0, Henrik Fåhreus’ vision of the game has a big focus on characters and storytelling, as well as approachability and player freedom. Reinforcing that through the art has been the main goal.  

To keep ourselves on-track, three key pillars guide the art department on CK3:  

**A ROLE-PLAYING EXPERIENCE -** This pillar is represented by our goal to give life to the characters and their unfolding stories. An example of this would be the characters’ portraits, we did not want them small and static, they are now front and center, and show off their standing or lack thereof through clothing, as well as show how they feel about what is happening to them through body language.  

![DD28_king_01.jpg](https://forumcontent.paradoxplaza.com/public/569117/DD28_king_01.jpg "DD28_king_01.jpg")

![DD28_king_02.jpg](https://forumcontent.paradoxplaza.com/public/569118/DD28_king_02.jpg "DD28_king_02.jpg")



**A MEDIEVAL GAME -** We made a great effort to keep a good level of historical accuracy in our designs. Our illustrations and icons are made to reflect the time period, just like the 3D art that populate the map. Of course, sometimes we had to try and find good compromises in the designs that would work for the entire timespan of the game.  

Where possible, we based clothes on reconstructed sewing patterns from extant medieval clothing. For example, we recreated the "coronation tunic" of Roger II of Sicily, a well preserved garment from the 1130s (though it was actually made some time after the coronation).  

![DD28_tunic_comp.jpg](https://forumcontent.paradoxplaza.com/public/569119/DD28_tunic_comp.jpg "DD28_tunic_comp.jpg")



Another example would be a loading screen with some really well-painted sunflowers, but these did not exist in europe until the 16th century, which was spotted in time thanks to our Beta testers: so we sent it back to get the flowers repainted…  

**A ROUGH WORLD -** Crusader Kings is not a game for all-ages, you live dangerously and people do terrible, terrible things to each other. This is reflected in the more somber palette and overall mood of the game.  

Now, let’s talk about the different types of art you’ll have fun with in CK3:  

**CHARACTERS**  
I’m very excited about our new character portraits, and what we can do with them visually. They are varied and have lots of, well, character. Every day there’s a screenshot shared in the dev chat featuring someone they’ve encountered in-game, and we usually agree, yes, that person wears that hat better than most, or indeed, he looks just like the poster boy for the Deviant trait.  

For me, the real test for the characters is if they make you feel, and It IS satisfying to throw especially smug-looking Rivals into your Dungeon, and you might feel a bit sorry for some harmless looking characters before you plot to have someone deliver poisonous snakes upon them.  

I really want to stress the fantastic work our Lead Character Artist Nils Wadensten and the character team have done in bringing this new generation of portraits to our games, alongside our Engine team.  

In fact, he’ll go into the character portraits a bit more in a future diary, hopefully he won’t show the first iterations of the wounds and diseases, some were a bit too much for a lot of people.. ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")  

For now, I’ll leave you with a sneak peek of Concept art and the final piece of Clothing as how it appears in the game.  

![DD28_steppe.jpg](https://forumcontent.paradoxplaza.com/public/569122/DD28_steppe.jpg "DD28_steppe.jpg")

![DD28_african_pagan.jpg](https://forumcontent.paradoxplaza.com/public/569123/DD28_african_pagan.jpg "DD28_african_pagan.jpg")



**ANIMATION**  
Making the characters move was quite a challenge since the movements need to be very discreet, and not call too much attention to themselves as that could become a distraction from the gameplay.  

The posing and idle animations are there to help the immersion and storytelling. Keeping the Rough World pillar in mind, they should not be silly and slapstick - while CK has some wonderful dark humor, we play it straight. I do think the look on a character's face when he realises they are locked up together with a Cannibal is appropriately shocked though.  

Generally the characters have a pose that reflects their personality or the situation they’re in.  

[https://www.youtube.com/embed/mSxOlwHUhtU?wmode=opaque](https://www.youtube.com/embed/mSxOlwHUhtU?wmode=opaque)

[https://www.youtube.com/embed/BZy_WDGkqqc?wmode=opaque](https://www.youtube.com/embed/BZy_WDGkqqc?wmode=opaque)


**EVENTS**  
Here is where the role-playing really kicks in. When an event pops up, we showcase the characters involved and how they feel about the current proceedings, set against a backdrop that really helps sell the setting. This means if you encounter the same event in another play-through, the visuals might be quite different due to the characters involved.  

The backdrops have a detailed but hand-painted style that complements our stylized characters’ well. In fact, we have some for you as wallpapers without text, icons and characters obscuring them, enjoy.  

When we create a new event background, we also do a hand-crafted lighting setup, which relights the portraits to fit the current scene:  

![DD28_events_01.jpg](https://forumcontent.paradoxplaza.com/public/569126/DD28_events_01.jpg "DD28_events_01.jpg")

![DD28_events_02.jpg](https://forumcontent.paradoxplaza.com/public/569127/DD28_events_02.jpg "DD28_events_02.jpg")

![DD28_events_03.jpg](https://forumcontent.paradoxplaza.com/public/569128/DD28_events_03.jpg "DD28_events_03.jpg")

![DD28_events_04.jpg](https://forumcontent.paradoxplaza.com/public/569129/DD28_events_04.jpg "DD28_events_04.jpg")



**ILLUSTRATIONS**  
Besides the events, there’s plenty of illustrations in CK3!  

For the loading screens, we wanted someone who can do images full of mood and storytelling, in a rough, painterly style. We went straight for the top and asked Craig Mullins. Fortunately, he was up for it, and has provided some really exciting imagery.  

They all are of course showcasing aspects of the Crusader Kings experience- from Templars in battle to babies in peril!  

Besides the loading screens and event backgrounds, we have cool paintings for Decision categories, terrain types, holdings, army movements, legacies… heck, our Personality trait icons and Tenets are small illustrations - there is a lot to discover and keep you entertained and immersed!  

![DD28_hunt_text.jpg](https://forumcontent.paradoxplaza.com/public/569144/DD28_hunt_text.jpg "DD28_hunt_text.jpg")



The Holding Illustrations make for great wallpapers as well, so we included that in our art drop!  

**UNITS**  
Our units are really cool! We were very enthusiastic about these, and really added quite a bit of detail. Let us know if you spot the nails that stick the shield handle into the shield at the back.  

The units’ appearance is based on culture - We have Western European, Byzantine, Middle-east / North Africa, Pagans, Indian and Turko-Mongol.  

A unit has three visual tiers, becoming more armor-clad and sophisticated as it progresses. So it was important for us to make sure a Tier 2 Byzantine looks equally as tough as a Tier 2 Turko-Mongol for instance.  

They have a lot of spark to them as we added a lot of different animations, they cheer when they win, bang their shields during sieges and we make use of red liquid particles when they land some nice hits.  

Culture, Tiers and Coat-of-arms colors and emblems make the Units look appropriate and unique. Here’s some examples:  

![DD28_units.png](https://forumcontent.paradoxplaza.com/public/569130/DD28_units.png "DD28_units.png")


[https://www.youtube.com/embed/opj-w5cqA5k?wmode=opaque](https://www.youtube.com/embed/opj-w5cqA5k?wmode=opaque)

[https://www.youtube.com/embed/kn0uSVscPLg?wmode=opaque](https://www.youtube.com/embed/kn0uSVscPLg?wmode=opaque)



**HOLDINGS**  
The Holdings were quite a challenge, they needed to be a certain size based on maximum zoom level and minimum Barony size. Since they are small they need to have strong, readable shapes without looking like toys.  

Their appearances are influenced by the region they are found in, in this case Western European, Mediterranean, India and Middle-east.  

Similar to Units, they have visual tiers, tied to the Holding’s Upgrade level. Temples and Cities have two tiers, whereas Castles and Walls have four tiers.  

Of course, we have primitive huts as well, and a big bunch of unique buildings, some easier to recreate (Pyramids) than others (Charlemagne's Palace).  

![DD28_western_castles.png](https://forumcontent.paradoxplaza.com/public/569134/DD28_western_castles.png "DD28_western_castles.png")

![DD28_mena_castles.png](https://forumcontent.paradoxplaza.com/public/569135/DD28_mena_castles.png "DD28_mena_castles.png")


![DD28_special_01.png](https://forumcontent.paradoxplaza.com/public/569138/DD28_special_01.png "DD28_special_01.png")

![DD28_special_02.png](https://forumcontent.paradoxplaza.com/public/569139/DD28_special_02.png "DD28_special_02.png")




**MAP**  
There’s a rumor going around that some of you CK2 players rarely look at the terrain map. We didn’t want that for CK3, so we made our map to not only be moody and pretty to look at, but also more useful, so you’d have more reasons to go there.  

CK is information heavy, so we try to make sure that everything in the terrain map serves a function, and is easy to see. Thus a cleaner look, to make sure the icons, borders, text and 3D models that sit on top of the land read well. At a glance, you should be able to see what terrain type a Barony has without consulting another map mode.  

![DD28_map_02.png](https://forumcontent.paradoxplaza.com/public/569141/DD28_map_02.png "DD28_map_02.png")

![DD28_map_03.png](https://forumcontent.paradoxplaza.com/public/569142/DD28_map_03.png "DD28_map_03.png")

![DD28_map_01.png](https://forumcontent.paradoxplaza.com/public/569143/DD28_map_01.png "DD28_map_01.png")



If you are into Political Map modes though, don’t worry, we’ve got you covered. You’ll notice it feels familiar.  

It seems our Paper map has been received well, we’re glad you like lobsters too! Getting the right amount of sea-monsters without making it look cluttered wasn’t easy, but I think we managed in the end.  

![DD28_papermap.png](https://forumcontent.paradoxplaza.com/public/569140/DD28_papermap.png "DD28_papermap.png")



**UI**  
A PDS game has a lot of UI. It is something made in close collaboration with UX and Game Design departments. It is constantly iterated upon and is one of the most challenging aspects of our games.  
Visually we took inspiration from game design’s character focus pillar and pulled in visual influences from Roleplaying games. To make it approachable we tried to keep it clean, and give everything some breathing room.  

![DD28_Character_Screen.png](https://forumcontent.paradoxplaza.com/public/569145/DD28_Character_Screen.png "DD28_Character_Screen.png")

![DD28_MAA.jpg](https://forumcontent.paradoxplaza.com/public/569146/DD28_MAA.jpg "DD28_MAA.jpg")



![DD28_letter.jpg](https://forumcontent.paradoxplaza.com/public/569148/DD28_letter.jpg "DD28_letter.jpg")



We use a lot of illustrations in our UI’s to help immersion and flavor, and we have a cool system where some of the image types are context sensitive, so for instance your Sultan will not stand in front of a western European throne room if he is hanging out in the Middle-east, and if you are dealing with Catholicism in Religion View, well you’ll see churches and similar imagery.  


**Coats of Arms**  
Heraldry is essential to the medieval immersion of Crusader Kings, and so heralds will be excited to hear that we have totally overhauled the Coat of Arms system.  

We started from scratch, poring over history books and contemporary armorials to ensure every detail is authentic. We designed accurate CoA for over a thousand titles and dynasties to complement a new scriptable random system that weights hundreds of unique elements based on culture, religion, and everything in between. We modeled minute differences across regions, so frequencies of designs and tinctures are different in Germany, France, and Spain. The amount of possible combinations? Millions.  

We achieved our primary goal of making our feudal European heraldry as accurate as possible, but we didn't stop there—we wanted to go into extra depth for all regions. For example, the eastern hordes decorate the Great Steppe with their special tamgha emblems, while the Islamic world is fleshed out with immersive Saracenic heraldry (no more endless stars and crescents). Emergent cadet houses differentiate their new arms by quartering, and yes, England's coat of arms will change if William wins the Norman Invasion.  

Here’s some examples of the heraldry system in action - firstly how England’s arms can react to gameplay, and secondly a selection of randomly-generated COA from around the world.  

![DD28_COA_1.png](https://forumcontent.paradoxplaza.com/public/569149/DD28_COA_1.png "DD28_COA_1.png")

![DD28_COA_2.png](https://forumcontent.paradoxplaza.com/public/569150/DD28_COA_2.png "DD28_COA_2.png")



**In summary:**  

The art team has worked very hard and it is a delight every day to see whatever new stuff is coming in. Making games is a group effort though, so we get invaluable help and feedback from the rest of the team: code, design, QA, sound, production all contribute as well.  

Of course, seeing pictures in a dev diary is one thing, we can’t wait for you to get your hands on the full experience! As always, your feedback will help guide us as we continue to make content and improvements for CK3!  

And for being good sports and reaching the end of the dev diary, here's links to some sweet wallpapers!  


<http://forumcontent.paradoxplaza.com/public/paradox/banners/ck3-wallpapers.zip>

<http://forumcontent.paradoxplaza.com/public/paradox/banners/ck3-map-wallpapers.zip>

 

#### Attachments

- [[https://forumcontent.paradoxplaza.com/data/video/569/569124-709db9167cc4d8f198515dec2faf5e20.mp4](https://forumcontent.paradoxplaza.com/data/video/569/569124-709db9167cc4d8f198515dec2faf5e20.mp4)](https://forumcontent.paradoxplaza.com/data/video/569/569124-709db9167cc4d8f198515dec2faf5e20.mp4)
  
  DD28_council.mp4
  8,9 MB

- [[https://forumcontent.paradoxplaza.com/data/video/569/569125-aa1124e54b7a2cf847d58754a4349b83.mp4](https://forumcontent.paradoxplaza.com/data/video/569/569125-aa1124e54b7a2cf847d58754a4349b83.mp4)](https://forumcontent.paradoxplaza.com/data/video/569/569125-aa1124e54b7a2cf847d58754a4349b83.mp4)
  
  DD28_event.mp4
  9,5 MB

- [[https://forumcontent.paradoxplaza.com/data/video/569/569131-0d23c3f89ac347c6032780ec281074ce.mp4](https://forumcontent.paradoxplaza.com/data/video/569/569131-0d23c3f89ac347c6032780ec281074ce.mp4)](https://forumcontent.paradoxplaza.com/data/video/569/569131-0d23c3f89ac347c6032780ec281074ce.mp4)
  
  DD28_combat_vid_1.mp4
  18,7 MB

- [[https://forumcontent.paradoxplaza.com/data/video/569/569133-684b5271f9663aba4e805649d32ddff1.mp4](https://forumcontent.paradoxplaza.com/data/video/569/569133-684b5271f9663aba4e805649d32ddff1.mp4)](https://forumcontent.paradoxplaza.com/data/video/569/569133-684b5271f9663aba4e805649d32ddff1.mp4)
  
  DD28_combat_vid_2.mp4
  19,2 MB

- [![DD28_western_castles.png](https://forumcontent.paradoxplaza.com/thumbnail/public/569136/DD28_western_castles.png)](https://forum.paradoxplaza.com/forum/attachments/dd28_western_castles-png.581777/)
  
  DD28_western_castles.png
  1 MB

 · Views: 0

Last edited: May 26, 2020

<!-- artifact:reactions:start -->
- 175 Love
- 142 Like
- 20 (unlabeled — rendered as base64 data URI)
- 9 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Carlberg](https://forum.paradoxplaza.com/forum/members/carlberg.940169/)**
Role: Senior Environment Artist
Badges: 40
Messages: 221
Reaction score: 2,288

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
