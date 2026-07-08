---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1857935/"
forum_thread_id: 1857935
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 183
title: "Dev Diary #183 - Coronations Art & Changelog"
dd_date: 2025-09-04
author_handle: PDX-Trinexx
expansion: Coronations
patch: Patch 1.17
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 944
inline_image_count: 2
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1857935'
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
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_245_to_249
    action: preserved_and_flagged
    counts:
      Like: 58
      (unlabeled — rendered as base64 data URI): 1
      Love: 5
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_257_to_343
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_344_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #183 - Coronations Art & Changelog

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Sep 4, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-183-coronations-art-changelog.1857935/)
<!-- artifact:thread_metadata:end -->

Hello everyone! Today's developer diary is a short one, as everyone at Studio Black is currently focused on putting extra polish on our remaining Major Updates this year. In this dev diary, we're sharing two high-resolution illustrations from Coronations, as well as giving you the full changelog for the 1.17 “Ascendant” Update itself.  

To be clear, the update is NOT live yet; it will be released alongside Coronations on September 9th.  

---

### Coronation & Anointment Art​

The two images we're including here were crafted by our wonderful Studio Black 2D Art team. This type of illustration is limited to 460x1100 in-game, but we're posting them in their original 2688x6224 resolution so you can see their full detail. Please note that they’re dynamically scaled down for display purposes here, but you can either download the images directly or open them in a new tab to view them at full size.  

![Coronation.jpg](https://forumcontent.paradoxplaza.com/public/1353401/Coronation.jpg "Coronation.jpg")



![Anointment.jpg](https://forumcontent.paradoxplaza.com/public/1353402/Anointment.jpg "Anointment.jpg")



---

### PC Update 1.17.0 "Ascendant" Changelog​

### Expansion Features (Paid)​

- Added Coronation activity
- Added game rules for Coronations: one making them optional by turning off Crowned laws, another that allows rank-up to emperor without losing crown
- Added laws for kings and emperors regarding their Uncrowned, Crowned or Anointed status
- Uncrowned kings and emperors - and their spouses - do not wear crowns
- Adds Coronation Tradition doctrine to faiths, determining whether they have Anointment Required (for emperors), Anointment Permitted or No Anointment
- Adds faith-based triggers for whether a culture is focused specifically on crowns during coronations, on regalia, or utilizes either without preference
- Two Coronation types: Regular Coronation and Anointment by the HoF
- Adds Request Anointment character interaction with the HoF
- New filter for activity locations that permits your capital and holy sites, both within and outside your realm
- Ties coronations into title gain events and elsewhere
- Provide coronation artifacts (crowns or regalia) through multiple avenues: on game start, from free inspirations, on regular pulse for AI
- Adds imperial rank-up event informing players that they become uncrowned when increasing tier
- Coronation activity options: Ceremony and Celebrations
- Coronation host intents: Impress Attendees, Embrace Supporters, Weaken Detractors, Exalt the Crown
- Coronation guest intents: Bear Witness, Seize Advantages, Advocate Domain, Profess Rights, Offer Support, Disrupt Loyalists
- ~44 prelude phase random host events
- ~19 prelude phase random guest events
- ~28 feast phase random host events
- ~18 feast phase random guest events
- Above events include guest intent fulfilment events, where guests with shared intents choose what related reward they are interested in asking of the host
- “Critical fail” outcome for Coronations based on guests with disrupt loyalists besting the host
- Events include content for Christians, administrative, clans, nomads, tribals and confederations
- New Activity Pulse Actions for Coronations
- 10 ceremony phase key events with triggered success-based and regional loc variations
- Magnificence meter determining a Coronation’s level of success
- Scaling Coronation and Oath rewards based on magnificence
- through activity and at conclusion, opinion gain with vassal stances based on intents
- Background relationship formations amidst and between Supporters and Detractors during Coronation
- Supporters and Detractors guest subsets
- Activity view widget displaying Major Supporters and Major Detractors
- Added 16 Oaths with bespoke rewards and fulfillment conditions
- Includes Oath-tracking story cycle, Oath decisions, and Oath failure and success events
- New Oath-based building lines
- New Oath-based cultural tradition
- Added crowning animation
- Added new intent icons for the coronation activity
- Coronation activity type illustration
- Illustrations for Regular Coronation and Anointment sub-types
- AI behavior adjustments so they will host a Coronation ASAP while uncrowned


### Game Content​

- Added bow inspiration type and added bows to the weapon option of the commission artifact decision.
  * Bow artifacts now increase hunter trait venator track xp gain.
- Adds 4 free random yearly events about being a councillor
- Underaged kings/emperors over 12 years old now wear crowns
- New camera angles for event characters, many playing with perspective
- ~8 new feast events
- Adds regional/government type-based custom loc keys like GetFighterTerm, GetRegionalSword, GetTitleTierAdjective, GetLocalCommonerTerm


### Bug Fixes​

- Fixed bug where player couldn't close the travel window after opening it during an ongoing travel - only check if a travel plan is cancel-able when checking if the travel window can be closed if we have a travel plan draft. for ongoing travels, the window should always be close-able.
- Fixed travel_danger_events.6000 listing the wrong character in its effects and hunt_legendary_animal_custom_loc_trigger no longer errors if scoped on the root character.
- Blocked certain disease recovery event outcomes for children
- Cultivated Sophistication's development bonus now only applies if your Estate is in your realm capital, preventing vassals from providing repeated development bonuses to their liege.
- Added a cooldown check for activities, so they are moved to the right list when they are unavailable, and tell you how long is left before they are available again on hover
- Various fixes to tsagaan sar feast flavor events
- Added non-nomad music tracks to nomadic music list to lessen repetition
- Fixed an issue with mass ransoming, where you would get all of the character’s money instead of a fixed amount
- Updates background triggers for more appropriate regional backgrounds
- Makes holy_site_unique background include generic fallback backgrounds
- Fixed the effects and progression of Paiza Office nomad domicile upgrade for the Barter Stalls yurt
- Fixed the effects of Skull Collection nomad domicile upgrade for Court Yurt
- Fixed edge cases in activity invalidation events
- Makes HoF more likely to accept Declaration of Repentance if you are their liege or top liege

---

That’s all we have for today. We’ll see you again on Tuesday!

<!-- artifact:reactions:start -->
- 58 Like
- 23 (unlabeled — rendered as base64 data URI)
- 15 (unlabeled — rendered as base64 data URI)
- 5 Love
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 30 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
