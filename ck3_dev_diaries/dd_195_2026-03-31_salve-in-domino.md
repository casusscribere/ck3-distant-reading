---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1914929/"
forum_thread_id: 1914929
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 195
title: "Dev Diary 195: Salve in Domino"
dd_date: 2026-03-31
author_handle: lachek
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3756
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1914929'
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
    location: raw_lines_324_to_329
    action: preserved_and_flagged
    counts:
      Love: 296
      Like: 141
      (unlabeled — rendered as base64 data URI): 4
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_337_to_451
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_452_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary 195: Salve in Domino

<!-- artifact:thread_metadata:start -->
- Thread starter [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)
- Start date [Mar 31, 2026](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-195-salve-in-domino.1914929/)
<!-- artifact:thread_metadata:end -->

Hello everyone, and welcome to a very special dev diary! Today we finally get to pull back the curtain on what we're cooking up next for Crusader Kings III. As some of you may have [already guessed](https://forum.paradoxplaza.com/forum/threads/dev-corner-catholic-architecture.1904086/), it's all about the very thing that made medieval Europe tick: the Christian Church.  

We're deep in development on this one and have a lot of ground still to cover, so this will be a broad overview of what we're building. Future dev diaries will go much deeper into individual systems, and we will be paying close attention to your feedback throughout.  

Before I get into all the juicy details, let me say a few words about what this expansion is and what it isn't, because I know the speculation machine has been running at full tilt. This is a systemic expansion focused on Christianity - with an emphasis on Catholicism - and the relationship between secular and ecclesiastical power. If you play anywhere in Christian Europe, the Byzantine Empire, or indeed anywhere Christianity has a presence, this expansion will transform the way you engage with your faith and the institutions which claim to speak for God. If you play outside of these regions you will still notice aspects of the revisions we're making to Faiths, but our aim is to add depth and immersive detail to Christian Europe first and foremost.  

With that out of the way, let's dig in.  

## 1- the vision.png

If there is one sentence that captures what we're going for, it's this: **the right to rule flows directly from God.**  

In the medieval world, kings and emperors didn't just need armies and gold - they required the blessing of the Church. Your legitimacy as a ruler was inseparable from your standing as a Christian. The Pope could make or break dynasties. Bishops accumulated enormous wealth and wielded it as political leverage. Holy men preached ideas that could ignite revolutions. And through all of this, the Church itself was evolving - splitting, reforming, debating, and occasionally tearing itself apart over questions of theology that had very real consequences for the people caught up in them.  

We want you to feel all of that in the game.  

Whether you're a French king trying to get a favorable Pope elected, a minor count whose Archbishop is agitating for your excommunication, an ambitious duke trying to get yourself a Cardinal's hat, or the Pope himself trying to hold Christendom together while half your clergy are preaching things that would make Augustine weep, faith should be something you are constantly, meaningfully engaging with. Not a passive stat on your character sheet, but a living, breathing force that shapes your realm and your dynasty's future.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1477707/image_04.png "image_04.png")


## ​

![2 - faith gets personal.png](https://forumcontent.paradoxplaza.com/public/1486334/2 - faith gets personal.png "2 - faith gets personal.png")


Let's start with the most fundamental change: how your character relates to their faith.  

Currently in CK3, your faith evokes a certain flavor, influences many game mechanics, and imposes certain modifiers. If you start as a Catholic, you have some doctrines and core tenets, certain traits are sinful or virtuous, and that's that until you convert or start your own faith. You don't really practice your faith in any meaningful way, nor does it evolve with the centuries. This is what we are looking to change.  

**Spiritual Fulfillment** is a new character metric that tracks how internally fulfilled your character is in their religious practice. Think of it as the spiritual counterpart to Stress, except instead of measuring how close you are to a mental breakdown, it measures how close you are to either sainthood or damnation.  

Your Spiritual Fulfillment is influenced by which religious practices (Tenets) you personally adopt as convictions, how well those align with your personality traits and lifestyle, the choices you make in events, and generally how closely your actions correspond with the beliefs of right practice in your faith. A Generous character who practices Asceticism and goes on regular pilgrimages will find deep spiritual peace. A Lustful character targeted by unceasing Seduction schemes will... have a harder time of it. Choosing the virtuous path despite your sinful nature is itself rewarded, even as it causes you Stress. Creating room for personal dilemmas to naturally emerge that players have a genuinely difficult time resolving is the kind of stuff us sadistic game designers live for.  

Tiers of Fulfillment - both positive and negative - unlock special decisions, modifiers, and events. High Fulfillment characters will be given temptations to overcome but have the ability to help others deal with spiritual conflicts, while those with low Fulfillment can try to repent. But even low Fulfillment comes with benefits, such as the ability to interfere with the Church more readily.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1477708/image_03.png "image_03.png")

## ​

