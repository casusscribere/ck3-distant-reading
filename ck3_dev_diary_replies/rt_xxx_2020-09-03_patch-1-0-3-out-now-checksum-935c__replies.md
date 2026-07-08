---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1416565/"
forum_thread_id: 1416565
content_type: reply_thread
parent_dd_file: dd_xxx_2020-09-03_patch-1-0-3-out-now-checksum-935c.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: Patch 1.0.3. Out now! Checksum [935c]
dd_date: 2020-09-03
expansion: Base game
patch: Crusader Kings III
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 9
reply_count: 163
participant_count: 82
reply_date_first: 2020-09-03
reply_date_last: 2020-09-29
body_word_count: 6707
inline_image_count: 0
quoted_span_count: 125
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — Patch 1.0.3. Out now! Checksum [935c]

*163 replies from 82 participants across 9 pages*

## Reply 1 — participant_001 · 2020-09-03 · post-26860826

Hi everyone! We have just deployed a new (small) patch, version 1.0.3. It fixes various issues related to succession. On behalf of the Crusader Kings III team, we are sincerely grateful and humbled by all your feedback! We are working hard to investigate and address the issues that have been reported! Independent from this patch, we have pushed a potential fix for Steam users that couldn’t fire up the game. This means that next time you will start the game via Steam, you will get an installation step (like on a first-time installation), don’t worry, this is perfectly normal! If you want to know more about how to post a bug report, check this thread! See you soon! Spoiler: Changelog Rewrote the order of succession system. This fixes a variety of issue related to succession. Some examples include half-siblings from the wrong parent inheriting, distant relatives not inheriting, and some issues with who would inherit land in partition.

## Reply 2 — participant_002 · 2020-09-03 · post-26860865

really? you fixed this ONE thing and not the constant boat spam? lazy

## Reply 3 — participant_003 · 2020-09-03 · post-26860869

<!-- artifact:quote:start -->
> tef said: really? you fixed this ONE thing and not the constant boat spam? lazy Click to expand...
<!-- artifact:quote:end -->
The succession bug fix was done weeks ago, they just didn't have time to bug test it for main release...

## Reply 4 — participant_004 · 2020-09-03 · post-26860875

<!-- artifact:quote:start -->
> tef said: really? you fixed this ONE thing and not the constant boat spam? lazy Click to expand...
<!-- artifact:quote:end -->
Boat spam? You mean AI being able to finally use water to move armies around in wars?

## Reply 5 — participant_005 · 2020-09-03 · post-26860882

What’s the specific succession fix? I’m still trying to get my head around how some bits of the new succession systems work - so difficult to tell what’s a bug from what I simply don’t get yet.

## Reply 6 — participant_006 · 2020-09-03 · post-26860883

<!-- artifact:quote:start -->
> tef said: really? you fixed this ONE thing and not the constant boat spam? lazy Click to expand...
<!-- artifact:quote:end -->
sometimes it helps to read the whole post, not just the changelog

## Reply 7 — participant_007 · 2020-09-03 · post-26860885

<!-- artifact:quote:start -->
> tef said: really? you fixed this ONE thing and not the constant boat spam? lazy Click to expand...
<!-- artifact:quote:end -->
Why they would fix thing what they make intentionaly?

## Reply 8 — participant_008 · 2020-09-03 · post-26860886

Is this compatible to release (1.0.2) saves?

## Reply 9 — participant_006 · 2020-09-03 · post-26860898

<!-- artifact:quote:start -->
> Greene said: Is this compatible to release (1.0.2) saves? Click to expand...
<!-- artifact:quote:end -->
it should be. certain changes tend to break save compatibility, but these shouldn't.

## Reply 10 — participant_009 · 2020-09-03 · post-26860902

<!-- artifact:quote:start -->
> tef said: really? you fixed this ONE thing and not the constant boat spam? lazy Click to expand...
<!-- artifact:quote:end -->
Succession was clearly and straightforwardly defective in ways that were making Really Bad Things happen. Boat spam is a balance and AI behaviour issue to which a variety of approaches are valid and which does not require a super-urgent fix the way "wtf why is my mother the heir to the male-preference titles I inherited from my father when I have two living uncles?" and friends did.

## Reply 11 — participant_010 · 2020-09-03 · post-26860904

<!-- artifact:quote:start -->
> Greene said: Is this compatible to release (1.0.2) saves? Click to expand...
<!-- artifact:quote:end -->
Yes.

## Reply 12 — participant_011 · 2020-09-03 · post-26860913

What succession bug? The Ironman one? Cause I just loaded my save where the succession was all over the place and happened again. Not to mention that the AI just uses boats to escape combat. Of course in the middle ages armies would summon ships out of the arse and escape. Makes sense. Once the new car smell dies off, the ugly shows its head. Guess they'll fix it with patch 1.13 or something.

## Reply 13 — participant_002 · 2020-09-03 · post-26860917

<!-- artifact:quote:start -->
> Illanair said: Boat spam? You mean AI being able to finally use water to move armies around in wars? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Pellaken said: sometimes it helps to read the whole post, not just the changelog Click to expand...
<!-- artifact:quote:end -->
no, the constant embarking and landing for no reason where do they mention the boat issue in the post? thought so.

## Reply 14 — participant_012 · 2020-09-03 · post-26860926

<!-- artifact:quote:start -->
> johnty5 said: What’s the specific succession fix? I’m still trying to get my head around how some bits of the new succession systems work - so difficult to tell what’s a bug from what I simply don’t get yet. Click to expand...
<!-- artifact:quote:end -->
My understanding is that it is spouses being in line to inherit titles. I'm not sure if there were other issues as well, but that was a pretty big one.

## Reply 15 — participant_003 · 2020-09-03 · post-26860936

<!-- artifact:quote:start -->
> johnty5 said: What’s the specific succession fix? I’m still trying to get my head around how some bits of the new succession systems work - so difficult to tell what’s a bug from what I simply don’t get yet. Click to expand...
<!-- artifact:quote:end -->
I'm not sure how many issues existed with succession laws - but sometimes the order of succession would change to include people who shouldn't be there after the rulers death. For example if you had a county with an heir of your dynasty, and your heir's mother had a child with someone else, that child would inherit after your heir instead of it passing back to your dynasty.

## Reply 16 — participant_013 · 2020-09-03 · post-26860941

I saw this & was just about to get upset that my game would be ruined, when I see there is already an option to play with the original version 1.02 on steam. Well done. Used to be a big bugbear in early CK2.

## Reply 17 — participant_006 · 2020-09-03 · post-26860948

<!-- artifact:quote:start -->
> tef said: where do they mention the boat issue in the post? thought so. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> PDX_Pariah said: Independent from this patch, we have pushed a potential fix for Steam users that couldn’t fire up the game. This means that next time you will start the game via Steam, you will get an installation step (like on a first-time installation), don’t worry, this is perfectly normal! Click to expand...
<!-- artifact:quote:end -->
I said read the whole post, not "they fixed the thing they are intentionally doing with boats that you misleadingly call spam" here's the part of the post you missed when you said they fixed "one thing"

## Reply 18 — participant_014 · 2020-09-03 · post-26860953

<!-- artifact:quote:start -->
> Illanair said: Boat spam? You mean AI being able to finally use water to move armies around in wars? Click to expand...
<!-- artifact:quote:end -->
I was playing as a count in Ireland and my enemy count who lived right beside me would put all of his troops on boats and then do an amphibious assault into my territory, instead of just walking into my area. The AI wastes money doing this but more importantly they have no chance of winning wars when they engage in their useless boat spam.

## Reply 19 — participant_010 · 2020-09-03 · post-26860956

We've updated the changelog now to be more descriptive: "Rewrote the order of succession system. This fixes a variety of issue related to succession. Some examples include half-siblings from the wrong parent inheriting, distant relatives not inheriting, and some issues with who would inherit land in partition. "

## Reply 20 — participant_006 · 2020-09-03 · post-26860970

<!-- artifact:quote:start -->
> iZach said: I was playing as a count in Ireland and my enemy count who lived right beside me would put all of his troops on boats and then do an amphibious assault into my territory, instead of just walking into my area. The AI wastes money doing this but more importantly they have no chance of winning wars when they engage in their useless boat spam. Click to expand...
<!-- artifact:quote:end -->
this sounds like some kind of error in AI programming (IE an actual problem) and not "boat spam"

## Reply 21 — participant_014 · 2020-09-03 · post-26860984

<!-- artifact:quote:start -->
> Pellaken said: this sounds like some kind of error in AI programming (IE an actual problem) and not "boat spam" Click to expand...
<!-- artifact:quote:end -->
It is both. You're playing a useless word game. The error is that they make use of boats incorrectly by spamming them for no reason.

## Reply 22 — participant_015 · 2020-09-03 · post-26860994

