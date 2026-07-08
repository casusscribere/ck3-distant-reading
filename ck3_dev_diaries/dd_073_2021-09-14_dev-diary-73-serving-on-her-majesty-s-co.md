---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1490806/"
forum_thread_id: 1490806
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 73
title: "CK3 Dev Diary #73 - Serving On Her Majesty's Court"
dd_date: 2021-09-14
author_handle: Servancour
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1074
inline_image_count: 8
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1490806'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1704.jpg?1631622762
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_231_to_235
    action: preserved_and_flagged
    counts:
      Like: 159
      Love: 88
      (unlabeled — rendered as base64 data URI): 8
      Haha: 3
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_243_to_352
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_353_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1704.jpg?1631622762)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #73 - Serving On Her Majesty's Court

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Sep 14, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-73-serving-on-her-majestys-court.1490806/)
<!-- artifact:thread_metadata:end -->

Greetings!  

In the update that will launch alongside the *Royal Court* expansion, we will introduce Court Positions - which can be seen as an evolution of CK2’s Minor Titles with a number of new improvements. While the old feature from CK2 had all sorts of various honorary titles, we wanted to focus on the most important positions at your court. Jobs that are relevant directly to you as a ruler, or that of your court.  

Court Positions include a number of different positions, such as a Court Tutor, or Seneschal. Most positions imply that the appointed character has an actual job at your court and provides you with their services. That doesn’t mean we haven’t added any of the classical honorary positions though. Expect to also be able to appoint a Master of the Hunt, Master of the Horse, or (if you are playing as England) a Keeper of the Swans.  

Each position will provide you with a set of bonuses, mostly in the form of various modifiers, but certain positions have more interesting benefits as well. For example, a Court Tutor increases the chances for children at your court to receive a better education trait.  

Not all characters are equally fit to serve in any given position. Their skills and traits have a significant impact on how good they are at their job. This is reflected in their Aptitude. A position uses one or several skills, such as Learning for a Court Physician, which is the main factor for what Aptitude a character will have. Each position also has a number of traits that may increase (or even decrease!) their Aptitude further. Aptitude is measured on a scale in five steps, ranging from ‘terrible’ to ‘excellent’. The higher the Aptitude is, the greater the benefit. Let’s look at the Seneschal as an example. A character with the lowest Aptitude will only grant you a Control Growth bonus of +0.1, while a character with the highest possible Aptitude will give you +0.5.  

![01_aptitude.jpg](https://forumcontent.paradoxplaza.com/public/743719/01_aptitude.jpg "01_aptitude.jpg")


*[Image showing the Aptitude for a court position]*​


Unlike CK2, hiring a character for a position is actually going to cost you, as each Court Position has an associated salary that you will be paying for out of your own pocket. While the salary for any given position won’t be very expensive, they will stack up. You’ll have to make a decision on how much gold you are willing to spend on all of your appointed positions, and if the characters you have available are skilled enough to warrant the salary.  

As you may remember from [Summer Teaser #3](https://forum.paradoxplaza.com/forum/threads/ck3-summer-teaser-3.1483461/), we’ve gone through several old events to make sure that if you have someone appointed in a relevant position, they can appear to provide extra options or affect an outcome to be more favourable. Additionally, some positions may appear in events related to schemes. We’ve also added Cultural Traditions that increase the Aptitude of specific positions for characters of that culture, or even unlock a position you normally wouldn’t have access to! The goal is to make sure that Court Positions feel like an integral part of the game, and to have them feel as immersive as possible.  

Before we wrap up, let’s take a look at a few examples of what some of the different Court Positions can do for you.  

The Court Physician has been updated to be a fully fledged Court Position and make use of the new system. As you’d expect, the appointed character will take care of the sick people within your court. Court Physicians have a lower salary than most, so you should in practice always be able to afford one. If you have the Royal Court expansion, having a Court Physician also provides you with a small bonus to your grandeur. A skilled physician was often seen as very prestigious after all.  

![02_court_physician.jpg](https://forumcontent.paradoxplaza.com/public/743720/02_court_physician.jpg "02_court_physician.jpg")


[Image of the Court Physician Court Position]​


Next is the Bodyguard. You can hire up to two Bodyguards at the same time. Bodyguards don’t provide any passive modifiers like most other positions, but do have two fairly powerful bonuses. They have a chance to prevent assassination attempts on you, and they reduce the risks of participating in battles, as long as both of you partake in the same battle. So make sure that your Bodyguards have been appointed as your knights to make the most use of them. But beware! Bodyguards are very powerful agents should they join a scheme against you. Keep an eye on their opinion to avoid any backstabbing shenanigans!  

*![03_bodyguard.jpg](https://forumcontent.paradoxplaza.com/public/743721/03_bodyguard.jpg "03_bodyguard.jpg")


[Image of the Bodyguard Court Position]*​


Another interesting position is the Food Taster. Any self-respecting (and perhaps paranoid) ruler should have one. A Food Taster not only gives you some protection against hostile schemes, they may even prevent a poison-related murder attempt against you! By, of course, eating your food and dying in your place… Just like a Bodyguard, a Food Taster is also a powerful agent should they join in on a scheme against you.  

*![04_food_taster.jpg](https://forumcontent.paradoxplaza.com/public/743722/04_food_taster.jpg "04_food_taster.jpg")


[Image of the Food Taster Court Position]*​


Let’s take a look at the Court Gardener. This court position is unlocked by a cultural tradition - Garden Architects. Gardeners provide a passive opinion bonus for your courtiers and guests (who doesn’t appreciate a well tended garden?), and depending on their skill, a significant bonus to the Development Growth in your realm capital.  

*![05_court_gardener.jpg](https://forumcontent.paradoxplaza.com/public/743723/05_court_gardener.jpg "05_court_gardener.jpg")


[Image of the Court Gardener Court Position]*​


And for reference, this is what the tradition looks like:  

*![06_garden_architects.jpg](https://forumcontent.paradoxplaza.com/public/743724/06_garden_architects.jpg "06_garden_architects.jpg")


[Image of the Garden Architects tradition]*​


Finally, we couldn’t show off Court Positions without showing the Court Jester, complete with a jester’s outfit!  

*![07_court_jester.jpg](https://forumcontent.paradoxplaza.com/public/743725/07_court_jester.jpg "07_court_jester.jpg")


[Image of the Court Jester Court Positions]  

![08_jester_clothing.png](https://forumcontent.paradoxplaza.com/public/743726/08_jester_clothing.png "08_jester_clothing.png")


[Image of the Court Jester's clothing]*​


That’s it for today!

<!-- artifact:reactions:start -->
- 159 Like
- 88 Love
- 14 (unlabeled — rendered as base64 data URI)
- 8 (unlabeled — rendered as base64 data URI)
- 3 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)**
Role: Game Designer
Badges: 4
Reaction score: 9,949

*[Full game-badge icon list of 49 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
