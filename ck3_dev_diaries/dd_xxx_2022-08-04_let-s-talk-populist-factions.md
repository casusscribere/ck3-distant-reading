---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1537785/"
forum_thread_id: 1537785
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: null
title: "Let's Talk: Populist Factions"
dd_date: 2022-08-04
author_handle: Servancour
expansion: Friends and Foes
patch: Patch 1.7 (Bastion)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1713
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1537785'
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
    location: raw_lines_~28_to_119
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_121_to_122
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_245_to_249
    action: preserved_and_flagged
    counts:
      Like: 87
      Love: 40
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_313_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Let's Talk: Populist Factions

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Aug 4, 2022](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

Status
Not open for further replies.

- [1](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/)
- [2](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/page-3)
- [4](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/page-4)
[Next](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/page-2)

1 of 4

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/page-4 "Last")

[Show only dev responses](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/?prdxDevPosts=1)

[![Servancour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/obsolete/s/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/servancour.465268/)

#### [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)

##### Game Designer

**Paradox Staff**

**4 Badges**

Mar 15, 2012

1.606

9.949

- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")
- ![500k Club](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/500k_red.png "500k Club")
- ![Paradox Order](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/pdx_order.png "Paradox Order")
- ![Stellaris Sign-up](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Stellaris_SignUp_icon.png "Stellaris Sign-up")

[](javascript:;)

- [Aug 4, 2022](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/post-28406853)


- [/forum/threads/lets-talk-populist-factions.1537785/post-28406853](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/post-28406853)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28406853/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/lets-talk-populist-factions.1537785/post-28406853)

Salutations!  
We’ll be starting up our regular Dev Diaries in the next few weeks or so, but until then, I wanted to take the opportunity to give you a brief look into some changes I’ve been working on. Specifically, I wanted to talk a bit about Populist Factions.  

Populist Factions have remained largely unchanged since release. We’ve done the occasional bug fixing and whatnot, but have yet to do something more substantial. They are, frankly, just as problematic now as they were at release. Populist factions have a number of problems that make them boring or frustrating to play against. These include (but are not necessarily limited to):  


- Significant issues in regards to vassal gameplay. It’s not particularly fun to have a large part of your realm (and possibly your domain) suddenly go independent with next to no warning.
- They are little more than a glorified peasant revolt that offers no real challenge for a top liege who has a decent amount of men-at-arms or knights at their disposal.
- You don’t really have a lot of tools to manage a Populist Faction, or the popular opinion of the counties joining one.
The last point was somewhat made better with the cultural rework in Royal Court, and the introduction of cultural acceptance. The rework gave you a new tool to influence and reduce the overall impact of popular opinion. I’d like to explore popular opinion further in the future, but for now, let’s focus on resolving the other two issues.  

In an effort to improve Populist Factions, I’ve been working on a smaller update to alleviate the issues mentioned above. Do note that some of the changes are a bit experimental in nature. Which is why I’d like to get your input and thoughts on how you think these might pan out. I approached the faction with the following goals in mind:  


- Solve the issue regarding the lack of player agency when playing as a vassal
- Differentiate them from Peasant Factions
- Increase difficulty to make them more interesting and challenging
Let’s start with the most outstanding issue, that of vassal gameplay. The main issue stems from the fact that the faction may only target the top liege. This prevents you as a vassal to have any influence in the outcome, and you don’t receive any real information as to what happens with the faction. Having a liege simply accept a Populist Faction's demand is a large source of frustration, as you can lose a big part of your realm without being able to do anything about it (and you are not even told why it happened).  

Simply switching the perspective to the vassal won’t cut it. We don’t want the reverse situation, where the vassal makes the decision without allowing the liege to have any say in the matter. So how do we solve it? I wanted to keep the functionality of the faction targeting the top liege. A popular uprising should go independent if they are successful. But vassals should be able to get involved. So I figured I’d try something new here, but stay away from any complicated solutions. When a Populist Faction goes to war, any direct vassal is now invited to participate in the faction war if they want to. The vassal has the option to join and help the liege, join the rebels, or stay out of it. Yes, that means that vassals and liege now fight side by side against a popular revolt. It’s limited to direct vassals only though, in order to keep the amount of vassals that may join on a reasonable level. We do, however, extend the functionality to any player sub-vassals, so that you always have the option of joining the war and protecting your lands (this is the problem we are attempting to solve here after all).  

![01_houston_we_have_a_problem.png](https://forumcontent.paradoxplaza.com/public/853211/01_houston_we_have_a_problem.png "01_houston_we_have_a_problem.png")


*The war overview for a populist revolt. Note the vassals who have joined on each side.*​


With vassals being able to join, an AI liege will never accept the faction demand if an affected vassal is a player. Cause if they do, that would just take us back to square one. This guarantees that, as a vassal, you can react and help your liege against a populist revolt which includes counties within your own realm. You’ll still have the option of joining a liege’s war even if you are unaffected, you just won’t get a direct invitation to the war.  

![02_an_offer_you_cant_refuse.png](https://forumcontent.paradoxplaza.com/public/853212/02_an_offer_you_cant_refuse.png "02_an_offer_you_cant_refuse.png")


*The letter event a vassal receives when a populist faction send their demands.*​


Now that vassals are allowed to join, we need to give a populist uprising additional military prowess. Otherwise they would be trivial to fight against. The difficulty has been ramped up in multiple ways. The most significant change here is that their armies will no longer only have levies. They’ll generate some base men-at-arms depending on the terrain type they spawn in. Hills will give them archers, mountains will give them spearmen, and so on. This should ensure that they get an appropriate troop composition. As before, the amount of levies and men-at-arms depends on the holdings of the counties participating in the revolt. Stronger holdings provide more troops. Additionally, armies will get some siege weapons that depend on the innovations the culture has unlocked. If the culture has gained access to trebuchets, that’s what they will spawn with. This will ensure that populists are able to stay relevant in the mid to late game, without having to besiege a holding for years before making any sort of progress.  

![03_you_and_what_army.png](https://forumcontent.paradoxplaza.com/public/853213/03_you_and_what_army.png "03_you_and_what_army.png")


*The troops of a populist revolt.*​


Populist revolts used to only spawn with the leader as an available commander. Step one was to make the leader a bit better. By increasing their martial skill, and giving them some better traits (you are not going to be a popular leader for nothing after all), they’ll be slightly more threatening. Step two was to provide them with multiple commanders. A revolt should generally start with enough commanders to assign one to each spawned army. These commanders tend to be fairly skilled as well, significantly increasing their advantage in battles.  

![04_I_am_spartacus.png](https://forumcontent.paradoxplaza.com/public/853214/04_I_am_spartacus.png "04_I_am_spartacus.png")


*The advantage of the leader of a revolt.*​


That about sums it up, at least for the major changes. I hope that Populist Factions will be significantly more interesting than before. Let me know what you think!

<!-- artifact:reactions:start -->
- 87 Like
- 40 Love
- 5 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
