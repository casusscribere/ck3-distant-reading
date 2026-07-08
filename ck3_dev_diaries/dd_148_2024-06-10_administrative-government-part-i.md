---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1687086/"
forum_thread_id: 1687086
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 148
title: "Dev Diary #148 - Administrative Government (Part I)"
dd_date: 2024-06-10
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
body_word_count: 5314
inline_image_count: 25
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1687086'
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
    location: raw_lines_~28_to_146
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_145
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3110.jpg?1718088533
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_478_to_482
    action: preserved_and_flagged
    counts:
      Like: 163
      Love: 141
      (unlabeled — rendered as base64 data URI): 4
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_490_to_604
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_605_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3110.jpg?1718088533)
<!-- artifact:thread_banner:end -->

# Dev Diary #148 - Administrative Government (Part I)

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Jun 10, 2024](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-148-administrative-government-part-i.1687086/)
<!-- artifact:thread_metadata:end -->

Greetings Crusaders!  

My name is Emil, resident game designer here on Crusader Kings III. Today I’m joined by Chad ([@chaddling](https://forum.paradoxplaza.com/forum/members/1717140/) ), my fellow game designer and comrade in arms when it concerns all things Byzantium, to invite all of you, from the most distant governors of our great empire to the esteemed nobles residing here in the capital, to our first in-depth dev diary for our upcoming Major Expansion Roads to Power.  

More specifically, we’ll be going over a brand-new government type: the Administrative Government. All of you who enjoy playing in Byzantium might wanna pay extra attention. I’ll be going into a fair amount of detail in an attempt to give you a clear picture of what to expect, how the new government plays, and what it is not.  

Please keep in mind the following:  


- All of the included screenshots show a **work in progress** and do not necessarily represent the final product, as we are still heavily at work on the expansion itself.
- This is especially true when it comes to several aspects of the UI, such as **layouts and visuals**. But that won’t stop us from including screenshots anyway, since we believe that showing what we have right now, even if not final, gives you a much better idea of what you can expect.
- All **values and numbers** in these screenshots are subject to **balancing** and will likely change before release.
- **This is only part 1** (of 2) for the dev diaries on Administrative Government. Some of the things you might be dying to learn about (e.g. how Appointment Succession works) will be covered in part 2!

With that out of the way, let’s get to it!  

---

### What is Administrative?​

First things first. Administrative (or Admin for short) is a new government type that draws a lot of inspiration specifically from the Byzantine Empire. While Byzantium isn’t the only inspiration, it is by far the most significant. Just like the historical inspiration, an Administrative realm is all about the empire itself. You have the emperor situated neatly at the top, with the many governors and noble families serving underneath. They are all small cogs, part of one big machine. They need each other, just as much as they are competing against one another. Regardless of their motives or actions, they serve the empire first and foremost. For a prosperous realm is much more worthwhile to be in.  

![image-01.jpg](https://forumcontent.paradoxplaza.com/public/1136761/image-01.jpg "image-01.jpg")


*[The Byzantine Empire and its internal structure of Themes (or governorships).]*  

The emperor is the ultimate authority of the realm. It is the emperor who creates new governorships and appoints the governor of a *Theme*. The pool of available candidates can be vast, and the emperor will have to consider if they want to appoint that troublesome nephew to keep as much power as possible within his own family, or if a member of another noble family would be a better choice. Having a more competent but docile governor might just be more useful, at least as far as the realm is concerned. Just as the emperor manages the overall structure of the empire, so too does he support and supervise his governors. He can lend them troops if needed, have them go to war on his behalf, and reward them when they are performing well to be in their good graces.  

The power of an Administrative realm is very much intended to ebb and flow. When the empire is well managed, it runs smoothly like a well-oiled machine, able to beat down its opponents with ease. When mismanaged, however, it becomes significantly weaker, unable to defend itself against opportunistic conquerors looming on its doorstep.  

Expect a playstyle where wars give way to schemes, intrigue, and good old-fashioned politics. Internal wars between vassals are practically non-existent, as your primary way of expanding within the realm will be to make efficient use of schemes and leverage your influence as you jockey for governorships and other influential positions. Governors are unable to create or join independence and dissolution factions, making Administrative realms excel as large and sprawling empires. While they are significantly less likely to collapse or break apart, succession is a much riskier business. Claimants won’t sit idly by while the empire’s fate lies in the hands of an inept emperor.  

The Byzantine Empire will play significantly differently from how you are used to playing the game. You would normally gain titles through proven means, such as wars or marriage, but to gain lands and extend your own power in an Administrative realm, you will have to engage in politics. You’ll scheme against your rivals, leverage hooks against your peers, and make use of your influence to sway the emperor to your side.  

To reinforce this new playstyle, schemes have been updated to be more engaging, and we have a new scheme type available only within Administrative realms – Political schemes. There are several new schemes of this type, as well as a swath of new interactions, that will help you manage the realm, interact with your liege, your vassals, and your peers. Ultimately, these are all tools with which you can leverage your influence to shape the realm to your will. We’ll go more in depth into these throughout this dev diary.  

Byzantium is the main focus of the expansion and will be the only realm that will have Administrative on game start, trading a lot of conventional gameplay in exchange for new and powerful tools, at the cost of increased micromanagement and a less secure succession. Any feudal or clan ruler can strive to surpass Byzantium and attempt to adopt this new government type if they so choose, but more on that later.  

### Noble Families: The Heart of Admin Realms​

Administrative Governments are unique in that they allow for the existence of Noble Families. Every House in an admin realm is a player in the vast political game, whether they hold land at a certain moment or not. All these families are jockeying for power, titles, and even control of the empire itself. As the head of a Noble Family, it is your prerogative to garner power in the form of securing appointments and positions for your house members, improving the family Estate, and undercutting any political rivals that would challenge your name.  

Directly owning landed titles on the map is not a requirement for rulers within Administrative realms. If you are appointed to a title and any corresponding counties, you are there to do a job. This is not your personal fiefdom to do as you please. Admin realms should feel like a sort of proto-nation state, as Byzantium can be described during our period. As an admin governor are meant to manage the land and act publicly on behalf of the realm and your liege. That’s not to say you can’t set something aside for yourself, however… It's a tough job managing the realm, after all.  

This means that you can quite easily also lose any land you hold, should you be forced to resign, unable to secure the succession, or you may even give it up willingly if you so choose (you might want to put yourself in line for a better theme, for example). Owning land can, in other words, be seen as temporary. You can expect your House members to hold some land most of the time, but there will be times when you won’t. If that happens, you can keep playing as a landless noble within the realm. Should the empire fall, however, you shall fall with it.  

While not holding land, you are still a powerful political force and can take a lot of actions to claw your way to power. Unlike the more mobile Adventurers you are still very much a part of your realm, as you cannot simply pick up your things and leave, and you will always retain access to your Estate (more on that later).  

Landless nobles are made playable with a new type of title, the Noble Family title. This new title is a duchy-tier title, typically held by the House Head. You can draw comparisons to how Mercenaries or Holy Orders are set up. They exist with a duchy-tier title held by their respective leaders. There is an important caveat to mention here. This means that if you don’t have a Noble Family title, you will be unable to play as a landless noble. You will almost always be playing as the House Head. However, if you find yourself in the extremely rare case that you aren’t, we’ve made the decision to create a cadet-branch much easier for Admin. As the player, you can take this at essentially any time if you aren’t the House Head. Doing so will give you a new Noble Family title, allowing you to keep playing even if you lose your land.  

![image-02.png](https://forumcontent.paradoxplaza.com/public/1136762/image-02.png "image-02.png")


*[Each Administrative House Head has a new title associated with their position.]*  

### Powerful and Dominant Families​

Noble Families are sorted into Normal, Powerful, and Dominant families. These designations are based on something called Powerful Family Rating (discussed below) and indicate each family’s level of power within an Admin realm. Think of Powerful Families as a who’s who of the realm. If a Powerful Family manages to become Dominant, they have by-and-large subdued the political milieu of the realm to their will. Should you so desire, you can manipulate and control an admin realm as the head of a Dominant or Powerful Family without ever becoming the Top Liege.  

Rather than having individual vassals playing a big role within the realm, it is the different Houses; the most influential of which have a greater impact on the realm at large. Powerful Families remain so regardless of the position of the House Head, who may go from being a governor to landless and back again. With this, we aim to create a sense of stability among the many and frequent vicissitudes of Administrative realms.  

Becoming a Powerful Family entitles your House members to several benefits and tools. For example, only members of Powerful Families can use the new Depose and Subsume Governorship Schemes. They get a flat discount to Promoting candidates in the new Succession type (discussed in our next dev diary) and are generally better at Political Schemes. It is also easier for them to be made Co-Emperor, which we’ll discuss in a later dev diary.  

Any Powerful Family that is able to also control a significant part of the realm will become a Dominant Family. This happens when they control enough governorships to cover 25% of the realm’s total realm size, so your family must control a fair amount of land in order to become Dominant.  

A Dominant Family enjoys all the benefits accorded a Powerful Family, but to a greater degree. They are much more of a problem, or nuisance, for the liege. Once reaching such a position of influence and power, they are difficult to dislodge. They have a much easier time becoming governors for one thing, by significantly reducing the cost of investing in candidates (covered in detail next week) and have a much easier time requesting support from lesser families. Additionally, all members of a dominant family are even better at political schemes than other powerful families.  

Every family’s rating also affects how likely the members of a House are to inherit the top liege’s title. E.g. becoming emperor of Byzantium, as a portion of the rating is added to a candidate’s score (discussed below). It will be much easier to compete for the title with a high rating, or to keep it within your family if you are already emperor.  

It’s important to note that Administrative realms don't have the concept of powerful vassals like other governments do. You can still have powerful vassals, should you have vassals of other government types, as those will be able to become powerful vassals as per usual. Administrative vassals, however, cannot. This is only relevant in the case where a Feudal or Clan vassal becomes part of an Admin realm.  

#### Powerful Family Rating​

There can only be a handful of Powerful Families at any given time – 5 to be exact. The top liege’s House is always considered Powerful, and does not take up one of these 5 spots. Houses are then sorted and ranked according to their rating.  

In order to become a Powerful Family, a House needs to have a rating above a certain threshold. This prevents small and seemingly insignificant Houses from becoming Powerful, as they need a certain amount of sway within the realm before they can gain the benefits of being a Powerful Family. When above the minimum threshold, it is the 5 Houses with the highest rating that are considered Powerful.  

![image-03.jpg](https://forumcontent.paradoxplaza.com/public/1136763/image-03.jpg "image-03.jpg")


*[An example of what the rating of a powerful family may look like.]*  

There are several factors that have an impact on a family’s rating. We have smaller factors, such as the current number of living House Members, which exists as potential tie breakers if families have a similar rating. Your Estate and the buildings you construct in it also play a central role in your rating. If the Estate is located in the realm capital, you gain yet another small bonus.  

Other factors you can actively pursue is being a part of your liege’s council, where every position counts. If you can get other family members onto the council, the rating increases for each councilor. Or you can pick up the Heart of the Family diplomacy perk, which grants a small, but not insignificant bonus. The most important factor, however, is the number of governorships your family holds. Each held governorship adds to a multiplier, increasing the value of all other factors. Which means that for each governorship your family controls, the family rating will increase quite significantly.  

#### Family Attributes​

To give each family some additional flavor, they have access to what we call a Family Attribute. It’s a small set of bonuses that apply directly to all House Members, as well as a separate bonus that only applies to their liege.  

A family’s attribute is only active if and when they are considered a powerful family. Since there is a limited number of powerful families, the liege won’t be able to stack these modifiers indefinitely. Instead, we hope they serve as an incentive to keep certain families around, making sure they remain a powerful family so that you don’t lose out on the bonus they provide. Dominant families are a bit special. Their House Members get to benefit from their attribute, but the liege will not.  

There’s a number of bonuses available, pertaining to different scheme types, improving troops, generating more Influence, and more.  

![image-04.jpg](https://forumcontent.paradoxplaza.com/public/1136764/image-04.jpg "image-04.jpg")


*[The window in which you can set your Family Attribute, showing the benefits of the Confident Schemers attribute.]*  

The attributes exist to give the different families some added flavor, to give them some additional identity and character. Not all families are alike, and the attribute symbolizes what they are good at, or perhaps their origin. The AI won’t change these on the fly, so when you are playing as the emperor, you know what bonuses each family provides at all times. As a House Head yourself, you are free to change the attribute at any time. There’s no cost attached. You’ll activate a short cooldown before you can change it again, but that’s it.  

All in all, Noble Families are at the heart of Administrative realms. Their members make up the body of ruling characters and they are constantly positioning themselves to grasp more power, station, and influence within the empire at large.  

### Spheres of Influence​

Influence is a brand-new resource, which represents your political capital and the sway you hold within an Administrative realm such as Byzantium. It's about your ability to manipulate others and leverage your political standing in order to achieve a favorable outcome. In many ways, Influence is the tool that will make you successful, and gaining Influence will be key to achieving your goals. Unlike other resources, Influence is hard to come by in great quantities, and it has many varied uses.  

It is the lifeblood of an Administrative realm; while a powerful Emperor or high-ranking Governor might be allowed to do what he wishes in *theory*, the *reality* is much more complex than that. This resource symbolizes how gracefully someone navigates the politics of the realm, and a truly powerful Emperor will secure their rule and might through clever use of influence - for example, by securing army support or ousting troublesome governors.  

![image-05.jpg](https://forumcontent.paradoxplaza.com/public/1136765/image-05.jpg "image-05.jpg")


*[The new Influence resource as shown in the top bar.]*  

![image-06.jpg](https://forumcontent.paradoxplaza.com/public/1136766/image-06.jpg "image-06.jpg")


*[Influence has Levels of Influence, just like Prestige and Piety.]*  

Some Levels of Influence directly affect how well you perform Schemes within the new Political category, making a truly influential character assume the form of a masterful political manipulator.  

#### Gaining Influence​

Your monthly Influence gain very much depends on your position within the realm, your skills at manipulation, and your success with schemes. Here are a few examples of what you can gain influence from:  

#### Governor Trait​

To track just how much skill characters have after becoming a governor, we’ve implemented a new Governor trait (flavored Strategos here for Byzantium). This trait offers tiered bonuses to monthly influence gain, among other things.  


![image-07.png](https://forumcontent.paradoxplaza.com/public/1136767/image-07.png "image-07.png")



#### Liege’s Council​

Having a seat on the emperor’s council is an easy way to secure some additional influence. Alongside some other bonuses pertaining specifically to the playstyle of an Administrative realm.  

![image-08.jpg](https://forumcontent.paradoxplaza.com/public/1136768/image-08.jpg "image-08.jpg")


*[Being on your liege’s council grants some significant influence gain each month.]*  

#### Governor Duties​

Governors in particular have some additional ways of acquiring influence. You are an administrator; first and foremost meant to oversee and manage the land you are appointed to. If you perform your duties well, you’ll be rewarded for it, primarily with influence, but more on this below.  


#### ​

#### Alliances​

Alliances are important for every realm and government type and Administrative is no different. If you manage to secure an alliance with the head of another noble family within the realm, you’ll get influence every month. These stack, so the more alliances you have, the more influence you’ll get.  

![image-09.jpg](https://forumcontent.paradoxplaza.com/public/1136769/image-09.jpg "image-09.jpg")


*[You gain monthly influence from having alliances with your liege and the heads of other noble families. Do note that the values are currently not formatted correctly.]*  

#### Estate Upgrades​

The primary building of your Estate offers compounding influence bonuses as it gets upgraded. There are additional internal and external buildings you can construct on your Estate to gain even more influence, like Guest Chambers, for example.  


![image-10.png](https://forumcontent.paradoxplaza.com/public/1136770/image-10.png "image-10.png")


*[The Mansion provides a flat +2 influence per month.]*  

![image-11.png](https://forumcontent.paradoxplaza.com/public/1136771/image-11.png "image-11.png")


*[Guest Chambers provide a +4% bonus to monthly influence at level 2.]*  

#### Holding Upgrades​

Constructing or holding certain buildings within your holdings also provides influence gains. For example, we have added a new Murex Fisheries building type which can be built around the Mediterranean. It provides additional monthly influence, which increases as you upgrade the building.  


![image-12.png](https://forumcontent.paradoxplaza.com/public/1136772/image-12.png "image-12.png")


*[Murex Fisheries Building.]*  

#### Spending Influence​

Now that we know how to get Influence, the next question naturally becomes: what can we do with it? Plenty, in fact! First and foremost, Influence is a key factor in securing governorships both for yourself and your family members by investing in succession candidates (I'll come back to how this works later), but you will generally use it to climb the political ladder in different ways. For example:  

#### Demand Council Position​

Administrative vassals have the option to request a council position by spending influence. It’ll cost you a fair bit of influence, but there are ways to reduce this amount. You also have the option to demand a council position with the use of a hook, which is significantly more cost effective since you will gain some influence once you are on the council.  

![image-13.jpg](https://forumcontent.paradoxplaza.com/public/1136773/image-13.jpg "image-13.jpg")


*[The interaction to request a council position costs influence and may be refused by your liege.]*  

#### Force to Join Faction​

Not having to rely solely on hooks, you can force other vassals to join your factions by spending influence. A handy tool when you just need a tiny bit of additional support for your claimant faction, so that you can push your claim for the throne.  

![image-14.jpg](https://forumcontent.paradoxplaza.com/public/1136774/image-14.jpg "image-14.jpg")


*[Force to Join Faction allows influence to be spent instead of a hook.]*  

#### Propose Alliance​

When proposing an alliance, you can spend your influence to make the target character more likely to accept.  

![image-15.jpg](https://forumcontent.paradoxplaza.com/public/1136775/image-15.jpg "image-15.jpg")


*[Propose Alliance allows you to spend influence as a means of increasing acceptance.]*  

#### Petition Liege​

For characters in an Administrative government, the decision to petition your liege costs influence instead of the usual prestige.  

![image-16.jpg](https://forumcontent.paradoxplaza.com/public/1136776/image-16.jpg "image-16.jpg")


*[The Petition Liege decision from the perspective of a governor.]*  

#### Bolster Governance​

You can put your influence to good use by aiding and improving your governors, while also granting you some opinion in the process.  

![image-17.jpg](https://forumcontent.paradoxplaza.com/public/1136777/image-17.jpg "image-17.jpg")


[The Bolster Governance interaction costs influence to use and improves your governors.]  

### Estates​

We’ve shown you a preview of Estates in a previous dev diary, so you may already know what they look like. If you haven’t seen them though, here is an Estate, located in Constantinople no less, in all of its glory.  

![image-18.jpg](https://forumcontent.paradoxplaza.com/public/1136778/image-18.jpg "image-18.jpg")


*[An Estate with several buildings constructed and upgraded.]*  

It took us a while until we settled on the final art style. We went over a few options before we decided upon what you see above, a style inspired by medieval manuscripts. Not only does it look great, but it has a lot of quirkiness to it. Perspectives are slightly off, or people may have odd postures, etc. More or less what you’d expect from actual medieval illustrations.We opted for this art style over reusing the previous style found in the Tournament interface as it feels more flavorful and authentic to the time period, as well as being far more flexible for other locations. The buildings you construct all look different from each other, and there are different backgrounds that are dependent on the local terrain of where your Estate is located. The backgrounds provide a lot of visual variety, but we really wanted to give a better sense of location. If your Estate is placed in mountains, we want the game to reflect that. It gives a much stronger feeling of belonging and immersion. A shout out to the art team for a job well done!  

In an Administrative realm, it’s the families of the nobles that really matter, i.e. their Houses. Each House Head will have access to an Estate, which is a representation of the family’s overall wealth and any small tracts of land they may own. While a noble family might not hold any governorships, they are still influential nobles that own a significant amount of real estate. The purpose of the Estate is twofold: It gives you a powerbase you can rely on at all times, acting as your home and the place where your character resides when you don’t have any other titles. Secondly, it exists as a means of progression; one that you can tailor to suit your own needs and playstyle. Estates grants you access to a whole bunch of buildings and upgrades, providing you with various bonuses, unlocking new interactions or decisions, and improving your existing toolbox in various ways. It is, without a doubt, one of the primary sources of increasing your Influence.  

![image-19.jpg](https://forumcontent.paradoxplaza.com/public/1136779/image-19.jpg "image-19.jpg")


*[The Guard Lodging building and its tooltip, showing the effects.]*  

Estates can become quite powerful on their own. So they are restricted to one per family, owned and controlled by the House Head. It’s only the House Head that may construct new buildings and upgrade existing ones, similar to how only the Dynasty Head can pick and unlock Dynasty legacies.  

One of our primary goals is to provide you with plenty of options as to what you can build, but buildings should also have a certain degree of synergy with each other. As you consider your options and what to build, we want you to be on the lookout for how buildings and upgrades complement each other.  

### Buildings​

There are two distinct types of improvements you can build within your Estate. The first is buildings. You have one building slot dedicated to your villa, or mansion, which is a bit special, as you will always start with this building on at least level one, and you can never demolish it. Aside from your mansion, you have six slots in total in which you can construct whichever available buildings you want. Two of these slots are available from the get go. Then you’ll unlock an additional slot with every level of your mansion. You’ll have two slots on level one, three slots on level two, and so on until you reach the maximum of six slots at level five.  

There are plenty of more buildings available than you have slots, so you’ll be forced to choose what you want to build. Buildings can be easily replaced whenever you want though, so you won’t be stuck with anything if you ever change your mind. It won’t cost you anything to replace a building other than the gold it requires to construct the new building.  

Your choices won’t end there, however. Some buildings (but not all) have multiple branches where you can choose to specialize your buildings further. Branches often share some effects from the base levels before it splits into separate branches, but will then go on to provide slightly different bonuses revolving around a similar theme.  

![image-20.jpg](https://forumcontent.paradoxplaza.com/public/1136780/image-20.jpg "image-20.jpg")


*[The Shrine building and its different branches and levels.]*  

![image-21.jpg](https://forumcontent.paradoxplaza.com/public/1136781/image-21.jpg "image-21.jpg")


*[The Storehouse building and its different branches and levels.]*  

### Upgrades​

The second type of improvements for Estates are building upgrades. Unlike buildings themselves, these are built inside of existing buildings. For Estates, upgrades are available in the mansion. The mansion has a limited number of upgrade slots available: You’ll have access to two slots from the get go, and you will gain more slots as you upgrade your mansion. When your mansion is brought up to level five, you’ll have no less than ten upgrade slots to fill as you please.  

Upgrades can also have branching building paths, but most of the upgrades do not. They also tend to have fewer levels in total compared to buildings. Buildings typically have six levels, but may have less in some cases, while upgrades tend to be closer to four levels.  

All of this variation should give you plenty of options throughout the many hundreds of years the game spans.  

![image-22.jpg](https://forumcontent.paradoxplaza.com/public/1136782/image-22.jpg "image-22.jpg")


*[The upgrades and upgrade slots for your mansion.]*  

### Building Examples​

Let’s look at another few examples of what you can build, and what type of effects you can expect.  

Your mansion can be upgraded with a library, in which the primary focus is on Learning Lifestyle experience. This particular upgrade has two distinct branches available. One of which ties in nicely is dedicated to education, improving your Tutor Court Position and allowing your children to get a rank five education.  

![image-23.jpg](https://forumcontent.paradoxplaza.com/public/1136783/image-23.jpg "image-23.jpg")


*[The Education Hall upgrade provides a number of useful bonuses.]*  

The mansion can also be upgraded with a Wine Room, which in turn is upgraded into a Wine Cellar. The upgrade unlocks a new activity option for feasts, allowing you to spend some gold to gain Influence for every guest attending your feast. Each level unlocks a corresponding level for the activity, allowing you to spend more gold for a larger amount of Influence gained. Feasts are no longer just a means of gaining prestige and opinion, but become a much more central tool as you attempt to gain more and more Influence.  

![image-24.jpg](https://forumcontent.paradoxplaza.com/public/1136784/image-24.jpg "image-24.jpg")


*[The Wine Room upgrade for the Estate serves as a potential source of generating Influence.]*  

The Vineyard is another great example. The building provides you with a steady income of gold, which is quite useful already, but the true value comes from also having the Wine Room mentioned above, as it increases the amount of Influence gained when you use the unlocked activity option for feasts.  

![image-25.jpg](https://forumcontent.paradoxplaza.com/public/1136785/image-25.jpg "image-25.jpg")


*[The Vineyard building, an excellent choice for when you need both gold and additional Influence.]*  

### Modding​

As per usual, you can expect Estates to be highly moddable. Changing, removing, or adding buildings is easy to do directly in script. You can add as many levels or branching options as you want. Icon and graphics can easily be adjusted as well, as you set these per building. You can, for example, see how we use unique icons for each building branch in the screenshots above.  

Any character modifier works out of the box, and these are applied to the owner of the Estate. For anything more complicated, we’ve enabled the use of parameters, much like those we already have for cultures or faiths.  

You can even set up new types, completely separate from the Administrative Estate, to be used however you’d like. We can’t wait to see what all of you can come up with!  

---

That’s it for today! We are not *nearly* done just yet though, so we’ll be back with Part II next week; we’ll be going more into depth regarding governors, how they work and what they do on a daily basis, how an administrative realm manages its troops, and more!

<!-- artifact:reactions:start -->
- 163 Like
- 141 Love
- 19 (unlabeled — rendered as base64 data URI)
- 10 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)**
Role: Game Designer
Badges: 4
Reaction score: 9,949

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
