---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1861436/"
forum_thread_id: 1861436
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 186
title: "Dev Diary #186 - Character Art of All Under Heaven"
dd_date: 2025-10-02
author_handle: akash garg
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2255
inline_image_count: 33
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1861436'
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
  - type: thread_metadata
    location: raw_lines_150_to_152
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_446_to_450
    action: preserved_and_flagged
    counts:
      Like: 68
      Love: 45
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_458_to_576
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_577_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #186 - Character Art of All Under Heaven

<!-- artifact:thread_metadata:start -->
- Thread starter [akash garg](https://forum.paradoxplaza.com/forum/members/akash-garg.1921711/)
- Start date [Oct 2, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-186-character-art-of-all-under-heaven.1861436/)
<!-- artifact:thread_metadata:end -->

Akash Garg here, 3D artist lead at Studio Black! Today we’re going to cover the new character art coming in All Under Heaven, so let’s get right into it.  


### Tang & Song Dynasties​

We wanted to share some insights into the creative process behind the character apparel in *All Under Heaven*. Our primary inspiration comes from two of the most aesthetically striking and culturally rich eras in Chinese history: the Tang Dynasty (618–907 AD) and the Song Dynasty (960–1279 AD). Together, the two dynasties fit our game's timeframe perfectly.  

Each of these dynasties had its own distinct cultural and creative identity, which we've carefully studied throughout the development of *All Under Heaven*. Our aim has been to provide a good level of visual variety as well as a believable representation of these historical time periods. We hope our effort in this area results in a richer and more historically authentic visual experience for all of our players.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1369819/image_01.png "image_01.png")


*[Examples of primarily Tang Dynasty attire. The Emperor is wearing a mianfu, the Empress a diyi. There are Ministers with yuanlingpao robes as well as a soldier in cord-and-plaque armor, and a Taoist priest.]*  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1369820/image_02.png "image_02.png")


*[A combination of primarily Song Dynasty attire. The Song Emperor is wearing Tongtianguanfu, and he is surrounded by court ladies, ministers (one of them wearing the iconic spread-horn futou), as well as a soldier with gilded mountain-pattern armor.]*  

### Research & References​

As always, we first needed to develop a solid understanding of the time period and learn as much as we could about the Chinese clothing styles of the Tang and Song dynasties. With great help from our stellar team of beta testers, as well as other team members with extensive knowledge and resources, we started by collecting historical references from:  


- Ancient murals, books, museum collections (e.g., Palace Museum, History Museum)
- Academic papers and books on Chinese costume history
- Reconstructions of Hanfu clothing

We then set up a moodboard/reference board to collect our sources and ideas in a visual way. At this point we also got help from our talented colleagues in the 2D art team who created concept art for many of the assets. These drawings, combined with the reference images, are what the 3D artists use as guides when working on each item.  


- **Tang Dynasty**: Typical features include long sleeves with long skirts and bold colors.
- **Song Dynasty**: Characterized by wide-sleeved Hanfu clothes, long skirts, floral embroidery, and elegant simplicity.

![image_03.png](https://forumcontent.paradoxplaza.com/public/1369822/image_03.png "image_03.png")


*[A snapshot of (a small part of!) the Miro board put together by the character art team to collect references for everything related to Chinese clothing.]*  

Overall, we have successfully created a total of 84 Chinese culture assets for this initiative, distributed as follows:  


- 16 hairstyles
- 21 clothing assets
- 12 beards
- 12 legwear
- 18 headgear
- 2 armor sets
- 3 map units

Below you can see some game renders for various hairstyles, beards, and headgear for both male and female characters. These items are triggered in the game based on the character's ranking and status.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1369823/image_04.png "image_04.png")


![image_05.png](https://forumcontent.paradoxplaza.com/public/1369824/image_05.png "image_05.png")


*[Some examples of Chinese hairstyles and headgear.]*  


### Clothing Patterns from the Tang and Song Dynasties​

We’ve also created many new fabric patterns for the Chinese clothes, all based on historical sources. These are applied to clothing in the game both as multicolored brocades as well as more subtle, monochromatic patterning.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1369825/image_06.png "image_06.png")


![image_07.png](https://forumcontent.paradoxplaza.com/public/1369826/image_07.png "image_07.png")


*[Pattern textures.]*  

Since Chinese dynasties had strict rules regarding colors, fabrics, and cuts of garments, we developed a system for classifying clothes according to their Merit ranking in-game. Our approach involves using specific palettes to categorize outfits based on color variations. This is then scripted so that a character like a minister will wear different-colored robes depending on their rank.  

We hope this system will provide players with a clearer understanding of how garment aesthetics played a role in status and hierarchy within China.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1369827/image_08.png "image_08.png")


*[Some examples of Chinese patterns and color combinations applied to the clothing.]*  


### Color Palettes​

We use color palettes like the example below to enhance the color diversity of each outfit. This is what allows us to do the previously mentioned robes for differently ranked ministers, for example, but it also lets us create more colorful outfits with many patterns and complex combinations. This expansion adds many garments with multiple layered components. To support them, we expanded our dynamic patterning system from four to six dynamic materials, which lets us represent the era’s colorful clothing more faithfully.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1369828/image_09.png "image_09.png")


