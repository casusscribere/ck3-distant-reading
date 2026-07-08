---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1700890/"
forum_thread_id: 1700890
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 154
title: "Dev Diary #154 - Art & Music of Roads to Power"
dd_date: 2024-08-26
author_handle: Gertax
expansion: Roads to Power
patch: Patch 1.13
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 4204
inline_image_count: 50
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1700890'
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
    location: raw_lines_~28_to_155
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_154
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3228.jpg?1724670943
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_157_to_159
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_586_to_589
    action: preserved_and_flagged
    counts:
      Love: 105
      Like: 83
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_597_to_713
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_714_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3228.jpg?1724670943)
<!-- artifact:thread_banner:end -->

# Dev Diary #154 - Art & Music of Roads to Power

<!-- artifact:thread_metadata:start -->
- Thread starter [Gertax](https://forum.paradoxplaza.com/forum/members/gertax.1709175/)
- Start date [Aug 26, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-154-art-music-of-roads-to-power.1700890/)
<!-- artifact:thread_metadata:end -->

*Note: You can also listen to today's Dev Diary here*[*on our YouTube channel!*](https://www.youtube.com/watch?v=Gvr5z2apSW4)  

---

Hello!  
Lucas Ribeiro here, 2D Art Lead at CKIII. I’m here to share with you the results of our art struggles to represent both the awesome splendor of the Byzantine Empire and the mud-splattered travels of medieval adventurers.  

---**Loading Screen**  

Let’s start off with the first thing that will greet the player in *Roads to Power*, the Loading Screen. Before picking a definitive subject matter for our loading screen, we created many composition studies. We went for themes such as nautical, imperial, religious and triumphal.  

![image-01.jpg](https://forumcontent.paradoxplaza.com/public/1170391/image-01.jpg "image-01.jpg")



1. The Emperor stands on a galley armed with a flamethrower and inspects the fleet.  
2. An Imperial comitive struts through the Boukoleon palace waterfront.  
3. An imperial comitive receives foreign dignitaries standing under the Boukoleon.  
4. The emperor returns from his victorious campaign and receives a triumph. A one-eyed man guides an army of blinded soldiers of the defeated army.  
5. The emperor is crowned  
6. A religious debate between Orthodox and Catholic priests.  
7. The emperor is crowned in the Hagia Sophia  
8. Another religious debate.  


The coronation in the Hagia Sophia and the imperial comitive striding by the docks were picked as the best ones. As a next step we created color sketches based on those chosen compositions. You can see the results here:  

![image-02.jpg](https://forumcontent.paradoxplaza.com/public/1170392/image-02.jpg "image-02.jpg")


![image-03.jpg](https://forumcontent.paradoxplaza.com/public/1170393/image-03.jpg "image-03.jpg")


*[Color sketches of the two favorite ideas.]*  

After some debate, we decided that the coronation had the most unique and striking composition out of the two. But, since the team liked the imperial comitive color sketch so much, we decided to save it and use it for the bureaucratic dynasty legacy.  

![image-04.jpg](https://forumcontent.paradoxplaza.com/public/1170394/image-04.jpg "image-04.jpg")


*[Our selected loading screen.]*  

![image-05.jpg](https://forumcontent.paradoxplaza.com/public/1170395/image-05.jpg "image-05.jpg")


*[Dynasty legacy based on the rejected color sketch.]*  

---


### **Story Event Illustrations**​


To mark great events that happen to the world or player characters we had originally introduced Story Event illustrations for *Fate of Iberia*. These dramatic splash screens would pop-up anytime something happened during the Iberian and Iranian struggles. On *Legends of the Dead* this format of illustration came back to represent major disease outbreaks and the black death. For EP3 we decided that these evocative images would be fitting for memorable events such as Triumphs, the Restoration of Rome and in the story of Hereward the Wake, the Harrying of the North.  

![image-06.jpg](https://forumcontent.paradoxplaza.com/public/1170396/image-06.jpg "image-06.jpg")


![image-07.jpg](https://forumcontent.paradoxplaza.com/public/1170397/image-07.jpg "image-07.jpg")


![image-08.jpg](https://forumcontent.paradoxplaza.com/public/1170398/image-08.jpg "image-08.jpg")



---


### Event Backgrounds​


While we had generic Mediterranean background images, it felt like they were insufficient to represent the particularities of Byzantine culture. The team thus made new versions for the feast, market, throne room, study, temple and relaxing room. This allowed us to represent some Greek particularities, such as the use of lavish recliners on their ostentatious feasts.  

![image-09.jpg](https://forumcontent.paradoxplaza.com/public/1170399/image-09.jpg "image-09.jpg")



1. A view of the Chrysotriklinos, also used as the main menu background for greek characters.  
2. A Byzantine study. Governors will be pondering administrative dilemmas in this office.  
3. A Greek market, full of color and exotic goods. Your traveler will probably stumble on this during their travels.  
4. An orthodox church or holy site. The striped walls really give it away.  
5. A Greek relaxation room. It is impossible to relax without some marble and mosaics under your feet.  
6. A Byzantine feast. The reclining chairs allow for maximum decadence, albeit the back pain.  

The hippodrome deserved special attention, as we have a background looking down from the stands into the track and one close down by the track directly.  

![image-10.jpg](https://forumcontent.paradoxplaza.com/public/1170400/image-10.jpg "image-10.jpg")


![image-11.jpg](https://forumcontent.paradoxplaza.com/public/1170401/image-11.jpg "image-11.jpg")



We wanted to make sure you would feel in the middle of the action when the chariots were neck and neck, racing to the finish line.  

Hagia Sophia could not go without receiving their own unique background as well. At first we considered having the “camera” on the walkway. Our hope was to show the scale of the edifice this way, but our designers informed us that these were normally reserved for female visitors only, so we opted for a different composition.  

![image-12.jpg](https://forumcontent.paradoxplaza.com/public/1170402/image-12.jpg "image-12.jpg")


*[The abandoned sketch]*  

![image-13.jpg](https://forumcontent.paradoxplaza.com/public/1170403/image-13.jpg "image-13.jpg")



Constantinople is the focus of many new events, both of doom and glory. Accordingly we have made the appropriate backgrounds.  

![image-14.jpg](https://forumcontent.paradoxplaza.com/public/1170404/image-14.jpg "image-14.jpg")


![image-15.jpg](https://forumcontent.paradoxplaza.com/public/1170405/image-15.jpg "image-15.jpg")



We put a lot of effort into trying to get everything in the right position in the city by following reconstructions and historical references.  

Our adventurers also demanded new backgrounds. Their camp life is represented by a variety of views of their encampment. By day or night, inside or outside.  

### image-16.jpg

### image-17.jpg

### image-18.jpg

### image-19.jpg

### image-20.jpg

### ​

### --- ​

### Animation​


In *Roads to Power*, our environment team and animation team worked together to give our characters even more life, with new animations and assets for them to wield or ride on. Here are some of the highlights:  

![image-21.gif](https://forumcontent.paradoxplaza.com/public/1170411/image-21.gif "image-21.gif")

![image-22.gif](https://forumcontent.paradoxplaza.com/public/1170412/image-22.gif "image-22.gif")


*[Charioteers will ride on appropriately colored chariots, according to their team.]*  


![image-23.gif](https://forumcontent.paradoxplaza.com/public/1170413/image-23.gif "image-23.gif")


*[The emperor flaunts his shiny stick to remind everyone who’s the boss.]*  

We have added around thirty new animations or variations of older animations. Some of these will be applied in place of the regular idle animation the character usually has to present their newfound situation, such as when they are incapable or imprisoned. Some councilors will also change their animation depending on what task they are assigned to at the moment. Hopefully this will make characters feel more alive than ever in Roads to Power.  

We also expanded on event visual effects. Instead of using bink videos like we did for Legends of the Dead, we have opted for shaders that are a lot lighter. The new event effects include: Earthquake, heavy smoke, sand storm, rainy fog and lightning storm.  

![image-24.gif](https://forumcontent.paradoxplaza.com/public/1170414/image-24.gif "image-24.gif")



---**Domiciles**  

![image-25.jpg](https://forumcontent.paradoxplaza.com/public/1170415/image-25.jpg "image-25.jpg")


*[Initial experiments for the estate screen.]*  

![image-26.jpg](https://forumcontent.paradoxplaza.com/public/1170416/image-26.jpg "image-26.jpg")


*[Initial Experiments for the camp screen.]*  


Settling on a style for the domicile screen was quite a struggle for the team. At first, we meant to have them be very similar to locales (as in, the Tournament Screen). While this would make for more internal consistency in art style, for four reasons we decided to deviate from this initial plan:  

First, we wanted this NOT to be full-screen, as unlike the tournament screen, we do not mean to take the player away from their plots and immerse them in the event. The domiciles (estates and camps) communicate directly with your actions in the game world, and should be convenient to navigate. This made for a smaller screen and thus, a more symbolic representation of buildings and their purpose would work better in this medium.  

Second, we felt that our 3D environment team efforts were better used elsewhere, it was unlikely we could’ve created cultural variations of buildings while depending on them. Keeping the work exclusively on the 2D artists expanded our capacity to create more buildings and have cultural variety on top of it.  

Third, The domiciles operate in a totally different way from tournaments, visual similarities would incorrectly communicate to the player that they should function the same way.  

Fourth, the team fell in love with the mockups we presented in the medieval art style. The non-descript isometric buildings ended up paling in comparison to the charming illustrations we had come up with.  

![image-27.jpg](https://forumcontent.paradoxplaza.com/public/1170418/image-27.jpg "image-27.jpg")



Estate buildings have different visuals according to culture. For now, we have Western, Byzantine and MENA themes.  

Camp buildings are the same regardless of culture, except for the main tent, which has western, steppe, tribal and mena themes.  

Besides variation of buildings by culture, we also wanted to reinforce the sense of place in the world of the domiciles by creating different backgrounds that change according to the position of the estate or the camp.  

Estate Background can be:  
Dry, Green, Jungle, Rough and Urban.  

While Camp Backgrounds can be:  
Dry, Green, Jungle, Rough, Snow and Snowy Mountains.  

---**Coat of Arms**  

While the Greeks showed less propensity to utilize coat-of-arms in the fashion we observe in western Europe, they did attach to the identity of their families certain symbols on their coins, murals and reliefs.  

It makes for an interesting variety that they would claim not only secular imagery, inspired on greco-roman myths, but also christian religious symbols. Their connection to the sea would also inspire many aquatic motifs.  

Thus, we can see mermaids, ophiotaurus and manticores side-by-side with Jesus, Mary, Archangel Gabriel and Saint George. These might be adorned with crosses, stars or shells.  

![image-28.gif](https://forumcontent.paradoxplaza.com/public/1170419/image-28.gif "image-28.gif")


*[Randomly generated Greek coat of arms.]*  

---**Character Art**  

With Roads to Power we had the chance to greatly expand the Byzantine wardrobe, which was historically quite distinct and interesting looking, and very notably different from surrounding cultures.  

As usual our work began with collecting references, preferably from first-hand contemporaneous sources, but we also looked for modern books and other material that focus on this subject matter (a special shout-out to a book called “By the Emperor’s hand” by Timothy Dawson - which contains a lot of amazing research and conclusions!).  

![image-29.jpg](https://forumcontent.paradoxplaza.com/public/1170421/image-29.jpg "image-29.jpg")


*[A snapshot of (a small part of!) the Miro board put together by Nils and the character art team to collect references for everything related to Byzantine clothing.]*  

There are quite a lot of both first and second hand sources that survive from the Byzantine Empire (perhaps not too surprising considering how vast it was and for how long it survived). Of particular value to note here are the “Coptic” garments that have survived in fantastic condition through the centuries in graves from Byzantine Egypt. Actual extant examples like these provide the best type of source we can wish for, and there are dozens of them! Most of them do pre-date the game by some margin, but we can see from 9th and 10th century manuscripts and mosaics that clothing in the same style was clearly still in use by our early start date.  

![image-30.jpg](https://forumcontent.paradoxplaza.com/public/1170422/image-30.jpg "image-30.jpg")


*[Some examples of “Coptic tunics” that have been excavated from Byzantine era Egypt.]*  


![image-31.jpg](https://forumcontent.paradoxplaza.com/public/1170423/image-31.jpg "image-31.jpg")


*[Here we see very similar looking tunics depicted in the “Paris Gregory” from c. 880 and the “Paris Psalter” from the mid 10th century.]*  

Following what we started with Western European clothes for Tours and Tournaments, we decided quite early on that Roads to Power should also include different clothes for early and late eras. This fits especially well with the new 1178 start date; Byzantine characters by that time will look quite different from those of three hundred years prior.  
Since there are very few preserved items of clothing from the later time period, we based those designs primarily on depictions in manuscripts and mosaics.  

![image-32.jpg](https://forumcontent.paradoxplaza.com/public/1170424/image-32.jpg "image-32.jpg")


*[From the Menologion of Basil II, 11th century (which - as a side note - is filled to the brim with these beautiful and disturbing paintings of saints being brutally tortured and murdered, people being burned alive, babies being skewered, with everyone looking slightly bored) and the Madrid Skylitzes, from around 1150.]*  

Since we are depicting a lot of the Creme de la Creme of people of the time, we are always looking for suitable Bling to add as accessories to these outfits. This expansion was no exception. Again, we turn to primary sources of jewelry that have survived to the present day.  

![image-33.jpg](https://forumcontent.paradoxplaza.com/public/1170425/image-33.jpg "image-33.jpg")


*[Some spectacular Byzantine jewelry from museums around the world that we recreated for Roads to Power.]*  

We then created concept-art to synthesize these disparate sources and fuzzy imagery into a more concrete form the 3D character artists could base their work on.  

![image-34.jpg](https://forumcontent.paradoxplaza.com/public/1170426/image-34.jpg "image-34.jpg")


*[Examples of concept art based on our collected references.]*  

![image-35.jpg](https://forumcontent.paradoxplaza.com/public/1170427/image-35.jpg "image-35.jpg")


*[And some finished clothing assets showing a comparison between the “early” and “late” eras. ]*  



![image-36.jpg](https://forumcontent.paradoxplaza.com/public/1170428/image-36.jpg "image-36.jpg")


*[This might look a bit funky, but we have to create many blendshapes so that the clothes can morph along with the character as they age and get thinner, fatter or muscular.]*  



![image-37-38.png](https://forumcontent.paradoxplaza.com/public/1170429/image-37-38.png "image-37-38.png")



We were grateful for the opportunity to bring to life many memorable headgear and accessories of the Byzantine world, such as the Propolôma hat or the Imperial Delmatikion with Diadêma. Most of them have their proper (Medieval Greek) names in the Barbershop.  

Overall, we’ve added 8 new hairstyles, 4 beards, 18 clothing sets, 2 armors, 3 sets of legwear, 4 cloaks and 24 different headgear. This great variety, layered on top of the original assets from the base game will make each character in the cast of your personal Greek drama be unique and memorable.  

![image-39.jpg](https://forumcontent.paradoxplaza.com/public/1170430/image-39.jpg "image-39.jpg")


![image-40.jpg](https://forumcontent.paradoxplaza.com/public/1170431/image-40.jpg "image-40.jpg")


*[Early and late era Byzantine courtiers dressed in some of the new clothes added with Roads to Power. ]*  

---**Patterns**  

Thanks to the fortunate survival of many textiles from the Byzantine times, we had our pick of the litter when it came to which trims and brocades to represent. It was more a matter of choosing the most characteristic, unique and interesting ones.  

Unlike other patterns, we have used a new type of texture map setup, where the bottom part of the medium trims is used for roundels. This permitted us to have specific bits of the pattern transform from a trim to a framed rounded-ish composition.  

![image-41.jpg](https://forumcontent.paradoxplaza.com/public/1170432/image-41.jpg "image-41.jpg")



---**Throne Room**  

The Byzantine throne room was a daunting task undertaken by our 3D environment Team. Our objective was to represent the Chrysotriklinos, the main ceremonial hall of the Great Palace of Constantinople. Unfortunately, the palace has been destroyed and there are no contemporaneous representations of the place. We had then to follow descriptions made at the time and observe other structures that take inspiration from the palace in some capacity (such as the Church of Ravena and the Palace of Aachen).  

![image-42.jpg](https://forumcontent.paradoxplaza.com/public/1170433/image-42.jpg "image-42.jpg")


*[Concept of the throne room.]*  

The overall shape of our interpretation is quite similar to the Palace of Aachen, but we opted to optimize the shape so that it could better be captured by our throne room camera setup, so the dome is probably a bit lower than it would’ve been at the time.  

We also knew we wanted to decorate the room with many mosaics, as was the fashion at the time.  

![image-43.jpg](https://forumcontent.paradoxplaza.com/public/1170434/image-43.jpg "image-43.jpg")



Instead of copying existent mosaics, we opted to create our own version, inspired by surviving examples. We wanted to have bigger individual mosaic bits. If we had made the individual tiles as small as they were in real-life, they’d become unreadable from a distance as being a mosaic.  

![image-44.jpg](https://forumcontent.paradoxplaza.com/public/1170435/image-44.jpg "image-44.jpg")


*[Here we can see the constituting texture maps to make up a mosaic, created by hand by our 2D Artists.]*  

For the trims and patterns that frame the architecture and make up the more geometric parts of the mosaic, we created a variety of trimsheets and materials.  

![image-45.jpg](https://forumcontent.paradoxplaza.com/public/1170436/image-45.jpg "image-45.jpg")



For subject matter, we knew from contemporaneous descriptions, the apse was dominated by christ on a lyre throne. We also knew emperors, saints and angels were represented. As well as verdant fields and flowers.  

When it came to deciding which figures to display, we wanted to do a nod to the fact that these mosaics were removed during the time of aniconism and then restored before our game starting date. We went with some staunch defenders of icons such as Irene of Athens and Theophanes the Confessor. We also included some classic characters such as Justinian, Constantine, St. Helen and Demetrius of Thessalonica.  

![image-46.jpg](https://forumcontent.paradoxplaza.com/public/1170437/image-46.jpg "image-46.jpg")


![image-47.jpg](https://forumcontent.paradoxplaza.com/public/1170438/image-47.jpg "image-47.jpg")



From the writings of an emissary to the Byzantine court, we got reports of chirping mechanical birds and roaring metal lions.  

We have done our part in emulating these marvels, as the golden lions flanking the Throne of Solomon will intermittently bang their tails on the ground and “roar”. We also added the mechanical birds and the Water Organ as a court artifact.  

![image-48.jpg](https://forumcontent.paradoxplaza.com/public/1170439/image-48.jpg "image-48.jpg")



![image-49.jpg](https://forumcontent.paradoxplaza.com/public/1170440/image-49.jpg "image-49.jpg")


*[Some of the new statue assets that can be found in the Byzantine court.]*  

---**Holdings and Special Buildings**  

Besides the terrain rework mentioned on previous dev diaries, our 3D environment team has populated Anatolia and Greece with a variety of special buildings. We had great inspirations to draw from such as monasteries built against sheer cliffs or ancient temples repurposed as orthodox churches.  

![image-50.jpg](https://forumcontent.paradoxplaza.com/public/1170441/image-50.jpg "image-50.jpg")



Greek-culture holdings now have unique graphics, distinguished from the generic Mediterranean ones.  

![image-51.jpg](https://forumcontent.paradoxplaza.com/public/1170442/image-51.jpg "image-51.jpg")



You can now see the characteristic warm colors, red striped walls and rounded roofs.  

---**Byzantine Hud and Table**  

![image-52.jpg](https://forumcontent.paradoxplaza.com/public/1170443/image-52.jpg "image-52.jpg")



Our environment team created a Byzantine version of the map table to make for an even more immersive experience for our players. The lamps and silverware are inspired by surviving pieces of Byzantine craft. The sword and the bag of gold on the rightmost area of the table are a nod to the adventurer aspect of the expansion.  

While playing as a Greek character, players will also enjoy a mosaic inspired HUD skin. Nature motifs are depicted by bits of colorful tiles. Some of the HUD elements have also been reworked to be modular, so it’s easier to add new buttons on the side panels and currencies on the top. Hopefully modders can make good use of that.  

---**Miscellaneous Improvements**  

The UI team also dedicated some time to making the game look and feel better by improving on some older features.  

Toasts have been reworked, they are now more clearly color coded so the player can tell if they failed or succeeded on an event quite more clearly. Toasts are also built in a way that they vary in size according to the amount of information to be displayed, which means you will get less hidden results marked by a nondescript “...”.  

![image-53.jpg](https://forumcontent.paradoxplaza.com/public/1170444/image-53.jpg "image-53.jpg")



Alerts are now color coded as well, so players will have a clearer distinction of when they are being offered an opportunity (purple), if it’s something that needs their immediate attention (red) or if they have a boon they can click to collect (green).  

![image-54.png](https://forumcontent.paradoxplaza.com/public/1170445/image-54.png "image-54.png")



We have also reworked all of the event headers. Icons were made crisper, their design improved. The mosaic header itself is now colored differently depending on which type of event the player is engaged with.  

![image-55.jpg](https://forumcontent.paradoxplaza.com/public/1170446/image-55.jpg "image-55.jpg")



I will now hand the Dev Diary over to Ernesto Lopez, our Audio Director to tell us more on the audio work for Roads to Power.  

---**Music Player**  

Hey everyone,  

We're thrilled to share some exciting news about the latest expansion for Crusader Kings III, and today we're focusing on something truly special: the music. As you dive into the new content, we want to give you a peek behind the curtain at the fascinating process that brought this soundtrack to life.  

One of the standout elements of this expansion is the incorporation of Orthodox Chants, a unique and evocative addition that adds a profound layer to the game's atmosphere. We had the incredible opportunity to collaborate with Prof. Dr. Konstantin Nikolakopoulos, a renowned expert in orthodox music. Together with our talented composers from Audinity, Yannick Süß and Robin Birner, we embarked on a journey to capture the essence of these ancient chants.  

The recording process was something truly extraordinary. The team, alongside Prof. Dr. Nikolakopoulos, ventured to the Salvatorkirche in Munich, Germany, where they recorded these chants live. This wasn't your typical studio session—it was raw, unstructured, and entirely authentic. With no predefined tempo or strict direction, the music was allowed to evolve organically from the live performance. What emerged was a soundtrack that not only captures the emotional depth of orthodox chants but also seamlessly integrates the signature Crusader Kings III vibe—a blend of medieval authenticity with a modern twist.  

Audinity deserves huge credit for how they approached this. They managed to maintain the integrity of the chants while infusing them with what we like to call a "modern-medieval" sound. It's a unique blend that feels both timeless and fresh, perfectly encapsulating the spirit of Crusader Kings III. The new Main Theme is a testament to this, showcasing the power and presence of Prof. Dr. Nikolakopoulos' performance in a way that is both majestic and haunting.  

But that's not all—we're also introducing a brand-new music player for Crusader Kings III. This has been a highly requested feature, and we're excited to finally bring it to you. The initial release will offer basic functionality, allowing you to have greater control over your in-game music. Whether you want to cue up specific tracks or mix and match songs from the base game with those from the Byzantium Empire expansion, the music player gives you that agency. You can enable or disable tracks at your discretion, allowing you to tailor your auditory experience to your exact preferences.  

![image-56.jpg](https://forumcontent.paradoxplaza.com/public/1170447/image-56.jpg "image-56.jpg")



We believe the music player is a fantastic addition, and we're committed to continuing its development based on your feedback. It's a significant step forward in giving you more control over how you experience the rich musical landscape of Crusader Kings III.  

So, dive into the new expansion, enjoy the incredible new music, and explore the music player to make your game soundtrack truly your own. We can't wait to hear what you think and to continue refining these features with your input.

<!-- artifact:reactions:start -->
- 105 Love
- 83 Like
- 6 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Gertax](https://forum.paradoxplaza.com/forum/members/gertax.1709175/)**
Role: Corporal
Badges: 102
Messages: 34
Reaction score: 1,184

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
