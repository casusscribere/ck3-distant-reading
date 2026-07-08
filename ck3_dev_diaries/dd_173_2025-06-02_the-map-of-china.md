---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1763581/"
forum_thread_id: 1763581
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 173
title: "Dev Diary #173 - The Map of China"
dd_date: 2025-06-02
author_handle: Cordelion
expansion: All Under Heaven
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3367
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1763581'
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
    location: raw_lines_~28_to_142
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_144_to_146
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_289_to_293
    action: preserved_and_flagged
    counts:
      Like: 162
      Love: 74
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_301_to_411
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_412_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #173 - The Map of China

<!-- artifact:thread_metadata:start -->
- Thread starter [Cordelion](https://forum.paradoxplaza.com/forum/members/cordelion.1759707/)
- Start date [Jun 2, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-173-the-map-of-china.1763581/)
<!-- artifact:thread_metadata:end -->

Good day, everyone! I'm Cordelion, one of the many Game Designers currently working on *All Under Heaven*, and today I'm going to be taking you on a short tour of the geographical side of our upcoming expansion - specifically, China!  

The following dev diaries will have a stronger mechanical focus, but since the map extension is essentially the foundation for this new expansion, we thought it best to give you the overview first to better familiarize everyone with where all the new action is taking place and how we’re approaching that. Something I want to make note of: we're currently experimenting with several aesthetic aspects of the map while also iterating on feedback we've received from our extremely helpful beta testers, as well as external partners and consultants, in order to ensure that our map expansion is as faithful to the period as possible and feels authentic to those whose history is being depicted.  

Your thoughts and opinions are extremely welcome and will absolutely be taken into consideration as this process continues: we’re starting this dev diary cycle earlier than we have for past DLC in order to broaden the window available to integrate your feedback.  

As a result of this, please be aware that what I'm about to share is **a work in progress**, and a great deal of what you're about to see is still very much subject to change, and will not necessarily be exactly what will appear in the expansion on release. I would have liked to have also been able to show you the distribution of faiths and cultures today, but they are not quite ready to be shown at this point, but we’ll be happy to give you a more detailed look in a future dev diary.  

## A Brief Word About Projections​

For those who might be unfamiliar with them, a map projection is essentially a way to reconcile the fact that the Earth is a sphere, but maps need to be able to be displayed in a flat, two-dimensional form. You may have heard of the Mercator projection, for example, to name one fairly widely known.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1304286/image_01.png "image_01.png")


*[Various map projection examples. Pick your least favorite and share it below!]*  

This inherently *always* results in distortion: there is no way around that. For this reason, there are many map projections in existence, each with differing degrees of distortion in different parts of the world. You can't avoid the distortion, you can only choose where it's distributed.  

The map projection we used when originally making CK3 was a custom one, tailored to meet the limits of computer monitor’s standard resolution as well as the game's general needs at the time, which unfortunately did not include most of Asia. The projection is inherently imperfect: we adjusted it as best we could for All Under Heaven, but we can’t replace it entirely - at least not without starting over and remaking all of the game’s maps.  

This will result in certain parts of the map, when compared to others, having a scale noticeably different than that of reality. The Chinese province of Shaanxi is, in reality, the size of Great Britain, but due to distortion and compression appears smaller in-game than the similarly-sized Korean peninsula, while eastern Siberia occupies significantly less of the game’s map than it would realistically.  

We know that to many, these differences may stand out compared to what you might have expected: I just want to clarify that those differences are not because we preferred that it be this way, but rather to explain the process that produced them and why.  

## Heaven Has Not Two Suns, nor the People Two Kings​

The Hegemony of China: the new highest tier of title available in the game and the only one extant on the game map at each of our start dates - although certain specific other hegemonies may be formed by decision after unifying similarly vast and expansive regions (such as the lands of the former Roman Empire and the Indian subcontinent) elsewhere. As for the unique mechanics of the hegemony itself, we’ll talk more about those in a future dev diary dedicated to the subject.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1304287/image_02.png "image_02.png")



