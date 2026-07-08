---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1408176/"
forum_thread_id: 1408176
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 35
title: "CK3 Dev Diary #35 - User Testing Before Release"
dd_date: 2020-07-28
author_handle: Naifuraifu
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1402
inline_image_count: 2
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1408176'
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
    location: raw_lines_~28_to_148
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_147
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1426.jpg?1595939389
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_150_to_152
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_207_to_210
    action: preserved_and_flagged
    counts:
      Like: 74
      (unlabeled — rendered as base64 data URI): 4
      Love: 4
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_218_to_273
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_274_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

<!-- artifact:thread_banner:start -->
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1426.jpg?1595939389)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #35 - User Testing Before Release

<!-- artifact:thread_metadata:start -->
- Thread starter [Naifuraifu](https://forum.paradoxplaza.com/forum/members/naifuraifu.1542634/)
- Start date [Jul 28, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-35-user-testing-before-release.1408176/)
<!-- artifact:thread_metadata:end -->

Hello everyone!  

My name is Hanna and I work in a growing field of game development called User Research! I’m here to tell you a little about the job itself and also how me and my team have worked with user testing for Crusader Kings III.  

**Ah, user testing, I get it - you’re QA/Quality Assurance!**  
Oh, how many times I hear that! But no, I am not. Very, very simplified it’s kind of like this: When QA evaluate a feature they report on it in a yes/no kind of way - Does it work? Yes/No, so here’s a bug report.  

When User Research are asked to evaluate a feature, we look at the game from a *user perspective* by trying to test and gather feedback on things like how well players understand the game, if any menus are confusing, if players are having fun, etc. This can be done in a variety of ways, but for Crusader Kings III we mostly used playtests where we let 2-15 players that match a specific profile (in this case - PDS strategy players) into our lab to play an unfinished version of the game while watching and recording them and then we brought video clips and player feedback to the dev team.  

Woah, that seems pretty abstract! How can you make sure that you’re getting these things completely right and accurate?  
You’re right, it is tough - We do this by using a lot of methods used in social science to be able to verify our findings. Most of the time we’ll use a combination of observation (meaning we watch the player playing and take notes on what they say/do), one or several surveys and then an interview. If we can see several people struggle with a tutorial step, chances are they won’t be alone in having that issue, and having them describe how it felt both verbally and in text let’s us pinpoint what’s wrong.  

But of course humans are complicated, and it’s important to remember that while we use scientific methods our job is not to produce scientific results. Instead, our job is giving our colleagues a heads up on how to tweak things by providing a basis for discussion and re-design.  

**And this is relevant to Crusader Kings III because…?**  
Well, I think having User Research done is good for any kind of interactive medium when it comes to evaluating the ideas and designs put into the game. Crusader Kings III is also an interesting challenge from a user design perspective - How do we keep the complexity hardcore players want while still making sure new players can discover the awesome feeling of inheriting a title because your nephew had an “accident”? If we don’t listen to what actual players say and think, we risk making mistakes and finding out about it when it’s too late to change anything.  

**Enough about Using Research or whatever, what did you do for Crusader Kings III?**  
As you’ve likely seen we’re doing a lot of new things in this game compared to both other PDS titles and Crusader Kings II, so this means that having player feedback early is a good idea to avoid going ahead with something that turns out to be a mistake.  

For example, one of the first things we did for Crusader Kings III was actually done internally - the dev team were making early designs for characters and User Research helped them out by sending out a survey to all of our colleagues to gather feedback. At the time, characters looked like this:  

![Early concept arts.jpg](https://forumcontent.paradoxplaza.com/public/590900/Early concept arts.jpg "Early concept arts.jpg")



And good thing we got some feedback, because the style turned out to be way too cartoony for most people! It might have brought our colleagues a lot of work, but I’m glad we discovered this way before release day…  

Throughout the development of the game, we’ve also run bi-monthly 1 hour playtests with 2-4 players. These tests are often done in close collaboration with the UX designers and are very focused on us seeing how well players are able to finish basic gameplay actions like getting married, starting and finishing a war, setting up a scheme and things like that. Thanks to these tests, several changes have been made to menus that have proven difficult for players to navigate like the Council, Marriage and Building menus and the Siege/War overviews.  

But my favourite part of my work is to actually see people play and experience the game during longer playtests. For Crusader Kings III the most important playtest was when it was time to evaluate the [tutorial and systems for in-game help](https://www.crusaderkings.com/news/dev-diary-16-tutorials-and-tooltips-and-encyclopedias-oh-my). For this test we had 12 participants, 6 of them with 200-800h of CK2 playtime and 6 of them “newbies”, try out the tutorial and then play the game for 2 hours using what they’d learned.  

And you know what? Most of them managed just fine, which isn’t really something I’m used to seeing when it comes to Paradox onboarding. New players loved that the tutorial used visual cues to guide them through menus and the suggestions helped them with an issue that many PDS titles have - What the heck do I do next? “Old” players found the UI took some time to get used to, but they also found the suggestion systems useful as checklists on what to do next.  

But of course, nothing is perfect - and thanks to the player feedback we could also pinpoint areas where more work was needed for both new and old players, especially regarding the UI. But throughout the playtests we’ve done I’ve been happy to see the game go from incomprehensible to approachable, both for new and returning Crusader Kings-fans.  

**So if you run these tests why aren’t the games perfect and amazing then?**  
Oh, I ask myself the same thing every day… But the truth is, game development is complicated and sometimes there’s just no time, manpower or money to address the issues we’ve discovered. We also share our results with community management and marketing to give them a heads up on the questions and concerns they can expect on release.  

**Has anything changed due to Corona?**  
Oh absolutely! The biggest change for my team of researchers is that we don’t have access to our beautiful lab at the Stockholm office. The lab is geared up with computer stations where you can prep game installation and recording setup beforehand. This makes setting up studies a lot easier for us and it’s also a good way of preventing leaks.  
Crusader Kings III has been lucky in that we had concluded most of the lab activities we’d planned before the release, but for other projects we’ve done studies remotely meaning that we let players play the game on their own computers and do all interviews via video chats. While we’re still trying to work things out, we’re also discovering a lot of benefits from this method of working - the biggest one being that we could potentially run playtests with people from all over the world!  

**What will you do after the release?**  
For Crusader Kings III, I will start working on gathering and reporting on feedback following the release - which means that anything you write on Steam or other pages, I’ll go over and try to summarize topics so we know what to improve on next. Then, it’s time to plan new playtests for patches and DLCs!  

I hope you’ve enjoyed reading about a lesser known field in game development and that you’ll look forward to the upcoming release of a game that I’ve absolutely loved working with. I will be on vacation when this is posted, but I’ll be happy to answer any questions about User Research when I’m back again on August 1st. Oh, and please be nice to my vanity character if you encounter her - she’s very, very weak.  

![Vanity Character.jpg](https://forumcontent.paradoxplaza.com/public/590901/Vanity Character.jpg "Vanity Character.jpg")

 

- 103

<!-- artifact:reactions:start -->
- 74 Like
- 11 (unlabeled — rendered as base64 data URI)
- 4 Love
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Naifuraifu](https://forum.paradoxplaza.com/forum/members/naifuraifu.1542634/)**
Role: Recruit
Messages: 1
Reaction score: 189
<!-- artifact:op_signature:end -->
