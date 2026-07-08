---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1882481/"
forum_thread_id: 1882481
content_type: reply_thread
parent_dd_file: dd_190_2025-11-28_1-18-2-preview.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 190
title: "Dev Diary #190 - 1.18.2 Preview"
dd_date: 2025-11-28
expansion: All Under Heaven
patch: null
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 6
reply_count: 114
participant_count: 67
reply_date_first: 2025-11-28
reply_date_last: 2025-12-12
body_word_count: 7153
inline_image_count: 0
quoted_span_count: 55
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Dev Diary #190 - 1.18.2 Preview

*114 replies from 67 participants across 6 pages*

## Reply 1 — participant_001 · 2025-11-28 · post-30944225

{ "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" } Greetings everyone, It's @rageair and @egghorse here, back with some updates. We know many of you are eagerly waiting for update 1.18.2, which we originally wanted to release this week. While the update is more-or-less finished and no more content additions are planned, we want to make sure that the release is as smooth as it can be, and we therefore decided to extend the timeline so that we can have a team of QA testers playtest it all next week. We are sure that you’d prefer this rather than if we rushed the update out, as we want to take the time to deliver something we’re genuinely happy with, and to make sure this update lands in the shape it should. Part of our focus has been improving the experience of playing as a Minister, and I will share a few more details about what we have added below. Next to those, the changelog spans more than a dozen pages of bugfixes, which we hope will contribute to a smoother experience of All Under Heaven for all of you. However, the more things you add to a patch, the more important it becomes to make sure all aspects of the game are in good shape and haven’t gotten worse: performance, multiplayer stability, balance, etc. We’re taking the necessary steps to ensure 1.18.2 is truly up to par on all those fronts. Open Beta​Now, for those of you who are eager to check out the new content ahead of time, we’ve set up an open beta branch on Steam. You can access update 1.18.2 ahead of time by opting into the open_beta beta branch on Steam. You can do this by right-clicking on the Crusader Kings III application in Steam, going to "Properties" then to "Betas" - from there, you can select the branch in the "Beta Participation" section. Be aware, we are still waiting for translations so the build is NOT fully localized. All languages except English will have missing strings and placeholders. This Open Beta should be especially interesting to anyone playing on Mac or Linux who currently has very low FPS when zooming in on the map. We’ve also fixed a number of crashes and stability issues. We are not planning to add additional content to the update, but we want to catch and fix bugs before we release it to the entire playerbase. Let us know if you encounter any critical bugs or gameplay blockers. You can report bugs for update 1.18.2 via this link to our Open Beta forum section: https://forum.paradoxplaza.com/forum/forums/open-beta.1198/ Please do not open beta bugs in the regular Bug Report forum section. If you write about issues anywhere other than there, there’s a risk we won’t see it! Ministers​ Below are some of the changes pertaining to Ministers, copied from the 1.18.2 changelog. Gave the Minister of Rites access to a unique Compel Conversion interaction to convert characters in the realm who belong to faiths that deem the Minister's (or the Huangdi's) faith as Hostile or Evil. Improved the Minister of Rites' success chance for the Promote Movement Power scheme, and made them a more challenging target for Slander Movement Power. Added the Compel Religious Uniformity Great Project, which can be started by the Minister of Rites, Grand Chancellor, or the Huángdì. Allowed the Minister of Rites to host Local Examinations. Increased the Army Maintenance discount given to the Grand Marshal. Unlocked the Recruit Terrain Specialist decision for the Grand Marshal and Minister of War; also expressed in Ministerial tooltips that they have access to the Summon Courtiers for the Celestial Bureau Decision Added Great Project for Minister of War to train troops. Gave the Minister of Revenue a discount when hosting Activities and the Grand Marshal a discount on Men-at-Arms Recruitment Cost. Added the Conduct Census Great Project for the Minister of Revenue. Added an interaction to pay off treasury debt of other Characters as Minister of Revenue/Emperor. Allowed the Minister of Works to initiate the Strengthen Capital and Construct Great Barracks Great Projects. Allowed the Son of Heaven and Minster of Works to construct buildings in tributaries in the Advancement Era. Allowed the Minister of Works to always construct buildings in the realm. Added missing effects and localization in the Known Criminal event from the Find Secrets scheme for the Minister of Justice. Added Dynastic Cycle catalysts to blackmailing and exposing secrets for the Minister of Justice and Grand Censor. Added possible outcome to Find Secrets scheme to imprison known criminals Allowed the Minister of Justice to use Find Secrets interaction and scheme. Added Dynastic Cycle catalysts to Find Secrets outcomes. Added current situation item for characters you have an imprisonment reason as the Minister of Justice and treasury cost to imprison them. Apply strife and catalyst penalty to the Minister of Justice only if imprisonment is done without a valid reason. Highlighted the Imprison and Pardon interaction if you are the Minister of Justice. Added current situation item for pardoning anyone in the realm as Minister of Justice. The Minister of Personnel now has automatic acceptance for the use of Demand Courtier and Offer Courtier within the same realm. Added special options for Ministers when using the Influence Career interaction, allowing them to bestow Merit or grant Examination exemptions. Blocked Ministers from having their claims pressed, and claimant wars will now invalidate if the claimant is appointed as a Minister while the conflict is ongoing. Added an extra scheme slot for all scheme types to all Ministers and the Emperor of China. Allow founders of Great Projects to ask other Characters to contribute Updated Adopt Feudal Ways decision for all new administrative governments, unless you are the Son of Heaven, to be able to use it. Added a secret for cheating during an examination, and a unique expose event. All ministers gain the ability to dip into their Treasury occasionally, via the Withdraw Funds from Treasury decision, gaining gold at a cost. This new decision is also available for independent administrative rulers (see below). ​ [Screenshot of the “Influence Career” interaction.] Ministers have new and unique options when trying to influence someone’s career. In a representation of historical privileges typically offered to high-ranking officials, once per lifetime you can grant a complete exemption - a free pass - on all examinations to a member of your family. You still have the ability to do so more than once, but abusing this privilege is corruption and will impact the Dynastic Cycle! [Screenshot of the “Conduct Census” Great Project.] The “Conduct Census” Great Project is now available to the Minister of Revenue. Every county that has had a census performed in it will gain the “Census Compliant” modifier: ​ [Screenshot of the "Census Compliant" modifier.] [Screenshot of the “Military Operation Exercise” Great Project.] The Minister of War now has the ability to train troops through a new Great Project, “Military Operation Exercise.” [Screenshot of the “Compel Religious Uniformity” Great Project.] A new Great Project to Compel Religious Uniformity, similar to Sinicize Area, is now available for the Minister of Rites, which will convert entire duchies to the Huángdì’s faith. It can also be started by the Grand Chancellor and the Huángdì. Other Content​Mines​As part of the update we have also gone over the mines of East Asia a second time, adding a number of new metal mines to China that were previously not there. Like the ones in the version before it these are for areas that were important for the regional economy and will add a bit more of interesting diversity to the region. Gold: Jiadong Gold mine, Zijinshan Gold mine Silver: Baofeing Silver Mine, Kaibo, Silver Mines, Liangzhe Silver Mine, Guiyang Silver Mine Salt: Ziliujing & Gongjing Salt Wells Iron: Hanxing Iron Mine, Chihu Iron mine Battle Points of Interest​We have added a number of new points of interest for historical battles in the East Asian region. These will provide a bit of martial lifestyle experience and give us an opportunity to tell a bit more of the regions history while also giving you new reasons to take a detour as you travel from one point of the map to another. The Battle of Sufuku (Japan) The Battle of Baekgang (Goryeo) The Battle of Palembang (Suvarnadvipa) The Battle of Angkor (Kambuja) The Battle of Songping (China) The Battle of Muye (China) The Battle of Guandu (China) The Battle of Red Cliffs (China) The Battle of Yiling (China) The Battle of Fei River (China) The Battle of Canhe Slope (China) The Battle of Xiangji Temple (China) The Battle of Gaoliang River (China) [Screenshot of “The Withering of Righteousness” event.] Those who select the Autumn of Virtue bookmark character Huang Chao in the 867 start date will now receive a new starting event, giving you the option to pursue his historical solution to the problem of having repeatedly failed the imperial examinations - setting out to overthrow the Tang dynasty himself. In the interests of player agency, you may choose one of four distinct options; attempting to seize control of the realm from within, embarking on the path of a Conqueror, venturing forth as an Adventurer (if Roads to Power is also present), or declaring yourself to be the Maitreya savior. [Screenshot of a decision to withdraw gold from your treasury as a Minister, costing Influence] Often in history the rulers of administrative realms like China or Byzantium had quite a bit of personal opportunity to dip into government funds without it being an outright illegal action. They are the Huangdi/Emperor after all! So we added a decision to convert an amount of treasury into personal gold, with some costs and cooldowns. An independent ruler can take this decision, costing an amount of Legitimacy, and gaining a legitimacy-gain decreasing modifier “Dipped into Treasury”. In the case of the Huangdi, it will also be a catalyst for the Dynastic Cycle. We also enabled this decision for ministers in China, since they hold a lot of power in the system - for them it costs Influence, and they will gain a similar modifier that will decrease their prestige and influence gain for a duration, plus it will also be a catalyst of course. Being technically legal doesn’t necessarily make it proper! That’s all for now! When we’re closer to release (likely the week after next) we will share the full 1.18.2 changelog. Until then we thank you for your patience and your help in making 1.18.2 worth the wait. If you encounter any bugs, remember to head over to the bug forum. Happy playing!

## Reply 2 — participant_002 · 2025-11-28 · post-30944328

so it come at the last possible day of november well done

## Reply 3 — participant_003 · 2025-11-28 · post-30944337

I will always be in favor of a delay for the sake of polish, good call!

## Reply 4 — participant_004 · 2025-11-28 · post-30944339

<!-- artifact:quote:start -->
> aadf97799c said: so it come at the last possible day of november well done Click to expand...
<!-- artifact:quote:end -->
At least it came. I swear sometimes y'all remind me of cats. Breakfast is at 7 AM, and woe betide the Human who serves Breakfast at 7:01 AM...

## Reply 5 — participant_005 · 2025-11-28 · post-30944342

Please address the Linux vulkan performance issues

## Reply 6 — participant_002 · 2025-11-28 · post-30944345

really hope great project are more available outside of hegemony especially the culture and faith conversion one and great barrack maybe some tradition could unlock them at empire tier also everyone should be able to build and upgrade great wall many minor power did build and maintain them throughout history census look like upgraded version of inspection census target duchy could be available to everyone limit the kingdom census to administrative empire or hegemony

## Reply 7 — participant_006 · 2025-11-28 · post-30944354

I would much rather this patch was released now and a hotfix deployed for any issues next week. QA will not find most issues that the players will.

## Reply 8 — participant_004 · 2025-11-28 · post-30944361

<!-- artifact:quote:start -->
> AbledCat said: I would much rather this patch was released now and a hotfix deployed for any issues next week. QA will not find most issues that the players will. Click to expand...
<!-- artifact:quote:end -->
Sadly, if the devs did that, they would never hear the end of it, what with the inevitable post-release bugs. Let's face it, players aren't exactly the most forgiving of people when it comes to bugs, and the Devs are-quite rightly IMO-making sure Ts are crossed, and I's properly dotted before release...

## Reply 9 — participant_007 · 2025-11-28 · post-30944363

very nice changes

## Reply 10 — participant_008 · 2025-11-28 · post-30944394

What will be the default choice when Huang Chao is managed as the AI? When playing as the Tang Emperor or as a military commander can we expect a sizable rebellion/war?

## Reply 11 — participant_009 · 2025-11-28 · post-30944422

<!-- artifact:quote:start -->
> AbledCat said: I would much rather this patch was released now and a hotfix deployed for any issues next week. QA will not find most issues that the players will. Click to expand...
<!-- artifact:quote:end -->
That would cause a larger avalanche of complaints. They are letting you to use the open beta if you are willing to play a buggy version.

## Reply 12 — participant_006 · 2025-11-28 · post-30944426

Also Huang Chao as a conqueror is just a complete joke, player agency is not a good excuse. If you want to give player agency like that then might as well let custom characters start out with the conqueror trait.

## Reply 13 — participant_010 · 2025-11-28 · post-30944437

<!-- artifact:quote:start -->
> AbledCat said: Also Huang Chao as a conqueror is just a complete joke, Click to expand...
<!-- artifact:quote:end -->
Glad to see the Huang Chao changes - he really should be the Haesteinn of the East and this gives some good options for him. Hopefully it gives some narrative direction to 867 China even when you're not playing as him too. I hope the extra options for ministers make their gameplay feel a little fuller. Any chance that regular Meritocratic empires could get king-tier ministers? Edit: Welp, opinions can vary!

## Reply 14 — participant_009 · 2025-11-28 · post-30944441

<!-- artifact:quote:start -->
> Videogames said: Glad to see the Huang Chao changes - he really should be the Haesteinn of the East and this gives some good options for him. Hopefully it gives some narrative direction to 867 China even when you're not playing as him too. I hope the extra options for ministers make their gameplay feel a little fuller. Any chance that regular Meritocratic empires could get king-tier ministers? Edit: Welp, opinions can vary! Click to expand...
<!-- artifact:quote:end -->
I'm personally fine with Huang Chao changes, it is just making him a conqueror right at the start that is silly. Haesteinn (deservedly) doesn't have that trait after all.

## Reply 15 — participant_011 · 2025-11-28 · post-30944630

Starting as a conqueror is crazy

## Reply 16 — participant_012 · 2025-11-28 · post-30944680

That's it? Being able to do great projects, which is one click to spend money and wait, and being able to build buildings, is the whole new minister gameplay?

## Reply 17 — participant_013 · 2025-11-28 · post-30944742

I would like to take the opportunity provided by this preview to suggest some changes to character interactions, particularly when the player has a government type that utilizes Influence. Specifically: Offer Vassalization: Offering vassalization to a non-administrative character allows the player to offer Influence to improve the target's acceptance. It goes without saying that this option is useless, as the target does NOT use Influence; therefore, it makes little sense to pay them with a currency they CANNOT USE. So I suggest this option to increment success, shouldn't be available if the target do not have a goverment with influence. I also suggest adding a negative acceptance modifier if the actor has an Administrative government and the recipient does not. Demand Administrative Government: This interaction should also be revised by increasing Gold and Influence costs. It should be significantly harder for a non-administrative ruler to renounce the privileges of their current government in favor of a new form where they risk losing their land, given the lack of hereditary succession in Administrative governments. Again, I suggest adding a negative acceptance modifier if the actor has an Administrative government and the recipient does not. I also suggest slightly nerfing the Frontier and Naval contracts (themes) for the Administrative government, . Furthermore, I still notice a tendency to blob, so I recommend revisiting the Casus Belli costs for Administrative vassals, as they are responsible for the majority of conquests. Finally, I want to point out the AI's inability to manage its treasury under the Administrative government; it often ends up hundreds, if not thousands, of gold in debt. I suggest fixing this issue/bug.

## Reply 18 — participant_014 · 2025-11-28 · post-30944797

<!-- artifact:quote:start -->
> aadf97799c said: really hope great project are more available outside of hegemony especially the culture and faith conversion one and great barrack maybe some tradition could unlock them at empire tier also everyone should be able to build and upgrade great wall many minor power did build and maintain them throughout history census look like upgraded version of inspection census target duchy could be available to everyone limit the kingdom census to administrative empire or hegemony Click to expand...
<!-- artifact:quote:end -->
all Great Church/ Holy sites can be built by great projects

## Reply 19 — participant_015 · 2025-11-28 · post-30944890

No changelog preview?..

## Reply 20 — participant_015 · 2025-11-28 · post-30944892

<!-- artifact:quote:start -->
> TempestM said: That's it? Being able to do great projects, which is one click to spend money and wait, and being able to build buildings, is the whole new minister gameplay? Click to expand...
<!-- artifact:quote:end -->
not that different from regular independent ruler gameplay tbh.

## Reply 21 — participant_002 · 2025-11-28 · post-30944913

almost forgot but please allow liege to replace building in vassal domain maybe lock that ability after higher authority law or something but watch vassal stuck with deactivated brewery forever are very annoying

## Reply 22 — participant_016 · 2025-11-28 · post-30944933

Paradox, we need separate teams that work on improving and enhancing existing DLCs. Older DLCs need to constantly be updated and incorporated into the rest of the game. For instance when you host a tournament we still see the same generic buildings. Every culture or at least region should have unique games, and unique buildings when hosting their own tournament. Furthermore what about Military commanders? When will we see a more interactive military commander system? I would love for us to be able to carry out situations like the An Lushan Rebellion.

## Reply 23 — participant_017 · 2025-11-28 · post-30945115

<!-- artifact:quote:start -->
> Benismann said: not that different from regular independent ruler gameplay tbh. Click to expand...
<!-- artifact:quote:end -->
Regulae independent ruler gameplay is about being a feudal ruler. As a minister you don't own land but you own powers attached to the offices which should allow you to manage and interact with governors of the empire differently.

## Reply 24 — participant_002 · 2025-11-28 · post-30945141

<!-- artifact:quote:start -->
> Altro-Habibi said: Paraox, we need separate teams that work on improving and enhancing existing DLCs. Older DLCs need to constantly be updated and incorporated into the rest of the game. For instance when you host a tournament we still see the same generic buildings. Every culture or at least region should have unique games, and unique buildings when hosting their own tournament. Furthermore what about Military commanders? When will we see a more interactive military commander system? I would love for us to be able to carry out situations like the An Lushan Rebellion. Click to expand...
<!-- artifact:quote:end -->
so many weak and outdated tenet and tradition some update for them would be nice also adding 5 economy 5 military 5 duchy building to the game shouldn't be that hard all the domicile type get so many building

## Reply 25 — participant_002 · 2025-11-28 · post-30945162

also really hope a trait decision or tradition unlock the outcast maa it is wasteful only adventurer get to use them

## Reply 26 — participant_018 · 2025-11-28 · post-30945196

That Compel Religious Uniformity great project should cause a moderate dip in popular opinion in the counties it effects. Not a punishing amount mind you, just enough to pose a challenge to the player. This will be good gameplay for two reasons: 1. To add challenge for the player. 2. Add to historical realism. In history, whenever the state tried to impose religious uniformity there was a pushback of popular resistance.

## Reply 27 — participant_002 · 2025-11-28 · post-30945221

<!-- artifact:quote:start -->
> hytth said: That Compel Religious Uniformity great project should cause a moderate dip in popular opinion in the counties it effects. Not a punishing amount mind you, just enough to pose a challenge to the player. This will be good gameplay for two reasons: 1. To add challenge for the player. 2. Add to historical realism. In history, whenever the state tried to impose religious uniformity there was a pushback of popular resistance. Click to expand...
<!-- artifact:quote:end -->
it should lower everything while in progress and get some other reward when it is down

## Reply 28 — participant_019 · 2025-11-28 · post-30945375

I propose a new punishment for crimes: confiscate the wealth of a prisoner and give it to the treasury. Especially since stealing from the treasury is a crime, the punishment would fit the deed.

## Reply 29 — participant_002 · 2025-11-28 · post-30945413

<!-- artifact:quote:start -->
> Silens said: I propose a new punishment for crimes: confiscate the wealth of a prisoner and give it to the treasury. Especially since stealing from the treasury is a crime, the punishment would fit the deed. Click to expand...
<!-- artifact:quote:end -->
confiscate and exile of entire household does happen sometimes emperor should be allowed to do it not only take the gold of the character but liquidate the domicile

## Reply 30 — participant_020 · 2025-11-28 · post-30945476

Let me repeat a number of things I'd like to see. 1. The Kong family (dynasty of Confucius) exist in game but they’re playable only in 1066. They were a unique family. The only family in China, other than imperial dynasties, to have a hereditary title for generations. Title of Duke Yansheng was held by them until 20th century. My suggestions for better representation of the Kong family: Make them playable on all starting dates. Give them a unique trait (sayyid-like) with additional prestige and opinion with Confucian faiths and characters with Confucian education. Give them a unique duchy-tier Family title (like noble families in admin gov). 2. In 867, the Japanese imperial family already had a unique status. Only Yamato dynasty members were able to sit on The Chrysanthemum Throne. That’s why the heir of the female Tenno was always a child whose father belonged to the Yamato dynasty. But in game it could be inherited by anyone throw marriage. My suggestions for better representation of the Yamato dynasty: Give them a unique trait (sayyid-like) with additional prestige and opinion with Shinto faiths and Japonic heritage. Link inheritance of The Chrysanthemum Throne with this trait. I think it’s pretty easy since we had same priority of the Born in the Purple for Byzantium. 3. Designated heirs in Celestial, Meritocratic, Ritsuryo. Currently rulers able to designate heir only from among children. If ruler haven’t any, the heir will be automatically installed by game based on succession law. But historically there was an opportunity to choose between claimants (Uncles, Brothers, Cousins, Nephews etc.). My suggestions for better representation of this: Give Celestial, Meritocratic, Ritsuryo rulers opportunity to designate heir from all relevant house members. Hope bugs with ceremonial monarchs will be fixed too. 4. Creation of the Siam kingdom must give buffs for promoting of Tai culture. The Sukhothai has 4 counties and 3 of it has Mon culture. 5. Give oppoortunity to canccel great project I can't participate in. I conquered some lands from mandala characters as merocratic ruler. Their temple complex projects just exist as mine. But I can't participate in it as well as cancel. It's a little annoying I also hope we will see historical legends and spawn of historical characters in Eastern Asia in future.

## Reply 31 — participant_021 · 2025-11-28 · post-30945735

Ministers are boring to play partly due to they can't host activities like hunts and funerals, which is totally an unnecessary restriction. Ministers should be treated as landed characters and can host any activity in locations within the top realm.

## Reply 32 — participant_022 · 2025-11-29 · post-30945832

<!-- artifact:quote:start -->
> vandevere said: Sadly, if the devs did that, they would never hear the end of it, what with the inevitable post-release bugs. Let's face it, players aren't exactly the most forgiving of people when it comes to bugs, and the Devs are-quite rightly IMO-making sure Ts are crossed, and I's properly dotted before release... Click to expand...
<!-- artifact:quote:end -->
As long as they don't dot the T's and cross the I's, I'm content to wait.

## Reply 33 — participant_023 · 2025-11-29 · post-30945838

<!-- artifact:quote:start -->
> awo.o said: Let me repeat a number of things I'd like to see. 1. The Kong family (dynasty of Confucius) exist in game but they’re playable only in 1066. They were a unique family. The only family in China, other than imperial dynasties, to have a hereditary title for generations. Title of Duke Yansheng was held by them until 20th century. My suggestions for better representation of the Kong family: Make them playable on all starting dates. Give them a unique trait (sayyid-like) with additional prestige and opinion with Confucian faiths and characters with Confucian education. Give them a unique duchy-tier Family title (like noble families in admin gov). 2. In 867, the Japanese imperial family already had a unique status. Only Yamato dynasty members were able to sit on The Chrysanthemum Throne. That’s why the heir of the female Tenno was always a child whose father belonged to the Yamato dynasty. But in game it could be inherited by anyone throw marriage. My suggestions for better representation of the Yamato dynasty: Give them a unique trait (sayyid-like) with additional prestige and opinion with Shinto faiths and Japonic heritage. Link inheritance of The Chrysanthemum Throne with this trait. I think it’s pretty easy since we had same priority of the Born in the Purple for Byzantium. 3. Designated heirs in Celestial, Meritocratic, Ritsuryo. Currently rulers able to designate heir only from among children. If ruler haven’t any, the heir will be automatically installed by game based on succession law. But historically there was an opportunity to choose between claimants (Uncles, Brothers, Cousins, Nephews etc.). My suggestions for better representation of this: Give Celestial, Meritocratic, Ritsuryo rulers opportunity to designate heir from all relevant house members. Hope bugs with ceremonial monarchs will be fixed too. 4. Creation of the Siam kingdom must give buffs for promoting of Tai culture. The Sukhothai has 4 counties and 3 of it has Mon culture. 5. Give oppoortunity to canccel great project I can't participate in. I conquered some lands from mandala characters as merocratic ruler. Their temple complex projects just exist as mine. But I can't participate in it as well as cancel. It's a little annoying I also hope we will see historical legends and spawn of historical characters in Eastern Asia in future. Click to expand...
<!-- artifact:quote:end -->
1) It is likely that you can play for this family since 1066, because the title of Duke Yangsheng was created around 1055, and the first family estate was built in 1038. Everything is logical and historical. But the suggestion to create an inheritable property is excellent.