The name of the Chinese hegemony in our 867 start date is Tang. This is correct for the ninth century, but obviously not at all fitting for the eleventh and beyond. Something new we’re adding with All Under Heaven is the capacity to have a title’s name evolve over time - while still retaining its previous names in the title’s history, so you won’t have past Tang rulers being shown as if they were Song once the dynasty’s name changes.  

As an extension of this, new ruling dynasties that rise to power in China will have the ability to take their name from a wide variety of historically-appropriate inspirations. Historically, new dynasties risen to power took their names not from their own family surnames, but would instead take the name of a past dynasty, or the name of an ancient state they felt they had a particular connection to. Emperor Gaozu, the founder of the Tang, had been awarded the title of Prince of Tang before he became emperor and founded his own dynasty, for example.  

In addition to the formal renaming of the realm under new ownership, you will also have the ability to choose one of several potential colors to represent their title on the map. This harkens back to the practice of different dynasties assuming certain elemental virtues and thematically adopting the color associated with each element - yellow for earth, red for fire, black for water, azure for wood, and white for metal. The Song dynasty identified the virtue of fire as their guiding principle, and so red was their dynastic color.  

## To Each Their Own Rule​

The next step down is, of course, the empire tier - previously the highest tier achievable in the game, but no longer. The hegemony of China, as it is defined for this period, consists of five empires; Qin, Liang, Shu, Wu, and Yue, all names which echo repeatedly throughout Chinese history.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1304288/image_03.png "image_03.png")



These empires are uncreated at game start, and exist as a step on your journey to claim the Hegemony of China after the previous dynasty’s collapse in a Chaotic Era (which is a phase of the Dynastic Cycle mentioned in the previous dev diary).  

As with the hegemony itself, the names of these political entities can and will change when they are formed, so you could, for example, found the historical (albeit short-lived) Qi dynasty when forming the de jure empire of Liang as the Tang rebel Huang Chao.  

At this tier, you’ll possess the dignity and many of the privileges of an imperial ruler, but your rule is not so widely accepted that you can claim to be the sole undisputed hegemon. You could make the claim, but there are enough others outside your borders powerful to call your invocation of Heaven’s favor into question. Similar to the hegemony, there is admittedly more to say about their specific components than these titles themselves, so we’ll discuss their distribution more in the next section.  

## Heaven Is High and the Emperor Is Far Away​

And now it comes to the kingdom tier, and here we’ve had to be a bit more flexible in terms of our approach. While ample references exist for administrative jurisdictions at the historical equivalent of our county tier, the same is significantly less true at the kingdom tier. We can’t exactly do without them, however, nor do we wish to have them of wildly inconsistent sizes or degrees of game balance, as it is not unlikely that China will at some point fracture into these units.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1304289/image_04.png "image_04.png")



As a result, the configuration at this tier is currently set up instead using a Song dynasty period administrative unit called a circuit, which historically was a bit more supervisory in nature and a little less hands on, but lines up reasonably well with the approximate size of many of our preexisting kingdoms, and gives the ducal tier player a higher layer of titles to which to aspire and pursue, even if they may not have been quite as prestigious a posting in time in which they existed.  

We recognize that the Song system of circuits was fairly unique when compared against the administrations of other dynasties, but the Song’s existence spanning two of our three start dates makes its influence more natural to adopt than that of future dynasties, or those further in the past whose practices did not persist into this time.  

There are some peripheral entities here worth making special mention of. The northern portion of what is modern day Vietnam was known as Annan in this period, nearing the end of around two centuries under Tang rule as its southernmost mainland province. In our later start dates you will see it appear instead as a neighboring state known as Đại Việt (Great Viet) under its own distinct ruling dynasty.  

Similarly worthy of note is the Xia kingdom in the north, previously one of the easternmost regions of our map’s former borders. In the space of our three start dates, this region evolved from a semi-autonomous military regime within the Tang state into a self-proclaimed independent kingdom before being overrun by Tangut invaders, who declared the foundation of the state of Dà Xià (Great Xia), the product of an interesting mixture of Tangut, Han, Uyghur, and Tibetan influences that at one point managed to compel the Song dynasty to pay it tribute for a time.  