## 3 - tenet revision.png

To make Spiritual Fulfillment work - and to make the whole religious system more dynamic - we're also doing a comprehensive revision of **Tenets**. We are making many new ones, and also reimagining existing ones, as active observances - things your character can choose to practice, champion, or secretly indulge in. Every Tenet will have both a faith-wide effect and a personal effect when a character adopts it into their daily practice, and Tenets can have different statuses within a faith — from Core teachings that define it, through approved and tolerated practices, all the way to outright forbidden ones. Adopting a forbidden Tenet means practicing it in secret, which of course means anyone who discovers your little theological indiscretion could get a juicy Secret Hook on you.  

This changes the entire dynamic of how faiths evolve. Instead of static labels, you get a living ecosystem of religious practice where ideas spread from person to person, where your Court Chaplain's own convictions actually matter, and where a new Pope's choice of which Tenets to elevate as Core teachings sends ripples across all of Christendom. Your character's spiritual journey could be as strategically important as their martial prowess or diplomatic cunning, and the theological preferences of the next Pope could make your carefully cultivated piety suddenly look a lot like heresy.  


## 4- rites.png

One of the biggest mechanical additions is **Rites**, subdivisions of a faith by both character and geography that represent local variations in religious practice.  

In 1066, not every Catholic in Europe practiced their faith identically. In fact, the entire premise of Catholic (=universal) Christianity was to permit local variations of liturgy, as long as some basic theological premises were adhered to. The insular Irish emphasized different aspects of their faith than Mozarabic practitioners, neither of which perfectly adhered to Roman liturgy. These weren't heresies, but natural variations within a single faith, led by local archbishops who had their own theological priorities.  

Clergy characters can start new Rites in which they can make changes to which Tenets are emphasized. An archbishop might elevate one Approved Tenet to Core status while de-emphasizing another. As long as these changes are modest, Rome won't bat an eye. But if a Rite starts teaching practices the Pope considers forbidden, or accumulates too much **Divergence** from the mainline rite... well, that's how you get Cathars. And nobody wants Cathars. (Or do you? More on that later.)  

Rites spread along Ecclesiastical Title borders - a new geographic layer representing the ancient archdiocese regions - and characters within a Rite's domain can choose to adopt it. Over time, neighboring archdioceses may adopt the same Rite, creating regional blocs of distinct religious practice within Catholicism. This naturally soft-contains Rites within realm borders while still permitting the kind of organic drift and cross-pollination that made medieval Christianity so fascinatingly messy.  

The intended dynamic is that Rites evolve slowly, gradually drifting closer to or further from the mainline. Most of the time this is perfectly fine. Sometimes it's not.  


## 5 - when rites go wrong.png

So what happens when a Rite's Divergence drifts too far? When that eccentric archbishop in Cologne starts teaching things that make Rome deeply uncomfortable?  

The Head of Faith can declare a Divergent Rite a **Heresy** through a Papal Bull decision or an Ecumenical Council. The Rite Head then faces a choice: disband and return to the fold, or double down and become a new Faith entirely. If they choose the latter, congratulations - you now have a full-blown heretical offshoot Faith on your hands, complete with its own Head of Faith, its own teachings, and its own followers who are no longer part of the Church.  

Particularly powerful Rites can also turn **Schismatic**. These cannot be declared heretical outright and instead triggers a theological crisis within the faith, which must either be laboriously healed or permitted to lead to an actual schism, where the unified faith turns into two distinct ones.  

We'll cover the full mechanics of heresies and schisms in a dedicated dev diary. For now, the key takeaway is that these emerge organically from the interplay of characters, their Traits, Tenets, and Rites rather than being solely scripted events - which means your game's religious landscape will be genuinely unpredictable.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1477710/image_01.png "image_01.png")

## ​

