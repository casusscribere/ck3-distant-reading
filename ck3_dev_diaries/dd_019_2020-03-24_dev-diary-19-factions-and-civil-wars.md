---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1363951/"
forum_thread_id: 1363951
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 19
title: "CK3 Dev Diary #19: Factions and Civil Wars"
dd_date: 2020-03-24
author_handle: Baron von Shoes
expansion: Base game
patch: Crusader Kings III
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 1675
inline_image_count: 7
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1363951'
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
    location: raw_lines_~28_to_142
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_144_to_146
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_252_to_255
    action: preserved_and_flagged
    counts:
      Like: 11
      (unlabeled — rendered as base64 data URI): 1
      Haha: 4
    note: Reactions block parsed; 2 of 4 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_263_to_332
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_333_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# CK3 Dev Diary #19: Factions and Civil Wars

<!-- artifact:thread_metadata:start -->
- Thread starter [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)
- Start date [Mar 24, 2020](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-19-factions-and-civil-wars.1363951/)
<!-- artifact:thread_metadata:end -->

Hello kings and queens, dukes and duchesses! I am back with another Dev Diary, and today we’re going to be talking about Factions and Civil Wars in Crusader Kings III!  

Much like in CK2, vassals who are unhappy with the current state of affairs in the realm will create a Faction that other vassals can then join. Factions that grow large enough will eventually deliver an ultimatum to their liege, demanding certain concessions in exchange for continued peace.  

**Anatomy of a Faction**  


