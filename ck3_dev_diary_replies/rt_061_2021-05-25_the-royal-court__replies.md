---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1476067/"
forum_thread_id: 1476067
content_type: reply_thread
parent_dd_file: dd_061_2021-05-25_dev-diary-61-the-royal-court.md
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 61
title: "CK3 Dev Diary #61 - The Royal Court"
dd_date: 2021-05-25
expansion: Royal Court
patch: Patch 1.5 (Fleur-de-lis)
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-10
fetched_at: 2026-06-10
text_layer_present: true
ocr_used: false
language: en
author_identity: anonymized_stable_pseudonym
pages_captured: 14
reply_count: 271
participant_count: 162
reply_date_first: 2021-05-25
reply_date_last: 2021-06-02
body_word_count: 18279
inline_image_count: 0
quoted_span_count: 153
extraction_rationale: |
  Full reply thread captured live via Claude in Chrome (article.message bodies).
  Quote blocks split into artifact:quote spans and excluded from word counts.
  Usernames replaced by stable per-thread participant ids; the dev-diary OP is
  excluded (see parent_dd_file).
notes_for_analyst: |
  Community-voice counterpart to the linked dev diary. Strip YAML + artifact
  comments before tokenizing, exactly as for dd_*.md.
---

# Reply thread — CK3 Dev Diary #61 - The Royal Court

*271 replies from 162 participants across 14 pages*

## Reply 1 — participant_001 · 2021-05-25 · post-27561659

Greetings! Welcome to the first Dev Diary for the Royal Court expansion! As we mentioned in a previous DD, we’ll go back to Azure patch DD’s for a few weeks after this one. But do not fear, there will be some more Royal Court DD’s before the summer holidays - and when we’re back from holidays we’ll have many, many Royal Court diaries for you! It’s really hard to pick a topic for where to start, but we decided upon a dive into the namesake feature of the expansion - the Royal Court itself, your seat of royal majesty and power! The Royal Court consists of many features, all collected within a 3D scene that we call the Throne Room. Here’s an early Work in Progress screenshot of the throne room - do note that it’s a very early version, but we just can't wait to show you what we have been working on! { "lightbox_close": "Close", "lightbox_next": "Next", "lightbox_previous": "Previous", "lightbox_error": "The requested content cannot be loaded. Please try again later.", "lightbox_start_slideshow": "Start slideshow", "lightbox_stop_slideshow": "Stop slideshow", "lightbox_full_screen": "Full screen", "lightbox_thumbnails": "Thumbnails", "lightbox_download": "Download", "lightbox_share": "Share", "lightbox_zoom": "Zoom", "lightbox_new_window": "New window", "lightbox_toggle_sidebar": "Toggle sidebar" } [Image: An early WIP western-style Throne Room, not indicative of final quality] Now, there are many things that go into the Royal Court itself. It interacts with numerous new features that’ll come with the expansion - we won’t go into detail on all of them today, if we did this DD would become much too long! It's worth noting that this isn’t just a graphical feature; while we admit the importance of immersion, we don't want any features to feel tacked-on or superfluous. The Throne Room is there to show what’s happening; what artifacts you’ve collected, which courtiers are having a fight, etc. This allows us to place your character in a scene together with others, showing that you’re actually present in the same world! We’re trying to bridge the gap between your character and the map, all while representing a side of medieval history we’ve never previously explored in detail - the importance for a ruler to show their power, their grandeur, to their subjects and peers. Every Feudal/Clan King and Emperor has a Royal Court. Tribal Rulers do not have one, as this feature primarily models the formality and ceremony surrounding the court, as well as the need for spending Gold, while Tribal rulers use Prestige as their main resource. If a ruler is demoted to a lower rank (through war, election, or just sheer bad luck) their Royal Court and everything therein will either stay dormant until you regain your lost status, or follow the character who now rules in your stead. Grandeur The key concept that enables this is called Grandeur - a measurement of your standing in the eyes of your peers. While it’s measured on a scale from 0-100, it’s not necessarily a simple system. Increasing your grandeur will lead to direct political benefits, such as increased opinions, marriage acceptance, etc. It will also unlock new Council Jobs, such as being able to peacefully demand De Jure land with the ‘Convince De Jure Territory’ job, or gain Knight Effectiveness while also decreasing enemy Scheme Success Chance with the ‘Manage Royal Guards’ job. These effects motivate you to aim for a high level of Grandeur, but naturally comes at a monetary cost. How much are you willing to spend on artifacts, amenities, or on positions within your court? You have to balance your political needs with your temporal ones, such as warfare or development. Sacrificing your grandeur entirely will cause instabilities both internal and external. Grandeur is not really a resource, and is not actively ‘spent’ - unlike something like Prestige. It works on a much slower timescale, and is something you must balance and work towards increasing over a longer period of time. Though there are of course choices in events that make Grandeur increase or decrease, with various trade-offs. Grandeur Effects As mentioned in the previous section, Grandeur has several different effects and modifiers. It is divided into 10 separate levels with their own effects. For example, the very first level of Grandeur unlocks the ability to Hold Court - which is a crucial component in achieving the higher Grandeur levels. The second level unlocks a Council Task called ‘Bestow Royal Favor’, which is a powerful single-target task that increases a vassal’s opinion of you while granting them, and you, prestige. One of the most significant effects of Grandeur is its effect on attraction of Inspired characters - the higher your Grandeur is compared to that of your neighbors, the likelier you are to have these creative travelers visit your court first, giving you an opportunity for patronage (more on Inspirations in a future DD). Some of these levels will give courtiers who stay within it a flavorful trait, which will increase their skills and attributes based on the type of court they’re staying at. A particularly grand court might even see a more powerful trait appear, making such characters excellent for various jobs and Court Positions (more on Court Positions in a later DD). Several Grandeur levels have effects and modifiers based on your Court Type - a type of flavorful perk for your court. Depending on your cultural Ethos you’ll get access to a few different types, such as a Diplomatic or Warlike Court. All royal courts have a type, and among other things it affects the type of trait that courtiers get (see previous paragraph). The bonuses granted from these types are varied and aim to enhance a certain style of play. The AI will tend to go for the Court Type most reflective of their Cultural Ethos and situation - for example, Indian Kings will often tend to want a Scholarly Court since many Indian cultures have a spiritual Ethos. As an example, having a Diplomatic Court Type will grant you bonuses to Vassalization acceptance, tyranny gain, opinion, and potentially even unlock a Personal Scheme slot. A Warlike Court Type might instead see bonuses to MaA counter efficiency, knight efficiency, and the maximum size of MaA regiments. As not all cultures can access all Court Types, this is another reason to pursue Hybridization or Divergence (more on that in a later DD). How Grandeur is Gained Grandeur is divided in two; baseline, and direct gain. The baseline decides the ‘trend’, with you passively (and slowly) either gaining or losing grandeur over time, until the baseline is met. The baseline is affected by many things; what Court Artifacts you have, what Court Positions you have filled, etc (more on Court Artifacts in a later DD). The rate of grandeur change can be modified by many things, such as Cultural Ethoses or Traditions, but is as a rule of thumb slow. It takes time for word of your glory to spread, after all! The most simple way to increase your Grandeur baseline is by investing in Amenities. Now, Amenities are simple and straightforward; but they’re still central to the concept of having a grand court! There are four different types; Lodgings, Food, Clothing and Servants. There are four levels to each, with each progressive level costing more gold to maintain, but giving more Grandeur baseline. They all come with a selection of flavor effects, for example; spending on food will slightly increase the disease resistance of your courtiers, but higher levels might also cause them to gain weight! Spending on clothes will increase their prestige, and will even cause them to wear fancier clothes at higher levels of expenditure (commoners will wear low nobility clothes, and so on). If your court is lacking in artifacts, spending on Amenities is the way to go. Worth noting is that the cost of amenities is relative to your size and income; a small realm won’t have to pay as much as a prosperous one - the intent here is to allow smaller kingdoms and empires to ‘punch above their weight’ diplomatically, making choosing between expansion and consolidation a more relevant matter. Reaching your baseline might take a long time, unless you decide to take action in order to speed it up - to gain grandeur fast, you need to Hold Court! Performing this decision invites your vassals and subjects to bring their issues, requests, and questions before you. The mere act of Holding Court will give you a one-time boost to your Grandeur, but the opportunities within the activity itself might give you opportunities to increase it further (or you could decide to lose grandeur for some temporal gain that is just too good to pass up!). The issues brought forth when Holding Court are many and varied, with many of them reacting to the state of your realm (more on Hold Court in a later DD). Grandeur Expectations Now, Grandeur isn’t only about reaching the level that gives the effect you desire, it’s also about managing expectations! Depending on a number of factors, such as your tier or the size of your realm, you will have a certain expectation put upon your Royal Court. This expectation is a double-edged sword - if your grandeur is below expectations you’ll suffer increasing diplomatic penalties as people lose respect, while if it’s exceeded you might see powerful diplomatic bonuses. These are scaled based on how powerful you are - a rather small Kingdom that undershoots its expectations won’t be hit particularly hard, while a massive empire such as the Holy Roman Empire or Byzantium will be punished much harder if they fail to live up to the expectations put upon them. The effects of not living up to your expectations are many; reduced prestige, renown, and a hefty hit to opinion with both foreign rulers, courtiers and vassals. A large realm might easily find itself facing significant unrest unless its ruler starts spending on grandeur! On the other hand, a small kingdom that vastly exceeds the expectations put upon it might see significant bonuses to its diplomatic power, as well as renown and other bonuses. Court Events Now, the Royal Court isn’t all about Grandeur, of course. Another important role it holds is to show that there’s life in your court! This is done through Court Events; happenings contained within the court, taking place between those who live therein. This new type of event uses the throne room as its backdrop, transforming the entire throne room into an event when they happen. Unlike normal events, this type of event is non-interruptive - you get notified that something is happening, whereby you can go into your Royal Court, inspect the scene, find whoever is involved, and trigger the event yourself. Usually these events are some sort of drama happening between your courtiers, which you can choose to simply ignore if you feel like you have more important matters to attend to. These events come in many different flavors, mostly focusing on how it is to live in the court. Some examples of court events that are being worked on currently include courtiers causing you embarrassment through their drinking or poor manners, or getting into arguments with your architect. Others involve things like rumors spreading about your predecessor on the throne, or popular and unflattering songs about you spreading within the court itself. Court events might also be things like foreign ambassadors trying to uncover your secrets or devout courtiers shaming you and your court for your frivolous living. --- Now, of course there’s more that goes into the Royal Court, but we’ll save going into details regarding Court Artifacts, the UI and graphical looks of the Throne Rooms, Court Positions and so on for future DevDiaries! Of course, this expansion isn’t all about the Royal Court; before the summer break starts you’ll get to read about some of the other features coming with the expansion and patch. That’s all for now!

## Reply 2 — participant_002 · 2021-05-25 · post-27562146

Promising stuff! Nice to see some pictures to get an idea of what we're getting!

## Reply 3 — participant_003 · 2021-05-25 · post-27562150

Sounds AMAZING!

## Reply 4 — participant_004 · 2021-05-25 · post-27562157

<!-- artifact:quote:start -->
> rageair said: Several Grandeur levels have effects and modifiers based on your Court Type - a type of flavorful perk for your court. Depending on your cultural Ethos you’ll get access to a few different types, such as a Diplomatic or Warlike Court. All royal courts have a type, and among other things it affects the type of trait that courtiers get (see previous paragraph). The bonuses granted from these types are varied and aim to enhance a certain style of play. The AI will tend to go for the Court Type most reflective of their Cultural Ethos and situation - for example, Indian Kings will often tend to want a Scholarly Court since many Indian cultures have a spiritual Ethos. As an example, having a Diplomatic Court Type will grant you bonuses to Vassalization acceptance, tyranny gain, opinion, and potentially even unlock a Personal Scheme slot. A Warlike Court Type might instead see bonuses to MaA counter efficiency, knight efficiency, and the maximum size of MaA regiments. As not all cultures can access all Court Types, this is another reason to pursue Hybridization or Divergence (more on that in a later DD). Click to expand...
<!-- artifact:quote:end -->
I'm assuming then there will be 5 court types, each ethos corresponding to one of the five skills?

## Reply 5 — participant_005 · 2021-05-25 · post-27562165

More roleplay in CK is always a big win in my book. I am very excited about this

## Reply 6 — participant_006 · 2021-05-25 · post-27562166

This all sounds really great. Really excited. Aside from all the other stuff it does, Grandeur sounds like it might provide some couterpressure/downsides to rapid expansion/larger realms (which I think everyone around here agrees the game needs) by forcing players not to expand beyond their ability to keep up with expected Grandeur.

## Reply 7 — participant_007 · 2021-05-25 · post-27562181

Excellent Concept. Like the real intrigues of court life. However queen should lso be present I hope as being an important member. Secondly With Increase in Grandeur the visual look should also improve. Thirdly what I feel, Those close to power should seat closer to the king and should carry some significance Lastly best of luck.

## Reply 8 — participant_008 · 2021-05-25 · post-27562188

Will the characters represented in your Throne Room be dynamically placed, or static? As in, will your Steward always stand in the same place in the same pose? Or is there variety to how characters are placed within the scene?

## Reply 9 — participant_009 · 2021-05-25 · post-27562196

<!-- artifact:quote:start -->
> rageair said: The most simple way to increase your Grandeur baseline is by investing in Amenities. Now, Amenities are simple and straightforward; but they’re still central to the concept of having a grand court! There are four different types; Lodgings, Food, Clothing and Servants. There are four levels to each, with each progressive level costing more gold to maintain, but giving more Grandeur baseline. They all come with a selection of flavor effects, for example; spending on food will slightly increase the disease resistance of your courtiers, but higher levels might also cause them to gain weight! Spending on clothes will increase their prestige, and will even cause them to wear fancier clothes at higher levels of expenditure (commoners will wear low nobility clothes, and so on). If your court is lacking in artifacts, spending on Amenities is the way to go. Click to expand...
<!-- artifact:quote:end -->
Well, this expansion is looking pretty nice. I'm wondering what do the "Servants" do. What impact do they have on court members?

## Reply 10 — participant_006 · 2021-05-25 · post-27562206

<!-- artifact:quote:start -->
> rageair said: There are four levels to each, with each progressive level costing more gold to maintain Click to expand...
<!-- artifact:quote:end -->
Couple of questions: 1. How inheritable is Grandeur? When a new King takes over, will they need to build up their Grandeur from scratch? 2. Does this mean that Amenities are an ongoing, monthly cost (like army maintanance) rather than a one-off "upgrade cost".

## Reply 11 — participant_010 · 2021-05-25 · post-27562209

On artifacts: would they work similarly to CKII? As in you collect them from different sources and they give you stat bonuses ? Would some of them (crowns, weapons etc) be visible on the portrait ? Can they be stolen / raided? Otherwise a cool concept as a whole, and the dynamic culture thing sounds like a very good addition gameplay and rp wise.

## Reply 12 — participant_011 · 2021-05-25 · post-27562212

<!-- artifact:quote:start -->
> johnty5 said: This all sounds really great. Really excited. Aside from all the other stuff it doesn, Grandeur sounds like it might provide some couterpressure/downsides to rapid expansion/larger realms (which I think everyone around here agrees the game needs) by forcing players not to expand beyond their ability to keep up with expected Grandeur. Click to expand...
<!-- artifact:quote:end -->
Yes! My biggest turn-off with CK3 right now is that the gameplay doesn't feel like it scales well into the mid to late game. Hopefully stuff like this + faction changes will help make it more interesting. Also will be very interesting to see the court scenes. A bit worried how they will work. The idea is great to have larger scenes of your court rather than the normal event window but will the fidelity feel satisfying or will it feel awkwardly abstract? Does feel like a very good direction in general for CK3 to get more value out of the 3D characters.

## Reply 13 — participant_012 · 2021-05-25 · post-27562213

Grandeur sounds like it gives a lot of bonuses just for existing. Will the game be balanced around having Grandeur (the DLC) toggled on or off, or will it be a pay-to-win DLC feature where the player will be more powerful simply by owning the DLC?

## Reply 14 — participant_013 · 2021-05-25 · post-27562216

Great additions. I just have few concerns/questions? 1) If we stay a count or Duke do we have some new interactions available? 2) Can we petition the King/Emperor or is that only AI ability? 3) Will some of these new travelers be available to lower ranks than KIng? 4) In terms of artifacts, are you still able to get them as count and if Throne room unlocks only their presentation( grandeur) or something else unique to them? Otherwise, looking forward to expansion.

## Reply 15 — participant_014 · 2021-05-25 · post-27562221

<!-- artifact:quote:start -->
> rageair said: Some examples of court events that are being worked on currently include courtiers causing you embarrassment through their drinking or poor manners, or getting into arguments with your architect. Others involve things like rumors spreading about your predecessor on the throne, or popular and unflattering songs about you spreading within the court itself. Court events might also be things like foreign ambassadors trying to uncover your secrets or devout courtiers shaming you and your court for your frivolous living. Click to expand...
<!-- artifact:quote:end -->
What about positive events?

## Reply 16 — participant_015 · 2021-05-25 · post-27562224

Every Feudal/Clan King and Emperor has a Royal Court. Tribal Rulers do not have one, wait so tribals dont have the court picture ?????

## Reply 17 — participant_016 · 2021-05-25 · post-27562226

Very cool concept. I feel like balance will be a key issue there - please don't make it like CK2 artifacts with soo many bonuses and few drawbacks. Also, I willl repeat question many people already asked: Is this feature mainly designed around playing as King/Emperor or can you interact with it meaningfully as a vassal in the court?

## Reply 18 — participant_006 · 2021-05-25 · post-27562228

<!-- artifact:quote:start -->
> Razmorg said: Also will be very interesting to see the court scenes. A bit worried how they will work. The idea is great to have larger scenes of your court rather than the normal event window but will the fidelity feel satisfying or will it feel awkwardly abstract? Does feel like a very good direction in general for CK3 to get more value out of the 3D characters. Click to expand...
<!-- artifact:quote:end -->
The event windows do a good job of showing character models reacting to each other. I'm hoping the court scene will by dynamic enough that you would see your rival stood off to the side glaring at you, the women at court who's trying to seduce your Chancellor actually doing that in the scene etc.

## Reply 19 — participant_017 · 2021-05-25 · post-27562231

This sounds very promising. Does the throne-room have more "slots" for characters than an event window. In other words: how many animated characters can be present?

## Reply 20 — participant_018 · 2021-05-25 · post-27562234

Nice. I now imagine myself being a chancellor doing embarassing things in a foreign court "on behalf" of my liege because I hate him.

## Reply 21 — participant_019 · 2021-05-25 · post-27562235

Honestly this is exceeding my expectations for the first DLC! Can't wait to play it!

## Reply 22 — participant_006 · 2021-05-25 · post-27562239

<!-- artifact:quote:start -->
> Furleppe said: Very cool concept. I feel like balance will be a key issue there - please don't make it like CK2 artifacts with soo many bonuses and few drawbacks. Also, I willl repeat question many people already asked: Is this feature mainly designed around playing as King/Emperor or can you interact with it meanigfully as a vassal in the court? Click to expand...
<!-- artifact:quote:end -->
I'm wondering whether the artifacts will tie in to the other new systems - rather than being staf boosts. Like particular artifacts boost your amenities, or unlock certain councillor jobs or give you grandeur +5 etc.

## Reply 23 — participant_020 · 2021-05-25 · post-27562250

I hope you guys think again with Tribals not having a courtroom, I get the point you make but maybe a more basic, intimate clan hall room would be appropriate with some of the mechanics disabled? Ignoring tribal realms completely sounds bad in my opinion. Give them a cozy, wooden hall, with fur and animal hides laying around. Finally, add a few basic mechanics that are weaker than feudal ones. Would make tribals not left out and still weaker than feudal courts. Just a thought.

## Reply 24 — participant_021 · 2021-05-25 · post-27562251

