---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1442919/"
forum_thread_id: 1442919
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 44
title: CK3 Dev Diary 44 - 1.2 Bits & Bobs
dd_date: 2020-11-17
author_handle: rageair
expansion: Post-release patches
patch: Patch 1.2 (Argent)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3397
inline_image_count: 12
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1442919'
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
    location: raw_lines_428_to_431
    action: preserved_and_flagged
    counts:
      Haha: 57
      (unlabeled — rendered as base64 data URI): 2
      Love: 1
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_459_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary 44 - 1.2 Bits & Bobs

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Nov 17, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-43-a-ruler-of-your-own.1441657/ "CK3 Dev Diary 43 - A Ruler of Your Own") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-45-1-2-patch-notes.1444123/ "CK3 Dev Diary #45 - 1.2 Patch Notes")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/?prdxDevPosts=1)

- [Nov 17, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/post-27108183)
- [Replies: 209](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/#posts)


- [/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/post-27108183](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/post-27108183)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27108183/bookmark "Bookmark")

Greetings!  

In this Dev Diary we’ll show off some of the other things we’ve been working on for the 1.2 patch! While the Ruler Designer is extremely cool, it’s not the only thing you’ll be getting - there’s plenty of exciting new things coming up! What follows below is a showcase of some of the things we’ve done, presented by someone who’s worked on it!  

Oh, and because we know you’re wondering - yes, saves made in 1.1 will be compatible in 1.2!  


**Kill List**  
A very fun feature from CK2 that we wanted to bring back is the Kill List, you might have noticed the new UI button in some of our Ruler Designer teasers before.  
This skull icon will appear on any character who has killed people you know about and when clicked opens a list of everyone they killed and how they met their grisly fate. So you can get a sense of just how much of a true beast some of your strong knights are and how many of your foes they have vanquished on the battlefield in your name.  
But of course it only shows the kills you know about, so some people that look innocent to you may in fact be hiding numerous skeletons in their closet…  


