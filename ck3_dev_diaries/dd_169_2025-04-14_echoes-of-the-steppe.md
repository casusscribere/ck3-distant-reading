---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1735434/"
forum_thread_id: 1735434
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 169
title: "Dev Diary #169 - Echoes of the Steppe"
dd_date: 2025-04-14
author_handle: PDX-Trinexx
expansion: Khans of the Steppe
patch: Patch 1.16
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2122
inline_image_count: 35
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1735434'
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
    location: raw_lines_~28_to_151
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_153_to_155
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_402_to_406
    action: preserved_and_flagged
    counts:
      Like: 94
      Love: 56
      (unlabeled — rendered as base64 data URI): 3
      Haha: 1
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_414_to_515
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_516_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #169 - Echoes of the Steppe

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Apr 14, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-169-echoes-of-the-steppe.1735434/)
<!-- artifact:thread_metadata:end -->

Hello everyone! Today's dev diary is written by two separate authors, and covers the art and music of Khans of the Steppe. There's a good bit to cover, so let's dive right into it.  

---

**Art & References**  

Salve,  
Lucas Ribeiro here, 2D Art Lead at CKIII. I’m here to share with you our efforts to bring to life the beautiful open splendor of the steppes and the blood-stained battlefields of the east through our humble artwork.  

### Loading Screen​

To start off, let’s talk about our new loading screen. We began by sketching out some ideas and running them through the team to get impressions. There was not much debate on what the theme was here, mostly how to represent it.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1273719/image_01.png "image_01.png")



From these 4, we picked the one with the charging band of warriors against the stormy sky. We felt that this composition had a lot of dynamism and looked unique compared to the other loading screens we’ve created so far. The juxtaposition of the riding band of warriors against the stormy skies suggests the strong connection between nature and the lifestyle of the steppe nomads.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1273720/image_02.png "image_02.png")



As a second step, we created a few different color sketches. We opted for the one where we could see a stormy sky against a calmer golden haze. This served two purposes: To correlate the riders with the encroaching tempest and to show the gameplay feature of the changing seasons.  

