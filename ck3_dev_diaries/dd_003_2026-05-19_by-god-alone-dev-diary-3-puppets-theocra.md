---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1923707/"
forum_thread_id: 1923707
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 3
title: "\"By God Alone\" Dev Diary #3 - Puppets & Theocratic Play"
dd_date: 2026-05-19
author_handle: lachek
expansion: By God Alone
patch: null
extraction_method: webfetch_xenforo_text_layer
extraction_date: 2026-06-09
fetched_at: 2026-06-09
text_layer_present: true
ocr_used: false
ocr_average_confidence: null
language: en
body_word_count: 2758
inline_image_count: 11
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1923707'
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
    location: raw_lines_~28_to_114
    action: discarded_from_output
  - type: thread_metadata
    location: raw_lines_116_to_117
    action: preserved_and_flagged
  - type: reactions
    location: raw_lines_286_to_291
    action: preserved_and_flagged
    counts:
      Like: 104
      Love: 47
      (unlabeled — rendered as base64 data URI): 3
      Haha: 1
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_299_to_409
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_410_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# "By God Alone" Dev Diary #3 - Puppets & Theocratic Play

<!-- artifact:thread_metadata:start -->
- Thread starter [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)
- Start date [May 19, 2026](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-3-puppets-theocratic-play.1923707/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-3-puppets-theocratic-play.1923707/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-3-puppets-theocratic-play.1923707/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-3-puppets-theocratic-play.1923707/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22945](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-2-trade-vision.1922255/ "&quot;Silk &amp; Silver&quot; Dev Diary #2 - Trade Vision") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-3-merchants-vision.1924995/ "&quot;Silk &amp; Silver&quot; Dev Diary #3 - Merchants Vision")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-3-puppets-theocratic-play.1923707/?prdxDevPosts=1)

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_banners/4/4512.jpg?1779184980)

# "By God Alone" Dev Diary #3 - Puppets & Theocratic Play

- Thread starter [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)
- Start date [May 19, 2026](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-3-puppets-theocratic-play.1923707/)

Happy Tuesday! Mikael here with another *By God Alone* update. Last time we walked through Ecclesiastical Titles and Rites and while we shone a light on clerical gameplay and faith mechanics, we did not really touch on how a secular character - who you as the player, most often control - can harness said clerical mechanics.  

So let's go there!  

The year is 1075. You are the King of West Francia, and one of your grouchiest dukes - the one you've stubbornly refused a council seat for decades - has become too big for his britches. He has virtually stopped pretending he isn't preparing a revolt, and you would like him stripped of his vassal oaths before it gets there. The Papacy, however, has made it clear that complaints from secular kings about which of their unruly dukes is or isn't in good standing with God are not, presently, one of Rome's priorities.  

Mercifully, you do have a Court Chaplain. Who happens to be the Archbishop! Who, by the strength of a Hook your spymaster fabricated last spring, owes you a favor large enough to impose an Excommunication order all on his own, which would in turn permit you to revoke his title without causing an upset with your other vassals. The duke, after all, falls under the Archbishop's spiritual jurisdiction as well. A brief letter to Rome (on your behalf), and your uppity duke has learned what can happen if he goes against his King's will.  

This week is about **Puppets** - the system by which you, the secular ruler, get clerical levers to move on your behalf - and **Playable Theocracies**, the answer to the question "what if I just played the clergyman myself?".  

Standard caveat: all of this is work in progress, nothing you see here is final, and we'd love your feedback.  


![divider_01.png](https://forumcontent.paradoxplaza.com/public/1500580/divider_01.png "divider_01.png")

A **Puppet** is a real character, who behaves in accordance with how NPCs typically act in Crusader Kings III. However, by virtue of your hold over them you can *also* make them act according to *your* ideas of what they should do. In *By God Alone*, we are introducing two puppet types which relate specifically to organized religions. The system itself is open both to future expansion and to modders, and is not fundamentally tied to religious matters as such.  

When puppets take action at their master's command, the game reads this action as originating from the puppet. Costs and consequences are levied on them, not on you. For the modders out there, this does involve some minimal setup per action (e.g. Character interaction, Decision, Great Project) to ensure the initiator is distinguished from the one actually executing it, but the system is designed to be as designer- and modder-friendly as possible.  

In *By God Alone*, your **Court Chaplain** is your persistent puppet candidate. To make them **Compliant** requires meeting some condition, the most obvious one being having a Hook on them, but a variety of other conditions can also be leveraged to ensure compliance: having a very high Level of Devotion yourself, having them as your friend (or… lover), if they sufficiently fear you, or if you are family. Having your dynasty deeply embroiled with the church machinery can be a powerful move.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1500581/image_01.png "image_01.png")


