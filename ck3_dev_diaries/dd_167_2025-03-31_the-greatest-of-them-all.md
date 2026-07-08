---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1733816/"
forum_thread_id: 1733816
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 167
title: "Dev Diary #167 - The Greatest of Them All"
dd_date: 2025-03-31
author_handle: PDX-Trinexx
expansion: Khans of the Steppe
patch: Patch 1.16
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 6303
inline_image_count: 85
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1733816'
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
    location: raw_lines_~28_to_162
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_161
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3661.jpg?1743407378
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_164_to_166
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_830_to_835
    action: preserved_and_flagged
    counts:
      Like: 101
      Love: 54
      (unlabeled — rendered as base64 data URI): 1
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_843_to_955
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_956_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3661.jpg?1743407378)
<!-- artifact:thread_banner:end -->

# Dev Diary #167 - The Greatest of Them All

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Mar 31, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-167-the-greatest-of-them-all.1733816/)
<!-- artifact:thread_metadata:end -->

Өглөөний мэнд!  

Today we will be covering most of the nomadic flavor that we've introduced with this update, so without further ado…  

---

### The Greatest of Khans​


Great are the plump princes in their southern fortresses, great are the chieftains of the grass sea… but great-EST? Only one is greatest. CHINGGIS KHAAN, Universal Ruler, Khan of Khans, biggest and baddest boi… well, actually, Genghis is only the greatest and the baddest baddie sometimes. In some other playthroughs, the Greatest of Khans will arise organically. Heck, the Greatest one could even be you.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1266892/image_01.png "image_01.png")


*[It’s quite the trait.]*  

The key point is that there is only one GREATEST. Once someone has become Greatest of Khans, no ruler ever can again. It’s the highest point of nomadic achievement, and an absolute game-changer! So yeah, should you or an AI ruler achieve this highest of titles in time… the Mongol Invasion won’t happen. That perilous time of nomadic conquest under a single, mighty ruler has basically just come early. Conversely, if Temujin becomes Genghis in your game session… it’s over for other aspiring GoKs. He is the Greatest of Khans, and there will be no other. So be mindful of your Mongol Invasion game rule.  

Now, it seems prudent to outline the path to becoming Greatest of Khans, as well as the opportunity you’re afforded to prevent others beating you to the finish line.  

All nomads can view the Become the Greatest of All Khans decision, but you must be Dominance level 5 - and therefore, must also be the Gurkhan (owner of the biggest herd on the steppe) - to take it.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1266893/image_02.png "image_02.png")


*[The triggers you must fulfil to begin the path to world conquest.]*  

Above, you can see some additional requirements. Not only must you be the first to achieve Greatest Khanship in your playthrough, but you need an empire of substantial size and to command the Obedience of a range of powerful nomads.  

Be warned! Taking this big step will immediately provoke quite a war against all those who’d like to stop you. There is much to be gained by winning the Great War of Defiance against those arrayed against you… and much to be lost by failure.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1266895/image_03.png "image_03.png")


![image_04.png](https://forumcontent.paradoxplaza.com/public/1266896/image_04.png "image_04.png")


*[The decision’s warning and victory effects]*  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1266897/image_05.png "image_05.png")


*[The decision’s failure effects]*  

When you’re ready to face an uncertain number of foes in order to achieve your grand destiny… click the button. The Great War of Defiance begins, and every nearby ruler in the steppe joins against you. At least one powerful non-nomad will join as well, since - like historical Byzantium and China - they certainly have no interest in a great steppe conqueror arising.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1266898/image_06.png "image_06.png")


*[The Attackers’ true strength is always at least double what’s immediately shown here.]*  

Though your Obedient vassals will join on your side, this should be a stiff fight! The coalition of rulers attack from all sides. If you’re a player trying to stop an AI Gurkhan who’s taken this decision: you’ll be given the chance to join the cause, and keep the Greatest of Khans available for yourself.  

It can end poorly for the Greatest of Khans…  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1266899/image_07.png "image_07.png")



Or… in absolute triumph.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1266900/image_08.png "image_08.png")



And there it is. You - or your fearsome foe - get the Greatest of Khans trait, a slew of big ol’ nomadic armies, and the mission to conquer a big chunk of the world and establish your lasting reign within 75 years. This is done through the Reform the Great Khanate decision.  

But, first, what tools do you have as GoK for expanding your empire? One is the Offer Submission or Ruin interaction, quite similar to Offer Vassalization but with some more intense effects.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1266901/image_09.png "image_09.png")


*[The Greatest of Khans can demand armies of special troops, if they’re not feeling particularly lenient]*  

