---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1920599/"
forum_thread_id: 1920599
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 2
title: "\"By God Alone\" Dev Diary #2 - Ecclesiastical Power & Rites"
dd_date: 2026-05-05
author_handle: lachek
expansion: By God Alone
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3415
inline_image_count: 18
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1920599'
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
    location: raw_lines_~28_to_114
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_116_to_117
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_300_to_304
    action: preserved_and_flagged
    counts:
      Like: 106
      Love: 103
      (unlabeled — rendered as base64 data URI): 6
      Haha: 1
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_312_to_384
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_385_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# "By God Alone" Dev Diary #2 - Ecclesiastical Power & Rites

<!-- artifact:thread_metadata:start -->
- Thread starter [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)
- Start date [May 5, 2026](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-2-ecclesiastical-power-rites.1920599/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-2-ecclesiastical-power-rites.1920599/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-2-ecclesiastical-power-rites.1920599/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-2-ecclesiastical-power-rites.1920599/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22945](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-1-tenets-spiritual-fulfillment.1919114/ "&quot;By God Alone&quot; Dev Diary #1 - Tenets &amp; Spiritual Fulfillment") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-2-trade-vision.1922255/ "&quot;Silk &amp; Silver&quot; Dev Diary #2 - Trade Vision")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-2-ecclesiastical-power-rites.1920599/?prdxDevPosts=1)

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_banners/4/4481.jpg?1777975056)

# "By God Alone" Dev Diary #2 - Ecclesiastical Power & Rites

- Thread starter [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)
- Start date [May 5, 2026](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-2-ecclesiastical-power-rites.1920599/)

Happy Tuesday! Mikael here again with another update on the development of *By God Alone*. Last week we [talked](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-1-tenets-spiritual-fulfillment.1919114/) a lot about **Rites**, and this week we're going to talk about their finer details - how they start, how they spread, how they go wrong, where the line is between local devotion and outright heresy. We're going to keep that promise, but we're also going to come at it sideways, because Rites in CK3 are not free-floating ideas. They are things specific characters do in specific places, and the places matter as much as the theology.  

To illustrate this, let's see how the mission of Cyril and Methodius plays out in the expansion, since many of you are likely familiar with this story.  

The year is 869. King Rastislav of Moravia - your current character, possibly - has spent the last couple of years in a peculiar kind of correspondence. A pair of brothers, Cyril and Methodius, arrived in his court at the end of the previous decade and taught the Holy Scriptures in his language, which was a novelty. They translated scripture into Church Slavonic, which had also not particularly been done. The work was good. The local clergy noticed. The clergy in Salzburg, several days' ride west, also noticed, and were not pleased.  

Cyril and Methodius travelled to Rome to settle the matter. Cyril died there, but Methodius came home with the Pope's blessing and a tightly defined parcel of permission: a Slavic liturgy, in the local tongue, recognized but contained. It is a real thing. It is also, structurally, a divergent variant of Christianity.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1492376/image_01.png "image_01.png")


*[Screenshot of the Moravian Mission story cycle]*​


That story plays out, more or less in that shape, in any 867 campaign in our current build. At the end of it (if you played your cards right) Methodius creates a new Rite, which enters the religious geography of Europe. The Slavic Rite is Christian, but carries *Anachoresis*, *Dulia*, and *Adaptive* as its starting Core Tenets. Scandalously, the Rite also permits priests to get married (which, while not unheard-of within mainline Chalcedonian Christianity, was at least frowned upon at this time).  

The Slavic Rite may be a pre-scripted storyline, but it leverages a more generalized system, which is what we'll talk about today.  