## Reply 34 — participant_024 · 2025-11-29 · post-30945940

Overall, this could be a good patch, although I haven't played a full game, only skimmed through it and therefore haven't checked every detail. On the positive side, the RU UI issues I've been reporting on for about two years, especially since AuH, have finally been addressed (assuming these fixes make it to release). At least visually, the interface is playable for characters playable from the launch dates and doesn't look broken. Of course, everything will be tested more thoroughly, and underlying issues will likely be uncovered, but so far the result is commendable. Although there's a small issue that I noticed fairly quickly: the character interaction button sometimes extends beyond the edges. This can be a problem if the character has many titles or court positions. Although it's not as critical as before. So I'm looking forward to the full patch release, thanks for the "very long awaited" fixes (and by long... I mean a loooong...).

## Reply 35 — participant_025 · 2025-11-29 · post-30945951

Instead of forcing conversion to a faith, it was more common to persecute faiths. Celestial Empire should have that religious black list to ban certain people from taking part in imperial exam, and fire those with an unwelcomed faith.

## Reply 36 — participant_026 · 2025-11-29 · post-30946003

Interesting changes. I beg you give meritocratic an outside war declaration law and it would be wonderful.

## Reply 37 — participant_027 · 2025-11-29 · post-30946014

<!-- artifact:quote:start -->
> Artorius_ said: Please address the Linux vulkan performance issues Click to expand...
<!-- artifact:quote:end -->
Seems like it's resolved! I'm able to zoom in and look around the map without issues, at higher settings. That was my number one concern; the game is now playable with the beautiful new 1.18 map!

