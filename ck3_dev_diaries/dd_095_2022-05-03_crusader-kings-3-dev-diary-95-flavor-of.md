---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1522983/"
forum_thread_id: 1522983
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 95
title: "Crusader Kings 3 Dev Diary #95 - Flavor of Iberia"
dd_date: 2022-05-03
author_handle: Hugo Cortell
expansion: Fate of Iberia
patch: Patch 1.6 (Castle)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2930
inline_image_count: 20
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1522983'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1936.jpg?1651588512
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_299_to_303
    action: preserved_and_flagged
    counts:
      Like: 121
      Love: 81
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_311_to_422
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_423_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1936.jpg?1651588512)
<!-- artifact:thread_banner:end -->

# Crusader Kings 3 Dev Diary #95 - Flavor of Iberia

<!-- artifact:thread_metadata:start -->
- Thread starter [Hugo Cortell](https://forum.paradoxplaza.com/forum/members/hugo-cortell.1630085/)
- Start date [May 3, 2022](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-95-flavor-of-iberia.1522983/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to Dev Diary #95, about the flavor that makes the flavor pack! I am Hugo ([@Hugo Cortell](https://forum.paradoxplaza.com/forum/members/1630085/)), and today my fellow content designer Ola ([@Vaniljkaka](https://forum.paradoxplaza.com/forum/members/1630093/)) will walk you through some of our design for culture, faith, and everything else before I introduce you to our events & decisions.  

In a region as dynamic and well-documented as Iberia, we were truly spoiled with possible content, and had to make some hard choices as to what would work best in the context of Crusader Kings III. Yet we have filled the Fate of Iberia with flavor content high and low, from fairytales whispered by a fireplace to grand designs of priests and kings. In the Fate of Iberia, you might encounter the Estadea, the wandering dead of Galician myth, the legendary Garduña thieves, great smiths of Toledo, cheese-making Vikings, and Andalusian polymaths dreaming of flight.  

For Fate of Iberia we’ve roped in talented content designers from all over our organization to help us pack Iberia full of historical flavor. There is hardly any subject that does not get some love.  

## Culture and Faith​

Iberia’s cultures were in a pretty good place already, thanks to the culture rework in the Royal Court. But, we’ve done a pass on their traditions to make sure they’re fitting and interesting. If you have the Royal Court Expansion, you’ll be able to make some compelling hybrid cultures here - why not Sephardi-Norse, or Berber-Castilian? It can also be a good way to get involved in the Struggle from the outside. Among other additions, you’ll find that Castilians are now Tabletop Warriors, able to challenge others to a grand game of chess!  

![This image depicts the cultural traditions section of a culture, it is highlighting the quote tabletop warriors and quote tradition.](https://forumcontent.paradoxplaza.com/public/821773/devdiary3.png "This image depicts the cultural traditions section of a culture, it is highlighting the quote tabletop warriors and quote tradition.")


 *The Kingdom of Castles, indeed!*  

Concerning faith, our new shared Head of Faith mechanic will add dynamism to Iberia’s fractured religious landscape. More info regarding this will come in a future Development Diary!  

There are events for Muslims, Christians, and pagans, but the big addition is the Mozarabic Faith. They’ll encourage historical “what if” playthroughs and some dramatic decisions, exploring the deep Visigothic roots of Iberian faith. Try to take control of Toledo if you play a Mozarabic Christian - it can allow you to convene a new great church council, echoing the one in 711. But take heed - such a council might also affect the struggle… How will your realm be affected by the vicious debates to follow? There are also other new decisions available to Mozarabs - including the ultimate prize, the restoration of the Kingdom of Toledo!  

![This image depicts Mozarab faith window, highlighting their adaptability tenet.](https://forumcontent.paradoxplaza.com/public/821815/devdiary8.png "This image depicts Mozarab faith window, highlighting their adaptability tenet.")


*The Mozarabs have a long history of adapting to changing circumstances.*  

![This image depicts a Mozarab holy site at toledo.](https://forumcontent.paradoxplaza.com/public/821774/devdiary4.png "This image depicts a Mozarab holy site at toledo.")


*Toledo plays a central role for the Mozarabic faith.*  

Basque Paganism, the other new faith, is a syncretistic belief with Christian and pagan elements, the most prominent vestige of pagan faith in Western Europe, ensconced in the Pyrenees. Among rulers, it is a dead religion at game start, but its traditions persist among the common folk, and an opportunistic ruler might find reason to Champion the Faith of the Country Basques, and bring it back to prominence.  

![This image depicts the remnants of the Basque pagan faith. Their faith window is open, highlighting their Christian Syncretism tenet.](https://forumcontent.paradoxplaza.com/public/821816/devdiary7.png "This image depicts the remnants of the Basque pagan faith. Their faith window is open, highlighting their Christian Syncretism tenet.")


*Remnants of pagan belief have endured in the redoubt of the Pyrenees.*  

## Special buildings, Dynasty tracks and Artifacts​

For monuments and special buildings, there are some you might expect - the great mosque of Córdoba, the basilica of Santiago, the walls of Toledo - and some you might not. We’ve begun exploring having natural wonders as province features, so you’ll find the Rock of Gibraltar here, too. While Iberia certainly has a rich history, it’s not as overcrowded in ruins of past splendor as say, Mesopotamia or Rome, so while there are some Visigothic and Roman monuments here, we focused on things built over the course of the Middle Ages. There’s accordingly also a few you can build yourself, after the game has started.  

![This image depicts The Great Mosque of Cordoba as seen in-game. It is a 3D model.](https://forumcontent.paradoxplaza.com/public/821775/devdiary1.png "This image depicts The Great Mosque of Cordoba as seen in-game. It is a 3D model.")


*The Great Mosque of Cordoba in all its glory! Art has done a tremendous job in bringing the monuments to life.*  

![This image depicts The Tower of Hercules, another 3D model visible on the game map.](https://forumcontent.paradoxplaza.com/public/821776/devdiary2.png "This image depicts The Tower of Hercules, another 3D model visible on the game map.")


*The Tower of Hercules, as it is also called, still stands today, the oldest extant lighthouse in the world.*  

We’re adding new artifacts as well of course, among them the famed Bells of Santiago - or in 1066, their melted-down and reforged state as aquamaniles in the Muslim Court of Toledo. Historically, of course, they were turned into mosque lamps, but that would have been hard to represent well in our 3D courts, so we went with aquamaniles instead. You’ll also be able to find armillary spheres, scallop shells from the pilgrim road to Santiago, chess boards, Visigothic votive crowns, and much more. If you have the Royal Court Expansion, of course some will be impressive items that our art team devoted lots of attention to, to be proudly displayed in your court.  

![This image depicts the quote (Former) Bells of Santiago and quote artifact, it looks like a dog made of bronze with a very lage, round mouth.](https://forumcontent.paradoxplaza.com/public/821836/devdiary5.png "This image depicts the quote (Former) Bells of Santiago and quote artifact, it looks like a dog made of bronze with a very lage, round mouth.")


*Once the pride of Galicia, they now decorate the Toledo court.*  

The two new dynasty legacies are Metropolitan and Coterie, expressing the themes of flourishing cities and interwoven, intrigue-riddled dynasties that seemed fitting for medieval Iberia. In the Coterie legacy, you can gain various benefits related to your dynasty and its members, useful for diplomacy and intrigue. The Reliable House perk, will give you 10% of your councillors’ primary skills, while the ultimate perk in this legacy, Pragmatic Roots, allows dynasty members to disinherit their children for a prestige and tyranny cost. The Metropolitan Legacy will aid you with development, construction and prestige, unlock a unique Expand Cities decision, and give you some added motivation to build new city holdings in your realm. The Republican Education perk introduces the Town Maven trait, that dynasty members might receive if they are educated in a county with hig development. Metropolitan is a great track if you prefer playing tall, building an economically strong realm.  


![This image depicts the new dynasty legacies. The Metropolitan legacy has a background depicting a courtyard full of scientists and inventors from all over the world, while the Coterie legacy shows a court full of people with documents, books and vials of unknown substances.](https://forumcontent.paradoxplaza.com/public/821805/devdiary6.png "This image depicts the new dynasty legacies. The Metropolitan legacy has a background depicting a courtyard full of scientists and inventors from all over the world, while the Coterie legacy shows a court full of people with documents, books and vials of unknown substances.")


*Coterie members can share secrets with each other.*  

I’ll now leave it to Hugo, to talk more about our decisions and events.  

## Events & Decisions​

Fate of Iberia contains a multitude of events and decisions ranging from struggle-specific events which shake-up plans, to flavor events designed to enrich the experience with classic paradox comical occurrences and references to regional curiosities.  

### Struggle Events​

As mentioned above, struggle events help add a bit of chaos to the overall equation, presenting many opportunities themed around the current phase for cunning strategists to turn one’s disaster into another’s advantage during the greater conflict. Struggle events are exclusive to characters partaking in the struggle.  

![This image depicts an event in which an old man is begging the player to rescue their village from it's villainous owner.](https://forumcontent.paradoxplaza.com/public/821778/img1.PNG "This image depicts an event in which an old man is begging the player to rescue their village from it's villainous owner.")


*Such as this event, in which the player is able to give their word in exchange for a claim on a county. Failing to keep your word will certainly have consequences…*  

![This image depicts an event in which your councilman has been murdered by an angry mob, you can take several actions to resolve the conflict.](https://forumcontent.paradoxplaza.com/public/821779/img2.PNG "This image depicts an event in which your councilman has been murdered by an angry mob, you can take several actions to resolve the conflict.")


*Some events will have you deal with unexpected losses, though you can still gain something from the situation if you play your cards right.*  

| ![This image depicts an event in which your prisoner is willing to tell you a secret they know about another ruler in exchange for their freedom. You can accept the deal, ignore it or even tell the other ruler about this.](https://forumcontent.paradoxplaza.com/public/821780/img3.PNG "This image depicts an event in which your prisoner is willing to tell you a secret they know about another ruler in exchange for their freedom. You can accept the deal, ignore it or even tell the other ruler about this.") | ![This image depicts an event in which a blacksmith demands control over the blacksmiths' guild in exchange for making very good swords for you.](https://forumcontent.paradoxplaza.com/public/821782/img5.PNG "This image depicts an event in which a blacksmith demands control over the blacksmiths' guild in exchange for making very good swords for you.") |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

*Other events can grant you advantages when you least expect it, but tread carefully as success is not guaranteed and things can always take a turn for the worse.*  

Struggle events —though all related, are quite different in the opportunities, benefits, and challenges that they present, encouraging players to adjust their strategy as circumstances call. *I would certainly start conquering my neighbors if I got ahold of some good steel, especially since it’d help me get those catalysts I’ve been after for a while…*  

### Flavor Events​

We have also included a variety of smaller, flavor-focused events that help bring the Iberian peninsula to life and create a greater breadth of content for players in the region to experience. Many of these events are inspired by recorded happenings in the region, while others are simply classic Crusader Kings’ events in a Mediterranean flavor. From a story about frightening “thunder stones”, to the myth of legendary Christian mobsters to a peaceful siesta event, you can be sure you will be getting a full Iberian roster of fascinating, action-packed, and ridiculous events.  

![This image depicts an event in which you have the option to allow or forbid eating a whale. It may explode if you try to eat it.](https://forumcontent.paradoxplaza.com/public/821783/img6.PNG "This image depicts an event in which you have the option to allow or forbid eating a whale. It may explode if you try to eat it.")


*Would you eat a whale? Would Allah approve? It probably tastes like chicken anyway.*  

![This image depicts an event that recreates a Valencian story about how a popular local drink came to be. The player, enchanted by this marvelous drink, has the choice to exploit the farmers and force them to only grow the ingredients for this drink.](https://forumcontent.paradoxplaza.com/public/821784/img7.PNG "This image depicts an event that recreates a Valencian story about how a popular local drink came to be. The player, enchanted by this marvelous drink, has the choice to exploit the farmers and force them to only grow the ingredients for this drink.")


*For anyone who has had horchata, this story should sound familiar. Well, with the exception of the whole “now you must only ever make horchata” option.*  

| ![This image depicts an event in which escaped slaves ask that you let them settle in your lands. You can even make a slave the mayor of a town if you want.](https://forumcontent.paradoxplaza.com/public/821785/img8.PNG "This image depicts an event in which escaped slaves ask that you let them settle in your lands. You can even make a slave the mayor of a town if you want.") | ![This image depicts an event in which a translator asks that you open a translation school.](https://forumcontent.paradoxplaza.com/public/822049/img17.PNG "This image depicts an event in which a translator asks that you open a translation school.") |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

*There'll be no shortage of opportunities to improve your realm.*  

### Decisions​

Besides new events, Fate of Iberia also features unique decisions which can be taken throughout the duration of the struggle at specific phases. Let’s take a quick look at two of them now.  

We’ve seen a lot of comments and requests in the previous dev diaries not to ignore the Jewish achievements of the period. In Fate of Iberia, one of its decisions allows you to make the most out of these achievements by enabling you to sponsor a golden age of science.  

![This image depicts a decision in which you can fund the sciences.](https://forumcontent.paradoxplaza.com/public/821789/img12.PNG "This image depicts a decision in which you can fund the sciences.")


*Sponsoring sciences is a noble but expensive endeavor.*  

As the sponsor, you will receive various positive modifiers, though everyone else in the struggle will receive a weaker version of them too. This decision is not exclusive and anyone can “steal” the golden age from you, doing so will strip you of the modifier and replace it with its weaker counterpart. I fully expect this to be the correct kind of chaotic during multiplayer matches.  


![This image depicts two character modifiers, both of them make your cultural fascinations develop faster. One is a better version of the other.](https://forumcontent.paradoxplaza.com/public/821790/img13.png "This image depicts two character modifiers, both of them make your cultural fascinations develop faster. One is a better version of the other.")


*Though not listed in the tooltips, sponsoring a golden age also gives you bragging rights in multiplayer lobbies.*  

Of course, this decision isn’t just a couple of modifiers strapped to a button. Sponsoring a golden age will lead to one of three random events that provide you with the opportunity to easily recruit highly talented scholars and members of the scientific community.  

![This image depicts a follow-up event to the previous decision, a doctor refuses to operate on your elderly vassal because the stars are not aligned correctly. This is based on a real story.](https://forumcontent.paradoxplaza.com/public/821791/img14.PNG "This image depicts a follow-up event to the previous decision, a doctor refuses to operate on your elderly vassal because the stars are not aligned correctly. This is based on a real story.")


*Making the doctor wait will add them to your court, while performing the operation may help you improve relations with your elderly vassal. Of course, under the... "right mindset", this can also become a learning opportunity for your young child, pre-industrial cataract surgery was a lot more successful with a young assistant present.*  


Now, for a more standard decision example: In classic Crusader Kings 3 fashion, we also have plenty of decisions to form titles and gain control over land, such as the “Iberian Foothold” decision, which encourages large foreign powers to make a dash for their piece of the metaphorical Iberian cake by letting them end the struggle from the outside. Though the military investment will certainly be large and the many disunified states in Iberia won’t take their conquest laying down…  

![This image depicts a decision that allows you to conquer Iberia, the French are currently the ones attempting to take the decision in the image.](https://forumcontent.paradoxplaza.com/public/821804/img15.PNG "This image depicts a decision that allows you to conquer Iberia, the French are currently the ones attempting to take the decision in the image.")


*There are plenty of opportunities to rewrite history in Crusader Kings, will you unite Iberia under the French banner or will a post-unification Iberia conquer Europe?*  

## Closing Comments​

We hope the content displayed in this dev diary has gotten you excited about our upcoming Flavor Pack, and look forward to hearing your thoughts on the discussion comments below.

 

Last edited: May 4, 2022

<!-- artifact:reactions:start -->
- 121 Like
- 81 Love
- 12 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Hugo Cortell](https://forum.paradoxplaza.com/forum/members/hugo-cortell.1630085/)**
Role: Court Horchata Taster (and Game Designer)
Badges: 78
Messages: 6
Reaction score: 425

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
