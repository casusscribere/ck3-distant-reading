---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1779028/"
forum_thread_id: 1779028
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 175
title: "Dev Diary #175 - Ritsuryō, Sōryō, Meritocratic"
dd_date: 2025-06-13
author_handle: PDX_Chop
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3654
inline_image_count: 20
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1779028'
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
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_395_to_399
    action: preserved_and_flagged
    counts:
      Like: 104
      Love: 70
      (unlabeled — rendered as base64 data URI): 3
      Haha: 2
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_407_to_517
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_518_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #175 - Ritsuryō, Sōryō, Meritocratic

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX_Chop](https://forum.paradoxplaza.com/forum/members/pdx_chop.1377369/)
- Start date [Jun 13, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-175-ritsuryo-soryo-meritocratic.1779028/)
<!-- artifact:thread_metadata:end -->

Hey, I’m Chop, a designer working on the upcoming *All Under Heaven* expansion, particularly Japan and Korea. Speaking of which, in today’s development diary we will be exploring the Japanese archipelago and Korean peninsula! Let’s take a closer look at the gameplay mechanics of three new government types: *Ritsuryō*, *Sōryō*, and *Meritocratic*.  


---

### The Land of the Rising Sun​

The Japanese islands occupy an interesting position, being near enough to China to have been heavily influenced by its culture, but remote enough to have largely escaped direct interference from its Hegemons. Expanding to eventually cover the southern islands of *Kyūshū* and *Shikoku*, and most of the main island of *Honshū*, the Yamato people occupy most of the archipelago united under a single emperor, and with no real external threats.  

However, the northern reaches of *Honshū* are populated by the *Emishi* tribes, further north the *Ainu* tribes reside on the island of *Hokkaidō*, and far to the south the island chains of Okinawa and Amami are home to the Ryukyuan tribes. Famed horse archers, the Emishi have long struggled against encroachment from their southern neighbors, who have launched incremental campaigns of conquest for centuries.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1311321/image_01.png "image_01.png")


*[The Japanese political map, note coats of arms are work in progress]*  

Eagle-eyed diary readers will notice that Japan is no longer red, instead taking the *Murasaki* purple of the wisteria flower, to add some visual distinction from Chinese Hegemons of the crimson variety.  


### A Fragile Peace​

During our period, Japan transitioned from a peaceful bureaucratic realm headed by aristocratic families, to a military shogunate dominated by more pragmatic samurai families, but is still a largely unwarlike place, far from the more militarized Japan of the later Sengoku era.  

Amidst all this, there is also a ruling emperor, or ***Ten’nō***, who is nominally the head of state, but whose power varies considerably depending on the circumstances. The ***Yamato*** dynasty has held this position in an unbroken line from ancient times, even up to the present day.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1311322/image_02.png "image_02.png")


*[The government split inside Japan at the 1066 bookmark.]*  

We strived to represent both of these styles of governments, as well the transition between them, along with the ever-present imperial family.  


### The Ritsuryō System​

In our earlier start dates, the *Heian* (Peace) era is in full-swing, following Emperor Kanmu’s establishment of the aptly named capital of ***Heian-kyō*** (now *Kyōto*) in 794. This bustling city’s palace is the center of the government bureaucracy and home of the imperial family, with the **Manors** of the aristocratic families close at hand.  

Taking inspiration from China, ***Ritsuryō*** is the Japanese legal framework, and as in China, the many provinces of Japan are assigned to governors, or *kokushi*. Along with the many branches of the ***Fujiwara*** family, the other aristocratic families of note compete for appointments and recognition.  

Unlike China, the government is de facto directed by a regent ruling on behalf of the sitting emperor. For gameplay purposes, we have simplified the naming distinction between regents of underage emperors, *Sesshō*, and those of adult emperors, under the unified name ***Kampaku***. Though nominally a regent, the *Kampaku* is not in a Diarch relationship with the emperor, and both characters may have their own Diarch when relevant.  

