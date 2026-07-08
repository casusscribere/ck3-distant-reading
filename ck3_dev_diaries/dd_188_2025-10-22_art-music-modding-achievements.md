---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1863996/"
forum_thread_id: 1863996
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 188
title: "Dev Diary #188 - Art, Music, Modding, Achievements"
dd_date: 2025-10-22
author_handle: PDX-Trinexx
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 8100
inline_image_count: 90
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1863996'
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
    location: raw_lines_~28_to_146
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_947_to_951
    action: preserved_and_flagged
    counts:
      Like: 67
      Love: 58
      (unlabeled — rendered as base64 data URI): 1
      Haha: 2
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_959_to_1023
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_1024_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #188 - Art, Music, Modding, Achievements

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Oct 22, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-188-art-music-modding-achievements.1863996/)
<!-- artifact:thread_metadata:end -->

Hello everyone! For the last of our *All Under Heaven* prerelease dev diaries, we’re covering a wide range of topics written by a wider range of authors. We know you’re eager to get to the New Stuff, so let’s get right into it.  

​

---

### 2D Art​

Hello, I’m Lucas Ribeiro, the 2D artist lead at Studio Black, and I’m here to bring you some insight into the work of our team.  

*All Under Heaven* has been a HUGE undertaking for the art team. The scale of the work necessary to bring East Asia to life is much greater than anything the team has gone through before, but at the same time, we were quite excited to tackle such a fresh subject matter. Some of us were quite unfamiliar with some of the themes we were to work with, so we depended on our friendly group of beta testers, native to the regions we are portraying, to steer us in the right direction. Shout-out to the Betas!  

### Loading Screen​

Our team started exploring the themes of the expansion with a few sketches. Our initial focus was on more intimate scenes, to represent the character-focused nature of CK3, but in a new locality. Placid scenes: poets and philosophers debating in serene, natural scenery. Elegant ladies floating along calm rivers.  

