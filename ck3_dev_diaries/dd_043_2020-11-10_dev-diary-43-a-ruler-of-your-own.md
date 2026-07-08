---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1441657/"
forum_thread_id: 1441657
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 43
title: CK3 Dev Diary 43 - A Ruler of Your Own
dd_date: 2020-11-10
author_handle: blackninja9939
expansion: Post-release patches
patch: Patch 1.2 (Argent)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2482
inline_image_count: 29
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1441657'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1507.jpg?1605016042
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_150_to_152
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_417_to_422
    action: preserved_and_flagged
    counts:
      Like: 199
      Love: 138
      (unlabeled — rendered as base64 data URI): 4
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_430_to_540
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_541_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1507.jpg?1605016042)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary 43 - A Ruler of Your Own

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [Nov 10, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-43-a-ruler-of-your-own.1441657/)
<!-- artifact:thread_metadata:end -->

Hello everyone and welcome to the 43rd CK3 Dev Diary!  

I’m Matthew, one of the Programmers on the CK3 team, and today I am going to talk to you about my little baby from over the past while: the much anticipated Ruler Designer!  

As promised during our lead up to release, the Ruler Designer will be a free feature so everyone can dive into creating their own wonderful (or monstrous) custom character!  

To create a custom character you must select the play/customize any ruler option in the frontend and then pick the realm you want to replace the ruler of.  


