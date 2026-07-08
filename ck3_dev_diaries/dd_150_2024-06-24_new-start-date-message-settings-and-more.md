---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1691073/"
forum_thread_id: 1691073
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 150
title: "Dev Diary #150 - New Start Date, Message Settings, and More"
dd_date: 2024-06-24
author_handle: Cordelion
expansion: Roads to Power
patch: Patch 1.13
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3900
inline_image_count: 16
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1691073'
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
  - type: thread_banner
    location: raw_line_145
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3144.jpg?1719310946
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_367_to_372
    action: preserved_and_flagged
    counts:
      Like: 177
      Love: 97
      (unlabeled — rendered as base64 data URI): 3
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_380_to_490
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_491_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3144.jpg?1719310946)
<!-- artifact:thread_banner:end -->

# Dev Diary #150 - New Start Date, Message Settings, and More

<!-- artifact:thread_metadata:start -->
- Thread starter [Cordelion](https://forum.paradoxplaza.com/forum/members/cordelion.1759707/)
- Start date [Jun 24, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-150-new-start-date-message-settings-and-more.1691073/)
<!-- artifact:thread_metadata:end -->

Good day, everyone!  

I'm [@Cordelion](https://forum.paradoxplaza.com/forum/members/1759707/): we’ve not had the pleasure of meeting before, and that’s because since I joined Paradox last year I’ve been working almost exclusively on the new start date and its two bookmarks that will be releasing as part of the free update alongside Roads to Power. I’ve been closely following what you have to say about it and I cannot overstate just how happy I am to see people excited by it, and so today it will be my pleasure and honor to give you a closer look at all it has to offer.  

---

### The Who, What, When, Where, and Why​

Let’s start with the obvious question that I know some of you have been asking: why choose *1178* specifically? That’s a great and very natural question; unlike our preexisting start dates of 1066 or 867, 1178 isn’t well known for any major, paradigm-altering historical events, but there are a few key factors that weighed the scales in its favor.  

One of the first things we look at when adding something like a new start date is who would be alive and interesting and playable at the time; we want to give you as many options for worthy historical figures as possible. This part of the process involves a little bit of back-and-forth at first; every time you move the year forward or backward you gain some figures and lose others, so we have to decide whom we can’t live without and who we’re willing to consider an acceptable – though unfortunate – sacrifice.  

We knew, for example, that we wanted to have the Crusader states and particularly Jerusalem under Baudouin IV – which gives you a preliminary range of 1174 to 1185 for his reign. Then we thought it could also be good to have Heinrich the Lion as Duke of Saxony and a rival and counterweight to the Holy Roman Emperor Friedrich Barbarossa, which would require a year before 1180/1181, when Heinrich was deposed. Just imagine doing this with a few more names and you should have a reasonably solid picture of the calculus involved.  

However, that’s not to say that this was our sole consideration, although it certainly accounted for a healthy amount of the discussion. Another factor that heavily influenced our choice was that we wanted to make sure that any new start date would be in a good position to integrate not only the new mechanics being introduced in Roads to Power, but also a wide range of components of potential future expansions going forwards – whatever they may be.  

No matter whether it’s the allied city-states of Lombard League asserting their independence from imperial suzerainty in northern Italy, or the iron men marching eastward to wage holy war at the urging of the men of the cloth, or a young man of as-yet untapped potential named Temüjin beginning to make a name for himself on the steppes, we will relentlessly and enthusiastically take advantage of everything 1178 brings to the table whenever and wherever the opportunity occurs.  

And please don’t take the above as indication of any specific plans for future expansions or the order in which they may or may not appear – I’ve merely highlighted a few relevant aspects that I personally find compelling – and take it instead as a declaration of our intent to make sure that 1178 remains a vital, thriving, fully integrated, and fun part of your Crusader Kings gameplay experience from here on out.  

Hopefully this has given you a bit more insight into the logic behind our choice of 1178. It’s perfectly alright if you still have more questions – in fact, I hope you do – because next we’re going to delve much deeper into the bookmarks themselves.  

### Call of the Empire​

![image-01.jpg](https://forumcontent.paradoxplaza.com/public/1143069/image-01.jpg "image-01.jpg")


*[Overview of the “Call of the Empire” bookmark]*  


Now, since *Roads to Power* is the expansion introducing Administrative government, let’s take a look at Call of the Empire first. For those of you who may be unfamiliar with the particulars of this era, the Byzantine Empire is presently enjoying a resurgence under the adroit rule of the aging Basileus Manuel Komnenos, but the specter of his cousin Andronikos (an ambitious and reckless adventurer of preternatural charm) looms forebodingly over the prospects of Manuel’s underage son and heir, young Alexios.  

Furthermore, the Byzantines have suffered a recent blow to their aspirations of reclaiming the Anatolian interior – defeat at the Battle of Myriokephalon at the hands of the Seljuk Sultan of Rum, **Kilij Arslan II** (whose name means “Sword Lion”, for the etymologically curious). The great-grandson of Suleiman ibn Qutalmish (the sultanate’s founder), Kilij Arslan has reigned ably in both war and peace thus far, but an abundance of potential successors (no less than eleven sons!) may bode poorly for the sultanate’s future stability.  

A more auspicious future may be in store for princess **Tamar Bagratuni**, the eldest daughter of King Giorgi III of Georgia, and another one of those historical figures who was an influencing factor on the start date; 1178 was the year her father officially confirmed her as his successor after he’d put down the rebellion of the Orbeli family. Historically, her subsequent rule over Georgia marked her as one of its greatest rulers – to quote a chronicle of her reign (*The Life of Tamar, the Great Queen of Queens*), “the entire world was full of her praise, and every language in which her name was pronounced, exalted her.”  

Governing along the Wallachian frontier of the Byzantine Empire you’ll find **Ioannes Kantakouzenos** – according to Niketas Choniates’ *Historia*, a man “huge in size and most courageous of heart, and with a booming voice.” However, the historian goes on to add that despite Kantakouzenos’ extensive military experience, his arrogance and impetuosity resulted in failure more often than success. As a bit of interesting genealogical trivia, the 14th century Byzantine emperor of the same name descended from a cousin of Ioannes’.  

The early genealogy of the Palaiologoi is more than a little Byzantine – pardon the pun – and so I’ll clarify that our **Alexios Palaiologos**, governor of Bulgaria, is the Alexios Palaiologos who was the grandfather of the (future) emperor Michael VIII Palaiologos, and not his younger cousin of the same name (the Byzantines were not renowned for their innovative choice in names), who is historically best known for his association with the emperor Alexios III Angelos.  

And, lastly, we have **Andronikos Angelos** governing in Epirus (where his illegitimate nephew Michael will one day establish an independent despotate), cousin to Basileus Manuel and grandson of Alexios Komnenos himself, and among whose sons are the future emperors Alexios III (mentioned above) and Isaakios II Angelos. Although exhibiting an authentically Byzantine inconsistency in what surname they prefer to use, the Angeloi are a sizable family by contemporary standards and well placed to stack the empire’s offices with their kindred.  

### Swords of Faith​

![image-02.jpg](https://forumcontent.paradoxplaza.com/public/1143070/image-02.jpg "image-02.jpg")


*[Overview of the “Swords of Faith” bookmark]*  


Before we get into detail on Swords of Faith, I do want to be transparent up front that an overhaul for crusades themselves is not a component of this expansion. Something of that magnitude and significance would need – and deserve – more than would be possible as second billing in an expansion with a very different mechanical focus. We know it’s important to you, so it’s important to us that we make sure what we deliver meets or exceeds your expectations.  

Now, to many of you, I expect some of the names in this bookmark will seem a good deal more familiar, in large part due to Ridley Scott’s *Kingdom of Heaven* (and, of course, the CK3 mod of the same name). Though set a few years earlier than the events adapted by the film, here too the leprous Baudouin IV rules the Crusader kingdom of Jerusalem with immense dignity and dedication despite his dreadful affliction – although our historical Balian d’Ibelin is a baron from the beginning, not a blacksmith.  

Given the nature of his malady, particular attention must be paid to his heir, his elder sister **Sibylla**, who is historically (and conveniently for us) between husbands in this particular year. Although historically Baudouin would be succeeded by Sibylla’s son, also named Baudouin, before Sibylla herself, at this point she was still being treated as the presumptive successor over the newborn infant. In addition, while bouncing baby Baudouin takes after his father’s dynasty at the start of the game, worry not – as Sibylla, you’ll get an event shortly to let you determine which side of his parentage he ought to take after.  

Rounding out the Jerusalemite cast is **Raimon de Toulouse**, son of a murdered father (Nizari assassins happened) and brother to a spurned sister (Basileus Manuel happened), a regent of the kingdom during Baudouin IV’s minority who had previously endured nearly a decade of captivity in a Zengid prison. The ruler of the county of Tripoli, the future of his lands is inextricably intertwined with that of the kingdom of Jerusalem itself.  

And, of course, what mention of Jerusalem could be made without acknowledging the exceptional character of **Salāh ad-Dīn Yusuf**, the last vizier to the Fatimid caliphs and the first Ayyubid sultan of Egypt? Of all our bookmark characters in this start date, he perhaps requires the least introduction – his victory over the crusaders at the Battle of Hattin and the reconquest of Jerusalem in 1187 would soon lead to the launch of the famous Third Crusade in response.  

As an additional point of interest, I’d like to mention that we’ve made some slight adjustments to how names are structured, in that Salāh ad-Dīn, his famous honorific (meaning “Righteousness of the Faith”), is now a prefixed nickname. Previously, many such honorifics were treated as components of given names and could be inherited as such, and so in the interests of accuracy and better representation we’ve gone through and reassigned a great many of them as historical nicknames instead.  

Segueing into our next bookmark character, **Muzaffar ad-Dīn Gökböri** is one of the preeminent military commanders in service to the Zengids, as was his father before him. Deposed and exiled from his fief of Erbil in favor of his younger brother, Gökböri presently rules in Harran but historically would go on to betray the Zengids and joined forces with Salāh ad-Dīn (even playing a key role at the Battle of Hattin) to reclaim his patrimony, which he ruled prosperously until his death on the eve of the Mongol invasions. Truly, a man with an excellent sense of timing.  

Last, but certainly not least, is Levon, younger brother to Roupen III, ruler of Armenian Cilicia. Historically, Roupen III is remembered as a kind and humane ruler, but one of retiring character who abdicated in Levon’s favor – perhaps his noblest deed of all, for Levon would be crowned the first true king of Armenian Cilicia and thoroughly earn the appellation *Metsagorts*, which is commonly translated as “the Magnificent'' or “the Great”, but can also be read as “the Thaumaturge,” in the sense of one who performs marvels.  

### Various and Sundry Concluding Words​

It’s been an immense personal pleasure to play a part in bringing 1178 to fruition, and I truly hope you’ve enjoyed today’s look at our new start date – *because we’re not done just yet*. You see, my mandate is to tell you all about the new start date, and that just means I have no alternative but to tell you all about all the *other* interesting parts of it, too, doesn’t it?  

![image-03.jpg](https://forumcontent.paradoxplaza.com/public/1143071/image-03.jpg "image-03.jpg")


*[Overview of England and France in 1178]*  

King **Henry II** of England has imprisoned his wife, **Eleanor of Aquitaine**, for inciting his sons against him in a significantly more literal form of teenage rebellion than is typically meant by the term. Among said sons is the athletic 12th century tournament celebrity **Henry** (called the Young King for having been crowned during his father’s reign), leonine **Richard**, smooth-tongued **Geoffrey**, and young **John**, who would go on to enjoy such harmonious relations with his vassals during his reign that they enthusiastically invited the future king of France to replace him.  

In this period, the French are ruled by king **Louis VII**, the former husband of Eleanor of Aquitaine and perhaps better known as the Younger than the Young at this particular stage in his life. Louis’ eldest daughter is married to one of his preeminent vassals, **Henri the Liberal**, ruler of Champagne, who contributed greatly to the expansion of the famous and prosperous Champagne fairs. Meanwhile, in the south, the heretical Cathar creed has taken hold in the lands of **Raimon of Toulouse**, which would soon lead to the Albigensian Crusade.  

![image-04.jpg](https://forumcontent.paradoxplaza.com/public/1143072/image-04.jpg "image-04.jpg")


*[Overview of the Holy Roman Empire in 1178]*  


The formidable Hohenstaufen Holy Roman Emperor **Friedrich Barbarossa** (“Redbeard”, after the color of his…well, you get the idea) is rivaled within his realm only by **Heinrich the Lion**, duke over both Saxony and Bavaria – the feud between their families gave rise to the enduring labels Guelph (after Heinrich’s house of Welf) and Ghibelline (after the Hohenstaufen castle of Waiblingen). Within the empire, I’d like to draw your particular attention to **Berthold von Andechs**, patriarch of an interesting and mildly obscure family that rose high in both the empire and Hungary and then burned out and went extinct within only a few generations.  

Some fifty years past, a young **Afonso the Conqueror** knighted himself on Pentecost in the Cathedral of Zamora, assembled a host beneath the banner of rebellion, and proceeded to emancipate himself from his mother and her Galician lover in near-legendary fashion, triumphing over them in the battle of Battle of São Mamede. For anyone else, this might have been enough adventure for a lifetime, but for Afonso this was only the prologue; he would soon become the first and founding king of Portugal. Now in his twilight years, Afonso has largely handed over management of the kingdom’s affairs to his favorite daughter Teresa – named, curiously, after his mother.  

![image-05.jpg](https://forumcontent.paradoxplaza.com/public/1143073/image-05.jpg "image-05.jpg")


*[Overview of Iberia in 1178]*  


Sharing the name of the Portuguese monarch are **Alfons the Troubadour**, king of Aragon, and **Alfonso VIII**, king of Castile. Of the two, the former has managed to expand his realm to encompass territories well beyond the Pyrenees, possessing lands of his own in the south of France as well as having seated his brother in Provence – although said brother would soon be murdered after embroiling himself in a war with the lords of Languedoc. It is the latter Alfonso, however, who will earn enduring fame as the future victor over the Almohad army at the Battle of Las Navas de Tolosa.  

Jumping now to another corner of the map, the historically last of the Seljuk sultans of Persia, **Togrul**, is still a child, with true power in the realm resting in the hands of **Jahan Pahlavan Mohammed**, the Ildeguzid atabeg of Azerbaijan, subjugator of rebellious princes and emirs, and one of my personal favorites among the cast of this start date – his honorific, incidentally, can be translated variously as “Hero of the World” or “World Champion.”  

![image-06.jpg](https://forumcontent.paradoxplaza.com/public/1143074/image-06.jpg "image-06.jpg")


*[Overview of Ciscaucasia in 1178]*  

Immediately east of the dwindling Seljuk state is the realm of the Ghurids, where power is presently split between **Muhammad of Ghor** and his older brother, who is technically *also* Muhammad of Ghor – they share a given name. Of the two, the younger is the more famous, and his exploits into India would ultimately give rise to the Delhi Sultanate only a few decades later. Standing in opposition to the Ghurids is **Prithviraja III Chauhan**, whose resistance against the foreign invaders earned him a legendary reputation, and has perhaps had more films made about him than anyone else in this list.  

![image-07.jpg](https://forumcontent.paradoxplaza.com/public/1143075/image-07.jpg "image-07.jpg")


[Overview of Mongolia in 1178]  

Lastly, even further to the east, as mentioned earlier, you’ll find a young man named Temüjin Borjigin, who will soon earn himself another appellation, one to make all the world tremble – Genghis Khan. Need I say more?  

### The Almost Very Definitely Real Final Conclusion​

This time, truly, we’ve reached the end – the list of those I’ve named is by no means exhaustive (I could easily name a good dozen more, and don’t even get me started on Montferrat, but if I start thinking of more names we really *will* be here all day), and I fully expect you’ll turn up countless more interesting figures to play as… or against!  

However, there’s still one more thing the team would like to share with you today – and it’s something I’m pretty happy about, too.  

---

### A Special Message​

Before we go, also coming with the free update is a small but oft requested quality of life improvement, Message Settings! You will now be able to customize the appearance of a variety of common interface messages to your heart’s desire.  

![image-08.png](https://forumcontent.paradoxplaza.com/public/1143076/image-08.png "image-08.png")


*[Location of the Message Settings options]*  

Messages are now sorted into Filter Groups. How each Group should appear is now up to you, as either a tried-and-true *Toast* message (banner messages that display near the top of the screen), a familiar *Feed* message (messages that appear in the notification feed at the bottom-right side of the screen), a *Popup* window (a new addition!), or simply be disabled entirely.  

![image-10.png](https://forumcontent.paradoxplaza.com/public/1143077/image-10.png "image-10.png")


*[Examples of Message Filter customization]*  

As you might have noticed, it is also possible per Filter Group to set whether the game should automatically be paused as it appears, regardless of its display type.  
Note: Certain Filter Groups, integral to giving the player information about the game state or the outcomes of their actions, cannot be disabled.  

![image-11.png](https://forumcontent.paradoxplaza.com/public/1143078/image-11.png "image-11.png")


*[The new ‘Popup’ message window]*  

This is possible thanks to a new and fully moddable database of message_filter_types that may be freely edited or expanded upon, adding new types for more granularity or mod-specific needs.  

![image-12.png](https://forumcontent.paradoxplaza.com/public/1143079/image-12.png "image-12.png")


*[An example of how Filter Groups can be manipulated via modding]*  


---

## Vassal Directives​

In the last two Dev Diaries we picked up on the idea that some of you would be interested in giving your vassals orders, and after thinking about it we came to the conclusion that it’s not only a sound suggestion, but one that can help reinforce the difference that Administrative realms has over other government forms.  

![image-13.png](https://forumcontent.paradoxplaza.com/public/1143688/image-13.png "image-13.png")


*[Overview of the Vassal Directives menu]*  

You will now be able to give Directives to your vassals, presuming that they respect you! Directives are either given from the character interaction menu, or via the ‘Vassals’ tab in My Realm, the latter having the benefit of showing you the current directive. All government types can issue directives to their vassals, in the picture it’s the Holy Roman Emperor doing it.  

![image-14.png](https://forumcontent.paradoxplaza.com/public/1143689/image-14.png "image-14.png")


*[Requirements to give a directive to a Feudal vassal]*  

As you can tell from the requirements, it’s not too easy to make them follow your orders. You have to work your way to a high level of crown authority, pursue specific lifestyles, or gain significant opinion with them. If you no longer fulfill this trigger, they will not follow your directive until you regain their trust. Directives are inherited, so you do not have to worry about setting them again as your vassals die.  

![image-15.png](https://forumcontent.paradoxplaza.com/public/1143690/image-15.png "image-15.png")


*[Differences in Vassal Directives for Administrative vassals]*  

Of course, if you’re Administrative, then following the directives you set is simply your vassal’s job! They will only ever refuse your directives if they are your rival, but otherwise you’re free to set any directive you wish. They’re fully baked into the Administrative UI’s to maximize visibility. Oh, and Administrative also has access to three more directives; Improve Development, Boost Men-at-Arms, and Recruit Men-at-Arms - all significantly more powerful than the default set.  


## ​

## Choose a New Destiny Improvements​

In previous Dev Diaries we gathered some feedback regarding the upcoming Choose a New Destiny feature, where it seemed as if a popular addition would be to add a ‘random’ mode. If you’re not interested in any of the three options, you can now choose to let the die of fate determine your destiny for you!  

![image-16.png](https://forumcontent.paradoxplaza.com/public/1143691/image-16.png "image-16.png")


*[Overview of the new Random Descendant options in the Choose a New Destiny screen]*  

We based the choices on what we could gather were popular fantasies, and added some extra for good measure!  

![image-17.png](https://forumcontent.paradoxplaza.com/public/1143692/image-17.png "image-17.png")


*[Several different options are available when selecting a random character]*  

Some restrictions still apply - such as being of your Dynasty, and keeping the difficulty reasonable (anything above Extremely Hard is, essentially, a game-over situation.)  

It’s still possible to add further categories, so if you feel like you think we’ve missed something feel free to give feedback!  

---

And that's everything for today! I sincerely thank you all for your time and attention; I hope you’ve found today's dev diary interesting, and that you’re looking forward to Roads to Power as much as I am (*and especially 1178, I say with a deep and profound personal and professional bias*).  

We still have a few dev diaries to go ahead of the release of *Roads to Power*, but it'll be a bit longer until the next one - it’s now the start of the Swedish summer break, and so we'll be temporarily parting ways until the team returns in early August.  

We intend to make it well worth the wait, though! When we come back, we'll be showing off another major feature that I think you'll find very intriguing: *Landless Adventurers*. Until then, if you have any questions about today’s topics, I’ll be here and do my best to answer.  

Thanks again, and have a great summer!

<!-- artifact:reactions:start -->
- 177 Like
- 97 Love
- 8 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Cordelion](https://forum.paradoxplaza.com/forum/members/cordelion.1759707/)**
Role: Corporal
Badges: 95
Messages: 28
Reaction score: 1,260

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