## Reply 38 — participant_028 · 2025-11-29 · post-30946066

The Han conversion to Confucianism privilege should take into account the faith of the empire and family head faith into account instead of it not having any checks right now. At the very least it should check if characters are zealous.

## Reply 39 — participant_025 · 2025-11-29 · post-30946128

Any way to impeach minister?

## Reply 40 — participant_029 · 2025-11-29 · post-30946134

Could you please add options for map brightness so we can use the 1.17 map colors and look if we want to (without playing 1.17)? Or at least tell us why we can't have those options (or how to mod them ourselves)? There are so many threads on this and I've yet to see any even acknowledgment of this issue. Maybe I missed it.

## Reply 41 — participant_025 · 2025-11-29 · post-30946147

Since bureacratic gameplay feels still lacking, why not add filial mourning? Being filial can bring merit, anyway.

## Reply 42 — participant_030 · 2025-11-29 · post-30946236

Could you guys also do something about the later 3 kingdoms period of Korea?

## Reply 43 — participant_031 · 2025-11-29 · post-30946283

Two cents from me: 1. it's nice for ministers to be able to Bestow Merit & Grant Examination Exemption in the Influence Career decision. That, however, begs question about the Influence Cost of said decisions. I switched to the starting Chancellor of Tang in 868, and I had to pay 300 Influence to Grant Examination Exemption, 400 to Bestow Merit, yet 500 to Influence Candidate score. It feels like the Influence Candidate Score should probably be cheaper than these, given that it is much less impactful? (Unless that is meant to be "who of the Rank 1 people will become the next Chancellor?") 2. do the inability to push the titles for the ministers pertains also to the claims on Hegemony? If so, I'd rather your immediate family wouldn't stop being a claimant threat - to the meager extent they are now - if you make them into Ministers.

