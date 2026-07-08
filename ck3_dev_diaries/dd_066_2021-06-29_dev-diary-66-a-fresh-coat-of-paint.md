---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1481298/"
forum_thread_id: 1481298
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 66
title: "CK3 Dev Diary #66 - A Fresh Coat of Paint"
dd_date: 2021-06-29
author_handle: Servancour
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2539
inline_image_count: 3
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1481298'
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
    location: raw_lines_~28_to_123
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_125_to_126
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_335_to_339
    action: preserved_and_flagged
    counts:
      Like: 31
      Love: 24
      Haha: 2
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
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

# CK3 Dev Diary #66 - A Fresh Coat of Paint

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Jun 29, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/ "CK3 Dev Diary #65 - One Culture Is Not Enough") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-67-a-view-to-a-map.1484762/ "CK3 Dev Diary #67 - A View to a Map")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/?prdxDevPosts=1)

- [Jun 29, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/post-27649706)
- [Replies: 123](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/#posts)


- [/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/post-27649706](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/post-27649706)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27649706/bookmark "Bookmark")

**CK3 Dev Diary #66 - A Fresh Coat of Paint**​

Greetings!  

The sun is out, and we’ve all been enjoying pristine Azure skies during the Swedish midsummer celebrations. Or, well, a few of us have! Some members of the team got to enjoy a massive downpour of rain (which is customary, to be fair), and others even got to experience a refreshing storm of hail. Speaking of Azure, we’re releasing another small patch today which addresses a handful of issues (most notably some stability concerns):  


Spoiler: Changelog

- Fixed unpause issues in multiplayer if choosing to continue in single player after network out of sync on 1.4.2
- Fixed crash on save and progressive dynasty and title coat of arms disappearing
- Fixed UI lists refresh, allowing to access characters for some interactions when they should not be available (i.e.: you could grant vassal to your liege characters from other realms)
- Fixed crash happening after starting a fort assault during a crusade on a long playthrough save on 1.4.2


Beginning next week a majority of the team will be going on summer vacation, which means that it’ll be mostly deserted for the next five weeks. In practice this means that the next few Dev Diaries won’t be as meaty as the ones that came before. You can think of them more as teasers than proper Dev Diaries. When we’re back we’ll of course resume having more substantial ones!  

With that being said, we don’t want to leave you empty handed. Summer vacation doesn’t start until *next* week after all. Some of you might have noticed in the previous Dev Diary that we had a small square at the top of the window when creating a hybrid or a divergent culture, showing a colour. This is of course a preview of the colour your new culture will have when it’s created. Clicking it allows you to change and set the colour of your culture exactly as you want it!  

