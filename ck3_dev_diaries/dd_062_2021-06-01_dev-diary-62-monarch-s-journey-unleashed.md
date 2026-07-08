---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1477376/"
forum_thread_id: 1477376
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 62
title: "CK3 Dev Diary #62 - Monarch’s Journey unleashed"
dd_date: 2021-06-01
author_handle: Pdx_Meedoc
expansion: Northern Lords
patch: Patch 1.4 (Azure)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2303
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1477376'
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
    location: raw_lines_375_to_379
    action: preserved_and_flagged
    counts:
      Haha: 95
      Like: 31
      (unlabeled — rendered as base64 data URI): 1
      Love: 1
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_456_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #62 - Monarch’s Journey unleashed

<!-- artifact:thread_metadata:start -->
- Thread starter [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)
- Start date [Jun 1, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-61-the-royal-court.1476067/ "CK3 Dev Diary #61 - The Royal Court") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-63-1-4-0-azure-patch-notes.1478364/ "CK3 Dev Diary #63 - 1.4.0 “Azure” Patch Notes")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/?prdxDevPosts=1)

- [Jun 1, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/post-27581879)
- [Replies: 153](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/#posts)


- [/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/post-27581879](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/post-27581879)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27581879/bookmark "Bookmark")

Hello everyone!  

I know you are all eager to learn more about the Royal Court, but as we announced last week, we will go into more details once the Azure patch is released. If everything goes according to plan, and there are no unexpected events, we aim to release Azure next week! But let’s focus on today's small dev diary for now!  

During the development of Crusader Kings III, we organized a community challenge where you could unlock unique cosmetics for the game, which we dubbed the Monarch’s Journey. With the 1.4.0 Azure patch, we’ve decided to make these cosmetics available for everyone!  

It includes:  


- Headgear:
  * Hennin
  * Chaperon
  * Jester's Hat
- Haircuts:
  * Miller
  * Miller Highlights
  * Jeanne d'Arc
  * Pageboy
  * Mullet
- And the Wizard's Beard!
In order to celebrate this, we’ve also hooked some of these assets in to be used by random characters. For instance, Scots will be able to randomly use the Mullet haircut, while Frankish women will be able to use the Jeanne d’Arc haircut.  