This sounds promising. I do have some questions though: -> Will I as a vassal be able to bring my issues, requests and questions before my liege if they hold court? -> Will artifacts only be accessible to rulers who have a court? To me it seems that counts, dukes and tribals should also be able to own artifacts. -> How will the renown bonuses or penalties from grandeur expectations be handled? Do they only apply for the dynasty head, or for each ruler of the dynasty who has a court? Also: I don't like the income scaling for amenity costs. Increasing costs with the size of your realm makes some degree of sense, since you need to provide for more people. But scaling costs to your income just makes your income meaningless.

## Reply 25 — participant_022 · 2021-05-25 · post-27562252

Grandeur sounds like more of the same problem we keep seeing in all Paradox DLCs -- extra modifiers which don't tie in well with base game systems. I really don't see a point to it. Either it will be very powerful for its cost making maxing it out a no-brainer, or it will be too weak for its cost and will become a 'dump stat' for extra money. I also don't see how it can be balanced effectively given that many rulers (counts, dukes, tribals) can't use it. And that's all without getting into what the weird abstraction actually is supposed to represent.

## Reply 26 — participant_001 · 2021-05-25 · post-27562259

<!-- artifact:quote:start -->
> Hospodar said: I'm assuming then there will be 5 court types, each ethos corresponding to one of the five skills? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> siddhartha_gamer said: However queen should lso be present I hope as being an important member. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Liggi said: Will the characters represented in your Throne Room be dynamically placed, or static? As in, will your Steward always stand in the same place in the same pose? Or is there variety to how characters are placed within the scene? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> King Anund said: I'm wondering what do the "Servants" do. What impact do they have on court members? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> johnty5 said: Couple of questions: 1. How inheritable is Grandeur? When a new King takes over, will they need to build up their Grandeur from scratch? 2. Does this mean that Amenities are an ongoing, monthly cost (like army maintanance) rather than a one-off "upgrade cost". Click to expand...
<!-- artifact:quote:end -->
Each Ethos unlocks more than one Court Type, and the Court Types are (currently) based on the five skills thematically, yes. Your spouse will very often be shown, we think that it's a very thematically appropriate character to place close to the ruler. I believe the idea is to have them of their own throne next to your, at least in certain court styles where such a thing was common. Dynamic, we're aiming for variation. The exact details are not nailed down yet. There are some modifiers, and depending on the Amenity level certain Court Events might be affected. 1. We're actually discussing this internally! We're considering having it drop on succession, at least by a bit - making it so that you have to prove your worth as a new monarch. 2. Yes, they're a type of maintenance.

## Reply 27 — participant_023 · 2021-05-25 · post-27562261

Look interesting. I'm hoping we can also sit on the throne and get to choose from several siting animations. And while we're at it, will we also be getting new idles that interact with the throne room?

## Reply 28 — participant_024 · 2021-05-25 · post-27562264

<!-- artifact:quote:start -->
> Salazard260 said: On artifacts: would they work similarly to CKII? As in you collect them from different sources and they give you stat bonuses ? Would some of them (crowns, weapons etc) be visible on the portrait ? Can they be stolen / raided? Otherwise a cool concept as a whole, and the dynamic culture thing sounds like a very good addition gameplay and rp wise. Click to expand...
<!-- artifact:quote:end -->
Yes. Artifacts are mentioned in the FAQ.

## Reply 29 — participant_025 · 2021-05-25 · post-27562265

Will AI rulers have their own royal court and grandeur rating? Will we be able to see what's going on in a life's court as a vassal?

## Reply 30 — participant_026 · 2021-05-25 · post-27562266

<!-- artifact:quote:start -->
> fodazd said: This sounds promising. I do have some questions though: -> Will I as a vassal be able to bring my issues, requests and questions before my liege if they hold court? -> Will artifacts only be accessible to rulers who have a court? To me it seems that counts, dukes and tribals should also be able to own artifacts. -> How will the renown bonuses or penalties from grandeur expectations be handled? Do they only apply for the dynasty head, or for each ruler of the dynasty who has a court? Also: I don't like the income scaling for amenity costs. Increasing costs with the size of your realm makes some degree of sense, since you need to provide for more people. But scaling costs to your income just makes your income meaningless. Click to expand...
<!-- artifact:quote:end -->
Personal artifacts can be held by characters, only the court artifacts are for the kings and emperor with a royal court.

## Reply 31 — participant_027 · 2021-05-25 · post-27562267

Thst throne room's ceiling looks too... low. Maybe it's historical or it's just the camera angle. Can you adjust the angle a bit to make it look bigger? Also it maybe realistic but would you consider something more fantasy-like? Maybe a special one at the highest tier of court. Or You see what I mean? Fantasy courts always have high ceiling XD.

## Reply 32 — participant_028 · 2021-05-25 · post-27562268

<!-- artifact:quote:start -->
> johnty5 said: Aside from all the other stuff it does, Grandeur sounds like it might provide some couterpressure/downsides to rapid expansion/larger realms (which I think everyone around here agrees the game needs) by forcing players not to expand beyond their ability to keep up with expected Grandeur. Click to expand...
<!-- artifact:quote:end -->
Downsides to big empires is understandable, but increased prices that scale from your income on top of size, making you pay more even if you didn't expand but focused on improving your domain, this I will probably mod out asap

## Reply 33 — participant_024 · 2021-05-25 · post-27562277

Can we name our weapons and choose how to decorate them?

## Reply 34 — participant_029 · 2021-05-25 · post-27562278

<!-- artifact:quote:start -->
> Hospodar said: I'm assuming then there will be 5 court types, each ethos corresponding to one of the five skills? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Liggi said: Will the characters represented in your Throne Room be dynamically placed, or static? As in, will your Steward always stand in the same place in the same pose? Or is there variety to how characters are placed within the scene? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> johnty5 said: Couple of questions: 1. How inheritable is Grandeur? When a new King takes over, will they need to build up their Grandeur from scratch? 2. Does this mean that Amenities are an ongoing, monthly cost (like army maintanance) rather than a one-off "upgrade cost". Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Salazard260 said: On artifacts: would they work similarly to CKII? As in you collect them from different sources and they give you stat bonuses ? Would some of them (crowns, weapons etc) be visible on the portrait ? Can they be stolen / raided? Otherwise a cool concept as a whole, and the dynamic culture thing sounds like a very good addition gameplay and rp wise. Click to expand...
<!-- artifact:quote:end -->
We have five court types, corresponding with the five primary skills. Ethos on the other hand, we have a few more of. About seven or so. Each ethos unlock a court type that is somewhat "thematically appropriate" more than anything else. While this is still a work in progress, they will be dynamic to an extent. It depends on what type of characters you'll have present in your court. 1. You can expect your heir to inherit a large part of your granduer, so you won't lose all of your progress just because a succession occurred. Exact details are TDB. 2. Correct. Amenities should be seen as a "long-term" investement for you to increase your grandeur over time. Though they do have a few additional effects as well. We'll go into details of how artifacts work in a future DD.

## Reply 35 — participant_030 · 2021-05-25 · post-27562279

<!-- artifact:quote:start -->
> rageair said: Worth noting is that the cost of amenities is relative to your size and income; a small realm won’t have to pay as much as a prosperous one - the intent here is to allow smaller kingdoms and empires to ‘punch above their weight’ diplomatically, making choosing between expansion and consolidation a more relevant matter. Click to expand...
<!-- artifact:quote:end -->
A lot of concepts, a lot of ideas. I do not know yet whether I like the whole thing, but it certainly is an ambitious endeavour. That's good! I keep my fingers crossed for the devs, as many parts are tricky to be done correctly. But there is surely potential for something amazing! Having said that, three things bother me. The throne room being 3D means that a lot more effort and assets are necessary to create a new one with a different style. We already see the consequence - there are only 4 cultural variants announced (kinda-pagan, kinda-Christian, kinda-Arabic, kinda-Far-East?). It is also inconsistent with all other parts of the game (background + some 3D art) and will probably cause CK3 to run much worse on older machines (and it is almost impossible to upgrade the PC right now). I feel that doing the court screen with hand-painted background might have been a better idea. BTW - (a question for the devs) - what is the estimated framerate drop on the court scheme? How it will influence required hardware? Court types, culture ethea (and education focus, and lifestyles, and so on...) tend to be tied to the 5 main skills. Which might make them boring. Want to do a military thing? Stack all the military things. Want to do a learning thing? Stack scholarship things. And so on. I would really like them to be divided in another way, so the mixing-and-matching them with our gameplay style will not be a no-brainer. Religions are well designed in that manner, as there are no clear "diplomacy" or "stewardship" ones. We are definitely moving towards the "gold does not matter, everything has a percentage-based cost" approach of CK2 and it makes me sad... See this comment for details.

## Reply 36 — participant_028 · 2021-05-25 · post-27562281

<!-- artifact:quote:start -->
> Spirit_mert said: Ignoring tribal realms completely sounds bad in my opinion. Click to expand...
<!-- artifact:quote:end -->
I think what's worse is completely ignoring Dukes. Super-powerful elector in HRE? No, only king of Bohemia will get something. Mega-duke in Aquitaine that rivals the king easily? Nope, nothing because you want to play vassal game and your king isn't strong enough to form empire. I hope they will change their mind and add court to some dukes (like 2-3 duchies) or to all dukes but with some limitations

## Reply 37 — participant_004 · 2021-05-25 · post-27562283

<!-- artifact:quote:start -->
> Spirit_mert said: I hope you guys think again with Tribals not having a courtroom, I get the point you make but maybe a more basic, intimate clan hall room would be appropriate with some of the mechanics disabled? Ignoring tribal realms completely sounds bad in my opinion. Give them a cozy, wooden hall, with fur and animal hides laying around. Finally, add a few basic mechanics that are weaker than feudal ones. Would make tribals not left out and still weaker than feudal courts. Just a thought. Click to expand...
<!-- artifact:quote:end -->
I'm guessing that in a future expansion they'll introduce it, possibly in connection with the introduction of nomad realms which will likewise have the same sort of court equivalent as the tribal realms. Less about etiquettes, more about interfamilial interactions (possibly introducing family feuds, bloodwits and what not).

## Reply 38 — participant_031 · 2021-05-25 · post-27562287

<!-- artifact:quote:start -->
> rageair said: If a ruler is demoted to a lower rank (through war, election, or just sheer bad luck) their Royal Court and everything therein will either stay dormant until you regain your lost status, or follow the character who now rules in your stead. Click to expand...
<!-- artifact:quote:end -->
Oh yes, this looks pretty nice so far. In regards to that I have the question about what happens if one takes over a higher court. Does his court transfer or does he leave his old court just there and goes to his new one?

## Reply 39 — participant_006 · 2021-05-25 · post-27562288

<!-- artifact:quote:start -->
> rageair said: 1. We're actually discussing this internally! We're considering having it drop on succession, at least by a bit - making it so that you have to prove your worth as a new monarch. 2. Yes, they're a type of maintenance. Click to expand...
<!-- artifact:quote:end -->
This is good to hear. I think adding grandeur-drops during succession and adding maintenance gold-sinks to Kings and Emperors sound like good ways of fighting the "snowball into a stable big realm then the game gets a bit boring" problem that some people are running into in the mid/late game.

## Reply 40 — participant_009 · 2021-05-25 · post-27562292

<!-- artifact:quote:start -->
> ShadyGuy_SuspiciousGoal said: Thst throne room's ceiling looks too... low. Maybe it's historical or it's just the camera angle. Can you adjust the angle a bit to make it look bigger? Also it maybe realistic but would you consider something more fantasy-like? Maybe a special one at the highest tier of court. View attachment 723633 Or View attachment 723634 You see what I mean? Fantasy courts always have high ceiling XD. Click to expand...
<!-- artifact:quote:end -->
Something like this is better. This is not Westeros.

## Reply 41 — participant_032 · 2021-05-25 · post-27562293

Oh wow... Thats amazing. We are getting the artifacts back. I hope I can steal them or gift them to others. The treasury was my most loved feature in CK2

## Reply 42 — participant_028 · 2021-05-25 · post-27562298

<!-- artifact:quote:start -->
> rageair said: Your spouse will very often be shown, we think that it's a very thematically appropriate character to place close to the ruler. I believe the idea is to have them of their own throne next to your, at least in certain court styles where such a thing was common. Click to expand...
<!-- artifact:quote:end -->
Will the throne room and events reflect somehow situations when your spouse is a ruler (foreign ruler, not vassal) elsewhere or will they appear at any court event anyway?

## Reply 43 — participant_026 · 2021-05-25 · post-27562312

<!-- artifact:quote:start -->
> Prpht said: A lot of concepts, a lot of ideas. I do not know yet whether I like the whole thing, but it certainly is an ambitious endeavour. That's good! I keep my fingers crossed for the devs, as many parts are tricky to be done correctly. But there is surely potential for something amazing! Having said that, three things bother me. The throne room being 3D means that a lot more effort and assets are necessary to create a new one with a different style. We already see the consequence - there are only 4 cultural variants announced (kinda-pagan, kinda-Christian, kinda-Arabic, kinda-Far-East?). It is also inconsistent with all other parts of the game (background + some 3D art) and will probably cause CK3 to run much worse on older machines (and it is almost impossible to upgrade the PC right now). I feel that doing the court screen with hand-painted background might have been a better idea. BTW - (a question for the devs) - what is the estimated framerate drop on the court scheme? How it will influence required hardware? Court types, culture ethea (and education focus, and lifestyles, and so on...) tend to be tied to the 5 main skills. Which might make them boring. Want to do a military thing? Stack all the military things. Want to do a learning thing? Stack scholarship things. And so on. I would really like them to be divided in another way, so the mixing-and-matching them with our gameplay style will not be a no-brainer. Religions are well designed in that manner, as there are no clear "diplomacy" or "stewardship" ones. We are definitely moving towards the "gold does not matter, everything has a percentage-based cost" approach of CK2 and it makes me sad... See this comment for details. Click to expand...
<!-- artifact:quote:end -->
Being able to see everyone and your artifacts etc is a big part of the immersion into the royal court that we want hence the 3d scene instead of painted backgrounds. We are well aware of the performance implications and will be aiming to make sure it can run fine across our minimum and recommended hardwares, with some reduction of number of things on screen etc if required for the min specs like the options we already have for them. What other divisions would you want here? I don't think that is too true here, the specific nature of it is that exceeding one's expectations is easier when you are small and the expectations are low compared to someone like the HRE or Byzantines. So I think it makes a lot of sense design wise and thematically for this system.

## Reply 44 — participant_033 · 2021-05-25 · post-27562324

Sound good to me.

## Reply 45 — participant_034 · 2021-05-25 · post-27562326

<!-- artifact:quote:start -->
> blackninja9939 said: I don't think that is too true here, the specific nature of it is that exceeding one's expectations is easier when you are small and the expectations are low compared to someone like the HRE or Byzantines. So I think it makes a lot of sense design wise and thematically for this system. Click to expand...
<!-- artifact:quote:end -->
True enough, but the issue is not with the size and tier scaling but with income scaling. If court maintenance costs more the more money I have, what's the point of increasing my income?

## Reply 46 — participant_028 · 2021-05-25 · post-27562329

<!-- artifact:quote:start -->
> Prpht said: Religions are well designed in that manner, as there are no clear "diplomacy" or "stewardship" ones. Click to expand...
<!-- artifact:quote:end -->
They are though... Something like Struggle or Warmonger are clearly warlike, Pacifism is for domain bulding, Gnosticism is for learning, etc. It makes sense for Courts to be even more specialized though because they are held for a reason - to decide something about realm's live, to push someone's agenda, etc

## Reply 47 — participant_035 · 2021-05-25 · post-27562333

<!-- artifact:quote:start -->
> rageair said: Each Ethos unlocks more than one Court Type, and the Court Types are (currently) based on the five skills thematically, yes. Your spouse will very often be shown, we think that it's a very thematically appropriate character to place close to the ruler. I believe the idea is to have them of their own throne next to your, at least in certain court styles where such a thing was common. Dynamic, we're aiming for variation. The exact details are not nailed down yet. There are some modifiers, and depending on the Amenity level certain Court Events might be affected. 1. We're actually discussing this internally! We're considering having it drop on succession, at least by a bit - making it so that you have to prove your worth as a new monarch. 2. Yes, they're a type of maintenance. Click to expand...
<!-- artifact:quote:end -->
Will this mean that grandeur functions like legitimacy? That through grandeur usurpers have to prove themselves to their subjects that they are rightful rulers? I assume petty kings won't have courts. WIll tribal kings, instead of holding court, be able to hold tribal assemblies?

## Reply 48 — participant_036 · 2021-05-25 · post-27562334

I hope that we can make a type 'learned diplomat', or 'learned warrior', or 'while having hybrid cultures' to make a course as great as it is prestige, but I hope that it will be very difficult. to do it all the guys while by merging. Otherwise, I can't wait to have this DLC. And to be in the immersion.

## Reply 49 — participant_034 · 2021-05-25 · post-27562336

<!-- artifact:quote:start -->
> lozikk said: They are though... Something like Struggle or Warmonger are clearly warlike, Pacifism is for domain bulding, Gnosticism is for learning, etc. It makes sense for Courts to be even more specialized though because they are held for a reason - to decide something about realm's live, to push someone's agenda, etc Click to expand...
<!-- artifact:quote:end -->
This doesn't bother me so much as it resembles the way dynasty legacies work. It's not like I play an uninterrupted line of martial characters in any of my playthroughs. In fact, I make it a point to switch it up generation to generation. So this is more like deciding what stat I want to be consistently decent across all generations.

## Reply 50 — participant_008 · 2021-05-25 · post-27562344

Are we able to interact with the system as a vassal at all? I appreciate that a Duke will not have their own Royal Court, but if they have a King-level Liege, does the AI King have a Court that you can interact with at a Vassal level? Can you bring your concerns to the King, and is your character eligible to participate in "Court Events" from the AI King's perspective?

## Reply 51 — participant_006 · 2021-05-25 · post-27562348

I think the fact that the court system isn't going to be available to Tribes is a cause for optimism. Part of the problem with CK2 were mechanics that sat across all government types despite not being appropriate for some. This approach makes me think that we'll see a big tribal update at some point with new mechanics unique to them. A lot of people have been saying that playing in different areas of the world feels the same - and those kind of differences address that.

## Reply 52 — participant_037 · 2021-05-25 · post-27562355

<!-- artifact:quote:start -->
> Gwydden said: True enough, but the issue is not with the size and tier scaling but with income scaling. If court maintenance costs more the more money I have, what's the point of increasing my income? Click to expand...
<!-- artifact:quote:end -->
It is what I'm liking about it. It's a money sink and has historical precedent. It's already easy enough to have a lot of gold after some time played. It's going to expand the RPG aspect of the game and internal affairs.

## Reply 53 — participant_030 · 2021-05-25 · post-27562365

<!-- artifact:quote:start -->
> blackninja9939 said: Being able to see everyone and your artifacts etc is a big part of the immersion into the royal court that we want hence the 3d scene instead of painted backgrounds. We are well aware of the performance implications and will be aiming to make sure it can run fine across our minimum and recommended hardwares, with some reduction of number of things on screen etc if required for the min specs like the options we already have for them. What other divisions would you want here? I don't think that is too true here, the specific nature of it is that exceeding one's expectations is easier when you are small and the expectations are low compared to someone like the HRE or Byzantines. So I think it makes a lot of sense design wise and thematically for this system. Click to expand...
<!-- artifact:quote:end -->
Thanks a lot for replying! 1. Sounds reassuring! 3. I mostly feel bad about "% of income" costs. Basing it on realm size, number of titles, development (please use development more! it should be easier to have a grand court in developed lands) is perfectly fine! 2. Something different? E.g. ten types of courts for every pair of skills (martial+scholarship=crusading, intrigue+stewardship=mercantile, etc.). Or treat it as religion (and as Stellaris empires) and make each court have 2-3 traits ("invites commoners", "enjoys fencing and tournaments", "drinks a lot", "lots of protocols", "customary gifts"). Or do it as a local quasi-political system ("autocratic monarch", "religious advisors", "influential spouses"). Basically anything that does not mimic the existing skill system and copy the lifestyle bonuses.

## Reply 54 — participant_036 · 2021-05-25 · post-27562369

Will it be possible to personalize our royal court? With size, Tapestry, Object, Seat ...

