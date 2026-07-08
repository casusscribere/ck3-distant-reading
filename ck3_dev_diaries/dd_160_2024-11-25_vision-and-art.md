---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1717586/"
forum_thread_id: 1717586
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 160
title: "Dev Diary #160 - Vision and Art"
dd_date: 2024-11-25
author_handle: El Tyranos
expansion: Wandering Nobles
patch: Patch 1.14
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1174
inline_image_count: 9
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1717586'
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
  - type: thread_banner
    location: raw_line_143
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3453.jpg?1732535169
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_146_to_148
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_244_to_247
    action: preserved_and_flagged
    counts:
      Like: 52
      Love: 32
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_255_to_357
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_358_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3453.jpg?1732535169)
<!-- artifact:thread_banner:end -->

# Dev Diary #160 - Vision and Art

<!-- artifact:thread_metadata:start -->
- Thread starter [El Tyranos](https://forum.paradoxplaza.com/forum/members/el-tyranos.519435/)
- Start date [Nov 25, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-160-vision-and-art.1717586/)
<!-- artifact:thread_metadata:end -->

Hello there!  

I’m Pierre “El Tyranos” Azuelos, the creator of the Community Flavor Pack mod. The past couple of months have been busy again and I am once again delighted to collaborate with Paradox Interactive on a second Content Creator Pack named “Western Slavic Attire”.  

This second project is a little more special as it does not come alone, for the 8th official language of Crusader Kings III will be released at the same time. The game will be entirely translated into Polish and for free of course!  

### Introducing the Content Creator Pack​

Before showing you some garments, explaining the artistic direction and getting into more technical details, I wish to (re-)introduce you to the vision of this project.  

The philosophy remains the same as “North African Attire” and this Content Creator Pack has been designed to be of similar size: you get an entire set of clothes, headwear, armors and trousers for Western Slavic characters. These assets are exclusive new content and they will be officially supported by Paradox Interactive in the future.  

### Artistic Direction​

At the interface between Western and Eastern influences, contemporary sources tend to show a Westernized or Byzantine ceremonial fashion in the highest ranks of the medieval polish societies.  

On the opposite, archaeology brings out that the lowest ranks wear similar clothes as the other regional Slavic groups (Sloveins, Ruthenians, Kievans, etc.), inherited from Great Moravia and the Viking age.  

Considering the many Western options already in CK3 and even if historical sources show no evidence that Polish high nobility ever dressed as lowborn western Slavs, this Content Creator Pack tries to prioritize Slavic garments as if a Slavic lower nobility fashion outbreaked in courtly dressing.  

### Character Art​

The tunic with apron is THE woman outfit of Eastern Europe and you will get two of them (for a total of 6 variants). “Architectonics of pra-Slavic costume had double or probably tipple layered structure which was kept in the Middle Ages as well” (NSEN, 2020). The main difference between Rus and Western Slavs is the jewelry, in particular the temple rings since they all wear coral necklaces. In contrast to fabrics those are very well documented in archeology. All pieces of jewelry are 1:1 reproductions of actual Polish or Czech artifacts.  

![1.png](https://forumcontent.paradoxplaza.com/public/1213039/1.png "1.png")


*[Mannequins from Archeology museum of Biskupinie and Museum of the Origins of the Polish State, Gniezno, Poland]*  

![2.png](https://forumcontent.paradoxplaza.com/public/1213040/2.png "2.png")


*[Left: Duchess Agnes of Głogów-Żagań, Kodeks lubiński, 1353 ; Right: Reenactment by Fibularius]*  

The svita was the wool outer clothing in the 10th through 13th centuries. It’s an unisex garment. It was made of heavy horizontal strips of a contrasting color fabric, braid or galoons (Kireyeva & Stamerov). The hat is very represented in 14th century Polish sources.  

![3.png](https://forumcontent.paradoxplaza.com/public/1213041/3.png "3.png")


*[Right: Henry the Bearded, Duke of Silesia and his son Henry II Pobożny, duke of Silesia and Greater Poland, Kodeks lubiński, 1353]*  

There’s no strong evident sources for such a garment, but it allows complex clothing for higher classes without falling back to Byzantine or Western options that are already in the game. The hat is likely Czech, also poorly represented.  

![4.png](https://forumcontent.paradoxplaza.com/public/1213042/4.png "4.png")


*[Left: Špitálky, Vestibule of the church – detail of a silver disc portraying a horseman holding a short baton, the so-called “Falconer” from grave 16, 2nd half of the 9th century ; Right: Around 1385 - detail of a fresco in the Church of St. James the Greater, Slavětín nad Ohří, photo by Martin Hřibc ]*  

For royalty and imperial tiers, you’ll find several famous crows, from left to right :  


- The crown of Bolesław I the Brave after representations of its second version (made for Ladislaus the Short in 1320) before it was melted in 1794 ;
- The crown of Casimir the Great as sculpted on his contemporary effigy (made just after his death in 1370) ;
- The crown of Emnilda słowiańska, wife of Bolesław I the Brave, after a statue of her at the cathedral of Naumburg (1250) ;
- The travel (or funerary) crown of Casimir the Great, mounted on his display bascinet and, found in his tomb in Krakow.

![5.png](https://forumcontent.paradoxplaza.com/public/1213043/5.png "5.png")



Kings and Emperors also get a special version of the svita with a golden belt, pearls and gems fastener as well as a reproduction of Szczerbiec. Szczerbiec is also available as a court artifact. For other characters such as knights and marshals, they will wear a Type Z “Starigard” sword.  

![6.png](https://forumcontent.paradoxplaza.com/public/1213044/6.png "6.png")



Speaking of swords, are you planning to go to war early in the game? Then grab your gambeson, scale armor and “Giecz” helmet. Based largely upon a little-known but important carved bone or ivory chess piece found in Cracow, this foot soldier illustrates the mixture of Western and Eastern traditions which continued to characterize parts of Poland, especially its eastern provinces. The cuirass is also based upon the chess piece, the details of its construction being taken from an inverted lamellar system seen in neighbouring Russia. (Osprey M.A.A. 445)  

![7.png](https://forumcontent.paradoxplaza.com/public/1213045/7.png "7.png")



Did you expand peacefully for a century? It’s never too late. As I know you all liked the crazy Aragon golden Dragon Crest from Community Flavor Pack, I could not resist to fit in this adaptation of Pranckh’s Topfhelm displayed in Vienna. The crest is inspired from the Battle of Legnica (1241) representation in Kodeks lubiński. Use it anywhere as long as you crush your enemies and see them driven before you. It will show up for Western Slavic high nobles during Era 3. Regular characters will enjoy the basic helm.  

![image-08.jpg](https://forumcontent.paradoxplaza.com/public/1213021/image-08.jpg "image-08.jpg")



Same setup for the bascinet (Era 4, crown for royalty and regular version for others). Side note: enhanced experience for Tours and Tournament owners who will be able to reenact Casimir the Great in his full plate armor glory. Chodźmy!  

### Conclusion​

![image-09.jpg](https://forumcontent.paradoxplaza.com/public/1213051/image-09.jpg "image-09.jpg")



It has been a blast to work on these two Content Creator Packs together with Paradox Interactive. I know the CK3 team has been very happy with this experience and that they have expanded the amount of Content Creators they are working with. I look forward to seeing the results of these new collaborations!  

It is now time for me to conclude this Dev Diary and also this chapter of my life. You, the community, are the fuel that made me able to reach this point and I will forever be grateful for your enthusiasm.  

I will now focus on other projects of Paradox Interactive, including for CK3. So… until next time!

<!-- artifact:reactions:start -->
- 52 Like
- 32 Love
- 5 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [El Tyranos](https://forum.paradoxplaza.com/forum/members/el-tyranos.519435/)**
Role: 3D bot
Badges: 139
Messages: 304
Reaction score: 2,225

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
