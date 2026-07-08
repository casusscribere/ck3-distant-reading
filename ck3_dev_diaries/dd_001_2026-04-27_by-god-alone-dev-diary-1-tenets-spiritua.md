---
source_url: "https://forum.paradoxplaza.com/forum/threads/.1919114/"
forum_thread_id: 1919114
forum_canonical_slug: null
wiki_index_source: "https://ck3.paradoxwikis.com/Developer_diaries"
wiki_number: 1
title: "\"By God Alone\" Dev Diary #1 - Tenets & Spiritual Fulfillment"
dd_date: 2026-04-27
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
body_word_count: 3808
inline_image_count: 17
extraction_command: 'python3 extract_diary.py <fetch_file> --forum-id 1919114'
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
    location: raw_lines_315_to_320
    action: preserved_and_flagged
    counts:
      Like: 122
      Love: 67
      (unlabeled — rendered as base64 data URI): 2
      Haha: 2
    note: Reactions block parsed; 3 of 6 reaction types have text labels in WebFetch output (others render as base64 data URIs and lose labels).
  - type: op_signature
    location: raw_lines_328_to_385
    action: preserved_and_flagged_collapsed
    note: OP author profile card preserved as a compact summary; full badge icon list omitted for readability.
  - type: replies
    location: raw_line_386_and_after
    action: discarded_from_output
    note: All reply posts after the OP are out of scope and discarded.
notes_for_analyst: |
  Deterministic extraction via extract_diary.py. Title heading,
  thread metadata, body span, reactions block, and reply boundary
  detected by regex without manual inspection. See detected_artifacts
  list for raw-fetch line ranges of every preserved-and-flagged or
  discarded element.
---

# "By God Alone" Dev Diary #1 - Tenets & Spiritual Fulfillment

<!-- artifact:thread_metadata:start -->
- Thread starter [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)
- Start date [Apr 27, 2026](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-1-tenets-spiritual-fulfillment.1919114/)
<!-- artifact:thread_metadata:end -->

[Jump to latest](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-1-tenets-spiritual-fulfillment.1919114/latest) [Follow](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-1-tenets-spiritual-fulfillment.1919114/watch) [Reply](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-1-tenets-spiritual-fulfillment.1919114/add-reply)

Menu

Install the app

Install

