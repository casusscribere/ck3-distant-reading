---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1406933/"
forum_thread_id: 1406933
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 34
title: "CK3 Dev Diary #34 - It’s all about appearances"
dd_date: 2020-07-21
author_handle: NilsW
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1772
inline_image_count: 15
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1406933'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1423.jpg?1595334543
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_269_to_274
    action: preserved_and_flagged
    counts:
      Love: 259
      Like: 131
      (unlabeled — rendered as base64 data URI): 1
      Haha: 4
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_282_to_339
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_340_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1423.jpg?1595334543)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #34 - It’s all about appearances

<!-- artifact:thread_metadata:start -->
- Thread starter [NilsW](https://forum.paradoxplaza.com/forum/members/nilsw.1192255/)
- Start date [Jul 21, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-34-its-all-about-appearances.1406933/)
<!-- artifact:thread_metadata:end -->

Hello, I’m Nils and I’m the lead character artist on Crusader Kings III. We’ve already touched briefly on a lot of the features of the portrait system but in this Dev Diary I’m going to dive deeper into the intricacies of the system. It might get a bit technical at points - so bear with me. I personally think all this stuff is very cool but I'm also a gigantic nerd when it comes to these things.  

![front_end.jpg](https://forumcontent.paradoxplaza.com/public/589041/front_end.jpg "front_end.jpg")


*There’s going to be a lot of text in this Dev Diary, but really, when it comes down to it, it’s mostly there as an excuse to show off the art!*​


Characters are generated dynamically in the game using a DNA system that defines their looks - everything from mouth shape to body height is stored in this DNA. A DNA is made up of a number of genes. Each gene defines a certain feature. Crusader Kings II already does something similar, but in CKIII we have more than 10 times the amount of genes for every character and a lot of added complexity. The system itself is very flexible and it was up to me how to set it up to get as much visual variation out of it as possible.  

Our predecessor, CK2, by necessity builds up characters from a limited number of facial features. There are x amount of noses combined with x amount of mouths and x amount of eyes and so on to make up a face. While this works well and gives a good amount of variation it still has some inherent limitations. What we’ve done in CKIII is to have a much more granular approach where we use many parameters to control each feature. So, for example, instead of just picking a nose (you shouldn’t pick your nose kids) out of a selection of pre-defined noses we store values for nose protrusion, nose height, nose length, nose nostril height, nose nostril width, nose ridge profile, nose ridge angle, nose ridge width, nose size, nose tip angle, nose tip protrusion, nose tip width, nose ridge definition and nose tip definition. In other words; if you’re into noses, or any other facial feature, this is the game for you.  

![faces.jpg](https://forumcontent.paradoxplaza.com/public/589044/faces.jpg "faces.jpg")


*Some of the many faces (and noses!) of Crusader Kings III*  
​

As you can imagine, this gives us quite detailed control over the facial features of characters. And they can vary greatly depending on many factors, which I will try to cover here. Let’s start with ethnicity.  

Like we’ve shown in other Dev Diaries already, the CKIII map covers a vast area of the world from Ireland in the west to modern day Mongolia in the east and from Arctic Norway in the north to Sub-Saharan Africa in the south. This big area is populated by groups of different ethnicities which we represent in the game. Due to the way that the character generating system is set up, we can use the same base assets for all different ethnicities and just script in different average values for the facial feature parameters. As an example, west african characters have, on average, darker skin, fuller lips and differently shaped noses than their european or asian counterparts, but they still use the exact same base model. This is good news for inheritance, which is the next subject I will discuss.  

![ethnicities.jpg](https://forumcontent.paradoxplaza.com/public/589045/ethnicities.jpg "ethnicities.jpg")


*A selection of characters of different ethnicities*  
​

Due to the fact that all characters use the same base model, we can easily create blends between multiple DNAs. Each character stores two sets of genes that we call dominant and recessive, respectively. (Disclaimer: Please note that the dominant and recessive genes in our system do not work exactly like in real life. We’re still dealing with an approximation of genetics. We haven’t fully replicated real world genetics. Yet.) When a baby is born it will inherit two versions of each gene - both of which will come randomly from either parent. As mentioned one of these genes will end up being dominant and the other one recessive based on a chance value (dominant genes from the parents have a higher chance of being inherited as dominant genes for the baby). The appearance of the newborn character is decided entirely by its dominant gene set. But the recessive genes are still there as a representation of genes carried down the generations. So when this new character gets to make its own babies they will have a chance of inheriting a gene from their grandparents, even though that gene might not have been visible on their parent.  

![inheritance.jpg](https://forumcontent.paradoxplaza.com/public/589049/inheritance.jpg "inheritance.jpg")


*Inheritance in action. Top row parents and bottom row their children. If you look closely you should be able to spot the inherited features.*  
​

I hope you guys are still awake for the continuation of this Dev Diary. What does all this genetics mumbo-jumbo mean for you as a player? It means that inheritance has a much bigger impact on the appearance of a character in CKIII than than it does in CK2. Characters of different ethnicities that get down for the hanky panky will make babies that look like a blend between both parents, with some genes from further back in the family tree thrown into the mix. Of course, there’s still a fair amount of randomness in the system so we won’t get identical siblings unless they are, you know, identical twins.  

Now, while we’re on the subject, let’s talk briefly about children and aging. This is the other huge factor in defining the appearance of a character: his or her age. The 3D system that we use gives us the possibility to have seamless aging and there’s a ton of things that are set up to take advantage of this. A newborn child will obviously be very tiny compared to when it’s all grown up. It’s adult facial features will be there already from birth but they are very toned down during early childhood to get gradually more pronounced as the character ages. When a character approaches their 30’s and 40’s their skin will get more rugged, age lines and wrinkles will start appearing in the face, and their hair turns grey. Once they enter old age their body will start sagging, posture will deteriorate, their ears and nose will get bigger and the jaw protrudes as they lose their teeth.  

![aging_somatu.jpg](https://forumcontent.paradoxplaza.com/public/589050/aging_somatu.jpg "aging_somatu.jpg")


*Chieftain Somatu of Kevrola, from age 0 to 99*​


In addition to genetics and age, lifestyle choices and changes also impact a character’s appearance. Body types vary greatly from alarmingly thin victims of starvation to truly impressive bulks of some high nobility gluttons. Different levels of muscularity and fitness are also represented and tied to the “prowess” value in the game.  

![body_types.jpg](https://forumcontent.paradoxplaza.com/public/589051/body_types.jpg "body_types.jpg")


*Examples of different body types*​



*![gaining_weight.gif](https://forumcontent.paradoxplaza.com/public/589052/gaining_weight.gif "gaining_weight.gif")


Like, every Christmas Holiday, ever*  

![working_out_02.gif](https://forumcontent.paradoxplaza.com/public/589053/working_out_02.gif "working_out_02.gif")


*I got ripped in five seconds!*  

There are a number of traits and conditions, genetic or otherwise, that have visual impact on the character portrait. Some examples of non-genetic ones are pregnancy, wounds, scars, lost arms, blindness and disfigurement. And some notable examples of genetic conditions are dwarfism, gigantism, albinism and hunchback.  

![traits.jpg](https://forumcontent.paradoxplaza.com/public/589054/traits.jpg "traits.jpg")


*Genetic traits*  

​

![Dragoman.png](https://forumcontent.paradoxplaza.com/public/589055/Dragoman.png "Dragoman.png")


*Dragoman  

![Dam.png](https://forumcontent.paradoxplaza.com/public/589056/Dam.png "Dam.png")


You know how some people have names that just feel “right” for them?*  


![wounded_anim.gif](https://forumcontent.paradoxplaza.com/public/589057/wounded_anim.gif "wounded_anim.gif")


*“You should see the other guy”*  

We have already discussed clothes in previous Dev Diaries so I won’t go into great detail about them. But I would like to show something I don’t think we’ve shown before. That is the barbershop feature which allows you to change clothes, head wear and hairstyle for your character:  

![barbershop.JPG](https://forumcontent.paradoxplaza.com/public/589058/barbershop.JPG "barbershop.JPG")


*Barbershop*  
​

Even though the vast majority of characters have randomly generated appearances, there are some notable exceptions. The detailed setup of the DNA system allows us to design quite specific appearances where we want to. There are some historical starting characters in the game whose looks were based on how they are described in historical sources. For example William the Conqueror and Harold Godwineson of England. Of course, medieval sources are not always... perfectly reliable and the portraiture from the time not the most accurate (to put it mildly!) so we did have to do some guesswork and use a lot of artistic license. There are also a whole bunch of developer characters with appearances that match their real life counterparts. They’re lurking around various courts in the game. If you want to find some, a pro tip is to browse through the characters in modern day Sweden…  

It is perfectly possible to mod DNAs as well as adding new ones, so if you feel like adding your own likeness or a medieval Abraham Lincoln to the game it is fairly easy to do so.  

![fate_of_England.jpg](https://forumcontent.paradoxplaza.com/public/589059/fate_of_England.jpg "fate_of_England.jpg")


*Historical characters from the “Fate of England” in the 1066 start date. Guess who is who!*  
​

And finally, to end this on a more gruesome note, the last thing I’d like to show you is some diseases. As you all know, the middle ages were a time of ravaging epidemics and quick unexpected death from disease. And the game reflects that in quite a graphical way.  

And if you don’t enjoy being disgusted - don’t worry - we have an option to turn off the worst looking diseases and replace them with something less nightmare-inducing.  

**WARNING: The following spoiler tags contain images that some viewers might find disturbing. Viewer discretion is advised.**

Spoiler: Diseases (Viewer Discretion is Advised)

![illnesses.jpg](https://forumcontent.paradoxplaza.com/public/589060/illnesses.jpg "illnesses.jpg")


*Don’t say I didn’t warn you*​

<!-- artifact:reactions:start -->
- 259 Love
- 131 Like
- 12 (unlabeled — rendered as base64 data URI)
- 7 (unlabeled — rendered as base64 data URI)
- 4 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [NilsW](https://forum.paradoxplaza.com/forum/members/nilsw.1192255/)**
Role: Principal Character Artist @ PDS
Badges: 3
Messages: 18
Reaction score: 1,065
<!-- artifact:op_signature:end -->
