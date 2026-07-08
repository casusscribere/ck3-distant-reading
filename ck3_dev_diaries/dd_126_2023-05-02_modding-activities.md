---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1580680/"
forum_thread_id: 1580680
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 126
title: "Dev Diary #126 - Modding Activities"
dd_date: 2023-05-02
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
body_word_count: 2853
inline_image_count: 14
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1580680'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2324.jpg?1683026606
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_142_to_144
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_423_to_426
    action: preserved_and_flagged
    counts:
      Like: 39
      Love: 26
      (unlabeled — rendered as base64 data URI): 5
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_434_to_531
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_532_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2324.jpg?1683026606)
<!-- artifact:thread_banner:end -->

# Dev Diary #126 - Modding Activities

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [May 2, 2023](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-126-modding-activities.1580680/)
<!-- artifact:thread_metadata:end -->

Hello and welcome to the 126th CK3 Dev Diary. I’m Matthew, one of the programmers on the team, and today we’re going to be covering changes to modding support coming alongside Tours and Tournaments as well as how modding activities themselves can work.  

### Activity Modding​

Activities are fully moddable, and as I mentioned in prior dev diaries they are composed of a variety of options and phases, where a phase is made up of a type and a location.  

There are a lot of scripting options in activities so I’m going to also attach our info file on them for a more detailed overview. For this dev diary I’m just going to cover a handful of the bigger things.  


#### Options​

Options are one of the more simple things, they are grouped into categories with different options which can be shown and picked, and it is scripted which is default. This default picking is a trigger so that different defaults can be set for different people; in vanilla we use this to make Hajj the default for Muslims, so they go on that first.  