## Reply 55 — participant_038 · 2021-05-25 · post-27562372

I've only had two serious CK3 playthroughs so far because the game still feels a bit empty. I felt like I had already seen almost everything, so I played CK2 instead and reformed the Suomenusko faith or something. This DLC, however, looks like it's just the update I have been waiting for to promote CK3 to CK2 levels of replayability. Artifacts were one of my favorite mechanics from CK2 - I'll never forget my conquest imprisonment murder rampage in Ethiopia to obtain the Ark of the Covenant, for example. I'm glad that they'll be back - they'll give me something else to collect other than congenital traits. Also, CK3's culture system felt quite lacking compared to the religion system, especially since some religious tenets could be argued to be more about cultural than religious norms. I appreciate that culture will be promoted to be as immersive as the religious system in the upcoming DLC. The return of minor titles, and expansion of their effects, is a welcome addition. They were always a bit boring in CK2 because most of them had no real gameplay effects, so I just named a guy Keeper of the Swans when I had to improve his opinion by 5 to force him to convert or something. I was hoping for flavor events related to the title, but there just weren't any. Btw, does somebody happwn to know the timestamp of the Royal Court being discussed in last weekend's PDXcon? I skipped some parts because I don't care about the management perspective and the non-GSG titles, and I must have accidentally skipped the Royal Court discussion.

## Reply 56 — participant_006 · 2021-05-25 · post-27562377

<!-- artifact:quote:start -->
> nyappi57 said: Will it be possible to personalize our royal court? With size, Tapestry, Object, Seat ... Click to expand...
<!-- artifact:quote:end -->
Oooh. Tapistries depicting things your character has done! Battles won, pilgrimages they've been on etc.

## Reply 57 — participant_039 · 2021-05-25 · post-27562383

About the inheritance of grandeur, I don't know if you are taking suggestions, but it would be really nice to have it tied at least a bit to some kind of coronation event. For something really basic, it could be simple like losing a certain quantity of grandeur depending on how much you are willing to spend for your coronation, but it would be nice if it were something more involved, like a feast. In any case, I think it would make a lot of sense thematically and give some flavour.

## Reply 58 — participant_036 · 2021-05-25 · post-27562385

Will each royal court be different for each culture?

## Reply 59 — participant_040 · 2021-05-25 · post-27562393

Looks great! Two questions: How moddable will the system be? Could courts for powerful Dukes or tribals be modded in? Is the decision of scaling court expenses to income final? If not, consider this suggestion: While realm size should definitely be factored in, scaling it to income needs to be carefully balanced in order to not make increasing income meaningless. If I have a gold mine in my domain, it should reflect on my court. To counterbalance, high income should (in addition to all other factors) increase the expectations of your court.

## Reply 60 — participant_041 · 2021-05-25 · post-27562395

I am absolutely in love in everything that was written in this DD.

## Reply 61 — participant_006 · 2021-05-25 · post-27562396

<!-- artifact:quote:start -->
> namewhichisnottakenyet said: especially since some religious tenets could be argued to be more about cultural than religious norms. Click to expand...
<!-- artifact:quote:end -->
This is a good point. There's definitely scope to remove some aspects from the religious system and add them to the cultural one.

## Reply 62 — participant_042 · 2021-05-25 · post-27562397

Incredible dev diary! I have three questions : - Will I, as a vassal, be able to interact with my liege's court? - Will I, as a ruler, be able to visit other monarch's court? - Are throne rooms related to geography? If you have your throne room in Paris, and lose Paris, do you still have access to your throne room? Thank you so much for all of the information!

## Reply 63 — participant_028 · 2021-05-25 · post-27562404

<!-- artifact:quote:start -->
> johnty5 said: This is a good point. There's definitely scope to remove some aspects from the religious system and add them to the cultural one. Click to expand...
<!-- artifact:quote:end -->
Would be a good idea if culture-merging wasn't a DLC mechanic. Expanding on this thought is ok, but not removing something from religions from base game

## Reply 64 — participant_043 · 2021-05-25 · post-27562419

The throne room looks awesome! Can we click on the characters? Is it interactive?

## Reply 65 — participant_006 · 2021-05-25 · post-27562420

<!-- artifact:quote:start -->
> lozikk said: Would be a good idea if culture-merging wasn't a DLC mechanic. Expanding on this thought is ok, but not removing something from religions from base game Click to expand...
<!-- artifact:quote:end -->
Ah, yeah. Hadn't thought of that.

## Reply 66 — participant_008 · 2021-05-25 · post-27562421

<!-- artifact:quote:start -->
> lozikk said: Would be a good idea if culture-merging wasn't a DLC mechanic. Expanding on this thought is ok, but not removing something from religions from base game Click to expand...
<!-- artifact:quote:end -->
I'm pretty sure the cultural overhaul isn't DLC locked.

## Reply 67 — participant_044 · 2021-05-25 · post-27562427

Will pets be shown ? It's a tiny thing but would be a nice touch ! Also I hope we can scheme to steal artifacts ... I wanna do a CK Oceans 11 !

## Reply 68 — participant_028 · 2021-05-25 · post-27562444

<!-- artifact:quote:start -->
> Liggi said: I'm pretty sure the cultural overhaul isn't DLC locked. Click to expand...
<!-- artifact:quote:end -->
Well it's talked about in the Vision of dlc. We don't know what is going to be in the free patch yet, only expansion content

## Reply 69 — participant_045 · 2021-05-25 · post-27562448

This looks amazing! I have just 1 question: Will high grandeur always be positive? There have been numerous examples throughout history of rulers being accused of decadence for spending too much on their court/feasts/clothes. Particularly in warlike societies (later Mongols), the Caliphates (late Abbasids for instance) and even some examples in Medieval Europe (Edward the II). Many of the accusations came from the clergy. It would be an interesting mechanic if, depending on your cultural ethos, you would get penalized with piety and opinion for overshooting your grandeur. Like a maximum expectation together with a minimum one. This would add more variety between cultures, provide a clear trade-off system (grandeur is still good even if penalized) and allow the player to change the constraints (can change cultural ethos for a more opulent society). What do you think? EDIT: Also for roleplay - Be the decadent bastard everyone hates that spends all the kingdoms money on feasts while the plague ravages the kingdom. Common I want to be hated for spending too much money!

## Reply 70 — participant_046 · 2021-05-25 · post-27562459

<!-- artifact:quote:start -->
> Prpht said: ... Having said that, three things bother me. ... and will probably cause CK3 to run much worse on older machines (and it is almost impossible to upgrade the PC right now). I feel that doing the court screen with hand-painted background might have been a better idea. BTW - (a question for the devs) - what is the estimated framerate drop on the court scheme? How it will influence required hardware? Click to expand...
<!-- artifact:quote:end -->
Low-spec machines are already encouraged to use static portraits, without animations, so in that case court room will also be static - 3D image won't be rendered every frame, but updated only when needed. Considering this scene hides the game map, we're quite optimistic that we'll be able to deliver a good result for all players.

## Reply 71 — participant_047 · 2021-05-25 · post-27562470

So... When will we be able to walk around London? like in 4-5 DLCs? Jokes aside, I hope someday we'll get 3D models for our pets. I'd love to see my Dog or Horse. And you could make that in some conditions your ruler would be on the horse. It's not an important feature xP But I would've loved if you had this on the list.

## Reply 72 — participant_041 · 2021-05-25 · post-27562482

I know You guys said that the Tribal Rules won't get Throne Room, but maybe would it be possible to make it locked behind Tier 3/Tier 4 Tribal Authority and/or tie it with some sort of religious celebration (event/decision)? And let the Grandeur have 0 baseline for them, so it will drop early or something like that.

## Reply 73 — participant_048 · 2021-05-25 · post-27562486

I suggest that you could win a banner when you win a war to show it in the court room.

## Reply 74 — participant_038 · 2021-05-25 · post-27562488

<!-- artifact:quote:start -->
> Anonim97 said: I know You guys said that the Tribal Rules won't get Throne Room, but maybe would it be possible to make it locked behind Tier 3/Tier 4 Tribal Authority and/or tie it with some sort of religious celebration (event/decision)? And let the Grandeur have 0 baseline for them, so it will drop early or something like that. Click to expand...
<!-- artifact:quote:end -->
Yes, I'd actually like to see a visual of a tribal longhouse decorated with bear pelts or so, even if it's just visual without a grandeur bonus.

## Reply 75 — participant_006 · 2021-05-25 · post-27562493

<!-- artifact:quote:start -->
> general_nabo said: I suggest that you could win a banner when you win a war to show it in the court room. Click to expand...
<!-- artifact:quote:end -->
Or the head of the defeated on a spike...

## Reply 76 — participant_049 · 2021-05-25 · post-27562498

Will you add more penalties and restraints related to the throne room? I hope the bonuses from artifacts won't be too great? The game is too simple, I would like more negative effects, events, etc.

## Reply 77 — participant_050 · 2021-05-25 · post-27562501

Considering the Vikings are the poster child for tribal rulers in this game (even having received the first flavour pack) why can't they have a court? Didn't they have their Viking Things where the tribal ruler would have his vassals assembled and bring their grievances? I think it's a wasted opportunity to not give tribal a court as well.

## Reply 78 — participant_041 · 2021-05-25 · post-27562509

<!-- artifact:quote:start -->
> namewhichisnottakenyet said: Yes, I'd actually like to see a visual of a tribal longhouse decorated with bear pelts or so, even if it's just visual without a grandeur bonus. Click to expand...
<!-- artifact:quote:end -->
Yup, I kinda tacked grandeur just for the sake of it, but this is my main motivation. I want to see it!

## Reply 79 — participant_051 · 2021-05-25 · post-27562520

I'm honestly really intrigued in seeing a court with multiple characters and artifacts, and I can't wait to see more about all the various additional jobs unlocked with grandeur, and especially about inspired guests\people! I don't know if you can answer it yet, since it's very early in development: have you an idea of how many artifacts can be displayed in the court room? Also, since the throne room is an entire new interface from what I've gathered, have you an idea of how much time in game should a player spend in the courtroom? Is it something you check up once every 1 or 2 years or every 3-4 months, or is it more "randomized"?

## Reply 80 — participant_052 · 2021-05-25 · post-27562529

<!-- artifact:quote:start -->
> rageair said: Now, Amenities are simple and straightforward; but they’re still central to the concept of having a grand court! There are four different types; Lodgings, Food, Clothing and Servants. Click to expand...
<!-- artifact:quote:end -->
Clothing? Only clothing? I can't force my courtiers to wear armour and behave in a martial way fitting of a martial court? I want those fops whipped into fighting shape, no fancy clothing in the Empire of Vorbasse!

## Reply 81 — participant_053 · 2021-05-25 · post-27562530

OMG, FANTASTIC! Are Throne Rooms moddable (graphics, models in particular)?

## Reply 82 — participant_054 · 2021-05-25 · post-27562536

<!-- artifact:quote:start -->
> rageair said: Court Events Now, the Royal Court isn’t all about Grandeur, of course. Another important role it holds is to show that there’s life in your court! This is done through Court Events; happenings contained within the court, taking place between those who live therein. This new type of event uses the throne room as its backdrop, transforming the entire throne room into an event when they happen. Unlike normal events, this type of event is non-interruptive - you get notified that something is happening, whereby you can go into your Royal Court, inspect the scene, find whoever is involved, and trigger the event yourself. Usually these events are some sort of drama happening between your courtiers, which you can choose to simply ignore if you feel like you have more important matters to attend to. These events come in many different flavors, mostly focusing on how it is to live in the court. Some examples of court events that are being worked on currently include courtiers causing you embarrassment through their drinking or poor manners, or getting into arguments with your architect. Others involve things like rumors spreading about your predecessor on the throne, or popular and unflattering songs about you spreading within the court itself. Court events might also be things like foreign ambassadors trying to uncover your secrets or devout courtiers shaming you and your court for your frivolous living. Click to expand...
<!-- artifact:quote:end -->
Will assassinations be rendered in gory detail as court events?

## Reply 83 — participant_055 · 2021-05-25 · post-27562540

Are there any plans to make every day ruling as a duke also more immersive ? If not by having their own grand court then perhaps by some other minor means like a greater number of new events connected to ruling a rather great piece of land ?

## Reply 84 — participant_056 · 2021-05-25 · post-27562555

This seems like an excellent thing to have cultural innovations/techs affect and change - it would be interesting to have your culture change things like whether dukes get a court, whether usurpers inherit their predecessor's Grandeur, how much is inherited by regular heirs... there are lots of possibilities!

## Reply 85 — participant_057 · 2021-05-25 · post-27562566

Will the court haver any permanence in the game world? The fact is that the moving of the court from one city to another was a HUGE DEAL within the timeframe of the game, and that there were far-reaching consequences and implications of setting up court elsewhere. See Versailles, St. Petersburg, Milan or the many Courts of Cordobans, Mamluks and Seljuks. Not only should it be costly, especially with larger courts, but which area (De Jure territory) religion, culture and such present should have implications for opinion and unrest, just as an example of possible consequences moving courts could have. Maybe having to build court complexes before moving to ensure a smooth transitions, not being able to just take the entire Parisian metropolean court and move it to some farmland further south overnight. Edit: To expand on this, the move of the court could be a good way to distance oneself from corrupt and old-fashioned aristocracy that had built itself up over the years, and many councillours and nobles would quickly have to decide wheter to embrace the move or not. It also was important in regional relations, as a closer proximity to the court became an important change both symbolically and logistically for those left behind, and those now hosting the new courts, be it the local population or the nobility.

## Reply 86 — participant_054 · 2021-05-25 · post-27562573

<!-- artifact:quote:start -->
> rageair said: It’s really hard to pick a topic for where to start, but we decided upon a dive into the namesake feature of the expansion - the Royal Court itself, your seat of royal majesty and power! The Royal Court consists of many features, all collected within a 3D scene that we call the Throne Room. Here’s an early Work in Progress screenshot of the throne room - do note that it’s a very early version, but we just can't wait to show you what we have been working on! Click to expand...
<!-- artifact:quote:end -->
Will there be a special throne room for the Byzantine Empire with mechanical singing birds and roaring lions? Fortunately, we have a detailed surviving account of it from the 10th century in the Relatio de Legatione Constantinopolitana by Liutprand of Cremona

## Reply 87 — participant_058 · 2021-05-25 · post-27562587

<!-- artifact:quote:start -->
> rageair said: Court Events ... Some examples of court events that are being worked on currently include courtiers causing you embarrassment through their drinking or poor manners, or getting into arguments with your architect. Others involve things like rumors spreading about your predecessor on the throne, or popular and unflattering songs about you spreading within the court itself. Court events might also be things like foreign ambassadors trying to uncover your secrets or devout courtiers shaming you and your court for your frivolous living. Click to expand...
<!-- artifact:quote:end -->
Everything looks awesome!!! A couple questions: - Right now the only way to make courtier leave the court is to kick them out or kill them off. Will there be cheaper alternatives than the current (100 prestige to kick out a lowborn courtier looks very high, a bowmen MaA regiment, for a tribal ruler, cost nearly 100 prestige) or some other mechanic? - What about a mechanic to avoid the overcrowding of a court, like in ck2? - Will there be court options (not with the Throne room) also for lower tier rulers (counts, dukes)? - Will there be also positive events inside the court? I'm all for increasing the difficulty of the game but you described only negative events. - Will this expansion included for the ones who purchased the premium at launch? Thanks for your amazing job!!!! Edit: prestige cost to kick out courtiers

## Reply 88 — participant_059 · 2021-05-25 · post-27562606

<!-- artifact:quote:start -->
> johnty5 said: Couple of questions: 1. How inheritable is Grandeur? When a new King takes over, will they need to build up their Grandeur from scratch? 2. Does this mean that Amenities are an ongoing, monthly cost (like army maintanance) rather than a one-off "upgrade cost". Click to expand...
<!-- artifact:quote:end -->
Considering they said maintain a monthly cost

## Reply 89 — participant_006 · 2021-05-25 · post-27562623

<!-- artifact:quote:start -->
> Koyraboro said: Considering they said maintain a monthly cost Click to expand...
<!-- artifact:quote:end -->
Yep. A dev replied and confirmed. tbf, "maintain" could have meant a one-off payment that boosts amenities for a set length of time - but needs to repeated eventually - or some a similar mechanism. I was just asking for some clarification.

## Reply 90 — participant_060 · 2021-05-25 · post-27562628

<!-- artifact:quote:start -->
> rageair said: Others involve things like rumors spreading about your predecessor on the throne, or popular and unflattering songs about you spreading within the court itself. Click to expand...
<!-- artifact:quote:end -->
This sounds so cool. I'm already hyped for this expansion - continue the good work! You mentioned there would be some dev diaries for the Azure patch before you go on summer holidays; when is the summer holidays for PDX and are you planning to release 1.4 before or after?

## Reply 91 — participant_061 · 2021-05-25 · post-27562629

<!-- artifact:quote:start -->
> rageair said: Of course, this expansion isn’t all about the Royal Court; before the summer break starts you’ll get to read about some of the other features coming with the expansion and patch. Click to expand...
<!-- artifact:quote:end -->
Could you give us a quick breakdown of which of the announced features would be included in the patch, and what in the expansion? For example: the culture overhaul would be included in the former or the latter?

## Reply 92 — participant_062 · 2021-05-25 · post-27562634

Nice. Looking forward to its release

## Reply 93 — participant_034 · 2021-05-25 · post-27562637

<!-- artifact:quote:start -->
> GeorgieBest said: This sounds so cool. I'm already hyped for this expansion - continue the good work! You mentioned there would be some dev diaries for the Azure patch before you go on summer holidays; when is the summer holidays for PDX and are you planning to release 1.4 before or after? Click to expand...
<!-- artifact:quote:end -->
Based on previous dev diaries, I believe the plan is to hopefully release Azure before the holidays and Royal Court with the accompanying patch by year's end.

## Reply 94 — participant_063 · 2021-05-25 · post-27562639

Will Coronation Crowns and robes ever be a thing? Especially for France and England?

## Reply 95 — participant_064 · 2021-05-25 · post-27562642

Really excited about the development going on. The future of CK3 is looking amazing. Ngl though, I am very curious to hear about the dynamic cultures talked about during PDXCon. I humbly request that that be one of the first topics after the Azure patch dev diaries are wrapped up. Keep up the good work!

## Reply 96 — participant_006 · 2021-05-25 · post-27562643

Can I just say how brilliant this thread is. People being excited, people asking for clarifications and getting them, people riffing idea/suggestions for the devs about how the mechanics might/could work. I think I've only spotted one kneejerk negative post in the whole thread. This is these forums at their best.

## Reply 97 — participant_065 · 2021-05-25 · post-27562660

Is Grandeur linked to a character or to a title?

## Reply 98 — participant_006 · 2021-05-25 · post-27562666

<!-- artifact:quote:start -->
> Liquid Ghost said: Is Grandeur linked to a character or to a title? Click to expand...
<!-- artifact:quote:end -->
One of the devs said it'll likely drop a bit on succession - so it sounds like it's a bit of both.

## Reply 99 — participant_046 · 2021-05-25 · post-27562671

<!-- artifact:quote:start -->
> TheMind said: OMG, FANTASTIC! Are Throne Rooms moddable (graphics, models in particular)? Click to expand...
<!-- artifact:quote:end -->
Character models are the same used in portraits and events windows, and throne room interior and various objects are described in various script files. So yes, it's moddable. Although the system is still heavily driven by royal court code logic, so it can only be used to display the royal court.

## Reply 100 — participant_066 · 2021-05-25 · post-27562676

It's a shame tribals don't get access but maybe that means they will get their own better suited mechanic later? It's also a shame dukes and counts agent getting a version of this. If your a vassal how do you interact with this system?

## Reply 101 — participant_046 · 2021-05-25 · post-27562677

<!-- artifact:quote:start -->
> Liquid Ghost said: Is Grandeur linked to a character or to a title? Click to expand...
<!-- artifact:quote:end -->
It's tied to the court - it's a thing in itself. It belongs to a single person at any time, and can be inherited

## Reply 102 — participant_006 · 2021-05-25 · post-27562686