Additionally, while we don’t have time to go into too much detail about them at the moment, special mention must be given of the Khitan-led Liao dynasty of the north, supplanted by the Jurchen Jin dynasty by 1178, which invaded and occupied much of northern China in a conflict that displaced millions of peasants and taking the emperor himself as a prisoner of war.  

In All Under Heaven, both the Liao and Jin dynasties will mix Chinese administrative and bureaucratic practices of their imperial government with tribal and nomadic vassals whose traditions and inclinations may clash with the oft-Sinicizing ways of their rulers and those at court. Further worthy of note, historically the Jin themselves would eventually experience a dramatic reversal of fortune in the early 13th century at the hands of a nomadic chieftain named Genghis Khan, with whom some of you may already be familiar…  

And, of course, this section would hardly be complete without mention of the Nanzhao kingdom in the southwest, which goes on to reincarnate as the state of Dàlǐ in our latter two bookmarks, its ruling family perhaps better known among the general public for featuring prominently in the popular martial arts novels by Jin Yong (such as *Demi-God* and *Semi-Devils* and *The Legend of the Condor Heroes*) than for their actual historical achievements. But then again, many things are possible in our game, and perhaps some of you will raise them to legendary levels of Prowess.  

## Governing a Large State Is Like Cooking a Small Fish​

As the primary tier of governorship under the Chinese hegemony is the duchy tier, we’re going to compress duchies and counties into the same section and show off the former while talking mainly about the latter, since the precise borders counties are undergoing a bit of adjustment right now (to try and further minimize the projection distortion mentioned earlier) and are small enough that their names don’t appear at this scale, either.  

One of the main challenges we encountered in drafting the province and county map for China is the fact that while it does possess a dizzying array of historically-documented administrative jurisdictions, they tended to undergo noticeable changes from one dynasty to the next.  

Names were particularly subject to alteration, sometimes going through quite a number of them before then returning to their original or an earlier name: for this reason, please don’t take any of the names you might notice as odd to be final. Names from a mixture of times and places, including the present day, have been used as points of reference throughout development due to many different maps and sources being used, and will be subject to further revision.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1304290/image_05.png "image_05.png")



In addition, settlement patterns tended to (understandably) heavily favor the rich Central Plains in the north, the Sichuan basin in the west, as well as key coastal areas, leaving much of the comparatively less populated interior and border areas to be partitioned among a relatively smaller number of jurisdictions encompassing vast swaths of land - their effective equivalent of our game's baronies or small counties sometimes exceeding the size of entire duchies.  

In the interests of being as consistent as possible in our depiction of the Chinese administrative apparatus, we have drawn primarily from administrative units used during (but not exclusively by) the Tang dynasty known commonly as zhou, an element recognizable even today in the names of great cities such as Guangzhou and Hangzhou. This does not apply, however, to the name of the ineffable and inestimable city of Zhoukou, which uses a completely different character for the first component of its name.  

Some artistic liberties have had to be taken, of course - some of these borders resulted in units that were simply far too large and had to be partitioned, others far too small and had to be merged, and while river crossings play an important role in our game's combat calculations, the assessors of administrative geography in the ninth century clearly played by different rules. That having been said, we still hope to strike a balance that favors historical accuracy as much as the necessary concessions to game mechanics and balance allow.  

## The Nation Is Ruined, but Mountains and Rivers Remain​

I would be remiss in my duties as designated dev diary author if I did not also take a moment to give you a glimpse of some of the (still very experimental) new aesthetic alterations to the terrain map. This is, as mentioned before, absolutely still a work in progress; it quite likely has changed even further in the simple span of time between my writing this dev diary and your reading it. That, however, is a subject for further discussion another time, so I’ll leave you with a taste of it and move on.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1304291/image_06.png "image_06.png")



