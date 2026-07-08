---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1308005/"
forum_thread_id: 1308005
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 9
title: "CK3 Dev Diary #09 - Lifestyles"
dd_date: 2020-01-14
author_handle: rageair
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 843
inline_image_count: 4
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1308005'
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
    location: raw_lines_194_to_195
    action: preserved_and_flagged
    counts:
      Like: 8
      (unlabeled — rendered as base64 data URI): 5
    note: Reactions block parsed; 1 of 2 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_203_to_282
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_283_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #09 - Lifestyles

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Jan 14, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-09-lifestyles.1308005/)
<!-- artifact:thread_metadata:end -->

Greetings! Today we’ll be taking a look at a new and exciting feature in CK3 - the Lifestyle system!  

Now, to start off, the lifestyles of CK3 have very little in common with those in CK2. The system has been changed and is vastly improved and much more interactive than CK2’s system. In fact, we have proper skill trees now, much like those you would find in an RPG. You will gather experience and unlock perks, which conveys all kinds of bonuses to your character! This allows you to tailor your character to your needs, immerse yourself in their story, and provides a lot of replayability, as it’s not only about what perks you get, but also when you get them.  

There are five Lifestyle categories, with each category containing three full skill trees. You first choose the Lifestyle you want, and then you select a focus within it.  

![DD_LS_1.png](https://forumcontent.paradoxplaza.com/public/526269/DD_LS_1.png "DD_LS_1.png")




The focuses convey immediate bonuses, much like they did in CK2 - you usually pick the Focus that provides the modifier you most need at the moment. For example, if you desperately need piety you can pick the Theology Focus, while if you have just conquered a large amount of land the Authority Focus might be more appropriate. You can pick any Focus within a Lifestyle to gain experience within it, the Focuses do not correspond to specific trees.  

Each Focus also comes with its own unique set of events, connected to the theme of the Focus. If you have the Temptation focus selected you might get events about subtly manipulating your vassals and guests, finding out their secrets or gaining hooks, while if you have the Wealth focus selected it might see you levy extra taxes upon your peasants, among other things. More on this in the next weeks DD.  

![DD_LS_2.png](https://forumcontent.paradoxplaza.com/public/526268/DD_LS_2.png "DD_LS_2.png")



After you’ve picked a Focus, you will start gaining experience and can start unlocking perks!  

Now, characters will not usually live long enough to unlock every perk. You will have to choose which path to go down, and you will unlock a new perk every few years. Perks are unlocked by spending experience, which is gained both passively (symbolizing that your character dabbles in subjects pertaining to their lifestyle during their free time) and actively (through choices in Lifestyle events, etc).  

Perks are wonderful things that unlock all manner of possibilities and opportunities. Going down the right paths will unlock special modifiers, decisions, casus bellis, and even schemes. Some perks will modify existing systems to work differently for your character - for example, going down the Avarice path makes Stress (more on this in a later DD) have some positive effects. There are perks that make your troops fight better, that make factions stay in line, or that fortify your health. Really, you’ll be spoilt for choice - and we’ll go into more detail on what each Lifestyle is capable of in the coming weeks!  

![DD_LS_3.png](https://forumcontent.paradoxplaza.com/public/526270/DD_LS_3.png "DD_LS_3.png")



The final Perk in each tree always gives you a trait, which is very powerful (think the Master Seducer trait in CK2), nicely rounding them off. If you live long enough, you’ll see yourself accumulate a few of these.  

![DD_LS_4.png](https://forumcontent.paradoxplaza.com/public/526280/DD_LS_4.png "DD_LS_4.png")

  
*Can you guess the traits? 15 of these traits are tied to the Lifestyle trees, the remaining can be gained through special events and activities.*  

While you won’t start using Lifestyles and unlocking perks before you’re an adult, it really begins during childhood. Depending on the education you get, you will have an affinity for a certain Lifestyle - now this doesn’t mean that you’re stuck with that Lifestyle, of course, you can choose any lifestyle regardless of your education. The education ranks directly correspond to a percentage increase in experience gained, a rank one education will give a 10% bonus, and a rank four one a 40% bonus, and so on.  

When a character becomes landed they will select a focus and unlock perks based on their age - the older they are, the more perks they will have unlocked. They will select an appropriate Lifestyle based on their education (making it even more important to manage your children’s education carefully), and perks based on their personality and traits. Do not worry though, if you’re not satisfied with the hand you’re dealt you can choose to reset all perks (within that Lifestyle) once per lifetime - though this will incur a massive amount of Stress (again, more on this in a later DD). Sometimes it’s worth playing the hand you’re dealt - perhaps going along with your lustful heir's seductive tendencies could open up a venue you hadn’t even considered?  

In the next few weeks we’ll dive deeper into the various aspects of the Lifestyle system, so stay tuned!

<!-- artifact:reactions:start -->
- 8 Like
- 5 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 17 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
