---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1357939/"
forum_thread_id: 1357939
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 18
title: "CK3 Dev Diary #18 - Men-at-Arms, Mercenaries and CBs"
dd_date: 2020-03-17
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
body_word_count: 1358
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1357939'
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
    location: raw_lines_~28_to_150
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_152_to_154
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_243_to_246
    action: preserved_and_flagged
    counts:
      Like: 10
      Love: 3
      (unlabeled — rendered as base64 data URI): 1
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_254_to_369
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_370_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #18 - Men-at-Arms, Mercenaries and CBs

<!-- artifact:thread_metadata:start -->
- Thread starter [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)
- Start date [Mar 17, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-18-men-at-arms-mercenaries-and-cbs.1357939/)
<!-- artifact:thread_metadata:end -->

Hello everyone, and welcome back!  

This week we’ll be talking about a lot of additional details surrounding warfare. Just a few bits and pieces that have changed since CK2.  

**Casus Belli**  
One thing that is as it ever was, however, is that you need a Casus Belli to go to war, and that CB determines what happens when the war is won (or lost!). The most common ones are for pressing claims, as you’re familiar with from CK2. In different situations there will be a different options, of course, and some are even unlocked in special ways, such as the ones unlocked by perks, as shown off in the Diplomacy Lifestyle dev diary.  


![Declare war view.PNG](https://forumcontent.paradoxplaza.com/public/542230/Declare war view.PNG "Declare war view.PNG")



**War Declaration Cost**  
One thing that has changed a little is the fact that different CBs come with different “declaration costs” attached to them. This is usually Prestige or Piety, depending on whether you are starting a war against a fellow believer or someone from another faith. On the other hand, we don’t want to keep you from taking advantage of a great opportunity just because you’re missing 10 Prestige at a crucial moment, so the costs are optional, in a sense.  

You can declare a war without paying its cost, at which point you’ll instead pay something bigger, such as a Level of Fame or Devotion.  

Levels of Fame/Devotion brings their own benefits, so ideally you want to avoid this, but it’s not as big a problem as - say - truce breaking. It’s not going to cripple your play, just set you back a little bit in exchange for getting to raise your armies and take some new titles while your enemy is weak. This is also one of the ways that Piety and Prestige gain has become more valuable than it was in CK2. You want to use it for more stuff, and it’s always useful to have lying around!  

**Men-at-Arms**  
We have talked about armies before, where we talked about the difference between your levies and your Men-at-Arms. Your levies are your unwashed masses, indistinguishable peasants more than willing to die for the few measly pieces of gold you throw their way. Men-at-Arms, on the other hand, are more specialist troops, and the component that gives you more control over precisely how you win your wars. They are in many ways your elite troops, ready to march through mountains and marshes for you.  


![MaA view.PNG](https://forumcontent.paradoxplaza.com/public/542235/MaA view.PNG "MaA view.PNG")

  

You have a maximum number of Men-at-Arms regiment slots for your army, and in addition they have an upkeep cost. It’s small when they’re unraised, but the moment you have them stand up to go to war, they’ll demand a lot more pay!  

Even though you can max out your MaA slots, there are other ways you can expand your army. Each MaA regiment can be increased a set number of times, to field even more of your deadly warriors. This will naturally increase their maintenance cost as well (both raised and unraised) so think twice before hiring twice as many soldiers!  

There are many different types of MaA regiments, and what their type is determines a number of things, such as what terrain they are good at fighting in, and what kind of MaA Regiments they are good at countering, or get countered by. Over time, you may also be able to acquire new types of MaA Regiments. This means that the bulk of armies are likely to be quite different if you start in 867 compared to when you reach the end of the game.  


![Create MaA view.PNG](https://forumcontent.paradoxplaza.com/public/542229/Create MaA view.PNG "Create MaA view.PNG")

  

MaAs also include siege engines, which is one of the easiest way of speeding up your land grabs. However, siege weapons are almost useless in regular combat, and taking them uses up one of your MaA slots, so it’s a decision that has to be carefully thought through.  


![MaA siege engine.PNG](https://forumcontent.paradoxplaza.com/public/542231/MaA siege engine.PNG "MaA siege engine.PNG")

  

In addition to a standard slate of MaA types, different cultures gain access to different unique MaAs. These will vary greatly across the world, but are generally specialised in the conditions of warfare that’s typical for the culture in question.  


![Camel Riders.PNG](https://forumcontent.paradoxplaza.com/public/542228/Camel Riders.PNG "Camel Riders.PNG")

  

You will also be able to look at battle reports to get an indication of what kind of impact specific types of MaAs have on your battles. This can let you figure out whether your strategies are paying off, or whether it’s finally time to get some Pikemen to counter the Light Cavalry that your rival is always fielding.  

So to sum it all up, Men-at-Arms are great for countering specific troop types, adjusting to specific types of terrain, and directly bolstering the number of soldiers in your army! Sometimes, strategising and countering isn’t enough, however, and that’s where Mercenaries come in!  

**Mercenaries**  
Mercenaries are familiar to any CK2 player, of course, but they have changed a little now.  

First of all, you no longer pay monthly maintenance for them. Instead you pay their cost for three years up front, and then they’re yours for that time to use as you see fit. They’ll stay with you through thick and thin (although mostly the thick of battle).  


![Mercenary company screenshot 3.PNG](https://forumcontent.paradoxplaza.com/public/542232/Mercenary company screenshot 3.PNG "Mercenary company screenshot 3.PNG")

  

Once the three years are almost up, you’ll receive an alert warning you that the Mercenaries are about to pack up and get on their way! You’ll then have the opportunity to pay them for another three years of service. This also means that they aren't going to betray you the second you go into debt, which I know will sadden a lot of you, but this new system makes it a lot easier to keep track of what you have and don't have during war.  

So Mercenaries are an expensive way of doing warfare, but sometimes it’s the only way you’ll survive. However, in order to find a Mercenary Company that fits you in both size and shape, we have a new system for generating them to make sure there's always a wide range to choose from.  


![Mercenary Hire view 2.PNG](https://forumcontent.paradoxplaza.com/public/542233/Mercenary Hire view 2.PNG "Mercenary Hire view 2.PNG")

  

Each culture generates between one and three Mercenary companies depending on the number of counties of that culture, with each additional company being bigger and more expensive than the previous one. They will also pick a county of their culture to keep as their headquarters, and will be available to be hired by anyone within a certain range of that county.  

With each culture generating Mercenaries, their names and coats of arms are either picked from a generated list of names specific to their culture so that you can get historical or particularly flavourful companies in there.  

On top of everything else, Mercenary companies come with one or more specific Men-at-Arms types, which means that you may want to consider not only which company is the biggest one you can afford, but which is the best suited for the war you’re about to fight.  

This should all offer you a lot of varied strategies for how you go about your wars. Is it worth saving up for the CB cost or mercenary-Gold ahead of time? What Men-at-Arms should you be using against your ancestral enemies? Who would win in a fight between the the White Company and the Company of the Hat??  

You’ll just have to wait until release to see...

<!-- artifact:reactions:start -->
- 10 Like
- 3 Love
- 1 (unlabeled — rendered as base64 data URI)
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Voffvoffhunden](https://forum.paradoxplaza.com/forum/members/voffvoffhunden.246161/)**
Role: Rouge Game Dev - Former CK3 Content Designer
Badges: 74
Messages: 261
Reaction score: 1,286

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
