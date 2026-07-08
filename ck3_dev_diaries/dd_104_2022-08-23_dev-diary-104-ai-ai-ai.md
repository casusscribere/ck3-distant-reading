---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1539411/"
forum_thread_id: 1539411
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 104
title: "CK3 Dev Diary #104: AI AI AI"
dd_date: 2022-08-23
author_handle: rageair
expansion: Friends and Foes
patch: Patch 1.7 (Bastion)
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 3978
inline_image_count: 17
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1539411'
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
    url: https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2036.jpg?1661263852
    note: Forum-injected banner image keyed off thread feature metadata; not authored by OP.
  - type: thread_metadata
    location: raw_lines_148_to_150
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_406_to_410
    action: preserved_and_flagged
    counts:
      Like: 200
      Love: 158
      (unlabeled — rendered as base64 data URI): 6
    note: Reactions block parsed; 2 of 5 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_418_to_490
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_491_and_after
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
![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_backgrounds/2/2036.jpg?1661263852)
<!-- artifact:thread_banner:end -->

# CK3 Dev Diary #104: AI AI AI

<!-- artifact:thread_metadata:start -->
- Thread starter [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)
- Start date [Aug 23, 2022](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-104-ai-ai-ai.1539411/)
<!-- artifact:thread_metadata:end -->

Greetings!  

One of the trickiest bits about GSGs is making a good AI. You want it to pose a challenge and play well, but you don’t want it to ruin the player’s fun by acting out of character. We’ve read a lot of discussions and threads in various places across the community, and we understand that there is room for improvement. Over the summer we’ve been working on a few aspects of the AI, specifically the economy (and a little bit of diplomacy). We’ve not focused on warfare, except for one thing which we’ll get to later.  

All changes outlined in this Dev Diary will be released in a future update.  

For the player to feel motivated to do well, the AI must show that it can do well alongside you. It doesn’t have to be fantastic or play optimally (in fact, that’s usually immersion-breaking), but it must be capable of progress. We want the AI in CK3 to be able to provide a good challenge and do well enough to motivate you to do even better. Also, we want it to do this without cheating.  

Before delving deeper into what we’ve done, I’d like to explain some of the challenges we set out to solve for the Economy:  


- Economically, all AIs currently play the same. We want their personality to affect how an AI decides to spend their hard-earned gold, and on what. You should be able to look at an AIs personality traits and, roughly, be able to tell what they’re up to.
- A player understands that there are certain ways of using gold that are optimal and appropriate regardless of their situation; that there are certain risks worth taking. We want the AI to understand this, employing decisions that make them prosper and are suitable to the stage the game is in.
- We want the AI to build more buildings, so that the world becomes more and more developed over time. Right now, only players realize the value that buildings bring in the long run, while AIs spend most of their gold on wars.
- The power of a ruler lies within their domain. The AI, much like the player, should strive to build a base of power and cultivate it over time.

…and here are some of the challenges we set out to solve for Diplomacy:  


- AI realms tend to fall apart, and never reform. Vast seas of counts and dukes, unwilling to accept the overlordship of neighboring kings. We want the AI to be able to diplomatically expand, much like the player is able to. New realms with great monarchs should rise out of the ashes of former empires.
- A stable realm is a prosperous realm, and there are many tools for achieving this. The AI should not hold back when using available methods of stabilization, be they diplomatic schemes or underhanded council actions.
- The AI should understand that Tyranny is sometimes appropriate. It’s for the greater good of the realm. Within reason, of course - personality and relationships must play a large role here. As it stands, the AI will never willingly take on Tyranny, under any circumstance.

…and for Warfare:  


- In real life, the Mongols were an existential threat. Currently, in CK, they are not. We want them to be. There is one pivotal change that enables this: the ability to gather armies closer to their target.

## The Economy, fools!​

The key to success in CK3 is a strong and stable economy, and such a thing is driven by buildings (and, partly, MaA). We’ve set out to change how the AI uses its gold so that it builds up its realm more. We’ve taken considerations to make sure that the AI does this in a way so that it, for example, doesn’t become too easy to defeat for the player. The backbone of this work rests upon a framework of Economic Archetypes.  


### Economic Archetypes​

There are four economic archetypes that AI rulers can fall into, of which three are significant: Warlike, Cautious, and Builder. If a character falls into none of these archetypes, they will be Unpredictable and use aspects of other archetypes in a semi-random fashion.  


