---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1479565/"
forum_thread_id: 1479565
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 64
title: "CK3 Dev Diary #64 - Cultures Are Forever"
dd_date: 2021-06-15
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
body_word_count: 3722
inline_image_count: 10
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1479565'
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
    location: raw_lines_436_to_437
    action: preserved_and_flagged
    counts:
      Like: 16
      Love: 1
    note: Reactions block parsed; 2 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: replies
    location: raw_line_447_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #64 - Cultures Are Forever

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Jun 15, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22939](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-63-1-4-0-azure-patch-notes.1478364/ "CK3 Dev Diary #63 - 1.4.0 “Azure” Patch Notes") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-65-one-culture-is-not-enough.1480529/ "CK3 Dev Diary #65 - One Culture Is Not Enough")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/?prdxDevPosts=1)

[Threadmarks](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/threadmarks "Threadmarks")

[View all 1 threadmarks](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/threadmarks)

---
[Reader mode](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/reader/)

---


#### Recent threadmarks

[1623760212,1623760211](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/#post-27618669 "Threadmark created by NicouLenny on Jun 15, 2021")

[Reader mode](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/reader/)

- [Jun 15, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/post-27618275)
- [Replies: 371](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/#posts)


- [/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/post-27618275](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/post-27618275)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27618275/bookmark "Bookmark")

CK3 Dev Diary #64 - Cultures Are Forever​

Salutations!  

Before we begin, first things first. We are working on an additional patch to fix some of the [issues introduced in 1.4](https://forum.paradoxplaza.com/forum/threads/currently-known-issues-updated-for-1-4-0.1436893/). The patch is still being worked on, but if everything goes as planned, we should be able to get it out sometime next week or so. We’ll let you know once the patch is ready.  

With that out of the way, let’s talk about something I’m quite excited to share with you all. As you probably know already, we’ve talked a bit about how we are revisiting cultures for the next expansion: Royal Court. Unlike faiths, which got a lot of attention prior to release as we made them quite dynamic and customizable, cultures can feel a bit static, and aren't anywhere near as interesting as faiths. That is all about to change!  

We are revising cultures as you know them. Most exciting is perhaps the possibility to create new cultures! Both for simulating historical events and to create plausible and interesting alt-history scenarios. But I’m getting ahead of myself. For now, let’s start by looking at the foundation of a culture and the different components they are made of. This is what the new culture screen will look like.  

![01_culture_window.jpg](https://forumcontent.paradoxplaza.com/public/719275/01_culture_window.jpg "01_culture_window.jpg")


*[Image of the new and updated culture interface]*​


## **Cultural Pillars**​

A culture has five main Cultural Pillars. These are Ethos, Heritage, Language, Martial Custom, and finally Aesthetics. Of these, the Ethos is perhaps the most significant, but all of them play a particular role in how a culture plays and how cultures view each other.  

**Ethos**  
Each ethos is framed around a particular theme that somehow ties into a fairly broad definition of what a culture is. A culture’s ethos not only provides effects and bonuses for having it, it also ties into how easy or difficult it is to acquire certain traditions (more on this further down). There are seven in total:  


- Bellicose
- Communal
- Courtly
- Egalitarian
- Inventive
- Spiritual
- Stoic

Here are a few examples of what they may look like in-game:  

![02_ethos_bellicose.jpg](https://forumcontent.paradoxplaza.com/public/719276/02_ethos_bellicose.jpg "02_ethos_bellicose.jpg")


*[Image of the Bellicose ethos]*  

![03_ethos_spiritual.jpg](https://forumcontent.paradoxplaza.com/public/719277/03_ethos_spiritual.jpg "03_ethos_spiritual.jpg")


*[Image of the Spiritual ethos]*  

![04_ethos_inventive.jpg](https://forumcontent.paradoxplaza.com/public/719278/04_ethos_inventive.jpg "04_ethos_inventive.jpg")


*[Image of the Inventive ethos]*​


**Heritage**  
A culture's heritage can be compared to the culture groups that you may be used to in the existing system. Heritages will roughly match said culture groups. You’ll see an Iberian Heritage for cultures like Basque and Castilian, or Turkic Heritage for Turkic cultures, such as Oghuz and Cuman. In terms of gameplay, the most outstanding effect of a shared heritage is the impact it has on Cultural Acceptance.  

**Language**  
Each culture has a designated language. Languages vary greatly across the map and between cultures. Some languages, such as Arabic, are spoken by quite a few cultures. Other languages are spoken by no more than two or three cultures, or in some cases, cultures even have their own unique language. An example of these would be Basque, who really don't have any closely related languages and it wouldn’t make too much sense to group them together with their neighbors. The vast majority of cultures share a language though, as a sort of “language group” rather than a specific language.  

Characters can always speak the associated language of their culture. They are, however, also able to learn multiple languages over their lifetime. Knowing multiple languages has its benefits, as speaking the same language as another character of a different culture, and county, will reduce the opinion penalty that character, or county, has towards you. Knowing the native language (i.e. the language of their culture) of your vassals is therefore fairly beneficial as a means of increasing their opinion of you.  

**Noble Martial Custom**  
The martial custom decides which gender you may appoint as knights and commanders. As you’d expect, you can either appoint men, women, or both. We always felt that having the gender doctrine on faiths decide which characters can and cannot participate in battles felt off. The doctrine is about the right to rule and the holding of titles, more so than anything else. Just because you want the Equal doctrine to allow female rulers, doesn’t mean that women would automatically lead your armies or join you as knights. Revising cultures gave us the ample opportunity to move the functionality from faiths over to cultures. Which also means that you’ll have additional options in shaping your realm.  

**Aesthetics**  
This pillar is really a collection of several smaller properties for what a culture “looks” like. It decides what type of clothes characters wear, the coat of arms style for dynasties, what architecture holdings use, and the type of armor the units on the map wear.  

This is also the pillar that contains what naming practices the culture uses. Mainly what character names to use, if they use a dynasty prefix, etc. The naming practice will also be used to change title and holding names, which used to be set per culture, so as to not have titles change names if you create a new culture.  

For all of you modders out there; all of these can be set individually per culture. Allowing you to mix and match the different aesthetics to your heart’s content.  

## **Traditions**​

Traditions are the meat of the cultural overhaul, and provide that extra layer of variety and immersion that can have a significant impact on gameplay. An important aspect of traditions is that they give us a clear means of visualizing and explaining existing mechanics that previously just “was a thing” and never explained. Take Anglo-Saxon as an example. They have access to the Saxon Elective succession for no apparent reason other than “they do”. Instead, they now have a tradition that grants them the succession law, making it clear as to why they have it. Secondly, and perhaps more importantly, traditions serve as the perfect means of giving a culture additional flavour or gameplay bonuses that add a greater degree of variety across the map.  

A culture can have no more than five traditions in total, but this number will increase as you enter a new era. Most cultures will start the game with around three or four, which leaves plenty of room for you to shape your culture as you play the game. As the cultural head, you’ll have the ability to establish new traditions.  

Not all traditions will be available everywhere. We have both regional traditions, as well as traditions that are available depending on your heritage. The vast majority of them can be established regardless of circumstances, but might require certain conditions, such as ‘Hill Dwellers’ having the requirement that your culture must be present in a county with hills.  

Traditions cost prestige to adopt. Which will be the largest hurdle for you to overcome if you want a specific tradition. The prestige cost is dependent on your ethos. Certain traditions will be more expensive than others, if you don’t have a matching ethos. Similarly, a tradition will increase in cost if your culture, or in some cases the cultural head, doesn’t fulfill a specific and thematic requirement. An example would be a tradition named ‘Only the Strong’, which is more expensive if you as the cultural head don't have at least six knights with at least 12 prowess. The increased cost is meant to act as a softer limit and make it slightly more difficult to establish certain traditions (depending on your circumstances), but not as much as to make it impossible to do so, should you want to go and unlock a particular tradition.  

Instead of explaining traditions in detail, I’ll just show you a few examples of what traditions may look like, as well as the type of effects you can expect from them.  

![05_tradition_swordsforhire.jpg](https://forumcontent.paradoxplaza.com/public/719279/05_tradition_swordsforhire.jpg "05_tradition_swordsforhire.jpg")


*[Image of the Swords for Hire tradition]*  

![06_tradition_chivalry.jpg](https://forumcontent.paradoxplaza.com/public/719280/06_tradition_chivalry.jpg "06_tradition_chivalry.jpg")


*[Image of the Chivalry tradition]*  

![07_tradition_esteemedhospitality.jpg](https://forumcontent.paradoxplaza.com/public/719281/07_tradition_esteemedhospitality.jpg "07_tradition_esteemedhospitality.jpg")


*[Image of the Esteemed Hospitality tradition]*  

![08_tradition_seafarers.jpg](https://forumcontent.paradoxplaza.com/public/719282/08_tradition_seafarers.jpg "08_tradition_seafarers.jpg")


*[Image of the Seafarers tradition]*  

![09_tradition_landofthebow.jpg](https://forumcontent.paradoxplaza.com/public/719283/09_tradition_landofthebow.jpg "09_tradition_landofthebow.jpg")


*[Image of the Land of the Bow tradition]*​


## **Cultural Acceptance**​

Cultural acceptance can be described as how well intermingled two cultures are, and how accepting they are of each other. Which means that given enough time, cultures will dislike each other less, and culture converting everything within your realm is no longer the only solution to combat cultural differences.  

The opinion penalty of being of a different culture used to be a static value. Now, it will depend on the cultural acceptance between your culture and the target culture. Each culture has an acceptance value of another culture, visualized as a percentage. Depending on the amount of acceptance, the “different culture” opinion penalty will gradually be reduced. At 0% acceptance, you’ll have the full opinion penalty. At 100%, the penalty is removed altogether. Acceptance goes both ways. So if the French have a 20% acceptance towards Normans, the same will be true from the Norman perspective.  

There are two ways for acceptance to change. The first is an acceptance baseline. Which increases if two cultures share similarities with one another. There are a number of different modifiers that can increase the baseline. Such as cultures that share the same religion or faith, ethos, or language. The most impactful modifier, however, is heritage. If two cultures share the same heritage, they have a significant bonus to their baseline.  

If acceptance is above the baseline, it will slowly decay over time towards the targeted value. Being below the baseline on the other hand, will not make the acceptance increase. A bad relation between cultures won’t disappear overnight.  

Secondly, acceptance very much changes depending on the circumstances. Don’t expect two cultures that never interact with one another to gain acceptance. If cultures exist within the same realm though, it will increase over time. This applies to both counties of another culture within your realm, as well as vassals. Acceptance is also reactive. Taking certain actions towards characters of a different culture will have consequences on your acceptance, such as declaring war or revoking titles. This generally scales on size. While the difference isn’t huge, revoking a single county from a small culture will decrease your acceptance more than if you would revoke a county from a much larger culture. At the end of the day, if you want to maintain a high acceptance and keep your Occitan vassals in France happy, you are at least gonna have to try and be nice to them.  

![10_cultural_acceptance.jpg](https://forumcontent.paradoxplaza.com/public/719284/10_cultural_acceptance.jpg "10_cultural_acceptance.jpg")


*[Image of what the cultural acceptance between two cultures may look like]*​


There we go. That’s what a culture will look like in the near future. Oh! Before I forget; Best of all? The cultural rework is free, and will accompany the free update that launches alongside the Royal Court expansion!  

Until next time!

 

[Reply](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/add-reply "Reply, quoting this message")

[Report](https://forum.paradoxplaza.com/forum/posts/27618275/report)

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

- [1](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/)
- [2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/page-2#posts)
- [3](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/page-3#posts)
- …
  
  #### Go to page
  
  Go

- [19](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/page-19#posts)
[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/page-2#posts)

1 of 19

#### Go to page

Go

[Next](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/page-2#posts) [Last](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/page-19#posts "Last")

[Sort by date](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/) [Sort by reaction score](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/?order=prdx_dd_reaction_score)

Threadmarks

 1623760212,1623760211

- [Index](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/threadmarks)

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

- [Jun 15, 2021](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/post-27618669)


- [/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/post-27618669](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/post-27618669)
- [Add bookmark](https://forum.paradoxplaza.com/forum/posts/27618669/bookmark "Bookmark")
- [#2](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-64-cultures-are-forever.1479565/post-27618669)

Hey everyone,  

If you missed the recent information about our next expansion, have a look at our [**FAQ Royal Court**](https://forum.paradoxplaza.com/forum/threads/ck3-royal-court-faq-developer-diaries-q-a-important-information.1475394/)!  
General questions, Dev Diaries, Videos & Trailer, Press & Articles Previews.  

As always, thanks for reading our news; Feel free to drop your questions to our development team ![:D](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Big Grin    :D")  

Cheers,

 

Toggle signature

**Ex-Community Ambassador for Crusader Kings III  
►** *[Twitter Nicou](https://twitter.com/NicouLenny)*

- 25

<!-- artifact:reactions:start -->
- 16 Like
- 1 Love
<!-- artifact:reactions:end -->
