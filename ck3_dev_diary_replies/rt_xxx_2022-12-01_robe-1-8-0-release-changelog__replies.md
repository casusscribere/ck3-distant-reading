---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1560180/"
forum_thread_id: 1560180
content_type: reply_thread
parent_dd_file: dd_xxx_2022-12-01_robe-1-8-0-release-changelog.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "CK3 - \"Robe\" 1.8.0 Release & Changelog"
dd_date: 2022-12-01
expansion: Friends and Foes
patch: Patch 1.8 (Robe)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 7
reply_count: 124
participant_count: 84
reply_date_first: 2022-12-01
reply_date_last: 2023-03-27
body_word_count: 7007
inline_image_count: 0
quoted_span_count: 72
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — CK3 - "Robe" 1.8.0 Release & Changelog

*124 replies from 84 participants across 7 pages*

## Reply 1 — participant_001 · 2022-12-01 · post-28653367

Hello everyone! I’m Henrik – nice to e-meet you – I’m a crazy plant person and producer at Paradox Interactive. I'm here to let you know that we have a release coming up for you today: 1.8.0 “ROBE” FREE UPDATE The update should be rolled out to a store near you some time during the day. I promise to keep this short because I understand you’re here for the changelog. As my dear colleague, and ambassador of horchata, Hugo presented last week, we’ve taken some time to put together an update that, apart from a couple of new features, focuses a fair bit on improved stability and bug fixes. We hope you are as excited as we are to continue the endeavours as rulers of lands and kingdoms (hopefully) both beautiful and prosperous. But enough me chit-chatting – to the details: Spoiler: 1.8.0 changelog ################### # Free Features ################### You can now save and load Custom Rulers! Create templates you can easily re-use everywhere on the world map. All the attributes besides the Dynasty and the Coat of Arms are saved. Completely reworked the Bookmark Screen; its now reorganized to allow more room for bookmarks, and they are now sorted by the year they belong to (867 and 1066). This comes with new and improved art for elements and buttons, as well as showing which DLC you have active. Added new and unique illustrations for every Tenet currently in the game! Added 17 new Custom Faith icons for use when creating new faiths, ranging from Ankhs and Boromian Circles to Doves and Chi Rhos! ################### # Hardware ################### Added support for Vulkan renderer OSX and Linux will now by default use the Vulkan renderer - This should increase the framerate significantly for M1 and M2 Mac players Added a setting to change the rendering backend under the graphics category ################### # Game balance ################### Disinheriting is now free for children with a disputed heritage or known bastard. There is however a global opinion penalty which is always applied when taking the interaction Mozarabs can now use a strong hook to force/coerce the pope into binding with rome Updated the consequences for revoking hostile Holy order, it now adds Fervor to their Faith, and potentially a negative county modifier Literalism is legal for all faiths to adopt If the game rule "strict regional heresy" is activated, the Mozarab faith will only appear in Iberia and North Africa Added additional reward to forming the Kingdom of Aragon Rulers will no longer be deposed if they happen to inherit a tyranny war from a lower tier ruler Added gold cost to the "truly special board" in the board game event “A Stroke of Luck” Breaking away from Rome now requires you to be in poor standing with your HoF Properly set low obligations on Custom Rulers who are vassals of the HRE ‘A Beautiful Specimen’ will be only triggered for lovers and soulmates now; not powerful vassals Iberian Conciliation achievement is now classified as "Hard" instead of "Medium" Auto-fire the Court Chaplain if they are excommunicated, except if you are also excommunicated yourself Contracting Assistance is now scaled by army size. ################### # AI ################### Fixed a case where a raiding unit could not find a path to go home in case when the capital was moved. In that case the unit will be disbanded The AI will not try convert children of a vassal with religious protection anymore The AI will marry young men to old women less often: the weight of alliances and the impact of age has been rebalanced The AI will now send fewer requests for chess challenges Blocked the AI from sending two interactions simultaneously, which could cause UI issues AI characters are a lot less likely to accept a war assistance contract against you if they are allied with you ################### # Interface ################### Fixed issue with change/revert buttons in interaction lists only being responsive on a small part of it Fixed so the Army Reorganization scroll area no longer scroll to the top when unit is moved The bookmark lands of Emir Yahya now match the actual in-game shape { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" } Holy orders no longer cause "Grant to..." button to disappear in the county capital Offer Guardianship notification and window now use the ‘Offer Guardianship’ title instead of ‘Send Proposal’ Unselectable beneficiaries will now be shown in the list with a tooltip explaining why they cannot be selected Adultery events (adultery.2001 & adultery.2002) now have improved texts for duels You can now always open the list of potential agents, even if none will accept to join the scheme. This can be used to, for example, plan who to seduce or fabricate hooks against to further your interests. Vassal contract modification window now warns when current liege is not the rightful liege Activated Regnal numbers for Count-tier characters to avoid non immersive lineages The "Is imprisoned = no" condition for all court positions is now hidden Court positions no longer display requirements that are the opposite of what they seek Added a section for showing the DLCs that are installed and active. It can be found in the main menu and the bookmark area ################### # Bug fixes ################### Fixed issue where players couldn't accept/decline artifact gifts Fixed issue with event learning_theology_special.1001 were doctrines from the same group wouldn't be removed before applying the new one Fixed German court grandeur tooltip for being above expected level Fixed issue where achievements would still be enabled after creating a custom ruler and not starting the game as them You no longer get "the Thief Slayer" nickname if you already have a positive nickname. Fixed issue where artifact repair cost would show wrong value in the repair window, now shows same value as in the repair button tooltip Fixed issue where ironman would reset when going into select any ruler Fixed issue where overwriting same ruler multiple times would block achievements to be enabled Bestow Royal Favor chancellor task is now canceled if the target vassal declares war on you Fixed an issues that would cause some hedonistic sins to be incorrectly categorized as virtues or vice versa Created missing localization for threatened_by_buildup_opinion Petitioning liege in Russian now uses correct localization macro Struggle messages will now only be shown for interlopers and involved characters Fixed chinese localization doing infinite recursion on localization macro Moved the locators for special buildings in Tenerife to spawn buildings on landmass rather than in the water We now properly communicate in advance that the Subjugation war is only available once per lifetime Notifications for struggle endings are no longer sent to every single player in the lobby, instead selecting those either involved in the struggle or within a certain proximity of the region. fp2_struggle.2021.a.a is no longer blatantly misleading The tooltip of Invite to Activity displays a proper explanation when none of them is available "Desires of the Flesh" now checks what world region you are in before selecting a faith for you to follow Properly handle Duchy and Kingdom Holy Wars within the Struggle Removed duplicated check that were done for characters joining some factions Holy Wars properly deactivated after the Detente ending for the relevant cultures Fixed namespace issues with fp2_Struggle.2024 (now martial_chivalry.4001) Explicitly say that a Faith or Culture needs to control 80% of the counties to get involved within the Iberian Struggle Fixed issue where FP2 3D assets were being overwritten by their generic counterparts. We now display the right cost for the "Invite to Activity interaction"; it used to be swapped Head of Faith titles can no longer be granted to vassals Prevent players from cloning their mercenary armies Fixed localization in invitation to lieges council letter for Spanish Character info is now hidden for the thief in fp2_struggle.2009 Player now receives heresiarch trait when converting to Adoptionism The Found an Empire is now blocked for Involved and Interloper of the Iberian Struggle. The new condition is however only displayed for characters with an involved Faith or Culture, and living nearby Fixed parsing issues with fund_inspiration.2080 Fixed an issue where multiplayer got out of sync when a player hot joined the session Offering Relief events no longer gives you an improved opinion towards yourself. With that fixed, it's still important to remember to love thy self, you're doing good, keep it up! Expanded acceptance criteria for christian bones, christian syncretists can now display christian bones in their court. Finally allowing Basque pagans to equip and enjoy christian bones. Added the word “been” to “I have riding” to result in “I have been riding” in fund_inspiration.6001 ################### # Other ################### Updated name of "Reconquista" cultural innovation to something more historically accurate Added the Sayyid trait to some characters from the Hammudid house who were missing it Added new outcomes to boardgames Fixed line breaks in select Chinese localization keys Aragonese now speak the Oc´Romance language Set Wanda as a daughter of Krak I as it should be in 867 Tabletop Warriors now has a more natural reading description Fixed the dynasty reference for the Chinese Xue Dynasty Clarified the consequences of Dissolution faction Added new localization for creating a new faith that keeps the former pope as the new pope Refresh factions against liege after player character change Fate of Iberia: the Struggle Ending Achievements now have greater clarity as to what ending they refer to Zandaqa can now be rejected when pledging submission to a caliph -HR (Not Human Resources)

## Reply 2 — participant_002 · 2022-12-01 · post-28655366

<!-- artifact:quote:start -->
> pdxhr said: You can now always open the list of potential agents, even if none will accept to join the scheme. This can be used to, for example, plan who to seduce or fabricate hooks against to further your interests. Click to expand...
<!-- artifact:quote:end -->
This is good. Always found this annoying.

## Reply 3 — participant_003 · 2022-12-01 · post-28655384

