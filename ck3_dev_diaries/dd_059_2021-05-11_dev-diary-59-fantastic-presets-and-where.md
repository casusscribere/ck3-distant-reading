---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1473458/"
forum_thread_id: 1473458
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 59
title: "CK3 Dev Diary #59 - Fantastic presets and where to save them"
dd_date: 2021-05-11
author_handle: KnightOfTheLions
expansion: Northern Lords
patch: Patch 1.4 (Azure)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2413
inline_image_count: 3
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1473458'
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
    location: raw_lines_313_to_315
    action: preserved_and_flagged
    counts:
      Like: 13
      Love: 3
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_376_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #59 - Fantastic presets and where to save them

<!-- artifact:thread_metadata:start -->
- Thread starter [KnightOfTheLions](https://forum.paradoxplaza.com/forum/members/knightofthelions.1585260/)
- Start date [May 11, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-58-stre-ss-tching-the-traits.1472092/ "CK3 Dev Diary #58 - Stre(ss)tching the traits") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-60-the-cost-of-warfare.1474533/ "CK3 Dev Diary #60 - The Cost of Warfare")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/?prdxDevPosts=1)

- [May 11, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/post-27520019)
- [Replies: 131](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/#posts)


- [/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/post-27520019](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/post-27520019)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27520019/bookmark "Bookmark")

Hello friends,  
Isn't it satisfying when things just work smoothly? If you agree then this Dev Diary will be right down your alley. I’m one of the jolly UX designers working on CK3 and today I’m very excited to give you a sneak peek of some of the quality of life improvements we have in store for the Azure free patch.  

We wanted to focus on some of the requests you've brought up, so we’ve worked to find organic ways to implement these in the game. While we can’t address all at once in a single patch, we still wanted to make some meaningful adjustments that will improve your time spent as medieval rulers, master strategists, and efficient trackers. Keep on reading to understand this last one.  

Today I’ll be covering *Raise Men-at-Arms*, *Game Rules Presets*, and *Character Search Presets*.  

**Raise only Men-at-Arms**  We had already mentioned that now you will be able to start your games with contingent Men-at-Arms regiments, but these troops have another nifty trick under their sleeves. Now you will be able to raise only Men-at-Arms, allowing you to subdue your enemies without having to bother your levies. Quite a power move, right?  

We know it’s dangerous to go adventuring alone, so raising Men-at-Arms will also raise your knights along with them. This ensures that you have a perfectly capable army to take on different challenges.  

This is how it works; you will find a button that allows you to raise only Men at Arms in your Military menu, clearly labeled “Raise all Men-at-Arms”. This button will also be present when selecting Rally Points. Hopefully, this will give you more freedom when planning the perfect military strategy.  


