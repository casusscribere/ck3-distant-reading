---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1489219/"
forum_thread_id: 1489219
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 71
title: "CK3 Dev Diary #71: A Coat of Arms of Your Own"
dd_date: 2021-08-31
author_handle: blackninja9939
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1193
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1489219'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1690.jpg?1630408091
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_150_to_152
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_241_to_246
    action: preserved_and_flagged
    counts:
      Love: 239
      Like: 108
      (unlabeled — rendered as base64 data URI): 2
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_254_to_313
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_314_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1690.jpg?1630408091)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #71: A Coat of Arms of Your Own

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [Aug 31, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-71-a-coat-of-arms-of-your-own.1489219/)
<!-- artifact:thread_metadata:end -->

Hello everyone and welcome to the 71st CK3 Dev Diary!  

I’m Matthew, one of the Programmers on the CK3 team, and today I am going to talk to you about one of the free features in the upcoming 1.5 patch: the much requested Coat of Arms Designer!  

I don’t think the idea needs much explanation, this feature lets you edit the coat of arms used for your titles, dynasty, and house in game and from within the ruler designer to create your own stunning medieval crest.  

I think it's easiest if I just show you, should go without saying by now but everything here is still under development and the interface is a work in progress and stands to be tweaked, shuffled around the layout and sizes changed by art.  
But right now here is what you will be greeted by now if you enter the customization window for the Holy Roman Empire:  

![1_main_screen.PNG](https://forumcontent.paradoxplaza.com/public/739696/1_main_screen.PNG "1_main_screen.PNG")



In the center you get the preview screen of the coat of arms as you edit it and to the right some options of what to do.  
I’ll start with the bottom right options:  


- Randomise within the rule sets we use to generate coat of arms normally, great if you want to reenact this [pain](https://www.reddit.com/r/CrusaderKings/comments/p72uo1/what_a_nice_day_to_start_a_new_game/).
- As with the Ruler Designer’s DNA we let you copy and paste your coat of arms to share.
- Discard any changes you’ve made to your work in progress masterpiece.
- If you have previously edited and saved your new coat of arms then the discard button will be joined by a button to reset to the historical coat of arms if available.

The meat of the system comes in the form of customizing your coat of arms from scratch or adjusting the existing one, both share their core components but adjusted mode is more limited if you want to take a pre-existing coat of arms and just tweak it a bit.  
The reason adjusted mode is separate is that some historical coat of arms are made up of a lot of emblems in an order that whilst looks pretty in game is rather cursed if you were to try and see the full layout and background usage.  

So for the bulk of this I will be using custom as the example to see how you can make your own heraldry from scratch and call out differences in adjusted mode where applicable.  
The coat of arms designer has three main panels: background, layout, and emblems.  

Starting with the background panel you can pick from any of the background patterns as well as pick what colours should be used. For all the colouring options in the coat of arms designer we provided a palette with some pre-selected colours that are used in heraldry generally and are what we use in randomization of coat of arms but we also give you a colour picker to let you pick whatever horrifying neon colour you want.  
In the adjusted mode you cannot pick a background pattern but you can change the colours.  

![2_background_panel.PNG](https://forumcontent.paradoxplaza.com/public/739697/2_background_panel.PNG "2_background_panel.PNG")



Next up we have the layouts panel, they dictate the overall amount and positioning of the emblems in your coat of arms. This panel is disabled entirely in the adjusted mode.  

To preempt this question, yes there are only a few layouts in the picture (some even duplicates) and that is because the other preset layouts are currently being worked on so there will be more than this in the released version.  
Though if you have any ideas for some cool layouts do let us know! Now is the perfect time to give us some ideas whilst the presets layouts are being implemented.  

![3_layouts_panel.PNG](https://forumcontent.paradoxplaza.com/public/739698/3_layouts_panel.PNG "3_layouts_panel.PNG")



The bulk of time you will spend is likely to be in the final emblems panel, this lets you pick which of the over a thousand emblem textures that you want to use as well as how you colour them.  

You can select which emblem instance you want to edit or select multiple of them by shift clicking, there is also a button to select all of them or reset your selection too so you can edit in bulk easier.  

![4_emblem_panel.PNG](https://forumcontent.paradoxplaza.com/public/739699/4_emblem_panel.PNG "4_emblem_panel.PNG")


![5_color_picker.PNG](https://forumcontent.paradoxplaza.com/public/739700/5_color_picker.PNG "5_color_picker.PNG")



Since some historical coat of arms can have a lotttt of emblems we show them in a paged setup of 10 at a time for easier editing.  
I used france a lot in my testing since it has so many to make sure things always worked on a large amount of them which has now ingrained into my brain that our france coat of arms has 33 fleur de lis on it.  

To try and help the contrast of the emblems we set it so that the previews have a background that is either white/black to help things stand out better.  

We also have a detailed edit mode which lets you go deeper and modify the exact positions, scale, and rotation of all your emblems as well as modify what layer they are on and even add and remove them to your heart’s content!  
The UI of this mode is especially work in progress, especially the layering part of it, that will be tidied up before the release.  

With the detail edit mode you can really end up with a custom coat of arms to represent the majesty of your dynasty, or as I’m sure some of you will do, try and find a way to make it look phallic as quickly as you possibly can.  

![6_detail_edit_layers.PNG](https://forumcontent.paradoxplaza.com/public/739701/6_detail_edit_layers.PNG "6_detail_edit_layers.PNG")


![7_detail_edit_values.PNG](https://forumcontent.paradoxplaza.com/public/739702/7_detail_edit_values.PNG "7_detail_edit_values.PNG")



All of these edits also support an undo/redo system to make incremental changes easier.  
Cadet Houses also get an additional option for if they want the quartering of their coat of arms enabled or not, in case you want to show your dad who’s boss.  

That is a lot of words to explain this but let's be honest you all just want to see it in action so here we go:  


[https://www.youtube.com/embed/ByJNLK73sK4?wmode=opaque](https://www.youtube.com/embed/ByJNLK73sK4?wmode=opaque)


Mini-shout out/commiserations to user “Lajos Tueur” who on Saturday released a [mod](https://steamcommunity.com/sharedfiles/filedetails/?id=2587306153) to try and implement a coat of arms designer and had to fight against doing all of this very manually in the script with a hacky UI only for me to come in a few days later and release this dev diary.  

That’s all for this week folks, thanks for tuning in and I hope you’re excited to make some majestic (or cursed) coat of arms for your rulers in 1.5!

<!-- artifact:reactions:start -->
- 239 Love
- 108 Like
- 14 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 Haha
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)**
Role: Former Senior Programmer - Crusader Kings 3
Badges: 99
Reaction score: 8,575
<!-- artifact:op_signature:end -->
