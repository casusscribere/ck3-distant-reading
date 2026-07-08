---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1550055/"
forum_thread_id: 1550055
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 110
title: "Dev Diary #110 - A Study in Black"
dd_date: 2022-10-25
author_handle: Fogbound
expansion: Friends and Foes
patch: Patch 1.8 (Robe)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2648
inline_image_count: 5
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1550055'
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
    location: raw_lines_~28_to_120
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_122_to_123
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_340_to_341
    action: preserved_and_flagged
    counts:
      Like: 3
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_418_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #110 - A Study in Black

<!-- artifact:thread_metadata:start -->
- Thread starter [Fogbound](https://forum.paradoxplaza.com/forum/members/fogbound.1203045/)
- Start date [Oct 25, 2022](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-109-floor-plan-for-the-future.1546534/ "Dev Diary #109 - Floor Plan for the Future") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-111-1-8-0-robe-feature-highlight.1546936/ "Crusader Kings 3 Dev Diary #111 - 1.8.0 “Robe” Feature Highlight")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/?prdxDevPosts=1)

- [Oct 25, 2022](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/post-28558334)
- [Replies: 73](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/#posts)


- [/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/post-28558334](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/post-28558334)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28558334/bookmark "Bookmark")

Greetings!  

A few weeks ago we shared our floor plan for the future, and this week I’d like to give you some tidbits from the studio itself. I will tell you a bit about the history of our studio and what we are about - interlaced with random quotes from the team collected throughout the year (courtesy of Wokeg - I think they paint a pretty accurate picture of the minds in our midst).  
So if you are eagerly awaiting updates on what’s coming for the actual game, I’m afraid you will have to wait a little longer.  

Firstly though, a brief introduction might be in order since I am very much a ‘behind the scenes’ kind of character *(and you will rarely catch me writing diaries)*:  
I was the Lead Producer on Crusader Kings III (until after its release in 2020). Having then spent some time with the space faring folks over in the Stellaris studio, I rejoined the CK3 team at the start of this year to create Studio Black - home of Crusader Kings - as the Studio Manager. And here we are.  

