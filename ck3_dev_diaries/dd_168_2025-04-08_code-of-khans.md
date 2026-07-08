---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1734805/"
forum_thread_id: 1734805
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 168
title: "Dev Diary #168 - Code of Khans"
dd_date: 2025-04-08
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
body_word_count: 3860
inline_image_count: 30
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1734805'
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
    location: raw_lines_~28_to_148
    action: discarded_from_output
  - type: thread_banner
    location: raw_line_147
    action: preserved_and_flagged
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3675.jpg?1744100123
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_150_to_152
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_471_to_474
    action: preserved_and_flagged
    counts:
      Like: 62
      (unlabeled — rendered as base64 data URI): 4
      Love: 14
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_482_to_535
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_536_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/3/3675.jpg?1744100123)
<!-- artifact:thread_banner:end -->

# Dev Diary #168 - Code of Khans

<!-- artifact:thread_metadata:start -->
- Thread starter [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)
- Start date [Apr 8, 2025](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-168-code-of-khans.1734805/)
<!-- artifact:thread_metadata:end -->

Hi! This expansion is adding quite a few new systems, and today we’re here to talk about the modability and underlying tech of some of them.  

### Tributaries​

One of the more impactful features we’re adding is tributaries. So we’re on the same page when it comes to terminology: a suzerain is to a tributary what a liege is to a vassal.  
Previously, a vassal had a collection of individual contracts defined on their government type which made up their complete “vassal contract”. This included things such as “feudal_government_taxes” added on the “feudal_government”, which determined how much a vassal with the feudal government would pay to their liege.  
However, with the addition of tributaries this has changed slightly. Firstly, pretty much everything related to “vassal contracts” have been renamed to “subject contracts”. To enable re-use of these contract lists and usage outside of governments, we’ve added a new database called “subject contract groups” which includes the typical list of individual contracts, but can also include extra parameters such as how they should be inherited on succession and how they should appear on the map. These are documented in the info file for subject contracts groups.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1271104/image_01.png "image_01.png")


*[An example of a subject contract group for a type of tributary]*  

Tributaries basically work the same way as vassals, with the same system for contracts. But instead of being applied automatically based on your government when you become someone’s vassal, tributaries need to be started manually through script.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1271105/image_02.png "image_02.png")


*[Starting new tributary contracts is easy!]*  

This effect will only work if both the tributary and the suzerain are independent rulers, and that the resulting tributary relation won’t result in a circular loop of people being tributaries to each other. This can easily be checked with the “can_be_tributary_of” trigger. They can also be broken with “scope:some_tributary_character = { end_tributary = yes }”  
Tributary contract groups are also marked with “is_tributary = yes” so that we can differentiate them from regular vassal relationships, as characters with tributary contracts are still considered “independent rulers”.  
To get a character’s suzerain you can use the new “character.suzerain” link, or “character.overlord” which will get either the liege if the character’s a vassal, or the suzerain if they’re a tributary. “top_suzerain” and “top_overlord” also exist. The latter will first find your top liege and then keep going to your top liege’s top suzerain, if they have one.  

The AI has a chance to break free from their suzerain each year based on the “ai_will_do” in the “cease_paying_tribute_interaction”, which is what’s displayed here:  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1271106/image_03.png "image_03.png")



### Obedience​

Any character who has a government type that uses the “obedience” government rule, or has a liege/suzerain/employer who does, will use obedience. The threshold needed to become obedient and the obedience value are both calculated in script:  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1271108/image_04.png "image_04.png")



Put simply, if the calculated Obedience value is greater than the threshold, that character will be Obedient. The Obedience target is set in Code with the following priority:  


- De Facto Liege
- Suzerain
- Employer
- De Jure Liege
- None

Obedience is checked in many places using the “is_obedient” and “is_obedient_to” triggers.  

### Confederations​

Confederations are a group of smaller independent rulers coming together, acting as allies in defense against greater threats. Creating one is simple using the “create_confederation” effect.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1271109/image_05.png "image_05.png")



Confederations invalidate on a daily tick if they have fewer than two members, so after a confederation has been created another member must be added using “add_confederation_member”  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1271110/image_06.png "image_06.png")



Members of the confederation will skew their map color towards the color of the confederation creator based on the define “CONFEDERATION_REALM_COLOR_FACTOR”.  

