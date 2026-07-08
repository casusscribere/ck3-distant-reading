---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1456752/"
forum_thread_id: 1456752
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 48
title: "CK3 Dev Diary #48 - The Team"
dd_date: 2021-02-16
author_handle: Imse Vimse
expansion: Northern Lords
patch: Patch 1.3 (Corvus)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2835
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1456752'
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
    location: raw_lines_343_to_345
    action: preserved_and_flagged
    counts:
      Like: 14
      Haha: 8
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_384_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #48 - The Team

<!-- artifact:thread_metadata:start -->
- Thread starter [Imse Vimse](https://forum.paradoxplaza.com/forum/members/imse-vimse.1136414/)
- Start date [Feb 16, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-47-happy-holidays.1448340/ "CK3 Dev Diary #47 - Happy Holidays!") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/ "Crusader Kings 3 Dev Diary #49 - A Cold Embrace")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/?prdxDevPosts=1)

[Threadmarks](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/threadmarks "Threadmarks")

[View all 1 threadmarks](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/threadmarks)

---
[Reader mode](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/reader/)

---


#### Recent threadmarks

[Moderator Warning](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/page-10#post-27296286 "Threadmark created by Had a dad on Feb 16, 2021")

[Reader mode](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/reader/)

- [Feb 16, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/post-27292520)
- [Replies: 299](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/#posts)


- [/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/post-27292520](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/post-27292520)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27292520/bookmark "Bookmark")

Greetings!  

It’s a new year, and we thought it would be interesting to give all of you an update on the status of the team! There’s quite a few of us, and we hope you’ll enjoy this brief insight into who’s working on updates, fixes and exciting new content for your enjoyment!  

My name is Carmille and I work as a Producer on CK3; I’ve been with the team for about one and a half years now. CK2 was one of my favorite games and the reason that I joined Paradox to begin with, so naturally I am feeling quite blessed to work on the project ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")  

Firstly, an announcement! It has been decided that Alexander Oltner (aka [@rageair](https://forum.paradoxplaza.com/forum/members/375731/)) will be stepping up as the new Game Director for the project! Alexander is the (now former) Design Lead for CK3, and has spent many years designing features for both CK2 and CK3. He started at the company in 2015 and, if you’ve tuned in to any of the pre-release streams or interviews, you surely know who he is already. Long-term fans might even recognize him as the lead designer behind Holy Fury for CK2, or perhaps you’ve seen him in one of the many past Dev Clashes. We have full confidence that Alex will be able to take up the reins and steer the project towards a bright future! The former Game Director, Henrik Fåhraeus (known on the forums as Doomdark), is ascending the ranks and will instead act as the Creative Director for many titles, CK3 included.  

With that said, let's move on to the team itself!  
You might think that with the release of the base game, the amount of people working on the project would be reduced. We’re actually doing the exact opposite, and are in the process of expanding the team instead! This will give us a lot more flexibility and freedom and should allow us to work on several different things at the same time.  
Naturally, we need to train and onboard our new team members so it is not something we can start with straight away, but our hope is that you will see the effects within a not so distant future.  

Now, how many are actually working on CK3 and what are they doing?  

The team is made up of many different disciplines, working together to create amazing experiences! We’ll go into more details on each of them below.  

#### **Producer**​

We have four people working in Production (myself included). Our job is to help the team bring the design to life and into your hands. We do this by setting up (and iterating upon) processes and workflows, identifying deadlines and milestones, making plans to hit those dates while staying in good shape and ensuring that everybody knows what to do. We can often be seen grooming CK3s task and bug database and making sure everything is according to plan, up to date and representative of the current situation as well as spending a lot of time looking at numbers in spreadsheets.  

#### **Game Design**​

Our Game Designer is working very closely together with the Game Director. Their focus is split between what is currently being developed and nailing down the design for future expansions. They can very frequently be seen playing the game as it is being developed and make tweaks or highlight areas of concern so that the feature feels as great in the game as it looks on paper.  

#### **UX Design**​

Just like Game Design, our two UX Designers have their focus split between what is happening in the game right now and what is being designed for future expansions. UX Design and Game Design work closely together and make sure that new features are both fun and user friendly. They focus on interactions and user interface, although they can often be seen giving feedback on when something just doesn’t feel intuitive.  

#### **Content Design**​

Although the two previously mentioned design disciplines can sometimes be seen creating content for features as they are being developed, it's the Content Designers that create the vast majority of it. We have eight Content Designers working on CK3, and unlike the other two Design disciplines, they are almost entirely focused on working with what’s being developed in the game here and now. They pride themselves on creating historically plausible content, and will spend a lot of their time researching something before it is being put into the game. They are skilled scripters and writers and very passionate about ensuring that all features have a soul made out of supportive events, decisions, interactions, etc.  

#### **Code**​

There are seven Programmers and two Tech Leads working on CK3. The Tech Leads are responsible for the overall technical health and spend a lot of their time setting up (and iterating upon) processes and best practices for the project. They play a major part during all development stages and are constantly aware of the big picture and the challenges that could come with it.  

Our Programmers are responsible for building the functionality and foundation of the features themselves. They work very closely together with the other disciplines on their features and can often be seen providing Code Support or in other ways using their skillset to make life easier for the non-coders. They will also keep an eye on performance and the overall stability of the game and jump upon an issue as soon as it appears.  

#### **Art Director** ​

There is one Art Director working on CK3, and their responsibility is the overall artistic vision. They work closely together with the Game Director and Production, but also with all of the Artists in the team.  

#### **2D UI Art**​

We have three 2D Artists on the team and they can often be seen collaborating with Code and UX Design to bring the interfaces of new CK3 features to life after Code has provided their framework. They will also create icons and illustrations as well as investigate artistic improvements to the UIs that is not part of the UX design.  

#### **2D Concept Art** ​

Our two Concept Artists help the game team by visualizing assets before they are to be created by a 3D Artist.  

#### **3D Character Art** ​

Just as the name indicates, our three Character Artists work on anything related to our characters. This not only includes the characters itself, but also the clothing, headgears and hairstyles. In addition to that they are also responsible for creating the Units that are walking around the map. They can often be seen working closely together with Animation.  

#### **3D Environment Art** ​

These Artists work mostly on the map itself. We have four of them and they can often be seen creating holdings, ships, siege weapons and other map assets. They are also painting the map as well as making sure that all the units, holdings and other buildings are located where it makes sense, both from a historical perspective and an artistic one.  

#### **Animation**​

There is one Animator working on the project and their main focus is on bringing our characters and units to life. They can be seen working on brand new poses and adding more variety to existing ones to make sure the characters show a wide range of different emotions and visually support different situations.  

#### **VFX** ​

CK3 is not a very VFX heavy game, and because of this we do not have a VFX artist working with us full time, but only on demand.  

#### **QA**​

Our QA is the glue that keeps everything together. We have a core team of seven QA, but expand to a lot more once we are starting to wrap up and getting ready for a release. They can often be seen playing the game and testing the new features as they become ready, but it is important to note that this is not the only thing they do. They have a holistic view of quality and work closely together with all disciplines to make sure that the end product is as great as possible. Sometimes this is achieved through testing alone, but other times they can identify a need to redesign / introduce more content to a feature that feels a bit weak or perhaps a need to tweak a process or workflow within the Project itself.  

#### **Audio**​

The Audio team works on all PDS games, so we can’t really claim them for ourselves.  
When they do work on CK3, they are often around two to three people and can be seen working on sound effects for our new features as well as composing music that fit the theme of the expansion.  

Naturally, we don’t all work on the same features or fixes at the same time, that’d be very confusing! We’re divided into smaller groups, each focusing on their own set of features or content. Once a week we have a couple of hours set aside to make sure that everybody on the CK3 team has time to sit down and play the game and see for themselves how everything is being tied together.  

The team is currently busy working on two things: one is big and the other is smaller. The smaller of these you'll be hearing more of in the coming weeks...

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27292520/report)

Click to expand...

[![Imse Vimse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/m/ck2_dev.png)](https://forum.paradoxplaza.com/forum/members/imse-vimse.1136414/)

Written by

### [Imse Vimse](https://forum.paradoxplaza.com/forum/members/imse-vimse.1136414/)

Producer, CK3

Your friendly neighborhood spider.

-

Messages
1.769

-

Reaction score
289

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [15](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/page-15#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/page-2#posts)

1 of 15

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/page-15#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/?order=prdx_dd_reaction_score)

[![Almas](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/Sengoku/s/sng_rokkaku.png)](https://forum.paradoxplaza.com/forum/members/almas.1476365/)

#### [Almas](https://forum.paradoxplaza.com/forum/members/almas.1476365/)

##### First Lieutenant

**16 Badges**

Oct 19, 2019

243

1.368

- ![Cities: Skylines](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/csl.png "Cities: Skylines")
- ![Cities: Skylines - After Dark](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CS_AD_16x16_fotumicon.png "Cities: Skylines - After Dark")
- ![Hearts of Iron IV: Cadet](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Cad.png "Hearts of Iron IV: Cadet")
- ![Hearts of Iron IV: Together for Victory](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4Tfv.png "Hearts of Iron IV: Together for Victory")
- ![Hearts of Iron IV: Death or Dishonor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4DoD.png "Hearts of Iron IV: Death or Dishonor")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MtGicon.png "Hearts of Iron IV: Expansion Pass")
- ![Hearts of Iron IV: La Resistance](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoILRicon.png "Hearts of Iron IV: La Resistance")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Hearts of Iron IV: Battle for the Bosporus](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/bftb.png "Hearts of Iron IV: Battle for the Bosporus")
- ![Victoria 3 Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v3_signup_forum_icon.png "Victoria 3 Sign Up")
- ![Hearts of Iron IV: By Blood Alone](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BBA_forum_icon_16x16.png "Hearts of Iron IV: By Blood Alone")
- ![Hearts of Iron IV: No Step Back](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/NSB_forum_icon_16x16.png "Hearts of Iron IV: No Step Back")
- ![Hearts of Iron IV: Arms Against Tyranny](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/AAT_forum_icon_16x16.png "Hearts of Iron IV: Arms Against Tyranny")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")

[](javascript:;)

- [Feb 16, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/post-27294513)


- [/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/post-27294513](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/post-27294513)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27294513/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/post-27294513)

YES

 

- 33

<!-- artifact:reactions:start -->
- 14 Like
- 8 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