<!-- artifact:quote:start -->
> pdxhr said: The AI will marry young men to old women less often: the weight of alliances and the impact of age has been rebalanced Click to expand...
<!-- artifact:quote:end -->
Thank god for that! (Image from 929221323 on reddit) On a side note, I don't see it in the patch notes, but does anyone know if the "Iberian walls are everywhere" bug has been fixed? Sometimes I see fixes get snuck in unannounced in the patch notes.

## Reply 4 — participant_004 · 2022-12-01 · post-28655386

County of CK3 Paradox Plaza gets Popular opinion: +10 (new Dev diary) Lurking Forum Rabble faction was disbanded

## Reply 5 — participant_005 · 2022-12-01 · post-28655399

<!-- artifact:quote:start -->
> pdxhr said: Holy orders no longer cause "Grant to..." button to disappear in the county capital Click to expand...
<!-- artifact:quote:end -->
I nearly missed this, because this post does not show up in the "featured content" area of the forum's main page. So that was the issue! It always drove me crazy when that button disappeared, but I was never able to see a pattern behind it.

## Reply 6 — participant_006 · 2022-12-01 · post-28655408

No fix for mods causing instant crashes on load when more than one modifies an accessory file? It's been nearly three months with no fix, it makes multiple mods essentially unusable :c CK III - Crash to Desktop when running two or more mods that modify one of the accessory files. Short summary of your issue Crash to Desktop when running two or more mods that modify one of the accessory files. Game Version 1.7.0 What OS are you playing on? Windows What platform are you using? Steam What DLC do you have installed? Royal... forum.paradoxplaza.com

## Reply 7 — participant_007 · 2022-12-01 · post-28655441

These Vulkan changes beg for additional UI changes to support Steam Deck!

## Reply 8 — participant_002 · 2022-12-01 · post-28655453

<!-- artifact:quote:start -->
> Buladelu said: These Vulkan changes beg for additional UI changes to support Steam Deck! Click to expand...
<!-- artifact:quote:end -->
I was going to ask about that - since I have no earthly idea about Vulkan or whatever it is, other than I believe it has something to do with Steamdeck (among other things). What difference will it make for Steamdeck?

## Reply 9 — participant_008 · 2022-12-01 · post-28655457

Please, please, please fix this bug: CK III - "Truth is Relative" perk makes finding secrets much less likely Short summary of your issue "Truth is Relative" perk makes finding secrets much less likely Game Version 1.7 What OS are you playing on? Windows What platform are you using? Steam What DLC do you have installed? Royal Court... forum.paradoxplaza.com

## Reply 10 — participant_009 · 2022-12-01 · post-28655477

Thanks for the update.

## Reply 11 — participant_010 · 2022-12-01 · post-28655479

I didn't see anything in the notes, does this fix the "Create Head of Faith" button stealing your money and doing nothing?

## Reply 12 — participant_007 · 2022-12-01 · post-28655480

<!-- artifact:quote:start -->
> johnty5 said: I was going to ask about that - since I have no earthly idea about Vulkan or whatever it is, other than I believe it has something to do with Steamdeck (among other things). What difference will it make for Steamdeck? Click to expand...
<!-- artifact:quote:end -->
Probably better performance and stability. But the current issue with Steamdeck is not that but the UI. Victoria 3 works perfectly on SD, but not CK3.

## Reply 13 — participant_011 · 2022-12-01 · post-28655484

When updating my mods I noticed that the court positions were changed, all the skill requirements have been removed so now they dont need skills for the court positions which makes no sense at all, wouldnt you want the best person for a court position ?? Would love to know the reasoning behind it for it being removed.

## Reply 14 — participant_012 · 2022-12-01 · post-28655488

<!-- artifact:quote:start -->
> pdxhr said: Iberian Conciliation achievement is now classified as "Hard" instead of "Medium" Click to expand...
<!-- artifact:quote:end -->
Nice change. Now since the changing difficulty indicator for the achievement is on the radar, could you guys change 'Saga in Stone' to very hard from easy? It's the hardest one without some exploiting IMO.

## Reply 15 — participant_004 · 2022-12-01 · post-28655496

[LIST] [*]Fixed issue where FP2 3D assets were being overwritten by their generic counterparts. [/LIST] Does it mean that Iberian walls being everywhere on the map is fixed?

## Reply 16 — participant_002 · 2022-12-01 · post-28655506

<!-- artifact:quote:start -->
> pdxhr said: Disinheriting is now free for children with a disputed heritage or known bastard. There is however a global opinion penalty which is always applied when taking the interaction Click to expand...
<!-- artifact:quote:end -->
It's only free to disinherit non-legitimised bastards, right? Legitimised ones still cost renown. Maybe I'm missing something, but why would you want to disinherit non-legitimised bastards? They don't inheret titles anyway.

## Reply 17 — participant_013 · 2022-12-01 · post-28655515

<!-- artifact:quote:start -->
> AdaChanDesu said: No fix for mods causing instant crashes on load when more than one modifies an accessory file? It's been nearly three months with no fix, it makes multiple mods essentially unusable :c CK III - Crash to Desktop when running two or more mods that modify one of the accessory files. Short summary of your issue Crash to Desktop when running two or more mods that modify one of the accessory files. Game Version 1.7.0 What OS are you playing on? Windows What platform are you using? Steam What DLC do you have installed? Royal... forum.paradoxplaza.com Click to expand...
<!-- artifact:quote:end -->
Heya AdaChanDesu, this should have been fixed with the latest update. Please let me know if it hasn't!

## Reply 18 — participant_014 · 2022-12-01 · post-28655533

Lets gooo!! Any word on being able to flavourise Court Position title names yet for modders ?

## Reply 19 — participant_015 · 2022-12-01 · post-28655545

Fantastic, thanks for the hard work. Can't wait for what come next.

## Reply 20 — participant_016 · 2022-12-01 · post-28655548

Code: ERROR: ld.so: object '/home/nixos/.applications/Steam/ubuntu12_32/gameoverlayrenderer.so' from LD_PRELOAD cannot be preloaded (wrong ELF class: ELFCLASS32): ignored. ERROR: ld.so: object '/home/nixos/.applications/Steam/ubuntu12_32/gameoverlayrenderer.so' from LD_PRELOAD cannot be preloaded (wrong ELF class: ELFCLASS32): ignored. ./ck3: error while loading shared libraries: libtinfo.so.6: cannot open shared object file: No such file or directory Sigh. I've tried a clean install, didn't help. Setting the version back to 1.7.2 does, though, so evidently the issue is with 1.8

## Reply 21 — participant_017 · 2022-12-01 · post-28655553

Was this bug fixed? CK III - Dualist characters with a "syncretism" tenet in their faith are hostile to members of the syncretized religion with "gnosticism" tenet Short summary of your issue Dualist characters with a "syncretism" tenet in their faith are hostile to members of the syncretized religion with "gnosticism" in their faith Game Version 1.6.1.2 What OS are you playing on? Windows What... forum.paradoxplaza.com

## Reply 22 — participant_018 · 2022-12-01 · post-28655554

<!-- artifact:quote:start -->
> AdaChanDesu said: No fix for mods causing instant crashes on load when more than one modifies an accessory file? It's been nearly three months with no fix, it makes multiple mods essentially unusable :c CK III - Crash to Desktop when running two or more mods that modify one of the accessory files. Short summary of your issue Crash to Desktop when running two or more mods that modify one of the accessory files. Game Version 1.7.0 What OS are you playing on? Windows What platform are you using? Steam What DLC do you have installed? Royal... forum.paradoxplaza.com Click to expand...
<!-- artifact:quote:end -->
Internally, this should work now; and during the past week the devs of Community Flavor Pack, Ethnicities and Portraits Expanded have been able to load together without problem, just wait for them to publically upload the newest patch; Although not mentioned in the notes; it has been fixed.

## Reply 23 — participant_019 · 2022-12-01 · post-28655572

<!-- artifact:quote:start -->
> Hellfell said: [LIST] [*]Fixed issue where FP2 3D assets were being overwritten by their generic counterparts. [/LIST] Does it mean that Iberian walls being everywhere on the map is fixed? Click to expand...
<!-- artifact:quote:end -->
Iberian masonry knowledge should no longer be unhistorically widespread. : )

## Reply 24 — participant_019 · 2022-12-01 · post-28655576

Also clarification for Vulkan renderer being added is that it was mainly added for our Mac and Linux players so they aren't forced to run the game on an outdated OpenGL renderer which also had compatibility issues for M1 and M2 chipsets. For Windows players we still recommend that you run the DirectX11 renderer.

## Reply 25 — participant_020 · 2022-12-01 · post-28655594

<!-- artifact:quote:start -->
> pdxhr said: Updated the consequences for revoking hostile Holy order, it now adds Fervor to their Faith, and potentially a negative county modifie Click to expand...
<!-- artifact:quote:end -->
Interesting change. However, I see no mention of "being unable to revoke lands from hostile holy order"bug fix though. Imo, I should be able to demand my vassals to revoke the land from them eventhough I do not hold the county directly.

## Reply 26 — participant_021 · 2022-12-01 · post-28655596

