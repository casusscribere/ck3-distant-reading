---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1518991/"
forum_thread_id: 1518991
content_type: reply_thread
parent_dd_file: dd_092_2022-04-05_dev-diary-92-anatomy-of-a-game-from-repo.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 92
title: "CK3 Dev Diary #92: Anatomy of a Game: From Report to Resolution"
dd_date: 2022-04-05
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 3
reply_count: 52
participant_count: 37
reply_date_first: 2022-04-05
reply_date_last: 2022-04-18
body_word_count: 3473
inline_image_count: 0
quoted_span_count: 35
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — CK3 Dev Diary #92: Anatomy of a Game: From Report to Resolution

*52 replies from 37 participants across 3 pages*

## Reply 1 — participant_001 · 2022-04-05 · post-28194313

To be honest, I prefer reporting bugs directly to Discord with a quick text and screenshot of the bug rather than filling the form on the forum. I've found too many bugs and yet I am too lazy to open threads for each one of them. I would gladly report it through discord tho.

## Reply 2 — participant_002 · 2022-04-05 · post-28194324

The bug report thread would be much more streamlined if the search function wasn't as messy to use. But this is a pretty cool post overall.

## Reply 3 — participant_003 · 2022-04-05 · post-28194349

Great stuff ! Love to sneak peaks backstage. Question about the bug report forum: there are long periods of time (sometimes months) when bug reports aren't flagged, which always leaves users wondering whether they are being parsed at all, and if it's even worth reporting more bugs. Any reason for this, and should we keep reporting? Bonus question: what's the proper etiquette when QA flags a bug report As Designed, and you're pretty sure it's not so? A report I have in mind was about a Varangian Adventure war after which the character that used the CB kept one of its initial holdings - which from what everything the game says about that CB, shouldn't happen. CK III - Keeping an old county when ending a Varangian Adventure Short summary of your issue Keeping an old county when ending a Varangian Adventure Game Version 1.3.1 What OS are you playing on? Windows What platform are you using? Steam Do you have mods enabled? No Have you tried... forum.paradoxplaza.com And yet another one: there are instances where reports are flagged As Designed, but where there's likely a flaw in the design itself. If it's flagged As Designed, it'll likely never be looked at further. What's the proper way to report those? On one such report, it was suggested I post it in Suggestions, but we have no idea what's your process in handling those, and there's no feedback at all (which doesn't really encourage using them).

## Reply 4 — participant_004 · 2022-04-05 · post-28194357

Interesting thread. Thanks for explaining the process of the bug report.

## Reply 5 — participant_005 · 2022-04-05 · post-28194362

Hello, could you fix the banner editor in russian localization? Problem is that when editing any figures, the sliders go off the screen. I really love the game, soon I will get all the achievements!

## Reply 6 — participant_006 · 2022-04-05 · post-28194366

Paradox uses GitLab it looks like. We do too. Cool to see it at a big company.

## Reply 7 — participant_007 · 2022-04-05 · post-28194383

You don't estimate on Jira. I see you're a man of culture as well.

## Reply 8 — participant_008 · 2022-04-05 · post-28194400

Nice insight into your dev process. Are you using capital letters for both classes and methods? .NET background?

## Reply 9 — participant_009 · 2022-04-05 · post-28194434

<!-- artifact:quote:start -->
> JaJe said: To be honest, I prefer reporting bugs directly to Discord with a quick text and screenshot of the bug rather than filling the form on the forum. I've found too many bugs and yet I am too lazy to open threads for each one of them. I would gladly report it through discord tho. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Chatoustikmou said: Question about the bug report forum: there are long periods of time (sometimes months) when bug reports aren't flagged, which always leaves users wondering whether they are being parsed at all, and if it's even worth reporting more bugs. Any reason for this, and should we keep reporting? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Chatoustikmou said: Bonus question: what's the proper etiquette when QA flags a bug report As Designed, and you're pretty sure it's not so? A report I have in mind was about a Varangian Adventure war after which the character that used the CB kept one of its initial holdings - which from what everything the game says about that CB, shouldn't happen. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Grzegorz Grzybek said: Are you using capital letters for both classes and methods? .NET background? Click to expand...
<!-- artifact:quote:end -->
I disagree, simply because Discord is a realtime medium of communication and ill suited for going back to see and respond to archived topics. Due to the short message nature of Discord, it's also hard to get proper details about something if there are also other ongoing discussions within the same channel at the same time. The forum is much better suited for this. I cannot really say much in regards to the bug reporting forum, as I grab my tickets from *shudder* Jira, but absolutely keep reporting. If you cannot find a thread with what you're experiencing, make a thread for it! We have an internal document that is regularly updated with top issues from the community, and these do affect which tasks I select from Jira when I go searching for tasks to do. Personally I think raising the question again within the thread, and reiterate upon the steps required to produce the outcome that you believe is faulty and what you believe should be the desired outcome. Some times this all falls down to a misunderstanding or miscommunication somewhere in the chain. I don't know the background of it for PDS, but I'm quite an enthusiast when it comes to clear and consise standards for writing code within an organization

## Reply 10 — participant_010 · 2022-04-05 · post-28194436

Very insightful DD. It can definitely be frustratring when bugs we report seem to be ignored, but this reveals that sometimes the process is a bit more complicated than it intially seems.

## Reply 11 — participant_011 · 2022-04-05 · post-28194558

Could you PLEASE post this in the HOI4 forum too?

## Reply 12 — participant_012 · 2022-04-05 · post-28194569

<!-- artifact:quote:start -->
> PDXOxycoon said: Personally I think raising the question again within the thread, and reiterate upon the steps required to produce the outcome that you believe is faulty and what you believe should be the desired outcome. Some times this all falls down to a misunderstanding or miscommunication somewhere in the chain. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Chatoustikmou said: And yet another one: there are instances where reports are flagged As Designed, but where there's likely a flaw in the design itself. If it's flagged As Designed, it'll likely never be looked at further. What's the proper way to report those? On one such report, it was suggested I post it in Suggestions, but we have no idea what's your process in handling those, and there's no feedback at all (which doesn't really encourage using them). Click to expand...
<!-- artifact:quote:end -->
Slight problem with this is that threads marked 'As Designed' are usually locked immediately? Which in these cases can just be a bit frustrating? I'll use an example of my own: CK III - Can no longer right-click characters on the character select screen Short summary of your issue Can no longer right-click characters on the character select screen Game Version 1.5.0 What OS are you playing on? Windows What platform are you using? Steam What DLC do you have installed? Royal... forum.paradoxplaza.com With the Royal Court patch, the ability to rightclick counties on the character select screen to view their lord's education traits and skill points at a glance was outright removed, but you can still see it by using the character finder, which just feels like an awkward workaround to a problem that never existed. In this case, it appears that characters were never meant to be able to be rightclicked in the character select screen, although I can see no benefit to them not being able to and having this feature removed, but I couldn't argue my case because the thread was closed immediately. Would appreciate some insight on this. Just adding an addendum that this dev diary was pretty much exactly what I've been looking for in terms of "Dev Diaries When Content Updates Are Otherwise Sparse", and while it's not as layman-friendly as the Outer Worlds devs explaining how they fixed a pervasive bug (https://www.polygon.com/2019/12/13/...s-companion-bug-dead-qa-taylor-swope-obsidian) (really great read by the way for game devs and non-devs alike), I'm happy with the direction transparency is going in.

## Reply 13 — participant_013 · 2022-04-05 · post-28194629

<!-- artifact:quote:start -->
> Chatoustikmou said: Great stuff ! Love to sneak peaks backstage. Question about the bug report forum: there are long periods of time (sometimes months) when bug reports aren't flagged, which always leaves users wondering whether they are being parsed at all, and if it's even worth reporting more bugs. Any reason for this, and should we keep reporting? Bonus question: what's the proper etiquette when QA flags a bug report As Designed, and you're pretty sure it's not so? A report I have in mind was about a Varangian Adventure war after which the character that used the CB kept one of its initial holdings - which from what everything the game says about that CB, shouldn't happen. CK III - Keeping an old county when ending a Varangian Adventure Short summary of your issue Keeping an old county when ending a Varangian Adventure Game Version 1.3.1 What OS are you playing on? Windows What platform are you using? Steam Do you have mods enabled? No Have you tried... forum.paradoxplaza.com And yet another one: there are instances where reports are flagged As Designed, but where there's likely a flaw in the design itself. If it's flagged As Designed, it'll likely never be looked at further. What's the proper way to report those? On one such report, it was suggested I post it in Suggestions, but we have no idea what's your process in handling those, and there's no feedback at all (which doesn't really encourage using them). Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> MaxMon said: Hello, could you fix the banner editor in russian localization? Problem is that when editing any figures, the sliders go off the screen. I really love the game, soon I will get all the achievements! Click to expand...
<!-- artifact:quote:end -->
So while we'd love to have a permanent presence on the forum, currently we ensure that we do a lot of coverage around patches - that's when we usually have a huge influx of players eager to test out new content, which coincides with higher report rate on the forum. In the past we used to be able to do it more regularly, but because our process is becoming more and more complex, our workflows complicated and QA is now involved in almost all parts of development like a helix, we have less time to do it ourselves. But that doesn't mean we don't do it - we simply concentrate efforts to go through current and some of the backlog. If you are very particular about certain bugs and you'd like them desperately fixed, you can help us locate and see them by upvoting threads with bugs you are very interested in. Usually each release in subsequent weeks we pick out top upvoted issues from the past week or two, select a few pages of them and make sure all of them are fixed. I'm pretty sure we fixed this one. Heavens, is it broken again?

## Reply 14 — participant_013 · 2022-04-05 · post-28194635

<!-- artifact:quote:start -->
> NATOaster said: Slight problem with this is that threads marked 'As Designed' are usually locked immediately? Click to expand...
<!-- artifact:quote:end -->
That shouldn't be the case, but if it is - feel free to report these to the respective QA who have locked the thread to keep them unlocked. We try to keep the conversation flowing, and sometimes it's not the QA is speaking, but we simply are the extensions of our internal dev team answering questions for you. Please don't be getting mad at us! (Also, I unlocked your thread )

## Reply 15 — participant_014 · 2022-04-05 · post-28194909

<!-- artifact:quote:start -->
> jakeowaty said: If you are very particular about certain bugs and you'd like them desperately fixed, you can help us locate and see them by upvoting threads with bugs you are very interested in. Usually each release in subsequent weeks we pick out top upvoted issues from the past week or two, select a few pages of them and make sure all of them are fixed. Click to expand...
<!-- artifact:quote:end -->
I certainly didn't realize that upvoting bug reports was a worthwhile activity, and, based on the fact that most bug reports get 0-2 votes, I suspect most other users didn't either. It feels like the main determiner of the number of votes a bug report gets is whether or not it is linked to in a thread in the main forum, not the severity or frequency with which players encounter it.

## Reply 16 — participant_012 · 2022-04-05 · post-28194948

<!-- artifact:quote:start -->
> Tiax said: I certainly didn't realize that upvoting bug reports was a worthwhile activity, and, based on the fact that most bug reports get 0-2 votes, I suspect most other users didn't either. It feels like the main determiner of the number of votes a bug report gets is whether or not it is linked to in a thread in the main forum, not the severity or frequency with which players encounter it. Click to expand...
<!-- artifact:quote:end -->
Yeah I usually just determine whether a bug has been noted (or the likelihood of this) by whether or not it has a dev response.

## Reply 17 — participant_015 · 2022-04-05 · post-28195064

With all due respect, this DD, with the Spanish translation still a mess more than a year later, is, to say the least, shocking.

## Reply 18 — participant_016 · 2022-04-05 · post-28195139

<!-- artifact:quote:start -->
> Ketzerian said: With all due respect, this DD, with the Spanish translation still a mess more than a year later, is, to say the least, shocking. Click to expand...
<!-- artifact:quote:end -->
You mean you didn't expect a kind of Spanish inept-translation?

## Reply 19 — participant_017 · 2022-04-05 · post-28195198

Interesting dev diary, thanks!

## Reply 20 — participant_018 · 2022-04-05 · post-28195351

<!-- artifact:quote:start -->
> Tiax said: I certainly didn't realize that upvoting bug reports was a worthwhile activity, and, based on the fact that most bug reports get 0-2 votes, I suspect most other users didn't either. Click to expand...
<!-- artifact:quote:end -->
While I agree, I also get the impression that many users don't know that upvoting is a thing, or how to do it. It can be very easy to not see any mention of it at times. IIRC, it took several months after I first joined the forums to read any mention of it.

## Reply 21 — participant_019 · 2022-04-06 · post-28195508

<!-- artifact:quote:start -->
> Mcgan said: While I agree, I also get the impression that many users don't know that upvoting is a thing, or how to do it. Click to expand...
<!-- artifact:quote:end -->
Perfectly true. And it's precisely you who taught me about this feature !

## Reply 22 — participant_020 · 2022-04-06 · post-28195528

<!-- artifact:quote:start -->
> jakeowaty said: (Editor's note: Can I mention the raw onion story?) Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Ketzerian said: With all due respect, this DD, with the Spanish translation still a mess more than a year later, is, to say the least, shocking. Click to expand...
<!-- artifact:quote:end -->
Yes, please! You can't pique our curiosity like that and leave us hanging! More seriously, this is interesting (and probably a response to people shouting "hey, do they not test their game at all?")… Like this, actually: Is it, though? The described process with several steps is awfully likely to have things fall between wheels.

## Reply 23 — participant_021 · 2022-04-06 · post-28195642

I hope CK3 gets a Custodian Team eventually like Stellaris has.

## Reply 24 — participant_009 · 2022-04-06 · post-28195859

<!-- artifact:quote:start -->
> Viridianus said: Yes, please! You can't pique our curiosity like that and leave us hanging! Click to expand...
<!-- artifact:quote:end -->
No... we don't need to elaborate on the onion story... it's cursed...

## Reply 25 — participant_009 · 2022-04-06 · post-28195872

<!-- artifact:quote:start -->
> Viridianus said: Is it, though? The described process with several steps is awfully likely to have things fall between wheels. Click to expand...
<!-- artifact:quote:end -->
Sad to say, even with such an involved process there are times when something falls between and some times those are very unforeseen. Most notably for that particular topic is the Spanish Culture Tradition translations between 1.5.0.x and 1.5.1.x. As could be seen in the images and deduced by astute readers, we use Git as our version control system through GitLabs and somewhere in the merges between 1.5.0.x and 1.5.1.0, the fix to the Spanish translations were reverted through a merge. That is to say: a merge was resolved to not include those fixes. Git does most of these resolutions on its own, and when a merge has thousands upon thousands of changes, it is logistically impossible to look at all the changes when merging two branches. I have no idea how, but the result was evident: 1.5.1 lacked the Spanish translations we resolved for 1.5.0.x.

## Reply 26 — participant_022 · 2022-04-06 · post-28196090

I have posted the following suggestion a few times over on EU4 forums but apparently it's never been noticed: What makes using the bug report forum frustrating for the standard bug reporter is that there is hardly any feedback on wether a bug report has been resolved or even been noticed. Since you make good use of Jira maybe you could have a forum bot do this job. If a report leeds to a Jira task make an automated response that it has been assigned - and one when it is resolved or merged. This has the added benefit, that when we're talking about a specific bug anywhere or accidentally re-report a known bug we could simply point to the appropriate ticket.

## Reply 27 — participant_009 · 2022-04-06 · post-28196119

<!-- artifact:quote:start -->
> Spartakus said: What makes using the bug report forum frustrating for the standard bug reporter is that there is hardly any feedback on wether a bug report has been resolved or even been noticed. Since you make good use of Jira maybe you could have a forum bot do this job. If a report leeds to a Jira task make an automated response that it has been assigned - and one when it is resolved or merged. Click to expand...
<!-- artifact:quote:end -->
I gave this some thought myself as to why we don't have a established routine of responding to threads when a bug gets closed internally, and I came to the conclusion that we probably don't want the top of the forum to be cluttered with issues we've resolved, as that will take the space of other, unresolved threads that people may want to vote upon. This is my own conclusion though. Maybe something else to be able to note threads as resolved internally without bringing the thread to the front. Another consideration is that a fix may be reverted before the update is released, and we cannot really commit to having a fix finalized until it's actually in a release build. This happened to a reported AI bug where the AI would have weird objectives assigned to the war coordinator. We fixed that bug to go into 1.5.0, however testing revealed some side effects of that fix were deemed so undesirable in comparison that this particular fix itself was reverted. This was then later fixed together with the AI improvements in 1.5.1 instead, where we had more time to test and iterate upon the improvements. QA was especially helpful in this regard. Fabian, whom you may know from the Crusader Kings 3 Weekly streams (check them out on www.twitch.tv/paradoxinteractive Wednesdays at 14:30 CEST), sat for hours watching the game play itself and wage war to make sure none of the improvements made had any undesirable side effects before it was committed into 1.5.1. I don't really know a good solution on clear and concise streams of communication on resolved issues before the patch notes hits the press.

## Reply 28 — participant_015 · 2022-04-06 · post-28196367

<!-- artifact:quote:start -->
> newtlord said: You mean you didn't expect a kind of Spanish inept-translation? Click to expand...
<!-- artifact:quote:end -->
The truth is that I am not surprised that the translation is not perfect. But the mediocre level of this game with respect to translation has irritated me to no end. There are bugs of important information for the player that in Spanish doesn't even appear. It's not that it's badly translated, it's that it doesn't even come out. I can understand if I make an effort that it doesn't come out at the beginning, but months later it's still the same, it's unacceptable. I wonder what they would think if Spanish speakers paid with invalid money.

## Reply 29 — participant_015 · 2022-04-06 · post-28196370

<!-- artifact:quote:start -->
> PDXOxycoon said: Sad to say, even with such an involved process there are times when something falls between and some times those are very unforeseen. Most notably for that particular topic is the Spanish Culture Tradition translations between 1.5.0.x and 1.5.1.x. As could be seen in the images and deduced by astute readers, we use Git as our version control system through GitLabs and somewhere in the merges between 1.5.0.x and 1.5.1.0, the fix to the Spanish translations were reverted through a merge. That is to say: a merge was resolved to not include those fixes. Git does most of these resolutions on its own, and when a merge has thousands upon thousands of changes, it is logistically impossible to look at all the changes when merging two branches. I have no idea how, but the result was evident: 1.5.1 lacked the Spanish translations we resolved for 1.5.0.x. Click to expand...
<!-- artifact:quote:end -->
Yeah, but what about all the bugs (which I won't put here as they are perfectly reported in their space) that have been there since the beginning of the game? Is it also a GitLabs issue? I sincerely believe it's a lack of attention to detail. And as a buyer of all Paradox games for more than a decade, it's a shame to end up like this.

## Reply 30 — participant_023 · 2022-04-06 · post-28196445

<!-- artifact:quote:start -->
> PDXOxycoon said: This is my own conclusion though. Maybe something else to be able to note threads as resolved internally without bringing the thread to the front. Click to expand...
<!-- artifact:quote:end -->
i think just use something that already is here, like "As Designed" "Confirmed" "Duplicate" use "Resolved" "under review" "in progress" "more details needed"

## Reply 31 — participant_024 · 2022-04-06 · post-28196463

<!-- artifact:quote:start -->
> helveticadomes said: i think just use something that already is here, like "As Designed" "Confirmed" "Duplicate" use "Resolved" "under review" "in progress" "more details needed" Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Hey Trinexx. Could it be an option to create a type of reaction that only PDX and the community team has access to - a type of "we've read your ideas" type reaction. In this way you don't have to respond - which often takes a lot of time and energy. But it would at the same time show that you are present. Click to expand...
<!-- artifact:quote:end -->
Or what @Secuter suggested here: So some kind of ‘noted’ icon?

## Reply 32 — participant_025 · 2022-04-06 · post-28196662

I usualy find a lot of bugs around, specialy in HOI4, but filling the form in the forum is quite a pain...

## Reply 33 — participant_026 · 2022-04-06 · post-28197246

There is still no way to select PS5 or XBOX in the menu on which OS you are playing on in the topic creation bugs sub-forum, so there is no way to describe specific problems on the console versions.

## Reply 34 — participant_027 · 2022-04-07 · post-28197381

<!-- artifact:quote:start -->
> Tiax said: I certainly didn't realize that upvoting bug reports was a worthwhile activity, and, based on the fact that most bug reports get 0-2 votes, I suspect most other users didn't either. It feels like the main determiner of the number of votes a bug report gets is whether or not it is linked to in a thread in the main forum, not the severity or frequency with which players encounter it. Click to expand...
<!-- artifact:quote:end -->
It may correlate in a very roundabout way. The more people have the problem, the more likely it is to get linked to in the main forum. Though this is biased in favour of bugs that are exploitable, which is probably the reason why "Fun detected" is such a meme.

## Reply 35 — participant_028 · 2022-04-07 · post-28197506

"This issue was a side effect of letting Holy Orders raise themselves for Great Holy Wars:" Except that they don't. That's also a bug that hasn't been fixed XD. I love you paradox but you walked into that one.

## Reply 36 — participant_029 · 2022-04-07 · post-28197605

We always have to remember, it may be a game for us. But for you, it's work Boring except for those in the industry. Anyway, we know you work hard! Keep it up!

## Reply 37 — participant_009 · 2022-04-07 · post-28198341

<!-- artifact:quote:start -->
> jogzy123 said: Except that they don't. That's also a bug that hasn't been fixed XD. I love you paradox but you walked into that one. Click to expand...
<!-- artifact:quote:end -->
I cannot say I did, because Holy Orders will raise themselves in Great Holy Wars they're pledged to. My self-proclaimed QA Hobgoblin showed it to me just a moment ago. Maybe there are some other reasons to why they don't raise themselves for you, such as being otherwise occupied against heathens elsewhere?

## Reply 38 — participant_028 · 2022-04-07 · post-28198760

<!-- artifact:quote:start -->
> PDXOxycoon said: I cannot say I did, because Holy Orders will raise themselves in Great Holy Wars they're pledged to. My self-proclaimed QA Hobgoblin showed it to me just a moment ago. Maybe there are some other reasons to why they don't raise themselves for you, such as being otherwise occupied against heathens elsewhere? Click to expand...
<!-- artifact:quote:end -->
Really? That was a confirmed bug in the pre royal court patch, and I didn't see anything in the patch notes that indicated it had been fixed since. Hmmmm.... Interesting. I guess it's time for a crusade then!

## Reply 39 — participant_030 · 2022-04-07 · post-28198790

This is a sensible topic for a dev diary and some dev responses. Thank you!

## Reply 40 — participant_031 · 2022-04-10 · post-28203719

Insightful I guess but ultimately we don't need to see how the sausage is made and it only invites more criticism. Based on the comic alone I can criticize your methods but that's kind of unfair. It does however reveal that there's seemingly no vision for the game. Been there/felt that on software projects in the past so it's kind of recognizable. (bring on the red Xs)

## Reply 41 — participant_032 · 2022-04-10 · post-28204061

<!-- artifact:quote:start -->
> durbal said: Insightful I guess but ultimately we don't need to see how the sausage is made and it only invites more criticism. Click to expand...
<!-- artifact:quote:end -->
The whole "if you like sausage don't look at how it's made" line is fascinating because it's remarkably compelling, yet essentially wrong-headed.

## Reply 42 — participant_031 · 2022-04-10 · post-28204417

<!-- artifact:quote:start -->
> grommile said: The whole "if you like sausage don't look at how it's made" line is fascinating because it's remarkably compelling, yet essentially wrong-headed. Click to expand...
<!-- artifact:quote:end -->
That's not really what I said.

## Reply 43 — participant_033 · 2022-04-10 · post-28204819

Hungarian Notation? It looks like you stick with the same naming convention since EU2 times

## Reply 44 — participant_034 · 2022-04-11 · post-28205114

You appear to have a duplicate image in the dev blog. [Code controlling if a order’s armies should be disbanded] and [Code to check if a character can use the Holy Order] both link to image7.png, admittedly with different URLs. This doesn't quite seem to be intended, as the accompanying text for the latter references code which isn't present in the image.

## Reply 45 — participant_035 · 2022-04-11 · post-28205750

The lifetime of a bug, yes, that story is familiar. Good to know you devs have a good flow in place. Is there per chance, somewhere in the Jira backlog, any bug report to finally allow us, non-QWERTY keyboard owners, to play the game without making knots in our fingers? The very first tutorial is how to use the WASD keys and you've already lost me there. So I hope that there is something in the works for it, and that the priority has not been set too low. It wasn't released yesterday and the support forums have many pages of this problem.

## Reply 46 — participant_034 · 2022-04-11 · post-28205767

<!-- artifact:quote:start -->
> Redglyph said: Is there per chance, somewhere in the Jira backlog, any bug report to finally allow us, non-QWERTY keyboard owners, to play the game without making knots in our fingers? The very first tutorial is how to use the WASD keys and you've already lost me there. Click to expand...
<!-- artifact:quote:end -->
You can go into your "/game/gui/shortcuts.shortcuts" file and edit your keybindings as you wish. In fact, this is one of the few files in the game that are not changeable by mods, so you'll be free to edit this to your heart's content and no mods will be able to mess with it.

## Reply 47 — participant_035 · 2022-04-11 · post-28205818

<!-- artifact:quote:start -->
> Tobbzn said: You can go into your "/game/gui/shortcuts.shortcuts" file and edit your keybindings as you wish. In fact, this is one of the few files in the game that are not changeable by mods, so you'll be free to edit this to your heart's content and no mods will be able to mess with it. Click to expand...
<!-- artifact:quote:end -->
This file doesn't contain the shortcuts to pan the camera unfortunately, which are the biggest problem. From what I read, the game didn't like this file to be modified anyway, but even if that's not the case anymore, the question is moot. Thanks for helping though

## Reply 48 — participant_036 · 2022-04-11 · post-28205879

<!-- artifact:quote:start -->
> Tiax said: I certainly didn't realize that upvoting bug reports was a worthwhile activity, and, based on the fact that most bug reports get 0-2 votes, I suspect most other users didn't either. It feels like the main determiner of the number of votes a bug report gets is whether or not it is linked to in a thread in the main forum, not the severity or frequency with which players encounter it. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> NATOaster said: Yeah I usually just determine whether a bug has been noted (or the likelihood of this) by whether or not it has a dev response. Click to expand...
<!-- artifact:quote:end -->
We are reading the forums on a daily basis, and reporting as a standard of a weekly basis. Usually we escalate threads, bugs & tech issues, suggestions... depending on many factors like the number of views, number of comments, is it a recent thread, is it an old threats but new comments are confirming the issue is still happening, number of upvotes, also the number of reports for this specific matter on other social Media platforms, ... Sometimes it is easier for us to note things down and report than commenting on each threads. Commenting could attract attention to a given issue and the community could think we aren't working on another thread/report because we haven't commented on that matter. Rest assured: We are reading the vast majority of comments in the CK3 forums, as much as we possibly can

## Reply 49 — participant_019 · 2022-04-11 · post-28206150

Thank you @jakeowaty for this overview of your work. And thanks to the devs and community managers for meeting the expectations of the players by being more present, answering topics sometimes, leaving little signs other times, and explaining the part of your work that we don't see. Thank you for that.

## Reply 50 — participant_037 · 2022-04-16 · post-28216127

<!-- artifact:quote:start -->
> Ckopcepeo said: There is still no way to select PS5 or XBOX in the menu on which OS you are playing on in the topic creation bugs sub-forum, so there is no way to describe specific problems on the console versions. Click to expand...
<!-- artifact:quote:end -->
More than two weeks post-release and this still hasn't been fixed. There's still no console-specific subforum, still no formal place at all to report console bugs (except, get this, a channel on the Discord server that @PDXOxycoon says should not be used). Console version is beta-quality at best and still no acknowledgement of the wide ranging issues nor any mention that a hotfix for the most serious bugs is being prioritized. Sad and disappointing, because it's a fun game and a pretty good console port which clearly needed just a little more time baking in the oven.

## Reply 51 — participant_026 · 2022-04-17 · post-28216927

<!-- artifact:quote:start -->
> Ener_Ji said: More than two weeks post-release and this still hasn't been fixed. There's still no console-specific subforum, still no formal place at all to report console bugs (except, get this, a channel on the Discord server that @PDXOxycoon says should not be used). Console version is beta-quality at best and still no acknowledgement of the wide ranging issues nor any mention that a hotfix for the most serious bugs is being prioritized. Sad and disappointing, because it's a fun game and a pretty good console port which clearly needed just a little more time baking in the oven. Click to expand...
<!-- artifact:quote:end -->
The transfer is really interesting! But that's clearly not what I expected for $50

## Reply 52 — participant_035 · 2022-04-18 · post-28218124

At least there are a lot console players, so you get a chance to have it fixed. To give some perspective, 2 weeks doesn't seem too long, in comparison the keyboard layout issue has been reported since the release. I saw the same problem for Stellaris too, which was released in 2016. I'm aware there are more QWERTY users than AZERTY, so I suppose it's not worth spending time on adding a few configuration lines in a file, maybe that's why these bug threads were closed. Though I wonder why there is a locale setting in that case, it can be set to French, but only for the text part, not the inputs. Sad times, it was easier when computers like the C64 all had the same hardware.