## Reply 44 — participant_032 · 2025-11-29 · post-30946331

''no more content additions are planned'' I suppose that is conformation that the original Chinese throne room will sadly not be implemented

## Reply 45 — participant_031 · 2025-11-29 · post-30946352

<!-- artifact:quote:start -->
> Mayoli44 said: ''no more content additions are planned'' I suppose that is conformation that the original Chinese throne room will sadly not be implemented Click to expand...
<!-- artifact:quote:end -->
I mean, I believe "the update is more-or-less finished and no more content additions are planned" pertains strictly to the 1.8.2 update, and not general state of AuH.

## Reply 46 — participant_002 · 2025-11-29 · post-30946399

really hoped for a lot more special building be added to liao territory and southeast asia

## Reply 47 — participant_033 · 2025-11-29 · post-30946427

New events and buttons to click are of course good. But when will the gameplay loop of china, japan and nomads will be addressed? It still feels like early alpha

## Reply 48 — participant_012 · 2025-11-29 · post-30946480

<!-- artifact:quote:start -->
> CrazyRat said: I mean, I believe "the update is more-or-less finished and no more content additions are planned" pertains strictly to the 1.8.2 update, and not general state of AuH. Click to expand...
<!-- artifact:quote:end -->
Nah they said something like "in perfect world no 1.8.3 would be needed and we want 1.8.2 to be it" and they will move on to next dlc entirely, so it's most likely all for AUH except some hotfixes

