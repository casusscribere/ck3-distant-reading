---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1279641/"
forum_thread_id: 1279641
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 3
title: "CK3 Dev Diary #3 - War"
dd_date: 2019-11-12
author_handle: Servancour
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2032
inline_image_count: 6
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1279641'
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
    location: raw_lines_234_to_237
    action: preserved_and_flagged
    counts:
      Like: 14
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 1 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_245_to_307
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_308_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #3 - War

<!-- artifact:thread_metadata:start -->
- Thread starter [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)
- Start date [Nov 12, 2019](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-3-war.1279641/)
<!-- artifact:thread_metadata:end -->

Greetings!  

War. What is it good for? You may ask. A whole lot I’d say. You can use it to press that juicy Claim you have been holding on to for a while, or perhaps you’d rather use it to put the unbelievers to the sword. Whichever strikes your fancy. The topic of the day is war, and more specifically, how we go about waging war.  

I aim to give you an overview of how wars will be fought. I will not go into details about CBs or anything like that this time. Bear in mind that the game is still very much in development and everything talked about here is subject to change.  

Let’s start by taking a look at what an army is made up of. Just like in Crusader Kings 2, the bulk of your armies consists of Levies. Levies in Crusader Kings 3 are made up of their own unit type, simply called Levy. These are essentially conscripted peasants forced to do your bidding and are not very impressive on their own. In great numbers, however, they are an efficient meat shield meant to complement the troops of your armies that have a far higher impact: Men-at-Arms.  

