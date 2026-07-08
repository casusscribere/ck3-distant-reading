---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1345581/"
forum_thread_id: 1345581
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 16
title: "CK3 Dev Diary #16 - Tutorials and Tooltips and Encyclopedias, Oh My!"
dd_date: 2020-03-03
author_handle: blackninja9939
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2607
inline_image_count: 13
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1345581'
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
    location: raw_lines_~28_to_144
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_146_to_148
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_294_to_297
    action: preserved_and_flagged
    counts:
      Like: 7
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 1 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_305_to_415
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_416_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #16 - Tutorials and Tooltips and Encyclopedias, Oh My!

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [Mar 3, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-16-tutorials-and-tooltips-and-encyclopedias-oh-my.1345581/)
<!-- artifact:thread_metadata:end -->

Hello everyone and welcome to the 16th CK3 Dev Diary!  

I’m Matthew, one of the Programmers on CK3, some of you might have seen me around the Discord server or on the forums from when I was on CK2. I started out as a modder on CK2 and then a couple of years ago started working as a Content Designer in house at Paradox, before moving into the Programming role where I’ve been for the past year and a half.  

As with the whole team I am of course very excited to be finally able to talk about the game after all our secrecy, so without further ado let us discuss the wonder of making pixels appear on the screen and convey useful information!  

CK2 is one of my favourite games, even before I started working here, and I’ve sunk thousands of hours into modding and playing it. But I think we can all be honest here together and admit something, it had a UI with what one might describe as questionable usability.  
I know when I started playing CK2 that I very quickly had to stop and go watch many hours of tutorials online because the UI was hard to use and buried relevant info without ever giving you an inkling of where to look.  

This is something we very much want to avoid for CK3 for obvious reasons, the strategy and challenge of the game should come from mastering its systems not finding which button you need to click or which number you need to tooltip…  

I’d like to quickly give a big shout out to our wonderful User Research team who has done lots of play tests with players of various experience levels in strategy games and given us lots of great feedback, all which has been invaluable in ensuring the various features of this dev diary can help to guide a new player who is unsure of what to do whilst also letting an expert to blaze through with doing what they want.  

A lot of work has been put in to make the interfaces clearer and display relevant information to you so let's dive right in and explore it in the way that most of you probably will, when you first launch the game!  

The first thing that will confront you when you open up and choose where to play is an option of if you want to start the guided tutorial or just dive in on your own. We are going to go down the guided tutorial otherwise this dev diary would lose quite the chunk of content!  

