---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1279641/"
forum_thread_id: 1279641
content_type: reply_thread
parent_dd_file: dd_003_2019-11-12_dev-diary-3-war.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 3
title: War
dd_date: 2019-11-12
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
pages_captured: 2
reply_count: 8
participant_count: 7
reply_date_first: 2019-11-12
reply_date_last: 2019-11-14
body_word_count: 135
inline_image_count: 1
quoted_span_count: 3
extraction_command: 'python3 extract_replies.py <pages...> --forum-id 1279641'
extraction_rationale: |
  Full reply thread captured across 2 page dump(s). Each XenForo
  post segmented on its author card; timestamp, permalink, body,
  quoted material, and reaction tally located by deterministic regex.
  Quotes and reactions preserved-and-flagged, never deleted, so the
  community body text can be distant-read alongside the dev-diary corpus.
detected_artifacts:
  - type: quoted_text
    action: preserved_and_flagged
    note: XenForo quote spans wrapped in artifact:quote; excluded from reply word counts.
  - type: reactions
    action: preserved_and_flagged
  - type: forum_chrome
    action: discarded_from_output
    note: pagination, control rows (Add bookmark/Report/Share), badge icon lists.
notes_for_analyst: |
  Reply corpus parallel to the dev-diary corpus. Body text is the union
  of all reply post bodies (OP excluded — see parent_dd_file). Strip
  YAML + artifact comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — War

*8 replies from 7 participants*

## Reply 1 — HrothgarTheBold · Nov 12, 2019 · post-25512345
<!-- post_author_url: https://forum.paradoxplaza.com/forum/members/hrothgarthebold.111222/ -->

This looks fantastic. The men-at-arms system sounds way more tactical than CK2 levies.
I really hope counters matter — pikes beating cavalry and so on.

<!-- artifact:reactions:start -->
- 23 Like
<!-- artifact:reactions:end -->

## Reply 2 — SiegeEnjoyer · Nov 12, 2019 · post-25512377
<!-- post_author_url: https://forum.paradoxplaza.com/forum/members/siegeenjoyer.333444/ -->

<!-- artifact:quote:start -->
Servancour said:
Levies are conscripted peasants forced to do your bidding.
Click to expand...
<!-- artifact:quote:end -->

So can we finally disband levies during harvest season? Asking for my starving peasants.

<!-- artifact:reactions:start -->
- 8 Haha
<!-- artifact:reactions:end -->

## Reply 3 — MapStarer · Nov 13, 2019 · post-25513001
<!-- post_author_url: https://forum.paradoxplaza.com/forum/members/mapstarer.555666/ -->

Will supply limits and terrain affect army movement? Mountains should slow big stacks.

## Reply 4 — QuietLurker · Nov 13, 2019 · post-25513099
<!-- post_author_url: https://forum.paradoxplaza.com/forum/members/quietlurker.777888/ -->

![](https://forumcontent.paradoxplaza.com/data/attachments/meme.png)

<!-- artifact:reactions:start -->
- 41 Love
<!-- artifact:reactions:end -->

## Reply 5 — HrothgarTheBold · Nov 13, 2019 · post-25513150
<!-- post_author_url: https://forum.paradoxplaza.com/forum/members/hrothgarthebold.111222/ -->

<!-- artifact:quote:start -->
MapStarer said:
Mountains should slow big stacks.
Click to expand...
<!-- artifact:quote:end -->

Agreed. Attrition plus terrain modifiers would make campaigns feel medieval instead of a deathball race.

<!-- artifact:reactions:start -->
- 12 Like
<!-- artifact:reactions:end -->

## Reply 6 — DefenderOfFaith · Nov 14, 2019 · post-25514220
<!-- post_author_url: https://forum.paradoxplaza.com/forum/members/defenderoffaith.999000/ -->

Holy wars were my favourite part of CK2. Glad to see religious casus belli return with more depth.

<!-- artifact:reactions:start -->
- 19 Like
<!-- artifact:reactions:end -->

## Reply 7 — NumbersGoblin · Nov 14, 2019 · post-25514301
<!-- post_author_url: https://forum.paradoxplaza.com/forum/members/numbersgoblin.121212/ -->

Please expose the combat width and damage formulas in the defines so modders can rebalance. Transparency on the math would be huge.

<!-- artifact:reactions:start -->
- 31 Like
<!-- artifact:reactions:end -->

## Reply 8 — Servancour · Nov 14, 2019 · post-25514455
<!-- post_author_url: https://forum.paradoxplaza.com/forum/members/servancour.465268/ -->

<!-- artifact:quote:start -->
NumbersGoblin said:
expose the combat width and damage formulas
Click to expand...
<!-- artifact:quote:end -->

Most of it lives in script and defines, yes — we want this very moddable. More in a future diary.

<!-- artifact:reactions:start -->
- 57 Love
<!-- artifact:reactions:end -->