<!-- artifact:quote:start -->
> iZach said: It is both. You're playing a useless word game. The error is that they make use of boats incorrectly by spamming them for no reason. Click to expand...
<!-- artifact:quote:end -->
Which is an AI issue, which are much harder to fix than succession bugs. Hence why they didn't make us wait until it was fixed internally before releasing the fix for another major bug (and one that had been spotted pre-release but post-code-freeze, so one they've probably had fixed and bug-tested for a while now).

## Reply 23 — participant_016 · 2020-09-03 · post-26860997

What is this supposed to fix? My son still inherits a non-existant title which I cant create either.

## Reply 24 — participant_006 · 2020-09-03 · post-26860998

<!-- artifact:quote:start -->
> iZach said: It is both. You're playing a useless word game. The error is that they make use of boats incorrectly by spamming them for no reason. Click to expand...
<!-- artifact:quote:end -->
using terms the devs can understand is hardly useless. If there's a boat misuse, then it should be reported, and fixed by the devs.

## Reply 25 — participant_014 · 2020-09-03 · post-26861005

<!-- artifact:quote:start -->
> Rubidium said: Which is an AI issue, which are much harder to fix than succession bugs. Hence why they didn't make us wait until it was fixed internally before releasing the fix for another major bug (and one that had been spotted pre-release but post-code-freeze, so one they've probably had fixed and bug-tested for a while now). Click to expand...
<!-- artifact:quote:end -->
I realize it will take time to fix. I'm not tef. I simply replied to the people who somehow think boat spam is not an issue.

## Reply 26 — participant_005 · 2020-09-03 · post-26861032

Excited for the thread for Patch 1.0.4 - I wonder what definition of boat spam we’ll be chatting about in that one.

## Reply 27 — participant_017 · 2020-09-03 · post-26861060

<!-- artifact:quote:start -->
> tef said: funny the guy that havent even played that game and dont understand what boat spam means and how it's an issue is talking about others not understanding. stop posting please Click to expand...
<!-- artifact:quote:end -->
Good idea. Report the problem, with saves, and a *clear* description. In the bug forum. They'll add it to the list of issues, and sort it in what they consider a priority order.

## Reply 28 — participant_018 · 2020-09-03 · post-26861085

Hey I'm playing on Ironman for Achievements but when I go into my load screen it says different version. Will I still get achievements with this? Thanks. Voice

## Reply 29 — participant_019 · 2020-09-03 · post-26861117

<!-- artifact:quote:start -->
> zorkman said: I saw this & was just about to get upset that my game would be ruined, when I see there is already an option to play with the original version 1.02 on steam. Well done. Used to be a big bugbear in early CK2. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> VoiceGS said: I'm playing on Ironman for Achievements but when I go into my load screen it says different version. Will I still get achievements with this? Click to expand...
<!-- artifact:quote:end -->
I'd also like an answer for this... I'd assume you should be able to continue an Ironman save with this patch, but can we get some dev confirmation of that? Also, how long should it take for succession in a 1.0.2 save to update to the 1.0.3 version? One month ingame? Until someone in the line of succession dies? Would be helpful to know when it recalculates, so we don't have a bunch of spurious "it didn't work" messages.

## Reply 30 — participant_002 · 2020-09-03 · post-26861120

<!-- artifact:quote:start -->
> grommile said: Succession was clearly and straightforwardly defective in ways that were making Really Bad Things happen. Boat spam is a balance and AI behaviour issue to which a variety of approaches are valid and which does not require a super-urgent fix the way "wtf why is my mother the heir to the male-preference titles I inherited from my father when I have two living uncles?" and friends did. Click to expand...
<!-- artifact:quote:end -->
i would say having the AI bankrupt itself and having constant disembark penalty and losing every war is a bit higher priority than you believe.

## Reply 31 — participant_020 · 2020-09-03 · post-26861133

<!-- artifact:quote:start -->
> MarkFranz said: Why they would fix thing what they make intentionaly? Click to expand...
<!-- artifact:quote:end -->
Imperator Rome dropped mana in patch 1.1, eu4 emperor first patch dropped ability to drop reform desireif not papal states. Paradox has gone back on their game designs a few times now

## Reply 32 — participant_021 · 2020-09-03 · post-26861157

<!-- artifact:quote:start -->
> PDX_Pariah said: Rewrote the order of succession system. This fixes a variety of issue related to succession. Some examples include half-siblings from the wrong parent inheriting, distant relatives not inheriting, and some issues with who would inherit land in partition. Click to expand...
<!-- artifact:quote:end -->
Will this require a new game? Because it does not fix the succession issue I was having, where I'm not getting my realm capital, due to what I think is a weird intersection of Partition and Tanistry. I let it run until a few days after a new year, no changes. Bug thread here.

## Reply 33 — participant_022 · 2020-09-03 · post-26861329

Was something changed in a question of House Head line of succession?

## Reply 34 — participant_010 · 2020-09-03 · post-26861428

<!-- artifact:quote:start -->
> Matt516 said: Also, how long should it take for succession in a 1.0.2 save to update to the 1.0.3 version? One month ingame? Until someone in the line of succession dies? Would be helpful to know when it recalculates, so we don't have a bunch of spurious "it didn't work" messages. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Jorlem said: Will this require a new game? Because it does not fix the succession issue I was having, where I'm not getting my realm capital, due to what I think is a weird intersection of Partition and Tanistry. I let it run until a few days after a new year, no changes. Bug thread here. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> aono said: Was something changed in a question of House Head line of succession? Click to expand...
<!-- artifact:quote:end -->
Opening your succession view or hovering over your primary title both force a succession recalc, so it should update immediately. It does not require a new game. That bug sounds like something that would be unaffected by the changes we made in this patch. House Head continues to follow the Player Heir succession.

## Reply 35 — participant_022 · 2020-09-03 · post-26861433

<!-- artifact:quote:start -->
> Meneth said: House Head continues to follow the Player Heir succession. Click to expand...
<!-- artifact:quote:end -->
So, whenever it's not a case it's a bug?

## Reply 36 — participant_010 · 2020-09-03 · post-26861541

<!-- artifact:quote:start -->
> aono said: So, whenever it's not a case it's a bug? Click to expand...
<!-- artifact:quote:end -->
Yeah. Be aware that Dynasty Head succession is separate from House Head though. The Dynasty Head is the strongest House Head, and can take up to a year to update.

## Reply 37 — participant_023 · 2020-09-03 · post-26861570

I know saves should be compatible, but would the former succession issues remain in saved games and we should start a new one to get the issue solved, or the issues should be solved even in games started before the update?

## Reply 38 — participant_024 · 2020-09-03 · post-26861571

[935c] 936 start date confirmed? Nah, Its probably my brain overreacting to some random numbers. Might just be a coincidence ... Unless if ...

## Reply 39 — participant_025 · 2020-09-03 · post-26861574

Any word on the bug where achievements that require you to start as certain characters are not firing when you meet the requirements? It's not a huge deal gameplay wise but it would be nice to know if those saves will be able to get the achievement once its fixed or if you would need to start all over again.

## Reply 40 — participant_026 · 2020-09-03 · post-26861667

Question, in my current game under the previous patch, I encountered a problem. I had one empire and five kingdoms. Scandinavian succession. All had my heir as first in line, only family was elegible. But when my emperor died, two of the kingdoms was inherited by outsiders not of my dynasty. One was even Russian and as far as I know not my vassal prior to this. Is this something that is fixed?

## Reply 41 — participant_010 · 2020-09-03 · post-26861677

<!-- artifact:quote:start -->
> EU3noob128 said: Any word on the bug where achievements that require you to start as certain characters are not firing when you meet the requirements? It's not a huge deal gameplay wise but it would be nice to know if those saves will be able to get the achievement once its fixed or if you would need to start all over again. Click to expand...
<!-- artifact:quote:end -->
We're aware of that issue, and are looking into it. It is unlikely the fix to it will fix existing saves; it'll probably only help new saves.

## Reply 42 — participant_027 · 2020-09-03 · post-26861702

great to see the update to succession system. Would you be able to look at the problem that culture-specific succession rules (like Czech Seniority) is applied to other titles that those guys hold (like Czech ruler holding Kingdom of Hungary, suddenly gets a huge bonus that Hungary also gets Seniority)? See https://forum.paradoxplaza.com/foru...ave-house-seniority-rule-super-early.1416126/

## Reply 43 — participant_019 · 2020-09-03 · post-26861707

<!-- artifact:quote:start -->
> Meneth said: That bug sounds like something that would be unaffected by the changes we made in this patch. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Meneth said: House Head continues to follow the Player Heir succession Click to expand...
<!-- artifact:quote:end -->
I think it would be really helpful for the community to get some dev word on the Tanistry/Partition interaction, as the tutorial is funneling players into Tanistry and they're getting some really weird results (like keeping the Kingdom but losing the capital County). Is this bugged? Is it WAD but confusing? Doesn't seem to be the case sometimes. When my first character died (Irish Duke), his granddaughter via his first (deceased) son became Player Heir while his second son became House Head. The second son was also a Duke after succession (Confed Partition created it) so maybe that had something to do with it? In any case, House Head definitely does not always follow Player Heir.

