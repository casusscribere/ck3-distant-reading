---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1560180/"
forum_thread_id: 1560180
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "CK3 - \"Robe\" 1.8.0 Release & Changelog"
dd_date: 2022-12-01
author_handle: pdxhr
expansion: Friends and Foes
patch: Patch 1.8 (Robe)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3481
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1560180'
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
    location: raw_lines_~28_to_126
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_128_to_129
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_458_to_458
    action: preserved_and_flagged
    counts:
      Like: 6
    note: Reactions block parsed; 1 of 1 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_535_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 - "Robe" 1.8.0 Release & Changelog

<!-- artifact:thread_metadata:start -->
- Thread starter [pdxhr](https://forum.paradoxplaza.com/forum/members/pdxhr.1709208/)
- Start date [Dec 1, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-111-1-8-0-robe-feature-highlight.1546936/ "Crusader Kings 3 Dev Diary #111 - 1.8.0 “Robe” Feature Highlight") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-112-year-in-review.1561106/ "Dev Diary #112 - Year in Review")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/?prdxDevPosts=1)

- [Dec 1, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/post-28653367)
- [Replies: 123](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/#posts)


- [/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/post-28653367](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/post-28653367)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28653367/bookmark "Bookmark")

Hello everyone!  

I’m Henrik – nice to e-meet you – I’m a crazy plant person and producer at Paradox Interactive. I'm here to let you know that we have a release coming up for you today:  

**1.8.0 “ROBE” FREE UPDATE**  

The update should be rolled out to a store near you some time during the day. I promise to keep this short because I understand you’re here for the changelog. As my dear colleague, and ambassador of horchata, Hugo presented last week, we’ve taken some time to put together an update that, apart from a couple of new features, focuses a fair bit on improved stability and bug fixes. We hope you are as excited as we are to continue the endeavours as rulers of lands and kingdoms (hopefully) both beautiful and prosperous.  

But enough me chit-chatting – to the details:  

Spoiler: 1.8.0 changelog

###################  
# Free Features  
###################  


- You can now save and load Custom Rulers! Create templates you can easily re-use everywhere on the world map. All the attributes besides the Dynasty and the Coat of Arms are saved.
- Completely reworked the Bookmark Screen; its now reorganized to allow more room for bookmarks, and they are now sorted by the year they belong to (867 and 1066). This comes with new and improved art for elements and buttons, as well as showing which DLC you have active.
- Added new and unique illustrations for every Tenet currently in the game!
- Added 17 new Custom Faith icons for use when creating new faiths, ranging from Ankhs and Boromian Circles to Doves and Chi Rhos!


###################  
# Hardware  
###################  


- Added support for Vulkan renderer
- OSX and Linux will now by default use the Vulkan renderer - This should increase the framerate significantly for M1 and M2 Mac players
- Added a setting to change the rendering backend under the graphics category

###################  
# Game balance  
###################  


- Disinheriting is now free for children with a disputed heritage or known bastard. There is however a global opinion penalty which is always applied when taking the interaction
- Mozarabs can now use a strong hook to force/coerce the pope into binding with rome
- Updated the consequences for revoking hostile Holy order, it now adds Fervor to their Faith, and potentially a negative county modifier
- Literalism is legal for all faiths to adopt
- If the game rule "strict regional heresy" is activated, the Mozarab faith will only appear in Iberia and North Africa
- Added additional reward to forming the Kingdom of Aragon
- Rulers will no longer be deposed if they happen to inherit a tyranny war from a lower tier ruler
- Added gold cost to the "truly special board" in the board game event “A Stroke of Luck”
- Breaking away from Rome now requires you to be in poor standing with your HoF
- Properly set low obligations on Custom Rulers who are vassals of the HRE
- ‘A Beautiful Specimen’ will be only triggered for lovers and soulmates now; not powerful vassals
- Iberian Conciliation achievement is now classified as "Hard" instead of "Medium"
- Auto-fire the Court Chaplain if they are excommunicated, except if you are also excommunicated yourself
- Contracting Assistance is now scaled by army size.

###################  
# AI  
###################  


- Fixed a case where a raiding unit could not find a path to go home in case when the capital was moved. In that case the unit will be disbanded
- The AI will not try convert children of a vassal with religious protection anymore
- The AI will marry young men to old women less often: the weight of alliances and the impact of age has been rebalanced
- The AI will now send fewer requests for chess challenges
- Blocked the AI from sending two interactions simultaneously, which could cause UI issues
- AI characters are a lot less likely to accept a war assistance contract against you if they are allied with you