<!-- artifact:quote:start -->
> Alien-47 said: Character models are the same used in portraits and events windows, and throne room interior and various objects are described in various script files. So yes, it's moddable. Although the system is still heavily driven by royal court code logic, so it can only be used to display the royal court. Click to expand...
<!-- artifact:quote:end -->
I don't even want to think about the Adamite mods that will arrive the day after the DLC releases.

## Reply 103 — participant_042 · 2021-05-25 · post-27562702

<!-- artifact:quote:start -->
> Alien-47 said: It's tied to the court - it's a thing in itself. It belongs to a single person at any time, and can be inherited Click to expand...
<!-- artifact:quote:end -->
I'll try my luck one last time because this is great information and I'm very excited : - If the court is a thing in itself, is it placed on the map? Let's say that you overthrow your Emperor Liege, and he becomes your King vassal. Does he keeps his court (since he is still King+ rank)? Do you get his court and he gets a new one? What happens to your old court if you inherit his? Or does the court follows title succession law and can move on the map?

## Reply 104 — participant_067 · 2021-05-25 · post-27562709

<!-- artifact:quote:start -->
> rageair said: Reaching your baseline might take a long time, unless you decide to take action in order to speed it up - to gain grandeur fast, you need to Hold Court! Performing this decision invites your vassals and subjects to bring their issues, requests, and questions before you. The mere act of Holding Court will give you a one-time boost to your Grandeur, but the opportunities within the activity itself might give you opportunities to increase it further (or you could decide to lose grandeur for some temporal gain that is just too good to pass up!). The issues brought forth when Holding Court are many and varied, with many of them reacting to the state of your realm (more on Hold Court in a later DD). Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> rageair said: Unlike normal events, this type of event is non-interruptive - you get notified that something is happening, whereby you can go into your Royal Court, inspect the scene, find whoever is involved, and trigger the event yourself. Click to expand...
<!-- artifact:quote:end -->
Will existing gatherings, namely feasts and hunts, also tie into the Grandeur system? I'd love to see new and old systems be integrated, instead of everything more or else existing on their own and not interacting. Will this work like the minor events in IR, where there's an alert in the outliner? Also, will we have the option to be able to set it so that it does pause the game, if we don't want to miss them? (I assume that if you actually open the event up, it does pause the rest of the game. I was referring more to when the event becomes available.) Also, I am rather concerned about the "inspect the scene, find whoever is involved, and trigger the event yourself" part. Having to hunt around a 3D UI like a point and click adventure game to trigger the events seems like it could become tedious very fast.

## Reply 105 — participant_068 · 2021-05-25 · post-27562736

When is the summers holiday on Sweden?

## Reply 106 — participant_069 · 2021-05-25 · post-27562751

<!-- artifact:quote:start -->
> zweihander said: When is the summers holiday on Sweden? Click to expand...
<!-- artifact:quote:end -->
The month of July. Not everyone takes the full month, but Sweden essentially shuts down during this month.

## Reply 107 — participant_046 · 2021-05-25 · post-27562770

<!-- artifact:quote:start -->
> Ul90 said: I'll try my luck one last time because this is great information and I'm very excited : - If the court is a thing in itself, is it placed on the map? Let's say that you overthrow your Emperor Liege, and he becomes your King vassal. Does he keeps his court (since he is still King+ rank)? Do you get his court and he gets a new one? What happens to your old court if you inherit his? Or does the court follows title succession law and can move on the map? Click to expand...
<!-- artifact:quote:end -->
If the emperor becomes king, he keeps his existing court. If you were a king and became the emperor, you keep your existing court. Both court parameters might change due to change in rank, though. The only way to get an existing court is to inherit it. Court is tied to a ruler and has no special connection to locations on the map. Court is located with the ruler

## Reply 108 — participant_070 · 2021-05-25 · post-27562792

Will the next hotfix drop with the expansion or can we expect some bugfixing in the meantime. . . .?

## Reply 109 — participant_028 · 2021-05-25 · post-27562799

<!-- artifact:quote:start -->
> Alien-47 said: It's tied to the court - it's a thing in itself. It belongs to a single person at any time, and can be inherited Click to expand...
<!-- artifact:quote:end -->
How will it work if a king inherits another kingdom? (Like Jimena siblings)? Will it remain as it was or get +/- to current Grandeur?

## Reply 110 — participant_006 · 2021-05-25 · post-27562800

<!-- artifact:quote:start -->
> Alien-47 said: If the emperor becomes king, he keeps his existing court. If you were a king and became the emperor, you keep your existing court. Both court parameters might change due to change in rank, though. The only way to get an existing court is to inherit it. Court is tied to a ruler and has no special connection to locations on the map. Court is located with the ruler Click to expand...
<!-- artifact:quote:end -->
This is interesting. Is it possible to downgrade your amenities? It occurs to me that a character that loses an empire and becomes a king might have a very expensive-to-maintain court (appropriate to the expected grandeur of an emperor) that becomes unsustainable (and unneccessary) at the king rank.

## Reply 111 — participant_071 · 2021-05-25 · post-27562804

<!-- artifact:quote:start -->
> rageair said: Grandeur The key concept that enables this is called Grandeur - a measurement of your standing in the eyes of your peers. While it’s measured on a scale from 0-100, it’s not necessarily a simple system. Increasing your grandeur will lead to direct political benefits, such as increased opinions, marriage acceptance, etc. It will also unlock new Council Jobs, such as being able to peacefully demand De Jure land with the ‘Convince De Jure Territory’ job, or gain Knight Effectiveness while also decreasing enemy Scheme Success Chance with the ‘Manage Royal Guards’ job. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> rageair said: One of the most significant effects of Grandeur is its effect on attraction of Inspired characters - the higher your Grandeur is compared to that of your neighbors, the likelier you are to have these creative travelers visit your court first, giving you an opportunity for patronage (more on Inspirations in a future DD). Click to expand...
<!-- artifact:quote:end -->
Does this mean neighboring AI with high grandeur will be able to take de jure land from me without giving me the opportunity to resist? Or does it rely on the target accepting the demand? If the latter, why would a player ever accept? Does this interact with the wanderer system, or is it just random events that spawn high stat characters? The current wanderer system feels extremely arbitrary and chaotic, and so is not particularly interesting, so this would be a great opportunity to improve it. A system that just generates more or fewer random high stat characters is much less compelling.

## Reply 112 — participant_006 · 2021-05-25 · post-27562805

<!-- artifact:quote:start -->
> Sh4ark said: Will the next hotfix drop with the expansion or can we expect some bugfixing in the meantime. . . .? Click to expand...
<!-- artifact:quote:end -->
Azure 1.4 is coming out before the next expansion (possibly in June if they get it done before the holidays).

## Reply 113 — participant_072 · 2021-05-25 · post-27562811

A bit disappointed that all of this flies over the heads of counts and dukes. I get that grandeur isn't exactly associated with lesser nobility, but playing as a small ruler is pretty slow as things are currently. I was hoping to myself there'd be some RP opportunities for minor nobles in order to make up for their low amount of engagement compared to kings and emperors, but now it looks like kings and emperors are only going to become even more fun to play relative to minors. Not only are you missing out on the high-level grand strategic gameplay as a minor, but now you're missing out on all this RP. But, reservations aside, the court looks like a fantastic addition to the game.

## Reply 114 — participant_073 · 2021-05-25 · post-27562827

Will our courts be the new main menu background?

## Reply 115 — participant_074 · 2021-05-25 · post-27562838

<!-- artifact:quote:start -->
> We’re trying to bridge the gap between your character and the map, Click to expand...
<!-- artifact:quote:end -->
The thing I wanted the most out of CK3. You can't take this too far for my taste. I hope this means that in the future events will be location aware and we won't have non-sensical events with teleporting participants.

## Reply 116 — participant_075 · 2021-05-25 · post-27562845

its a shame dukes dont get it. maybe it could be based on how many vassals/courtiers you have if youre a count/duke

## Reply 117 — participant_004 · 2021-05-25 · post-27562847

<!-- artifact:quote:start -->
> rageair said: making choosing between expansion and consolidation a more relevant matter. Click to expand...
<!-- artifact:quote:end -->
As long as partition is the default succession method then expansion is the only relevant option.

## Reply 118 — participant_053 · 2021-05-25 · post-27562849

<!-- artifact:quote:start -->
> Alien-47 said: Court is tied to a ruler and has no special connection to locations on the map. Court is located with the ruler Click to expand...
<!-- artifact:quote:end -->
So I can Hold Court whilst on a pilgrimage?

## Reply 119 — participant_042 · 2021-05-25 · post-27562858

<!-- artifact:quote:start -->
> TheMind said: So I can Hold Court whilst on a pilgrimage? Click to expand...
<!-- artifact:quote:end -->
Probably not, I'm pretty sure you'll need to be available and at court, much like to hold a feast.

## Reply 120 — participant_046 · 2021-05-25 · post-27562859

<!-- artifact:quote:start -->
> IntoTheStars said: Will our courts be the new main menu background? Click to expand...
<!-- artifact:quote:end -->
No, current backgrounds are static 2D-images, royal court scene is a complicated composition driven by various parameters and its own logic. There's simply no way to access any of it in the main menu.

## Reply 121 — participant_060 · 2021-05-25 · post-27562864

<!-- artifact:quote:start -->
> Gwydden said: Based on previous dev diaries, I believe the plan is to hopefully release Azure before the holidays and Royal Court with the accompanying patch by year's end. Click to expand...
<!-- artifact:quote:end -->
Thanks!

## Reply 122 — participant_076 · 2021-05-25 · post-27562865

Just imagine, in CK4 you can walk trough your courtroom, or maybe your castle. How friggin' awesome.

## Reply 123 — participant_071 · 2021-05-25 · post-27562869

<!-- artifact:quote:start -->
> rageair said: The effects of not living up to your expectations are many; reduced prestige, renown, and a hefty hit to opinion with both foreign rulers, courtiers and vassals. A large realm might easily find itself facing significant unrest unless its ruler starts spending on grandeur! On the other hand, a small kingdom that vastly exceeds the expectations put upon it might see significant bonuses to its diplomatic power, as well as renown and other bonuses. Click to expand...
<!-- artifact:quote:end -->
The AI already finds itself thousands of gold in debt because it cannot close out wars in a timely fashion and is eager to embark/disembark its armies. How will the AI manage to find money to spend on grandeur? Similarly, whenever a realm is partitioned in inheritance, the second son is currently left with nothing but a pile of levies, making it almost impossible to hold their new throne. Apparently 1.4 will give them some starting men at arms, which might help. But will they now suffer from having an empty court, no grandeur, and no time to acquire any? How will a newly partitioned son manage?

## Reply 124 — participant_077 · 2021-05-25 · post-27562870

What happens if a character inherits a court that already has one? Do you get to choose which one you want to keep? Or do you get everything and average the Grandeur of the two courts?

## Reply 125 — participant_078 · 2021-05-25 · post-27562915

Does the court have any effect on you if you are a vassal? Do you get some events on your liege's court and can you view it?

## Reply 126 — participant_079 · 2021-05-25 · post-27562922

i know this question is dodged, but : Playing as a vassal to a king/empreror, do we have access to our liege court when he's holding the court ?

## Reply 127 — participant_080 · 2021-05-25 · post-27562924

I always liked this feature in Civilization (II?) and i don't know why they scrapped it for the following installments of the series.

## Reply 128 — participant_073 · 2021-05-25 · post-27562939

<!-- artifact:quote:start -->
> Alien-47 said: No, current backgrounds are static 2D-images, royal court scene is a complicated composition driven by various parameters and its own logic. There's simply no way to access any of it in the main menu. Click to expand...
<!-- artifact:quote:end -->
Ah well. Thanks for the answer!

## Reply 129 — participant_081 · 2021-05-25 · post-27562947

Now let's talk about savegame compatibility. Are last version savegames playable? PLEASE SAY YES

## Reply 130 — participant_082 · 2021-05-25 · post-27562951

"devout courtiers shaming you and your court for your frivolous living" Reminder that not all the world is Catholic, and that several game events already make wrong assumptions about that Devout courtiers whose religion has Ritual Celebrations should have a completely different opinion of what counts as "frivolous living", compared to say Asceticism.

## Reply 131 — participant_083 · 2021-05-25 · post-27562956

What happens if the king is a baby/newborn? Does it just show them in a pile of blankets on the throne? Would a regent-servant-wetnurse-etc hold them?

## Reply 132 — participant_028 · 2021-05-25 · post-27562961

<!-- artifact:quote:start -->
> MoSherif said: Now let's talk about savegame compatibility. Are last version savegames playable? PLEASE SAY YES Click to expand...
<!-- artifact:quote:end -->
Unlikely because of culture changes. Anyway, there's no way it comes out anytime soon. Azure will come out somewhere in summer (and they say they have a full July as vacations), and DLC will only be some time after that. Even if you play 1 year per day you'll probably finish any ongoing campaign by the release day

## Reply 133 — participant_028 · 2021-05-25 · post-27562969

<!-- artifact:quote:start -->
> Pancakelord said: What happens if the king is a baby/newborn? Does it just show them in a pile of blankets on the throne? Would a regent-servant-wetnurse-etc hold them? Click to expand...
<!-- artifact:quote:end -->
Here's hoping that free patch will introduce regencies to accompany dlc so the throne will be taken by the regent

## Reply 134 — participant_082 · 2021-05-25 · post-27562978

<!-- artifact:quote:start -->
> lozikk said: Here's hoping that free patch will introduce regencies to accompany dlc so the throne will be taken by the regent Click to expand...
<!-- artifact:quote:end -->
Unless you're Gondor, then the throne will be empty while the regent sits on the steps

## Reply 135 — participant_084 · 2021-05-25 · post-27563000

Unless the gameplay impacts of not living up to expectations are incredibly severe and crippling, I do not see grandure as relevant to the gameplay other than roleplaying.

## Reply 136 — participant_085 · 2021-05-25 · post-27563014

With the new court positions, have you considered adding designated regents? I really like the idea of adding regents who interact with the court while you are away- either leading an army, sick, on a pilgrimage, etc.- who may either maliciously or accidentally screw things up at home while you are away. Think of Prince John ruling in the stead of Richard the Lionheart, who ended up angering all of the nobility while his brother was off crusading. Leaving your court should be a difficult decision because you will be leaving your people in the hands of another, and I think that this is something CK3 needs more of. While we all like micromanaging everything, because we as players can min/max it, delegating authority and deciding who to delegate it to was in many ways the primary job of any feudal ruler, and I think the game can better represent this

## Reply 137 — participant_086 · 2021-05-25 · post-27563015

<!-- artifact:quote:start -->
> or popular and unflattering songs about you spreading within the court itself Click to expand...
<!-- artifact:quote:end -->
Good stuff. The throne room will be more than just cosmetic padding, and I do agree that Grandeur will probably have some kind of a buffer effect against rapid expansion. But please reconsider not allowing dukes to have courts. I can understand counts not having courts (this would just cause massive lag), but dukes should be able to have courts if they are independent or have more than a certain number of vassals.

## Reply 138 — participant_071 · 2021-05-25 · post-27563043

<!-- artifact:quote:start -->
> Dsingis said: Unless the gameplay impacts of not living up to expectations are incredibly severe and crippling, I do not see grandure as relevant to the gameplay other than roleplaying. Click to expand...
<!-- artifact:quote:end -->
I'm curious what the devs envision the experience being like if a player just chooses to not spend any money on grandeur ever. Will it be totally unworkable, like refusing to spend any money on men at arms?

## Reply 139 — participant_006 · 2021-05-25 · post-27563044

<!-- artifact:quote:start -->
> Dsingis said: Unless the gameplay impacts of not living up to expectations are incredibly severe and crippling, I do not see grandure as relevant to the gameplay other than roleplaying. Click to expand...
<!-- artifact:quote:end -->
I read the dev diary as suggesting that lack of grandeur will cause real problems. I hope that's how it ends up. Empire/Kingdom level realms could really use more problems.

## Reply 140 — participant_028 · 2021-05-25 · post-27563080

If those problems from lack of grandeur will mean vassals and courtiers opinion maluses and penalties (which makes the most sense) then they would need also to nerf or completely rebalance Dread or Grandeur might end up ignored unless you're already really strong

## Reply 141 — participant_087 · 2021-05-25 · post-27563082

<!-- artifact:quote:start -->
> johnty5 said: The event windows do a good job of showing character models reacting to each other. I'm hoping the court scene will by dynamic enough that you would see your rival stood off to the side glaring at you, the women at court who's trying to seduce your Chancellor actually doing that in the scene etc. Click to expand...
<!-- artifact:quote:end -->
yeah,exactly,it looks kinda wierd right now

## Reply 142 — participant_088 · 2021-05-25 · post-27563087

Its nice to see you trying things that weren't in CK2.

## Reply 143 — participant_089 · 2021-05-25 · post-27563107

<!-- artifact:quote:start -->
> Cymsdale said: Grandeur sounds like it gives a lot of bonuses just for existing. Will the game be balanced around having Grandeur (the DLC) toggled on or off, or will it be a pay-to-win DLC feature where the player will be more powerful simply by owning the DLC? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Alien-47 said: Low-spec machines are already encouraged to use static portraits, without animations, so in that case court room will also be static - 3D image won't be rendered every frame, but updated only when needed. Considering this scene hides the game map, we're quite optimistic that we'll be able to deliver a good result for all players. Click to expand...
<!-- artifact:quote:end -->
This looks like a great new feature for those who buy the DLC. I am a role-player, not a map painter, and this looks like it will be so much fun, especially for less violent playthroughs. This is a really important point. At first glance, it looks like Grandeur will only be active if you have the DLC. There is a big advantage to that. The game would only have two balance states (Grandeur on and off) in this respect. That will make the devs' lives much easier later on, when there are dozens of possible DLC combinations. Thank you for considering the needs of low spec gamers! I built my current PC to match the CK3 minimum spec; I would be disappointed if a DLC upped the requirement.

## Reply 144 — participant_090 · 2021-05-25 · post-27563128

