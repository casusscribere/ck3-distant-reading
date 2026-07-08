---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1546936/"
forum_thread_id: 1546936
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 111
title: "Crusader Kings 3 Dev Diary #111 - 1.8.0 “Robe” Feature Highlight"
dd_date: 2022-11-22
author_handle: Hugo Cortell
expansion: Friends and Foes
patch: Patch 1.8 (Robe)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2048
inline_image_count: 15
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1546936'
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
    location: raw_lines_~28_to_142
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_141
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2138.jpg?1669200921
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_144_to_146
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_247_to_252
    action: preserved_and_flagged
    counts:
      Like: 115
      Love: 24
      (unlabeled — rendered as base64 data URI): 4
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_260_to_362
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_363_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2138.jpg?1669200921)
<!-- artifact:thread_banner:end -->

# Crusader Kings 3 Dev Diary #111 - 1.8.0 “Robe” Feature Highlight

<!-- artifact:thread_metadata:start -->
- Thread starter [Hugo Cortell](https://forum.paradoxplaza.com/forum/members/hugo-cortell.1630085/)
- Start date [Nov 22, 2022](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-111-1-8-0-robe-feature-highlight.1546936/)
<!-- artifact:thread_metadata:end -->

![This image depicts an in-game notification with the title “1.8.0 Feature Highlight”, to the right is the vanity character of Hugo Cortell, while to the left is the Paradox Interactive logo. The text within the notification body says “The Paradox Community gained 20 opinion of you (Received Dev diary).](https://forumcontent.paradoxplaza.com/public/883178/dev_diary_asset_header.png "This image depicts an in-game notification with the title “1.8.0 Feature Highlight”, to the right is the vanity character of Hugo Cortell, while to the left is the Paradox Interactive logo. The text within the notification body says “The Paradox Community gained 20 opinion of you (Received Dev diary).")

Hello crusaders! I’m [@Hugo Cortell](https://forum.paradoxplaza.com/forum/members/1630085/), game designer and horchata drinking aficionado at Paradox Thalassic, and today I am here to present everything new and exciting with the upcoming 1.8.0 “Robe” free update.  

We’ve worked hard to ensure that this update is a wonderful blend of bug fixes, refinements, and brand-new features. Since this is a “Feature Highlight”, I’ll be keeping it short and sweet and focusing on the latter two. But worry not, I'll still be showing off two of our more interesting changes from the upcoming changelog diary.  
Without further ado, *let’s begin.*  

## New Bookmark Screen​

The biggest thing you’ll notice when starting a new game with 1.8.0 will certainly be the new and shiny bookmark screen, which has been redesigned to more cleanly fit new scenarios.  

![This image is animated, showing a before and after comparison of the bookmark screen User Interface. The new one is much more stylish.](https://forumcontent.paradoxplaza.com/public/883180/new_before_after.gif "This image is animated, showing a before and after comparison of the bookmark screen User Interface. The new one is much more stylish.")


*Click (*[*here*](https://forumcontent.paradoxplaza.com/public/883183/BEFORE_NEW.png)*) and (*[*here*](https://forumcontent.paradoxplaza.com/public/883182/AFTER_NEW.png)*) for high-quality still images.*  

| ![Screenshot showing the 867 'The Struggle for Iberia' bookmark.](https://forumcontent.paradoxplaza.com/public/883186/1.png "Screenshot showing the 867 'The Struggle for Iberia' bookmark.") | ![Screenshot showing the 867 'The Carolingians' bookmark.](https://forumcontent.paradoxplaza.com/public/883188/2.png "Screenshot showing the 867 'The Carolingians' bookmark.")                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Screenshot showing the 1066 'The Fate of England' bookmark.](https://forumcontent.paradoxplaza.com/public/883189/3.png "Screenshot showing the 1066 'The Fate of England' bookmark.")       | ![Screenshot showing the 1066 'From Rags to Riches' bookmark. Emir Yahya is selected on this screenshot.](https://forumcontent.paradoxplaza.com/public/883190/4.png "Screenshot showing the 1066 'From Rags to Riches' bookmark. Emir Yahya is selected on this screenshot.") |

*Everyone loves a good image collage, right?*  

The new bookmark screen not only looks better but it is also more streamlined: for example, the scenario information box and the character information tab become a single togglable tab once you select a bookmark character, avoiding unnecessary clutter on the screen.  

![This image is a side-by-side comparison of the new togglable information menu, the left side shows scenario information, while the right has information about the character itself.](https://forumcontent.paradoxplaza.com/public/883193/new_bookmark_tab.png "This image is a side-by-side comparison of the new togglable information menu, the left side shows scenario information, while the right has information about the character itself.")



To top it off, alongside the new bookmark screen we have also updated the main menu to conveniently display all the downloadable content you own and easily access any that you may be missing out on. You’ll be able to find it on the bottom left corner of the main menu screen.  

![This image shows the DLC icons on the main menu. One of the DLCs, Fate of Iberia, is being highlighted by the cursor, prompting it to display information about itself. It is also informing the user in the picture that the DLC is enabled and that clicking will open the store page for that DLC.](https://forumcontent.paradoxplaza.com/public/883194/dlccounter.png "This image shows the DLC icons on the main menu. One of the DLCs, Fate of Iberia, is being highlighted by the cursor, prompting it to display information about itself. It is also informing the user in the picture that the DLC is enabled and that clicking will open the store page for that DLC.")



## Custom Ruler Saving​

To complement the new bookmark screen, we’ve also added the ability to save and load custom characters! At long last, you can finally use for multiple playthroughs that one character that you’ve spent so much time detailing to perfection.  

Saving and loading is done through buttons that you’ll find at the bottom left of the ruler designer.  
Selecting load will bring up a list of all saved characters and allow you to conveniently preview your selected creation before loading them into the designer itself.  

| ![This image shows the Ruler Designer window. In the center of the screen lies an overwhelmingly handsome man named Theodore Thalassic, canonically the son of John Paradox. On the bottom left there are two new buttons, one of them (titled 'save') saves the character on screen, while the other (titled 'load'), opens a menu to load a character.](https://forumcontent.paradoxplaza.com/public/883198/Theodore_Thalassic_Son_of_John_Paradox.png "This image shows the Ruler Designer window. In the center of the screen lies an overwhelmingly handsome man named Theodore Thalassic, canonically the son of John Paradox. On the bottom left there are two new buttons, one of them (titled 'save') saves the character on screen, while the other (titled 'load'), opens a menu to load a character.") | ![This image shows the menu used to load saved characters into the Ruler Designer. The window is divided into two parts. The left side contains a list of saved characters, containing their name, a headshot, and the amount of points utilized by that character. The right side has a compact breakdown of the character’s details, their Age, Faith, Family, Skills, and Traits are all displayed in this menu.](https://forumcontent.paradoxplaza.com/public/883199/Character_Loading_Sample.png "This image shows the menu used to load saved characters into the Ruler Designer. The window is divided into two parts. The left side contains a list of saved characters, containing their name, a headshot, and the amount of points utilized by that character. The right side has a compact breakdown of the character’s details, their Age, Faith, Family, Skills, and Traits are all displayed in this menu.") |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


Additionally, saved rulers are stored as individual files in `..\Documents\Paradox Interactive\Crusader Kings III\ruler`, meaning that you will be able to easily share your magnificent creations & abominations with the rest of the CK3 community. I look forward to seeing a mix of gorgeous and cursed creatures in the forums once this release comes to be.  

## Unique Illustrations For Every Tenet​

Yes, you heard right. Get ready for art galore because our artists have been hard at work making new illustrations for ***every single tenet in the game*** that was previously missing one.  


*PSA: if you are visually impaired, hover over the image to get a written description!*  

We don’t want to spoil all of them here, so look forward to seeing them in-game for yourself when the update releases. The art team did a great job making these, especially considering how tenets can have very abstract concepts, which I am sure must have taken a lot of back-and-forths to get just right.  

## Changelog Highlights​

We’ve worked very hard to fix as many bugs as possible for this release. I hope our commitment to making a high-quality product will be made apparent when you see the size of the final changelog *in an upcoming changelog dev diary*. As mentioned at the start of the post, I’ll be sharing two highlights.  
Please note that the current titles may not match their name on the final changelog.  

#### Mozarabs can now use a strong hook to coerce the Pope into binding with Rome​

If you have a strong hook on the pope, you can now use it to skip the requirements for binding with Rome. Though the pope will not like that.  

![This image shows the 'Bind the Faith to Rome' decision side-by-side. The left side shows the requirements, which state that you must either fulfill all the regular requirements or have a strong hook before being able to make the decision. The right side shows the effects of the decision when you use a strong hook to bypass the regular requirements, which includes the pope disliking you and your hook being consumed.](https://forumcontent.paradoxplaza.com/public/884076/mozarab_binding_sample.png "This image shows the 'Bind the Faith to Rome' decision side-by-side. The left side shows the requirements, which state that you must either fulfill all the regular requirements or have a strong hook before being able to make the decision. The right side shows the effects of the decision when you use a strong hook to bypass the regular requirements, which includes the pope disliking you and your hook being consumed.")


*It goes without saying that if you fulfill all requirements, but also have a hook, it will pick the regular outcome before the coercion one.*  

#### Zandaqa can now have their pledge of submission rejected by the Caliph​

Pledging submission to a caliph will send out an actual in-game letter rather than instantly consulting the AI upon selecting the option. If you enjoy playing as a Caliph in multiplayer mode, look forward to deciding the fate of the Zandaqa players for yourself.  

| ![Image of the 'Heirs of the Prophet: Zandaqa' event, where the Zandaqa gets to pick who their head of faith may be. The first option is to elect their own leaders, while the second lets them 'Realign with the Sunni orthodoxy'. The player in this screenshot has their mouse over the second option, which has made a tooltip showing the possible outcomes appear. The first outcome is that the Caliph rejects your pledge, forcing you to select your own head of faith. The second one is that the Caliph accepts your pledge, getting a weak hook on you in the process.](https://forumcontent.paradoxplaza.com/public/884911/zan_new_1.png "Image of the 'Heirs of the Prophet: Zandaqa' event, where the Zandaqa gets to pick who their head of faith may be. The first option is to elect their own leaders, while the second lets them 'Realign with the Sunni orthodoxy'. The player in this screenshot has their mouse over the second option, which has made a tooltip showing the possible outcomes appear. The first outcome is that the Caliph rejects your pledge, forcing you to select your own head of faith. The second one is that the Caliph accepts your pledge, getting a weak hook on you in the process.") | ![Image of the follow-up event that the Caliph receives. It comes in the form of a letter from the Zandaqa player. There are options to accept or decline the pledge, but accepting comes with greater benefits. Both options come with the nice detail of having icons, a designer somewhere in Paradox Interactive probably spent too much time on that.](https://forumcontent.paradoxplaza.com/public/884912/zan_new_2.png "Image of the follow-up event that the Caliph receives. It comes in the form of a letter from the Zandaqa player. There are options to accept or decline the pledge, but accepting comes with greater benefits. Both options come with the nice detail of having icons, a designer somewhere in Paradox Interactive probably spent too much time on that.") |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |



*Alright, that is everything I’ve got to show for now. I hope that we’ve managed to excite you for what’s coming in the immediate future for Crusader Kings. Let us know your thoughts below!*

 

#### Attachments

- [![AFTER_NEW.png](https://forumcontent.paradoxplaza.com/thumbnail/public/883182/AFTER_NEW.png)](https://forum.paradoxplaza.com/forum/attachments/after_new-png.895692/)
  
  AFTER_NEW.png
  3 MB

 · Views: 0

- [![BEFORE_NEW.png](https://forumcontent.paradoxplaza.com/thumbnail/public/883183/BEFORE_NEW.png)](https://forum.paradoxplaza.com/forum/attachments/before_new-png.895693/)
  
  BEFORE_NEW.png
  3 MB

 · Views: 0

<!-- artifact:reactions:start -->
- 115 Like
- 24 Love
- 11 (unlabeled — rendered as base64 data URI)
- 9 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Hugo Cortell](https://forum.paradoxplaza.com/forum/members/hugo-cortell.1630085/)**
Role: Court Horchata Taster (and Game Designer)
Badges: 39
Messages: 6
Reaction score: 425

*[Full game-badge icon list of 39 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