## Reply 49 — participant_034 · 2025-11-29 · post-30946615

Yes, that's good. Bug fixes are always great. I also appreciate the attempt to create historical depth. Thanks and respect for your efforts, everyone.

## Reply 50 — participant_035 · 2025-11-29 · post-30946715

Does anyone know what The Battle of Sufuku (Japan) is? Sufuku?

## Reply 51 — participant_036 · 2025-11-29 · post-30946751

Anything not related to China in the patch? Like AI Byzantines always bankrupt after 1 civil war?

## Reply 52 — participant_002 · 2025-11-29 · post-30946847

<!-- artifact:quote:start -->
> Jose_ck3 said: Anything not related to China in the patch? Like AI Byzantines always bankrupt after 1 civil war? Click to expand...
<!-- artifact:quote:end -->
that seem to be all administrative problem so hope that will be fixed too

## Reply 53 — participant_037 · 2025-11-29 · post-30946873

Is it possible to start an ironman save from 1.18.1 on this open beta 1.18.2 patch and it still be achievements-compatible? Also, will it be later possible to run such „migrated” save back on non-beta 1.18.3?

## Reply 54 — participant_038 · 2025-11-29 · post-30946928

Also the issue of title MAA army in Celesital governments needs to be reworked. Every type of governor should have a title army to protect themselves, not rely on the army of military governors hundreds of kilometers away, or rely on the governor's own personal MAA, that's unhistorical. My feeling is that the publishers don't play the game so they give everything arbitrarily like that.

## Reply 55 — participant_010 · 2025-11-29 · post-30947092

<!-- artifact:quote:start -->
> hasegawatiki said: Does anyone know what The Battle of Sufuku (Japan) is? Sufuku? Click to expand...
<!-- artifact:quote:end -->
It's certainly not googleable. I do see there's a ruined temple Sufuki-ji on the western side of Lake Biwa. That makes me think of the Jinshin War and Fujiwara no Nakamaro's rebellions, which both played out their military confrontations around there. The site's not an exact match for either though.

## Reply 56 — participant_002 · 2025-11-29 · post-30947099

<!-- artifact:quote:start -->
> Giang Trung said: Also the issue of title MAA army in Celesital governments needs to be reworked. Every type of governor should have a title army to protect themselves, not rely on the army of military governors hundreds of kilometers away, or rely on the governor's own personal MAA, that's unhistorical. My feeling is that the publishers don't play the game so they give everything arbitrarily like that. Click to expand...
<!-- artifact:quote:end -->
there should be more law for all administrative realm to decide how much maa governor get but song dynasty at the 1066 start are famous for separate local military and administration the army of million they employee are more levy than professional army

## Reply 57 — participant_039 · 2025-11-29 · post-30947161

<!-- artifact:quote:start -->
> egghorse said: Added an extra scheme slot for all scheme types to all Ministers and the Emperor of China. Click to expand...
<!-- artifact:quote:end -->
If we unlock "Twice Schemed" from Schemer lifestyle, will there be 3 scheme slot or 2?

## Reply 58 — participant_010 · 2025-11-29 · post-30947176

<!-- artifact:quote:start -->
> srihman said: If we unlock "Twice Schemed" from Schemer lifestyle, will there be 3 scheme slot or 2? Click to expand...
<!-- artifact:quote:end -->
Yes, that happens already when you stack extra scheme slots. And it makes the gameplay a terrible slog if you want to actually maximize those slots. You can generate insane amounts of influence, for example, by constantly running Challenge Status schemes, but you have to dump so much time into finding a new target and clicking through it every approximately 50 days, and you have to maintain it for all scheme slots.

## Reply 59 — participant_040 · 2025-11-29 · post-30947487

Any chance we could get more great works? It's one of the few things I was looking forward to in the DLC and they feel very barebones.

## Reply 60 — participant_002 · 2025-11-29 · post-30947575

<!-- artifact:quote:start -->
> DaBombXXX said: Any chance we could get more great works? It's one of the few things I was looking forward to in the DLC and they feel very barebones. Click to expand...
<!-- artifact:quote:end -->
would be nice if all the university and great temple use great work system and most of the upgradable special building maybe even allow player to build some of those gigantic budda statue

## Reply 61 — participant_041 · 2025-11-29 · post-30947643

Will there be anything done about the high merit character spawned in that bloats china's appointment lader in the game 60 or so years after start?

## Reply 62 — participant_042 · 2025-11-29 · post-30947861

What about sorting by merit/influence while granting titles? The cycle always enters tension cuz I hand out titles to characters with too low merit, but I can't find the highest merit ones?

## Reply 63 — participant_031 · 2025-11-29 · post-30948017

<!-- artifact:quote:start -->
> Videogames said: Yes, that happens already when you stack extra scheme slots. And it makes the gameplay a terrible slog if you want to actually maximize those slots. You can generate insane amounts of influence, for example, by constantly running Challenge Status schemes, but you have to dump so much time into finding a new target and clicking through it every approximately 50 days, and you have to maintain it for all scheme slots. Click to expand...
<!-- artifact:quote:end -->
On the other hands, I believe Murder schemes against Ministers and holder of Hegemony tick so slowly that it may barely allow you to assassinate them at your usual rate xP

## Reply 64 — participant_043 · 2025-11-30 · post-30948795

<!-- artifact:quote:start -->
> aadf97799c said: confiscate and exile of entire household does happen sometimes emperor should be allowed to do it not only take the gold of the character but liquidate the domicile Click to expand...
<!-- artifact:quote:end -->
Proscription as a punishment is a sorely needed feature for Admin governments, and probably Republics as well once those come out.

## Reply 65 — participant_002 · 2025-11-30 · post-30948806

<!-- artifact:quote:start -->
> Commander Flazgar said: Proscription as a punishment is a sorely needed feature for Admin governments, and probably Republics as well once those come out. Click to expand...
<!-- artifact:quote:end -->
administrative legacy already give the ability to mass arrest entire house so it is not like the function doesn't exist just make it available for emperor

## Reply 66 — participant_023 · 2025-11-30 · post-30949189

<!-- artifact:quote:start -->
> Gamshud said: Overall, this could be a good patch, although I haven't played a full game, only skimmed through it and therefore haven't checked every detail. On the positive side, the RU UI issues I've been reporting on for about two years, especially since AuH, have finally been addressed (assuming these fixes make it to release). At least visually, the interface is playable for characters playable from the launch dates and doesn't look broken. Of course, everything will be tested more thoroughly, and underlying issues will likely be uncovered, but so far the result is commendable. Although there's a small issue that I noticed fairly quickly: the character interaction button sometimes extends beyond the edges. This can be a problem if the character has many titles or court positions. Although it's not as critical as before. So I'm looking forward to the full patch release, thanks for the "very long awaited" fixes (and by long... I mean a loooong...). Click to expand...
<!-- artifact:quote:end -->
But the search for titles in Cyrillic (the key V) apparently won't be fixed(