- [](https://forum.paradoxplaza.com/forum/account/dismiss-notice?notice_id=377 "Dismiss notice") We have updated our [Community Code of Conduct](https://forum.paradoxplaza.com/forum/help/terms/). Please read through the new rules for the forum that are an integral part of Paradox Interactive’s User Agreement.

JavaScript is disabled. For a better experience, please enable JavaScript in your browser before proceeding.

You are using an out of date browser. It may not display this or other websites correctly.  
You should upgrade or use an [alternative browser](https://www.google.com/chrome/).

[Crusader Kings III 22945](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii.1059/) [Open Beta 222](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-open-beta.1202/) [Console 447](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-console.1135/) [Suggestions 7208](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-suggestions.1082/) [Bug Report 7170](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-bug-report.1143/) [Tech Support 2918](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-tech-support.1078/) [User Mods 2091](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-user-mods.1080/) [Multiplayer 176](https://forum.paradoxplaza.com/forum/forums/crusader-kings-iii-multiplayer.1079/) [AARs (After Action Reports)](https://forum.paradoxplaza.com/forum/link-forums/aars-after-action-reports.1111/) [MP Open Beta Feedback 27](https://forum.paradoxplaza.com/forum/forums/mp-open-beta-feedback.1094/)

[Previous dev diary](https://forum.paradoxplaza.com/forum/developer-diary/silk-silver-dev-diary-1-design-vision.1917178/ "&quot;Silk &amp; Silver&quot; Dev Diary #1 - Design Vision") [Next dev diary](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-2-ecclesiastical-power-rites.1920599/ "&quot;By God Alone&quot; Dev Diary #2 - Ecclesiastical Power &amp; Rites")

[Show only dev responses](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-1-tenets-spiritual-fulfillment.1919114/?prdxDevPosts=1)

![](https://forumcontent.paradoxplaza.com/data/thfeature/feature_banners/4/4462.jpg?1777289821)

# "By God Alone" Dev Diary #1 - Tenets & Spiritual Fulfillment

- Thread starter [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)
- Start date [Apr 27, 2026](https://forum.paradoxplaza.com/forum/developer-diary/by-god-alone-dev-diary-1-tenets-spiritual-fulfillment.1919114/)

Happy Tuesday, and welcome to our first *official* dev diary for our upcoming expansion By God Alone! In our [sneak preview](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-195-salve-in-domino.1914929/), we gave you the grand tour from the mountaintop. This week, we're going to zoom in on one particular slice of the new expansion features, where your character starts having an actual *relationship* with their faith. This is the foundation upon which many of the features we'll discuss in later dev diaries are built.  
We will look over our revisions to **Tenets**, **Spiritual Fulfillment**, **Personal Tenets**, and the new **Study Faith** scheme. Along the way, I'll walk you through the reworked Faith UI, which is where most of this comes together. As always, everything here is under active development and subject to change, and we'll be reading your feedback carefully. Let's dig in!  



![01 the vision.png](https://forumcontent.paradoxplaza.com/public/1488089/01 the vision.png "01 the vision.png")



The one-liner in our last diary was that the right to rule flows from God, which is true for the expansion overall. This week's catchphrase is more personal: **your faith is something you *practice*, not something you *have*.**  

In live CK3, religion is essentially a label with a handful of modifiers and restrictions hanging off it. You inherit your religious doctrines and core tenets at birth, and unless you convert or found a new Faith outright, your spiritual life is a static block of stats that never changes. What we want to replace that with is something that behaves a lot more like the real thing - a daily practice with personal convictions, moral tension, and plenty of room to drift over the course of a lifetime.  

Imagine a newly-minted archbishop who adopts Scholasticism and starts nudging the Tenets of his Rite, year by year, until the theology of an entire region has quietly drifted toward something his grandfather would not have recognized. Or a Lustful, Greedy duke who nevertheless drags himself through decades of fasting and self-denial because he knows, on some level, that his predilections are going to earn him nothing but eternal anguish in the end. Or a count who quietly practices a forbidden teaching and lives in daily terror of his local Archbishop. These are the kinds of stories we want the religion system to naturally produce.  


![02 tenet revision.png](https://forumcontent.paradoxplaza.com/public/1488090/02 tenet revision.png "02 tenet revision.png")



To make any of this work, we have to start with **Tenets**, the building blocks of every faith's identity. We're doing a comprehensive pass on them, with over two dozen new ones coming with By God Alone, targeting primarily the various Christian traditions. We're talking about things like *Peace of God*, *Apostolic Succession*, *Transubstantiation*, *Hesychasm*, *Scholasticism*, *Simony*, and *Mortification of the Flesh*.  

![image_01.png](https://forumcontent.paradoxplaza.com/public/1488091/image_01.png "image_01.png")


*[Illustration of 26 new Tenet icons. Feel free to guess in the comments what they represent!]*​


Every Tenet now has two distinct effects: a **faith-wide effect** applied to followers of the Faith (actually Rite, but more on that next time) when the Tenet is being actively promoted (this is the old behavior, mostly preserved), and a **personal effect** applied only to characters who adopt the Tenet as a personal conviction.  

As a concrete example, picking *Peace of God* as a personal tenet lowers your knight limit (you're not supposed to be keeping a huge martial retinue if you're really serious about this) but gives you cheaper ally calls and sturdier alliances - the politics of the reluctant warrior. Adopting *Transubstantiation* unlocks extra social benefits from feasts. *Dulia* lets you select a patron saint of your own. *Ora et Labora* gives you the Gardener trait. Each personal tenet is a small vow with an impact both on how you play and your Spiritual Fulfillment.  

Tenets also now have a **status within a faith**: *Core*, *Permitted*, *Prohibited*, or just *Known*. If a Tenet is not known the faith is genuinely *unaware* that a Tenet exists, and therefore can neither teach it nor forbid it. This status also exists on characters, so you can "know" something (and even adopt it as a personal tenet!) even if your faith doesn't. Tenets become Known to the faith via characters and their actions; for example, by an Archbishop founding a new divergent Rite and actively preaching a tenet, or someone bringing up a foreign practice they learned about in an Ecumenical Council. Once a Tenet is Known, they can be promoted to Permitted, Prohibited, or Core through Ecumenical Councils or by the Head of Faith declaring them such (in Catholicism, via a Papal Bull).  

Adopting Permitted and Core Tenets as your character's core conviction is safe. Adopting one Known to you but not to your Faith is trickier, since it could be declared anathema at any time if the Church finds out. Prohibited tenets must be practiced in secret - and anyone who catches you at it walks away with a very juicy blackmail Hook.  

![image_02.png](https://forumcontent.paradoxplaza.com/public/1488092/image_02.png "image_02.png")


*[Screenshot: the tenet tooltip, showing the faith-wide effect on top and the "When selected as personal tenet" block below.]*​


While the new Tenets are limited to Christians, we are also going over old Tenets to ensure they all have personal effects and are appropriately balanced. Adopting personal tenets is not limited to Christians after all, and neither is…  


![03 spiritual fulfillment.png](https://forumcontent.paradoxplaza.com/public/1488093/03 spiritual fulfillment.png "03 spiritual fulfillment.png")



**Spiritual Fulfillment** is a new character metric, running from -100 to +100, that tracks how closely the life you actually live matches the life your faith asks you to lead, and how this impacts your spiritual well-being. It is entirely internal: other characters cannot intrinsically intuit how you're faring on your spiritual journey - unless you tell them of course.  

![image_03.png](https://forumcontent.paradoxplaza.com/public/1488094/image_03.png "image_03.png")


*[Screenshot: the Take Confession Decision is available to all Christians regardless of Spiritual Fulfillment level, but has different effects depending on how good you are with God.]*​


Here I want to take a second to correct something I wrote last time: *"Think of it as the spiritual counterpart to Stress, except instead of measuring how close you are to a mental breakdown, it measures how close you are to either sainthood or damnation."* That is **not** entirely accurate, so to be extra precise: it measures how close *you feel you are* to being blessed in the Lord versus being slated for eternal damnation - or, in another belief system, your karmic balance, or how in tune you are to the Great Spirit. Naturally, this inner spiritual turmoil rubs off on how you behave towards people around you as well to some degree, but it is not something others judge you for - any penance necessary is all yours to administer upon yourself. This in turn has an *effect on* Stress, as well as other conditions, described below.  

This is in contrast to Piety, which measures how much the rest of your faith respects you as a figure of religious standing. You could very well choose an event option that yields Piety for your external display while dropping your Spiritual Fulfillment because it doesn't correspond with what your Faith (or, more precisely, your chosen Rite) believes to be right living. More commonly, an option that adds Stress because it conflicts with your Traits, but also adds Spiritual Fulfillment because it's *the virtuous thing to do*.  

For Christian characters, Fulfillment steps through seven named tiers, each with its own unlocks. At the very bottom is **Doomed** (-95 and below), where stress gain is cranked up substantially but the gloves are also off: murder schemes do not generate stress, hostile schemes against clergy are similarly worry-free, and you can fabricate hooks on your own Court Chaplain. The worst place to be spiritually, but in some ways the most liberating place politically. Above that sits **Forsaken** (-65), which still gives you free rein to plot against your clergy, but eases off the stress-gain multiplier. **Troubled** (-30) retains only the Chaplain-hook permission - you're still sinning, but now you're noticing. **Penitent** (0) is the neutral midpoint, with nothing unlocked and nothing penalized; you're at peace with yourself, if not with God. **Absolved** (+30) starts charging you extra Fulfillment for hostile schemes against clergy and lets you run Befriend on your Chaplain. **Settled** (+65) boosts your stress *drain*, extends Befriend to your Head of Rite, and opens up the new **Act of Devotion** decision. And finally, at **In Grace** (+95), you get the full kit: further improved stress reduction, and access to the **Mentor in Spiritual Fulfillment** decision which lets you guide other characters through their own spiritual journeys.  

What we're hoping this produces is exactly the kind of dilemma we've been talking about. A Generous, Pious ruler who climbs to In Grace feels *great* and has tools other characters don't, but has also made it costlier to scheme against the Church. A Doomed or Forsaken ruler has more levers to pull and stronger nerves for pulling them, but suffer more for going against their nature. Low Fulfillment isn't a failure state - it's just a different playstyle, and depending on your character's personality it might even be the more coherent one.  

Non-Christian faiths use a simpler three-tier fallback that swings Stress gain one way or the other but doesn't unlock bespoke content.  

![image_04.png](https://forumcontent.paradoxplaza.com/public/1488095/image_04.png "image_04.png")


*[Screenshot: the Spiritual Fulfillment bar on the Personal Faith window, showing the current level icon and a tooltip listing the unlocked mechanics.]*​



![04 personal faith.png](https://forumcontent.paradoxplaza.com/public/1488096/04 personal faith.png "04 personal faith.png")



So how does Fulfillment actually move? Three ways: your **Personal Faith** (the specific set of Tenets you've chosen to champion), certain religious actions like going on Pilgrimages and taking Confessions, and the choices you make in events.  

Each personal adoption pushes your Fulfillment up or down depending on how well it aligns with your personality traits, and Tenets that reward a *Virtue* you actually have are weighted twice as heavily. A Generous character adopting *Philanthropia* gets a big positive swing. A Lustful character adopting *Mortification of the Flesh* is choosing the virtuous path in spite of their sinful nature, and the system is sympathetic to that - the Stress is real, but so is the Fulfillment. Event options that match the Virtues or Sins of a relevant Tenet of your Rite come with their own small Fulfillment swings, up or down, depending on whether you lived up to the vow in the moment. In addition to all the new interactions with the Church, this is what permits you to actually practice your faith throughout each character's lifetime.  

The cost of revoking one of these vows you've made depends on what you're overriding. Dropping a **Permitted** Tenet for another one comes with a cost, because your Church is fine with both and you're just making a legitimate choice. Dropping a **Core** or **Prohibited** Tenet costs Stress instead, because you're going against the grain of either the institution or your own conscience.  

Your personal convictions also have a quiet way of leaking out into the world. A Tenet you practice openly - what isn't Prohibited in your Faith - becomes available to close family automatically, and may also spread to members of your court and other relations you have. If they like what they see they may even adopt it themselves. AI characters are also more likely to start new Rites (again with these Rites - next time, I promise) incorporating convictions they hold dear. The personal and the institutional are never fully walled off from each other, which is the whole point.  


![05 study faith.png](https://forumcontent.paradoxplaza.com/public/1488097/05 study faith.png "05 study faith.png")



The other big way to change your personal faith is, of course, to learn someone else's. **Study Faith** is a new Learning-based scheme, targeted at another character whose Faith isn't yours. Each phase takes some amount of time, with success chance driven by your Learning skill, Piety, and the usual roster of traits and perks you'd expect (*Theologian*, *Erudite*, *Mystic*, *Scholar*, *Open-Minded*, plus the Intellect trio).  

While the scheme is running, a stream of events colors the experience. For example, a young heir picks up the material unreasonably fast; a court tutor spots what you're up to and offers to help; a priest of your own faith challenges you to a public disputation (you can duel him instead if you'd rather not argue); a rival sabotages your notes; the target turns out to be a closet non-believer, or worse, a practitioner of some ancient rite hiding in plain sight. Each of these nudges your progress one way or the other and, more importantly, gives the study phase its own narrative texture.  

On completion of a phase, Study Faith does one of three things depending on how you finish and what's available. You might **learn Tenets**, such that those practiced by the target's Rite (sigh) becomes **Known** to you personally. You might also **learn Doctrines**, typically a prerequisite for the more structural changes you might want to make later on. Or you might choose to **convert spontaneously**, an option offered at the end of a successful study. There is no up-front Piety cost to convert - instead how smooth the transition feels depends on how much of the target's faith you've already absorbed. The more of its Core and Permitted Tenets you know, and the more of its Doctrines you already practice, the gentler the landing in terms of Piety and Levels of Devotion lost in the process. It's easier to convert to a Faith that's similar-enough to your previous one, after all.  

Study Faith replaces the previous conversion path. You can still be subject to demands to convert by your liege, demand others convert, or convert in response to being Holy Warred, but if they choose to do so, they will go through the new system and suffer consequences for it depending on how well they can pick up the new teachings. You may even counter-offer with a demand to learn more about it first.  

![image_05.png](https://forumcontent.paradoxplaza.com/public/1488098/image_05.png "image_05.png")


*[Screenshot: mid-scheme, an event where you're caught in the act of reading another faith's religious scriptures, potentially making you suspect of heresy by fellow Christians.]*​



![06 visualized belief.png](https://forumcontent.paradoxplaza.com/public/1488099/06 visualized belief.png "06 visualized belief.png")



Hello! This is Ellie. It’s been a while. Last time we spoke, I want to recall updating you all on my recent sojourn into the Lost Realms. While I don’t have any further updates to share on the matter, I will still caution you all against entering into any bargains with any fae creatures, no matter how honeyed their words may be. This is especially true during the approaching time of the summer solstice, during which, as we all know, the gauntlet separating this world from the ones beyond grows weaker.  

For those of you who are unacquainted with me and my work, I ply my trade in the mysterious and often dangerous realm of User Experience. I’m a UX Designer on CK3, and I’ve been hard at work making sure that we’re delivering the ~experience~ that we all want to play. One thing we’re doing, as you might have guessed, is redesigning the Faith View. We’ll probably show more of this later, but for now I wanted to highlight **Personal Faith** specifically!  

Your Personal Faith consists of a couple of elements. First and foremost, we have the Spiritual Fulfillment bar! This tracks how, well... spiritually fulfilled you are. We just talked about it. Internally, we called this the sin-o-meter for a really long time. I think that name still has a certain charm to it. Anyway, there’s also some more stuff in here, like the personal tenets you subscribe to, as well as which Tenets and Doctrines you’ve learned about.  

![image_06.png](https://forumcontent.paradoxplaza.com/public/1488100/image_06.png "image_06.png")


*[Screenshot of a mockup of the Personal Faith window]*​


The above is a screenshot of a mockup of how we want it to look! Here’s what it actually looks like in-game right now.  

![image_07.png](https://forumcontent.paradoxplaza.com/public/1488101/image_07.png "image_07.png")


*[In-game screenshot depicting the Personal Faith window]*​


As you can see, we still have some ways to go, but all the bones are there! The little numbers indicate how much Spiritual Fulfillment you’d gain by adopting that specific Tenet as a Personal Tenet. Your Faith might also have opinions about which Tenets you’re allowed to practice, and which ones might be considered heretical...  

That’s it from me! I know you might be curious to see the redesigned Faith View, but it’s still cooking. We’re really excited about how it’s shaping up, and we hope you’ll like it. Anyway, see you later, gamers!  


![07 last rites.png](https://forumcontent.paradoxplaza.com/public/1488102/07 last rites.png "07 last rites.png")



Hail and well met pilgrims, this is [@TheFrankeleyn](https://forum.paradoxplaza.com/forum/members/1956642/). I know you all, but you’re yet to make my acquaintance. I am a designer on CK3 and would like to tell you about our work on Last Rites.  

Last Rites is a Decision you can take to put your soul in order while on death’s door. This was a high-stakes affair in our period, and many a monarch worked hard to ‘die well’.  

Just think, much of the stakes of Hamlet are in relation to when and how people die, have they *‘had their shriving time’* or were they *‘Cut off, even in the blossoms of their sin, Unhouseled, disappointed, unaneled, No reck’ning made, but sent to their account with all their imperfections on their head.’*  

This decision, and its ensuing event chain, will allow you to confess your sins, be anointed by a priest, take the eucharist, and then provide the opportunity to donate funds or lease lands to a Holy Order or the Church. This will aid in your being remembered well, standing your heir in good stead. Mechanically this translates to your heir getting delicious modifiers, based on the institution you supported, for the early years of their reign.  

The event chain will also reflect the likely cause of your imminent death, your believed proximity to salvation or damnation based on your level of spiritual fulfillment, and who sees fit to be at your bedside to send you across the threshold. Are you surrounded by loved ones and ministering angels, or has your life of sin conjured up visions of demons there to claim your soul for a bath in hellfire?  

![image_08.jpeg](https://forumcontent.paradoxplaza.com/public/1488103/image_08.jpeg "image_08.jpeg")


*[Screenshot: mid-event chain, where you reflect on your relative sense of salvation or damnation and what sins may have brought you there.]*​



![08 whats next.png](https://forumcontent.paradoxplaza.com/public/1488104/08 whats next.png "08 whats next.png")



Next week we'll dig into **Rites** proper (yes!) - how they spread along Ecclesiastical Title borders, how Divergence accumulates, and what it takes to turn a Rite into a full-blown heresy. If today's diary was about the view from inside one character's head, next week's is about the view from orbit.  

As always, we'd love to hear what you think. Until then!  

*Non nobis, Domine, non nobis, sed nomini tuo da gloriam.*

<!-- artifact:reactions:start -->
- 122 Like
- 67 Love
- 11 (unlabeled — rendered as base64 data URI)
- 3 (unlabeled — rendered as base64 data URI)
- 2 Haha
- 2 (unlabeled — rendered as base64 data URI)
<!-- artifact:reactions:end -->

<!-- artifact:op_signature:start -->
**Written by [lachek](https://forum.paradoxplaza.com/forum/members/lachek.669315/)**
Role: Design & UX Manager/Lead, Crusader Kings III
Badges: 37
Messages: 814
Reaction score: 49,611
<!-- artifact:op_signature:end -->
