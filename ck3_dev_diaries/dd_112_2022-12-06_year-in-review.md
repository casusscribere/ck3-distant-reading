---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1561106/"
forum_thread_id: 1561106
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 112
title: "Dev Diary #112 - Year in Review"
dd_date: 2022-12-06
author_handle: rageair
expansion: Friends and Foes
patch: Patch 1.8 (Robe)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1174
inline_image_count: 5
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1561106'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2150.jpg?1670333914
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_213_to_217
    action: preserved_and_flagged
    counts:
      Like: 108
      (unlabeled — rendered as base64 data URI): 4
      Love: 17
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_225_to_337
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2150.jpg?1670333914)
<!-- artifact:thread_banner:end -->

# Dev Diary #112 - Year in Review

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Dec 6, 2022](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-112-year-in-review.1561106/)
<!-- artifact:thread_metadata:end -->

Greetings!  

The wintery season is upon us, and soon most of us will be joining our friends & family (or friends & foes?) for the holidays - this is an excellent time to reflect on the year that has gone by, and look at all that we’ve done. I also wish to leave you with a small teaser of things to come (nothing major though, as mentioned before that communication will begin sometime in Q1 next year!)  

Early in the year, we released Royal Court, the first major expansion for CK3. With kings squabbling over who has the grandest court, impressive artifacts being crafted and displayed, court position holders scheming, and cultures diverging, hybridizing, and shifting - to name only a few things that were in the update - it’s safe to say that the game got a shakeup with lots of new things to do. We also drew a lot of good learnings from it, both from the process (which was undoubtedly troubled, seeing the state of the world at the time) and the reception. Good lessons that we’ll bring with us in the future.  

The Fate of Iberia followed and breathed new life into the Iberian peninsula. With content such as bonds of friendship stronger than iron, titles changing hands over a game of chess, and the revival of lost faiths (if you’re observant enough…) The Struggle, a central mechanical core surrounded by flavor, struck a balance that was enjoyed by many - a winning formula that we’re more than likely to follow in the future.  

Friends & Foes was an experiment that played to the strengths of the game - by adding dramatic content, and proved how it’s always a nice thing to have more of it! Not only did it seem to be an appreciated format, but it was very motivating for us to make. For more news on this, stay tuned early next year…  

And to round the year off we released the Robe update, which focused on adding graphical variety and fixing issues. It revamped the bookmark screen, added a full set of art for tenets, and made custom rulers saveable, in addition to balance and AI fixes. We will always strive to make sure the game is in a good, healthy state.  

---  

Now, some of you know the above already, and want to see something new! As we won’t be back with Dev Diaries for a while (they’ll start back up sometime in January) I want to leave you with something that can be discussed for a while. We’ve seen a lot of discussions regarding Nicknames, or rather the lack of them, and have taken your feedback to heart!  

In an upcoming update, we’ll be adding in a new system for gaining nicknames passively, not too unlike the system in CK2, but vastly improved (in CK2, it was just a highly obfuscated system with little-to-no fanfare at all). These nicknames can be earned at any point during the game, and will reflect your character’s status as well as they can. They can be bad or good, with most (if not all) being overwritable by more prestigious nicknames should you do something extraordinary (such as uniting the Spanish Thrones, or Uniting Africa, etc). Gaining a nickname comes with a small boon or penalty to prestige and opinion, just enough to make it matter.  

![nickname_event_1.png](https://forumcontent.paradoxplaza.com/public/911538/nickname_event_1.png "nickname_event_1.png")


*A positive nickname, celebrated by a good friend.*  

![nickname_event_2.png](https://forumcontent.paradoxplaza.com/public/911539/nickname_event_2.png "nickname_event_2.png")


*A negative nickname, gained while in prison, with the news delivered by someone who’s not exactly a fan of yours.*  

This system focuses on nicknames that aren’t particularly active, it won’t give you ‘the Conqueror’ for example. It will, however, pick one of 200+ appropriate passive nicknames. These are in part existing nicknames in the database that didn’t exist outside of historical characters (‘the Fat’, ‘the Poet’, ‘the Brave’, ‘the Tyrant’, etc.), nicknames adopted from CK2 (‘the Zealot’, ‘the Lucky’, ‘the Resilient’, ‘the Strange’, etc.), historical nicknames that were never used before (‘the Desired’, ‘the Idle’, ‘the Wrathful’, ‘Longsword’, etc.), and community suggestions (‘the Navigator’, ‘the Berserker’, etc.). All of these nicknames have triggers so that they only appear where logical, for example; you can only gain ‘the Tyrant’ if you have a certain amount of tyranny opinion, and you can only gain ‘the Fat’ if your character is of the heavier persuasion. A lot of these also take your prestige or piety levels into account, so having a high prestige level can ‘protect’ you from gaining poor nicknames. There’s also a game rule that controls the frequency.  


![nickname_snapshot.png](https://forumcontent.paradoxplaza.com/public/911540/nickname_snapshot.png "nickname_snapshot.png")


*Some examples of nicknames you can get through this system.*  

We aspire to keep most nicknames in line with history, or what would be plausible. That said, feel free to suggest more nicknames! Who knows, perhaps you’ll suggest something that’ll make it in… just remember that they shouldn’t be too ‘active’, so no ‘the Conqueror’ or ‘the Destroyer’.  

To make nicknames a bit more… spicy than they are, we’ve also added a small new feature that allows you to see what a nickname actually means! Charles the Bald, for example, wasn’t without hair but rather without a suitable crown for most of his life. By hovering over nicknames, you can now see an explanation.  


![nickname_reason_charles.png](https://forumcontent.paradoxplaza.com/public/911541/nickname_reason_charles.png "nickname_reason_charles.png")


*Charles wasn’t so bald after all, and now you know why.*  

![nickname_description_2.png](https://forumcontent.paradoxplaza.com/public/911542/nickname_description_2.png "nickname_description_2.png")


*Quite self-explanatory, but still informative.*  

Finally, a word from our community manager Pariah about a QnA session we will be having with some of the devs on our Discord server:  

*"As the holiday season approaches, we will also be holding a QnA session where you can feel free to ask any burning questions or just anything on your mind about the game. While we can’t give away any company secrets or tell you exactly what we are working on next, it will be a chance to sit down and discuss things with members from most if not all disciplines of the game!  

The QnA session will be taking place on our Discord server on Tuesday December 13 from 16:00 - 18:00 CET, which is a terrific place to help supplement these Forums. The Discord is filled with tons of your fellow Crusader Kings community and always a good place to find knowledge and conversation. If you are not already part of our terrific Discord family and would like to get in ahead of the QnA, you can find a link [HERE](https://discord.com/invite/ck3)!"*  

That’s it for this year - we’ll see you in 2023! Have a God Jul and a Gott Nytt År as we say here in the frigid north!

<!-- artifact:reactions:start -->
- 108 Like
- 29 (unlabeled — rendered as base64 data URI)
- 17 Love
- 9 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