<!-- artifact:quote:start -->
> rageair said: Greetings! Welcome to the first Dev Diary for the Royal Court expansion! As we mentioned in a previous DD, we’ll go back to Azure patch DD’s for a few weeks after this one. But do not fear, there will be some more Royal Court DD’s before the summer holidays - and when we’re back from holidays we’ll have many, many Royal Court diaries for you! It’s really hard to pick a topic for where to start, but we decided upon a dive into the namesake feature of the expansion - the Royal Court itself, your seat of royal majesty and power! The Royal Court consists of many features, all collected within a 3D scene that we call the Throne Room. Here’s an early Work in Progress screenshot of the throne room - do note that it’s a very early version, but we just can't wait to show you what we have been working on! View attachment 723585 [Image: An early WIP western-style Throne Room, not indicative of final quality] Now, there are many things that go into the Royal Court itself. It interacts with numerous new features that’ll come with the expansion - we won’t go into detail on all of them today, if we did this DD would become much too long! It's worth noting that this isn’t just a graphical feature; while we admit the importance of immersion, we don't want any features to feel tacked-on or superfluous. The Throne Room is there to show what’s happening; what artifacts you’ve collected, which courtiers are having a fight, etc. This allows us to place your character in a scene together with others, showing that you’re actually present in the same world! We’re trying to bridge the gap between your character and the map, all while representing a side of medieval history we’ve never previously explored in detail - the importance for a ruler to show their power, their grandeur, to their subjects and peers. Every Feudal/Clan King and Emperor has a Royal Court. Tribal Rulers do not have one, as this feature primarily models the formality and ceremony surrounding the court, as well as the need for spending Gold, while Tribal rulers use Prestige as their main resource. If a ruler is demoted to a lower rank (through war, election, or just sheer bad luck) their Royal Court and everything therein will either stay dormant until you regain your lost status, or follow the character who now rules in your stead. Grandeur The key concept that enables this is called Grandeur - a measurement of your standing in the eyes of your peers. While it’s measured on a scale from 0-100, it’s not necessarily a simple system. Increasing your grandeur will lead to direct political benefits, such as increased opinions, marriage acceptance, etc. It will also unlock new Council Jobs, such as being able to peacefully demand De Jure land with the ‘Convince De Jure Territory’ job, or gain Knight Effectiveness while also decreasing enemy Scheme Success Chance with the ‘Manage Royal Guards’ job. These effects motivate you to aim for a high level of Grandeur, but naturally comes at a monetary cost. How much are you willing to spend on artifacts, amenities, or on positions within your court? You have to balance your political needs with your temporal ones, such as warfare or development. Sacrificing your grandeur entirely will cause instabilities both internal and external. Grandeur is not really a resource, and is not actively ‘spent’ - unlike something like Prestige. It works on a much slower timescale, and is something you must balance and work towards increasing over a longer period of time. Though there are of course choices in events that make Grandeur increase or decrease, with various trade-offs. Grandeur Effects As mentioned in the previous section, Grandeur has several different effects and modifiers. It is divided into 10 separate levels with their own effects. For example, the very first level of Grandeur unlocks the ability to Hold Court - which is a crucial component in achieving the higher Grandeur levels. The second level unlocks a Council Task called ‘Bestow Royal Favor’, which is a powerful single-target task that increases a vassal’s opinion of you while granting them, and you, prestige. One of the most significant effects of Grandeur is its effect on attraction of Inspired characters - the higher your Grandeur is compared to that of your neighbors, the likelier you are to have these creative travelers visit your court first, giving you an opportunity for patronage (more on Inspirations in a future DD). Some of these levels will give courtiers who stay within it a flavorful trait, which will increase their skills and attributes based on the type of court they’re staying at. A particularly grand court might even see a more powerful trait appear, making such characters excellent for various jobs and Court Positions (more on Court Positions in a later DD). Several Grandeur levels have effects and modifiers based on your Court Type - a type of flavorful perk for your court. Depending on your cultural Ethos you’ll get access to a few different types, such as a Diplomatic or Warlike Court. All royal courts have a type, and among other things it affects the type of trait that courtiers get (see previous paragraph). The bonuses granted from these types are varied and aim to enhance a certain style of play. The AI will tend to go for the Court Type most reflective of their Cultural Ethos and situation - for example, Indian Kings will often tend to want a Scholarly Court since many Indian cultures have a spiritual Ethos. As an example, having a Diplomatic Court Type will grant you bonuses to Vassalization acceptance, tyranny gain, opinion, and potentially even unlock a Personal Scheme slot. A Warlike Court Type might instead see bonuses to MaA counter efficiency, knight efficiency, and the maximum size of MaA regiments. As not all cultures can access all Court Types, this is another reason to pursue Hybridization or Divergence (more on that in a later DD). How Grandeur is Gained Grandeur is divided in two; baseline, and direct gain. The baseline decides the ‘trend’, with you passively (and slowly) either gaining or losing grandeur over time, until the baseline is met. The baseline is affected by many things; what Court Artifacts you have, what Court Positions you have filled, etc (more on Court Artifacts in a later DD). The rate of grandeur change can be modified by many things, such as Cultural Ethoses or Traditions, but is as a rule of thumb slow. It takes time for word of your glory to spread, after all! The most simple way to increase your Grandeur baseline is by investing in Amenities. Now, Amenities are simple and straightforward; but they’re still central to the concept of having a grand court! There are four different types; Lodgings, Food, Clothing and Servants. There are four levels to each, with each progressive level costing more gold to maintain, but giving more Grandeur baseline. They all come with a selection of flavor effects, for example; spending on food will slightly increase the disease resistance of your courtiers, but higher levels might also cause them to gain weight! Spending on clothes will increase their prestige, and will even cause them to wear fancier clothes at higher levels of expenditure (commoners will wear low nobility clothes, and so on). If your court is lacking in artifacts, spending on Amenities is the way to go. Worth noting is that the cost of amenities is relative to your size and income; a small realm won’t have to pay as much as a prosperous one - the intent here is to allow smaller kingdoms and empires to ‘punch above their weight’ diplomatically, making choosing between expansion and consolidation a more relevant matter. Reaching your baseline might take a long time, unless you decide to take action in order to speed it up - to gain grandeur fast, you need to Hold Court! Performing this decision invites your vassals and subjects to bring their issues, requests, and questions before you. The mere act of Holding Court will give you a one-time boost to your Grandeur, but the opportunities within the activity itself might give you opportunities to increase it further (or you could decide to lose grandeur for some temporal gain that is just too good to pass up!). The issues brought forth when Holding Court are many and varied, with many of them reacting to the state of your realm (more on Hold Court in a later DD). Grandeur Expectations Now, Grandeur isn’t only about reaching the level that gives the effect you desire, it’s also about managing expectations! Depending on a number of factors, such as your tier or the size of your realm, you will have a certain expectation put upon your Royal Court. This expectation is a double-edged sword - if your grandeur is below expectations you’ll suffer increasing diplomatic penalties as people lose respect, while if it’s exceeded you might see powerful diplomatic bonuses. These are scaled based on how powerful you are - a rather small Kingdom that undershoots its expectations won’t be hit particularly hard, while a massive empire such as the Holy Roman Empire or Byzantium will be punished much harder if they fail to live up to the expectations put upon them. The effects of not living up to your expectations are many; reduced prestige, renown, and a hefty hit to opinion with both foreign rulers, courtiers and vassals. A large realm might easily find itself facing significant unrest unless its ruler starts spending on grandeur! On the other hand, a small kingdom that vastly exceeds the expectations put upon it might see significant bonuses to its diplomatic power, as well as renown and other bonuses. Court Events Now, the Royal Court isn’t all about Grandeur, of course. Another important role it holds is to show that there’s life in your court! This is done through Court Events; happenings contained within the court, taking place between those who live therein. This new type of event uses the throne room as its backdrop, transforming the entire throne room into an event when they happen. Unlike normal events, this type of event is non-interruptive - you get notified that something is happening, whereby you can go into your Royal Court, inspect the scene, find whoever is involved, and trigger the event yourself. Usually these events are some sort of drama happening between your courtiers, which you can choose to simply ignore if you feel like you have more important matters to attend to. These events come in many different flavors, mostly focusing on how it is to live in the court. Some examples of court events that are being worked on currently include courtiers causing you embarrassment through their drinking or poor manners, or getting into arguments with your architect. Others involve things like rumors spreading about your predecessor on the throne, or popular and unflattering songs about you spreading within the court itself. Court events might also be things like foreign ambassadors trying to uncover your secrets or devout courtiers shaming you and your court for your frivolous living. --- Now, of course there’s more that goes into the Royal Court, but we’ll save going into details regarding Court Artifacts, the UI and graphical looks of the Throne Rooms, Court Positions and so on for future DevDiaries! Of course, this expansion isn’t all about the Royal Court; before the summer break starts you’ll get to read about some of the other features coming with the expansion and patch. That’s all for now! Click to expand...
<!-- artifact:quote:end -->
if we are gonna show off, can we show off our COA? if we can do that, can we design our COA by ourselves?

## Reply 145 — participant_091 · 2021-05-25 · post-27563163

I'm personally iffy on amenities cost scaling with realm income; I think it would make more sense for it to scale with rank or realm size.

## Reply 146 — participant_092 · 2021-05-25 · post-27563198

3D Throne room? At this speed, In five years we will be able to enjoy CK3 in full immersive VR mode.

## Reply 147 — participant_088 · 2021-05-25 · post-27563210

<!-- artifact:quote:start -->
> C.N. said: 3D Throne room? At this speed, In five years we will be able to enjoy CK3 in full immersive VR mode. Click to expand...
<!-- artifact:quote:end -->
Striding across the map like an even larger Gulliver ?

## Reply 148 — participant_093 · 2021-05-25 · post-27563227

Very nice, I'm looking forward to it! I hope there are more positions/expression for the characters/guests though. The two serfs(?) on the left and right seem a bit stiff and default. Would be nice if, once it's out, characters will/ can have different expressions through body language or facial expression. Different position they are standing at and different body expressions.

## Reply 149 — participant_058 · 2021-05-25 · post-27563228

<!-- artifact:quote:start -->
> johnty5 said: Can I just say how brilliant this thread is. People being excited, people asking for clarifications and getting them, people riffing idea/suggestions for the devs about how the mechanics might/could work. I think I've only spotted one kneejerk negative post in the whole thread. This is these forums at their best. Click to expand...
<!-- artifact:quote:end -->
yep we can be wholesome too

## Reply 150 — participant_094 · 2021-05-25 · post-27563238

So since I haven't seen this question answered yet by the devs. Royal Courts are apparently only available to Feudal and Clan Kingdoms/Empires. Surely tribal kings would just as likely hold courts with ceremony and formality. Perhaps a slight bit less so on the formality part. But to exclude them from the mechanic just because of that seems weird. Are there plans to have a tribal version of it at some point?

## Reply 151 — participant_088 · 2021-05-25 · post-27563245

I guess the only negative thing I could think of with this, would be that after a few runs, everything might get too ' Samey'. Do the devs plan to do anything to stop this from happening. Indeed, is there anything that can be done to stop this ?

## Reply 152 — participant_042 · 2021-05-25 · post-27563247

<!-- artifact:quote:start -->
> Unknown Sage said: So since I haven't seen this question answered yet by the devs. Royal Courts are apparently only available to Feudal and Clan Kingdoms/Empires. Is there a specific reason tribals do not have access to it? Because I do not see it. Surely Tribal Kings would be just as likely to hold court? Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> rageair said: Every Feudal/Clan King and Emperor has a Royal Court. Tribal Rulers do not have one, as this feature primarily models the formality and ceremony surrounding the court, as well as the need for spending Gold, while Tribal rulers use Prestige as their main resource. If a ruler is demoted to a lower rank (through war, election, or just sheer bad luck) their Royal Court and everything therein will either stay dormant until you regain your lost status, or follow the character who now rules in your stead. Click to expand...
<!-- artifact:quote:end -->
*(no text body — reaction-only or media-only post)*

## Reply 153 — participant_012 · 2021-05-25 · post-27563253

Missed opportunity- having the throne room seen by zooming all the way out and revealing the map you are looking at is sitting on a table in the throne room.

## Reply 154 — participant_095 · 2021-05-25 · post-27563258

Man... This expansion will take the game to incredible levels. I trust you, paradox!

## Reply 155 — participant_096 · 2021-05-25 · post-27563284

<!-- artifact:quote:start -->
> blackninja9939 said: Being able to see everyone and your artifacts etc is a big part of the immersion into the royal court that we want hence the 3d scene instead of painted backgrounds. We are well aware of the performance implications and will be aiming to make sure it can run fine across our minimum and recommended hardwares, with some reduction of number of things on screen etc if required for the min specs like the options we already have for them. What other divisions would you want here? I don't think that is too true here, the specific nature of it is that exceeding one's expectations is easier when you are small and the expectations are low compared to someone like the HRE or Byzantines. So I think it makes a lot of sense design wise and thematically for this system. Click to expand...
<!-- artifact:quote:end -->
Mostly replying to your question in “2”. Some potential divisions we could have would be things like morality or even a handful of event specific ones. You could have a few reserved for some of the zanier religions/ religious doctrines. You could have an “evil” themed one, mirroring some of the really nasty bloodlines from CK2. Maybe even a handful of unique cultural ones, like one for the Byzantines, one for the Mongol Empire, one for a restored Rome, etc. Some of these could be done merely by being hybrids between two of the stat- based ones (ERE being a hybrid of war and intrigue for example) and a handful of flavour events/ clothing changes.

## Reply 156 — participant_034 · 2021-05-25 · post-27563318

<!-- artifact:quote:start -->
> Ezoo said: Mostly replying to your question in “2”. Some potential divisions we could have would be things like morality or even a handful of event specific ones. You could have a few reserved for some of the zanier religions/ religious doctrines. You could have an “evil” themed one, mirroring some of the really nasty bloodlines from CK2. Click to expand...
<!-- artifact:quote:end -->
I'll have to pass on the zaniness, I'm afraid. I'd rather things stayed relatively grounded.

## Reply 157 — participant_097 · 2021-05-25 · post-27563337

<!-- artifact:quote:start -->
> blackninja9939 said: What other divisions would you want here? Click to expand...
<!-- artifact:quote:end -->
This all sounds amazing. I'm glad you all are being ambitious with these expansions. Are there ways to interact with your liege's royal court as a vassal? I hope you can at least petition them when they hold court, if not also be able to get up to other shenanigans. Personally I'd prefer if you took the 5 skill based courts and instead of each being based on 1 skill, they are based on 2 skills. So the the 5 courts would be the 5 neighbouring skills in the education system (the childhood traits can even give some inspiration for what the themes of these courts could be). This way if you want a war focused court you still know that you want one of the martial themed courts, but also still need to decide if you want to go Martial & Stewardship or Martial & Intrigue. This would also feel more natural as I don't think a court could be summed up as a single skill, but still allows the court to have a cohesive theme (same goes for culture and it's ethos, but it sounds like you are already doing something different for that which is good). Either way, looking forward to this expansion Edit: clarity

## Reply 158 — participant_098 · 2021-05-25 · post-27563339

This looks amazing literally the expansion that I've been hoping for! Plus the changes to culture which I wasn't even expecting. The only negative I can see is that tribal rulers won't have access to the court. Tribal monarchs often had as much ceremonial and courtly responsibilities as other types of monarchs. The presentation of your court and interaction with your vassals was just as important to say Harald Fairhair as it was to Harald Hardrada. Also as a tribal ruler I really need things to spend gold on I have too much most of the time. Is there any chance that will be looked at in the future?

## Reply 159 — participant_099 · 2021-05-25 · post-27563410

<!-- artifact:quote:start -->
> rageair said: for example, Indian Kings will often tend to want a Scholarly Court since many Indian cultures have a spiritual Ethos. Click to expand...
<!-- artifact:quote:end -->
Looks interesting, and I'm really into these developments, I think they're really going to be fun...but I can't help but be worried about this quote here I know where y'all are coming from, but as an Indian-American, it feels like this is going to be really a vast simplification of the interests of the various Indian nations and their interests (given many Indian nations were equally interested in War or trade over just simply religion). Y'all asked me to have faith and give y'all the benefit of the doubt in regards to the Ethos system, which I've been very vocal about regarding my concerns, but this type of thing is definitely not assuaging my concerns. I really don't understand why ethos isn't something dynamic and determined by circumstance and/or the cultural leader...Not only is it something that'll let you avoid overly simplifying history and unintentionally playing into stereotypes, but it seems more fun in terms of the alt history side of things to be not pigeonholed into being spiritual if I'm playing as an Indian King. I know there's not much info out on the ethos system yet, and I may have misinterpreted or be misinformed, but just as a Indian-American, this has me a bit worried.

## Reply 160 — participant_100 · 2021-05-25 · post-27563475

<!-- artifact:quote:start -->
> Cymsdale said: Missed opportunity- having the throne room seen by zooming all the way out and revealing the map you are looking at is sitting on a table in the throne room. Click to expand...
<!-- artifact:quote:end -->
Please no more zoom mapmodes.

## Reply 161 — participant_071 · 2021-05-25 · post-27563493

<!-- artifact:quote:start -->
> Anonymous01 said: Please no more zoom mapmodes. Click to expand...
<!-- artifact:quote:end -->
Agree. Zooming out from the map into the throne room would look neat in a promo video, but it would be extremely annoying to try to zoom out to see more map, but accidentally boot yourself into the throne room if you spin your mouse wheel a few ticks too far.

## Reply 162 — participant_021 · 2021-05-25 · post-27563520

<!-- artifact:quote:start -->
> Tiax said: Agree. Zooming out from the map into the throne room would look neat in a promo video, but it would be extremely annoying to try to zoom out to see more map, but accidentally boot yourself into the throne room if you spin your mouse wheel a few ticks too far. Click to expand...
<!-- artifact:quote:end -->
I agree with this. However: If the transition didn't happen on zoom out, but only when you deliberately access the court, then we could have the nice visuals as without a usability cost.

## Reply 163 — participant_032 · 2021-05-25 · post-27563545

How would I access the throne room? Is there going to be a button like there is for the Dynasty and so on. Plus, if my capital got raided by those despicable swedes... Would it show in the throne room?

## Reply 164 — participant_101 · 2021-05-25 · post-27563549

Will Courts have different graphics depending on cultures? I would assume a French court and an Ayyubid court would look different.

## Reply 165 — participant_102 · 2021-05-25 · post-27563555

It's a tad weird to be expected to pay for my underlings clothes, food is fine, but clothing? Would you be willing to consider a system where you can set an appropriate level of clothing as the ruler with the twist of the courtiers paying for it themselves (landless courtiers not included, or as part of some monthly pittance). As far as I know, that was the strategy at the absolutist courts of Europe (not the timeframe I know), to bleed out poor courtiers forcing them to pay for the latest fashion. Otherwise I like this DD and the way the game develops very much!

## Reply 166 — participant_103 · 2021-05-25 · post-27563561

So do you actually walk around the throne room (e.g. with WASD) or is it more a point-and-click thing where you are presented a dynamically generated image (3D) but you essentially have to click to focus on any one character or element?

## Reply 167 — participant_104 · 2021-05-25 · post-27563598

Looking forward to this dlc. But i have one Question: Will you also adopt the concept of "Reisekönigtum"(german)/"travelling kingdom/itinerant kingship". For in special for the HRE and some other european areas it was common in the whole medieval timespan that the kings and emperors where travelling from place to place or imperial palace to imperial palace to keep the power over their realm. I mean finaly they still resided at (changing) courts, but in my opinion it would add much flavour and immersion for the specific areas to have at least some event(chains) adressing this special form of ruling a realm.

## Reply 168 — participant_105 · 2021-05-25 · post-27563624

More RP potential? I love it already!

## Reply 169 — participant_106 · 2021-05-25 · post-27563628

Is it possible to mod the existence of courts for Counts and Dukes? How easy would it be?

## Reply 170 — participant_107 · 2021-05-25 · post-27563632

<!-- artifact:quote:start -->
> rageair said: Every Feudal/Clan King and Emperor has a Royal Court. Tribal Rulers do not have one, as this feature primarily models the formality and ceremony surrounding the court, as well as the need for spending Gold, while Tribal rulers use Prestige as their main resource. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> rageair said: If a ruler is demoted to a lower rank (through war, election, or just sheer bad luck) their Royal Court and everything therein will either stay dormant until you regain your lost status, or follow the character who now rules in your stead. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> rageair said: How much are you willing to spend on artifacts, amenities, or on positions within your court? Click to expand...
<!-- artifact:quote:end -->
Sounds pretty interesting! I'm looking forward to seeing where it goes from here. From dev replies, it also sounds like there's a distinction between personal and court artifacts, which is also pretty nice. As understandable as this it, I really hope that gets reworked in the future. Tribal rulers not having access to it seems odd. I don't think it would be a problem at all if, to compensate for their different playstyle, their court mechanics are rather different, either. In fact, I think that would be more popular. That sounds like fertile ground for glitches so I hope it's pretty stable by release, haha. Court positions sounds a bit like the return of Honorary Titles. That would be nice but we'll have to wait and see!

## Reply 171 — participant_108 · 2021-05-25 · post-27563640

I only want for it to not be linear levels of grandeur accumulation that is easy to maintain. A bad King or circumstance should dent you.

## Reply 172 — participant_109 · 2021-05-25 · post-27563643

I am just hoping that if we siege a King's/Emperor's Capital, that we get a scene of us in *their* throne room. Would be kinda cool, not gonna lie.

## Reply 173 — participant_034 · 2021-05-25 · post-27563644

<!-- artifact:quote:start -->
> PenitusVox said: Court positions sounds a bit like the return of Honorary Titles. That would be nice but we'll have to wait and see! Click to expand...
<!-- artifact:quote:end -->
Court positions are returning in an expanded capacity as part of the free patch. I'll take this opportunity to remind people to read the FAQ for this DLC, which has a surprising amount of information.

## Reply 174 — participant_110 · 2021-05-25 · post-27563666

Overall, it's pretty neat. Particularly the part about different levels of grandeur and various types of court (and how that ties to culture). I still heavily disagree with denying the whole system from dukes (though like I said in the previous thread, I think a nice compromise here would be to allow it only to dukes that have multiple duchy titles, i.e. upstart kings) because vassal play is an important part of the game, as well as from tribals (because, like I also said in the previous thread, it's rather silly to think that a tribal emperors would not concern themselves with things like hoarding treasures, showing off their power and splendor or addressing the issues of people in their realm). The even worse part about the "no tribals" thing though is how you limit court styles to only four options. That correspond to the general four areas that start as feudal in 867. OK, you don't want to give courts to tribals. I may disagree, but this is apparently the direction here. But the areas that start as tribal are still going to transform into feudalism (or clan government) during the time span of the game. It's literally one of their primary short term goals. Why shouldn't they have their own court styles once they transition? What court style are Mongols going to use, for example? Middle Eastern, when they are half the steppe away from it? Or Indian, even though they are separated from the Indian Peninsula by the Tibetan Plateau? If anything, if the game is going with the weird "cultures that start as tribal are going to use an architectural style of a more 'civilized' culture when they turn feudal/clan because they are too stupid to use their own architecture, or alone develop it further to fit some arbitrary metric of being courtly enough" Mongols should look at Chinese architecture as an inspiration, because that's the culture Mongols would be logically most exposed to. Yet Chinese style isn't an option either. On another, while the example of a court used here looks neat overall, something about the ceiling looks off. Though maybe it's the static lightning that's playing tricks on me. And while I'm on the topic, I know we will fill the empty spaces with artifacts, but will grandeur also affect how that space looks like on a more baseline level? Take the throne, for example. Will it get upgraded at higher levels to look even more prestigious? And would the type of court also affect things here? Continuing the example of the throne, in CK2's Great Works you could construct a skull throne in the Royal Palace. Would it be possible if you went with intrigue-related court for bonuses to dread and the like?