![image_01.jpg](https://forumcontent.paradoxplaza.com/public/1378522/image_01.jpg "image_01.jpg")



After a discussion with our Game Director, though, we ended up going in another direction. A bustling city, showing the cosmopolitan side of China. Scholars can be seen congregating before they head to an examination. This was also preferred for having more points of interest for the player to contemplate during loading times.  


![image_02.jpg](https://forumcontent.paradoxplaza.com/public/1378524/image_02.jpg "image_02.jpg")



![image_03.jpg](https://forumcontent.paradoxplaza.com/public/1378525/image_03.jpg "image_03.jpg")



## Story Events​

We were also tasked with creating images to represent the turning of the Dynastic Cycle.  

For the Stability Era, officials line up in front of the emperor. Their robe colors and their disposition in the room represent their rank.  

![image_04.jpg](https://forumcontent.paradoxplaza.com/public/1378526/image_04.jpg "image_04.jpg")



For the Tension Era, a slovenly official is carried by a group of downtrodden servants. The governor has abandoned his duties to the people in favor of his own indulgences. This represents the corruption and social tension brewing in the country.  

![image_05.jpg](https://forumcontent.paradoxplaza.com/public/1378527/image_05.jpg "image_05.jpg")



For the Chaotic Era, the peasantry is roused to action. The cycle of corruption has culminated in an explosion of violence. Though this is a moment of suffering, it also represents the opportunity for the rebirth of the country through the assertive action of a more righteous ruler.  

![image_06.jpg](https://forumcontent.paradoxplaza.com/public/1378528/image_06.jpg "image_06.jpg")



To go along with these illustrations, we have the Dynastic Cycle wheel. This interface element spins as the political situation in the Hegemony of China shifts. You can also see that the stability phase has two variants, one with the tiger (expansion), another with cranes (advancement).  

![image_07.jpg](https://forumcontent.paradoxplaza.com/public/1378530/image_07.jpg "image_07.jpg")



Besides the Chinese dynastic cycle story event images, we also have a beautiful splash image for Japan. What we had in mind was the ascension of the first Shogun to power, an event that would take place a while after our latest starting date. This should pop up when Japan is about to go through some *big* transformations.  

![image_08.jpg](https://forumcontent.paradoxplaza.com/public/1378531/image_08.jpg "image_08.jpg")



## Event Backgrounds​

While sometimes we could use some “generic” western backgrounds in many situations when dealing with non-western cultures without causing dissonance, *All Under Heaven* required us to go all-out and create a new version of basically every type of standard event background for an Asian context. We focused on China, but hopefully the imagery is tangential enough to pass in other nearby regions. So, when your character visits a roadside inn or talks to a fellow gentleman in a garden, everything should look fitting to our new setting.  

![image_09.jpg](https://forumcontent.paradoxplaza.com/public/1378532/image_09.jpg "image_09.jpg")



![image_10.jpg](https://forumcontent.paradoxplaza.com/public/1378533/image_10.jpg "image_10.jpg")



![image_11.jpg](https://forumcontent.paradoxplaza.com/public/1378534/image_11.jpg "image_11.jpg")



![image_12.jpg](https://forumcontent.paradoxplaza.com/public/1378535/image_12.jpg "image_12.jpg")



![image_13.jpg](https://forumcontent.paradoxplaza.com/public/1378537/image_13.jpg "image_13.jpg")



We also have new backgrounds to put our characters in the middle of the newly added natural disasters.  

![image_14.jpg](https://forumcontent.paradoxplaza.com/public/1378538/image_14.jpg "image_14.jpg")



In total there are over 36 new event backgrounds, not all of them pictured here.  

## Activities​

### Debates​

The political movements in China seek to steer the direction of the Dynastic Cycle.  

Players can engage in debates to further their personal position within the movement, as seen on the first image, where the characters are engaged in an intimate, political setting. The second image shows the struggle of the political movements in front of the emperor. The movement leaders present the case for their own vision of what China’s future might be like.  

![image_15.jpg](https://forumcontent.paradoxplaza.com/public/1378539/image_15.jpg "image_15.jpg")



## Examinations​

For Examinations, we had the task to represent Stewardship, Martial or Learning focuses in the activity  

![image_16.jpg](https://forumcontent.paradoxplaza.com/public/1378542/image_16.jpg "image_16.jpg")



### Tour Arrival Screens​

With every system that is introduced in the game, we add a new concern when expanding our game world. For tour arrivals, for example, we needed new imagery that would make sense in the East Asian context.  

![image_17.jpg](https://forumcontent.paradoxplaza.com/public/1378543/image_17.jpg "image_17.jpg")



### Holding Illustrations​

With the addition of so many new religions, cultures, and government types, of course we had to create new holding artwork to represent them and go along with our awesome new on-map assets.  

![image_18.jpg](https://forumcontent.paradoxplaza.com/public/1378546/image_18.jpg "image_18.jpg")



### Legacy Tracks​

We had the chance to add three new legacy tracks with *All Under Heaven*. For China, our focus was on metropolitan life; scholarly pursuits and courtly politics. For Southeast Asia, our focus was on building temples and positioning yourself as a god-like being. For Japan, our focus was on the intersection between family, art, poetry, and martial endeavors.  

![image_19.jpg](https://forumcontent.paradoxplaza.com/public/1378547/image_19.jpg "image_19.jpg")



### UI Skin​

With *All Under Heaven* we introduce another new UI Skin for CK3. This will be used for most East-Asian cultures. Additionally though, we have reworked how our UI is structured so that skins can affect a lot more than window margins and the main game HUD. Most primary UI elements such as the window backgrounds and decorative patterns are now also skinnable. Players will observe when playing with our new East Asian skin that headers have a wave pattern instead of the original diamond one. The main color theme of the game, a sober dark blue, is substituted by a calming dark green. Hopefully, this will also allow modders to take their own game skins even further.  

![image_20.jpg](https://forumcontent.paradoxplaza.com/public/1378548/image_20.jpg "image_20.jpg")



## Coat-of-Arms​

With so many new and diverse cultures added to *All Under Heaven*, the way we worked with coat-of-arms just couldn’t cover it anymore. We have introduced culture-based frames for house and dynasty coat-of-arms. There are now over 30 house frames distributed across the medieval world.  

![image_21.png](https://forumcontent.paradoxplaza.com/public/1378549/image_21.png "image_21.png")



![image_22.png](https://forumcontent.paradoxplaza.com/public/1378550/image_22.png "image_22.png")



We also have a wide variety of new templates for randomly generated coat-of-arms for China and Japan.  

Chinese coat-of-arms are inspired by seal stamps. We have added a new way for the coat-of-arms generation system to check for specific dynasty (or house) names and then find a corresponding emblem to add. This way, if a character’s house is “Li (674e)”, then there’s a high likelihood that the randomly generated CoA will include that specific character.  

Besides their house characters, the seal stamps can include decorative frames, shaped like beasts or objects. The seals can also share space with animals for further adornment.  

Here are four randomly generated CoAs that are using a character’s dynasty name.  

![image_23.jpg](https://forumcontent.paradoxplaza.com/public/1378552/image_23.jpg "image_23.jpg")



For Japan CoAs, we wanted to really understand the thought process behind how Kamons were created. To this end, instead of creating popular and well-known Kamons in a single, solid shape, we dissected them into small modular pieces. We identified several types of modules and how they interacted with each other (such as small branches that can either bloom vertically or spread out radially from the center). Our 98 new emblems can then be combined across 100 templates, creating an enormous number of possible Kamons  

![image_24.gif](https://forumcontent.paradoxplaza.com/public/1378554/image_24.gif "image_24.gif")



![image_25.jpg](https://forumcontent.paradoxplaza.com/public/1378555/image_25.jpg "image_25.jpg")



For Realm CoAs, we have a large variety of government types at this point. This means, some emblems looked awkward on some government types as the shapes of the flags would make them look offset, too big, or too small. Even worse, should a character change their government type, some flags looked horrendous when transposing an emblem to a different shape.  

To remediate this, we have introduced scriptable scaling and offset for realm flags, depending on government type. This means, when designing a CoA, one does not need to worry about nudging elements to fit an awkwardly shaped flag, as long as your design is centered, it will be properly placed in the flag shape. On the following screenshot you can see how this is clearly applied to the Ritsuryo flag, moving the center of the emblem to the left to account for the indentations.  

![image_26.jpg](https://forumcontent.paradoxplaza.com/public/1378557/image_26.jpg "image_26.jpg")



Hopefully, our players will have a great time creating their own CoAs by exploring our modular emblems. The “dynasty name triggers” for emblems also open a lot of space for modders, should they want to connect emblems with specific names (As in, one could set it up that a name like Canossa is more likely to trigger the dog emblem). The new flag offsets will also open a lot of space for easier CoA scripting and more creative flag shapes.  

![image_27.jpg](https://forumcontent.paradoxplaza.com/public/1378559/image_27.jpg "image_27.jpg")



## Men-at-Arms​

Every non-culture specific men-at-arms was, up to this point, represented by mostly western looking illustrations. With the addition of East Asia, we would’ve been stretching this too far. We have reworked how the men-at-arms’ illustrations are set up, so that it is now possible to use cultural triggers to pick which image is to be used. (we also took the opportunity to make the original heavy cavalry and light cavalry a bit more historically grounded and visually consistent with the others)  

![image_28.jpg](https://forumcontent.paradoxplaza.com/public/1378560/image_28.jpg "image_28.jpg")



We look forward to seeing if modders will use this new and easy way of adding cultural variations for MAA’s.  

When it comes to siege weapons though, we opted to, instead of using Asian reskins, have altogether unique siege engines for Asia. These will have their own attributes, map graphics, and art.  

![image_29.jpg](https://forumcontent.paradoxplaza.com/public/1378561/image_29.jpg "image_29.jpg")



Of course, we also have unique cultural men-at-arms, such as the Hwacha, Firelancers, Samurai (Mounted-Archer or otherwise), Pesilat Warriors and more.  

![image_30.jpg](https://forumcontent.paradoxplaza.com/public/1378563/image_30.jpg "image_30.jpg")



Now that the gunpowder innovation might drift through the silk road, we have also added new art to represent early western handgunners.  

![image_31.jpg](https://forumcontent.paradoxplaza.com/public/1378565/image_31.jpg "image_31.jpg")



## Estates​

Celestial, Meritocratic, Soryo and Ritsuryo characters have estates, much like administrative characters. Following up with what we started with Mongol domiciles, we have used a more Asian inspired illustration style for these cultures. There is a set of buildings dedicated to China and one for Japan, with a small overlap. We hope to have created a large variety of quaint and quirky paintings to represent your ever-expanding family estate.  

![image_32.jpg](https://forumcontent.paradoxplaza.com/public/1378567/image_32.jpg "image_32.jpg")



![image_33.jpg](https://forumcontent.paradoxplaza.com/public/1378568/image_33.jpg "image_33.jpg")



Thanks for reading the 2D art segment of today’s dev diary!  

There’s honestly a lot more work that will have to go unmentioned, such as many new UI elements, hundreds of icons, decision images, great project illustrations. But I hope this gives you a glimpse into what the 2D art team has been up to in *All Under Heaven*.  

---

### 3D Art​

Heya everyone! I am the 3D Environment Lead for Crusader Kings III, and I am here to talk a little bit about some of the work we’ve put together for our upcoming release, *All Under Heaven*! As artists, we often work with references to create many of the intricate sculptures and environments that you are used to seeing for our DLCs. Up until *All Under Heaven*, we’ve mostly been working with references from the Western world - museums, libraries, archaeological sites. These were often translated into, or at the very least, searchable in English.  

However, since this time we had to rely on reference libraries from Asia, the language barrier proved a much bigger challenge than we expected! Luckily for us, we’ve been truly fortunate to have a fantastic community that has helped us source and translate many of the references that we ended up using for this expansion. Additionally, the feedback we received from our beta group has proven invaluable in iterating our designs in order to provide the most immersive experience possible of Medieval Asia  

With the rest of the dev diary, I want to take you through some of the many different pieces of content we worked on.  

### Throne Rooms​

We are excited to share a glimpse of the Tang and Song Dynasties throne room with you, a space we’ve carefully crafted to capture the elegance, symbolism, and atmosphere of the era.  

From ornate architectural elements to subtle decorative details, this room is the result of close collaboration between the team and our dedicated beta testers. Their feedback, particularly in research and historical reference gathering, was instrumental in shaping the final design.  

While the throne room went through many iterations, each step helped us get closer to the authentic look and feel we were aiming for. Early on, we faced challenges due to a lack of accurate references, and our first version, created before the beta program, ended up drawing more from the Ming Dynasty than intended.  

Thanks to our community’s insight, we identified the historical mismatches and made the decision to rework the scene almost entirely. The result is a throne room we’re incredibly proud of, one that feels richly rooted in the Tang and Song Dynasties’ visual identity.  

It was a big undertaking, but absolutely worth it to bring this important piece of history to life with the care and accuracy it deserves.  

![image_34.png](https://forumcontent.paradoxplaza.com/public/1378570/image_34.png "image_34.png")


*[Release version of the Chinese Imperial throne room]*  

There are still a few leftover elements, like the wooden screen, which haven’t been fully updated yet. Consider them historical Easter eggs… or reminders of how far the room has come!  

![image_35.png](https://forumcontent.paradoxplaza.com/public/1378572/image_35.png "image_35.png")


*[Release version of the Chinese Imperial throne room]*  

Early previews of this throne room generated more community feedback however, saying that our version was too austere! We’ve made some tweaks to the throne room as a result; the updated throne room will be available in a post-release update after *All Under Heaven* releases. For now, here’s a quick look at the updated version.  

![image_36.png](https://forumcontent.paradoxplaza.com/public/1378574/image_36.png "image_36.png")


*[Updated throne room, releasing with 1.18.1]*  

![image_37.png](https://forumcontent.paradoxplaza.com/public/1378575/image_37.png "image_37.png")


*[Updated throne room, releasing with 1.18.1]*  

![image_38.png](https://forumcontent.paradoxplaza.com/public/1378577/image_38.png "image_38.png")



A sneak peek behind the scenes! We gathered references from a wide range of sources - including online museum collections, historical texts, and even Chinese films and TV series to help establish the mood and atmosphere. And of course, our community helped out a ton!  

![image_39.png](https://forumcontent.paradoxplaza.com/public/1378579/image_39.png "image_39.png")



![image_40.png](https://forumcontent.paradoxplaza.com/public/1378580/image_40.png "image_40.png")


*[First iteration of the Chinese throne room.]*  

We’re actually quite fond of this version, and we’ve been toying with the idea of bringing it back someday as an optional variant, so if that’s something you'd like to see, let us know!  

We’ve also added a Japanese throne room in this expansion. Some of you keen-eyed players may notice that this particular throne room is inspired by 17th-century architecture. Due to limited historical references from the correct time period, we occasionally take creative liberties, but we always aim to ground those choices in reality. In this case, we drew inspiration from Nijō Castle, which technically postdates the game’s timeframe.  

We’re always open to feedback, so after you’ve played *All Under Heaven*, let us know what you’d like to see done differently in the future. Your input helps shape our work. While it may not be 100% period-accurate, we hope you’ll fall in love with this throne room just as we did. Below are some beauty shots and close-ups of the tiling materials and custom assets we created for it.  

![image_41.png](https://forumcontent.paradoxplaza.com/public/1378581/image_41.png "image_41.png")



![image_42.png](https://forumcontent.paradoxplaza.com/public/1378582/image_42.png "image_42.png")



![image_43.png](https://forumcontent.paradoxplaza.com/public/1378583/image_43.png "image_43.png")



![image_44.png](https://forumcontent.paradoxplaza.com/public/1378584/image_44.png "image_44.png")



![image_45.png](https://forumcontent.paradoxplaza.com/public/1378585/image_45.png "image_45.png")


*[First iterations of the Japanese throne room. Here we were testing out the composition and layout of the room.]*  

## Special Buildings​

As we expanded into all of Asia, we knew we'd need *a lot* more holding models to represent the diverse architecture across the region. Thankfully, with the amazing help with both research and creation from modders Kefir úr and PiGu we could make this happen.  

Here are some of the new special buildings you’ll see on the map in-game!  

![image_46.png](https://forumcontent.paradoxplaza.com/public/1378587/image_46.png "image_46.png")



### Chang’an City​

Bringing Chang’an to life was a complex task. As the largest city in the world for much of its history, and the heart of imperial China during the Tang dynasty, Chang’an was a political, cultural, and economic center at the eastern end of the Silk Road. Its immense scale and global influence made it essential to capture in the game.  

We aimed to capture key landmarks such as Daming and Taiji Palaces, the Imperial City, and both the Small and Giant Wild Goose Pagoda. We also wanted to portray the Silk Road passing through Jinguang Gate, the bustling Eastern and Western Markets, and Chunming Gate, while highlighting the monumental Mingde and Dangfeng Gates.  

Trying to strike a balance between historical accuracy and playability, we scaled up important locations for clarity while still conveying the vast scale of this incredible city.  

![image_47.png](https://forumcontent.paradoxplaza.com/public/1378588/image_47.png "image_47.png")



### Holdings​

Here are just a few of the new holding models you’ll spot while playing in Asia.  

![image_48.png](https://forumcontent.paradoxplaza.com/public/1378589/image_48.png "image_48.png")


*[Japanese castles and wall tiers]*  

![image_49.png](https://forumcontent.paradoxplaza.com/public/1378590/image_49.png "image_49.png")


*[Southeast Asian temple and wall tiers]  

![image_50.png](https://forumcontent.paradoxplaza.com/public/1378591/image_50.png "image_50.png")


[Chinese Castles and wall tiers]*  

![image_51.png](https://forumcontent.paradoxplaza.com/public/1378593/image_51.png "image_51.png")


*[Southeast Asian Tribal Temple tiers, Holy Site, and village.]*  

![image_52.png](https://forumcontent.paradoxplaza.com/public/1378594/image_52.png "image_52.png")


*[Japanese Pagodas and Temples]*  

## Artifacts​

Here are some highlights of all the new court artifacts and character props that you’ll encounter in this expansion. Here we must thank our beta community once again for helping with picking fitting artifacts for this expansion and sending really nice references.  

Below is a Chinese armillary sphere, a Korean incense burner and a Kagura suzu.  

![image_53.png](https://forumcontent.paradoxplaza.com/public/1378595/image_53.png "image_53.png")



Below you can see a selection of Chinese, Japanese and Korean weapons as well as a Khmer shield, a guqin, a go game and hanging wall decorations among other things.  

![image_54.png](https://forumcontent.paradoxplaza.com/public/1378596/image_54.png "image_54.png")




![image_55.png](https://forumcontent.paradoxplaza.com/public/1378597/image_55.png "image_55.png")



![image_56.png](https://forumcontent.paradoxplaza.com/public/1378598/image_56.png "image_56.png")



![image_57.png](https://forumcontent.paradoxplaza.com/public/1378599/image_57.png "image_57.png")



*[Song dynasty pedestals and lectern.]*  

### Map Table​

For *All Under Heaven*, we designed a Song Dynasty–inspired map table that reflects the aesthetics and symbolism of the period.  
Scattered across the table are subtle references to the Four Treasures of the Study - the inkstone, brush, paper, and inkstick. Essentials on any classical scholar’s desk.  

![image_58.png](https://forumcontent.paradoxplaza.com/public/1378600/image_58.png "image_58.png")



You’ll also find Dingsheng cakes, each inscribed with '定勝,' meaning “Certain Victory.”  

The table features various celadon wares, prized during the Song Dynasty for their jade-like color, such as a vase with a chrysanthemum floral arrangement.  

For this expansion, we experimented with baking the lighting directly into the assets on the map table, not only to capture subtle effects like subsurface scattering on elements such as the flowers and cookies, but also to achieve more detailed shadows. A welcome side effect of this approach is improved performance: by baking the lighting into a single texture rather than using multiple, we reduce the overall texture load.  

![image_59.png](https://forumcontent.paradoxplaza.com/public/1378601/image_59.png "image_59.png")



## Map Update​

We already had a Dev Diary especially dedicated to the new map updates, but we’ve been hard at work iterating on the terrain since then. So here are a few fresh screenshots! The map will be an ongoing area of focus for us, so expect to see more exciting things happening on it in future patches.  

![image_60.png](https://forumcontent.paradoxplaza.com/public/1378602/image_60.png "image_60.png")



![image_61.png](https://forumcontent.paradoxplaza.com/public/1378603/image_61.png "image_61.png")



## Animation​

As this expansion covered many new cultures, we wanted to avoid having the western-based animations be the default, so we added new idle animations to differentiate them. The new ones use a mix of the old system of picking the new idle animations based on their traits, and the new holding Hu animations. There are also variations of some other animations, such as drinking:  

![image_62.gif](https://forumcontent.paradoxplaza.com/public/1378604/image_62.gif "image_62.gif")

![image_63.gif](https://forumcontent.paradoxplaza.com/public/1378605/image_63.gif "image_63.gif")


*[New drinking vs old drinking]*  

As some modders *may* have noticed, we added more joints to our skeletons in *Khans of the Steppe*. In *All Under Heaven* you will see why! Because of these new joints, our sleeves will no longer ignore gravity and will allow for longer sleeves. Something much needed for the type of fashion we’ve recreated!  

![image_64.gif](https://forumcontent.paradoxplaza.com/public/1378608/image_64.gif "image_64.gif")


*[Conversation while fanning]*  

We of course need some new culturally appropriate curtseying animations as well!  

![image_65.gif](https://forumcontent.paradoxplaza.com/public/1378613/image_65.gif "image_65.gif")

![image_66.gif](https://forumcontent.paradoxplaza.com/public/1378614/image_66.gif "image_66.gif")


[*Zuoyi Bowing, Female and Male*]  

![image_67.gif](https://forumcontent.paradoxplaza.com/public/1378626/image_67.gif "image_67.gif")

![image_68.gif](https://forumcontent.paradoxplaza.com/public/1378627/image_68.gif "image_68.gif")


*[Baoquan Martial Bowing, and Bowing low/Prostrating]  

All Under Heaven* has been one of our most ambitious expansions yet. It features the largest number of new assets we’ve ever created for a DLC and marks our first deep dive into this fascinating region of the world. It came with its fair share of challenges, but exploring such a rich and complex historical setting has been incredibly rewarding for the whole team.  

We’ve poured a lot of passion into bringing these eras to life, and we truly hope you’ll love playing this expansion as much as we’ve loved creating it.  

Thank you for reading, and we can’t wait for you to have your hands on *All Under Heaven* on October 28th!  


​

---


Hey there! Welcome to another Dev Diary, this time focused on Audio. Audio isn’t just music, as you’ll see—it also includes sound design, ambiences, interactions, and even the systems behind them. Today, we’re going to talk about both sides of that coin. I’m Leon Lopez Moral, Sound Designer for this expansion, and along with my colleague Robert Wozniak, we will introduce you to the work we did for this expansion.  

### How Sound Can Take You Elsewhere​

Sound has the power to transport us to other places. It can evoke a sense of time, space, and history. But how do we achieve that? With a lot of research. And when we say a lot, we mean it.  

![image_69.png](https://forumcontent.paradoxplaza.com/public/1378628/image_69.png "image_69.png")



We investigate what kinds of metals were used, what landscapes sound like, how to accompany illustrations, and how culture itself plays a role. This time, we had to understand the many differences between cultures and make them recognizable through their sounds. Think of the **hyōshigi**—two wooden clappers traditionally struck together at the start of ceremonies in Japan’s feudal era—monks’ chants, or different bells. What does each gong mean? And we can’t settle for the typical gong we hear in movies. (Yes, it sounds cool, but the world of gongs is vast!)  

![image_70.png](https://forumcontent.paradoxplaza.com/public/1378629/image_70.png "image_70.png")



From imagining how kitchens in imperial China might have sounded—clay pots bubbling over open flames, the rhythmic chopping of vegetables on wooden boards—to the bustling life of a crossroad inn in the heart of the countryside. We design ambiences to be true to what you see on screen, but also to feel alive: distant conversations blending with the clinking of mugs, a sudden neigh from a horse outside, a gust of wind rattling wooden shutters. Every element is placed so that, even with your eyes closed, you can picture exactly where you are. And, as always, our goal is to make you not just see the world of CK3, but hear and feel it all around you.  

## When Sound Becomes Ceremony: From Blades to Bronze​

But it’s not all about ambience… it’s also about stories! There are pivotal moments in a realm’s history that demand sound design to tell their tale. Whether a dynasty is solidifying, corruption is spreading, or stability reigns, audio helps convey that narrative.  

This ties directly into what we think of as the **Dynasty Cycle**—the rise, fall, and renewal of power. Some of these moments are inherently visual: revolutions with crowds marching through the streets, the flicker of torches raised in protest, or the heavy stillness of a ruler’s court when corruption has taken hold. We translate these images into sound.  

Chains rattling in the distance, metallic clinks that speak of oppression, the weary and subdued murmur of voices weighed down by hardship—each element reinforces the story. Even **silence** becomes one of our most powerful tools: it can magnify the tension before unrest erupts, convey the suffocating atmosphere of tyranny, or highlight the weight of a ruler’s unchallenged authority.  

Perhaps the greatest challenge for us was the Shogunate. Japan’s history is deeply symbolic and steeped in ritual. Take the ceremonial investiture of a shogun, where the deliberate, singular motion of drawing a katana embodies authority and solemnity.  

We wanted to capture that exact moment in sound: the katana, drawn in one ceremonious, deliberate gesture, producing a crisp, resonant note of steel cutting through silence. The sound had to feel dry and immediate, yet loaded with centuries of tradition—a strike that resonates with the weight of power, respect, and history.  

And it wasn’t just the katana. We also delved into the world of **Chinese gongs**, each with its own distinctive pitch, resonance, and ceremonial meaning. From the deep, commanding tone of a temple gong marking a ritual’s start, to the brighter, sharper strikes used to punctuate announcements—we aimed to honor not just the instrument, but its cultural weight. Paired with proper context, these sounds become narrative moments in their own right.  

## Stingers That Tell a Tale​

Stingers may be brief musical references, but they *tell stories*. In our Japanese-themed content, we looked beyond the shamisen—since it didn’t exist during the early centuries—and instead embraced instruments authentic to that era, such as **taiko drums** (used for announcements and marches, not in later performance drumming contexts) and the refined court music tradition known as **Gagaku.  


![image_71.png](https://forumcontent.paradoxplaza.com/public/1378632/image_71.png "image_71.png")



Gagaku** is the oldest surviving orchestral music in Japan, performed at imperial courts with a blend of wind, string, and percussion instruments. It is characterized by its serene, floating melodies and stately rhythm, often using instruments like the **hichiriki** (a double-reed flute), **ryūteki** (a transverse flute), and **sho** (a mouth organ). Together with gentle drums and stringed instruments, Gagaku evokes a sense of gravitas, ceremony, and age-old nobility. By weaving Gagaku-inspired stingers into our audio, we capture the elegance and authority of imperial Japan—each short chord or flourish carrying the weight of tradition and cultural depth.  

So, how did we make this centuries-old genre sound real in the game? The answer is simple: we have a dedicated team for it. Our team worked together to study the instruments, performance techniques, and recording approaches that would make Gagaku authentic in both tone and feel. They sourced historical references, analyzed playing styles, and recreated the unique timbre of each instrument.  

And speaking of the people behind the music… It's the perfect moment to hand the stage over to our music team, so they can tell you how they transformed these ideas into the soundtrack you’ll hear in-game.  

## Music​

Hello, everyone. Ernesto Lopez here, Audio Director for *Crusader Kings III*. I am aware how much you like the music of our different expansions, and I’m happy to report that this time, we pushed as much as we could for you. So, I’m bringing you a behind-the-scenes look at the music for ***All Under Heaven*** and how we worked to capture the spirit, scale, and diversity of East Asia within CK3’s musical identity.  

### Crafting a Cohesive Soundscape​

For this expansion, we set out to create a body of music that feels varied and unified. We recorded two substantial bulks of new content—one drawing on a broad range of East Asian influences, and another built around the traditions of Imperial China. By developing them side by side, we ensured they complement each other, blending breadth and depth into a single, cohesive listening experience.  

This resulted in over **65 minutes** of fully recorded, authentic music—22 unique tracks, including a fantastic rendition of our Main Theme “The Dynasty”. You’ll hear traditional instruments such as guzheng, erhu, koto, shakuhachi, pipa, guqin, and taiko, all performed with care and attention to cultural authenticity while maintaining the orchestral style that defines CK3.  

Every piece was written to serve the player’s journey—whether you’re navigating court intrigue in China, leading armies across the steppes, trading along the Silk Road, or enjoying the quiet reflection of a palace garden. The music for this expansion will suit and serve for all these moments.  

We can’t wait for you to hear it all when *All Under Heaven* releases on October 28th! For now though, here’s a small collection of music tracks to serve as an appetizer.  

[https://www.youtube.com/embed/GsqoGYhvA0U?wmode=opaque](https://www.youtube.com/embed/GsqoGYhvA0U?wmode=opaque)


[https://www.youtube.com/embed/PtEpseU38_4?wmode=opaque](https://www.youtube.com/embed/PtEpseU38_4?wmode=opaque)


[https://www.youtube.com/embed/jTQV3v9QijM?wmode=opaque](https://www.youtube.com/embed/jTQV3v9QijM?wmode=opaque)


[https://www.youtube.com/embed/5e7zMa1vfE8?wmode=opaque](https://www.youtube.com/embed/5e7zMa1vfE8?wmode=opaque)


[https://www.youtube.com/embed/Z1sGyppc1IU?wmode=opaque](https://www.youtube.com/embed/Z1sGyppc1IU?wmode=opaque)




​

---


### Modding​

Ladies and gentlemen! Scoundrels and blaggards! Nobles and knights! Welcome to the JonZone and join me in giving a shout-out to the most hallowed of all players. The kind of player that looks at a map filled with near™ ***infinite*** possibilities - and says “I’d like to make it ***infinitier***. Dearest modder, fulfiller of dreams and complicator of our jobs - this one goes out to you. Today we’re going to go behind the curtains and show off a few of the scripting and modding toys arriving with *All Under Heaven*!  

The first improvement for scripters and modders regards our new *Graphical Unit Types.* Let me paint you a picture:  
You’re playing as the Sultan Muhammad ibn Abd al-Rahman of Andalusia in 867. You’re desperately fighting off the Christians. You open the military view - and the icons of your Fāris look like this.  

![image_72.png](https://forumcontent.paradoxplaza.com/public/1378633/image_72.png "image_72.png")



These things might not be the biggest “game breaking bugs” so to speak - but they add up to bring you out of the immersion we’re trying to reach. Well - we wanted to see if there was something we could improve here with as much *bang for the buck* as possible - and I believe we have done so with the new system of graphical unit types. With this, we can easily switch these illustrations out in all kinds of places.  

We already have a lot of places in the code where we define the 3d graphics to be tied to certain unit_gfx. This allows us to nicely swap out the illustrations of knights and levies by simply hijacking the unit_gfx and adding an entry for it inside our new 00_graphical_unit_types.txt. This allows us to always make sure your illustrations match the graphics of your units.  

![image_73.png](https://forumcontent.paradoxplaza.com/public/1378634/image_73.png "image_73.png")



![image_74.png](https://forumcontent.paradoxplaza.com/public/1378635/image_74.png "image_74.png")



Suddenly, our Fāris look much more proper.  

![image_75.png](https://forumcontent.paradoxplaza.com/public/1378636/image_75.png "image_75.png")



And this can be added for all kinds of models! Do you feel like the Norse levies have a distinct lack of frosted tips and baseball bats that have gone untouched for too long? Say no more. Simply make a new .dds image and place it into the gfx\interface\illustrations\graphical_unit_types\ folders with the corresponding name.  

![image_76.png](https://forumcontent.paradoxplaza.com/public/1378637/image_76.png "image_76.png")



This will also show up in battles and such, reflecting the true status of your culture. No more will battle reports show western crusaders versus western crusaders - when you’re trying to secure the Indus River.  

The second improvement I’d like to highlight is some additions to the tools available to the avid modder or scripter - when it comes to innovations and culture fascinations.  

First, innovations are finally accepted as their own scopes. We now also have unlocked the following effects for your discretion:  

For any general innovation:  


- *add_innovation_progress*
  * This one adds X percentage of progress to any innovation. You can hardcode it if you’d like - or send in a saved innovation scope.
- *add_innovation_progress_time*
  * This one adds X amount of months to any innovation. You can hardcode it if you’d like - or send in a saved innovation scope.
For the spread of innovations from one culture to another:  


- *add_spread_progress*
  * This one adds X percentage of progress to the current spread of an innovation.
- *add_spread_progress_time*
  * This one adds X amount of months to the current spread of an innovation.

For the cultural fascination:  


- *add_fascination_progress*
  * This one adds X percentage of progress to the current cultural fascination.
- *add_fascination_progress_time*
  * This one adds X amount of months to the current cultural fascination.

Some extra effects for bonus fascinations:  


- *set_bonus_fascination_innovation*
  * *S*ets the current bonus fascination to a specified innovation. This can be hard-coded - or you can send in a saved innovation scope.
- *remove_bonus_fascination_innovation*
  * This one kind of does what it says on the tin, and simply removes the previous bonus fascination.

All these commands also accept scripted values, to hopefully accept and support any wild ideas modders want to throw at it.  

We are also aware of how much modders itch to be able to have better control of the AI - and we’re doing our best to open more doors for you. Something we have added to culture innovations is the following ai_values:  


- *ai_weight_for_spread*
  * How likely the AI is to select this particular innovation to spread to other cultures.
- *ai_weight_for_fascination*
  * How likely the AI is to select this particular innovation as the current cultural fascination. Perhaps an AI cultural head with a martial education would have a higher weight for selecting military to explore siege weapon innovations for example.


![image_77.png](https://forumcontent.paradoxplaza.com/public/1378638/image_77.png "image_77.png")



Innovations, much like the graphical unit types - can also now have their names and icons be dependent on culture, through a new asset system:  

![image_78.png](https://forumcontent.paradoxplaza.com/public/1378639/image_78.png "image_78.png")



Governments have received some new fancy toys as well! Did you ever feel like you wanted to add some kind of Lovecraftian mega-theocracy where you can rise through never-ending ranks of faith while being capped to only two tiers of prestige? No problem. Simply add the following script to the government in question:  

![image_79.png](https://forumcontent.paradoxplaza.com/public/1378640/image_79.png "image_79.png")



If nothing is added - it will simply revert to the default value as defined in *00_define.txt*.  

With these dynamic values - we open a ton of different doors. To give you the maximum creativity - we have also added the possibility of modifiers that can add even more cap to your rulers, like *character_max_piety_level_add.*  


![image_80.png](https://forumcontent.paradoxplaza.com/public/1378641/image_80.png "image_80.png")



Currently, we have mostly used these for the new Mandala government - with various religious modifiers - but the world is your oyster - and as usual - we expect our modders to bend and break the game restrictions in ways we couldn’t envision ourselves. Maybe a salmon shapeshifter in Ireland would be able to reach higher tiers of prestige than ever before - or perhaps an orc is capped to a certain tier of prestige depending on their prowess. I personally ***dare*** you to surprise me.  

![image_81.png](https://forumcontent.paradoxplaza.com/public/1378642/image_81.png "image_81.png")


*[An especially prestigious salmon shapeshifter.]*  



Governments can also now be specified to a *family* of governments, by giving them access to the field *mechanic_type.* This essentially makes the code-part of the game treat the custom government as another government. This is especially useful for new custom modded governments, since they can’t access the codebase in the same way that designers can force us code-monkeys to help them with. If you want to make a new kind of herder government that is meant to herd some kind of living mushroom - you can just set the mechanic_type like this  

![image_82.png](https://forumcontent.paradoxplaza.com/public/1378643/image_82.png "image_82.png")



And et voilà - the codebase will treat your custom government as a herder government. The accepted values here are the following government mechanic types:  


- feudal
- mercenary
- holy_order
- clan
- theocracy
- administrative
- landless_adventurer
- herder
- nomad
- mandala

We have also added a few ai_values for you to help guide the AI a bit when playing as a government. A feudal ruler would want a vast personal kingdom - whereas a more administrative ruler would perhaps like more individual rulers controlling the realm in question.  

![image_83.png](https://forumcontent.paradoxplaza.com/public/1378645/image_83.png "image_83.png")



Something new and shiny for administrative realms is the *appointment_trait_flag* and the *appointment_trait_override*. This property is now part of the subject contract obligation (think administrative themes). In *All Under Heaven* - these are mostly used to split up the two celestial merit pools into civilian or militaristic depending on what education you have, but in theory - you could make this be whatever you’d like. Perhaps you’d like to make a government type where only the tallest people are fit to rule - and you have separate merit pools for giants. Again, we’d love to see what you do with it!  

Now - something exciting for modders - but maybe not as flashy to the players, I’d like to put yourself in their shoes for just one second. Let’s envision that you’re making a mod adding a ton of flavorized cultural council positions - that pretty much work the exact same way as they do in the base game - but you’d like the descriptions to be uniquely specialized for the different cultures / governments. Perhaps you’d like to add a new council position for a ***high court judge*** that is a mix of the chancellor and realm priest, and you’d like to make a mix of existing court tasks with new descriptions.  

Well now - you can now actually simply “clone” existing council tasks. This will make the task function exactly the same as the task that you’re cloning - but you can flavorize it however you like. Perhaps our new ***high court judge*** should be able to fabricate claims, much like a realm priest - but with another description. Well - we can simply clone the *task_fabricate_claim* and call it something else.  

![image_84.png](https://forumcontent.paradoxplaza.com/public/1378647/image_84.png "image_84.png")



Wham! Completely different! *It’s like a whole new game.* Again - not really something the end-player might notice - but indispensable for the budding modder.  

*“But JonZone! What about a new system for separate modifiers when a building is disabled?”* You might ask. Now that is an incredibly convenient coincidence - because I’m thrilled to announce: ***The separate modifiers when a building is disabled.***  

Let’s say you have made a mod in honor of ***The Flying Spaghetti Monster*** as a new and exciting world religion. You have a massive church in the style of a granite and marble carbonara. This is no doubt exciting and awe-inspiring to any culture or religion - and maybe you’d like the general occupier to get one set of modifiers even though it’s not technically active. Maybe it still gives the owner prestige. Perhaps it even gives them dread. Perhaps you’d like the building to actively drain money when not active. With the new separate modifiers - it’s all up to you. You can set the modifier to be one thing for active followers of the pasta-religion - and one other set of modifiers if it is disabled. A minor change - but with major possibilities and opportunities.  

Something else that could use a better segue, is the added support for saved variables within SituationSubRegions and SituationParticipantGroups! Situations - like the Great Steppe and the Dynastic Cycle - are something we see major potential in for modders. Essentially - situations are a building block to make super specific events that can either be located and relegated to specific areas of the map - or growing, breathing spectacles that could take over the entire world. What are the rules when it comes to what a situation should look like? That’s the neat part. There are no rules. This is one of those features that we’d love modders to go absolutely nuts with, and now you can do so with saved custom script variables.  

I’d also like to again bring up a great script tool that was mentioned in the performance dev diary. This is the tiered AI frequency. Now I know that all you users and players hate the idea of hamstringing the AI. However - I also know how much you hate when the simulation of your game doesn’t run to your hopes and expectations. Since this is always such a balance, that works differently from mod to mod, and hardware to hardware - why not try to see if you can balance the performance best yourself?  

![image_85.png](https://forumcontent.paradoxplaza.com/public/1378649/image_85.png "image_85.png")



With this frequency as part of the interactions you make - you can make sure that only the relevant tiers of AI rulers use the interaction! Or maybe reduce the number of times the game should check if they can do a certain interaction! Perhaps you have an amazingly complex super-decision - if you should try to become some phoenix prince and reshape the entire world in your own name, and it should be available to a wide variety of people - but only if they are a hegemon or emperor. Well now you can easily sort them into the correct buckets!  

Something final to mention - is that when we have tried to refactor and optimize interactions to the utmost potential that they can be - we have decided to deprecate the property *ai_potential*, and we urge you all to instead switch over to using *is_available*. This should now handle both the player and the AI interactions - and hopefully remove duplication of code / script. Of course - we haven’t removed *ai_potential* from being functional - it will still function as it did - we don’t want to break existing mods, but if you’re making new interactions or taking a gander at your old interactions - we recommend that you take the chance to remove annoying duplication of script!  

That’s a taste of what’s to come in *All Under Heaven* for script-enthusiasts! I’m sure there are many things that I failed to cover - but I invite you to explore our scripts yourselves come game release! Here’s to the modders! Here’s to the scripters! Here’s to all of you!  

​

---


Achievements  

Rounding out this Dev Diary, let’s talk about achievements! As always, we designed our achievements in a way to cover most of the critical paths for this expansion. There’s plenty of fun challenges here, no matter if you choose to play in China, Japan, or South-East Asia. It was also high time we paid service to our Hæsteinn aficionados (yes, we’ve seen the threads for people who were already discussing this run in particular).  

So, if you want to have maximum bragging rights for being the first in your friend group to unlock all of the *All Under Heaven* achievements, take a close look at the list below and start planning your runs. Let us know in the comments what you think the most ideal playthrough is to get most of them!  

### Very Easy​

![image_86.png](https://forumcontent.paradoxplaza.com/public/1378654/image_86.png "image_86.png")


**Easy  


![image_87.png](https://forumcontent.paradoxplaza.com/public/1378655/image_87.png "image_87.png")



Medium  


![image_88.png](https://forumcontent.paradoxplaza.com/public/1378656/image_88.png "image_88.png")



Hard  


![image_89.png](https://forumcontent.paradoxplaza.com/public/1378657/image_89.png "image_89.png")



Very Hard  


![image_90.png](https://forumcontent.paradoxplaza.com/public/1378658/image_90.png "image_90.png")**  

​

---


And that’s all we have for this week! Bringing *All Under Heaven* to life has been an incredible undertaking for our studio, and we’re beyond excited for you to finally get your hands on it when it releases next week.

<!-- artifact:reactions:start -->
- 67 Like
- 58 Love
- 9 (unlabeled — rendered as base64 data URI)
- 2 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 2 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
