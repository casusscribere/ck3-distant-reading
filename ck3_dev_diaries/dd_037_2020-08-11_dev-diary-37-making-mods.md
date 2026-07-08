---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1410656/"
forum_thread_id: 1410656
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 37
title: "CK3 Dev Diary #37 - Making Mods"
dd_date: 2020-08-11
author_handle: blackninja9939
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3239
inline_image_count: 8
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1410656'
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
  - type: thread_metadata
    location: raw_lines_150_to_152
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_399_to_403
    action: preserved_and_flagged
    counts:
      Like: 76
      Love: 49
      (unlabeled — rendered as base64 data URI): 4
      Haha: 2
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_411_to_487
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_488_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #37 - Making Mods

<!-- artifact:thread_metadata:start -->
- Thread starter [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)
- Start date [Aug 11, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-37-making-mods.1410656/)
<!-- artifact:thread_metadata:end -->

Hello everyone and welcome to the 37th CK3 Dev Diary!  

I’m Matthew, one of the Programmers on the CK3 team, and today I am going to talk to you about the modding in Crusader Kings III!  

Mods are something very important to the team and something especially close to my heart. I got started at Paradox as a Content Designer due to my modding work on Crusader Kings II, so being able to make sure the sequel has lots of modding opportunities and trying to give back to the community that aided me in getting into this industry is something I am very passionate about, and I know others on the team had similar starts in modding as well.  

We’ve aimed to make the game a lot more open in terms of what can be achieved in modding: we’ve got over 80 database object folders (some even with sub-folders), a very versatile event system structure, a GUI system that can be fully changed, history files, localization, sound, music, and more! So huge parts of the game can be changed to suit your needs!  