## Reply 175 — participant_111 · 2021-05-25 · post-27563688

If you're a vassal, can you be invited into your Liege's Royal Court?

## Reply 176 — participant_112 · 2021-05-25 · post-27563696

In case it wasnt mentioned already, please reconsider it being unavailable to dukes. By default, all vassals in the HRE and ERE are dukes, so the only court would be the emperors. I haven't played in the ERE but take for instance, the duke of Bohemia. A powerful elector, stable realm, one of the biggest HRE vassals.. and they don't get a court. Meanwhile, the king of Navarre, all of 5 counties on the Iberian coast, gets to hold Court with all his vassals (those very important barons and mayors etc). Just seems a bit... incongruent, you know?

## Reply 177 — participant_113 · 2021-05-25 · post-27563704

I am interested to see how artefacts are handled in CK3. In CK2 in the multiplayer I played in we always had the unspoken goal to have the most number of human parts and to see how many Saint/Jesus hybrids we could theoretically build with what we had on hand Frankenstein style.

## Reply 178 — participant_096 · 2021-05-25 · post-27563813

<!-- artifact:quote:start -->
> Gwydden said: I'll have to pass on the zaniness, I'm afraid. I'd rather things stayed relatively grounded. Click to expand...
<!-- artifact:quote:end -->
Some of those things are already present. For example, having some unique events that mention the fact that Byzantium has returned to its Hellenic pantheon would be interesting, if that were to occur.

## Reply 179 — participant_114 · 2021-05-25 · post-27563822

I am so hyped, I can't wait for this expansion. When you play the game of thrones, you either win or die.

## Reply 180 — participant_110 · 2021-05-25 · post-27563824

Wait, actually I have to reconsider my initial opinion on linking court types to cultural Ethea. Judging by the remark that many Indian cultures have a spiritual Ethos, it sounds like each base culture has an Ethos from the get go. And as per PDX-Nicou's recent post in the previous thread, Divergence is the only answer to wanting to swap an Ethos out. That's further corroborated by this dev diary, as it mentions how Divergence and Hybridization (meaning it's actually two ways) are the only answers to wanting different court types (as that in turn requires an Ethos change). And that's kinda limiting. And while some choice is good in games, this is limiting in a bad way. Let's say you want to play as a French dynasty. Perhaps you're French yourself or at least some of your ancestors were. Perhaps you're a fan of French history. Or perhaps the idea of eating frogs simply speaks to you on a spiritual level. Whatever your reason for playing French may be, you're limited to the - I'm going to guess here - two court types unlocked by the Ethos it has from the get go. So, what happens if the court types unlocked by that Ethos don't suit your playstyle? The only answers provided by the devs are either Hybridization or Divergence. I.e. creating a culture that is NOT French. Completely defeating the point of wanting to play as specifically French. And here you're not limited in your choices because you did something, like how picking certain buildings means you can't have others because building slots are limited. You're simply limited from the get go. It'd be like limiting characters of French culture to a specific religion. According to the GameWatcher article, Traditions can be picked by the Cultural Head if you have free spots by using Prestige. Which indicates that unlike Ethea Traditions are not there from the get go. Or at least not all spots are filled. As such, I'd argue that Traditions would make for a better mechanic to tie court types to. You'd still have to make a choice but here you'd be in control.

## Reply 181 — participant_004 · 2021-05-25 · post-27563835

When you hold court i would love to be able to invite Holy warriors for some special occasion like discussing crusade

## Reply 182 — participant_051 · 2021-05-25 · post-27563836

<!-- artifact:quote:start -->
> SauronGorthaur said: Overall, it's pretty neat. Particularly the part about different levels of grandeur and various types of court (and how that ties to culture). I still heavily disagree with denying the whole system from dukes (though like I said in the previous thread, I think a nice compromise here would be to allow it only to dukes that have multiple duchy titles, i.e. upstart kings) because vassal play is an important part of the game, as well as from tribals (because, like I also said in the previous thread, it's rather silly to think that a tribal emperors would not concern themselves with things like hoarding treasures, showing off their power and splendor or addressing the issues of people in their realm). The even worse part about the "no tribals" thing though is how you limit court styles to only four options. That correspond to the general four areas that start as feudal in 867. OK, you don't want to give courts to tribals. I may disagree, but this is apparently the direction here. But the areas that start as tribal are still going to transform into feudalism (or clan government) during the time span of the game. It's literally one of their primary short term goals. Why shouldn't they have their own court styles once they transition? What court style are Mongols going to use, for example? Middle Eastern, when they are half the steppe away from it? Or Indian, even though they are separated from the Indian Peninsula by the Tibetan Plateau? If anything, if the game is going with the weird "cultures that start as tribal are going to use an architectural style of a more 'civilized' culture when they turn feudal/clan because they are too stupid to use their own architecture, or alone develop it further to fit some arbitrary metric of being courtly enough" Mongols should look at Chinese architecture as an inspiration, because that's the culture Mongols would be logically most exposed to. Yet Chinese style isn't an option either. On another, while the example of a court used here looks neat overall, something about the ceiling looks off. Though maybe it's the static lightning that's playing tricks on me. And while I'm on the topic, I know we will fill the empty spaces with artifacts, but will grandeur also affect how that space looks like on a more baseline level? Take the throne, for example. Will it get upgraded at higher levels to look even more prestigious? And would the type of court also affect things here? Continuing the example of the throne, in CK2's Great Works you could construct a skull throne in the Royal Palace. Would it be possible if you went with intrigue-related court for bonuses to dread and the like? Click to expand...
<!-- artifact:quote:end -->
I think that specific cultures would probably get their own version of a royal court with their accompanying expansion\flavour pack. Whenever a "Horse Lords" or "Legacy of Rome"-like DLC for CK3 comes out, it's not far-reaching to say it may come out with its own version of culture-appropriate royal\imperial court. Better this, than having to make placeholder mechanics and artwork for current tribal or Mongol rulers, then having to make them from scratch once more when the "Horse Lords 2.0" DLC comes out.

## Reply 183 — participant_115 · 2021-05-25 · post-27563875

Picking a small guy and working your way up to King/Emperor is more fun than starting as one. Sad that counts and dukes aren’t getting a court mechanic :/ Not such a grand court but at least something small...

## Reply 184 — participant_110 · 2021-05-25 · post-27563878

<!-- artifact:quote:start -->
> LukeCreed13 said: I think that specific cultures would probably get their own version of a royal court with their accompanying expansion\flavour pack. Whenever a "Horse Lords" or "Legacy of Rome"-like DLC for CK3 comes out, it's not far-reaching to say it may come out with its own version of culture-appropriate royal\imperial court. Better this, than having to make placeholder mechanics and artwork for current tribal or Mongol rulers, then having to make them from scratch once more when the "Horse Lords 2.0" DLC comes out. Click to expand...
<!-- artifact:quote:end -->
Why would their court artwork need to be redone from scratch even if they get their own expansions later on? Any mechanics introduced by those expansions are unlikely to affect the Court, as Paradox usually shies away from modifying DLC features in further DLCs. Also, I'm pretty sure one of the four styles has been confirmed to be Mediterranean, meaning that Byzantine Empire will get its own court style and it won't be a "placeholder" just because ERE is likely to be revamped down the line.

## Reply 185 — participant_116 · 2021-05-25 · post-27563929

I'd love a court type that flips the dynamic of grandeur on its head for christians and buddhists. For pious courts of these faiths you'll be sacrificing grandeur at your own risk and at the discontent of your rich vassals but with big piety and religious gains.

## Reply 186 — participant_117 · 2021-05-25 · post-27563933

Can't wait to play it

## Reply 187 — participant_060 · 2021-05-25 · post-27563935

<!-- artifact:quote:start -->
> SauronGorthaur said: If anything, if the game is going with the weird "cultures that start as tribal are going to use an architectural style of a more 'civilized' culture when they turn feudal/clan because they are too stupid to use their own architecture, or alone develop it further to fit some arbitrary metric of being courtly enough" Mongols should look at Chinese architecture as an inspiration, because that's the culture Mongols would be logically most exposed to. Yet Chinese style isn't an option either. Click to expand...
<!-- artifact:quote:end -->
I don't know about with regards to Mongols, but afaik didn't the Norse settlers adopt the local castle building traditions when they stayed in northern France and Sicily?

## Reply 188 — participant_118 · 2021-05-25 · post-27563945

Besides baseline grandeur will there be a max grandeur? E.g. will ascetic faiths shun us if our court spending is too lavish?

## Reply 189 — participant_051 · 2021-05-25 · post-27563956

<!-- artifact:quote:start -->
> SauronGorthaur said: Why would their court artwork need to be redone from scratch even if they get their own expansions later on? Any mechanics introduced by those expansions are unlikely to affect the Court, as Paradox usually shies away from modifying DLC features in further DLCs. Also, I'm pretty sure one of the four styles has been confirmed to be Mediterranean, meaning that Byzantine Empire will get its own court style and it won't be a "placeholder" just because ERE is likely to be revamped down the line. Click to expand...
<!-- artifact:quote:end -->
The way the royal court seems to be set up, it seems to be a new major part of gameplay. I doubt it's going to be released for the Royal Court DLC and then never touched again forever after in future patches or DLCs. Graphic assets would probably be touched upon whenever they'll make a new flavour pack\major DLC, I can imagine culture-specific thrones, artifacts, clothes, etc. That's why I'm assuming they'll probably do this if\whenever the ERE gets reworked, so that the Mediterranean royal court can be replaced by a proper Byzantine\Roman royal (imperial?) court. And the various court interactions would need to change accordingly too, to reflect the fact that you're the Basileus\Roman Emperor.

## Reply 190 — participant_110 · 2021-05-25 · post-27563970

<!-- artifact:quote:start -->
> GeorgieBest said: I don't know about with regards to Mongols, but afaik didn't the Norse settlers adopt the local castle building traditions when they stayed in northern France and Sicily? Click to expand...
<!-- artifact:quote:end -->
When they stayed in Northern France and Sicily? Sure. They were settlers and a minority. And they quickly ceased to be actual Norse, instead turning into Normans. In Scandinavia, not so much. And Scandinavian Norsemen still feudalized IRL, as they are prone to do in CK3 as well (especially if played by the player).

## Reply 191 — participant_097 · 2021-05-25 · post-27564002

<!-- artifact:quote:start -->
> SauronGorthaur said: Wait, actually I have to reconsider my initial opinion on linking court types to cultural Ethea. Judging by the remark that many Indian cultures have a spiritual Ethos, it sounds like each base culture has an Ethos from the get go. And as per PDX-Nicou's recent post in the previous thread, Divergence is the only answer to wanting to swap an Ethos out. That's further corroborated by this dev diary, as it mentions how Divergence and Hybridization are the only answers to wanting different court types (as that in turn requires an Ethos change). And that's kinda limiting. And while some choice is good in games, this is limiting in the bad way. Let's say you want to play as a French dynasty. Perhaps you're French yourself or at least some of your ancestors were. Perhaps you're a fan of French history. Or perhaps the idea of eating frogs simply speaks to you on a spiritual level. Whatever your reason for playing French may be, you're limited to the - I'm going to guess here - two court types unlocked by the Ethos it has from the get go. So, what happens if the court types unlocked by that Ethos don't suit your playstyle? The only answers provided by the devs are either Hybridization or Divergence. I.e. creating a culture that is NOT French. Completely defeating the point of wanting to play as specifically French. And here you're not limited in your choices because you did something, like how picking certain buildings means you can't have others because building slots are limited. You're simply limited from the get go. It'd be like limiting characters of French culture to a specific religion. According to the GameWatcher article, Traditions can be picked by the Cultural Head if you have free spots by using Prestige. Which indicates that unlike Ethea Traditions are not there from the get go. Or at least not all spots are filled. As such, I'd argue that Traditions would make for a better mechanic to tie court types to. You'd still have to make a choice but here you'd be in control. Click to expand...
<!-- artifact:quote:end -->
These are some good points. One, I hope the culture head will have some ability to change the culture's ethos without hybridization or divergence. Two, as not every king isn't going to be able to be culture head (and changing your entire culture every time you want to play as a different court type seems weird), I'm not a fan of the move it to traditions option. I think the better solution would for the ethos to steer you towards certain court types, rather than lock you out of others. So an ethos could gives bonuses to two or three different court types (the bonus it gives is also another way to add some flavour and variety). Meaning you can get a benefit for picking a court type the matches your cultural ethos, but can still decide to go against the grain if you so desire. Could even add in some penalties that you have to overcome if your court type is of the wrong type, such as a lower base grandeur.

## Reply 192 — participant_119 · 2021-05-25 · post-27564041

I always imagined CK having a point and click Castle "rooms" instead of the standard map with tabs. Might have to start a new game before this releases.

## Reply 193 — participant_120 · 2021-05-25 · post-27564269

Looks really good. Can't wait to be messing around with my council personality types.

## Reply 194 — participant_121 · 2021-05-25 · post-27564324

Given the fact the question of vassal interactions with the liege's court has been continously dodged, I think it's safe to assume that there won't be any of these. I hope there will be new events at least - to make up for it. For the game which was marketed, among all things, as a step to try making vassal gameplay more engaging, completely ignoring vassal players in the DLC looks really sad and strange. At least bring back the events which were related to your character when he was a part of liege's council, please.

## Reply 195 — participant_122 · 2021-05-25 · post-27564361

I hope that the cost of different amenities is different depending on where is the capital located. For example, the most expensive food (ie: rare spices) should be cheaper in India than in Iceland. Servants should be cheaper in the lands which are more densely populated. Lodgings shoul be cheaper in plain lands with little obstacles (swamps, forests, jungle...). This would make for distinct gameplay depending on the country, and may encourage expansive empires to move their capital to newly, and better conquered lands. I think it would be very cool.

## Reply 196 — participant_123 · 2021-05-26 · post-27564433

<!-- artifact:quote:start -->
> lozikk said: Would be a good idea if culture-merging wasn't a DLC mechanic. Expanding on this thought is ok, but not removing something from religions from base game Click to expand...
<!-- artifact:quote:end -->
It'd be nice to move some of the arguably cultural elements of the current religious system into cultures though. Say being able to be part of a religion that has it be criminal to be homosexual, but you treat it as one step lighter (so that it's now "shunned" rather than criminal), reflecting the de facto behaviour in some more... decadent areas of Europe. Potentially it would allow for Welsh Catholics to have a different attitude to inheritance (effectively "no bastards") compared to their Anglo-Norman counterparts (effectively unable to legitimise bastards). It'd mean that cultures that *really* didn't get on with kinslayers could stay in the same faith as those who tolerate them somewhat more - especially when it comes to consideration of who/what is considered kin. Potentially it might allow for someone under Catholicism to move to *equal* succession without having to split into a heresy.

## Reply 197 — participant_124 · 2021-05-26 · post-27564571

I dont know if this has been discussed but as a count or duke would you get invited to the court of the king and maybe get some bonuses or grandeur? Or if you are a King would you get an invite to the court of the Emperor?

## Reply 198 — participant_125 · 2021-05-26 · post-27564603

I can only echo the mistake of neglecting the existence and prominence of ducal courts, especially in France, Spain, Italy and the HRE. I can also see why not all dukes should hold court, but there's a specific group that definitely did and should. Namely independent dukes and prominent vassal dukes in Empires and Kingdoms where centralisation is low.

## Reply 199 — participant_126 · 2021-05-26 · post-27564634

<!-- artifact:quote:start -->
> rageair said: This new type of event uses the throne room as its backdrop, transforming the entire throne room into an event when they happen. Unlike normal events, this type of event is non-interruptive - you get notified that something is happening, whereby you can go into your Royal Court, inspect the scene, find whoever is involved, and trigger the event yourself. Usually these events are some sort of drama happening between your courtiers, which you can choose to simply ignore if you feel like you have more important matters to attend to. Click to expand...
<!-- artifact:quote:end -->
I hope they bake in the older "drama" events etc that happened between courtiers into this as well. Something I always appreciate is when older events are revisited for newer content to incorporate the feature even better.

## Reply 200 — participant_126 · 2021-05-26 · post-27564658

<!-- artifact:quote:start -->
> Alien-47 said: The only way to get an existing court is to inherit it. Click to expand...
<!-- artifact:quote:end -->
So in a sense it is tied to the main title and the character then? One bad election in Sweden and your court will slip into another family, I guess?

## Reply 201 — participant_127 · 2021-05-26 · post-27564699

Will different cultures have their appropriate court traditions?

## Reply 202 — participant_046 · 2021-05-26 · post-27564700

<!-- artifact:quote:start -->
> korvmaskin said: So in a sense it is tied to the main title and the character then? One bad election in Sweden and your court will slip into another family, I guess? Click to expand...
<!-- artifact:quote:end -->
No, it's not. Court is tied to character's realm. If character loses election and inherits only a duchy/counties, they still inherit court, but it becomes dormant. When that character gets a title of the appropriate tier, court gets reactivated.

## Reply 203 — participant_128 · 2021-05-26 · post-27564759

Ok so, what are the negatives? Because I only see positives with this Grandeur and Royal Court thing. EDIT--ah wait, there's a Grandeur Expectation. So I reckon amenities will be the biggest money sink in the game, so we don't get filthy rich by the midgame anymore?

## Reply 204 — participant_129 · 2021-05-26 · post-27564805

Can traits like content and humble cancel out the penalties for low grandeur?

## Reply 205 — participant_130 · 2021-05-26 · post-27564890

The Byzantines should have the mechanical lion and birds as artefacts (along with works of aristotle etc.) Maybe artifacts could be transferred as part of surrendering in a war? Also, will court events be different depending on culture? the abbasids and byzantines had completely different court customs to the western feudal kingdoms. I hope we see things like hippodrome events, deciding how to treat foreign embassies and coronations. Also I'd love to see scheming events between the emperor and patriarch (maybe the patriarch refuses to crown the emperor or openly insults him) like Michael and Isaac Comnenus

## Reply 206 — participant_126 · 2021-05-26 · post-27565066

<!-- artifact:quote:start -->
> Alien-47 said: No, it's not. Court is tied to character's realm. If character loses election and inherits only a duchy/counties, they still inherit court, but it becomes dormant. When that character gets a title of the appropriate tier, court gets reactivated. Click to expand...
<!-- artifact:quote:end -->
Thanks for the answer. I think I understand how the system works now. If you would indulge me, could you please elaborate on what happens if say, the king of Sweden has a court and his heir is the king of Denmark which also has a court. Would they combine by taking the mean of the two grandeur values? How about the artifacts? I guess they would just combine into one inventory. Would this be a way to grow and consolidate courts?

