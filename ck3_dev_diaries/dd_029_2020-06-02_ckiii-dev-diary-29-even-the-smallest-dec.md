---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1395308/"
forum_thread_id: 1395308
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 29
title: "CKIII Dev Diary #29 - Even the Smallest Decision..."
dd_date: 2020-06-02
author_handle: Heptopus
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1062
inline_image_count: 9
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1395308'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1391.jpg?1591101015
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_221_to_225
    action: preserved_and_flagged
    counts:
      Like: 142
      Love: 57
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_233_to_331
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_332_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1391.jpg?1591101015)
<!-- artifact:thread_banner:end -->

# CKIII Dev Diary #29 - Even the Smallest Decision...

<!-- artifact:thread_metadata:start -->
- Thread starter [Heptopus](https://forum.paradoxplaza.com/forum/members/heptopus.1269016/)
- Start date [Jun 2, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ckiii-dev-diary-29-even-the-smallest-decision.1395308/)
<!-- artifact:thread_metadata:end -->

Come one, come all, and hear the tale of Kalevi of Karelia. We’ll follow him on the perilous road from High Chieftain of a few counties to King and defender of Ukko as a Holy Warrior! We will pay close attention to what choices he makes to further his agenda, for what is life but the decisions you make along the way?  

![final_young_old.png](https://forumcontent.paradoxplaza.com/public/571592/final_young_old.png "final_young_old.png")



Surprise surprise, in this dev diary we will take a closer look at Decisions: what they are and how they work. The easy way to describe a Decision is that they are an action a ruler can take, but they end up being so much more than that over the course of a game!  

We’ve focused on adding a wide spread of Decisions in the game so that you will have unique experiences playing different characters all over the map.  

![final_decision_view.png](https://forumcontent.paradoxplaza.com/public/571594/final_decision_view.png "final_decision_view.png")


*[Two examples of what the decision view might look like for different characters]*  

There are two types of Decisions: Major Decisions and… well, Decisions. Major Decisions are displayed in a prominent position at the top of the interface and can be viewed as something to work towards, if you want; we have designed them to give the player a rewarding goal – a kind of mission. Major Decisions are often life-changing and their effects will be felt throughout the world; you can make decisions that affect your whole dynasty, or a whole religion. Examples of Major Decisions are “Found a New Kingdom”, “Consecrate Bloodline” and, of course, “Mend the Great Schism”.  

Regular Decisions, on the other hand, can function as a means to reach those lofty goals and are often more accessible and more immediately relevant to your everyday life as a ruler. Decisions cover a wide range of actions you can take, everything from “Host Feast” to “Flagellate”. This gives you a lot of control over what actions your character takes and how you shape your realm.  

So, back to Kalevi of Karelia. Our story begins just as the young High Chieftain Kalevi, only 16 years of age, has stepped into the role of a ruler after his father’s passing. Orthodoxy is spreading upward from the south, Catholicism is a growing concern in the west, and Kalevi wants nothing more than to protect the old ways and the Suomenusko faith he was brought up with. It might seem like a big task for any lone man, but he has a plan! He intends to raise a Hall of Heroes and lay the foundations for Holy Warriors to defend the faith.  

![final_defenders_of_ukko_young.png](https://forumcontent.paradoxplaza.com/public/571595/final_defenders_of_ukko_young.png "final_defenders_of_ukko_young.png")



The road ahead might seem long and taxing, but such is the way of life when your goal is as lofty as this.  

He does currently stand alone at the rudder, however, and he wishes for a companion – a spouse. As luck would have it he stumbles across a skillful and beautiful peasant woman when he is out hunting!  

![final_call_hunt.png](https://forumcontent.paradoxplaza.com/public/571596/final_call_hunt.png "final_call_hunt.png")



![final_far_from_people.png](https://forumcontent.paradoxplaza.com/public/571597/final_far_from_people.png "final_far_from_people.png")



Together they start a new family, and the first Decision among many has been made.  

One of the requirements to fortify a Holy Site, by taking the Major Decision “Defenders of Ukko”, is to have a Holy Site to fortify. After a quick glance at the Suomenusko Holy Sites, Kalevi’s gaze settles on Raivola in Kakisalmi, currently under the control of his neighbor Chieftain Susi. Susi believes in the right Gods, but Kalevi doubts he would allow other people access to the Holy Site... War it is, then.  

![final_invite_champions.png](https://forumcontent.paradoxplaza.com/public/571598/final_invite_champions.png "final_invite_champions.png")



To tip the scales in his favor, Kalevi decides to send out heralds to let it be known that he is searching for Champions to join him. Soon he has bolstered his forces enough to take on his neighbor.  

After the war Kalevi is perplexed… He has a Holy Site under his control, and he has the will; why won’t the people help him build the Hall of Heroes? Why won’t they help him defend the true faith? Then it hits him: he doesn’t have enough strong people backing him, and he is not known to be pious enough to inspire the respect needed. This realization sets Kalevi down a path of many years of character-building, in the form of pious endeavors, and realm-building, in the form of conquest and vassalization, until he has founded his own Kingdom.  

![final_found_kingdom.png](https://forumcontent.paradoxplaza.com/public/571599/final_found_kingdom.png "final_found_kingdom.png")



As his realm stabilizes he realizes what must follow; he needs to go on a pilgrimage to truly understand the Suomenusko faith.  

![final_pilgrimage_physician.png](https://forumcontent.paradoxplaza.com/public/571600/final_pilgrimage_physician.png "final_pilgrimage_physician.png")



However, during his pilgrimage Kalevi is grievously wounded! Word is sent out that the court is looking for a physician, and soon enough his wounds have been tended, but the scars will forever mar him.  

Gaining traits, like Wounded, might spur you to make a Decision you otherwise wouldn’t, and Decisions can also become available through traits, events, and a myriad of other changing conditions in the game. If you find a Decision particularly interesting you can mark it as important and you will then get an alert when the conditions are met and you can take the Decision!  

For Kalevi a lot of time has passed. Finally, at the tender age of 60 and a life full of decisions small and great behind him, King Kalevi of Karelia finds the support needed to fortify a Holy Site and bolster the defense of Suomenusko.  

![final_defenders_of_ukko_old.png](https://forumcontent.paradoxplaza.com/public/571601/final_defenders_of_ukko_old.png "final_defenders_of_ukko_old.png")



Who knows what will follow for Kalevi; maybe he’ll Found a New Empire to stabilize the region further, or perhaps he’ll Adopt Feudal Ways in a bid to – at long last – attempt to develop the region in a new direction. But one thing is for certain: the threat of Christianity has done nothing but grow during all these years…  

Thank you for reading and see you next week!

<!-- artifact:reactions:start -->
- 142 Like
- 57 Love
- 40 (unlabeled — rendered as base64 data URI)
- 10 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Heptopus](https://forum.paradoxplaza.com/forum/members/heptopus.1269016/)**
Role: Content Designer
Badges: 2
Messages: 47
Reaction score: 917

*[Full game-badge icon list of 38 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