###################  
# Interface  
###################  


- Fixed issue with change/revert buttons in interaction lists only being responsive on a small part of it
- Fixed so the Army Reorganization scroll area no longer scroll to the top when unit is moved
- The bookmark lands of Emir Yahya now match the actual in-game shape


![r03kGkx8R1ZOPBapO4-Xx3CykhMOuznws0SAKI4J1Bi5Ycit9faSnC3gcI-zr41rJvLWDIoNfLla-DCVz2Qbsblry6T8I0LBf-xkIXkCEwdkceCuXttuF5_WTNJOYNPoCPJI8zCdS1rx4zOltj3-5ts6d1vqI-2QBWwEVV4CpzKYeHPl_51_bEz-avVGLw](https://lh6.googleusercontent.com/r03kGkx8R1ZOPBapO4-Xx3CykhMOuznws0SAKI4J1Bi5Ycit9faSnC3gcI-zr41rJvLWDIoNfLla-DCVz2Qbsblry6T8I0LBf-xkIXkCEwdkceCuXttuF5_WTNJOYNPoCPJI8zCdS1rx4zOltj3-5ts6d1vqI-2QBWwEVV4CpzKYeHPl_51_bEz-avVGLw "")


- Holy orders no longer cause "Grant to..." button to disappear in the county capital
- Offer Guardianship notification and window now use the ‘Offer Guardianship’ title instead of ‘Send Proposal’
- Unselectable beneficiaries will now be shown in the list with a tooltip explaining why they cannot be selected
- Adultery events (adultery.2001 & adultery.2002) now have improved texts for duels


![BZUeCMJrF45VVDTMgREagKb6NyrtVpNVvJ-b7SMq9N0zO-qHlB-47H9LeVhcZ7ajJ8fjrr7sxW05NXqAxhBrfgXvms3gDZy9tYxFlvW-_WWvyc_0NqHKVK8b00K4xuowb3q78YzEyFz7YGvvR1AP8No5_WHeZAnpDdWq60wPTbJTAPh8mLv2pDVvMkhixw](https://lh5.googleusercontent.com/BZUeCMJrF45VVDTMgREagKb6NyrtVpNVvJ-b7SMq9N0zO-qHlB-47H9LeVhcZ7ajJ8fjrr7sxW05NXqAxhBrfgXvms3gDZy9tYxFlvW-_WWvyc_0NqHKVK8b00K4xuowb3q78YzEyFz7YGvvR1AP8No5_WHeZAnpDdWq60wPTbJTAPh8mLv2pDVvMkhixw "")



- You can now always open the list of potential agents, even if none will accept to join the scheme. This can be used to, for example, plan who to seduce or fabricate hooks against to further your interests.
- Vassal contract modification window now warns when current liege is not the rightful liege
- Activated Regnal numbers for Count-tier characters to avoid non immersive lineages
- The "Is imprisoned = no" condition for all court positions is now hidden
- Court positions no longer display requirements that are the opposite of what they seek
- Added a section for showing the DLCs that are installed and active. It can be found in the main menu and the bookmark area


###################  
# Bug fixes  
###################  


- Fixed issue where players couldn't accept/decline artifact gifts
- Fixed issue with event learning_theology_special.1001 were doctrines from the same group wouldn't be removed before applying the new one
- Fixed German court grandeur tooltip for being above expected level
- Fixed issue where achievements would still be enabled after creating a custom ruler and not starting the game as them
- You no longer get "the Thief Slayer" nickname if you already have a positive nickname.
- Fixed issue where artifact repair cost would show wrong value in the repair window, now shows same value as in the repair button tooltip
- Fixed issue where ironman would reset when going into select any ruler
- Fixed issue where overwriting same ruler multiple times would block achievements to be enabled
- Bestow Royal Favor chancellor task is now canceled if the target vassal declares war on you
- Fixed an issues that would cause some hedonistic sins to be incorrectly categorized as virtues or vice versa
- Created missing localization for threatened_by_buildup_opinion
- Petitioning liege in Russian now uses correct localization macro
- Struggle messages will now only be shown for interlopers and involved characters
- Fixed chinese localization doing infinite recursion on localization macro
- Moved the locators for special buildings in Tenerife to spawn buildings on landmass rather than in the water
- We now properly communicate in advance that the Subjugation war is only available once per lifetime
- Notifications for struggle endings are no longer sent to every single player in the lobby, instead selecting those either involved in the struggle or within a certain proximity of the region.
- fp2_struggle.2021.a.a is no longer blatantly misleading
- The tooltip of Invite to Activity displays a proper explanation when none of them is available
- "Desires of the Flesh" now checks what world region you are in before selecting a faith for you to follow
- Properly handle Duchy and Kingdom Holy Wars within the Struggle
- Removed duplicated check that were done for characters joining some factions
- Holy Wars properly deactivated after the Detente ending for the relevant cultures
- Fixed namespace issues with fp2_Struggle.2024 (now martial_chivalry.4001)
- Explicitly say that a Faith or Culture needs to control 80% of the counties to get involved within the Iberian Struggle
- Fixed issue where FP2 3D assets were being overwritten by their generic counterparts.
- We now display the right cost for the "Invite to Activity interaction"; it used to be swapped
- Head of Faith titles can no longer be granted to vassals
- Prevent players from cloning their mercenary armies
- Fixed localization in invitation to lieges council letter for Spanish
- Character info is now hidden for the thief in fp2_struggle.2009
- Player now receives heresiarch trait when converting to Adoptionism
- The Found an Empire is now blocked for Involved and Interloper of the Iberian Struggle. The new condition is however only displayed for characters with an involved Faith or Culture, and living nearby
- Fixed parsing issues with fund_inspiration.2080
- Fixed an issue where multiplayer got out of sync when a player hot joined the session
- Offering Relief events no longer gives you an improved opinion towards yourself. With that fixed, it's still important to remember to love thy self, you're doing good, keep it up!
- Expanded acceptance criteria for christian bones, christian syncretists can now display christian bones in their court. Finally allowing Basque pagans to equip and enjoy christian bones.
- Added the word “been” to “I have riding” to result in “I have been riding” in fund_inspiration.6001

###################  
# Other  
###################  


- Updated name of "Reconquista" cultural innovation to something more historically accurate
- Added the Sayyid trait to some characters from the Hammudid house who were missing it
- Added new outcomes to boardgames
- Fixed line breaks in select Chinese localization keys
- Aragonese now speak the Oc´Romance language
- Set Wanda as a daughter of Krak I as it should be in 867
- Tabletop Warriors now has a more natural reading description
- Fixed the dynasty reference for the Chinese Xue Dynasty
- Clarified the consequences of Dissolution faction
- Added new localization for creating a new faith that keeps the former pope as the new pope
- Refresh factions against liege after player character change
- Fate of Iberia: the Struggle Ending Achievements now have greater clarity as to what ending they refer to
- Zandaqa can now be rejected when pledging submission to a caliph



-HR (Not Human Resources)

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/28653367/report)

Click to expand...

[![pdxhr](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/Female_Advisors_EUIV/m/naval_reformer_female.png)](https://forum.paradoxplaza.com/forum/members/pdxhr.1709208/)

Written by

### [pdxhr](https://forum.paradoxplaza.com/forum/members/pdxhr.1709208/)

Recruit

-

Messages
3

-

Reaction score
151

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [7](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/page-7#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/page-2#posts)

1 of 7

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/page-7#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/?order=prdx_dd_reaction_score)

[![johnty5](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/ck3/s/avatar_01.png)](https://forum.paradoxplaza.com/forum/members/johnty5.920454/)

#### [johnty5](https://forum.paradoxplaza.com/forum/members/johnty5.920454/)

##### Field Marshal

**77 Badges**

Aug 5, 2014

2.502

16.611

- ![Victoria 3 Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v3_signup_forum_icon.png "Victoria 3 Sign Up")
- ![BATTLETECH: Flashpoint](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BTFlashpoint.png "BATTLETECH: Flashpoint")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MtGicon.png "Hearts of Iron IV: Expansion Pass")
- ![BATTLETECH: Season pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BTUrbanwarfare.png "BATTLETECH: Season pass")
- ![Hearts of Iron IV: Death or Dishonor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4DoD.png "Hearts of Iron IV: Death or Dishonor")
- ![BATTLETECH: Heavy Metal](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/BTHvymtlicon.png "BATTLETECH: Heavy Metal")
- ![Prison Architect: Psych Ward](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/psychwardicon.jpg "Prison Architect: Psych Ward")
- ![Hearts of Iron IV: Together for Victory](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoI4Tfv.png "Hearts of Iron IV: Together for Victory")
- ![Hearts of Iron IV: La Resistance](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HoILRicon.png "Hearts of Iron IV: La Resistance")
- ![Hearts of Iron IV Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/HOI_signup.png "Hearts of Iron IV Sign-up")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Island Bound](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/paib.png "Island Bound")
- ![Hearts of Iron IV: Battle for the Bosporus](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/bftb.png "Hearts of Iron IV: Battle for the Bosporus")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellnova.png "Stellaris: Galaxy Edition")
- ![Europa Universalis IV](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_forumicon.png "Europa Universalis IV")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Europa Universalis 4: Emperor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_emperor.png "Europa Universalis 4: Emperor")
- ![Imperator: Rome - Magna Graecia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MagnGraeciaIcon.png "Imperator: Rome - Magna Graecia")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Victoria 2](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/vic2.png "Victoria 2")
- ![Hearts of Iron IV: Cadet](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Cad.png "Hearts of Iron IV: Cadet")
- ![Pillars of Eternity](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/PillarsOfEternity_forumicon.png "Pillars of Eternity")
- ![BATTLETECH](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/battletech_standard.png "BATTLETECH")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![Prison Architect](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Prisonicon.png "Prison Architect")
- ![Europa Universalis IV: Common Sense](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cs_forumicon.png "Europa Universalis IV: Common Sense")
- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Europa Universalis IV: Cossacks](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/eu4_cossacks.jpg "Europa Universalis IV: Cossacks")
- ![Crusader Kings II: Conclave](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DLC_icon_Conclave.png "Crusader Kings II: Conclave")
- ![Hearts of Iron IV: Expansion Pass](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/hoi_tiger_forum_icon.png "Hearts of Iron IV: Expansion Pass")
- ![Stellaris](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_base.png "Stellaris")
- ![Stellaris Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Stellaris_SignUp_icon.png "Stellaris Sign-up")
- ![Crusader Kings II: Reapers Due](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/reapers_due_forum_icon.png "Crusader Kings II: Reapers Due")
- ![Europa Universalis IV: Cradle of Civilization](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/EUIV_CoC.png "Europa Universalis IV: Cradle of Civilization")
- ![Stellaris: Digital Anniversary Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/plantoid.png "Stellaris: Digital Anniversary Edition")
- ![Stellaris: Leviathans Story Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/leviathans.png "Stellaris: Leviathans Story Pack")
- ![Crusader Kings II: Monks and Mystics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/monksandmystics.png "Crusader Kings II: Monks and Mystics")
- ![Europa Universalis IV: Mandate of Heaven](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/moh_forum_icon.png "Europa Universalis IV: Mandate of Heaven")
- ![Europa Universalis IV: Dharma](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/dharmaicon.png "Europa Universalis IV: Dharma")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Imperator: Rome Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorsignup.png "Imperator: Rome Sign Up")
- ![Europa Universalis IV: Golden Century](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/gc_forum_icon.png "Europa Universalis IV: Golden Century")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Stellaris: Distant Stars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Distantstars.png "Stellaris: Distant Stars")
- ![Europa Universalis IV: Rule Britannia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/rule_britania_icon.png "Europa Universalis IV: Rule Britannia")

[](javascript:;)

- [Dec 1, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/post-28655366)


- [/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/post-28655366](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/post-28655366)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28655366/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-robe-1-8-0-release-changelog.1560180/post-28655366)

> [pdxhr said:](https://forum.paradoxplaza.com/forum/goto/post?id=28653367)
>
> You can now always open the list of potential agents, even if none will accept to join the scheme. This can be used to, for example, plan who to seduce or fabricate hooks against to further your interests.
>
> Click to expand...

This is good. Always found this annoying.

 

Toggle signature

Songs of Yuletide 2, when? [Join the campaign >>>](https://forum.paradoxplaza.com/forum/threads/song-of-yuletide-2.1576291/)

- 20

<!-- artifact:reactions:start -->
- 6 Like
<!-- artifact:reactions:end -->