Something that those of you familiar with Chinese geography may have noticed is that the Chinese coastline in All Under Heaven has some noticeable differences when compared to the modern day. The twentieth and twenty-first centuries have seen extensive land reclamation efforts totaling thousands of square kilometers won from the sea, so in some areas of our map the coastline is distinctly different from how it appears on a map today, and we’ve made efforts to ensure our depiction will be as close to that of the period as possible.  

Similarly, the course of some major rivers may be a source of momentary dissonance when you note that they are not quite exactly where you recall them being. The Yellow River, for example, changed course significantly even within our game's time period, but since navigable rivers are themselves inherently a component of the province map and not something able to be altered without major changes to the game’s fundamental underlying architecture, we had to settle on only one of its courses, the most enduring and the one in place in 867.  

## Geniuses Emerge in Every Generation, Each of Whom Is Remembered for Centuries​

Populating China with historical figures is, as you might imagine, no small task, and has quickly proven itself to be the largest scale addition we’ve made to our historical database since release by a significant, all-encompassing margin. After the vagaries of historical research carried out for much of the rest of the game world, it's almost refreshing to encounter documentation as rich and abundant as it is here, a testament to the diligence and dedication of millennia of bureaucrats and functionaries.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1304292/image_07.png "image_07.png")


*[Wang Anshi’s two sons were indeed both named Wang Pang - but only in English: the Chinese characters for their names were different!]*  

That having been said, in some ways the system that produced such a treasure trove of documentation itself poses a challenge as much as it is a boon to our researchers and design. Magistrates and governors in China held office for what we would consider to be extremely short periods of time, very often only a year.  

As a result of this, some ruler assignments (at least when the game starts) have had to be a little less rigid than we might usually prefer in cases where we don’t have known placements available for the exact years in which the game starts.  

Something else we're specifically working to do as much as possible here is to also include significant numbers of historical figures and their families (such as the patriotic general Yue Fei, the Jin founder Wanyan Aguda, or the Tang warlord An Lushan) who lived during or prior to our gameplay period in our game files, and not just those who were alive or had living descendants at each of our current three start dates.  

This way, modders who wish to explore alternative periods in Chinese history will have an easier time and find them already populated with key figures, as well as making things simpler for ourselves, as well, should we choose to add another start date to the game. This is not a declaration of intent to do so (nor not do so), but rather just an investment in making things more straightforward for future developers should we choose to pursue that possibility further.  

## But What About Performance, You Ask?​

There is one more thing I would like to briefly discuss, as I know full well that for a great many of you this aspect of the expansion is of paramount concern: performance.  

We have significantly extended the existing map to encompass the rest of Asia, adding thousands of historical figures to ensure the same degree of fidelity and depth as we have to Europe or anywhere else in the game world. We are aware, of course, that this raises concerns of potential performance difficulties.  

For that reason, improving performance is something that we're also working on very seriously while developing All Under Heaven, to ensure that your enjoyment of the game will not suffer or be reduced from this broadening of its horizons, and that you can freely and thoroughly enjoy all that the expansion has to offer.  

Please be assured that we're working hard at it just as much as the rest of the expansion, and we will go into more detail in the future in a developer diary dedicated exclusively to this subject.  

## The Play Is at an End, and the Audience Dispersed​

And so we come to the conclusion of today’s dev diary. I hope this has been an informative glimpse into what China will look like in All Under Heaven, and maybe you’ve already spotted somewhere you’d like to play in.  

I’m happy to take any questions or feedback that you may have. My capacity to answer mechanical and gameplay questions related to China right now is limited, though, because that’s what we’re going to be digging into in next week’s dev diary. Look forward to it, and thank you for reading!

<!-- artifact:reactions:start -->
- 162 Like
- 74 Love
- 20 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Cordelion](https://forum.paradoxplaza.com/forum/members/cordelion.1759707/)**
Role: Corporal
Badges: 77
Messages: 28
Reaction score: 1,260

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