Historically the position of regent was totally dominated by the main line of the *Fujiwara* family, who tried to minimize the influence of the imperial family beyond their ceremonial roles and maintain their pre-eminence among nobility. The *Fujiwara* were an extremely prolific family, whose influence and sheer size essentially dwarfed those of any other family, with almost *500* living members in 1178. Playing as another bureaucratic family attempting to unseat the Fujiwara is a great challenge in itself, though not impossible.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1311323/image_03.png "image_03.png")


*[Example of Kampaku succession score]*  

Becoming Kampaku works similarly to the Acclamation succession of Byzantium, and can be directly raised or lowered by spending Influence, but also has a unique system of specific weights related to the imperial family, and Blocs (which we will discuss more below).  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1311324/image_04.png "image_04.png")


*[The Japanese province map]*  

Also unlike China or other administrative government types in the game, provinces are largely county tier appointments, and generally a governor cannot hold more than one at the same time. This represents the historic Ritsuryō provinces, or *kuni*, of Japan, and the fragmented power of any one official. Almost all historical kuni are represented as counties in-game, except for a few exceptions which were deemed too small and incorporated into a neighbour, such as Iga, Shima, and Awa (in Chiba).  

By default, Ritsuryō rulers cannot create duchies or kingdoms in Japan, even the Kampaku. Shrewd Houses may instead fill many appointments with their own members, leveraging their power as a united family rather than as individuals, a theme common in our Japanese features.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1311325/image_05.png "image_05.png")


[The Japanese Manor domicile, art is work in progress]  

The Manor is a new type of domicile, unique to Japanese governments, with its own buildings, art, and bonuses. *Sōryō* (more on that shortly) is our only non-administrative government type that grants an estate-style domicile, retaining any upgrades when switching between the Japanese government types. Some building chains are only unlocked by certain House Aspirations, which will be discussed more later.  

### The Chrysanthemum Throne​

Though historically the emperor was largely sidelined, the Yamato family was still an influential political force. Over time, it became common for emperors to become monks, abdicating the throne to their heir to escape the direct responsibilities of the throne, while still influencing politics as a so-called cloistered emperor, or ***Hōō***.  

In *All Under Heaven*, the emperor is a playable character, a member of the Yamato family who holds a Noble Family and Manor like other Ritsuryō rulers, and has their own Royal Court. The emperor is only a valid candidate for the regency of Japan itself, while other members of the Yamato family are valid candidates only for governorships.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1311326/image_06.png "image_06.png")


*[The Emperor of Japan, note art is still WIP]*  

If an emperor does manage to take the top title by Influence, they will receive an event where they are given the option to abdicate and rule Japan as a powerful cloistered emperor, or attempt to hold on to both titles, representing the historical possibility of renewed direct rule, though doing so will not be well received by the chattering classes.  

Historically, many branches of the Yamato family were eventually disinherited to prune the royal ranks, taking new names, the most famous being the various ***Taira*** and ***Minamoto*** houses, identified by which emperor they descend from. In our game, Yamato governors can form or join these houses, organically creating new branch families.  

### Imperial Policies​

The sitting top liege of Japan, be they Kampaku, Shōgun, or Ten’no, always has access to a unique law category, **Imperial Policies**, issued in the name of the emperor. Despite the relative political stability, the policies of the Japanese government varied substantially throughout our era, as the bureaucracy was replaced and external politics changed. Like Crown Authority, Imperial Policies can be changed freely besides a cooldown.  

There are a variety of available policies, suited to different objectives and situations, some with wide-reaching edicts which can substantially change the gameplay in the Japanese islands. For example, rulers in the empire of Japan are not able to freely declare external wars, representing the general lack of ambition for conquest besides extending the northern frontier for most of our period. However, by implementing the Imperial Expansion policy, the usual inter-realm casus bellis available elsewhere may be unlocked, along with a reduction to the cost of Mercenaries and Men-at-Arms.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1311327/image_07.png "image_07.png")


*[The Imperial Policies law window, art and vassal approval requirements are work in progress!]*  

Other Policies change the balance between government types in Japan, or provide simple situational benefits at an opportunity cost.  

Conversely, if Japan finds itself under true threat from an external invasion, the Defence Mobilization policy will become available, providing an extra edge in Advantage and allowing Ritusryō rulers access to the usually Sōryō-limited Mounted Samurai horse archer Men-at-Arms.  

