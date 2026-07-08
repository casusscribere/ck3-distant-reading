---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1524239/"
forum_thread_id: 1524239
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 96
title: "Crusader Kings 3 Dev Diary #96 - Fate of Iberia 3D Art Showcase"
dd_date: 2022-05-10
author_handle: egghorse
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3363
inline_image_count: 37
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1524239'
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
    location: raw_lines_~28_to_140
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_139
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1946.jpg?1652186222
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_443_to_448
    action: preserved_and_flagged
    counts:
      Like: 127
      Love: 83
      (unlabeled — rendered as base64 data URI): 1
      Haha: 5
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_456_to_561
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_562_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1946.jpg?1652186222)
<!-- artifact:thread_banner:end -->

# Crusader Kings 3 Dev Diary #96 - Fate of Iberia 3D Art Showcase

<!-- artifact:thread_metadata:start -->
- Thread starter [egghorse](https://forum.paradoxplaza.com/forum/members/egghorse.1672622/)
- Start date [May 10, 2022](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-96-fate-of-iberia-3d-art-showcase.1524239/)
<!-- artifact:thread_metadata:end -->

Hey folks! I’m Lucia, one of the artists on CK3, and I will be your host for today. Together with Nils ([@NilsW](https://forum.paradoxplaza.com/forum/members/1192255/), 3D Character Art Lead) and Joacim ([@Carlberg](https://forum.paradoxplaza.com/forum/members/940169/), 3D Environment Art Lead), we are very excited to walk you through some of the new 3D art that you will soon be seeing all over the Iberian Peninsula and the process behind their creation. This will be a long one, so grab a hot beverage of your choice and enjoy the ride!  


### Goals​

With the Struggle being the main focus of Fate of Iberia, we decided early on that we would put equal attention into the portrayal of both the Muslims and the Christians there. The character art team has brought forth new headgear, clothes and hairstyles for both parties — which you might have seen floating around in the wilds of the web or in the trailer.  

Meanwhile, on the environment art side the focus has been on bringing life to the Iberian map. You might remember a few of the monuments featured in last week's Dev Diary, but this time we will give you a sneak peek into the creation process. Those of you who are looking to add some Iberian flavor to your courtrooms – fear not, we got you covered with several new court artifacts!  


### Character Assets​

Nils: When designing new clothes, headgear and hairstyles, the first step - unsurprisingly - is to decide how they should look. In stark contrast to most historical movies and TV shows, we actually *at least try* to base them on historical examples. With Fate of Iberia, we were fortunate that there are quite a few good sources available of how people dressed and looked in the Iberian peninsula during this time. So we start by collecting all the reference material we can find, put it in an enormous pile and begin forming an idea of what kind of assets we want to add. In addition to historical accuracy, we also look for things like interesting and unique appearance, how well it would translate to a 3D model (i.e. how much pain it’s going to cause us when making it), and if it fits in with other styles already in the game.  

As a bonus, a lot of nerd points can be earned during this process. I mean, who isn’t going to be impressed when you start casually throwing around Spanish or Arabic words for obscure medieval clothing items?  

Let’s look at some examples:

![FP2_clothes_01.jpg](https://forumcontent.paradoxplaza.com/public/824201/FP2_clothes_01.jpg "FP2_clothes_01.jpg")


*Showing reference image, concept art and the finished asset of one of the new Christian outfits. We designed these clothes primarily based on a 12th century manuscript illumination depicting Alfonso II of Aragon. The outfit consists of an undergarment with narrow sleeves called a Brial and a looser outer garment known as a Piel. The latter has decorative trims on sleeves, collar and at the hem of the skirt. Both Brial and Piel were often split in the front and back to better allow for riding.*  

![FP2_clothes_02.jpg](https://forumcontent.paradoxplaza.com/public/824266/FP2_clothes_02.jpg "FP2_clothes_02.jpg")



*One of the new Muslim outfits. This one was based mainly on an illustration in the 13th century “Codex Rico”, a part of the "Cantigas de Santa Maria" - A famous collection of four codices containing medieval poems with musical notation and many detailed illustrations. The image depicts the Almohad caliph Abu Hafs Umar al-Murtada wearing a loose robe known as a Jubba. On the upper sleeves are sewn on “Tiraz” bands, a very popular fashion throughout the medieval Islamic world. The sleeves and neck opening are also decorated with embroidered or brocade trims.*  

![FP2_clothes_03.jpg](https://forumcontent.paradoxplaza.com/public/824203/FP2_clothes_03.jpg "FP2_clothes_03.jpg")



*This is based on several sources depicting very similar styles of garments. The examples shown here are from an Andalusian manuscript telling the story called "Hadith Bayad wa Riyad" - An Arabic love story and the "Libro de los Juegos" (Book of games) - A 13th century book commissioned by Alfonso X of Castile containing rules for a large number of medieval board games as well as 150 miniature illustrations. As you can see the clothes are quite similar to the male garment above. Female and male fashions at this time generally had more similarities than differences, and sometimes it is even hard to tell whether an illustration portrays a man or a woman.*  

![FP2_clothes_04.jpg](https://forumcontent.paradoxplaza.com/public/824204/FP2_clothes_04.jpg "FP2_clothes_04.jpg")



*This Christian Armor is based on 13th century mural paintings of the Conquest of Majorca by James I of Aragon, presently found in Museu Nacional d'Art de Catalunya in Barcelona. The sword, with leaf shaped pommel and guard decorations, is based on a sword still in existence, allegedly from the 13th century, at the Royal Armory in Madrid. The armor consists of chainmail Hauberk with mittens, chausses (leggings), a surcoat and something called a “Perpunt” - a light gambeson worn on top of the rest of the armor for additional protection. For head protection a chainmail coif and a “Cervellera” helmet is worn. NGL, this must have been a sweaty experience in the Spanish summer!*  

![FP2_clothes_05.jpg](https://forumcontent.paradoxplaza.com/public/824205/FP2_clothes_05.jpg "FP2_clothes_05.jpg")



*This… interesting looking headdress is based on numerous examples from both illustrations and sculptures and must have been considered extremely fashionable at the time. It was probably constructed from strips of ruffled linen or silk wrapped around a light wood base, decorated with embroidered or woven bands and held in place by a “Barbette” (chinstrap). As with most things, the taller the better is the rule here!*  

![FP2_clothes_06.jpg](https://forumcontent.paradoxplaza.com/public/824206/FP2_clothes_06.jpg "FP2_clothes_06.jpg")



*The very badass helmet above might look like some impractical fantasy creation but is in fact based on numerous depictions in the "Cantigas de Santa Maria" illustrations. The conical shaped helmet is decorated with a large gilded metal leaf. A day when the Rule of Cool perfectly aligns with primary sources is a good day, in my book.*  

![FP2_clothes_07.jpg](https://forumcontent.paradoxplaza.com/public/824207/FP2_clothes_07.jpg "FP2_clothes_07.jpg")



*If we’re really lucky, there might be a suitable extant item that survives to this day, as is the case with this “Capiello” of Fernando de la Cerda, the heir of Alfonso X of Castile (Who seems to - Fernando that is - have had a very CK life and tragically died a father of two at the age of 19). This distinctive cylindrical headgear was hugely popular in 13th century Spain. An extant example like the one shown above is, of course, the ideal type of reference, but unfortunately very few medieval garments have survived in as good condition as this.*  

### Character Art Process​

So, we’ve decided what to do, that’s all nice and well, but what are the steps involved in actually creating one of these assets? Follow along in this exclusive behind the scenes look at the Character Art workflow! Exciting, right!  

![workflow_concept_art.jpg](https://forumcontent.paradoxplaza.com/public/824233/workflow_concept_art.jpg "workflow_concept_art.jpg")



Once we have the finished concept art, we start off in a program called Marvelous Designer to create a 3D version of the garment. This is similar to designing clothes in real life as you work with sewing patterns that are simulated to create a natural fall. Again, whenever possible, we try to base the patterns on surviving examples.  

![workflow_01.jpg](https://forumcontent.paradoxplaza.com/public/824208/workflow_01.jpg "workflow_01.jpg")


*The pattern, created using Marvelous designer, for one of the new female Christian outfits. This dress, called a Brial, is constructed based on historical patterns from similar garments that have survived to our time.*  

We then add any additional details by 3D modeling in a program like Maya or Zbrush. In this case, the belt and brooch at the neck were added at this stage.  

![workflow_02.jpg](https://forumcontent.paradoxplaza.com/public/824209/workflow_02.jpg "workflow_02.jpg")


*The final “High poly” model.*  

This model consists of several million polygons, which is too much to render in the game (if you appreciate frame rates above 0.1 anyway). Therefore, the next step is to create the “low poly” - meaning the model that will actually be exported to the game. We do this by matching the shape of the “high poly” model as closely as possible but with - you guessed it - a much smaller number of polygons (in this case around 4400, which is around 1000 times less than the high poly model!).  

![workflow_03.jpg](https://forumcontent.paradoxplaza.com/public/824254/workflow_03.jpg "workflow_03.jpg")


*Showing the “low poly” model being created with the “high poly” model as a guide.*  

The details are then transferred from the high to the low resolution mesh using a normal map. We do this in a software called Marmoset Toolbag.  

![workflow_04.jpg](https://forumcontent.paradoxplaza.com/public/824212/workflow_04.jpg "workflow_04.jpg")


*The models – both low and high –- imported into Marmoset Toolbag for the “baking” step. Coloring is temp.  

![workflow_04_textures.jpg](https://forumcontent.paradoxplaza.com/public/824213/workflow_04_textures.jpg "workflow_04_textures.jpg")


The resulting textures that we get out of Marmoset allow us to display all the fine details from the high poly mesh. From top left they are called Normal map, Curvature map, Ambient Occlusion map and Color ID map. This will all be on the test so you better pay attention.*  

We create textures in a program called Substance Painter. But because we use dynamic colors and materials in CK3 the textures at this stage are mostly a neutral white – in the game those white areas will make use of dynamic materials.  

![workflow_05.jpg](https://forumcontent.paradoxplaza.com/public/824262/workflow_05.jpg "workflow_05.jpg")



Before exporting to the game we need to create something called “blend shapes” - which we use to deform the asset to fit different body types. We also do something called “skin bind” at this stage - which means attaching the clothes to the skeleton that animates the body.  

![workflow_06.jpg](https://forumcontent.paradoxplaza.com/public/824216/workflow_06.jpg "workflow_06.jpg")


*Showing blend shapes before export. From left to right: Average, Overweight, Underweight, Muscular, Old.*  

![workflow_07.jpg](https://forumcontent.paradoxplaza.com/public/824217/workflow_07.jpg "workflow_07.jpg")


*Showing the clothes skinned (attached) to the rig (animation skeleton). The pose is anachronistic.*  

Finally, we are ready to export the asset and look at it in the game. This involves a considerable amount of scripting work to make sure the game knows how to find the asset and when it should show up, what it should be called, who should wear it and so on.  

![workflow_08.jpg](https://forumcontent.paradoxplaza.com/public/824218/workflow_08.jpg "workflow_08.jpg")



Above you can see the final result with dynamic materials applied. We created new sets of patterns and color combinations for the Iberian assets (of which you can see more examples in the screenshots below).  

After all that is done and looking good we can move on to working through the never-ending list of clipping bugs that arise when combining these assets with each other…  

And that’s all there is to it! As you can see, very quick and easy.  

![FP2_character_line_up.jpg](https://forumcontent.paradoxplaza.com/public/824259/FP2_character_line_up.jpg "FP2_character_line_up.jpg")


### Iberian Army Units​

With Fate of Iberia, we’re adding two new sets of army units representing the Christian and Muslim styles, to be used by Iberian heritage culture. Of course, each model represents a specific tier of army quality so we need to keep this in mind when designing their appearance. Generally, the first tier is supposed to represent something like a drafted peasant, the second tier a professional soldier, and the third tier a knight or equivalent.  

Below you can see the concept art and 3D models for all 3 Tiers of the Christian Unit. The Tier 1 model was mainly based on manuscript illustrations depicting commoners and peasants. As you can see, he is not wearing any armor at all. The simple armor of Tier 2 consists of a gameson and a steel helmet. Lastly, we have the Tier 3 unit model — its design is similar to the one used for the new Christian armor that characters can equip, and was based on the 13th century mural paintings of the Conquest of Majorca of James I of Aragon, currently found in Museu Nacional d'Art de Catalunya in Barcelona.  

![christianunits_1.png](https://forumcontent.paradoxplaza.com/public/824238/christianunits_1.png "christianunits_1.png")



Much like its Christian counterpart, the design of the Tier 1 Muslim unit represents an unarmored soldier wearing the same kind of clothes as a civllian. Tier 2 is also dressed similarly to the Christian Tier 2, with a gambeson and a helmet. Finally, the design for Tier 3 represents a more heavily armored warrior, with a hooded chainmail hauberk and helmet with noseguard.  

![muslimunits_1.png](https://forumcontent.paradoxplaza.com/public/824239/muslimunits_1.png "muslimunits_1.png")



Now, over to my eminent colleague Joacim for a look at the environment art side of things.  

### Ships​

Joacim: With the focus on Iberia and the intermingling and conflicts of the Mediterranean and middle eastern cultures, we’ve now added new ship type visuals for both the Mediterranean cultures, as well as those of the mena region. This should mean a lot less cogs sailing around the Mediterranean (spare the odd invasion, crusade or viking raid).  


### FoI-Ships.png

### Holdings​

For the Iberian peninsula we looked at creating a style of holding that represented the region and makes it stand apart from the Mediterranean, Western and MENA styles. Since Iberia was such a mix of cultures and architectural styles mingled between the cultures and religious influences, we’ve created a style that works for the area as a whole. Below you can see screenshots of the two Iberian cities together with four new castle models.  

![holdings_citiescastles.jpg](https://forumcontent.paradoxplaza.com/public/824230/holdings_citiescastles.jpg "holdings_citiescastles.jpg")



Here we have the new church and mosque temple holdings.  

![holdings_temples.jpg](https://forumcontent.paradoxplaza.com/public/824231/holdings_temples.jpg "holdings_temples.jpg")



Lastly, the models for new walls can be seen in the screenshot below:  

![holdings_walls.jpg](https://forumcontent.paradoxplaza.com/public/824232/holdings_walls.jpg "holdings_walls.jpg")


### Monuments​

All over the landscape you’ll now find multiple different kinds of monuments. Some magnificent works that have stood since the age of Rome, others that have been erected since, and some that are yet to be initiated by your architects.  


#### Roman Walls of Lugo​

These walls in Galicia were built sometime around 263 and 276 A.D. to protect Lugo, or Lucus Augusti as it was known to the Romans.  

![monument_lugo.jpg](https://forumcontent.paradoxplaza.com/public/824228/monument_lugo.jpg "monument_lugo.jpg")



Just like with units, we try to hold off from investing too much of our polygon budget into the 3D models for holdings and monuments. Below you can see a screenshot of the low poly model for the Roman Walls of Lugo. Positioning map assets correctly in Maya is an essential step, to prevent them looking out of place once they are actually in the game.  

![monument_lugo_lowpoly.jpg](https://forumcontent.paradoxplaza.com/public/824229/monument_lugo_lowpoly.jpg "monument_lugo_lowpoly.jpg")



#### Mosque of Cordoba​

The great mosque of Cordoba is claimed to have been built on the site of a Visigothic basilica, and is one of the oldest structures still standing from the Muslim era of Al-Andalus.  

![monument_cordoba.jpg](https://forumcontent.paradoxplaza.com/public/824225/monument_cordoba.jpg "monument_cordoba.jpg")


#### The Alhambra​

One of the distinct monuments of Iberia from the base game that has now gotten some visuals. A fortress palace whose construction began in 1238 historically. Will you begin the construction early to show off your splendor?  

![monument_alhambra.jpg](https://forumcontent.paradoxplaza.com/public/824237/monument_alhambra.jpg "monument_alhambra.jpg")



#### Santiago de Compostela​

The Cathedral (construction historically began in 1075) was built in the Romanesque style. While the modern day cathedral has seen its facade rebuilt and modernized over the centuries, we’ve recreated this original look of the cathedral for this era.  

![monument_santiago.jpg](https://forumcontent.paradoxplaza.com/public/824224/monument_santiago.jpg "monument_santiago.jpg")


### Artifacts​

If you have the Royal Court expansion, you will also be finding some of these new artifacts having unique visuals when presented in your court. But worry not, artifacts are also available as trinkets if you don't have the Royal Court to display them in.  

#### Aquamanile​

Don't let the animal shape of this bronze craft fool you! It’s actually an ewer for dispensing water which was generally used for washing your hands.  

![artifact_aquamanile_2.jpg](https://forumcontent.paradoxplaza.com/public/824251/artifact_aquamanile_2.jpg "artifact_aquamanile_2.jpg")



#### Armillary Sphere​

To determine the path, journey and position of celestial objects, scholars would have these spheres created to better understand the skies and stars above them.  

![artifact_armillarysphere.jpg](https://forumcontent.paradoxplaza.com/public/824223/artifact_armillarysphere.jpg "artifact_armillarysphere.jpg")



After reference gathering (sometimes accompanied by concept art, sometimes not), a low poly blockout is created for artifacts. Below you can see the blockout model for the Armillary Sphere, with a basemesh of a CK3 character next to it, for scale.  

After reference gathering (sometimes accompanied by concept art, sometimes not), a low poly blockout is created for artifacts. Below you can see the blockout model for the Armillary Sphere, with a base mesh of a CK3 character next to it, for scale. It’s important to make sure that the silhouette and the shapes appear distinct and are readable from a distance, since Artifacts are seen from a certain distance by the player in the courtroom.  

![artifact_armillarysphere_blockout.jpg](https://forumcontent.paradoxplaza.com/public/824246/artifact_armillarysphere_blockout.jpg "artifact_armillarysphere_blockout.jpg")



High poly details are added in Zbrush, after which a game-ready low poly model is created in Maya or Blender:  

![artifact_armillarysphere_lp.jpg](https://forumcontent.paradoxplaza.com/public/824247/artifact_armillarysphere_lp.jpg "artifact_armillarysphere_lp.jpg")



#### Votive Crown​

A votive crown is one not meant for wearing, instead it is a religious offering, made for display and to be suspended at altars or shrines. Just like a regular crown they consist of fine craftsmanship, precious metals and stones. Most of the surviving examples of these today come from 7th century Visigothic Iberia.  

![artifact_votivecrown.jpg](https://forumcontent.paradoxplaza.com/public/824222/artifact_votivecrown.jpg "artifact_votivecrown.jpg")


#### Tizona​

One of the two swords of the famous El Cid, the other being the sword known as Colada. Its design is based on the museum displayed sword claimed to be the famous blade.  

![artifact_tizona.jpg](https://forumcontent.paradoxplaza.com/public/824221/artifact_tizona.jpg "artifact_tizona.jpg")



#### Chessboard​

In Iberia, games of skill and tactics were highly praised, and multiple types of chess can be acquired to show your strategically inclined mind.  

![artifact_chessboard.jpg](https://forumcontent.paradoxplaza.com/public/824220/artifact_chessboard.jpg "artifact_chessboard.jpg")



#### Bell of Santiago​

This grand bell (which you might remember being featured in a previous Dev Diary), if recaptured and recast, can be put in your court to display that feat.  

![artifact_bellofsantiago.jpg](https://forumcontent.paradoxplaza.com/public/824248/artifact_bellofsantiago.jpg "artifact_bellofsantiago.jpg")


### Closing Comments and Upcoming Livestream​

We hope that this sneak peek has got you excited for Fate of Iberia and we can’t wait for you to get your hands on the full experience on May 31st!  

For those of you who are interested in seeing more of the behind the scenes process of creating 2D and 3D assets for CK3, we have some good news. On **May 18th, 14:30 - 16:00** we will host an **art livestream** with several artists from the team. We will walk you through the pipeline without holding back on the technical details, so if that’s something for you, be sure not to miss it! The livestream will air on the ParadoxInteractive Twitch channel, at [**twitch.tv/paradoxinteractive**](http://twitch.tv/paradoxinteractive).  

As always, we look forward to your thoughts and we will stick around in the thread for a few hours to answer any questions.  

![Honest Work.png](https://forumcontent.paradoxplaza.com/public/824249/Honest Work.png "Honest Work.png")


​

<!-- artifact:reactions:start -->
- 127 Like
- 83 Love
- 16 (unlabeled — rendered as base64 data URI)
- 5 Haha
- 4 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [egghorse](https://forum.paradoxplaza.com/forum/members/egghorse.1672622/)**
Role: Producer
Badges: 3
Messages: 13
Reaction score: 486

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