![image_10.png](https://forumcontent.paradoxplaza.com/public/1369829/image_10.png "image_10.png")


*[Chinese Hanfu garments.]*  

Chinese Armor  
Tang/Song Dynasty armors were often made of lamellar and mountain-pattern plates tied together with leather or silk cords, sometimes incorporating metal, lacquered leather, and silk, symbolizing the empire's wealth and martial strength. We have included a Tang-era cord-and-plaque armor and a Song-era elite mountain-pattern armor.  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1369830/image_11.png "image_11.png")


![image_12.png](https://forumcontent.paradoxplaza.com/public/1369831/image_12.png "image_12.png")


*[Chinese armors]*  


#### Military Units​

In addition to portrait characters, we also represent the military might of the Chinese dynasties with new army units on the map.  

For every culture, we typically have three tiers of map units.  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1369832/image_13.png "image_13.png")


![image_14.png](https://forumcontent.paradoxplaza.com/public/1369833/image_14.png "image_14.png")


*[Chinese map units.]*  



### Japanese Heian Period​

The Japanese Heian Period (794–1185) was characterized by grace, ceremony, and multi-layered clothing, and is the inspiration for the Japanese set of character attire. The rich patterns, hues, textures, and Heian court dress are what we aim to capture.  

Important clothes :  

**Jūnihitoe** (Twelve-Layer Robe): Worn by ladies of the court, this elegant, multi-layered ensemble uses carefully chosen colors to reflect seasons. This was an interesting challenge for our team; we used cloth simulation software to faithfully recreate each layer of this costume, one after the other.  

![image_15.jpeg](https://forumcontent.paradoxplaza.com/public/1369834/image_15.jpeg "image_15.jpeg")


*[3D model made for the Jūnihitoe]*  

**Sokutai** (imperial robe): For male courtiers, from the middle ranks all the way up to the Emperor, the Sokutai includes wide sleeves, tall headwear (kanmuri or eboshi), and a stiff, formal silhouette. Our version blends ceremonial grandeur with slight mobility for animations.  

As with the jūnihitoe, we constructed the sokutai in a true‑to‑life way, with each layer of the real outfit included in the simulation. The outermost garment is the **hōeki no hō**, worn over six additional layers that help create the sokutai’s iconic silhouette.  

As you can see, we also modeled the ceremonial kazari-tachi sword based on a real example from the Heian Period.  

![image_16.jpeg](https://forumcontent.paradoxplaza.com/public/1369835/image_16.jpeg "image_16.jpeg")


![image_17.jpeg](https://forumcontent.paradoxplaza.com/public/1369836/image_17.jpeg "image_17.jpeg")


*[3D models of the sokutai and kazari-tachi sword]*  

**Ō-yoroi Armor** and **Kabuto Helmet**: Iconic boxy silhouette with large shoulder guards, chest armor, and a skirt of lamellar plates (kusazuri). Tied with brightly colored silk cords, the armor was both defensive and highly decorative.  

![image_18.png](https://forumcontent.paradoxplaza.com/public/1369837/image_18.png "image_18.png")


*[Combination of Heian Period attire and robes worn by important nobles. The male official wears sokutai and his wife jūnihitoe. There are two men wearing less formal clothing and a third one in full ō‑yoroi armor, as well as a Buddhist monk in Japanese-style kasaya.]*  

![image_19.png](https://forumcontent.paradoxplaza.com/public/1369838/image_19.png "image_19.png")


*[Combination of low-ranking official, the Emperor in sokutai, and a high-ranking official]*  

![image_20.png](https://forumcontent.paradoxplaza.com/public/1369839/image_20.png "image_20.png")


*[How the jūnihitoe robe is worn with empress and noblewoman clothing]*  

![image_21.png](https://forumcontent.paradoxplaza.com/public/1369840/image_21.png "image_21.png")


*[Combination of dō-maru and ō‑yoroi armor along with Ori-eboshi and kabuto helmet]*  

![image_22.png](https://forumcontent.paradoxplaza.com/public/1369841/image_22.png "image_22.png")


*[A family wearing clothes decorated with their family kamon]*  


### Research & References​

Similar to the previously described process for creating Chinese garments, for the Japanese assets we started by collecting historical references from:  


- Ancient murals, museum collections (e.g., Palace Museum, History Museum)
- Books and websites focused on Japanese history
- Patterns that are still used today in imperial ceremonies and as part of living history events

We set up a separate moodboard for the Japanese collection.  

![image_23.png](https://forumcontent.paradoxplaza.com/public/1369842/image_23.png "image_23.png")


*[Reference board for the Japanese assets]*  

Overall, we have created a total of 47 assets for Japanese culture:  


- 6 hairstyles
- 18 clothing assets
- 4 beards
- 5 legwear
- 9 headgear pieces
- 2 armor sets
- 3 map units

Here we have some game renders for various hairstyles, beards, and headgear for both male and female characters. These items are triggered in the game based on the character's ranking and status.  

![image_24.png](https://forumcontent.paradoxplaza.com/public/1369843/image_24.png "image_24.png")


*[A selection of Japanese hairstyle and headgear assets]*  


### Japanese Clothing Patterns​

Much like the Chinese system of government, the ranking system for Japanese dynasties heavily relies on the color and design of garments. We try to group the outfits by rank using color palettes.  

We have also developed numerous brocades and trims that are unique to Japanese culture.  

![image_25.png](https://forumcontent.paradoxplaza.com/public/1369844/image_25.png "image_25.png")


*[Some of the Japanese patterns and color combinations]*  

![image_26.png](https://forumcontent.paradoxplaza.com/public/1369846/image_26.png "image_26.png")


*[Various Japanese garments]*  


#### Japanese Military Units​

For every civilization, we typically have three tiers of map units.  

![image_27.png](https://forumcontent.paradoxplaza.com/public/1369847/image_27.png "image_27.png")


*[Japanese map units]*  


### Khmer Empire​

The Khmer Empire (9th–10th centuries) influences character clothing, emphasizing the splendor of Angkorian‑era style. Royal attire, such as the sampot (a long, wrapped skirt), features golden belts and elaborate crowns or headdresses, and is typically worn by kings or high officials.Temple-dancer (or *apsara*) outfits typically feature flowing silk garments and elaborate jewelry. These are usually worn with large, heavily-decorated crowns or headdresses.  

![image_28.jpeg](https://forumcontent.paradoxplaza.com/public/1369848/image_28.jpeg "image_28.jpeg")


![image_29.png](https://forumcontent.paradoxplaza.com/public/1369849/image_29.png "image_29.png")


![image_30.png](https://forumcontent.paradoxplaza.com/public/1369850/image_30.png "image_30.png")


*[3D model of the Sampot Tep Apsara and Crown]*  

Overall, we created a total of two sets of clothes and headgear for this region.  

![image_31.png](https://forumcontent.paradoxplaza.com/public/1369851/image_31.png "image_31.png")


*[Combination of Royal attire (Sampot with Body Jewelry) and Sampot Tep Apsara along with Khmer Noble's Crown and Apsara Crown]*  



### Asian Ethnicities​

With the map significantly expanded to cover vast new regions, there are many new cultures and peoples represented in the game. One important aspect of that representation is the new ethnicities we added across East Asia. You can see some examples of character appearances from different regions below.  

![image_32.jpeg](https://forumcontent.paradoxplaza.com/public/1369852/image_32.jpeg "image_32.jpeg")


*[A selection of characters from all over East and Southeast Asia]*  


### General Improvements​

If you study the screenshots closely, you may notice something that looks a little different from the current version of Crusader Kings III. We have made some overall improvements to skin textures, lighting, shading, and render settings. This affects all characters in the game (not just those from the new areas!) and should result in all of them looking a bit better.  

![image_33.jpeg](https://forumcontent.paradoxplaza.com/public/1369853/image_33.jpeg "image_33.jpeg")


*[Some more examples of characters from other parts of the map after the overall improvements]*  


### Conclusion​

Featuring by far the largest number of assets we have made for an expansion (not to mention focusing on an entirely new area of the world) *All Under Heaven* provided a significant challenge for us, but it was also very rewarding to dive into this incredibly rich source material and bring it to life within *Crusader Kings III*. We’re pleased with the results and the volume of content, and we sincerely hope it contributes to the immersion of this new DLC  

It’s been incredibly important for us to enable many of you to be able to play in your countries and cultures you’ve always wanted to play (It might even be your own!). While we had a lot of material and references to work with for this expansion, the sheer size of it meant we couldn’t implement everything on day one. There are so many beautiful clothes and accessories from that era that we would love to realize one day, so please, after *All Under Heaven* releases we would LOVE to hear from you what YOU felt was missing and would love for us to add in the future.

<!-- artifact:reactions:start -->
- 68 Like
- 45 Love
- 9 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [akash garg](https://forum.paradoxplaza.com/forum/members/akash-garg.1921711/)**
Role: Private
Badges: 102
Messages: 10
Reaction score: 307

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