### Situations​

We have implemented a new general system for supporting dynamic region-based gameplay, which we call the Situation system. Its purpose is to provide a fundamental building block for various types of systems, from Struggle-like socio-political systems, to environment systems like the Great Steppe, or smaller temporary effects like a Natural Disaster. (All Under Heaven mentioned!)  

In this sense you can consider Situations to be an evolution of the Struggle system, where we took the learnings of that system, and made it more dynamic and flexible. Extendable in our C++ code base (example: Migrations), but also flexible in our GUI system, and more moddable.  

To note: we have not converted existing Struggles to be Situations, because Struggles contain specific functionality and bespoke interfaces that we do not have in exactly the same way as in the new Situation system.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1271111/image_07.png "image_07.png")



As you can see from the documentation file above, we’re using this system in both Khans of the Steppe, as well as All Under Heaven. It is part of the base game, and thus available for all modders regardless of DLC ownership.  
Now how is this system structured? I will try to explain in a succinct manner. The terms might be a bit dry, but that is because it is a core system - each implementation can rename things in the interface as they like!  

**Sub-regions** - A Situation type consists of one or more geographical sub-regions. These subregions are fixed in number, but each can grow and contract their geographical area while the game is running. Example: the three sub-regions of the Great Steppe - west, central, and east.  

**Phases** - Each Situation type has a set of phases which can transition from one to another via various mechanics. We grabbed some functionality from the Struggle system and extended it.  

An active phase can transition to another phase in these ways:  


- **Max Duration Reached** - If a maximum phase duration is defined, and it is reached, a new phase is picked from the possible future phases, according to a rule, either a weighted pick of the future phases based on the points they have accumulated, or entirely random.  
Example: The Great Steppe seasons progress in this manner.
- **Points Takeover** - One of the future phases has accumulated enough points to reach its “takeover” target. Similar to Struggles, you can use catalysts to add points to specific future phases. It will stop the current phase, and put itself as the active phase.  
Example: Some of the special seasons of The Great Steppe work this way
- **Duration Takeover** - One of the future phases has reached a specific duration. It will stop the current phase, and put itself as the active phase. This can be used to provide a more predictable version of the points takeover phase.
- **Changed via Script** - Our script system is powerful - and we can switch phases directly, skipping the automatic systems. It can also change to a phase that isn’t an official ‘future phase’ of the active phase.

Each sub-region has its own active phase, and its own phase progression, but the possible phases are defined on a situation level. Nothing would prevent us (or a modder) from implementing multiple phase ‘cycles’ within a situation though!  

Of course a situation phase definition also contains modifiers and parameters that will apply to the region (county_modifiers), or the characters participating in the situation (character_modifiers), filtered by their Participant Group, which segues nicely into…  

**Participant Groups** - Who is impacted by the situation? Well we can define a set of participant groups within the situation. Similarly to sub-regions, the groups themselves are pre-defined in the situation type, but are dynamic while the game is running - characters can join and leave groups.  
Each sub-region has their own set of these pre-defines participant groups, and within each sub-region a character can only belong to one participant group (or none).  
So what determines which group you would belong to? This is determined by potential candidates, and settings on the groups. By default the candidates are all the rulers within the geographical area of the relevant sub-region. But you can also add and remove candidates manually via script. (for example you could add the Pope to the Great Steppe even though they are nowhere near)  

For each sub-region, we go through all the candidates, and the first group that is valid for them is where they are added. It is possible to not be valid for any group! Then they’re not part of the Situation.  