![Quote_pt1.png](https://forumcontent.paradoxplaza.com/public/881733/Quote_pt1.png "Quote_pt1.png")


*Random quotes, part 1*  


### PDS - A Tale of Studios​


The story of Paradox Development Studio goes back more than a quarter of a century - a pretty incredible feat in itself and a testament to the sheer talent, passion and motivation of the people working here. As we’ve added more games and grown the studio over the years, there came a point where we wanted to get the studio closer to to our games again, and at the end of 2020 PDS was divided into three sub-studios: **Green** (Stellaris), **Gold** (Hearts of Iron) and **Red** (Crusader Kings & Victoria). At this point, our friends at Europa Universalis had already set sail to warmer latitudes and set up **Tinto** in Spain.  

As Victoria III was ramping up their efforts (*and a big shout-out and CONGRATULATIONS is in order - the release is happening TODAY* ![:D](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Big Grin    :D") ), it was time to build a castle of our own, hence studio **Black** was born on February 14th (I’m sure you can figure out why I chose this date).  

![Quote_pt2.png](https://forumcontent.paradoxplaza.com/public/881734/Quote_pt2.png "Quote_pt2.png")


*Random quotes, part 2*  


### Court Positions​


Having the right people in the right place is of course paramount to any kind of development - in our case, that means we rely on our **Programmers**, **Designers**, **Artists**, **QA Testers** and **Producers** to bring our game to life, with the help of central support from **Audio**, **Engine Team**, **User Research**, **Marketing** and many other departments.  
Building a studio around an existing development team is quite a luxury - most often, you would start from scratch; with limited funding, resources and just a great dream (and hopefully a team) to carry you forward. In our case, it was rather the other way around (great game & team = check!), which means we can focus more on filling skill gaps and making sure we have a good support structure in place.  

![Quote_pt3.png](https://forumcontent.paradoxplaza.com/public/881735/Quote_pt3.png "Quote_pt3.png")


*Random quotes, part 3*  


### Character DNA​


You might think that with the roots firmly planted in the dynasty of PDS, we all share the same culture DNA? You’d be wrong. Something I discovered back in the day (moving from the EU4 team to the CK2 team at the time), was how some subtle, yet noticeable, parts of the team culture seemed to stem from a very central core. This theory was confirmed as I stepped away to the realm of Stellaris for a while; the essence of the project team culture was as firmly rooted around Jeff and other shared moments as CK ever was around… keeping it in the family.  
However quirky and meme-friendly each game teams culture might be, there are also some very noticeable similarities that confirms what Paradox is very much about, when it boils down to it: Helpful, Curious & Nerdy (in that *‘Hey, I’m really into cross-stitching medieval tapestry, want to know more?’* kind of way).  

![Quote_pt4.png](https://forumcontent.paradoxplaza.com/public/881737/Quote_pt4.png "Quote_pt4.png")


*Random quotes, part 4*  

### Keeping the Legacy​


So where are we headed as a studio, you might ask? Well, we are all here to keep the legacy of Crusader Kings alive and well. We have an amazing game at the earlier stage of its lifespan, and a team of highly creative and skilled people to help realize the incredible potential of CK3. I won’t pretend that 2 years of pandemic haven’t had an impact on our work, but we are truly committed to keep making releases for CK3 that we are proud of - and that we hope you will find hundreds (maybe thousands?) of hours of enjoyment from, for many years to come!  


That’s it for today folks, next time we’ll have some more game specific updates for you all!  

![CK3_Team.png](https://forumcontent.paradoxplaza.com/public/881739/CK3_Team.png "CK3_Team.png")


*A part of our team, having a royal blast at this year's PDXCON!*

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/28558334/report)

Click to expand...

[![Fogbound](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/m/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/fogbound.1203045/)

Written by

### [Fogbound](https://forum.paradoxplaza.com/forum/members/fogbound.1203045/)

Recruit

-

Messages
9

-

Reaction score
454

- [1](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/page-3#posts)
- [4](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/page-4#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/page-2#posts)

1 of 4

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/page-4#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/?order=prdx_dd_reaction_score)

[![Surtur01](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/ck3/s/avatar_28.png)](https://forum.paradoxplaza.com/forum/members/surtur01.149090/)

#### [Surtur01](https://forum.paradoxplaza.com/forum/members/surtur01.149090/)

##### Production Director - Crusader Kings 3

**139 Badges**

Aug 7, 2009

48

62

[steamcommunity.com](https://steamcommunity.com/id/Surtur/)

- ![Supreme Ruler 2020](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SR2020.gif "Supreme Ruler 2020")
- ![Heir to the Throne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/httt_forum_icon.png "Heir to the Throne")
- ![Hearts of Iron III: Their Finest Hour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/TFH_forumicon.png "Hearts of Iron III: Their Finest Hour")
- ![Hearts of Iron III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi3_forum_icon.gif "Hearts of Iron III")
- ![Galactic Assault](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ga_icon.gif "Galactic Assault")
- ![For the Motherland](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FTM1.png "For the Motherland")
- ![For The Glory](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Ftg_medal.png "For The Glory")
- ![Mount &amp; Blade: Warband](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/WARBAND.png "Mount &amp; Blade: Warband")
- ![Lost Empire - Immortals](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/LostEmpire.gif "Lost Empire - Immortals")
- ![Divine Wind](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3DW_forumicon.png "Divine Wind")
- ![Europa Universalis III Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu3_complete.gif "Europa Universalis III Complete")
- ![Victoria 2: A House Divided](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2AHD_forumicon.png "Victoria 2: A House Divided")
- ![East India Company](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eic_icon.gif "East India Company")
- ![Darkest Hour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DHicon.gif "Darkest Hour")
- ![Victoria 2: Heart of Darkness](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v2hod_icon.png "Victoria 2: Heart of Darkness")
- ![Hearts of Iron II: Armageddon](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/armageddon.gif "Hearts of Iron II: Armageddon")
- ![Cities in Motion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/cim_forum_icon.png "Cities in Motion")
- ![Sword of the Stars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/icon_Final_BLUE.png "Sword of the Stars")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Semper Fi](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/sefi.png "Semper Fi")
- ![War of the Vikings](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/warofthevikings_forum_icon.png "War of the Vikings")
- ![Warlock: Master of the Arcane](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/warlock_forumicon.png "Warlock: Master of the Arcane")
- ![Victoria: Revolutions](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/victoriarevolutions.gif "Victoria: Revolutions")
- ![Supreme Ruler: Cold War](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SRCW.png "Supreme Ruler: Cold War")
- ![Commander: Conquest of the Americas](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/cota.gif "Commander: Conquest of the Americas")
- ![Starvoid](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/starvoid_icon.png "Starvoid")
- ![Majesty 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/m21.gif "Majesty 2")
- ![Warlock 2: The Exiled](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/warlock2_forum_icon.png "Warlock 2: The Exiled")
- ![Europa Universalis IV: El Dorado](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_eldorado_forumicon.png "Europa Universalis IV: El Dorado")
- ![Ship Simulator Extremes](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/shipsim.png "Ship Simulator Extremes")
- ![Europa Universalis III Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nap_icon.gif "Europa Universalis III Complete")
- ![War of the Roses](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/wotr_icon.png "War of the Roses")
- ![Majesty 2 Collection](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/m_gold.png "Majesty 2 Collection")
- ![Europa Universalis IV: Mare Nostrum](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_marenostrum.png "Europa Universalis IV: Mare Nostrum")
- ![King Arthur II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/KAII.png "King Arthur II")
- ![Europa Universalis III Complete](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/in_nomine_icon_forum.gif "Europa Universalis III Complete")
- ![Impire](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/impire_icon.png "Impire")
- ![Teleglitch: Die More Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/teleglitch_icon.png "Teleglitch: Die More Edition")
- ![Rise of Prussia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/riseofprussia.png "Rise of Prussia")
- ![Europa Universalis IV: Common Sense](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cs_forumicon.png "Europa Universalis IV: Common Sense")
- ![Pillars of Eternity](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/PillarsOfEternity_forumicon.png "Pillars of Eternity")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Achtung Panzer](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/achtung_medal.png "Achtung Panzer")
- ![500k Club](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/500k_red.png "500k Club")
- ![Mount &amp; Blade: With Fire and Sword](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/WFAS.png "Mount &amp; Blade: With Fire and Sword")
- ![Hearts of Iron IV: No Step Back](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/NSB_forum_icon_16x16.png "Hearts of Iron IV: No Step Back")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Pride of Nations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/PoN.png "Pride of Nations")
- ![The Showdown Effect](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tse_forum.png "The Showdown Effect")
- ![Cities in Motion 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CIM2forumIcon.png "Cities in Motion 2")

[](javascript:;)

- [Oct 25, 2022](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/post-28561275)


- [/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/post-28561275](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/post-28561275)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28561275/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-110-a-study-in-black.1550055/post-28561275)

Hey all,  

As our Studio Manager is unavailable, I will be around for a little bit to answer questions where I can.

<!-- artifact:reactions:start -->
- 3 Like
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
