---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1582655/"
forum_thread_id: 1582655
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 127
title: "Dev Diary #127 – Joust Art & Achievements"
dd_date: 2023-05-09
author_handle: Portable Grump
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 5354
inline_image_count: 56
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1582655'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2347.jpg?1683635283
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_624_to_629
    action: preserved_and_flagged
    counts:
      Love: 132
      Like: 71
      (unlabeled — rendered as base64 data URI): 1
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_637_to_749
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_750_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2347.jpg?1683635283)
<!-- artifact:thread_banner:end -->

# Dev Diary #127 – Joust Art & Achievements

<!-- artifact:thread_metadata:start -->
- Thread starter [Portable Grump](https://forum.paradoxplaza.com/forum/members/portable-grump.1503097/)
- Start date [May 9, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-127-joust-art-achievements.1582655/)
<!-- artifact:thread_metadata:end -->

Welcome to this Dev Diary, just ahead of the release of Tours and Tournaments! Today, we will take a dive into the senses: the music and the visual art you’ll spot throughout your travels and activities. And, at the end, we’ll reveal the achievements yearning for the completionist to try them out.  

---


### Animations​

Hello, everyone. Our team has been able to add a great deal of animations to Crusader Kings 3, and we are pleased to finally be able to present some of them in this Dev Diary.  

In-game events are obviously crucial to the CK3 experience, so we are excited to announce that we’re adding a bit more life to them with “Expressive Animations”.  

After all, the definition of an animator is:  

/ˈænɪmeɪtə/ · noun. someone who imparts energy and vitality and spirit to other people.  

And with “Expressive Animations”, we hope that we have accomplished this. Many events will now have several seconds of characters emoting, before then moving onto their current static looping animation. This better communicates just how the characters feel about the event in question, and breathes more life into the game.  

In the first image, we can see the old-style event animation: a static animated loop.  

![anger_loop.gif](https://forumcontent.paradoxplaza.com/public/966482/anger_loop.gif "anger_loop.gif")



In the second image, the character plays an expressive animation, then goes into the static loop.  

![anger_expression_animation.gif](https://forumcontent.paradoxplaza.com/public/966483/anger_expression_animation.gif "anger_expression_animation.gif")



In addition to expressive animations, and in support of Tours and Tournaments, we have been able to add animated attachments to the game. Doesn’t sound exciting, does it? Well, what if I were to tell you those animated attachments include a knight's best friend? That's right — your faithful steed has arrived. Horses are a new animated attachment, and will be cantering and galloping in travel and tournament events.  

![horse1080.png](https://forumcontent.paradoxplaza.com/public/966484/horse1080.png "horse1080.png")



And last, but not least, another animated attachment: our feathered friend, the falcon. Falcons can be seen aiding you in certain Hunting Events, and come along with certain interaction animations, such as a very necessary petting animation.  

![falcon.png](https://forumcontent.paradoxplaza.com/public/966485/falcon.png "falcon.png")





---


### Audio​

What would a Tournament sound like? What music would be ideal for having a Grand Wedding? How should my falcon sound when I send it to hunt? Those were a few questions we asked ourselves to develop the soundscape for this new DLC. We wanted to create an ambience filled with heroism, wanderlust, romance, and mystery that could enhance your playthrough in all the new and revamped activities.  

We created an orchestral score to intensify your activities while reflecting your character's culture. By hosting or joining activities in different regions, you will get beautiful renditions of the soundtrack to accompany your Tournaments, Tours, Weddings, and even when you go berserk in a Murder Feast. We had the fantastic opportunity to work again with the City of Prague Philharmonic Orchestra. We created the perfect playlist for all the amazing activities you’ll find in this DLC.  

![image24.jpg](https://forumcontent.paradoxplaza.com/public/966486/image24.jpg "image24.jpg")



During these activities, you’ll probably wield a sword, shoot an arrow, travel to a holy site, and explore different cities. We made sure to cover every need to enhance your immersion during your adventures and to give you the best experience to create the perfect soundtrack for your stories.  

---


### Fashion and Armor​

What’s up everybody, I’m Nils, Principal Character Artist on Crusader Kings III. I will write a bit about the exciting new character clothing and hair assets that we are adding to the game with Tours and Tournaments!  

This expansion provided us with an opportunity to add some long-awaited new clothing to the game. The tournaments in particular are an excellent excuse to add a bunch of shiny new armors. And who doesn’t like those? So we once again dug down into our resources to make designs for new European, Middle-Eastern, Byzantine, Steppe and Indian armors and helmets. You can see the results below.  

![image50.jpg](https://forumcontent.paradoxplaza.com/public/966487/image50.jpg "image50.jpg")


*New armors and helmets added for Western, Byzantine, Steppe, Middle-Eastern and Indian cultures. Shoutout to the new Barbershop for making it about 1000x easier to do these kinds of lineup screenshots!*  

These armors will be used alongside the already existing ones, both when appropriate in Tournaments but also in wars and battles.  

Another very cool (if I may say so myself!) addition is what we call Tiers of Armor. These will make sure higher rank characters wear appropriately more fancy armor than their lower tier counterparts. We have added a lot of such variations both for the already existing armors in the game as well as the new ones included with the expansion. That means no more going to war in some rusty old scrap - if you’re a king you deserve the best!  

![image10.jpg](https://forumcontent.paradoxplaza.com/public/966493/image10.jpg "image10.jpg")


*Some examples of the new tiers of armor system, comparing low nobility and high nobility versions of armors and helmets.*  

Oh, and if you haven’t already noticed in the screenshots, we now add Coat of Arms colors and symbols to surcoats dynamically, so that you can finally show off that epic custom-made Coat of Arms on your chest as you crush your enemies!  

![image20.jpg](https://forumcontent.paradoxplaza.com/public/966494/image20.jpg "image20.jpg")


*Some examples of dynamic Coats-of-Arms on Surcoats in action!*  


### From Carolingians to Plantagenets​


If you look closely at the screenshots of new armors above, you may notice that some of them appear to belong in different eras. This is not by mistake or oversight, but rather part of a new feature we call Fashion through the Ages.  

The idea is to add some visual change to the clothes characters wear as the game progresses. It is something we have wanted to do for a long time. We are, after all, dealing with a generational game covering as much as 600 years of history. So it has always felt a bit off that there is no change in fashion between the 9th and 15th centuries. Now, with Tours and Tournaments, was finally our chance to start turning this idea into reality.  

We have initially focused on European cultures since these are probably the most familiar to a majority of players, and potentially the ones that changed most dramatically during our time period. The ambition is of course to keep adding to this in the future, and to include other cultures as well.  

The first priority was to make sure the two start dates we represent in the game have characters wearing visibly different clothing. Since most of the clothes we have since before historically belong somewhere in the 11th to 12th centuries it was the early start date that needed the most attention.  

To address this we have added a full new set of clothes for the Western cultures in the early start date. These designs were based primarily on Carolingian illuminated manuscripts from the 9th century, such as the so-called *Vivian Bible* of Charles the Bald, the *Stuttgart Psalter* and the *Psalterium Aureum*.  

![image22.jpg](https://forumcontent.paradoxplaza.com/public/966496/image22.jpg "image22.jpg")


*A selection from the manuscript sources. (People back then sure had some creepy fingers!)  

![image46.jpg](https://forumcontent.paradoxplaza.com/public/966497/image46.jpg "image46.jpg")


And here the in-game results. Carolingian rulers and courtiers in 867, wearing some of the new clothing!*  

Of course, we needed to set it up in the game so that these clothes will get replaced as time progresses and the ideas of what is fashionable change. This is done by looking at the year a character was born as well as their age. So, after we pass a certain in-game year, any character who is between the ages of 16 and 25 will be among the first adopters of the new fashions. Meanwhile, older characters will stick to the styles of their youth. Kind of like the real world, don’t you think? (Like, for example, yours truly still rocking skinny jeans like it’s 2009…).  

![image28.jpg](https://forumcontent.paradoxplaza.com/public/966498/image28.jpg "image28.jpg")


*European characters in the clothing style of the 11th to 12th centuries. With Tours and Tournaments, these clothes will appear gradually some time after the year 1000.*  

When you reach the late 12th and early 13th centuries, clothes will once again start to change to the High Medieval styles that we have also added in Tours and Tournaments. During this time historically, surcoats were used extensively both in military and civilian fashion. They were often adorned with fancy brooches and expensive belts, and - for the first time in European history - buttons!  

![EP2_characters_screenshots_era3_sources.jpg](https://forumcontent.paradoxplaza.com/public/966499/EP2_characters_screenshots_era3_sources.jpg "EP2_characters_screenshots_era3_sources.jpg")


*Some of the source material for the new high medieval assets.*  

![image17.jpg](https://forumcontent.paradoxplaza.com/public/966500/image17.jpg "image17.jpg")


*A court of the 13th century, showing the new high medieval clothes added with Tours and Tournaments, as they will show up together with a few existing assets once you reach the late 12th century and early 13th centuries.*  

### New Personal Gear​

While out on your travels to tournaments, hunts, or defending yourself on the road you may come across a series of new weapons and gear, as well as new trophies to obtain, wield and/or show off in court.  


#### Bows and Crossbows​

Ranged weapons are now entering the repertoire, whether it's for hunting or for marksmanship on the battlefield, these weapons puts a much healthier distance between your ruler and the quarry.  

![image36.jpg](https://forumcontent.paradoxplaza.com/public/966501/image36.jpg "image36.jpg")


**Hunting/Shortbows:** Shortbows were smaller bows, typically around 4 to 5 feet (1.2 to 1.5 meters) in length, and were used primarily for hunting and in close-quarter combat.  

![image44.jpg](https://forumcontent.paradoxplaza.com/public/966502/image44.jpg "image44.jpg")


**Longbows:** Longbows were often over 6 feet (1.8 meters) in length, and were used primarily for military purposes in the Middle Ages. Longbows were made from a single piece of wood and were highly effective in battles due to their long range and power.  

![image6.jpg](https://forumcontent.paradoxplaza.com/public/966503/image6.jpg "image6.jpg")


**African Bows:** There are many types of bows used in Africa, but these bows were typically made from wood, animal sinew, and/or horn, and were used for hunting and warfare.  

![image12.jpg](https://forumcontent.paradoxplaza.com/public/966504/image12.jpg "image12.jpg")


**Bamboo Bows:** Bamboo bows are a type of bow made from bamboo, which is a strong and flexible material. These bows were commonly used in Asia for hunting and warfare.  

![image27.jpg](https://forumcontent.paradoxplaza.com/public/966505/image27.jpg "image27.jpg")


**Steppe Composite Bows:** Composite bows are made from a combination of materials, typically wood, horn, and animal sinew. These bows were highly effective in battles due to their long range, power, and accuracy.  

![image48.jpg](https://forumcontent.paradoxplaza.com/public/966506/image48.jpg "image48.jpg")


**Crossbows:** Crossbows were designed to be fired from a horizontal position and were typically easier to learn to use compared to other types of bows. Crossbows were highly effective at penetrating armor and did not rely on the wielder's stamina and strength to remain strung in a firing position.  


#### Lance and Shield​

![image23.jpg](https://forumcontent.paradoxplaza.com/public/966507/image23.jpg "image23.jpg")


![image11.jpg](https://forumcontent.paradoxplaza.com/public/966508/image11.jpg "image11.jpg")



The lance was a long, spear-like weapon used in medieval warfare and jousting. The war lance was typically made of wood with a metal tip, and was used by knights on horseback to charge and attack their opponents. The jousting lance was longer and heavier, and was used in jousting tournaments to knock opponents off their horses. In both cases, lances were designed for use by cavalry and required significant skill and training to use effectively. Jousting thus was a show of the knight's prowess under (somewhat) safer circumstances than actual medieval warfare. We’ve made sure that heraldic coloring is applied on both the shields and the lances.  


#### Hunting Blades and Boar Spear​

![image9.png](https://forumcontent.paradoxplaza.com/public/966509/image9.png "image9.png")


Medieval hunting blades were specialized knives or short swords used primarily for hunting game, although they could also be used for self-defense or as a utility tool. They varied in size and shape, but generally had a broad, sturdy blade with a sharp point and a handle that allowed for a secure grip. Hunting blades were typically made from high-quality steel and were often finely crafted with ornate designs. They were used to skin and butcher game, and were often used in conjunction with other hunting tools such as spears, bows, and traps.  


### Prizes​

Whether you’re out on the hunt for animals, or to win the local tournaments, we have a whole new range of prizes that you can win and decorate your throne rooms with. A preview of some of the possible winnings:  


![image15.jpg](https://forumcontent.paradoxplaza.com/public/966510/image15.jpg "image15.jpg")


#### New Hunting Trophies and Furs​

To show off your accomplishments during the hunting activities you will now be able to collect additional pelt types.  


![image5.jpg](https://forumcontent.paradoxplaza.com/public/966511/image5.jpg "image5.jpg")


New pelts for white Tigers, Stags, Wolves and more.  

![image4.png](https://forumcontent.paradoxplaza.com/public/966512/image4.png "image4.png")


New trophy skulls for hunting Gazelles, Hyenas and Fallow Deer.  

---

### Illustrations​


Hello! My name is Pavel and I am an illustrator in the Crusader Kings 3 team. Along with Alessandro I have been working on the new illustrations for the Tours and Tournaments expansion and I am going to briefly talk about the creation process.  

Illustrations in Crusader Kings constitute a visual layer on top of game mechanics that helps to turn math and numbers into stories and drama and spark the player's imagination. Tours and tournaments introduced new game mechanics and new types of illustrations were required. These illustrations are supposed to communicate what each activity means and add emotional flavor to it.  

Activity illustrations are relatively small, but for us, artists, they gave a broad variety of themes and stories to depict. Also we tried to use these illustrations as an opportunity to show the variety of our game world with many different cultures presented and shift away from euro-centric tendency in perception of the medieval era.  

### Process​

The first thing an artist does before starting to draw is research of the subject that is to be depicted. This is especially important in case of a historical project where it is too easy to be trapped by the modern era cliches and popular culture (vikings with horned helmets etc). This is where we, artists, can get priceless help from our game designers.  

![image53.jpg](https://forumcontent.paradoxplaza.com/public/966513/image53.jpg "image53.jpg")



A good reference in our case does not have to be a fancy high resolution image. Quite often these are miniature paintings from codices, sometimes in poor quality but providing a more historically reliable information.  

Technically, activity illustrations are big buttons that exist in the context of a rather complex UI with text and icons overlays. From the UX and UI design team we got mockups showing constraints we had to take into consideration.  

![image16.png](https://forumcontent.paradoxplaza.com/public/966515/image16.png "image16.png")



The above image from studio’s internal documentation shows UI context and describes major constraints that an artist should consider when contriving composition. As you can see, the tournament illustrations were the most challenging because a big portion of it could be covered by a UI element and composition should work well both with and without that element.  

The general workflow is pretty conventional for every 2D illustration. The foundation is laid out by doing black & white composition sketches where an artist suggests his vision of the theme using the minimal amount of artistic devices. At this stage it is best to focus the attention on basic shapes and use only 2-3 tones.  

![image41.png](https://forumcontent.paradoxplaza.com/public/966517/image41.png "image41.png")


The image above shows composition sketches for the board game tournament as they are presented to the art director for review, showing two clear composition solutions and how they work in the context of the UI constraints. The sketches were done by Alessandro. Though both of these composition solutions are successful for a standalone illustration, the first(leftmost) variant was chosen as it is more focused on the chess game and competitors.  

A good composition provides a firm ground for the next stage - finding a color solution. There are several things to consider besides getting a pretty color combination:  


1. Does the color scheme contribute to the specific theme of the illustration?
2. Does it come well together with the other activity illustrations that will be presented at the same time in the game interface?

The image below shows evaluation of the color scheme for intimidation tour activity. Three color variants of that illustration are compared against two other tour images (majestic and taxation).  


![image38.jpg](https://forumcontent.paradoxplaza.com/public/966520/image38.jpg "image38.jpg")


After some discussion it was decided to proceed with the third(rightmost) variant because:  


1. The tension the colors invoke works well with the intimidation theme (variant 1 is too joyful).
2. The color scheme makes it distinct from the majestic and taxation tours images (not the case with variant 2).

With the proper major decisions taken (composition and color scheme) the process of painting and finalizing the illustration is pretty straightforward for an experienced artist. One of the caveats is to keep in mind that this is a small illustration and the level of detail should stay in balance with the purpose of the image. As elements on the picture become more defined, it is good to check them with our “dress police” - team members who have a broad knowledge of the history of costume design.  

![image18.jpg](https://forumcontent.paradoxplaza.com/public/966521/image18.jpg "image18.jpg")



Not all of the ideas for activities reached the final stage and appeared in the game release. For instance, the fist fighting tournament(the image below) did not make it past the sketching phase and was cut by the design. While deep inside every artist would like his creation to see the release, such decisions are inevitable and a part of the complex process of game development. On a positive side, there are very few artworks that did not become part of the Tours & Tournaments release.  


![image1.jpg](https://forumcontent.paradoxplaza.com/public/966522/image1.jpg "image1.jpg")



## Finished illustrations​

On a final note I would like to showcase some of the finished artworks and share thoughts and emotions behind them.  


### Drama of choice​

![image29.jpg](https://forumcontent.paradoxplaza.com/public/966524/image29.jpg "image29.jpg")


Crusader Kings is heavily focused on characters and creates a fertile soil for dramatic situations and very contrasty role playing. That is something we wanted to highlight in activities and, honestly, that inspires us as artists a lot. Wedding and feast illustrations created by Pavel (me).  


### Culture diversity​

![image52.jpg](https://forumcontent.paradoxplaza.com/public/966525/image52.jpg "image52.jpg")


As I mentioned at the beginning, we wanted our activity images to convey the diversity of the medieval world encompassing many nations. Some activities were so unique that they were strictly tied to a specific area, like jousting for western europe or hajj for muslims. Certain sports were distinct for a specific culture and we used that to feature that culture in our illustrations, like it was with traditional Mongolian wrestling. A more common activity could be used to showcase countries that are not always associated with the middle ages but still part of the era and the game world. Thus we got an African flavored depiction of the majestic tour. Hajj was painted by Alessandro, the rest are by Pavel(me).  


### Women of medieval times​

![image19.jpg](https://forumcontent.paradoxplaza.com/public/966526/image19.jpg "image19.jpg")


The Middle ages were dominated by men. And we tried to follow the historical knowledge as much as we could. Yet we found quite a few opportunities to feature women while staying historically accurate. All of these illustrations were created by Alessandro.  


### Personal attitude​

When an artist works on an illustration, there is more than just following the task guidelines. There is always something that fuels his inspiration and quite often the source of it comes from his very personal experience and preferences. Here I would like to share a few thoughts and fantasies behind some of the illustrations we did for the expansion.  

![image54.jpg](https://forumcontent.paradoxplaza.com/public/966527/image54.jpg "image54.jpg")


- Duel (by Pavel): Among the initially presented sketches for that theme, this one did not have the strongest composition. But I saw a good potential to show strong emotions of conflict between two fighting warriors. I have got a great pleasure painting the red-haired strung face of the viking clashing with his opponent and I like how the character's personality came out. The northern region setting not only allowed showcasing a bit of medieval Scandinavian culture but also gave me an opportunity to use an unconventional color palette consisting of ochre and violet shades.

- The legendary hunt (by Alessandro): This is a great example of how taking a break can sometimes save your work. I was in trouble at first, I had no idea what kind of legendary animal would work without doing repetitions with other animals we've done before or doing something too obvious. In talking to Pavel, we both agreed that a northern lights setting would give the image a special feel, but my concern was about the choice of an animal that was special and imposing at the same time. I was having a coffee, thinking about what to do, when by chance talking to Nils, our 3d artist, I discovered the existence of a white moose in Sweden, which to me as an Italian was completely unknown. I fell in love with the idea, it was just perfect even for the type of environment I had in mind. I used two triangular shapes, with the ground and the negative space behind the animal, to center the figure and make it stand out in the scene, and that was it, a legendary hunt began.

- Taxation tour (by Pavel): That illustration went hard at the beginning. I have put off the classic trope of coins being collected by a public officer as there should be something special for a grand tour of a lord. So I have been looking into some sort of tribute collection in non monetary form that would better contribute to the medieval flavor of the game and give me more dramatic elements to express the theme. During one of the discussions within our team the painting “[Valdemar Atterdag fire taxes Visby](https://sv.wikipedia.org/wiki/Valdemar_Atterdag_brandskattar_Visby)” by Carl Gustaf Hellqvist was mentioned. This picture can be seen live in the National Museum in Stockholm, the city where the main Paradox office is. In the end that artwork became a major source of inspiration for that illustration.

- Solo pilgrimage (by Alessandro): When I thought of the image "pious pilgrimage" my first idea was about a madonna, who looks out of the picture and through the light she hears the call of God. This iconographic choice was very classic, perhaps too much, so I decided to overturn the concept, where the light comes from behind her and we see a much more collected and intimate emotion of the call. In my fantasy the woman kneels on the floor because at that moment it is not interesting to where or how. By opting for this choice I took advantage of the woman's clothes, and I tried to direct the folds of her clothes towards her face (which is very evident in the curve that the skirt makes on the floor). It has been a fun and interesting challenge.


That concludes my brief highlight of our work behind the activity illustrations. If you paused for a second or two looking at the illustration before delving into a tour or tournament, then I think we, artists, succeeded in our work.  

### --- ​

### Achievements​

To round things off, why don’t we have a look at the new achievements coming together with the Expansion? After all, they’re pieces of inspiring art too! Let's start with the easiest ones and work our way to the top:  

#### Easy​

![image30.jpg](https://forumcontent.paradoxplaza.com/public/966528/image30.jpg "image30.jpg")


**Hunting Accident -** Succeed with the Murder intent while on a Hunt  
A reference to another Paradox game which most of us know and love.  

#### Medium​

![image3.jpg](https://forumcontent.paradoxplaza.com/public/966529/image3.jpg "image3.jpg")


**The Grandest Tour** - *Visit ten Kingdom-tier Vassals on a Tour*  
Arguably a little bit harder than Medium; but the challenge lies in building up a large empire, not necessarily in the Tour itself - meaning that this is an excellent achievement to collect at the same time as, for example, trying to restore Rome!  

![image49.jpg](https://forumcontent.paradoxplaza.com/public/966531/image49.jpg "image49.jpg")


**Imperial March** - *As an Emperor, go on an Intimidation Tour visiting all of your Powerful Vassals*  
It is better to be feared than to be loved, if one cannot be both. There might also be a reference to a popular franchise in here, somewhere.  

![image25.jpg](https://forumcontent.paradoxplaza.com/public/966534/image25.jpg "image25.jpg")


**Black Dinner** - *Successfully host a Murder Feast or a Bloody Wedding*  
A reference to the historical Black Dinner, hosted in 1440 by James II of Scotland.  

![image51.jpg](https://forumcontent.paradoxplaza.com/public/966536/image51.jpg "image51.jpg")


**The Very Best** - *Finish any track in the Hastiluder Trait*  
Your journey begins here with either Horse, Foot, Archery, or Wit - which will be your ‘starter’?  

![image39.jpg](https://forumcontent.paradoxplaza.com/public/966537/image39.jpg "image39.jpg")


**A Thousand & One Nights** - *Orchestrate a Grand Wedding where the Spouses become Soulmates*  
A tale as old as time. Bound to happen sooner or later; more likely if you are one of the spouses.  

![image35.jpg](https://forumcontent.paradoxplaza.com/public/966538/image35.jpg "image35.jpg")


**Lions & Tigers & Bears, Oh My!** - *Capture a large wild animal while on a hunt*  
Bound to happen if you hunt frequently. Might be easier if you find & follow a yellow-brick road.  


![image34.jpg](https://forumcontent.paradoxplaza.com/public/966539/image34.jpg "image34.jpg")


**Fly, My Pretty!** - *Finish the Falconer Track in the Hunter Trait*  
We obviously have people that enjoy the Wizard of Oz on the team… unfortunately you can only hunt with falcons and kestrels, not flying monkeys.  

![image33.jpg](https://forumcontent.paradoxplaza.com/public/966540/image33.jpg "image33.jpg")


**Pathway to Heaven** - *With any one Character, go to Pilgrimages to all of your Holy Sites*  
Pilgrimages take a long time; might be easiest to achieve when adhering to a faith with the ‘Mandatory’ Pilgrimage Doctrine, as that’ll speed up the journey significantly.  

![image32.jpg](https://forumcontent.paradoxplaza.com/public/966541/image32.jpg "image32.jpg")


**Sir Lance-a-Lot** - *Participate in a Joust with a maxed-out Horse Hastiluder track*  
An absolutely unavoidable reference when making an expansion such as this one…  

#### Hard​


![image47.jpg](https://forumcontent.paradoxplaza.com/public/966542/image47.jpg "image47.jpg")


**Your Eternal Reward** - *As a Regent, successfully Coup your Liege and take their Realm without War or Schemes*  
Finally, a way to become King without bloodshed! Unless the Coup you choose involves a lot of knives, of course…  

![image37.jpg](https://forumcontent.paradoxplaza.com/public/966543/image37.jpg "image37.jpg")


**There and Back Again** - *Finish both Track of the Traveler Trait*  
The hardest part of this is to level up the ‘Seasoned’ track, which you can only really do by going head-first into dangerous terrain. Good luck, hopefully there are no black dragons at the end of your path!  

![image14.jpg](https://forumcontent.paradoxplaza.com/public/966552/image14.jpg "image14.jpg")


**A Knight’s Tale** - *Have one of your Lowborn Knights win a Joust, then land them*  
A reference to a surprisingly-accurate movie (disregarding certain music and costume design). Easiest to do if you’re the host and have plenty of lowborn knights in your roster.  

![image45.jpg](https://forumcontent.paradoxplaza.com/public/966545/image45.jpg "image45.jpg")


**In My Element(s)** - *Pass through every Terrain, including sea and ocean, whilst on the same Travel*  
The QA department keeps telling me this one should be in the ‘Very Hard’ category, maybe, maybe - it’s doable though! You just have to take a detour into Africa whilst going home from Jerusalem…  

![image26.jpg](https://forumcontent.paradoxplaza.com/public/966546/image26.jpg "image26.jpg")


**A True and Perfect Knight** - *Have a max rank Acclaimed Knight with the Warrior of the Faith (Crusader) Trait*  
Maintaining several Accolades and going into a lot of Wars/Tournaments should do the trick. The grandness of their story might reach all the way to Canterbury.  

![image13.jpg](https://forumcontent.paradoxplaza.com/public/966547/image13.jpg "image13.jpg")


**A.E.I.O.U & Me** - *Starting as the Habsburgs, ruler the Archduchy of Austria, arrange 5+ Grand Weddings, and don’t wage War*  
The Archduchy of Austria used to be one of the hardest titles to create in the game, as it requires you to have a Strong Hook on the Holy Roman Emperor. With Grand Weddings (in combination with a Legacy perk in the new Activities Legacy) this is now more achievable. Add on the extra challenge of never waging war, and you’re set for one exciting serving of diplomacy-and-intrigue with extra Habsburg spice. I’m also ridiculously satisfied with the name, as it made our pun-resistant [@Wokeg](https://forum.paradoxplaza.com/forum/members/1325927/) flinch with a force never before seen in the office.  

![image2.jpg](https://forumcontent.paradoxplaza.com/public/966553/image2.jpg "image2.jpg")


**The Iron and Golden King** - *Have a capital Barony with 60+ Income, a 500+ size stationed Heavy Cavalry unit, and a Special mine*  
This reference to Ottokar II of Bohemia seemed fitting together with a challenge that requires you to engage with many of the new free systems such as MaA Stationing, the Building Slots Revamp, and the addition of new Special Mines. In fact, Bohemia is an excellent place to do this Achievement, as they have the Kutná Hora Mines there.  


#### Very Hard​

![image40.jpg](https://forumcontent.paradoxplaza.com/public/966548/image40.jpg "image40.jpg")


**Like No One Ever Was** - *Finish all Tracks in the Hastiluder Trait*  
Gotta complete em’ all. Requires a well-rounded character and a life practically dedicated to Tournament-going!  

![image42.jpg](https://forumcontent.paradoxplaza.com/public/966549/image42.jpg "image42.jpg")


**Ahab** - *Succeed a Legendary Hunt*  
With persistence you might find your Holy Grail. Make sure to have a Master of the Hunt hired, preferably a really good one.  

![image21.jpg](https://forumcontent.paradoxplaza.com/public/966550/image21.jpg "image21.jpg")


Little William Marshal - Win every Contest in a Tournament with at least three contests  
Easier said than done - but with persistence you too might become a legend similar to William Marshal himself!  

That’s it for this time. On the 11th we’ll be posting the full update notes for 1.9, see you then!

 

#### Attachments

- [![image14.jpg](https://forumcontent.paradoxplaza.com/thumbnail/public/966544/image14.jpg)](https://forum.paradoxplaza.com/forum/attachments/image14-jpg.978976/)
  
  image14.jpg
  64,9 KB

 · Views: 0

<!-- artifact:reactions:start -->
- 132 Love
- 71 Like
- 9 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
- 1 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Portable Grump](https://forum.paradoxplaza.com/forum/members/portable-grump.1503097/)**
Role: ♛ CK3 Community Team ♛
Badges: 18
Messages: 276
Reaction score: 1,620

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