### House Aspirations​

Each House in Japan has an **Aspiration**, similar to the House Powers of Byzantium, representing the character and goals of the family as a whole. Each Aspiration has several Levels, each granting new boons. The House Head may spend Prestige to increase the Level of their current Aspiration or change its Type, starting from the lowest Level once again when changing Type.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1311328/image_08.png "image_08.png")


*[The House Aspiration window, art very much work in progress!]*  

Each type of Aspiration is focused on a different area, with some more suited to certain government types than other; **Service** grants bonuses to Governor Efficiency and Candidate Score, and is a good pick for those who wish to climb the bureaucratic ranks and serve emperor; **Ceremony** grants bonuses to Prestige and Renown generation, a sure choice for the noblest of families; **Strength** improves Men-at-Arms and martial skill, ensuring dominance on the battlefield.  

Beyond the bonuses granted, the Aspiration a House chooses will also determine their political goals to a certain extent, and is a driving force in another new feature, House Blocs, which I will touch on a little later.  

### House Relations​

Our free patch accompanying *All Under Heaven* includes another family-oriented mechanic, the **House Relation**. These work similar to character relations like Rivals and Friends, but are between two Houses rather than two Characters.  

Now, whenever a friendly or hostile action is taken between Houses within the same Realm or similar rank, such as declaring wars or arranging marriages, the Relation between the two Houses will increase or decrease.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1311329/image_09.png "image_09.png")


*[Example of a House Relation and the levels, art work in progress!]*  

There is a spectrum of 7 levels, from **Feud** to **Amity**, with each rank towards the extremes modifying the Opinion of all House members to members of the other House. In addition, each level grants other bonuses or modifiers to standard gameplay when interacting with the other House, such as allowing the free negotiation of Alliances, or reducing the costs of all Wars.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1311330/image_10.png "image_10.png")


*[Work-in-progress image of the work-in-progress House Relation history window. It's a work in progress.]*  

This change allows inter-generational disputes and collaborations between families to persist more organically, adding another layer of reactivity to the world. Like Character Memories, the reasons for changes over time are tracked, and can be similarly browsed to get a picture of how a relationship has developed over time.  

### Blocs​

With the fragmented political map inside Japan, we wanted a better way to depict the various political groups, and a way to allow them to defend each other without traditional Alliances, maintaining the fragile peace that so often prevailed.  

**House Blocs** are our solution, and work similarly to the Confederations added in *Khans of the Steppe*, but with Houses as members rather than Characters. A Leading House acts as the main decision-maker of the Bloc, with other Houses considered to be their willing cooperators. The House Head of the Leading House gets to decide which Houses are allowed entry to the Bloc, and may also expel other member Houses at will.  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1311331/image_11.png "image_11.png")


*[The House Bloc window, still very work in progress]*  

Each House Bloc has a Cohesion value, with additional bonuses for all members unlocked for keeping this value high. Cohesion is based on the number and governments of member Houses, whether their House Aspiration matches that of the Leading House, and the Relations between its member Houses.  

The Aspiration of the Leading House acts as a sort of defining principle of the Bloc; a *Service* orientated Bloc will naturally represent Ritsuryō interests, while a *Strength* focused Bloc seeks to expand military power. The Aspiration of a House is not generally limited by their government type, and various combinations are possible. Generally multiple Blocs led by Houses of the same Aspiration type are not common, with interests coalescing around the most able leadership.  

Crucially, Bloc members will automatically join the Factions of the House Head of their Bloc’s Leading House, increase their succession score for Kampaku (if they are Ritsuryō), and also join in their defensive wars, including Tyranny wars started by attempts at Imprisonment or Revocation. This makes challenging a Bloc something to consider carefully, and any wars that do occur are far more impactful than they would be if Japanese vassals were merely isolated county-tier rulers with scattered alliances.  

In addition, acquiring governorships for members of Houses within your Bloc, be they your own or others, can directly aid in strengthening your Factions and succession score or preventing attacks to your position, while being without a Bloc leaves you worryingly exposed to your enemies.  

### The Rise of the Bushi​

