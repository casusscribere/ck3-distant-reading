---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1493718/"
forum_thread_id: 1493718
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 76
title: "CK3 Dev Diary #76 - Royal Audio"
dd_date: 2021-10-05
author_handle: Metal King
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1013
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1493718'
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
    location: raw_lines_~28_to_152
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_151
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1728.jpg?1633437248
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_154_to_156
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_261_to_265
    action: preserved_and_flagged
    counts:
      Like: 102
      Love: 47
      (unlabeled — rendered as base64 data URI): 6
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_273_to_377
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_378_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1728.jpg?1633437248)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #76 - Royal Audio

<!-- artifact:thread_metadata:start -->
- Thread starter [Metal King](https://forum.paradoxplaza.com/forum/members/metal-king.1027995/)
- Start date [Oct 5, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-76-royal-audio.1493718/)
<!-- artifact:thread_metadata:end -->

Hello!  

Welcome to another Dev Diary! This time I’m back to tell and show you a little behind the scenes of what we have been doing with Audio & Music for Royal Court  

### The room matters!​


The introduction of Court View made us really excited in the Audio Dept and also a new challenge! After working so long with games that mainly use paper maps, finally having a 3D space there was some extra room to play around with Sound Design and also getting a bit creative.  

Of course, we wanted to add sound effects onto certain different objects like fireplaces and chandeliers and also including room ambiences for each type. But we also thought it would be a perfect opportunity to give more “life” to the court rooms by adding something we call “walla”. Or perhaps known more commonly as “crowd recording”.  

Since restrictions did start to loosen up more in Stockholm, (and also it’s a fun activity) we thought about recording some of our team members from the CK team (and a few more colleagues from other projects)  

Now you might be wondering how you even do something like this? Of course, it requires a bit of patience and having a couple of microphones!  

![eh8mEDpuQPI_afcC3wJfSziRXRS0a3auCeI_J9u54ZfpHQ5TqZp-eR-WdxgpE9Zez-u-3M0-b5s_raSsFngGM83nXUACMlhLIEOhPTzQjzwbgySIWiI0svdji4XvHqotu7_mlpGF=s0](https://lh6.googleusercontent.com/eh8mEDpuQPI_afcC3wJfSziRXRS0a3auCeI_J9u54ZfpHQ5TqZp-eR-WdxgpE9Zez-u-3M0-b5s_raSsFngGM83nXUACMlhLIEOhPTzQjzwbgySIWiI0svdji4XvHqotu7_mlpGF=s0 "")




![uns_HY1WP1TV7zvLzfI3DvfRnMs6z5OQtBFpKW7knH83LhmHVY6qvTTrQoslgZbKVh5U-yzWqia6j4500GszNWBRWhJY1TSc1gry2JOGyNqWgNBJMs3OhWhWBGxQsTU94A20wbVY=s0](https://lh5.googleusercontent.com/uns_HY1WP1TV7zvLzfI3DvfRnMs6z5OQtBFpKW7knH83LhmHVY6qvTTrQoslgZbKVh5U-yzWqia6j4500GszNWBRWhJY1TSc1gry2JOGyNqWgNBJMs3OhWhWBGxQsTU94A20wbVY=s0 "")


So this is me and Tobey Evans, the Sound Designer working on Royal Court, sitting down in one of the Sound Studios and doing pre-work before the big recording session. we’re testing out all the equipment, making sure all the cable works as intended and it all sounds great!  



After all that we did manage to book the biggest room we have in the office, which is called “the Library”. Not only was it to ensure that we would be able to have distance between all people while recording all their voices, but also it had the best acoustics to match the size of the Court Rooms.  


![TQbYbORdJnUzsMhMAi6Um9FJ6EAc3WjtWEVR_FK2e0JIKPe5t1xGHMFkZV7UrH2-WT-43N2R5Vis0v2XPpXnHzbWfMc64_53lY_pKHgxHziwfctrQi_hxvXg08ocwWxyqkhhtp70=s0](https://lh5.googleusercontent.com/TQbYbORdJnUzsMhMAi6Um9FJ6EAc3WjtWEVR_FK2e0JIKPe5t1xGHMFkZV7UrH2-WT-43N2R5Vis0v2XPpXnHzbWfMc64_53lY_pKHgxHziwfctrQi_hxvXg08ocwWxyqkhhtp70=s0 "")


![v_2DV8J2jOTaSYba85Ky6rUWjsUKdQ7eNpouoH2aiC6grpqWqI3MLvrxcqcWWg2_taH1DE9SpSloA7M3redGSgRZK4PUd1RkIw9UWr83cHQKGYQLGIKOifshAAAxcL589g9OXmp0=s0](https://lh5.googleusercontent.com/v_2DV8J2jOTaSYba85Ky6rUWjsUKdQ7eNpouoH2aiC6grpqWqI3MLvrxcqcWWg2_taH1DE9SpSloA7M3redGSgRZK4PUd1RkIw9UWr83cHQKGYQLGIKOifshAAAxcL589g9OXmp0=s0 "")



The next question would be what kind of script we were using for this recording. It’s rather difficult to record “walla” in all languages, so instead, we did use a script made in Latin. Not because we all are fluent in Latin (would have been cool though!) but because,from my experience, that has been some of the best languages to use when you need some “gibberish” talk in the background. Especially since we had a big mix of people with different accents.  


![b391MHdRVJP-D9rEDJZ7ONZYET5hthKMDdprJFO6r8mQgnU8RhNxXxuy9Y_DRumzUsbUf68kMLEg-ZWZuUxREgNDsaW3qfZ5LpuQaoBozjpM2vra9pkxeVP6_LBIiHW1p3QSHzhS=s0](https://lh6.googleusercontent.com/b391MHdRVJP-D9rEDJZ7ONZYET5hthKMDdprJFO6r8mQgnU8RhNxXxuy9Y_DRumzUsbUf68kMLEg-ZWZuUxREgNDsaW3qfZ5LpuQaoBozjpM2vra9pkxeVP6_LBIiHW1p3QSHzhS=s0 "")


![50FDdfNkSIB6awtETaVERVlpEkPDWCyxYn3_DJ91mgU7l3O7GUwAm6OHd9MzvceERgA50S8ehSP1ZI1UTePzKCcHAqPJ2Za8cBg9W4NXhx1IqlE5taWeeZ9Vn4O7Ng725kumkOz1=s0](https://lh5.googleusercontent.com/50FDdfNkSIB6awtETaVERVlpEkPDWCyxYn3_DJ91mgU7l3O7GUwAm6OHd9MzvceERgA50S8ehSP1ZI1UTePzKCcHAqPJ2Za8cBg9W4NXhx1IqlE5taWeeZ9Vn4O7Ng725kumkOz1=s0 "")



It was a fun big session we had, and everyone was happy to be part of such a big team event again after not seeing each other for such a long time in person!  


![Jh1rRrCZ-hSqpdU_h814v4OPV66lsH2we1Q0h1j5vQj8a8uI40n7LH7sP4fvoAlpD5JWAfuso6agXI2m8qx7yWYVEU73izZ4uC9ir8GIJe3gHoGTwp8hi-V13VIaKqM-Sy-Nnxwa=s0](https://lh5.googleusercontent.com/Jh1rRrCZ-hSqpdU_h814v4OPV66lsH2we1Q0h1j5vQj8a8uI40n7LH7sP4fvoAlpD5JWAfuso6agXI2m8qx7yWYVEU73izZ4uC9ir8GIJe3gHoGTwp8hi-V13VIaKqM-Sy-Nnxwa=s0 "")




So we did go a bit extra to make these new fancy rooms in CK3 sounding more alive and enhance the experience for you players. ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")  

How will all this sound in the end? It will change depending on your Court’s Grandeur level! The higher this value, the more of the crowd you will hear in the room, (and this will also work the other way around, so less Grandeur , fewer people.  

### Royal Tunes​


Hi everyone, it’s Yannick and Robin from Audinity. After having written music for several Paradox games and expansions, we’re happy to be on board again for CK3: Royal Court and share some insights into the new music for this expansion!  


The soundtrack for this Expansion will consist of some new ambient Mood Tracks, Cue Tracks and even a new Main Theme.  

The main direction for these new tracks was trying to make them sound a bit different compared to the existing music from the base game. Medieval music can have many different sounds, but since we are at the Royal Court this time, the keyword for the music for this Expansion was “Royal”. So you can hear some powerful fanfares, noble strings, and a medieval guitar ensemble that make you feel like standing right in the King’s hall.  

While the Mood Tracks will add some noble flavours to the general ambient music, the Cue Tracks will play when you are Holding Court in your Kingdom. And when starting the game, the new Main Theme will welcome you to this Expansion and to the Royal Court!  

We did not only record several fantastic solo musicians playing some fancy historical instruments for this soundtrack, we also wanted to go a bit extra on the orchestral side, so we actually went to Prague and recorded the music live with the FILMharmonic Orchestra at Smecky Music Studios!  

This was the studio before the recording session...  

![rmq6xev0JScSVzZIxob-bi1hWjWtfXI9IQmkLEDEbQ2rSKxbzHKpoDLAUXnbr7jLUWtds8o0RJLs9fdynb4lB5X64WqfCf3vN256BKAvoN4cu2l5H5xa9zwaMSA_Wu2rEFtemgDh=s0](https://lh4.googleusercontent.com/rmq6xev0JScSVzZIxob-bi1hWjWtfXI9IQmkLEDEbQ2rSKxbzHKpoDLAUXnbr7jLUWtds8o0RJLs9fdynb4lB5X64WqfCf3vN256BKAvoN4cu2l5H5xa9zwaMSA_Wu2rEFtemgDh=s0 "")



...and this is what it looked like during the session with over 60 great musicians at work!  


![E0_3X9GBADuXFiusapSzv5JwZSorgb9ZEMmlVzPUcEYJIWGOfWHcBjsx0ZQz7myd7FqEPw05xPydtynq2-allpkLie4ZlFSzZl9JXZ-06QK_lSjUj9_EQ4K40y6AKj_wdnfCpd0J=s0](https://lh6.googleusercontent.com/E0_3X9GBADuXFiusapSzv5JwZSorgb9ZEMmlVzPUcEYJIWGOfWHcBjsx0ZQz7myd7FqEPw05xPydtynq2-allpkLie4ZlFSzZl9JXZ-06QK_lSjUj9_EQ4K40y6AKj_wdnfCpd0J=s0 "")




![qnPNWdPVNuQcTLH6Q_dA3xNKSiYfmLWBK182M9i9_MtyN0S5YxCrESqIWUbURAyH77FvHVl_4E8ZCaX2hGanWpX79MOqnZEa1FzNvdog86n-zZb5DppdkopsD7jfxiiLAiLwOI8Y=s0](https://lh4.googleusercontent.com/qnPNWdPVNuQcTLH6Q_dA3xNKSiYfmLWBK182M9i9_MtyN0S5YxCrESqIWUbURAyH77FvHVl_4E8ZCaX2hGanWpX79MOqnZEa1FzNvdog86n-zZb5DppdkopsD7jfxiiLAiLwOI8Y=s0 "")


Two happy composers ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")  


We could keep writing about the music, but we think you get the best insight into the soundtrack for CK3: Royal Court when listening to some of the music itself!  
So we are happy to share with you the “Holding Court” Cue Track for Western Europe as a preview!  

[https://www.youtube.com/embed/530ZNj8FUb0?wmode=opaque](https://www.youtube.com/embed/530ZNj8FUb0?wmode=opaque)


So back to Metal King, I hope you enjoyed this week’s Dev Diary, understand it might not tell you so much about the features but at least we got to show you a little behind the scenes when we do work with Sound Design & Music.

<!-- artifact:reactions:start -->
- 102 Like
- 47 Love
- 12 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Metal King](https://forum.paradoxplaza.com/forum/members/metal-king.1027995/)**
Role: Audio Director
Badges: 6
Messages: 143
Reaction score: 2,252

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