## Reply 207 — participant_067 · 2021-05-26 · post-27565107

<!-- artifact:quote:start -->
> Call Me Vandal said: A bit disappointed that all of this flies over the heads of counts and dukes. I get that grandeur isn't exactly associated with lesser nobility, but playing as a small ruler is pretty slow as things are currently. I was hoping to myself there'd be some RP opportunities for minor nobles in order to make up for their low amount of engagement compared to kings and emperors, but now it looks like kings and emperors are only going to become even more fun to play relative to minors. Not only are you missing out on the high-level grand strategic gameplay as a minor, but now you're missing out on all this RP. But, reservations aside, the court looks like a fantastic addition to the game. Click to expand...
<!-- artifact:quote:end -->
Maybe lower ranked nobility can be part of their ruler's court, and take part in the RP that way?

## Reply 208 — participant_131 · 2021-05-26 · post-27565118

<!-- artifact:quote:start -->
> rageair said: Grandeur Expectations These are scaled based on how powerful you are - a rather small Kingdom that undershoots its expectations won’t be hit particularly hard, while a massive empire such as the Holy Roman Empire or Byzantium will be punished much harder if they fail to live up to the expectations put upon them. The effects of not living up to your expectations are many; reduced prestige, renown, and a hefty hit to opinion with both foreign rulers, courtiers and vassals. A large realm might easily find itself facing significant unrest unless its ruler starts spending on grandeur! On the other hand, a small kingdom that vastly exceeds the expectations put upon it might see significant bonuses to its diplomatic power, as well as renown and other bonuses. Click to expand...
<!-- artifact:quote:end -->
Let's hope the DLC includes the typical byzantine throneroom then, with an automated elevating throne with singing bird and lion statues (no kidding, totally real). Finding History » How hard was it to see a Byzantine emperor in person? larsbrownworth.com

## Reply 209 — participant_132 · 2021-05-26 · post-27565136

<!-- artifact:quote:start -->
> Jorlem said: Maybe lower ranked nobility can be part of their ruler's court, and take part in the RP that way? Click to expand...
<!-- artifact:quote:end -->
I think this is everyone's hope. If they include that interaction as a vassal and do it well, I think most people would be happy with it. You'll still miss out if you're an independent count or duke or aren't feudal, but it would cover most players. Unfortunately, there is nothing that suggests they are planning to allow that liege's court interaction, so it may not happen.

## Reply 210 — participant_133 · 2021-05-26 · post-27565146

The throne room must have good feng shui. Are you consider this devs?

## Reply 211 — participant_134 · 2021-05-26 · post-27565204

Had anybody asked how this new court fashion system will work with Natural Primitivism and some other tenets that encourage modesty?

## Reply 212 — participant_028 · 2021-05-26 · post-27565457

<!-- artifact:quote:start -->
> DreadLindwyrm said: It'd be nice to move some of the arguably cultural elements of the current religious system into cultures though Click to expand...
<!-- artifact:quote:end -->
Sure, but since Culture mechanics will be included in the DLC, that would be taking away from the player without it. It could be both - for example if culture has some doctrine as "Accepted" while religion has it as "Criminal", the mixed result might give "Shunned"

## Reply 213 — participant_135 · 2021-05-26 · post-27565608

