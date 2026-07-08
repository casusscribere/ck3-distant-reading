---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1856829/"
forum_thread_id: 1856829
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 181
title: "Dev Diary #181 - Natural Disasters"
dd_date: 2025-08-25
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
body_word_count: 2752
inline_image_count: 14
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1856829'
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
    location: raw_lines_~28_to_144
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_146_to_148
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_289_to_293
    action: preserved_and_flagged
    counts:
      Like: 95
      Love: 20
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_301_to_402
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_403_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# Dev Diary #181 - Natural Disasters

<!-- artifact:thread_metadata:start -->
- Thread starter [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)
- Start date [Aug 25, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-181-natural-disasters.1856829/)
<!-- artifact:thread_metadata:end -->

Hello hello! [@lachek](https://forum.paradoxplaza.com/forum/members/669315/) here to talk about a feature that will be coming to the whole world with *All Under Heaven*, but which will have a special impact on China - Natural Disasters.  

When considering the success rate of medieval rulers, we often consider how cleverly they played important factions against each other, how they picked the right time and place to lead their armies to victory, and in Crusader Kings terms, how they managed their dynasty's blood through setting up capable successors and arranging the right marriages. But another important factor is how they respond when disaster strikes. When the unthinkable happens, will you be prepared or caught short? Will you be able to look after your people with the selfless care your crown demands, or will someone else swoop in and seize the opportunity to demonstrate their own benevolence? Will you stand tall, or will you have to cash in all your goodwill and sell your soul to restore control over your provinces?  

These are the signs of a skillful ruler we're challenging you to display with the Natural Disasters feature.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1347484/image_01.png "image_01.png")


*[An illustration of the impact of a Natural Disaster on the people of the realm]*  

Famously, the devastating *Huang He* (Yellow River) floods in the 11th-12th centuries not only inflicted casualties to the tune of hundreds of thousands lives lost, but also undermined the Song dynasty's ability to fund defenses against the Jurchens and Mongols. And the *Huang He* was not content with contributing only to the fall of the Song dynasty - in the 14th century, when China had fallen to the Mongols and was ruled by the Yuan dynasty, it flooded again, precipitating the famine and revolts that eventually gave rise to the Red Turban rebellion and the subsequent rise of the Ming dynasty. The scope of devastation inflicted by floods and earthquakes upon China was enormous, and directly tied to the people's view of how suited they were to hold the Mandate of Heaven.  

But calamity is indiscriminate - it can happen to anyone, anywhere. The Rhine flooded frequently, causing difficulty for local princes and townships in the Holy Roman Empire. The Aleppo earthquake of 1138, which may have claimed over 200,000 lives, weakened Muslim states in the Levant and served as a temporary boon for the Crusader states in the area - until the power vacuum paved the way for leaders like Nur ad-Din to emerge, who later became a central figure in resisting the same European invaders.  

In designing this feature, we had to be careful to ensure that natural disasters shake up the political landscape of the region appropriately while not punishing players caught up in it through no fault of their own. True, natural disasters are by their very nature random, and there's not much even the wisest ruler - particularly in medieval times - can do to stop an earthquake or flood from happening. To address this we leaned into the governance aspect of natural disasters - how do you *respond* to a calamity occurring in your realm?  

To illustrate this, let me take you on a bit of a journey.  

The year is 1081, and Caliph al-Majid "The Trickster" rules the Fatimid Sultanate, freshly [crowned](https://store.steampowered.com/news/app/1158310/view/509588921973211152) at a mere 34 years of age after the untimely death of his father, claimed before his time by a mild tickle in his throat. All is well in the realm, were it not for my unceasing war against Emir Hussain "the Priest-Hater" of the Hashimid Emirate and his godless supporters, and the 627 issues Errorhoof is screaming about on this debug build. Life is pretty good in Egypt, under the circumstances.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1347485/image_02.png "image_02.png")


*[Screenshot of the Fatimid Sultanate and its ruler shortly after the Coronation]*  

The Nile is revered for its frequent flooding, but this year is different. The water won't stop rising. Something is amiss.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1347486/image_03.png "image_03.png")


*[Event signaling the imminent flood of the Nile River]*  

The river expands even beyond the floodplains, engulfing everything in its path. We know what's coming, but the (as yet) unwashed masses by and large do not yet.  

A Natural Disaster is a type of Situation, like The Great Steppe from *Khans of the Steppe*, and the Dynastic Cycle and Silk Road also from *All Under Heaven*. Situations have participating characters, geographic regions, and can go through phases, each with their own effects and modifiers. I see that we're now in the Warning phase of the disaster, which has no effects. This will soon change.  

As the first warning signs appear, we get a choice of waiting to see what happens or immediately devoting ourselves to addressing this calamity. If the disaster had affected our court, we'd also have an option to go into isolation - though this would cost us dearly in the court of public opinion in the short term, it's better the ruler survives to see the disaster through to its conclusion than perish alongside his people, right? Right?  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1347487/image_04.png "image_04.png")


*[Screenshot of the Natural Disaster panel in the Warning phase and the future Disaster Relief Great Project, alongside an event where the ruler has to choose what approach to take to it]*  

Soon thereafter, the disaster reaches its Impact phase. People at large now understand the terrible danger they're in, and who do they blame? You, of course!  

When Impact hits, you lose Legitimacy. Usually the amount is bearable if you're a well-established ruler with a good track record and the trust of the people, but me, a recently crowned Caliph who can't seem to wrap up a war against the Priest-Hater? It hurts.  

Note that this Legitimacy loss will be substantially higher if you are the Emperor of China, due to the entanglement between the welfare of the realm and the Mandate of Heaven. A flood or earthquake in China could be spun as proof of the ruling dynasty's corruption, and if the disaster strikes during a period of instability in the Dynastic Cycle, it hits even harder.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1347488/image_05.png "image_05.png")


*[Screenshot of the Natural Disaster panel in the Impact phase with negative consequences, alongside an event where the ruler loses Legitimacy, affected counties are struck by a negative modifier, and Control decreases in the disaster region]*  

People will die. My half-brother, Prince Muammar, is among them. One less claimant to the throne, perhaps.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1347490/image_06.png "image_06.png")