![1 - Ecclesiastical Titles.png](https://forumcontent.paradoxplaza.com/public/1492377/1 - Ecclesiastical Titles.png "1 - Ecclesiastical Titles.png")


As mentioned above, Rites are not random ideas floating about in the air; they live on the map, on counties and provinces, and are informed by a new title layer we've added called **Ecclesiastical Titles** (the generic term, for the modders out there, is "clerical_region_titles" which can be leveraged to create analogous mechanics for your total conversion mod or whatever). In the West they're known as Archdioceses, in the East as Patriarchates. They sit *underneath* the secular map — your Kingdom of West Francia contains several Archdioceses, the Archbishop of Reims holds one of them, his counties overlap parts of your domain and parts of Lotharingia, and his ecclesiastical authority does not particularly respect either of your realm borders.  

These titles broadly follow the ancient Roman administrative borders the medieval Church inherited and then proceeded to argue about for centuries. However, they are shaped differently in each of the 867, 1066, and 1178 start dates to reflect the evolution of the church's reach over these eras. Where a Christian Kingdom emerges that doesn't host one - which might happen more than you might think, especially over a long campaign - a new Ecclesiastical Title can be created by the Head of Faith. Up-and-coming local clergy, especially ones backed by powerful secular rulers and perhaps a Cathedral of the latest architectural fashion, can also petition the Papacy for his own See, or request the merger of their See and a neighboring one if its Archbishop is sufficiently hapless.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1492378/image_02.png "image_02.png")


*[Screenshot of the 867 Ecclesiastical Regions]*  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1492379/image_03.png "image_03.png")


*[Screenshot of the 1066 Ecclesiastical Regions, notably more widespread and fragmented in some places]*​


The Archbishop or Patriarch holding one of these is an actual person with an actual job. He has subordinate Bishops to oversee. He sees to the faithfulness and souls of local Christian rulers. He starts and administers Church-related Great Projects in his region. He ensures everyone in the region follows the right teachings. When his See vacates, the next holder is selected from local clergy by a Clerical Appointment score - we're still tuning the factors, so I'm not going to walk you through the formula, but the principle is that the next Archbishop of Reims is somebody you can scout before he gets there and have some influence over. The Head of Faith can also override the local process, parachuting in a preferred Cardinal over the heads of an aggrieved local clergy. That happens sometimes. God works in mysterious ways.  


![2- grand cathedrals.png](https://forumcontent.paradoxplaza.com/public/1492380/2- grand cathedrals.png "2- grand cathedrals.png")


An important aspect of tending to your flock is to make sure they have an impressive house to worship in. Currently in CK3, some important cathedrals exist in fixed locations on the map as Great Buildings. In *By God Alone*, most Grand Cathedrals will be constructed - and reconstructed, when a new, more impressive, architectural style emerges - dynamically via Great Projects. As such they can be placed anywhere, but most commonly, they will appear in the designated Seats of Archdioceses.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1492381/image_04.png "image_04.png")


*[Screenshot of the Grand Cathedral Great Project]*​


Construction is roughly thirty in-game years at the default rate - a lifetime in CK3 terms, or even potentially a multi-generational endeavour - and is funded by the holding Archbishop and contributed to by anyone in the region who feels strongly enough about it: local lieges, the top liege, vassals, allies, the Head of Faith if he likes you. Once a Grand Cathedral is built, it is a piece of geography you cannot ignore. It also serves as a Domicile for the clergy holding it, and as such can be expanded upon over time.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1492382/image_05.png "image_05.png")


*[Screenshot of a Cathedral Complex Domicile]*​


Cathedrals, and other Great Buildings designated as religious sites, can be turned into Holy Sites. This requires the Head of Faith to bless the site as such, and also demands it contain a holy relic of some kind.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1492383/image_06.png "image_06.png")


*[In-game render of different Grand Cathedral models]*​


I'll save the proper Holy Sites diary for another week since it's still being iterated on, but the point I want to land today is that a Cathedral *elevates* the Archbishop who holds it. The occupant of a wealthy, well-built metropolitan See is someone the Pope listens to. The administrator of a poor See run out of an unconsecrated chapel with no relics is not. Most of the political weight that you, the player, eventually want an Archbishop of yours to throw around in council comes from making him the kind of man whose Cathedral is famous enough, leading to a larger flock of followers and pilgrims.  