<!-- artifact:quote:start -->
> Nubjunkie said: Please, please, please fix this bug: CK III - "Truth is Relative" perk makes finding secrets much less likely Short summary of your issue "Truth is Relative" perk makes finding secrets much less likely Game Version 1.7 What OS are you playing on? Windows What platform are you using? Steam What DLC do you have installed? Royal Court... forum.paradoxplaza.com Click to expand...
<!-- artifact:quote:end -->
There's a mod for that, I think called exactly that, forgive me if I'm not telling you anything new though. I couldn't hit download hard enough when I found out.

## Reply 27 — participant_022 · 2022-12-01 · post-28655597

Still no fix for Islam religion and Orthodox nit holy warring each other?(may be a de jure problem between Byzantine and Persia/Arabia de jure empires) Anyway, thanks for the patch!

## Reply 28 — participant_013 · 2022-12-01 · post-28655616

<!-- artifact:quote:start -->
> Satcharna said: Code: ERROR: ld.so: object '/home/nixos/.applications/Steam/ubuntu12_32/gameoverlayrenderer.so' from LD_PRELOAD cannot be preloaded (wrong ELF class: ELFCLASS32): ignored. ERROR: ld.so: object '/home/nixos/.applications/Steam/ubuntu12_32/gameoverlayrenderer.so' from LD_PRELOAD cannot be preloaded (wrong ELF class: ELFCLASS32): ignored. ./ck3: error while loading shared libraries: libtinfo.so.6: cannot open shared object file: No such file or directory Sigh. I've tried a clean install, didn't help. Setting the version back to 1.7.2 does, though, so evidently the issue is with 1.8 Click to expand...
<!-- artifact:quote:end -->
Heya! For any issues or bugs, please make a bug report in our bug report forum and we will take a look at it! Crusader Kings III - Bug Report (Archive) forum.paradoxplaza.com

## Reply 29 — participant_023 · 2022-12-01 · post-28655619

Count tier vassals finally receiving Regnal numbers! Huge improvement for RP, thanks guys. Now Count Hugues XVIII de Lusignan can happen lol.

## Reply 30 — participant_024 · 2022-12-01 · post-28655646

I can now transfer all my knights from army to army without scrolling down for each one, this is the most important change in CK3's history.

## Reply 31 — participant_025 · 2022-12-01 · post-28655659