*[An event showing a roster of dozens of characters who died in the latest flooding event. Players may also die this way if they're not careful, but are given more of a chance to react in their final moments.]*  

Not only people, but the land itself will be affected. Hopefully the Priest-Hater isn't in a position to take advantage of this…  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1347491/image_07.png "image_07.png")


*[An event showing how fortifications were damaged across the affected provinces as a result of the latest flooding event]*  

Your counties can be afflicted by many different consequences of the disaster.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1347492/image_08.png "image_08.png")


*[An event showing holding taxes being greatly reduced, along with a continuous loss of development, across the affected provinces. Modifiers are cleared after the Recovery Great Project is completed.]*  

Finally, the worst is over. We now enter a Recovery phase, where we can try to rebuild what was lost and restore the people's faith in your rule. But even this phase is not harmless. For every month we remain in disrepair, we lose more Legitimacy.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1347493/image_09.png "image_09.png")


*[Screenshot showing the Disaster Situation panel in the Recovery phase, with a -0.25 monthly loss of Legitimacy applying to all affected rulers until the situation is resolved. In addition, governorships in the affected area are cheaper to revoke during the Recovery phase, letting an administrative ruler more readily manage their roster of governors to eliminate dead weight and elevate more promising ones.]*  

The road to people's hearts is paved with gold, of course - the more the better. But it's not all doom and gloom - once this [Great Project](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-176-southeast-asia.1802991/) is complete, not only will you remove most or all of the negative modifiers you suffered due to the disaster, but you will also gain rewards for every contribution you made. In addition, for Floods specifically, the affected provinces gain bonuses from the silt and moisture left behind.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1347494/image_10.png "image_10.png")


*[Screenshot showing the Flood Recovery Great Project, with three mandatory contributions required to construct alongside three optional ones. Each costs Gold (or Treasury, if you have it) and provides a number of possible benefits or rewards to the ruler who contributes to the project.]*  

The cost of each component of the restoration can be sizable, and depend primarily on the number of counties affected, their development, and the severity of the disaster. No two disasters will play out the same in this regard, so you might want to carefully consider which is best to do first given the expense.  

Land Drainage, for example, will tie up much of your army for 10 years but give you a permanent +10 Direct Vassal Opinion boost as soon as you fund it. The primary rewards, in terms of Legitimacy and Learning Experience in this case, aren't gained until the whole project is completed. Meanwhile, Survivor Recovery will give you a Popular Opinion boost upon taking it, but also a tax burden to carry through the recovery efforts until the project is completed.  

Optional contributions are not necessary to complete the project, but if you can afford them, they can give you much greater rewards. Resettling refugees requires you to give up some land until the project is complete - resulting in a reduced domain limit for characters of most cultures - but yields twice the Legitimacy and a Levy Reinforcement boost.  

All of these rewards and costs are scaled by innovations - Elephants make it easier to remove debris, for example. But of course, as time passes, so does Development, and recovering from late-game natural disasters can be much more expensive, especially if you haven't kept up with your technological progress. China starts with many relevant innovations to help it control disasters even in 1066, while others will need time to catch up.  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1347495/image_11.png "image_11.png")