![01_culture_colour_picker.png](https://forumcontent.paradoxplaza.com/public/722947/01_culture_colour_picker.png "01_culture_colour_picker.png")


*[Image of selecting a colour during culture creation]*​


But we didn’t stop there! We added this new and wonderful tool in a couple of other places as well. As when creating a culture, we've added it for creating a new faith too.  

![02_faith_colour_picker.png](https://forumcontent.paradoxplaza.com/public/722948/02_faith_colour_picker.png "02_faith_colour_picker.png")


*[Image of selecting a colour when creating a faith]*​


You'll also be able to change the colour when customizing a title. No longer will you have to settle on the colour the game picks for you when creating a custom kingdom or empire! Especially when that colour turns out to be neon pink... You can edit the colour for any title you hold or is held by your vassals, similar to how you are allowed to edit the name & adjective for titles in your realm. Yes, this means that you can make your vassal lands sport a cavalcade of colour if you so desire!  

![03_title_colour_picker.png](https://forumcontent.paradoxplaza.com/public/722949/03_title_colour_picker.png "03_title_colour_picker.png")


*[Image of selecting a colour when customizing a title]*​


That's it for today, I'm afraid. While this might be a fairly small addition in the grand scheme of things, we do think it’s a nice and flavourful tool that lets you customize your experience more than before!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27649706/report)

Click to expand...

[![Servancour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/obsolete/m/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/servancour.465268/)

Written by

### [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)

Game Designer

***Paradox Staff******4 Badges***

-

Messages
1.606

-

Reaction score
9.949

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [7](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/page-7#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/page-2#posts)

1 of 7

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/page-7#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/?order=prdx_dd_reaction_score)

[![Davisx3m](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/Imperatorsignupavatar/s/Imperatorsignup.png)](https://forum.paradoxplaza.com/forum/members/davisx3m.63616/)

#### [Davisx3m](https://forum.paradoxplaza.com/forum/members/davisx3m.63616/)

##### Long live love!

**98 Badges**

Dec 16, 2006

7.033

7.360

- ![Europa Universalis IV: Cossacks](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cossacks.jpg "Europa Universalis IV: Cossacks")
- ![Knights of Honor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/knightsofhonor.png "Knights of Honor")
- ![Europa Universalis IV: Mandate of Heaven](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/moh_forum_icon.png "Europa Universalis IV: Mandate of Heaven")
- ![Crusader Kings II: Monks and Mystics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/monksandmystics.png "Crusader Kings II: Monks and Mystics")
- ![Europa Universalis IV: Rights of Man](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rom_forum_icon.png "Europa Universalis IV: Rights of Man")
- ![Crusader Kings II: Reapers Due](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/reapers_due_forum_icon.png "Crusader Kings II: Reapers Due")
- ![Hearts of Iron IV: Cadet](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Cad.png "Hearts of Iron IV: Cadet")
- ![Stellaris Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Stellaris_SignUp_icon.png "Stellaris Sign-up")
- ![Hearts of Iron IV Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HOI_signup.png "Hearts of Iron IV Sign-up")
- ![Stellaris](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_base.png "Stellaris")
- ![Europa Universalis IV: Mare Nostrum](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_marenostrum.png "Europa Universalis IV: Mare Nostrum")
- ![Cities: Skylines - Snowfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/snowflake_16_4.png "Cities: Skylines - Snowfall")
- ![Crusader Kings II: Conclave](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DLC_icon_Conclave.png "Crusader Kings II: Conclave")
- ![Europa Universalis IV: Third Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/third_rome_forum_icon.png "Europa Universalis IV: Third Rome")
- ![Cities: Skylines - After Dark](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CS_AD_16x16_fotumicon.png "Cities: Skylines - After Dark")
- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Europa Universalis IV: Common Sense](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cs_forumicon.png "Europa Universalis IV: Common Sense")
- ![Humble Paradox Bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HumbleParadoxBundleIcon.png "Humble Paradox Bundle")
- ![Pillars of Eternity](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/PillarsOfEternity_forumicon.png "Pillars of Eternity")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Mount &amp; Blade: With Fire and Sword](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/WFAS.png "Mount &amp; Blade: With Fire and Sword")
- ![Mount &amp; Blade: Warband](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/WARBAND.png "Mount &amp; Blade: Warband")
- ![Rise of Prussia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/riseofprussia.png "Rise of Prussia")
- ![Europa Universalis IV: Pre-order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_special_forumicon.png "Europa Universalis IV: Pre-order")
- ![Europa Universalis IV: El Dorado](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_eldorado_forumicon.png "Europa Universalis IV: El Dorado")
- ![Shadowrun Returns](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Returns.PNG "Shadowrun Returns")
- ![Hearts of Iron IV: No Step Back](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/NSB_forum_icon_16x16.png "Hearts of Iron IV: No Step Back")
- ![Victoria 3 Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v3_signup_forum_icon.png "Victoria 3 Sign Up")
- ![Europa Universalis 4: Emperor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_emperor.png "Europa Universalis 4: Emperor")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Imperator: Rome - Magna Graecia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MagnGraeciaIcon.png "Imperator: Rome - Magna Graecia")
- ![Hearts of Iron IV: La Resistance](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoILRicon.png "Hearts of Iron IV: La Resistance")
- ![Imperator: Rome Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorsignup.png "Imperator: Rome Sign Up")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Europa Universalis IV: Golden Century](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gc_forum_icon.png "Europa Universalis IV: Golden Century")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Cities: Skylines](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/csl.png "Cities: Skylines")
- ![Europa Universalis IV: Dharma](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/dharmaicon.png "Europa Universalis IV: Dharma")
- ![Cities: Skylines - Parklife](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSLParkLife.png "Cities: Skylines - Parklife")
- ![Surviving Mars: Digital Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_DDE.png "Surviving Mars: Digital Deluxe Edition")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")
- ![Crusader Kings II: Jade Dragon](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2jd_forumicon.png "Crusader Kings II: Jade Dragon")
- ![Europa Universalis IV: Cradle of Civilization](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EUIV_CoC.png "Europa Universalis IV: Cradle of Civilization")
- ![Age of Wonders III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AoW3_forum_badge.png "Age of Wonders III")
- ![Hearts of Iron IV: Death or Dishonor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4DoD.png "Hearts of Iron IV: Death or Dishonor")
- ![PDXCon 2017 Awards Winner](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ParadoxAwards2017.png "PDXCon 2017 Awards Winner")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![Darkest Hour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DHicon.gif "Darkest Hour")

[](javascript:;)

- [Jun 29, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/post-27649943)


- [/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/post-27649943](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/post-27649943)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27649943/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/post-27649943)

C U S T O M I Z A T I O N !

 

Toggle signature

Owner of a Imperial Socialist P Ribbon ●  Winner of Preussen 1825 with my Vereinigte Preussische Partei!  Winner of Britain 1950 with my Communist Party of Britain!  Winner of Denmark 1900 with my Tyskliberala Monarkistpartiet.  
[A Town We Never Forget! My newest AAR](https://forum.paradoxplaza.com/forum/showthread.php?p=9884802#post9884802)  
*"We don't do marxistic historical games, where its mandatory that some countries will always fail." - Johan*  Follow me on [Bluesky](https://bsky.app/profile/davisx3m.bsky.social)!  
Biji Kurdistan!  
​

<!-- artifact:reactions:start -->
- 31 Like
- 24 Love
- 2 Haha
- 2 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