If your offer of Submission is rudely refused, a particularly devastating war is instantly declared on the recipient. This war slaughters courtiers, destroys buildings, reduces development, and even erases holdings. And, helpfully, makes other rulers more willing to simply submit to you peacefully.  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1266902/image_10.png "image_10.png")


![image_11.png](https://forumcontent.paradoxplaza.com/public/1266903/image_11.png "image_11.png")


*[It is soooo on.]*  

The casus belli used by Offer Submission or Ruin is also available to the Great Khan independent of the interaction, to be freely used for seizing whole realms. However, it only has its devastating refusal effects when incurred as a result of, well, being refused.  

The Greatest of Khans will lose these special capacities if they do not take the Reform the Great in time. It’s a possible end goal for them, and is it ever an endgame one, my dudes. It will afford you with new de jure lands and a major choice: establish an admin/feudal/clan empire OR RAZE CIVILIZATION TO THE GROUND AND LET NOMADISM REIGN.  

I’ll leave the specifics of that madness to your imagination, but it really shouldn’t disappoint.  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1266904/image_12.png "image_12.png")



### Yurt Buildings​


The Nomadic Domicile lands somewhere between the Landless Adventurer’s Camp and the Administrative Estate in many aspects. While mobile like the Camp (as you can gather from the wheels attached to the central yurt), it serves as the focal point for the whole realm, rather than just a small group of adventurers. We tried to reflect that with the domicile buildings, referred to hitherto as yurts. We hope they give Nomads numerous ways to deal with the harshness of the steppe.  
As always, please be mindful that the numbers are not final and are prone to change.  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1266905/image_13.png "image_13.png")


*[Example of the fully upgraded yurts]*  

Each of the yurts provides various bonuses centered around particular aspects of Nomadic life. There is one more yurt not visible in the screenshot above, the Barter Stalls, upgradable into Grand Bazaar. It can be constructed if your realm borders the settled people outside the Steppe and connects to Summon Wealthy Visitors and Establish Paiza System decisions shown in the [previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-166-on-the-move.1733004).  

Let us take a closer look at the central yurt first.  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1266906/image_14.png "image_14.png")


*[First level yurt that county-level Nomads start with]*  

As you can see, it is a start but not much. Resources, cunning, and higher Dominance will be needed to expand your Domicile.  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1266907/image_15.png "image_15.png")


*[Third-level yurt upgrade preview]*  

Without higher dominance levels, you cannot upgrade your central yurt. And without higher levels of the central yurt, you cannot construct and upgrade additional yurts. And without yurts… no yurts. Thus your Nomadic Capital grows with your power and hopefully serves as a record of the road that got you there.  
As you can see, each yurt has internal slots for upgrades that allow for further customization of your domicile. I will be referring to them as yurts as well. It’s all yurts now.  