## Reply 67 — participant_023 · 2025-11-30 · post-30949207

It's a historical fact that Japanese emperors never left the country until Emperor Meiji broke with tradition. This presents a game design dilemma: while limiting the emperor's travel would restrict player interactions, the notion of a ceremonial emperor attending parties in Chinese or Korean courts is historically comical) Yet, completely preventing the Japanese Emperor from traveling the world also feels like an unnecessary limitation.

## Reply 68 — participant_002 · 2025-11-30 · post-30949233

<!-- artifact:quote:start -->
> Extinrebok said: It's a historical fact that Japanese emperors never left the country until Emperor Meiji broke with tradition. This presents a game design dilemma: while limiting the emperor's travel would restrict player interactions, the notion of a ceremonial emperor attending parties in Chinese or Korean courts is historically comical) Yet, completely preventing the Japanese Emperor from traveling the world also feels like an unnecessary limitation. Click to expand...
<!-- artifact:quote:end -->
the next step of travel system is obvious send envoy for stuff like tribute to tang or visit silk road market this could be expend further into invest and send out merchant caravan

## Reply 69 — participant_044 · 2025-11-30 · post-30949642

What I also want for change is allow the Son of Heaven to build all the buildings of the Estate. Because right now I am blocked from getting certain buildings once I became the Emperor as there is no real way like in Administrative to get my one son becomming the SoH while my other son inherit the Dynasty head so especially if I start in a soon to be Division Era start, there is now no way to get a Minister Post and so the building or as SoH to change my political career which I need for certain buildings.

## Reply 70 — participant_045 · 2025-11-30 · post-30950119

<!-- artifact:quote:start -->
> hasegawatiki said: Does anyone know what The Battle of Sufuku (Japan) is? Sufuku? Click to expand...
<!-- artifact:quote:end -->
Looks like its been renamed to Subushi. I believe it's supposed to be this battle, which only has a Japanese wiki article. https://ja.wikipedia.org/wiki/巣伏の戦い Interesting, this would mean that the only 2 battles on the map involving Japan (Subushi and Baekgang) are both about Japanese defeats.

## Reply 71 — participant_024 · 2025-12-01 · post-30950589

<!-- artifact:quote:start -->
> Extinrebok said: But the search for titles in Cyrillic (the key V) apparently won't be fixed( Click to expand...
<!-- artifact:quote:end -->
I've never used the title search, but I went into the game to check, and it really doesn't recognize Cyrillic. It looks really strange, to be honest, I can't even imagine why it doesn't work.

## Reply 72 — participant_046 · 2025-12-01 · post-30950801

<!-- artifact:quote:start -->
> AbledCat said: I would much rather this patch was released now and a hotfix deployed for any issues next week. QA will not find most issues that the players will. Click to expand...
<!-- artifact:quote:end -->
When Paradox releases an unpolished build, players complain about them not spending more time on QA. When Paradox delays a release for QA, players complain about them not releasing it faster. Maybe the devs should just ignore us.

## Reply 73 — participant_004 · 2025-12-01 · post-30950840

<!-- artifact:quote:start -->
> GreatWyrmGold said: When Paradox releases an unpolished build, players complain about them not spending more time on QA. When Paradox delays a release for QA, players complain about them not releasing it faster. Maybe the devs should just ignore us. Click to expand...
<!-- artifact:quote:end -->
"When it’s hot, he wants it cool; When it’s cool, he wants it hot. Always wanting, what is not.” Quote attributed to Benjamin Disraeli, believe it or not. But this one feels very apt, considering the circumstances...

## Reply 74 — participant_047 · 2025-12-01 · post-30950967

Still appears to be no way to see the current budget as a celestial vassal (even as the Minister of Revenue), is that anywhere on the roadmap?

## Reply 75 — participant_002 · 2025-12-01 · post-30951324

<!-- artifact:quote:start -->
> GreatWyrmGold said: When Paradox releases an unpolished build, players complain about them not spending more time on QA. When Paradox delays a release for QA, players complain about them not releasing it faster. Maybe the devs should just ignore us. Click to expand...
<!-- artifact:quote:end -->
that is what most dev do listen to loudest player too much make the worst game even decent modder make terrible dlc after they become developer it is especially hard for dev as sluggish as paradox to make any improvement for their game

## Reply 76 — participant_012 · 2025-12-01 · post-30951691

<!-- artifact:quote:start -->
> GreatWyrmGold said: When Paradox releases an unpolished build, players complain about them not spending more time on QA. When Paradox delays a release for QA, players complain about them not releasing it faster. Maybe the devs should just ignore us. Click to expand...
<!-- artifact:quote:end -->
Ah yes, the single hivemind entity known as "The Players" , where one posting means one united opinion

## Reply 77 — participant_048 · 2025-12-01 · post-30951721

Thanks for the update.

## Reply 78 — participant_049 · 2025-12-01 · post-30952623

Oooh and here I was thinking : A 2026 PREVIEW! YAY! Always nice to see a dev diary but this one (unjustly) disappointed me...

## Reply 79 — participant_050 · 2025-12-02 · post-30953769

<!-- artifact:quote:start -->
> Mayoli44 said: ''no more content additions are planned'' I suppose that is conformation that the original Chinese throne room will sadly not be implemented Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> CrazyRat said: I mean, I believe "the update is more-or-less finished and no more content additions are planned" pertains strictly to the 1.8.2 update, and not general state of AuH. Click to expand...
<!-- artifact:quote:end -->
Made an account just to say I strongly believe that it will be added given it's reception, just not in this patch. From the artwork we've seen it looks as good as finished, would be a waste not to use the assets. Agreed

## Reply 80 — participant_051 · 2025-12-02 · post-30953914

<!-- artifact:quote:start -->
> Spectre0170 said: Will there be anything done about the high merit character spawned in that bloats china's appointment lader in the game 60 or so years after start? Click to expand...
<!-- artifact:quote:end -->
I don't get why this is not gets adressed enough, playing as a vassal in China is impossible after your first succession, you can't even get a county appointment bacause of endless stream of lvl 2-3 merit randoms without a family

## Reply 81 — participant_002 · 2025-12-02 · post-30953935

<!-- artifact:quote:start -->
> Betheven said: I don't get why this is not gets adressed enough, playing as a vassal in China is impossible after your first succession, you can't even get a county appointment bacause of endless stream of lvl 2-3 merit randoms without a family Click to expand...
<!-- artifact:quote:end -->
keju system will always need to balance between high born privilege and low born talent maybe the stratified society tradition work better for the first part

## Reply 82 — participant_052 · 2025-12-02 · post-30954923

Does this patch turn the Qara Khitai into meritocratic nomad in the last start date?

## Reply 83 — participant_053 · 2025-12-02 · post-30956254