<!-- artifact:quote:start -->
> pdxhr said: # Hardware ################### Added support for Vulkan renderer Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Divine said: Also clarification for Vulkan renderer being added is that it was mainly added for our Mac and Linux players so they aren't forced to run the game on an outdated OpenGL renderer which also had compatibility issues for M1 and M2 chipsets. For Windows players we still recommend that you run the DirectX11 renderer. Click to expand...
<!-- artifact:quote:end -->
Nice! ... ok, that tooltip is a bit less nice Oh, alright. I thought it might have been for AMD users too, good to know. Edit: Also, error log when starting the game now (as soon as reaching the main menu) : Spoiler: Error.log Code: [18:04:51][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueFloat' in 'RandomizableValueFloat.GetValue'. [18:04:51][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueFloat' in 'RandomizableValueFloat.GetValue'. [18:04:51][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueFloat.GetValue' [18:04:51][pdx_gui_localize.cpp:249]: gui/tool_property_randomizable_types.gui:43 - Failed parsing localized text: [RandomizableValueFloat.GetValue|3] [18:04:51][pdx_gui_factory.cpp:911]: gui/tool_property_randomizable_types.gui:43 - Failed converting property 'raw_text'(2327) [18:04:51][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueFloat' in 'RandomizableValueFloat.SetValue'. [18:04:51][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueFloat' in 'RandomizableValueFloat.SetValue'. [18:04:51][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueFloat.SetValue' [18:04:51][pdx_gui_factory.cpp:906]: gui/tool_property_randomizable_types.gui:48 - Failed parsing data statement 'RandomizableValueFloat.SetValue' for property 'oneditingfinished'(853) [18:04:51][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueFloat' in 'RandomizableValueFloat.Randomize'. [18:04:51][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueFloat' in 'RandomizableValueFloat.Randomize'. [18:04:51][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueFloat.Randomize' [18:04:51][pdx_gui_factory.cpp:906]: gui/tool_property_randomizable_types.gui:53 - Failed parsing data statement 'RandomizableValueFloat.Randomize' for property 'onclick'(775) [18:04:51][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueInt' in 'RandomizableValueInt.GetValue'. [18:04:51][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueInt' in 'RandomizableValueInt.GetValue'. [18:04:51][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueInt.GetValue' [18:04:51][pdx_gui_localize.cpp:249]: gui/tool_property_randomizable_types.gui:65 - Failed parsing localized text: [RandomizableValueInt.GetValue] [18:04:51][pdx_gui_factory.cpp:911]: gui/tool_property_randomizable_types.gui:65 - Failed converting property 'raw_text'(2327) [18:04:51][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueInt' in 'RandomizableValueInt.SetValue'. [18:04:51][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueInt' in 'RandomizableValueInt.SetValue'. [18:04:51][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueInt.SetValue' [18:04:51][pdx_gui_factory.cpp:906]: gui/tool_property_randomizable_types.gui:70 - Failed parsing data statement 'RandomizableValueInt.SetValue' for property 'oneditingfinished'(853) [18:04:51][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueInt' in 'RandomizableValueInt.Randomize'. [18:04:51][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueInt' in 'RandomizableValueInt.Randomize'. [18:04:51][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueInt.Randomize' [18:04:51][pdx_gui_factory.cpp:906]: gui/tool_property_randomizable_types.gui:75 - Failed parsing data statement 'RandomizableValueInt.Randomize' for property 'onclick'(775) [18:04:51][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueFloat' in 'RandomizableValueFloat.GetValue'. [18:04:51][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueFloat' in 'RandomizableValueFloat.GetValue'. [18:04:51][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueFloat.GetValue' [18:04:51][pdx_gui_localize.cpp:249]: gui/tool_property_randomizable_types.gui:88 - Failed parsing localized text: [RandomizableValueFloat.GetValue|3] [18:04:51][pdx_gui_factory.cpp:911]: gui/tool_property_randomizable_types.gui:88 - Failed converting property 'raw_text'(2327) [18:04:51][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueFloat' in 'RandomizableValueFloat.SetValue'. [18:04:51][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueFloat' in 'RandomizableValueFloat.SetValue'. [18:04:51][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueFloat.SetValue' [18:04:51][pdx_gui_factory.cpp:906]: gui/tool_property_randomizable_types.gui:93 - Failed parsing data statement 'RandomizableValueFloat.SetValue' for property 'oneditingfinished'(853) [18:04:51][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueFloat' in 'RandomizableValueFloat.Randomize'. [18:04:51][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueFloat' in 'RandomizableValueFloat.Randomize'. [18:04:51][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueFloat.Randomize' [18:04:51][pdx_gui_factory.cpp:906]: gui/tool_property_randomizable_types.gui:98 - Failed parsing data statement 'RandomizableValueFloat.Randomize' for property 'onclick'(775) [18:04:52][pdx_data_factory.cpp:1391]: Failed to find type 'FilterablePropertyList' in 'FilterablePropertyList.Search'. [18:04:52][pdx_data_factory.cpp:1398]: Could not find promote for 'FilterablePropertyList' in 'FilterablePropertyList.Search'. [18:04:52][pdx_data_factory.cpp:1079]: Failed converting statement for 'FilterablePropertyList.Search' [18:04:52][pdx_gui_factory.cpp:906]: gui/toolspropertytypes.gui:424 - Failed parsing data statement 'FilterablePropertyList.Search' for property 'ontextchanged'(854) [18:04:52][pdx_data_factory.cpp:1391]: Failed to find type 'FilterablePropertyList' in 'FilterablePropertyList.GetSearchText'. [18:04:52][pdx_data_factory.cpp:1398]: Could not find promote for 'FilterablePropertyList' in 'FilterablePropertyList.GetSearchText'. [18:04:52][pdx_data_factory.cpp:1079]: Failed converting statement for 'FilterablePropertyList.GetSearchText' [18:04:52][pdx_gui_localize.cpp:249]: gui/toolspropertytypes.gui:426 - Failed parsing localized text: [FilterablePropertyList.GetSearchText] [18:04:52][pdx_gui_factory.cpp:911]: gui/toolspropertytypes.gui:426 - Failed converting property 'text'(143) [18:04:52][pdx_data_factory.cpp:1391]: Failed to find type 'FilterablePropertyList' in 'FilterablePropertyList.ClearSearchText'. [18:04:52][pdx_data_factory.cpp:1398]: Could not find promote for 'FilterablePropertyList' in 'FilterablePropertyList.ClearSearchText'. [18:04:52][pdx_data_factory.cpp:1079]: Failed converting statement for 'FilterablePropertyList.ClearSearchText' [18:04:52][pdx_gui_factory.cpp:906]: gui/toolspropertytypes.gui:432 - Failed parsing data statement 'FilterablePropertyList.ClearSearchText' for property 'onclick'(775) [18:04:52][pdx_data_factory.cpp:1391]: Failed to find type 'FilterablePropertyList' in 'FilterablePropertyList.GetPropertiesLabel'. [18:04:52][pdx_data_factory.cpp:1398]: Could not find promote for 'FilterablePropertyList' in 'FilterablePropertyList.GetPropertiesLabel'. [18:04:52][pdx_data_factory.cpp:1079]: Failed converting statement for 'FilterablePropertyList.GetPropertiesLabel' [18:04:52][pdx_gui_localize.cpp:249]: gui/toolspropertytypes.gui:450 - Failed parsing localized text: [FilterablePropertyList.GetPropertiesLabel] [18:04:52][pdx_gui_factory.cpp:911]: gui/toolspropertytypes.gui:450 - Failed converting property 'text'(143) [18:04:52][pdx_data_factory.cpp:1391]: Failed to find type 'FilterablePropertyList' in 'FilterablePropertyList.Search'. [18:04:52][pdx_data_factory.cpp:1398]: Could not find promote for 'FilterablePropertyList' in 'FilterablePropertyList.Search'. [18:04:52][pdx_data_factory.cpp:1079]: Failed converting statement for 'FilterablePropertyList.Search' [18:04:52][pdx_gui_factory.cpp:906]: gui/toolspropertytypes.gui:424 - Failed parsing data statement 'FilterablePropertyList.Search' for property 'ontextchanged'(854) [18:04:52][pdx_data_factory.cpp:1391]: Failed to find type 'FilterablePropertyList' in 'FilterablePropertyList.GetSearchText'. [18:04:52][pdx_data_factory.cpp:1398]: Could not find promote for 'FilterablePropertyList' in 'FilterablePropertyList.GetSearchText'. [18:04:52][pdx_data_factory.cpp:1079]: Failed converting statement for 'FilterablePropertyList.GetSearchText' [18:04:52][pdx_gui_localize.cpp:249]: gui/toolspropertytypes.gui:426 - Failed parsing localized text: [FilterablePropertyList.GetSearchText] [18:04:52][pdx_gui_factory.cpp:911]: gui/toolspropertytypes.gui:426 - Failed converting property 'text'(143) [18:04:52][pdx_data_factory.cpp:1391]: Failed to find type 'FilterablePropertyList' in 'FilterablePropertyList.ClearSearchText'. [18:04:52][pdx_data_factory.cpp:1398]: Could not find promote for 'FilterablePropertyList' in 'FilterablePropertyList.ClearSearchText'. [18:04:52][pdx_data_factory.cpp:1079]: Failed converting statement for 'FilterablePropertyList.ClearSearchText' [18:04:52][pdx_gui_factory.cpp:906]: gui/toolspropertytypes.gui:432 - Failed parsing data statement 'FilterablePropertyList.ClearSearchText' for property 'onclick'(775) [18:04:52][pdx_data_factory.cpp:1391]: Failed to find type 'FilterablePropertyList' in 'FilterablePropertyList.GetPropertiesLabel'. [18:04:52][pdx_data_factory.cpp:1398]: Could not find promote for 'FilterablePropertyList' in 'FilterablePropertyList.GetPropertiesLabel'. [18:04:52][pdx_data_factory.cpp:1079]: Failed converting statement for 'FilterablePropertyList.GetPropertiesLabel' [18:04:52][pdx_gui_localize.cpp:249]: gui/toolspropertytypes.gui:450 - Failed parsing localized text: [FilterablePropertyList.GetPropertiesLabel] [18:04:52][pdx_gui_factory.cpp:911]: gui/toolspropertytypes.gui:450 - Failed converting property 'text'(143) [18:04:52][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueInt' in 'RandomizableValueInt.GetValue'. [18:04:52][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueInt' in 'RandomizableValueInt.GetValue'. [18:04:52][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueInt.GetValue' [18:04:52][pdx_gui_localize.cpp:249]: gui/tool_property_randomizable_types.gui:110 - Failed parsing localized text: [RandomizableValueInt.GetValue] [18:04:52][pdx_gui_factory.cpp:911]: gui/tool_property_randomizable_types.gui:110 - Failed converting property 'raw_text'(2327) [18:04:52][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueInt' in 'RandomizableValueInt.SetValue'. [18:04:52][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueInt' in 'RandomizableValueInt.SetValue'. [18:04:52][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueInt.SetValue' [18:04:52][pdx_gui_factory.cpp:906]: gui/tool_property_randomizable_types.gui:115 - Failed parsing data statement 'RandomizableValueInt.SetValue' for property 'oneditingfinished'(853) [18:04:52][pdx_data_factory.cpp:1391]: Failed to find type 'RandomizableValueInt' in 'RandomizableValueInt.Randomize'. [18:04:52][pdx_data_factory.cpp:1398]: Could not find promote for 'RandomizableValueInt' in 'RandomizableValueInt.Randomize'. [18:04:52][pdx_data_factory.cpp:1079]: Failed converting statement for 'RandomizableValueInt.Randomize' [18:04:52][pdx_gui_factory.cpp:906]: gui/tool_property_randomizable_types.gui:120 - Failed parsing data statement 'RandomizableValueInt.Randomize' for property 'onclick'(775) And yes, this is vanilla CK3 1.8.0, and I also checked the game files integrity with Steam. Was this update... rushed (somehow)?

## Reply 32 — participant_026 · 2022-12-01 · post-28655662

4 new languages support incoming (Japanese, Braz-Por, Polish, Turkish)?

## Reply 33 — participant_027 · 2022-12-01 · post-28655671

https://forum.paradoxplaza.com/forum/threads/ck-iii-ai-ignores-war-target.1547122/#post-28614222 Guys, it's ONE code string. ONE. I even posted in the thread, it worked fine in 1.5 patch. Can you please fix it? As it stands right now enemy unit province has way higher priority than wargoal_province. AI will NEVER attack actual war goal and will ignore it for as long as humanly (nonhumanly) possible.

## Reply 34 — participant_016 · 2022-12-01 · post-28655673

<!-- artifact:quote:start -->
> Arakrates said: Heya! For any issues or bugs, please make a bug report in our bug report forum and we will take a look at it! Crusader Kings III - Bug Report (Archive) forum.paradoxplaza.com Click to expand...
<!-- artifact:quote:end -->
CK III - Game refuses to launch with Steam Runtime Environment on Linux (1.8.0) Short summary of your issue Game refuses to launch with Steam Runtime Environment on Linux (1.8.0) Game Version 1.8.0 What OS are you playing on? Linux What platform are you using? Steam What DLC do you have installed? Royal... forum.paradoxplaza.com I don't like filling out forms.

## Reply 35 — participant_028 · 2022-12-01 · post-28655748

such a big update for a 0.1 version

## Reply 36 — participant_029 · 2022-12-01 · post-28655750

<!-- artifact:quote:start -->
> pdxhr said: Fixed issue where achievements would still be enabled after creating a custom ruler and not starting the game as them Click to expand...
<!-- artifact:quote:end -->
So I guess this means the CK3 team is still devoted to the un-modded iron man achievement requirement despite the many reasons to get rid of it and the support for removing it? I realize I might be reading a bit more into this than I should, but it does not bode well for the issue. I also very much liked the ability to include a custom character in the game somewhere even when going for a "start as..." achievement.

## Reply 37 — participant_030 · 2022-12-01 · post-28655775

- Fixed font atlas not notifying the map system when textures where recycled, leading to garbled map names especially frequent in Chinese, Japanese, and Korean languages V3 inherited this bug from CK3, and this bug has been fixed in V3. So is there any plan to fix it in CK3？

## Reply 38 — participant_008 · 2022-12-01 · post-28655790

<!-- artifact:quote:start -->
> SmokeyMcSubpoena said: There's a mod for that, I think called exactly that, forgive me if I'm not telling you anything new though. I couldn't hit download hard enough when I found out. Click to expand...
<!-- artifact:quote:end -->
I know! I made the mod

## Reply 39 — participant_031 · 2022-12-01 · post-28655795

Well. This was a pleasent surprise. I am looking forward to play it this weekend. Hopefully the seduction-attempts are also curbed down. And more Faith-Icons are always a win.

## Reply 40 — participant_021 · 2022-12-01 · post-28655803

<!-- artifact:quote:start -->
> Nubjunkie said: I know! I made the mod Click to expand...
<!-- artifact:quote:end -->
Hahahaha thank you so much then, SUPER happy I added the caveat I did rofl Honestly your mod made me realize I wasn't going crazy, and the feature didn't work right. Thanks again!

## Reply 41 — participant_032 · 2022-12-01 · post-28655869

The character select screen lost some features a few patches ago that haven't been restored Just wanted to highlight this personal bugbear of mine since there's a few threads at the moment about missing features. This was the character select screen as of Patch 1.2.1, which was the latest I remember it having this kind of... forum.paradoxplaza.com Still would just like to attempt to lobby for this feature to be restored!!

## Reply 42 — participant_008 · 2022-12-01 · post-28655930

<!-- artifact:quote:start -->
> SmokeyMcSubpoena said: Hahahaha thank you so much then, SUPER happy I added the caveat I did rofl Honestly your mod made me realize I wasn't going crazy, and the feature didn't work right. Thanks again! Click to expand...
<!-- artifact:quote:end -->
A pleasure, my friend. The irony, of course, being that I only play on ironman. I only made the mod to show how easy it is to fix!

## Reply 43 — participant_025 · 2022-12-01 · post-28655954

<!-- artifact:quote:start -->
> Nubjunkie said: The irony, of course, being that I only play on ironman. Click to expand...
<!-- artifact:quote:end -->
I assume you meant "for achievements" since nothing would prevent you from playing modded ironman otherwise?

## Reply 44 — participant_033 · 2022-12-01 · post-28655972

So how do you get that crown?

## Reply 45 — participant_034 · 2022-12-01 · post-28655984

<!-- artifact:quote:start -->
> Luka031 said: So how do you get that crown? Click to expand...
<!-- artifact:quote:end -->
Go to Crusaderkings.com and sign up for the newsletter and link your account to whatever place you have the game in the settings there. If you are, then you'll find it last in the headgear section. "Plock diadem".

## Reply 46 — participant_035 · 2022-12-01 · post-28656053

Thanks for the update

## Reply 47 — participant_036 · 2022-12-01 · post-28656110

Wasn't expecting the patch this soon, very nice. Is this bugfix list exhaustive? Was hopeful the "battles not giving fame/prestige" bug from royal court's release would be addressed.

## Reply 48 — participant_033 · 2022-12-01 · post-28656132

<!-- artifact:quote:start -->
> Voy said: Go to Crusaderkings.com and sign up for the newsletter and link your account to whatever place you have the game in the settings there. If you are, then you'll find it last in the headgear section. "Plock diadem". Click to expand...
<!-- artifact:quote:end -->
Linked my account and subbed to the news. DIdn't get the crown. Do you need to reedem it somehow or it will automatically get in the game?

## Reply 49 — participant_034 · 2022-12-01 · post-28656148

<!-- artifact:quote:start -->
> Luka031 said: Linked my account and subbed to the news. DIdn't get the crown. Do you need to reedem it somehow or it will automatically get in the game? Click to expand...
<!-- artifact:quote:end -->
Do some experimenting.

## Reply 50 — participant_037 · 2022-12-01 · post-28656187

Super an update that is already a serious bug, I could not choose a period. I'm really looking forward to the new hyper interesting improvement that is adding new useless icon. I can't wait to see the real update after paying a 15$ dlc.

## Reply 51 — participant_002 · 2022-12-01 · post-28656207

<!-- artifact:quote:start -->
> Dragonaryx said: I could not choose a period Click to expand...
<!-- artifact:quote:end -->
What does this mean?

## Reply 52 — participant_037 · 2022-12-01 · post-28656252

<!-- artifact:quote:start -->
> johnty5 said: What does this mean? Click to expand...
<!-- artifact:quote:end -->
I can't choose the start date. I'm just stuck at 1066. I don't know if this was the purpose of the update but it's annoying. I wanted to test the new update but apparently I have to wait for another update to fix the problem of the new update.

## Reply 53 — participant_038 · 2022-12-01 · post-28656263

I hope this is a bug, with strict herecies i get forced to become a heretic from catholosism without a choice.

## Reply 54 — participant_002 · 2022-12-01 · post-28656274

<!-- artifact:quote:start -->
> Dragonaryx said: I can't choose the start date. I'm just stuck at 1066. Click to expand...
<!-- artifact:quote:end -->
Working for me. What happens when you click the 867 tab?

## Reply 55 — participant_037 · 2022-12-01 · post-28656280

<!-- artifact:quote:start -->
> johnty5 said: Working for me. What happens when you click the 867 tab? Click to expand...
<!-- artifact:quote:end -->
It has nothing to display, the only thing I know that I am in the year 1066 is when I click on one of the characters.

## Reply 56 — participant_037 · 2022-12-01 · post-28656283

<!-- artifact:quote:start -->
> Ambush19 said: I hope this is a bug, with strict herecies i get forced to become a heretic from catholosism without a choice. Click to expand...
<!-- artifact:quote:end -->
AH

## Reply 57 — participant_002 · 2022-12-01 · post-28656289

<!-- artifact:quote:start -->
> Dragonaryx said: It has nothing to display, the only thing I know that I am in the year 1066 is when I click on one of the characters. Click to expand...
<!-- artifact:quote:end -->
So is it that you can you see the 867 tab - but nothing happens when you click it? Or is it that the 867 tab doesn't appear for you?

## Reply 58 — participant_037 · 2022-12-01 · post-28656298

<!-- artifact:quote:start -->
> johnty5 said: So is it that you can you see the 867 tab - but nothing happens when you click it? Or is it that the 867 tab doesn't appear fo Click to expand...
<!-- artifact:quote:end -->
There is no 867 that appears in my screen.

## Reply 59 — participant_002 · 2022-12-01 · post-28656304

<!-- artifact:quote:start -->
> Dragonaryx said: There is no 867 that appears in my screen. Click to expand...
<!-- artifact:quote:end -->
So, when you click to start a new game - you don't see those "867" and "1066" tabs along the top? Can you post a screenshot of what you're seeing?

## Reply 60 — participant_037 · 2022-12-01 · post-28656324

<!-- artifact:quote:start -->
> johnty5 said: View attachment 921785 So, when you click to start a new game - you don't see those "867" and "1066" tabs along the top? Can you post a screenshot of what you're seeing? Click to expand...
<!-- artifact:quote:end -->
https://steamuserimages-a.akamaihd....icy=Letterbox&imcolor=#000000&letterbox=false . Maybe in the French version it has not

## Reply 61 — participant_034 · 2022-12-01 · post-28656346

<!-- artifact:quote:start -->
> Dragonaryx said: https://steamuserimages-a.akamaihd.net/ugc/2010323985675618422/097DEB7FD2976ADF267F2E3F1C6BDAA2EF907D7E/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=#000000&letterbox=false . Maybe in the French version it has not Click to expand...
<!-- artifact:quote:end -->
Make sure you're not any other branches/versions of the game by going to Betas and making sure it is none, restart steam and verify integrity if nothing works.

## Reply 62 — participant_037 · 2022-12-01 · post-28656372

<!-- artifact:quote:start -->
> Voy said: Make sure you're not any other branches/versions of the game by going to Betas and making sure it is none, restart steam and verify integrity if nothing works. Click to expand...
<!-- artifact:quote:end -->
Finally it was good to close and open steam.

## Reply 63 — participant_039 · 2022-12-01 · post-28656373

<!-- artifact:quote:start -->
> Hellfell said: [LIST] [*]Fixed issue where FP2 3D assets were being overwritten by their generic counterparts. [/LIST] Does it mean that Iberian walls being everywhere on the map is fixed? Click to expand...
<!-- artifact:quote:end -->
Not only did they fix the Iberian walls, they also started using the Mediterranean 03 and 04, MENA 03 and India 03 and 04 walls that have never been in use in the game before! They don't look dramatically different from regular walls, but at least now you can expect your wall coloring to match your castle coloring. I am very happy.

## Reply 64 — participant_040 · 2022-12-01 · post-28656472

is Sacred Childbirth meant to be an option to all religions now? Because that wasn't in the patch notes.

## Reply 65 — participant_041 · 2022-12-01 · post-28656893

Do saves from a previous version work?

## Reply 66 — participant_042 · 2022-12-02 · post-28656921

Glad it's easier to disinherit bastards now.

## Reply 67 — participant_043 · 2022-12-02 · post-28656931

So, we get only a very small update

## Reply 68 — participant_034 · 2022-12-02 · post-28656934

<!-- artifact:quote:start -->
> Ksiendzu said: So, we get only a very small update View attachment 921880 Click to expand...
<!-- artifact:quote:end -->
It does more than the patch notes lead on.

## Reply 69 — participant_044 · 2022-12-02 · post-28656963

No unique tenet icon for the Canary Islands Faith? Regardless, these new graphics are great. My compliments to the artists.

## Reply 70 — participant_045 · 2022-12-02 · post-28656992

<!-- artifact:quote:start -->
> pdxhr said: Fixed issue where ironman would reset when going into select any ruler Click to expand...
<!-- artifact:quote:end -->
Thank you, it only took 27 months

## Reply 71 — participant_046 · 2022-12-02 · post-28657006

Nice patch. I think struggle’s Dominance ending’s condition should be more easy. After uniting all of iberia, waiting for Hostility struggle phase is not fun at all.

## Reply 72 — participant_047 · 2022-12-02 · post-28657032

No dismantle artifacts still?!

## Reply 73 — participant_048 · 2022-12-02 · post-28657099

<!-- artifact:quote:start -->
> pdxhr said: Literalism is legal for all faiths to adopt Click to expand...
<!-- artifact:quote:end -->
Nice.

## Reply 74 — participant_049 · 2022-12-02 · post-28657206

Any chance Sacrificial Ceremonies can get opened up for non-Achamanism? Since it was released it's always felt too restrictive to me that Eastern and even Pagan religions can't take it, even though they're permitted Gruesome Festivals. Also, now that Head of Faith titles can't be given to vassals, how would one convert religions or allow titles to pass to an heir with a different faith?

## Reply 75 — participant_050 · 2022-12-02 · post-28657252

<!-- artifact:quote:start -->
> OSX and Linux will now by default use the Vulkan renderer - This should increase the framerate significantly for M1 and M2 Mac players Click to expand...
<!-- artifact:quote:end -->
I have Linux, just launched the game and renderer says "Open GL". Ok, changed it to Vulkan, but the fps fell horribly, even on on menu screen it's 8-10.

## Reply 76 — participant_051 · 2022-12-02 · post-28657288

<!-- artifact:quote:start -->
> pdxhr said: ‘A Beautiful Specimen’ will be only triggered for lovers and soulmates now; not powerful vassals Click to expand...
<!-- artifact:quote:end -->
Love can't bloom at council meeting now

## Reply 77 — participant_019 · 2022-12-02 · post-28657411

<!-- artifact:quote:start -->
> snegovick said: I have Linux, just launched the game and renderer says "Open GL". Ok, changed it to Vulkan, but the fps fell horribly, even on on menu screen it's 8-10. Click to expand...
<!-- artifact:quote:end -->
In our internal tests we saw the largest gains for Mac machines but we still saw some gains for Linux machines over the OpenGL renderer. Would you mind listing your hardware/OS specifications to me in a DM? I can't promise anything but it could be an interesting case for us to see if we can replicate. There are so many hardware configurations live now so it's not uncommon that certain combinations have unique results due to some compatibility issue showing up - and maybe we can find a way to level those issues.

## Reply 78 — participant_001 · 2022-12-02 · post-28657497

<!-- artifact:quote:start -->
> kosteyy said: Do saves from a previous version work? Click to expand...
<!-- artifact:quote:end -->
In general - may adventures that took place in the previous release, stay in the previous release. We do test saved games from a previous version but it is not something we officially support.

## Reply 79 — participant_052 · 2022-12-02 · post-28657588

<!-- artifact:quote:start -->
> pdxhr said: OSX and Linux will now by default use the Vulkan renderer - This should increase the framerate significantly for M1 and M2 Mac players Click to expand...
<!-- artifact:quote:end -->
I still have high hopes you make a port to Ipad. The only issue is that I would have to buy all expansions twice.

## Reply 80 — participant_053 · 2022-12-02 · post-28657598

@pdxhr Sounds an ok update, the regnal number for count really would be very nice now. But on steam it says a new crown if you register on the site, how do we get the new crown. haha sounds stupid, but that pick my interest​

## Reply 81 — participant_019 · 2022-12-02 · post-28657681

<!-- artifact:quote:start -->
> Dragonaryx said: https://steamuserimages-a.akamaihd.net/ugc/2010323985675618422/097DEB7FD2976ADF267F2E3F1C6BDAA2EF907D7E/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=#000000&letterbox=false . Maybe in the French version it has not Click to expand...
<!-- artifact:quote:end -->
This looks suprisingly much like our old bookmark selection screen. Do you have any mod active that might be changing the interface here which would override the new vanilla bookmark interface?

## Reply 82 — participant_054 · 2022-12-02 · post-28657718

<!-- artifact:quote:start -->
> dannazgui said: @pdxhr ​Sounds an ok update, the regnal number for count really would be very nice now. But on steam it says a new crown if you register on the site, how do we get the new crown. haha​​sounds stupid, but that pick my interest​ Click to expand...
<!-- artifact:quote:end -->
Go to crusaderkings.com and sign up for the newsletter, then you'll find it last in the headgear section.

## Reply 83 — participant_055 · 2022-12-02 · post-28657850

ck2 had 8 big dlcs at this time while ck3 has 1 big dlc, 2 small dlcs, 1 event pack and couple small patches. I know it hurted your wallet back then but game always was fresh and new, you always can do something new. But this patch add some fixes and small balance changes. Boring

## Reply 84 — participant_037 · 2022-12-02 · post-28657879

<!-- artifact:quote:start -->
> Divine said: This looks suprisingly much like our old bookmark selection screen. Do you have any mod active that might be changing the interface here which would override the new vanilla bookmark interface? Click to expand...
<!-- artifact:quote:end -->
I had understood that it was the mods activated, but even deactivated it is necessary to leave steam and open it otherwise it does not work. And so when you activate, I have the old interface.

## Reply 85 — participant_056 · 2022-12-02 · post-28658065

<!-- artifact:quote:start -->
> stargames said: ck2 had 8 big dlcs at this time while ck3 has 1 big dlc, 2 small dlcs, 1 event pack and couple small patches. I know it hurted your wallet back then but game always was fresh and new, you always can do something new. But this patch add some fixes and small balance changes. Boring Click to expand...
<!-- artifact:quote:end -->
How are you are getting 8? Ck3 has now been out for around 2 years and 3 months (Released september 2020). Ck2 was released in Februari 2012. 2 years and 3 months after that had 7 expansions released (SoI, LoR, SI, TR, TOG, SoA and ROI). Moreover not all of those would qualify as a big dlc. I'd say the only expansions that would qualify as "big" in this time were The Old gods and Rajas of India and TOG is comparable to "Northern Lords" in ck3. CK2 did probably have more content, but not by a significant amount and in fact the last year of CK3 content has outpaced most CK2 years (We have had 2 significant expansions and an event pack in 2022).

## Reply 86 — participant_019 · 2022-12-02 · post-28658079

<!-- artifact:quote:start -->
> Dragonaryx said: I had understood that it was the mods activated, but even deactivated it is necessary to leave steam and open it otherwise it does not work. And so when you activate, I have the old interface. Click to expand...
<!-- artifact:quote:end -->
Thank you for elaborating. It should be enough to deactivate or remove the mod in the launcher but there might still be some oddities that might occur. Happy to hear that it's working for you now. : )

## Reply 87 — participant_057 · 2022-12-02 · post-28658290

<!-- artifact:quote:start -->
> Disinheriting is now free for children with a disputed heritage or known bastard Click to expand...
<!-- artifact:quote:end -->
No celtic cross in new faith icons? Come on, Ireland deserves some love But not for an adopted commoner?

## Reply 88 — participant_036 · 2022-12-02 · post-28658821

<!-- artifact:quote:start -->
> stargames said: ck2 had 8 big dlcs at this time while ck3 has 1 big dlc, 2 small dlcs, 1 event pack and couple small patches. I know it hurted your wallet back then but game always was fresh and new, you always can do something new. But this patch add some fixes and small balance changes. Boring Click to expand...
<!-- artifact:quote:end -->
This patch does not fix many longstanding bugs, and introduces some far more obvious graphical bugs.

## Reply 89 — participant_058 · 2022-12-03 · post-28658891

So, with this update you can no longer create a custom character then play a different non-custom character while leaving ironman intact. Just a heads-up because in-game tooltips do not reflect this or indicate it in any way.

## Reply 90 — participant_059 · 2022-12-03 · post-28659111

<!-- artifact:quote:start -->
> pdxhr said: The Found an Empire is now blocked for Involved and Interloper of the Iberian Struggle. The new condition is however only displayed for characters with an involved Faith or Culture, and living nearby Click to expand...
<!-- artifact:quote:end -->
This will not fix the issue, that the spanish kingdoms can drift away to other empires, causing the iberian struggle to be forever, because Hispania has no longer any de-jure titles. And by the way someone can easily conquer a kingdom, who is not part of Hispania, switch their capital to this Kingdom, create an custom Empire and Hispania as no longer de-jure titles.

## Reply 91 — participant_060 · 2022-12-03 · post-28659207

<!-- artifact:quote:start -->
> pdxhr said: Iberian Conciliation achievement is now classified as "Hard" instead of "Medium" Click to expand...
<!-- artifact:quote:end -->
Why then not fix the saga in stone achievement?

## Reply 92 — participant_061 · 2022-12-03 · post-28659292

<!-- artifact:quote:start -->
> stargames said: ck2 had 8 big dlcs at this time while ck3 has 1 big dlc, 2 small dlcs, 1 event pack and couple small patches. I know it hurted your wallet back then but game always was fresh and new, you always can do something new. But this patch add some fixes and small balance changes. Boring Click to expand...
<!-- artifact:quote:end -->
I have to say that CK3 is more graphically complex than its predecessor, which would require more time to work on. However, overall I agree that for the time that the game has existed, one could implement way more content than there actually is.

## Reply 93 — participant_062 · 2022-12-03 · post-28659416

Not enough to be the last patch of the year. Lets hope in 2023

## Reply 94 — participant_063 · 2022-12-03 · post-28659734

<!-- artifact:quote:start -->
> Aragonese now speak the Oc´Romance language Click to expand...
<!-- artifact:quote:end -->
Is this a new Language? And is it just me or has Aragonese ingame still Iberian Vulgar?

## Reply 95 — participant_064 · 2022-12-03 · post-28659902

Hey @pdxhr there is something wrong with this post. It does not show up on the "Featured Conted" page at all.

## Reply 96 — participant_065 · 2022-12-04 · post-28660173

A new patch is always nice. But I can't see a fix for this gamebreaking bug, https://forum.paradoxplaza.com/foru...-as-a-maturidist-and-resigning-later.1543392/ nor for that bug: https://forum.paradoxplaza.com/foru...idnt-convert-after-demand-conversion.1543065/

## Reply 97 — participant_066 · 2022-12-04 · post-28660233

I noticed that my royal court positions of master of horse and hunt and royal architect were no longer restricted to vassals

## Reply 98 — participant_067 · 2022-12-04 · post-28660255

<!-- artifact:quote:start -->
> apollo1989vieten said: I noticed that my royal court positions of master of horse and hunt and royal architect were no longer restricted to vassals Click to expand...
<!-- artifact:quote:end -->
REALLY??? send me a screenshot.

## Reply 99 — participant_066 · 2022-12-04 · post-28661394

<!-- artifact:quote:start -->
> partywithhugo said: REALLY??? send me a screenshot. Click to expand...
<!-- artifact:quote:end -->
*(no text body — reaction-only or media-only post)*

## Reply 100 — participant_067 · 2022-12-05 · post-28661572

<!-- artifact:quote:start -->
> apollo1989vieten said: View attachment 923218 Click to expand...
<!-- artifact:quote:end -->
Yooo! Finally they fixed that! I didn't make sense to give vassals court positions because vassals are not courtiers. I always wanted to appoint my courtiers as my master of the hunt, master of the horse and royal architect. Now we have more positions for the courtiers.

## Reply 101 — participant_068 · 2022-12-05 · post-28661707

<!-- artifact:quote:start -->
> pdxhr said: Activated Regnal numbers for Count-tier characters to avoid non immersive lineages Click to expand...
<!-- artifact:quote:end -->
Such a small thing but it's absolutely my favorite in the whole update! I'm a sucker for regnal numbers.

## Reply 102 — participant_069 · 2022-12-05 · post-28662879

I'm using mac os and steam. I don't see the update available. Last I see is Bastion. How can I get this updated?

## Reply 103 — participant_070 · 2022-12-05 · post-28663105

<!-- artifact:quote:start -->
> pezezez said: I'm using mac os and steam. I don't see the update available. Last I see is Bastion. How can I get this updated? Click to expand...
<!-- artifact:quote:end -->
let the steam client connect to the internet, then select "none" in the beta list.

## Reply 104 — participant_071 · 2022-12-06 · post-28663761

just re-signed up for the newsletter. How do I receive the free unique crown now?

## Reply 105 — participant_036 · 2022-12-06 · post-28664028

Should we expect any hotfixes before christmas? The new tooltip/UI bug introduced in 1.8.0 makes the game pretty frustrating to navigate.

## Reply 106 — participant_072 · 2022-12-06 · post-28664180

Hello, I'm having an issue with the update 1.8., It doesn't show up. Instead there's a update named: avx_issue_hotfix. Don't know if anyone else is having this problem. In that case, were you aware of it? Do you know what I have to do to get the upddate? Thanks for the help.

## Reply 107 — participant_070 · 2022-12-06 · post-28665608

<!-- artifact:quote:start -->
> manukord said: Hello, I'm having an issue with the update 1.8., It doesn't show up. Instead there's a update named: Click to expand...
<!-- artifact:quote:end -->
Select "NONE" from the beta list.

## Reply 108 — participant_054 · 2022-12-09 · post-28669982

<!-- artifact:quote:start -->
> pdxhr said: Spoiler: 1.8.0 changelog ################### # Other ################### Added the Sayyid trait to some characters from the Hammudid house who were missing it Click to expand...
<!-- artifact:quote:end -->
Rahima bint Muhammad Hammudid still doesn't have the Sayyid trait!

## Reply 109 — participant_073 · 2022-12-09 · post-28670068

I didn't receive the update through paradox launcher. The latest version I have is 1.6.1.2

## Reply 110 — participant_074 · 2022-12-09 · post-28670129

The tooltip/UI is bugged. There is also trouble with ironman mode and achievements. Can we expect a hotfix near soon?

## Reply 111 — participant_032 · 2022-12-09 · post-28670154

<!-- artifact:quote:start -->
> DiZa said: The tooltip/UI is bugged. There is also trouble with ironman mode and achievements. Can we expect a hotfix near soon? Click to expand...
<!-- artifact:quote:end -->
Yeah just checking we can maybe expect a hotfix before the Winter break?

## Reply 112 — participant_075 · 2022-12-09 · post-28670539

<!-- artifact:quote:start -->
> DiZa said: The tooltip/UI is bugged. There is also trouble with ironman mode and achievements. Can we expect a hotfix near soon? Click to expand...
<!-- artifact:quote:end -->
There’s trouble with Ironman mode and achievements? Is this a new thing?

## Reply 113 — participant_076 · 2022-12-10 · post-28671879

<!-- artifact:quote:start -->
> pdxhr said: OSX and Linux will now by default use the Vulkan renderer - This should increase the framerate significantly for M1 and M2 Mac players Click to expand...
<!-- artifact:quote:end -->
Thank you!!! I can finally play on my M1 Mac without insane lag!!!!!!

## Reply 114 — participant_077 · 2022-12-10 · post-28671946

I found something weird with the latest version. When I start a game with randomized faiths it crashes before/just after it reaches the 2nd day. I've checked every other game rule separately with randomized faith off and no problem. Has anyone else seen this? If you test this and say it's fine I'll assume it's something on my end. Update: I reinstalled the launch version and tested starting a new game with randomized faiths through each update. The bug appears at version 1.6.1. There were a lot of religion based changes (new events, new religions) in this version so can't pinpoint a likely root cause. Further update: I managed to start a game on the 1.6.0.1 version with full DLC, run 3 days, and save. I then updated to latest version and loaded the save file, no problems from there. So the issue is sitting in day 1 initiation. I suspect this means I'm not the only one who would be affected, but not many people mess around with these rules.

## Reply 115 — participant_078 · 2022-12-11 · post-28674456

<!-- artifact:quote:start -->
> pdxhr said: Added new and unique illustrations for every Tenet currently in the game! Click to expand...
<!-- artifact:quote:end -->
Cultural traditions next?

## Reply 116 — participant_079 · 2023-01-01 · post-28703198

Please put the update into Paradox Launcher. We are stuck at 1.6.1.2

## Reply 117 — participant_080 · 2023-01-01 · post-28703370

Will you please stop making these small updates... it deletes the game we have... ANd these small updates you a giving us is of no use anyway... If you do these updates, give us something more than "the man of steel" give of the pharoes or do something for china or india or tibet. Gives us something wild and new, And not the Iberian struggle, its not fun...(make it an option)

## Reply 118 — participant_075 · 2023-01-01 · post-28703542

<!-- artifact:quote:start -->
> Karnagedk said: Will you please stop making these small updates... it deletes the game we have... ANd these small updates you a giving us is of no use anyway... If you do these updates, give us something more than "the man of steel" give of the pharoes or do something for china or india or tibet. Gives us something wild and new, And not the Iberian struggle, its not fun...(make it an option) Click to expand...
<!-- artifact:quote:end -->
Most of the smallest updates (e.g., 1.8.0 to 1.8.1) will not affect your save game. If you did not feel a particular update was of use to you, you can always roll back and continue playing without fear of an update disrupting your current game. Also, the Iberian struggle can be disabled by either disabling the DLC or using a mod.

## Reply 119 — participant_042 · 2023-01-01 · post-28703605

<!-- artifact:quote:start -->
> Karnagedk said: Will you please stop making these small updates... it deletes the game we have... ANd these small updates you a giving us is of no use anyway... If you do these updates, give us something more than "the man of steel" give of the pharoes or do something for china or india or tibet. Gives us something wild and new, And not the Iberian struggle, its not fun...(make it an option) Click to expand...
<!-- artifact:quote:end -->
Also if they didn't periodically release smaller updates then people would start getting worried about "radio silence" and the "game is dead/dying" people would pop up again.

## Reply 120 — participant_081 · 2023-01-11 · post-28716683

<!-- artifact:quote:start -->
> pdxhr said: 1.8.0 “ROBE” FREE UPDATE Click to expand...
<!-- artifact:quote:end -->
It won't let me click on the link to download it

## Reply 121 — participant_075 · 2023-01-11 · post-28716826

<!-- artifact:quote:start -->
> DrPepperBand1t said: It won't let me click on the link to download it Click to expand...
<!-- artifact:quote:end -->
That’s not a link, it’s a title. You download updates through your Steam client, for example, and usually automatically.

## Reply 122 — participant_082 · 2023-02-18 · post-28778725

Just in case this was not as obvious for Steam gamers, look at the attached screenshot of my Steam client's CK3 "Launcher" pop-up, and zoom in middle right to see where it says just above the bottom-of-screen icons the version number is "1.8.1 (Robe)" that is listed just at the "king" left shoulder on the graphic -- that is exactly what you are looking for as Steam launches the game, to verify your Game Version for CK3. Hope this helps, as I just waded through many posts here and it seems some Steam users didn't understand whether they did/didn't have the current version installed. This is how you check your CK3 game version before you actually launch the game with that "Play" button on the launcher screen. You do NOT sign up for Betas to get this, simply have the "None" for Betas in your Steam account's Properties/Settings area (as many have prior suggested). SUGGESTION for Paradox Dev's: INCREASE the Font Size of that Launcher's Game Version statement, Bold Font, make it plainly obvious on that Steam client Launcher pop-up as to the Version of the game that will be launched. Notice how large the Font is just below it for "PDXCON Historian Panel" -- that's the Font size you should use to portray the Version Number of CK3 being launched. @pdxhr @Johan

## Reply 123 — participant_083 · 2023-02-19 · post-28778881

<!-- artifact:quote:start -->
> Nuclear Elvis said: Just in case this was not as obvious for Steam gamers, look at the attached screenshot of my Steam client's CK3 "Launcher" pop-up, and zoom in middle right to see where it says just above the bottom-of-screen icons the version number is "1.8.1 (Robe)" that is listed just at the "king" left shoulder on the graphic -- that is exactly what you are looking for as Steam launches the game, to verify your Game Version for CK3. Hope this helps, as I just waded through many posts here and it seems some Steam users didn't understand whether they did/didn't have the current version installed. This is how you check your CK3 game version before you actually launch the game with that "Play" button on the launcher screen. You do NOT sign up for Betas to get this, simply have the "None" for Betas in your Steam account's Properties/Settings area (as many have prior suggested). SUGGESTION for Paradox Dev's: INCREASE the Font Size of that Launcher's Game Version statement, Bold Font, make it plainly obvious on that Steam client Launcher pop-up as to the Version of the game that will be launched. Notice how large the Font is just below it for "PDXCON Historian Panel" -- that's the Font size you should use to portray the Version Number of CK3 being launched. @pdxhr @Johan Click to expand...
<!-- artifact:quote:end -->
All this time and I never knew where to look...

## Reply 124 — participant_084 · 2023-03-27 · post-28848930

<!-- artifact:quote:start -->
> pdxhr said: Hello everyone! I’m Henrik – nice to e-meet you – I’m a crazy plant person and producer at Paradox Interactive. I'm here to let you know that we have a release coming up for you today: 1.8.0 “ROBE” FREE UPDATE The update should be rolled out to a store near you some time during the day. I promise to keep this short because I understand you’re here for the changelog. As my dear colleague, and ambassador of horchata, Hugo presented last week, we’ve taken some time to put together an update that, apart from a couple of new features, focuses a fair bit on improved stability and bug fixes. We hope you are as excited as we are to continue the endeavours as rulers of lands and kingdoms (hopefully) both beautiful and prosperous. But enough me chit-chatting – to the details: Spoiler: 1.8.0 changelog ################### # Free Features ################### You can now save and load Custom Rulers! Create templates you can easily re-use everywhere on the world map. All the attributes besides the Dynasty and the Coat of Arms are saved. Completely reworked the Bookmark Screen; its now reorganized to allow more room for bookmarks, and they are now sorted by the year they belong to (867 and 1066). This comes with new and improved art for elements and buttons, as well as showing which DLC you have active. Added new and unique illustrations for every Tenet currently in the game! Added 17 new Custom Faith icons for use when creating new faiths, ranging from Ankhs and Boromian Circles to Doves and Chi Rhos! ################### # Hardware ################### Added support for Vulkan renderer OSX and Linux will now by default use the Vulkan renderer - This should increase the framerate significantly for M1 and M2 Mac players Added a setting to change the rendering backend under the graphics category ################### # Game balance ################### Disinheriting is now free for children with a disputed heritage or known bastard. There is however a global opinion penalty which is always applied when taking the interaction Mozarabs can now use a strong hook to force/coerce the pope into binding with rome Updated the consequences for revoking hostile Holy order, it now adds Fervor to their Faith, and potentially a negative county modifier Literalism is legal for all faiths to adopt If the game rule "strict regional heresy" is activated, the Mozarab faith will only appear in Iberia and North Africa Added additional reward to forming the Kingdom of Aragon Rulers will no longer be deposed if they happen to inherit a tyranny war from a lower tier ruler Added gold cost to the "truly special board" in the board game event “A Stroke of Luck” Breaking away from Rome now requires you to be in poor standing with your HoF Properly set low obligations on Custom Rulers who are vassals of the HRE ‘A Beautiful Specimen’ will be only triggered for lovers and soulmates now; not powerful vassals Iberian Conciliation achievement is now classified as "Hard" instead of "Medium" Auto-fire the Court Chaplain if they are excommunicated, except if you are also excommunicated yourself Contracting Assistance is now scaled by army size. ################### # AI ################### Fixed a case where a raiding unit could not find a path to go home in case when the capital was moved. In that case the unit will be disbanded The AI will not try convert children of a vassal with religious protection anymore The AI will marry young men to old women less often: the weight of alliances and the impact of age has been rebalanced The AI will now send fewer requests for chess challenges Blocked the AI from sending two interactions simultaneously, which could cause UI issues AI characters are a lot less likely to accept a war assistance contract against you if they are allied with you ################### # Interface ################### Fixed issue with change/revert buttons in interaction lists only being responsive on a small part of it Fixed so the Army Reorganization scroll area no longer scroll to the top when unit is moved The bookmark lands of Emir Yahya now match the actual in-game shape Holy orders no longer cause "Grant to..." button to disappear in the county capital Offer Guardianship notification and window now use the ‘Offer Guardianship’ title instead of ‘Send Proposal’ Unselectable beneficiaries will now be shown in the list with a tooltip explaining why they cannot be selected Adultery events (adultery.2001 & adultery.2002) now have improved texts for duels You can now always open the list of potential agents, even if none will accept to join the scheme. This can be used to, for example, plan who to seduce or fabricate hooks against to further your interests. Vassal contract modification window now warns when current liege is not the rightful liege Activated Regnal numbers for Count-tier characters to avoid non immersive lineages The "Is imprisoned = no" condition for all court positions is now hidden Court positions no longer display requirements that are the opposite of what they seek Added a section for showing the DLCs that are installed and active. It can be found in the main menu and the bookmark area ################### # Bug fixes ################### Fixed issue where players couldn't accept/decline artifact gifts Fixed issue with event learning_theology_special.1001 were doctrines from the same group wouldn't be removed before applying the new one Fixed German court grandeur tooltip for being above expected level Fixed issue where achievements would still be enabled after creating a custom ruler and not starting the game as them You no longer get "the Thief Slayer" nickname if you already have a positive nickname. Fixed issue where artifact repair cost would show wrong value in the repair window, now shows same value as in the repair button tooltip Fixed issue where ironman would reset when going into select any ruler Fixed issue where overwriting same ruler multiple times would block achievements to be enabled Bestow Royal Favor chancellor task is now canceled if the target vassal declares war on you Fixed an issues that would cause some hedonistic sins to be incorrectly categorized as virtues or vice versa Created missing localization for threatened_by_buildup_opinion Petitioning liege in Russian now uses correct localization macro Struggle messages will now only be shown for interlopers and involved characters Fixed chinese localization doing infinite recursion on localization macro Moved the locators for special buildings in Tenerife to spawn buildings on landmass rather than in the water We now properly communicate in advance that the Subjugation war is only available once per lifetime Notifications for struggle endings are no longer sent to every single player in the lobby, instead selecting those either involved in the struggle or within a certain proximity of the region. fp2_struggle.2021.a.a is no longer blatantly misleading The tooltip of Invite to Activity displays a proper explanation when none of them is available "Desires of the Flesh" now checks what world region you are in before selecting a faith for you to follow Properly handle Duchy and Kingdom Holy Wars within the Struggle Removed duplicated check that were done for characters joining some factions Holy Wars properly deactivated after the Detente ending for the relevant cultures Fixed namespace issues with fp2_Struggle.2024 (now martial_chivalry.4001) Explicitly say that a Faith or Culture needs to control 80% of the counties to get involved within the Iberian Struggle Fixed issue where FP2 3D assets were being overwritten by their generic counterparts. We now display the right cost for the "Invite to Activity interaction"; it used to be swapped Head of Faith titles can no longer be granted to vassals Prevent players from cloning their mercenary armies Fixed localization in invitation to lieges council letter for Spanish Character info is now hidden for the thief in fp2_struggle.2009 Player now receives heresiarch trait when converting to Adoptionism The Found an Empire is now blocked for Involved and Interloper of the Iberian Struggle. The new condition is however only displayed for characters with an involved Faith or Culture, and living nearby Fixed parsing issues with fund_inspiration.2080 Fixed an issue where multiplayer got out of sync when a player hot joined the session Offering Relief events no longer gives you an improved opinion towards yourself. With that fixed, it's still important to remember to love thy self, you're doing good, keep it up! Expanded acceptance criteria for christian bones, christian syncretists can now display christian bones in their court. Finally allowing Basque pagans to equip and enjoy christian bones. Added the word “been” to “I have riding” to result in “I have been riding” in fund_inspiration.6001 ################### # Other ################### Updated name of "Reconquista" cultural innovation to something more historically accurate Added the Sayyid trait to some characters from the Hammudid house who were missing it Added new outcomes to boardgames Fixed line breaks in select Chinese localization keys Aragonese now speak the Oc´Romance language Set Wanda as a daughter of Krak I as it should be in 867 Tabletop Warriors now has a more natural reading description Fixed the dynasty reference for the Chinese Xue Dynasty Clarified the consequences of Dissolution faction Added new localization for creating a new faith that keeps the former pope as the new pope Refresh factions against liege after player character change Fate of Iberia: the Struggle Ending Achievements now have greater clarity as to what ending they refer to Zandaqa can now be rejected when pledging submission to a caliph -HR (Not Human Resources) Click to expand...
<!-- artifact:quote:end -->
Big thanks for the Mac-specific part of the update. Highly appreciated!

