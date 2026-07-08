---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1498899/"
forum_thread_id: 1498899
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 83
title: "CK3 Dev Diary #83 - Adventurer Inspirations and Other Royal Court News"
dd_date: 2021-11-23
author_handle: Trin Tragula
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1378
inline_image_count: 11
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1498899'
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
    location: raw_lines_~28_to_147
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_146
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1795.jpg?1637619775
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_149_to_151
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_250_to_254
    action: preserved_and_flagged
    counts:
      Like: 107
      Love: 69
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_262_to_372
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_373_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1795.jpg?1637619775)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #83 - Adventurer Inspirations and Other Royal Court News

<!-- artifact:thread_metadata:start -->
- Thread starter [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)
- Start date [Nov 23, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-83-adventurer-inspirations-and-other-royal-court-news.1498899/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to another development diary for Crusader Kings 3: Royal Court!  
Today I am here to talk a bit more about one of the more special inspiration types, the Adventurer.  

As mentioned in an [earlier development diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-68-inspiration-never-dies.1485460/) inspiration will strike characters at various times and will mean that they have an artifact or a type of artifact that they want to make for someone who is willing to fund their work.  

The adventurer is a somewhat unique type of inspiration in that it is much less clear what this person will present to you in the end. Instead this is a character who knows that they want to undertake a journey to explore and look for an interesting thing for you and your court.  

![Screenshot of an inspired person being hired by the player.](https://forumcontent.paradoxplaza.com/public/763838/fundinspiration.png "Screenshot of an inspired person being hired by the player.")



How far away a region that an adventurer will want to target with their expedition is mainly dependent on their skill and generally the adventurer already knows where they want to head when they appear to seek your patronage. A highly skilled adventurer might leave the choice of destination up to you.  

Regardless of what destination an adventurer will aspire to travel to they will ask you what type of thing they should be looking for. You can let them decide for themselves as their adventure unfolds or you can ask them for a general category of object from the get go (see below).  
Depending on the adventurer skill you may even be able to ask them to look for something unique, which will make them actively search for one of the unique historical artifacts that exist in the game. Nothing is entirely certain though, and even an adventurer of low skill might run into something interesting if you tell them to keep an eye open for anything interesting, it is just less likely than asking someone with higher skill to do so.  

![Screenshot of an inspired person headed for Asia Minor, asking what type of artifact to look out for.](https://forumcontent.paradoxplaza.com/public/763835/choosegoal.png "Screenshot of an inspired person headed for Asia Minor, asking what type of artifact to look out for.")


The above are the most common choices, animal trophies, artwork or trinkets are all potential court artifacts that the adventurer can go looking for.  
When given free reins you may also end up with a piece of armor, or a weapon from that region (with a visual appearance and local technique to match). There is also a small chance that an adventurer who is told to trust their own instincts could return with something more rare and unique.  

![Screenshot of an adventurer who has run into a crocodile in a county along the Nile.](https://forumcontent.paradoxplaza.com/public/763836/crocodile.png "Screenshot of an adventurer who has run into a crocodile in a county along the Nile.")


As an adventurer sets out on a hunt for an artifact to please his employer he or she will send occasional updates to you. Apart from letting you know what happened in the various places the adventurer visited, these events will let you guide them further, potentially impacting the quality of what they bring you home in the end or the length of their journey.  

![Screenshot of an adventurer complaining about an Irish marsh](https://forumcontent.paradoxplaza.com/public/763841/terrain.png "Screenshot of an adventurer complaining about an Irish marsh")


The adventurer character will move around in the region their expedition has targeted, and events as well as their in-game location will reflect what barony they are currently in.  

![Screenshot of an adventurer who has gotten lost.](https://forumcontent.paradoxplaza.com/public/763839/lost.png "Screenshot of an adventurer who has gotten lost.")


Sometimes things don’t go as expected. Getting lost is not all bad though, as it might mean reaching a region that was otherwise too far away from where they started.  

![Screenshot of an adventurer who has run into bandits.](https://forumcontent.paradoxplaza.com/public/763833/bandits.png "Screenshot of an adventurer who has run into bandits.")


Travelling abroad is always a risk, even for a seasoned adventurer.  

![Screenshot of an adventurer who is discovered as never having left the home town of his employer, instead wasting the money on food and alcohol.](https://forumcontent.paradoxplaza.com/public/763840/pubcrawl.png "Screenshot of an adventurer who is discovered as never having left the home town of his employer, instead wasting the money on food and alcohol.")


Even the most promising explorers can sometimes turn out to be charlatans (or just be plagued by the stress of the expectations placed upon them).  

![Screenshot of a letter from an adventurer in Asia Minor.](https://forumcontent.paradoxplaza.com/public/763842/yoghurt.png "Screenshot of a letter from an adventurer in Asia Minor.")


Some updates are just short letters and the odd trinket.  

![Screenshot of an adventurer returning from the Netherlands with the hide of a defeated Bear.](https://forumcontent.paradoxplaza.com/public/763834/bear.png "Screenshot of an adventurer returning from the Netherlands with the hide of a defeated Bear.")



Eventually the adventurer will return and present you with their find. Depending on the goal you gave them this might be anything from a trophy made from a rare animal to a unique artifact.  

**Unique Artifacts**  

![Screenshot of the ark of the Covenant, resting in an Indian court.](https://forumcontent.paradoxplaza.com/public/763832/arkcovenant.png "Screenshot of the ark of the Covenant, resting in an Indian court.")



Unique artifacts are rarer things that don’t correspond to any of the existing non-adventurer inspirations. They can be relics like one of the swords of Mohammed (a court artifact to be displayed rather than something to fight your enemies with), they can also be great diamonds, or a weapon or crown once wielded by a known king of the past.  

As we mentioned in a previous diary, a unique or historical artifact is not always necessarily what it is claimed to be. As these artifacts are accepted as genuine by your contemporaries they do however make a certain impression on them, reflected in the artifact effects. In terms of rarity a much larger number of these unique artifacts will be rated higher than other artifacts you would run into in the game.  

Around 50 such artifacts can come to be found in the game, some of which might also exist in a court at start depending on the start date. Should these be lost at any point adventurers will be eligible to discover them again in their travels. What artifact is found during an adventurer depends on their skill as well as their destination, you won’t find Quernbiter on a journey in India (and also not unless you’ve played past a certain year).  


![Screenshot of an adventurer returning with an enormous diamond.](https://forumcontent.paradoxplaza.com/public/763837/diamond.png "Screenshot of an adventurer returning with an enormous diamond.")



Since adventurer inspirations are relatively more rare than other inspired characters we have also tried to balance the effects of unique artifacts in a way as to make them worthwhile even if they are meant to clearly not be supernatural.  

**And Now For Something Completely Different!**  

Howdy y’all!  

This year has not been without news of ALL sorts and we do our best to be the first to give you all your Crusader Kings news!  

This time is no exception and we are glad to announce without any further ado, that Royal Court will be released February 8th, 2022!  

This means your throne room will be the center of your kingdom - like it should be. Become a master of languages, founder of cultures, collector of relics, and more on your own path to become the greatest ruler of all time! Witness the features you have been expecting and even some you didn’t know you wanted.  

Feel free to check out our trailer  


[https://www.youtube.com/embed/E9DwUPsIWAg?wmode=opaque](https://www.youtube.com/embed/E9DwUPsIWAg?wmode=opaque)


- Pariah

<!-- artifact:reactions:start -->
- 107 Like
- 69 Love
- 12 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Trin Tragula](https://forum.paradoxplaza.com/forum/members/trin-tragula.18587/)**
Role: Game Designer - Crusader Kings 3
Badges: 36
Reaction score: 16,644

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