<!-- artifact:quote:start -->
> Betheven said: I don't get why this is not gets adressed enough, playing as a vassal in China is impossible after your first succession, you can't even get a county appointment bacause of endless stream of lvl 2-3 merit randoms without a family Click to expand...
<!-- artifact:quote:end -->
Sure you can! As martial. For some reason, there's never a lack of martial track appointments available.

## Reply 84 — participant_051 · 2025-12-03 · post-30957314

<!-- artifact:quote:start -->
> Fuchsia tude said: Sure you can! As martial. For some reason, there's never a lack of martial track appointments available. Click to expand...
<!-- artifact:quote:end -->
Yeah, for martial characters the queue is completely empty, that is another problem. And then you can ask emperor to switch your administration to civilian. But I highly doubt that both of these are intended way of playing, and completely unimmersive. As a civilian character from the start your gameplay is very natural: you earn merit - you get county, you earn more merit - you get duchy, you earn even more merit - you get kingdom, then you earn more merit and can get ministry. As a martial: you enter queue - you get kingdom immediatly, then emperor sends you a direct invite to ministry couple years in. As a second generation civilian: you earn merit, you earn merit, you earn merit, you get merit lvl 3 and finally you can breeze past army of randomly generated AI oafs and get any appointments.

## Reply 85 — participant_054 · 2025-12-03 · post-30957422

Can you guy also fix the "Siberian Permafrost" modifier removal method ? I've already made a bug report : https://forum.paradoxplaza.com/foru...mafrost-inconsistant-removeal-method.1884440/ Long story short , If you're a tribe , you conquer any county with this modifier , then decide to turn feudal via the "Adopt feudal ways" while you or your vassal holding these holdings , the modifier will stay there while the county become feudal . This by itself seems fine , but the irony is , if an holding with this modifier is an nomadic settlement and you're tribal government , you can remove it using the "Trivialize Holding" interaction . or you're feudal/clan/admin , and the county is tribal , you can remove it using the "Feudalize Holding" interaction

## Reply 86 — participant_055 · 2025-12-04 · post-30960481

Shamanism Religion can not show their witch god's name correctly, this is a bug report.

## Reply 87 — participant_055 · 2025-12-04 · post-30960508

As I played the open beta, I found that tiefutu is back somehow, but it is more like light cav instead of heavy cav. Tiefutu is described as the best among the best as chinese ancient files recorded, and its founder, jurchen people are also known for their high quality and low quantity, as desribed by Emperor Taizu of Liao（Khitan）​ "女真不满万，满万不可敌。”（jurchen army is less than 10 thousand, but once they reach the number they are unstoppable.) So ideally, tiefutu should be like accolade armies, with high quality but limited quantity. And, still tiefutu's founder jurchen people, cannot recruit tiefutu cav, which is, again, ridiculous.

## Reply 88 — participant_002 · 2025-12-04 · post-30960523

<!-- artifact:quote:start -->
> RexNusquam said: As I played the open beta, I found that tiefutu is back somehow, but it is more like light cav instead of heavy cav. Tiefutu is described as the best among the best as chinese ancient files recorded, and its founder, jurchen people are also known for their high quality and low quantity, as desribed by Emperor Taizu of Liao（Khitan）​"女真不满万，满万不可敌。”（jurchen army is less than 10 thousand, but once they reach the number they are unstoppable.) So ideally, tiefutu should be like accolade armies, with high quality but limited quantity. And, still tiefutu's founder jurchen people, cannot recruit tiefutu cav, which is, again, ridiculous. Click to expand...
<!-- artifact:quote:end -->
player been saying jin doesn't get tiefutu are hilarious since first announced but paradox didn't change it after many month so it is clearly intentional not sure why

## Reply 89 — participant_056 · 2025-12-04 · post-30961062

"We are sure that you’d prefer this rather than if we rushed the update out, " - yeap, i am certain that an update much better be well tested by QA, we will wait for a week))

## Reply 90 — participant_057 · 2025-12-07 · post-30970489

I'd like to see some additional information added to the royal titles. In particular, I'd like to see the title "Princess Consort" added to the prince's spouse, and for cases like "Queen Dowager" and "Empress Dowager," the titles should be permanent.

## Reply 91 — participant_057 · 2025-12-07 · post-30970491

Additionally, in East Asia, there are titles of Emperors and Kings who have abdicated, such as the King of the Shang Dynasty and Emperor of the Sanghwa Dynasty, and the titles of Grand Emperor and Grand Emperor of the Sanghwa Dynasty. These are titles held by the father and grandfather of the monarch, respectively. I hope this will be reflected in Asia and Europe.

## Reply 92 — participant_058 · 2025-12-07 · post-30970847

<!-- artifact:quote:start -->
> selima2921 said: These are titles held by the father and grandfather of the monarch, respectively. I hope this will be reflected in Asia and Europe. Click to expand...
<!-- artifact:quote:end -->
sinophere got some types: - temple name - posthumous name etc... hope that they can add them

## Reply 93 — participant_046 · 2025-12-07 · post-30971899

<!-- artifact:quote:start -->
> TempestM said: Ah yes, the single hivemind entity known as "The Players" , where one posting means one united opinion Click to expand...
<!-- artifact:quote:end -->
Non sequitur. I didn't accuse The Players of hypocrisy, I said that different players have contradictory opinions, which makes their feedback collectively useless. Hence my conclusion being "Maybe the devs should just ignore us," rather than any condemnation of The Players.

## Reply 94 — participant_012 · 2025-12-07 · post-30971980

<!-- artifact:quote:start -->
> GreatWyrmGold said: Non sequitur. I didn't accuse The Players of hypocrisy, I said that different players have contradictory opinions, which makes their feedback collectively useless. Hence my conclusion being "Maybe the devs should just ignore us," rather than any condemnation of The Players. Click to expand...
<!-- artifact:quote:end -->
Well this is a bad conclusion. Feedback is never collectively unified, yet it's still useful

## Reply 95 — participant_024 · 2025-12-07 · post-30972320

<!-- artifact:quote:start -->
> GreatWyrmGold said: Non sequitur. I didn't accuse The Players of hypocrisy, I said that different players have contradictory opinions, which makes their feedback collectively useless. Hence my conclusion being "Maybe the devs should just ignore us," rather than any condemnation of The Players. Click to expand...
<!-- artifact:quote:end -->
But a game as a product is purchased by players, which pays the developers. If the developers are out of touch with reality and develop the game in a way that's contrary to what players want, then the game is usually neither purchased nor played. (In this case, the annual subscription to new content, which Paradox calls "chapters," is simply not renewed.) Developers should listen to players, evaluate all opinions and requests, and implement everything necessary for a comfortable gaming experience. That's literally their job. And yes, all types of players do have different needs, but most often they don't conflict and can be implemented without degrading the gaming experience for others. And I understand why roleplayers want better AI and more decisions, interactions, etc., while min-maxers want better balance and automation. And these two requirements don't conflict in any way; in fact, they complement each other. So, developers shouldn't improve based on "one player's wishes," but rather improve the gaming experience for all major playstyles. And to do this, of course, developers need to listen to players who offer useful ideas in the form of feedback.

## Reply 96 — participant_059 · 2025-12-08 · post-30972717

