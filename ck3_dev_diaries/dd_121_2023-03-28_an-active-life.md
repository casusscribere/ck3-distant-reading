---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1576149/"
forum_thread_id: 1576149
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 121
title: "Dev Diary #121 – An Active Life"
dd_date: 2023-03-28
author_handle: blackninja9939
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 6164
inline_image_count: 41
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1576149'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2263.jpg?1680005298
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_631_to_636
    action: preserved_and_flagged
    counts:
      Love: 276
      Like: 168
      (unlabeled — rendered as base64 data URI): 4
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_644_to_756
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_757_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2263.jpg?1680005298)
<!-- artifact:thread_banner:end -->

# Dev Diary #121 – An Active Life

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [Mar 28, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-121-an-active-life.1576149/)
<!-- artifact:thread_metadata:end -->

Hello everyone and welcome to the 121st CK3 Dev Diary!  

I’m Matthew ([@blackninja9939](https://forum.paradoxplaza.com/forum/members/795679/)), one of the Programmers on the team, and today we’re going to be talking about the overhaul we’ve done to the activity system as well as the improvements to two existing activities; Hunts and Pilgrimages. We’ll be covering the other improved existing activities (Feasts, Blot now known as Festival, and Playdates) in the future as well.  

I’m gonna kick things off with how we’ve changed the activity system to better support our goals.  

On release activities were little more than a random event chain, they never felt as involved or interesting as we had wanted them to be; you had very little agency over what was actually going to happen in your activity when planning one or when your guests arrived and it was not very clear to see how your activity was actually progressing as you played.  

First of all we’ve moved activities out of the decisions menu and into their own dedicated list in the UI, this list is where you’ll see the activities you can host, any ongoing activities you can join, as well as your current activity too. You can also see your current activity in the HUD as well.  

![1-activities.png](https://forumcontent.paradoxplaza.com/public/949345/1-activities.png "1-activities.png")


*[Image of the new activity screen, with sections for activities you can host, grand activities you can host, activities you are invited to, and a checkbox to be notified about tournaments you can join]*  

When you click on any of these activities you get to see a more detailed breakdown of what hosting one is likely to have as an outcome for you and your guests, as well as any other useful information like missing a Master of the Hunt or how long the cooldown will be.  
You can also flag each activity type to notify you via alert when it is available to host, much like decisions this is on by default for the more important Grand Activities.  

![2-hunt-host.png](https://forumcontent.paradoxplaza.com/public/949346/2-hunt-host.png "2-hunt-host.png")


*[Image of Hunt activity detailed breakdown, listing flavor text, image, expected rewards, warnings and cooldowns. Look out for more details on Acclaimed Knights in a future Dev Diary]*  

This view also contains all activities you can potentially join, either ones you have been specifically invited to or any Grand Tournaments nearby as they are open activities that anyone can choose to join of their own volition.  
Invites list information about the activity and why you might want to attend as a guest, as after all not only the host of an activity benefits from attending and over a full game you can quite easily attend more activities than you host. If you accept the invitation you are taken to the travel planner where you can pick out your route and travel options etc.  

![3-feast-invitation.png](https://forumcontent.paradoxplaza.com/public/949347/3-feast-invitation.png "3-feast-invitation.png")


*[Image of an activity invite, a parchment background with a letter invite, a timeline of the activity phase, details on the effects of joining, and buttons to accept and decline the invite]*  

Once you click to plan an activity that is where the real big changes begin as you get taken to the all new activity planner. The first choice you make in most activities is what special type you would like to engage in, these types set the overall theme and tone of the activity, some are available to everyone and others are unlocked by more specific conditions such as various perks or modifiers.  
These provide a variety of different potential rewards that you are aiming to get by hosting this activity, and what costs or risks you may incur too.  

![4-hunt-types.png](https://forumcontent.paradoxplaza.com/public/949348/4-hunt-types.png "4-hunt-types.png")


*[Image of the hunt special types selection: Regular, Falconry and Legendary]*  

After you decide your type you then need to pick a location, or depending on your activity multiple locations such as in a Tour, where your activity will occur. The map automatically zooms out to fit all the locations on screen, mainly so you don’t forget about any of those Holy Sites that are a bit further away from your realm.  

The map will highlight all valid locations you can go to and every location is given a score of how good hosting there is likely to be, what this score and impact is depends on each individual activity.  
So for a Hunt things like terrain can impact your success chance, for a Tournament having relevant buildings can reduce the cost, and Tours care more about the vassal’s opinion of you.  

The valid locations also have a map marker on them, each activity can also be defined to only show the top X markers so as to not clutter the map. Hunts for example only show the top 5, though you can still pick any location you desire still.  

![5-hunt-locations.png](https://forumcontent.paradoxplaza.com/public/949349/5-hunt-locations.png "5-hunt-locations.png")


*[Image showing the various locations I can hunt in my realm]*  

Now is a good time for me to go a bit more in depth about the mechanics of a new activity, each activity is now broken up into multiple distinct phases. A phase is a combination of two things: a location and some action you will do whilst there.  

Every activity handles their phases differently, some like Hunts are at a single location with a single predefined action, you go somewhere and you try and find some animal to brutally slaughter or you can let that poor bunny rabbit run back to Bambi.  

Other activities like a Tour are multiple locations with different actions you can pick, you can visit multiple of your vassals and each Tour “stop” is a phase and you pick the action to do there. Tours also always insert a final predefined phase which is your journey home.  

A Tournament on the other hand is a single location with multiple different contests, but more about those in a future dev diary.  

All of these different requirements for what locations and phases you can pick are fully moddable, including logic for if they are predefined, picked by the player, a combination of both, and if they take place at one or more locations. So the system is very versatile in what you can plan, all of these are taken care of in the activity planner.  

For now with Hunts we have chosen our location and now we can see the route we will travel to our destination as well as various options and guests that we can customize in the activity.  

![6-travel-map.png](https://forumcontent.paradoxplaza.com/public/949350/6-travel-map.png "6-travel-map.png")


*[Image showing the travel planner from dev diary 119 and the activity planner tab for your intent, options, and guests as well as cost and start button]*  

For a refresher on the travel planner go back and check out [Dev Diary 119](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-119-tours-and-travel.1573700/) as everything you could do for traveling there you can do when you travel to any activity such as changing your travel options and customizing your route.  

In the bottom right though you can see a few more options related to the activity itself. We’ve got our Intent, Activity Options, Guest List, and finally the cost and button to start the activity.  

I’ll look at them left to right so let's start with Intents. Intents represent what you specifically want to get out from the activity on a more personal level. Every activity has a default intent which is generally Recreation, you are going to just relax and try to reduce your stress. There are many more intents though, some shared and some unique to each activity, such as Slay Beast, that you can select.  

Every character attending the activity has an intent, and you can change your intent mid way through an activity if you decide to pursue something else or if you complete your intent and move onto another goal. Some intents without a specific goal like Recreation cannot be failed, because you always manage to do something entertaining whilst at an activity.  

![7-hunt-intent.png](https://forumcontent.paradoxplaza.com/public/949351/7-hunt-intent.png "7-hunt-intent.png")


*[Image showing intent selection, on the left is the host’s portrait with an animation based on the selected intent, on the right is a list of intents that can be selected alongside their icon and text describing the selected one]*  

Some intents even come with a target you pick from your invited guests, such as trying to find an excuse to Murder someone during your Hunt, or maybe you’ve got more *cough* amorous plans…  

![8-hunt-intent-2.png](https://forumcontent.paradoxplaza.com/public/949352/8-hunt-intent-2.png "8-hunt-intent-2.png")


*[Image showing intent selection, on the left is the host’s portrait in an evil pose on the right is the selected murder intent and the portrait of the selected target]*  

There are some additional options you can pick depending on the activity type as well, these often have a cost attached to them in exchange for improving the activity, or if you’re low on cash you can lower them to have a slightly less impressive time.  

Often these options will tie into the quality of rewards with the activity so that you get out something proportional to what you put in, other options tie into what characters will be automatically added to your entourage and invited to your activity.  

![9-attendants.png](https://forumcontent.paradoxplaza.com/public/949390/9-attendants.png "9-attendants.png")


*[At the bottom is two icons for activity option categories, above them is the current cost, and at the top is the current option and its effects and radio buttons to change to different options in the current category]*  

Each activity option, and the activity itself, can be scripted to invite people to your entourage and they will try to add people who are relevant to the activity type. Additionally most activities will automatically invite anyone in your entourage to the activity as a guest, not all activities do this, such as Playdates, because it would be pretty weird for your Travel Leader and Bodyguards to come and hang out at a kids party…  

Speaking of your guests, let's take a look at who we want to invite to our activities!  


![10-invite-groups.png](https://forumcontent.paradoxplaza.com/public/949354/10-invite-groups.png "10-invite-groups.png")


*[On the left is the list of different activity invite groups, along with an explanation of who is good to invite to a Hunt and a warning about inviting too many people. On the right is a list of invited characters and their portrait etc]*  

We decided to go down the route of having various categories of guests you can invite, this is primarily set up to reduce micromanagement and let you invite groups of relevant people. As most of the time you would like everyone who meets some category to be invited.  

Each character has an acceptance chance and an estimated travel time, if they can not make it at all they are likely to decline outright.  
There is also a limit to how many characters can attend a given activity, this depends on the activity type with larger festivities like Weddings and Tournaments allowing more people than a Hunt, if you go above the cap then guests invited with a less important role will be filtered out first.  

Once the activity has started you can still invite any character manually via character interaction, so you can invite people these groups don’t catch such as your friends in Multiplayer.  

Certain activities have one or more special Honorary Guests, these are guests who the activity itself is centered around such as the Honored Guest in a Feast or the two spouses in a Grand Wedding. Depending on the activity type these special guests are either selected by you from your attending guests or are automatically filled such as in a Grand Wedding.  

These Honorary Guests are much more likely to agree to attend an activity, and for some of them they might even be required to attend and you can not plan the activity if they don’t. Once the activity begins it will wait for the host and all the Honorary Guests to arrive before progressing to the festivities, less important guests who set out but do not make it get removed from the activity because it is deeply rude to be 3 months late to my party [@Wokeg](https://forum.paradoxplaza.com/forum/members/1325927/) god damn it can’t you turn up on time??  

Now that our planning is complete we now move onward to our destination, since we hosted the Hunt outside of our capital we naturally need to travel to it.  

![11-map-entity.png](https://forumcontent.paradoxplaza.com/public/949355/11-map-entity.png "11-map-entity.png")


Most activity types have a unique map entity shown in the province where you choose to host, here I’m Hunting in a province without a holding but we can see the Hunting tents still!  

![12-yourhunt1.png](https://forumcontent.paradoxplaza.com/public/949356/12-yourhunt1.png "12-yourhunt1.png")



I’m going to break this image down a bit section by section, in the center we have the main stage which has a background and set of characters based on the current state of the activity.  

Right now it is me traveling towards my Hunt on my trusty steed now finally modeled in game!  
Once I arrive I get to see my other hunters and a background based on the type of hunt I do, the location and more!  

![13-yourhunt2.png](https://forumcontent.paradoxplaza.com/public/949357/13-yourhunt2.png "13-yourhunt2.png")



At the bottom we’ve got quite a few more elements, going from left to right we first see our current state in the Hunt. There are three states you can be in during an activity:  


- Travel: You are traveling to the next phase’s destination, if two phases are held consecutively at the same location there is no travel
- Waiting: You are at the destination and passively waiting for the phase to become active, depending on the activity you will get different interactions here, many are events that revolve around the guests and your intent. Some activities skip this phase once everyone has arrived, this is mainly for thematic reasons as it makes little sense to wait another month to start hunting when everyone is there with their bow in hand already.
- Active: You are at the destination and the phase is in full swing, this can be a contest in a Tournament, Hunting your prey, or engaged in a Tour stop. This is where you get events very specific to this activity and your current phase.

Below that we have information on our current intent which we are free to change at any time during the activity, as long as there isn’t currently an event open.  

For Hunts we have the success chance widget which shows how likely we are to succeed in our hunt at all. Every activity can contain custom UI elements specific to that activity type to help convey information. For example Tours instead have a bar showing how much you have managed to meet the goal of your Tour type, if you’ve been particularly majestic or really managed to intimidate people.  

For the modders out there these plugin widgets are fully scripted and can be applied both to the ongoing activity window and to the activity planner itself too for any custom planning information.  

Above the success chance we have the activity timeline, this shows you which phase you are currently in, and what you are progressing too. The first and last are always planning and the conclusion respectively.  

Around your current phase there is a progress wheel which ticks up each week and has a chance to fire an activity pulse action, what our designers have lovingly shortened to Apas, these pulse actions are smaller events more akin to Toasts in which you get informed about what people in the activity are getting up to.  

It may be you make extra progress in tracking the boar in your Hunt, it could be two guests getting more friendly with each other, your Spouse showing off at your Feast, or someone gifting you a Trinket in honor of your Grand Wedding.  

All of these appear in the top right of the screen and last for a few seconds before fading away, the UI for these actions is currently work in progress and will change before final release.  


![14-yourhunt3.png](https://forumcontent.paradoxplaza.com/public/949358/14-yourhunt3.png "14-yourhunt3.png")



And all of these, along with other events that take place related to your activity, generate log entries which are opened using the button in the bottom right.  
These log entries let you look through an activity to see what has been going on, this is especially useful as log entries can refer to other characters and what they are doing too.  

![15-hunt-log.png](https://forumcontent.paradoxplaza.com/public/949359/15-hunt-log.png "15-hunt-log.png")



Speaking of activity events, here is how they appear. They operate much like our regular events but take place inside the activity window itself so all the information you need about them is at hand.  


![16-activity-event.png](https://forumcontent.paradoxplaza.com/public/949360/16-activity-event.png "16-activity-event.png")



Once the last phase in an activity is complete we enter into the conclusion, here we tie up the narrative threads and give you a summary of the most important effects that impacted you during this activity.  

![17-activity-conclusion.png](https://forumcontent.paradoxplaza.com/public/949391/17-activity-conclusion.png "17-activity-conclusion.png")


*[Conclusion screen of a hunt, here we see the effects that happened on the left alongside relevant artifacts and traits. To the right we have some of the involved characters.]*  

A lot of the activity system is very open to mods, I’ll be going further in depth into a variety of changes we’ve made with the script language in a future modding dev diary, but we’re excited to see how both us and our modders can expand the system with new fun activities!  

---

### Hunts​

Hey! I’m Joe, or [@PDX_Chop](https://forum.paradoxplaza.com/forum/members/1377369/) here on the forums, one of the Game Designers working on CK3. Today we’ll be dusting off our boar spears and hooding our falcons, ready to take a look at the new and improved Hunt activity!  

Hunts, of course, provide opportunities to prove your vigor, gain some sweet Prestige, and take a load of Stress off — with the odd accident thrown in for good measure.  

With the Location and Activities overhauls coming with Tours and Tournaments, we took the chance to revamp Hunts, tying them more closely to the map and improving the experience. For anyone expecting Hunts would have only minor facelifts, hold on to your bycockets — it’s time to stalk our quarry!  

As mentioned above, you can pick what Type of Hunt to host. Legendary is now only available once your character has caught ‘the bug’, and only in places you suspect the mythical animal to actually be - more on this later.  

![18-hunt-type2.png](https://forumcontent.paradoxplaza.com/public/949362/18-hunt-type2.png "18-hunt-type2.png")


*[Image - Type selection]*  

While we have added lots of new content to the base Hunts in the free update, Falconry will also be available to owners of the Tours & Tournaments expansion, with its own events, equal sex participation, and a separate Hunter Trait track - more on this later too.  

Secondly, you now decide where it is you want to hunt, with a variety of factors playing into your selection. You can now host a Hunt in any Barony within your subrealm, traveling to the Location and back.  

![19-location-selection.png](https://forumcontent.paradoxplaza.com/public/949363/19-location-selection.png "19-location-selection.png")


*[Image - Location selection]*  

The planner will show you the best places in your realm to hold a Hunt, with tooltips giving a rough breakdown of the reasons. Now you might well ask, but what do these pluses and minuses actually mean? And what on earth is a Sighting? I’m glad you asked.  


**Success Chance**  

While in the past, you would receive a few random events and then a summary, Hunts now have a formal structure, from leaving your hunting camp to coming home, with opportunities to affect the outcome and decide how to proceed along the way.  

The Success Chance is an abstraction of a variety of factors which play into how likely you are to actually succeed.  

![20-success-chance.png](https://forumcontent.paradoxplaza.com/public/949364/20-success-chance.png "20-success-chance.png")


*[Image - Success Chance]*  

The main factors affecting your Success Chance are your Hunting skills, the Aptitude of your Master of the Hunt, and the chosen Location.  

Master of the Hunt is now available to all tiers; given its new importance in the activity it didn’t make sense to limit it to only Kings and above anymore.  

You can now focus on developing specific holdings for Hunts, and offset penalties in Locations which might not be naturally advantageous. For example, high Development or a recently held Hunt reduces Success Chance in a Barony, while a Royal Reserves Building or Sighting will increase it.  

![21-hunting-grounds.png](https://forumcontent.paradoxplaza.com/public/949365/21-hunting-grounds.png "21-hunting-grounds.png")


*[Image - Hunting Grounds]*  

Since you can host Hunts in your vassal’s lands, it’s also possible to take advantage of their holdings — it’s good to be king.  

At the end of the Hunt, all the choices you have made will affect the chance that you successfully tracked the animal.  


**Sightings**  

Sightings represent rumors of abundant or rare game in a County, temporarily raising the Success Chance of Hunts held there, and are only usable by the one who received them. As Hunts held without a Sighting give no guarantee of specific animals, Sightings are also guaranteed opportunities to pursue prestigious game.  

![22-sighting-event.png](https://forumcontent.paradoxplaza.com/public/949367/22-sighting-event.png "22-sighting-event.png")


*[Image - Sighting event]*  

Sighting events may fire if you have employed a Master of the Hunt or have a Hunter at court, with their frequency and location influenced by your Lifestyle experience, Master of the Hunt Aptitude, and certain Buildings.  

![23-sighting-modifier.png](https://forumcontent.paradoxplaza.com/public/949368/23-sighting-modifier.png "23-sighting-modifier.png")


*[Image - Sighting modifier]*  

Legendary Hunts are also explicitly tied to Legendary Sightings, which are now required for such a Hunt to be hosted, and can be received either from events within the Hunt activity or from Sighting events once you have first spotted a legendary beastie.  


**Animals & Peril**  

As you may have noticed above, the Prestige rewards are now also more explicitly tied to the animal you are hunting. Peril is an abstraction of the specific dangers associated with an animal; a boar is far more dangerous than a fox, but therein lies the glory.  

![24-animal-event.png](https://forumcontent.paradoxplaza.com/public/949369/24-animal-event.png "24-animal-event.png")


*[Image - Animal event]*  

When there is not a specific Sighting present, your gamemasters will suggest the most favorable animal to hunt on the day. You may also decide you want to hunt something else, for a small decrease to your Success Chance.  

A fox or hare Hunt is safer if you care less about Prestige, or you can go out of your way to track a wolf or stag to prove your mettle and impress your court. The choice of method will also affect the danger and skills used, will you ambush your prey with bows, or bring it to bay on horseback?  

![25-kill-event.png](https://forumcontent.paradoxplaza.com/public/949370/25-kill-event.png "25-kill-event.png")


*[Image - Kill event]*  

This danger will usually manifest in the outcome of a successful hunt, where you may decide how to bring the animal down. Single-handedly slaying a lion is an impressive feat, but shooting it or using the advantage of numbers will help stave off your heir’s succession.  

![26-successful-ending.png](https://forumcontent.paradoxplaza.com/public/949371/26-successful-ending.png "26-successful-ending.png")


*[Image - Successful ending event]*  

In addition to the Prestige gained from slaying the beast, more Perilous animals also increase the overall Prestige rewards of successful Hunts, generally produce rarer artifacts, and award more Hunter trait experience.  

It should also be mentioned that the rewards of Legendary hunts now also scale with the animal type: cornering the White Hare of Caerbannog is a feat, to be sure, but not quite as impressive as undoing the Black Leopard of Seoni.  

As a side note, the variety of animals has also been upped considerably, based on region and terrain, providing more regional flavor and bringing an end to the hordes of deer currently dominating the map. Examples include bison, roe, elk, gazelle, antelope, hyenas, and leopards.  


**Participation**  

As mentioned in the Type selection, only martial sexes will actively participate in standard Hunts and have opportunities to gain animal slaying Prestige, though non-martial sexes can still host, attend, and appear in events.  

The exception to martial sex requirements is Falconry, which was historically practiced by both sexes as a noble social pursuit, and thus open for all bird enthusiasts to enjoy.  


**Intents**  

In addition to the Stress loss and Prestige obtained by simply hosting or attending a Hunt, there is also a specific Intent: Slay Beast. Completing this intent will provide extra rewards if you personally take a hand in slaying the animal, and is thus only available to martial sexes on standard hunts.  

There are also several intents shared with the other revamped activities, namely:  


- Recreation
- Murder
- Seduce
- Befriend

The first is a general Stress reduction Intent; you want to unwind and enjoy the occasion. The others are targeted against specific guests, and offer social and unscrupulous opportunities.  

Historically, Hunts were a prime opening for murder and abduction —find a list of rulers who ‘accidentally’ ate a follower’s arrow or ‘fell’ from their horse and you’ll see what I mean. In short, you’d do well to watch who you invite to your Hunts if you are to avoid a sticky end, over and above the genuine risks of unfortunate accidents and rampaging beasts offered by the wild.  


**Hunter Trait**  

Speaking of Falconry, the Hunter trait has received some love too. Relying on RNG, hidden script, and reading the entrails of chickens to determine when your Trait will level up, is a thing of the past.  

![27-hunter-trait.png](https://forumcontent.paradoxplaza.com/public/949372/27-hunter-trait.png "27-hunter-trait.png")


*[Image - Trait]*  

It is also now split into two 'tracks', Venator and Falconer, representing the skills and knowledge of the respective pursuits.  

More on the above in a future dev diary! ![;)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Wink    ;)")  


**Art**  

Lots of gorgeous new art assets have been added to flesh out the Hunt, including skull and pelt trophy models to display in your Royal Court, event images, and even archery and hunting animations.  

![28-animations.gif](https://forumcontent.paradoxplaza.com/public/949373/28-animations.gif "28-animations.gif")


*[Image - Animations]*  

Thanks for reading, that’s all from me and hunts! It’s time to pass over to Trin and talk a bit about the reworked Pilgrimages.  

---

### Pilgrimages​


Hello ![:)](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 "Smile    :)") I am [@Trin Tragula](https://forum.paradoxplaza.com/forum/members/18587/), also known as Henrik, the Design Lead on CK3 and today I am here to talk about the new and improved Pilgrimage activity.  

The ambition for the Pilgrimage rework has been for us to provide a more full experience of what a pilgrimage would have been like, both for the pious characters of the game world as well as those who would take on a Pilgrimage more as an opportunity to see the world itself. With travel now taking place directly on the map we are able to make this the journey it is meant to be. Pilgrimages also make use of the new activity system to let you decide in what way you undertake this activity.  

#### Planning your Pilgrimage​


Much like Tours the Pilgrimage will have a bar that measures how successful you have been in acting in accordance with the Pilgrimage type. The type, as well as your intent and options will determine what rewards you can reap by engaging in the activity as well as what type of content you will get on your way there. The size of the reward, as well as the costs are dependent on how far away the holy site you are aiming to visit is.  

#### Types​

![29-pilgrimage-type-selection.png](https://forumcontent.paradoxplaza.com/public/949374/29-pilgrimage-type-selection.png "29-pilgrimage-type-selection.png")


*[Image - Type Selection]*  

There are 3 types of Pilgrimage that a character can embark on: Pious, Worldly and Hajj, these types govern what rewards you can expect from your Pilgrimage as well as what choices you will be presented with on your way to the Holy Site.  


A Pious Pilgrimage is one where the pilgrimage and the holy site are a means to spiritual growth and enlightenment (or at least to appear as a devout ruler). During your journey, as well as at the destination you will be presented with events with a religious theme and if you act in accordance to what is expected of you there will be rewards mainly in the form of piety.  


![30-hajj-event.png](https://forumcontent.paradoxplaza.com/public/949375/30-hajj-event.png "30-hajj-event.png")


*[Image - Hajj Event]*  

The Hajj is only available to Muslim characters and a Hajj must always be targeting the Holy Site of Mecca. Once a Muslim character has undertaken a Hajj they can later in life also perform other Pilgrimages to the Holy Sites of their faith. A Hajj is otherwise similar to a Pious Pilgrimage and differs from the other types mainly by what happens when you are at the Holy Site (what you do here follows a more set order than for the standard pilgrimages, though you still have choice in how you confront these expected rituals). Once completed the Hajj also gives the Hajj trait.  


![31-hajj-event2.png](https://forumcontent.paradoxplaza.com/public/949376/31-hajj-event2.png "31-hajj-event2.png")


*[Image - Hajj Event]*  

The new activity also comes with new special clothing made for when you have performed the traditional Hajj.  


![31.5-new-clothing.png](https://forumcontent.paradoxplaza.com/public/949379/31.5-new-clothing.png "31.5-new-clothing.png")



Undertaking a Worldly Pilgrimage means that the journey will be a goal in itself more than a spiritual awakening. Your character will be given opportunities to interact with the locals of the lands you pass through and by engaging with them you can increase what you get out of the Pilgrimage. A worldly Pilgrimage will still give you piety, you are undertaking a holy ritual, but less so than a pious pilgrim, instead you will also gain Cultural acceptance as well as opinions of other cultures and faiths.  

![32-worldly-pilgrimage-event.png](https://forumcontent.paradoxplaza.com/public/949380/32-worldly-pilgrimage-event.png "32-worldly-pilgrimage-event.png")


*[Image - Worldly Pilgrimage Event]*  


#### ​

#### Activity Options​

Like all activities in the new system Pilgrimages have two option types, these mainly affect the speed and rewards of the activity.  

**Fidelity**: The Fidelity option is about how true you want to stay to an ideal pilgrimage. In some ways it is a measure of how seriously you take the holy journey itself. This option lets you trade speed for higher rewards. You can choose to go longer and dwell on your spiritual journey or you can choose to go faster at the cost of lower rewards at the end.  


![33-pilgrimage-activity-options.png](https://forumcontent.paradoxplaza.com/public/949381/33-pilgrimage-activity-options.png "33-pilgrimage-activity-options.png")


*[Image - Pilgrimage Activity Options]*  

**Pomp**: This option governs the size of your entourage. You can choose to go alone, and save on costs as well as increasing the perceived piousness of your endeavor, if taking a bigger risk on your way there. On the other end of the spectrum you can spend more and take most of your court with you on this journey, greatly increasing your safety and the public perception of your Pilgrimage (which _also_ increases the final rewards).  


#### Intents​

Separate from the type of Pilgrimage is the intent, which is individual to each attending character. Pilgrimages offer 3 different intents which will affect what opportunities you are presented with both on your way to the Holy Site and what happens when you get there.  

![34-reflection-event.png](https://forumcontent.paradoxplaza.com/public/949382/34-reflection-event.png "34-reflection-event.png")


*[Image - Reflection Event]*  

**Reflection**: The reflection intent focuses on content relating to the spiritual and intellectual growth of your character. Apart from piety it is very likely your character will also lose a fair amount of stress with this intent.  

![35-altruism-event.png](https://forumcontent.paradoxplaza.com/public/949383/35-altruism-event.png "35-altruism-event.png")


*[Image - Altruism Event]*  

**Altruism**: This intent is one you will remember from the Tours development diary. The Altruism intent will offer you opportunities to show your piousness through your generosity. Leading to opportunities to increase your piety as well as popular opinion. Zealous, Generous and Improvident characters will also lose stress with this option.  

![36-zealotry-event.png](https://forumcontent.paradoxplaza.com/public/949384/36-zealotry-event.png "36-zealotry-event.png")


*[Image - Zealotry Event]*  

**Zealotry**: For those with a strong religious conviction a pilgrimage is not just an opportunity to learn about the faith, it is also when you can spread your own ideas of the divine. Zealots will gain piety through engaging in religious debates and will be given opportunities to convert characters both en route and at the Holy Site itself.  

#### The act of Pilgrimage and the arrival at the Holy Site​


![37-travel-event-intent-effect.png](https://forumcontent.paradoxplaza.com/public/949385/37-travel-event-intent-effect.png "37-travel-event-intent-effect.png")


*[Image - Travel Event with Pilgrimage intent effects]*  

Once you have planned the activity you will embark on the journey itself, encountering both the usual travel dangers and other interactions, as well as engaging with opportunities relating to the choices you made for the activity.  

![38-holy-site-arrival.png](https://forumcontent.paradoxplaza.com/public/949386/38-holy-site-arrival.png "38-holy-site-arrival.png")


*[Image - Holy Site Arrival]*  


Unlike a Feast or a Tournament the Pilgrimage activity can be said to be ongoing as soon as you leave your capital, but of course the Holy Site is your goal and this is where you will be able to make more impactful choices relating to the success of your activity.  

![39-pilgrimage-conclusion.png](https://forumcontent.paradoxplaza.com/public/949387/39-pilgrimage-conclusion.png "39-pilgrimage-conclusion.png")



The Pilgrim Trait  

![40-pilgrim-trait.png](https://forumcontent.paradoxplaza.com/public/949388/40-pilgrim-trait.png "40-pilgrim-trait.png")


*[Image - Pilgrim Trait Experience Track]*  

At your destination is also where you will pick up the Pilgrim trait. Unlike the one for Hunts this trait has only one experience track, which increases with every undertaken Pilgrimage, reflecting how the act of Pilgrimages becomes an increasingly important aspect of your character's life and reputation.  

### Conclusion​

Thanks for reading everyone! We hope these details have got you excited to play some of the reworked activities, we’ll be reading and answering questions here today and we’ll be talking more about the other reworked activities and the new Grand Activities in the future.  

However, for next week we’re taking a look at the much requested Regency mechanics and showing how elegant the fashion in your Empire can be!

<!-- artifact:reactions:start -->
- 276 Love
- 168 Like
- 12 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)**
Role: Former Senior Programmer - Crusader Kings 3
Badges: 99
Reaction score: 8,575

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