![1.jpg](https://forumcontent.paradoxplaza.com/public/714040/1.jpg "1.jpg")


*[A classy French woman with a Jeanne d’Arc haircut]*  

![t3BtwD4oQ0zJCvxyK2KHOtw4Dwk6pVvjpU530WSuEyNk55-SjWcjExtyhDE1nt7DgGkQ_N5-BvyVdlE2ljIkattcQVF-PDauZERoMP3xTBm_7Asce0lE12AzY3Z8brOGu5zGWn1i](https://lh6.googleusercontent.com/t3BtwD4oQ0zJCvxyK2KHOtw4Dwk6pVvjpU530WSuEyNk55-SjWcjExtyhDE1nt7DgGkQ_N5-BvyVdlE2ljIkattcQVF-PDauZERoMP3xTBm_7Asce0lE12AzY3Z8brOGu5zGWn1i "")


*[A charming Scot with a Mullet]*​


And because fashion changed over time, the Chaperon and Hennin will be available in the western world only after 1300.  

![3.jpg](https://forumcontent.paradoxplaza.com/public/714042/3.jpg "3.jpg")


*[A wonderful Chaperon]*  

![pAP7DzFVQd9YEXx7KWPVSBaFNlMuzCp0hhBeOMD2bq-gk4o8uR-lBo5nd21TPuKmMmEWOqH6XJcP5QdPVr_wHYms_0UAoO2MJg1kyiJZtilktTwc4mMF-aWulNBspWIBxVnmVPIi](https://lh5.googleusercontent.com/pAP7DzFVQd9YEXx7KWPVSBaFNlMuzCp0hhBeOMD2bq-gk4o8uR-lBo5nd21TPuKmMmEWOqH6XJcP5QdPVr_wHYms_0UAoO2MJg1kyiJZtilktTwc4mMF-aWulNBspWIBxVnmVPIi "")


*[A magnificent Hennin]*​


In addition to that, we fixed several visual bugs highlighted by you:  


- Spouses of rulers will now once again wear clothes based on their spouse's culture
- Arabic High Nobility will now use the Scholar's Turban and Caliphs will use the Caliphal Robes
- The 'Spindly' Trait will not make people's limbs too thin anymore


On the AI side, we reworked how vassals handle holy war and added constraints on Feudal and Clans rulers to limit their aggression of Tribal rulers. These modifications still allow the Byzantine empire to expand but in a more elegant way. Let’s have a look at a few results from Observe mode!  

![5.jpg](https://forumcontent.paradoxplaza.com/public/714045/5.jpg "5.jpg")



![6.jpg](https://forumcontent.paradoxplaza.com/public/714046/6.jpg "6.jpg")



![7.jpg](https://forumcontent.paradoxplaza.com/public/714047/7.jpg "7.jpg")


​

And this is it for today! As mentioned at the beginning of this dev diary, we should be back next week with the changelog for the patch if everything goes well!  

Until then, I wish you the best and, hopefully, have fun!

 

#### Attachments

- [![2.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/714041/2.jpg)](https://forum.paradoxplaza.com/forum/attachments/2-jpg.726623/)
  
  2.jpg
  351 KB

 · Views: 0

- [![4.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/714043/4.jpg)](https://forum.paradoxplaza.com/forum/attachments/4-jpg.726625/)
  
  4.jpg
  379,6 KB

 · Views: 0

Last edited: Jun 1, 2021

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27581879/report)

Click to expand...

[![Pdx_Meedoc](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/MagickaWizardWars/m/MWW Avatar (51).png)](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)

Written by

### [Pdx_Meedoc](https://forum.paradoxplaza.com/forum/members/pdx_meedoc.1574079/)

Corporal

-

Messages
39

-

Reaction score
2.254

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [8](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/page-8#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/page-2#posts)

1 of 8

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/page-8#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/?order=prdx_dd_reaction_score)

[![EmeraldThanatos](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/ck3/s/avatar_28.png)](https://forum.paradoxplaza.com/forum/members/emeraldthanatos.1542271/)

#### [EmeraldThanatos](https://forum.paradoxplaza.com/forum/members/emeraldthanatos.1542271/)

##### Second Lieutenant

**49 Badges**

Jun 30, 2020

131

1.188

- ![Europa Universalis IV: Dharma](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/dharmaicon.png "Europa Universalis IV: Dharma")
- ![Stellaris - Path to Destruction bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Utopia.png "Stellaris - Path to Destruction bundle")
- ![Europa Universalis IV: Mandate of Heaven](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/moh_forum_icon.png "Europa Universalis IV: Mandate of Heaven")
- ![Europa Universalis IV: Third Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/third_rome_forum_icon.png "Europa Universalis IV: Third Rome")
- ![Stellaris: Synthetic Dawn](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Syn_dawn_forum_icon.png "Stellaris: Synthetic Dawn")
- ![Tyranny - Tales from the Tiers](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Tyr_TftT.png "Tyranny - Tales from the Tiers")
- ![Tyranny - Bastards Wound](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Tyr_bw.png "Tyranny - Bastards Wound")
- ![Europa Universalis IV: Cradle of Civilization](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EUIV_CoC.png "Europa Universalis IV: Cradle of Civilization")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")
- ![Stellaris: Distant Stars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Distantstars.png "Stellaris: Distant Stars")
- ![Stellaris: Leviathans Story Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/leviathans.png "Stellaris: Leviathans Story Pack")
- ![Stellaris: Megacorp](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MegaCorp-ForumIcon.png "Stellaris: Megacorp")
- ![Europa Universalis IV: Golden Century](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gc_forum_icon.png "Europa Universalis IV: Golden Century")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Imperator: Rome - Magna Graecia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MagnGraeciaIcon.png "Imperator: Rome - Magna Graecia")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Europa Universalis 4: Emperor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_emperor.png "Europa Universalis 4: Emperor")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Europa Universalis IV: Common Sense](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cs_forumicon.png "Europa Universalis IV: Common Sense")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Europa Universalis IV: Art of War](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aow_forum_icon.png "Europa Universalis IV: Art of War")
- ![Europa Universalis IV: Conquest of Paradise](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cop_forumicon.png "Europa Universalis IV: Conquest of Paradise")
- ![Europa Universalis IV: Wealth of Nations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_won_forumicon.png "Europa Universalis IV: Wealth of Nations")
- ![Europa Universalis IV: Call to arms event](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EU4_signupForumIcon_01.png "Europa Universalis IV: Call to arms event")
- ![Europa Universalis IV: Res Publica](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/respublica_icon.png "Europa Universalis IV: Res Publica")
- ![Victoria 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2.png "Victoria 2")
- ![Victoria 2: A House Divided](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2AHD_forumicon.png "Victoria 2: A House Divided")
- ![Victoria 2: Heart of Darkness](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v2hod_icon.png "Victoria 2: Heart of Darkness")
- ![Europa Universalis IV: El Dorado](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_eldorado_forumicon.png "Europa Universalis IV: El Dorado")
- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Europa Universalis IV: Cossacks](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cossacks.jpg "Europa Universalis IV: Cossacks")
- ![Europa Universalis IV: Mare Nostrum](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_marenostrum.png "Europa Universalis IV: Mare Nostrum")
- ![Stellaris](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_base.png "Stellaris")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellnova.png "Stellaris: Galaxy Edition")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellgalaxy.png "Stellaris: Galaxy Edition")
- ![Europa Universalis IV: Rights of Man](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rom_forum_icon.png "Europa Universalis IV: Rights of Man")
- ![Tyranny: Archon Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tyr_com.png "Tyranny: Archon Edition")
- ![Tyranny: Archon Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tyr_arc.png "Tyranny: Archon Edition")
- ![Tyranny: Gold Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tyr_ove.png "Tyranny: Gold Edition")
- ![Stellaris: Digital Anniversary Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/plantoid.png "Stellaris: Digital Anniversary Edition")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Victoria 3 Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v3_signup_forum_icon.png "Victoria 3 Sign Up")

[](javascript:;)

- [Jun 1, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/post-27582142)


- [/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/post-27582142](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/post-27582142)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27582142/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-62-monarchs-journey-unleashed.1477376/post-27582142)

> [Pdx_Meedoc said:](https://forum.paradoxplaza.com/forum/goto/post?id=27581879)
>
> These modifications still allow the Byzantine empire to expand but in a more elegant way.
>
> Click to expand...

Proceeds to show bordergore

<!-- artifact:reactions:start -->
- 95 Haha
- 31 Like
- 26 (unlabeled — rendered as base64 data URI)
- 1 Love
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
