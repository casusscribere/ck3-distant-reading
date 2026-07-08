---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1399764/"
forum_thread_id: 1399764
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 31
title: "CK3 Dev Diary #31 - A Stressful Situation"
dd_date: 2020-06-16
author_handle: Baron von Shoes
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1173
inline_image_count: 8
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1399764'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1405.jpg?1592309852
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_145_to_147
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_229_to_233
    action: preserved_and_flagged
    counts:
      Like: 188
      Love: 84
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_241_to_337
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_338_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1405.jpg?1592309852)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #31 - A Stressful Situation

<!-- artifact:thread_metadata:start -->
- Thread starter [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)
- Start date [Jun 16, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-31-a-stressful-situation.1399764/)
<!-- artifact:thread_metadata:end -->

**Dev Diary #31 - A Stressful Situation**  
Hello everyone! I come to you today with the long-awaited Dev Diary on how Stress works in Crusader Kings III! While the system is relatively straightforward, it does have some rather far-reaching ramifications for how characters choose to behave, so let us dive right in!  

**Stress**  
Stress is a representation of a character’s mental well-being. As characters accumulate Stress, they will increase up their Stress Level, with each level causing increasing penalties to their health and fertility values. The penalties at Stress Level 1 are fairly minor, but the penalties at Stress Level 3 can lead your character to an early grave!  

![image7.jpg](https://forumcontent.paradoxplaza.com/public/577902/image7.jpg "image7.jpg")


[A screenshot showing the player character with nearly-maxed out Stress]  

The primary way that characters gain Stress is when the demands of the realm force them to take actions which go against their nature. For example, a Compassionate character will gain Stress for executing prisoners in the dungeon, even if those prisoners were traitorous rebels or, ahem… inconveniently positioned in the line of succession.  

![image4.jpg](https://forumcontent.paradoxplaza.com/public/577903/image4.jpg "image4.jpg")


[A screenshot showing a Compassionate character gaining 42 Stress for executing a prisoner]  

There are other sources of Stress too, though. Being locked up in the dungeon of another character will gradually increase Stress over time, as the isolation and neglect take their toll on your psyche. Other causes include overwork or the death of a loved one. Regardless of the source, once a character accumulates enough Stress to pass a certain threshold and gain a Stress Level, they will suffer from a Mental Break.  

**Mental Breaks**  

Mental Breaks are a special kind of event which occurs when Stress overwhelms a character and compels them to do something — anything — to gain relief. Exactly what type of Mental Break a character has depends heavily on their personality traits, and each one gives the character several options for dealing with the situation they have found themselves in.  

![image3.jpg](https://forumcontent.paradoxplaza.com/public/577904/image3.jpg "image3.jpg")


[A screenshot showing the player character suffering from overwhelming guilt and shame as part of a Mental Break]  

Not all Mental Breaks are equal, and the severity of the Mental Break will depend on your Stress Level when the event occurs. A Level 1 Mental Break may cause a Wrathful character to yell at one of their vassals in front of the whole court, insulting them and wounding their pride… but a Tier 3 Mental Break may instead drive that same character to murder their chosen heir in a fit of rage!  

In addition to differing by Stress Level, some Mental Breaks are influenced by the situation you find yourself in. As an example, characters who are locked up in a dungeon cell will suffering from completely different Mental Breaks (often of greater severity), some of which can radically change their personality.  

![image6.jpg](https://forumcontent.paradoxplaza.com/public/577905/image6.jpg "image6.jpg")


[A screenshot showing the player character swearing vengeance on their enemies from prison]  

Regardless of what kind of Mental Break they suffer from, all Mental Breaks give the afflicted character the opportunity to lose a large amount of Stress. Many of these options will also grant the afflicted character a Coping Mechanism trait, which will help them relieve stress in the future and thus reduce the likelihood of having additional Mental Breaks.  

**Coping Mechanisms**  
Coping Mechanisms are traits that represent the long-term methods characters have developed to deal with the Stress of their life. Most of them impose some form of minor penalty on a character’s skills, but in exchange they will enhance the potency of all forms of stress loss.  

![image2.jpg](https://forumcontent.paradoxplaza.com/public/577906/image2.jpg "image2.jpg")


[A screenshot showing a selection of 4 Coping Mechanism traits: Rakish, Drunkard, Flagellant, and Comfort Eater]  

In addition to the passive effects of each trait, each one also enables a unique Decision characters can take to indulge in their vice and relieve a portion of their accumulated stress.  

![image1.jpg](https://forumcontent.paradoxplaza.com/public/577908/image1.jpg "image1.jpg")


[A screenshot showing the Decision to visit a brothel and lose stress]  

Regardless of the form it takes, all Coping Mechanisms are useful in one form or another. Having the ability to make Stressful decisions at-will is often more useful than a few extra points of Diplomacy or Stewardship, and each Coping Mechanism a character acquires makes it progressively easier for them to manage their Stress. It is expected that most rulers will acquire 1 or 2 Coping Mechanisms during their lifetime, though in some rare circumstances a character may end up with more.  

**Strategic Considerations**  
As developers, our goal with the Stress system is not to prohibit or punish players for taking certain actions, but rather to make them think twice about otherwise no-brainer decisions. Is it really worth it to execute that foreign claimant when doing so will give you 42 Stress? Maybe, but maybe not! That is a decision you will need to make when the time comes.  

In this way, Stress also gives us another tool we can use to balance the various personality traits against each other. Some traits like Ambitious and Compassionate may have higher numerical bonuses, but they cause you to acquire Stress more frequently or in larger amounts. Others like Sadistic may make your vassals loathe you, but your character won’t be bothered by pesky concerns like morality when they have to do what needs to be done. Who knows... they might even enjoy it!  

![image8.jpg](https://forumcontent.paradoxplaza.com/public/577909/image8.jpg "image8.jpg")


[A screenshot showing showing the Skill and Stress differences between the Lazy and Diligent Personality Traits]  

Regardless of what personality traits your character has, the optimal strategy with Stress is often not to avoid acquiring Stress at all costs, but rather to strategically acquire certain Coping Mechanisms and leverage them intelligently to keep your character’s Stress at ideal levels. Managing your character’s Stress well will ensure you are always able to take advantage of any opportunities that come your way, while behaving recklessly may leave you Stressed to the point of insanity during a crucial moment of your reign…  

![image5.jpg](https://forumcontent.paradoxplaza.com/public/577910/image5.jpg "image5.jpg")


[A screenshot showing a stressed ruler having their very own Nero moment]  

Anyway, that is all I have for you this week. I hope this has given you some insight into how the Stress system works in Crusader Kings III, and that this has inspired everyone to think of new and creative ways to leverage the system to its full potential! Feel free to ask any questions you have in the comments, as I will be sticking around for a few hours to explain and elaborate on the Stress system.

 

Last edited: Jun 16, 2020

<!-- artifact:reactions:start -->
- 188 Like
- 84 Love
- 33 (unlabeled — rendered as base64 data URI)
- 15 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)**
Role: Content Designer
Badges: 38
Messages: 65
Reaction score: 2,138

*[Full game-badge icon list of 38 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
