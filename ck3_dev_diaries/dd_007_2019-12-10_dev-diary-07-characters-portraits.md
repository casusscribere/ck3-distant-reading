---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1295264/"
forum_thread_id: 1295264
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 7
title: "CK3 Dev Diary #07 - Characters & Portraits"
dd_date: 2019-12-10
author_handle: rageair
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1105
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1295264'
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
    location: raw_lines_~28_to_144
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_146_to_148
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_195_to_198
    action: preserved_and_flagged
    counts:
      Like: 4
      Love: 3
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_206_to_316
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_317_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #07 - Characters & Portraits

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Dec 10, 2019](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-07-characters-portraits.1295264/)
<!-- artifact:thread_metadata:end -->

Greetings!  

Today we’re taking a look at what makes up a character in CK3. As you already know, the game revolves around characters and all the things they get up to, so to make it interesting we have to make sure that they have as much personality as possible!  

To start off; each character still has skills and traits, just like in CK2. Their skills determine how well they can do different things, a character will high Diplomacy will be well-liked, while one with high Martial will excel as a commander. The main source of these skills are traits, the foremost of which is the Personality Traits.  

Unlike CK2, where personality traits were much like any other trait, we’ve decided to put more emphasis on the personality traits in CK3. In CK2 you could easily end up with 5-8 personality traits without much effort, but then what really defined you? It was hard to get a grip on who a character really was, something we’ve improved in CK3. Personality traits now have a massive effect on the behavior of each individual character, so when a character is Greedy you’ll really feel it. To emphasize this, characters tend to not have more than 3 personality traits so that you can at a quick glance tell who they are (other types of traits are of course still unlimited).  

![Personality_traits.png](https://forumcontent.paradoxplaza.com/public/518930/Personality_traits.png "Personality_traits.png")


*Personality Trait icons. Can you guess which one is which?*  

We’ve also added a feature where a character's personality is summed up in two words, which is then displayed in their character view. This is very useful when, for example, assigning vassals or getting agents. A ‘Rapacious Blackguard’ might not make for the most loyal vassal, but quite a good agent, while an ‘Honorable Empath’ would be the opposite!  

![character_portraits_01.jpg](https://forumcontent.paradoxplaza.com/public/518933/character_portraits_01.jpg "character_portraits_01.jpg")



Prestige and Piety remain in CK3, though with a new element to them. In CK2, you accumulated prestige that you then spent on various things - this rarely made much sense, why would launching an invasion suddenly make everyone like you less, for example? Therefore we’ve decided to split the currency part of prestige/piety from the perception part. In CK3, all prestige and piety accumulated by a character will contribute towards their Level of Fame/Devotion. These have various effects, for example, your Level of Fame increases the opinion of all secular rulers (as it did in CK2), give your more Knights, and unlocks special interactions - such as invasions should you be Tribal. Your Level of Devotion increases the opinion of the clergy and allows you to declare better Holy Wars among other things. These levels range between 0-5, with 0 representing disgrace. Instead of only losing prestige when doing truly dishonorable things, such as breaking a truce, you now also lose Levels of Fame, making the whole thing more of a hard choice. Accumulated prestige and piety can be used for various things as a currency, just like in CK2, prestige being used for vassal interactions, decisions, and war, while piety is the primary resource used when interacting with the church.  

![Exalted.png](https://forumcontent.paradoxplaza.com/public/518931/Exalted.png "Exalted.png")



Before moving on to the Portraits themselves, I’d like to mention genetic traits! Traits such as Strong and Genius were much sought-after in CK2, and you often went out of your way to breed those traits into your direct line. In CK3 this is even more involved, with genetic traits having multiple levels that you can improve with successive generations (which can be sped up by inbreeding!), and there’s also more of them. Genetic traits will often have a visual effect on your portrait - the Beautiful line of traits will make your characters more-and-more symmetrical, for example. On the negative end of the spectrum, we have traits such as Ugly or Albino, which will *reduce* symmetry or alter your character's skin tone respectively (the Middle Ages were full of prejudice).  

Now, without further ado, let's move on to the Portrait section, hosted by our very own portrait artist, Nils!  

So, when it comes to the visual presentation of characters in the game, we've chosen to switch out the 2D "paperdoll" style portraits of CK2 for full animated 3D characters in CK3. While the portraits in CK2 undeniably have their charm, going 3D just gives us so many more possibilities for all kinds of dynamic features.  

Every character has a DNA in which their appearance is defined. Each facial feature that we can control has its own gene. And there's a great number of those to give us a lot of variations and an endless amount of possible faces. For example, the nose alone has over 10 different parameters that define its shape. Compared to just one in CK2.  

Another thing we wanted to change is how much of the character we display in the UI. This is, of course, the middle ages we are talking about, where a person's clothes are a more important indicator of who they are than even their facial features. So it made sense to show more of the body than just head and shoulders. How fancy and expensive a character’s clothing looks will give you as player information about their rank. The larger frame also allows us to show different animated poses, and as Alex mentioned above they give a hint of the character’s personality. Additionally, we can do more with body types as well. Characters have different heights (yes including dwarfism and gigantism) as well as different weights and body composition, something that is affected by their lifestyle and traits. So if your character is a gluttonous hedonist, chances are they will have a body rather on the stout side of things while if they are a legendary warrior their pecs and deltoids will also likely be of the legendary variety.  

![character_portraits_02.jpg](https://forumcontent.paradoxplaza.com/public/518932/character_portraits_02.jpg "character_portraits_02.jpg")



Other cool features that the 3D system allows us to do is seamless aging and disease overlays. Now you can see your toddler gradually change into an adult and eventually (barring any unforeseen incidents...) to an elderly 100-year old. Should your character, heavens forbid, catch a serious illness their appearance will reflect that with suitably repulsive skin texture overlays.  

We will have a more in-depth look at the portraits in a future dev diary, so stay tuned for that!

<!-- artifact:reactions:start -->
- 4 Like
- 3 Love
- 2 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 48 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
