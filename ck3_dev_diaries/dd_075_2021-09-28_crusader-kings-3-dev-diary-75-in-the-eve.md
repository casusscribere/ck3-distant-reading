---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1492792/"
forum_thread_id: 1492792
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 75
title: "Crusader Kings 3 Dev Diary #75 - In the Event of Court Events"
dd_date: 2021-09-28
author_handle: Wokeg
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1022
inline_image_count: 12
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1492792'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1720.jpg?1632843694
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_235_to_239
    action: preserved_and_flagged
    counts:
      Like: 112
      Love: 69
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_247_to_302
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_303_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1720.jpg?1632843694)
<!-- artifact:thread_banner:end -->

# Crusader Kings 3 Dev Diary #75 - In the Event of Court Events

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Sep 28, 2021](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-75-in-the-event-of-court-events.1492792/)
<!-- artifact:thread_metadata:end -->

Welcome comrades! In today’s (not at all late shutup SHUTUP) dev diary, we’ll be going over the new court-type event; many of you will likely have seen them a bit already in a few preceding dev diaries, but for the rest, allow me to formally introduce court-type events:  


![001.PNG](https://forumcontent.paradoxplaza.com/public/748060/001.PNG "001.PNG")



This new event type is seen exclusively within the court view, where they replace standard character-type events.  

We added these because one of the major design limitations with character-type events is that they’re uhh… they’re small. Really, really, really small, and having comparatively little space to work with means they impose a lot of restrictions on their use.  

Those of you who mod, or have dabbled at modding, will likely know what I’m talking about: generally, a character event can only fit *about* three paragraphs of copy and 3-4 options before it starts to look a little naff. Less if there are characters or titles involved with very long names, or if you have to do a lot of paragraphing.  

There are good reasons for them to be this small - they get in the way less when popping up, it encourages concise delivery of information, and it frames the portrait characters in each event nicely.  

For the court scene, these considerations are (generally) moot, so we wanted to play around with a more liberal event format. We don’t need to worry about framing characters in the traditional sense since we show them in the scene, the player always opts into a court-type event and thus can’t have one pop-up unexpectedly, and though information (and options) still need to be reasonably concise, it’s nice to have a little room to flex the meaning of “concise” somewhat.  

![002.PNG](https://forumcontent.paradoxplaza.com/public/748061/002.PNG "002.PNG")



From a player’s perspective, you’ll mostly interact with court-type events through the not-at-all-confusingly-named court events pool. Similar to random yearlies, court events reflect the life of your court just existing, with all the petty drama and courtly intrigue you’d expect from a medieval monarch’s household. They primarily involve characters consistently within your court (rather than far-flung vassals or guests), and often tie into court grandeur and your different levels of amenities.  

![003.PNG](https://forumcontent.paradoxplaza.com/public/748062/003.PNG "003.PNG")



Other than their tone, size, and occasional number of options, the biggest differences that players will notice are their usage of different camera shots instead of backgrounds and portraits…  

![004.PNG](https://forumcontent.paradoxplaza.com/public/748063/004.PNG "004.PNG")


![005.PNG](https://forumcontent.paradoxplaza.com/public/748064/005.PNG "005.PNG")


![006.PNG](https://forumcontent.paradoxplaza.com/public/748065/006.PNG "006.PNG")



… and their optional nature. Unlike yearly events, court events are opt-in, meaning that you don’t have to take them if you don’t want to, in which case their default (neutral-ish) option will be selected after a long-ish time-out period.  

To open a court event, you simply click on a button that’ll appear floating over one of your court’s relevant characters. Whenever you’ve got court events you could be checking, you’ll be notified via the Royal Court button in the right-hand panel.  

![007.PNG](https://forumcontent.paradoxplaza.com/public/748066/007.PNG "007.PNG")



From a scripting perspective, court-type events share a fair amount of DNA with character-type events, but differ mostly in the form of their court_scene block.  

Usually, I’d go on to explain everything in a bit more depth inside the dev diary itself, but since court-type events can be tricksy to script till you get the hang of ‘em, we’ve included an example court-type event inside one of the event files that breaks down their make-up:  


![008.PNG](https://forumcontent.paradoxplaza.com/public/748067/008.PNG "008.PNG")



^^ Hopefully, this should be a solid annotated example, but just in case, here’s a few pre-emptive clarifications:  
1) Every court-type event must have a button character, even if that character is just your character, so that must always be set up.  
2) The group parameter defines which spot in the scene that character stands in. These groups themselves are scriptable (with a bit of work) elsewhere, so you can arrange characters inside the court however you like. The groups shown in the example actually contain multiple different preset positions within the court scene, one of which is selected randomly for each event when it tries to fire.  
3) For animations, we can access all the standard ones, plus a slew of new animations created specifically for the court scene.  

Finally, just for fun, let’s have some more court events:  


![009.PNG](https://forumcontent.paradoxplaza.com/public/748068/009.PNG "009.PNG")


![010.PNG](https://forumcontent.paradoxplaza.com/public/748069/010.PNG "010.PNG")


![011.PNG](https://forumcontent.paradoxplaza.com/public/748070/011.PNG "011.PNG")



Oh, right, yes, I titled the dev diary “and friend” too, didn’t I? Welp, the new court-type isn’t the only event type we’re adding with this expansion (just the most exciting). We *also* have the new duel event type!  

Duels were added as part of our first flavour pack, but I’m sure you’ve all noticed that the space for ‘em is pretty limited, and the animations don’t work so well for this context. Welp, we’ve revamped both of those with this new type, giving duels a face-lift:  


![012.PNG](https://forumcontent.paradoxplaza.com/public/748071/012.PNG "012.PNG")



… Naturally, the weapon held by either character does correspond to their signature weapon type, or whatever weapon artefact they have equipped (if they’ve got one).  

And that’s all from me, folks. As ever, I’ll be around in the comments for an hour or so to answer questions, but otherwise, see y’all next diary!

<!-- artifact:reactions:start -->
- 112 Like
- 69 Love
- 15 (unlabeled — rendered as base64 data URI)
- 8 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)**
Role: Former CK3 Experienced Game Designer
Messages: 528
Reaction score: 15,169
<!-- artifact:op_signature:end -->
