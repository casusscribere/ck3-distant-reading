---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1480529/"
forum_thread_id: 1480529
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 65
title: "CK3 Dev Diary #65 - One Culture Is Not Enough"
dd_date: 2021-06-22
author_handle: Servancour
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3943
inline_image_count: 11
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1480529'
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
    location: raw_lines_~28_to_123
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_125_to_126
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_446_to_448
    action: preserved_and_flagged
    counts:
      Like: 42
      Love: 7
      (unlabeled — rendered as base64 data URI): 2
    note: Reactions block parsed; 2 of 3 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_458_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #65 - One Culture Is Not Enough

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Jun 22, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/ "CK3 Dev Diary #64 - Cultures Are Forever") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-66-a-fresh-coat-of-paint.1481298/ "CK3 Dev Diary #66 - A Fresh Coat of Paint")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/?prdxDevPosts=1)

[Threadmarks](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/threadmarks "Threadmarks")

[View all 1 threadmarks](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/threadmarks)

---
[Reader mode](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/reader/)

---


#### Recent threadmarks

[1624363200,1624363200](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/#post-27634815 "Threadmark created by NicouLenny on Jun 22, 2021")

[Reader mode](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/reader/)

- [Jun 22, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/post-27634550)
- [Replies: 562](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/#posts)


- [/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/post-27634550](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/post-27634550)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27634550/bookmark "Bookmark")

### **CK3 Dev Diary #65 - One Culture Is Not Enough**​

Hello everyone!  

Last week we had a rundown of what a culture looks like in the upcoming overhaul. This time around, let’s have a closer look at how you go about creating your own culture! There are two different ways of doing so, forming a hybrid culture and diverging your culture. Both are slightly different in their approach and in what they allow you to do with your new culture.  

Now, while the cultural overhaul is a free feature that will accompany the Royal Court expansion, the ability to create a hybrid or divergent culture will require you to own the DLC.  

Before we start, culture creation is quite dependent on the new cultural overhaul, so if you have yet to read [last week's DD](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/), I suggest you give it a read for context. Also, keep in mind that everything shown in screenshots is still a work in progress!  

Form a Hybrid Culture  
Forming a hybrid culture is a way for you to meld the aspects of your current culture with that of another, in any way you so choose.  

There are a few restrictions you’ll have to keep in mind before you are able to form a hybrid. First, the culture you want to form a hybrid with has to be present within your realm. No weird hybridization with cultures on the other side of the world please. Secondly, you’ll need a certain amount of cultural acceptance. You cannot go in and conquer an area to only create a new culture immediately, but the required amount can vary depending on your current traditions. And finally, you cannot hybridize with a culture of the same heritage as you. The reasoning here is that the two cultures have to be different enough to warrant them being combined into a single culture, rather than just assimilating one in favour of the other.  

Once you are able to form a hybrid culture, you’ll need to come up with a good name for it. We pick a default name that is a combination of the two cultures you are attempting to hybridize, such as “Andaluso-French”, or “Greco-Persian”. For added immersion and flavour, however, we have a set of names that can appear depending on which cultures you hybridize, or where you are creating your new culture. For example, hybridizing a culture of a Frankish heritage with one of a central germanic heritage in the area in and surrounding Lotharingia, you can have a culture named Rhinelander. You are, of course, free to name your new culture whatever you want as well!  

Starting with the pillars. You can freely pick between the two cultures' pillars, mixing ethos, heritage, language, and martial custom as you’d like. For example, you could pick the heritage from culture A, but language from culture B. One caveat is that you have to pick at least one pillar from each culture. It isn’t much of a hybrid otherwise, is it?  

![01_hybrid_pillars.jpg](https://forumcontent.paradoxplaza.com/public/721159/01_hybrid_pillars.jpg "01_hybrid_pillars.jpg")


*[Image of pillar selection when forming a hybrid culture]*​


The same principle applies to traditions. You can pick and choose which traditions you want to keep, from either culture, as long as you don’t go above the slot limit. You can even choose to only pick a few traditions, leaving slots empty and give room for future traditions that you may want to adopt later. Some traditions are unique to certain cultures, regions, or heritages however, so this is the only chance you might have to acquire traditions that normally would be out of your reach.  

![02_hybrid_traditions.jpg](https://forumcontent.paradoxplaza.com/public/721160/02_hybrid_traditions.jpg "02_hybrid_traditions.jpg")


*[Image of tradition selection when forming a hybrid culture]*​


Aesthetics work in the same way. You are free to pick and choose all of the subcomponents from either culture. For some of the categories, you are even able to choose a “hybrid” option, using the preset from both cultures! The hybrid option exists for names, fashion, and CoAs. Are you hybridizing a culture from East Africa with an Indian culture? Perhaps you’d like to go for the Indian unit, hybrid naming, Indian architecture, African fashion, and finally hybrid CoAs. Actual combination is entirely up to you!  

![03_hybrid_aesthetics_1.jpg](https://forumcontent.paradoxplaza.com/public/721161/03_hybrid_aesthetics_1.jpg "03_hybrid_aesthetics_1.jpg")


*[Image of Military Equipment, Naming Practices, and Architecture when forming a hybrid culture]*  

![04_hybrid_aesthetics_2.jpg](https://forumcontent.paradoxplaza.com/public/721162/04_hybrid_aesthetics_2.jpg "04_hybrid_aesthetics_2.jpg")


*[Image of Fashion and Coats of Arms when forming a hybrid culture]*​


The new hybrid culture will automatically acquire any innovation that either parent culture has discovered already, giving you the possibility to gain access to innovations that your previous culture has yet to discover.  

Before we move on, there’s a prestige cost to forming a hybrid culture. Normally, creation isn’t very expensive, and relies more on having enough cultural acceptance for it to be valid. A high acceptance will reduce the cost though, making it fairly cheap if you have managed to greatly increase acceptance.  

The initial size of a hybrid culture on the map also depends on the acceptance you’ve built up between the two cultures. If you decide to hybridize at the lowest required acceptance level, the hybrid will start out rather small. Rulers of hybrid cultures have a much easier time using the ‘Promote Culture’ council task in counties belonging to either of its parent cultures for a set amount of years after it has been formed.  

Diverge Your Culture  
A divergent culture is essentially a culture that deviates from their original culture, allowing you the opportunity to shape it as you see fit.  

Similar to forming a hybrid, you get to choose a name for your new culture. The default name here on the other hand, depends on your primary title. Diverging a culture as the king of Anatolia can give you an Anatolian culture, or Austrian if you are the duke of Austria. This makes sure that divergent cultures always have a sensible name to them. At least most of the time. I did see a Wormsian culture in a recent observer game, from the county of Worms. As with hybridization, you are free to name it however you want if you don’t want to use the default name.  

As for the pillars, options are slightly different. You can pick and choose any ethos. Language won’t have any additional options for you most of the time. Martial custom can be changed as long as you fulfill the conditions for them, which would include things such as having a corresponding succession law. Aesthetics will also rarely have additional options, except in some historical cases. Diverging from Norse in Sweden, for example, will give you access to Swedish Aesthetics.  

You have to change at least one pillar in order to diverge your culture. Most of the time you won’t have a lot of valid alternatives for the additional pillars, so your only option will be to change your ethos.  

![05_diverge_pillars.jpg](https://forumcontent.paradoxplaza.com/public/721163/05_diverge_pillars.jpg "05_diverge_pillars.jpg")


*[Image of pillars when diverging from an existing culture]*​


Traditions can be replaced with something new, as long as you are able to afford the tradition cost. Unlike hybridization, you will have plenty of options, and can replace a tradition with any other tradition that your culture fulfills the requirements of.  

![06_diverge_traditions.jpg](https://forumcontent.paradoxplaza.com/public/721164/06_diverge_traditions.jpg "06_diverge_traditions.jpg")


*[Image of traditions when creating a divergent culture]*​


Diverging also costs prestige. Here the cost scales on how much of your own culture you control. Attempting to diverge Greek as Byzantium will be fairly expensive. Meanwhile, attempting to diverge a small part of your culture, such as a small Andalusian emir on the Iberian peninsula will be significantly cheaper.  

Dynamic Culture Emergence  
The above options describe how you as a player will be able to create new cultures, that doesn't mean that cultures won’t also appear dynamically. Over the course of a campaign, cultures may diverge depending on their situation.  

For dynamic Divergent cultures we decided that we wanted them to feel immersive and logical whenever they showed up. There are many factors that go into this, such as the culture size, if the culture is ‘united’ under strong rulers, etc. Divergent cultures will appear either in border regions where a culture meets another (or several others), or in island regions. Divergences also do not appear in the capital lands of the Culture Head, in order to safeguard what is most likely the ‘heartland’ of the culture.  
For example, one of the cultures that usually Diverge a few times (1066) is the Bedouin culture. It’s large, spread out, and some of its lands are under rulers that are not Bedouin themselves. On the other hand we have Greek; a large culture, but with practically all counties of its culture united under one ruler - they tend to not diverge unless territories go independent.  

Hybridization, on the other hand, is something powerful rulers strive towards! If a ruler finds themselves ruling a large swathe of land of a foreign culture while at the same time having no motivation to assimilate, they’ll try and increase Cultural Acceptance until they’re eligible for Hybridization. They tend to want to hybridize with large cultures in their realm, the prime example being the Oghuz Seljuks wanting to Hybridize with Persian above all other cultures they have in their realm. Some AI rulers do not pursue hybridization though, such as large Elective realms (HRE) where cultures take turns being the top ruler, or realms such as the Papacy.  

By default, the AI will not create hybrids-of-hybrids (unless historical hybrids, such as Maghrebi or English), as the naming schemes can quickly go out of hand. Though if you’d like the AI to do this, there’s a game rule you can enable...  

There’s also a small chance that hybrids appear in realms of not so powerful rulers, this allows interesting hybrids such as Hiberno-Norse to appear even from tiny realms. This happens through an event that can also occur for the player. These events will most often happen for Cultures that have certain traditions that allow them to more easily create Hybrids with other cultures.  

Naturally there’s a host of Game Rules that allow you to customize your experience. Do you want no Divergent or Hybrid cultures to appear at all? Set their frequencies to none. Do you want the AI to create hybrids of hybrids of hybrids of hybrids? Set the Hybrid Culture Restrictions to Very Relaxed!  

![07_game_rules.jpg](https://forumcontent.paradoxplaza.com/public/721165/07_game_rules.jpg "07_game_rules.jpg")


*[Image of the new culture Game Rules]*​


To round things off, let’s take a look at a few examples of what the AI did during an observer game. First up, from the 867 start, and 200 years in. You’ll see quite a few new cultures here:  


- Ango-Norse, Hybrid Culture, emerged in 918.
- Cumbro-Norse, Hybrid Culture, formed in 948.
- Norse-Gael, Hybrid Culture, emerged in 1029.
- You can also see that English has largely replaced Anglo-Saxon as the dominant culture in England.


![08_cultures_in_britain.jpg](https://forumcontent.paradoxplaza.com/public/721166/08_cultures_in_britain.jpg "08_cultures_in_britain.jpg")


*[Image of AI created cultures on the British islands]*​


Started in 867, and 100 years into the game:  


- Kufan, Bedouin Divergence, emerged in 933.
- Badarayani, Mashriqi Divergence, emerged in 956.
- Kurdo-Mashriqi, Hybrid Culture, emerged in 911.
- Nihawandi, Persian Divergence, emerged in 907.
- Shirvani, Persian Divergence, emerged in 946.


![09_cultures_in_persia.jpg](https://forumcontent.paradoxplaza.com/public/721167/09_cultures_in_persia.jpg "09_cultures_in_persia.jpg")


*[Image of AI created cultures in and around Persia]*​


In another game, started in 1066, a Swedish noblewoman was made queen in the newly established Kingdom of Jerusalem, following a successful crusade. After a few generations, the local cultures merged into what would become Mashriqi-Swedish! Ushering the kingdom into a new era of prosperity.  

![10_mashriqi_swedish_jerusalem.jpg](https://forumcontent.paradoxplaza.com/public/721168/10_mashriqi_swedish_jerusalem.jpg "10_mashriqi_swedish_jerusalem.jpg")


*[Image of the Kingdom of Jerusalem becoming Mashriqi-Swedish]*  

![11_mashriqi_swedish_culture.jpg](https://forumcontent.paradoxplaza.com/public/721169/11_mashriqi_swedish_culture.jpg "11_mashriqi_swedish_culture.jpg")


*[Image of the culture window of Mashriqi-Swedish]*​


As mentioned earlier, we have a number of historical names for cultures that can appear in specific circumstances. If you have any cultural names that would make sense for a divergent or hybrid culture, let me know! Who knows? Perhaps your suggestion ends up in the game!  

That's it for this time!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27634550/report)

Click to expand...

[![Servancour](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/obsolete/m/Pdx_dev_forum_avatar.png)](https://forum.paradoxplaza.com/forum/members/servancour.465268/)

Written by

### [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)

Game Designer

***Paradox Staff******4 Badges***

-

Messages
1.606

-

Reaction score
9.949

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [29](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/page-29#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/page-2#posts)

1 of 29

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/page-29#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/?order=prdx_dd_reaction_score)

Threadmarks

 1624363200,1624363200

- [Index](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/threadmarks)

[![NicouLenny](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/avatars/MagickaWizardWars/s/MWW Avatar (43).png)](https://forum.paradoxplaza.com/forum/members/nicoulenny.1478317/)

#### [NicouLenny](https://forum.paradoxplaza.com/forum/members/nicoulenny.1478317/)

##### Captain

**39 Badges**

Oct 22, 2019

459

3.074

- ![Surviving Mars: First Colony Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/greenplanet.png "Surviving Mars: First Colony Edition")
- ![Crusader Kings II: Jade Dragon](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2jd_forumicon.png "Crusader Kings II: Jade Dragon")
- ![Stellaris: Humanoids Species Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/humanoid_forumicon.png "Stellaris: Humanoids Species Pack")
- ![Stellaris: Apocalypse](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/apocalypse_forum_icon2.png "Stellaris: Apocalypse")
- ![Stellaris: Distant Stars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Distantstars.png "Stellaris: Distant Stars")
- ![Surviving Mars: First Colony Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SpaceRace.png "Surviving Mars: First Colony Edition")
- ![Stellaris: Megacorp](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/MegaCorp-ForumIcon.png "Stellaris: Megacorp")
- ![Crusader Kings II: Holy Fury](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/holy_fury_nonPO.png "Crusader Kings II: Holy Fury")
- ![Prison Architect](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Prisonicon.png "Prison Architect")
- ![Surviving Mars](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/SuMa_standard.png "Surviving Mars")
- ![Stellaris: Ancient Relics](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellarisrelics.png "Stellaris: Ancient Relics")
- ![Age of Wonders: Planetfall](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/aowstandard.png "Age of Wonders: Planetfall")
- ![Stellaris: Lithoids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/lithoids_forum_badge.png "Stellaris: Lithoids")
- ![Stellaris: Federations](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/FederationsIcon.png "Stellaris: Federations")
- ![Crusader Kings III](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3.png "Crusader Kings III")
- ![Crusader Kings III: Royal Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck3-royal.png "Crusader Kings III: Royal Edition")
- ![Stellaris: Necroids](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_necroids.png "Stellaris: Necroids")
- ![Stellaris: Nemesis](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/nemesis.png "Stellaris: Nemesis")
- ![Stellaris: Leviathans Story Pack](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/leviathans.png "Stellaris: Leviathans Story Pack")
- ![Stellaris: Digital Anniversary Edition](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/plantoid.png "Stellaris: Digital Anniversary Edition")
- ![Stellaris](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/stellaris_forumicon_base.png "Stellaris")
- ![Crusader Kings II: Conclave](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/DLC_icon_Conclave.png "Crusader Kings II: Conclave")
- ![Crusader Kings II: Horse Lords](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/horse_lords_medal.png "Crusader Kings II: Horse Lords")
- ![Crusader Kings II: Way of Life](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_way_of_life_forumicon.png "Crusader Kings II: Way of Life")
- ![Mount &amp; Blade: With Fire and Sword](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/WFAS.png "Mount &amp; Blade: With Fire and Sword")
- ![Stellaris - Path to Destruction bundle](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Utopia.png "Stellaris - Path to Destruction bundle")
- ![War of the Roses](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/wotr_icon.png "War of the Roses")
- ![Magicka](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/magickaIcon.png "Magicka")
- ![Imperator: Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Imperatorstandardicon.png "Imperator: Rome")
- ![Crusader Kings II: Charlemagne](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_charlemagne_forumicon.png "Crusader Kings II: Charlemagne")
- ![Crusader Kings II: Legacy of Rome](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_legacy_of_rome_forumicon.png "Crusader Kings II: Legacy of Rome")
- ![Crusader Kings II: The Old Gods](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_old_gods_forumicon.png "Crusader Kings II: The Old Gods")
- ![Crusader Kings II: Rajas of India](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_rajas_of_india_forumicon.png "Crusader Kings II: Rajas of India")
- ![Crusader Kings II: The Republic](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_the_republics_forumicon.png "Crusader Kings II: The Republic")
- ![Crusader Kings II: Sons of Abraham](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sons_of_abraham_forumicon.png "Crusader Kings II: Sons of Abraham")
- ![Crusader Kings II: Sunset Invasion](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sunset_invasion_forumicon.png "Crusader Kings II: Sunset Invasion")
- ![Crusader Kings II: Sword of Islam](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_sword_of_islam_forumicon.png "Crusader Kings II: Sword of Islam")
- ![Stellaris: Synthetic Dawn](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/Syn_dawn_forum_icon.png "Stellaris: Synthetic Dawn")
- ![Crusader Kings II](https://forum.paradoxplaza.com/forum/styles/paradox/owneditems/icons/ck2_forumicon.png "Crusader Kings II")

[](javascript:;)

- [Jun 22, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/post-27634815)


- [/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/post-27634815](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/post-27634815)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27634815/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/post-27634815)

Also note that we have released [**Hotfix 1.4.2**](https://forum.paradoxplaza.com/forum/threads/releasing-1-4-2-azure.1480520/) this morning, fixing multiple issues that came with the 1.4.0 "Azure" Patch.  
We thank you for your patience! ![:D](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Big Grin    :D")

 

Toggle signature

**Ex-Community Ambassador for Crusader Kings III  
►** *[Twitter Nicou](https://twitter.com/NicouLenny)*

<!-- artifact:reactions:start -->
- 42 Like
- 7 Love
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->