#### Warlike​

![warlike_archetype_example.png](https://forumcontent.paradoxplaza.com/public/857652/warlike_archetype_example.png "warlike_archetype_example.png")


[Image - Warlike Personality Example]  
The Warlike archetype wants to be ready to declare war, always. This is the archetype that is most similar to how the AI behaves in the game right now. They will put their gold into a war chest before considering other options. If a Warlike archetype is at peace for an extended period of time, they will use the gold in their war chest to develop the realm - but they will first and foremost prepare for war, even in the early game.  

Bold and greedy AI’s tend to be Warlike. Common traits include Wrathful, Impatient, Sadistic, Ambitious, Vengeful, Irritable, and Zealous. Tribal rulers and cultures with the Bellicose Ethos are also drawn to this archetype, as well as any character in the Iberian struggle that wants to escalate towards the hostility phase.  

#### Cautious​

![cautious_archetype_example.png](https://forumcontent.paradoxplaza.com/public/857653/cautious_archetype_example.png "cautious_archetype_example.png")


[Image - Cautious Personality Example]  
Not to be confused with cowardly, the Cautious archetype wants to be prepared for having war be declared upon them. They are somewhat averse to declaring offensive wars, instead preferring a slow buildup. This archetype will save up a minimum buffer of gold, depending on their tier. When choosing to invest gold into buildings or MaA, they will evaluate the state of their military, how long they’ve been at peace, how many allies they have, and their level of dread - depending on these factors, they will feel ‘safe’ and invest more gold than they would otherwise, while keeping the aforementioned minimum buffer.  

Non-bold AIs tend to be Cautious. Common traits include Patient, Calm, Craven, Paranoid, and Content. Rulers with the Fickle or Lunatic trait will never be cautious. Rulers with the Stoic Ethos or the Stalwart Defenders Cultural Tradition are also drawn to this archetype.  


#### Builder​

![builder_archetype_example.png](https://forumcontent.paradoxplaza.com/public/857654/builder_archetype_example.png "builder_archetype_example.png")


[Image - Builder Personality Example]  
The Builder archetype wants to invest all of its gold into the realm. They will empty their treasury in order to build buildings and MaA as quickly as they can, and will also tend to construct more economical buildings and new holdings than other archetypes. They are bold and a bit reckless, only saving up a war chest if they are under a direct threat (such as a strong faction). This is the rarest of all archetypes.  

Bold AIs with a propensity for building and no particular inclination for war fall into this archetype. Common traits include Calm, Patient, Diligent, Generous, Stubborn, Profligate, and Improvident. Where Warlike AI’s want to expand their realm, the Builder wants to build up their domain. Rulers with the Domain Focus also tend to fall into this category.  


#### Unpredictable​

![neither_archetype_example.png](https://forumcontent.paradoxplaza.com/public/857655/neither_archetype_example.png "neither_archetype_example.png")


[Image - Unpredictable Personality Example]  
The Unpredictable archetype doesn’t have a propensity towards anything in particular, and might decide upon any strategy. They can decide to boom their economy much like the Builder archetype, but they do so randomly (weighed up by traits such as Diligent or Architect), and the amount will be modified by how bold they are. Otherwise, they will want to build up their realms to a minimum degree (higher than a Warlike archetype), keep a decent buffer (lower than a Cautious archetype), and go to war at a normal pace.  

AIs who do not qualify for any of the above categories will fall into this archetype.  


### Economic Stages​

The AI divides its economic game into three stages; Capital Development, Domain Development, and Late Development. The first two of these are ‘early’ stages that should be all but over roughly 100 years into the game.  

Each of these stages modifies how the AI spends its gold, which is then again modified by the economic personalities above.  

#### Early Capital Development​

The most important holding to develop is your capital, I’m sure you all agree. The AI will strive quite hard to fill all of the empty slots in its capital before doing many other things, as first-level buildings have a significantly higher return of investment than upgrades do. At this stage, the archetypes matter less, but this phase is also over somewhat quickly.  

This has a quite significant effect on the AI overall. By being able to kickstart their economy earlier than before, you will see them doing much better in the mid-late game. In the current version, you see a lot of provinces with open building slots well into the late game: even places of prominence, such as Paris, can sometimes be devoid of buildings - after these changes, this will be exceedingly rare.  

#### Early Domain Development​

In the second stage, the AI wants to develop its secondary counties by constructing first-level buildings there too. Truth be told, many AI’s elect to buy MaA or keep developing their capital during this phase as the choice of what to do/construct is semi-random and weighted - but this really just results in more powerful rulers overall.  

At this stage, the archetypes are manifesting, with Warlike AI’s saving war chests (albeit for shorter periods than in the Later stage!), Cautious AI’s saving up buffers, etc.  

When first-level buildings are present in an AI’s entire domain, they move on to the Later Economic Behavior.  

#### Later Economic Behavior​

During this stage, the archetypes will manifest fully. Builder AI’s will constantly build up their realm. Cautious AI’s will want a buffer, allies, and a powerful military, Warlike AI’s will only invest their gold if they’ve been at peace for many, many years - and so on.  

Interestingly enough, despite the AI being disincentivized from declaring frequent wars (previously all AIs were constantly gearing up for war), there are no fewer wars in the world. The wars that are declared are, however, more intense and exciting, as the AIs are generally more built up and have a stronger economic backbone.  

While the Economy part of this update isn’t the only thing contributing to what you’re about to see, here’s a comparison of the Live version of the game compared to the upcoming update. The sample size is 200 years, and there are no major deviations except for the Mongol Empire not having collapsed yet in the Live comparison.  


![comparison_stats_ai.png](https://forumcontent.paradoxplaza.com/public/857656/comparison_stats_ai.png "comparison_stats_ai.png")


[Image - Various Comparisons between the Live Version (1.6.1.2) and the upcoming update (1.7.0)]  
Counts+ in this context means Counts, Dukes, Kings, and Emperors.  

## Diplomatic Matters​

One of the AI’s faults is that it underuses the tools given to it, choosing to use them only sporadically and without much direction. The AI acting out its personality is all well and good, but in many instances, personality didn’t even matter at all, for example when choosing to revoke a title. We’ve done many small things that together add up to a vastly improved experience.  

### Domain Consolidation​

The AI is now going to strive towards having a strong capital and domain, prioritizing first and foremost the consolidation of lands within their De Jure Capital Duchy. For example, the king of France will want to hold Isle-de-France and all counties within the duchy of Valois.  

In order to do this, they are now willing to take on a modicum of Tyranny via revoking or retracting, modified by their personality. For reference, the AI has never before willingly taken on Tyranny and has always waited for a revocation reason. All AIs will want their capital county and at least a small domain (3 or so), regardless of personality, but Just and Generous AIs will stop after that point. Depending on the AI’s rationality, they will be willing to take on more or less Tyranny. Wise and rational rulers will want to let their Tyranny decay completely before taking a tyrannical action again, while more irrational rulers are willing to keep their Tyranny high in order to consolidate their domain.  

In order to consider revocation, the AI looks to its reserves of gold and military strength, making sure to not get into Tyranny wars it doesn’t think it can win (of course, it still happens that a ruler is overthrown via Tyranny, but it’s rarer!).  

Of course, relationships are accounted for, so you won’t see the AI revoking from their friends, lovers, children, etc.  

In practice, this means that the average AI ruler is much more powerful, and you won’t see things such as the king of France being content with having one single domain county in Brittany, just because they don’t have a revoke reason on the current ruler of Isle-de-France. In combination with the previously mentioned economic changes, this results in economically powerful AI rulers.  


![scotland_consolidated_domain.png](https://forumcontent.paradoxplaza.com/public/857657/scotland_consolidated_domain.png "scotland_consolidated_domain.png")


[Image - Alba having consolidated their capital duchy]  

The AI has also been taught to revoke secondary baronies in the counties it owns, which is especially useful for Clan rulers, as they can hold temples. This makes it so that much of the Clan sphere has a stronger economy, especially early on, and is able to match European and Indian feudal realms which generally have more favorable terrain.  

### Vassalization​

One of the things that we’ve changed a lot is how vassalization works and how the AI uses it. This isn’t a pure AI change, as we’ve also rebalanced all the modifiers that affect whether a character wishes to accept your overlordship or not. But, yes, simultaneously we’ve taught the AI to consider these facts and try to make their neighbors into vassals.  

A sub-goal here was to make vassalization into a viable alternative to military conquest, while also dialing back the most powerful sources of vassal acceptance and adding more interactive modifiers. While I won’t go into all of the detail here, I’ll say that the modifiers from Diplomatic Court and True Ruler have been lowered, while modifiers such as Average Powerful Vassal Opinion (-20/+20) have been added to promote alternatives to only being militarily powerful. We’ve also tweaked the opinion modifiers for Clan rulers so that Feudal rulers don’t have a fundamental advantage when it comes to vassalization (by offering low Contracts).  

The AI will now much more frequently check if neighbors would accept vassalization, and they will actively seek to sway or befriend neighbors if the AI considers them targets for diplomatic expansion. This means that the player does not have a monopoly on vassalizations any longer; if you take too long, AI rulers will sweep in and offer overlordship to your small independent neighbors.  

In practice, this means that areas stay shattered and stagnant for less time, while also creating more interesting realms where different cultures (and even faiths) are represented in the vassal strata. As an example, you might see a great unifying Sultan appear somewhere in Persia and diplomatically sweep up the remains of a shattered Seljuk Empire.  


![vassalize_example.png](https://forumcontent.paradoxplaza.com/public/857658/vassalize_example.png "vassalize_example.png")


[Image - Example of new vassalization modifiers]  

### Holy Wars​

As it turns out, rulers of the same faith as the defender in a Holy War would never join in their defense, despite the game claiming they would. This is our bad: a set of triggers were looking at the wrong character, and thus no one would consider joining. This is now changed, and we’ve put some effort into ensuring that the rulers who join up against you feel right.  

Protecting the boundaries of your faith is important, and the AI is now aware of this. Depending on personality and economic readiness, they will now assist their brothers-in-faith against encroaching heathens. Zealous and bold AI’s are the first to join, while you can be certain that cynical and cowardly rulers will not. Vassals of your target won’t join in, though vassals of neighboring rulers might - generally, you need only look within the immediate area as you declare wars. Extremely zealous rulers, though, might decide to join in from further away.  

In practice, you have to prepare well before declaring a holy war, but taking stock of your neighbors will help you here - personalities are telling, so you shouldn’t be overly surprised when someone aids your target.  

From a game perspective, this makes it much less likely for the Middle East to be completely overtaken by either Catholics or Orthodox Christians (which seemed to happen in at least 90% of all observer games that ran until the end date). Major religious upsets are now rarer, but when they happen they are all that much more likely to stick, as they’ve probably been launched by strong rulers during an opportune time.  

### Realm Stability​

AI rulers should now be somewhat more aware of the state of their realm, and proactively try to improve its stability. There are many flavors of stability, some more underhanded than others…  

Firstly, the AI is now much more likely to sway, and when they choose who to sway they are much more likely to pick important characters. For example, they will sway their realm priest, spymaster, and angry powerful vassals much more often, and also keep swaying them for a longer time. This also goes for the befriend scheme, should it be available. In the comparison screenshot at the end of the economy section, you’ll note that there are significantly more AIs with bishops/realm priests who endorse them.  

AI rulers with a more… unsavory disposition will use the Find Secrets council task, which the AI previously didn’t use. They’ll tend to target their vassals or rivals, if the chance of being found out isn’t too great. They’ll then blackmail and use the ensuing hooks to improve vassal contracts. Rulers who have unlocked the Fabricate Hook scheme will also much more often use it on vassals whose contracts can be modified. Over the generations, this means that the contracts AI rulers have with their vassals tend to be much better than they used to.  

![contracts_1389.png](https://forumcontent.paradoxplaza.com/public/857659/contracts_1389.png "contracts_1389.png")


[Image - Sample vassal contracts, France 1389]  

In general, we’ve taken a pass on when AIs will use certain Council Tasks. They will avoid certain things completely (using bestow royal favor on vassals-of-vassals), and more proactively switch to tasks that support them in the short term (support schemes when any hostile scheme is active, Organize Army when gold is running very low, etc).  

There’s a whole lot more that we’ve taught the AI to do, most of them small - but small things add up. They will send non-primary children to be educated by vassals they want to appease (it’s 15 opinion per child after all!), make their children learn the languages of their subjects to prepare them for a smooth succession, hire seneschals if they have more than one county with very low control, etc, etc. It really does add up.  

All of these changes lead to AI realms being more stable and better at recovering from bad wars or messy successions. Of course, there’s still a lot of the hallmark CK3 chaos that we all know and love - it’s just not all there is, now!  

Let's compare two areas, one from the Live version, and one from the upcoming update. They are 200 years from game start (in fact, these are the same saves used for comparison stats earlier in the DD).  


![comparison_1.png](https://forumcontent.paradoxplaza.com/public/857660/comparison_1.png "comparison_1.png")


[Picture - Comparison between an area in Live and the Update]  
Do note that these changes do not mean you’ll see the same realms in every game. It’s still as it’s always been, where you might have a powerful Burgundy in the south or a Wales controlling the British Isles; it’s just that, now, the emerging Burgundian and Welsh realms will be much stronger and able to thrive! Additionally, given the AI is now consolidating a larger, more centralized domain, partition splits are nicer and border gore is reduced.  


## Ikh Mongol Uls​

No matter what changes we’ve made to the Mongols in the past, they always fall on one single point: when they grow large enough, it takes them too long to march their troops to their target, and thus lose too many troops to attrition and too much warscore to time.  

We’ve taught the AI to raise their troops closer to the target of their wars. They will seek to raise in a safe county within their realm that is close, but not bordering, to the wargoal. While this is the most impactful for the Mongols, all Duke or above rulers will now do this. What this means for the Mongols: they will no longer march all the way from far eastern Mongolia after every conquest. This change alone magnifies their potential for conquest tenfold (at least). They now fulfill their purpose; they shake up the world and reshape the lands they conquer. More than ever, you must now seriously consider if you wish to submit to the Great Khan…  

In addition to the new raising behavior, we have improved the way the Mongols pick their targets (making them less likely to gallop into the mountains of Tibet or immediately crash against a massively strong Byzantine empire), and we’ve changed how successor khanates work. The Golden Horde, Ilkhanate, Chagatai, etc, were never long for this world after they spawned. There were many reasons for this: they didn’t get a proper domain, no de jure lands, no gold, etc. While they still dissolve with some regularity (as they should) they now sometimes persist, and even thrive, as we’ve improved their starting positions by assigning them some starting resources, domain, and De Jure land depending on what they’ve managed to conquer.  

While it isn’t overly common that the Mongols exceed their historical conquests, here’s an example of how far they can spread under somewhat-ideal circumstances (long-lived Khans).  


![mongol_1.png](https://forumcontent.paradoxplaza.com/public/857662/mongol_1.png "mongol_1.png")


[Image - Initial state of the world]  

![mongol_2.png](https://forumcontent.paradoxplaza.com/public/857663/mongol_2.png "mongol_2.png")


[Image - Some years in: note that Tibet was taken because Ü had land in mongolia]  

![mongol_3.png](https://forumcontent.paradoxplaza.com/public/857664/mongol_3.png "mongol_3.png")


[Image - The newly-shattered Persia gets absorbed]  

![mongol_4.png](https://forumcontent.paradoxplaza.com/public/857665/mongol_4.png "mongol_4.png")


[Image - Strategically avoiding a Byzantium that is almost their strength, the Mongols go towards eastern europe]  

![mongol_5.png](https://forumcontent.paradoxplaza.com/public/857666/mongol_5.png "mongol_5.png")


[Image - After taking all of eastern Europe, they turn to Arabia and the Fatimids]  

![mongol_6.png](https://forumcontent.paradoxplaza.com/public/857667/mongol_6.png "mongol_6.png")


[Image - Eventually, Hungary falls after an intense war]  

![mongol_7.png](https://forumcontent.paradoxplaza.com/public/857668/mongol_7.png "mongol_7.png")


[Image - The Khan dies and successor khanates spawn in. Who knows how long they’ll last?]  

That’s it for now. The full update notes with all the details will come soon, so stay tuned!

 

#### Attachments

- [![bishop_stats.png](https://forumcontent.paradoxplaza.com/thumbnail/public/857661/bishop_stats.png)](https://forum.paradoxplaza.com/forum/attachments/bishop_stats-png.870175/)
  
  bishop_stats.png
  7,1 KB

 · Views: 0

<!-- artifact:reactions:start -->
- 200 Like
- 158 Love
- 14 (unlabeled — rendered as base64 data URI)
- 8 (unlabeled — rendered as base64 data URI)
- 6 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [rageair](https://forum.paradoxplaza.com/forum/members/rageair.375731/)**
Role: CK3 Game Director
Badges: 43
Reaction score: 11,829

*[Full game-badge icon list of 10 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
