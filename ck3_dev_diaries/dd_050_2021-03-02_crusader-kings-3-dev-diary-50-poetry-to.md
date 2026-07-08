---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1460062/"
forum_thread_id: 1460062
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 50
title: "Crusader Kings 3 Dev Diary #50 - Poetry to my Ears"
dd_date: 2021-03-02
author_handle: Wokeg
expansion: Northern Lords
patch: Patch 1.3 (Corvus)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1448
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1460062'
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
    location: raw_lines_~28_to_143
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_142
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1570.jpg?1614694205
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_145_to_147
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_308_to_313
    action: preserved_and_flagged
    counts:
      Like: 210
      Love: 57
      (unlabeled — rendered as base64 data URI): 8
      Haha: 14
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_321_to_395
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_396_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1570.jpg?1614694205)
<!-- artifact:thread_banner:end -->

# Crusader Kings 3 Dev Diary #50 - Poetry to my Ears

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Mar 2, 2021](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-50-poetry-to-my-ears.1460062/)
<!-- artifact:thread_metadata:end -->

### Crusader Kings 3 Dev Diary #50 - Poetry to my Ears​

Welcome, comrades, to the latest dev diary, and let’s all give an especially warm welcome to the poet trait! This venerable little piece of content is making a triumphant return from the annals of CK2 as part of the 1.3 free patch.  

This ain’t just your CK2 poet trait, though, this is the all *new* poet trait: reworked stats, a character interaction, and (for which I am so very, very sorry) randomised poetry generation.  