## Reply 44 — participant_028 · 2020-09-03 · post-26861799

Does the patch fix your mother inheriting before your uncle or sister or your grandchildren being primary heir before your children.

## Reply 45 — participant_029 · 2020-09-03 · post-26861804

<!-- artifact:quote:start -->
> PDX_Pariah said: Hi everyone! We have just deployed a new (small) patch, version 1.0.3. It fixes various issues related to succession. On behalf of the Crusader Kings III team, we are sincerely grateful and humbled by all your feedback! We are working hard to investigate and address the issues that have been reported! Independent from this patch, we have pushed a potential fix for Steam users that couldn’t fire up the game. This means that next time you will start the game via Steam, you will get an installation step (like on a first-time installation), don’t worry, this is perfectly normal! If you want to know more about how to post a bug report, check this thread! See you soon! Spoiler: Changelog Rewrote the order of succession system. This fixes a variety of issue related to succession. Some examples include half-siblings from the wrong parent inheriting, distant relatives not inheriting, and some issues with who would inherit land in partition. Click to expand...
<!-- artifact:quote:end -->
This patch de ironmanned my save??? How do I fix it??

## Reply 46 — participant_019 · 2020-09-03 · post-26861855

<!-- artifact:quote:start -->
> Abbta said: This patch de ironmanned my save??? How do I fix it?? Click to expand...
<!-- artifact:quote:end -->
Same question. Are we seriously not supposed to be able to play an Ironman game through a patch?

## Reply 47 — participant_030 · 2020-09-03 · post-26861891

<!-- artifact:quote:start -->
> Meneth said: House Head continues to follow the Player Heir succession. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Meneth said: Be aware that Dynasty Head succession is separate from House Head though. The Dynasty Head is the strongest House Head, and can take up to a year to update. Click to expand...
<!-- artifact:quote:end -->
Except both those are not true. My character (char 1) abdicated because of mental break and remained house head AND dynasty head. His younger brother (2) inherited the titles (and i was playing him because ironman). The old head (1) then died and both titles went to his heir (son of 1, born after the abdication), which is not only much weaker in every aspect then my character (2) and is even his vassal because (2) ranked up to king in the meantime. All of above are in the same house. Dynasty head did not updated yet.

## Reply 48 — participant_019 · 2020-09-03 · post-26861940

<!-- artifact:quote:start -->
> dilbertini said: mother inheriting before your uncle or sister Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> dilbertini said: grandchildren being primary heir before your children Click to expand...
<!-- artifact:quote:end -->
I think this is the bug they fixed, yeah. Don't think this is a bug, if it's the child of your deceased firstborn. Firstborn still gets their due if they have heirs, even if they're dead. I think.

## Reply 49 — participant_028 · 2020-09-03 · post-26862022

<!-- artifact:quote:start -->
> Matt516 said: Don't think this is a bug, if it's the child of your deceased firstborn. Firstborn still gets their due if they have heirs, even if they're dead. I think. Click to expand...
<!-- artifact:quote:end -->
This is logical, but since in ck2 your children had priority over those children of your deceased firstborn and there was a bug linked to succession, I wanted confirmation if it's working as wanted.

## Reply 50 — participant_031 · 2020-09-03 · post-26862236

My Ironman save is also incompatible now. I really don't feel like abandoning this save that I've already gotten so interested in, so I'm downgrading back to launch version until this (hopefully) gets worked out.

## Reply 51 — participant_032 · 2020-09-03 · post-26862261

<!-- artifact:quote:start -->
> PDX_Pariah said: Spoiler: Changelog Rewrote the order of succession system. This fixes a variety of issue related to succession. Some examples include half-siblings from the wrong parent inheriting, distant relatives not inheriting, and some issues with who would inherit land in partition. Click to expand...
<!-- artifact:quote:end -->
Does this mean the lowborn widow of the king of Castille inheriting the throne after her son was indeed a bug?...

## Reply 52 — participant_033 · 2020-09-03 · post-26862505

This patch broke my ironman save game. Any way to fix it?

## Reply 53 — participant_034 · 2020-09-03 · post-26862566