Sounds very promising. Especially if it will be interactive both ways - i.e. player being a vassal invited to court will be able to bring up their real issues based on what is happening in game. Some questions: 1. Will Grandeur baseline / expectations be affected by your dynasty properties (i.e. Duke X's lineage goes all the way back to Charlemagne, certainly his court should reflect this! Or - "even though they are quite poor now, N's used to be Kings of .... , so they do deserve some credit".) 2. What will happen with court / Grandeur in case of partition inheritance - it is quite often in game that a father King manages to assemble a big personal demesne with high incomes and stability and upon their death everything gets partitioned into way smaller holdings. 3. Will other events happen during "Hold Court" periods - like royal hunts, tournaments in lists and in melee, opportunities for marriage and illicit affairs etc., etc.? 4. What will happen with religious holdings? Will Archbishops hold court if they have secular vassals?

## Reply 214 — participant_136 · 2021-05-26 · post-27565663

With the court being where the ruler is, will the scene change if the ruler is leading an army or sieging? What about when on a pilgrimage? Also viking rulers tended to travel around from one important "vassal" to the next, all around the realm. Will that be represented in the court room mechanic?

## Reply 215 — participant_028 · 2021-05-26 · post-27565735

<!-- artifact:quote:start -->
> brynjarg said: Also viking rulers tended to travel around from one important "vassal" to the next, all around the realm. Will that be represented in the court room mechanic? Click to expand...
<!-- artifact:quote:end -->
Not only vikings but feudal rulers in general. Apparently it won't be represented in any way

## Reply 216 — participant_137 · 2021-05-26 · post-27565873

I'm glad we still got the culture rework to look forward to. Because I'm not sure how I feel about what's been presented so far. I like the general idea of the court , I really do, but there are quite a few things already which don't feel right to me. Not having any court options available to Dukes feels wrong to me given the timeframe of the game. Limiting it to Kings alone feels like it would suit more in the post-Medieval/Absolutist Kingdom era, while one of the things that made the Feudal era so different was that it was very much possible for a powerful Duke to equal or even eclipse their King liege. Sure, some options should be limited to Kings and Emperors, but disallowing a Duke from having a court at all, I disagree with. I can also understand not giving tribals the full options of a feudal court, but nothing at all? At the very least having some kind of longhouse with a throne and sharing stories and showcasing artifacts from their raids is absolutely suitable to tribals. And scaling amenities with income is also a very iffy choice IMO. Scaling it with realm size, definitely, and I can think of a few other ways to scale it as well such as how multicultural your realm is - those can be explained in universe, but I don't like gold sinks that are based on x% of income.

## Reply 217 — participant_138 · 2021-05-26 · post-27565899

Awesome A lot of these things I suggested on this very forum last week so I'm gonna go ahead and take credit I wanted a 'call council' option, more titles and an option to buy and sell de jure territory. CK needed a council feature so I'm happy it's finally coming. Not sure how grandeur works so I'll have to go back and read it again but if I've got it right it's used exclusively to manage the size and features of your court. I HATE the idea of things costing more for larger realms to give smaller realms a handicap. I wish Paradox would stop doing this because it's basically punishing the player for having a rich and prosperous realm. On my current playthrough I spent 50 years amassing 6000 gold only to realize that a pilgrimage to Jerusalem now costs over 1000 gold :/

## Reply 218 — participant_139 · 2021-05-26 · post-27566186

<!-- artifact:quote:start -->
> JackTheHat said: Awesome A lot of these things I suggested on this very forum last week so I'm gonna go ahead and take credit I wanted a 'call council' option, more titles and an option to buy and sell de jure territory. CK needed a council feature so I'm happy it's finally coming. Not sure how grandeur works so I'll have to go back and read it again but if I've got it right it's used exclusively to manage the size and features of your court. I HATE the idea of things costing more for larger realms to give smaller realms a handicap. I wish Paradox would stop doing this because it's basically punishing the player for having a rich and prosperous realm. On my current playthrough I spent 50 years amassing 6000 gold only to realize that a pilgrimage to Jerusalem now costs over 1000 gold :/ Click to expand...
<!-- artifact:quote:end -->
Thanks for all the work, expansion is going to be awesome.

## Reply 219 — participant_140 · 2021-05-26 · post-27566244

Okay now because its ck i am looking forward to a court which is famous for seduction. Even its more intrigue. if its not in the vanilla DLC i think sooner then later we will see a proper mod so we can create famous courts which have a reputation for seduction......

## Reply 220 — participant_132 · 2021-05-26 · post-27566540

I was thinking some more about the lack of court for dukes and counts... right now, you have petty kings who are duke tier, but are treated as kings. How will they work? Do they get courts? I think they should if they are being considered as kings regardless if they are duke tier. But then you get the question of why some duke tier rulers have courts and some don't. It's not a very good line to have.

## Reply 221 — participant_141 · 2021-05-26 · post-27566575

<!-- artifact:quote:start -->
> Elfin said: Had anybody asked how this new court fashion system will work with Natural Primitivism and some other tenets that encourage modesty? Click to expand...
<!-- artifact:quote:end -->
The most expensive and smooth leaves!

## Reply 222 — participant_034 · 2021-05-26 · post-27566633

<!-- artifact:quote:start -->
> BoomKidneyShot said: The most expensive and smooth leaves! Click to expand...
<!-- artifact:quote:end -->
Birch leaves are so last season.

## Reply 223 — participant_142 · 2021-05-26 · post-27566677

So exciting! And very cool that the theme of the expansion seems to be a surprise to most everyone. Not sure if this is already clear, and I just missed it, but—can you change the type of court (e.g. martial or diplomatic) once its set, maybe once in a ruler's lifetime, or once every certain amount of years? Or is the court type set forever once its chosen? It would be cool to be able to change court types (e.g. from diplomatic to martial if you were foreseeing a long episodic war for another empire or something), but I don't think it should be something that could happen quickly, or over and over again.

## Reply 224 — participant_132 · 2021-05-26 · post-27566694

<!-- artifact:quote:start -->
> thebadmiral said: So exciting! And very cool that the theme of the expansion seems to be a surprise to most everyone. Not sure if this is already clear, and I just missed it, but—can you change the type of court (e.g. martial or diplomatic) once its set, maybe once in a ruler's lifetime, or once every certain amount of years? Or is the court type set forever once its chosen? It would be cool to be able to change court types (e.g. from diplomatic to martial if you were foreseeing a long episodic war for another empire or something), but I don't think it should be something that could happen quickly, or over and over again. Click to expand...
<!-- artifact:quote:end -->
No. The type is based on your culture. You can change your culture through hybridization or divergence (a different ethos can be a different court type) and change your court that way, but otherwise it is set in stone based on your culture.

## Reply 225 — participant_004 · 2021-05-26 · post-27566700

<!-- artifact:quote:start -->
> Riamus said: No. The type is based on your culture. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> rageair said: Each Ethos unlocks more than one Court Type Click to expand...
<!-- artifact:quote:end -->
Correction: Dunno if you can change it after you've picked one though.

## Reply 226 — participant_142 · 2021-05-26 · post-27566709

<!-- artifact:quote:start -->
> Riamus said: No. The type is based on your culture. You can change your culture through hybridization or divergence (a different ethos can be a different court type) and change your court that way, but otherwise it is set in stone based on your culture. Click to expand...
<!-- artifact:quote:end -->
Ah right, of course. Thanks so much for the reply!

## Reply 227 — participant_143 · 2021-05-26 · post-27566830

Thank you to all the developers who have posted in this thread - @rageair, @blackninja9939, @Servancour, @Alien-47, and @PDXOxycoon! It really means a lot to us players when developers take the time to talk to us, and to see so many do that in this thread is very heartening! I have a question: are there any plans to introduce message settings into the game with this update? If not, are there any such plans for the future? Thank you again for your time and attention!

## Reply 228 — participant_144 · 2021-05-26 · post-27567103

<!-- artifact:quote:start -->
> Spirit_mert said: I hope you guys think again with Tribals not having a courtroom, I get the point you make but maybe a more basic, intimate clan hall room would be appropriate with some of the mechanics disabled? Ignoring tribal realms completely sounds bad in my opinion. Give them a cozy, wooden hall, with fur and animal hides laying around. Finally, add a few basic mechanics that are weaker than feudal ones. Would make tribals not left out and still weaker than feudal courts. Just a thought. Click to expand...
<!-- artifact:quote:end -->
I agree. Ducal court's should also definitely be a thing. Court size, effect, cost, bonuses and appearance should just scale on title rank.

## Reply 229 — participant_123 · 2021-05-26 · post-27567104

<!-- artifact:quote:start -->
> lozikk said: Sure, but since Culture mechanics will be included in the DLC, that would be taking away from the player without it. It could be both - for example if culture has some doctrine as "Accepted" while religion has it as "Criminal", the mixed result might give "Shunned" Click to expand...
<!-- artifact:quote:end -->
That would be an acceptable way of doing it for me - it goes along with the idea I mentioned of having a "criminal" element being treated one degree lighter by that specific culture thanks to a cultural trait.

## Reply 230 — participant_145 · 2021-05-26 · post-27567170

<!-- artifact:quote:start -->
> Alien-47 said: It's tied to the court - it's a thing in itself. It belongs to a single person at any time, and can be inherited Click to expand...
<!-- artifact:quote:end -->
What happens if I usurp a kingdom as a duke, downgrading the previous king to a duke?

## Reply 231 — participant_006 · 2021-05-26 · post-27567243

<!-- artifact:quote:start -->
> Admiral Boysen said: What happens if I usurp a kingdom as a duke, downgrading the previous king to a duke? Click to expand...
<!-- artifact:quote:end -->
The old King’s court will stop working/become inaccessible - but remain available to him if/when he becomes a King again.

## Reply 232 — participant_146 · 2021-05-27 · post-27568102

An interesting DLC idea. I like the idea of the Royal Court. I hope it leads to more courtly intrigue. Question: What about rulers whose virtues do not run towards the rich and opulent, will they have different, "austere" courts? Question 2: Will the game be further optimized in the new patch? I wish the game ran faster so that my little laptop's CPU temperatures no longer hit 90ºC. I don't have a dedicated video card, guys. Game needs to go more vrum vrum (althrough its pretty fast already) so I can no longer fear that it will melt my computer.

## Reply 233 — participant_085 · 2021-05-27 · post-27568190

<!-- artifact:quote:start -->
> lozikk said: If those problems from lack of grandeur will mean vassals and courtiers opinion maluses and penalties (which makes the most sense) then they would need also to nerf or completely rebalance Dread or Grandeur might end up ignored unless you're already really strong Click to expand...
<!-- artifact:quote:end -->
This. Dread, in my opinion, should just result in an increase in the strength required for a faction to press its demands against the ruler, while only having its current terrify effect against craven characters. Also, I don't know if this might already exist, but conceding to demands, losing or white-peacing a war, etc., should have a massive negative effect on dread

## Reply 234 — participant_147 · 2021-05-27 · post-27568300

<!-- artifact:quote:start -->
> Elfin said: Had anybody asked how this new court fashion system will work with Natural Primitivism and some other tenets that encourage modesty? Click to expand...
<!-- artifact:quote:end -->
Jokes aside this is a good question. Modest rulers and religions like Insular Christianity should have higher opinions of modest courts. I'm not sure if the grandeur will be a baseline thing in opinion or vary person to person, but it definitely should

## Reply 235 — participant_148 · 2021-05-27 · post-27568546

Can pages and squires be introduced so that you can groom your own knights from "inside the system" as opposed to them arriving from X place in your realm/aborad? This could be a viable route for bastard sons that does not qualify to be a legitimate heir. They could work their way up and gain enough prestige so that they would become legitimate pretenders in the future. Good potential for an RPG playstyle.

## Reply 236 — participant_132 · 2021-05-27 · post-27568599

<!-- artifact:quote:start -->
> Hospodar said: Riamus said: No. The type is based on your culture. Click to expand... Correction: rageair said: Each Ethos unlocks more than one Court Type Click to expand... Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> Riamus said: No. The type is based on your culture. Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> rageair said: Each Ethos unlocks more than one Court Type Click to expand...
<!-- artifact:quote:end -->
<!-- artifact:quote:start -->
> ♛ ▲ I'm assuming then there will be 5 court types, each ethos corresponding to one of the five skills? ► Each Ethos unlocks more than one Court Type, and the Court Types are (currently) based on the five skills thematically, yes. ► We have five court types, corresponding with the five primary skills. Ethos on the other hand, we have a few more of. About seven or so. Each ethos unlock a court type that is somewhat "thematically appropriate" more than anything else. Click to expand...
<!-- artifact:quote:end -->
Yes, but ethos is part of culture. Your court type will be tied to ethos (part of your culture). If you change cultures and end up with a different ethos, you could have a different court type. It gives you a reason to hybridize or diverge your culture if you want a different court type. To clarify based on the FAQ: In other words, there are 5 court types and 7 (currently) ethos. That means 2 court types (at this time) will be tied to two ethos instead of only one. I think that's what rageair is referring to. Yes, the first part of the answer in the FAQ says it unlocks more than one for each ethos, but if you read the second answer, it appears to contradict that some, so perhaps there is confusion between the two devs who answered that question. In the end, yes, ethos determines court type. However, since you have one ethos for your culture, you can also state that it's determined by your culture, which ethos is a part of. In terms of changing it, you can either hybridize or diverge your culture to change ethos. Culture traditions can change over time without doing that, but it isn't stated that ethos can change over time and I kind of doubt that will happen. So it is most likely limited to hybridization and divergence if you want a different court type.

## Reply 237 — participant_123 · 2021-05-27 · post-27568616

<!-- artifact:quote:start -->
> Riamus said: Yes, but ethos is part of culture. Your court type will be tied to ethos (part of your culture). If you change cultures and end up with a different ethos, you could have a different court type. It gives you a reason to hybridize or diverge your culture if you want a different court type. To clarify based on the FAQ: In other words, there are 5 court types and 7 (currently) ethos. That means 2 court types (at this time) will be tied to two ethos instead of only one. I think that's what rageair is referring to. Yes, the first part of the answer in the FAQ says it unlocks more than one for each ethos, but if you read the second answer, it appears to contradict that some, so perhaps there is confusion between the two devs who answered that question. In the end, yes, ethos determines court type. However, since you have one ethos for your culture, you can also state that it's determined by your culture, which ethos is a part of. In terms of changing it, you can either hybridize or diverge your culture to change ethos. Culture traditions can change over time without doing that, but it isn't stated that ethos can change over time and I kind of doubt that will happen. So it is most likely limited to hybridization and divergence if you want a different court type. Click to expand...
<!-- artifact:quote:end -->
Perhaps each ethos opens two court types? One is very much on brand for the ethos in question, and one is *nearly* on brand, but potentially close to one of the others? Speculation of course. Or they've not got all the ethos types nailed down yet.

## Reply 238 — participant_035 · 2021-05-27 · post-27569105

<!-- artifact:quote:start -->
> K'shar said: I agree. Ducal court's should also definitely be a thing. Court size, effect, cost, bonuses and appearance should just scale on title rank. Click to expand...
<!-- artifact:quote:end -->
Certainly for independent dukes. For dukes with a liege perhaps being able to hold a court should be part of a contract.

## Reply 239 — participant_141 · 2021-05-27 · post-27569269

<!-- artifact:quote:start -->
> Gwydden said: Birch leaves are so last season. Click to expand...
<!-- artifact:quote:end -->
And the jester has to wear poison ivy leaves.

## Reply 240 — participant_059 · 2021-05-27 · post-27569313

<!-- artifact:quote:start -->
> SauronGorthaur said: Wait, actually I have to reconsider my initial opinion on linking court types to cultural Ethea. Judging by the remark that many Indian cultures have a spiritual Ethos, it sounds like each base culture has an Ethos from the get go. And as per PDX-Nicou's recent post in the previous thread, Divergence is the only answer to wanting to swap an Ethos out. That's further corroborated by this dev diary, as it mentions how Divergence and Hybridization (meaning it's actually two ways) are the only answers to wanting different court types (as that in turn requires an Ethos change). And that's kinda limiting. And while some choice is good in games, this is limiting in a bad way. Let's say you want to play as a French dynasty. Perhaps you're French yourself or at least some of your ancestors were. Perhaps you're a fan of French history. Or perhaps the idea of eating frogs simply speaks to you on a spiritual level. Whatever your reason for playing French may be, you're limited to the - I'm going to guess here - two court types unlocked by the Ethos it has from the get go. So, what happens if the court types unlocked by that Ethos don't suit your playstyle? The only answers provided by the devs are either Hybridization or Divergence. I.e. creating a culture that is NOT French. Completely defeating the point of wanting to play as specifically French. And here you're not limited in your choices because you did something, like how picking certain buildings means you can't have others because building slots are limited. You're simply limited from the get go. It'd be like limiting characters of French culture to a specific religion. According to the GameWatcher article, Traditions can be picked by the Cultural Head if you have free spots by using Prestige. Which indicates that unlike Ethea Traditions are not there from the get go. Or at least not all spots are filled. As such, I'd argue that Traditions would make for a better mechanic to tie court types to. You'd still have to make a choice but here you'd be in control. Click to expand...
<!-- artifact:quote:end -->
Only Hybridization allows you to change Ethos. Divergence is just for changing Traditions.

## Reply 241 — participant_059 · 2021-05-27 · post-27569319

<!-- artifact:quote:start -->
> Voy said: I can only echo the mistake of neglecting the existence and prominence of ducal courts, especially in France, Spain, Italy and the HRE. I can also see why not all dukes should hold court, but there's a specific group that definitely did and should. Namely independent dukes and prominent vassal dukes in Empires and Kingdoms where centralisation is low. Click to expand...
<!-- artifact:quote:end -->
Even restricting it to independent that's is still a lot of Courts to simulate. I really think it's just an issue of resources at the end of the day and making a threshold between King and the below tiers

## Reply 242 — participant_125 · 2021-05-27 · post-27569344

<!-- artifact:quote:start -->
> Koyraboro said: Even restricting it to independent that's is still a lot of Courts to simulate. I really think it's just an issue of resources at the end of the day and making a threshold between King and the below tiers Click to expand...
<!-- artifact:quote:end -->
Well, I for one can't wait for the expansion "the Prince" where being a vassal is interesting.

## Reply 243 — participant_059 · 2021-05-27 · post-27569460

<!-- artifact:quote:start -->
> Voy said: Well, I for one can't wait for the expansion "the Prince" where being a vassal is interesting. Click to expand...
<!-- artifact:quote:end -->
Same

## Reply 244 — participant_149 · 2021-05-27 · post-27569913

Very excited to hear about the new expansion! The game really needs new ways to interact with courtiers and vassals. My characters keep dying of complications of obesity due to attending too many feasts! Will be nice to have some other options.

## Reply 245 — participant_150 · 2021-05-27 · post-27570414

I really hope they bring back coronations and the jeweler mechanic. also maybe introduce legendary artifacts like hunting for Excalibur in England to help cement your rule. and armor/weapons to give bonuses to duels or protection from schemes. and pets/mounts that could be seen in the court.

## Reply 246 — participant_151 · 2021-05-28 · post-27571964

I wonder how Grandeur will work with ascetic faiths. Lollards don't looks like being impressed by fancy stuff in palace

## Reply 247 — participant_152 · 2021-05-28 · post-27572158

I am excited for this DLC!! I hope it lives up to the potential.

## Reply 248 — participant_153 · 2021-05-28 · post-27572347

<!-- artifact:quote:start -->
> fodazd said: I agree with this. However: If the transition didn't happen on zoom out, but only when you deliberately access the court, then we could have the nice visuals as without a usability cost. Click to expand...
<!-- artifact:quote:end -->
An animated transition should be optional, otherwise a nice indulgent gimmick becomes frustrating. Though I am not certain I would keep my maps of vital strategic intel in my throne room.

## Reply 249 — participant_139 · 2021-05-28 · post-27572555

As someone who didnt really play CK2 (30 hrs) i cant compare the two games. But for me im really likeing the look of the expansion and i hope as i recall in an early dev diary on tutorials they will update theirs when they bring out new big features and expansion packs, did i dream that or is that something thats going to happen?

## Reply 250 — participant_154 · 2021-05-28 · post-27574024

Cool that the artifact system comes back, and that it will be extended and mixed up with other new systems, I just hope they won't remove all the other ways to get cool artifacts and won't limit it to just ordering them from your guests/artisans. On the 3D room, meh, I don't know. Sometimes less is more, and some things should be left to our imagination.

## Reply 251 — participant_153 · 2021-05-29 · post-27576240

<!-- artifact:quote:start -->
> Sinister2202 said: The throne room must have good feng shui. Are you consider this devs? Click to expand...
<!-- artifact:quote:end -->
The throne room should have good feng shui, or bad things will happen. It might be coincidence and not causal though, confirmation bias is hell of a drug. And we need a scheme to subtly disrupt the feng shui of the throne rooms of our enemies.

## Reply 252 — participant_155 · 2021-05-30 · post-27576476

<!-- artifact:quote:start -->
> blackninja9939 said: Being able to see everyone and your artifacts etc is a big part of the immersion into the royal court that we want hence the 3d scene instead of painted backgrounds. We are well aware of the performance implications and will be aiming to make sure it can run fine across our minimum and recommended hardwares, with some reduction of number of things on screen etc if required for the min specs like the options we already have for them. What other divisions would you want here? I don't think that is too true here, the specific nature of it is that exceeding one's expectations is easier when you are small and the expectations are low compared to someone like the HRE or Byzantines. So I think it makes a lot of sense design wise and thematically for this system. Click to expand...
<!-- artifact:quote:end -->
Hey @blackninja9939, got some suggestions ! 2. I'd love to see itinerant courts, where you travel throughout the year with your entourage, from palace to palace, often hosted by your major vassals (which, of course, gives the host a great deal of access to you, and a level of control over who else has access to you), and of course, often on the road itself. In general, a lot of the "focus" of a court depended on the location of the court - just consider the tribulations of high medieval English kings and their attempts to assert royal control over the finances of London, and thus the establishment of Westminster just outside the old city limits. Even the French kings weren't permanently situated in La Cité, moving to a more secure location (near the Bastille) during the HYW, and La Cité became more and more of an administrative center and location for special events through the late Medieval period. In a period dependent on personal relationships to hold together great territories, the court was key in making sure that the monarch could maintain connections with the key people he needs to keep onside, and be seen ruling and demonstrating that he holds power. In many ways, centralization in the period (and to a greater extent in the early modern era) relied on the monarch being able to build a power base outside of the aristocracy, and much of this depended on who could easily access the court to petition the king. Rulers can also hold court when they're personally on campaign, which also, temporarily, completely changes the character of the court, while back home, the court seneschal/majordomo might be overstepping their caretaker role ... Beyond just access, there's also the question of power base, so, what social groups does the king rely on for supporting his rule, and how are these groups welded to him to ensure continued support? This could determine a lot about which advisors the king keeps close, what kinds of people sit on the in-game council itself, and how the king is practically forced to respond to various kinds of petition - for example, if he relies heavily on the Church for administration, and has a lot of church figures as regulars in his court, then a petitioner against the church might be summarily dismissed by one of his advisors, and you have to decide if you countermand a key supporter of your rule. And outside the king's power base, how is rulership maintained over the rest of the kingdom? Does the king rely on fealty through justice and right of rule, is the king the lynchpin that balances diverging interests among his vassals/subjects, or is his power derived from his ability to hold his vassals together for mutual defense, or perhaps, is he a controller of sufficient wealth in his own right that he can keep vassals and power-brokers on-side through agreements of mutual benefit? For example, the early Capetians very much play the balancing game, and really that's an important part of French politics until after the HYW. How all of this reflects on your "court style" is through the fact that your court protocol/culture is determined partially by culture, partially by what kinds of people you want to impress, partially by what kinds of people have access to petition you, and partially by what other powerful people in your kingdom want your court to be like, since their own decisions will have an impact and you won't necessarily be able (or willing) to counter them. This might work well as a set of traits, where traits are permitted/forbidden based on culture, ruler personality, some element of powerbase, and then the player chooses a non-conflicting set of traits from the given set of options. On top of that, a court would have a current location and current host, which skews the probabilities for different types of petitioner, and can cause friction between the host and the court members if there are incompatibilities, with the ruler able to weigh in. 3. Let the expected level of grandeur slowly chase the actual level of grandeur, and then set the starting expectations, in history files, based on the level of grandeur of the predecessors of starting kings and emperors. Also, foreigners should judge a court's level of grandeur based on their own expectations. For example, a tribe migrating into the balkans might be wowed by Byzantine splendor, and that might make it easier to convince them to become vassals, but as they get used to the level of opulence displayed in Constantinople, they eventually (perhaps after a generation) don't get overawed by that, and so when they, for example, break away from the Byzzies and get conquered by the king of Sicily, they're disappointed that his wealthy and well-stocked court is, nevertheless, outright spartan compared to Byzantine splendor. Overall though, I'm excited to see this dlc taking shape!

## Reply 253 — participant_027 · 2021-05-30 · post-27577064

Will there be walking animation?

## Reply 254 — participant_132 · 2021-05-30 · post-27577701

<!-- artifact:quote:start -->
> ShadyGuy_SuspiciousGoal said: Will there be walking animation? Click to expand...
<!-- artifact:quote:end -->
Just a guess, but I doubt it. Everything I've seen references "placing" objects/people in various locations. This isn't a first person or third person type of game where you can control where you walk. It is very unlikely that they'll put in that kind of work into this and will likely just have people and objects placed throughout the scene. Hopefully they will add some new standing animations, though. Some of them are good, but some seem strange and some are clearly missing. With a court and many characters present and full body views instead of just headshots means you'll want more variety in animations so people aren't all doing the same thing.

## Reply 255 — participant_116 · 2021-05-30 · post-27578484

I know they're doing this piece meal to not bite off more than they can chew but I really hope the devs are planning on having estates/hearths for the rulers that can't have courts. It doesn't need all the splendor but having a place to show your characters/family and store your artifacts for EVERYONE just seems like an important fundamental design choice.

## Reply 256 — participant_099 · 2021-05-31 · post-27578749

<!-- artifact:quote:start -->
> Senfmann said: It's a tad weird to be expected to pay for my underlings clothes, food is fine, but clothing? Would you be willing to consider a system where you can set an appropriate level of clothing as the ruler with the twist of the courtiers paying for it themselves (landless courtiers not included, or as part of some monthly pittance). As far as I know, that was the strategy at the absolutist courts of Europe (not the timeframe I know), to bleed out poor courtiers forcing them to pay for the latest fashion. Otherwise I like this DD and the way the game develops very much! Click to expand...
<!-- artifact:quote:end -->
time to refuse my courtiers clothes

## Reply 257 — participant_099 · 2021-05-31 · post-27578751

<!-- artifact:quote:start -->
> SauronGorthaur said: Wait, actually I have to reconsider my initial opinion on linking court types to cultural Ethea. Judging by the remark that many Indian cultures have a spiritual Ethos, it sounds like each base culture has an Ethos from the get go. And as per PDX-Nicou's recent post in the previous thread, Divergence is the only answer to wanting to swap an Ethos out. That's further corroborated by this dev diary, as it mentions how Divergence and Hybridization (meaning it's actually two ways) are the only answers to wanting different court types (as that in turn requires an Ethos change). And that's kinda limiting. And while some choice is good in games, this is limiting in a bad way. Let's say you want to play as a French dynasty. Perhaps you're French yourself or at least some of your ancestors were. Perhaps you're a fan of French history. Or perhaps the idea of eating frogs simply speaks to you on a spiritual level. Whatever your reason for playing French may be, you're limited to the - I'm going to guess here - two court types unlocked by the Ethos it has from the get go. So, what happens if the court types unlocked by that Ethos don't suit your playstyle? The only answers provided by the devs are either Hybridization or Divergence. I.e. creating a culture that is NOT French. Completely defeating the point of wanting to play as specifically French. And here you're not limited in your choices because you did something, like how picking certain buildings means you can't have others because building slots are limited. You're simply limited from the get go. It'd be like limiting characters of French culture to a specific religion. According to the GameWatcher article, Traditions can be picked by the Cultural Head if you have free spots by using Prestige. Which indicates that unlike Ethea Traditions are not there from the get go. Or at least not all spots are filled. As such, I'd argue that Traditions would make for a better mechanic to tie court types to. You'd still have to make a choice but here you'd be in control. Click to expand...
<!-- artifact:quote:end -->
this this this, this summarizes many of my concerns regarding ethoses

## Reply 258 — participant_063 · 2021-05-31 · post-27578777

<!-- artifact:quote:start -->
> Senfmann said: It's a tad weird to be expected to pay for my underlings clothes, food is fine, but clothing? Would you be willing to consider a system where you can set an appropriate level of clothing as the ruler with the twist of the courtiers paying for it themselves (landless courtiers not included, or as part of some monthly pittance). As far as I know, that was the strategy at the absolutist courts of Europe (not the timeframe I know), to bleed out poor courtiers forcing them to pay for the latest fashion. Otherwise I like this DD and the way the game develops very much! Click to expand...
<!-- artifact:quote:end -->
Actually, the records of Medieval Royal courts are full of details like the King ordering so many bolts of silk, and/or satin, for his courtiers to use for apparel. So, apparently, that was a thing...

## Reply 259 — participant_123 · 2021-05-31 · post-27578785

<!-- artifact:quote:start -->
> vandevere said: Actually, the records of Medieval Royal courts are full of details like the King ordering so many bolts of silk, and/or satin, for his courtiers to use for apparel. So, apparently, that was a thing... Click to expand...
<!-- artifact:quote:end -->
I'm not 100% certain, but that may have been limited to the household and any noble with a "job" that was employed directly by the King (and thus technically part of the household). Not so much for the Duke of Random who might be forced to maintain himself and his clothing at his own expense - unless he could get a title of some sort within the court that would see him granted livery rights.

## Reply 260 — participant_028 · 2021-05-31 · post-27579345

<!-- artifact:quote:start -->
> pending on clothes will increase their prestige, and will even cause them to wear fancier clothes at higher levels of expenditure (commoners will wear low nobility clothes, and so on) Click to expand...
<!-- artifact:quote:end -->
But whose said this is for Duke of Random? It's logical that this is for employed ones. From the first post:

## Reply 261 — participant_156 · 2021-05-31 · post-27579641

When did CK3 became The Sims Medieval?

## Reply 262 — participant_125 · 2021-05-31 · post-27579698

<!-- artifact:quote:start -->
> Demony said: When did CK3 became The Sims Medieval? Click to expand...
<!-- artifact:quote:end -->
Paraphrasing but Henrik Fåhreus said he imagined crusader kings to be a mix between game of thrones and the sims back when CK2 was fresh.

## Reply 263 — participant_157 · 2021-05-31 · post-27579702

So glad you're going with something roleplay-focused. It really is what makes the franchise special and the one thing that this amazing game needs more of.

## Reply 264 — participant_099 · 2021-06-01 · post-27581137

<!-- artifact:quote:start -->
> Demony said: When did CK3 became The Sims Medieval? Click to expand...
<!-- artifact:quote:end -->
...always? Crusader Kings was pretty obviously always designed to almost be more role-play heavy than strategy focused.

## Reply 265 — participant_158 · 2021-06-01 · post-27581575

Looks amazing I really hope you create a more convinient and visual money sink than the holding upgrades. It is so cumbersome to spend money upgrading and knowing what you have already upgraded. My fingers are still crossed for an amazing trade system something like in eu 4 but dynamic so you can pull trade to you cities if they are powerfull enough or having the ability to leach of powerfull cities.

## Reply 266 — participant_159 · 2021-06-01 · post-27582791

Nice! Now I will be able to see my displeased council plot against me in a more life-like way!

## Reply 267 — participant_160 · 2021-06-01 · post-27583131

I really like the idea of having a court type, and of grandeur! Just a suggestion to improve immersion: what if instead of the court type giving a trait to existing courtiets, it will cause you to attract/generate more courtiers of the specified type? So basically the king is focusing on inviting diplomats, generals, or scholars to his court, rather than his friends and family magically becoming diplomats, generals, or scholars.

## Reply 268 — participant_160 · 2021-06-01 · post-27583144

<!-- artifact:quote:start -->
> Cymsdale said: Grandeur sounds like it gives a lot of bonuses just for existing. Will the game be balanced around having Grandeur (the DLC) toggled on or off, or will it be a pay-to-win DLC feature where the player will be more powerful simply by owning the DLC? Click to expand...
<!-- artifact:quote:end -->
Although I agree with what you are saying, I am not sure this is really an issue: in miltiplayer games, everybody plays with the same rules, and in singleplayer I don't think that there's much concern over the player being OP because he can set his own limitations.

## Reply 269 — participant_161 · 2021-06-02 · post-27583928

I know others have said it, but I need to piggyback on this. I really hope royal courts will be implemented for independent dukes in the future. I understand the limitation from an operational perspective since different start dates have different amounts of independent dukes thanks to internal fracturing, but in reality and in CK3 independent dukes can sometimes be even more influential and powerful than some fully formed kingdom rulers. For them not to have their own courts is not only inaccurate from a historical perspective but also a little game breaking for smaller realms. It gives already preformed kingdoms like France a huge advantage over smaller independent realms who are already at a disadvantage from game start. Take the 867 start date in Great Britain for example. Most of the realms in Great Britain start as petty kingdoms all equally vying for power over their neighbours. From the start none of them can really touch France, but after a few decades of consolidation on the part of super-duke Alfred, it really doesn’t take that long for his “petty” kings to become a serious threat to the french powerhouse. I don’t think I’ve ever had a play-through where he’s actually invaded France, but I’ve had many where he COULD have if only he had chosen to do so. I once had a playthrough were AI Essex took over all of Mercia, Northumbria and Jorvik thanks to not being completely crap at war. She took over half the island in only 13 years with an army of around 2k, and by the end had almost tripled it through conquest. If however you give France all the perks from holding court that scenario of a little petty kingdom being able to grow and consolidate enough to overthrow them becomes almost impossible, because it pretty much negates the one disadvantage that France always has; internal fracturing. It’s a little weird that none of them can hold court despite being independent rulers with serious military and financial might sometimes rivalling actual in-game “kings” simply because their title is counted as “ducal” instead of “kingdom” by game mechanics. I feel this is especially true for leaders like Alfred of Wessex who was well know for his intellectual achievements. Alfred was responsible for improving learning and intellect in his kingdom on a scale unseen in the British isles since the fall of the Romans. He built universities and libraries, and hired intellectuals from all over Europe to give lectures and teach his courtiers/persons of importance various languages and skills that would help improve their craft and relations with foreign dignitaries. He was able to overcome huge disadvantages in battle thanks to his intellect and tactical thinking which he went on to impart onto his commanders. He was quite well know during his time for this exact reason. For him not to be able to hire “inspirational characters” via his court in game simply because he’s considered a “duke” and not a “king” seems a bit off.

## Reply 270 — participant_132 · 2021-06-02 · post-27584051

I don't think RC's grandeur and court mechanics are going to be "all powerful" and allow a kingdom to become far more powerful than a duke who has a large realm. That would pretty much break the game. The court mechanics are going to be a balancing game where it can help you or hurt you depending on how you manage it. The AI is likely going to be set up so that how well it manages it will vary based on traits of the rulers, so you might have one King of France who gains a lot of benefit from the mechanics and then their heir will end up with a lot of negatives from the mechanics because they have traits that make them not put in much effort into maintaining a good level of grandeur. And that's just a very generalized way of looking at it. I'm sure there will be a lot of things that can take the AI both ways and I think in the end, even with high grandeur, I really don't think it will make you all that noticeably more powerful than you are without the DLC. I may be wrong, but I expect the highest levels of grandeur/court will put you slightly better than without the DLC, while you have the possibility of being much worse off than you'd be without the DLC if you don't manage your grandeur well. Or, if they make it so the average level of grandeur is where you are without the DLC, then I would expect the difficulty of getting really high levels of grandeur will be very high and/or the benefits will quickly start to drop off as you get more grandeur so you won't become OP compared to not having the DLC.

## Reply 271 — participant_162 · 2021-06-02 · post-27584517

<!-- artifact:quote:start -->
> Cymsdale said: Grandeur sounds like it gives a lot of bonuses just for existing. Will the game be balanced around having Grandeur (the DLC) toggled on or off, or will it be a pay-to-win DLC feature where the player will be more powerful simply by owning the DLC? Click to expand...
<!-- artifact:quote:end -->
I'm not quite sure. It seems that it actually costs money to maintain, which is already a fairly important resource. Undershooting grandeur also seems like it will impose some fairly bad penalties, so you'd need to balance your economy around it. Which tbh sounds like a great approach - if you do not have the dlc, you can spend money on stuff like armies or buying favors, with the dlc you have the additional layer of having to worry about this instead, but get good bonuses for your trouble. Also, thematically appropriate

