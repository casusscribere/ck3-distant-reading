---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1573700/"
forum_thread_id: 1573700
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 119
title: "Dev Diary #119 - Tours and Travel"
dd_date: 2023-03-14
author_handle: Meka66
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3209
inline_image_count: 31
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1573700'
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
    location: raw_lines_~28_to_149
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_148
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2240.jpg?1678798163
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_151_to_153
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_456_to_460
    action: preserved_and_flagged
    counts:
      Love: 202
      Like: 174
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_468_to_550
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_551_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2240.jpg?1678798163)
<!-- artifact:thread_banner:end -->

# Dev Diary #119 - Tours and Travel

<!-- artifact:thread_metadata:start -->
- Thread starter [Meka66](https://forum.paradoxplaza.com/forum/members/meka66.1470167/)
- Start date [Mar 14, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-119-tours-and-travel.1573700/)
<!-- artifact:thread_metadata:end -->

Dev Diary #119 – Tours and Travel  


Hello! My name is Chad and this is my premiere here on the forums. We’re really excited to kick off a series of dev diaries showing off all the work we have put into Tours and Tournaments. To briefly reiterate a bit of what was covered in [@rageair](https://forum.paradoxplaza.com/forum/members/375731/) ’s last dev diary, [the Tours & Tournaments Expansion](https://store.steampowered.com/app/2311920/Crusader_Kings_III_Tours__Tournaments/) will provide a comprehensive rework of the Activity system. Not only have we reworked Feasts, Hunts, and Pilgrimages, but we have added brand spanking new Grand Activities: Tours (also in this dev diary), Tournaments, and Grand Weddings! Along with this rework comes the new Travel System (which I’ll be talking about in more detail today) and the long-awaited Regencies feature–both free additions. You can expect to hear more about all these additions in subsequent dev diaries!  

Please note the standard disclaimer that all images are of things currently in development and are subject to change before release.  

## Travel​


As we said in last week’s dev diary, we want to reinforce the connection between the character and the map. And what’s the best way to do that? Travel.  

Every character in the game now has a bonafide Location. With the new Travel Mechanic in place, every character travels to activities that aren’t held in their current location (including the AI). Whenever you plan a Grand Tournament or accept an invitation to your vassal’s Feast, you now also have decisions to make about how you get there. Will you be daring and choose a dangerous route or play it safe? Who will you hire as your Caravan Master to ensure the journey goes smoothly?  

### The Basics: Speed, Safety, Danger​

Every Travel Plan has two basic stats: Speed and Safety. Speed is represented by a percentage, where 100% is standard (roughly similar to army movement speed). To no one’s surprise, this affects how fast a character moves from province to province. Safety is a value ranging from 1 to 100 and counteracts Danger.  

You can expect to encounter a dazzling array of situations as you travel across the map. Perhaps you will encounter a hermit living among the wilderness…  

![Travel_1_Event_Hermit.png](https://forumcontent.paradoxplaza.com/public/944042/Travel_1_Event_Hermit.png "Travel_1_Event_Hermit.png")


[Image: Event where you encounter a hermit]  

Or perhaps you’ll meet someone from a different culture who can speak your native tongue…  


![Travel_2_Event_Culture.png](https://forumcontent.paradoxplaza.com/public/944086/Travel_2_Event_Culture.png "Travel_2_Event_Culture.png")


[Image: Event where you encounter someone from faraway who can speak your native language]  

Or maybe you will even chance upon a knight-errant and convince them to join your entourage?  


![Travel_3_Event_Knight_Errant.png](https://forumcontent.paradoxplaza.com/public/944044/Travel_3_Event_Knight_Errant.png "Travel_3_Event_Knight_Errant.png")


[Image: Event where you encounter a knight-errant]  

Danger lurks in every corner of the map. Every province has a Danger score based on a variety of factors like terrain, county control, owner, et cetera. Traveling through the mountains might expose you to treacherous cliffs, while sailing the seas presents its own, unique hazards, for example.  

![Travel_4_Event_Danger_Mountains.png](https://forumcontent.paradoxplaza.com/public/944045/Travel_4_Event_Danger_Mountains.png "Travel_4_Event_Danger_Mountains.png")


[Image: Event where one of your entourage members falls from a cliff in mountainous terrain]  

![Travel_5_Event_Danger_Sea.png](https://forumcontent.paradoxplaza.com/public/944084/Travel_5_Event_Danger_Sea.png "Travel_5_Event_Danger_Sea.png")


[Image: Event where you encounter a squall destroys your sails while traveling at sea]  

There are also several dynamic factors that affect how dangerous provinces are. For example, Holdings decrease Danger while any army activity (sieges, battle, raiding) greatly increase danger. While there is always a possibility of encountering Danger, a well-prepared traveler who invests in their Safety will encounter dangerous events far less frequently.  

So how do I prepare to set out on the open road? Glad you asked, let’s take a look at the brand new Travel Planner.  

![Travel_6_Planner.png](https://forumcontent.paradoxplaza.com/public/944046/Travel_6_Planner.png "Travel_6_Planner.png")


[Image: Example of planning to travel for a Pilgrimage]  

### Caravan Master​

Along with the Travel System, we introduce the Caravan Master as a new Court Position. The Caravan Master is the face of your journey and handles all the banal, practical aspects to traveling. Hiring a skilled character will increase both your Speed and Safety while providing some passive bonuses to Army Movement Speed, Supply Limit, and Court Grandeur.  

![Travel_7_Caravan_Master.png](https://forumcontent.paradoxplaza.com/public/944047/Travel_7_Caravan_Master.png "Travel_7_Caravan_Master.png")


[Image: Selection window for choosing a Caravan Master court position]  

### Travel Options​

Every time you set out on a journey, you have the chance to pick 2 Travel Options. These additional features provide a range of possible bonuses when added to your travel.  

![Travel_8_Options.png](https://forumcontent.paradoxplaza.com/public/944048/Travel_8_Options.png "Travel_8_Options.png")


[Image: Selection screen for choosing Travel Options]  

Most Travel Options have an associated cost for the benefits they provide. Hiring Experienced Sea Captains will add a salty sea dog to your Entourage, thus making your journey across open water safer. Some are unlocked by Buildings in your domain or your character’s Traits. To illustrate, if you have built Stables or Camelries up to level 4 or higher, you can unlock the Superior Mounts Travel Option and get a nice boost to Speed. It costs nothing, of course, since you own the Stables already.  

![Travel_9_Options_Mounts.png](https://forumcontent.paradoxplaza.com/public/944049/Travel_9_Options_Mounts.png "Travel_9_Options_Mounts.png")


[Image: Superior Mounts Travel Option]  

Another example is the Train Knights Travel Option, which is unlocked by having Military Academies built in your domain. When selected, 3 of your least-skilled Knights are added to your Entourage. It increases your Safety and there is a chance for each Knight to increase their skills along the journey.  

![Travel_10_Options_Train_Knights.png](https://forumcontent.paradoxplaza.com/public/944050/Travel_10_Options_Train_Knights.png "Travel_10_Options_Train_Knights.png")


[Image: Train Knights Travel Option]  

While it’s not required to select Travel Options (especially for short journeys), they can prove quite useful when setting out on a longer journey, such as a Pilgrimage. This is also a way to affect which characters join your Entourage, the group of characters who travel at your side. Some characters, such as your Court Physician and Bodyguard, will automatically join your Entourage if you employ those Court Positions. Otherwise, your Entourage is primarily composed of characters relevant to the Activity to which you are traveling. Your Knights will join you for Tournaments, for example.  

### Custom Route Editor​

When planning a journey, you will always be presented with the shortest path towards your destination. But perhaps you really don’t want to travel through your Rival’s lands or maybe you’ve always wanted to see the splendor of Rome? Well fear not, for we have included a Custom Route Editor!  

![Travel_11_Custom_Route_Editor.png](https://forumcontent.paradoxplaza.com/public/944051/Travel_11_Custom_Route_Editor.png "Travel_11_Custom_Route_Editor.png")


[Image: Example of adding waypoints to a journey via the Custom Route Editor]  

We allow you to customize your route by adding waypoints along your path. If employed cunningly, you may be able to avoid assassins hired by your Nemesis or gaze up at Caesar’s Needle from the hallowed streets of Rome.  

### Additional Notes​

Since Travel inevitably touches nearly every aspect of the game, I figured I’d spend some time here at the end attempting to answer a few questions that are sure to arise.  

The focus for this expansion has been to create a Travel System that will specifically work for getting characters to and from Activities. With that said, we’ve endeavored to make this system as flexible as possible for future work and iterations–which is why it’s a free feature. The Travel Mechanic has also been integrated into smaller activities such as Meet Peers, Grand Blot, and Grand Rite. We are currently working on integrating the mechanic into more game systems.  

Some Schemes are still completable while you or your Target is traveling. For example, you can still sway a character or attempt to learn their language while either of you are traveling. You cannot, however, attempt to seduce someone who is not in your location. (The power of letters only goes so far…) These Schemes will be frozen until both characters are no longer traveling.  

I know you’re all eager for things like trade routes–so are we! That won’t be coming in this expansion, but it is something we have our eye on for the future.  

## Tours​

Hello hello hello, I am Meka66 and it has been a while since I was last able to write a dev diary, way back in my Hearts of Iron days. Today I'm here to talk to you about Grand Tours!  

What is a tour? Well, more broadly a Grand Tour is your opportunity to use the travel system to hold royal visits across your realm; bringing you closer to your direct vassals and giving you the opportunity to get closer to sub-realms usually in your periphery, yielding powerful rewards to help you manage your unruly subjects; both noble and lowborn.  


![placeholder-art.png](https://forumcontent.paradoxplaza.com/public/944052/placeholder-art.png "placeholder-art.png")


The art in this screen is placeholder until we get our more complete gorgeous art.  

Primarily, you will be visiting vassals, choosing from one of three things to do on your visit: Tour the Grounds, Attend a Dinner, or Attend a Cultural Festival. Each of these will yield different rewards both for the realm you're visiting and for yourself personally. Let's start with Tour the Grounds.  


![route-planning.png](https://forumcontent.paradoxplaza.com/public/944053/route-planning.png "route-planning.png")


Here you can plan your route around your kingdom  


### Stops​

#### Tour the Grounds​

![tour-arrival.png](https://forumcontent.paradoxplaza.com/public/944054/tour-arrival.png "tour-arrival.png")


Arrival at a Tour of the Grounds, the layout of this window is still being worked on.  

When Touring the Grounds of your vassal's holding, you're having a look around at daily life in your vassal's capital; visiting the village, hanging around their holding, and exploring their hunting grounds. Overall this results in a boost in Control in counties within your vassal's realm, since it is difficult to ignore the authority of the King when he's right on your doorstep.  


![vassal-control.png](https://forumcontent.paradoxplaza.com/public/944056/vassal-control.png "vassal-control.png")


One of many opportunities to raise control in your vassal's holdings  

You'll also have opportunities to boost your prestige and renown, by flexing your hunting skills on your dear vassals.  


![hunting-skills.png](https://forumcontent.paradoxplaza.com/public/944063/hunting-skills.png "hunting-skills.png")


An opportunity here to show off your hunting skills  


#### Hosted Dinner​

![dinner-arrival.png](https://forumcontent.paradoxplaza.com/public/944067/dinner-arrival.png "dinner-arrival.png")


Arriving at a dinner  

Next up we have the Hosted Dinner. The dinner is much like a feast, but far more intimate. The dinner will give you opportunities to not only share some time with your vassal and form friendships and gain hooks, but it is also an opportunity to interfere with their court; offering their courtiers a better life in the capital, becoming the guardian for your vassal's heir, and discovering secrets at your vassal's court.  


![hook-opportunity.png](https://forumcontent.paradoxplaza.com/public/944068/hook-opportunity.png "hook-opportunity.png")


One of many opportunities you have to make friends, learn secrets, and gain hooks.  

#### Cultural Festival​

![culture-festival.png](https://forumcontent.paradoxplaza.com/public/944069/culture-festival.png "culture-festival.png")


Arriving at a Cultural Festival in Sweden. A true oxymoron if ever there was one.  

Lastly we have my personal favorite, the Cultural Festival. A realm is typically made up of all sorts of people belonging to different faiths and cultures, and what better way to demonstrate the magnanimousness of your rule than to experience the strange traditions of your subjects? If you're a highly diverse realm like Khazaria or a stranger in a strange land like a Norman invader, this is an excellent opportunity to get some powerful bonuses to cultural acceptance.  


![cultural-acceptance.png](https://forumcontent.paradoxplaza.com/public/944070/cultural-acceptance.png "cultural-acceptance.png")


Spreading cultural acceptance around your realm by showing your subjects you embrace their traditions. Here we have the Emperor visiting a Bulgarian nativity play.  

But no culture is a monolith of course, and Cultural Festivals can still yield powerful rewards even if you're visiting a county of your own culture. Showing your respect for the customs of folks outside of the capital will result in potent popular opinion gains, allowing you to bring your unruly subjects in line.  


![culture-festival-rewards.png](https://forumcontent.paradoxplaza.com/public/944071/culture-festival-rewards.png "culture-festival-rewards.png")


Same-culture festivals still yield powerful rewards.  

### The Tour Planner​

Your tour consists of several stops across your realm, with one of the above activities taking place at each location. Here we have our beloved Byzantine Emperor planning a tour of his realm; having dinners with his powerful vassals, touring the grounds of his distant subjects, and observing the local culture of his Armenian and Bulgarian subjects.  


![byzantine-route.png](https://forumcontent.paradoxplaza.com/public/944072/byzantine-route.png "byzantine-route.png")


A roundabout route of the Byzantine Empire  

### A Travelling Court​

But visiting nobles isn't the only thing you're doing on your tour, of course. You are traveling with your court! On your journey, you'll get a chance to meet with your lowliest of subjects, and what you do with them exactly is up to you! You may encounter drunkards muttering of rebellion in a tavern, or be accosted by highwaymen on the road. While most travel events are just about things that happen on your journey, a tour travel event is an opportunity to remind the commoners that their liege is ever present.  

To this effect, we have several Intents. Intents in Tours determine what exactly it is you hope to do with commoners while on the road; do you want to show charity, assert your authority, or just drink and visit brothels on your merry way across your realm?  


![intent-selection.png](https://forumcontent.paradoxplaza.com/public/944073/intent-selection.png "intent-selection.png")


Here we have the intent selection screen, which can be changed at any time before or during your tour!  

We'll start with the more stone-faced intents: Altruism and Justice.  

The Altruism intent is inspired much by the concept of both charity and the Royal Touch; the belief that Kings had the power to heal the sick just with their touch. On an Altruistic route across your realm, you will show your piousness and generosity to your realm; giving piety, popular opinion, and stress loss with the right traits (compassionate, zealous, etc).  


![altruistic-opportunity.png](https://forumcontent.paradoxplaza.com/public/944074/altruistic-opportunity.png "altruistic-opportunity.png")


An altruistic opportunity to show you are not disgusted by your subjects… or not  

Justice is your chance to remind commoners that the crown is ever-present, and you can show justice, whatever it may mean to you. This can include judging local trials, meeting with peasant leaders, and sending in your men to clear out bandits. Justice results in stress loss for the appropriate traits, and some chances to fill your dungeon and increase control along your route.  


![crowns-justice.png](https://forumcontent.paradoxplaza.com/public/944075/crowns-justice.png "crowns-justice.png")


A chance to bring the Crown's justice to the countryside  

Lustful characters can also benefit from the Lechery intent, giving them the opportunity to seek out new paramours on the road and pay visits to local brothels to reduce their stress and find new lovers. If you're a player who enjoys lustful content, this intent is for you; otherwise, the lechery intent is entirely opt-in. What you want to get out of your tour is up to you!  


![violet-woods.png](https://forumcontent.paradoxplaza.com/public/944076/violet-woods.png "violet-woods.png")


This intent can be particularly useful if your spouse is unable to give you an heir  

Lastly we have the Relax intent, which is the default. In this intent, you just want to use your time on the road to visit taverns and take it easy on your tour, giving you large gains in stress reduction.  


![sin-den.png](https://forumcontent.paradoxplaza.com/public/944077/sin-den.png "sin-den.png")


There are all manner of ways to reduce stress on your Tour.  

### Tour Type​

But there is more! What primarily motivates your tour is determined by your Tour Type, of which we have three: Majesty, Taxation, and Intimidation. These options will determine what exactly it is you demand from your vassals when you stop by for a visit, is it just to show how much of a great ruler you are? Or is it to extract taxes? To strike fear into your unruly subjects?  

A Majesty Tour is all about vassal opinion and prestige. During your visits, you will show your grace and magnificence to all.  


![majesty.png](https://forumcontent.paradoxplaza.com/public/944078/majesty.png "majesty.png")



A Taxation Tour is all about finding those little loopholes and oversights your vassals have been taking advantage of and tying them up, and taking what is rightfully yours. You may cause some upset, but it's all worth it to fill the treasury, right?  


![taxation.png](https://forumcontent.paradoxplaza.com/public/944079/taxation.png "taxation.png")



Intimidation Tours are all about showing how much your vassals should fear you. You'll get chances to do all manner of things to unsettle your subject. Direct confrontation can be a powerful tool, and can even motivate some vassals to leave their hostile factions against you.  


![intimidation.png](https://forumcontent.paradoxplaza.com/public/944080/intimidation.png "intimidation.png")



Which Tour type are you most interested in trying first? We would love to hear your thoughts!  

Each time you perform an action which corresponds with your selected tour type, it will increase this tour success bar here. The rewards you get at the end of your tour will scale and change depending on just how successful you've been in achieving your goals, and if done right, it can be a powerful tool for strengthening and stabilizing your realm.  


![majesty-success.png](https://forumcontent.paradoxplaza.com/public/944081/majesty-success.png "majesty-success.png")


Here we have the Majesty success bar  

Tours are a big investment in both time and money, but they also yield powerful and long lasting rewards; everything from cultural acceptance to control to dread to prestige, a tour is an all-encompassing realm management tool, taking your court on the road and bringing the presence of the crown wherever it is needed.  

That's all for now, we'll be around to answer questions as always. See you next week where we'll talk about some of the smaller-but-broader systemic changes we've made to vassals, buildings, men-at-arms, and more!

 

Last edited by a moderator: Mar 14, 2023

<!-- artifact:reactions:start -->
- 202 Love
- 174 Like
- 15 (unlabeled — rendered as base64 data URI)
- 15 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Meka66](https://forum.paradoxplaza.com/forum/members/meka66.1470167/)**
Role: CK3 Game Design
Badges: 100
Messages: 399
Reaction score: 13,781

*[Full game-badge icon list of 22 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
