---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1397140/"
forum_thread_id: 1397140
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 30
title: "Crusader Kings 3 Dev Diary #30 - Event Scripting"
dd_date: 2020-06-09
author_handle: Wokeg
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2734
inline_image_count: 12
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1397140'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1400.jpg?1591705865
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_317_to_321
    action: preserved_and_flagged
    counts:
      Like: 60
      Love: 33
      (unlabeled — rendered as base64 data URI): 1
      Haha: 1
    note: Reactions block parsed; 3 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_329_to_434
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_435_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/1/1400.jpg?1591705865)
<!-- artifact:thread_banner:end -->

# Crusader Kings 3 Dev Diary #30 - Event Scripting

<!-- artifact:thread_metadata:start -->
- Thread starter [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)
- Start date [Jun 9, 2020](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-30-event-scripting.1397140/)
<!-- artifact:thread_metadata:end -->

Welcome, comrades, to another dev diary! Today, we’ll be taking a look at the structure of an event in CK3, how they’re assembled in script, and how they differ from CK2.  

**Anatomy of an Event**  
The core of a standard character event is almost certainly quite familiar to you already: we have a title, a description, typically a portrait, and one or more options along the bottom.  

In script, however, we’ve changed a few things around, looking to improve functionality, readability, and general script hygiene over time. Here’s a comparison of the start of an event in CK2 vs. CK3:  


