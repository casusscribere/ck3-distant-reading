---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1316277/"
forum_thread_id: 1316277
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 11
title: "CK3 Dev Diary #11 - Seduction, Torture and the Intrigue Perk Trees"
dd_date: 2020-01-28
author_handle: Voffvoffhunden
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2168
inline_image_count: 31
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1316277'
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
    location: raw_lines_426_to_427
    action: preserved_and_flagged
    counts:
      Like: 4
      (unlabeled — rendered as base64 data URI): 3
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_435_to_505
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_506_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #11 - Seduction, Torture and the Intrigue Perk Trees

<!-- artifact:thread_metadata:start -->
- Thread starter [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)
- Start date [Jan 28, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-11-seduction-torture-and-the-intrigue-perk-trees.1316277/)
<!-- artifact:thread_metadata:end -->

Welcome and welcome back to all!  

This week I’m here to tell you all more about Intrigue: it's not just an act, it's a Lifestyle.  

As covered in a previous dev diary, each character Skill has a Lifestyle, and each Lifestyle has three associated Focuses and three Perk trees, which is what we'll be diving into today.  

Keep in mind that all values listed below are subject to change!  

For Intrigue, the three focuses are:  

![Intrigue Lifestyle Focuses.PNG](https://forumcontent.paradoxplaza.com/public/529104/Intrigue Lifestyle Focuses.PNG "Intrigue Lifestyle Focuses.PNG")


[Skulduggery Focus — Agent Acceptance: +10, Intrigue: +3]  
[Temptation Focus — Fertility: +25%, Attraction Opinion: 10, Seduction Scheme Power: +20%]  
[Intimidation Focus — Intrigue: +2, Dread Gain: +10%, Natural Dread: +20]  

Each perk tree — Schemer, Seducer, and Torturer — concludes with the unlocking of its namesake trait. I know this might be an insurmountable challenge, but feel free to guess which is which:  


![intrigue lifestyle traits.png](https://forumcontent.paradoxplaza.com/public/529123/intrigue lifestyle traits.png "intrigue lifestyle traits.png")


(Ah, is there any greater torture than the desires of the heart...)  

I'll also be running down the effects of every unlockable perk that leads to those, and I'm naturally going to start by talking about the Temptation focus, that eternal vice, and the Seducer tree, but first I want to describe its closely related Seduce Scheme.  


**The Seduce Scheme**  

Seduction is a little more complicated than it was in CK2, with factors such as the target's personal preferences playing a larger part. Indeed, Scheme Power is not merely affected by your Intrigue, but who you are, and who they are.  

That also means that you have to be a little careful. If a target gets annoyed rather than enticed, and you suffer a Critical Failure, they may give you a hard rejection - preventing you from attempting to Seduce them again - or even publicly out you as the lecherous villain you are!  

![Seduction Rejection.PNG.png](https://forumcontent.paradoxplaza.com/public/529113/Seduction Rejection.PNG.png "Seduction Rejection.PNG.png")




**The Seducer Tree**  

So how will the Seduce tree help you? A few Perks offer straightforward bonuses by increasing your Scheme Power or making you more attractive to those of an appropriate gender and sexuality.  

![enticing opportunity tt.PNG](https://forumcontent.paradoxplaza.com/public/529099/enticing opportunity tt.PNG "enticing opportunity tt.PNG")


[Enticing Opportunity — Seduction Scheme Power: +30%]  

![smooth operator tt.PNG](https://forumcontent.paradoxplaza.com/public/529115/smooth operator tt.PNG "smooth operator tt.PNG")


[Smooth Operator — Seduction Scheme Success Chance: +25%]  

![home advantage tt.PNG](https://forumcontent.paradoxplaza.com/public/529101/home advantage tt.PNG "home advantage tt.PNG")


[Home Advantage — Seduction Scheme Success Chance against own Courtiers and Guests: +50%]  

Others may expand your pool of... available targets.  

![subtle desire tt.PNG](https://forumcontent.paradoxplaza.com/public/529114/subtle desire tt.PNG "subtle desire tt.PNG")


[Subtle Desire — Removes the Incestuous penalty from your Seduction Schemes]  

Just to be clear, this affects the Scheme, not the relationship. If you're caught getting too close to family, you will still suffer consequences.  

Similarly, if you find your own sexual preferences getting in the way of who you can Seduce efficiently, there are ways you can overcome that:  

![unshackled lust tt.PNG](https://forumcontent.paradoxplaza.com/public/529121/unshackled lust tt.PNG "unshackled lust tt.PNG")


[Unshackled Lust — Removes your attraction penalties in Seduction Schemes]  
(There’s no way of overcoming your target’s sexual preferences, though. I’m sorry, but your liege is Just Not That Into You.)  


There are perks to help a different kind of “effectiveness” in your Seduce Schemes:  

![like weeds in a garden tt.PNG](https://forumcontent.paradoxplaza.com/public/529106/like weeds in a garden tt.PNG "like weeds in a garden tt.PNG")


[Like Weeds in a Garden — Fertility: +30%]  

And perks to mitigate the consequences of messing up:  

![graceful recovery tt.PNG](https://forumcontent.paradoxplaza.com/public/529102/graceful recovery tt.PNG "graceful recovery tt.PNG")


[Graceful Recovery — You can no longer Critically Fail Seduction Schemes]  

Ah, the number of times I have desperately needed the Graceful Recovery perk...  


Bringing a Lover to your court doesn’t come entirely risk-free, of course, so we also have a Perk to minimise the risk to you, at the unfortunate cost of maximising the risk for them:  

![Mortal adoration tt.PNG](https://forumcontent.paradoxplaza.com/public/529107/Mortal adoration tt.PNG "Mortal adoration tt.PNG")


[Mortal Adoration — Your Lovers are less likely to join Murder Schemes against you. Lovers are more likely to save you in case of attempted Murders.]  

What can I say? Not every love story has a happy ending.  


The final perk in the tree is the one that grants you the Seducer trait. It comes with increases to Intrigue, Fertility, and a hefty boost to Attraction Opinion for anyone who finds themselves unfortunate enough to be of the relevant sexual orientation. Rulers of the world, lock up your wives! And husbands! And family members! Maybe also yourself for good measure!  


**Torture**  

Of course, Intrigue does not merely embody pleasure, but also pain. I'm happy to announce that the fan-favourite of "Torture" is going to be making a return for CK3.  

What is it good for? Well, being Dreadful, for one thing, making your vassals fear you. Another benefit is the possibility that a victim will try to bribe you with Secrets to get you to stop. You're going to need those Secrets for leverage anyways, since the victim's family will hold you in utter disdain. Being an avid torturer also comes with a Piety penalty and a loss of Clergy opinion (unless your Faith happens to make exceptions for this kind of thing…).  

![torture interaction.jpg](https://forumcontent.paradoxplaza.com/public/529117/torture interaction.jpg "torture interaction.jpg")



**The Torturer Tree**  

Now, we wouldn't let you take the pliers to flesh without giving you a way of getting really good at it, would we? The Torturer tree is all about making your vassals and peasants fear whatever might be going on in your dungeons! Or in your throne room. Or in your presence in general.  

It has a series of Dread-increasing effects, as well as adding bonuses to various sources of dread.  

![dreadful tt.PNG](https://forumcontent.paradoxplaza.com/public/529097/dreadful tt.PNG "dreadful tt.PNG")


[Dreadful — Dread Gain: +30%]  

![divine retribution.PNG](https://forumcontent.paradoxplaza.com/public/529098/divine retribution.PNG "divine retribution.PNG")


[Divine Retribution — You do not lose Piety or Clergy Opinion from Torturing or Executing others]  

![prison-feudal complex tt.PNG](https://forumcontent.paradoxplaza.com/public/529110/prison-feudal complex tt.PNG "prison-feudal complex tt.PNG")


[Prison-Feudal Complex — Imprison Chance: +50%]  

And of course there are ways of making sure you keep that hard-earned Dread for as long as possible:  

![forever infamous tt.PNG](https://forumcontent.paradoxplaza.com/public/529103/forever infamous tt.PNG "forever infamous tt.PNG")


[Forever Infamous — Dread Decay: -100%]  

Of course, once you start "going off the rails" (as my fellow developers assure me my playstyle should be described as) you need to make sure that it doesn't go unnoticed. Keep the faint of heart in line, and all that.  

![malice implicit tt.PNG](https://forumcontent.paradoxplaza.com/public/529108/malice implicit tt.PNG "malice implicit tt.PNG")


[Malice Implicit — Dread Gain Per Tyranny: +0.5]  

It’s not all about Dread, however. Intimate familiarity with human anatomy can help in other ways, too:  

![dark insights tt.PNG](https://forumcontent.paradoxplaza.com/public/529094/dark insights tt.PNG "dark insights tt.PNG")


[Dark Insights — When you Torture someone: 50% chance to gain either 1 Intrigue or 1 Prowess]  

While it’s not a relief for Stress per se (unless you’re particularly sadistic), the Perk tree offers additional side benefits for your poor coping methods:  

![thriving in chaos tt.PNG](https://forumcontent.paradoxplaza.com/public/529118/thriving in chaos tt.PNG "thriving in chaos tt.PNG")


[Thriving in Chaos — Martial and Intrigue Per Stress Level: +1. Prowess Per Stress Level: +2]  

Dread (and the actions that give it) is quite powerful on its own, offering alternative ways of controlling your vassals, but what if we could make it even better?  

![fear tax tt.PNG](https://forumcontent.paradoxplaza.com/public/529100/fear tax tt.PNG "fear tax tt.PNG")


[Fear Tax — Increased tax and levy contributions from Intimidated and Cowed vassals]  

The last Perk in the tree grants the Torturer trait, which offers a slight Levy and Prowess boost, along with an additional improvement to your Dread gain. This will allow you to keep your Dread exceptionally high as you imprison, revoke, torture and execute to your heart’s content.  


**The Schemer Tree**  

Some of you out there are less bombastic in your methods, which brings us to our last tree for this diary. Skulduggery rules the shadows, keeping potential threats in line by more subtle tricks.  


It provides a number of different bonuses to your Hostile Schemes, and to your Spymaster’s tasks:  

![swift execution tt.PNG](https://forumcontent.paradoxplaza.com/public/529116/swift execution tt.PNG "swift execution tt.PNG")


[Swift Execution — Murder Scheme Power: +30%]  

![a job done right.PNG](https://forumcontent.paradoxplaza.com/public/529093/a job done right.PNG "a job done right.PNG")


[A Job Done Right — Hostile Scheme Success Chance: +25]  
(Hostile Schemes does not mean Schemes hostile against yourself, but rather Schemes that are categorised as Hostile instead of Personal.)  

![digging for dirt tt.PNG](https://forumcontent.paradoxplaza.com/public/529095/digging for dirt tt.PNG "digging for dirt tt.PNG")


[Digging for Dirt — Find Secrets Progress Speed: +25%]  

Find Secrets is the Spymaster Council Task you might remember from a few diaries ago.  

There are also a handful of defensive measures, should your enemies come looking for revenge:  

![court of shadows tt.PNG](https://forumcontent.paradoxplaza.com/public/529096/court of shadows tt.PNG "court of shadows tt.PNG")


[Court of Shadows — Disrupt Schemes Effectiveness: +50%]  
Disrupt Schemes is another —very useful— Spymaster Task.  

![prepared for anything tt.PNG](https://forumcontent.paradoxplaza.com/public/529109/prepared for anything tt.PNG "prepared for anything tt.PNG")


[Prepared for Anything — Enemy Hostile Scheme Success Chance: -25. Enemy Hostile Scheme Success Chance against your Courtiers: -10.]  

Once you've unlocked this collection of perks, it will be very hard to turn your own methods against you. You will only really have to worry about people who are your equal as a Schemer. But you should be worrying about those people anyways.  

In the previous dev diary about Schemes, you already got a sneak preview of a Scheme to Fabricate Hooks, which becomes available in the Schemer tree, and it's not the only scheme to be unlocked this way:  

![Truth is relative tt.PNG](https://forumcontent.paradoxplaza.com/public/529120/Truth is relative tt.PNG "Truth is relative tt.PNG")


[Truth is Relative — Enables the Fabricate Hook Scheme. Find Secrets may also fabricate Hooks.]  

![kidnapper tt.PNG](https://forumcontent.paradoxplaza.com/public/529105/kidnapper tt.PNG "kidnapper tt.PNG")


[Kidnapper *—* Enables the Abduction Scheme]  

Abduction is a criminal scheme, and therefore secret. However, if you succeed, you’re automatically discovered. They're not going to wonder for long whose dungeon they're locked in. You have nothing to worry about, though. The victim will be entirely at your mercy, after all.  


But with all these Schemes, and only a single hostile scheme slot, what is a poor little Power Behind the Throne to do? Why, get yourself a second Scheme slot, of course!  

![twice schemed tt.PNG](https://forumcontent.paradoxplaza.com/public/529119/twice schemed tt.PNG "twice schemed tt.PNG")


[Twice Schemed *—* Max Hostile Schemes: +1]  

Lastly, this Perk tree offers up the Schemer trait. Not only does it grant a major bonus to your Intrigue in general. It also significantly boosts your Scheme Power, speeding up the inevitable success of your ingenious plans.  


And with that we conclude this week's dev diary. I hope you're already daydreaming about all the ways you can grasp for power, and how to hold on to it once you've got it.  

Next week we’ll be diving into the perk trees for the Stewardship lifestyles, so adieu until then!  
Just remember to watch your back.

 

#### Attachments

- [![schemer tt.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/529111/schemer tt.PNG)](https://forum.paradoxplaza.com/forum/attachments/schemer-tt-png.541756/)
  
  schemer tt.PNG
  97,4 KB

 · Views: 827

- [![seducer tt.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/529112/seducer tt.PNG)](https://forum.paradoxplaza.com/forum/attachments/seducer-tt-png.541757/)
  
  seducer tt.PNG
  98,8 KB

 · Views: 757

- [![torturer tt.PNG](https://forumcontent.paradoxplaza.com/thumbnail/public/529122/torturer tt.PNG)](https://forum.paradoxplaza.com/forum/attachments/torturer-tt-png.541767/)
  
  torturer tt.PNG
  74,2 KB

 · Views: 676

Last edited: Jan 28, 2020

<!-- artifact:reactions:start -->
- 4 Like
- 3 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)**
Role: Rouge Game Dev - Former CK3 Content Designer
Badges: 74
Messages: 261
Reaction score: 1,286

*[Full game-badge icon list of 5 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
