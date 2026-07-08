---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1556674/"
forum_thread_id: 1556674
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 5
title: CK3 Console DD - Free Update/Ruler Designer
dd_date: 2022-11-15
author_handle: PDX_Pariah
expansion: Console Edition
patch: Crusader Kings III Console Edition
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1737
inline_image_count: 8
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1556674'
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
    location: raw_lines_122_to_124
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_255_to_258
    action: preserved_and_flagged
    counts:
      Like: 16
      (unlabeled — rendered as base64 data URI): 1
      Love: 3
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_282_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Console DD - Free Update/Ruler Designer

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)
- Start date [Nov 15, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/latest) [Follow](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/watch) [Reply](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22941](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

- [1](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/)
- [2](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/page-2)
- [3](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/page-3)
[Next](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/page-2)

1 of 3

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/page-2) [Last](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/page-3 "Last")

[![PDX_Pariah](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/dev/s/paradox5.png)](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

#### [PDX_Pariah](https://forum.paradoxplaza.com/forum/members/pdx_pariah.1547197/)

##### Community Manager

Jul 21, 2020

119

4.454

[](javascript:;)

- [Nov 15, 2022](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/post-28615445)


- [/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/post-28615445](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/post-28615445)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/28615445/bookmark "Bookmark")
- [#1](https://forum.paradoxplaza.com/forum/threads/ck3-console-dd-free-update-ruler-designer.1556674/post-28615445)

Howdy all!  

As we recently announced, we are proud to release Northern Lords this coming Thursday (11/17) which will be accompanied by a Free Update which will of course include Ruler Designer. Without much further delay, we will let the team from Lab42 tell you what to expect with their own words:  


**Ruler Designer:**  
The Ruler Designer is coming to CK3 console. Now you can terrorize and bemuse the inhabitants of the world with your unique and overpowered godlike rulers. Despite looking far different from the original, it plays as well. The menus and navigation have been re-designed to guarantee a smooth experience across the board. They have been revamped and restructured – much like the base game – to be suitable for consoles. Which has been a major undertaking for the LAB42 team, and we appreciate all the work our developers have put into making it what it is now.  

When adapting the Ruler Designer from PC to console, the core challenge was the main screen of the Ruler Designer. When you open it on pc this is what you see:  

![1668509121137.png](https://forumcontent.paradoxplaza.com/public/898392/1668509121137.png "1668509121137.png")



Although suitable for PC, it is clear that a significant amount of work was required to make the transition from PC to console. This was a key area of focus for the team.  

To start with, we made the conscious decision to follow the same design philosophy that resonates throughout the console adaptation. By keeping the controls identical to what players already know and by keeping a structure that is already familiar, we hope that getting familiar with this new extensive feature will be an easy and quick process.  

Our first step was to separate the menu into categories. We looked at various UI elements present in the menu and tried to group them into tabs with a consistent theme or logic.  

![1668509275340.png](https://forumcontent.paradoxplaza.com/public/898393/1668509275340.png "1668509275340.png")



Apart from the elements marked as meta information, all other groupings were turned into tabs. Each with two or more subtabs to better separate and organize the different parts of the customization process. As an example, for the character details tab, we added three sub tabs: Sex & Sexual Orientation, Age & Weight, Name & family (all self-explanatory).  


The same organizational process was used on the Change Appearance options, with the slight difference that we used the already existing buttons (Head, Neck, Eyes, etc) as the base for the tabs.  

![1668509365467.png](https://forumcontent.paradoxplaza.com/public/898394/1668509365467.png "1668509365467.png")



All the small selectable icons in the base game were changed to buttons and arranged in their respective categories. For example, the Venus and Mars symbols were made into selectable buttons that players can select to change the sex of their ruler.  

![1668509401870.png](https://forumcontent.paradoxplaza.com/public/898395/1668509401870.png "1668509401870.png")



We’ve kept the sliders where they were, adding a glow around them so you know which one is currently highlighted. Because the sliders were originally made to be used with a mouse, we had to change the way console players interact with them, by adding incremental speed to the slider itself. Single presses will move the slider one value, while holding down left/ right direction on the d-pad or left analog stick, will move the slider faster and faster.  

The colour picker was a unique UI element, which meant it had to be designed from scratch. The main challenge with this tool was the fact that it needed to “capture input” meaning that when in use, no other UI element could be interacted with – in other words, no other UI element in the menu can be accessed or interactable while the colour picker is active. This was not an easy task, as it required us to disable all interactions outside the square that makes the colour picker – something not necessary in the PC version, where interactions determined by the location of the mouse on the screen.  

This led to many occasions where, after selecting the colour picker, players were still able to navigate the rest of the UI elements while picking a colour. We eventually figured out a way to implement the colour picker, so it locked all controls outside of itself. Which then led to one of the funnier bugs we’ve had during the development of Northern Lords: the noisy colour picker.  

This bug was a simple fix, and it came down to a repeating sound that was caused by the colour picker emulating a UI button behind the scenes. Which meant that every time a new colour was picked, A.K.A the cursor was moved to a different position/ colour, the game interpreted it as a new button being highlighted, playing the sound cue for it. This led to the sound being repeated constantly for as long as players scrolled through the colours. We did have a bit of fun with it.  

The Faith and Culture lists were transformed into a big list of dropdown menus, where players can expand and collapse the dropdowns as they wish and highlight each one of the cultures/ faiths and see their tooltip for information on it.  

![1668509601410.png](https://forumcontent.paradoxplaza.com/public/898396/1668509601410.png "1668509601410.png")



The Traits were one of the more interesting parts to re-design, as they required multiple types of interactions. In the end, we decide to follow the true tested method of making a list. Each category of traits (Education, Personality, Other Traits) has a button that players can select to open a list with the respective traits of that category. In situations where you can pick multiple traits from the list, it will stay open until you decide to close it with a press of the Back Button.  

![1668509803125.png](https://forumcontent.paradoxplaza.com/public/898398/1668509803125.png "1668509803125.png")



If during the selection players accidentally pick something they don’t want, they can backout of the list and remove that trait from the group of selected traits, by highlighting the trait and pressing the select button.  

![1668510803076.png](https://forumcontent.paradoxplaza.com/public/898399/1668510803076.png "1668510803076.png")



With the Skills we decided to separate the base level of the skill from the bonuses it gets from selected traits. This decision came as a result of very high skill levels, from player created characters, showing a skill of 100 and players still being able to press the Add Point button, increasing the total score of the character without increasing the total value of the skill (since the cap is 100). Because this could easily be interpreted as a bug, we decided to separate the two values. It not only solved that issue, but also worked to organize the skill points in an easier to understand format. Don’t worry, you can use the Advanced Tooltips Mode to check where all the points in the bonus value are coming from.  

![1668510867508.png](https://forumcontent.paradoxplaza.com/public/898400/1668510867508.png "1668510867508.png")



And that pretty much sums up our experience developing the Ruler Designer into a console ready menu for your enjoyment. We hope you all have as much fun playing around with it as we have working on it.  


Now, go forth and create your own rulers!

<!-- artifact:reactions:start -->
- 16 Like
- 8 (unlabeled — rendered as base64 data URI)
- 3 Love
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