![common_folder.png](https://forumcontent.paradoxplaza.com/public/594848/common_folder.png "common_folder.png")


[screenshot of common database folders]  

In the rest of this diary I’ll talk less about what you can do overall and more spotlight some things I think modders of CK2 will be excited about, as otherwise this diary would be huge and I need to get back to coding at some point.  

At its core our scripting language in Imperator and Crusader Kings III is based on an in-house grand strategy library called Jomini, which acts as a more GSG focused layer used on top of our Clausewitz engine.  

When Imperator released I posted a lot of information about the things that come directly from Jomini and which are shared between both games, so I would recommend checking out my [Grand Jomini Modding Information Manuscript](https://forum.paradoxplaza.com/forum/threads/grand-jomini-modding-information-manuscript.1170261/.) thread if you are an interested modder.  

If you’d like to know more about event scripting then [Dev Diary 30](https://forum.paradoxplaza.com/forum/threads/crusader-kings-3-dev-diary-30-event-scripting.1397140/) had a very good coverage of that which you should check out!  

Feel free to ask questions about both the linked threads in this one as well!  

**Character Interactions**  
To focus more on game level things, one of the biggest things changed from CK2 is the character interactions.  

For a brief history lesson in CK2 modding, most of these core interactions were hardcoded, things like arranging marriages, declaring war, alliances etc. It was only after quite a few patches that the ability to add custom “targeted decisions” was introduced, and it’s worth noting that it was only the ability to add or modify those targeted decisions - the older hardcoded core interactions were still not particularly moddable.  

For CK3 we wanted to open all of that up to go through one unified character interaction system, so every action goes through our script system now. This gives many benefits: with script being able to change it we can now change weights for the AI’s use of these actions with just a few text file changes instead of needing code time, we can change who can do them, and what people are considered good matches etc. And of course that opens it all up for modders as well.  

The AI can also be scripted to use all of these custom interactions, tell them who’s a good target, as well as how often they should evaluate it (which is important for performance).  

There are still some hard coded links with the interactions, specifically when it’s an interaction that’s needed to be used by the AI in a non-trivial manner. These interactions are all marked clearly, though, and if you attempt to remove them then the game will give you a warning when loading that it really needs this interaction so put it back please. This behaviour in fact applies to almost all hard coded database objects, not just those which are interactions.  

For reference here is a full list of all the options interactions can use that impact how they are taken, received, responded to, shown graphically and used by the AI:  


Spoiler

my_interaction = {  
interface_priority = number # Used by interaction menu  
common_interaction = yes/no # Used by interaction menu  
category = interaction_category_hostile # Used by interaction menu  
is_highlighted = trigger # Should the interaction be highlighted in the menu  
highlighted_reason = loc_key # Tooltip if highlighted in menu  
on_decline_summary = dynamic description # Flavor text that is shown under acceptance widget. Use it when you need to draw more attention to the on decline effect  
special_interaction = type # This interaction uses specialized GUI  
special_ai_interaction = type # This interaction runs specialized code that identifies the interaction by this  
interface = call_ally/marriage/grant_titles/etc. # What interface does the interaction use?  
scheme = elope/murder/etc. # The type of scheme the interaction starts  
popup_on_receive = yes # Have the interaction pop-up for the recipient when received  
force_notification = yes/no # Force diplomatic item if interaction is auto-accept  
pause_on_receive = yes/no # Pause the game on receive. It usually makes sense to combine it with popup_on_receive  
ai_accept_negotiation = yes/no # If the interaction is declined negotiations will start. We don't show "won't accept", etc. because there is still a possibility that the interaction will be accepted via negotiation event chain  
hidden = yes # Is the interaction hidden?  
use_diplomatic_range = yes/no/trigger # Does this interaction check diplomatic range? Yes by default  
can_send_despite_rejection = yes # Interaction can be sent and the ai might reject  
ignores_pending_interaction_block = yes # If the actor is a player and the recipient already has received an interaction from them pending a response, can this interaction be sent anyway. Defaults to no  
send_name = loc_key # The name of the interaction in context of it being seen once sent. Defaults to database object key  
needs_recipient_to_open = yes # Does the interaction need a recipient set to be able to be allowed to open and be shown. Defaults to no  
show_answer_notification = no # Does this show a response info pop up when an interaction is answered if the actor is a player. Defaults to yes  
show_effects_in_notification = no # Should the effects of the interaction be shown in the notification window when an interaction is sent. Defaults to yes  

icon = texture_path # Icon used in various places. Default is gfx/interface/icons/character_interactions/my_interaction.dds  
alert_icon = texture_path # Default is gfx/interface/icons/character_interactions/my_interaction_alert.dds  
icon_small = texture_path # Default is gfx/interface/icons/character_interactions/my_interaction_small.dds  
should_use_extra_icon = { always = yes } # When to show an extra icon. Tooltip key is <key>_extra_icon  
extra_icon = "gfx/<...>/hook_icon.dds" # Icon to show when should_use_extra_icon is true  

target_type = type # Possible types: title, none (default)  
target_filter = type # See FAQ for possible types  

ai_maybe = yes # The ai can reply maybe  
ai_min_reply_days = 4 # Minimum days before ai replies  
ai_max_reply_days = 9 # Maximum days before ai replies  

desc = loc_key # Short description of the interaction  
greeting = negative/positive # Sets tone in request text  
notification_text = loc_key # Request text  
prompt = loc_key # What text should be shown under the portrait? (For example: "Pick a Guardian")  

show_effects_in_notification = yes/no # Should the effects be shown in the notification?  

cooldown = { years = x } # How long until the decision can be taken again?  
cooldown_against_recipient = { years = x } # How long until the decision can be taken against recipient again?  

is_shown = trigger # Is the interaction available and visible between scope:actor and scope:recipient  
is_valid_showing_failures_only = trigger # Is the interaction valid to be selected in it's current setup, trigger only displays failures  
is_valid = trigger # Is the interaction valid to be selected in it's current setup  
has_valid_target_showing_failures_only = trigger # TODO  
has_valid_target = trigger # TODO  
can_be_picked = trigger # TODO  
can_be_picked_title = trigger # TODO  
auto_accept = yes/no/trigger # Is the interaction automatically accepted, or can recipient decide  
can_send = trigger # Can the interaction be sent  
can_be_blocked = trigger # Can the interaction be blocked by the recipient (i.e. by a hook on the actor)  
is_highlighted = trigger # Should the interaction be highlighted in the menu  
can_send = trigger # Can the interaction be sent?  

redirect = {} # This changes the redirection of characters using the scopes actor, recipient, secondary_actor and secondary_recipient  
populate_actor_list = {} # Everyone sorted into the list 'characters' has the potential of being shown to be selected. Uses the scopes actor, recipient, secondary_actor and secondary_recipient.  
populate_recipient_list = {}  

localization_values = = {} # To be able to use values in loc (for example: RANSOM_COST = scope:secondary_recipient.ransom_cost_value lets you use $RANSOM_COST|0$ in loc)  

options_heading = loc_key # Text shown above options block - describes all options in general  
send_option = { # Adds an option  
is_shown = trigger # Is option shown  
is_valid = trigger # Is option selectable  
current_description = desc # Tooltip  
flag = flag_name # If selected then scope:flag_name will be set to yes  
localization = loc_key # Loc_key for option label  
starts_enabled = trigger # Trigger for whether this should be on when the window opens. If not defined, defaults to off  
can_be_changed = trigger # Trigger for whether this option can be changed from its default  
can_invalidate_interaction = bool # If yes then when the AI picks an interaction it will do the full can send this entire interaction check instead of the more performance saving checking of recipient refusal and ai will do, use with care and profile it  
}  
# Options should avoid preventing an interaction from sending (except by the recipient refusing), as we assume that to be the case in the AI for performance reasons, use can_invalidate_interaction if you need it to be re-checked  
send_options_exclusive = yes/no # Are the options exclusive?  

on_send = effect # Executes directly the interaction is sent  
on_accept = effect # Executes when accepted by recipient  
on_decline = effect # Executes when declined by recipient  
on_blocked_effect = effect # Executes when blocked by recipient  
pre_auto_accept = effect # Only executes if the interaction was auto accepted. Done before any other side effect (E.G., hard coded ones like marriage)  
on_auto_accept = effect # Only executes if the interaction was auto accepted  

reply_item_key = loc_key # The key to the loc to show in the interaction item tooltip. Receives the name of the interaction in $INTERACTION$. Default value "INTERACTION_REPLY_ITEM"  

# These loc keys are shown to the player when sending the interaction. The meaning is what is going to be the answer from the target.  
pre_answer_yes_key = loc_key # The key to the loc when the interaction is going to be accepted. Default value "ANSWER_YES"  
pre_answer_no_key = loc_key # The key to the loc when the interaction is NOT going to be accepted. Default value "ANSWER_NO"  
pre_answer_maybe_key = loc_key # The key to the loc when the interaction maybe is accepted. Receives the acceptance value in $VALUE$. Default value "ANSWER_MAYBE"  
pre_answer_maybe_breakdown_key = loc_key # The key used to localize the chance of acceptance of an interaction with provided chance value. Defaults to ANSWER_SUM_MAYBE  

# These loc keys are shown to the player when answering an interaction.  
answer_block_key = loc_key # The key to the loc to block the interaction. Default value "ANSWER_BLOCK"  
answer_accept_key = loc_key # The key to the loc to accept the interaction. Default value "ANSWER_YES"  
answer_reject_key = loc_key # The key to the loc to reject the interaction. Default value "ANSWER_NO"  
answer_acknowledge_key = loc_key # The key to the loc to reject the interaction. Default value "ANSWER_ACKNOWLEDGE"  

cost = { # Scripted cost for the interaction. The interaction will be disabled if the actor can't pay up, and the cost will be subtracted from the actor when the interaction is sent. Renown can only be spent by the dynast.  
piety = {}  
prestige = {}  
gold = {}  
renown = {}  
}  

ai_set_target = {} # Set scope:target to make the AI target something specific. Title targeting interactions don't need this  
ai_targets = {  
ai_recipients = type # Which characters does the ai consider as recipient for the interaction, can be scripted multiple times to combine lists  
# Available lists are in the "ai_targets" section of this file (trying to add an invalid list will trigger an error message with all available )  
chance = 0-1 # A low chance, such as 0.25, randomly excludes that number of characters from being checked - this is useful for saving performance  
}  
ai_target_quick_trigger = { # Quick triggers for the ai_targets  
adult = yes # The target needs to be adult  
attracted_to_owner = yes # The target needs to be attracted to owner  
owner_attracted = yes # Owner needs to be attracted to the target  
prison = yes # Target must be in prison  
}  

ai_frequency = months # How often should the ai consider doing this interaction  
ai_potential = trigger # Will the ai consider trying this interaction  
ai_accept = mtth # Will the ai accept a request for this interaction  
ai_will_do = mtth # How interested is the ai in sending this interaction (tested after selecting targets) 0-100 percent chance, will be clamped.  
# Note that for title interactions, each individual target title will get evaluated, and the one giving the highest ai_will_do will get used. If the interaction has options, the combination of options that gives the highest ai_will_do will be used.  
}


**Combining Mods**  
Combining multiple mods together has always been a bit tricky but I wanted to try and make some gains with compatibility so that it doesn’t require as many manual patches.  

To aid in this a bit I’ve made it so database entries can be overridden by key even if that new entry is in a different file. This means if you want to override what the lunatic trait does then instead of needing to copy the entire traits file just to change one entry you can just make your own file just containing your new definition of what the lunatic trait does, such as giving it a boost in learning, prowess, and attraction opinion like I have done below!  

![lunatic_override.png](https://forumcontent.paradoxplaza.com/public/594849/lunatic_override.png "lunatic_override.png")


[screenshot of a file overriding the lunatic trait]  

![lunatic_override_in_game.png](https://forumcontent.paradoxplaza.com/public/594850/lunatic_override_in_game.png "lunatic_override_in_game.png")


[screenshot of the new lunatic trait]  

This also applies to files from other mods, as long as yours is loaded first, so you can overwrite traits and other database elements from other mods  

Currently we do not support appending to a definition instead of fully overwriting, as we’d need to rework a good chunk of things and test it extensively though it is something I am keeping in mind for the future.  

**Alerts, Issues and Notifications**  
As I mentioned in [Dev Diary 16](https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-16-tutorials-and-tooltips-and-encyclopedias-oh-my.1345581/), all of the new interface utilities we have for explaining the game are moddable. Which means you can add, remove, and modify any of these things through script instead of them being hard coded like in CK2.  

I’ll start with the notifications and toasts as they are the simplest. You simply make a database entry in the common folder for your notification and then wherever you want to run it from you use the send_interface_message or send_interface_toast effect.  

Those effects take the type of message as well as optional overrides for the title and text instead of using what was scripted in the database. They can also take any number of effects to run which will then be included as text when displayed, though it is often recommended to use a custom tooltip instead of bloating the message with a lot of mechanical text.  

For alerts, advice and current issues they all go through the same “important actions” system, the core difference between them is which type they are specified to use which controls their visual appearance and location.  

These important actions have a check_create_action and effect block, both run interface effects (specially marked effects that do not modify the game state across MP but just local UI things) to see if they can be created and what to do when clicked.  

The main interface effect to run in check_create_action will be the try_create_important_action which attempts to create a UI element for this action type and this will usually be behind an if check.  

In the effect block for when the UI element is clicked there are a couple of things which are a good idea to run, if its a piece of reactive advice then using the start_tutorial_lesson is a great idea, and for alerts or issues then the open_view_data effect is the way to go to open the window that can help address whatever is causing the alert or issue!  

![custom_alert.png](https://forumcontent.paradoxplaza.com/public/594851/custom_alert.png "custom_alert.png")


[a custom alert]  

*Note: Whilst making this dev diary I actually found out that in 1.0 adding a custom icon like you see via a mod is actually not functional, it's already been fixed for 1.1 but I thought I should note that here quickly for people coming back to this dev diary to tell me off when it doesn’t work right away.*  

The suggestions are similar to the important actions, but also have fields for the weight which checks how important the suggestion is to the player and a score which checks which potential target of a suggestion is best.  

For example, in the fabricate claim suggestion the weight is based on if there is anything nearby you could fabricate on, how many claims you already have, and if you are already fabricating a claim. The score for which title to suggest you fabricate is based on a much larger list of values such as the development level of the county, how easy it’ll probably be to conquer, if you share a faith or culture, etc.  

**Scripted GUIs**  
Like with Imperator the interface is incredibly moddable, the GUI scripting language whilst different from the normal database and event script is still very versatile and lets you change both the appearance and positioning and full functionality of almost all the GUI elements in the game. We also have a GUI debug mode in game which allows viewing through the hierarchy and opening to the file and line of where elements are defined which makes working with the interface a lot easier.  

Currently we do not support creating your own new windows GUIs (though it is on my never ending to do list), but the easy work around there is just to make them as children of the main HUD window, which is always shown, and then you can have anything.  

As is listed briefly in the Jomini Modding info I linked it is possible to make scripted GUIs, which allow a link to exist between the GUI system to the normal script system so you can test for if different triggers evaluate true or false and to run effects in the game state safely across multiplayer.  

I am very excited to see what people end up doing with this especially, there should hopefully be a massive reduction in the number of hacks needed to display information now that real interfaces can be made for mods to show things about their unique mechanics.  

Here is a very small example of a custom interface I put together to give you a little button you can press for “fun” aka for murder against another adult character of a different faith.  

![murder_button.PNG](https://forumcontent.paradoxplaza.com/public/594858/murder_button.PNG "murder_button.PNG")


![murder_confirmation.PNG](https://forumcontent.paradoxplaza.com/public/594860/murder_confirmation.PNG "murder_confirmation.PNG")


[screenshot of a custom interface button and its confirmation pop up]  

![murder_script.PNG](https://forumcontent.paradoxplaza.com/public/594859/murder_script.PNG "murder_script.PNG")


![murder_gui.PNG](https://forumcontent.paradoxplaza.com/public/594861/murder_gui.PNG "murder_gui.PNG")


[screenshot of the script and gui entry for the button]  


Thanks for tuning in folks! I know this diary might have some more niche appeal, for those of you looking for a look at more gameplay then make sure to tune in for our next gameplay stream!

<!-- artifact:reactions:start -->
- 76 Like
- 49 Love
- 31 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 2 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [blackninja9939](https://forum.paradoxplaza.com/forum/members/blackninja9939.795679/)**
Role: Former Senior Programmer - Crusader Kings 3
Badges: 99
Reaction score: 8,575

*[Full game-badge icon list of 16 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
