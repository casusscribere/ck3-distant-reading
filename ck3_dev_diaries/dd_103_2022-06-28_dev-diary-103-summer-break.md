---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1533555/"
forum_thread_id: 1533555
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 103
title: "CK3 Dev Diary #103: Summer Break"
dd_date: 2022-06-28
author_handle: rageair
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 953
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1533555'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1996.jpg?1656428620
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_190_to_195
    action: preserved_and_flagged
    counts:
      Like: 72
      (unlabeled — rendered as base64 data URI): 5
      Love: 7
      Haha: 3
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_203_to_310
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_311_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1996.jpg?1656428620)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #103: Summer Break

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Jun 28, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-103-summer-break.1533555/)
<!-- artifact:thread_metadata:end -->

Greetings!  

Summer is upon us, and with Fate of Iberia and the 1.6.1 update(s) (note: another small fix update will be released this week), we feel confident that the game is in a good place where it can be enjoyed over the break! (As always, keep those reports up if you find an issue) Soon we’ll all be out enjoying the beautiful Swedish summer, taking some well-deserved rest, and recharging for the time ahead!  

As mentioned in Dev Diary 100, we have big and small plans, some of which will be revealed later this year. We’re very excited to see what you think, but we can’t say anything yet!  

From this point onwards we will not have any regularly scheduled Dev Diaries until we’re all back! There may be a small dev diary here and there, but no promises. **We’ll be back before the end of August.**  

If you want to keep discussing the game over the break, [head over to our Discord](https://discord.com/invite/ck3). Also, note that we’ll have videos every Wednesday and Friday throughout the summer, mostly of the DevClash that wrapped up recently.  

Before we leave you for the summer, did you know that we added several historical figures that can appear under the right circumstances? Here’s an overview written by Ola, known as [@Vaniljkaka](https://forum.paradoxplaza.com/forum/members/1630093/) here on the forums!  
> **Abbas ibn Firnas** (~810-887), known in Latin as Armen Firman, was an Andalusian polymath. Sources claim that he made an attempt at flight by jumping from a tower in Córdoba clad in a loose cloak stiffened with wooden struts. For this, he got immortalized, and now has a statue outside Baghdad’s airport. Though Ibn Firnas would be alive in our 867 bookmark, you’ll only encounter him if the right event fires.
>
> **al-Zahrawi** (936–1013), known as Albucasis in Latin, was one of the greatest surgeons of the Middle Ages, and court physician to the caliph in Córdoba. If you manage to encounter him in the game (you’ll need some luck for this, and an event about medicine…), he’ll even tell you an anecdote from his career.
>
> **Ibn al-Wafid** (997 – 1074), known as Abenguefith in Latin, was a pharmacist and agronomist in Toledo in the middle of the 11th century. Historical sources claim that he was a pupil of al-Zahrawi, but this seems improbable, as al-Zahrawi died before 1013. Ibn al-Wafid is a great court physician if you play emir Yahya in the Rags to Riches bookmark.
>
> **Al-Zarkali** (1029-1100), known in Latin as Arzachel, was a craftsman and astronomer based in Toledo. He fled the city when Castille conquered it in 1085. His work formed part of the basis for the Toledan Tables, a set of astronomical tables that were later translated into Latin by Gerard of Cremona. He is in the court of Toledo in the 1066 start.
>
> **Joseph ibn Nagrela** (1035-1066), also known as Joseph ha-Nagid, was vizier to the incompetent, alcoholic emir Badis of Granada. Ibn Nagrela belonged to a prominent lineage of Sephardic Jews; his father Samuel was a famous scholar, warrior, and poet. Ibn Nagrela was the chief victim of the Granada Massacre in December 1066, crucified by an angry mob for supposedly trying to usurp the throne. However, our game begins in January 1066, so perhaps he will fare better in this history…
>
> **Ibn Zuhr** (1094-1162), known in Latin as Avenzoar, was a physician and poet, who seems to have had a dramatic fallout with one of his employers, the Almoravid ruler. This fallout was very much the inspiration for one of the events in Struggle for Iberia…
>
> **Ibn Tufail** (1105 – 1185), known in Latin as Abubacer Aben Tofail, was a physician, novelist, and astronomer, among other things. He was quite keen on autopsies, as you’ll notice if you encounter him, which will require the right event at the right time.
>
> **Gerard of Cremona** (~1114-1187) was an Italian translator of scientific books from Arabic into Latin, active in the kingdom of Castille. After the fall of Toledo, his work was instrumental in making Arabic knowledge available to the Western European intellectual sphere, ushering in the “Renaissance of the Twelfth Century”. Gerard can be encountered if you get an appropriate event during the years when he was active - make sure that conciliation is the prevailing mood in Iberia!
>
> **Ibn Rushd** (1126-1198), known in Latin as Averroes, was a polymath and jurist and one of the most influential intellectuals of the Middle Ages, with a whole school of thought, averroism, that bears his name. In his youth, he seems to have been a pupil of both Ibn Zuhr and Ibn Tufail. There seem to be claims that he experimented with flight, just like ibn Firnas. Though he is very famous, he lived after our game’s current bookmark dates, and you’ll only encounter him with a bit of luck through an event in the right time period…
>
> **Qasmuna** (11th-12th century) was a female Sephardi poet. Some of her poems are preserved, but little is known of her life. However, there is a theory that she was the sister of Joseph ibn Nagrela. I chose to go with this, since it made their family tree more interesting and allowed us to include her in the game. You’ll likely find her with her brother in the court of Granada.
>
> Click to expand...


We are excited to come back refreshed and relaxed after vacation, and resume working on the game that we all know and love! Until August, goodbye!

<!-- artifact:reactions:start -->
- 72 Like
- 24 (unlabeled — rendered as base64 data URI)
- 17 (unlabeled — rendered as base64 data URI)
- 7 Love
- 5 (unlabeled — rendered as base64 data URI)
- 3 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
