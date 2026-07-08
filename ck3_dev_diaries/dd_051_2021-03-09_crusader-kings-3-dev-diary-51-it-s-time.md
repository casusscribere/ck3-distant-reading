---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1461029/"
forum_thread_id: 1461029
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 51
title: "Crusader Kings 3 Dev Diary #51 - It's Time to Duel"
dd_date: 2021-03-09
author_handle: Snow Crystal
expansion: Northern Lords
patch: Patch 1.3
extraction_method: claude_in_chrome_dom_capture
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1468
inline_image_count: 0
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1461029'
extraction_rationale: |
  Captured via Claude in Chrome (get_page_text) because WebFetch returned
  a truncated inline response or a Cloudflare challenge. XenForo structural
  markers were synthesized by process_chrome_capture.py so extract_diary.py's
  boundary regexes can locate the body, reactions, and signature anchors.
detected_artifacts:
  - type: webfetch_metadata
    location: raw_lines_1_to_~27
    action: discarded_from_output
  - type: forum_chrome
    location: raw_lines_~28_to_5
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_7_to_9
    action: preserved_and_flagged
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
  Chrome-captured fetch: author_handle is synthesized because the
  XenForo signature card is not present in DOM text. inline_image_count
  reflects body-text image references only. Reactions block absent.
---

# Crusader Kings 3 Dev Diary #51 - It's Time to Duel