![DD_WM_ExampleFaction.png](https://forumcontent.paradoxplaza.com/public/545386/DD_WM_ExampleFaction.png "DD_WM_ExampleFaction.png")


[A screenshot showing a Claimant Faction with Faction Members, Discontent, and Military Power displayed]  

All Factions have a Military Power rating, which is a ratio between the combined military strength of all members and the military strength of their liege. Factions also have a Discontent score, which gauges how close the Faction is to sending their ultimatum.  

Factions will begin accruing Discontent once their Military Power goes over a certain threshold, typically 80%. Stronger Factions acquire Discontent rapidly in an attempt to seize the moment, while weaker Factions hem and haw a little in the hopes that more supporters will join their cause. Either way, once Discontent reaches 100% the Faction will soon deliver their ultimatum; at that point, their liege must either accept their demands or fight all joined faction members in a civil war.  

**Civil Wars**  


![DD_WM_CivilWarBorders.png](https://forumcontent.paradoxplaza.com/public/545387/DD_WM_CivilWarBorders.png "DD_WM_CivilWarBorders.png")


[A screenshot of the map showing several Faction Members at war with their liege, who is the player]  

Unlike in CK2, when a civil war is declared faction members do not form a new temporary realm. While they nominally remain vassals of their liege, they will immediately stop providing taxes and levies to them, and their liege will lose access to certain powers (such as imprisonment).  

During a civil war the faction members turn hostile to both their liege and all non-faction vassals, though they will focus on fighting their liege. The exact war goal varies depending on the Faction type, but both sides earn war score by defeating hostile armies and sieging down hostile provinces.  

Once one side emerges triumphant, they will enforce their demands. A victorious Faction will enforce their ultimatum with some additional concessions thrown in, while a victorious liege will imprison all faction members and gain title revocation reasons against them. If a white peace is agreed to, things largely go back to the way they were, though the liege gains an imprisonment reason against all the rebels. Actually imprisoning the rebels is another matter entirely, as a failed imprisonment attempt can trigger another rebellion.  

**Types of Factions**  
There are currently 5 distinct types of Factions, each of which has its own goals.  

- The Independence Faction, seeking to gain independence from their liege.
- Claimant Factions, seeking to replace their liege with a new one.
- The Liberty Faction, seeking to reduce Crown Authority in the realm.
- Populist Factions, seeking to form a new realm of their religion and culture.
- The Peasant Faction, seeking to pay fewer taxes to their liege.

Vassals only join The Independence Faction if they feel like they do not belong in their liege’s realm. This can be due to a variety of reasons, but it generally boils down to a combination of three major factors: not being a de jure vassal of their liege, not sharing their liege’s culture [group], and their religious hostility towards their liege (more on that in a future Dev Diary!). As a result, Independence Factions tend to be ‘clumpy’, forming distinct regional blocs within a realm.  

![DD_WM_IndependenceWarTerms.png](https://forumcontent.paradoxplaza.com/public/545391/DD_WM_IndependenceWarTerms.png "DD_WM_IndependenceWarTerms.png")


[A screenshot of an ongoing Independence Faction War against the HRE, showing the clustering of rebels within Italy]  

Claimant Factions, on the other hand, are all about opinion. Vassals who personally dislike their liege while still feeling like they belong to their liege’s realm will favor this type of Faction. Of course, Claimant Factions are also an area where opportunistic vassals can push to acquire titles for themselves or their relatives!  

The Liberty Faction is the place for vassals who are *almost* happy with the current state of affairs. They want to lower either the realm’s crown authority laws or their obligations to their liege, and are typically the easiest Faction to manage.  

Populist and Peasant Factions are special in that they are not created by unhappy vassals. Instead, they are created by unhappy *counties*.  

![DD_WM_CountyFactions.png](https://forumcontent.paradoxplaza.com/public/545394/DD_WM_CountyFactions.png "DD_WM_CountyFactions.png")


[A screenshot of the Faction Tab showing an active Kurdish Apostolic Populist Faction and a Peasant Rabble Faction]  

Much like vassals, counties have an opinion of their holder which is influenced by culture, religion, events, and war. When the opinion of a county drops too low, they will join one of these two factions. Like the other factions, if these factions gain enough Discontent, they will send an ultimatum, and will revolt if the ultimatum is refused. This completely replaces the random province revolt chance that existed in CK2 — gone are the days of “Duke McPeasantFace has declared the 19th Orthodox Uprising on you.”  

Populist Factions are the more dangerous type of county faction and form when counties wish to be governed by a ruler of their own culture and/or religion. While Populist Factions are created by and primarily consist of counties, sympathetic vassals in your realm may also pledge loyalty to their cause. A successful Populist revolt will cause all member counties and vassals to break away and form a new realm!  

While an Independence Faction causes all members split off into their own separate realms, a Populist Faction will create a single realm with all members united under one ruler. That ruler will always share the Faction’s culture and religion, and as a hero of the liberation war they will almost always be a competent commander. In addition, a successful Populist Faction will automatically usurp or create an appropriate title for their leader to hold, which can even generate new Kingdom-tier titles in certain circumstances!  

![DD_WM_SuccessfulPopularRevolt.png](https://forumcontent.paradoxplaza.com/public/545395/DD_WM_SuccessfulPopularRevolt.png "DD_WM_SuccessfulPopularRevolt.png")


[A screenshot of the Kingdom of Jüterbog, split off of the HRE by a successful Polabian Popular Revolt]  

All of this taken together means that any realm formed by Popular Revolt will end up being a formidable foe that likely has several De Jure claims on its neighbors. This can substantially alter the balance of power in your region — even if you weren't the initial faction target!  

On the other hand, Peasant Rabble are the simplest and least dangerous type of Faction. Unlike all other Factions, there is no minimum Military Power requirement for the Peasant Rabble to revolt, and its Discontent will always tick upwards at a constant rate. When the Rabble inevitably revolt, they will almost certainly be weaker than the liege they are targeting — but don’t let that lull you into a false sense of security! Every time the Rabble’s forces occupy a county, all of that county’s levies will immediately join them. What started as a minor uprising can quickly balloon out of control if left unchecked! Luckily their only demands are to pay reduced taxes and provide fewer levies to their liege, which is an annoying if manageable setback.  

**Faction Management**  

So as a ruler, how do you manage all of these Factions? Well, there are several ways!  

For starters, any alliances you have made with your vassals will prevent them from joining a Faction against you. This makes arranged marriages within your realm valuable even if you don’t benefit as much militarily as you would from a foreign marriage.  

Adding to this, any vassals you have a hook on will be unable to join a Faction against you, whether that hook is due to them owing you a favor or due to blackmail.  

You can also attempt to intimidate vassals away from their Faction, as a high Dread will lower their willingness to be in one. If the threat of imprisonment and torture doesn’t work, actual imprisonment will — vassals in your dungeons can not be part of any Faction. Just be careful, as an unjust imprisonment attempt may provoke a powerful Faction into revolting early, regardless of their Discontent!  

![DD_WM_FactionRetaliation.png](https://forumcontent.paradoxplaza.com/public/545398/DD_WM_FactionRetaliation.png "DD_WM_FactionRetaliation.png")


[A screenshot warning the player that imprisoning this vassal may trigger a Faction Revolt]  

Finally, if all else fails you can actually address the grievances your vassals have with you. Vassals who are happy enough will never join any kind of faction, which means improving their opinion of you and fixing structural issues in your realm will ensure that nobody challenges your rule!  

That is all for this week, but I have an extra special treat in store you next time when we finally begin diving into how religion works in Crusader Kings III!  

**Blooper Reel: The Extremely Popular Revolt**  
Very early on in CK3's development, I started looking into ways to make Popular Revolts more challenging. No matter how large a revolt got, their forces would always be spread out across all of their member counties, making it trivial to pick off their armies one at a time.  

To help remedy this, instead of letting each county spawn its own army I made it so each duchy would spawn a single army based on the combined military power of all faction counties inside of it. However, I made a mistake — instead of adding up the military power of all counties in a duchy, I accidentally added up the military power of all counties in the world*... per duchy.*  

![DD_WM_Blooper_RevoltingPeasantsCut.png](https://forumcontent.paradoxplaza.com/public/545400/DD_WM_Blooper_RevoltingPeasantsCut.png "DD_WM_Blooper_RevoltingPeasantsCut.png")



It turns out that no matter how many knights you have or how good of a commander you are, 8.8 million angry peasants will overwhelm you in battle every time.

<!-- artifact:reactions:start -->
- 11 Like
- 7 (unlabeled — rendered as base64 data URI)
- 4 Haha
- 1 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [Baron von Shoes](https://forum.paradoxplaza.com/forum/members/baron-von-shoes.1426511/)**
Role: Content Designer
Badges: 11
Messages: 65
Reaction score: 2,138

*[Full game-badge icon list of 11 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