![MAA-button.jpg](https://forumcontent.paradoxplaza.com/public/704771/MAA-button.jpg "MAA-button.jpg")


*[Image of the Raise all Men-at-Arms action]*  
​

**Game Rules presets**  We all have different playstyles and sometimes it’s nice to spice things up by changing up the rules a bit. Sometimes we want to ask the Mongols to hold their horses and stay at home by turning off the Mongol Invasions, or maybe you want to see if you can withstand yearly visits from your friendly neighbors, the Norse invaders. To allow you to quickly change the rules, now you can save rules presets.  

To create your Game Rules presets, all you need to do is set the specific combination of rules that you want, and then click the save button at the top of the window. Doing this will open up a secondary window that lets you name, and save your presets. Loading the presets is very straightforward, all you need to do is to select the desired preset from the dropdown menu at the top of the window.  

![Game-Rules-presets.jpg](https://forumcontent.paradoxplaza.com/public/704775/Game-Rules-presets.jpg "Game-Rules-presets.jpg")


*[Image of the Game Rules Presets being saved]* ​


**Character Search presets**  I said that the Azure patch will improve your tracking skills, and this is thanks to the introduction of Character Search Presets. Much like Game Rules Presets, the idea is to allow you to save different combinations of search filters into presets you can easily select.  

You can save and load presets by using the 2 new buttons you’ll find at the top of the search filters window. That means that if you find yourself constantly searching for a specific mix of traits or any other search criteria, then keeping tabs on them will be much easier.  

![Search-Presets.jpg](https://forumcontent.paradoxplaza.com/public/704776/Search-Presets.jpg "Search-Presets.jpg")


*[Image of the new Character Search Preset buttons]*  
​

While this feature is very useful to streamline the process of recurrent searches with the same criteria, it still comes with some limitations, we are not able to save the dynamic objects in the filter (Dynasty, House and Custom Faith).  

That’s all for today, I sincerely hope these quality of life improvements help you try other gameplay styles and that character search presets will make it easier for you to find that special someone somewhere in this fantastic medieval world.  

Thanks for reading! Stay tuned for future updates on the Azure patch. Until next time!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27520019/report)

Click to expand...

[![KnightOfTheLions](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/m/stellaris_dev_avatar_ai_robot.png)](https://forum.paradoxplaza.com/forum/members/knightofthelions.1585260/)

Written by

### [KnightOfTheLions](https://forum.paradoxplaza.com/forum/members/knightofthelions.1585260/)

Recruit

-

Messages
2

-

Reaction score
380

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [7](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/page-7#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/page-2#posts)

1 of 7

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/page-7#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/?order=prdx_dd_reaction_score)

[![ToraktheNord](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/ck3/s/avatar_13.png)](https://forum.paradoxplaza.com/forum/members/torakthenord.1028984/)

#### [ToraktheNord](https://forum.paradoxplaza.com/forum/members/torakthenord.1028984/)

##### First Lieutenant

**37 Badges**

Aug 15, 2015

214

816

- ![Victoria 2: Heart of Darkness](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v2hod_icon.png "Victoria 2: Heart of Darkness")
- ![Europa Universalis IV: Cradle of Civilization](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EUIV_CoC.png "Europa Universalis IV: Cradle of Civilization")
- ![Europa Universalis IV: Mare Nostrum](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_marenostrum.png "Europa Universalis IV: Mare Nostrum")
- ![Hearts of Iron IV Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HOI_signup.png "Hearts of Iron IV Sign-up")
- ![Hearts of Iron IV: Cadet](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Cad.png "Hearts of Iron IV: Cadet")
- ![Crusader Kings II: Reapers Due](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/reapers_due_forum_icon.png "Crusader Kings II: Reapers Due")
- ![Europa Universalis IV: Rights of Man](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rom_forum_icon.png "Europa Universalis IV: Rights of Man")
- ![Crusader Kings II: Monks and Mystics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/monksandmystics.png "Crusader Kings II: Monks and Mystics")
- ![Europa Universalis IV: Mandate of Heaven](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/moh_forum_icon.png "Europa Universalis IV: Mandate of Heaven")
- ![Hearts of Iron IV: Death or Dishonor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4DoD.png "Hearts of Iron IV: Death or Dishonor")
- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Europa Universalis IV: Golden Century](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gc_forum_icon.png "Europa Universalis IV: Golden Century")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Imperator: Rome Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorsignup.png "Imperator: Rome Sign Up")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Victoria 3 Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v3_signup_forum_icon.png "Victoria 3 Sign Up")
- ![Europa Universalis IV: Common Sense](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cs_forumicon.png "Europa Universalis IV: Common Sense")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Europa Universalis IV: El Dorado](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_eldorado_forumicon.png "Europa Universalis IV: El Dorado")
- ![Victoria 2: A House Divided](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2AHD_forumicon.png "Victoria 2: A House Divided")
- ![Victoria 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2.png "Victoria 2")
- ![Europa Universalis IV: Cossacks](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cossacks.jpg "Europa Universalis IV: Cossacks")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Victoria: Revolutions](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/victoriarevolutions.gif "Victoria: Revolutions")
- ![Europa Universalis IV: Wealth of Nations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_won_forumicon.png "Europa Universalis IV: Wealth of Nations")
- ![Europa Universalis IV: Art of War](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aow_forum_icon.png "Europa Universalis IV: Art of War")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Europa Universalis IV: Conquest of Paradise](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cop_forumicon.png "Europa Universalis IV: Conquest of Paradise")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")

[](javascript:;)

- [May 11, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/post-27520224)


- [/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/post-27520224](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/post-27520224)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27520224/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-59-fantastic-presets-and-where-to-save-them.1473458/post-27520224)

Finally

 

- 47

<!-- artifact:reactions:start -->
- 13 Like
- 3 Love
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
