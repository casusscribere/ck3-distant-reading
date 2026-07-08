---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1577736/"
forum_thread_id: 1577736
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 123
title: "Dev Diary #123 – Hastiluding for Glory"
dd_date: 2023-04-11
author_handle: Paradoksalny Kierownik
expansion: Tours and Tournaments
patch: Patch 1.9
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 8513
inline_image_count: 73
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1577736'
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
    location: raw_lines_~28_to_156
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_155
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2287.jpg?1681208813
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_158_to_160
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_930_to_935
    action: preserved_and_flagged
    counts:
      Love: 214
      Like: 112
      (unlabeled — rendered as base64 data URI): 4
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_943_to_1045
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_1046_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2287.jpg?1681208813)
<!-- artifact:thread_banner:end -->

# Dev Diary #123 – Hastiluding for Glory

<!-- artifact:thread_metadata:start -->
- Thread starter [Paradoksalny Kierownik](https://forum.paradoxplaza.com/forum/members/paradoksalny-kierownik.1725641/)
- Start date [Apr 11, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-123-hastiluding-for-glory.1577736/)
<!-- artifact:thread_metadata:end -->

Mine lords, mine ladies, and everybody else not seated upon a cushion! On this day! On this day thee find thineselves equals, for thee are all equally blessed! We haveth the privilege, nay, the joy of giveth introduction to a most joyous occasion. Our exalted majesty hath proclaimed that a tourney is to be held! Right here! In nary a moon thine village shalt be hosts to a Grand Tourney! Rise, rise to this momentous occasion! Rejoice and partake in the glorious festivities!  

Hello everyone, and welcome to Developer Diary#123! We are your hosts: Elisabeth, also known as Oxycoon - a programmer on Crusader Kings 3; Nick, also known as Noodle - a designer on Crusader Kings 3; and Jon, also known as… just Jon - a 2D UI artist on Crusader Kings 3, and today we are discussing Grand Activities. Specifically the Grand Tournament.  


### Visions of a Cloth of Gold​

The commonly-held concept of a Medieval tournament is pretty straightforward. Knights in glittering armour, pennants streaming from their lances. A gallop, a tilt, a crash, and a victor saluting the crowd. It’s an evocative image, but it’s also quite narrow in its application. CK3 isn’t just about a High Medieval western European knight on his charger: it’s also about the Indian archer taking aim at a target, the Persian wrestler throwing his opponent to the floor, the steppe horseman thundering around a course. Our scope is wide and encompasses so many cultures, so what we offer with a Tournament must also encompass this rich and varied tapestry of humanity.  

Sport and sporting occasions have been a part of humanity since time immemorial, with feats of strength, endurance and agility turning up in every nook and cranny across the globe. Anywhere humans exist, there will always be someone claiming they can best others in feats with increasingly esoteric rulesets - though, of course, most cultures prefer something more akin to ‘who can run the fastest’ or ‘who can pick up this big rock’ rather than the West Country of England, where people throw themselves down a cliff in pursuit of some cheese. You must always remember that no matter how arcane and obscure your sport gets, at least you won’t get injured chasing a block of coagulated milk down a hill. But I digress.  

In a Tournament, the actual act of getting atop your charger and splintering a lance on the chest of an adversary might play second fiddle to wandering around and engaging with the great and the good who have come from all over the region to partake in your hospitality. We’ve endeavoured to present Tournaments as less of a simple procession of meatheads bonking each other with blunted swords and more of the major sporting and cultural festivals that they were. That’s not to say there’s not fame and prizes to be won in the events, of course, but a good ruler will recognise that their own personal glory could be sacrificed in order to bolster their realm in other ways.  

A final relevant piece of this puzzle is exactly how you interact with the Tournaments themselves. We’ve done ‘contests’ between characters before through our single combat system and playing chess in Fate of Iberia. Those are quite tit-for-tit, locked-in engagements: you make your move, your opponent makes theirs. They’re fun and engaging, but we didn’t want to retread our steps with them by just making a bigger version of what we already have. We’ll talk about how Tournaments are laid out a bit later, but for now…  

### I’ll invite myself!​

There are a few unique aspects of the Grand Tournament activity type. First is that it is an open activity, meaning that you do not send invitations to this activity, but characters will instead decide for themselves if they want to come. As a player you will be able to choose to attend any Tournament happening nearby, provided you can get there in time, and the same is true for any AI when you host a tournament. Another is that it makes use of the special activity locales; we will get more into what this means a bit further down.  

Let us see what being an open tournament means on the map.  

![tournament-invitation-3.png](https://forumcontent.paradoxplaza.com/public/953703/tournament-invitation-3.png "tournament-invitation-3.png")



*Duke Vratislav II hosting a Grand Tournament, King Boleslaw II’s Point of View  

Anyone* can join an Open Activity, and you will be able to see them on the map with a big, flashy banner so it catches your attention. If you actively want to participate in Tournaments there is this handy little toggle you can tick to be notified when there is one within range which you can travel to. This notification is enabled by default.  

![tournament-invitation.png](https://forumcontent.paradoxplaza.com/public/953704/tournament-invitation.png "tournament-invitation.png")


*Count of Zatec eyeing his liege’s Tournament*  

![tournament-invitation-2.png](https://forumcontent.paradoxplaza.com/public/953705/tournament-invitation-2.png "tournament-invitation-2.png")


*Count of Zatec eyeing his liege’s Tournament 2*  

Of course, you might not reach the tournament in time once one is hosted, so take care to make the appropriate travel arrangements to get there in time. If you have not arrived by the time the first contest begins, you will turn the entourage back. While conceptually a participant could arrive late and join in the following contests, we decided not to do this in order to maintain a consistency between the activities as well as reduce needless complexity in handling guest arrival and the like.  


### The Spice of Life​

In order to accurately represent the earlier-mentioned huge variation in cultural sporting events, we chose a selection of eight different events to tickle your fancy within Tours and Tournaments, a selection of the most widely-applicable and most famous of their ilk. Each one offers its own unique challenges, opportunities and even availability. For example, whilst a Joust might not fit in the Tibetan Plateau, Archery is something enjoyed by a vast array of cultures, to the point where you’d be hard pressed to find any that have never encountered the concept of a friendly shooting contest.  

Having this eight - Melee, Archery, Recital, Board Games, Joust, Wrestling, Duel and Horse Race - also allows us to open up exactly who can partake. Under standard gamerules it’s not possible to have a woman participate in the Joust, for example, but even the staunchest supporter of traditional gender roles would admit that a Recital has no such issue. It also opens up options for specialists of a different kind: if you’re not into physical shows of strength, you could even just organise what Rageair affectionately likes to describe as a ‘Tournament for Nerds’ by setting up an event that only has a Recital and Board Games.  

![Contests 1.png](https://forumcontent.paradoxplaza.com/public/953706/Contests 1.png "Contests 1.png")


![Contests 2.png](https://forumcontent.paradoxplaza.com/public/953707/Contests 2.png "Contests 2.png")


 *The Contests*  

There’s also variation within the contests themselves, as you might expect from a rather diverse selection of sporting events. Each Contest falls into one of four Formats: Knock-Out, Teams, Turns and Race. As such, your path to victory will vary between each of these. A Horse Race is a very simple and rather short Contest, for example, but a Contest with rounds like Duels or Jousts has you facing multiple opponents in turn, a much longer form of spectacle. More on that later.  

Finally, there’s also some changes as time goes on. One of the things you as a community have asked for repeatedly is more delineation between early ages and late ones as the game progresses, and we’ve tried to reflect that in some small way in Tournaments. In the early start date, you might find your Tournaments only capable of hosting a single Contest.  


![Contest Era 1.png](https://forumcontent.paradoxplaza.com/public/953708/Contest Era 1.png "Contest Era 1.png")


Later on, however, Tournaments have evolved past being simply a way to train for bopping other folks in the head a bit more effectively, and have become bona fide festivals. All people from all walks of life, the young and the old, the frail and the fit, the peasants and the upper crust, come to Tournaments to take in the sights and the sounds. The prospect of high-quality sporting entertainment is just one attraction amongst the revelry, and the scale - and cost! - of such an event swells accordingly.  


![Contest Era 2.png](https://forumcontent.paradoxplaza.com/public/953709/Contest Era 2.png "Contest Era 2.png")



Of course, you _can_ still hold smaller Tournaments in the later eras, if you don’t fancy incurring the costs, but as you unlock them you will always have the option to throw the biggest sporting bonanza you possibly can. It’s also worth noting that the amount of Contests you have can also vary, as seen in the screenshot, by such sundries as Cultural Traditions. The French, for example, were _very_ into the pomp and magnificence of the tourney, and so they unlock a slot an era sooner than others do.  


#### Location, location, location​

![tournament_planning_1.png](https://forumcontent.paradoxplaza.com/public/953710/tournament_planning_1.png "tournament_planning_1.png")


*Tournament Location Planning  

Tournaments benefit from having infrastructure, that is to say: buildings, to support them. Specific contests within a Tournament will get cheaper by having already built supporting buildings within the barony that hosts it. This can substantially reduce the cost of a tournament within said barony, as the hosting barony will not have to construct said buildings before the tournament and tear them down afterwards. Want to host a Joust or a Horse Race? Already having a Jousting Grounds constructed within will cut the cost of hosting these contests in half. Other buildings can reduce the cost of hosting the tournament itself, such as the Royal Armories Duchy Building line reducing the cost by 25%! Having a barony planned for hosting Tournaments with appropriate buildings will help with managing the costs.*  


![tournament_planning_7.png](https://forumcontent.paradoxplaza.com/public/953711/tournament_planning_7.png "tournament_planning_7.png")


*A Late Medieval Era tournament with no discounts*  

#### Planning a spectacle​

Once we have found our location, we can select the contests we want. As mentioned previously, we have eight contests to choose from.  


![tournament_planning_8.png](https://forumcontent.paradoxplaza.com/public/953714/tournament_planning_8.png "tournament_planning_8.png")


*Late Medieval Era contest selection*  

Contests have differing costs to them. A Joust, being a whole deal with a panoply of armor, a particularly antsy horse and a lance of indeterminately massive size, is naturally more expensive to host than, say, a Recital, as anyone who has ever gone to an open mic on a Friday night will sadly attest to.  


![tournament_planning_2.png](https://forumcontent.paradoxplaza.com/public/953715/tournament_planning_2.png "tournament_planning_2.png")


*A Early Medieval Era contests with spectate option mouseover*  
During the contest planning you can also select whether or not you wish to compete in the contest with a simple toggle. You can toggle between these at any time, except when a contest is currently ongoing.  


### Locales, et al​

As mentioned, it’s not just about the events at a Tournament. A key part of the whole deal is interacting with others and experiencing the Tournament itself.  


![Locale window complete with plugin widgets.png](https://forumcontent.paradoxplaza.com/public/953757/Locale window complete with plugin widgets.png "Locale window complete with plugin widgets.png")


*The Locale Scene*  

When you attend a Grand Tournament, you are met with what we call the Locale view. This is a new way to experience certain activities, unique to the Grand Tournaments, and stretches across the entire screen while you are interacting with content in the activity.  

In the downtime before and between contests, you have the option of interacting with the various locale buildings. So what is the purpose of these buildings? Well, it depends on what you are after in this particular tournament. The buildings each have a pool of unique events, as well as some shared ones, weighted based on the building in question and which intent you have selected. The short of it is: mechanically you will choose what sort of events you want to pursue.  

One building type favours stress reducing events, another favours improving your character’s chances of winning the upcoming contest and another can even give you knights to recruit! As you would imagine, staggering into the Tavern is eminently more likely to trigger the likes of a game of dice or even a drunken brawl than a Church is, unless you’ve been to significantly more lit religious ceremonies than I’m used to.  

For the the Tournament we have selected to have the following buildings available:  


- The Settlement
- Religious Building
- Tourney Grounds
- Tavern
- Artisan’s Quarter
- The Camp

There is a certain cooldown to interacting with a specific building, and a cooldown to interacting with the locales in general, but you can pick and choose which building you wish to interact with. This also means if you arrive early, you have the time to interact with more buildings, giving you an advantage over your competitors. Furthermore, if you do not pick a locale to interact with, one of the locales will be automatically picked for you, weighted by your intent, so you don’t *have* to have the APM of a competitive RTS player to stay on top of the locales.  

We’ll talk more about the visuals and how we constructed the Locale scene later. For now, let’s take a quick dive into how Tournaments actually proceed.  


### A Quick Bout​

Now, the actual process of going through a Tournament has quite a few facets to it and I don’t want to bore you all too much with a blow-by-blow account of how I spent hundreds of the realm’s gold to take first place in an archery competition.  

Wait, yes I do. Let’s do that.  

I am playing as Grand Prince Vseslav II of Polotsk, and I have a bit too much gold burning a hole in my pocket. What better thing to spend it on than a pointless flex of my martial ability?  

The Grand Tournament is to be held in Polotsk, my capital province, a somewhat substandard choice given the thick woodland. I fancy an Archery contest this time. Never mind that I have no real aptitude for it, having a mighty Prowess of 1. No, no, I must prove my skill with the mighty yew!  

![Accommodations _ Prizes.png](https://forumcontent.paradoxplaza.com/public/953717/Accommodations _ Prizes.png "Accommodations _ Prizes.png")


*Accomodations and Prizes*  

I pick from my setup options. Ramshackle Tents will do just fine for my visitors, but the prizes, now *those* need to be glorious. I’m going to win, after all.  

A quick interlude here to explain contest formats! We’re partaking in an Archery contest, which is rather straightforward: a group of people compete against each other, and then once that phase is over, one of them wins. This is also seen in Horse Racing and also Recital.  

It isn’t quite as simple with some others, however. A contest like a Duel or a Joust has competitors progressing through a knockout format, whittling their numbers down slowly until one finally triumphs from the final two. The same is true for Wrestling and Board Games.  

The final, and most unique setup, involves the Melee. Often thought to be the pre-eminent example of Medieval European tourneying until the advent of jousting, a Melee involved a mock battle between two teams of participants. Chaotic, huge and dangerous, melees often covered large distances and had indeterminate victory conditions. In-game, this involves you being sorted into a team, with your collective score being tied in with your teammates’.  

Anyway, enough of this dilly-dallying!  

#### First Hurdles​

![Qualification.png](https://forumcontent.paradoxplaza.com/public/953718/Qualification.png "Qualification.png")


*Qualification Window*  


Before the guests begin to trickle in, I am naturally considered the most favoured contestant in the area! That the rest haven’t even arrived in said area yet is completely by-the-by, and frankly I think it’s rude you even mention it.  

The very first challenge I have to pass is being considered worthy enough to actually participate. Tournaments in bigger realms can have over a hundred people attending, so the wheat needs to be separated from the chaff. Somewhat insultingly, my pathetic Prowess and complete lack of existing martial practice have left my qualification very much in doubt. If you squint a bit, you might be able to see the tiny sliver of bar that has been filled up. The first order of business is to pump those numbers up!  

![A Glorious Guest.png](https://forumcontent.paradoxplaza.com/public/953719/A Glorious Guest.png "A Glorious Guest.png")


*A Glorious Guest event*  

I wander into the Tournament Grounds and who should I find but a famed Tourney knight! Simeon might be a little portly, but his ability is undoubted. Perhaps he can teach me a thing or two?  


![Drat.png](https://forumcontent.paradoxplaza.com/public/953721/Drat.png "Drat.png")


*Drat!*  

Drat.  

With time running out, I dive into the Artisan’s Quarters. I come across Yelisay, the local bowyer - as a side note, all Tournaments have a set of local artisans and religious figures that ply their trade at said Tournament for the entire duration of the event - and lo and behold, he happens to have a little something for sale.  


![Brace Yourself.png](https://forumcontent.paradoxplaza.com/public/953722/Brace Yourself.png "Brace Yourself.png")


*Brace Yourself event*  

I’d be a fool to turn it down! What’s a little more gold shovelled out of the realm’s coffers, after all?  

As guests pour in, the qualification adjusts itself. If I would have been a noted archer, for example, it’s possible that I would have qualified right off the bat without having to do anything, leaving me free to wander the nearby village or relax at the tavern. If lots of skilled participants turned up, though, I might have had to find a few ways to increase my score regardless.  

In this case, however, my lack of ability is masked at least somewhat by the correspondingly rubbish competition. As such, it only takes this addition of my bracer - along with a quick trip to the tavern to put a tab on for my competitors - to have me well in control of my destiny:  

![Another Round.png](https://forumcontent.paradoxplaza.com/public/953723/Another Round.png "Another Round.png")


*Another Round event  


![Never Again.png](https://forumcontent.paradoxplaza.com/public/953724/Never Again.png "Never Again.png")


Never again toast  

Success! All shall soon know my might, my poise, and my aim!  


![Qualified Threshold.png](https://forumcontent.paradoxplaza.com/public/953725/Qualified Threshold.png "Qualified Threshold.png")


Successful Qualification*  


Look at that! We’re on the verge of qualifying. The adjudicators allow us in, and up opens the Contest window.  

#### The Beautiful Game​

![Archery Contest Begins.png](https://forumcontent.paradoxplaza.com/public/953726/Archery Contest Begins.png "Archery Contest Begins.png")


*Contest Begins event*  

Pretty, isn’t it?  

Not content with throwing away enough gold to bury the average family, I decide to have a little wager. And who else to bet on but the best?  


![Bet on myself.png](https://forumcontent.paradoxplaza.com/public/953727/Bet on myself.png "Bet on myself.png")


*Bet on myself*  


I even find the time to, in accordance with my intent to win the Tournament, attempt a little skullduggery:  


![Sabotage.png](https://forumcontent.paradoxplaza.com/public/953729/Sabotage.png "Sabotage.png")


*Sabotage Event  

![Sabotage Result.png](https://forumcontent.paradoxplaza.com/public/953730/Sabotage Result.png "Sabotage Result.png")


Sabotage Event Outcome*  

Take that, Count Ovtay!  

I won’t take you through every happening, but suffice to say a bystander got hit with an arrow and I rather failed with my attempt to liven things up with a particularly outlandish attempt. Whether those two things are related, I suppose nobody will ever know.  

#### A Pivotal Time​


At the sharp end of the contest, it has really come down to it. I am doing rather well, but at a given point in a Contest an event called a Pivotal Moment will trigger. This is a very straightforward, very simple event: you will have the opportunity to improve your score, but you must beware, for we have one small new mechanical addition to the game that is worth mentioning here.  

Previously, if a scripter wanted to perform a skill duel - as in, comparing a skill like Prowess or Martial against another character’s corresponding skill or a set value - we could only perform it against another single skill. Now, thanks to the quick work of our coder Joror, we can duel multiple skills against each other. The game will take the average of the two (or more; theoretically you can use literally all skills at once) skills and pit them against each other.  

This allows us (and modders!) to check skills against each other in a much more flexible manner. Before, if you wanted to check two character’s skill against each other in a theological debate - for example - you would have to choose between Learning and Diplomacy. Now, you can combine them, giving a truer representation of the rigours of intellectual discourse.  

![Prowess Challenge.png](https://forumcontent.paradoxplaza.com/public/953731/Prowess Challenge.png "Prowess Challenge.png")



You will see plenty of use of this small new script feature across this expansion, as it has proved quite handy!  

To take us back to the matter at hand, in this even all options are skill duels, and there’s nowhere to hide. The closest is the fourth option, which only takes from a single skill. The rest are all combined skill duels, giving you a chance utilise a skill not normally associated with the event you are currently engaged in. For example, during a Recital you might attempt to combine your usual Diplomacy with a little Intrigue, or opt for your experience in battle with a rousing Martial-led verse. Here, I’m not really good at anything, so I try to maintain my advantage.  


![Striking True.png](https://forumcontent.paradoxplaza.com/public/953732/Striking True.png "Striking True.png")


*Striking True event*  

Arrow! Black arrow! I have saved you to the last-  


![Arrow Target Hit.png](https://forumcontent.paradoxplaza.com/public/953733/Arrow Target Hit.png "Arrow Target Hit.png")


*Arrow Target Hit*  

Well, I mean, it could be worse. I could have missed the target entirely.  

![Highly Strung.png](https://forumcontent.paradoxplaza.com/public/953734/Highly Strung.png "Highly Strung.png")


*Highly Strung event*  

I was already amongst the front runners, so frankly maintaining my lead is a fairly good outcome. The last few competitors take their shot and…  

![Contest Winner.png](https://forumcontent.paradoxplaza.com/public/953735/Contest Winner.png "Contest Winner.png")


*Contest Winner*  

Hold that!  


![Grand Tournament Conclusion.png](https://forumcontent.paradoxplaza.com/public/953790/Grand Tournament Conclusion.png "Grand Tournament Conclusion.png")



![Conclusion Screen.png](https://forumcontent.paradoxplaza.com/public/953736/Conclusion Screen.png "Conclusion Screen.png")


*Grand Tournament Conclusion window*  

A fine afternoon of work! I might have spent the realm’s riches on holding a Tournament, but at least I won! The returns aren’t too shabby either; oodles of prestige, a snazzy new ring, a little money back on my expenses (plus the wager winnings!) and a rather handy modifier:  

![Merry Aim.png](https://forumcontent.paradoxplaza.com/public/953737/Merry Aim.png "Merry Aim.png")


*Merry Aim modifier*  

It’s worth saying at this point that rewards scale rather heavily by the scale of your Tournament, and thus are also lightly tied to what era you’re in. If you organise a gigantic late-game tournament with five contests, the prestige rewards can easily scale into the thousands, and even more juicy rewards like dynasty renown may become available.  


#### A Grand Day Out​

Of course, this experience is only relevant if you’re actually participating in a Tournament. If you are not a martial gender, things play out somewhat differently. Tournaments are inherently less directly interactive if you’re not partaking - though as mentioned, there will generally be at least some options to participate, given the ubiquity of the likes of Recitals and Board Games - and so naturally less attractive to a non-martial gender ruler, but we wanted to give players at least an opportunity to host them and reap the rewards.  

As a spectator, you’ll be able to wander the grounds with no interest in attempting to improve your score, letting you gain some neat rewards.  

You may not always be in a position to participate in your contests; be it due to being of a non-martial gender, injury or any other reason. We still want you to be able to amass the rewards of attending or hosting a Tournament. If you want to still take something of an interest, though, you can appoint a Personal Champion for the duration of the Tournament, as your own personal stand-in. Any reward the Personal Champion is handed, their liege takes a major cut of. They are competing on your behalf, after all! If you can, you may still elect to participate in the contests while your Personal Champion is competing, at which you’ll have more chances to get rewards! It is good to be the Liege.  


![tournament_planning_5.png](https://forumcontent.paradoxplaza.com/public/953738/tournament_planning_5.png "tournament_planning_5.png")


*Activity Summary View*  

![tournament_planning_4.png](https://forumcontent.paradoxplaza.com/public/953739/tournament_planning_4.png "tournament_planning_4.png")


*Designate Personal Champion, while you have someone in the Court Position*  

As the liege, you are also able to command the knights attending your tournament to a certain extent.  


![tournament-your-knights.png](https://forumcontent.paradoxplaza.com/public/953741/tournament-your-knights.png "tournament-your-knights.png")


*Your attending knights overview*  

You can designate them to participate in upcoming contests, if they are able to, or force them to sit on the sidelines. You still get rewards when your knights perform well in the contests, but if they are particularly good and you are eyeing that top spot for yourself, you might just ease your personal competition. It is a tradeoff you have to choose between.  

There’s also quite a few other facets regarding knights in Tournaments - and, indeed, in general - but we won’t go over them much here. Keep your eyes peeled for info on that in the future!  

### Vis-à-vis Visuals​

After establishing what we wanted to be able to interact with inside the tournament scene, such as the different buildings, we started to experiment with how to visualize it. We eventually settled on what to create a scene that would display the tournament area and its surroundings.  

![tournament_visuals_1.png](https://forumcontent.paradoxplaza.com/public/953743/tournament_visuals_1.png "tournament_visuals_1.png")


*The very first concept sketches of the tournament locale that we decided to move forward with*  

During the initial exploration we started to experiment with a workflow that would allow us to combine 2D assets to add different types of buildings and terrains. This way, we could create multiple combinations of cultures and environments. We eventually ended up with something that looked like a modern take on early PC strategy games – and we loved it!  


![tournament_visuals_2.png](https://forumcontent.paradoxplaza.com/public/953744/tournament_visuals_2.png "tournament_visuals_2.png")


![tournament_visuals_3.png](https://forumcontent.paradoxplaza.com/public/953745/tournament_visuals_3.png "tournament_visuals_3.png")


*Early PC strategy games were a huge inspiration when creating the tournament locale scene.*  

To make the scene work with 2D assets we started to add “slots” for our buildings – areas that could be swapped out with different content. This would allow multiple people to create building models at the same time and easily add them to the final scene. We wanted to be able to have buildings of different cultures and visually represent how extravagant the tournament is.  


![tournament_visuals_4.png](https://forumcontent.paradoxplaza.com/public/953746/tournament_visuals_4.png "tournament_visuals_4.png")


*In order to make the system work we had to establish where we can and where we cannot put buildings.*  


#### ​

#### Workflow​


After we had created the initial prototypes the graphics production continued as a collaboration  
between our 2D and 3D departments. Our talented environment artists would start with creating  
base 3D buildings within the scene. When they are done, the buildings are rendered into separate assets. After this the 2D art department takes over. Here we can add additional detail, variations of color and texture, and some final adjustments.  

![tournament_visuals_5.png](https://forumcontent.paradoxplaza.com/public/953747/tournament_visuals_5.png "tournament_visuals_5.png")


*After the 3D asset is made and rendered we do an additional pass of digital painting.*  

One of the biggest challenges with creating assets within this system is to set it up to allow different buildings to fit and look natural in different types of environments. A key factor in creating this was to have consistent lighting for every building and terrain. Thanks to the 3D workflow we are able to use the same lighting setup on every building, tree or other objects, and keep consistency within the scene.  

To help the scene come to life our tech artists have also created VFX. These are things like smoke from chimneys, trees swaying in the wind and birds flying by.  


![tournament_visuals_6.png](https://forumcontent.paradoxplaza.com/public/953748/tournament_visuals_6.png "tournament_visuals_6.png")


*Using VFX to help bring the scene to life.*  


#### Result​


Creating the visuals for the locale scene has been a collaboration between multiple disciplines in the team, with 3D creating the initial buildings, 2D making the paintovers and final touches, and eventually tech art adding VFX.  

Here is an example of what the final scene can look like for a western culture.  


![tournament_visuals_7.png](https://forumcontent.paradoxplaza.com/public/953749/tournament_visuals_7.png "tournament_visuals_7.png")


*Completed Western culture locale visuals*  


### Are you modders now?!​

Now that we know how the visuals of the locale scene has been realised, let us talk briefly about modding activities with locales, as it is much the same as how we make the interface for the locale window.  

The locale system is something that makes *extensive* use of the plugin widgets mentioned in Dev Diary #121. The base locale window is very barren with what it provides, but in return you have a lot of control over what goes into it. The astute modder who likes delving into the changes to the game files may discover a bunch of cool features used to simplify and make these widgets, but we will delve into more modding specific improvements in a later Dev Diary.  

For now, to give some perspective on what goes into making the locale window come to life before we add any of the locale custom widgets. This is what it will look like before the locales widgets are added. A simple background, as defined within the activity itself.  


![Empty Unpopulated Tournament Window.png](https://forumcontent.paradoxplaza.com/public/953750/Empty Unpopulated Tournament Window.png "Empty Unpopulated Tournament Window.png")


*Empty, unpopulated Locale Window*  

When you set out to make a locale there are also some requirements set upon you to make it all come together. A certain strictly enforced structure. Every locale needs defined visuals, the creative process of which was discussed previously. These visuals will then be used within strictly structured custom widgets.  


![Locale widget files to make the western farmlands locale visual.png](https://forumcontent.paradoxplaza.com/public/953751/Locale widget files to make the western farmlands locale visual.png "Locale widget files to make the western farmlands locale visual.png")


*Locale widget files to make the western farmlands locale visual*  

Each of these files have a purpose! One file for every variation of a locale building, one file for the background itself with the background visual effects and one file for the top layer with visual effects on top of the locale buildings. The locale scene is then constructed in four layers: the background layer, the locale widgets (buildings) layer, the background top layer and finally the locale banner layer. These together build the basic locale scene that we see above. There are some other files with some basic types defined, but we won’t go into details on those here.  

Putting the above files together, for all the locale buildings for the Grand Tournament we get the following scene:  


![Locale window populated with buildings.png](https://forumcontent.paradoxplaza.com/public/953756/Locale window populated with buildings.png "Locale window populated with buildings.png")


*Locale window populated with buildings*  

We then add in the necessary plugin widgets to populate the rest of the interface with what we need for the Tournaments: the phase tracker widget, favoured contestants widget, the aptitude widgets, the knights overview widget, the contest information widget, the tournament specialised fullscreen event widget and the contest background widget.  

Now let us compare this to the complete Tournament with all custom widgets. Well, all of the custom widgets in between contests, without any of the custom widget windows that can be opened.  


![Locale window complete with plugin widgets.png](https://forumcontent.paradoxplaza.com/public/953759/Locale window complete with plugin widgets.png "Locale window complete with plugin widgets.png")


*Locale window complete with plugin widgets*  

That roughly covers making the locale window itself come to life from the visual development to GUI implementation! No specialised Paradox Development Studios only code magic! Everything is constrained within the confines of our script and gui systems! ~~Except any future code support we might need, because we have that leg up on you.~~  


### Tiers in Heaven​

As briefly mentioned in the Dev Diary #121, we have a whole new system for how tiered traits work in Tours and Tournaments. Since Tournaments - and one specific trait related to it - was more or less the genesis of this system, we figured we’d talk you through it here.  

Before, in the cold and dark times, there were tiered traits. Their methods were arcane, their information opaque, the knowledge contained within them buried deep. Those who interacted with them took their gifts willingly, but warily, no comprehension of their murky depths gleaned from the brief meeting.  

To be a little bit more concise, tiered traits used to be a little bit confusing, to the player and even to the developer. Tiered traits essentially had a _chance_ of leveling up each time they nudged up against the next level, and the result was tiered traits feeling occasionally unsatisfying to use and clunky to build mechanics around.  

With this in mind, we redesigned it conceptually, using what has now become the Hastiluder trait as a template, and our venerable Blackninja set about rebuilding it from the ground up. Now, rather than progress XP being hidden, it is visible on the trait itself. Rather than having a chance to level up, the progress is linear: if you are on 29 XP, the threshold to get to level 2 is 30 XP and you gain 2 more XP, you are now at level 2. No muss, no fuss.  

This proved such a success that you’ll see tiered traits and their XP bars now populating a lot of the new traits added in Tours and Tournaments, but Hastiluder remains special even amongst those as the only trait with four separate XP tracks. Let’s take a look at what makes it and the whole new tiered trait system special, shall we?  


#### Get the ‘ludes!​

Behold, the Hastiluder trait:  


![Hastiluder Unfilled.png](https://forumcontent.paradoxplaza.com/public/953808/Hastiluder Unfilled.png "Hastiluder Unfilled.png")


*Hastiluder Trait*  

Originally concepted as a pure Tournament participation trait, it has evolved a little over time to represent all sorts of martial practice, from hunting to tourneying to mock duels.  

At the moment it’s not very impressive, right? But you will surely notice it has four tracks: Foot, Bow, Horse and Wit.  

These tracks correspond to the four trait experience types we use when determining how skilled a participant is in a particular contest type. The tiers here are not the sole factor when determining a character’s aptitude, but they heavily influence it. These trait tacks can also affect other activities - and you can even gather XP for it by winning duels or even on occasion doing something as mundane as travelling - but you primarily accrue Hastiluder Trait experience by participating in tournaments. You don’t necessarily have to participate, as there are ways to obtain it from locale events, but the primary way of getting experience is by participating in contests of the appropriate categories.  

So let us take a look at what bonuses you get from the various tracks:  


![hastiluder.png](https://forumcontent.paradoxplaza.com/public/953763/hastiluder.png "hastiluder.png")


*Hastiluder Trait - Wit Track description*  

Now, the trick here is that *these effects stack*. Not only do they stack within themselves, they also stack with each other. In other words, if you have level 1 in Wit and level 1 in Horse, you’re getting both that +5% Prestige and also the +1 to Diplomacy.  

Now, I’m sure the most observant of you have worked something out by now. The thought on your mind right now is probably something along the lines of: “This seems waaaay too strong, you cannot possibly be serious about this trait?!”  

You are right. It is too strong, but that is the intention. It is extremely unlikely that you will get all tracks leveled to this point. If you do, then you’ll no doubt have spent the vast majority of your life tourneying and vanquishing all comers, a feat that frankly deserves such a rich reward. For context, that Tournament I played earlier with Vseslav, in which I won the whole contest, only got him *close* to level 1 of Bow. It’s very rare.  

However, as I was writing this, we did manage to come across one such specimen in an observer game in 1250. This is so vanishingly rare, in fact, that he was the only one alive in that save who had a maxed Hastiluder trait.  

Meet Count Martin “the Shy”. The irony is not lost on us.  


![the_shy_beast.png](https://forumcontent.paradoxplaza.com/public/953765/the_shy_beast.png "the_shy_beast.png")


*Image of Count Martin “the Shy” of Rossello*  
He’s a sprightly 67 years of age, doesn’t like showing his face, has a bunch of experience travelling around Europe, and just happens to be the most feared Tourney knight in the history of the world. Witness the power of his fully operational Hastiluder trait:  


![Maxed out Hastiluder.png](https://forumcontent.paradoxplaza.com/public/953768/Maxed out Hastiluder.png "Maxed out Hastiluder.png")


*Hastiluder Trait - all tracks maxed*  

Marty here managed to win well over 20 Contests in his life, spending his days sitting in his house at the foot of the Pyrenees. That is, whenever he wasn’t turning up at literally any Tournament that’d have him, no doubt to the exasperated groans of every other knight on the continent.  

Another thing you may take note of, apart from the absurdity of this fully powered trait, is that the icon has changed compared to before. The Hastiluder Trait will change its icon depending on which trait track experience your character has. It will take the following icons, and combine them accordingly. We’ve used this functionality to switch how a trait icon looks - for example, Crusader and Mujahid - in the past, but those are always set depending on your character’s parameters. This is the first time we’ve ever had a trait’s icon change dynamically on the fly according to the inherent parameters of the trait itself, so we’re breaking a bit of new ground here too.  

![tournament_trait_components.png](https://forumcontent.paradoxplaza.com/public/953769/tournament_trait_components.png "tournament_trait_components.png")


*Hastiluder trait - individual icon components*  

To show it off a little, if you were to have enough XP to gain level 1 in both Wit and Horse - presumably engaging in lots of ~~card games~~ board games on ~~motorcycles~~ horseback, your trait would look like:  


![Hastiluder with Horse and Wit.png](https://forumcontent.paradoxplaza.com/public/953771/Hastiluder with Horse and Wit.png "Hastiluder with Horse and Wit.png")


*Hastiluder trait - Horse and Wit*  

In the case of the Hastiluder trait the ‘final’ icon, should the character have 30 or more experience in every track, looks like this:  

![tournament_foot_archery_horse_mind.png](https://forumcontent.paradoxplaza.com/public/953816/tournament_foot_archery_horse_mind.png "tournament_foot_archery_horse_mind.png")


*[Hastiluder trait - final icon with all tracks represented]*  

It is worth mentioning that these combinations are not automatically merged together to create the effect, they are created as separate textures.  

For the modders who are seeking to make their own tiered trait icons, this works on a simple trigger system where it selects the appropriate texture, so if you want something similar you need to make an icon for each combination you wish to display. Speaking of modding tiered traits…  


#### Cheers for Tiers!​

Now we know hungry modders wish to get their hands on this, so let us quickly go over how you can use this for yourselves. A simple, new field has been added which you can define within any trait.  


![tiered_trait_script.png](https://forumcontent.paradoxplaza.com/public/953821/tiered_trait_script.png "tiered_trait_script.png")


*Hastiluder Trait script definition*  

Here we see the definition of the Hastiluder trait. The `tracks` field with *unique* names determine the ranks where any number between 0 and 100, inclusively, can be defined with a list of modifiers for this level to include. The XP thresholds *must* be in ascending order. Then we have a simple icon implementation, put the appropriate texture named the same as the track and you’re good to go!  

![WRp2kq5rkI0Sk8BjijS-MbLt6DdCmNKywuiaRw4szAcOKbRFGDB7WJ-h7TGq9cEcWPer3L1N833Y6zN8AmeN5u1uVg_I2nwKO5oRndh7odKj9ySF3Kae6ZfiObNjbULLeqvOdZqDKRNGjo63XmKqorU](https://lh4.googleusercontent.com/WRp2kq5rkI0Sk8BjijS-MbLt6DdCmNKywuiaRw4szAcOKbRFGDB7WJ-h7TGq9cEcWPer3L1N833Y6zN8AmeN5u1uVg_I2nwKO5oRndh7odKj9ySF3Kae6ZfiObNjbULLeqvOdZqDKRNGjo63XmKqorU "")


*Tiered Trait Track icon file structure*  

One of the most exciting aspects for modders here is actually an unused feature for Tours and Tournaments. One of the original requested features for the Hastiluder trait was the ability to decay away XP over time. As it turns out, we decided we preferred it without it, but we’ve kept the functionality in. For the sake of completion, here is a snippet:  


![oEKQHr7QRO8UuvfrxSLs8-GF97Pu-q4B_TmjHdUnYn4bNhV30ZJIlcsH8My560kLf2jV8qHtgYRS_ROliIRLo8ImmT1uZlmZyrza_ktTHR9ct3e2lHjlqpnYe0vvfeFg_MthgyKEkKmByAf-iYhRwmU](https://lh3.googleusercontent.com/oEKQHr7QRO8UuvfrxSLs8-GF97Pu-q4B_TmjHdUnYn4bNhV30ZJIlcsH8My560kLf2jV8qHtgYRS_ROliIRLo8ImmT1uZlmZyrza_ktTHR9ct3e2lHjlqpnYe0vvfeFg_MthgyKEkKmByAf-iYhRwmU "")



![FGeGIQc2YcL4tb5UkMgNnkyxsDYZDz3CsfDdQWwI2CRmXewujyYE8RDAtX1u_E4qzR_8QDmqLKZn-izbXy5lIuc5oju2L0XrDvTPaAqygn9xpEpjIexyfd4rMGvCBrM07C9OMAjLSJnKUdcRZnUGgQU](https://lh5.googleusercontent.com/FGeGIQc2YcL4tb5UkMgNnkyxsDYZDz3CsfDdQWwI2CRmXewujyYE8RDAtX1u_E4qzR_8QDmqLKZn-izbXy5lIuc5oju2L0XrDvTPaAqygn9xpEpjIexyfd4rMGvCBrM07C9OMAjLSJnKUdcRZnUGgQU "")


*Monthly trait experience decay example*  

Simple enough! If the trait’s track experience is above 30, it will trend towards 30 at a rate of -1.5 experience per month. You can, of course, set this minimum higher or lower, and adjust the rate of change to your liking. Whilst we’re not currently using this functionality in-game, we can foresee plenty of exciting possibilities for modders.  

That covers the basics of adding your own tiered traits!  


### Forbidden Knowledge…​

As a little bonus, here is some forbidden knowledge for you to peruse, if you dare.  

Spoiler: The forbidden knowledge

So you have deigned to delve into the forbidden archive? Come closer. Closer. This is not for the faint of heart. I bestow upon you the forbidden knowledge of how Tournaments looked during development before our artists got their hands on it. Are you committed to this knowledge? If so, take a look below.  

Spoiler: Early development screenshots

So you are committed then. Let us proceed…  

We shall begin with the very first, functional implementation of the locale scene, and it is the view our developers’ eyes bled upon for the better part of half a year until our artists finished the locale visuals. As a bonus, this screenshot is also showing the AI’s first hosted Tournament, which incidentally was held by the Pope. He knew what he wanted.  


![Forbidden Knowledge - AI Pope hosting first tournament in very pink locale window.png](https://forumcontent.paradoxplaza.com/public/953773/Forbidden Knowledge - AI Pope hosting first tournament in very pink locale window.png "Forbidden Knowledge - AI Pope hosting first tournament in very pink locale window.png")


*Forbidden Knowledge - AI Pope hosting first tournament in very pink locale window*  

Marvel in the eye bleeding pink! We know we did! For several months! The amount of pink varied greatly over the course of development, much to our artists’ dismay. Some of them even went on light de-pinkification crusades just to make it easier on the eyes, before more things were implemented with more pink! It was a vicious battle between Art and Code!  
*![Forbidden Knowledge - Early Locale window with visuals.png](https://forumcontent.paradoxplaza.com/public/953774/Forbidden Knowledge - Early Locale window with visuals.png "Forbidden Knowledge - Early Locale window with visuals.png")


Forbidden Knowledge - Early Locale window with visuals*  

Quite the difference between in-development and the final version, right? The pretty planner? Didn’t look nearly as pretty when I handed it off to the artists to prettify.  


![Forbidden Knowledge - Contest Planner.png](https://forumcontent.paradoxplaza.com/public/953776/Forbidden Knowledge - Contest Planner.png "Forbidden Knowledge - Contest Planner.png")


*Forbidden Knowledge - Contest Planner*  

I can hear the artists scream in the background.  

Speaking of screaming in the background. We have an audioscape in the tournament scene! Something fitting for a buzzling Tournament. This was, of course, not always the case during development. During some parts of development, we had some placeholder audio in place of the sound effects. You know: to make sure we don’t forget to replace them with the proper sounds.  

![Forbidden Knowledge - Placeholder Pink Audio located.png](https://forumcontent.paradoxplaza.com/public/953777/Forbidden Knowledge - Placeholder Pink Audio located.png "Forbidden Knowledge - Placeholder Pink Audio located.png")


*Forbidden Knowledge - Placeholder Pink Audio located*  

Apparently, sufficient warning on this being enabled was not provided. ~~If you want to hear it for yourself: turn the volume down, open the console and do audio.play_effect event:/Error/placeholder_obnoxious_ui  

![Forbidden Knowledge - Developer dismay over placeholder pink audio.png](https://forumcontent.paradoxplaza.com/public/953784/Forbidden Knowledge - Developer dismay over placeholder pink audio.png "Forbidden Knowledge - Developer dismay over placeholder pink audio.png")~~  
*Forbidden Knowledge - Developer dismay over placeholder pink audio*  

In order to differentiate between and customise which event window to display, we also had to figure out a way to verify whether or not a different window was, in fact, being displayed! Enter the wonderful debug_square:  


![Forbidden Knowledge - Testing event window variation.png](https://forumcontent.paradoxplaza.com/public/953780/Forbidden Knowledge - Testing event window variation.png "Forbidden Knowledge - Testing event window variation.png")


*Forbidden Knowledge - Testing event window variation*  

QA was quick to report this little, stray square before I closed the ticket with a big “WAD”. We needed to ensure it was working properly, because the tournament has a whopping three different event windows to juggle!  

There was so much going on with pink, and I *REVEL* in it!  

![Forbidden Knowledge - Pink placeholder animation being denied.png](https://forumcontent.paradoxplaza.com/public/953781/Forbidden Knowledge - Pink placeholder animation being denied.png "Forbidden Knowledge - Pink placeholder animation being denied.png")


*Forbidden Knowledge - Pink placeholder animation being denied*  

![Pink placeholder animation is in fact real.gif](https://forumcontent.paradoxplaza.com/public/953782/Pink placeholder animation is in fact real.gif "Pink placeholder animation is in fact real.gif")


*Forbidden Knowledge - Pink placeholder animation is in fact real*  

~~But please remove all of it before release, pretty artists please.~~  

I should bolt before the artists start a witch hunt.


### A ceremonial finish​

That is all we have for this week! We hope you’ve enjoyed this dive into the Grand Tournaments! Come back next week for a look into the Grand Weddings and Feasts, as well as the changes coming to the other, smaller activities.  

Finally: last year we had one of our artists make art of our developers and we showed them in some of our dev diaries, and our authors for today have yet to show theirs off for you. We have: Elisabeth with a lovely, adorable, cute-as-a-button fox friend; Jon in the height of Norse fashion; and of course Nick with a big, insufferable, smug smile on his face and a vicious, mass-murdering and unrepentant bird friend.  

![IrWdPjQyXAyB9vagKhQR6jrpWswEnP9PdtSMqnXBY2Mol270sc_T5M3DZSvAWTZsnQ2VEb65rEIZ5gtR8ZtGr698qkE-45LqrHNzxEgLrjYxr5UQwku-kKhOG86bvgisTceiSVs6_o3-YU5K9J8RSk0](https://lh5.googleusercontent.com/IrWdPjQyXAyB9vagKhQR6jrpWswEnP9PdtSMqnXBY2Mol270sc_T5M3DZSvAWTZsnQ2VEb65rEIZ5gtR8ZtGr698qkE-45LqrHNzxEgLrjYxr5UQwku-kKhOG86bvgisTceiSVs6_o3-YU5K9J8RSk0 "")


*Art of our authors - Elisabeth, Jon and Nick*  

Until next time!

 

#### Attachments

- [![Arrow Target Hit.png](https://forumcontent.paradoxplaza.com/thumbnail/public/953685/Arrow Target Hit.png)](https://forum.paradoxplaza.com/forum/attachments/arrow-target-hit-png.966183/)
  
  Arrow Target Hit.png
  1,5 MB

 · Views: 0

- [![tournament_planning_2.png](https://forumcontent.paradoxplaza.com/thumbnail/public/953712/tournament_planning_2.png)](https://forum.paradoxplaza.com/forum/attachments/tournament_planning_2-png.966210/)
  
  tournament_planning_2.png
  2,3 MB

 · Views: 0

- [![tournament_planning_2.png](https://forumcontent.paradoxplaza.com/thumbnail/public/953713/tournament_planning_2.png)](https://forum.paradoxplaza.com/forum/attachments/tournament_planning_2-png.966211/)
  
  tournament_planning_2.png
  2,3 MB

 · Views: 0

- [![Locale window complete with plugin widgets.png](https://forumcontent.paradoxplaza.com/thumbnail/public/953716/Locale window complete with plugin widgets.png)](https://forum.paradoxplaza.com/forum/attachments/locale-window-complete-with-plugin-widgets-png.966214/)
  
  Locale window complete with plugin widgets.png
  3,9 MB

 · Views: 0

- [![Locale window complete with plugin widgets.png](https://forumcontent.paradoxplaza.com/thumbnail/public/953755/Locale window complete with plugin widgets.png)](https://forum.paradoxplaza.com/forum/attachments/locale-window-complete-with-plugin-widgets-png.966253/)
  
  Locale window complete with plugin widgets.png
  3,9 MB

 · Views: 0

- [![Maxed out Hastiluder.png](https://forumcontent.paradoxplaza.com/thumbnail/public/953761/Maxed out Hastiluder.png)](https://forum.paradoxplaza.com/forum/attachments/maxed-out-hastiluder-png.966259/)
  
  Maxed out Hastiluder.png
  455 KB

 · Views: 0

- [![Maxed out Hastiluder.png](https://forumcontent.paradoxplaza.com/thumbnail/public/953766/Maxed out Hastiluder.png)](https://forum.paradoxplaza.com/forum/attachments/maxed-out-hastiluder-png.966264/)
  
  Maxed out Hastiluder.png
  455 KB

 · Views: 0

- [![Maxed out Hastiluder.png](https://forumcontent.paradoxplaza.com/thumbnail/public/953767/Maxed out Hastiluder.png)](https://forum.paradoxplaza.com/forum/attachments/maxed-out-hastiluder-png.966265/)
  
  Maxed out Hastiluder.png
  455 KB

 · Views: 0

- [![Forbidden Knowledge - Developer dismay over placeholder pink audio.png](https://forumcontent.paradoxplaza.com/thumbnail/public/953778/Forbidden Knowledge - Developer dismay over placeholder pink audio.png)](https://forum.paradoxplaza.com/forum/attachments/forbidden-knowledge-developer-dismay-over-placeholder-pink-audio-png.966276/)
  
  Forbidden Knowledge - Developer dismay over placeholder pink audio.png
  13,5 KB

 · Views: 0

- [![Conclusion Screen.png](https://forumcontent.paradoxplaza.com/thumbnail/public/953789/Conclusion Screen.png)](https://forum.paradoxplaza.com/forum/attachments/conclusion-screen-png.966287/)
  
  Conclusion Screen.png
  952 KB

 · Views: 0

- [![1681217437673.png](https://forumcontent.paradoxplaza.com/thumbnail/public/953805/1681217437673.png)](https://forum.paradoxplaza.com/forum/attachments/1681217437673-png.966303/)
  
  1681217437673.png
  126,1 KB

 · Views: 0

Last edited: Apr 11, 2023

<!-- artifact:reactions:start -->
- 214 Love
- 112 Like
- 14 (unlabeled — rendered as base64 data URI)
- 12 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Paradoksalny Kierownik](https://forum.paradoxplaza.com/forum/members/paradoksalny-kierownik.1725641/)**
Role: Corporal
Badges: 44
Messages: 27
Reaction score: 1,566

*[Full game-badge icon list of 44 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