<!-- artifact:quote:start -->
> dilbertini said: Does the patch fix your mother inheriting before your uncle or sister or your grandchildren being primary heir before your children. Click to expand...
<!-- artifact:quote:end -->
Mothers still seem to inherit before uncles in my game as Navarra today. (Infante Aznar is my paternal uncle) { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" }

## Reply 54 — participant_033 · 2020-09-03 · post-26862579

<!-- artifact:quote:start -->
> unmerged(733812) said: This patch broke my ironman save game. Any way to fix it? Click to expand...
<!-- artifact:quote:end -->
Found multiple threads on the same issue that happened to me. Its when the game crashes during an autosave to a cloud save: Ironman Save Games keeps getting corrupted Unfortunately, I don't see a way to stop the game from using the cloud so I can't attach the save file. But it seems like after I spend 12 hours on a playthrough, the cloud file gets all corrupted. Is there any way to grab the cloud save... forum.paradoxplaza.com Game Crashed While saveing Ironman save, and my save was corrupted Basically what I said in the title, My game was saving and crashed now my Ironman save is corrupted. Can I get a back up or did I just lose 11 hours of progress. forum.paradoxplaza.com CK III - Crash during autosaving corrupts Ironman save Short summary of your issue Crash during autosaving corrupts Ironman save Game Version 1.02 What OS are you playing on? Windows What platform are you using? Steam Do you have mods enabled? No Have you tried verifying your game... forum.paradoxplaza.com [Crash] [Cloudsave Corruption] Game crashes repeatatly and this corrupts my ironman cloudsave Because I don't have access to my good pc right now, I am using Steam In Home Streaming over the Internet to connect to my PC at home. It mostly works quite well like with other Paradox games, but with CK3 I have the problem that now already for... forum.paradoxplaza.com

## Reply 55 — participant_035 · 2020-09-03 · post-26862606

<!-- artifact:quote:start -->
> tef said: no, the constant embarking and landing for no reason where do they mention the boat issue in the post? thought so. Click to expand...
<!-- artifact:quote:end -->
They probably made the AI embark for free to prevent it from bankrupting itself, and now it's abusing the hell out of it.

## Reply 56 — participant_003 · 2020-09-03 · post-26862628

<!-- artifact:quote:start -->
> thorned96183 said: Mothers still seem to inherit before uncles in my game as Navarra today. (Infante Aznar is my paternal uncle) View attachment 617437 Click to expand...
<!-- artifact:quote:end -->
Was this from a fresh save?

## Reply 57 — participant_013 · 2020-09-03 · post-26862632

<!-- artifact:quote:start -->
> ChaosGoat said: My Ironman save is also incompatible now. I really don't feel like abandoning this save that I've already gotten so interested in, so I'm downgrading back to launch version until this (hopefully) gets worked out. Click to expand...
<!-- artifact:quote:end -->
I am so glad, I changed the beta back to 1.0.02 on Steam, as that seems to be still working in Ironman.

## Reply 58 — participant_036 · 2020-09-03 · post-26862677

Fantastic game!

## Reply 59 — participant_037 · 2020-09-03 · post-26862699

<!-- artifact:quote:start -->
> Jarolleon said: They probably made the AI embark for free to prevent it from bankrupting itself, and now it's abusing the hell out of it. Click to expand...
<!-- artifact:quote:end -->
We could see the issue from the March previews. Pain in the ass chasing tiny stacks embarking ....

## Reply 60 — participant_034 · 2020-09-03 · post-26862713

<!-- artifact:quote:start -->
> GeorgieBest said: Was this from a fresh save? Click to expand...
<!-- artifact:quote:end -->
Yeah, I started a new game right after the update.

## Reply 61 — participant_038 · 2020-09-03 · post-26862766

<!-- artifact:quote:start -->
> dilbertini said: This is logical, but since in ck2 your children had priority over those children of your deceased firstborn and there was a bug linked to succession, I wanted confirmation if it's working as wanted. Click to expand...
<!-- artifact:quote:end -->
In CK2 this was dependent on succession law. Your firstborn's children would inherit ahead of your second born under primogeniture, but not gavelkind. I guess CK3 made it more consistent.

## Reply 62 — participant_028 · 2020-09-03 · post-26862815

<!-- artifact:quote:start -->
> Tatterhood said: In CK2 this was dependent on succession law. Your firstborn's children would inherit ahead of your second born under primogeniture, but not gavelkind. I guess CK3 made it more consistent. Click to expand...
<!-- artifact:quote:end -->
I can understand that, but I would like the game in that case to notify you when your children have children and your heir change, since it was quite the surprise to end up playing a 2 year old grandchild I didn't know existed when I thought I would play one of his 2 uncle who would have inherited a full duchy each if not for him.

## Reply 63 — participant_039 · 2020-09-03 · post-26862834

<!-- artifact:quote:start -->
> Abbta said: This patch de ironmanned my save??? How do I fix it?? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Matt516 said: Same question. Are we seriously not supposed to be able to play an Ironman game through a patch? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> ChaosGoat said: My Ironman save is also incompatible now. I really don't feel like abandoning this save that I've already gotten so interested in, so I'm downgrading back to launch version until this (hopefully) gets worked out. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> unmerged(733812) said: This patch broke my ironman save game. Any way to fix it? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> unmerged(733812) said: Found multiple threads on the same issue that happened to me. Its when the game crashes during an autosave to a cloud save: Click to expand...
<!-- artifact:quote:end -->
That seems like a likely explanation, @unmerged(733812). I deliberately turned off cloud saves when I started my game because I'd heard they had messed up ironman saves for some people on Stellaris, and my save still works with achievements enabled after the patch. My condolences, guys. Getting shafted out of all that hard work because of a glitch like that... You must be steaming right now.

## Reply 64 — participant_040 · 2020-09-03 · post-26862842

Does this fix religious head titles being passed around in partition when they are supposed to pass to main heir?

## Reply 65 — participant_041 · 2020-09-03 · post-26862856

I've got an ironman cloud save from the last version that I just loaded up then exited to menu, the game is perfectly happy with it so far.

## Reply 66 — participant_019 · 2020-09-03 · post-26862868

<!-- artifact:quote:start -->
> Karlington said: That seems like a likely explanation, @unmerged(733812). I deliberately turned off cloud saves when I started my game because I'd heard they had messed up ironman saves for some people on Stellaris, and my save still works with achievements enabled after the patch. Click to expand...
<!-- artifact:quote:end -->
Any way to continue a cloud ironman off of cloud?

## Reply 67 — participant_019 · 2020-09-03 · post-26862875

<!-- artifact:quote:start -->
> Laetoy said: Does this fix religious head titles being passed around in partition when they are supposed to pass to main heir? Click to expand...
<!-- artifact:quote:end -->
Ooh, you should definitely report that on the Bug Report forum. Sounds like it might be similar to whatever is going on with House Head passing to someone who isn't the main heir - "special" titles that should always follow main heir are not.

## Reply 68 — participant_029 · 2020-09-03 · post-26862928

<!-- artifact:quote:start -->
> Karlington said: That seems like a likely explanation, @unmerged(733812). I deliberately turned off cloud saves when I started my game because I'd heard they had messed up ironman saves for some people on Stellaris, and my save still works with achievements enabled after the patch. My condolences, guys. Getting shafted out of all that hard work because of a glitch like that... You must be steaming right now. Click to expand...
<!-- artifact:quote:end -->
Appreciating your sympathy! I had just stabilized Mali and was about to reform my faith when it happened. About 4.5 hours wasted Hopefully Paradox can do something. How do you stop cloud saves?

## Reply 69 — participant_041 · 2020-09-03 · post-26862980

<!-- artifact:quote:start -->
> Abbta said: Appreciating your sympathy! I had just stabilized Mali and was about to reform my faith when it happened. About 4.5 hours wasted Hopefully Paradox can do something. How do you stop cloud saves? Click to expand...
<!-- artifact:quote:end -->
One other option is to store backup Ironman saves, if you paste them back in the correct folder while the game is still running in the main menu then exit, the game will assume *that* cloud Ironman is the 'real' one and let it take over as the cloud save. This requires an uncorrupted Ironman save, ofc.

## Reply 70 — participant_035 · 2020-09-03 · post-26863140

<!-- artifact:quote:start -->
> Matt516 said: Ooh, you should definitely report that on the Bug Report forum. Sounds like it might be similar to whatever is going on with House Head passing to someone who isn't the main heir - "special" titles that should always follow main heir are not. Click to expand...
<!-- artifact:quote:end -->
Also if you make your top-tier title elective, whichever dynast wins the election will be your main heir (i.e. the one you play as) but every other title including house head and your capital county(!) will pass to your gavelkind/primo/seniority heir. Luckily I haven't seen an AI house head piss away the dynasty's renown on denouncements yet, so you can just vote for your house head when the renown is close to 1000 to pick the next legacy.

## Reply 71 — participant_042 · 2020-09-03 · post-26863464

saves are broken

## Reply 72 — participant_043 · 2020-09-03 · post-26863547

<!-- artifact:quote:start -->
> dilbertini said: Does the patch fix your mother inheriting before your uncle or sister or your grandchildren being primary heir before your children. Click to expand...
<!-- artifact:quote:end -->
In my game my nephew who was my vassal had his mother of a different dynasty be primary heir over his own two sisters and me his uncle or anyone else of our dynasty. I tried using console commands to recalculate succession but it had no effect so I killed his mother instead. (This was on a 1.02 save I continued playing).

## Reply 73 — participant_044 · 2020-09-04 · post-26863680

I have a weird graphical bug since this patch released. The map stays constantly zoomed out, despite trying to zoom in our out. The UI elements change, like Holdings labels get bigger/ smaller when you zoom, and the map mode clearly changes at the bottom right. However, the map just stays zoomed out to the max so my game is currently unplayable. Starting a new game does not fix this issue for me. Edit: I finally fixed this by unplugging my controller. This issue has been introduced with the new patch.

## Reply 74 — participant_045 · 2020-09-04 · post-26863758

<!-- artifact:quote:start -->
> Tatterhood said: In CK2 this was dependent on succession law. Your firstborn's children would inherit ahead of your second born under primogeniture, but not gavelkind. I guess CK3 made it more consistent. Click to expand...
<!-- artifact:quote:end -->
I noticed under CK3's Partition laws, grandchildren now get their father's share inheritance if said father dies prematurely.

## Reply 75 — participant_046 · 2020-09-04 · post-26864148

This patch broke my perfectly working 1.0.2 game and now I cant even load into game without crashing. Fix asap Paradox or we're refunding and writing bad reviews since even your crash reporter keeps crashing

## Reply 76 — participant_047 · 2020-09-04 · post-26864283

Is this going to make our current saves incompatible or start bugging out?

## Reply 77 — participant_048 · 2020-09-04 · post-26864659

Can't load my 1.0.2 savegames with this patch

## Reply 78 — participant_030 · 2020-09-04 · post-26864871

<!-- artifact:quote:start -->
> Karlington said: That seems like a likely explanation, @unmerged(733812). I deliberately turned off cloud saves when I started my game because I'd heard they had messed up ironman saves for some people on Stellaris, and my save still works with achievements enabled after the patch. My condolences, guys. Getting shafted out of all that hard work because of a glitch like that... You must be steaming right now. Click to expand...
<!-- artifact:quote:end -->
Can confirm. I never save to cloud and i did not do it in CK3 too, and my save is still in ironman and i'm getting achievements normally.

## Reply 79 — participant_029 · 2020-09-04 · post-26865145

<!-- artifact:quote:start -->
> Vanhal said: Can confirm. I never save to cloud and i did not do it in CK3 too, and my save is still in ironman and i'm getting achievements normally. Click to expand...
<!-- artifact:quote:end -->
Where do I turn this off? I can't seem to get a straight answer from anyone and the game is too young to double check. No option existed in the settings in game.

## Reply 80 — participant_021 · 2020-09-04 · post-26865234

<!-- artifact:quote:start -->
> Abbta said: Where do I turn this off? I can't seem to get a straight answer from anyone and the game is too young to double check. No option existed in the settings in game. Click to expand...
<!-- artifact:quote:end -->
If you save manually, there’s a cloud checkbox under the file name entry field. Unchecking that will keep it from saving to the cloud until the next time you reload the game. There doesn’t appear to be a way to turn it off by default, though.

## Reply 81 — participant_049 · 2020-09-04 · post-26865531

Even after the patch I don't think inheritance works correctly. I am the King of Frisia, no sons, 1 daughter, 1 half brother. He is my vassal and we have the same father from whom we inherited our titles. Succession law is male-preference, confederate partition. Why is my daughter my heir and not my half-brother? This is a major problem because I cannot marry off my daughter for an alliance. I could disinherited her but what a waste.

## Reply 82 — participant_042 · 2020-09-04 · post-26865676

<!-- artifact:quote:start -->
> Staal said: Why is my daughter my heir and not my half-brother? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Staal said: male-preference Click to expand...
<!-- artifact:quote:end -->
by the way ironmane saves that are displayed as from another version-loaded, but it is not clear whether the achievements will work

## Reply 83 — participant_050 · 2020-09-04 · post-26865725

I'm pretty used to major patches breaking savegames in Paradox games, but hotfixes? Really? And the crash reporter is crashing as well? That's new.

## Reply 84 — participant_049 · 2020-09-04 · post-26865973

<!-- artifact:quote:start -->
> Scanz said: by the way ironmane saves that are displayed as from another version-loaded, but it is not clear whether the achievements will work Click to expand...
<!-- artifact:quote:end -->
Just to clarify, are you saying it is WAD that male-preference means daughter inherits before uncles? Guess I have no choice but to disinherit. Can you do that once she has been married off?

## Reply 85 — participant_051 · 2020-09-04 · post-26866142

<!-- artifact:quote:start -->
> Battlex said: Imperator Rome dropped mana in patch 1.1, eu4 emperor first patch dropped ability to drop reform desireif not papal states. Paradox has gone back on their game designs a few times now Click to expand...
<!-- artifact:quote:end -->
Don't know about EU4, but what you're saying about Imperator is wrong. They dropped mana in 1.2, and let's remember that this isn't a 1.1 for CK3, just a simple hotfix. I'm saying these things because se should all remember that reworking this kind of stuff takes more time and in this faith patience should be a virtue. But you're right that it's not unprecedent

## Reply 86 — participant_052 · 2020-09-04 · post-26866271

<!-- artifact:quote:start -->
> Staal said: Even after the patch I don't think inheritance works correctly. I am the King of Frisia, no sons, 1 daughter, 1 half brother. He is my vassal and we have the same father from whom we inherited our titles. Succession law is male-preference, confederate partition. Why is my daughter my heir and not my half-brother? This is a major problem because I cannot marry off my daughter for an alliance. I could disinherited her but what a waste. Click to expand...
<!-- artifact:quote:end -->
She is your daughter, she is your child. She inherits first before your brother.

## Reply 87 — participant_053 · 2020-09-04 · post-26866431

Please consider fixing religion in the next patch. Catholicism is almost ubplayable because of the way fervor and conversion work. It is currently way too prone to heresy and because fervor is always so low you can never convert any of your provinces. Unreformed pagans can convert you in like a year and it takes 20 for you to convert them. Also, please bring back missionaries or at least put pressure on unreformed pagan rulers to convert to Christianity or Islam based on their geographic location.

## Reply 88 — participant_003 · 2020-09-04 · post-26866439

<!-- artifact:quote:start -->
> Staal said: Even after the patch I don't think inheritance works correctly. I am the King of Frisia, no sons, 1 daughter, 1 half brother. He is my vassal and we have the same father from whom we inherited our titles. Succession law is male-preference, confederate partition. Why is my daughter my heir and not my half-brother? This is a major problem because I cannot marry off my daughter for an alliance. I could disinherited her but what a waste. Click to expand...
<!-- artifact:quote:end -->
That's working perfectly fine. Male children inherit before daughters under male-preference, which I'm assuming you have as a catholic. It would go to your half-brother if you followed a religion which was male-only.

## Reply 89 — participant_009 · 2020-09-04 · post-26866451

<!-- artifact:quote:start -->
> Staal said: Just to clarify, are you saying it is WAD that male-preference means daughter inherits before uncles? Click to expand...
<!-- artifact:quote:end -->
Yes. Primogeniture considers all your descendants before any of your siblings.

## Reply 90 — participant_054 · 2020-09-04 · post-26866509

<!-- artifact:quote:start -->
> zorkman said: I saw this & was just about to get upset that my game would be ruined, when I see there is already an option to play with the original version 1.02 on steam. Well done. Used to be a big bugbear in early CK2. Click to expand...
<!-- artifact:quote:end -->
Above they said this patch should be compatible with saves

## Reply 91 — participant_039 · 2020-09-04 · post-26866647

<!-- artifact:quote:start -->
> Abbta said: Appreciating your sympathy! I had just stabilized Mali and was about to reform my faith when it happened. About 4.5 hours wasted Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Matt516 said: Any way to continue a cloud ironman off of cloud? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Abbta said: Hopefully Paradox can do something. How do you stop cloud saves? Click to expand...
<!-- artifact:quote:end -->
That sucks, man. Unfortunately I don't know of a way. When you start an iron man game and pick the name for your save game there is a checkbox for saving to the cloud or not, and I just deselected it when I first started the game.

## Reply 92 — participant_039 · 2020-09-04 · post-26866661

<!-- artifact:quote:start -->
> Scanz said: by the way ironmane saves that are displayed as from another version-loaded, but it is not clear whether the achievements will work Click to expand...
<!-- artifact:quote:end -->
Press Escape while you are in the game, then click "Achievements." The window that pops up should say "Available" in green under the "Achievements" text in that window (not the same text you clicked to get the window to appear).

## Reply 93 — participant_039 · 2020-09-04 · post-26867189

<!-- artifact:quote:start -->
> Scanz said: by the way ironmane saves that are displayed as from another version-loaded, but it is not clear whether the achievements will work Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Karlington said: Press Escape while you are in the game, then click "Achievements." The window that pops up should say "Available" in green under the "Achievements" text in that window (not the same text you clicked to get the window to appear). Click to expand...
<!-- artifact:quote:end -->
I took a screenshot: { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" }

## Reply 94 — participant_010 · 2020-09-04 · post-26867688

<!-- artifact:quote:start -->
> Matt516 said: I think it would be really helpful for the community to get some dev word on the Tanistry/Partition interaction, as the tutorial is funneling players into Tanistry and they're getting some really weird results (like keeping the Kingdom but losing the capital County). Is this bugged? Is it WAD but confusing? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Matt516 said: Doesn't seem to be the case sometimes. When my first character died (Irish Duke), his granddaughter via his first (deceased) son became Player Heir while his second son became House Head. The second son was also a Duke after succession (Confed Partition created it) so maybe that had something to do with it? In any case, House Head definitely does not always follow Player Heir. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Matt516 said: Ooh, you should definitely report that on the Bug Report forum. Sounds like it might be similar to whatever is going on with House Head passing to someone who isn't the main heir - "special" titles that should always follow main heir are not. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Staal said: Even after the patch I don't think inheritance works correctly. I am the King of Frisia, no sons, 1 daughter, 1 half brother. He is my vassal and we have the same father from whom we inherited our titles. Succession law is male-preference, confederate partition. Why is my daughter my heir and not my half-brother? This is a major problem because I cannot marry off my daughter for an alliance. I could disinherited her but what a waste. Click to expand...
<!-- artifact:quote:end -->
It's bugged, and we're working on the issue. There's an occasional bug with that, and we're working on it. We're looking into an issue like that. Your kids in male-preference go ahead of your siblings or parents. That's working correctly.

## Reply 95 — participant_006 · 2020-09-04 · post-26867945

I'm sorry but the idea of the crash reporter crashing almost made me spit water all over my monitor

## Reply 96 — participant_055 · 2020-09-04 · post-26868375

@Meneth I don't yet fully understand all these succession law variants so I just wanted to ask: is there a succession law which passes from brother to bother within the same immediate family (dynasty, I think) but not outside of your specific dynasty (so not to other branches of your house)? In CK II I used to like the idea of Seniority but I didn't like how it became unwieldly the larger your dynasty got, so often titles went to obscure relatives you had nothing to do with. I like to have the succession pass from brother to brother, then to the eldest brother's sons in order, and so on. For example, I used to like playing as Denmark and playing through all of Svend's sons (he about 15) in order, until the youngest died. Does this form of Seniority exist?

## Reply 97 — participant_021 · 2020-09-04 · post-26868402

<!-- artifact:quote:start -->
> Meneth said: There's an occasional bug with that, and we're working on it. Click to expand...
<!-- artifact:quote:end -->
As a temporary workaround for the issue with dynasty/house head not inheriting properly, is there a console command to make the player character the head of the dynasty/house? Also, is High Crown Authority supposed to stop Partition from removing counties from your realm? Because I ran into a situation where two of my counties (one of which was my realm capital) went to my dying character's grandson instead of the chosen Tanist, and as the grandson held the title for Lucca, those provinces became independent from the Kingdom of Ireland.

## Reply 98 — participant_049 · 2020-09-04 · post-26868694

<!-- artifact:quote:start -->
> grommile said: Yes. Primogeniture considers all your descendants before any of your siblings. Click to expand...
<!-- artifact:quote:end -->
Thanks.

## Reply 99 — participant_056 · 2020-09-05 · post-26869016

<!-- artifact:quote:start -->
> Monkbel said: great to see the update to succession system. Would you be able to look at the problem that culture-specific succession rules (like Czech Seniority) is applied to other titles that those guys hold (like Czech ruler holding Kingdom of Hungary, suddenly gets a huge bonus that Hungary also gets Seniority)? See https://forum.paradoxplaza.com/foru...ave-house-seniority-rule-super-early.1416126/ Click to expand...
<!-- artifact:quote:end -->
This is WAD, Czech culture has a unique innovation that allows them to change their succession law to House Seniority regardless of their other innovations or laws.

## Reply 100 — participant_010 · 2020-09-05 · post-26870336

<!-- artifact:quote:start -->
> Pied-Noir said: @Meneth I don't yet fully understand all these succession law variants so I just wanted to ask: is there a succession law which passes from brother to bother within the same immediate family (dynasty, I think) but not outside of your specific dynasty (so not to other branches of your house)? In CK II I used to like the idea of Seniority but I didn't like how it became unwieldly the larger your dynasty got, so often titles went to obscure relatives you had nothing to do with. I like to have the succession pass from brother to brother, then to the eldest brother's sons in order, and so on. For example, I used to like playing as Denmark and playing through all of Svend's sons (he about 15) in order, until the youngest died. Does this form of Seniority exist? Click to expand...
<!-- artifact:quote:end -->
That doesn't exist, no. However, it's worth noting that the House Seniority law only passes your realm within your house. That should get far less unwieldy than in CK2, since your house tends to stay smaller as branches split off as cadet houses.

## Reply 101 — participant_016 · 2020-09-05 · post-26870416

<!-- artifact:quote:start -->
> Meneth said: We're looking into an issue like that. Click to expand...
<!-- artifact:quote:end -->
Its very surprising that we cant see who is next in line as Dynasty Head and how its decided. Effectively it acts as a title. Some clarity in the tooltip would be appreciated. Edit: I take that part back I just cant read.

## Reply 102 — participant_057 · 2020-09-05 · post-26870559

Thank you, I am very satisfied with CK3. I was especially happy when I discovered the rather original coat of arms of Jüterbog. Therefore I would like to make a cheeky but historically relevant suggestion: Please put in the starting year 1066 the dynasty Askanien ( Adalbert with sister Adelheid ) with county Wolkenstein and Vogtland to their true roots to Halberstadt and Blankenburg. The local family of the Brunonen with Ekbert at the head can live very well in Wolkenstein and Vogtland. The dynasty Askanien has its origin in the region of Aschersleben.

## Reply 103 — participant_055 · 2020-09-05 · post-26870633

<!-- artifact:quote:start -->
> Meneth said: That doesn't exist, no. However, it's worth noting that the House Seniority law only passes your realm within your house. That should get far less unwieldy than in CK2, since your house tends to stay smaller as branches split off as cadet houses. Click to expand...
<!-- artifact:quote:end -->
Thank you. If you could somehow patch in brother-to-brother succession at some point that would be great!

## Reply 104 — participant_058 · 2020-09-05 · post-26871627

There seems to be a problem with 1.0.3 and Ironman. Once you Resume (possibly also load) a game for the first time in 1.0.3, your game appears to revert to non-Ironman. I didn't notice until I exited the game and saw the Switch Character button and the icons next to the settings were grayed out -- no Ironman and no achievements. If anyone isn't getting achievements anymore, check that you're still Ironman. I'll probably have to start a new game as I doubt they'll fix saves to make them Ironman again.

## Reply 105 — participant_028 · 2020-09-05 · post-26872465

I am on a new 1.03 game and I just saw that my new vassal, who is the last of his dynasty and have no family, had a lowborn woman in his court be his heir without any relationship between them. I use the over title trick mentioned by the dev in this thread and it recalculated succession to me and that worked. The problem is that if I didn't do that, would that lowborn woman with no right to the tile inherit it and become my vassal? If yes, that might be part of the reason why the world have a tendency in some game to end up with a majority of landed noble who are woman, because all the men in your court die as knight and you wife, daughter or lowborn courtier, for the independent counts, end up as the heir, because there is no possible male heir still alive.

## Reply 106 — participant_059 · 2020-09-06 · post-26875347

succession is still broken. If you add a law on a title, this title will be exempt from the partition. For exemple you have 2 kingdoms title with partition with 2 sons, normally on death both son will inherit 1 kingdom and your kingdom will be split in 2 kingdoms. But if you add a Male only law on 1 title, this title with be exempt from the partition and your 1st son will inherit both kingdom titles. you can easily check this by playing west francia in 867 which have 2 kingdom titles and 2 sons with male only on one. I think it's how it's suppose to do with special law like feudal election, but this shouldn't do that when you have 2 son with male only.

## Reply 107 — participant_017 · 2020-09-06 · post-26876051

<!-- artifact:quote:start -->
> jkenna117 said: Please consider fixing religion in the next patch. Catholicism is almost ubplayable because of the way fervor and conversion work. It is currently way too prone to heresy and because fervor is always so low you can never convert any of your provinces. Unreformed pagans can convert you in like a year and it takes 20 for you to convert them. Also, please bring back missionaries or at least put pressure on unreformed pagan rulers to convert to Christianity or Islam based on their geographic location. Click to expand...
<!-- artifact:quote:end -->
I'm not suffering from that in my game, but it's still reasonably early, and I've been actively converting (Arpad start 867, converted to Catholic almost immediately) and expanding so that I'm now the Emperor of Carpathia. And that's even with repeated "Wicked Bishop" events firing for one particular Pope. My previous game as the pagan Hvitserks *did* tank Catholic fervour, but I was converting everything in sight, and a Lollard outbreak became established in France and spread.

## Reply 108 — participant_060 · 2020-09-06 · post-26876239

would be nice if you could make ironman saves better,in late game every 2 or so months my game freezes for 5 seconds and it's super annoying

## Reply 109 — participant_061 · 2020-09-07 · post-26881294

Can't quite find a clear answer anywhere. When is the whole Ruler/Dynasty Designer feature coming out? I booted up CK3 only to realize how much I miss it.

## Reply 110 — participant_009 · 2020-09-07 · post-26881390

<!-- artifact:quote:start -->
> Shadow86 said: When is the whole Ruler/Dynasty Designer feature coming out? Click to expand...
<!-- artifact:quote:end -->
the current official answer is "when it's ready".

## Reply 111 — participant_062 · 2020-09-07 · post-26882549

<!-- artifact:quote:start -->
> Meneth said: We're looking into an issue like that. Click to expand...
<!-- artifact:quote:end -->
If (or hopefully when) this bug gets fixed, will it fix itself in an already ongoing save? Like, will the game register that my current emperor is really supposed to be the house head? Or will I have to start a new game? That would really fucking suck

## Reply 112 — participant_063 · 2020-09-08 · post-26885477

Small questions to the dev. Is it worth is to report Historical mistakes as bugs or is it too much work at this point? (Like Centohl V of Béarn was not count of Bigorre in 1066, it was Bernat of Carcassonne son of the count of Foix) Are there any plan to be able to play some of the characters that are still there but became unlanded because of the merge of counties (like the Comminges Family who has been unsettled from the county by the count of Armagnac) edit: nm reported as bugs so if you have time you can decide what to do

## Reply 113 — participant_064 · 2020-09-08 · post-26887086

Realm authority does NOT apply to sub-vassals unlike CK2, so those sub-vassals are free to war against whoever they like.

## Reply 114 — participant_039 · 2020-09-09 · post-26888879

<!-- artifact:quote:start -->
> luis3007 said: Realm authority does NOT apply to sub-vassals unlike CK2, so those sub-vassals are free to war against whoever they like. Click to expand...
<!-- artifact:quote:end -->
Are you sure about this? I have never seen this happen. The only wars I have seen among sub-vassals are those that have to do with revolts and factions, but never anything that is declared the normal way.

## Reply 115 — participant_065 · 2020-09-11 · post-26901082

At this point, i take anything. To many things are bugged right now.

## Reply 116 — participant_066 · 2020-09-11 · post-26902119

<!-- artifact:quote:start -->
> Ares Enyalios said: At this point, i take anything. To many things are bugged right now. Click to expand...
<!-- artifact:quote:end -->
Same. In the meantime I am trying to stay productive by finishing other games in my backlog.

## Reply 117 — participant_067 · 2020-09-14 · post-26912578

So 11 days since the last patch, do we have some prediction of when the next one will be released?

## Reply 118 — participant_068 · 2020-09-14 · post-26912620

<!-- artifact:quote:start -->
> Qoff said: So 11 days since the last patch, do we have some prediction of when the next one will be released? Click to expand...
<!-- artifact:quote:end -->
Hopefully this week. At least a small patch to fix some of the more critical bugs would be nice like the ones related to succession.

## Reply 119 — participant_003 · 2020-09-14 · post-26913110

<!-- artifact:quote:start -->
> Qoff said: So 11 days since the last patch, do we have some prediction of when the next one will be released? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Rancor26 said: Hopefully this week. At least a small patch to fix some of the more critical bugs would be nice like the ones related to succession. Click to expand...
<!-- artifact:quote:end -->
Probably after dev diaries resume in a few weeks. I think that's very optimistic. Would love to see something this week but I'm guessing they are waiting to do one large patch at the end of this month/early October.

## Reply 120 — participant_069 · 2020-09-14 · post-26913203

I'd love something like beta 1.04 patch. Let it has some issues, but fix others.

## Reply 121 — participant_070 · 2020-09-14 · post-26913438

<!-- artifact:quote:start -->
> GeorgieBest said: Probably after dev diaries resume in a few weeks. I think that's very optimistic. Would love to see something this week but I'm guessing they are waiting to do one large patch at the end of this month/early October. Click to expand...
<!-- artifact:quote:end -->
Ya, there are some pretty critical bugs going on that need to be fixed asap. I don't think waiting that long to fix these bugs is really a good idea. Why wait until October when your game is currently experiencing it's peak number of players right now? By October the playerbase will have probably fallen off by a decent amount, and the bugs may have potentially left a negative last impression on people. This is personally the case for me. After sinking dozens of hours into my game, I experienced the matrilineal marriage bug, which absolutely killed any desire I had to continue playing. I haven't touched the game since, and don't plan to until the game gets patched. The game needs at least a small hotfix patch for the most critical bugs.

## Reply 122 — participant_039 · 2020-09-14 · post-26913460

<!-- artifact:quote:start -->
> GeorgieBest said: Probably after dev diaries resume in a few weeks. Click to expand...
<!-- artifact:quote:end -->
Ah, have they given a date yet?

## Reply 123 — participant_071 · 2020-09-15 · post-26913680

<!-- artifact:quote:start -->
> M426 said: Ya, there are some pretty critical bugs going on that need to be fixed asap. I don't think waiting that long to fix these bugs is really a good idea. Why wait until October when your game is currently experiencing it's peak number of players right now? By October the playerbase will have probably fallen off by a decent amount, and the bugs may have potentially left a negative last impression on people. This is personally the case for me. After sinking dozens of hours into my game, I experienced the matrilineal marriage bug, which absolutely killed any desire I had to continue playing. I haven't touched the game since, and don't plan to until the game gets patched. The game needs at least a small hotfix patch for the most critical bugs. Click to expand...
<!-- artifact:quote:end -->
Yeah I don't like this "wait until we have a big patch" thing. They've been promising several fixes and at least one addition (ruler designer) since before the game launched. Let alone all the bugs and mechanic problems that have been reported since then. They should be releasing hotfixes every few days, if not daily, since launch.

## Reply 124 — participant_003 · 2020-09-15 · post-26913850

<!-- artifact:quote:start -->
> CensorshipIsEvil said: Yeah I don't like this "wait until we have a big patch" thing. They've been promising several fixes and at least one addition (ruler designer) since before the game launched. Let alone all the bugs and mechanic problems that have been reported since then. They should be releasing hotfixes every few days, if not daily, since launch. Click to expand...
<!-- artifact:quote:end -->
I think it's a bit much to expect patches that frequently. Although I am surprised we aren't getting weekly updates. If they do wait till October that will be nearly a month without any bug fixes.

## Reply 125 — participant_072 · 2020-09-16 · post-26918335

<!-- artifact:quote:start -->
> GeorgieBest said: I think it's a bit much to expect patches that frequently. Although I am surprised we aren't getting weekly updates. If they do wait till October that will be nearly a month without any bug fixes. Click to expand...
<!-- artifact:quote:end -->
Considering the sorry state of the AI right now surrounding the building issue, it needed a hotfix on day 1. We're now 2 weeks post launch and I'd argue that the game is still not playable. It's not fun when you autowin every war because the AI hasn't built anything the past 50 years.

## Reply 126 — participant_069 · 2020-09-16 · post-26918860

It's a shame that we have to rely on mods to fix basic stuff (not introduce depth, this is what mods are for). What's even worse - bugs in the codebase do not allow modders to fix everything (example with matrilineal marriage). Paradox, just release beta 1.04. Let it be untested. Let it have some bugs. At least it will be new bugs and old ones will be fixed.

## Reply 127 — participant_065 · 2020-09-16 · post-26920839

It's really about time. 2 Weeks are definitly not okey for a major release that is extremly unbalanced. I honestly stoped playing like a week ago. It's just annoying.

## Reply 128 — participant_003 · 2020-09-16 · post-26920967

<!-- artifact:quote:start -->
> Ares Enyalios said: It's really about time. 2 Weeks are definitly not okey for a major release that is extremly unbalanced. I honestly stoped playing like a week ago. It's just annoying. Click to expand...
<!-- artifact:quote:end -->
Don't think we'll see a patch till October.

## Reply 129 — participant_039 · 2020-09-16 · post-26921147

<!-- artifact:quote:start -->
> GeorgieBest said: Don't think we'll see a patch till October. Click to expand...
<!-- artifact:quote:end -->
Is this based on something from Paradox or more of a feeling you have?

## Reply 130 — participant_073 · 2020-09-16 · post-26921213

<!-- artifact:quote:start -->
> GeorgieBest said: Don't think we'll see a patch till October. Click to expand...
<!-- artifact:quote:end -->
I hope not, since I've stopped playing the game until they at least fix the "starting as [x]" achievements not firing.

## Reply 131 — participant_009 · 2020-09-16 · post-26921304

<!-- artifact:quote:start -->
> CensorshipIsEvil said: They should be releasing hotfixes every few days, if not daily, since launch. Click to expand...
<!-- artifact:quote:end -->
No, they shouldn't. I can absolutely get behind pushing them as opt-in public betas that often, for sure, but not as releases.

## Reply 132 — participant_074 · 2020-09-16 · post-26921524

<!-- artifact:quote:start -->
> Meneth said: Yeah. Be aware that Dynasty Head succession is separate from House Head though. The Dynasty Head is the strongest House Head, and can take up to a year to update. Click to expand...
<!-- artifact:quote:end -->
Can you please define "strongest"? I am king of Tutorial Ireland, cultural head, head of the original house, won 3 crusades and placed 3 relatives on the thrones of Jerusalem, Catholic France (3 formerly heretic counties) and Galicia. Now the dynasty head is the sultan (lol) of Jerusalem.l, from a cadet branch. So... Does it look for personal/realm counties? Personal/realm army strength? Prestige? Stats?

## Reply 133 — participant_066 · 2020-09-17 · post-26921728

<!-- artifact:quote:start -->
> Cocco81 said: Can you please define "strongest"? I am king of Tutorial Ireland, cultural head, head of the original house, won 3 crusades and placed 3 relatives on the thrones of Jerusalem, Catholic France (3 formerly heretic counties) and Galicia. Now the dynasty head is the sultan (lol) of Jerusalem.l, from a cadet branch. So... Does it look for personal/realm counties? Personal/realm army strength? Prestige? Stats? Click to expand...
<!-- artifact:quote:end -->
From the wiki: "The most powerful House Head of a Dynasty (as determined by military strength) will always become the Dynasty Head upon the death of the current one. "

## Reply 134 — participant_074 · 2020-09-17 · post-26921785

<!-- artifact:quote:start -->
> MunkyII said: From the wiki: "The most powerful House Head of a Dynasty (as determined by military strength) will always become the Dynasty Head upon the death of the current one. " Click to expand...
<!-- artifact:quote:end -->
But is it my personal military strength, or my realm's, including vassals? Does it count soldiers number, or also quality and type?

## Reply 135 — participant_059 · 2020-09-17 · post-26924655

I think we need a patch for at least fixing the gender law on partition bug. This is a breaking bug and the AI is just abusing it like hell

## Reply 136 — participant_039 · 2020-09-17 · post-26924670

<!-- artifact:quote:start -->
> gekj said: I think we need a patch for at least fixing the gender law on partition bug. This is a breaking bug and the AI is just abusing it like hell Click to expand...
<!-- artifact:quote:end -->
I find it hilarious. Like, there is an unintended bug and the AI is actively exploiting it. How the heck did that even come to pass? Don't get me wrong, I also agree that it needs to be fixed ASAP. I just find it odd that the AI is actively exploiting it on the scale it is. Skynet is nigh, friends.

## Reply 137 — participant_027 · 2020-09-18 · post-26926248

can we get a next patch please?

## Reply 138 — participant_075 · 2020-09-18 · post-26926871

<!-- artifact:quote:start -->
> Monkbel said: can we get a next patch please? Click to expand...
<!-- artifact:quote:end -->
Yes it's time.

## Reply 139 — participant_003 · 2020-09-18 · post-26926987

Another week without a patch...

## Reply 140 — participant_076 · 2020-09-18 · post-26927032

There are a lot of mistakes in the game, and you still need to test everything. I don't expect until October.

## Reply 141 — participant_074 · 2020-09-18 · post-26927103

<!-- artifact:quote:start -->
> MunkyII said: From the wiki: "The most powerful House Head of a Dynasty (as determined by military strength) will always become the Dynasty Head upon the death of the current one. " Click to expand...
<!-- artifact:quote:end -->
Update for you and @Meneth : Dynasty head switches upon death of current head between me and the sultan (lol) of jerusalem. I died, he became DH. He died, I became DH. Has been doing so at least 3 or 4 times in a row now. Note: my character and the sultan are both heads of their respective houses. Is this a bug or working as designed?

## Reply 142 — participant_075 · 2020-09-18 · post-26927153

<!-- artifact:quote:start -->
> GeorgieBest said: Another week without a patch... Click to expand...
<!-- artifact:quote:end -->
It's a shame that even there is no little fix.. Time for a shame walk.

## Reply 143 — participant_073 · 2020-09-18 · post-26928043

Do Paradox ever release patches on a Friday? Kinda sad I won't get to CK3 this weekend.

## Reply 144 — participant_066 · 2020-09-18 · post-26928569

My guess is that next patch comes out the 22nd with the multiplayer fix.

## Reply 145 — participant_039 · 2020-09-18 · post-26929497

<!-- artifact:quote:start -->
> MunkyII said: My guess is that next patch comes out the 22nd with the multiplayer fix. Click to expand...
<!-- artifact:quote:end -->
Nice "guess."

## Reply 146 — participant_003 · 2020-09-20 · post-26935081

<!-- artifact:quote:start -->
> MunkyII said: My guess is that next patch comes out the 22nd with the multiplayer fix. Click to expand...
<!-- artifact:quote:end -->
Nah. If they are giving us a week warning for turning the multiplayer servers off and on again, they'll definitely give us a week warning before the first patch. We probably won't see a patch till early October.

## Reply 147 — participant_070 · 2020-09-21 · post-26935908

<!-- artifact:quote:start -->
> GeorgieBest said: Nah. If they are giving us a week warning for turning the multiplayer servers off and on again, they'll definitely give us a week warning before the first patch. We probably won't see a patch till early October. Click to expand...
<!-- artifact:quote:end -->
They're giving us a warning for multiplayer because they're going to bring the servers down temporarily. That isn't the case for patches. That being said, I am not keeping my hopes up that we'll get a patch next week. They'll probably wait for dev diaries to "tease" with what's upcoming in the next patch. Though nobody really wants a teaser at this point though, we literally just want a bug fix patch so we can just play the game in a reasonable state.

## Reply 148 — participant_075 · 2020-09-21 · post-26936204

<!-- artifact:quote:start -->
> M426 said: They'll probably wait for dev diaries to "tease" with what's upcoming in the next patch. Though nobody really wants a teaser at this point though, we literally just want a bug fix patch so we can just play the game in a reasonable state. Click to expand...
<!-- artifact:quote:end -->
So God damn true. Need 32 mods right now that the most annoying KI decisions, Bugs and those empty spaces got filled (events for example) Still don't get it why you cant have battle events or decisions. Didn't paradox wanted to make more options in battle via events, not less? And why isn't there some duel options any more? A big big Patch hopefully will put things right and hopefully it will come soon. Always thought after a release most people have more workshedule because they want a smooth experience for the fanbase.

## Reply 149 — participant_077 · 2020-09-21 · post-26938702

<!-- artifact:quote:start -->
> GeorgieBest said: Nah. If they are giving us a week warning for turning the multiplayer servers off and on again, they'll definitely give us a week warning before the first patch. We probably won't see a patch till early October. Click to expand...
<!-- artifact:quote:end -->
Serious bugs only get fixed together with the next DLC, it is how it has always been. Paradox games are always a fun broken mess until they have been fixed by the patches for the first couple of DLCs, and then later DLC will slowly break the game again

## Reply 150 — participant_039 · 2020-09-21 · post-26938716

<!-- artifact:quote:start -->
> Carewolf2 said: Serious bugs only get fixed together with the next DLC, it is how it has always been. Paradox games are always a fun broken mess until they have been fixed by the patches for the first couple of DLCs, and then later DLC will slowly break the game again Click to expand...
<!-- artifact:quote:end -->
This sounds like a metaphor for Hegelian dialectics.

## Reply 151 — participant_066 · 2020-09-22 · post-26942426

<!-- artifact:quote:start -->
> MunkyII said: My guess is that next patch comes out the 22nd with the multiplayer fix. Click to expand...
<!-- artifact:quote:end -->
Oh you sweet summer child....

## Reply 152 — participant_078 · 2020-09-23 · post-26944253

They said they would come with some news first before releasing the patch. So as long as there's radio silence, there's little hope that the patch will come soon, sadly.

## Reply 153 — participant_079 · 2020-09-23 · post-26945254

<!-- artifact:quote:start -->
> JtW said: They said they would come with some news first before releasing the patch. So as long as there's radio silence, there's little hope that the patch will come soon, sadly. Click to expand...
<!-- artifact:quote:end -->
Should be hearing about it shortly, apparently...

## Reply 154 — participant_078 · 2020-09-23 · post-26945959

<!-- artifact:quote:start -->
> Colonel Bogey said: Should be hearing about it shortly, apparently... Click to expand...
<!-- artifact:quote:end -->
Yeah, I've seen. Next week, is it?

## Reply 155 — participant_079 · 2020-09-23 · post-26946170

<!-- artifact:quote:start -->
> JtW said: Yeah, I've seen. Next week, is it? Click to expand...
<!-- artifact:quote:end -->
Annoyingly it was in a live stream rather than here. Patch expected next week (date unconfirmed).

## Reply 156 — participant_079 · 2020-09-23 · post-26946174

Actually I think I read your message wrong and simply agreed with you. Lol.

## Reply 157 — participant_078 · 2020-09-23 · post-26946310

<!-- artifact:quote:start -->
> Colonel Bogey said: Actually I think I read your message wrong and simply agreed with you. Lol. Click to expand...
<!-- artifact:quote:end -->
Yeah, I didn't watch the stream but I saw this: https://forum.paradoxplaza.com/forum/threads/can-you-guys-like-patch-the-game.1425985/post-26945551

## Reply 158 — participant_075 · 2020-09-28 · post-26960688

Paradox the "next Week" is here so how will it be? Some more teasing in the Forum, or maybe a Dev Diary, or maybe release it with the changelog?

## Reply 159 — participant_080 · 2020-09-28 · post-26961207

Lol!! Stop commenting on this post!!! Everytime I log on I see Patch 1.0.3. Out now! And forget what version we are on and get super excited thinking it's a new patch

## Reply 160 — participant_039 · 2020-09-28 · post-26961916

Enjoy.

## Reply 161 — participant_081 · 2020-09-28 · post-26962284

was the game finished? I played for 27 hours. Tutorial? okay. simple and not covering everything, but it's paradox game so i didn't expect anything. 3-4 hours not very fun but okay i got the game feel, i like it. I hope i won't have the same shit as in CK2 with the vassal micro management of their number.... fingers cross. First game (ironman)? after an manager kill because i made a stupid decision... corrupt save => ok do not use kill task in that game, got it. Still lose 6 hours of play. Second game ironman? I had to quit the game and the save got corrupt... okay bad luck. 7 hours lost. Third game ironman? Vassal number > 40 => give away vassals randomly. As in CK2 not easy, not intuitive, and boring. But at least in CK2 it wasn't bugged. Now? number of vassals do not update. Leave the game and restart to fix? CTD. Probably corrupt save. 10 hours lost. FIX your game. What is this paradox? are we paying to test your products?

## Reply 162 — participant_013 · 2020-09-28 · post-26962378

<!-- artifact:quote:start -->
> AngelRay said: was the game finished? I played for 27 hours. Tutorial? okay. simple and not covering everything, but it's paradox game so i didn't expect anything. 3-4 hours not very fun but okay i got the game feel, i like it. I hope i won't have the same shit as in CK2 with the vassal micro management of their number.... fingers cross. First game (ironman)? after an manager kill because i made a stupid decision... corrupt save => ok do not use kill task in that game, got it. Still lose 6 hours of play. Second game ironman? I had to quit the game and the save got corrupt... okay bad luck. 7 hours lost. Third game ironman? Vassal number > 40 => give away vassals randomly. As in CK2 not easy, not intuitive, and boring. But at least in CK2 it wasn't bugged. Now? number of vassals do not update. Leave the game and restart to fix? CTD. Probably corrupt save. 10 hours lost. FIX your game. What is this paradox? are we paying to test your products? Click to expand...
<!-- artifact:quote:end -->
I played for around 100 hours & had a good time, though got abit boring in the later years. My problems were all balance issues, poor UI, & lack of info. Never had any crashes. One thing. Are you saving to cloud? I have used Ironman throughout with no problems, & saved to hard drive. Many people have had problems saving to cloud from Ironman.

## Reply 163 — participant_082 · 2020-09-29 · post-26965844

Time to let this thread go I think!