![01 - activity options.PNG](https://forumcontent.paradoxplaza.com/public/962705/01 - activity options.PNG "01 - activity options.PNG")



Additionally, every option can forcefully add characters to the entourage of the host and invited guests, it will pick from their court characters and allows a weight for selecting them and a maximum to pick from for player and AI.  
These invited characters also get an invite order, which I’ll cover in more depth shortly.  


![02 - entourage.PNG](https://forumcontent.paradoxplaza.com/public/962706/02 - entourage.PNG "02 - entourage.PNG")



Lastly one option category can be set as the “special” category, this option will be picked first when planning an activity. In vanilla we use this for the special activity types like which type of Tour you are going on. It is fed into many triggers and scripted values in the activity setup for checking.  


#### Phases​

Setting up phases can be quite complicated, mainly centering around how the location of them should be picked.  

You can think of there being two types of phases: Predefined and Pickable.  

Predefined phases are always present and not removable, they can be selected either by the script picking a location or automatically set to the first or last phase.  

For example, in a Tour the final phase is “Journey Home” is predefined and has a scripted selection of always taking you to your capital province, so you return home.  


![03 - phases.PNG](https://forumcontent.paradoxplaza.com/public/962707/03 - phases.PNG "03 - phases.PNG")



For pickable phases the player instead selects a province themselves, phases can be repeatedly picked and have a max limit so you cannot go on a Tour to visit every vassal.  

Every phase also has an order in which it happens, for a simple activity like a feast where all phases are predefined this just controls the order they happen. In more complicated activities where the player can pick things the order becomes more complicated, it will respect the order you script but also if the order is matching it will be the last one the player picked.  

To take Tours as an example again in the above image you can see order is set to 2, and for the pickable phases where you visit different vassals the order is set to 1.  
So that means the Journey Home is always at the very end of everything, and for the vassal stops whichever you the player picked last will be towards the end of your journey.  

#### Special Guests​

Special guests can be selected in two ways, either a trigger which you then pick from all invited characters who match it, or they can be automatically filled by an effect. This allows weddings to automatically set the bride and groom whereas in a feast you can pick your honorary guest.  


![04 - special guest.PNG](https://forumcontent.paradoxplaza.com/public/962708/04 - special guest.PNG "04 - special guest.PNG")


![05 - special guest trigger.PNG](https://forumcontent.paradoxplaza.com/public/962709/05 - special guest trigger.PNG "05 - special guest trigger.PNG")


Additionally, as you may have spotted special guests can be required or not, if required then the activity will not be plannable without them and if they decline then it will be invalidated.  


#### ​

#### Invite Rules​

Every activity has multiple invite rules which control who can be invited, these rules are reusable and can be shared among different activities and are defined in their own files.  

On its own an invite rule is just an effect which adds character to a list, how you get those characters from the host is up to you really.  


![06 - invite rules.PNG](https://forumcontent.paradoxplaza.com/public/962710/06 - invite rules.PNG "06 - invite rules.PNG")



When an activity decides to use those invite rules it can decide if the rule should be enabled by default and more importantly what order the invite rule should be applied. This comes into play when the invite rules are adding more characters than your activity can support, it will try to invite characters based on the order and later less important characters will be skipped.  


![07 - invite order.PNG](https://forumcontent.paradoxplaza.com/public/962711/07 - invite order.PNG "07 - invite order.PNG")



Special guests are always invited first since the activity to some degree revolves around them. Equally those you manually invite via interaction will be put to the front of the invite list.  

#### Intents​

Like invite rules our intents are defined in their own files and can be reused by different activities. The default intent for hosts and guests is defined per activity, the player and AI will pick their own specific one from there.  

Every intent can optionally have a target character and they are scripted similarly to interaction targets. One thing to keep in mind when modding intents is the AI target usage; since every invited character is a target, you should make liberal use of the AI target filtering we provide and put maximus on potentially very large groups of people.  


![08 - intents.PNG](https://forumcontent.paradoxplaza.com/public/962712/08 - intents.PNG "08 - intents.PNG")



#### Plugin Widgets​

Due to the nature of activities wanting to display special information, and in the case of Tournaments basically showing its entire own window, we came up with a system of allowing the activity script to define what plugin widgets it would like inserted into the main window.  


![09 - plugin widgets.PNG](https://forumcontent.paradoxplaza.com/public/962714/09 - plugin widgets.PNG "09 - plugin widgets.PNG")



The format of these is that the left-hand side refers to the name of the plugin widget and the name of the file it will be in, similar to the event window widgets, all of which are found under the gui/activity_window_widgets directory.  

The right-hand side refers to the name of the widget in the main activity window they should be inserted under. We’ve got a few that we use already in vanilla but mods can expand and add more places they insert widgets and use custom widgets for their own activity information.  

### Leveled Traits​

As shown off in some earlier dev diaries we now have leveled traits built into the game instead of needing to be handled purely in script.  

Script wise they are very simple; any trait can define one or more tracks and what XP thresholds needs to be met for modifiers to apply. The modifiers are stacking so you always get the rewards of previous levels on top of them.  

Any trait can be made into a leveled trait, for now we’ve done it to lifestyle traits where you can level them up. But we may apply this in the future to other things!  


![10 - trait tracks.PNG](https://forumcontent.paradoxplaza.com/public/962715/10 - trait tracks.PNG "10 - trait tracks.PNG")



Currently unused in vanilla, we’ve also added it so the trait XP can degrade over time which I am sure mods will be able to put to good use. The below will make the XP degrade by 5 every month, but only to a minimum of 20 so you don’t lose all your hard-earned XP.  


![11 - trait degredation.PNG](https://forumcontent.paradoxplaza.com/public/962716/11 - trait degredation.PNG "11 - trait degredation.PNG")



Alongside this rework we also went through and added more documentation to traits and combined some properties that could never coexist and now give better errors.  

### Database Scopes​

One larger rework that will be a work in progress over the next few patches is that now database types can be registered as scope types.  

I’ve reworked our backend to support this better now and still keep things safe, mainly by disallowing effects to be run on these database scopes since they are not modifiable. So now for example traits and activity types are scopes which can be saved and used in script.  

Currently the support is mostly in its bare minimum state, but in future patches I plan to make a variety of database types into scopes. This should hopefully improve mod compatibility and reduce down script duplication of manually checking over every single trait by hand.  

Coming in the next release after Tours and Tournaments I’ve made traits fully integrated into this for both triggers and effects, so you could look for a random opposite trait of someone and then add it to your character for example.  

For Tours and Tournaments, we’ve mostly used this in the activity system to support alerts better, so instead of having a hard coded alert about activities you can host we can just check them like normal script.  


![12 - database scopes.PNG](https://forumcontent.paradoxplaza.com/public/962717/12 - database scopes.PNG "12 - database scopes.PNG")



So modders reading this: I’d love to know what types you’d like added as scopes and what triggers and effects that take database keys you’d like to see take scopes. I’ve already got traits done for a future patch, so I am interested in others I can do!  

### Data Models​

I’ve reworked the backend of how data models work, which now allows us to in gui script dynamically get sub-sections of a datamodel as well as set a datacontext to a specific item in the data model.  

For example, you can now limit a datamodel to the first three people:  


Code:

```
datamodel = "[DataModelFirst( ActivityWindow.GetCharacters, '(int32)3' )]"
```


Or you can get the skip the first few of them:  


Code:

```
datamodel = "[DataModelSkipFirst( ActivityWindow.GetCharacters, '(int32)3' )]"
```


There also exists a “Last” version of these which gets/skips the end and DataModelSubSpan which lets you do both an offset and desired size.  

Using datacontext_from_model you can also get a specific item, oftentimes this will be the very first one so you can show the top scoring character, or first completed intent etc.  


![13 - datacontext model.PNG](https://forumcontent.paradoxplaza.com/public/962718/13 - datacontext model.PNG "13 - datacontext model.PNG")



The index can also be dynamic so you can save a value in script and then get that character out of your data model.  

### Conditional Scope Change​

As some of you eagle eyed people might have spotted, or if you’ve modded Vicky and see they released with our change first, is the new conditional scope change operator ?=.  

Normally when you change to a scope you will get errors if it does not exist, but in many cases you know that the thing may not be set in which case you don’t want an error but to fail the trigger.  
The previous way of doing that is to add an exists trigger on the line above every time as that then returns false if they are not around, but that could be quite cumbersome.  

Now you can combine that together so instead of loads of extra typing it's just one convenient ? being involved!  


![14 - conditional scope change.PNG](https://forumcontent.paradoxplaza.com/public/962719/14 - conditional scope change.PNG "14 - conditional scope change.PNG")



This also works for scope comparisons where it will return false if the left-hand side does not exist. When used in effects it will just skip running the effects in that scope change if the scope doesn’t exist.  

And lastly as a little sneak peek of the patch notes here is the user modding section!  

Spoiler

###################  
# User Modding  
###################  
- Added character modifier, Men-at-arms Counter Resistance  
- Rename hidden_effect_new_artifact to hidden_effect_new_object  
- Add GetBaronyNameExplicitly and GetBaronyNameExplicitlyNoTooltip to provinces to get the barony even if it's the capital.  
- Add building_slot_add modifier for holdings.  
- Add prowess_no_portrait trigger.  
- Add trait modifiers based on faith doctrine parameters, analogous to culture  
- Added defines for simple text glow formats  
- Adds the hostile_county_attrition_raiding to modify the hostile county attrition of raiding armies. Will apply from both commanders and owners of armies. This IGNORES the regular lower limit of 10%, such that hostile county attrition for raiding armies can be reduced to 0. Go forth, land vikings! Pillage! Rule!  
- Adds the movement_speed_land_raiding to modify the speed of raiding armies moving over land. Will apply from both commanders and owners of armies.  
- Consistently use reference for triggered background/textures instead of sometimes duplicating with event_background.  
- Custom loc can now have the "all" type which lets it match to any scope type.  
- Interactions can now also set a cooldown on all other interactions in the same category via the 'category_cooldown' and 'category_cooldown_against_recipient' properties  
- Make province GetName and GetNameNoTooltip both return the county if capital.  
- Remove 'goto' field from 'send_interface_message' and 'send_interface_toast'  
- Remove GUI support for 'PlayerMessageItem' members 'GetGotoProvince', 'HasGotoProvince', and 'OnGoto'  
- Remove the add_building_slot effect, only use the new building_slot_add modifier.  
- Rework how open_view and open_view_data handle additional script provided data, the view_message field has been renamed to data and can be used in either of those effects it will now pass the additional data to the specific interface it is opening which will use it as appropriate.  
- The 'duel' script effect can now use multiple skills at once, averaging their value. Up to six skills can be compared.  
- Add diarchy_succession_character script list builder  
- Add effect change_diarchy_type  
- Add effect set_diarch  
- add trigger is_diarchy_successor  
- Per modder request, added some instructions (and a small correction) to on_actions.info to help newbie modders just getting started  
- Per modder request, added standardised cultural parameters for raiding overland and overseas to increase mod interoperability. Also made it easier to add dynasty modifiers, house modifiers, & cultural innovations that unlock raiding (either according to standard restrictions for non-tribals or, optionally, without restrictions)  
- Per modder request, replaced almost all instances of has_government with government_has_flag (and added relevant flags to each government type) to allow for easy hooking in of additional government types to vanilla content & systems, as well as better mod interoperability  
- Add function [Army.GetArmyStatusTooltip]  
- Introduce [Army.GetArmyStatusOutlinerIcon]  
- Renamed [Army.GetArmyStatusIcon] to [Army.GetArmyStatusIllustration].  
- add change_diarchy_power_level effect  
- add diarchy_has_parameter trigger  
- add diarchy_power_level trigger  
- add set_diarchy_power_level effect  
- Converted tribal imprisonment block to use a government flag for marginally higher mod compatibility  
- Added 'memory_creation_date', 'memory_end_date' and 'memory_age_years' triggers for Character Memories.  
- Add HasCharacterFlag datafunction for characters  
- Added IsDateAfter promote that takes a date and a target date.  
- Added IsDateBefore promote that takes a date and a target date.  
- Added IsDateBetween promote that takes a target date, a start time and an end time.  
- Added IsDateToday promote that takes a date.  
- Added GetDateAsTotalDays promote for Dates  
- Added promote HasFlag to the (Player) MessageType in order to allow specializations for message appearances.  
- Added effect start_travel_plan, which opens the travel planning window for the player and can take multiple (optional) input parameters like destination(s), companion(s), events/on_actions, et al.  
- New `*_neighboring_province` list can be used to efficiently get adjacent provinces in script  
- New `*_army_in_location` list can be used to quickly find armies in a province  
- The "Settings" window doesn't pop up anymore when reloading localization data  
- New expand auto-complete mode for console: Toggle via `settings` -> Tools -> Console auto-complete mode  
- Can kick out existing councillor "nicely" by using `remove_existing_councillor = yes` in `assign_councillor_type` effect  
- Interactions targetting artifacts can now directly open up a specific artifact  
- You can now actually generate a 'lowborn' character from character templates (`dynasty = none` is now correctly honored)  
- The PdxData data_binding 'macro' system now supported for mods too  
- You can attach character portrait assets to the root of a 3D entities via `at_root_of_entity` (same config location as `shared_pose_entity` / `node`)  
- New 'scope exists' script operator "?=" added, so we don't have to write "exist = bla bla = { stuff }" thousands of times and can just do “bla ?= { stuff }”  
- Scope exists operator `bla ?= {}` in effects will not execute effects inside scope if the scope `bla` does not exist  
- Added new 'ransomed' artifact history state  
- `set_location` effect now has `stick_to_location = yes` if you want to pin down someone’s default location to be different from their capital or court

 

#### Attachments

- [/forum/attachments/toto-modding-zip.975211/](https://forum.paradoxplaza.com/forum/attachments/toto-modding-zip.975211/)
  
  ToTo Modding.zip
  102,1 KB

 · Views: 0

<!-- artifact:reactions:start -->
- 39 Like
- 26 Love
- 18 (unlabeled — rendered as base64 data URI)
- 5 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)**
Role: Former Senior Programmer - Crusader Kings 3
Badges: 99
Reaction score: 8,575

*[Full game-badge icon list of 44 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
