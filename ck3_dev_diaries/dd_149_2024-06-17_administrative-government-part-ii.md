---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1688808/"
forum_thread_id: 1688808
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 149
title: "Dev Diary #149 - Administrative Government (Part II)"
dd_date: 2024-06-17
author_handle: Servancour
expansion: Roads to Power
patch: Patch 1.13
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 5971
inline_image_count: 28
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1688808'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3131.jpg?1718707094
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_497_to_501
    action: preserved_and_flagged
    counts:
      Like: 166
      Love: 109
      (unlabeled — rendered as base64 data URI): 5
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_509_to_623
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_624_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3131.jpg?1718707094)
<!-- artifact:thread_banner:end -->

# Dev Diary #149 - Administrative Government (Part II)

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Jun 17, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-149-administrative-government-part-ii.1688808/)
<!-- artifact:thread_metadata:end -->

Salutations! Welcome back as we take another look at all things Byzantium and how our new government, Administrative, works. If you haven’t already, I highly recommend that you first go and read up on [our previous Dev Diary and Part 1, posted last week.](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-148-administrative-government-part-i.1687086/)  

As with last week, please keep in mind the following:  


- All of the included screenshots show a **work in progress** and do not necessarily represent the final product, as we are still heavily at work on the expansion itself.
- This is especially true when it comes to several aspects of the UI, such as **layouts and visuals**. We believe that showing what we have right now, even if not final, gives you a much better idea of what you can expect.
- All **values and numbers** in these screenshots are subject to **balancing** and will likely change before release.

Without further ado, let’s begin with a deeper look into governors!  

---


### Governors​

Governors are the foundation of an Administrative realm. In order to make it easy to both see and inspect all of the governors, we present an overview of the realm in a new interface dedicated to all things revolving around the Administrative Government type. Here you can see who the different governors are, how good they are, which noble family they belong to, and their current line of succession. We want you to be able to get an at-a-glance view of not just the realm at large, but what themes you could potentially attempt to get your hands on and which themes your own noble family already controls. As a vassal, you will even have quick access to some common actions you may take towards the emperor.  