![ag0OSLonNk6WsHbkYpRUfnj5pENtksF3VCe1gKqj0ufCj3K9r8Hd3Socvs0Ixjc0OKgJVMpD6JA9GDm1moMix4NG6y5MTs2Smh0J0jks1g-PdzUOBdnivh3jf5Iwk5wExPYhBaMn](https://lh3.googleusercontent.com/ag0OSLonNk6WsHbkYpRUfnj5pENtksF3VCe1gKqj0ufCj3K9r8Hd3Socvs0Ixjc0OKgJVMpD6JA9GDm1moMix4NG6y5MTs2Smh0J0jks1g-PdzUOBdnivh3jf5Iwk5wExPYhBaMn "")



Oh yeah, *we’re doing this*.  

### Writing a Poem​

First, a little detour into how poetry works. Every poem has a theme, and, at present, we have five themes to choose from:  


1. Romance - in which the poet expresses affection and desire for the subject.
2. Legacy - in which the poet muses on the nature of death and power, and the subject’s impact on the world.
3. Mourning - in which the poet discusses the death and lingering emotions left behind after the subject, or a relative of theirs, passes away.
4. Strife - where the poet expounds on the necessity of seizing power, life, and opportunity when it appears, and on glories yet to be won.
5. Incompetence - wherein the poet slams the subject for their weakness, incompetence, and method of eating asparagus.

![v16SFREuLVjvYnq0rMrI4sMxbYpcJdh7F0-Cebt0HveUu91V6mlsMImgLsGpXKqG2aOQmhtl865uK5if1C7teqV3wyfsdYmfyLPkdKaTo9NWNooGKpl6PdRiuoM8W1QpByvu7DmM](https://lh6.googleusercontent.com/v16SFREuLVjvYnq0rMrI4sMxbYpcJdh7F0-Cebt0HveUu91V6mlsMImgLsGpXKqG2aOQmhtl865uK5if1C7teqV3wyfsdYmfyLPkdKaTo9NWNooGKpl6PdRiuoM8W1QpByvu7DmM "")



Once we know the theme and subject (if any), we can feed that into custom localisation functions that randomise a couplet. At present, we have both intro and outro functions for each theme, as well as title generation, allowing us to generate ditties between two and four lines in length plus title, though I hope to expand on these in future.  

Since these are just ordinary custom locs, they can be dropped into any event or event chain fairly easily, meaning we can auto-generate bad poetry *anywhere* in future.  

Let’s have some examples. Here’s a love poem to the woman that Lord Elisedd ap Tewdwr never quite met:  


![Kocl7xWoncPloG33_qfFvhH4PnF9hnzY0SUIvmatCDvPopnszEqgLXqcMQbYnsa9gipCKWt_FxXEadCZ2YyU2shPDLAV3dlc5Ub0k034OFC0dMlgBtsMDno5gQRi6757MDD_qfWM](https://lh4.googleusercontent.com/Kocl7xWoncPloG33_qfFvhH4PnF9hnzY0SUIvmatCDvPopnszEqgLXqcMQbYnsa9gipCKWt_FxXEadCZ2YyU2shPDLAV3dlc5Ub0k034OFC0dMlgBtsMDno5gQRi6757MDD_qfWM "")



And another, as he ruminates on the problems of succession:  


![0eBBV5BM_cMKqLyCqQRFowOTlqz_W7ColX09Q1CRQVEQagzvRsKLzq-7JKuW7ZpIusw055ToQbssdi4oC-5ikTN6laNnuTtCC6Yf_J393vdrCz0FjJLQ_ynBt0Jf3J9m3OTlAiyw](https://lh3.googleusercontent.com/0eBBV5BM_cMKqLyCqQRFowOTlqz_W7ColX09Q1CRQVEQagzvRsKLzq-7JKuW7ZpIusw055ToQbssdi4oC-5ikTN6laNnuTtCC6Yf_J393vdrCz0FjJLQ_ynBt0Jf3J9m3OTlAiyw "")



And a third, where the lord laments the success of Prince Rhodri ap Merfyn in northern Wales:  


![swutZdgi9XHijMQqywuSIuXTIq4Qf0tJFe9VLX-wyAfkXLA6oqUcgO1Cl7Fk8le7GEaquLFU8RbQlXmcOkQt0f6FrQ3r6yqSt85wjd3DFiDKiq741BmjCCxOo3Qnpd1Y-DXlK-JJ](https://lh5.googleusercontent.com/swutZdgi9XHijMQqywuSIuXTIq4Qf0tJFe9VLX-wyAfkXLA6oqUcgO1Cl7Fk8le7GEaquLFU8RbQlXmcOkQt0f6FrQ3r6yqSt85wjd3DFiDKiq741BmjCCxOo3Qnpd1Y-DXlK-JJ "")



### Use​

So, that’s all well and good (or, y’know, utterly horrible if you have any command of basic rhyming), but how do we actually use poems in-game? A few ways!  

Firstly, we have the triumphant return of the V-completelyoriginal tortuous poetry interaction variant:  


![eUv8Mr79GthgJb_VAEbGMk9ABw0cWnIlPNnuxcaqBQa46NaTzXOBTqtNOGz53PYeeqFZ6MFn6uylHRzcjoxtW13UZBX12dorCbCnxwxkaJLu9LfpRHGbutiUHFcV6Cs6JS-g3kXI](https://lh5.googleusercontent.com/eUv8Mr79GthgJb_VAEbGMk9ABw0cWnIlPNnuxcaqBQa46NaTzXOBTqtNOGz53PYeeqFZ6MFn6uylHRzcjoxtW13UZBX12dorCbCnxwxkaJLu9LfpRHGbutiUHFcV6Cs6JS-g3kXI "")



Characters who are poets and elect to torture their prisoners will, frequently, spend hours declaiming their very *worst* poetry to them. As with any use of the torture interaction, this can cause a hideous amount of stress.  

More than this, though, poets can also send poems to most characters within diplomatic range. In all instances, sending a poem costs a little prestige, but the effects available depend on the theme selected, and the themes available depend on who you’re writing to.  

A romantic poem makes the subject like you, a poem about their legacy makes them like you and gives them a little piety, a poem about strife makes them like you and gives them a little prestige, and a poem about mourning makes them like you and gives them a little stress loss. Unless, of course, they dislike the poem and publicly mock you for it...  

![8d1P1mNWcKTqwz-3THzVX37KHmlz3TMqUUV0MWH0ggMhboji2o3hbcx83va4W4oZwolSQtOvBTPOWMDVWCFE3Z-pSpQoLMDNLNtxUGiXwyt99DIjfNq-kcsJDhoFHJ43SNsHxyfv](https://lh6.googleusercontent.com/8d1P1mNWcKTqwz-3THzVX37KHmlz3TMqUUV0MWH0ggMhboji2o3hbcx83va4W4oZwolSQtOvBTPOWMDVWCFE3Z-pSpQoLMDNLNtxUGiXwyt99DIjfNq-kcsJDhoFHJ43SNsHxyfv "")



Some poems are quite flattering to receive, and may well be accepted without question:  


![wLEWk1UlrkHGFtic_G3qOdoGNUs57NwsKlOd3Kd-Fq7tGT0yV-mmgzQA90cROWPV5mWdrCljgMXQ7ab7rYcVE2dy5dK2kj2t5LtAip7gGXLLONtaAKo9qixUDldsC2V75P4a0G7f](https://lh6.googleusercontent.com/wLEWk1UlrkHGFtic_G3qOdoGNUs57NwsKlOd3Kd-Fq7tGT0yV-mmgzQA90cROWPV5mWdrCljgMXQ7ab7rYcVE2dy5dK2kj2t5LtAip7gGXLLONtaAKo9qixUDldsC2V75P4a0G7f "")



Whilst others are… less polite.  

![qwlLx6xK_frI9Wlbxh2RjdWlk_XeVmyadTBtJ6DmBYFEfO7tZIxo35a1iRQsgrdjxLap8zcxUMzgUYKM3EwV-4Xc13O9V2gl428SY65O5lVebdFdt2XChgVe0QLqdYvrxFYhTPS7](https://lh3.googleusercontent.com/qwlLx6xK_frI9Wlbxh2RjdWlk_XeVmyadTBtJ6DmBYFEfO7tZIxo35a1iRQsgrdjxLap8zcxUMzgUYKM3EwV-4Xc13O9V2gl428SY65O5lVebdFdt2XChgVe0QLqdYvrxFYhTPS7 "")



And yes, these are all useable in MP.  

Just for fun, let’s have a few out-of-context poems.  

![7Gl3NKTXOHmYSXg0sp9ouEUF2D-Gv2VJGxGCB9j9Y2XswJAJom2ruVm6qp9MDdwK6VLrmufmgDbpHLG3c6IyY3MkNoN2FpV8MbK5La6L1K1GAsDhOLgN02UiAOcb1OTcEaE1k25W](https://lh4.googleusercontent.com/7Gl3NKTXOHmYSXg0sp9ouEUF2D-Gv2VJGxGCB9j9Y2XswJAJom2ruVm6qp9MDdwK6VLrmufmgDbpHLG3c6IyY3MkNoN2FpV8MbK5La6L1K1GAsDhOLgN02UiAOcb1OTcEaE1k25W "")


![YSlOzkqxFYl9PpotmjNc_YTBssvyRRvN1YgxhJtJkzH3FGge6yJw-yBkf_5ib0zYlVOs3nxclEL58rr8bjCEG0T2oik6g65XcNfKmLH9JYo791XSC8A2THCBwvyhVNiWBidoqcO0](https://lh4.googleusercontent.com/YSlOzkqxFYl9PpotmjNc_YTBssvyRRvN1YgxhJtJkzH3FGge6yJw-yBkf_5ib0zYlVOs3nxclEL58rr8bjCEG0T2oik6g65XcNfKmLH9JYo791XSC8A2THCBwvyhVNiWBidoqcO0 "")


![Yuuvl-h3gL8XxJ3mcnmZLNLrHKMC5SPNQ1wwcSgI7-yvGklYL5rFo6WuYFQ5g6GbWmEVbp9LEcozcI-x2XnPNb2i5e7qtZaUaOjt4FMsY1MEgfL41EVRBjWDCTrlyGa_9eYQsKwg](https://lh5.googleusercontent.com/Yuuvl-h3gL8XxJ3mcnmZLNLrHKMC5SPNQ1wwcSgI7-yvGklYL5rFo6WuYFQ5g6GbWmEVbp9LEcozcI-x2XnPNb2i5e7qtZaUaOjt4FMsY1MEgfL41EVRBjWDCTrlyGa_9eYQsKwg "")


![Bbdl2e3ccG1Lq9hvV0NqWUR_oa8Y52I4AvI_tK6VO_80YxUFXn2-FkBy1W2ghSGLInO3I51lI-nVoWA8uhnsidA5UMB_7wULfVqu3vDSGpvr4QxzUvjFncLT--FFPM0ySl-o7w2Z](https://lh5.googleusercontent.com/Bbdl2e3ccG1Lq9hvV0NqWUR_oa8Y52I4AvI_tK6VO_80YxUFXn2-FkBy1W2ghSGLInO3I51lI-nVoWA8uhnsidA5UMB_7wULfVqu3vDSGpvr4QxzUvjFncLT--FFPM0ySl-o7w2Z "")


![4_wkmVxd545rh6M1hP7V1M0mCk24lS1Ip3IZwpSCe94uSPMhlAjtgzP2_r6VGQREhXR2IRVfIKQ1YlCuu-wUOfiVR6JNYel8Hlmt1t_8VJucuteKSSlyb4_r7KVPbm3YUYNGedM_](https://lh3.googleusercontent.com/4_wkmVxd545rh6M1hP7V1M0mCk24lS1Ip3IZwpSCe94uSPMhlAjtgzP2_r6VGQREhXR2IRVfIKQ1YlCuu-wUOfiVR6JNYel8Hlmt1t_8VJucuteKSSlyb4_r7KVPbm3YUYNGedM_ "")


![xbtg7UMcO7UH4qkUY18OuSp1uXagRw5uMex7TiP2AQuhom_VaGbZO9V6zra0PDMm4WuvUKsghcOi0F6x3nZHvhYvsabKzvZh1Q4Ztg87GwBpP7iFwXt0h4xh6IO-0Gai-2jmZdgS](https://lh3.googleusercontent.com/xbtg7UMcO7UH4qkUY18OuSp1uXagRw5uMex7TiP2AQuhom_VaGbZO9V6zra0PDMm4WuvUKsghcOi0F6x3nZHvhYvsabKzvZh1Q4Ztg87GwBpP7iFwXt0h4xh6IO-0Gai-2jmZdgS "")



To round off this DD, we'd like to give you a sneak peek at some of the upcoming fixes & changes in the 1.3 patch. These aren't the full patch notes! More will come in upcoming DDs.  


Spoiler: Patch Notes

###################  
# Balance  
###################  
- Men-at-Arms, Special Troops and Mercenaries now have travel time and, like Levies, have a penalty to disband/re-raise during wars. Travel time is based on the distance to the realm capital. This should effectively stop being able to ‘teleport’ MaA across the map  
- The renown cost of acquiring Dynasty Legacies has been overhauled. Instead a linear progression (1000, 2000, 3000… etc.) the cost is now dynamic. It should be much easier to unlock your first few Legacy perks, but significantly harder to unlock all Legacies in the game.  
- All Dynasty Legacy perks have been rebalanced. Their effects should now be much more tangible and interesting.  
- The Yearly Event pools have been restructured, and a lot of triggers loosened or removed outright. In practice this means that you’ll see more events when playing (roughly one random event from this pool every 4 years rather than every 5-6 years). This also means that some extremely rare events will now appear more frequently.  
- The Infirm trait events have been moved from the Yearly pulse to the Health pulse. What this means is that all characters can now become infirm, not only rulers. It is also much more likely for elderly characters to actually get the trait.  
- Grandchildren and Great-Grandchildren should no longer wander off, following the same rules as Children  
- Married characters will no longer wander off if they are in a realm where they are subservient to the other part of the marriage, and their spouse is in the same court  
- You can now Disinherit people outside your diplomatic range  
- AI rulers who form an alliance in the middle of a war now wait 1 month before calling their new ally to arms.  
- Feudalizing as a Tribe no longer requires all Tribal-Era innovations, now you only need 70% (9) of all Civic & Military Innovations  
- You will no longer get stress from Parents or Siblings dying of old age when they're 65 or older (if they're friends or lovers you might still get stress, though)  
... and many more [will be posted in future DDs]  

###################  
# Interface  
###################  
- Hovering over the unit plate of a friendly unit now shows its full path. Great for seeing where your allies are going  
- Players now receive a warning when their enemy in a war forms a new alliance  
- Updated the Current Situation widget with a fresh new coat of paint. It’s now darker with more muted colors, and some flavorful decor.  
- Current Situation entries now only show ‘X’ to close when hovered  
- Added a Current Situation item for hooks about to expire; it'll tell you when a hook expires in less than 3 months  
- Added a message that lets the employer know if their councilors leave because of marriage or title inheritance  
- Building a new holding will now in the Domain view say you're building the holding type (E.G., "Castle") rather than the name of the main building (E.G., "Motte")  
- Ensured scheme success and secrecy modifiers show up as percentages in all cases  
... and many more [will be posted in future DDs]  

###################  
# Game Content  
###################  
- All formerly inaccessible Religious Clothes/Headgear are now accessible in the Barbershop. You want to wear the Pope’s hat and Steppe Pagan robes? Go right ahead!  
- Added a small interaction to pardon a subject’s crimes in exchange for opinion.  
- A guardian might now get a hook on their ward, should they be of a greedy/deceitful persuasion  
- You can now offer concubines and consorts to other characters!  
- When Offering Vassalization to a feudal ruler, you may now offer a more lenient Contract to improve their chance of accepting.  
- Added a narrative event for converting to a new Faith, as well as a notification for when your liege converts to a new Faith.  
... and many more [will be posted in future DDs]


Well, that’s all from me for this week, but stay tuned for next week’s diary, where we’ll be getting into something a little less *passive* aggressive.

<!-- artifact:reactions:start -->
- 210 Like
- 57 Love
- 15 (unlabeled — rendered as base64 data URI)
- 14 Haha
- 9 (unlabeled — rendered as base64 data URI)
- 8 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)**
Role: Former CK3 Experienced Game Designer
Badges: 16
Messages: 528
Reaction score: 15,169

*[Full game-badge icon list of 16 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