![dd_03_armynumbers.png](https://forumcontent.paradoxplaza.com/public/512326/dd_03_armynumbers.png "dd_03_armynumbers.png")



Men-at-Arms are the equivalent to the Retinues of CK2. They are trained troops that come in several different unit types which excel in their given role. There are base variations available for everyone to recruit, such as Light Cavalry and Heavy Infantry, but the really interesting ones are usually unique to certain cultures or specific regions of the map, though all have their own stats and uses. Speaking of stats, there are four different values present on a Men-at-Arms regiment that you need to keep track off:  

Damage - This is obviously the amount of damage a single soldier of this type is able to inflict on the opponent.  

Toughness - This is how much damage a soldier can take.  

Pursuit - In the aftermath of a battle (more on this below), Pursuit increases the amount of damage you can inflict upon a routing enemy.  

Screen - The opposite of Pursuit, Screen allows you to protect fleeing soldiers from being killed.  

![dd_03_pikemen.png](https://forumcontent.paradoxplaza.com/public/512330/dd_03_pikemen.png "dd_03_pikemen.png")



Not all Men-at-Arms are equal. You will have access to a few immediately from the start and unlock access to additional regiment types as you progress throughout the game. Some will be similar to each other, but may be tailored towards a certain terrain type. Others may just be a straight upgrade, but will in those cases be much more expensive than their weaker counterpart.  

Men-at-Arms allow you to customize your army for any given situation. If you know where or who you will fight, certain Men-at-Arms will be far superior. Is there a lot of hilly terrain in your region? Then Archers are the way to go. Are you facing a lot of cavalry? Bring Pikemen! A smaller army will stand a much higher chance of winning if you bring a Men-at-Arm type that counters those of the enemy. When a regiment is countered, it’s efficiency in battle will be lowered, with its Damage output significantly reduced. If the countered regiment is greatly outnumbered by the countering type, efficiency will reduce even further. There’s a limit to how much a Men-at-Arm’s Damage can be reduced though, as to not make your expensive troops completely useless.  

Next we have a special kind of Men-at-Arms: Siege Weapons. Medieval warfare was all about sieges. Castles and sieges are very iconic for the time frame, so we felt that it was necessary to have that properly represented. You’ll start off with access to a rather weak catapult, but it will still allow you to besiege holdings faster than without one. Later on, you’ll unlock improved siege weapons, such as trebuchets, that are able to speed up sieges significantly.  

![dd_03_siegeweapons.png](https://forumcontent.paradoxplaza.com/public/512324/dd_03_siegeweapons.png "dd_03_siegeweapons.png")



You can only own a certain number of Men-at-Arms regiments at any given time, so choose carefully which troops you decide to recruit!  

Levies and Men-at-Arms are not the only soldiers available to you. As a ruler, you have a number of Knights at your disposal. These are the vassals and courtiers of your realm with a high Prowess, which is the equivalent to Combat Rating in CK2, and represents how good a character is at fighting and is used when they participate in battles. You can normally only have a few dedicated Knights, but there are various ways to increase the number of Knights, as well as their effectiveness.  

![dd_03_knight.png](https://forumcontent.paradoxplaza.com/public/512328/dd_03_knight.png "dd_03_knight.png")



Finally, we have the Commander. An army can only have a single Commander, who uses his Martial skill to improve the troops under his command. There are plenty of different commander traits available, which either have a direct effect on battles, such as terrain bonuses, or give the Commander bonuses outside of battles. One such example is the ability to have supply last longer (more on this below).  

![dd_03_commanders.png](https://forumcontent.paradoxplaza.com/public/512325/dd_03_commanders.png "dd_03_commanders.png")



![dd_03_holywarrior.png](https://forumcontent.paradoxplaza.com/public/512327/dd_03_holywarrior.png "dd_03_holywarrior.png")



With armies out of the way, let’s have a look at battles! At the very start of any battle, a combat width is set that decides how many troops are able to fight each other at the same time. The width is set to the relative size of the defender, depending on the terrain type you are fighting in, being larger in flat and open terrain, and smaller in rough terrain and mountains. I would generally advise against attacking larger armies in plains for example...  

The single most important part of a battle is Advantage, which is essentially a modifier that increases the damage of all troops on either side. When a battle starts, all sources of Advantage is taken into consideration. It can come from traits, terrain, buildings, etc. but most importantly, the Martial skill of your Commander. All of these are added together for both sides of the battle. The difference is then added as the Advantage bonus for the side with the higher Advantage.  

Example: Your army has a total Advantage of 40, and attacks an enemy army that has a lousy total of 10. This means that you will have an Advantage bonus of 30 during the battle, which then translates into a rather significant damage bonus for your troops.  

In addition to the starting Advantage, each Commander also makes a roll every few days in an attempt to increase their Advantage or even it out. This tug of war can be further expanded by various modifiers and traits. For example, the trait ‘Cautious Leader’ will decrease your potential max roll, but also increase your lowest possible roll, trading a high potential for a higher average. These exist to make even battles a tad bit unpredictable, but will rarely be the deciding factor.  

Soldiers on the combat line damage the enemy on every tick. When a soldier “dies”, he will be considered to be either a Casualty, or to be Routed. Casualties, you guessed it, are considered dead and will have to be replenished over time. Routed soldiers, on the other hand, are troops that are injured or fled the battle and are added back to the army once the battle is resolved. Battles are resolved once either side runs out of fighting troops.  

Once the battle is won, it enters the Aftermath phase which lasts for a few days. This is when the victor has the opportunity to chase down and kill any survivors (the Routed troops). As mentioned earlier, this is the time for certain Men-at-Arms to shine. With a high Pursuit you can kill a larger amount of the enemy to really capitalize on your victory. Alternatively, you can have a high amount of Screen to make losing battles less penalizing. Keep in mind that battles will grant you a fairly limited amount of War Score. Which brings us to sieges!  

Besieging and occupying enemy holdings is the main way of gaining War Score and winning wars. As mentioned in lats week's map dev diary, Baronies are their own provinces. You will not have to siege all of them in order to occupy a full county or seize your War Goal, only fortified holdings have to be besieged. Castles and County Capitals are all fortified by default, with how difficult it is to besiege these holdings being decided by their Fort Level. Fort Level can be increased by certain buildings and modifiers.  

Each Fort level increases the amount of Siege Progress you need to get before it gets occupied. You gain a base amount of Siege Progress every tick, which can be increased further by heavily outnumbering the garrison or having Siege Weapons. This constant progress won’t change over the course of a siege. It allows you to know what the maximum duration of the siege will be and you can take that into account as you plan your next move. Sieges also have what we call ‘siege events’, which occur with a fixed interval, and can make the siege progress faster by giving you a one time Siege Progress bonus, or increase your base Siege Progress. Siege Weapons are required to get the ‘breached walls’ event, which in turn allow you to directly assault the holding. This is a risky maneuver since it will cost you troops, at the benefit of vastly increasing your daily Siege Progress.  

Being attacked while besieging a holding will make you the attacker of the battle, making you lose out on any usual defender bonuses you would get from the terrain. Sieges are therefore slightly riskier, and assaulting the holding to gain control of it before the enemy attacks might well be worth the cost.  

A few final words on moving armies around. As I mentioned briefly in last week’s DD thread, major rivers have designated fords for crossing. You can no longer cross them freely as in CK2, and will often have to move your army to find a good place to cross. Beware though, crossing a major river will make you lose Advantage should you engage an enemy in battle on the other side, making river crossings for perfect places to catch your opponent. Along with the increased amount of Impassable Terrain, there are plenty of bottlenecks that you can use to your advantage (pun intended).  

Have you ever been annoyed by walking into a province just for a short while in CK2, only to go above the Supply Limit and lose a bunch of troops? Fear not. Armies now carry an amount of Supply with them. Supply is drained whenever armies are in Baronies with a lower Supply Limit than their size. You can therefore safely march through a few Baronies with a low Supply Limit without troops dying. If you army runs out of Supply however, it will start to take attrition and lose troops over time. Supply is increased as long as you are below the Supply Limit in territory you control. Beware though, your army might not take attrition on low Supply, but it will suffer an Advantage Penalty in battles!  

Chasing armies deep into enemy land is certainly not recommended. Marching into a County controlled by the enemy, that doesn’t border anything you control and is not on the coast, will make your army take a single and quite significant attrition hit. If you have a huge amount of troops to spare though, then perhaps you don’t need to worry about it.  

Phew. That turned out to be a bit lengthier than expected. I hope you’ve gotten a fairly good (although slightly summarized) picture of what to expect when waging war in Crusader Kings 3!

 

Last edited: Nov 12, 2019

<!-- artifact:reactions:start -->
- 14 Like
- 3 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Servancour](https://forum.paradoxplaza.com/forum/members/servancour.465268/)**
Role: Game Designer
Badges: 4
Reaction score: 9,949

*[Full game-badge icon list of 2 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