As the Heian era wore on, many noble families, frustrated by the fierce competition for appointments with the Fujiwara, despaired of ever climbing the bureaucratic ranks, and instead left the capital, establishing manors in the provinces. Far from the disinterested aristocrats of the capital, the power of these families eventually grew to the point they ruled de facto as a hereditary local nobility.  

We represent this by allowing Ritsuryō rulers to establish a held appointment as a fief, switching their government type to ***Sōryō***. This is considered a crime by the Kampaku, and all Ritsuryō governors are able to use a casus belli which returns the title. However, Sōryō rulers pack more of a punch than the bureaucrats, with access to the Mounted Samurai horse archer Men-at-Arms type. In addition, Sōryō rulers will generally band together to defend themselves, making resisting their spread a less simple proposition.  

By our last start date almost all of Japan was effectively beyond the reach of the Ritsuryō apparatus, instead now dominated by the rising bushi families, most notably the Taira and Minamoto houses.  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1311332/image_12.png "image_12.png")


[The political situation of Japan in 1178]  

By 1178, the head of the *Kanmu Taira*, **Kiyomori**, had effectively supplanted the power of the Fujiwara, ruling as a de facto dictator in a manner which would ultimately come to be known as a ***Shōgun***. Just two years after our last bookmark, the Minamoto houses resisted the overwhelming Taira domination in the **Genpei**, or Minamoto-Taira, war, with their leader **Yoritomo** ultimately wiping out the Taira and establishing the first true shogunate in Kamakura.  


---

### The Three Kingdoms​

Like Japan, the Korean peninsula occupies an interesting position as a heavily Chinese-influenced region, with its own deep cultural and political history. Though it is at greater exposure to invasion from the various states and tribes which lay to its north, it is a fairly developed mountainous region, and any threats will struggle to gain a foothold as long as Korea remains united.  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1311333/image_13.png "image_13.png")


*[Kingdom of Goryeo in 1066, character art, coats of arms, and map are work in progress]*  

By our earliest start date, the *Gim* dynasty of the ***Unified Kingdom of Silla*** in the east had long-subdued its main rivals, the kingdoms of ***Baekje*** in the south and ***Goguryeo*** in the north-west. The struggle between these three states, known as the Later Three Kingdoms or *Husamguk*, had raged for centuries, with Silla ultimately emerging victorious. Further north, the kingdom of ***Balhae***, or *Bóhǎi*, straddles the hinterland between China, Korea, and the Jurchen tribes.  

However, this status quo would not last long; a resurgent Goguryeo aristocracy under the *Wang* dynasty would ultimately overthrow Silla, establishing the ***Unified Kingdom of Goryeo*** based in Gaeseong, ruling the entire peninsula until the establishment of the *Joseon* dynasty in the late 14th century. Meanwhile, soon after Silla fell, Balhae was conquered by Khitan nomads, who would later establish the Chinese-influenced state of ***Great Liao***.  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1311334/image_14.png "image_14.png")


*[Unified Silla in 867 and the Unite the Husamguk decision, art is work in progress]*  

We represent the unification of the Later Three Kingdoms via a special decision, **Unify the Husamguk**, which can be taken by any ruler who holds at least one of the kingdoms and has taken over the entire peninsula in a dominant position. This decision destroys the old kingdom titles and creates an empire-tier Unified Kingdom title, which may be named ***Samhan*** or ***Goryeo*** based on the culture of the unifier. This is the only way for a Korean culture ruler to form the Korean empire-tier title.  

This decision also creates the **Yongsun Throne**, a special Primogeniture kingdom-tier titular title similar to the Chrysanthemum Throne of Japan. The name of this title may also vary based on the culture of the decision taker, with *Yongsun*, or Dragon, deriving from the legend of King Taejo the Great’s draconic heritage, the historical founder of Goryeo. In addition, the decision increases cultural acceptance between your culture and the other Korean cultures, making it easier to create a new Hybridized Korean culture, uniting the Silla, Baekje, and Goguryeo peoples.  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1311335/image_15.png "image_15.png")


*[Screenshot of the Unified Kingdom of Goryeo in 1178, art and map are work in progress]*  