![001.png](https://forumcontent.paradoxplaza.com/public/574141/001.png "001.png")



The first change you’ll notice is that we’ve swapped the event type and the event ID: an event is now created by a namespace (still defined at the top of each file) and unique ID, and the type defined inside the event, rather than the inverse. This means that you can now still read event IDs after folding the events themselves!  

![002.png](https://forumcontent.paradoxplaza.com/public/574142/002.png "002.png")



Next, is that we’ve changed how triggered text works. In CK2, this was a really useful tool for ensuring that flavour was localised appropriately to the player’s situation, and let us make events very broadly applicable whilst still feeling unique. It could, however, get a bit cumbersome, since we had no method for triggered text to be easily mutually exclusive, occasionally leading to situations like this:  


![003.png](https://forumcontent.paradoxplaza.com/public/574143/003.png "003.png")



Not the worst in the world, but pretty chonky for what we actually want it to do.  

In CK3, we can cut this down by using a first_valid block inside triggered text blocks (as in the first image shown), picking the first entry from a list which meets a set of criteria. This means that, instead of having to make sure triggered text blocks are always mutually exclusive according to a trigger (and one which tends to increase in complexity along with the number of triggered texts), we can just order our preferred text logically according to fairly simple triggers.  

For instance, if I have a triggered text block where the copy is different for a French character, an Ashari character, and a character who’s over eighty years old, with a fallback for anyone who doesn’t fit into those categories, I’d script something like the following:  


![004.png](https://forumcontent.paradoxplaza.com/public/574144/004.png "004.png")



This will then automatically proceed down the list. A French character would see one thing, a non-French Ashari would see another thing, a non-French non-Ashari who’s over eighty would see a third thing, and everyone else would see a fourth. This makes it incredibly easy to add new context-sensitive copy to both event descriptions and titles.  

A further minor point, but as triggered text is now also kept within the body of a superior block, it’s far easier to sort on the fly: no matter how much triggered text you have, it’s just one click to collapse the body in your file editor of choice, not a dozen or more. When minimising clicks, every little bit helps!  

**Event Themes & Backgrounds**  
A couple of notable absences in the CK3 format are the picture & border blocks.  

Well, that’s with good reason! These have mostly been subsumed into the new event theming system, which you can see in the very first CK3 script example above.  

Themes are what decide on the event icon displayed in the top-left, helping to group together broadly-thematic sets of events, and to let the player know what they can expect an event to relate to. They also give us a default appropriate image background (which, itself, sets the lighting used on the character portraits), which will change according to your situation, and different sets of ambient SFX.  

Backgrounds and theme icons can be overridden as necessary via a manual line of script if we feel like we’ve got a more appropriate one to show, too, so although the system is set-up to reduce the amount of work that goes in to adding extra flavour to each event, we still have total control over what flavour we actually include should we want it.  

Needless to say, event themes are fully scriptable: you can mod in whatever icon, default background, character model lighting, & ambient SFX you like, as well as create and adjust themes with ease.  

**Portraits & Animations**  
The good stuff! Portraits in the new system are, very surprisingly, somewhat more dynamic than in CK2, and any given event can have between 0 and 5 total portraits present. Of these, two are fully animated (positioned to the left and the right, respectively), and three are headshots lined up evenly along the bottom of the event. These can be used in any combination you like to get *just* the right look for an event.  

![005.png](https://forumcontent.paradoxplaza.com/public/574145/005.png "005.png")



The left and right portraits can use any of a fairly wide array of animations created for release. Headshots are not animated, instead allowing you to visualise ancillary characters mentioned in the event’s description.  

**On Actions for All!**  
All events come from somewhere, and, in CK2 (especially earlier in the title’s life cycle), this was often done through the Mean Time To Happen system, which let us define roughly how long an event would take to fire in (typically) months. Unfortunately, when balancing extremely large numbers of events against each other, the flexibility of this system becomes more of a disadvantage than anything else, making it difficult to govern how frequently an event should spawn without particularly stringent triggers. It also caused a lot of weird statistical anomalies due to working off of pure probabilities, and absolutely tanked performance.  

Over CK2’s long life, we started to move more towards triggering events via on_actions, small hooks in code attached to features or regular pulses that activate events (and, if necessary, effects) whenever that hook is called. These take a bit more work to balance, but give us much more control over how and when events are called, as well as making tweaking such significantly easier, and are super fast performance-wise.  

For CK3, we use entirely on_actions to fire events. There’s quite an array hooked up from code, allowing us to trigger events either when a specific action occurs in the world (e.g., when a character is born) or on a regular pulse (e.g., every five years). These can be set to go off every time that on_action fires, or placed in a weighted list of potential events that might fire (in which case, weight multipliers still apply and support the usual factors and such).  

One major improvement over CK2’s on_actions (other than a more thorough, rationalised system of use, which I think is very exciting but I also appreciate that other people lead much more interesting lives than me and may have stricter standards) is the addition of scripted on_actions! These allow us (and, of course, you!) to create and hook up on_actions entirely in script that behave as regular on_actions, instead of always having to rely on the hard-coded on_actions. Scripted on_actions then behave exactly as coded on_actions, acting as a complex of weighted & unweighted events/effects, just called from somewhere in the accessible-script rather than the inaccessible-code.  

For instance, say I’ve made a new set of events about reconciliation after a civil war, neighbours learning to live side by side with each other after fighting for opposite lieges, that type of thing, and I want to hook it up to happen whenever a civil war ends. All I have to do to set up that flow is add something like this to the relevant war end effects:  


![006.png](https://forumcontent.paradoxplaza.com/public/574146/006.png "006.png")



And then create a file including this in the appropriate directory:  


![007.png](https://forumcontent.paradoxplaza.com/public/574147/007.png "007.png")



Anywhere that you can script an effect, you can script a reference to a new (or existing scripted) on_action.  

**The Immediate Block & You**  
A major new addition to CK scripting, which we use with extreme regularity in the immediate block, is the scripted list!  

These allow us to sort through various groups, pick out relevant characters matching a set of criteria, and then sort within the list of relevant characters *only* with ease.  

For instance, let’s say I want to grab every ornery old man from amongst my vassals and courtiers, I’d write something vaguely thus:  


![008.png](https://forumcontent.paradoxplaza.com/public/574149/008.png "008.png")



And then, I want to pick out the two angriest and orneriest from amongst *them* so that I can have them get into an argument in an event or what have you:  


![009.png](https://forumcontent.paradoxplaza.com/public/574150/009.png "009.png")



Sorted! I can then refer to these two characters in my localisation, apply effects to them, make them portrait characters, etc., as needed. You may note our cool new alternative_limit functionality: these are limits which are checked if the limit immediately above them fails.  

That said, we’re all about minimising unnecessary maintenance and nipping potential bugs before they exist, and this script should still be setting off alarm bells, what with calling two separate lists that use the same conditions, which are, themselves, part of a separate scripted trigger.  

There are a few ways we could solve this, but let’s go for showing off some new functionality, with the ordered_in_list effect:  


![010.png](https://forumcontent.paradoxplaza.com/public/574151/010.png "010.png")



Ordered_in_list takes a list, and, using a system called script_maths (which we’ll hopefully have time to talk about another time), assigns numerical values to items in that list. It then applies any effects in its block as normal to, by default, the highest valued item in the list (though, as here, we can tell it to apply its effects to any number of items in the list). Here, we were sorting a relatively small amount of list items by a fairly limited set of factors, but this sorting functionality can be as complex and as extensive as you require.  

In other immediate block-related news, we’ve also made it easier to save scopes (formerly event targets, which you can see a bit of in the above example), and variables, and customarily use this block to define musical stings for *maximum drama*. Standard immediate block functionality (being executed before the event is displayed) is unchanged, and visible effects executed in the Immediate will be shown under a “Has Happened” header in all event option tooltips.  

**Options: Giving the AI Personality & Stressing Out Players**  
Finally, options. Options behave similarly to CK2, with a minimum of one per visible event and each option requiring a text label, but otherwise allowing you to enter any and various effects you fancy.  

![011.png](https://forumcontent.paradoxplaza.com/public/574152/011.png "011.png")



The two main additions to this area that you’ll notice are a drastically expanded use of ai_chance, and, fairly commonly, stress_impact.  

AI chance, as in CK2, governs the approximate chance that an NPC character will pick that option. In CK3, we’re making much more extensive use of this block, and of our exposed ai_value_modifiers (building a personality for each character based off how much/little of each value they have, in turn derived mostly from their traits) to ensure that characters act in accordance with their personality as much as possible by weighing almost all event options up or down based on appropriate ai_value_modifiers. The block still takes other triggers as well, so we can have the AI prefer an option more or less based on traits, if they’re at war, if the option relates to a rival, etc.  

Stress_impact, meanwhilst, is how we organise the new stress mechanic, which you may remember from some diaries ago! Don’t stress (*ahem*) if you don’t: stress is, in a nutshell, a measure of negative effects that your character gains when performing actions that run contrary to their personality (e.g., a compassionate character does not enjoy torturing people).  

We check for that here, by filling out the stress_impact block with any personality traits relevant to picking a particular option, and using the scripted stress_impact values. Due to sorcerous automagic, we can combine any number of stresses gained and lost in the stress_impact block, and it’ll be calculated on an event option into one number.  

You can also add stress as an ordinary effect, outside of the stress_impact block, in which case it will not combine. If desired, you can even add multiple stress impact blocks, which will only combine the individual stress modifiers, or you can omit the block entirely. Whatever floats your scripting-boat.  

And, with that, we come to the end of another dev diary. I’ll be around for a couple of hours to answer any questions you might have, and we look forward to seeing you ne-  

**A-aren’t you going to cover Triggers?**  
Ha, you fell for my cunning plot-twist. Hands up anyone who noticed the stealthy trigger spoiler in an earlier screenshot, you win exactly one internet point!  

For everyone else, let’s have that screenshot again:  


![012.png](https://forumcontent.paradoxplaza.com/public/574155/012.png "012.png")



Now, a quick recap: scripted triggers in CK2 were a way of grouping a long list of requirements together under a single reference, and then referring to that reference when needing to check things.  

For instance, say I have two places in an event where I need to check 20+ conditions: the event will be perfectly functional if I script all those conditions out twice, but what if someone in the future updates one set of triggers but not the other? Instant source of bugs. Now, what if I have to check those triggers more than twice, or across multiple events, or, for maximum-sadism, across multiple events *in different files*?  

As you can imagine, that rapidly devolves into chaos. However, we don’t want to use less complex triggers, partially because that makes the title worse and less fun for everyone (is it *really* CK without ludicrous amounts of specificity?), and partially because that’s only reducing the scale of the problem, not fixing it.  

Instead, we’d create a scripted trigger, which is the list of triggers written out *once* in a file that can be referenced by other files. Then, in any spot needing to check those triggers, we call the scripted trigger, which checks its contents. Any time the triggers need updating or fixing, simply fix the scripted trigger once, and, typically, all subsequent places that check the scripted trigger have been fixed by proxy also. Instant maintenance savings, immediate huge reductions in bug potential!  

However, in CK2, these scripted triggers had to be stored inside a specific folder in /common, separate from the events (and other script) that they referenced. This may not sound like a huge deal, but it adds a bit of extra leg-work to creating and maintaining scripted triggers, and only really gives you a huge list of scripted triggers, some of which may be used only a few times in a couple of places.  

In CK3, we’re improving on this by adding inline scripted triggers, meaning scripted triggers that can be written *directly* into the file that uses them, provided they are only used in that file. For more utilitarian scripted triggers that need to be used across multiple files, the old folder system still works. This lets us split up major and minor scripted triggers, and use scripted triggers (and, for that matter, scripted effects) significantly more thoroughly throughout the title, making it markedly easier for us (and you!) to create script that doesn’t compromise on complexity or detail whilst still being easy to maintain.  

And with *that*, we come to the actual end of the dev diary. We look forward to seeing you next week!

 

- 87

<!-- artifact:reactions:start -->
- 60 Like
- 33 Love
- 5 (unlabeled — rendered as base64 data URI)
- 1 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Wokeg](https://forum.paradoxplaza.com/forum/members/wokeg.1325927/)**
Role: Former CK3 Experienced Game Designer
Badges: 75
Messages: 528
Reaction score: 15,169

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