*[Screenshot of a very WIP Puppet panel showing your Court Chaplain's available actions]*​


Currently, you can work through your puppeted Court Chaplain to do the following:  


- **Found a Rite** - the secular ruler's only legal route into the Rite system you saw last time. Now you know who's holding the pen.
- **Plan and Construct a Grand Cathedral** as a Great Project, funded out of the Church Treasury rather than your purse.
- **Mass-convert neighboring pagans** through a Great Project.
- **Excommunicate a character in the same Archdiocese**, with the request lodged under his name rather than yours.
- **Request a new Ecclesiastical Title**, splitting their current region in two
- Request an **Elevation to the See** for your Puppet, i.e. make them an Archbishop or Patriarch.
- **Turn him into the Head of Faith** of a Faith that doesn't currently have one (such as 867+ Chalcedonian Christianity).

Virtually every new action we're making available to theocratic characters, we're also making available through the puppet system. We're not looking to duplicate actions you can normally do yourself, though - the actions you can take through your Puppet is typically limited to that which you do not have direct control over.  

The other Puppet type we're adding is the Pope. If you somehow manage to elevate your Puppet to this position, or declare your Puppet the true (anti)pope and depose the pretender, you will have the Pope himself under your thumb via the same system. More on this (and Antipopes) later!  

There is, of course, a more elegant solution to the problem of an uncooperative Court Chaplain (if his Superior won't accede to your demands of replacing him). Which is to be your own clergyman.  


![divider_02.png](https://forumcontent.paradoxplaza.com/public/1500582/divider_02.png "divider_02.png")

**Theocratic characters** - Prince-Bishops; landed Archbishops, Patriarchs, and Cardinals; and even the Pope himself - are now playable. Theocratic government has been in the codebase since launch, but the title-holders have always been NPCs whose succession went into a black box. With *By God Alone* you can play them, inherit through them in the limited sense theocrats inherit, or continue your dynasty's story through them rather than around them.  

There's been a lot of speculation over the years around how theocracies could be made playable, and even if they *should* be made playable, given they don't follow dynastic inheritance. Well, Crusader Kings III has evolved a lot over the years, with landless play, administrative realms, and Choose Your Destiny type features already transforming what the core play experience looks like. So it's time to rip off the band-aid and give you a new type of player succession, along organizational rather than dynastic lines.  

Simply, when playing a theocracy, if you die without a member of your dynasty set to inherit your title, you will instead resume playing the next clergyman in line for your title.  

However, while clerical dynasty building was certainly something both the Christian Church and secular rulers tried to crack down on throughout history, it was not unheard of. With the faith's evolution over centuries of tumult modelled in *By God Alone*, particularly in the early start date both getting your cake and eating it too is far from impossible, as I'll outline below.  

But before we go too far, let's talk about what you can actually *do* as a theocratic ruler. Within Christianity this is done within the confines of a new government type, **Ecclesiastical** **Government** - similar to but not identical to Theocratic Government. Succession is appointment-based: when a theocrat dies, the next holder is selected from local clergy, with weights based on how good of a Christian they are (or appear to be) and how well they have served the faith.  

A theocratic ruler:  


- Has a Treasury (which belongs to the Church, and works similarly to Treasury in admin realms), as distinct from their Gold
- Has a personal clerical domicile, they can build up to better see to the needs of their flock
- Appoints subordinates (bishops) within their own ecclesiastical hierarchy
- Often serves as the Court Chaplain of local secular rulers
- Cannot start wars against Christian rulers, but *can* gain land from Christian rulers by exploiting their inheritance laws
- Maintains their own Church Authority law-group, the theocratic parallel to a feudal lord's Crown Authority. Raising it costs Piety but unlocks abilities, most notably the legal precondition for establishing a theocratic dynasty. Letting it slip exposes you to a new Humiliation CB that Christian neighbors with higher authority or Piety can declare (at considerable consequences, of course)
- They remain a political actor. They can still rise, fall, and be schemed against

What you *don't* get is automatic direct dynastic continuity through children, the way a feudal duke does. Most theocrats are ostensibly sworn to celibacy, and the canonical succession model is appointment to a related-or-promising clergy character rather than to your bloodline. We've leaned into this rather than around it: the dynasty-building loop for a theocrat is about ensuring the *next* holder of your See is also of your house, by mentoring and elevating eligible nephews and protégés in time for them to be on the appointment shortlist when you die.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1500583/image_02.png "image_02.png")


*[Screenshot of the Designate Theocratic Heir interaction, which becomes available if you have a dynasty (like Prince-Bishop Heinrish of Trent here) or once you've established a theocratic dynasty by raising your Church Authority]*  


![divider_03.png](https://forumcontent.paradoxplaza.com/public/1500584/divider_03.png "divider_03.png")

The extreme case is the Holy Father himself.  

As Pope, you sit on top of the central Church Treasury, funded by tithes from every Catholic church in Christendom, and quite possibly the largest single pot of gold in the game - at least when the Church is healthy. You hold the levers a secular player can only *influence* through their Puppets:  


- You appoint (and pay) **Cardinals**, and give them **Orders**
- You call **Ecumenical Councils** and decide what they are about
- You **Excommunicate** rulers who displease you, with all the secondary consequences that cascade through the political map
- You approve **Holy Sites** for Catholicism
- You issue **Papal Bulls**, powerful edicts underwritten by Rome. These include the ability to launch a targeted crusade, declaring a Rite heretical, or declaring a certain Tenet permitted or forbidden.

![image_03.png](https://forumcontent.paradoxplaza.com/public/1500585/image_03.png "image_03.png")


*(Screenshot of the orders that can be given to Cardinals - by the Pope, or by a secular ruler who's Puppeted them)*​


Of course, every secular Christian ruler is, at some level, trying to influence you. Christian Kings and Emperors will line up at the Apostolic Palace to request some favor or another. It's up to you to decide who to hear, and whose wishes align with the will of God. Note that we will no longer direct every request for divine grace through the Pope - many concerns can be handled by the Church's local representatives (e.g. Archbishops), to avoid spamming a player whenever some local count thinks their half-brother is an affront to God  

Speaking of the Apostolic Palace, this will be a new Throne Room which you will see (and have to maintain) both when playing as the Pope, and when visiting Rome to ask the Papacy to grace you in various ways. Visuals will be coming later, I promise!  


![divider_04.png](https://forumcontent.paradoxplaza.com/public/1500586/divider_04.png "divider_04.png")

With the ability to play as the Pope, it also makes the question of who *becomes* the next Pope that much more relevant.  

While there were certainly times in the history of Catholicism when it took quite a long time for a Pope to get elected (the record held by the election of Pope Gregory X in 1271, after over 1000 days of divisive debates resulting in the locals locking the cardinals up and restricting their access to food and shelter until they came to an agreement, thus establishing the conclave tradition we know today), CK3 isn't really paced for tactical plotting over a short period of days or weeks. As such, the College is always considered to be deliberating over who will take the seat next, and cardinals can be influenced at any time.  

There are always three candidates for the seat, selected based on the following criteria:  


- The obvious choice (Cardinal most entrenched in the Church power structure)
- The pious choice (Cardinal with the highest level of Devotion)
- The powerful choice (Rite Head with the largest flock)

Of these selected candidates, cardinals will select their preferred option based on typical parameters like opinion, but also how their teachings align with the cardinal's traits. Every papal candidate has the opportunity to switch one Core Tenet as they rise to the seat, and if this change sits well with a particular cardinal, they're more likely to align with that candidate. Spiritual Fulfillment thereby becomes the driving force of the evolution of the Christian faith.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1500587/image_04.png "image_04.png")


*[WIP screenshot of the College of Cardinals electoral process. The preferred tenets here are a bit samey, the intent is that post-balancing these will offer a more enticing buffet of possibilities.]*​


Oh, and *should* you manage to get elected, you may of course select what Christendom will henceforth know you as.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1500588/image_05.png "image_05.png")


*[Screenshot of an event where you get to select your own pontifical name after having been elected Pope]*  


![divider_05.png](https://forumcontent.paradoxplaza.com/public/1500589/divider_05.png "divider_05.png")

The Puppet system is faith-agnostic at the framework level. The same compliance check would carry over to any organized religion with a realm priest. However, a lot of the new actions we're making for *By God Alone* are specifically geared towards Christianity - manipulating the Archdiocese titles, asking for a Cardinalate, building Cathedrals. As such, the applicability of non-Christian realm priest puppets will be a bit lower.  

Playable Theocracies are the more broadly applicable half. The pre-existing Theocracy government type covers clergy-as-ruler arrangements outside Christianity. What does not generalize is the centralized Christian institutional spine: the Curia, the College of Cardinals, the Papal Bull, the Ecclesiastical Title hierarchy. Those remain Christian-only because that's primarily what the expansion is modelling.  

See you next time!

<!-- artifact:reactions:start -->
- 104 Like
- 47 Love
- 8 (unlabeled — rendered as base64 data URI)
- 4 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 1 Haha
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)**
Role: Design & UX Manager/Lead, Crusader Kings III
Badges: 37
Messages: 814
Reaction score: 49,611

*[Full game-badge icon list of 50 titles omitted for readability; preserved in raw fetch.]*
<!-- artifact:op_signature:end -->