![KillList.png](https://forumcontent.paradoxplaza.com/public/640845/KillList.png "KillList.png")


[Picture of kill list button location]  

![YourKills.png](https://forumcontent.paradoxplaza.com/public/640846/YourKills.png "YourKills.png")


[Picture of the open kill list]  


**Attach to Army**  
Another helpful utility we wanted to add was being able to attach your armies to follow ally armies to their destinations. This is especially useful during bigger wars like Crusades where you are not the primary participant; you can attach to any friendly unit of an ally in the same province as your unit and of course then detach when you decide to go your own way. If there are multiple armies in a province you can attach to then a pop up window will open for you to decide which one you would like to follow.  


![Attach.png](https://forumcontent.paradoxplaza.com/public/640847/Attach.png "Attach.png")


[Picture of the attach to army button]  


**Force Realm Priest Endorsement**  
Your realm priest will endorse you normally if they have a good opinion of you, and we’ve now extended that so if you have a strong hook on them then they will passively be forced to endorse you regardless of their personal opinion of you.  
That way you can still get all of those sweet taxes and levies from their church holdings even if they might personally think you are a blasphemous fool!  


![HookEndorsement.png](https://forumcontent.paradoxplaza.com/public/640851/HookEndorsement.png "HookEndorsement.png")


[Picture of realm priest being forced to endorse you via a strong hook]  


**Tribal Walls / Tribal Holding variants**  
Tribes in different parts of the world will now look different! From longhouses in the north to yurts in the steppes, there’s now a visual difference between the major tribal regions on the map. We’ve also added one more visual tier of walls, symbolising the very lowest possible fort level a holding can have.  


![TribalHoldings.png](https://forumcontent.paradoxplaza.com/public/640852/TribalHoldings.png "TribalHoldings.png")


[Picture of new Tribal Holding variants]  


**Reworked Dynasty UI**  
The Dynasty view has gotten some more love! The window now has two dynamic info boxes explaining how dynasty and house head is chosen, especially how Max military strength determines who's dynasty head. Military strength can now also be seen and compared between house heads in the house list. The legacy area has gotten a new look to easier show which legacy tracks you have unlocked, how many steps are unlocked, and which ones you've finished.  


![NewDynastyView.png](https://forumcontent.paradoxplaza.com/public/640853/NewDynastyView.png "NewDynastyView.png")


[Picture of updated Dynasty UI]  


**Improved Battle UI**  
Battles have also gotten some more love, with the UI having received an overhaul. It now both looks nicer and places important information in a better layout!  


![NewBattle.png](https://forumcontent.paradoxplaza.com/public/640854/NewBattle.png "NewBattle.png")


[Picture of the improved Battle UI]  


**Player Coat of Arms Graphics**  
Your Coat Of Arms is now decorated with mantling! It adds a sense of flair and you can also spot other players easier on the map during multiplayer.  


![Mantling.png](https://forumcontent.paradoxplaza.com/public/640855/Mantling.png "Mantling.png")


[Picture of Mantling on a player CoA]  


**Rally Point Improvements**  
We’ve done some work on the troop system in 1.2. As part of this we hope to have eliminated some bugs like levies failing to reinforce when they should.  
More visibly, we’ve made one change to how troops get raised at rally points. Now if you exceed the supply limit the game will automatically split the army up to obey the supply limit, spreading it out over adjacent provinces.  


![RallyPointRaise.png](https://forumcontent.paradoxplaza.com/public/640857/RallyPointRaise.png "RallyPointRaise.png")


[Picture of a rally point where armies are spread out]  

Pictured is what now happens when trying to raise a bit over 10k men in an area with supply limits of 2.5k.  


**Siberian Paganism**  
Suomenusko has long been in a bit of an awkward spot. It stretches over large territories where the people in reality worshiped many different deities. To improve the situation, we've made two changes. The first is a simple name change, as we've renamed Suomenusko to Ukonusko (after the main deity). It gives the faith a name that isn't specifically Finnish, since we have several other cultures that share the same faith.  

![NewSetup.png](https://forumcontent.paradoxplaza.com/public/640858/NewSetup.png "NewSetup.png")


[Picture of new Faith Setup in the north]  

Secondly, we've split it into two separate faiths by adding a new faith for the Siberian region. We felt that adding a new faith would be a significant improvement as to better reflect the varied beliefs of the Ugrian peoples. Named Turumic, after their main patron deity Numi-Turum, it is in some ways similar to Ukonusko in that it's a faith closely linked to nature, but is different by their veneration of hunting. The tenets are the following: Ancestor Worship, Ritual Celebrations, and Sanctity of Nature. It uniquely has the Hunter lifestyle traits as virtues. The other virtues being Brave, Generous, and Temperate. Meanwhile, being Greedy, Craven, or Vengeful, is considered a sin.  


**Improved Ugliness System**  
In CK3, the “ugly” trait is a lot more interesting than it was in CK2, having a noticeable effect on portraits, and coming in three levels of severity. However, beyond the first level of the trait we didn’t quite achieve the levels of ugliness we wanted at release. So in 1.2 we’ve improved the system we use to distort the portraits of ugly people to make them uglier while still not feeling too out of place within the art style. Before 1.2 ugliness worked by changing skin texture and making all facial features more extreme. This is still the case, but in 1.2 we also pick a single or a small set of features to make especially extreme. This can result in a character for instance having a particularly messed up nose, a face that’s too small for their head, or the tiniest mouth. Focusing on small feature sets like this helps ensure that ugly people are varied in their ugliness, and more readily identifiable as “ugly”.  
Below are a couple examples of how ugly characters will look in 1.2 vs. 1.1.  


![UglyComparison.png](https://forumcontent.paradoxplaza.com/public/640859/UglyComparison.png "UglyComparison.png")


[Picture of a comparison between the same level of ugliness in 1.1 vs 1.2]  

As you can see the difference isn’t massive, but helps make them a bit more interesting. There’s still room for improvement and especially so for the “Hideous” trait, but this was a relatively simple and safe change to make for 1.2.  


**Matrilineal Game Rules**  
We’ve added a new game rule that controls the behaviour of the AI when choosing which type of marriage to pursue. There’s plenty of options to choose from, so regardless what your preference is, it should hopefully be represented! All options are achievement compatible.  

![MatriRules.png](https://forumcontent.paradoxplaza.com/public/640860/MatriRules.png "MatriRules.png")


[Picture of Matrilineal Marriages Game Rule settings]  

**Naming Dynasty Members in Court**  
You now get to name all Dynasty members that are born in your court, not just your own children. This means that you can make sure that the correct names are passed down as you prefer!  


**New Event Content**  
You can now grow old, sick, tired, and depressed more efficiently, with new events that dole out the “Infirm” trait.  

For those seeking even swifter departures from this mortal coil, we have expanded the Murder scheme with additional events and deadly outcomes! But take care — the mastermind behind a scheme can now be unmasked, in addition to the existence of the scheme itself. To even things out a bit, a Court Physician you recruit as an agent has a chance to purposely mess up treatments of your target — and they can now also properly treat their own wounds and conditions.  

Other schemes and mechanics have gotten numerous content tweaks, additions, and updates.  


That’s it for this time! Don't forget to tune in to tomorrows CK3 stream, where we'll show off the 1.2 patch! Who knows, maybe you'll even get to know the release date?  
Details:  
[Link](https://www.twitch.tv/paradoxinteractive)  
Live at 16:30 CET, tomorrow!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27108183/report)

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

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [11](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/page-11#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/page-2#posts)

1 of 11

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/page-11#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/?order=prdx_dd_reaction_score)

[![jakeowaty](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/s/stellaris_dev_avatar_ai_robot.png)](https://forum.paradoxplaza.com/forum/members/jakeowaty.1376360/)

#### [jakeowaty](https://forum.paradoxplaza.com/forum/members/jakeowaty.1376360/)

##### Captain

**44 Badges**

Nov 17, 2018

476

728

- ![Europa Universalis IV: Rights of Man](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rom_forum_icon.png "Europa Universalis IV: Rights of Man")
- ![Europa Universalis IV: El Dorado](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_eldorado_forumicon.png "Europa Universalis IV: El Dorado")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Europa Universalis IV: Common Sense](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cs_forumicon.png "Europa Universalis IV: Common Sense")
- ![Crusader Kings II: Limited Collectors Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_deluxe.png "Crusader Kings II: Limited Collectors Edition")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellnova.png "Stellaris: Galaxy Edition")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellgalaxy.png "Stellaris: Galaxy Edition")
- ![Hearts of Iron IV: Field Marshal](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FM.png "Hearts of Iron IV: Field Marshal")
- ![Crusader Kings II: Reapers Due](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/reapers_due_forum_icon.png "Crusader Kings II: Reapers Due")
- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Cities: Skylines - Natural Disasters](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CS_ND_icon_16x16.png "Cities: Skylines - Natural Disasters")
- ![Crusader Kings II: Monks and Mystics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/monksandmystics.png "Crusader Kings II: Monks and Mystics")
- ![Stellaris - Path to Destruction bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Utopia.png "Stellaris - Path to Destruction bundle")
- ![Stellaris: Synthetic Dawn](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Syn_dawn_forum_icon.png "Stellaris: Synthetic Dawn")
- ![Stellaris: Megacorp](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MegaCorp-ForumIcon.png "Stellaris: Megacorp")
- ![Imperator: Rome Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ImperatorDeluxeicon.png "Imperator: Rome Deluxe Edition")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Prison Architect](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Prisonicon.png "Prison Architect")
- ![Cities: Skylines](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/csl.png "Cities: Skylines")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Hearts of Iron IV: Colonel](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Col.png "Hearts of Iron IV: Colonel")
- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Crusader Kings II: Rajas of India](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_rajas_of_india_forumicon.png "Crusader Kings II: Rajas of India")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Europa Universalis IV: Mandate of Heaven](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/moh_forum_icon.png "Europa Universalis IV: Mandate of Heaven")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![Crusader Kings II: Sunset Invasion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sunset_invasion_forumicon.png "Crusader Kings II: Sunset Invasion")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Europa Universalis IV: Art of War](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aow_forum_icon.png "Europa Universalis IV: Art of War")
- ![Europa Universalis IV: Conquest of Paradise](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cop_forumicon.png "Europa Universalis IV: Conquest of Paradise")
- ![Crusader Kings II: Holy Knight (pre-order)](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_gold_forumicon.png "Crusader Kings II: Holy Knight (pre-order)")
- ![Hearts of Iron IV: Cadet](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Cad.png "Hearts of Iron IV: Cadet")
- ![Europa Universalis IV: Wealth of Nations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_won_forumicon.png "Europa Universalis IV: Wealth of Nations")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellbase.png "Stellaris: Galaxy Edition")
- ![Europa Universalis IV: Call to arms event](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EU4_signupForumIcon_01.png "Europa Universalis IV: Call to arms event")
- ![Europa Universalis IV: Mare Nostrum](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_marenostrum.png "Europa Universalis IV: Mare Nostrum")
- ![Crusader Kings II: Conclave](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DLC_icon_Conclave.png "Crusader Kings II: Conclave")
- ![Europa Universalis IV: Cossacks](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cossacks.jpg "Europa Universalis IV: Cossacks")
- ![Europa Universalis IV: Res Publica](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/respublica_icon.png "Europa Universalis IV: Res Publica")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Cities: Skylines Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/csldelux.png "Cities: Skylines Deluxe Edition")
- ![Europa Universalis IV: Pre-order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_special_forumicon.png "Europa Universalis IV: Pre-order")

[](javascript:;)

- [Nov 17, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/post-27108642)


- [/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/post-27108642](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/post-27108642)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27108642/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-44-1-2-bits-bobs.1442919/post-27108642)

First!  

I can't wait for this to release!  

Oh, wait...

<!-- artifact:reactions:start -->
- 57 Haha
- 2 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 1 Love
<!-- artifact:reactions:end -->