![tutorial_pick.png](https://forumcontent.paradoxplaza.com/public/537563/tutorial_pick.png "tutorial_pick.png")



In the tutorial you will take control of Petty King Murchad mac Donnchad of Munster: yes we have fully embraced tutorial Ireland as our starting location.  

The tutorial will guide you through various parts of the interface and mechanics of the game, it will open the windows you need to see and highlight relevant pieces of information. Such as how to navigate the map, interacting with characters, and getting married.  
All of this takes place in game, so it will be showing you the exact places in the UI you are meant to be looking at and interacting with instead of lumping just walls of text or screenshots at you.  

![tutorial_in_game.png](https://forumcontent.paradoxplaza.com/public/537564/tutorial_in_game.png "tutorial_in_game.png")



I am not going to go through every piece of information here, as that is best served by going through the tutorial yourself once the game is released than me parroting the text here. But suffice to say it will give you a good starting grasp on how to use the UI and the core mechanics to get you started and playing.  

One of the new features in CK3 is Tooltips in Tooltips, the aim of this is that relevant information can just be a mouse move away whenever you see blue highlighted text in game. Instead of making you need to dig through a wiki to find out what a Game Concept means you can just mouse over it and get an explanation!  

![tutorial_popup.png](https://forumcontent.paradoxplaza.com/public/537565/tutorial_popup.png "tutorial_popup.png")



For example if you tooltip the word Duchy here you get this popup:  

![tooltip_in_tooltip.png](https://forumcontent.paradoxplaza.com/public/537566/tooltip_in_tooltip.png "tooltip_in_tooltip.png")



This behaviour is nesting so you can get more and more information, so all the blue highlighted Game Concepts in this can also be highlighted to explain what a Ruler is and then what a Title itself is etc.  

![tooltips_4_days.png](https://forumcontent.paradoxplaza.com/public/537567/tooltips_4_days.png "tooltips_4_days.png")



There are two different modes for Tooltips in Tooltips, timer lock and action lock with the former being the default. These modes determine what causes the Tooltips in Tooltips to lock in place and stay, either a timer which is configured in the settings menu or by clicking in the middle mouse button to manually lock them in place.  
We have these two modes so that once you get more comfortable with the game you can turn the tooltips in tooltips into an opt in mode with the action lock for when you come across something you want to see instead of it being more present trying to aid you.  

Once you finish the guided section of the tutorial the Reactive Advice section begins. These are bits of advice that appear as a purple info icon during normal gameplay, they will give you mini tutorials based on your current state in the game. If you remember from the tutorial selection popup the second option was to dive in on your own, that option skips the guided tutorial and jumps you right in to play and receive in the game advice.  

For example, if your Bishop is not endorsing you and refusing to give you those taxes and troops that you rightfully deserve, as mentioned in [Dev Diary #6](https://forum.paradoxplaza.com/forum/index.php?threads/ck3-dev-diary-06-council-powerful-vassals-spouse-councillor.1292549/), then you can click the bubble and get a run down of what that means for you instead of needing to find it on the wiki or find the relevant dev diary.  

![reactive_advice.png](https://forumcontent.paradoxplaza.com/public/537568/reactive_advice.png "reactive_advice.png")



As with the guided tutorial, this advice will highlight relevant interface elements to show you where to look as well as give examples of actions you could potentially take.  

The reactive advice can be reset in the settings menu to show advice you’ve already seen again if you feel like you are forgetting information and need a quick refresher. The reactive advice is also usable in multiplayer so your friends you just introduced the game to can play with you and still get the advice they may need.  

Throughout the course of the game other pieces of information will appear in this top bar, as with our other games alerts about things that require your attention will appear such as prompting you go get married or that you have no heir of your dynasty and risk the game ending on your death.  
These alerts are all something that can be solved by you by taking relevant actions to make them disappear, which clicking them will take you to a suitable action, they are not a status reminder of something constant such as being at war or having a truce expiring soon, as sometimes happens in our other games because those are not things you can take an action to fix.  

![alert.png](https://forumcontent.paradoxplaza.com/public/537569/alert.png "alert.png")



Alongside the Alerts and Advice in the top bar is the Issues tab, this shows some summaries of your current situation such as claims you can press, duchies you can create or the fact you have emptied the realm’s cofferts and are bankrupt and in desperate need of money.  
These are things you may wish to take action on but are not an urgent thing to fix, or potentially not something you can instantly fix like bankruptcy, you can think of them almost as mini-alerts.  

Alongside these are Suggestions of things you can do, they will appear and based on your current situation give you a task you may wish to do, every few months they will appear and can be dismissed as you see fit or entirely disabled in the settings menu once you feel you can work without them.  
In our play tests this feature has proven useful for both new and old players, as it gives guidance to new players of things they can do in this big sandbox world and for the more experienced players it acts as a good checklist whilst playing for things you know you want to handle.  

![issues.png](https://forumcontent.paradoxplaza.com/public/537570/issues.png "issues.png")



For less long term information or pressing things to solve there are two more methods of showing new information, Notifications and Toasts.  

A Notification is what it says on the tin really, like the message feed in CK2, smaller pieces of information which are sent over, they are not necessarily some big situation you need to pay attention and generally relate to the happenings of other characters that you may care to see.  
Only a few will be displayed at a time and minimise themselves to allow room for the next one before automatically dismissing themselves after some in game time has passed.  

![notifications.gif](https://forumcontent.paradoxplaza.com/public/537574/notifications.gif "notifications.gif")

  

Toasts on the other hand are slightly more bombastic compared to their more timid sibling Notifications, they appear at the top of the screen and inform you of good things to celebrate, and sometimes less good things to commiserate about.  

They are used for things like the outcomes of events, to tell you what outcome in that dice roll you got without throwing up a huge event window or having it appear as a small notification, and for feedback on actions you’ve taken.  

Unlike notifications, they will only show one at a time in a timed queue to show the next, of course if you mouse over one of them that timer will stall itself until you move the mouse away again to let it progress and fade away.  

![toasts.gif](https://forumcontent.paradoxplaza.com/public/537575/toasts.gif "toasts.gif")

  

Now last, but in my opinion not least, is the new in game Encyclopedia. It acts as a central place where information on many different parts of the game can be found. From the highlightable Game Concepts mentioned before, to recaps of the guided tutorial and reactive advice, to the various types of terrains and traits present in the game and their effects.  

![encyclopedia.png](https://forumcontent.paradoxplaza.com/public/537571/encyclopedia.png "encyclopedia.png")



The Encyclopedia contains various pages and is fully searchable as well as including a history of searches and the pages they were on which can be used to scroll back and forward between searches.  
All the information on these pages is automatically generated by the game from our script files, so unlike pages on a fan wiki they will automatically update if any values or descriptions change.  

Something I’d like to mention about all the new features I’ve talked about here is that they are entirely moddable. Mods are free to create new game concepts which will hook in to the tooltips in tooltips and Encyclopedia automatically, make new lessons in the tutorial to cover their new systems, add more reactive advice or alerts, make new suggestions and situation descriptions, and hook in more notifications or toasts in the script.  

One of the aims of CK3 is to be even more moddable than CK2, which is already a very moddable game, and one of those things we’ve looked at improving a lot is the interface modding. In CK2 at best you could change some textures and move things a few pixels but you could rarely add new things, in CK3 we’ve made a lot of things more easily scripted so you can by and large create any new things just as we can.  

So in conclusion we’ve worked on a lot of stuff to make the depth and strategy of our games shine through in the choices you make, not the 20 minutes you spend trying to find the information to help you make those choices because the interface is obtuse.  

Hopefully you’ve enjoyed the dev diary, if you wanna chat more then I highly recommend joining our [CK Discord Server](https://discord.gg/ck3) as well.  

**Bonus Dev Story:**  

Once a month at the development studio we all spend a day (if your project is not extra busy for a milestone or release) doing whatever we decide to grow our professional skills, this is how the Encyclopedia came about as my little baby over multiple of these personal development days. I thought it would be fun to briefly walk people through its evolution from just an idea to a full feature!  

To start with it only included the game concepts, and looked a lot less pretty as art had yet to bless me with their time and wisdom, here is a little screenshot of the “greybox” version that simply vomited out un-formatted text and had a search bar:  

![first_iter_encycloepdia.png](https://forumcontent.paradoxplaza.com/public/537572/first_iter_encycloepdia.png "first_iter_encycloepdia.png")



Moving on from there I wanted to reorganise it into this concept of “Pages”, so we could also show information on things like all the traits in the game instead of you needing to find someone with the trait to discover what it does, I worked on that and one of the artists generously used some of their time to give the whole thing a much needed makeover:  

![second_iter_encycloepdia.png](https://forumcontent.paradoxplaza.com/public/537573/second_iter_encycloepdia.png "second_iter_encycloepdia.png")



Our QA has then gone over this through the various iterations raising any issues, especially once it was in a more beta state to give more suggestions for polish and find bugs for me to fix.  

Now that I had the text formatted nicer and some suggestions from QA I started adding more and more pages to get to the ones we now have, as well as adding some more luxury features like a search history, better interaction with hotkeys, showing all pages at once, and some debug functionality.  

One of the technical problems I ran into was the hot reloading of files crashing the game now, in our debug builds we attach file watchers to all game files so if you change the values of a trait or add a new building type then the game will update its databases internally and update or add those new things. But the problem with that is the Encyclopedia was pointing now to the invalid memory of the old entries we had deleted, the solution to this was adding reload callbacks to fix up the encyclopedia by flushing out its old data and regenerating it, internally this just means that the encyclopedia instead has to register a bunch of page generators that it can re-run instead of using the actual database objects which can get corrupted if modified and the pointers invalidated.  

Then with a little bit more polish and tweaking we finally get it in the state it is now which will hopefully prove useful to you all whilst playing!

<!-- artifact:reactions:start -->
- 7 Like
- 2 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)**
Role: Former Senior Programmer - Crusader Kings 3
Badges: 99
Reaction score: 8,575

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