![image-01.jpg](https://forumcontent.paradoxplaza.com/public/1140041/image-01.jpg "image-01.jpg")


*[The administrative UI, showing the theme of Armeniac.]*  

The first objective of any landless noble is to try and make themselves a governor, as this is one of the best ways to gain further Influence. Governors are the backbone of any Administrative realm, and they have a significant impact on how well the realm performs, which is of key importance to the Emperor in particular.  

Any Administrative vassal who holds land alongside a duchy (other than their family title) or kingdom becomes what we refer to as governors. When a character becomes a governor for the first time, they also get the Governor trait. At first, this trait doesn’t offer much value. As you gain trait experience and level it up, however, it starts providing some significant bonuses; especially in regard to the amount of Influence you’ll get, making the trait a great source of Influence gain if you can get it to those higher levels. The rank of the trait can be seen as their overall experience as a governor, and the trait will level up as you perform your duties, handsomely rewarding you for your service towards the empire.  

![image-02.jpg](https://forumcontent.paradoxplaza.com/public/1140042/image-02.jpg "image-02.jpg")


*[The governor trait at the first level.]*  

![image-03.jpg](https://forumcontent.paradoxplaza.com/public/1140043/image-03.jpg "image-03.jpg")


*[The governor trait at the highest level.]*  

Unlike vassals of other government types, Administrative governors will normally only hold a single governorship at a time. This limit exists for two reasons.  

The first is regarding immersion and logic. If you are appointed as a governor of a province somewhere, you wouldn’t also be appointed to a different province somewhere else. If you were, you would take up your new position and be replaced as governor for your initial province by someone else.  

Secondly, we want to encourage the use of family members to a much larger extent for Administrative governments. Once you have secured a governorship for yourself, you’ll have to start making use of your family. Having family members in high places allows for a wider-spreading web of influence. Given that there is a cap on influence investments (which we discuss below), the more family members you have to spend influence supporting your candidates, the more powerful your family may become.  

Another limitation is that potential governors always have to be adults. Being a governor is much more a job than inheriting a regular title. If you happen to find yourself in a situation where you don’t have any adult children, you would go back to being a landless noble.  

### Appointment Succession​

Admin realms use a new form of succession called Appointment. In its basic form, every character that is defined as eligible for a title is given a candidate score, which is based on a scripted value. Some characters are not added to the succession list by default but are only added after having received an investment by another character in the realm.  

Since Administrative government is primarily modeled on Byzantium, we have created two different forms of this new succession type: Appointment for Governors and Acclamation for the Emperor. The primary differences between these two lies in the calculation of candidate score and the fact that children are only eligible under Acclamation Succession. In other words, children cannot hold governorships, but are permitted to be acclaimed as Emperor. For the rest of this section, we’ll take the succession of Governors as the primary point of discussion since that’s what you’ll encounter most.  

For those of you who remember viceroyalties in CK2, you may remember that one of the most significant drawbacks of how they worked was the constant micro of having to hand out the titles again and again. All governors have a new succession law to combat this, named Appointment. This new succession law makes managing your vassals significantly easier and, more importantly, provides the vassals with a whole new level of agency as they have a venue of attempting to seize titles for themselves. An important element when you consider the landless aspect, as you won’t have to sit around waiting and hoping that your liege appoints you as a governor.  

In tandem with this newfound agency for Governors, the emperor is also bound up in this rat race of politicking. While the top liege of an admin realm has a few additional tools to make changes to the lay of the realm (as is their lawful right), they must also contend with the bargaining and exchange of favors proffered by Governors and Noble Family Heads.  

By default, any eligible family members of the governor will be added to the line of succession for any held governorship, sorted by their candidate score.The score a character gets includes a wide set of factors, such as skills, their relation with the current governor, potential upgrades in the Estate, and much more.  

![image-04.jpg](https://forumcontent.paradoxplaza.com/public/1140044/image-04.jpg "image-04.jpg")


*[You can check the candidate score tooltip for every candidate to see a breakdown of their score.]*  

The interesting part is that other governors, landless nobles, and even the liege can spend their Influence to invest in the candidacy of other characters. These investments are done per character and per title, and you can invest in characters not already in the line of succession.  

![image-06.png](https://forumcontent.paradoxplaza.com/public/1140045/image-06.png "image-06.png")


*[The new interaction to invest in a candidate allows you to spend various amounts of Influence to increase and decrease a character’s Candidate Score for a specific title.]*  

That said, we do impose an investment cap, which is calculated from a variety of factors, but is primarily based on your House’s Powerful Family Rating. This means that you can only invest up to a certain amount of influence per character, per title, and that is directly proportional to the power of your House. Say you’ve hit the cap, but your candidate still isn’t first in the line of succession. What then? You must convince other Governors and Noble Family Heads to support your candidate, whether through goodwill, bribes, exerting more influence, or the like.  

![image-07.png](https://forumcontent.paradoxplaza.com/public/1140046/image-07.png "image-07.png")


*[You may also consider asking other politicking characters in the realm to support your chosen candidates.]*  

Investing in a character for a title will make them appear in the line of succession, getting their own candidate score, which is increased further by the amount of Influence you choose to invest. So not only can you make yourself, or members of your family, appear in the line of succession of other governorships, but by spending large amounts of Influence, you can even compete to make your candidate appear first in line. Then all you need is for the current governor to have a *happy little accident…*  

That’s a pretty classic CK way of going about it, though. A true Byzantine politicker would go a more political route and force that governor to resign their appointment or use the new Slander scheme to run their reputation into the ground.  

![image-08.png](https://forumcontent.paradoxplaza.com/public/1140047/image-08.png "image-08.png")


*[A new interaction allows you to convince the emperor to force a governor’s resignation.]*  

![image-09.png](https://forumcontent.paradoxplaza.com/public/1140048/image-09.png "image-09.png")


*[The new Slander Scheme provides ample opportunity to ruin other characters’ candidate scores.]  
[CM Note: We'll talk more about the changes to this particular mechanic in a future dev diary.]*  

![image-10.png](https://forumcontent.paradoxplaza.com/public/1140049/image-10.png "image-10.png")


*[Choose the precise moment you’re ready to drag your political opponent’s reputation with the new Scheme interface.]  
*[CM Note: We'll talk more about the changes to this particular mechanic in a future dev diary.]**  

Since a character can normally only hold a single governorship at a time, they can’t inherit a second one. There are ways to get a second governorship, even if you already have one, but it will be the exception rather than the rule. You’ll have to rely on your family members getting and holding governorships if you want to extend your family’s influence, and spending your Influence to invest in their candidacy for a given title is the primary way of doing so. You won’t be the only one attempting to contest titles, however. You’ll be competing with the other noble families of the realm, all attempting to secure governorships for themselves.  

One way for characters to slide into this exception is by scheming to Subsume another Governorship. This new Scheme allows Governors to leverage all their intrigue and influence to secure an additional, neighboring governorship appointment. That said, each title will retain its own line of succession and be granted to different governors upon succession.  

Investing in candidates for various titles is going to be one of the primary ways for you to spend and utilize your Influence. That said, there are numerous ways of getting your House members into positions of power; you just have to play your cards right.  

### Governor Efficiency​

All governors have something we call Governor Efficiency. It can be described as how good they are at their job of being a governor. It is a value, set between -50 and +50, and acts as a modifier on the land a governor holds. It translates directly into how much levies or taxes their holdings provide. Let’s say a governor has a -25% Efficiency; the holdings of that governor then provide 25% less taxes and levies.  

A governor’s Efficiency is mainly decided by their overall skills. They’ll need a minimum amount of skill points to go above the -50% threshold. When their skills are high enough, every skill point will further increase their Efficiency. Meaning that a highly skilled character will have a much higher efficiency, and therefore also be a much more valuable vassal.  

While Efficiency is mainly a measurement of a character’s overall skill, there are a few other factors that greatly impact their total Efficiency. We want a character’s education and experience as a governor to matter. While these traits do provide additional skills (thus increasing their base Efficiency), they also grant a bonus on top of it.  

Some of Governor Efficiency’s main factors include the following:  


- The governor’s overall skill
- The rank of their governor trait
- Having a rank 4 or 5 education
- Upgrades in the governor’s Estate
- The administration type of their governorship
- Eunuchs have an extra bonus - Making them better than average as governors
- Mentor in Governance - A scheme where you attempt to improve a governor’s Efficiency

![image-11.jpg](https://forumcontent.paradoxplaza.com/public/1140050/image-11.jpg "image-11.jpg")


*[Governor Efficiency as shown for a governor.]*  

For convenience, we show a character’s Efficiency in the character view if a character is Administrative (regardless of if they are a governor or not) or if they are completely landless. This makes it easy to see the efficiency of existing governors and the potential efficiency of a character you might want to appoint as a governor.  

For the Emperor of an Administrative realm, this is handy for deciding who to appoint as Governors (if they have the necessary influence). For Noble Family Heads, this is a good indicator of which family members will perform well and would therefore be good candidates for investment. Sometimes these considerations will (fortunately) overlap, but more often than not, there will be wide-scale political friction amongst those jockeying for the same governorship.  

### Governor Duties​

Let’s circle back to being a governor, and the governor trait specifically. As we mentioned above, you’ll gain trait experience for performing your duties as a governor. This can be done in multiple ways; for example, you are expected to construct buildings in the holdings you control. Whenever a building finishes its construction, you’ll gain some trait experience as well as some minor amounts of Influence.  

The primary way of leveling up your governor trait is by solving what we call “governor issues”. These appear on the map, most often in the form of various issues you have to deal with, for you to address as soon as you are able. Perhaps you have a large bandit presence you have to deal with, utilizing your marshal skill, or perhaps you have villagers complaining about an evil presence haunting them, pleading to you for help.  

![image-12.jpg](https://forumcontent.paradoxplaza.com/public/1140051/image-12.jpg "image-12.jpg")


*[The governor issue Rampant Bandits with the corresponding map marker.]*  

Most of the governor issues are problems you have to solve in some way, but not all of them are issues. They can appear as opportunities or as rewards for being at the right place at the right time. If you have baronies with farmland terrain present in your governorship, you might enjoy a higher chance to reap the benefits of a bountiful harvest, allowing you to choose what to do with the surplus. Are you the diligent governor who provides for the people, increasing development and granting you some governor trait experience in the process? Perhaps you would rather donate it to charity and gain some piety? Or are you the type of governor to sell it and keep the gold to yourself, losing governor trait experience as a result?  

![image-13.jpg](https://forumcontent.paradoxplaza.com/public/1140052/image-13.jpg "image-13.jpg")


*[The governor issue Bountiful Harvest lets you choose what to do with the grain produced in your governorship.]*  

As an aside: you may also notice the colorful new art gracing the title of the event shown above. We’ve added colored banners to all event titles so that they match their relevant icon. This is of course editable in script should you wish to insert custom art in a mod.  

Regardless of the situation, the overall format is fairly straightforward. If the issue appears in a barony that isn’t your capital, you’ll usually have to travel there in order to solve it. Once there, some issues will require you to first succeed before you can pick a solution, usually in the form of a skill duel. When successful, or if you don’t have a skill duel to succeed, you are presented with a few different options of how to tackle the issue at hand. These options are typically randomized, but the number of options available depends on the level of your governor trait, giving you a greater selection of options as you gain more experience. Every option offers slightly different rewards. You may gain varying amounts of trait experience, some will offer you some gold or prestige, perhaps your character gets a modifier with some long-term benefit, etc.  

![image-14.jpg](https://forumcontent.paradoxplaza.com/public/1140053/image-14.jpg "image-14.jpg")


*[The resolution of the governor issue “Titles for Sale” with the potential options you may choose between.]*  

You will get a governor issue every few years or so. They are not meant to be very frequent, but still be something you get on a somewhat regular basis. The issues you get will, to some extent, reflect your theme and how it's being managed. They offer a unique experience in that it is you, the governor, who has the responsibility to manage the land you are appointed to and solve any issues that may appear, unlike a feudal structure where each subject has to manage their own lands.  

### Administration Type​

Each governorship can have one of several administration types assigned to it. These come in a few different flavors, very much inspired by the different Themes of the Byzantine Empire. There are six types available, all offering bonuses such as increased tax contribution, new CBs, increased Legitimacy for the liege, and more. Each type (other than the default) also has an associated increase to the holder’s Governor Efficiency, but let’s take a look at each of them and see what they do.  

#### Balanced​

The Balanced Administration is your default and doesn’t change or add anything drastic, but it’s available to everyone and has no associated drawbacks. The main benefit will be for the governor, who gets increased trait experience, increasing the speed at which they’ll be able to level up their trait.  

![image-15.jpg](https://forumcontent.paradoxplaza.com/public/1140054/image-15.jpg "image-15.jpg")


*[The Balanced administration type and its associated effects.]*  

#### Civilian​

A Civilian Administration is all about improving the economy and encouraging overall development. An empire won’t last long without a solid foundation, after all. Here the governor also gains a bonus to their Efficiency based on their stewardship. All of it comes at the cost of reduced military capability, but surely a Theme tucked away safely in the heartlands of Anatolia is in no danger, right?  

![image-16.jpg](https://forumcontent.paradoxplaza.com/public/1140055/image-16.jpg "image-16.jpg")


*[The Civilian administration type and its associated effects.]*  

#### Military​

The opposite of a Civilian Administration. Military Administration focuses on troops, by increasing the number of troops you have access to, and keeping the lands safe. Martial is the name of the game, and the governor gets an Efficiency bonus from their own martial skill. The drawback is that you’ll greatly reduce the Theme’s economic output, but you know what they say: the best defense is a good offense.  

![image-17.jpg](https://forumcontent.paradoxplaza.com/public/1140056/image-17.jpg "image-17.jpg")


*[The Military administration type and its associated effects.]*  

#### Frontier​

Here is where things start getting interesting. A Frontier Administration can only be used for Themes along the border. It gives the governor some hefty defensive bonuses, to give you a much easier time defending against invasions. It also gives the vassal access to a new CB: Duchy Expansion. This allows the vassal to expand the realm more easily without the emperor having to go to war.  

![image-18.jpg](https://forumcontent.paradoxplaza.com/public/1140057/image-18.jpg "image-18.jpg")


*[The Frontier administration type and its associated effects.]*  

#### Imperial​

The Imperial Administration type is inspired by how certain Themes within the Byzantine Empire were considered to have a higher seniority than others. It would lead to a few Themes being seen as more prestigious and more valued compared to other Themes. As such, a Theme under Imperial Administration provides a lot of prestige, and leans more into the influence and political part of an Administrative realm. Only a single theme can have the Imperial Administration.  

![image-19.jpg](https://forumcontent.paradoxplaza.com/public/1140059/image-19.jpg "image-19.jpg")


*[The Imperial Administration type and its associated effects.]*  

#### Naval​

Byzantium wouldn’t feel complete without some form of naval-themed, well, Themes. Before you get hopeful for naval combat or naval Men-at-Arms, let me stop you right there: **We are not introducing any new naval mechanic with this release.**  

A Naval Administration can be seen as something in between a civilian and frontier Theme. It gives you some economical advantage by increasing the development growth (portrayed as increased trade and overall naval activity) as well as some military perks. The Governor gains access to the Naval Duchy Expansion CB, alongside bonuses such as reduced embarkation cost and coastal advantage, making it considerably easier to invade other realms across the mediterranean. It goes without saying that the Theme has to be situated on the coast for it to be naval.  

![image-20.jpg](https://forumcontent.paradoxplaza.com/public/1140060/image-20.jpg "image-20.jpg")


*[The Naval Administration type and its associated effects.]*  

The emperor is able to change type almost at will with no cost attached. They are in charge after all, and you are telling the governor how they should run the governorship they are appointed to. The governor can request the liege to change it, however. It costs some Influence to do so, and as long as the liege is willing to accept, you can change your administration into whichever available type you want. If you have a hook on your liege, you gain two benefits. You can force the emperor to accept and change your type, even if they would normally refuse, and using a hook also lets you circumvent the Influence cost. Very handy when you have plenty of other things to spend your Influence on.  

### Imperial Troops​

The Byzantine military was primarily made up of organized armies and well-drilled troops, led by highly skilled commanders. They tended to rely more on professional troops and less on levied soldiers, at least during the later centuries of the empire's existence. We are introducing a new system to represent this, one where both governors and the emperor are able to recruit and keep Men-at-Arms for their titles.  

Title Men-at-Arms are recruited directly to a held title of duchy tier or above (not including Noble Family titles), and are then raised like any other type of troops. Since they belong to a title, these are not a character’s personal troops that they get to keep upon succession. When you lose a title that has Men-at-Arms, those troops will follow the title itself and be made available to the new holder. In other words, these troops will pass from governor to governor, regardless of who the new governor is.  

![image-21.jpg](https://forumcontent.paradoxplaza.com/public/1140061/image-21.jpg "image-21.jpg")


*[An army list showing the available troops of your governors.]*  

These new Men-at-Arms include some obvious advantages for an Administrative realm. The empire's military strength is significantly higher than those of other realms, since the emperor will have access to a lot more Men-at-Arms through his governors. The emperor has the ability to “borrow” armies managed by the governors, effectively taking command of a governor’s Title Troops directly. He can also reassign a governor's army to another governorship, allowing the corresponding governor to use them instead. Taking or reassigning troops can be done by spending Influence. If you as the emperor have the Influence to spare, you can get access to a tremendous amount of Men-at-Arms, allowing you to beat your enemies with ease. Which brings us to the original vision of Administrative realms. When well managed, we want them to perform exceedingly well and be very powerful in comparison to other government types.  

The empire has a clear benefit by having access to a much greater pool of Men-at-Arms to draw from when expanding its borders or defending itself against enemies. But it also means that the governors have a lot more punching power. Should they end up in a position where they dislike the emperor or are coerced into joining a claimant faction, civil wars will be frequent and pose a substantial threat!  

The Influence cost for taking or reassigning troops varies depending on your situation. The cost is reduced slightly for defensive wars for example, giving you an easier time to defend yourself. When you are fighting offensive wars on the other hand, taking troops from governors who are far away from the frontline will cost you a lot more Influence. This creates a fine balance where you have to consider how you are waging your wars. You’ll have to be mindful of how much Influence you have available, and where the troops are coming from, in order to make the most use of your governor’s armies.  

![image-22.jpg](https://forumcontent.paradoxplaza.com/public/1140062/image-22.jpg "image-22.jpg")


*[A governor’s army being shown costs a certain amount of Influence to take control of.]*  

Title Men-at-Arms have two further considerations. They can be stationed just like personal Men-at-Arms. The governor is expected to recruit troops for their theme and station them within the theme's domain. Additionally, Title Men-at-Arms are affected by the Governor Efficiency of the title’s holder. Just as the Efficiency increases or decreases the amount of taxes of a holding, so too will Efficiency affect the stats of a title’s troops. Yes, this does mean that if you have really good governors available, their troops are going to pack quite a punch. A great boon when you can find and appoint highly skilled governors. As long as they are on your side. If they rise up in rebellion against you, you’ll be fighting against significantly better troops. Most governors will, however, generally have a lower Efficiency, and decrease the efficiency of their troops accordingly.  

![image-23.jpg](https://forumcontent.paradoxplaza.com/public/1140063/image-23.jpg "image-23.jpg")


*[Title Men-at-Arms stats as affected by a governor’s Efficiency.]*  

To further balance the much larger pool of available Men-at-Arms, we have done several things. The overall limit and regiment size is notably lower for Title Men-at-Arms than it is for Personal Men-at-Arms. As the realm expands, you’ll have more titles and thus also gain more troops. These really add up over time, so limiting how many regiments each title can have makes a lot of sense. Currently, the limit for titles will also not increase with Eras or Innovations, meaning that expanding the realm is the primary way to get more of them. Which meshes well with the idea that an Administrative realm is meant to become a large and sprawling empire. Another balancing factor is that Administrative rulers will have less space for personal Men-at-Arms. Both the regular Men-at-Arms Limit and the Men-at-Arms Size are reduced, allowing them to field less personal troops than other government types. The availability of Title troops makes up for it to a large extent, the focus here is after all less on personal troops and more on providing the empire with efficient armies.  

Administrative, as a result of the focus on Men-at-Arms, also has a lot less emphasis on levies. We reduce the overall amount of levies by a flat -50%, making levies largely irrelevant. Remember that a governor's Efficiency may also reduce the amount of levies further, should their Efficiency be below 0.  

### Imperial Bureaucracy​

Administrative realms have a new law, which replaces the regular Crown Authority law, named Imperial Bureaucracy. By and large the effects are quite similar to Crown Authority, but they focus more heavily on the features that make Administrative Government stand out.  

A few effects worth mentioning;  


- Vassal titles cannot be inherited outside of the realm starting at level 1.
  * In practice, this prevents them from ever doing so.
- Higher levels only increase the tax contribution of Admin vassals.
  * Vassals of other government types are unaffected, making them much less valuable.
- War declarations for non-Administrative vassals are heavily imposed with each consecutive level.
  * At maximum level, they are unable to declare war outright.
- The highest level reduces the Influence cost for the emperor to take command of a governor’s troops.

Another significant difference is that only the top liege can change the Bureaucracy level. All Administrative vassals will simply follow suit automatically, using whichever level their liege has. Not only will the vassals not have to worry about changing their own laws, but it reinforces the feeling that you are part of something bigger. You don’t set the laws, you follow the laws decided upon those further up the hierarchy.  

![image-24.jpg](https://forumcontent.paradoxplaza.com/public/1140064/image-24.jpg "image-24.jpg")


*[The tooltip for the second level of Imperial Bureaucracy, about to be adopted as the emperor recently changed to this law.]*  

Any vassals of other government types will still retain their corresponding Authority law (Crown or Tribal Authority). These work as per usual, where the vassal can change the level independently from what their liege has.  

### State Faith​

With the variance of leadership and governance that occur within Administrative realms, the time has finally come to implement a feature like State Faith. In Administrative realms, the faith of the Top Liege and the faith associated with the empire in general, have been separated.  

![image-25.png](https://forumcontent.paradoxplaza.com/public/1140065/image-25.png "image-25.png")


*[The Administrative government UI displays State Faith along with two buttons for decisions to Change or Adopt the faith.]*  

For example, Byzantium may well see multiple Iconoclast or Bogomolist emperors come and go throughout the years while remaining Orthodox at its core. That’s not to say one of these emperors can’t change the State Faith, which is done through a new decision (though at great cost).  

![image-26.png](https://forumcontent.paradoxplaza.com/public/1140066/image-26.png "image-26.png")


*[A new decision allows the emperor to change the State Faith of an Administrative realm.]*  

This further affects how characters within the realm interact with each other. It’s harder to get characters to convert away from the State Faith, and on the flip-side, much easier to get them to start practicing it. Peer pressure goes a long way here.  

![image-27.png](https://forumcontent.paradoxplaza.com/public/1140067/image-27.png "image-27.png")


*[Converting characters away from the State Faith is more difficult.]*  

State Faith is not tied specifically to Administrative realms. For ease of use in the modding sphere, we’ve tied the functionality of State Faith to a Government Rule in script. Right now, it’s only shown in the UI for Admin realms since that’s the only place we are using it in vanilla at this stage, but modders should feel free to add it to different government types if they so desire. There are basic triggers and effects to accompany it, so it should be fully usable!  

I’ll note that this feature wasn’t exactly planned for when we set out to make this DLC, but we added State Faith because it felt wrong not to have it. We think this, along with the other features we have discussed in this dev diary, will help Admin realms feel markedly different and novel compared to established playstyles.  

### Adopting Administrative​

Any feudal or clan ruler will have access to a decision that lets them replace their current government and become Administrative. Note that you have to be an empire already before you can do so. Additionally, you will need to surpass a minimum realm size; an Administrative realm is meant to be a large empire, so adopting it as a tiny ruler makes little sense. You will also need the approval of your powerful vassals, as you won’t be able to perform such a radical reform in your government with at least your most influential vassals supporting you.  

It will cost you quite a lot of gold to become an Admin realm, though. The gold cost scales with your realm size, so you’ll want to become administrative before you become too large. No one ever said it would be cheap nor easy to strive towards a more bureaucratic playstyle.  

![image-28.jpg](https://forumcontent.paradoxplaza.com/public/1140068/image-28.jpg "image-28.jpg")




Upon taking the decision, the vast majority of your vassals will change governments alongside you. Though not everyone probably will. Your powerful vassals will always change government, since you need their approval. Other vassals are less eager. Vassals of a different faith, for example, will likely not accept, since it is your own faith that will become the new State Faith. And if your empire is fairly vast already, any non-de jure vassals you may have will also not become Administrative. Fortunately, you have tools available to convince these vassals to become a part of your bureaucracy sooner or later. A new character interaction allows you to spend gold in an attempt to make non-Admin vassals adopt your new government type.  

Do note that the requirements are still pending, as they may change depending on overall balance and what feels right as you take the decision.  

### Historical Administrative Realms​

Since the content focus of Roads to Power is centered on Byzantium, we have not applied Administrative Government to any other realms on game start by default. We’ll discuss content a bit later on this summer in the dev diary about Byzantine flavor, but suffice it to say that the content for Admin realms is greatly inspired by Byzantium, while not being completely locked to that cultural context.  

We know players will be itching to try out Admin in other places. And while they can always convert from Feudal/Clan to Admin (as shown above), we thought it would be fun to add a few historical game rules that set the following realms Government Type as Administrative on game start:  


- Egypt
- Arabian Empire
- Ghana
- Kabulistan
- Persia
- Maghreb
- The Carolingians
- Tamilakam
- All Players

To give you a taste of how this will look, feast your eyes on an Administrative Arabian Empire with our lovely new Admin UI panel:  

![image-29.png](https://forumcontent.paradoxplaza.com/public/1140069/image-29.png "image-29.png")


*[The Arabian Empire and its internal structure of Governorships.]*  

---

And there we go! That should cover the fundamentals of Administrative, our new Government type, and we hope to have given you an idea of how it plays. Join us again next week as we cover the details of our new start date, 1178, and its two associated bookmarks!

<!-- artifact:reactions:start -->
- 166 Like
- 109 Love
- 15 (unlabeled — rendered as base64 data URI)
- 8 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)**
Role: Game Designer
Badges: 4
Reaction score: 9,949

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