![image_16.png](https://forumcontent.paradoxplaza.com/public/1266908/image_16.png "image_16.png")


*[Example of main yurt upgrade. Those seats are very comfy, we swear!]*  

Yurts cost gold, prestige, and herd. While the costs are fairly low at the start, they get much higher with each upgrade. The steepest difference is in the gold cost. As gold income for the Nomads is much smaller than for the settled people, fully upgraded yurts require a lot of gold redistribution via raiding. So what can you get for your hard-earned wealth?  

![image_17.png](https://forumcontent.paradoxplaza.com/public/1266909/image_17.png "image_17.png")


*[Fully upgraded Square of the Tumen yurt]*  

This yurt focuses heavily on warfare and raiding. If you're curious about the Heavy Horse Archers men at arms, please keep on reading or quickly scroll down to the Men-at-Arms section at the bottom.  

![image_18.png](https://forumcontent.paradoxplaza.com/public/1266910/image_18.png "image_18.png")


*[Square of the Tumen internal yurt example]*  

If you wish to rely on sellswords, this yurt has you covered. The modifier gives you martial, prowess, and stewardship skills and is available only on the 6th level of this yurt.  

![image_19.png](https://forumcontent.paradoxplaza.com/public/1266911/image_19.png "image_19.png")


*[Another Square of the Tumen internal yurt example]*  

If your tributaries provided you with archers and skirmishers, this yurt will allow you to squeeze extra value from them.  

![image_20.png](https://forumcontent.paradoxplaza.com/public/1266912/image_20.png "image_20.png")


*[Fully upgraded Court Yurt]*  

As one of the most trusted Temujin advisors allegedly once said, conquering the world on horseback is easy; it is dismounting and governing that is hard. For when your glorious horde has swept the steppe, the Court Yurt will provide you with more tools to deal with your trusted subordinates and newfound subjects.  

![image_21.png](https://forumcontent.paradoxplaza.com/public/1266913/image_21.png "image_21.png")


*[Example of Court yurt upgrade]*  

If ruling the steppe is a family business for you, since only blood guarantees loyalty, this yurt will allow you to reap additional bonuses from having your step-aunts and step-brothers in your Kurultai. If your curious about Kurultai, please continue reading, more about them below.  

![image_22.png](https://forumcontent.paradoxplaza.com/public/1266914/image_22.png "image_22.png")


*[Millet Storage yurt upgrade]*  

This is an upgrade to the fertility and herd-centered Millet Storage yurt. For others, the deserts are inhospitable and provide little fertility and herd, with a little bit of investment your Nomads can thrive where others perish. There are similar yurts that cover other types of terrain as well. To further specialize, some cultural traditions have received Nomadic bonuses as well, once again, more about it down below.  

### Obedience​

We have already talked about Obedience in our first [Nomadic Dev Diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-162-steppe-by-steppe.1728107), but as a refresher Obedience is a binary state for subjects and courtiers of Nomadic rulers.  

Obedience increases the chances of a peaceful migration and vassalization, and it reduces the chance of a tributary breaking free or joining their allies in a war against their suzerain, as well as reducing the chances of a character using a Murder scheme against their overlord, or joining a faction against them. Most importantly, Obedience is the only way to guarantee a peaceful succession, explained in our [previous Dev Diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-166-on-the-move.1733004).  

Several factors impact Obedience, like opinion, having a good relationship, being a Kurultai member or being employed in a Court Position. Your spouse and family also have higher spouses, but only your preferred heir will – all other children of martial gender will look at your favourite with disdain, and their obedience may not be guaranteed.  

Traits also impact how likely a character is to be obedient, and underage characters and herders will always be obedient.  

However, there are some tools that you can use to convince someone to become obedient to you:  

**Negotiate Obedience** is a character interaction that can be used to bribe someone with Herd or Gold.  

![image_23.png](https://forumcontent.paradoxplaza.com/public/1266915/image_23.png "image_23.png")



**Demand Obedience** costs prestige, but only those with 45 Dread or more will be able to intimidate their targets.  

![image_24.png](https://forumcontent.paradoxplaza.com/public/1266916/image_24.png "image_24.png")



**Impose Obedience** is a new intent available for all types of Hunts. With it, events are more likely to give out obedience as a reward, especially if the hunt is successful.  

![image_25.png](https://forumcontent.paradoxplaza.com/public/1266917/image_25.png "image_25.png")


![image_26.png](https://forumcontent.paradoxplaza.com/public/1266918/image_26.png "image_26.png")



### Nomadic Court Positions​

Besides the Stargazer, already covered in the[previous Dev Diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-166-on-the-move.1733004), we needed to add some other Court Positions to make the Nomads feel unique from the Feudal rulers. In some cases, we have simply renamed the positions, whereas for others we have chosen to replace one position with another.  

![image_27.png](https://forumcontent.paradoxplaza.com/public/1266921/image_27.png "image_27.png")



The first is the chief law overseer, who, in many ways, takes the role of the Seneschal for a Feudal ruler. They ensure capital control, legitimacy, and obedience. They have access to the Seneschal tasks, ‘Organize Court’ (Aptitude) and ‘Manage Domain’ (Control), but also have access to a new task called ‘Blend Cultures,’ which will increase culture acceptance with cultures in the realm.  

![image_28.png](https://forumcontent.paradoxplaza.com/public/1266922/image_28.png "image_28.png")



The second is the Boyan, one of your leading generals. It improves your military and gives you access to two new tasks: 'Cow Vassals’ (Increased Vassal Contribution) and ‘Prepare Raids’ (Increased Raid Speed and Movement).  

![image_29.png](https://forumcontent.paradoxplaza.com/public/1266923/image_29.png "image_29.png")



The third is the Yurtchi, a position similar to a quartermaster that oversees both your camp and your troops. It has access to two tasks, either decreasing everyone’s opinion of you and costing a lot of prestige but gaining more gold, or spending gold to increase everyone’s opinions of you and popular opinion.  

![image_30.png](https://forumcontent.paradoxplaza.com/public/1266924/image_30.png "image_30.png")



The Keeper of the Horses ensures your steeds are well-equipped for war and travel. They also have access to the two tasks that Master of the Horses usually have access to.  

![image_31.png](https://forumcontent.paradoxplaza.com/public/1266925/image_31.png "image_31.png")



The siege engineer is instrumental if you want to start sieging areas outside the Steppes. It has access to the task to increase fort level in your lands, but also a new task that gives a chance to get access to Siege Weapon MAAs (which is usually harder for Nomads to get access to). This position can only be held by someone with the Military Engineer trait, so you will likely have to look outside the Steppes to find a fitting candidate.  

![image_32.png](https://forumcontent.paradoxplaza.com/public/1266926/image_32.png "image_32.png")



As the chief of the bodyguards, the Cherbi will improve other bodyguards, give access to more knights, and increase some of your Men-at-Arms. They can access the regular bodyguard task and a new task that improves your scheme defenses.  

![image_33.png](https://forumcontent.paradoxplaza.com/public/1266927/image_33.png "image_33.png")



Finally, we have a position for those with many tributaries. It has access to the task ‘Entertain Courtiers’ from the Court Jester and a new task to increase culture acceptance and gain opinion with your tributary cultures.  

### The Kurultai​

Nomadic rulers no longer have access to the regular Council but instead have a unique Kurultai setup for its council. They keep the Spymaster, but the rest of the positions have been replaced with a new Kurultai position.  

![image_34.png](https://forumcontent.paradoxplaza.com/public/1266928/image_34.png "image_34.png")



Each of the four Kurultai members has access to the same eight tasks:  


- Two for Diplomacy
- Two for Stewardship
- Two for Martial
- Two for Learning

To start, two tasks have been moved from regular councillors to the Kurultai:  


- Increase Control (from the Marshal)
- Domestic Affairs (from the Chancellor)

As for their other tasks, let us start with their new default task.  

![image_35.png](https://forumcontent.paradoxplaza.com/public/1266929/image_35.png "image_35.png")



It is a simple Diplomacy task that they can always fall back on to improve Herd Gain and Capacity for their liege.  

![image_36.png](https://forumcontent.paradoxplaza.com/public/1266930/image_36.png "image_36.png")



For the Nomads who are growing larger and more settled down, they should consider utilizing the Manage Fertility task to ensure that their lands are as well taken care of as possible.  

![image_37.png](https://forumcontent.paradoxplaza.com/public/1266931/image_37.png "image_37.png")



Whereas for a smaller Nomad planning to migrate more often, maybe you just want to squeeze the land before moving on. Then, it might be good to see if you can get as much out of it as possible before moving on.  

![image_38.png](https://forumcontent.paradoxplaza.com/public/1266932/image_38.png "image_38.png")



If you are interested in… being a tourist in foreign lands, let’s say, this will enable you to maximize the number of souvenirs you can bring home again.  

![image_39.png](https://forumcontent.paradoxplaza.com/public/1266933/image_39.png "image_39.png")



If you want to maximize the potential of your Stargazer and their predictions, having a well-taught Kurultai member who can help them out will be key to improving their Aptitude.  

![image_40.png](https://forumcontent.paradoxplaza.com/public/1266934/image_40.png "image_40.png")



If you are more interested in hybridizing your culture or changing something around, you should look to the final new task for the Kurultai. This will mesh well with the two new Court Position Tasks we have added to improve cultural acceptance in your or tributary lands.  

Three of these tasks can only be done by one Kurultai Member at once:  


- Organize Raiders
- Aid Stargazer
- Explore Cultures
Because otherwise, they would most likely be too effective or work funkily (Explore Cultures).  

Two tasks cannot be done in the same province at once:  


- Manage Fertility
- Exploit Lands
Because they are pretty much doing the opposite of one another. Exploit Lands can only be done inside your Domain instead of in the Realm at large. We found it was way too good if you could simply squeeze your vassals dry by exploiting their land.  

As you might have noticed in the first picture, we have a small UI change to how their tasks look.  

![image_41.png](https://forumcontent.paradoxplaza.com/public/1266935/image_41.png "image_41.png")



Since it was pretty noisy to have eight tasks shown for all 4 Kurultai members at all times, we added a new little window you can open and close to choose the tasks you want.  

### Hunt Activity Adjustments​

Nomads on the Steppe hunted all the time - it was a way of life for them. To represent this we couldn’t leave hunts exactly as they were, costing gold which is a resource that nomads generally do not have. Instead they cost herd, and have a host of additional benefits for nomads in particular. Nomads pay a nominal amount of Herd to start their Hunt Activities, and upon finishing a hunt they gain a Stocked Meat modifier which reduces the cost of their next Feast - a perfect way to get the gold required for hosting Tsagaan Sars!  

![image_42.png](https://forumcontent.paradoxplaza.com/public/1266936/image_42.png "image_42.png")


*[Nomad-specific host Hunt effects]*  

Nomads tend to find a lot more Animal Sightings through their flavor content, which boosts success chances for any Hunts hosted in those provinces.  

![image_43.png](https://forumcontent.paradoxplaza.com/public/1266937/image_43.png "image_43.png")


![image_44.png](https://forumcontent.paradoxplaza.com/public/1266938/image_44.png "image_44.png")


*[Two simple hunt sighting events]*  

![image_45.png](https://forumcontent.paradoxplaza.com/public/1266939/image_45.png "image_45.png")


*[Some seasons have special hunt events, like Everlasting Summer]*  

They’ll get sightings for regular game, birds, and dangerous beasts - the latter of which has additional benefits to hunt: taking down dangerous beasts, such as wolves, will give you both dread (a currency very useful for nomads) and prowess, both for you and all of your hunters.  

![image_46.png](https://forumcontent.paradoxplaza.com/public/1266940/image_46.png "image_46.png")


*[Dread and Prowess gain from hunting a wolf]*  

Expect to be invited to many hunts on the steppe, as AI Nomads are always on the hunt for more Prestige, and will now, in addition to who they previously invited, invite their tributaries, suzerains, and potential friends/lovers to their hunts.  

### Nerge and Tsagaan Sar​

![image_47.png](https://forumcontent.paradoxplaza.com/public/1266941/image_47.png "image_47.png")



Moving onto a more flavorful (literally) topic, the nomad feast – the Tsagaan Sar! Observed in the coldest months of the year (December to March), the Tsagaan Sar ensured the new year started with a bout of revelry, and many would exchange gifts.  

![image_48.png](https://forumcontent.paradoxplaza.com/public/1266942/image_48.png "image_48.png")


*[Choosing a preferred gift for the Feast]*  

As the host, you can choose which gift you’d prefer to receive, and as a guest, send a gift to the host.  

The Tsagaan Sar brings encounters not seen in a regular feast. Race against your peers, gamble against your local yurt’s drunkard, or even demand gifts from your guests. And of course, you cannot forget a staple of steppe culture – throat singing! During your feast you can learn a throat singing style, which can benefit you in tournaments!  

![image_49.png](https://forumcontent.paradoxplaza.com/public/1266943/image_49.png "image_49.png")


*[A Throatsinger at the Tsagaan Sar]*  

For followers of Tengri, the feast concludes with a declaration honoring the animal according to the lunar calendar. There are 12 different animals associated with the lunisolar calendar, each offering a different boon!  

![image_50.png](https://forumcontent.paradoxplaza.com/public/1266944/image_50.png "image_50.png")


*[Receiving a boon for the Year of the Pig]*  

![image_51.png](https://forumcontent.paradoxplaza.com/public/1266945/image_51.png "image_51.png")



Building on the Hunt changes mentioned before, Nomads have access to a new hunt type - the Nerge. Known as the Great Hunt, dozens of hunters would gather in the steppe to slay hundreds of animals. Along with being an opportunity to gain prestige, this new hunt type offers a unique Intent - Dreadful. The Nerge was not only an opportunity to slaughter beasts for the next feast, but is a great way to flex on your tributaries and vassals.  

![image_52.png](https://forumcontent.paradoxplaza.com/public/1266946/image_52.png "image_52.png")


*[Showcasing the Dreadful Intent]*  

Contrary to a traditional hunt, the Nerge was used to practice military tactics that led to Mongol victories.  

![image_53.png](https://forumcontent.paradoxplaza.com/public/1266947/image_53.png "image_53.png")


*[You’ll get to decide the best tactic as the Nerge host.]*  

If your Nerge is successful, along with gaining prestige, gold, and legitimacy, you’ll bring the strategies used into battle - via commander traits and experience.  

![image_54.png](https://forumcontent.paradoxplaza.com/public/1266948/image_54.png "image_54.png")


*[Nerge outcome event]*  

### Pleasure Dome​

![image_55.png](https://forumcontent.paradoxplaza.com/public/1266949/image_55.png "image_55.png")


*[Devise Pleasure Dome Decision]*  

What better way to immortalize your legacy as a mighty Khan than to construct a leisure palace fit for a conqueror? This decision becomes available to you once you have a Kingdom title. Based on a vision in a dream, the Kubla Khan poem by Samuel Taylor Coleridge. A favorite here among the development staff.  

![image_56.png](https://forumcontent.paradoxplaza.com/public/1266950/image_56.png "image_56.png")


*[Pleasure Dome Special Building]*  

This decision allows you to construct the ‘Pleasure Dome’ building, offering a substantial bonus to your Feasts, Taxes, Prestige, Schemes, and Court Grandeur. It is said that different kinds of wine flowed from its silver tree fountain! Sign me up please.  

![image_57.png](https://forumcontent.paradoxplaza.com/public/1266951/image_57.png "image_57.png")


*[Summon Fair Courtiers Decision]*  

On top of that, you can now invite Courtiers with congenial beauty traits. It is time to secure your dynasty’s lineage!  

### Burkhan Khaldun​

![image_58.png](https://forumcontent.paradoxplaza.com/public/1266952/image_58.png "image_58.png")



The Burkhan Khaldun is one of the Khentii Mountains in northeastern Mongolia. This mountain had a special religious significance to the peoples of the steppe, as it was the mythical birthplace of the historical Genghis Khan.  

To reflect that, we've added a special building to the map, giving out Piety and Renown rewards, as well as some military advantages to having control over such an imposing natural feature.  

![image_59.png](https://forumcontent.paradoxplaza.com/public/1266953/image_59.png "image_59.png")



### Expanding the Steppe​

"Oh bother!" you might say in your most emphatic Winnie the Khan voice, "The steppes are too small, and my realm has overflowed into a neighboring region full of icky settled peoples and not enough pasturage for my herds!" Worry not, O Horse Lord of the Thousand-Acre Steppe! You can *Expand the Steppe* if your grip on these new lands is firm enough.  

![image_60.png](https://forumcontent.paradoxplaza.com/public/1266954/image_60.png "image_60.png")



Completely control, through vassals or tributaries, specific regions that neighbor the existing Steppes, and with enough prestige and pizzazz you can add your conquered region to the Steppe, giving these lands some much-needed fertility and making it much easier to migrate around in as a good nomadic leader. Even more regions can be added as the Steppe grows — the only limit is the endurance of your horde, and how far they're willing to ride.  

### From Adventurer to Nomad, and Back Again​

If your character is an adventurer there's a chance that the nomadic life will appeal to them. For this, we have added a special Decision to Adopt the Nomadic Ways.  

![image_61.png](https://forumcontent.paradoxplaza.com/public/1266955/image_61.png "image_61.png")



If you move your camp to a county held by a Herder you'll be able to take over their lands and hybridize with the local culture, becoming a proper Nomad. A Percentage of your Provisions will be transformed into Herd, and you will join the Great Steppe situation.  

However, if that Herd was a Tributary or Vassal to a previous nomadic ruler you will be asked to become a tributary yourself or make an awful first impression.  

![image_62.png](https://forumcontent.paradoxplaza.com/public/1266956/image_62.png "image_62.png")



### Special Casus Belli​

Besides the Migration, Invasion, Tributarization and Nomadic Quarrels we have added two extra new types of Casus Belli, only available to Nomads.  

The **Humiliation CB** is available to target a ruler of higher Dominance than you, or the Gurkhan (the character with the highest Herd in all the Great Steppe). This is a great tool to try and stop someone on their way to become the Greatest of Khans.  

If you win a Humiliation war, the loser is forced to go down one Dominance level (putting the regular 5 year cooldown on them to prevent them from changing it back immediately), and to pay part of their Herd and Prestige to you, as well as some of their obedient vassals deciding that they should not obey a defeated liege.  

![image_63.png](https://forumcontent.paradoxplaza.com/public/1266957/image_63.png "image_63.png")



The **Retaliation CB** becomes available when a character migrates into one of your tributaries' lands and decides to not pay tribute to you.  

![image_64.png](https://forumcontent.paradoxplaza.com/public/1266958/image_64.png "image_64.png")



If you win a Retaliation War you will force the character to become your Tributary regardless, and make them pay some Herd and Prestige to you in addition to that.  

### Recruit Courtiers from Nomadic Capital Decision​

Now, you’re the leader of a nomadic people - it feels wrong to not have skilled hunters and other characters ready at your will. Because of this we’ve added a ‘Recruit from nomadic Capital’ decision where you can choose to spend a nominal amount of herd (symbolizing that the ones you recruit can no longer manage their flocks) in exchange for three courtiers of the desired type.  

![image_65.png](https://forumcontent.paradoxplaza.com/public/1266959/image_65.png "image_65.png")


*[Recruitment decision]*  

These characters will be of the Culture and Faith of your people - and will generally be quite skilled. Not all types are available from the start though, some require you to construct specific Yurt Buildings. A perfect way to get skilled hunters for your Hunt Activities (where the Hunting skill of the guests affects success chance!). You can also get good knights, commanders, shepherds (good as vassals!), brides, and husbands.  

### New Schemes​

With Herd being the bread and butter of a nomadic ruler, and the main currency, there must be multiple ways to obtain it at will. Landed rulers can increase their taxes, ask their head of faith for gold, and others can trade hooks for gold. But as a ruler of the steppe, you have no such options. So how will you obtain herd outside of normal means? Well, since you cannot embezzle or launder large flocks of animals, the next best thing is to steal!  

![image_66.png](https://forumcontent.paradoxplaza.com/public/1266960/image_66.png "image_66.png")


*[Steal herd scheme window]*  

You’ll be able to choose how much herd to steal, and bigger amounts make the task more difficult. The scheme uses agents, ensuring your thievery is a success.  

![image_67.png](https://forumcontent.paradoxplaza.com/public/1266961/image_67.png "image_67.png")


*[Steal herd scheme sidebar]*  

If you manage to succeed in stealing another ruler’s Herd, there is a small chance of gaining additional outcomes. You can go for more herd, some of the ruler’s gold, his wife, or even a headstart at a murder plot against them! (evil character playthroughs only)  

![image_68.png](https://forumcontent.paradoxplaza.com/public/1266962/image_68.png "image_68.png")


*[Steal herd scheme giga outcome]*  

### New Cultural Traditions​

Before we started working on this expansion, the cultural tradition selection for Nomads was a bit bland. The big three of Horse Lords, Malleable Invaders, and Steppe Tolerance were present for almost all the cultures, meaning there was little difference between Kimeks and Mongols. And since all three were required to have access to Nomad-like flavor and mechanics, further customization was heavily limited. Now, with all the shiny bright new features and content this DLC brings to you, this is no longer the case. The starting cultural traditions have been rearranged, some existing traditions have received new effects and modifiers. And we have new ones as well!  

![image_69.png](https://forumcontent.paradoxplaza.com/public/1266963/image_69.png "image_69.png")


*[Wolves of the Deep Steppe cultural tradition]*  

The strength of the inner steppe. The Mongols start with this tradition, and while all Nomads cultures can get it as well, it is much more expensive for cultures with heritage other than Mongolic. For details on Mangudai men at arms, please keep reading!  

![image_70.png](https://forumcontent.paradoxplaza.com/public/1266964/image_70.png "image_70.png")


*[Iron Cavalry cultural tradition]*  

Where the Steppe warriors meet the ironworking wonders of the settled people. Turkmen and Oghuz cultures have this tradition at the game start.  

![image_71.png](https://forumcontent.paradoxplaza.com/public/1266965/image_71.png "image_71.png")


*[Tribes of the North cultural tradition]*  

This one is a bit different. It is present for the cultures that border the northern end of the ck3 map, the Buryats, Kirghiz, Ostyaks, Oirats, and Permians. Some of those have the Nomadic government like the Buryats, while Ostyaks and Permians are still tribal. Those tribes had a history of defiance while faced with adversaries: heirs of Temujin, ruling over the vast lands, still needed to endeavor a punitive expedition every decade or so to bring the northerners to heel, if only for prestige's sake.  
This tradition can be obtained via hybridization; it is heavily connected to the Siberian Permafrost county modifier. This modifier is placed on the game start to counties up north, and it offers some powerful bonuses while preventing development growth and the creation of a feudal state with stone castles.  

![image_72.png](https://forumcontent.paradoxplaza.com/public/1266966/image_72.png "image_72.png")


*[Siberian Permafrost modifier breakdown. Its effects change if the owner does not have the Tribes of the North modifier]*  

Additionally, we have added new Nomadic effects to some of the existing cultural traditions, to make them a more viable and interesting choice when riding across the Great Steppe. Below you have just a couple of examples.  

![image_73.png](https://forumcontent.paradoxplaza.com/public/1266967/image_73.png "image_73.png")


*[Stalwart Defenders Cultural Tradition unlocks a special Yurt and gives a Toughness bonus to your Nomadic Horde]*  

![image_74.png](https://forumcontent.paradoxplaza.com/public/1266968/image_74.png "image_74.png")


*[Pastoralist Cultural Tradition provides a fertility boost in certain terrains and increases the fertility growth of Herders]*  

### New Men-at-Arms​


Do you ever pop open CK to play as your favorite steppe people (the Kimeks, obviously), flip open your Army tab, and… see that you have pikemen, siege weapons, and some other units that don’t exactly represent the riders of your tribe?!? It was clear what had to be done for nomads’ MaA in this expansion: they needed to be limited from units that are much more emblematic of sedentary armies, and they needed some cool new units of their own.  

So, there you go. If you’re playing a nomad (with no unique MaA through Traditions), your main way to get heavy/light infantry, pikemen, archers and proper siege weapons is through your non-nomadic Tributaries. How exactly this works was outlined in Dev Diary #165.  

But forget about those dorks plodding around in the dust in their soft lil civilized shoes. You don’t need their MaA. As a mighty nomad, you need only - and are supremely skilled as - CAVALRY.  

![image_75.png](https://forumcontent.paradoxplaza.com/public/1266969/image_75.png "image_75.png")


*[The MaA units available to the Khan of Great Liao in 1066.]*  

The main mass of nomadic armies aren’t levies: these are replaced by the less-pathetic Horde Riders, which are converted over from Herd size when armies are raised. Even though they’re, of course, themed after horse archers, they don’t have the Archer Cavalry type, in order to limit the effects of bonuses and counters. Otherwise, these could really get out of hand, given Horde Riders will make up the vast majority of every nomadic army.  

![image_76.png](https://forumcontent.paradoxplaza.com/public/1266970/image_76.png "image_76.png")



All nomads have access to classic, basic Horse Archers. They’re largely unchanged.  

![image_77.png](https://forumcontent.paradoxplaza.com/public/1266971/image_77.png "image_77.png")



Steppe Raiders are nomadic light cavalry which are better-suited to dry and rough terrain than other nomadic cavalry units, receiving only mild penalties in hills, mountains and wetlands. They’re also available to all nomads.  

![image_78.png](https://forumcontent.paradoxplaza.com/public/1266972/image_78.png "image_78.png")



Nomadic rulers won’t have direct access to real, substantially effective siege weapons. Until they can get a sweet tributary connection to hook them up, they make do with Torch-Bearers. Even worse than onagers, at least this standard nomad siege unit gets a siege bonus against nomadic holdings.  

![image_79.png](https://forumcontent.paradoxplaza.com/public/1266973/image_79.png "image_79.png")



Only unlocked by building the Square of the Tumen domicile building, Heavy Horse Archers are a more costly alternative with more fighting punch, and a very handy counter against light cavalry (also, elephants). To counterbalance this, they suffer more penalties in harsh terrains.  

![image_80.png](https://forumcontent.paradoxplaza.com/public/1266974/image_80.png "image_80.png")



The second level of Dominance allows Nomad Lancers to be recruited. What this means is nomadic rulers of means have access to heavy cavalry, even right at the 867 game start.  

![image_81.png](https://forumcontent.paradoxplaza.com/public/1266975/image_81.png "image_81.png")



The Mongol tradition ‘Wolves of the Deep Steppe’ gives them access to the Mangudai. These vainglorious warriors have very high attack and pursuit, but low defence, meaning that they devastate defeated armies and leave few survivors. Their reckless attack and repeated retreats excel at breaking up formations, allowing armies with Mangudai to counter heavy infantry and spearmen.  

![image_82.png](https://forumcontent.paradoxplaza.com/public/1266976/image_82.png "image_82.png")



Inspired by the Tangut Iron Harriers and the Mamelukes, this unit is available to a spread of cultures that were known for their employment of heavily armored horse archers. Note, however, that the unit's type is Heavy Cavalry and not Archer Cavalry: this allows Cataphract Archers to counter Archer Cavalry, and be one of the best ways to fight back against steppe conquerors.  

![image_83.png](https://forumcontent.paradoxplaza.com/public/1266977/image_83.png "image_83.png")



That’s not a panini press on his chest. That’s armor. The Maturkan Warriors represent foot archers from all along the northern Siberian frontier, drawing particular inspiration from the noble Khanty warriors which lent the unit its name.  

![image_84.png](https://forumcontent.paradoxplaza.com/public/1266978/image_84.png "image_84.png")



The glorious guard of Genghis himself can be yours, should you make it far enough down the new nomadic Dynasty Legacy. You’re limited to hiring just one regiment of this special unlock, but increase that regiment in size and you’ll see it packs quite the punch.  

![image_85.png](https://forumcontent.paradoxplaza.com/public/1266979/image_85.png "image_85.png")



---

And with that we reach almost the end of our Development Diaries dedicated to *Khans of the Steppe*! We will go over the modding support, art and music in the future, but this is our last feature spotlight. Thank you for reading – go forth, and conquer!

<!-- artifact:reactions:start -->
- 101 Like
- 54 Love
- 10 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
- 1 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