<!-- artifact:thread_metadata:start -->
- Thread starter [Snow Crystal](https://forum.paradoxplaza.com/forum/members/synthetic.0/)
- Start date [Mar 09, 2021](https://forum.paradoxplaza.com/forum/threads/.1461029/)
<!-- artifact:thread_metadata:end -->

Crusader Kings 3 Dev Diary #51 - It's Time to Duel
Welcome comrades! Today, we'll be talking about our final major free patch feature: single combat.

Duels in CK2 have been a much-beloved feature for years, and whilst we've certainly got duelling content in CK3, we wanted the option to invoke something a bit more elaborate when circumstances called for it.

Following up on and improving such a feature was always going to be a tough ask, but we're pretty happy with what we've got.

Plus, QA dared me, so here we are.

Ethos
When designing the new single combat system, we had a few key points in mind to guide our implementation.

1. Duels should be dangerous
The outcome of an in-depth duel should never be a completely forgone conclusion: a desperate rookie can still surprise a veteran master, or get lucky/play smart. If the fight would be ended before it's even begun, it should use a simpler effect or auto-win option.

2. Duels should be reusable
Duels should be easy to add anywhere in script, and their results should be as agnostic as possible. A detailed duelling system should be able to account for everything from strict honour duels to battlefield bouts to a knife fight in the tavern.

3. Duels should be variable
Duels should vary in content and strategy depending on the characters involved and the location and circumstances around them. No two fights should ever be totally identical.

4. Duels should be character-driven
Character traits, relationships, and other qualities should all have an impact on duels, not just prowess.

5. Duels should allow for both experience and intuition
Although understanding the mechanics of the system should be rewarding and allow competent play, a newbie just guessing should still have a fair chance of success.

6. Duels should allow for both roleplay and rollplay
It should be viable to both always play to win, and to play according to what makes sense for your character, without either totally kneecapping you. This should carry over to the AI, who should be somewhat readable based on skills and character traits.

Mechanics
All single combats take place between exactly two characters, and are fought to a predetermined end (be that a slight cut, an increase in the wounded trait, or a fatal blow), at the end of which the loser may be wounded or killed as appropriate.

Combat is divided up into distinct rounds, with first the defender, then the attacker selecting an option, before we work out whether one or the other has done enough to win or lose. All combats last between two and four of these rounds, ending automatically after the fourth (though this is a scripted value and easily changed if you prefer the possibility for prolonged, dramatic fights).

Options available are stylised as distinct combat moves, like headbutting your opponent, rushing into an all-out attack, playing defensively, and so on. At the start of your turn in each round, you randomly draw three such options from a pool of available choices, with the relative usefulness & drawbacks of each move related to your prowess skill.

The higher your prowess, the more likely you are to draw good moves, the worse your prowess, the more likely you are to draw bad ones. It's a little more complicated than that in practice, but that's how it feels player-side.

Instead of one of your regular combat moves, you may also draw a special move. Rather than being based on just your prowess skill, these take into account traits, location, special relationships between you and your opponent, all manner of things. They range from giving a demoralising speech to your opponent to using your skill as a raider to make an example of them as you fight.

As a rule of thumb, special moves tend to either offer a better pay-off than standard combat moves, or else give secondary effects outside the duel (e.g., dread gain or stress loss) At present, we have 18 standard combat moves and 22 special moves.

The primary method of winning a bout is to gain enough Likelihood of Success. This is a sort of tug-of-war between you and your foe, representing who is currently winning the duel, with almost all moves adding to the score. The first character to get their score a certain threshold above the other's wins.

However, most combat moves also give you some Risk of Injury, representing how overextended you are and how easy it is for you to make a mistake and hurt yourself or else be dramatically foiled. As this goes up, it makes it more likely that you'll simply lose when a round ends if you haven't managed to explicitly win.

The basic rubric for fighting is thus trying to maximise your Likelihood of Success without extending your Risk of Injury enough that you lose before you can beat your opponent.

In the penultimate round of a fight (by default, though this can again be changed easily by tweaking one number), it becomes much easier both to win and to injure yourself, and certain special moves can also adjust these thresholds.

If, after the final round of the fight, there's still no winner, then the highest prowess skill wins.

The AI selects combat moves and strategy based roughly off of personality, meaning that not only can it change as they gain prowess-related traits, but different characters will often fight differently even if they share identical prowess.

Finally, we have the duel edge system. As you duel, certain moves by you or your opponent may accrue duel edge bonuses and maluses for one or both of you, helping or hurting your prowess skill for the duration of the bout. This helps to keep things risky, and means that just because you entered a fight knowing who had the best prowess, it won't necessarily stay that way for the whole combat.

Duelling in Context
Since one of our prime goals with the new duelling system has been to make it useable in as many circumstances as possible, setting one up is nice and easy. We have a single effect that configures the circumstances of the bout, and every use of the effect requires two small follow-up events. One tells the duel what happens if it invalidates for some reason (usually we just send out toasts informing the affected parties), the other processes the after-effects of the duel itself, be they losing a bet or gaining a friend.

And… that's it. It can be dropped into any effect block, any interaction, decision, or event, with whatever net results or criteria you like. Complex fight sequences with no muss, no fuss.

There are several ways we use this system in-game at the moment, with the most noticeable being an interaction to duel your rivals now unlocked by the Chivalry lifestyle tree's Stalwart Leader perk (pictured a ways above). We also use it in several paid events in 1.3, and, of course, the all-new [REDACTED] interaction.

Over time, we hope to improve the combat system with general QoL tweaks, dedicated UI, and, last but not least, more combat moves. We also intend to pepper it throughout future content, as well as rework certain elements of old content on an on-going basis to use these more elaborate duels as appropriate.

Stick 'em with the Pointy End
Let's have a bash at using the single combat system in anger, shall we?

Here's me, as High Chieftain Waththab, fighting my son and rival, Musa, in a non-lethal bout.

Skills-wise, my son out-matches me quite drastically. I've got a fairly low prowess rating, whilst he's at the upper end of average.

This means that he'll be rolling average to excellent moves, and I'll likely be rolling terrible to average moves. Both of us lack most traits that would grant special combat moves, and we have no extraneous circumstances that would give us any either (though we've got some special dialogue in places due to be related).

That said, there's still a strategy here. I can see that my son is deceitful and craven, so overall, he's likely to pick combat moves that are cautious or cunning. This means he'll probably play it safe on trying to win via Likelihood of Success, and instead wait for me to injure myself with my blunders. If I can overwhelm Likelihood of Success before my Injury Risk gets too high, then I might be able to beat his

Written by

### [Snow Crystal](https://forum.paradoxplaza.com/forum/members/synthetic.0/)

Paradox Staff