*[Screenshot showing the effects of the Land Drainage mandatory contribution, which costs 300 Gold in this instance and imposes a 10 year long Levy Reinforcement penalty on contribution, but also yields a positive Vassal Opinion modifier. When the project is completed, the ruler gains Legitimacy and Learning Lifestyle experience. Note that if the contributing character is not an independent ruler, they still benefit - governors gain Governor Effectiveness experience, and characters in realms that use Merit gain Merit.]*  

If you cannot pay yourself, perhaps there are others who can? The Natural Disaster Recovery project screen gives you insight into who else might be willing to foot the bill for a part of this project, and it also lets you try to convince them to do so. My vassal Emir Hisn al-Dawla, for example, is on decent terms with me and might be willing to help with the Land Drainage while I deal with Housing Reconstruction…  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1347496/image_12.png "image_12.png")


*[Screenshot showing a list of two vassals who are potential contributors to the project on account of being able to afford it. One can be convinced to contribute by the player while the other refuses.]*  

…only in exchange for a Strong Hook, but that will do. At least he will suffer a -75% Levy Reinforcement rate for a while, so in the event he rises up against me…  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1347497/image_13.png "image_13.png")


*[Character Interaction where the player is trying to convince the vassal to contribute. They will only do so in exchange for a Strong Hook currently. Other options are a regular Hook for a smaller Opinion modifier, or using a Hook you have on them.]*  

(deep breath) Grand. This is doable. It'll be fine. Teamwork makes the dream work! Maybe in a few years I'll get another wealthy vassal who I could convince to handle the last part, since this war against the Priest-Hater is really taxing me…or maybe I could fabricate a hook on that wealthy nephew of mine who refuses to play ball. Though if I could only raise the cash myself somehow, I sure could use the Legitimacy to cement my rule once and for all…  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1347499/image_14.png "image_14.png")


*[Screenshot of the Disaster Recovery Great Project, showing two dynastic seals stamped over two of the three mandatory contributions, and a remaining total cost of 376 Gold for the final one]*  

Natural Disasters will be displayed on-map in two different ways:  

- A map pin will appear on disaster epicenters, at quite generous zoom levels to let you easily spot them even when they don't occur in your realm. Selecting the map pin will open the Situation panel for the disaster, and will also display which counties are affected with a border
- Terrain shaders will be applied when zoomed in, so you can really feel the devastation! Here's where I would show you an epic screenshot, but these are currently getting their final touches applied after the [recent map graphics upgrades](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-177-a-fresh-coat-of-paint.1854817/), so you'll have to wait to see them in-game

Natural Disasters obviously do not care about realm borders. A flood will affect all counties adjacent to the river, and an earthquake can span counties in multiple realms. Where a single disaster overlaps many realms, a recovery project will be constructed in each. You only pay for the provinces in your realm, but it's also only those provinces that reap the benefits of your contributions. The disaster situation will disappear once the final recovery has been completed.  

Finally, let's talk about frequency - and about China. Natural Disasters are rare occurrences. You might play a full campaign and not be directly affected by one at all, even across centuries. To some degree this also depends on the terrain in your realm and what part of the world you're playing in. Regions that historically suffered earthquakes or floods during this era have a higher probability of being afflicted by one. When a region is afflicted, it is more likely to be centered in terrain suitable for that disaster. Mountainous regions will be more prone to suffer earthquakes, and provinces far from major rivers won't get flooded.  

However - quite naturally - the larger the realm, the larger the risk one part of it will be struck by disaster at any given time. For a realm the size of China, the likelihood of having to deal with them is high. Thankfully, the Emperor has access to two tools to deal with this problem that most rulers don't: the Imperial Treasury, which can be used in place of Gold to pay for Great Projects, and a great many Governors whose fat salaries should really be put to better use than improving their Estates when the future of the realm is at risk. With the increased impact on Legitimacy, due to the unceasing turning of the Dynastic Cycle and the people's perception of how disasters are a sign from the Heavens that change is needed, natural disasters could possibly break - or make - a Chinese dynasty.  

We hope you will enjoy this opportunity to prove your benevolence as a ruler, or for the more cunning among you, use the upheaval to your advantage!

<!-- artifact:reactions:start -->
- 95 Like
- 20 Love
- 10 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)**
Role: Design & UX Manager/Lead, Crusader Kings III
Badges: 37
Messages: 814
Reaction score: 49,611

*[Full game-badge icon list of 41 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