![1_RD_FrontendEnter.PNG](https://forumcontent.paradoxplaza.com/public/638645/1_RD_FrontendEnter.PNG "1_RD_FrontendEnter.PNG")


[picture of front end play or create ruler button]  


![2_rd_createinlobby-png.651290](https://forum.paradoxplaza.com/forum/attachments/2_rd_createinlobby-png.651290/?hash=3058244eaf3a023822064f3a007d8a65 "")


[picture of customize ruler button location]  

So without further ado, here is what you’ll be greeted with when you open up the Ruler Designer:  


![3_RD_MainView.PNG](https://forumcontent.paradoxplaza.com/public/638655/3_RD_MainView.PNG "3_RD_MainView.PNG")


[picture of the ruler designer when you open it]  

I’ll go through it step by step as to how you can set up your custom ruler. The left hand side deals with your base choices: first of all on the top left side we’ve got being able to pick your sex and sexual orientation from the options that appear in game.  


![4_RD_TopLeft.PNG](https://forumcontent.paradoxplaza.com/public/638656/4_RD_TopLeft.PNG "4_RD_TopLeft.PNG")


[picture of top left base info section]  

From there you can pick a culture and a faith, they default to those of the character you are replacing but you can open up a collapsible list of the culture groups and religions which contain their related cultures and faiths.  


![5_RD_FaithList.PNG](https://forumcontent.paradoxplaza.com/public/638657/5_RD_FaithList.PNG "5_RD_FaithList.PNG")


[picture of the faith selection list and tooltip]  

In the lower left side you can enter your first name and dynasty name, or randomise it based on your culture or, if religious names exist, your faith. You can also randomise your dynasty and realm coat of arms.  


![6_RD_BottomLeft.PNG](https://forumcontent.paradoxplaza.com/public/638658/6_RD_BottomLeft.PNG "6_RD_BottomLeft.PNG")


[picture of lower left with entered text and randomised coat of arms]  

To ensure we could release the ruler designer in a timely fashion and offer a deep visual cosmetic system for your characters we took the decision to not spend time on a custom coat of arms designer.  
I know this will be a disappointment to some of you, it is to us as well, but we wanted to prioritise giving you all a functional and fun Ruler Designer for the core aspects first.  
We currently support randomising the coat of arms instead, the randomisation rules obey our normal coat of arms generation rules so it will be filled with emblems and designs fitting of your faith, culture, and title.  

For the CK3 Ruler Designer we decided to move away from the restrictions imposed by the CK2 design as we felt it highly limited your ability to make that custom character that you wanted and wanted a free and open approach. This was something the community also felt as various “Ruler Designer Unlocked” mods for CK2 were consistently popular downloads.  
To that end, the points themselves are not a hard limit to your customization and you can exceed them as you wish, but doing so will disallow getting achievements if you would otherwise be able to. But as long as you stay under, and obey the other requirements to get achievements, then you can play with your custom character in achievement runs.  


![7_RD_TopRight_Breakdown.PNG](https://forumcontent.paradoxplaza.com/public/638659/7_RD_TopRight_Breakdown.PNG "7_RD_TopRight_Breakdown.PNG")


[picture of point and breakdown]  

Next you can choose your age and character weight, these not only affect the visuals of your character but also have mechanical impacts on the traits you can choose and the health of your character.  


![8_RD_Old_Fat.PNG](https://forumcontent.paradoxplaza.com/public/638660/8_RD_Old_Fat.PNG "8_RD_Old_Fat.PNG")


[picture of age and weight slider effects]  

Of course we then move onto the ever important traits selection. Clicking on one of the trait slots opens up a menu showing the various traits in that category such as education or personality traits. Every trait has an associated cost in points, though again there is no hard limit on what you can pick except for mechanical limitations like no childhood traits on adults or picking two traits that are opposites of each other.  


![9_RD_TraitList.PNG](https://forumcontent.paradoxplaza.com/public/638661/9_RD_TraitList.PNG "9_RD_TraitList.PNG")


[picture of trait picker with various traits selected]  

You can also modify your character’s base stats if you want that little extra boost in intrigue without wanting to compromise the personality you have built for your character. Increasing your prowess will also increase your physical muscle mass so you can show off your gym gains.  

And finally in the bottom right we have the family section which lets you decide whether your created character should start married or with some children. If you do then your children will look like you, and your spouse if they exist, just like they would in normal gameplay.  


![10_RD_BottomRight.PNG](https://forumcontent.paradoxplaza.com/public/638662/10_RD_BottomRight.PNG "10_RD_BottomRight.PNG")


[bottom section family picture]  

Speaking of which, no custom character creator would be complete without the ability to customise the appearance of your new ruler!  

When you click the change appearance button you are first presented with the ethnicity selection screen. Picking an ethnicity here will randomise within the predefined guidelines of that ethnicity, it doesn’t limit any further customization it just provides the basis.  


![11_RD_EthnicitySelect.PNG](https://forumcontent.paradoxplaza.com/public/638663/11_RD_EthnicitySelect.PNG "11_RD_EthnicitySelect.PNG")


[ethnicity select screen]  

Customizing further gets you into the real meat of the portrait creation process, we’ve got over 90 individual genes spread over 7 anatomical groupings to customize your portrait. Ranging from height and skin colour, to your lip definition and profile, the nose tip detail, and the depth of the eye corner. So safe to say a lot of options to choose from when customizing your character!  


![12_RD_PortraitDetail.PNG](https://forumcontent.paradoxplaza.com/public/638664/12_RD_PortraitDetail.PNG "12_RD_PortraitDetail.PNG")


[detail customization screen body section]  

![13_RD_Detail_Face.PNG](https://forumcontent.paradoxplaza.com/public/638665/13_RD_Detail_Face.PNG "13_RD_Detail_Face.PNG")


[detail customization screen facial structure section]  

The various sliders allow for customising the “strength” of the gene, which ranges from meaning size to intensity depending on the gene. Some of these options come with specific templates as well, they do a modification in a more binary sense such as changing from having a straight nose profile or a hawked one.  


![14_RD_Nose_Straight.PNG](https://forumcontent.paradoxplaza.com/public/638666/14_RD_Nose_Straight.PNG "14_RD_Nose_Straight.PNG")


![15_RD_Nose_Hook.PNG](https://forumcontent.paradoxplaza.com/public/638667/15_RD_Nose_Hook.PNG "15_RD_Nose_Hook.PNG")


[straight nose vs hawk nose]  

One can also pick from a variety of hair, and beard if male, stylings as well. You can of course also pick your hair colour. Though we do have a limited palette as I was sad to find I couldn’t make my self-insert character quite as ginger as I am in real life, though to be fair nothing is quite that orange.  


![16_RD_HairStyles.PNG](https://forumcontent.paradoxplaza.com/public/638669/16_RD_HairStyles.PNG "16_RD_HairStyles.PNG")


[hair styles]  

I think the easiest way to demonstrate it however is a clip of me creating doing a few edits to a character to demonstrate some of the types of changes you can do, you can morph the face to look very different from your randomised baseline if you want to but for this video I kept it to just a few edits.  


[https://www.youtube.com/embed/AXHDsmh8ViE?wmode=opaque](https://www.youtube.com/embed/AXHDsmh8ViE?wmode=opaque)

[video of editing a character portrait]  

You can also copy and paste character DNA so you can share it with your friends and the community if you make a particularly awesome, or absolutely cursed, looking character. As a fun tidibt this works even if you change the sex of your character.  


![18_RD_CopyPasteDna.PNG](https://forumcontent.paradoxplaza.com/public/638672/18_RD_CopyPasteDna.PNG "18_RD_CopyPasteDna.PNG")


[copy and paste dna buttons]  

And once you are finally done with making your new ruler you hit Finalize and away we go! Into the game with our new custom ruler!  


![19_RD_FinalizeCharacter.PNG](https://forumcontent.paradoxplaza.com/public/638673/19_RD_FinalizeCharacter.PNG "19_RD_FinalizeCharacter.PNG")


![20_RD_CharacterInGame.PNG](https://forumcontent.paradoxplaza.com/public/638674/20_RD_CharacterInGame.PNG "20_RD_CharacterInGame.PNG")


[picture of in game ruler made in the designer]  

All of this is usable in multiplayer as well of course, so you and your friends can create custom rulers in multiplayer games together.  

As I said at the beginning of this dev diary, the Ruler Designer will be a free feature in the upcoming 1.2 patch. We are not ready to give an exact release date at this time but the aim is for it to be out before the end of the year.  

I hope this has got you excited for creating your own ruler!  

**Making the ~~Sausage~~ Feature**  
I thought it would be fun to detail a little bit the process I went through of making a full feature from scratch, to show the various things that go into it from our perspective because making games is an otherwise weirdly secretive process these days compared to the creation of other media like movies, television, or music.  

To start off a lot of estimations and scoping of the feature were done by the team, very important work but also not particularly interesting screenshot wise so I’m gonna skip over it and get to when I started doing the implementation. Needless to say all of the images are of older versions with my beautiful placeholder art, thankfully our artists came in and prettied it all up in the current version!  

First of all I just wanted a window that showed you some character and when you clicked a button it made that character, to start with everything being random like traits, name and portrait was fine.  


![1_Making_RD.png](https://forumcontent.paradoxplaza.com/public/638675/1_Making_RD.png "1_Making_RD.png")


[image of the initial portrait and button]  

Once I had that going I could then start exposing more things to the interface to be modified, I did the left side of the screen first as it makes up the section that doesn’t cost points to change like name and culture selection.  


![2_Making_RD.png](https://forumcontent.paradoxplaza.com/public/638676/2_Making_RD.png "2_Making_RD.png")


[image of wip left side of screen]  

From there I set up the layout of the right side of the screen, though I left that to fill out later as part of another task as I wanted to spend time getting the portrait customization working.  


![3_Making_RD.png](https://forumcontent.paradoxplaza.com/public/638677/3_Making_RD.png "3_Making_RD.png")


[image of wip right side of screen]  

Adding in all the portrait editing was where a good chunk of time was spent, compared to CK2 our portraits were a lot more complex so just having a few options per category would not work, instead we wanted full sliders for controlling the exact intensity of various genes. Some genes were also mirror of each other, like ear size positive and ear size negative, to make sure they were not two separate sliders or buttons I added in logic so combine them into one slider with the midpoint being zero for both and then scaling the intensity from there.  


![4_Making_RD.png](https://forumcontent.paradoxplaza.com/public/638678/4_Making_RD.png "4_Making_RD.png")


![5_Making_RD.png](https://forumcontent.paradoxplaza.com/public/638679/5_Making_RD.png "5_Making_RD.png")


[image of initial portrait editing]  

This portrait editing led to some bugs to fix such as some vaguely skeleton looking characters missing most of their face from being rendered.  


![6_Making_RD.png](https://forumcontent.paradoxplaza.com/public/638680/6_Making_RD.png "6_Making_RD.png")


[image of horror show clipping face]  

After getting all the portrait options setup and working it was then onto the final stage of being able to customise your age and traits and family generation. Thankfully our code was already set up nicely so every character is generated through the same code path, so changing these base values was already unified so it was mostly a matter of tying the UI into doing this in a neat way.  


![7_Making_RD.png](https://forumcontent.paradoxplaza.com/public/638681/7_Making_RD.png "7_Making_RD.png")


[image of right side more finished]  

Which led to some fun issues when I used the wrong UI box type and the traits section could grow to be huge if you added to many.  


![8_Making_RD.png](https://forumcontent.paradoxplaza.com/public/638682/8_Making_RD.png "8_Making_RD.png")


[image of traits growing instead of overlapping]  

The points now actually mattering meant I needed to fix up our achievement settings to check for that and make sure our characters were known if they came from the ruler designer or not.  

With our portraits editable and traits pickable it was then time to make sure that picking a trait which changes the portrait would also show up in game, I had to re-work how the traits were handled for this because the base portrait modifier system wants a character and in the ruler designer we don’t actually have a real character we just have a bunch of raw components needed to make one when we finalize.  
Adding this in gave me some absolutely cursed portraits when stacking all the visual illness traits, do not open unless you are ok with some gross looking portraits:  


Spoiler: Gross Illness Portrait

![9_Making_RD.png](https://forumcontent.paradoxplaza.com/public/638686/9_Making_RD.png "9_Making_RD.png")

[all sickness trait image]  

Finally it was a matter of tidying up some things, fixing a few bugs and adding the last bits of polish to the UI feel. Art had been going through once I had got the core features done and were making the UI look good and remove all my placeholders. After all of that and some QA testing for me to fix those last bugs, so much fun with fixing multiplayer issues, we were all done!  

I hope this unveiled a bit about how making a feature happens, it was very high level and I avoided the nitty gritty details of it, but I think it can still be illuminating to see the work and various stages of development that go into making a brand new feature!

 

#### Attachments

- [![2_RD_CreateInLobby.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/638649/2_RD_CreateInLobby.PNG)](https://forum.paradoxplaza.com/forum/attachments/2_rd_createinlobby-png.651290/)
  
  2_RD_CreateInLobby.PNG
  673,9 KB

 · Views: 0

- [![18_RD_CopyPasteDna.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/638671/18_RD_CopyPasteDna.PNG)](https://forum.paradoxplaza.com/forum/attachments/18_rd_copypastedna-png.651312/)
  
  18_RD_CopyPasteDna.PNG
  67,1 KB

 · Views: 0

<!-- artifact:reactions:start -->
- 199 Like
- 138 Love
- 13 (unlabeled — rendered as base64 data URI)
- 13 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)**
Role: Former Senior Programmer - Crusader Kings 3
Badges: 99
Reaction score: 8,575

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
