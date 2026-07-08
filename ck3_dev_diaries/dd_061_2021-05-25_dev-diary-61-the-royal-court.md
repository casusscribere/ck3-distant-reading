---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1476067/"
forum_thread_id: 1476067
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 61
title: "CK3 Dev Diary #61 - The Royal Court"
dd_date: 2021-05-25
author_handle: rageair
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3204
inline_image_count: 1
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1476067'
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
    location: raw_lines_333_to_335
    action: preserved_and_flagged
    counts:
      Like: 22
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 1 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_408_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #61 - The Royal Court

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [May 25, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-60-the-cost-of-warfare.1474533/ "CK3 Dev Diary #60 - The Cost of Warfare") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/ "CK3 Dev Diary #62 - Monarch’s Journey unleashed")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/?prdxDevPosts=1)

[Threadmarks](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/threadmarks "Threadmarks")

[View all 1 threadmarks](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/threadmarks)

---
[Reader mode](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/reader/)

---


#### Recent threadmarks

[1621938358,1621937583](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/page-2#post-27562259 "Threadmark created by rageair on May 25, 2021")

[Reader mode](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/reader/)

- [May 25, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/post-27561659)
- [Replies: 270](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/#posts)


- [/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/post-27561659](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/post-27561659)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27561659/bookmark "Bookmark")

Greetings!  

Welcome to the first Dev Diary for the Royal Court expansion! As we mentioned in a previous DD, we’ll go back to Azure patch DD’s for a few weeks after this one. But do not fear, there will be some more Royal Court DD’s before the summer holidays - and when we’re back from holidays we’ll have many, many Royal Court diaries for you!  

It’s really hard to pick a topic for where to start, but we decided upon a dive into the namesake feature of the expansion - the Royal Court itself, your seat of royal majesty and power! The Royal Court consists of many features, all collected within a 3D scene that we call the Throne Room.  

Here’s an early Work in Progress screenshot of the throne room - do note that it’s a ***very*** early version, but we just can't wait to show you what we have been working on!  


![RoyalCourtSceneExtremelyWIP.png](https://forumcontent.paradoxplaza.com/public/710991/RoyalCourtSceneExtremelyWIP.png "RoyalCourtSceneExtremelyWIP.png")


*[Image: An early WIP western-style Throne Room, not indicative of final quality]*  

Now, there are many things that go into the Royal Court itself. It interacts with numerous new features that’ll come with the expansion - we won’t go into detail on all of them today, if we did this DD would become much too long!  

It's worth noting that this isn’t just a graphical feature; while we admit the importance of immersion, we don't want any features to feel tacked-on or superfluous. The Throne Room is there to show what’s happening; what artifacts you’ve collected, which courtiers are having a fight, etc. This allows us to place your character in a scene together with others, showing that you’re actually present in the same world! We’re trying to bridge the gap between your character and the map, all while representing a side of medieval history we’ve never previously explored in detail - the importance for a ruler to show their power, their grandeur, to their subjects and peers.  

Every Feudal/Clan King and Emperor has a Royal Court. Tribal Rulers do not have one, as this feature primarily models the formality and ceremony surrounding the court, as well as the need for spending Gold, while Tribal rulers use Prestige as their main resource. If a ruler is demoted to a lower rank (through war, election, or just sheer bad luck) their Royal Court and everything therein will either stay dormant until you regain your lost status, or follow the character who now rules in your stead.  

**Grandeur**  
The key concept that enables this is called Grandeur - a measurement of your standing in the eyes of your peers. While it’s measured on a scale from 0-100, it’s not necessarily a simple system. Increasing your grandeur will lead to direct political benefits, such as increased opinions, marriage acceptance, etc. It will also unlock new Council Jobs, such as being able to peacefully demand De Jure land with the ‘Convince De Jure Territory’ job, or gain Knight Effectiveness while also decreasing enemy Scheme Success Chance with the ‘Manage Royal Guards’ job. These effects motivate you to aim for a high level of Grandeur, but naturally comes at a monetary cost. How much are you willing to spend on artifacts, amenities, or on positions within your court? You have to balance your political needs with your temporal ones, such as warfare or development. Sacrificing your grandeur entirely will cause instabilities both internal and external.  

Grandeur is not really a resource, and is not actively ‘spent’ - unlike something like Prestige. It works on a much slower timescale, and is something you must balance and work towards increasing over a longer period of time. Though there are of course choices in events that make Grandeur increase or decrease, with various trade-offs.  

**Grandeur Effects**  
As mentioned in the previous section, Grandeur has several different effects and modifiers. It is divided into 10 separate levels with their own effects. For example, the very first level of Grandeur unlocks the ability to Hold Court - which is a crucial component in achieving the higher Grandeur levels. The second level unlocks a Council Task called ‘Bestow Royal Favor’, which is a powerful single-target task that increases a vassal’s opinion of you while granting them, and you, prestige.  

One of the most significant effects of Grandeur is its effect on attraction of Inspired characters - the higher your Grandeur is compared to that of your neighbors, the likelier you are to have these creative travelers visit your court first, giving you an opportunity for patronage (more on Inspirations in a future DD).  

Some of these levels will give courtiers who stay within it a flavorful trait, which will increase their skills and attributes based on the type of court they’re staying at. A particularly grand court might even see a more powerful trait appear, making such characters excellent for various jobs and Court Positions (more on Court Positions in a later DD).  

Several Grandeur levels have effects and modifiers based on your Court Type - a type of flavorful perk for your court. Depending on your cultural Ethos you’ll get access to a few different types, such as a Diplomatic or Warlike Court. All royal courts have a type, and among other things it affects the type of trait that courtiers get (see previous paragraph). The bonuses granted from these types are varied and aim to enhance a certain style of play. The AI will tend to go for the Court Type most reflective of their Cultural Ethos and situation - for example, Indian Kings will often tend to want a Scholarly Court since many Indian cultures have a spiritual Ethos.  

As an example, having a Diplomatic Court Type will grant you bonuses to Vassalization acceptance, tyranny gain, opinion, and potentially even unlock a Personal Scheme slot. A Warlike Court Type might instead see bonuses to MaA counter efficiency, knight efficiency, and the maximum size of MaA regiments. As not all cultures can access all Court Types, this is another reason to pursue Hybridization or Divergence (more on that in a later DD).  

**How Grandeur is Gained**  
Grandeur is divided in two; baseline, and direct gain. The baseline decides the ‘trend’, with you passively (and slowly) either gaining or losing grandeur over time, until the baseline is met. The baseline is affected by many things; what Court Artifacts you have, what Court Positions you have filled, etc (more on Court Artifacts in a later DD). The rate of grandeur change can be modified by many things, such as Cultural Ethoses or Traditions, but is as a rule of thumb slow. It takes time for word of your glory to spread, after all!  

The most simple way to increase your Grandeur baseline is by investing in Amenities. Now, Amenities are simple and straightforward; but they’re still central to the concept of having a grand court! There are four different types; Lodgings, Food, Clothing and Servants. There are four levels to each, with each progressive level costing more gold to maintain, but giving more Grandeur baseline. They all come with a selection of flavor effects, for example; spending on food will slightly increase the disease resistance of your courtiers, but higher levels might also cause them to gain weight! Spending on clothes will increase their prestige, and will even cause them to wear fancier clothes at higher levels of expenditure (commoners will wear low nobility clothes, and so on). If your court is lacking in artifacts, spending on Amenities is the way to go.  

Worth noting is that the cost of amenities is relative to your size and income; a small realm won’t have to pay as much as a prosperous one - the intent here is to allow smaller kingdoms and empires to ‘punch above their weight’ diplomatically, making choosing between expansion and consolidation a more relevant matter.  

Reaching your baseline might take a long time, unless you decide to take action in order to speed it up - to gain grandeur fast, you need to Hold Court! Performing this decision invites your vassals and subjects to bring their issues, requests, and questions before you. The mere act of Holding Court will give you a one-time boost to your Grandeur, but the opportunities within the activity itself might give you opportunities to increase it further (or you could decide to lose grandeur for some temporal gain that is just too good to pass up!). The issues brought forth when Holding Court are many and varied, with many of them reacting to the state of your realm (more on Hold Court in a later DD).  

**Grandeur Expectations**  
Now, Grandeur isn’t only about reaching the level that gives the effect you desire, it’s also about managing expectations!  

Depending on a number of factors, such as your tier or the size of your realm, you will have a certain expectation put upon your Royal Court. This expectation is a double-edged sword - if your grandeur is below expectations you’ll suffer increasing diplomatic penalties as people lose respect, while if it’s exceeded you might see powerful diplomatic bonuses.  

These are scaled based on how powerful you are - a rather small Kingdom that undershoots its expectations won’t be hit particularly hard, while a massive empire such as the Holy Roman Empire or Byzantium will be punished much harder if they fail to live up to the expectations put upon them.  

The effects of not living up to your expectations are many; reduced prestige, renown, and a hefty hit to opinion with both foreign rulers, courtiers and vassals. A large realm might easily find itself facing significant unrest unless its ruler starts spending on grandeur! On the other hand, a small kingdom that vastly exceeds the expectations put upon it might see significant bonuses to its diplomatic power, as well as renown and other bonuses.  

**Court Events**  
Now, the Royal Court isn’t all about Grandeur, of course. Another important role it holds is to show that there’s life in your court! This is done through Court Events; happenings contained within the court, taking place between those who live therein.  

This new type of event uses the throne room as its backdrop, transforming the entire throne room into an event when they happen. Unlike normal events, this type of event is non-interruptive - you get notified that something is happening, whereby you can go into your Royal Court, inspect the scene, find whoever is involved, and trigger the event yourself. Usually these events are some sort of drama happening between your courtiers, which you can choose to simply ignore if you feel like you have more important matters to attend to.  

These events come in many different flavors, mostly focusing on how it is to live in the court.  

Some examples of court events that are being worked on currently include courtiers causing you embarrassment through their drinking or poor manners, or getting into arguments with your architect. Others involve things like rumors spreading about your predecessor on the throne, or popular and unflattering songs about you spreading within the court itself.  
Court events might also be things like foreign ambassadors trying to uncover your secrets or devout courtiers shaming you and your court for your frivolous living.  

---  

Now, of course there’s more that goes into the Royal Court, but we’ll save going into details regarding Court Artifacts, the UI and graphical looks of the Throne Rooms, Court Positions and so on for future DevDiaries! Of course, this expansion isn’t all about the Royal Court; before the summer break starts you’ll get to read about some of the other features coming with the expansion and patch.  

That’s all for now!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27561659/report)

Click to expand...

[![rageair](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/obsolete/m/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/rageair.375731/)

Written by

### [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)

CK3 Game Director

Grand Stategy

***Paradox Staff******43 Badges***

-

Messages
1.826

-

Reaction score
11.829

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [14](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/page-14#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/page-2#posts)

1 of 14

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/page-14#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/?order=prdx_dd_reaction_score)

[![PrutteHans](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/ck2_avatars_kingdoms/s/k_denmark.png)](https://forum.paradoxplaza.com/forum/members/pruttehans.1334900/)

#### [PrutteHans](https://forum.paradoxplaza.com/forum/members/pruttehans.1334900/)

##### Private

**16 Badges**

Jun 5, 2018

21

136

- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Stellaris](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_base.png "Stellaris")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellnova.png "Stellaris: Galaxy Edition")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellgalaxy.png "Stellaris: Galaxy Edition")
- ![Stellaris: Synthetic Dawn](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Syn_dawn_forum_icon.png "Stellaris: Synthetic Dawn")
- ![Stellaris - Path to Destruction bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Utopia.png "Stellaris - Path to Destruction bundle")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Hearts of Iron IV: Cadet](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Cad.png "Hearts of Iron IV: Cadet")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")
- ![Hearts of Iron IV: Death or Dishonor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4DoD.png "Hearts of Iron IV: Death or Dishonor")
- ![Prison Architect](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Prisonicon.png "Prison Architect")

[](javascript:;)

- [May 25, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/post-27562146)


- [/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/post-27562146](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/post-27562146)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27562146/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/post-27562146)

Promising stuff! Nice to see some pictures to get an idea of what we're getting!

<!-- artifact:reactions:start -->
- 22 Like
- 11 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
