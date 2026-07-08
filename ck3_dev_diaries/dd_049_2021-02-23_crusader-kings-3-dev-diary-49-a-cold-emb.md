---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1458798/"
forum_thread_id: 1458798
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 49
title: "Crusader Kings 3 Dev Diary #49 - A Cold Embrace"
dd_date: 2021-02-23
author_handle: Servancour
expansion: Northern Lords
patch: Patch 1.3 (Corvus)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3189
inline_image_count: 5
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1458798'
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
    location: raw_lines_374_to_375
    action: preserved_and_flagged
    counts:
      Like: 11
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_432_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Crusader Kings 3 Dev Diary #49 - A Cold Embrace

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Feb 23, 2021](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-48-the-team.1456752/ "CK3 Dev Diary #48 - The Team") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-50-poetry-to-my-ears.1460062/ "Crusader Kings 3 Dev Diary #50 - Poetry to my Ears")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/?prdxDevPosts=1)

- [Feb 23, 2021](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/post-27315718)
- [Replies: 234](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/#posts)


- [/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/post-27315718](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/post-27315718)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27315718/bookmark "Bookmark")

Greetings everyone!  

Don’t stand out there in the cold. Come on in and warm yourself by the fire!  

Have you made yourself comfortable? Excellent. Before we get to it, first things first. I know that all of you are eagerly awaiting more news regarding upcoming DLC content, but we’re not ready to start talking about those quite yet. Don’t fret, you will not have to wait that long. They say that patience is a virtue, but knowing better, I’ll [leave this right here](https://www.paradoxinteractive.com/en/paradox-insider-returns-on-march-13/).  

For the next few weeks and the coming dev diaries we’ll talk a bit about what we have in store for the next major update, 1.3. In usual fashion, you can expect 1.3 to land alongside the upcoming DLC. Without further ado, let’s get to it shall we?  

Winter is Coming  
Winter is being introduced to CK3, making the already unforgiving world of the Middle Ages a much harsher place! As winter approaches, the map will gradually get covered in snow, clearly showing the extent of the freezing cold. The system itself is fairly flexible and allows for a great degree of control, as we can set which provinces should experience winter, and which shouldn’t. Winter won’t be limited to just the northernmost parts of the map, so expect snow to appear in places such as the Persian Mountains, or on the heights of the Tibetan plateau.  

![winter_dd_01_tibet.png](https://forumcontent.paradoxplaza.com/public/672561/winter_dd_01_tibet.png "winter_dd_01_tibet.png")



With the introduction of winter comes new gameplay considerations. It wouldn’t be any point in adding this cool system if it didn’t do anything interesting. Winter comes in three different variants; mild, normal, and harsh. Mild and normal winters will be fairly common throughout central Europe and parts of southern Europe, while harsh winters are rarer but can still occur. If you find yourself lost in the frozen landscape of places such as Sápmi, Mongolia, or Himalaya, expect harsh winters to be the norm and plan accordingly!  

We wanted to make sure that it’s easy to see what level of winter is present in any given barony at a glance. The amount of snow increases with higher levels. Mild winters should generally be fairly easy to spot, with patches of green still clearly visible. In contrast, harsh winters mostly cover an entire province with snow. Certain areas might even have clouds with steady snowfall appearing for that extra level of detail!  

Depending on the severity of winter, your armies will start to lose supply over time. Harsh winter means you’ll lose more supply each month, making it a risky business to go above the supply limit for an extended period during the winter season. Harsh winters will also have armies suffer more fatal casualties during battles.  

Winter will also have an effect on your Men-at-Arms. Most noticeably, cavalry units will perform worse in normal and harsh winters. Heavy cavalry, in particular, will suffer some hefty penalties. I would advise against the use of heavy cavalry if you know you’ll be fighting battles in mountainous terrain during the winter season. On the other hand, some Men-at-Arms will get (sometimes quite significant) bonuses while fighting in winter. One such unit is the Tibetan culture unit, Mountaineers. Accustomed to the cold and the snow in the mountains, they can utilize it to their advantage in the form of a damage bonus whenever they participate in battles when winter is present.  

![winter_dd_02_maa.png](https://forumcontent.paradoxplaza.com/public/672578/winter_dd_02_maa.png "winter_dd_02_maa.png")



The system for setting winter bonuses (or penalties if you will) on Men-at-Arms works just like setting terrain bonuses, making it very friendly for any modders out there.  

While winter and snow might look and play nice, it wouldn’t be complete without a fitting soundscape. I’ll hand over to our sound designer Gustav to talk a bit about what he did to bring winter to life!  

A Sound Plan  
Winter for a Swede is like butter on toast, we love it! (brr… please be spring soon!) There are two areas where we have updated audio on the map.  

**Holdings:**  
Audio gets reflected with real-time updates to holdings. When winter spreads over your lands; or any lands for that matter, folks now go inside their homes, birds have migrated to more southern regions, and the animals are now in their stables or inside by the hearths, cozy!  

[https://www.youtube.com/embed/9S_XdVvdDME?wmode=opaque](https://www.youtube.com/embed/9S_XdVvdDME?wmode=opaque)


The way we achieve this is to link the shader that covers the region with snow and Ice to a real-time float parameter, that then talks to our Audio Middleware Engine Fmod.  

Awesome, but what does it actually do?  
It attenuates sound layers, controls effects such as equalizers and reverb, and reshapes the original sound that was there during summertime, and morphs it into wintertime.  

[https://www.youtube.com/embed/rtOlmSFxcTs?wmode=opaque](https://www.youtube.com/embed/rtOlmSFxcTs?wmode=opaque)


VFX:  
We also have snow storms appearing, for both mild and harsh winters.  
If you hear the sounds, be wary, your troops will most likely suffer some penalties in these areas.  
Tread carefully!  

[https://www.youtube.com/embed/bU-raHZBFro?wmode=opaque](https://www.youtube.com/embed/bU-raHZBFro?wmode=opaque)


The snowstorms are spawned on the map with the particle system, which allows us to be able to spatialize the sound effects ( position them in a 3D location X-Y-Z ) as the mild snowstorm morphs into the harsh storm, so do the sound effects. I’ll leave you with this; a snippet of what goes on under the hood inside Fmod during winter.  

[https://www.youtube.com/embed/C2m6P973tf8?wmode=opaque](https://www.youtube.com/embed/C2m6P973tf8?wmode=opaque)


Obligatory Map Update  
Anyone who has followed the history of CK2 or the DDs for CK3 will know that I do enjoy my maps, and I’ll try to get in smaller map updates or improvements whenever I can. Since release, we’ve identified a few general areas that we think can be improved upon. Some of these will be updated in 1.3. First up, Ireland.  

The baronies in Ireland were a bit too large, making the emerald island have a significantly less holding density than its neighbors, England and Scotland. The western half of Ireland in particular suffered from a few quite large baronies. To solve this issue, we’ve added a number of new baronies, along with a couple of new counties, that should improve the overall experience of playing in Ireland.  

![winter_dd_03_ireland.png](https://forumcontent.paradoxplaza.com/public/672579/winter_dd_03_ireland.png "winter_dd_03_ireland.png")



While Italy hasn't suffered from larger baronies in the same vein as Ireland, the area didn’t quite feel up to par with many other regions within Europe. Especially in terms of overall holding count. Italy generally had a bit too few holdings per county, so we’ve added new baronies in various places throughout the peninsula, from the slopes of the Alps all the way down to Reggio Calabria. The southern half in particular got some much needed attention. In the new setup, you’ll find significantly less counties with only two baronies. To mention a few examples, you’ll find that the county of Veneto has Malamacco as a new barony, Agnone can be found in the county of Lanciano, and Lecce is now an actual holding in the county with the same name. Overall, this should make Italy more representative of its historical impact and more fun to play in.  

![winter_dd_04_italy.png](https://forumcontent.paradoxplaza.com/public/672580/winter_dd_04_italy.png "winter_dd_04_italy.png")



![winter_dd_05_sicily.png](https://forumcontent.paradoxplaza.com/public/672581/winter_dd_05_sicily.png "winter_dd_05_sicily.png")



That’ll be it for today! I do have a few more map improvements in store for you, but those will have to wait.  
Until next time!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27315718/report)

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

- [1](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [12](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/page-12#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/page-2#posts)

1 of 12

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/page-12#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/?order=prdx_dd_reaction_score)

[![Voy](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/Wiki_patron/s/TopPatronBadge.png)](https://forum.paradoxplaza.com/forum/members/voy.478583/)

#### [Voy](https://forum.paradoxplaza.com/forum/members/voy.478583/)

##### Wiki Royalty

**52 Badges**

Apr 20, 2012

3.978

8.039

- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![Sengoku](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Sengoku.png "Sengoku")
- ![Magicka](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/magickaIcon.png "Magicka")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Stellaris - Path to Destruction bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Utopia.png "Stellaris - Path to Destruction bundle")
- ![Cities: Skylines - Mass Transit](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CitiesSkylines_MassTransit_16x16.png "Cities: Skylines - Mass Transit")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![Crusader Kings II: Jade Dragon](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2jd_forumicon.png "Crusader Kings II: Jade Dragon")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Cities: Skylines - Parklife](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CSLParkLife.png "Cities: Skylines - Parklife")
- ![Crusader Kings II: Holy Fury Pre-order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holyfuryPO.png "Crusader Kings II: Holy Fury Pre-order")
- ![Stellaris: Distant Stars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Distantstars.png "Stellaris: Distant Stars")
- ![Stellaris: Megacorp](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MegaCorp-ForumIcon.png "Stellaris: Megacorp")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Imperator: Rome Deluxe Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ImperatorDeluxeicon.png "Imperator: Rome Deluxe Edition")
- ![Cities: Skylines - Natural Disasters](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CS_ND_icon_16x16.png "Cities: Skylines - Natural Disasters")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Imperator: Rome - Magna Graecia](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MagnGraeciaIcon.png "Imperator: Rome - Magna Graecia")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Victoria 3 Sign Up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/v3_signup_forum_icon.png "Victoria 3 Sign Up")
- ![Crusader Kings II: Conclave](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DLC_icon_Conclave.png "Crusader Kings II: Conclave")
- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")
- ![500k Club](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/500k_red.png "500k Club")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Cities: Skylines - After Dark](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/CS_AD_16x16_fotumicon.png "Cities: Skylines - After Dark")
- ![Crusader Kings II: Monks and Mystics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/monksandmystics.png "Crusader Kings II: Monks and Mystics")
- ![Cities: Skylines - Snowfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/snowflake_16_4.png "Cities: Skylines - Snowfall")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellnova.png "Stellaris: Galaxy Edition")
- ![Stellaris: Galaxy Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellgalaxy.png "Stellaris: Galaxy Edition")
- ![Crusader Kings II: Reapers Due](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/reapers_due_forum_icon.png "Crusader Kings II: Reapers Due")
- ![Tyranny: Archon Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/tyr_com.png "Tyranny: Archon Edition")
- ![Major Wiki Contributor](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/WikiModicon.png "Major Wiki Contributor")
- ![Stellaris: Digital Anniversary Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/plantoid.png "Stellaris: Digital Anniversary Edition")
- ![Stellaris: Leviathans Story Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/leviathans.png "Stellaris: Leviathans Story Pack")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Crusader Kings II: Rajas of India](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_rajas_of_india_forumicon.png "Crusader Kings II: Rajas of India")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![Tyranny - Tales from the Tiers](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Tyr_TftT.png "Tyranny - Tales from the Tiers")
- ![Stellaris: Synthetic Dawn](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Syn_dawn_forum_icon.png "Stellaris: Synthetic Dawn")
- ![Stellaris](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_base.png "Stellaris")

[](javascript:;)

- [Feb 23, 2021](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/post-27315727)


- [/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/post-27315727](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/post-27315727)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27315727/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-49-a-cold-embrace.1458798/post-27315727)

That's so nice to see. Thank you for bringing back some variation to the map! ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)")  

Maybe this will halt the expansion into Sapmi by the Scandinavian kings. Finger's crossed.

 

Last edited: Feb 23, 2021

<!-- artifact:reactions:start -->
- 11 Like
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