Votre jeu est une honte... Il est génial... Mais votre lancer... C’est vraiment de la. Quand vous aurez enlever le luncher et fait en sorte de pouvoir directement jouer au jeu, je pourrais peut être faire des louanges et des compliments sur votre travail. 300 heures de jeu partit en fumé, car votre luncher crash tout le temps... Pour ceux qui n’on pas encore acheter le jeu,,,Revenez d’ici 10 ans, ils auront peut être compris les bases du codage... En tous cas je leurs souhaites.

## Reply 97 — participant_060 · 2025-12-08 · post-30972887

Are these bugs being addressed in this patch : 1. Mandala succession bugs 2. Co-Monarch Designated Heir succession bugs in Feudal Government

## Reply 98 — participant_049 · 2025-12-08 · post-30973554

<!-- artifact:quote:start -->
> aadf97799c said: the next step of travel system is obvious send envoy for stuff like tribute to tang or visit silk road market this could be expend further into invest and send out merchant caravan Click to expand...
<!-- artifact:quote:end -->
I agree that this is absolutely needed. We can sponsor adventurers to gain an artifact so this seems like a logical extension. I find it weird that a feudal emperor from Europe can take a gap year to go backpacking in Asia.

## Reply 99 — participant_061 · 2025-12-08 · post-30974043

Will the patch come out today or tomorrow or later in the week?

## Reply 100 — participant_002 · 2025-12-08 · post-30974122

<!-- artifact:quote:start -->
> ClawofBeta said: Will the patch come out today or tomorrow or later in the week? Click to expand...
<!-- artifact:quote:end -->
vacation coming soon 1.18.2 will have to be this week if it happen this year

## Reply 101 — participant_062 · 2025-12-08 · post-30974150

<!-- artifact:quote:start -->
> aadf97799c said: vacation coming soon 1.18.2 will have to be this week if it happen this year Click to expand...
<!-- artifact:quote:end -->
I think it would have to be today or tomorrow so that there is a window of days to follow up and, if necessary, develop a new patch to correct a serious error that might arise (I don't think the latter will happen because it seems that they are focusing a lot on this update).

## Reply 102 — participant_010 · 2025-12-08 · post-30974236

<!-- artifact:quote:start -->
> ClawofBeta said: Will the patch come out today or tomorrow or later in the week? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> aadf97799c said: vacation coming soon 1.18.2 will have to be this week if it happen this year Click to expand...
<!-- artifact:quote:end -->
The good news is that there's an open beta and it's easy to opt into. I have a fairly large bug that I've posted for it that's currently In Review. I wouldn't mind if they leave the beta open through the winter break and take the time to really crunch down the bugs and iterate on design - once we're out of post-release support it'll be much harder to get dev attention on lingering bugs and design kinks for AUH content.

## Reply 103 — participant_063 · 2025-12-08 · post-30974259

A friendly reminder: if you are unable to deliver the update at the promised time, please issue an additional announcement to clarify the situation. I also work in IT, so I fully understand the complexity and challenges involved in certain tasks, and I am willing to accept any explanation you provide. However, when an update is delayed without any communication, it can be confusing and disappointing. Thank you very much.

## Reply 104 — participant_049 · 2025-12-08 · post-30974486

<!-- artifact:quote:start -->
> ClawofBeta said: Will the patch come out today or tomorrow or later in the week? Click to expand...
<!-- artifact:quote:end -->
I think they said ''the week after this one'' when it was posted. So that would mean: next week, before the holidays.

## Reply 105 — participant_046 · 2025-12-09 · post-30975636

<!-- artifact:quote:start -->
> Gamshud said: And yes, all types of players do have different needs, but most often they don't conflict and can be implemented without degrading the gaming experience for others. Click to expand...
<!-- artifact:quote:end -->
This is a weird response, considering the context is me pointing to one group of players who wants faster releases (even if it means less QA) and another who wants more QA (even if it means slower releases). The needs and desires of different kinds of players don't always conflict*, but this is one case where they very explicitly do. *Though they are more likely to conflict if there is a secret third factor to consider, like budget or verisimilitude or a third group of players with a third set of dissonant desires

## Reply 106 — participant_064 · 2025-12-09 · post-30975688

@PDX-Trinexx @egghorse Since the beginning of this year, there's been a serious problem. "Crowns of the World" DLC conflicts with "West Slavic Attire" DLC, causing all Slavic kings to wear identical Vladimir crowns and sometimes moustaches, completely ignoring the crowns and fashion of Western Slavic. The "Crowns of the World" DLC is generally quite aggressively designed. Since its release, I haven't seen any East Slavic or West Slavic kings or queens wearing any other crowns. Problem with crowns Information I have verifed my game files (Steam only) Yes I have disabled all mods Yes I am running the latest game update Yes Required Summary Problem with crowns Description I don't know if it's a bug or was it intended but should the... forum.paradoxplaza.com The problem isn't limited to these DLCs. Clothing and fashion items from other DLCs, such as "Elegance of the Empire" and "Garments of the Holy Roman Empire," often override the default fashion, leading to a frequent issue with queens no longer wearing their crowns, as described in this thread. The Eastern Roman Problem and Clothing Fix Needed TLDR: I couldn't be bothered to put this in the Bug Report forum since people have already brought this issue up and they've hardly been given a just due response. The Eastern Romans have been bastardized. From the early era clothing to the Born... forum.paradoxplaza.com Overall, it's worth paying attention to the scripts for all the fashion DLCs, they're clearly not working correctly.

## Reply 107 — participant_065 · 2025-12-09 · post-30977014

Do we know when this will be released?

## Reply 108 — participant_015 · 2025-12-09 · post-30977090

<!-- artifact:quote:start -->
> Whaim said: Do we know when this will be released? Click to expand...
<!-- artifact:quote:end -->
potentially tomorrow, but dont tell anyone i told you that

## Reply 109 — participant_061 · 2025-12-10 · post-30980681

Apparently not tomorrow. Fingers crossed that it’s sooner since RICE just got updated and I’m itching for a new campaign.

## Reply 110 — participant_002 · 2025-12-10 · post-30980703

<!-- artifact:quote:start -->
> ClawofBeta said: Apparently not tomorrow. Fingers crossed that it’s sooner since RICE just got updated and I’m itching for a new campaign. Click to expand...
<!-- artifact:quote:end -->
what rice getting what update

## Reply 111 — participant_066 · 2025-12-10 · post-30980861

<!-- artifact:quote:start -->
> aadf97799c said: what rice getting what update Click to expand...
<!-- artifact:quote:end -->
Its a flavor pack mod that just got an update to account for the new regions in AUH. And I agree, at least an update on where we are and what we can expect, even tentatively, would be appreciated. Nevertheless, I have no clue how complicated these things are or how busy they might be so ¯\_(ツ)_/¯. Optimistically before the day ends, in all hope before the week ends is what I am personally hoping for. I at least hope that 867 is fixed on the open beta on my platform soon. That's my preferred start date.

## Reply 112 — participant_023 · 2025-12-10 · post-30981397

<!-- artifact:quote:start -->
> Truenorth14 said: Could you guys also do something about the later 3 kingdoms period of Korea? Click to expand...
<!-- artifact:quote:end -->
Add a separate county with Seoul?)

## Reply 113 — participant_067 · 2025-12-11 · post-30984290

HRE rework and sea battles please

## Reply 114 — participant_015 · 2025-12-12 · post-30984893

No sea battles please, make land battles worth having first