![image_03.jpeg](https://forumcontent.paradoxplaza.com/public/1273721/image_03.jpeg "image_03.jpeg")



For our nomad dynastic legacy we thought we could use the opportunity of a horizontal layout to display a big migrating wave, stretching towards the horizon.  

![image_04.jpeg](https://forumcontent.paradoxplaza.com/public/1273722/image_04.jpeg "image_04.jpeg")



### Event Backgrounds​

While we had a few steppe themed event backgrounds, we made sure to cover every sort of event theme with new and appropriate steppe backgrounds. Amongst these are Oovos, A camp at night and day, the inside of a nomadic tent, Karakorum, Hunt, Throne Room, An eastern village (and their burning version), different versions of a steppe background and many more.  

![image_05.jpeg](https://forumcontent.paradoxplaza.com/public/1274263/image_05.jpeg "image_05.jpeg")


![image_06.jpeg](https://forumcontent.paradoxplaza.com/public/1273725/image_06.jpeg "image_06.jpeg")


![image_07.jpeg](https://forumcontent.paradoxplaza.com/public/1273726/image_07.jpeg "image_07.jpeg")


![image_08.jpeg](https://forumcontent.paradoxplaza.com/public/1273728/image_08.jpeg "image_08.jpeg")


![image_09.jpeg](https://forumcontent.paradoxplaza.com/public/1273729/image_09.jpeg "image_09.jpeg")


![image_11.jpeg](https://forumcontent.paradoxplaza.com/public/1273731/image_11.jpeg "image_11.jpeg")

![image_10.jpeg](https://forumcontent.paradoxplaza.com/public/1273730/image_10.jpeg "image_10.jpeg")



We also have new holding illustrations for nomadic and herder governments:  

![image_12.jpeg](https://forumcontent.paradoxplaza.com/public/1273732/image_12.jpeg "image_12.jpeg")


![image_13.jpeg](https://forumcontent.paradoxplaza.com/public/1273733/image_13.jpeg "image_13.jpeg")



**Activity Types**  
We have added 2 unique activity types for Mongols. A new type of feast, the Tsagaan Sar. And a new type of hunt, the Nerge.  

For the Tsagaan Sar, we wanted to show the participants wearing white, as is customary. The plentifulness of food is represented by the bowls and baskets of treats. And the tradition of bringing the Khan gifts is also present in the image.  

In the Nerge hunt, riders would work together to round up animals from all across the region for their ultimate slaughter once surrounded by a veritable army of hunters. We tried to represent this encirclement by how the characters occupy the composition. The animals are seen in desperate flight, while the men are positioned on both sides of them.  

![image_14-15.png](https://forumcontent.paradoxplaza.com/public/1273765/image_14-15.png "image_14-15.png")



**Men-at-Arms**  
The nomad experience is closely associated with warfare, as such, we knew we had to give them a significant variety of men-at-arms. We also have many different steppe cultures and the men-at-arms gave us the opportunity to make them a bit more unique.  

![image_16-22.png](https://forumcontent.paradoxplaza.com/public/1273768/image_16-22.png "image_16-22.png")



**Character Art**  
While we fortunately had some Mongol culture clothes and headgear in the game, the variety was quite small. With Khans of the Steppe we had the chance to greatly expand this repertoire.  

![image_23.png](https://forumcontent.paradoxplaza.com/public/1273744/image_23.png "image_23.png")



As with every expansion, we dedicated a significant amount of time to collect references, preferably accounts or representations closer to our time period. When references are a bit fuzzy on the details or a bit too abstract, we take to the drawing board and come up with some concepts that help solidify these ideas. Here are a few examples:  

![image_24.jpeg](https://forumcontent.paradoxplaza.com/public/1273745/image_24.jpeg "image_24.jpeg")


*[Mongol imperial Clothes]*  

![image_25.jpeg](https://forumcontent.paradoxplaza.com/public/1273746/image_25.jpeg "image_25.jpeg")


*[Steppe Feathered Hat]*  

![image_26.jpeg](https://forumcontent.paradoxplaza.com/public/1273747/image_26.jpeg "image_26.jpeg")


*[Yuan Style Mongol Armor]*  

![image_27.jpeg](https://forumcontent.paradoxplaza.com/public/1273748/image_27.jpeg "image_27.jpeg")


![image_28.jpeg](https://forumcontent.paradoxplaza.com/public/1273749/image_28.jpeg "image_28.jpeg")




**Animation**  
Our original animations for travelling characters and marching armies felt quite insufficient when depicting peoples that spent so much of their time on the saddle. To remedy this we have given nomadic travelling characters and military units a horse and animations to go with it. Your armies will now siege enemy holdings while still astride their steeds.  

![image_29.gif](https://forumcontent.paradoxplaza.com/public/1273750/image_29.gif "image_29.gif")


*[Chasing enemies]*  

![image_30.gif](https://forumcontent.paradoxplaza.com/public/1273751/image_30.gif "image_30.gif")


*[Celebrating victory]*  

![image_31.gif](https://forumcontent.paradoxplaza.com/public/1273752/image_31.gif "image_31.gif")


*[Rearing up]*  

![image_32.gif](https://forumcontent.paradoxplaza.com/public/1273753/image_32.gif "image_32.gif")


*[Galloping]*  

We also have a unique model for when you migrate your nomadic camp. Your people are represented by a wheeled yurt being pulled by oxen.  

![image_33.jpeg](https://forumcontent.paradoxplaza.com/public/1273754/image_33.jpeg "image_33.jpeg")




**The Map**  
As might’ve been touched on in previous development diaries, the steppe regions include seasons, a mechanic with significant gameplay implications. We felt that it was necessary to clearly reflect these changes on the map, so that the player could tell something has changed. So, whenever a White Zud hits, you will see the landscape covered in thick white snow. When a season has an Everlasting Summer, vivid green patches will creep even amongst formerly dry terrain.  

Steppe nomads now have their own holding graphics. Yurts with colorful roofs surround the magnificent tent of the Khan. On Tengri temple holdings, ovoos are decorated with colorful flags. We came to a dilemma, though, regarding holding walls. While it would make sense to not display any walls, specially beyond the level of palisades, on most nomad holdings, this would conflict with the necessity to show the player that they still need to siege a nomad holding (even though, they’re normally easier to siege than a fortified castle). To try and thread this ludonarrative dissonance, we have opted to have yurts both inside and outside the protective walls, this way, it shows the player that a siege must happen, but the nomadic holding doesn’t have a appear as constrained as other holdings types.  

![image_36-37.png](https://forumcontent.paradoxplaza.com/public/1273767/image_36-37.png "image_36-37.png")



On the easternmost part of the map, we have added the Burkhan Khaldun, a magnificent mountain group that carries much significance to the local steppe people.  

![image_38.jpeg](https://forumcontent.paradoxplaza.com/public/1273757/image_38.jpeg "image_38.jpeg")



**Throne Room**  
The grandiose yurt of a leader of the steppe people is also present in Khans of the Steppe. With the diligent and precise work of El Tyranos, we have constructed a throne room worthy of Genghis Khan. The throne has different versions depending on your grandeur level. Uniquely, your Coat-of-Arms is present as a huge banner draped over yourself and behind your throne.  

![image_39.png](https://forumcontent.paradoxplaza.com/public/1273758/image_39.png "image_39.png")




**Hud Skin**  

When you play the game as a nomadic character, your HUD will adopt a style inspired by Mongol patterns, carvings and art. Nomadic government characters also have a unique widget that concentrates all the most important functions that their unique playstyle requires.  

![image_40.jpeg](https://forumcontent.paradoxplaza.com/public/1273759/image_40.jpeg "image_40.jpeg")



We have also, for the first time, created a skinned version of the paper-like interfaces in the game (for example, contracts or letters). The wax seal is substituted for an ink stamp, and instead of the western ornament on the edges of the letter, a delicate eastern style of plant arrangement decorates the character portrait. We are hoping to introduce more and more thematic UI elements as we move towards All Under Heaven.  

![image_41.jpeg](https://forumcontent.paradoxplaza.com/public/1273760/image_41.jpeg "image_41.jpeg")



As it is done for other government types, nomad and herder governments also get a unique coat-of-arms banner shape. We found a striking design amongst those that the steppe people have flown, with a triangular layout and organic dents along the edges.  

![image_42.jpeg](https://forumcontent.paradoxplaza.com/public/1273761/image_42.jpeg "image_42.jpeg")



We have created a new pattern variation for COA’s that work better with this new layout, giving the dented edges a different color from the rest of the COA.  

![image_43.jpeg](https://forumcontent.paradoxplaza.com/public/1273762/image_43.jpeg "image_43.jpeg")



As for the Herders, their COA shape is somewhat inspired by the Nomad one, as it is triangular as well. But, it is a bit smaller, frayed, and doesn’t have the dented design or the secondary color on the edge.  

**Bookmarks**  
For our new bookmarks, we have decided to utilize a new paper map style, the eastern Asian one. This already reflects the new map theme you can switch between that will be arriving with the All Under Heaven expansion.  

![image_44.jpeg](https://forumcontent.paradoxplaza.com/public/1273763/image_44.jpeg "image_44.jpeg")



**Domicile Screen**  
Much like the adventurer camps and administrative estates in Roads to Power, nomads have their own domiciles. With the prospect of All Under Heaven coming up, we decided that it’d be better to take this opportunity and make this domicile art in a somewhat new style. Instead of using western artwork as inspiration, we went for an asian inspired style, with more fluid and loose ink strokes.  

![image_45.jpeg](https://forumcontent.paradoxplaza.com/public/1273764/image_45.jpeg "image_45.jpeg")



I will now hand the Dev Diary over to Ernesto Lopez, our Audio Director to tell us more on the audio work for Khans of the Steppe.  


---

### Audio & Music​


In Khans of the Steppe, our goal was to authentically capture the vastness and spirit of the Mongol Empire through sound. To achieve this, we collaborated with esteemed composer Philip Wareborn, known for his work on Stellaris and Crusader Kings III, and the talented Tuvergen Band, a Chicago-based folk-fusion trio specializing in Mongolian and Tuvan musical traditions.  

Central to Tuvergen Band’s unique sound is Tamir Hargana, an award-winning throat singer from Hulunbuir, Inner Mongolia. Tamir brings mastery of the morin khuur (horsehead fiddle) and traditional throat singing techniques, enriching the game’s musical landscape.  

This collaboration has resulted in six evocative tracks that immerse players in the Mongolian steppes. Compositions such as *Call of Gobi*, *Nomad’s Journey*, and *The Khan’s Glory* not only accompany your conquests but also embody the essence of Mongol culture and landscapes.  

[https://www.youtube.com/embed/4nWtyMw98m4?wmode=opaque](https://www.youtube.com/embed/4nWtyMw98m4?wmode=opaque)

[https://www.youtube.com/embed/HEam9CRB9BI?wmode=opaque](https://www.youtube.com/embed/HEam9CRB9BI?wmode=opaque)

[https://www.youtube.com/embed/W3nRm38ggkA?wmode=opaque](https://www.youtube.com/embed/W3nRm38ggkA?wmode=opaque)


Beyond music, we’ve enhanced the game’s ambient audio to reflect life on the steppe. Mongol-themed events now feature unique atmospheric sounds, and units are accompanied by realistic horse animations and animal noises, bringing the environment to life. Whether it’s the distant call of an eagle or the rhythmic gallop of hooves, these details ensure that the Mongol experience is both seen and heard.  

Through these auditory enhancements, Khans of the Steppe offers a deeply immersive journey into the heart of the Mongol Empire.  

---

That's all we have for this week! Join us next Tuesday for the final dev diary for Khans of the Steppe: The changelog itself.

<!-- artifact:reactions:start -->
- 94 Like
- 56 Love
- 6 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 39 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