![3 - Church Funds.png](https://forumcontent.paradoxplaza.com/public/1492384/3 - Church Funds.png "3 - Church Funds.png")


Cathedrals are costly to construct, and while patronage was a major source of that wealth, much of it falls on the Church to fund. So how does the Archbishop get his funding?  

As we have mentioned previously, the new Ecclesiastical government type has access to a **Treasury** fueled by taxes (tithes) collected by local Bishops, which flows up through the Church hierarchy to be used to promote the faith. This is driven by the **Ecclesiastical Lease**, which is the contract under which Christian temple holdings are leased to clergy. In addition to gold being funneled up through the vassal-realm priest structure as usual, we now also get a slice of money that flows through the organization through the treasury system; Bishops to Archbishops, Archbishops to Pope, typically.  

Of course, a character can be *both* an Archbishop and the Court Chaplain of a King or Emperor. This gives them two sources of income, one gold-based and one treasury-based. It also gives the King in question a good reason to ensure their Court Chaplain is on their side and owes them lots of favors.  

The Ecclesiastical Treasury can be used for a lot of things: title creation, holding construction, mercenary contracts, Holy Order endowments, calling Ecumenical Councils, contributing to a Cathedral somewhere far from Rome. It can also be squirreled away by a less-than-scrupulous metropolitan who needs a little cash infusion for throwing a grand feast. None of us are truly free from sin.  

A powerful secular ruler with theocratic vassals can also violate the contract relationship. The **Levy the Tithes** Decision makes every clerical vassal in your realm pay you a one-shot tribute, at the cost of a large amount of Piety. We expect some kings to do this occasionally. We expect the Pope to *react* when they do.  


![4 - Founding a Rite.png](https://forumcontent.paradoxplaza.com/public/1492385/4 - Founding a Rite.png "4 - Founding a Rite.png")


So: wealthy Archbishops on a map that doesn't match anyone's realm, sending the Pope a monthly check on top of running their own buildings. What does any of that have to do with what they *teach*?  

A Rite is the answer. Cyril and Methodius founded one. Any clergy character in the right circumstances can found one - a Patriarch, an Archbishop, the Head of a Holy Order (and, as we hinted last time and will detail next time, you have Puppets you can work through to do this as a secular Christian ruler.) The flow is similar to the old Create Faith UI: the founder picks Tenets to elevate or demote and Doctrines to swap. Each individual change carries its own Piety cost, modulated by the parent Faith's Fervor - a modest Rite that nudges one or two Permitted Tenets up to Core is cheap, an aggressive Rite that promotes an anathema teaching is not. The UI shows you a predicted Divergence number alongside each candidate change before you confirm. You (or your Puppet) should never be doing this blindly.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1492386/image_07.png "image_07.png")


*[Screenshot of the Rites of Chalcedonian Christianity in 867. The vertical lines indicate Divergence; the Carolingians may have their own liturgy, and it's very powerful even compared to the influence of Rome, but at least they don't diverge too much in their teachings - for now. Those Insular Irish however…]*  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1492387/image_08.png "image_08.png")


*[Screenshot of the Rite panel, where we can see why Insularism diverges to the extent it does]*​


The Tenets and Doctrines you get to pick from are the ones known to you (or your clergy puppet, as the case may be). You can't just make up a new theological idea you've never been exposed to before, after all. As per our last dev diary, this means Studying other faiths or learning about them in some other way, like travelling far and wide, inviting foreign guests, etcetera. A well-travelled [Merchant family](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-1-design-vision.1917178/) for example might well prove a wealth of foreign knowledge and might originate some very strange ideas if they are put in a position where they can found their own Rite. If you truly want to be a religious innovator, you can also aim to become a *Herald* through becoming a renowned theologian, which gives you access to Tenets nobody has even heard of before.  

What the Slavic Rite actually did, when Methodius founded it, is concrete and embedded into the game. It promoted *Anachoresis* - the Eastern, contemplative, Desert-Fathers ideal - where the Roman Rite has *Apostolic Succession*, the institutional and hierarchical posture of top-down clergy authority. It kept *Dulia* alongside, because the Slavs were not theologically distant from Rome on the topic of saints. Yet it *permits* clerical marriage where the Roman Rite does not. This makes their clergy married men, embedded in their villages, whose moral and political incentives are different from those of a celibate Roman priest.  


![5 - Conversion.png](https://forumcontent.paradoxplaza.com/public/1492388/5 - Conversion.png "5 - Conversion.png")


Counties follow Rites, not just Faiths. This makes them "convertible", at faster rates if the Rites are of the same Faith, and metropolitans (Archbishops, Patriarchs) will always do this within their Ecclesiastical Regions. A powerful Archbishop who founds a new Rite will quite rapidly ensure his followers adhere to the right liturgy.  

Characters can also try to convince one another to switch to their Rite. This means neighboring metropolitans might try to convince one another to unify their teachings, which could make a divergent rite quite a power center over time. This increases the pressure on secular rulers to ensure their local metropolitan teaches what they prefer, and gives you a lever to try to promote your own rite across Christendom.  


![6 - How Far Is Too Far.png](https://forumcontent.paradoxplaza.com/public/1492389/6 - How Far Is Too Far.png "6 - How Far Is Too Far.png")


Every Tenet has a status in any given Rite - Core, Permitted, Known, or Prohibited - and each status carries a weight in the calculation of Divergence. Two Rites that both treat *Apostolic Succession* as Core agree. Two Rites where one has it Core and the other Prohibited disagree, sharply. Add up the per-Tenet contributions across the whole list of Tenets and Doctrines and you have a Divergence score from one Rite to its Faith's mainline.  

At 50 points of Divergence and above, the Rite crosses into what the game flags as potentially heretical territory: a different bucket in the Church's politics, a distinct ragged border on the religious map, and - if a Pope is in a position and a mood to do something about it - the prospect of a **Papal Bull** naming the Rite a Heresy outright. The Rite's Head is then offered a chance to submit and rejoin the mainline. If they choose not to, they will become their own Faith, with the consequence of being labeled a heresy of its parent. While this means the total Divergence across the parent faith has decreased, which is good for the Pope, having a heretical faith to contend with is not typically good for a stable status quo.  

Should you try to create a Rite with an immediate Divergence score above 100 - for example by suggesting all these teachings of the Roman Rite are fine and all, but we should have Lay Clergy and a Temporal Head of Faith, because that's what God's word truly intended - there's not a pressing need for a lead-up period, you'll just be declared a heretical faith outright. Good luck!  


![7 - In Other Faiths.png](https://forumcontent.paradoxplaza.com/public/1492390/7 - In Other Faiths.png "7 - In Other Faiths.png")


Most of what you've learned about today works the same regardless of if you're Christian or not. Most faiths have been split up by Rite, and some faiths have become Rites where we think it better reflects history. For example, Islam has been reshaped around the major historical branches and schools of law: Sunni, Shia, Kharijite, and the early community of Sadr al-Islam are now subdivided into Rites such as Hanafi, Maliki, Shafi'i, Hanbali, Ismaili, Imami, Zayidi, Ibadi, and others. This lets characters and provinces better reflect regional and historical differences, from North African Malikis to Persian Hanafis and the varied Shia communities of the medieval world. Some groups, such as Druze and Quranism, remain distinct faiths where that better fits their historical role.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1492391/image_09.png "image_09.png")


![image_10.png](https://forumcontent.paradoxplaza.com/public/1492392/image_10.png "image_10.png")


*[Screenshot of revised Islamic setup in 867]*​


Obviously, Grand Cathedrals don't exist outside Christianity, but the ability to request your local Great Building be designated a Holy Site, and in general the new dynamic nature of Holy Sites, is universal.  

Rites can be created, divergences punished, and heresies formed in other Faiths as well.  

The key distinction between Christianity and other religions in *By God Alone* with respect to the above is the administrative institution of the Church, split up into regions based on ancient Roman provinces. Everything else that's Christian-only flows from this: the special titles and interactions of these characters, the way they automatically spread the influence of their Rite, the way the money flows through the organization, etcetera.  

---

In the next dev diary for By God Alone, we're going to be talking about **Puppets and Playable Theocracies**, where we'll start to understand how you as a secular ruler can act *through* clergy without necessarily playing them (but also what to expect if you choose to do so). We will also get into the different types of clergy you could play: Prince-Bishops, Archbishops, Cardinals, and the Big Man himself.  

In the meantime: may your Archbishop be loyal, your Cathedral construction not get stuck in development hell, and your Divergence be precisely high enough to be *interesting* without being *embarrassing*.

<!-- artifact:reactions:start -->
- 106 Like
- 103 Love
- 8 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)**
Role: Design & UX Manager/Lead, Crusader Kings III
Badges: 37
Messages: 814
Reaction score: 49,611

*[Full game-badge icon list of 12 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