The new Unified Kingdom title also gains a unique Acclamation-style succession law, which is weighted towards the ruling Yongsun Throne dynasty. This leaves open the historical possibility of a powerful family taking control of the state from the royalty, as happened by our latest start date with the rise of the military dictators, or *Banju*, beginning with **Yi Ui-bang** and **Jeong Jung-bu**, leaving the royal Wang dynasty in a ceremonial position similar to the Yamato family.  

### Meritocratic Government​

Along with the Korean kingdoms, the kingdoms of Dai Viet, Balhae, and the Liao and Jin states will use a form of government similar to the Chinese Celestial Government, known as ***Meritocratic***. This government type represents the largely administrative states heavily influenced by China due to proximity, interference, or their aspiration to claim the Mandate of Heaven as a conqueror.  

![image_16.png](https://forumcontent.paradoxplaza.com/public/1311336/image_16.png "image_16.png")


*[Map of governments in East Asia in 1178]*  

Meritocratic governments retain the Noble Families, Estates, Merit, and Examinations of the Celestial government type, promoting their bureaucrats to governorships via a similar system, but may not hold Imperial Examinations of the highest tier. When other forms of government transition into administrative via decision, if they are near to Celestial China they tend to adopt Meritocratic rather than the standard Administrative type.  


---

### Map Corner​

Let’s conclude with a little look at the current map, all of which is of course subject to change based on feedback and should be taken with a pinch of salt. Let’s start with the de jure title structures of the far east.  

![image_17.png](https://forumcontent.paradoxplaza.com/public/1311337/image_17.png "image_17.png")


*[De jure Empire mapmode]*  

As you can see, Japan does not have de jure rights to the north of Honshū at game start, given the ongoing campaigns against the Emishi tribes and that part of Japan being the least integrated into the bureaucracy. Instead the kingdom of ***Hitakami***, or ***Michinoku*** if ruled by Japan, is a de jure part of the empire of ***Amur***, along with the islands of *Sahaliyan* and *Hokkaidō* in the kingdom of ***Aynumosir***. On the mainland, the empire of Samhan, or Goryeo, is bordered by the empire of ***Andong***, composed of Balhae and its environs.  

![image_18.png](https://forumcontent.paradoxplaza.com/public/1311338/image_18.png "image_18.png")


*[De jure Kingdom mapmode]*  

Here we can see the internal kingdoms of Japan, made up of ***Tsukushi*** covering the island of Kyūshū, ***Yamato*** covering western Honshū and Shikoku, and ***Azuma*** covering most of eastern Honshū . On the mainland, Samhan is divided between its three constituent kingdoms of Goguryeo, Baekje, and Silla.  

![image_19.png](https://forumcontent.paradoxplaza.com/public/1311339/image_19.png "image_19.png")


*[De jure Duchy mapmode]*  

As for duchies, Japan is split into regional administrative divisions based on the Gokishichidō circuits. As Ritsuryō rulers cannot create duchies, they will mostly be formed by powerful Sōryō lords, who will use their House names. The duchies of Samhan are based on the *Mok* administrative divisions of the kingdom of Goryeo. To the north, Balhae is split into its administrative divisions, while other areas are based on the dominant tribes of those areas.  

![image_20.png](https://forumcontent.paradoxplaza.com/public/1311340/image_20.png "image_20.png")


*[Culture mapmode in 867]*  

Our cultures are still a work in progress, but broadly Japan is mostly united under the Yamato culture, while the cultures of Korea’s Later Three Kingdoms are yet to be united in the Goryeo culture present by 1066. To the north, the Balhae culture is a hybrid of Goguryeo and *Mohe*.  

Our faith map is about to undergo a large overhaul, so I will hold off on that one this week!  

---

That wraps up our topics for today, I hope you enjoyed this early look at Japan and Korea. Your thoughts and feedback are most welcome, and I’ll do my best to answer your questions below!

<!-- artifact:reactions:start -->
- 104 Like
- 70 Love
- 10 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX_Chop](https://forum.paradoxplaza.com/forum/members/pdx_chop.1377369/)**
Role: CK3 Game Designer
Badges: 1
Messages: 54
Reaction score: 2,021

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
