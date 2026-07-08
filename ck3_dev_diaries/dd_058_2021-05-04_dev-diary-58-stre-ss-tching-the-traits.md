---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1472092/"
forum_thread_id: 1472092
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 58
title: "CK3 Dev Diary #58 - Stre(ss)tching the traits"
dd_date: 2021-05-04
author_handle: Pdx_Meedoc
expansion: Northern Lords
patch: Patch 1.4 (Azure)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 728
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1472092'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1618.jpg?1620131431
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_196_to_201
    action: preserved_and_flagged
    counts:
      Like: 254
      Love: 50
      (unlabeled — rendered as base64 data URI): 1
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_209_to_317
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_318_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1618.jpg?1620131431)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #58 - Stre(ss)tching the traits

<!-- artifact:thread_metadata:start -->
- Thread starter [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)
- Start date [May 4, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-58-stre-ss-tching-the-traits.1472092/)
<!-- artifact:thread_metadata:end -->

Hello everyone!  

Nice to meet you all! I recently joined the Crusader Kings III game design team and am honored to inaugurate my PDX account with this Dev Diary. Today we will cover two improvements planned for the upcoming patch: additional content and AI warfare improvements.  


**Trait changes**  

One of the many pleasures of Crusader Kings is to personify a plethora of characters. Every one of them offers a good opportunity to roleplay, thanks to the various combinations of traits they offer. The Azure patch will expand upon existing content by updating and adding some trait-specific interactions and consequences. With this update, we want to connect the stress system even closer to personality traits.  

One of the notable changes is for Shy: it will no longer generate Stress when launching a Personal Scheme. Shy characters can still receive Stress via some of the scheme event options however, and they will be less efficient at performing personal schemes (it will take them longer), but they will be able to do it without ending up having a mental breakdown.  

We also added a few new interactions and decisions. For instance, Forgiving characters can abandon one of their hooks to lose Stress. You can either decide to be a truly forgiving character, abandoning a hook you obtained unwittingly, or you can actively look for hooks and then choose to be merciful. We have also added new options for Diligent characters; they can dedicate themselves to improving the Development of their Capital, but doing so will generate a lot of Stress. Finally, if Impatient characters are Stressed, they can speed up the progress of their current Personal Scheme, without affecting their current Stress levels.  


![17ypLPkLPOs0EHv4oF9l9KTLDMNySc81oQCf6eKWcXJa58REKYby6cESmzziKPkJJ73u-2gwJA4DUJoTwv_7JnddPgg_DRtTyAjdeSmVux_EYPoqoKoNqi7iAeYzkEMyOW4r85x9](https://lh3.googleusercontent.com/17ypLPkLPOs0EHv4oF9l9KTLDMNySc81oQCf6eKWcXJa58REKYby6cESmzziKPkJJ73u-2gwJA4DUJoTwv_7JnddPgg_DRtTyAjdeSmVux_EYPoqoKoNqi7iAeYzkEMyOW4r85x9 "")


*[Image of the Develop Capital decision available for Diligent characters]*  


Some traits have also gained access to interactions that are not related to the stress system but still improve upon the expression of their personality. For instance, Arbitrary characters can now dismiss a Hook a vassal holds on them by spending a lot of Prestige and gaining Tyranny.  


![bgq3ZnaSlYfZu6FwHqdyrh9epMpAUxt1dUK-PcIzPJeR4AiwMMbh8HX7VhSLykv3JAjMDZXMwKLp5oqtd-fPSBYYZ6sWmGvJfE6KgqV92jPu3lhVhdM4HFs1dabrREv2gN2XEvUR](https://lh5.googleusercontent.com/bgq3ZnaSlYfZu6FwHqdyrh9epMpAUxt1dUK-PcIzPJeR4AiwMMbh8HX7VhSLykv3JAjMDZXMwKLp5oqtd-fPSBYYZ6sWmGvJfE6KgqV92jPu3lhVhdM4HFs1dabrREv2gN2XEvUR "")


*[Image of the Dismiss Hook interaction available for Arbitrary characters]*  

We would love to hear your feedback, and also suggestions for improving other traits!  


**AI and Warfare**  

There is also a number of AI improvements, mostly about how the AI moves its units while at war. Pathfinding has been revised, and AI armies should now take more optimal routes to reach their targets, whether they be close but surrounded by treacherous terrain, or far away across the sea (which was most visible during Crusades; there will be no more island hopping for Christian armies, and Vikings should also be more swift and direct in their raids). The new pathfinding logic now factors in time, attrition and threat when selecting and routing to a destination.  

Getting close to the enemy is only the first step in warfare though, and the AI should behave more sensibly in other areas too. After winning crucial battles, AI armies should use their full might to more efficiently besiege enemy fortresses - you should see less mangonels and bombards chasing peasants while there is a perfectly good castle waiting to be ruined. We also adjusted the AI behaviors depending on their Casus Bellis, making sure that they not only prioritize territorial conquest but also capturing hostages when relevant. While there’s likely to be some odd behaviors in the military AI still, we believe this will be a noticeable change in the right direction.  


Lastly, an important organizational change: the version number of the patch will be 1.4 instead of 1.3.X as announced previously. This is to make the scope of the patch a bit clearer. While it is still a relatively small patch, it is also larger than a hotfix or a pure bugfix patch we've released in the past. Some mods will need to be updated. And while we always strive to keep save games compatible, with the nature of the game you might still run into edge cases with your old saves that we did not catch.  

And that’s it for today! Thanks again for your precious feedback, and please keep providing more! I hope you enjoyed it, and see you next week for more information about the Azure patch!

<!-- artifact:reactions:start -->
- 254 Like
- 50 Love
- 20 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 1 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)**
Role: Corporal
Badges: 95
Messages: 39
Reaction score: 2,254

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