![image_08.png](https://forumcontent.paradoxplaza.com/public/1271112/image_08.png "image_08.png")



**Dynamic Sub-region Creation** - When you have defined a situation type, it can be added to the world via a history definition, or via a script effect. But you can also define a new set of sub-regions while starting a situation! This allows us to instantiate the same situation type in multiple locations.  

![image_09.png](https://forumcontent.paradoxplaza.com/public/1271113/image_09.png "image_09.png")



**Ending** - A Situation ends automatically when a phase (in any sub-region) ends without a new phase starting. Additionally, they can be ended in script via an ‘end_situation’ effect.  

**Graphical Features** - Bundled with the Situation system we also have some additional graphical features. Simple ones include the ability to define the map-color of specific sub-regions or participant groups. But more notably we have also added **Map Province Effects** - a way to apply an effect on the map based on the current Situation phase of a sub-region.  
These effects can be applied with a specific effect type and intensity (0.0 - 1.0), we bundle some effects out of the box in Khans of the Steppe: Drought, Summer, Snow - but mods could add more of course!  

![image_10.png](https://forumcontent.paradoxplaza.com/public/1271114/image_10.png "image_10.png")


*[Regular terrain north of the Aral sea]*  

![image_11.png](https://forumcontent.paradoxplaza.com/public/1271115/image_11.png "image_11.png")


*[Summer province effect at full intensity]*  

![image_12.png](https://forumcontent.paradoxplaza.com/public/1271116/image_12.png "image_12.png")


*[Snow province effect at full intensity - this effect is hooked into our existing winter shader, so it will fade in/out neatly]*  

![image_13.png](https://forumcontent.paradoxplaza.com/public/1271117/image_13.png "image_13.png")


*[Drought province at full intensity]*  

All-in-all the Situation system is a building block which allows a game-play feature to use what they need, and tweak what they want, often without requiring new C++ code.  

### Migration​

Nomadic migration is an extension of the situations system - situation type can set that it supports migrations. This will enable additional mechanics for the player and the AI in the map area covered by the specific situation. Migration process and AI decision-making in regards to migration is a complex task, largely controlled by code. We do that every time when there’s high overall complexity and performance risks. Here are the customization points that can be used to tweak how and what happens during migration.  

Migration always happens within some situations. A game rule allows you to enable additional situations in different parts of the world, and migrations will happen independently inside those areas. When you mod your own situations that support migration, please do note that such situations shouldn’t overlap.  

Both player and AI start migration via special interaction called “migration_interaction” in script. Initiation of migration travel or war is handled in code, but the rest can be adjusted. For example, actual transfer of land after migration is up to script. The property of the interaction “ai_accept” controls if the recipient allows you to migrate into their lands peacefully, or will it lead to war. “ai_will_do” on the other hand is used to score the best migration target when AI makes its decision where to migrate. Unlike other interactions, this one gets lots of additional data provided by code to script, so scoring can be more nuanced. Additional scopes are migration target, all potential enemies in case of hostile migration, target land fertility, total military power of all defenders and their allies - all this allows you to prioritise for different targets, balancing risks and benefits.  

When migration is hostile, it uses a special casus belli - “migration_cb”.  

Migration range is limited by migration distance (MAX_MIGRATION_SQUARED_DISTANCE), and there are modifiers (max_migration_distance_mult) that extend or shrink it. It allows you to control different AI behaviors, setting some rulers to be more free-roaming, and putting harsher restrictions on others.  

### Domiciles​

It is our second expansion that uses domiciles, and it introduces a new domicile type - nomadic camp. With more hand-on experience with this system some previous technical decisions proved to be error-prone and hard to work with. So we decided to change how domiciles are connected to playable landless rulers. Domiciles are now owned not by a person, but by a special landless title. Adventurers always have their camp title, landless noble families have noble family title, and nomads have a nomadic camp title. This solves several problems at once - domicile inheritance is now completely controlled by inheritance of special titles. No more cases when code has to decide for a ruler which of the 2 domiciles they should keep - their own or the one they inherited from someone else. Title can have no holder for some time, and when it gets a new holder at some point, domicile is returned back into the game - no risk of accidentally destroying a rich and build-up domicile due to an unfortunate succession. Nothing changes in script or UI - there’s still a direct connection between a ruler and active domicile they have. When a ruler holds several special titles with domiciles, only one of those domiciles will be active - the one that matches the ruler's government type. This shouldn’t normally happen in the base game though.  

### Fertility​

Fertility is a value calculated at the County level. Every County that is in Situation with Migration or whose Holder has a Government Type with the Government Rule uses_county_fertility has County Fertility calculated and shown in the UI.  

![image_14.png](https://forumcontent.paradoxplaza.com/public/1271118/image_14.png "image_14.png")


*[Government Rules for Nomadic Government]*  

If you want to mod in a Situation that uses Fertility without Migration, just add migration = yes to the Situation setup, but disable the migration interaction (migration_interaction) and make sure you add the uses_county_fertility government rule where necessary.  

Herders are a bit special in that they also replenish County Fertility, which is another Government Rule called replenishes_county_fertility. They contribute a base monthly Fertility gain per county, governed by the define BASE_HERDER_GAIN_PER_COUNTY.  

Monthly Fertility change is a bit more complex than our usual systems. We adjust both Growth and Decline to better simulate how nomadic herds would reduce local pastureland, with the overall change often settling at some lower number (though this depends on your domain size and some other factors).  

County Fertility Growth is changed according to this function:  

![image_15.png](https://forumcontent.paradoxplaza.com/public/1271119/image_15.png "image_15.png")


![image_16.png](https://forumcontent.paradoxplaza.com/public/1271120/image_16.png "image_16.png")


*[County Fertility Growth Equation and Graph]*  

County Fertility Decline is changed according to this function:  

![image_17.png](https://forumcontent.paradoxplaza.com/public/1271121/image_17.png "image_17.png")


![image_18.png](https://forumcontent.paradoxplaza.com/public/1271122/image_18.png "image_18.png")


*[County Fertility Decline Equation and Graph]*  

Where these two curves intersect is theoretically the Equilibrium point of a given County in the game. A County’s Fertility will always trend toward the Equilibrium point. There is, however, a “pusher” which determines how sensitive Equilibrium is to the difference between Growth and Decline.  

![image_19.png](https://forumcontent.paradoxplaza.com/public/1271123/image_19.png "image_19.png")


*[County Fertility Pusher Equation]*  

Given the complexity of these equations, we opted for a simpler way to calculate the Equilibrium point to display in the UI, using the small angle approximation sin(x) ≈ x :  

![image_20.png](https://forumcontent.paradoxplaza.com/public/1271124/image_20.png "image_20.png")


*[County Fertility Equilibrium Approximation Equation]*  

Put together with Character, Holding, and County modifiers, these functions contribute what you see in the game as Monthly County Fertility Change.  

It is important to note that the math behind all this is largely contained in what we’ve called “Current County Fertility Modifier” in the monthly change breakdown. This number is the result of these calculations and what directs the Fertility in a County to trend toward its Equilibrium point.  

![image_21.png](https://forumcontent.paradoxplaza.com/public/1271125/image_21.png "image_21.png")


*[Example of a Fertility Monthly Change breakdown]*  

For anyone that hasn’t taken a math class recently, this may all seem like gobbledygook, so here’s the main takeaway for modders: The central way to affect how County Fertility grows and declines, and where it will hit Equilibrium, is by adjusting the following defines which hook into the functions above:  

![image_22.png](https://forumcontent.paradoxplaza.com/public/1271126/image_22.png "image_22.png")


*[Defines for affecting how County Fertility Change behaves]*  

### Herd​

Herd is a new currency stored by a Character’s Domicile.  

![image_23.png](https://forumcontent.paradoxplaza.com/public/1271127/image_23.png "image_23.png")


*[Yurt Domicile script showing the herd parameter]*  

Every Domicile has Current Herd and Max Herd values, accessible by the following triggers:  

![image_24.png](https://forumcontent.paradoxplaza.com/public/1271128/image_24.png "image_24.png")


*[herd and max_herd triggers available for domiciles]*  

A Domicile’s Herd Limit (Max Herd) is determined by their tier plus any relevant modifiers. There is a new define listing base Herd Limit values by tier  

![image_25.png](https://forumcontent.paradoxplaza.com/public/1271129/image_25.png "image_25.png")


*[Defines affecting Herd Capacity, Herd Conversion, and Monthly Gold Income from Herd]*  

Along with that comes a Base Herd Conversion rate, which determines how many of your Herd get turned into Horde Riders when you raise your armies. And additionally a define to control how much Gold income a Character gets based on their Herd.  

Every month, your Herd will increase based on the Herd Gain from your domain as well as contributions from Vassals and Tributaries. The Herd you gain from your Domain is equal to the current County Fertility of that County multiplied by the define HERD_GAIN_FROM_COUNTY_MULTIPLIER  

![image_26.png](https://forumcontent.paradoxplaza.com/public/1271130/image_26.png "image_26.png")


*[Herd Gain from County Fertility Multiplier Define]*  

### Raid Intents​

With raid intents we’re adding some customizability to raiding. It can change what you receive when you return with loot, and modify the raiding army in some way.  

![image_27.png](https://forumcontent.paradoxplaza.com/public/1271131/image_27.png "image_27.png")



Here we see the raze intent which will add prestige and dread when your raiding army returns with loot, but gives a -60% modifier to raiding speed.  
We also use the “on_raid_action_completion” on-action to have different effects happen after each successful raid on a holding depending on the active raid intent of the raiding army. You can check a scoped army’s raid intent using “raid_intent = NAME_OF_INTENT” trigger.  

### Generated Character Templates​

It is now possible to specify a scripted character template per Government Type. This template will be used when a new character is automatically generated for that government type in code, for example, when granting a title to an automatically generated character.  

![image_28.png](https://forumcontent.paradoxplaza.com/public/1271132/image_28.png "image_28.png")


*[Script syntax for specifying a generated character template]*  

![image_29.png](https://forumcontent.paradoxplaza.com/public/1271133/image_29.png "image_29.png")


*[Scripted character template for a Herder]*  

We use this pretty frequently in the Steppe when you start Migration and leave behind your lands to Herders. So whenever you begin migrating, the Herders that appear to oversee your previous Domain are generated according to the template above.  

The aim here is to give script and modders more control over the characters that are created for titles that already have government types specified.  

### Skeleton Update​

With this release comes an updated skeleton for the characters. We’ve added new sleeve, skirt, and cloak joints, to help increase the animation fidelity for clothing. The adding of joints to the male_body.mesh and female_body.mesh also means that any item modders may have created that uses these skeletons will have to have those joints added, or the item will look very weird (sort of “exploding”), as the joint count array now places joints in a different order and has a larger amount of them. To help modders out, we’ve decided to publish our skeleton files, both our own Maya files as well as in the more universal FBX format. You can find these files [over here](https://forum.paradoxplaza.com/forum/threads/important-update-for-clothing-mods.1726533/).  

To expedite fixing old clothes, cloaks, and legwear, modders can use these files to copy over the skinning from the various types of clothes in the files to their own items. Some manual reskinning is generally necessary, but hopefully this should make it much faster than doing it all manually. In general, legwear (pants) get the skinweights copied from the regular body (skinned to the legs), cloaks have a specific cloak item in the files to copy from (skinned to the cloak joints as well as the upper arms/neck/upper back), and regular clothes can copy from a “body and skirt” item (skinning the upper body to the body's joints, and the lower body to the skirt joints). Pick whatever item seems to suit the one needing reskinning.  

Our previously made clothing should look and act pretty much the same as before, while new animations and clothes will be able to have more movement independent of the body. This will allow us to simulate better movement based on weird poses or fast movement.  

### Combat​

For the combat-loving modders out there, we have added some commonly requested on-actions you can use to apply effects when combat starts, or when an army joins a combat.  

![image_30.png](https://forumcontent.paradoxplaza.com/public/1271134/image_30.png "image_30.png")



Additionally we have added some new script effects which will allow more control over combat outcomes:  


- **set_winner** = yes - effect you can apply to a combat side to force a winner in combat without reducing soldiers to 0. (on the next tick, more clean)
- **force_win** = yes - effect you can apply to a combat side to force a winner in combat without reducing soldiers to 0. (instantly)
- **set_disallowed_retreat** = yes - effect to disallow retreat on a combat side (they will wipe on defeat)
- **set_allow_early_retreat** = yes - effect to allow retreat when battle just started (prevents wipes)
- **set_skip_pursuit** = yes - effect to skip the pursuit phase after a combat win (so soft casualties are not converted to hard casualties)

We have also added a new ‘defeated’ map military unit animation state, which is set when a unit is defeated after combat, allowing for some cool extra animations.  


---

That's all for now! We'll be back next week to talk about some of the art and music coming in *Khans of the Steppe*, so be sure to check that out next Tuesday.

<!-- artifact:reactions:start -->
- 62 Like
- 17 (unlabeled — rendered as base64 data URI)
- 14 Love
- 4 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [PDX-Trinexx](https://forum.paradoxplaza.com/forum/members/pdx-trinexx.1654099/)**
Role: Community Manager
Badges: 102
Messages: 642
Reaction score: 17,753
<!-- artifact:op_signature:end -->