![6 - college of cardinals.png](https://forumcontent.paradoxplaza.com/public/1486342/6 - college of cardinals.png "6 - college of cardinals.png")


Of course, none of this matters much if you can't influence who decides what is right and wrong - i.e., who sits on the Papal Throne.  

Cardinals are appointed by the Pope, and in the **College of Cardinals** electoral system their most important task is to vote for his successor. But it's not as simple as "highest score wins" - there are three candidate tracks, representing the most politically connected candidate, the most personally devout, and the most radical or reformist. Cardinals sort themselves by theological alignment, and unaligned Cardinals are the swing votes that determine the outcome.  

As a ruler, you will be able to work through specific Cardinals to influence the vote and sway support toward your preferred candidate. You can see who the projected candidates are and what Core teachings they would impose on all of Catholicism if elected - letting you assess, before the vote, how the next Pope might affect your character's Spiritual Fulfillment and the direction of the faith.  

Naturally, putting a member of your own dynasty on the papal throne is the ultimate prize. A friendly Pope can smooth over your sins, crush your enemies with excommunication, and redirect the wealth of the Church toward your ambitions. An unfriendly Pope could do all of those things to you.  

How Papal elections work also changes with the start date. In 867, only clergy in Rome and Italy may vote, with strong influence from the Italian political situation. By 1066, the College of Cardinals is fully established and much more susceptible to the machinations of ambitious rulers across Europe. We'll get into the full details of this system in a later diary.  


## 7 - church on the map.png

To make all of this work, we're adding **Ecclesiastical Titles**, a new geographic layer representing the archdiocese and patriarchate regions that form the administrative backbone of the Church.  

Each Ecclesiastical Title has a capital seat corresponding to a metropolitan city, and an archbishop (or patriarch, depending on your tradition) who holds it. These characters collect a share of all bishopric taxes within their region, giving them real economic power.  

The capital seat of an Ecclesiastical Title can be the site of a **Cathedral**. Cathedral construction is a Great Project that takes a long time and, in typical Great Project fashion, can be contributed to by rulers in the same region. Once complete, the cathedral is represented by a Domicile (and, of course, a model on the map!), which the holder of the Ecclesiastical Title can upgrade to serve a variety of functions. All this wealth poured into cathedral construction and development translates directly into determining the importance and ecclesiastical power of the metropolitan's seat. Raise a promising young theologian, and perhaps one day you will see him in charge of all the faithful at Reims.  

Ecclesiastical Title holders have more leeway than other characters in practicing and teaching Rites that diverge from the mainline, particularly if their importance starts to challenge that of Rome's. Due to this, archbishops have a greater tendency to be in charge of their own Rite or follow divergent Rites. This is something you can leverage as a ruler, if you find a way to hold sway over your archbishop.  

The Pope and other organized faith leaders will have a **Church Treasury**, separate from their personal wealth, which is filled by taxes and tithes from bishoprics across their faith. The Church Treasury can only be spent on Church business: funding temple construction, Great Projects, holy war funding and mercenaries, commissioning religious Artifacts, siphoned into the priest's pockets, and so on. This means the Catholic Church can be relatively wealthy or relatively poor depending on how large it is, how many heresies are siphoning off tax income, and how wisely (or corruptly) its various representatives spend what they collect.  

The Religious map mode has been updated to let you drill down from the faith level to the Rite level, so you can see at a glance how the religious landscape is fracturing (or consolidating) across the map. Combined with the new Ecclesiastical Titles, our aim is to make the Church feel like a living institution with geographic presence, internal politics, and real power.  


## 8 - revised faith creation.png

With all these new systems for how faiths evolve organically, you might be wondering what happens to the old "stockpile Piety, click button, design custom faith from scratch" flow. The short answer is: it's been replaced by something we think will be much more interesting.  

Creating a new Faith now means working through the Rite system. You start by shaping the beliefs and practices within your current faith - elevating Tenets, nurturing a divergent Rite, building enough theological credibility and political power to either schism on your own terms or force the Head of Faith's hand. Your heresy has a causal history, it didn't spring fully formed from the mind of one eccentric king. Instead it grew, spread, and eventually became too big to ignore. We feel that's a much better story, and it also means the AI will produce more believable religious landscapes over the course of a campaign.  

Conversion has gotten a similar treatment. Through the new **Study Faith** scheme, you can learn the Doctrines and Tenets of another religious practice over time - whether from a foreign spouse, a court guest, or a neighboring realm. As you study, you can work newly learned ideas into your personal practice or even have them adopted officially through your Rite. At the conclusion of the scheme you also have the option to convert outright, with the transition being smoother (or rougher) depending on how much theological common ground actually exists between where you started and where you're going.  

You can still convert to any faith in the game, and we're not hard-locking any player fantasies behind this change. While this will undoubtedly make creating a new Faith more challenging, we think you'll find that faiths which evolve through play - through characters making choices, Rites drifting, and theological ideas spreading from person to person - feel considerably more alive than ones assembled from a menu.  


![image_05.png](https://forumcontent.paradoxplaza.com/public/1477709/image_05.png "image_05.png")

## ​

## 9 - holy order types.png

Holy Orders are also getting some love, with **Monastic Orders** distinguished from Military Orders.  

Monastic Orders lease temples rather than castles, and serve as centers of learning and theological development. Rulers can found them just like Military Orders, with some control over how they are shaped, though they become independent entities after that. Both Monastic and Military Orders can now expand across the map by establishing new abbeys, and will gain and lose power over the course of the game.  

All Holy Orders now have their own unique Rite, informed by the choices made during their founding. This means they can become centers of divergent practice - potential allies for reformist rulers, or targets for an orthodox Church cracking down on heterodoxy. Monastic Holy Orders serve as an alternate means of creating and nurturing divergent Rites and are meant as a counterforce to the Vatican's influence.  

Players can become Patrons of Holy Orders and can interact with Holy Order leaders in new ways, including sending family members to specific Orders and inviting Orders into their realm by offering them land.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1477712/image_02.png "image_02.png")

## ​

## 10 - saints.png

What would Catholicism be without its Saints? (Okay, yeah, well, Protestantism, probably.)  

While the Saint Trait and Living Saint Legends already exist in the game, we're now adding several dozen historical Saints for you to adore, plus a path to become canonized after death for your pious deeds. What exactly this means we'll get further into in another dev diary, but for the moment let me tease that it has a lot to do with Spiritual Fulfillment, Personal Tenets, and Artifacts.  

Having a Saint in your family tree is, of course, very beneficial to you and your dynasty - especially when dealing with the Church.  


## 11 - play as the pope.png

Yes, you will be able to play as the Pope.  

Theocratic characters with landed titles become playable, including the Pope. This means wielding the Church Treasury (funded by taxation across Christendom), appointing Cardinals, declaring heresies, calling Ecumenical Councils, excommunicating rulers who displease you, and generally being the most influential person in medieval Europe. It also means navigating the expectations of every Catholic ruler simultaneously. Good luck!  

It's worth noting that despite making this previously unplayable class of characters available, the expansion is emphatically not about playing as clergy trying to seize control of the Church. It is about establishing the Church as machinery which the player, typically in the role of a secular ruler, can strategically interact with and get pushback from. Our goal is to ensure that if you find yourself in the role of a landed character with real influence in church matters, you can still continue playing your dynasty - now with access to more levers to pull - rather than Game Over. Make the most of it!  


## 12- puppets.png

As a secular ruler, you typically don't have a whole lot of say in Church matters. Sure, you can get your Court Chaplain to convert a county for you, or sponsor a Cathedral, or petition the Pope to lift an excommunication. But control over who teaches what, how Ecclesiastical Titles should be organized, whether an Ecumenical Council is called and what it should be about, or who should be the next Pope, these are matters only clergy have a say in.  

All of these new systems create a richly dynamic religious landscape, but as a secular ruler, you'll want to do more than watch from the sidelines while the expansion plays itself. It would be strange and ahistorical to give secular rulers direct ways of imposing change in most cases though, so what we're doing instead is giving you **Puppets** to toy with.  

The Puppet system is a new mechanic that lets you *act through another character* for specific actions in a specific context. Think of it as "your guy on the inside" who can get things done for you, assuming you have enough leverage on them. In the expansion this guy is your Court Chaplain. If you can get and maintain a Hook on them, there are certain things they can do on your behalf: for example, if they are a Rite Head they could start teaching a new Tenet, or even start a new Rite; construct a Cathedral with Church Treasury according to your specifications; and much more. If your Court Chaplain is also an Archbishop or Cardinal, they get access to more ways to reshape the Church and its practices.  

The Puppet system is not specific to Church matters but is also extensible to other domains that we will explore in future expansions, and will even be accessible to modders to create their own ways of manipulating other characters directly.  


## 13 - chalcedonian faith.png

As you might have intuited from a lot of the things I've discussed above, we are also addressing the biggest crime against the historical representation of the Christian Church currently in the game: the lack of a unified Christian church in 867, and the artificial distinction between Orthodoxy and Catholicism across start dates in lieu of an organic schism.  

In the 867 bookmark, most of Christianity (with notable exceptions of the Coptic and Apostolic Faiths) will be unified under one Faith called Chalcedonian Christianity, with multiple Rites such as the aforementioned Insular and Mozarabic Rites, Carolingian Christianity which directly threatens the Vatican's dominance, and the Patriarchates of Constantinople, Antioch, and Alexandria. It's unclear whether Christianity's most important seat is in Rome or Constantinople, so the Faith won't have a proper Head yet. Other Rites will emerge as the game goes on, and a Christian Church Situation will track the tensions both within the faith and with its neighbors. As the Situation moves into new phases due to the natural actions of the various central characters or the outcomes of Ecumenical Councils, the fracture between east and west may become untenable.  

It's a bit of a novel approach for CK3, but we hope this way of telling the centuries-long dynamic story of the medieval church will be fun and exciting to follow in your campaigns!  


## 14 - whats next.png

We have a lot of dev diaries ahead of us to explore each of these systems in detail, and more features, additions, and tweaks relating to Christianity and Faiths overall which I have not mentioned here. Keep in mind that everything you've read today is under active development, is subject to change, and your feedback - as always - will directly influence the final product. We cannot wait to hear what you think!  

In nomine Patris, et Filii, et Spiritus Sancti. Amen.

<!-- artifact:reactions:start -->
- 296 Love
- 141 Like
- 9 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)**
Role: Design & UX Manager/Lead, Crusader Kings III
Badges: 37
Messages: 814
Reaction score: 49,611

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
